# Phase 1 findings: PFR, Lean dependency graph

*Data: [`teorth/pfr`](https://github.com/teorth/pfr) @ `ddd44f6ce82e`, Lean
`v4.35.0-rc2`. Declarations were extracted with
[`lean/extract_deps.lean`](../lean/extract_deps.lean) from modules `PFR.*` and
`AddCombi.*` (a dependency that holds 3 blueprint declarations). The raw dump
is committed as `results/phase1/pfr/pfr_decls.jsonl.gz`, so the analysis
reruns without Lean. Full tables:
[`results/phase1/pfr/phase1.md`](../results/phase1/pfr/phase1.md). Reproduce
from scratch with `scripts/phase1_pfr.sh`, which takes about 7 minutes: 2 to
fetch the Mathlib cache and 4 to build PFR.*

## Why

Phase 0 scored the authors' order against dependency links (`\uses`) that the
same authors wrote. Here the links come from Lean instead. Blueprint node `B`
→ node `A` if some declaration of `A` uses a declaration of `B`, either directly
or through helper lemmas that the blueprint never mentions.

## The formal graph

- There are 1,395 project declarations: 1,244 theorems and 139 definitions,
  after compiler auxiliaries (`_proof_n`, `match_n`, recursors, constructors,
  notation helpers) are folded into their parents. They have 5,768 internal
  dependency edges.
- **Joining the blueprint to Lean is almost lossless.** 251 of 255 `\lean{}`
  names (98.4%) resolve, and 208 of the 218 nodes have at least one
  declaration. The only misses are 4 names that now live in Mathlib, such as
  `ProbabilityTheory.cond`. (The scope doc guessed 86% from grepping the
  source; that guess was wrong.)
- **1,019 project theorems are never named in the blueprint.** The blueprint
  is a summary about 5 times coarser than the formal development.
  That ratio is the "cluster / elide" signal for Phase 2.

## Author links vs Lean links

| | count |
|---|---:|
| Author `\uses` edges | 469 |
| … also a direct Lean dependency | 407 (87%) |
| … implied by a chain of Lean dependencies | 20 |
| … not a Lean dependency at all | 42 (9%) |
| Lean edges | 1,172 |
| … not written by the author | 765 (65%) |
| … … from a definition node | 439 |

- **Authors are precise but leave a lot out.** What they write is almost all
  true in Lean, but they record only about a third of the real dependencies.
- **Most omissions are background.** 57% of the unreported edges come from
  definitions: `entropy-def` alone accounts for 143. Most of the rest point to
  a few workhorse lemmas: `ruz-copy` (39), `copy-ent` (36), `ruzsa-symm` (22)
  and `independent-exist` (19). This matches the notes' warning that
  structural importance ≠ conceptual importance: authors don't cite utilities.
  It also motivates IDF-style down-weighting.
- **The 42 edges missing from Lean are places where the informal and formal
  proofs diverge.** For example, the blueprint proves `cond-reduce` via
  `alternative-mutual`, but the Lean proof of `condEntropy_le_entropy` doesn't
  go that way. These are worth reading one by one.
- The projected graph has two small cycles (among `relabeled-entropy`,
  `data-process-single`, `chain-rule` and `entropy-comm`). They happen because
  one blueprint node groups several declarations. The ordering analysis breaks
  them by dropping forward references.

## Does the Phase 0 ordering result survive?

![mean open](../results/phase1/pfr/phase1_mean_open.png)

The metric is mean results held open (lower is better):

| Scope | n | human | just-in-time DFS | optimised | uniform median | uniform orders better than human |
|---|---:|---:|---:|---:|---:|---:|
| whole, author edges | 208 | 31.2 | 37.2 | 26.3 | 52.6 | 0% |
| whole, Lean edges | 208 | 45.5 | 48.2 | 44.0 | 65.7 | 0% |
| whole, Lean edges without definitions | 208 | 37.1 | 37.0 | 28.6 | 51.9 | 0% |
| entropy | 28 | 5.8 | 7.0 | 4.9 | 8.2 | 0% |
| distance | 26 | 5.6 | 5.6 | 4.4 | 7.6 | 0% |
| entropy_pfr | 23 | 7.1 | 7.3 | 7.0 | 8.5 | 0% |
| torsion | 48 | 12.6 | 12.0 | 9.2 | 15.3 | 0% |
| further_improvement | 38 | 10.1 | 9.6 | 9.0 | 10.9 | 2% |
| small chapters (8–10 nodes) | | ≈ optimum | | | | 0–4% |

1. **The main result holds.** On author-independent links, the human order
   still beats essentially every random valid order in every scope. The
   written order is organised to limit working-memory load.
2. **The Phase 0 caveat was real: the author graph flattered the human
   order.** On Lean links, a naive just-in-time order (each lemma right before
   its first use) matches or beats the human order in `distance`, `torsion`
   and `further_improvement`. The local-search optimum is 25–30% lower in
   `torsion` and `distance`. "Near-optimal" holds for `entropy_pfr` and the
   small chapters, but not everywhere.
3. **Across chapters, the conclusion is unchanged.** The whole-document optimum
   again reaches the human's load only by splitting the 13 chapters into
   102–115 interleaved runs. **Cluster, then order** is still the right
   structure.
4. **Forward references go from 2 to 8.** Six of the new ones point to
   `data-process-single` or `chain-rule`. These are basic facts the authors
   treat as background even though Lean uses them early.

## What this means for Phase 2

- For the ordering baseline, use cutwidth or local search *within* clusters,
  with just-in-time DFS as a strong simple baseline. The gap between human and
  optimum in `torsion`/`distance` is where a learned or LLM ordering might add
  something. The other possibility is that the human order is optimising
  something we don't yet measure.
- For key-node scoring, the 1,395 → 208 compression ratio and the
  helper-lemma chains are the data for task (c): which declarations did the
  authors promote to named results?
- For utility down-weighting, the unreported-edge sources are a ready-made
  list of "workhorse" nodes to test IDF weighting against.
