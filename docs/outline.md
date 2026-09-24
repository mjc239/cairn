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
uses, and the helper lemmas folded into it. An optional LLM layer adds chapter
titles, English statements and proof sketches, checked against the Lean (see
[Prose](#prose-titles-english-statements-proof-sketches)).

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
## 24. The Polynomial Freiman–Ruzsa Conjecture

*Lean module `PFR.Main`*

- **Theorem** (`PFR_conjecture`). Let $A$ be a nonempty subset of $G$ (an elementary abelian $2$-group) with
  $|A+A|\le K|A|$. Then there exist a subgroup $H\le G$ and a set $c\subseteq G$ with $|c|<2K^{12}$,
  $|H|\le|A|$, and $A\subseteq c+H$.
  Lean: `[Countable G] [Module (ZMod 2) G] [Finite G] (hA₀ : A.Nonempty) (hA : ↑(A + A).ncard ≤ K * ↑A.ncard) :
        ∃ H c, ↑(Nat.card ↑c) < 2 * K ^ 12 ∧ (↑H).ncard ≤ A.ncard ∧ A ⊆ c + ↑H`
- *Proof of* `PFR_conjecture`. It is derived from the auxiliary statement `PFR_conjecture_aux`: the bounds … are
  converted, with an auxiliary positivity lemma, into a covering by fewer than $2K^{12}$ cosets …
  (uses `PFR_conjecture_aux`; folds in 1 helper lemma: `PFR_conjecture_pos_aux'`)
```

The goal-first version (`--top-down 0.6 --roadmap chapter`) opens the same
chapter by announcing `PFR_conjecture` and `PFR_conjecture_aux`, marked
*(proof deferred)*, and proves them at the end. It defers 57 proofs in total.

## Short statements

`extract_deps.lean` also prints a **short statement** (`stmt_short`) for each
user-facing declaration. It opens the binders with `forallTelescope` and keeps:

- explicit arguments and hypotheses, e.g. `(hA : A.Nonempty)`;
- instance assumptions that carry content: a proposition (`[Finite G]`,
  `[IsProbabilityMeasure μ]`), or a class applied to more than bare variables
  (`[Module (ZMod 2) G]`).

It drops implicit arguments and purely structural instances such as
`[AddCommGroup G]` or `[MeasurableSpace Ω]`. Proofs inside terms are hidden,
and namespaces that a reader would have open are stripped. The median
statement shrinks from 274 to 146 characters on PFR and from 246 to 116 on
Carleson. The full statement stays in the
dump as `type_pp`.

## Prose: titles, English statements, proof sketches

`python/cairn/prose.py` adds the LLM layer, anchored to the verified
statements. Everything goes through files, so any model can fill them in:

```sh
cairn outline … --prose DIR --write-prose-prompts   # DIR/<chapter>.prompt.md → fill DIR/<chapter>.prose.json
cairn outline … --prose DIR --write-check-prompts   # DIR/<chapter>.check.md  → fill DIR/<chapter>.check.json
cairn outline … --prose DIR -o outline.md           # render; prints translated / checked / flagged
```

1. **Translate.** For each chapter, the prompt lists every result with its
   short Lean statement, its docstring, and for theorems the results its
   proof uses (with their statements) and the helpers folded in. The model
   returns a chapter title of at most 8 words, a faithful English statement
   per result, and a one- or two-sentence proof sketch per theorem based on
   the listed uses.
2. **Check.** A *separate* reader sees only Lean/English pairs, never the
   translator's prompt, and marks each translation faithful or not, with the
   issue. The prose itself never replaces the Lean: the rendered outline shows
   the English, then the verified Lean statement beneath it, and a ⚠ with the
   checker's issue on flagged items.
3. **Render.** Chapter headings become the generated titles, with the Lean
   module underneath.

Both example outlines were translated and checked this way, with Claude
subagents as the translator and checker:

CHECK_RESULTS

Caveats:

- **The translations came from an earlier prompt.** It clipped Lean
  statements at 600 characters and did not yet show instance assumptions.
  Six long statements (`sum_dist_diff_le`, `e764_preCS`,
  `combine_estimates₀/₁`, `aux₄`, `estimate_trnc₁`, plus two
  `global_tree_control1_edist_part*`) were cut off, and the English says so.
  The checker saw the full current statements, so any hypothesis the English
  misses as a result is flagged. The prompts now allow 3,000 characters.
- **Sketches are not checked.** Several go beyond the listed dependencies,
  reconstructing the standard argument (e.g. `classical_carleson`,
  `ent_bsg`). They read well but are the least grounded part of the outline.
- **Notation meaning is inferred from names** when there is no docstring
  (e.g. "characteristic 2" in `sum_of_rdist_eq_char_2`). The checker is the
  guard against this.

## Limitations and next steps

- ~~Statements are Lean syntax, not prose~~ and ~~module names serve as
  chapter titles~~. Done: short statements, prose and titles above.
- **Flagged translations are only marked, not fixed.** A repair loop would
  send each flagged item back to the translator with the checker's issue, then
  check it again.
- **Proof sketches are unchecked.** A checker could compare each sketch
  against the proof's actual dependencies.
- **`detail` is a global share.** A per-chapter budget, or a target outline
  length, may suit readers better.
- **Only two training projects.** Adding more blueprint projects to
  `key_model.json` is the most direct way to improve selection.
