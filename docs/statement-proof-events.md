# Statements, proofs and motivation

*Prompted by the observation that Carleson states a result, proves intermediate
results, and only then proves the original result. Those "forward references"
are a clarity device, not a failure of ordering. Reports:
[`results/events/pfr`](../results/events/pfr/events.md) and
[`results/events/carleson`](../results/events/carleson/events.md). Figure:
[`results/cross_project/motivation_frontier.png`](../results/cross_project/motivation_frontier.png).
Code: `cairn events` (`python/cairn/events.py`).*

## The model

Phases 0–2 treated each blueprint node as one point in the text. That is wrong
for "state now, prove later". Each node is now **two events**:

- its statement `S:v`;
- its proof `P:v`, located via `\proves{}` or the next `proof` environment.

The reading constraints are:

- `S:v` comes before `P:v`;
- if `v`'s **statement** mentions `u`, then `S:u` comes before `S:v`;
- if only `v`'s **proof** uses `u`, then `S:u` comes before `P:v`. The proof of
  `u` may come later: a **deferred proof**.

Whether a use is in the statement or the proof comes from Lean: a dependency in
the declaration's type vs only in its value. The blueprint's own `\uses` can't
be trusted for this; Carleson puts proof dependencies in statement blocks. The
load metrics carry over unchanged. A deferred proof is charged as one open item
from `S:v` to `P:v`, and a "forward reference" now means only a genuine
use-before-statement.

## Carleson's forward references are mostly deferred proofs

On Lean edges, Carleson's 126 node-level forward references break down as:

- **93 (74%) are deferred proofs:** the goal is stated first and its proof
  comes after the lemmas it needs. They are valid under the event model.
- **33 are proofs citing a lemma stated later** ("by Lemma X below"). 18 of
  these are in one section, the proof of the classical Carleson theorem.
- **None** are statements that need a later statement.

The blueprint defers 37 proofs, all with `\proves{}`. PFR defers none and has 8
genuine forward references.

With this correction the Phase 0 conclusion flips for Carleson. Its human order
beats **every** uniform random valid order on load in **all 7** sections, where
before it looked worse than random in 4 of 7. This is counted with each proof
in the section where it actually sits: 9 proofs are in a different section
from their statement. The earlier claim that "the
working-memory story is PFR-specific" was an artefact of the single-point
model.

## A second quantity: motivation

The notes' principle "no node before the goal it serves" can be measured. The
**motivated share** is the fraction of supporting results that are stated
*after* the statement of a result that uses them. A goal announced in an earlier
section, such as Carleson's overview, counts.

| | human | random valid order |
|---|---:|---:|
| PFR (chapter average) | 2% | ~54% |
| Carleson (chapter average) | 67% | ~62% |

Carleson's motivation is not spread evenly across its lemmas:

- **87%** of the lemmas serving a deferred-proof goal come after that goal
  (89 of 102);
- only **15%** of the other supporting results do (9 of 61);
- deferred goals sit early in their section (median 21% of the way through).

So Carleson is **goal-first for its key results and bottom-up underneath**.
PFR is bottom-up throughout.

## One setting spans both styles

`hybrid_order(g, goals)` states each *goal* first, then builds what its proof
needs, then proves it. Every other result is built bottom-up, with its proof
straight after its statement. With the label-free rule "a goal is a result
whose proof uses at least *m* others":

- *m* = ∞ gives pure bottom-up;
- *m* = 1 gives fully top-down.

![motivation vs load](../results/cross_project/motivation_frontier.png)

Averaged over chapters (each proof counted in the section where it sits):

| | motivated | mean open | τ with human |
|---|---:|---:|---:|
| PFR human | 2% | 6.3 | 1 |
| PFR bottom-up (*m* = ∞) | 1% | 6.6 | **0.54** |
| PFR hybrid *m* = 3 | 49% | 7.5 | 0.50 |
| PFR top-down (*m* = 1) | 93% | 8.8 | 0.19 |
| Carleson human | **67%** | **5.5** | 1 |
| Carleson bottom-up | 18% | 5.5 | 0.04 |
| Carleson hybrid *m* = 3 | 61% | 6.3 | 0.11 |
| Carleson top-down | 74% | 7.7 | 0.10 |

For the whole document, mean open is 46.2 for the PFR human order, against
47.9 bottom-up and 52.5 top-down. For Carleson it is 12.7 human, against 22.0
bottom-up and 30.6 top-down. A uniform random order scores 118.9 and 94.3.

