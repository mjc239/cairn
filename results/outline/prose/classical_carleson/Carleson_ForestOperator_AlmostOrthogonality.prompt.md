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

## Chapter (Lean module `Carleson.ForestOperator.AlmostOrthogonality`)

### `TileStructure.Forest.indicator_adjoint_tree_estimate` (theorem)
Lean: `(hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : eLpNorm (F.indicator (adjointCarlesonSum ((fun x => t.𝔗 x) u) g)) 2 volume ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * dens₂ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm g 2 volume`
Docstring: Part 2 of Lemma 7.4.2.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileStructure.Forest.adjoint_density_tree_bound2`: `(hf : BoundedCompactSupport f volume) (h2f : Function.support f ⊆ F) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSu…`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.𝔖₀` (definition)
Lean: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) : Set (𝔓 X)`
Docstring: The set `𝔖` defined in the proof of Lemma 7.4.4. We append a subscript 0 to distinguish it from the section variable.

### `TileStructure.Forest.overlap_implies_distance` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hp : p ∈ (fun x => t.𝔗 x) u₁ ∪ (fun x => t.𝔗 x) u₂) (hpu₁ : ¬Disjoint ↑(𝓘 p) ↑(𝓘 u₁)) : p ∈ t.𝔖₀ u₁ u₂`
Docstring: Part 1 of Lemma 7.4.7.
Proof uses:
- `Grid.dist_strictMono`: `(hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_1_2`, `C2_1_2_le_inv_256`, `C2_1_2_le_one`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`

### `TileStructure.Forest.adjoint_tree_control` (theorem)
Lean: `(hu : u ∈ t) (hf : BoundedCompactSupport f volume) (h2f : Function.support f ⊆ G) : eLpNorm (fun x => t.adjointBoundaryOperator u f x) 2 volume ≤ ↑(Forest.C7_4_3 a) * eLpNorm f 2 volume`
Docstring: Lemma 7.4.3.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `E₂`: `(l : ℝ) (p : 𝔓 X) : Set X`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.adjoint_tree_estimate`: `(hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : eLpNorm (adjointCarlesonSum ((fun x => t.𝔗 x) u) g) 2 volume ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ …`
- `TileStructure.Forest.𝔖₀`: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) : Set (𝔓 X)`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `dens₁`: `(𝔓' : Set (𝔓 X)) : ENNReal`
- `hasStrongType_maximalFunction_one`: `(hp : 1 < p) : HasStrongType (maximalFunction μ 𝓑 c r 1) (↑p) (↑p) μ μ ↑(CMB A p)`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.adjoint_density_tree_bound2` (theorem)
Lean: `(hf : BoundedCompactSupport f volume) (h2f : Function.support f ⊆ F) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) * f x‖ₑ ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * dens₂ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Proof uses:
- `TileStructure.Forest.density_tree_bound2`: `(hf : BoundedCompactSupport f volume) (h2f : Function.support f ⊆ F) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSu…`
- `adjointCarlesonSum_adjoint`: `(hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (ℭ : Set (𝔓 X)) : ∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ℭ f x = ∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ℭ g…`
- `carlesonSum`: `(ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `FunctionDistances`, `FunctionDistances.coeΘ`, `FunctionDistances.metric`

### `TileStructure.Forest.adjoint_density_tree_bound1` (theorem)
Lean: `(hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) * f x‖ₑ ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Proof uses:
- `TileStructure.Forest.density_tree_bound1`: `(hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ …`
- `adjointCarlesonSum_adjoint`: `(hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (ℭ : Set (𝔓 X)) : ∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ℭ f x = ∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ℭ g…`
- `carlesonSum`: `(ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `FunctionDistances`, `FunctionDistances.coeΘ`, `FunctionDistances.metric`

### `TileStructure.Forest.adjoint_tree_estimate` (theorem)
Lean: `(hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : eLpNorm (adjointCarlesonSum ((fun x => t.𝔗 x) u) g) 2 volume ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm g 2 volume`
Docstring: Part 1 of Lemma 7.4.2.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileStructure.Forest.adjoint_density_tree_bound1`: `(hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) * f…`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`
