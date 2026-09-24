# Blueprint harvest: first 12 projects

*Code: `scripts/harvest.py` and `scripts/harvest_projects.toml`. Per-project results are in
[`results/harvest/`](../results/harvest/), and the triage table is
[`results/harvest/triage.md`](../results/harvest/triage.md). Phase 0 reports are in
`results/harvest/<project>/phase0/`.*

The harvester works through the projects on the leanblueprint README list,
smallest first. For each one it clones, parses the blueprint, builds with the
Mathlib cache, extracts dependencies and runs Phase 1. Each project took 3–5
minutes, and disk use stays bounded.

The run was stopped after 12 of 23 projects, so the small ones could be
reviewed before the large ones. The remaining eight medium projects are
APAP, Iwasawa, FormalBook, testing lower bounds, sphere eversion, sphere
packing, Brownian motion and New Foundations. After those come PNT+, FLT and
Equational Theories.

## What each project is good for

| Project | Blueprint nodes | Nodes linked to Lean | Usable for |
|---|---:|---:|---|
| semicircle | 205 | 58 (28%) | order (Phase 0), Lean comparison on a subset |
| toric | 145 | 25 (17%) | order; Lean comparison is thin: 59 of 89 `\lean` names are in Mathlib |
| flt3 | 92 | — (extraction failed) | order |
| bonn_analysis | 65 | — (extraction failed) | order: sparse (37 edges), a set of separate topics |
| abc_exceptions | 58 | — (extraction failed) | order |
| clt | 50 | 7 (14%) | order; 38 of 45 `\lean` names are now in Mathlib |
| flt_regular | 45 | 12 (27%) | order; 24 of 36 `\lean` names are in Mathlib (last commit with a blueprint, 2026-09-01) |
| infinity_cosmos | 41 | 0 | order only: the blueprint has no `\lean` links |
| chandra_furst_lipton | 31 | 14 (45%) | order, Lean comparison (small) |
| banach_tarski | 30 | 0 | order only: no `\lean` links |
| zeta3 | 30 | — (extraction failed) | order: a single dense section (92 edges) |
| cam_combi | 0 | — | nothing: the blueprint is a two-line stub |

For comparison, PFR links 208 of its 218 nodes and Carleson 170 of its 180.
**No new project is yet as well linked as the two we started with.** Every
blueprint except the stub supports the order analysis, which needs only the
blueprint.

## Why projects fall short

1. **The extractor doesn't run on older Lean (4 projects).** FLT3 (v4.7),
   Bonn (v4.10), zeta3 (v4.18) and ABC (v4.21) all built, then failed at
   extraction. `extract_deps.lean` uses recent APIs such as
   `declRangeExt.find? (level := …)` and `value? (allowOpaque := …)`.
   The harvester also lost the error text: Lean prints compile errors to
   stdout, which went into the dump file and was then deleted. New Foundations
   (v4.21) will hit the same problem.
2. **Upstreamed results.** Finished projects move their lemmas into Mathlib and
   update the blueprint's `\lean` names to point there. The dump only covers the
   project's own modules, so those nodes look unlinked (CLT, Toric,
   FLT-regular).
3. **Blueprints without `\lean` links** (Banach–Tarski, Infinity Cosmos) and a
   **stub blueprint** (LeanCamCombi).
4. **Formalisation in progress.** The semicircle law blueprint has 205 nodes
   but links only 58; the rest isn't formalised yet.

## Does the human order minimise load? (Phase 0, 11 new blueprints)

*gap* = (human − optimised) / (uniform random − optimised), computed on mean
open results. 0 means as light as our optimiser, 1 means no better than a
random valid order, and negative means lighter than the optimiser.
"Chapter gap" is the median over chapters with at least 5 nodes.

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
| zeta3 | 30 | 0 | 9.9 / 7.9 / 9.2 | 1.53 | 1.53 (1) |

- **Across whole documents, the PFR finding generalises.** Human orders sit
  much closer to the load optimum than to a random valid order: 8 of the 11
  new blueprints have a gap of 0.3 or less. The semicircle law's order is
  slightly *lighter* than our optimiser's. Chapter structure is probably a
  large part of this, since random orders scatter related results; we
  haven't measured that split here.
- **Within chapters, the two styles show up again.** PFR-like chapters stay near
  the optimum (semicircle 0.12, Banach–Tarski 0.14, FLT3 0.23, FLT-regular
  0.32). Carleson-like ones are about as heavy as random (ABC 1.17, Bonn
  1.00, Toric 0.80, CLT 0.75, Chandra–Furst–Lipton 1.00, zeta3 1.53). This
  matches the earlier reading: some authors write chapters in dependency
  order, others follow the argument of a paper.
- **Forward references are rare.** Only ABC (12), Toric (7) and semicircle (5)
  have any, against Carleson's 90. Carleson's habit of stating a goal early
  and proving it later is unusual among these projects.
- **Small projects are noisy.** Seven blueprints have 50 nodes or fewer, and
  their chapter gaps rest on one to four chapters. zeta3's 1.53 is a single
  dense 30-node section, where the random baseline is itself close to the
  optimum.

## Before the larger projects

1. **Make extraction work on older Lean, and capture its errors.** This
   recovers FLT3, Bonn, zeta3 and ABC, and later New Foundations. It
   probably needs one variant of `extract_deps.lean` for toolchains before the
   module-system APIs.
2. **Resolve `\lean` names that point into Mathlib.** Pass the blueprint's
   external names to the extractor, and record the dependency edges among
   those declarations through Mathlib. This restores the Lean comparison for
   CLT, Toric and FLT-regular, and for future finished projects.
3. **Skip stub blueprints automatically** (fewer than about 10 nodes), and
   report the share of nodes linked to Lean in the triage table.
4. Then run the remaining medium projects, which are more like PFR and
   Carleson in size (7–42k lines).
