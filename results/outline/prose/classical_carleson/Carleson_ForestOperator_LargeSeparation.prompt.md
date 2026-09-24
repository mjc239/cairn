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

## Chapter (Lean module `Carleson.ForestOperator.LargeSeparation`)

### `TileStructure.Forest.correlation_distant_tree_parts` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf₁ : BoundedCompactSupport f₁ volume) (hf₂ : BoundedCompactSupport f₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁) f₁ x * (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u₂ ∩ t.𝔖₀ u₁ u₂) f₂ x)‖ₑ ≤ ↑(Forest.C7_4_5 a n) * eLpNorm (fun x => (↑(𝓘 u₁)).indicator (t.adjointBoundaryOperator u₁ f₁) x) 2 volume * eLpNorm (fun x => (↑(𝓘 u₁)).indicator (t.adjointBoundaryOperator u₂ f₂) x) 2 volume`
Docstring: Lemma 7.4.5
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileStructure.Forest.cdtp_le_iHolENorm`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf₁ : BoundedCompactSupport f₁ volume) (hf₂ : BoundedCompactSupport f₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁)…`
- `TileStructure.Forest.holderFunction`: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) (f₁ : X → ℂ) (f₂ : X → ℂ) (J : Grid X) (x : X) : ℂ`
- `TileStructure.Forest.holder_correlation_tree`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf₁ : BoundedCompactSupport f₁ volume) (hf₂ : BoundedCompactSupport f₂ volume) : iHolENorm (t.holderFunction u₁…`
- `TileStructure.Forest.lower_oscillation_bound`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) : ↑(Forest.C7_5_11 a n) ≤ dist_{c J, 8 * ↑(defaultD a) ^ s J} (𝒬 u₁) (𝒬 u₂)`
- `TileStructure.Forest.union_𝓙₅`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) : ⋃ J ∈ t.𝓙₅ u₁ u₂, ↑J = ↑(𝓘 u₁)`
- `TileStructure.Forest.χtilde`: `(J : Grid X) (u₁ : 𝔓 X) (_ : X) : NNReal`
- `TileStructure.Forest.𝓙`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₅`: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) : Set (Grid X)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.χtilde` (definition)
Lean: `(J : Grid X) (u₁ : 𝔓 X) (_ : X) : NNReal`
Docstring: The definition of χ-tilde, defined in the proof of Lemma 7.5.2

### `TileStructure.Forest.𝓙₅` (definition)
Lean: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) : Set (Grid X)`
Docstring: The definition `𝓙'` at the start of Section 7.5.1. We use a different notation to distinguish it from the 𝓙' used in Section 7.6

### `TileStructure.Forest.χ` (definition)
Lean: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) (J : Grid X) (x : X) : NNReal`
Docstring: The definition of χ, defined in the proof of Lemma 7.5.2

### `TileStructure.Forest.holderFunction` (definition)
Lean: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) (f₁ : X → ℂ) (f₂ : X → ℂ) (J : Grid X) (x : X) : ℂ`
Docstring: The definition of h_J, defined in the proof of Section 7.5.2

