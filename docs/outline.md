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
| 0.05 | 101 (59) | 78% | 27% | 30% | 0.82 | 0.44 | 0.88 |
| 0.10 | 167 (119) | 72% | 44% | 48% | 0.84 | 0.51 | 0.61 |
| 0.15 | 230 (178) | 61% | 53% | 58% | 0.85 | 0.52 | 0.62 |
| 0.20 | 291 (237) | 52% | 59% | 63% | 0.84 | 0.53 | 0.61 |
| 0.30 | 415 (354) | 44% | 73% | 76% | 0.85 | 0.54 | 0.57 |

**Carleson** (style `top_down = 0.2` with a chapter roadmap; the blueprint
names 7% of declarations and no definitions):

| `detail` | named (theorems) | theorem precision | recall | blueprint nodes covered | chapter NMI | τ whole | τ within chapters |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.05 | 420 (121) | 48% | 27% | 35% | 0.71 | 0.40 | 0.79 |
| 0.10 | 549 (217) | 43% | 42% | 51% | 0.71 | 0.43 | 0.27 |
| 0.15 | 711 (346) | 35% | 54% | 64% | 0.72 | 0.47 | −0.03 |
| 0.20 | 882 (500) | 29% | 64% | 74% | 0.72 | 0.43 | −0.03 |

