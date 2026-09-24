You are writing the text of a mathematical outline generated from a verified Lean formalisation.
Below are the results of one chapter, in the order the outline presents them. For each you get its Lean name, its
statement in Lean (only explicit hypotheses are shown; implicit and type-class assumptions are omitted), its
docstring if there is one, and, for theorems, the named results its proof uses (with their statements) and the
helper lemmas folded into the proof.

Write:
1. `title`: a short chapter title (at most 8 words), as a mathematician would name this material.
2. For every result, `statement`: the statement in clear mathematical English, using LaTeX between $...$ for
   formulas. Be faithful: keep every hypothesis and the exact conclusion; do not add, drop, strengthen or weaken
   anything. If some notation's meaning is unclear, keep the notation rather than guessing. For a definition, say
   what is being defined.
3. For every theorem, `sketch`: one or two sentences on how the proof goes, based only on the listed results it
   uses and their statements. Do not invent steps; if the structure is not clear, just say which results it
   combines.

Reply with only a JSON object:
{"title": "...", "results": {"<lean name>": {"statement": "...", "sketch": "..."}}}
(omit "sketch" for definitions). Use every Lean name exactly as given.

Namespaces open (prefixes omitted): TileStructure, MeasureTheory, Antichain.

## Chapter (Lean module `Carleson.TwoSidedCarleson.NontangentialOperator`)

### `nontangential_from_simple` (theorem)
Lean: `(ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) : HasBoundedStrongType (nontangentialOperator K) 2 2 volume volume ↑(C10_0_2 a)`
Docstring: Lemma 10.0.2. The formal statement includes the measurability of the operator.
Proof uses:
- `simple_nontangential_operator_le`: `(ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hr : 0 ≤ r) : HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `cotlar_estimate` (theorem)
Lean: `(ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hg : BoundedFiniteSupport g volume) (hr : r ∈ Set.Ioc 0 R) : ‖czOperator K R g x‖ₑ ≤ 4 * globalMaximalFunction volume 1 (czOperator K r g) x + ↑(C10_1_5 a) * globalMaximalFunction volume 1 g x`
Docstring: Lemma 10.1.5
Proof uses:
- `cotlar_set_F₂`: `(ha : 4 ≤ a) (hr : 0 < r) (hR : r ≤ R) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hg : BoundedFiniteSupport g volume) : (volume.restrict (Metric.ball x (R / 4)…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `cotlar_set_F₂` (theorem)
Lean: `(ha : 4 ≤ a) (hr : 0 < r) (hR : r ≤ R) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hg : BoundedFiniteSupport g volume) : (volume.restrict (Metric.ball x (R / 4))) {x' | ↑(C10_1_4 a) * globalMaximalFunction volume 1 g x < ‖czOperator K r ((Metric.ball x (R / 2)).indicator g) x'‖ₑ} ≤ volume (Metric.ball x (R / 4)) / 4`
Docstring: Part 2 of Lemma 10.1.4 about `F₂`.
Proof uses:
- `estimate_czOperator`: `(ha : 4 ≤ a) (hr : 0 < r) (hf : BoundedFiniteSupport f volume) (hT : HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) : distribution (czOperator K r f) α volume ≤ ↑(C10_0_3 a) / α *…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `simple_nontangential_operator` (theorem)
Lean: `(ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hr : 0 < r) : HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
Docstring: Lemma 10.1.6. The formal statement includes the measurability of the operator. See also `simple_nontangential_operator_le`
Proof uses:
- `cotlar_estimate`: `(ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hg : BoundedFiniteSupport g volume) (hr : r ∈ Set.Ioc 0 R) : ‖czOperator K R g x‖ₑ ≤ 4 * globalMaximalF…`
- `hasStrongType_maximalFunction`: `(hp₁ : 0 < p₁) (hp₁₂ : p₁ < p₂) : HasStrongType (maximalFunction μ 𝓑 c r ↑p₁) (↑p₂) (↑p₂) μ μ ↑(C2_0_6 A p₁ p₂)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `simple_nontangential_operator_le` (theorem)
Lean: `(ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hr : 0 ≤ r) : HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
Docstring: This is the first step of the proof of Lemma 10.0.2, and should follow from 10.1.6 + monotone convergence theorem. (measurability should be proven without any restriction on `r`.)
Proof uses:
- `simple_nontangential_operator`: `(ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hr : 0 < r) : HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
Helper lemmas folded into the proof: `BoundedFiniteSupport`, `C10_1_6`, `C_K`, `C_Ts`, `IsOneSidedKernel`, `IsTwoSidedKernel`, `MeasureTheory.DoublingMeasure`, `MeasureTheory.DoublingMeasure.toBorelSpace`