### `TileStructure.Forest.edist_holderFunction_le` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf₁ : BoundedCompactSupport f₁ volume) (hf₂ : BoundedCompactSupport f₂ volume) (mx : x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) (mx' : x' ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) : edist (t.holderFunction u₁ u₂ f₁ f₂ J x) (t.holderFunction u₁ u₂ f₁ f₂ J x') ≤ ↑(Forest.I7_5_4 a) * t.P7_5_4 u₁ u₂ f₁ f₂ J * (edist x x' / ↑(defaultD a) ^ s J) ^ (↑a)⁻¹`
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.global_tree_control1_edist_left`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSupport f volume) (hx : x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) (hx' : x' ∈ Metric…`
- `TileStructure.Forest.global_tree_control1_edist_right`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSupport f volume) (hx : x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) (hx' : x' ∈ Metric…`
- `TileStructure.Forest.global_tree_control1_supbound`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (ℭ : Set (𝔓 X)) (hℭ : ℭ = (fun x => t.𝔗 x) u₁ ∨ ℭ = (fun x => t.𝔗 x) u₂ ∩ t.𝔖₀ u₁ u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSuppor…`
- `TileStructure.Forest.global_tree_control2`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSupport f volume) : ⨆ x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J), ‖adjointCarlesonSum …`
- `TileStructure.Forest.union_𝓙₅`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) : ⋃ J ∈ t.𝓙₅ u₁ u₂, ↑J = ↑(𝓘 u₁)`
- `TileStructure.Forest.χ`: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) (J : Grid X) (x : X) : NNReal`
- `TileStructure.Forest.𝓙`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.holder_correlation_tile_two` (theorem)
Lean: `(hu : u ∈ t) (hp : p ∈ (fun x => t.𝔗 x) u) (hf : BoundedCompactSupport f volume) (hx : x ∈ Metric.ball (𝔠 p) (5 * ↑(defaultD a) ^ 𝔰 p)) (hx' : x' ∈ Metric.ball (𝔠 p) (5 * ↑(defaultD a) ^ 𝔰 p)) : edist (Complex.exp (Complex.I * ↑((𝒬 u) x)) * adjointCarleson p f x) (Complex.exp (Complex.I * ↑((𝒬 u) x')) * adjointCarleson p f x') ≤ ↑(Forest.C7_5_5 a) / volume (Metric.ball (𝔠 p) (4 * ↑(defaultD a) ^ 𝔰 p)) * (edist x x' / ↑(defaultD a) ^ 𝔰 p) ^ (↑a)⁻¹ * ∫⁻ (x : X) in E p, ‖f x‖ₑ`
Proof uses:
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.holder_correlation_tile` (theorem)
Lean: `(hu : u ∈ t) (hp : p ∈ (fun x => t.𝔗 x) u) (hf : BoundedCompactSupport f volume) : edist (Complex.exp (Complex.I * ↑((𝒬 u) x)) * adjointCarleson p f x) (Complex.exp (Complex.I * ↑((𝒬 u) x')) * adjointCarleson p f x') ≤ ↑(Forest.C7_5_5 a) / volume (Metric.ball (𝔠 p) (4 * ↑(defaultD a) ^ 𝔰 p)) * (edist x x' / ↑(defaultD a) ^ 𝔰 p) ^ (↑a)⁻¹ * ∫⁻ (x : X) in E p, ‖f x‖ₑ`
Docstring: Lemma 7.5.5.
Proof uses:
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileStructure.Forest.holder_correlation_tile_two`: `(hu : u ∈ t) (hp : p ∈ (fun x => t.𝔗 x) u) (hf : BoundedCompactSupport f volume) (hx : x ∈ Metric.ball (𝔠 p) (5 * ↑(defaultD a) ^ 𝔰 p)) (hx' : x' ∈ Metric.ball (𝔠 p) (5 * ↑(defaultD a) ^ 𝔰 p)) : edis…`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.global_tree_control1_edist_part1` (theorem)
Lean: `(hu : u ∈ t) (hℭ : ℭ ⊆ (fun x => t.𝔗 x) u) (hf : BoundedCompactSupport f volume) (hs : ∀ p ∈ ℭ, ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) → s J ≤ 𝔰 p) (hx : x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) (hx' : x' ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) : edist (Complex.exp (Complex.I * ↑((𝒬 u) x)) * adjointCarlesonSum ℭ f x) (Complex.exp (Complex.I * ↑((𝒬 u) x')) * adjointCarlesonSum ℭ f x') ≤ ↑(Forest.C7_5_5 a) * 2 ^ (4 * a) * edist x x' ^ (↑a)⁻¹ * ∑ k ∈ Finset.Icc (s J) ↑(defaultS X), ↑(defaultD a) ^ (-↑k / ↑a) * ⨍⁻ (x…`
Docstring: Part 1 of equation (7.5.18) of Lemma 7.5.9.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileStructure.Forest.holder_correlation_tile`: `(hu : u ∈ t) (hp : p ∈ (fun x => t.𝔗 x) u) (hf : BoundedCompactSupport f volume) : edist (Complex.exp (Complex.I * ↑((𝒬 u) x)) * adjointCarleson p f x) (Complex.exp (Complex.I * ↑((𝒬 u) x')) * adjoin…`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `As`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `D2`, `ENNReal.edist_sum_le_sum_edist`

### `TileStructure.Forest.global_tree_control1_edist_part2` (theorem)
Lean: `(hu : u ∈ t) (hℭ : ℭ ⊆ (fun x => t.𝔗 x) u) (hf : BoundedCompactSupport f volume) (hs : ∀ p ∈ ℭ, ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) → s J ≤ 𝔰 p) (hx : x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) (hx' : x' ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) : edist (Complex.exp (Complex.I * ↑((𝒬 u) x)) * adjointCarlesonSum ℭ f x) (Complex.exp (Complex.I * ↑((𝒬 u) x')) * adjointCarlesonSum ℭ f x') ≤ ↑(Forest.C7_5_9d a) * (edist x x' / ↑(defaultD a) ^ s J) ^ (↑a)⁻¹ * ⨅ x ∈ J, maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 …`
Docstring: Part 2 of equation (7.5.18) of Lemma 7.5.9.
Proof uses:
- `TileStructure.Forest.global_tree_control1_edist_part1`: `(hu : u ∈ t) (hℭ : ℭ ⊆ (fun x => t.𝔗 x) u) (hf : BoundedCompactSupport f volume) (hs : ∀ p ∈ ℭ, ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) …`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `ENNReal.rpow_le_rpow_of_nonpos`, `ENNReal.sum_geometric_two_pow_neg_one`, `ENNReal.sum_geometric_two_pow_toNNReal`

### `TileStructure.Forest.scales_impacting_interval` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hp : p ∈ (fun x => t.𝔗 x) u₁ ∪ (fun x => t.𝔗 x) u₂ ∩ t.𝔖₀ u₁ u₂) (h : ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (16 * ↑(defaultD a) ^ s J))) : s J ≤ 𝔰 p`
Docstring: Lemma 7.5.8.
Proof uses:
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.overlap_implies_distance`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hp : p ∈ (fun x => t.𝔗 x) u₁ ∪ (fun x => t.𝔗 x) u₂) (hpu₁ : ¬Disjoint ↑(𝓘 p) ↑(𝓘 u₁)) : p ∈ t.𝔖₀ u₁ u₂`
- `TileStructure.Forest.𝓙`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `FunctionDistances`, `FunctionDistances.coeΘ`, `FunctionDistances.metric`

### `TileStructure.Forest.global_tree_control1_edist_right` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSupport f volume) (hx : x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) (hx' : x' ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) : edist (Complex.exp (Complex.I * ↑((𝒬 u₂) x)) * adjointCarlesonSum ((fun x => t.𝔗 x) u₂ ∩ t.𝔖₀ u₁ u₂) f x) (Complex.exp (Complex.I * ↑((𝒬 u₂) x')) * adjointCarlesonSum ((fun x => t.𝔗 x) u₂ ∩ t.𝔖₀ u₁ u₂) f x') ≤ ↑(Forest.C7_5_9d a) * (edist x x' / ↑(defaultD a) ^ s J) ^ (↑a)⁻¹ * ⨅ x ∈ J, maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f x`
Docstring: Equation (7.5.18) of Lemma 7.5.9 for `ℭ = t u₂ ∩ 𝔖₀ t u₁ u₂`.
Proof uses:
- `TileStructure.Forest.global_tree_control1_edist_part2`: `(hu : u ∈ t) (hℭ : ℭ ⊆ (fun x => t.𝔗 x) u) (hf : BoundedCompactSupport f volume) (hs : ∀ p ∈ ℭ, ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) …`
- `TileStructure.Forest.scales_impacting_interval`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hp : p ∈ (fun x => t.𝔗 x) u₁ ∪ (fun x => t.𝔗 x) u₂ ∩ t.𝔖₀ u₁ u₂) (h : ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defau…`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `FunctionDistances`, `FunctionDistances.coeΘ`, `FunctionDistances.coeΘ_injective`

### `TileStructure.Forest.global_tree_control1_edist_left` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSupport f volume) (hx : x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) (hx' : x' ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) : edist (Complex.exp (Complex.I * ↑((𝒬 u₁) x)) * adjointCarlesonSum ((fun x => t.𝔗 x) u₁) f x) (Complex.exp (Complex.I * ↑((𝒬 u₁) x')) * adjointCarlesonSum ((fun x => t.𝔗 x) u₁) f x') ≤ ↑(Forest.C7_5_9d a) * (edist x x' / ↑(defaultD a) ^ s J) ^ (↑a)⁻¹ * ⨅ x ∈ J, maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f x`
Docstring: Equation (7.5.18) of Lemma 7.5.9 for `ℭ = t u₁`.
Proof uses:
- `TileStructure.Forest.global_tree_control1_edist_part2`: `(hu : u ∈ t) (hℭ : ℭ ⊆ (fun x => t.𝔗 x) u) (hf : BoundedCompactSupport f volume) (hs : ∀ p ∈ ℭ, ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) …`
- `TileStructure.Forest.scales_impacting_interval`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hp : p ∈ (fun x => t.𝔗 x) u₁ ∪ (fun x => t.𝔗 x) u₂ ∩ t.𝔖₀ u₁ u₂) (h : ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defau…`
- `TileStructure.Forest.𝔖₀`: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) : Set (𝔓 X)`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `FunctionDistances`, `FunctionDistances.coeΘ`, `FunctionDistances.coeΘ_injective`

### `TileStructure.Forest.global_tree_control1_supbound` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (ℭ : Set (𝔓 X)) (hℭ : ℭ = (fun x => t.𝔗 x) u₁ ∨ ℭ = (fun x => t.𝔗 x) u₂ ∩ t.𝔖₀ u₁ u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSupport f volume) : ⨆ x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J), ‖adjointCarlesonSum ℭ f x‖ₑ ≤ (⨅ x ∈ Metric.ball (c J) (8⁻¹ * ↑(defaultD a) ^ s J), ‖adjointCarlesonSum ℭ f x‖ₑ) + ↑(Forest.C7_5_9s a) * ⨅ x ∈ J, maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f x`
Docstring: Equation (7.5.17) of Lemma 7.5.9.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileStructure.Forest.global_tree_control1_edist_left`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSupport f volume) (hx : x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) (hx' : x' ∈ Metric…`
- `TileStructure.Forest.global_tree_control1_edist_right`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSupport f volume) (hx : x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) (hx' : x' ∈ Metric…`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.limited_scale_impact_second_estimate` (theorem)
Lean: `(hp : p ∈ (fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (h : ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (8⁻¹ * ↑(defaultD a) ^ s J))) : 𝔰 p ≤ s J + 3`
Docstring: Part of Lemma 7.5.6.
Proof uses:
- `Grid.succ`: `(i : Grid X) : Grid X`
- `TileStructure.Forest.𝓙`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CompatibleFunctions.cdist_le`, `CompatibleFunctions.cdist_mono`, `CompatibleFunctions.le_cdist`, `CoveredByBalls`

### `TileStructure.Forest.local_tree_control_sumsumsup` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) : ⨆ x ∈ Metric.ball (c J) (8⁻¹ * ↑(defaultD a) ^ s J), ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) f x‖ₑ ≤ ∑ k ∈ Finset.Icc (s J) (s J + 3), ∑ p with 𝔰 p = k ∧ ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (8⁻¹ * ↑(defaultD a) ^ s J)), ⨆ x ∈ Metric.ball (c J) (8⁻¹ * ↑(defaultD a) ^ s J), ‖adjointCarleson p f x‖ₑ`
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileStructure.Forest.limited_scale_impact_second_estimate`: `(hp : p ∈ (fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (h : ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (8⁻¹ * ↑(defaultD a) ^ s J))) : 𝔰 p ≤ s J + 3`
- `TileStructure.Forest.overlap_implies_distance`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hp : p ∈ (fun x => t.𝔗 x) u₁ ∪ (fun x => t.𝔗 x) u₂) (hpu₁ : ¬Disjoint ↑(𝓘 p) ↑(𝓘 u₁)) : p ∈ t.𝔖₀ u₁ u₂`
- `TileStructure.Forest.𝓙`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `D2`, `ENNReal.biSup_add_le_add_biSup`, `ENNReal.biSup_finsetSum_le_finsetSum_biSup`

### `TileStructure.Forest.local_tree_control` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSupport f volume) : ⨆ x ∈ Metric.ball (c J) (8⁻¹ * ↑(defaultD a) ^ s J), ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) f x‖ₑ ≤ ↑(Forest.C7_5_7 a) * ⨅ x ∈ J, maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f x`
Docstring: Lemma 7.5.7.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileStructure.Forest.local_tree_control_sumsumsup`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) : ⨆ x ∈ Metric.ball (c J) (8⁻¹ * ↑(defaultD a) ^ s J), ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) f …`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.global_tree_control2` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSupport f volume) : ⨆ x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J), ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ ∩ t.𝔖₀ u₁ u₂) f x‖ₑ ≤ (⨅ x ∈ Metric.ball (c J) (8⁻¹ * ↑(defaultD a) ^ s J), ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂) f x‖ₑ) + ↑(Forest.C7_5_10 a) * ⨅ x ∈ J, maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f x`
Docstring: Lemma 7.5.10
Proof uses:
- `TileStructure.Forest.global_tree_control1_supbound`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (ℭ : Set (𝔓 X)) (hℭ : ℭ = (fun x => t.𝔗 x) u₁ ∨ ℭ = (fun x => t.𝔗 x) u₂ ∩ t.𝔖₀ u₁ u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSuppor…`
- `TileStructure.Forest.local_tree_control`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSupport f volume) : ⨆ x ∈ Metric.ball (c J) (8⁻¹ * ↑(defaultD a) ^ s J), ‖adjointCarlesonSum…`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `ENNReal.biInf_enorm_sub_le`, `ENNReal.exists_enorm_sub_eps_le_biInf`, `FunctionDistances`

### `TileStructure.Forest.union_𝓙₅` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) : ⋃ J ∈ t.𝓙₅ u₁ u₂, ↑J = ↑(𝓘 u₁)`
Docstring: Part of Lemma 7.5.1.
Proof uses:
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.overlap_implies_distance`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hp : p ∈ (fun x => t.𝔗 x) u₁ ∪ (fun x => t.𝔗 x) u₂) (hpu₁ : ¬Disjoint ↑(𝓘 p) ↑(𝓘 u₁)) : p ∈ t.𝔖₀ u₁ u₂`
- `TileStructure.Forest.𝓙`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝔖₀`: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) : Set (𝔓 X)`
- `TileStructure.Forest.𝔗`: `(self : Forest X n) (_ : 𝔓 X) : Set (𝔓 X)`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `FunctionDistances`, `FunctionDistances.coeΘ`, `FunctionDistances.metric`

### `TileStructure.Forest.enorm_holderFunction_le` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf₁ : BoundedCompactSupport f₁ volume) (hf₂ : BoundedCompactSupport f₂ volume) (mx : x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J)) : ‖t.holderFunction u₁ u₂ f₁ f₂ J x‖ₑ ≤ ↑(Forest.C7_5_9s a) * ↑(Forest.C7_5_10 a) * t.P7_5_4 u₁ u₂ f₁ f₂ J`
Proof uses:
- `TileStructure.Forest.global_tree_control1_supbound`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (ℭ : Set (𝔓 X)) (hℭ : ℭ = (fun x => t.𝔗 x) u₁ ∨ ℭ = (fun x => t.𝔗 x) u₂ ∩ t.𝔖₀ u₁ u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSuppor…`
- `TileStructure.Forest.global_tree_control2`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf : BoundedCompactSupport f volume) : ⨆ x ∈ Metric.ball (c J) (16 * ↑(defaultD a) ^ s J), ‖adjointCarlesonSum …`
- `TileStructure.Forest.χ`: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) (J : Grid X) (x : X) : NNReal`
- `TileStructure.Forest.𝔖₀`: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) : Set (𝔓 X)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `FunctionDistances`, `FunctionDistances.coeΘ`, `FunctionDistances.coeΘ_injective`

### `TileStructure.Forest.holder_correlation_tree` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf₁ : BoundedCompactSupport f₁ volume) (hf₂ : BoundedCompactSupport f₂ volume) : iHolENorm (t.holderFunction u₁ u₂ f₁ f₂ J) (c J) (16 * ↑(defaultD a) ^ s J) (defaultτ a) ≤ ↑(Forest.C7_5_4 a) * t.P7_5_4 u₁ u₂ f₁ f₂ J`
Docstring: Lemma 7.5.4.
Proof uses:
- `TileStructure.Forest.edist_holderFunction_le`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf₁ : BoundedCompactSupport f₁ volume) (hf₂ : BoundedCompactSupport f₂ volume) (mx : x ∈ Metric.ball (c J) (16 …`
- `TileStructure.Forest.enorm_holderFunction_le`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) (hf₁ : BoundedCompactSupport f₁ volume) (hf₂ : BoundedCompactSupport f₂ volume) (mx : x ∈ Metric.ball (c J) (16 …`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `FunctionDistances`, `FunctionDistances.coeΘ`, `FunctionDistances.metric`

### `TileStructure.Forest.cdtp_le_iHolENorm` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf₁ : BoundedCompactSupport f₁ volume) (hf₂ : BoundedCompactSupport f₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁) f₁ x * (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u₂ ∩ t.𝔖₀ u₁ u₂) f₂ x)‖ₑ ≤ ∑ J ∈ (t.𝓙₅ u₁ u₂).toFinset, ↑(C2_0_5 ↑a) * volume (Metric.ball (c J) (8 * ↑(defaultD a) ^ s J)) * iHolENorm (t.holderFunction u₁ u₂ f₁ f₂ J) (c J) (2 * (8 * ↑(defaultD a) ^ s J)) (defaultτ a) * (1 + edist_{c J, 8 * ↑(defaultD a) ^ s J} (𝒬 u₂) (𝒬 u₁)) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹)`
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.union_𝓙₅`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) : ⋃ J ∈ t.𝓙₅ u₁ u₂, ↑J = ↑(𝓘 u₁)`
- `TileStructure.Forest.χ`: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) (J : Grid X) (x : X) : NNReal`
- `TileStructure.Forest.χtilde`: `(J : Grid X) (u₁ : 𝔓 X) (_ : X) : NNReal`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `holder_van_der_corput`: `(φ_supp : Function.support φ ⊆ Metric.ball z R) : ‖∫ (x : X), Complex.exp (Complex.I * (↑(f x) - ↑(g x))) * φ x‖ₑ ≤ ↑(C2_0_5 ↑a) * volume (Metric.ball z R) * iHolENorm φ z (2 * R) (defaultτ a) * (1 +…`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.lower_oscillation_bound` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hJ : J ∈ t.𝓙₅ u₁ u₂) : ↑(Forest.C7_5_11 a n) ≤ dist_{c J, 8 * ↑(defaultD a) ^ s J} (𝒬 u₁) (𝒬 u₂)`
Docstring: Lemma 7.5.11
Proof uses:
- `Grid.succ`: `(i : Grid X) : Grid X`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.overlap_implies_distance`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hp : p ∈ (fun x => t.𝔗 x) u₁ ∪ (fun x => t.𝔗 x) u₂) (hpu₁ : ¬Disjoint ↑(𝓘 p) ↑(𝓘 u₁)) : p ∈ t.𝔖₀ u₁ u₂`
- `TileStructure.Forest.𝓙`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝔖₀`: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) : Set (𝔓 X)`
- `TileStructure.Forest.𝔗`: `(self : Forest X n) (_ : 𝔓 X) : Set (𝔓 X)`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CompatibleFunctions.cdist_le`, `CompatibleFunctions.cdist_mono`, `CoveredByBalls`, `FunctionDistances`