*(With `--no-define-used`, Carleson's list shrinks to 169–672 results with the
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

From `pfr_conjecture.md` (`--root PFR_conjecture --detail 0.25`: 131 results
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
  `[IsProbabilityMeasure μ]`), a class applied to more than bare variables
  (`[Module (ZMod 2) G]`), or `[Fintype G]`, which is data but says G is finite.
  Dumps made before `Fintype` was kept get it back from the full statement
  (`formal.restore_fintype`).

It drops implicit arguments and instances on bare variables such as
`[AddCommGroup G]` or `[MeasurableSpace Ω]`. Proofs inside terms are hidden,
and namespaces that a reader would have open are stripped. The median
statement shrinks from 274 to 146 characters on PFR and from 246 to 116 on
Carleson.

**The short form is only for the displayed line.** Dropped assumptions can
matter: `[AddCommGroup G]` says G is abelian, `[MetricSpace X]` is stronger
than `[PseudoMetricSpace X]`, and `[ProofData …]` bundles all of Carleson's
standing hypotheses. So nothing that feeds the prose uses it alone (see
[Nothing hidden](#nothing-hidden-from-the-translator-or-checker) below). The
rendered outline shows the short line and, under a *Full Lean statement*
toggle, the full one (`type_pp`). That form has every implicit argument and
instance, typed numerals (`(12 : ℝ)`, `(4 : ℕ)`), and the space behind each
ambiguous instance (`IsProbabilityMeasure (α := Ω₀₁) volume`).

## Prose: titles, English statements, proof sketches

`python/cairn/prose.py` adds the LLM layer, anchored to the verified
statements. Everything goes through files, so any model can fill them in:

```sh
cairn outline … --prose DIR --write-prose-prompts   # DIR/<chapter>.prompt.md → fill DIR/<chapter>.prose.json
cairn outline … --prose DIR --write-check-prompts   # DIR/<chapter>.check.md  → fill DIR/<chapter>.check.json
cairn outline … --prose DIR --write-repair-prompts  # DIR/<chapter>.repair.md → fill DIR/<chapter>.repair.json; check again
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
3. **Repair.** Flagged items go back to a translator with the Lean statement,
   the previous English and the checker's issue. The corrected statements
   override the originals (rounds stack as `.repair.json`, `.repair2.json`, …),
   and the repaired chapters are checked again by a fresh checker.
4. **Render.** Chapter headings become the generated titles, with the Lean
   module underneath.

Both example outlines were translated and checked this way, with Claude
subagents as the translator and checker:

| Round | PFR (134 results) | Carleson (196 results) |
|---|---:|---:|
| 1. Translate, check | 83 flagged | 12 flagged |
| 2. Repair flagged, re-check their chapters | 0 of the 83 still flagged; 15 others newly flagged | 0 of the 12 still flagged |
| 3. Repair those 15, re-check | 0 flagged | — |

At that point every English statement in both outlines passed its latest check (the later, stricter rounds
under [Nothing hidden](#nothing-hidden-from-the-translator-or-checker) reopened many). The
per-round verdicts are kept in `*.check.round1.json` and `*.check.round2.json`.

What the checks caught:

- **Dropped instance hypotheses** were most of round 1 on PFR. The
  translations came from an earlier prompt that did not show instance
  assumptions, so the English lacked "$G$ is finite", "$\mu$ is a probability
  measure" or "$X$ takes finitely many values". The checker saw the current
  statements. Carleson's statements rarely hang on instances, hence its much
  lower count.
- **Truncated statements.** The earlier prompt clipped Lean statements at 600
  characters. Six long Carleson bounds (`combine_estimates₀/₁`, `aux₄`,
  `estimate_trnc₁`, `e764_preCS`, `global_tree_control1_edist_part1/2`) had
  English that stopped at "…". Prompts now allow 3,000 characters, and the
  repairs state the full bounds.
- **Claims the Lean doesn't make:** for example that the sets `ℭ(k,n)`
  partition `𝔓(k)`, or that a family of tile sets consists of antichains.
- **Checkers vary.** The round-2 checkers flagged omitted `Countable` and
  `MeasurableSingletonClass` assumptions that the round-1 checkers had judged
  technical. A single check pass is a noisy filter. Re-checking whole chapters,
  not only the repaired items, is what surfaced this.

Caveats:

- **Sketches are not checked.** Several go beyond the listed dependencies,
  reconstructing the standard argument (e.g. `classical_carleson`, `ent_bsg`).
  They read well but are the least grounded part of the outline.
- ~~Some readings are the translator's~~. Where the printed Lean was
  ambiguous (which space a `volume` lives on, the type of `1 / 2`), the English
  had to pick a reading. The full statements are now printed unambiguously, so
  these readings are checked (see
  [Nothing hidden](#nothing-hidden-from-the-translator-or-checker)).
- **Translator and checker are the same model family**, as separate
  subagents. They share context isolation but may share blind spots.

## Outlines of the 9 training projects

*Code: `scripts/outline_projects.py`. Outlines and evaluation:
[`results/outline/projects/`](../results/outline/projects/)
([`eval.md`](../results/outline/projects/eval.md)).*

With 9 well-linked projects ([`cross_project.md`](cross_project.md)), each
one can be outlined by a model that has never seen it. The key-declaration
model is trained on the other 8, and the outline uses the exposition style
fitted to the project's blueprint. It is evaluated at the blueprint's own
level of detail, the share of declarations its authors named. The baseline is
the previous model, trained on PFR and Carleson only (minus the project).

| Project | Detail | Style | Named (theorems) | Theorem precision | Recall | Nodes covered | Chapter NMI | τ within chapters | Baseline: named, theorem precision |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| PFR | 0.18 | `top_down=0` | 282 (213) | 60% | 60% | 66% | 0.85 | +0.68 | 305, 50% |
| Carleson | 0.07 | `top_down=0.2`, chapter roadmap | 537 (192) | 40% | 35% | 47% | 0.72 | +0.26 | 464, 46% |
| brownian_motion | 0.15 | `top_down=0` | 426 (263) | 29% | 39% | 39% | 0.78 | +0.58 | 464, 25% |
| testing_lower_bounds | 0.12 | `top_down=0` | 157 (116) | 26% | 33% | 33% | 0.63 | +0.54 | 165, 24% |
| sphere_packing | 0.07 | `top_down=0` | 204 (81) | 28% | 54% | 53% | 0.82 | +0.89 | 211, 28% |
| flt3 | 0.38 | `top_down=0` | 101 (60) | 78% | 58% | 58% | 1.00 | +0.28 | 119, 61% |
| sphere_eversion | 0.06 | `top_down=0.2` | 188 (42) | 48% | 62% | 65% | 0.62 | +0.51 | 205, 34% |
| abc_exceptions | 0.20 | `top_down=0.2`, chapter roadmap | 78 (43) | 49% | 71% | 91% | 0.92 | +0.67 | 82, 44% |
| apap | 0.04 | `top_down=0` | 46 (27) | 78% | 74% | 76% | 0.83 | +0.64 | 53, 67% |

*Named counts include the definitions added so that every statement can be read
(`define_used`), which is why they exceed the detail share. Structure fields count
with their structure.*

- **Selection works well beyond chance on projects it has never seen.** At
  each blueprint's own detail, precision on named theorems is 2–18 times the
  base rate. The highest lifts are on the most selective blueprints: APAP names
  4% of its declarations and the outline hits 78%; sphere eversion names 6%
  and the outline hits 48%.
- **More training projects make outlines tighter, not broader.** Across all 45
  project and detail settings, recall is unchanged (mean 57% for both
  models). Theorem precision rises in 37 settings and falls in 7 (mean 42% vs
  38%). At the blueprints' own detail, the new model names 3–15% fewer
  results on 8 of 9 projects, with recall within 2 points. It spends its budget on
  fewer, better-chosen theorems.
- **Carleson is the exception.** The new model names more of its declarations
  as theorems (192 against 147) and loses theorem precision (40% vs 46%),
  though recall improves (35% vs 31%). Carleson's blueprint names no
  definitions at all, unlike most training projects, so a model trained on
  them transfers less well there.
- **Chapters from Lean modules match the blueprint's chapters** (NMI
  0.62–1.00). **Order within chapters agrees well** with the authors
  (τ +0.51 to +0.89) except in FLT3 and Carleson (+0.28, +0.26), whose
  authors follow the argument rather than the dependency order.
- **The hardest projects are the largest.** Brownian motion and testing lower
  bounds reach 26–28% theorem precision and 33–39% recall. Their blueprints
  name many mid-level lemmas that look structurally like helpers, as in the
  key-model results.
- **Structure fields are shown with their structure.** Projections such as
  `DualPair.v` used to be pulled in by `define_used` as named definitions of
  their own. The loader now reads each structure's fields from its
  constructor, and selection names the structure instead. This shortens
  outlines by 2–25 results (sphere eversion 224 → 199, Carleson's example
  196 → 194) without changing which theorems are chosen: precision and
  recall are unchanged.

## Checked prose for a new project: APAP

[`results/outline/apap.md`](../results/outline/apap.md) is the first harvested
project with English prose. The outline comes from the model trained on the
other 8 projects, never on APAP (`key_model_without_apap.json`), at the
blueprint's own detail (0.044): 46 results in 20 chapters. The prose went
through the same translate, check and repair loop as PFR and Carleson:

| Round | Flagged |
|---|---:|
| 1. Translate (2 agents), check (fresh agent, Lean/English pairs only) | 3 of 47 |
| 2. Repair those 3, re-check their chapters | 0 |
| 3. Short statements now show `[Fintype G]` (below): re-check the 14 chapters whose Lean lines changed | 30 of 39 |
| 4. Repair those 30, re-check their chapters | 0 |

At that point all 46 English statements passed their latest check (reopened by the later rounds under
[Nothing hidden](#nothing-hidden-from-the-translator-or-checker)).

What the checker caught:

- **A real notation error.** In Chang's lemma the Lean takes
  `Real.log (x)⁻¹`, the log of the inverse. The English had written
  $\log(x)^{-1}$, which reads as one over the log. The repair writes
  $\log(1/x)$.
- **Definition glosses that claimed too much.** The signature of `BohrSet`
  shows only `Type → Type`, but the English described its fields. The English
  for `dLpNorm` asserted a normalisation that the signature can't show. The
  repairs keep to the signature and attribute extra detail to the docstring
  ("according to its docstring…").
- **Missing finiteness, once the Lean showed it.** The first short statements
  dropped `[Fintype G]` (see below), and 30 English statements never said G is
  finite. Round 3 flagged all of them as soon as the Lean line showed the
  assumption.

**Two fixes this prompted, for every project:**

- **`[Fintype X]` is now shown.** Short statements keep instance assumptions
  that are propositions (`[Finite G]`) or carry content (`[Module (ZMod q) G]`),
  and drop data classes on a bare variable such as `[AddCommGroup G]`.
  `Fintype X` is data, but it says X is finite, so both extractors now keep
  it. `formal.restore_fintype` adds it back to older dumps from the full
  statement, so no re-extraction is needed. Only APAP's outline statements
  change (PFR uses `[Finite G]`). Other data classes, such as `DecidableEq`,
  stay hidden as technical.
- **Boilerplate instances are never named results.** The first APAP outline
  named an auto-generated `DecidablePred` instance.
  `outline.is_boilerplate_instance` now excludes auto-named instances of
  plumbing classes (`Decidable…`, coercions, `Inhabited`, `Repr`, `FunLike`
  and similar). Instances of mathematical classes stay eligible, because
  blueprints do name them: `SimpleProcess.instModule` (Brownian motion),
  `instIsZLatticeE8Lattice` (sphere packing), `instFunctionDistancesReal`
  (Carleson). Outlines lose 1–15 results; precision and recall move by at most
  a point. This list was later narrowed to classes with no mathematical content
  (see [Nothing hidden](#nothing-hidden-from-the-translator-or-checker)).

**Readability note.** Several sketches go beyond the listed dependencies, as for
PFR and Carleson (e.g. "iterated density increment" for `ff`, inferred from
helper names).

## Nothing hidden from the translator or checker

The short statements, the APAP fixes and the boilerplate rule all drop
something, so we audited every drop. Question: could anything dropped ever
matter for the prose, or even help it? It could, in each case:

- **Hidden instances carried content.** Among the instances dropped from short
  statements were `AddCommGroup` (commutativity), `Field`, `MetricSpace` vs
  `PseudoMetricSpace`, `DoublingMeasure X A` (the doubling constant) and
  Carleson's standing bundles (`ProofData`, `KernelProofData`,
  `TileStructure`).
- **Some excluded instance classes can carry content.** `Nonempty`,
  `Inhabited`, `Unique` and `Subsingleton` instances state facts. `CoeSort` and
  `FunLike` instances define how an object is read as a set or function.
- **The printer hid information.** Bare numerals left their type implicit.
  `𝕔 / 4` is floor division on ℕ, and `K ^ 12` could be a natural-number or a
  real power. `IsProbabilityMeasure volume` did not say which space. PFR's own
  numeral delaborator (`Mathlib.Tactic.RPowRing.delab_ofNat`) printed some
  numerals as raw `nat_lit`.
- **Binder types were hidden.** `∃ H c, …` in `PFR_conjecture` did not say that
  H is a subgroup and c a set. The same gap affected 30 of the 371 outlined
  results.
- **Prompts truncated.** Uses lists stopped at 10 entries, helper lists and
  docstrings were clipped, and check prompts had no docstrings, so checkers
  could not verify glosses attributed to them.

Removing a term buys only a shorter displayed line. It never helps the
translator or checker, so they now see everything:

- **Full statements everywhere.** Translate, check and repair prompts give each
  result as `Lean (short)` and `Lean (full)` (only one line when they agree).
  The *proof uses* list gives full statements, all of them. Helpers and
  docstrings are complete, and check prompts include docstrings.
- **Unambiguous printing.** `type_pp` is printed with `pp.numericTypes`,
  `pp.funBinderTypes` (so `∃ U : Ω → G`, not `∃ U`) and `pp.analyze` (falling back to plain printing if analysis fails).
  Project-local `OfNat` delaborators are erased before printing
  (`eraseProjectNumeralDelabs`). The three dumps were re-extracted at their
  pinned commits (`scripts/reextract.sh`). Of the whole PFR dump, only 4
  tactic-internal statements still print `nat_lit`, and none is a result.
- **Project definitions in every prompt.** Statements use project notions (`ProofData`, 𝔗(u), `rdist`,
  `carlesonSum`) whose meaning a checker cannot verify from the statement alone. Each prompt opens with a
  glossary of the project notions its chapter refers to, followed three levels deep through statements and
  definition bodies (`prose.glossary`). Each entry gives the full statement, the docstring, the definition body
  (`value_pp`, now extracted) and, for a structure, its constructor with every field and type (`ctor_pp`).
  Results that are themselves definitions or structures show their body or constructor too.
- **Narrow exclusions.** `is_boilerplate_instance` now excludes only instances
  of classes with no mathematical content: `Decidable…`, `Repr`, `ToString`,
  `Hashable`, `BEq`. Tactic implementation code (`….Tactic.…`) is also
  excluded.
- **The budget ignores exclusions.** `detail × |universe|` is computed before
  the exclusions. Before this fix, excluding tactic code shrank the budget and
  two real PFR theorems dropped out (`IsUniform.entropy_eq`,
  `sum_of_rdist_eq_char_2`). A regression test covers it.
- **Stricter checking.** The checker must flag:
  - any missing assumption, including one carried by an instance (only
    `Decidable…` may stay unstated);
  - a stronger assumption than the Lean's (metric for pseudometric);
  - an unstated restrictive type (ℕ, ℝ≥0);
  - a definition that doesn't name its setting;
  - a citation or remark that neither the docstring nor the Lean supports.

  Standing bundles (`ProofData`, `KernelProofData`, `TileStructure`,
  `GridStructure`) may be named compactly.

All 371 results (PFR 131, Carleson 194, APAP 46) were re-checked from scratch
under this regime:

Each round is a fresh check of every chapter by separate checker agents, followed by repairs of what was flagged.
Each step that exposed more information, or made the rules stricter, raised the count before repairs brought it
down:

| Round | What changed before the check | Flagged (of 371) |
|---|---|---:|
| 1 | Checkers see full statements (every implicit argument and instance) | 142 |
| 2 | Stricter rules: settings of definitions, no strengthened assumptions, restrictive types, supported citations | 117 |
| 3 | Borderline passes reported by checkers are flagged too | 37 |
| 4 | Typed binders (`∃ U : Ω → G`); every variable typed, every symbol introduced, no unsupported descriptions | 138 |
| 5 | Prompts list the project definitions each chapter uses (glossary) | 95 |
| 6 | Definition bodies and structure constructors shown; a definition must say what it defines | 173 |

The per-round verdicts are kept as `*.check.full1.json` and `*.check.strict1.json` … `*.check.strict6.json`.

**Where this stopped.** The loop was stopped after round 6 to save usage, before it reached zero. Of the 173
statements round 6 flagged, 147 have been revised (round-6 repairs) but not re-checked, and 26 were not repaired.
The outlines say which is which: a revised statement carries "⚠ Translation flagged, then revised; the revision
is not yet re-checked", an unrepaired one "⚠ Translation flagged", each with the checker's issue. The other 198
statements passed round 6. `cairn outline … --prose DIR` prints the same counts. Most round-6 flags are about
completeness (a definition that paraphrases its docstring instead of saying what its body defines, a symbol not
introduced); fewer are errors of substance, such as "bounded and measurable" for `BoundedCompactSupport`, which
asks only for essential boundedness and a.e.-strong measurability, or "supp f ⊆ F" where the Lean means
`Function.support`.

The count did not fall monotonically: each time the checkers were shown more (typed binders, the glossary,
definition bodies and constructors) or given a stricter rule, they found a new kind of gap. To finish, run the
repair prompts still unanswered (`--write-repair-prompts`), then full re-checks until one flags nothing. A full
check reads about 2.8 MB of prompts, so re-checking only the chapters that changed is the cheaper option.

What the full statements caught, beyond missing assumptions:

- **`drc` (APAP):** `p` is a natural number, but the English treated it as a
  real exponent.
- **`construct_good` (PFR):** the English put the random variables on the wrong
  probability space. The analysed printing shows which `volume` each
  hypothesis refers to.
- **Strengthened assumptions:** "metric space" where the Lean has a
  pseudometric (Carleson), and "finite group" where only `[Finite G]` on an
  `AddCommGroup` was assumed.
- **Types:** `Tile.I12_le'` uses ℕ floor division `𝕔 / 4`. The exponents
  `(1 / 2 : ℝ)` in Carleson are real, as the typed numerals now show.
- **Definitions without their setting:** most of the strict round's flags.

## Limitations and next steps

- ~~Statements are Lean syntax, not prose~~ and ~~module names serve as
  chapter titles~~. Done: short statements, prose and titles above.
- ~~Ambiguous pretty-printing~~. Done: typed numerals and `pp.analyze` in the
  full statements, which the translator and checker now see (above).
- **Prose checks not finished.** 173 of 371 statements are flagged or revised-but-unchecked after round 6
  (above). Finish with targeted re-checks of changed chapters.
- **Standing assumptions are named, not listed, in each statement.** Carleson statements say "assume
  `ProofData`" rather than repeating its twenty fields. The rendered outline could show each chapter's glossary
  (standing structures and definitions) once, so the reader sees them without the prose repeating them.
- **Proof sketches are unchecked.** A checker could compare each sketch
  against the proof's actual dependencies.
- **`detail` is a global share.** A per-chapter budget, or a target outline
  length, may suit readers better.
- ~~Only two training projects~~. Done: `key_model_all.json` is trained on 9
  projects (above and [`cross_project.md`](cross_project.md)).
- ~~`[Fintype G]` hidden in short statements, boilerplate instances named as
  results~~. Done (see APAP above).
- ~~Structure fields as definitions~~. Done: projections are shown with their
  structure (above).
