# Second project: Carleson, and what generalises from PFR

*Data: [`fpvandoorn/carleson`](https://github.com/fpvandoorn/carleson) @
`d966776f60fe` (2026-09-23), Lean `v4.34.0-rc2`. The blueprint is a single
file, so its 11 `\section`s play the role of chapters (`--group-by section`).
Reproduce everything with `scripts/carleson.sh`: about 10 minutes with the Lean
build (Mathlib cache 2.5 min, build 6.5 min, extraction 16 s), or 1 minute from
the committed dump with `--no-lean`. Reports:
[`results/phase0/carleson`](../results/phase0/carleson/phase0.md),
[`phase1`](../results/phase1/carleson/phase1.md),
[`phase2`](../results/phase2/carleson/phase2.md),
[`LLM runs`](../results/phase2/carleson/llm_runs.md) and
[`key-declaration transfer`](../results/cross_project/key_node_transfer.json).*

## Why Carleson

It is finished and completely formalised: all 180 blueprint nodes have
`\lean{}` and `\leanok`. It is in a different area from PFR (harmonic analysis
vs additive combinatorics) and was written by a different team. Its blueprint
is also written in a different *style*, which turned out to matter most.

## The data

| | PFR | Carleson |
|---|---:|---:|
| Blueprint nodes / chapters | 218 / 13 | 180 / 11 sections |
| Definitions among nodes | 30 | 0 |
| `\lean{}` names resolved | 98% | 95% (the misses are Mathlib lemmas) |
| Project declarations | 1,395 | 3,422 |
| Share named in the blueprint | 18% | 7% |
| Author `\uses` edges confirmed by Lean | 87% | 94% |
| Lean edges the authors wrote down | 35% | 56% |
| **Forward references in the human order** | **1%** | **36–41%** |

A caveat on the Lean side: Carleson's `ToMathlib/RealInterpolation/LorentzInterpolation.lean`
still contains a `sorry`, so a few dependency edges there may be missing.

## Findings

### 1. The two blueprints are written in opposite styles

- **PFR is bottom-up:** every lemma comes before the result that uses it.
- **Carleson reads like the paper:** a section states its main proposition,
  proves it "using Lemmas A, B, C below", then states and proves those lemmas.
  About 40% of its dependency edges point forward.

The load metric gives a reversed order exactly the same score (tested in
`test_metrics_are_reversal_invariant`), so a consistently top-down blueprint
would not be penalised. Carleson is not consistently top-down, though: a
goal-first DFS matches its within-section order at only τ 0.15. It **mixes**
directions.

### 2. ~~So the working-memory story is PFR-specific~~ Corrected: deferred proofs

The first analysis treated each result as one point. Within sections it found
Carleson worse than a random valid order in 4 of 7 sections. **That was an
artefact.** Carleson states a goal, proves the lemmas it needs, and only then
proves the goal. That is 37 `\proves{}`-deferred proofs, accounting for 74% of
its forward references.

When statements and proofs are modelled as separate events, the human order
beats every random valid order on load in 6 of 7 sections. It also turns out
to sit on a measurable trade-off between working memory and motivation. See
[`statement-proof-events.md`](statement-proof-events.md).

### 3. Key declarations generalise; ordering does not

| Task | PFR | Carleson |
|---|---:|---:|
| Key declarations, AUROC (in-project, modules held out) | 0.87 | 0.90 |
| Key declarations, precision@k (base rate) | 60% (18%) | 46% (7%) |
| **Key declarations, trained on the *other* project** | **0.79** | **0.85** |
| Chapters: Lean module NMI / best graph-community NMI | 0.83 / 0.58 | 0.72 / 0.82 |
| Order within chapters: random / best structural / LLM (τ) | 0.54 / 0.73 / 0.85 | −0.10 / 0.18 / 0.19 |
| Lean source order vs blueprint order (τ within chapters) | 0.87 | 0.18 |

- **Key declarations are the robust result.** The same few signals pick out
  named results in both projects: uses many project lemmas, large statement,
  sizeable proof, on paths towards the main results, not private. A model
  trained on one project works on the other with little loss. The
  "variant of" features help slightly on Carleson (+0.01 AUROC, +2 points
  precision@k) and not at all on PFR.
- **Chapter recovery works in both, but the best signal differs.** Lean
  modules win on PFR; graph communities win on Carleson. Carleson's files are
  organised differently from its blueprint sections (47 modules against 11
  sections).
- **Ordering is where the projects differ.**
  - In PFR the blueprint order is largely predictable. Load minimisation gives
    0.73 and the LLM 0.85, but the Lean files were written in the same order,
    so that result is partly shared authorship.
  - In Carleson *nothing* we have predicts the within-section order well: not
    load minimisation, not goal-first DFS, not the Lean file order and not the
    LLM (0.19 ± 0.03 over 4 runs). The LLM does well on two long sections
    (discrete Carleson 0.78, forest operator 0.77) and badly on others.
  - Carleson's order encodes the *paper's proof narrative*: which step of the
    argument each lemma serves. That isn't visible from statements and
    dependencies alone. Its authors' own proof sketches (the text between
    lemmas) are the obvious missing input.

### 4. The LLM result on PFR survives anonymisation

With random ids and no titles, the LLM's PFR τ drops from 0.85 ± 0.00 to
0.83 ± 0.01 (3 runs each; details in
[`results/phase2/pfr/llm_runs.md`](../results/phase2/pfr/llm_runs.md)). So it
was not reading the order off the authors' labels. Recognising the statements
from the PFR paper remains possible; that would need paraphrased statements to
test. On Carleson anonymisation makes no difference either (0.20 vs 0.18), but
there is little signal to lose.

## Implications for Cairn

1. **"Readable order" is not one objective** (made precise in
   [`statement-proof-events.md`](statement-proof-events.md): load vs motivation, with one setting between them). A tool needs at least two
   styles:
   - bottom-up (PFR, textbook-like), where load minimisation plus an LLM
     reorder gets close to human choices;
   - narrative (Carleson, paper-like), where the order follows a proof sketch.

   The narrative style probably has to be generated together with the
   connecting prose, not recovered from the graph. This lines up with the
   *augment* step in the original notes.
2. **Key-declaration selection is ready to use** as the "which lemmas deserve
   a name" component. It is cheap, it transfers, and its errors are
   interpretable.
3. **For clustering**, try Lean modules and graph communities and pick
   whichever is more modular. Neither wins everywhere.