1. **Motivation has a price in working memory,** at least for the heuristics.
   Going from bottom-up to top-down raises load by 35–40% in both projects.
   This is a quantitative handle on the trade-off between Sanderson's
   "motivated explanation" and a proof that is easy to follow.
2. **PFR's human order sits at the bottom-up end of that trade-off,**
   slightly better on load than the heuristic.
3. ~~Carleson's human order beats the trade-off curve.~~ **Corrected in
   [`style.md`](style.md):** chapter-by-chapter scoring never charges a goal
   announced in one section and proved in another. On the whole document,
   with chapters intact, a style arrangement reaches 68% motivation at load
   11.4, against the human's 60% at 12.7. The human order is close to the
   curve, not below it. The chapter-level table above still holds as
   measured, but it overstates Carleson's advantage.
4. **The setting fixes the trade-off, not the sequence.** Which lemma comes
   next inside a goal's proof still follows the paper's argument (τ ≤ 0.11 for
   every heuristic on Carleson).

## LLM baseline with proofs placed separately

`cairn event-prompts` asks the model to order steps `S:x` (state) and `P:x`
(prove), and tells it it may announce results and prove them later. Each
chapter prompt lists exactly the steps that belong to that chapter, including
"prove only" steps for results stated in an earlier section.

The runs: 2 labelled plus 2 anonymised per project, all by the current Claude
model via subagents, with every response valid. They are compared with the
earlier node-level runs, recast with each proof straight after its statement.
All methods are scored on each chapter's *core*: the results stated and
proved there. Reports:
[`results/events/pfr/llm_eval.md`](../results/events/pfr/llm_eval.md) and
[`results/events/carleson/llm_eval.md`](../results/events/carleson/llm_eval.md).

| | PFR τ | PFR motivated | Carleson τ | Carleson motivated |
|---|---:|---:|---:|---:|
| Human | 1 | 2% | 1 | 67% |
| Best heuristic | 0.53 (bottom-up) | 1% | 0.12 | 25–86% |
| LLM, node-level (proofs forced in place) | **0.86** / 0.85 | 1% | 0.39 / 0.33 | 25% |
| LLM, event-level (may defer proofs) | 0.58 / 0.52 | 29% | **0.49** / 0.46 | 56% |

*(labelled / anonymised; a single motivated share is given for the heuristic
and LLM rows.)*

1. **On Carleson, letting the model defer proofs helps.** τ goes from 0.39 to
   0.49, the best of any method. Its motivation moves towards the authors'
   (56% vs 67%), and it defers about 3 proofs per chapter against the
   authors' 4. It reaches this at a load between bottom-up and human.
2. **On PFR it hurts.** τ drops from 0.86 to 0.58, because the model defers
   about 2 proofs per chapter where PFR's authors defer none. The damage is
   concentrated in the short chapters (`improved_exponent` goes from 0.79 to
   −0.11/−0.55, `weak_pfr` from 0.81 to 0.22/0.12). There, announcing the
   main theorem first reorders almost everything.
3. **The model has its own middle style.** Given the choice, it lands at
   roughly 30% motivation on PFR and 55% on Carleson. It adapts in the right
   direction (more deferral for the paper-style content) but not to either
   author's extreme. That fits "style is a setting": the LLM has a default,
   and a tool should let the user, or the target genre, set it.
4. **Anonymising changes little** (τ −0.01 to −0.06), as with the node-level
   runs.

Caveats: 2 runs per variant; τ on events mixes statement order and proof
placement; and contamination can't be ruled out for either project.

## What this means for Cairn

- **Make the style an explicit, user-facing setting.** A bottom-up
  (textbook/blueprint) mode minimises load; a goal-first mode buys motivation
  at a measurable cost. The *m* threshold is a first rule for choosing goals.
  The key-declaration score from Phase 2 is a natural alternative to try
  next: state first the results the model says deserve a name.
- **Score candidate expositions on both axes, load and motivation**, not load
  alone. A single-objective optimiser will always produce PFR-style text.
- **Always model statements and proofs separately.** Doing so turned
  Carleson from "worse than random" into "better than every heuristic". It
  also lets an LLM reproduce a paper-style exposition better (τ 0.39 → 0.49).
- **Tell the LLM which style to write in.** Left to itself it picks a middle
  style that fits neither blueprint. A style instruction or target
  motivation level (bottom-up for a blueprint or textbook, goal-first for a
  paper) is the obvious next prompt experiment.
