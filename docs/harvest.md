# Blueprint harvest: 20 projects

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

A project takes 3–16 minutes, and disk use stays bounded.

The 12 small projects were harvested twice. The sections below report the
second pass, run after three fixes, and compare it with the first. The 8
medium projects then ran once with the fixed pipeline, and all succeeded
([Medium projects](#medium-projects)).

**Where this leaves us:** 19 projects harvested plus one stub skipped, with 3
large projects to go (PNT+, FLT, Equational Theories). **Nine** of the new
projects link at least half of their blueprint nodes to Lean (PFR and Carleson
link over 90%):
- sphere eversion 100%
- FLT3 98%
- CLT 80%
- APAP 76%
- Brownian motion 74%
- sphere packing 65%
- FLT-regular 64%
- ABC 57%
- testing lower bounds 51%

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

All four extraction failures are fixed. Nearly every `\lean` name now
resolves. The rest are stale names: 5 in CLT (e.g. `contDiff_charFun`), 7 in
FLT-regular (including Lean 3 spellings such as
`is_primitive_root.zeta_pow_sub_eq_unit_zeta_sub_one`) and 1 in Bonn. What
still limits linkage is the blueprints themselves:
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

*Superseded: the tables in this section and under Medium projects use the old
optimiser, which minimised edge length rather than mean open and did not scale.
Updated numbers for all 20 blueprints are in
[`cross_project.md`](cross_project.md#order-vs-load-all-20-blueprints).*

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

## Medium projects

8 projects, 7–42k lines of Lean each, all harvested in one pass of about an
hour. Each took 5–6 minutes, except Brownian motion (16). New Foundations
(Lean v4.21) used the legacy extractor.

### Linkage

| Project | Lean | Blueprint nodes | `\uses` edges | Chapters | Linked | … only through Mathlib | Stale names |
|---|---|---:|---:|---:|---:|---:|---:|
| brownian_motion | v4.33 | 663 | 1608 | 15 | **492 (74%)** | 183 | 1 |
| testing_lower_bounds | v4.35 | 344 | 867 | 17 | **177 (51%)** | 59 | 0 |
| formal_book | v4.34 | 192 | 103 | 45 | 69 (36%) | 0 | 0 |
| con_nf | v4.21 | 159 | 293 | 8 | 55 (35%) | 0 | 6 |
| sphere_packing | v4.32 | 141 | 246 | 11 | **91 (65%)** | 18 | 0 |
| sphere_eversion | v4.34 | 73 | 104 | 5 | **73 (100%)** | 10 | 0 |
| apap | v4.35 | 49 | 74 | 7 | **37 (76%)** | 4 | 0 |
| iwasawa | v4.33 | 15 | 3 | 5 | 7 (47%) | 0 | 0 |

- **Brownian motion and testing lower bounds are the largest blueprints we
  have.** They have 3× and 1.6× PFR's nodes, 1,608 and 867 `\uses` edges, and
  15–17 chapters.
- **Mathlib linking matters at this scale.** It recovers 183 of Brownian
  motion's linked nodes and 59 of testing lower bounds'.
- **Unfinished proofs.** New Foundations annotates only 59 of 159 nodes.
  FormalBook still has `sorry` in 30 of its 68 blueprint-named theorems.
- **Iwasawa** has a 15-node blueprint with 3 edges for 10,000 lines of Lean,
  so it's of little use for either analysis.

### Author `\uses` vs Lean (Phase 1)

| Project | Linked nodes | Author edges | Direct | Implied | Absent | Lean edges | Unreported |
|---|---:|---:|---:|---:|---:|---:|---:|
| brownian_motion | 492 | 1058 | 87% | 2% | 11% | 2428 | 62% |
| testing_lower_bounds | 177 | 316 | 81% | 3% | 16% | 883 | 71% |
| sphere_packing | 91 | 123 | 79% | 2% | 20% | 315 | 69% |
| sphere_eversion | 73 | 104 | 88% | 0% | 12% | 265 | 65% |
| con_nf | 55 | 87 | 72% | 0% | 28% | 519 | 88% |
| apap | 37 | 43 | 91% | 0% | 9% | 46 | 15% |
| formal_book | 69 | 23 | 9% | 0% | 91% | 3 | 33% |

- **Agreement is high and consistent with the other projects:** 72–91% of author
  edges are direct Lean dependencies. Brownian motion matches PFR (87%) with
  twice as many author edges.
- **FormalBook is the exception, for a known reason.** 30 of its 68
  blueprint-named theorems still depend on `sorry`, so their Lean proofs have
  no dependencies to compare. Its 45 chapters are also independent proofs, with
  few `\uses` between them.
- **New Foundations' authors report very little of the Lean graph.** They leave
  out 88% of Lean edges, the most of any project. Its proofs lean on a large
  set of technical lemmas the blueprint doesn't name.

### Order vs load (Phase 0)

*Superseded; see [`cross_project.md`](cross_project.md#order-vs-load-all-20-blueprints).*

| Project | Nodes | Forward refs | Mean open: human / optimised / random | Gap (whole) | Chapter gap (n) |
|---|---:|---:|---|---:|---|
| brownian_motion | 663 | 15 | 39.7 / 59.1 / 145.1 | −0.23 | 0.18 (14) |
| testing_lower_bounds | 344 | 28 | 32.8 / 32.0 / 61.7 | 0.03 | 0.49 (12) |
| formal_book | 192 | 11 | 1.2 / 1.5 / 32.8 | −0.01 | 0.52 (8) |
| con_nf | 159 | 2 | 15.1 / 14.7 / 29.4 | 0.03 | 0.19 (7) |
| sphere_packing | 141 | 13 | 15.7 / 15.6 / 33.2 | 0.00 | 0.15 (5) |
| sphere_eversion | 73 | 11 | 7.9 / 8.3 / 20.4 | −0.03 | 0.45 (4) |
| apap | 49 | 0 | 5.3 / 5.0 / 11.8 | 0.04 | 0.14 (4) |
| iwasawa | 15 | 0 | 1.1 / 0.2 / 1.0 | (too small) | — |

- **Whole documents: every medium project except tiny Iwasawa is at the load
  optimum or better** (gap between −0.23 and 0.04). With the small batch, 15 of
  the 18 blueprints large enough to score have a whole-document gap of 0.3 or
  less. Authors order whole documents almost as tightly as an optimiser.
- **Our optimiser doesn't scale to Brownian motion.** Its 663-node order is
  heavier than the authors' (59.1 open against 39.7), so the negative gap there
  shows the limit of greedy search with local moves, not superhuman authors.
  The local search needs more restarts, or a better start, on large graphs.
- **Within chapters, these projects are mostly PFR-like:** APAP 0.14, sphere
  packing 0.15, Brownian motion 0.18, New Foundations 0.19. Testing lower
  bounds (0.49), FormalBook (0.52) and sphere eversion (0.45) sit in between.
  None has Carleson's paper-like chapters (1.26), unlike ABC, Bonn and
  Chandra–Furst–Lipton in the small batch. Larger projects also give firmer
  chapter estimates: 4–14 chapters each.
- **Forward references stay rare:** at most 28 (testing lower bounds), against
  Carleson's 90.

## Next

- **Use the well-linked projects in the cross-project models.** At least 9
  projects now link half or more of their nodes to Lean, and three are bigger
  than PFR. The key-declaration model and style fits are still trained on PFR
  and Carleson only. The style and events commands would need to opt in to
  external records for projects linked through Mathlib.
- **Make the optimiser scale** (more restarts, or starting from the author's
  order) before comparing orders on 500+ node blueprints.
- **The three large projects** (PNT+, FLT, Equational Theories) are next in the
  manifest. PNT+ built in 33 minutes in the aborted first run.
- **Check Toric's and Semicircle's absent edges:** trace a sample through
  Mathlib to see whether a deeper reach search would find them.
