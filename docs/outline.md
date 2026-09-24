# Blueprint-free outlines and the `detail` parameter

*Code: `python/cairn/outline.py`; commands `cairn key-model`, `cairn outline`,
`cairn outline-eval`. Everything reproduces with `scripts/outline.sh`.
Examples:
[`results/outline/pfr_conjecture.md`](../results/outline/pfr_conjecture.md)
(bottom-up),
[`pfr_conjecture_topdown.md`](../results/outline/pfr_conjecture_topdown.md)
(goal-first),
[`classical_carleson.md`](../results/outline/classical_carleson.md) and
[`pfr_full.md`](../results/outline/pfr_full.md).*

This is the end-to-end tool the project set out to build. The input is a Lean
development's dependency dump; **no blueprint is used**. The output is a
readable outline: which results to state, in what order, grouped into
chapters, each with its Lean statement, its docstring, the results its proof
uses, and the helper lemmas folded into it.

## Pipeline

1. **Extract.** `lean/extract_deps.lean` now also records each declaration's
   docstring and its statement pretty-printed with the project's notation
   (e.g. `H[X; 0] = 0`). This needs `importModules … (loadExts := true)` so
   notation is available.
2. **Select** (the **`detail`** parameter). Rank all declarations with the
   key-declaration model and keep the top `detail` share. Alternatives:
   `--count N`; `--root NAME` to outline only the dependency cone of a main
   theorem; `--modules PREFIX` to leave out dependency packages. By default
   the project definitions that named statements mention are added too, so
   every statement can be read. `--no-define-used` turns this off.
3. **Fold.** Project the Lean graph onto the named results through the
   unnamed declarations. Each result records the helpers its proof absorbs.
4. **Group** by Lean module (default) or graph community, and order chapters
   topologically, breaking ties by where the Lean sources put them.
5. **Arrange** with a `Style` (`--top-down`, `--roadmap`, `--definitions`,
   `--goal-rule`; see [`style.md`](style.md)) and render markdown.

The key-declaration model (`KeyModel`) is the Phase 2 logistic regression,
trained on one or more blueprints and saved as JSON.
`results/outline/key_model.json` is trained on PFR and Carleson together, for
use on new projects.

## How close does it get to the human blueprints?

Each project is outlined with a model trained **only on the other project**,
in the style fitted to its blueprint in [`style.md`](style.md). The blueprint
is used only to score the result. Precision is over named theorems; recall
is over the declarations the blueprint names.

**PFR** (`--modules PFR`, style `top_down = 0`; the blueprint names 18% of
declarations):

| `detail` | named (theorems) | theorem precision | recall | blueprint nodes covered | chapter NMI | τ whole | τ within chapters |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.05 | 107 (60) | 78% | 27% | 30% | 0.82 | 0.44 | 0.85 |
| 0.10 | 173 (119) | 72% | 44% | 48% | 0.84 | 0.51 | 0.61 |
| 0.15 | 237 (179) | 61% | 53% | 58% | 0.85 | 0.52 | 0.63 |
| 0.20 | 298 (238) | 52% | 59% | 63% | 0.84 | 0.53 | 0.61 |
| 0.30 | 423 (356) | 44% | 73% | 76% | 0.85 | 0.54 | 0.57 |

**Carleson** (style `top_down = 0.2` with a chapter roadmap; the blueprint
names 7% of declarations and no definitions):

| `detail` | named (theorems) | theorem precision | recall | blueprint nodes covered | chapter NMI | τ whole | τ within chapters |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.05 | 442 (121) | 48% | 27% | 35% | 0.71 | 0.40 | 0.80 |
| 0.10 | 573 (218) | 43% | 42% | 51% | 0.71 | 0.44 | 0.29 |
| 0.15 | 736 (347) | 35% | 54% | 64% | 0.72 | 0.48 | −0.02 |
| 0.20 | 909 (502) | 29% | 64% | 74% | 0.72 | 0.44 | 0.06 |

*(With `--no-define-used`, Carleson's list shrinks to 171–513 results with the
same recall; PFR's precision is unchanged. Full numbers are in
`results/outline/*_eval*.json`.)*

- **Selection is several times better than chance** at the blueprint's own
  level of detail:
  - PFR at `detail` 0.15–0.20: about 55% precision and recall, against an 18%
    base rate.
  - Carleson at `detail` 0.05–0.10: 43–48% theorem precision against 7%.

  This is out of project: no labels from the project being outlined were
  used.
- **`detail` works as a precision/recall dial.** Raising it covers more of
  the authors' results (up to 76–88% of blueprint nodes at 0.30) at the cost
  of naming more that they would have folded away.
- **Chapters from Lean modules match the blueprint's chapters well** (NMI
  0.85 on PFR, 0.71 on Carleson), better than graph communities on both
  (0.35–0.63).
- **The order agrees moderately with the authors'** (τ 0.4–0.54 overall). Within
  chapters the agreement is high for PFR (0.57–0.85) but collapses for Carleson
  above `detail` 0.05. That's consistent with everything before: Carleson's
  within-section order follows the paper's argument, which structure alone
  does not recover.
- **Model transfer has a style cost.** Trained on PFR, whose blueprint names
  definitions, the model over-selects definitions for Carleson, whose
  blueprint names none. Training on more projects, or making "include
  definitions" its own setting, would help.

## What the outline looks like

From `pfr_conjecture.md` (`--root PFR_conjecture --detail 0.25`: 134 results
out of 1,395 declarations, 24 chapters):

```
## 24. `PFR.Main`
- **Theorem** `PFR_conjecture`
  `∀ {G : Type u_1} [inst : AddCommGroup G] {A : Set G} {K : ℝ} … A.Nonempty → ↑(A + A).ncard ≤ K * ↑A.ncard → ∃ H c, ↑(Nat.card ↑c) < 2 * K ^ 12 ∧ …`
  — The polynomial Freiman-Ruzsa (PFR) conjecture: if `A` is a subset of an elementary abelian 2-group …
- *Proof of* `PFR_conjecture` — uses `PFR_conjecture_aux`; folds in 7 helper lemmas …
```

The goal-first version (`--top-down 0.6 --roadmap chapter`) opens the same
chapter by announcing `PFR_conjecture` and `PFR_conjecture_aux`, marked
*(proof deferred)*, and proves them at the end. It defers 57 proofs in total.

## Limitations and next steps

- **Statements are Lean syntax, not prose.** Implicit arguments and instance
  binders make them long. Pretty-printing with implicits hidden
  (`pp.explicit false`, dropping instance binders) is a cheap improvement.
  Turning statements into mathematical English is the natural LLM step, now
  anchored to verified statements.
- **Module names serve as chapter titles.** Naming a chapter, for example
  from the docstrings of its results, is another small LLM task.
- **`detail` is a global share.** A per-chapter budget, or a target outline
  length, may suit readers better.
- **Only two training projects.** Adding more blueprint projects to
  `key_model.json` is the most direct way to improve selection.
