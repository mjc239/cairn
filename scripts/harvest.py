#!/usr/bin/env python3
"""Harvest Lean blueprint projects: for each project in scripts/harvest_projects.toml, clone it, parse its
blueprint, build it (Mathlib from cache), extract declaration-level dependencies with lean/extract_deps.lean,
run the Phase 1 comparison, and record a triage row. Disk use is kept bounded: after each project only the
blueprint sources and Lean pins are kept (data/raw/harvest/<name>/), and the build, the Mathlib cache and the
Lean toolchain are deleted.

    uv run python scripts/harvest.py                 # all projects not yet harvested, commit + push each
    uv run python scripts/harvest.py --only pnt clt  # just these (re-harvests them)
    uv run python scripts/harvest.py --no-commit     # leave results uncommitted
    uv run python scripts/harvest.py --report        # only rebuild results/harvest/triage.md

Outputs per project, in results/harvest/<name>/: triage.json, blueprint.json (parsed nodes and \\uses edges),
decls.jsonl.gz (the dependency dump) and phase1.{md,json} when the build and extraction succeed.
"""

from __future__ import annotations

import argparse
import gzip
import json
import os
import re
import shutil
import subprocess
import sys
import time
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "scripts" / "harvest_projects.toml"
RESULTS = ROOT / "results" / "harvest"
WORK = ROOT / "data" / "raw" / "harvest"
ELAN = Path.home() / ".elan"
ENV = {**os.environ, "PATH": f"{ELAN / 'bin'}:{os.environ['PATH']}"}
BUILD_TIMEOUT = 45 * 60
EXTRACT_TIMEOUT = 60 * 60
SKIP_LIB = re.compile(r"(?i)^(test|tests|docs?|blueprint|scripts?|archive|counterexamples|bench.*)$")


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def run(cmd, cwd=None, timeout=None, log_to: Path | None = None) -> tuple[int, str]:
    """Run ``cmd``; return (exit code, last 40 lines of output). Exit code 124 means timeout."""
    try:
        p = subprocess.run(cmd, cwd=cwd, env=ENV, timeout=timeout, capture_output=True, text=True)
        out, code = p.stdout + p.stderr, p.returncode
    except subprocess.TimeoutExpired as e:
        out = (e.stdout or b"").decode(errors="replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        code = 124
    if log_to:
        with log_to.open("a") as f:
            f.write(f"\n$ {' '.join(map(str, cmd))}\n{out}")
    return code, "\n".join(out.strip().splitlines()[-40:])


def free_gb() -> float:
    return shutil.disk_usage(ROOT).free / 1e9


# ---------------------------------------------------------------- Lean project structure

def lean_libs(repo: Path) -> list[str]:
    """Root modules of the project's lean_libs whose root file exists (test/docs libs skipped)."""
    names: list[tuple[str, list[str]]] = []
    toml, lean = repo / "lakefile.toml", repo / "lakefile.lean"
    if toml.exists():
        for lib in tomllib.loads(toml.read_text()).get("lean_lib", []):
            names.append((lib["name"], list(lib.get("roots", [lib["name"]]))))
    elif lean.exists():
        text = lean.read_text()
        block = r"lean_lib\s+(«[^»]+»|[\w.]+)(.*?)(?=\n(?:lean_lib|lean_exe|require|@\[|package|target|\Z))"
        for m in re.finditer(block, text + "\n", re.S):
            name = m.group(1).strip("«»")
            roots = re.search(r"roots\s*:=\s*#\[([^\]]*)\]", m.group(2))
            rs = [r.strip().lstrip("`").strip("«»") for r in roots.group(1).split(",")] if roots else [name]
            names.append((name, [r for r in rs if r]))
    out = []
    for name, roots in names:
        if SKIP_LIB.match(name):
            continue
        out += [r for r in roots if (repo / (r.replace(".", "/") + ".lean")).exists()]
    return list(dict.fromkeys(out))


def uses_mathlib(repo: Path) -> bool:
    manifest = repo / "lake-manifest.json"
    return manifest.exists() and '"name": "mathlib"' in manifest.read_text()


def mathlib_rev(repo: Path) -> str:
    try:
        pkgs = json.loads((repo / "lake-manifest.json").read_text())["packages"]
        return next(p["rev"][:12] for p in pkgs if p["name"] == "mathlib")
    except Exception:
        return ""


# ---------------------------------------------------------------- blueprint

ENTRIES = ("content.tex", "chapter/main.tex", "blueprint.tex", "web.tex")


def find_blueprint(repo: Path) -> tuple[Path, str, bool] | None:
    """(blueprint source dir, entry file, generated?). Generated blueprints (LeanArchitect) \\input TeX that
    ``lake build :blueprint`` writes under .lake/build/blueprint."""
    dirs = [repo / "blueprint" / "src"] + [p.parent for p in sorted(repo.rglob("content.tex"))
                                           if ".lake" not in p.parts]
    for src in dirs:
        for entry in ENTRIES:
            f = src / entry
            if f.exists() and (entry != "web.tex" or "\\input" in f.read_text(errors="replace")):
                return src, entry, ".lake/build/blueprint" in f.read_text(errors="replace")
    return None


def last_commit_with_blueprint(repo: Path) -> str | None:
    """Parent of the commit that deleted the blueprint, for projects that dropped it after finishing."""
    for path in ("blueprint/src/content.tex", "blueprint/src/chapter/main.tex"):
        h = subprocess.run(["git", "log", "-1", "--format=%H", "--diff-filter=D", "--", path], cwd=repo,
                           capture_output=True, text=True).stdout.strip()
        if h:
            return h + "^"
    return None


def choose_group_by(src: Path, entry: str) -> str:
    from cairn.blueprint import parse_blueprint

    for g in ("file", "chapter"):
        chapters = {n.chapter for n in parse_blueprint(src, entry, g).nodes}
        if len(chapters) >= 3:
            return g
    return "section"


# ---------------------------------------------------------------- one project

def harvest(proj: dict, commit_results: bool) -> dict:
    name, repo_name = proj["name"], proj["repo"]
    out, work = RESULTS / name, WORK / name
    out.mkdir(parents=True, exist_ok=True)
    clone = WORK / f"{name}.clone"
    shutil.rmtree(clone, ignore_errors=True)
    shutil.rmtree(work, ignore_errors=True)
    work.mkdir(parents=True)
    logf = work / "harvest.log"
    row: dict = {"name": name, "repo": repo_name, "status": "started", "stage": "clone"}
    t0 = time.time()
    try:
        log(f"{name}: clone {repo_name} (free {free_gb():.0f} GB)")
        code, tail = run(["git", "clone", "--quiet", "--filter=blob:none", f"https://github.com/{repo_name}.git",
                          str(clone)], timeout=1800, log_to=logf)
        if code:
            return fail(row, "clone", tail)
        if proj.get("commit"):
            run(["git", "fetch", "--quiet", "origin", proj["commit"]], cwd=clone, log_to=logf)
            run(["git", "checkout", "--quiet", proj["commit"]], cwd=clone, log_to=logf)
        row["commit"] = subprocess.run(["git", "rev-parse", "HEAD"], cwd=clone, capture_output=True,
                                       text=True).stdout.strip()
        row["commit_date"] = subprocess.run(["git", "log", "-1", "--format=%cs"], cwd=clone, capture_output=True,
                                            text=True).stdout.strip()
        row["toolchain"] = (clone / "lean-toolchain").read_text().strip() if (clone / "lean-toolchain").exists() else ""
        row["mathlib"] = mathlib_rev(clone)

        # Blueprint (a generated one is parsed after the build)
        row["stage"] = "blueprint"
        found = find_blueprint(clone)
        if found is None and not proj.get("commit") and (old := last_commit_with_blueprint(clone)):
            run(["git", "checkout", "--quiet", old], cwd=clone, log_to=logf)
            row["note"] = "blueprint deleted at HEAD; harvested the last commit that has it"
            row["commit"] = subprocess.run(["git", "rev-parse", "HEAD"], cwd=clone, capture_output=True,
                                           text=True).stdout.strip()
            row["commit_date"] = subprocess.run(["git", "log", "-1", "--format=%cs"], cwd=clone,
                                                capture_output=True, text=True).stdout.strip()
            for f in ("lean-toolchain",):
                row["toolchain"] = (clone / f).read_text().strip() if (clone / f).exists() else ""
            row["mathlib"] = mathlib_rev(clone)
            found = find_blueprint(clone)
        if found is None:
            return fail(row, "blueprint", "no blueprint entry file found")
        src, entry, generated = found
        entry = proj.get("entry", entry)
        row.update(blueprint_dir=str(src.relative_to(clone)), entry=entry, generated_blueprint=generated)
        for f in ("lean-toolchain", "lake-manifest.json", "lakefile.lean", "lakefile.toml"):
            if (clone / f).exists():
                shutil.copy2(clone / f, work / f)

        def parse_and_keep() -> None:
            from cairn.blueprint import parse_blueprint

            group_by = proj.get("group_by") or choose_group_by(src, entry)
            bp = parse_blueprint(src, entry, group_by)
            row.update(group_by=group_by, nodes=len(bp.nodes), uses_edges=len(bp.edges()),
                       chapters=len({n.chapter for n in bp.nodes}),
                       lean_nodes=sum(1 for n in bp.nodes if n.lean_decls),
                       leanok_nodes=sum(1 for n in bp.nodes if n.leanok))
            run(["uv", "run", "cairn", "parse", str(src), "--entry", entry, "--group-by", group_by,
                 "-o", str(out / "blueprint.json")], cwd=ROOT, log_to=logf)
            keep = work / row["blueprint_dir"]
            shutil.rmtree(keep, ignore_errors=True)
            shutil.copytree(src, keep)
            if generated:  # same relative layout, so the entry's \\input still resolves
                shutil.copytree(clone / ".lake" / "build" / "blueprint", work / ".lake" / "build" / "blueprint",
                                dirs_exist_ok=True)

        if not generated:
            parse_and_keep()

        # Build
        libs = proj.get("libs") or lean_libs(clone)
        row["libs"] = libs
        if not libs:
            return fail(row, "libs", "no lean_lib with an existing root file")
        row["stage"] = "build"
        if uses_mathlib(clone):
            log(f"{name}: toolchain {row['toolchain']}, mathlib cache")
            code, tail = run(["lake", "exe", "cache", "get"], cwd=clone, timeout=3600, log_to=logf)
            if code:
                return fail(row, "cache", tail)
            if not any((clone / ".lake" / "packages" / "mathlib" / ".lake" / "build").rglob("Mathlib.olean")):
                return fail(row, "cache", "no prebuilt Mathlib for this version; building it would take hours")
        log(f"{name}: lake build {' '.join(libs)}")
        tb = time.time()
        timeout = int(proj.get("build_timeout", BUILD_TIMEOUT // 60)) * 60
        code, tail = run(["lake", "build", *libs], cwd=clone, timeout=timeout, log_to=logf)
        row["build_minutes"] = round((time.time() - tb) / 60, 1)
        if code:
            return fail(row, "build (timeout)" if code == 124 else "build", tail)
        if generated:
            row["stage"] = "blueprint"
            code, tail = run(["lake", "build", ":blueprint"], cwd=clone, timeout=BUILD_TIMEOUT, log_to=logf)
            if code:
                return fail(row, "blueprint (generate)", tail)
            parse_and_keep()

        # Extract
        row["stage"] = "extract"
        prefixes = sorted({lib.split(".")[0] for lib in libs})
        decls = work / "decls.jsonl"
        log(f"{name}: extract {','.join(libs)} {' '.join(prefixes)}")
        with decls.open("w") as f:
            p = subprocess.run(["lake", "env", "lean", "--run", str(ROOT / "lean" / "extract_deps.lean"),
                                ",".join(libs), *prefixes], cwd=clone, env=ENV, stdout=f, stderr=subprocess.PIPE,
                               text=True, timeout=EXTRACT_TIMEOUT)
        if p.returncode:
            return fail(row, "extract", p.stderr[-3000:])
        with decls.open("rb") as f, gzip.GzipFile(out / "decls.jsonl.gz", "wb", mtime=0, compresslevel=9) as g:
            shutil.copyfileobj(f, g)

        # Join and Phase 1
        row["stage"] = "phase1"
        from cairn.blueprint import parse_blueprint
        from cairn.formal import join_blueprint, load_decls

        bp = parse_blueprint(src, entry, row["group_by"])
        ds = load_decls(decls)
        j = join_blueprint(bp, ds)
        row.update(decls=len(ds), theorems=sum(1 for d in ds.values() if d.kind == "theorem"),
                   lean_resolved=round(j.coverage, 3), nodes_linked=len(j.node_decls))
        prov = f"{repo_name} @ {row['commit'][:12]} ({row['commit_date']}), Lean {row['toolchain']}"
        code, tail = run(["uv", "run", "cairn", "phase1", str(work / row["blueprint_dir"]), str(decls),
                          "--entry", entry, "--group-by", row["group_by"], "--project", name, "--provenance", prov,
                          "--samples", "200", "-o", str(out)], cwd=ROOT, timeout=3600, log_to=logf)
        if code:
            return fail(row, "phase1", tail)
        row["status"], row["stage"] = "ok", "done"
        return row
    except Exception as e:  # keep going with the next project
        return fail(row, row.get("stage", "?"), f"{type(e).__name__}: {e}")
    finally:
        row["minutes"] = round((time.time() - t0) / 60, 1)
        (out / "triage.json").write_text(json.dumps(row, indent=1) + "\n")
        log(f"{name}: {row['status']} at {row['stage']} after {row['minutes']} min")
        shutil.rmtree(clone, ignore_errors=True)
        (work / "decls.jsonl").unlink(missing_ok=True)
        cleanup()
        report()
        if commit_results:
            commit(name, row)


def fail(row: dict, stage: str, detail: str) -> dict:
    row.update(status="failed", stage=stage, error=detail[-2000:])
    return row


def cleanup() -> None:
    """Drop the Mathlib cache and all Lean toolchains; each project installs its own again."""
    shutil.rmtree(Path.home() / ".cache" / "mathlib", ignore_errors=True)
    for tc in (ELAN / "toolchains").glob("*"):
        shutil.rmtree(tc, ignore_errors=True)
    shutil.rmtree(ELAN / "update-hashes", ignore_errors=True)


# ---------------------------------------------------------------- report and commit

def report() -> None:
    rows = [json.loads(p.read_text()) for p in sorted(RESULTS.glob("*/triage.json"))]
    order = {p["name"]: i for i, p in enumerate(tomllib.loads(MANIFEST.read_text())["project"])}
    rows.sort(key=lambda r: order.get(r["name"], 99))
    ok = [r for r in rows if r["status"] == "ok"]
    lines = ["# Blueprint harvest", "",
             f"*{len(ok)} of {len(rows)} projects harvested. Generated by `scripts/harvest.py` from "
             "`scripts/harvest_projects.toml`.*", "",
             "| project | status | blueprint nodes | `\\uses` edges | chapters (by) | Lean decls | theorems | "
             "`\\lean` resolved | nodes linked | build min | Lean |",
             "|---|---|---:|---:|---|---:|---:|---:|---:|---:|---|"]
    for r in rows:
        status = "ok" if r["status"] == "ok" else f"failed: {r['stage']}"
        status += " (generated blueprint)" if r.get("generated_blueprint") else ""
        res = f"{r['lean_resolved']:.0%}" if "lean_resolved" in r else ""
        lines.append(f"| [{r['name']}](https://github.com/{r['repo']}) | {status} | {r.get('nodes', '')} | "
                     f"{r.get('uses_edges', '')} | {r.get('chapters', '')} ({r.get('group_by', '')}) | "
                     f"{r.get('decls', '')} | {r.get('theorems', '')} | {res} | {r.get('nodes_linked', '')} | "
                     f"{r.get('build_minutes', '')} | {r.get('toolchain', '').split(':')[-1]} |")
    failed = [r for r in rows if r["status"] != "ok"]
    if failed:
        lines += ["", "## Failures", ""]
        for r in failed:
            err = (r.get("error") or "").strip().splitlines()
            lines.append(f"- **{r['name']}** at {r['stage']}: `{(err[-1] if err else '')[:200]}`")
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "triage.md").write_text("\n".join(lines) + "\n")


def commit(name: str, row: dict) -> None:
    paths = [str(RESULTS / name), str(RESULTS / "triage.md")]
    subprocess.run(["git", "add", *paths], cwd=ROOT)
    msg = (f"Harvest {name}: {row['status']}" + ("" if row["status"] == "ok" else f" at {row['stage']}")
           + "\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n"
           "Claude-Session: https://claude.ai/code/session_01SoGZmWbBAWC8u4nyqxeKio")
    if subprocess.run(["git", "commit", "-q", "-m", msg, "--", *paths], cwd=ROOT).returncode:
        return
    branch = subprocess.run(["git", "branch", "--show-current"], cwd=ROOT, capture_output=True,
                            text=True).stdout.strip()
    for wait in (0, 2, 4, 8, 16):
        time.sleep(wait)
        if subprocess.run(["git", "push", "-q", "-u", "origin", branch], cwd=ROOT).returncode == 0:
            return


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="harvest only these projects (even if already harvested)")
    ap.add_argument("--no-commit", action="store_true")
    ap.add_argument("--report", action="store_true", help="only rebuild triage.md")
    args = ap.parse_args()
    if args.report:
        report()
        return
    sys.path.insert(0, str(ROOT / "python"))
    projects = tomllib.loads(MANIFEST.read_text())["project"]
    for proj in projects:
        if args.only is not None and proj["name"] not in args.only:
            continue
        if args.only is None and (RESULTS / proj["name"] / "triage.json").exists():
            continue
        harvest(proj, not args.no_commit)
    log("harvest finished")


if __name__ == "__main__":
    main()
