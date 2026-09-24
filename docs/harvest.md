# Blueprint harvest: first 12 projects

*Code: `scripts/harvest.py`, `scripts/harvest_projects.toml`, `lean/extract_deps.lean` and
`lean/extract_deps_legacy.lean`. Per-project results are in
[`results/harvest/`](../results/harvest/), and the triage table is
[`results/harvest/triage.md`](../results/harvest/triage.md).*

The harvester works through the projects on the leanblueprint README list,
smallest first. For each one it:

1. clones the project and parses its blueprint;
2. runs Phase 0 (human order vs load), which needs only the blueprint;
3. builds with the Mathlib cache and extracts dependencies;
4. runs Phase 1 (author `\uses` vs Lean).

A project takes 3–10 minutes, and disk use stays bounded.

The first 12 projects were harvested twice. This page reports the second
pass, run after three fixes, and compares it with the first.

**Not yet harvested:** eight medium projects (APAP, Iwasawa, FormalBook,
testing lower bounds, sphere eversion, sphere packing, Brownian motion, New
Foundations). After those come PNT+, FLT and Equational Theories.

## Fixes between the passes

1. **Old Lean toolchains.** `extract_deps.lean` uses APIs from v4.22 and later.
   `extract_deps_legacy.lean` is the same program for v4.7–v4.21. It computes
   its own term sizes (structurally distinct subterms, a close stand-in for
   `Expr.numObjs`). The harvester picks the variant by toolchain and falls back
   to the legacy one if the current one fails. It also keeps the compiler's
   error text, which the first pass lost.
2. **Results upstreamed to Mathlib.** The harvester gives the extractor the
   blueprint's `\lean` names through `CAIRN_EXTRA`. Names outside the project
   are emitted as `external` records. Each blueprint-named declaration also gets
   `blueprint_reach`: the external blueprint names its proof reaches, directly
   or through up to two helper lemmas outside the project. Only theorems are
   followed, so the search stays fast and can't link everything through basic
   Mathlib. `load_decls` leaves external records out unless asked, so
   blueprint-free analyses (key model, outlines) are unchanged. Phase 1 opts in.
3. **Stub blueprints** (fewer than 10 nodes) are skipped before building.

Two problems turned up along the way:
- **zeta3 had the wrong blueprint.** Since 2026-03-20 its live `content.tex` has
  been an IMO 2025 P4 blueprint, with the ζ(3) one commented out. The manifest
  now pins the last ζ(3) commit.
- **The first reach search was too broad.** It had no depth limit and also
  followed definitions. On FLT3 it managed about 45 records a minute; the
  bounded version extracts all of FLT3 in 24 seconds.

## Linkage, before and after

| Project | Lean | Blueprint nodes | Linked, first pass | Linked now | … only through Mathlib |
|---|---|---:|---:|---:|---:|
| flt3 | v4.7 | 92 | extraction failed | **90 (98%)** | 0 |
| clt | v4.29 | 50 | 7 (14%) | **40 (80%)** | 33 |
| flt_regular | v4.34 | 45 | 12 (27%) | **29 (64%)** | 17 |
| abc_exceptions | v4.21 | 58 | extraction failed | **33 (57%)** | 0 |
| toric | v4.35 | 145 | 25 (17%) | **67 (46%)** | 42 |
| chandra_furst_lipton | v4.35 | 31 | 14 (45%) | 14 (45%) | 0 |
| semicircle | v4.24 | 205 | 58 (28%) | 58 (28%) | 0 |
| bonn_analysis | v4.10 | 65 | extraction failed | 13 (20%) | 7 |
| zeta3 | v4.18 | 30 | extraction failed | 0: no `\lean` names | — |
| banach_tarski | v4.25 | 30 | 0 | 0: no `\lean` names | — |
| infinity_cosmos | v4.34 | 41 | 0 | 0: no `\lean` names | — |
| cam_combi | v4.35 | 0 | built for nothing | skipped (stub) | — |

All four extraction failures are fixed. Every `\lean` name now resolves except
one in Bonn and those in projects without names. What still limits linkage is
the blueprints themselves:
- **Semicircle** has 205 nodes but only 58 with `\lean`; the rest is not
  formalised yet.
- **Bonn** annotates 14 of 65 nodes.
- **Chandra–Furst–Lipton** annotates 14 of 31.
- Three blueprints have no `\lean` names at all.

**FLT3 is now as well linked as PFR**, and CLT and FLT-regular are close
behind.

## Author `\uses` vs Lean dependencies (Phase 1)

Share of the author's `\uses` edges, between linked nodes, that are a direct
Lean dependency, only implied through a chain, or absent from Lean. "Unreported"
is the share of projected Lean edges that the author never wrote.

