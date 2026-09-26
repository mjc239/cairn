# Navier–Stokes and Euler blowup: blueprint-free outlines

Outlines of [openai/NavierStokesAndEuler](https://github.com/openai/NavierStokesAndEuler) at commit `f9e8bc5`,
produced by `scripts/outline_navier_stokes.sh` with **no LLM**: statements are the verified Lean statements, and the
selection model (`key_model_all.json`) was trained on 9 other projects' blueprints, never on this one.

| Outline | Main theorem | Results | Chapters |
|---|---|---:|---:|
| [`ns_R3.md`](ns_R3.md) | `NavierStokes.Comparator.navier_stokes_breakdown_R3` | 151 | 67 |
| [`ns_periodic.md`](ns_periodic.md) | `NavierStokes.Comparator.navier_stokes_breakdown_periodic` | 151 | 67 |
| [`euler_R3.md`](euler_R3.md) | `Euler.euler_breakdown_R3` | 151 | 127 |

The development has about 56,000 user-facing declarations (38,500 theorems, 10,800 definitions, 12,700
docstrings, no `sorry`), in 2,655 files; proofs are short (median 8 lines, longest 205). It is the opposite of a
monolithic AI proof: the structure is all there, and the difficulty is choosing ~150 results out of 56,000.

What these first outlines show:
- **Too many chapters.** Chapters are Lean modules, and this project has one small module per step, so 150 results
  spread over 67–127 chapters, 31 of them with a single result. Grouping modules (by name prefix or graph
  community) into a dozen chapters is the obvious next step.
- **Selection looks plausible but is unvalidated.** There is no blueprint to score against. The main theorems and
  their comparator definitions are in, along with the large intermediate "bounds", "invariant" and "cycle" results
  the proof is built from.
- **Readable names and docstrings help.** Many results carry docstrings, which the outline shows.
- Not done here (to save usage): English statements, proof sketches, chapter titles.

Two scaling fixes this needed: betweenness is estimated from 500 sampled sources on graphs over 20k nodes (exact
took ~5 h), and each result's list of folded helper lemmas shows at most 30 names.
