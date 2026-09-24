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

## Chapter (Lean module `Carleson.ForestOperator.RemainingTiles`)

### `TileStructure.Forest.correlation_near_tree_parts` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf₁ : BoundedCompactSupport f₁ volume) (hf₂ : BoundedCompactSupport f₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁) f₁ x * (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) f₂ x)‖ₑ ≤ ↑(Forest.C7_4_6 a n) * eLpNorm (fun x => (↑(𝓘 u₁)).indicator (t.adjointBoundaryOperator u₁ f₁) x) 2 volume * eLpNorm (fun x => (↑(𝓘 u₁)).indicator (t.adjointBoundaryOperator u₂ f₂) x) 2 volume`
Docstring: Lemma 7.4.6
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.approxOnCube`: `(C : Set (Grid X)) (f : X → E') (x : X) : E'`
- `TileStructure.Forest.bound_for_tree_projection`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf : BoundedCompactSupport f volume) : eLpNorm (Forest.approxOnCube (t.𝓙₆ u₁) fun x => ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖…`
- `TileStructure.Forest.tree_projection_estimate`: `(hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_2_1 a) * eLpNorm (F…`
- `TileStructure.Forest.𝓙`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₆`: `(t : Forest X n) (u₁ : 𝔓 X) : Set (Grid X)`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `adjointCarlesonSum_adjoint`: `(hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (ℭ : Set (𝔓 X)) : ∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ℭ f x = ∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ℭ g…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.𝓙₆` (definition)
Lean: `(t : Forest X n) (u₁ : 𝔓 X) : Set (Grid X)`
Docstring: The definition `𝓙'` at the start of Section 7.6. We use a different notation to distinguish it from the 𝓙' used in Section 7.5

### `TileStructure.Forest.thin_scale_impact_prelims` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hJ : J ∈ t.𝓙₆ u₁) (hd : ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (8 * ↑(defaultD a) ^ s J))) (h : ↑(s J) - Forest.C7_6_3 a n < ↑(𝔰 p)) : dist (𝔠 p) (c J) < 16 * ↑(defaultD a) ^ (↑(𝔰 p) + Forest.C7_6_3 a n + 2) ∧ ∃ J', J < J' ∧ s J' = s J + 1 ∧ ∃ p ∈ (fun x => t.𝔗 x) u₁, ↑(𝓘 p) ⊆ Metric.ball (c J') (100 * ↑(defaultD a) ^ (s J' + 1))`
Docstring: Some preliminary relations for Lemma 7.6.3.
Proof uses:
- `Grid.succ`: `(i : Grid X) : Grid X`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.𝓙`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `FunctionDistances`, `FunctionDistances.coeΘ`, `FunctionDistances.metric`

### `TileStructure.Forest.thin_scale_impact_key` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hp : p ∈ (fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) (hJ : J ∈ t.𝓙₆ u₁) (hd : ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (8 * ↑(defaultD a) ^ s J))) (h : ↑(s J) - Forest.C7_6_3 a n < ↑(𝔰 p)) : 2 ^ (defaultZ a * (n + 1) - 1) < 2 ^ (↑a * (↑𝕔 * ↑a ^ 2 * (Forest.C7_6_3 a n + 2 + 1) + 9)) * 2 ^ (↑(defaultZ a) * ↑n / 2)`
Docstring: The key relation of Lemma 7.6.3, which will eventually be shown to lead to a contradiction.
Proof uses:
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.thin_scale_impact_prelims`: `(hu₁ : u₁ ∈ t) (hJ : J ∈ t.𝓙₆ u₁) (hd : ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (8 * ↑(defaultD a) ^ s J))) (h : ↑(s J) - Forest.C7_6_3 a n < ↑(𝔰 p)) : dist (𝔠 p) (…`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CompatibleFunctions.cdist_le`, `CompatibleFunctions.cdist_mono`, `CoveredByBalls`, `FunctionDistances`

### `TileStructure.Forest.e763` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf : BoundedCompactSupport f volume) : eLpNorm (Forest.approxOnCube (t.𝓙₆ u₁) fun x => ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) f x‖) 2 volume ≤ ∑ k ∈ Finset.Icc ⌊Forest.C7_6_3 a n⌋ (2 * ↑(defaultS X)), (∑ J ∈ (t.𝓙₆ u₁).toFinset, (volume ↑J)⁻¹ * (∫⁻ (y : X) in ↑J, ∑ p ∈ ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂).toFinset with ¬Disjoint (↑J) (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) ∧ 𝔰 p = s J - k, ‖adjointCarleson p f y‖ₑ) ^ 2) ^ 2⁻¹`
Docstring: Equation (7.6.3) of Lemma 7.6.2.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileStructure.Forest.thin_scale_impact_key`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hp : p ∈ (fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) (hJ : J ∈ t.𝓙₆ u₁) (hd : ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.b…`
- `TileStructure.Forest.𝓙`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.e764_preCS` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf : BoundedCompactSupport f volume) : eLpNorm (Forest.approxOnCube (t.𝓙₆ u₁) fun x => ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) f x‖) 2 volume ≤ ↑(C2_1_3 a) * 2 ^ (4 * a) * ∑ k ∈ Finset.Icc ⌊Forest.C7_6_3 a n⌋ (2 * ↑(defaultS X)), (∑ J ∈ (t.𝓙₆ u₁).toFinset, (volume ↑J)⁻¹ * (∑ I with s I = s J - k ∧ Disjoint ↑I ↑(𝓘 u₁) ∧ ¬Disjoint (↑J) (Metric.ball (c I) (8 * ↑(defaultD a) ^ s I)), ∫⁻ (y : X) in ↑J, (Metric.ball (c I) (8 * ↑(defaultD a) ^ s I)).indicator 1 y * maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f…`
Docstring: Equation (7.6.4) of Lemma 7.6.2 (before applying Cauchy–Schwarz).
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileStructure.Forest.e763`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf : BoundedCompactSupport f volume) : eLpNorm (Forest.approxOnCube (t.𝓙₆ u₁) fun x => ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖…`
- `TileStructure.Forest.overlap_implies_distance`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hp : p ∈ (fun x => t.𝔗 x) u₁ ∪ (fun x => t.𝔗 x) u₂) (hpu₁ : ¬Disjoint ↑(𝓘 p) ↑(𝓘 u₁)) : p ∈ t.𝔖₀ u₁ u₂`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.e764_postCS` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf : BoundedCompactSupport f volume) : eLpNorm (Forest.approxOnCube (t.𝓙₆ u₁) fun x => ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) f x‖) 2 volume ≤ (↑(C2_1_3 a) * 2 ^ (11 * a + 2) * ∑ k ∈ Finset.Icc ⌊Forest.C7_6_3 a n⌋ (2 * ↑(defaultS X)), ↑(defaultD a) ^ (-↑k * defaultκ a / 2)) * eLpNorm ((↑(𝓘 u₁)).indicator fun x => maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f x) 2 volume`
Docstring: Equation (7.6.4) of Lemma 7.6.2 (after applying Cauchy–Schwarz and simplification).
Proof uses:
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.e764_preCS`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf : BoundedCompactSupport f volume) : eLpNorm (Forest.approxOnCube (t.𝓙₆ u₁) fun x => ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖…`
- `TileStructure.Forest.𝓙`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.bound_for_tree_projection` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf : BoundedCompactSupport f volume) : eLpNorm (Forest.approxOnCube (t.𝓙₆ u₁) fun x => ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) f x‖) 2 volume ≤ ↑(Forest.C7_6_2 a n) * eLpNorm ((↑(𝓘 u₁)).indicator fun x => maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f x) 2 volume`
Docstring: Lemma 7.6.2.
Proof uses:
- `TileStructure.Forest.e764_postCS`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf : BoundedCompactSupport f volume) : eLpNorm (Forest.approxOnCube (t.𝓙₆ u₁) fun x => ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_1_3`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `FunctionDistances`, `FunctionDistances.coeΘ`