| Project | Linked nodes | Author edges | Direct | Implied | Absent | Lean edges | Unreported |
|---|---:|---:|---:|---:|---:|---:|---:|
| *PFR (reference)* | 208 | 469 | 87% | 4% | 9% | 1172 | 65% |
| *Carleson (reference)* | 170 | 212 | 94% | 0% | 6% | 353 | 44% |
| flt3 | 90 | 204 | 96% | 2% | 1% | 368 | 47% |
| abc_exceptions | 33 | 80 | 84% | 0% | 16% | 147 | 54% |
| bonn_analysis | 13 | 12 | 83% | 0% | 17% | 19 | 47% |
| chandra_furst_lipton | 14 | 20 | 80% | 0% | 20% | 27 | 41% |
| flt_regular | 29 | 31 | 77% | 3% | 19% | 40 | 40% |
| clt | 40 | 57 | 74% | 0% | 26% | 64 | 34% |
| semicircle | 58 | 75 | 64% | 1% | 35% | 139 | 65% |
| toric | 67 | 86 | 62% | 6% | 33% | 144 | 63% |

- **Most author dependencies are real Lean dependencies:** 62–96% are direct.
  FLT3 matches Lean almost exactly, like Carleson.
- **About a third of Semicircle's and Toric's `\uses` are absent from Lean.**
  Two explanations are possible, and we haven't checked which applies:
  - the blueprint states a dependency the Lean proof avoids, such as a
    definition the formal proof unfolds differently;
  - the route goes through more than two Mathlib helpers, beyond what
    `blueprint_reach` follows. Toric links 42 nodes only through Mathlib, which
    makes this more likely there.
- **Authors leave out 34–65% of the Lean edges,** as in PFR and Carleson: a
  blueprint cites the key results, not every lemma used.

## Order vs load (Phase 0)

*Gap* = (human − optimised) / (uniform random − optimised), on mean open
results. 0 means as light as our optimiser; 1 means no better than a random
valid order. "Chapter gap" is the median over chapters with at least 5 nodes.
Phase 0 needs only the blueprint, so the fixes change only zeta3.

| Project | Nodes | Forward refs | Mean open: human / optimised / random | Gap (whole) | Chapter gap (n) |
|---|---:|---:|---|---:|---|
| *PFR (reference)* | 218 | 2 | 31.9 / 30.5 / 55.4 | 0.06 | 0.17 (8) |
| *Carleson (reference)* | 180 | 90 | 16.6 / 13.3 / 39.2 | 0.13 | 1.26 (7) |
| semicircle | 205 | 5 | 14.6 / 15.8 / 41.6 | −0.05 | 0.12 (4) |
| toric | 145 | 7 | 17.7 / 12.8 / 36.2 | 0.21 | 0.80 (7) |
| flt3 | 92 | 0 | 16.0 / 10.6 / 20.4 | 0.55 | 0.23 (2) |
| bonn_analysis | 65 | 0 | 1.2 / 1.0 / 5.1 | 0.04 | 1.00 (3) |
| abc_exceptions | 58 | 12 | 9.8 / 9.3 / 13.4 | 0.13 | 1.17 (2) |
| clt | 50 | 0 | 8.8 / 6.6 / 14.2 | 0.30 | 0.75 (4) |
| flt_regular | 45 | 1 | 3.7 / 3.6 / 12.0 | 0.01 | 0.32 (4) |
| infinity_cosmos | 41 | 0 | 4.4 / 1.4 / 7.3 | 0.50 | 0.56 (2) |
| chandra_furst_lipton | 31 | 0 | 7.7 / 6.0 / 8.9 | 0.57 | 1.00 (1) |
| banach_tarski | 30 | 1 | 4.4 / 4.1 / 8.0 | 0.09 | 0.14 (1) |
| zeta3 | 30 | 0 | 5.2 / 4.0 / 8.3 | 0.28 | 0.28 (1) |

- **Across whole documents, the PFR finding generalises.** Human orders sit
  much closer to the load optimum than to a random valid order: 9 of the 11
  have a gap of 0.3 or less. zeta3's 1.53 in the first pass was an artefact of
  the IMO blueprint; the real ζ(3) blueprint scores 0.28.
- **Within chapters, the two styles show up again.** PFR-like chapters stay near
  the optimum (semicircle 0.12, Banach–Tarski 0.14, FLT3 0.23, zeta3 0.28,
  FLT-regular 0.32). Carleson-like ones are about as heavy as random (ABC 1.17,
  Bonn 1.00, Chandra–Furst–Lipton 1.00, Toric 0.80, CLT 0.75).
- **Forward references are rare.** Only ABC (12), Toric (7) and semicircle (5)
  have any, against Carleson's 90.
- **Small projects are noisy.** Seven blueprints have 50 nodes or fewer, and
  their chapter gaps rest on one to four chapters.

## Next

- **Harvest the eight medium projects** with the fixed pipeline.
- **Use the well-linked projects in the cross-project models.** FLT3, CLT and
  FLT-regular have 64–98% of nodes linked, and ABC and Toric about half. The
  key-declaration model and style fits are still trained on PFR and Carleson
  only. The style and events commands would need to opt in to external
  records for CLT, Toric and FLT-regular.
- **Check Toric's and Semicircle's absent edges:** trace a sample through
  Mathlib to see whether a deeper reach search would find them.
