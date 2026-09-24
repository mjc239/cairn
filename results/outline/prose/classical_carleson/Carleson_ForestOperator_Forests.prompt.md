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

## Chapter (Lean module `Carleson.ForestOperator.Forests`)

### `forest_operator_le_volume` (theorem)
Lean: `(𝔉 : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hA : MeasurableSet A) (sA : A ⊆ G) : ∫⁻ (x : X) in A, ‖∑ u with u ∈ 𝔉, carlesonSum ((fun x => 𝔉.𝔗 x) u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * dens₂ (⋃ u ∈ 𝔉, (fun x => 𝔉.𝔗 x) u) ^ (q⁻¹ - 2⁻¹) * volume F ^ (1 / 2) * volume A ^ (1 / 2)`
Docstring: Version of the forest operator theorem, but controlling the integral of the norm instead of the integral of the function multiplied by another function, and with the upper bound in terms of `volume F` and `volume G`.
Proof uses:
- `forest_operator'`: `(𝔉 : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hA : MeasurableSet A) (sA : A ⊆ G) : ∫⁻ (x : X) in A, ‖∑ u with u ∈ 𝔉, carlesonSum ((fun x => 𝔉.𝔗 x) u) f x‖ₑ ≤ ↑(C2_0…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_0_4`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `FunctionDistances`, `FunctionDistances.coeΘ`

### `TileStructure.Forest.forest_operator_f` (theorem)
Lean: `(t : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * ∑ u with u ∈ t, carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C2_0_4_aux a) * dens₂ (⋃ u ∈ t, (fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Docstring: The `f` side of Proposition 2.0.4.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `Grid.dist_strictMono`: `(hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.forest_operator_f_inner`: `(hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : eLpNorm (G.indicator (t.carlesonRowSum j f)) 2 volume ≤ ↑(Forest.C7_7_2_2 a n) * dens₂ (⋃ u ∈ t, (fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f…`
- `TileStructure.Forest.rowDecomp`: `(t : Forest X n) (j : ℕ) : Row X n`
- `TileStructure.Forest.rowDecomp_𝔘`: `(t : Forest X n) (j : ℕ) : Set (𝔓 X)`
- `TileStructure.Row`: `(X : Type u_1) (n : ℕ) : Type u_1`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.rowDecomp_𝔘` (definition)
Lean: `(t : Forest X n) (j : ℕ) : Set (𝔓 X)`

### `TileStructure.Forest.rowDecomp` (definition)
Lean: `(t : Forest X n) (j : ℕ) : Row X n`
Docstring: The row-decomposition of a tree, defined in the proof of Lemma 7.7.1. The indexing is off-by-one compared to the blueprint.

### `TileStructure.Forest.indicator_row_bound` (theorem)
Lean: `(hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) : eLpNorm (F.indicator (t.adjointCarlesonRowSum j g)) 2 volume ≤ ↑(Forest.C7_7_2_2 a n) * dens₂ (⋃ u ∈ t, (fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm g 2 volume`
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.indicator_adjoint_tree_estimate`: `(hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : eLpNorm (F.indicator (adjointCarlesonSum ((fun x => t.𝔗 x) u) g)) 2 volume ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x =…`
- `TileStructure.Forest.rowDecomp`: `(t : Forest X n) (j : ℕ) : Row X n`
- `TileStructure.Forest.rowDecomp_𝔘`: `(t : Forest X n) (j : ℕ) : Set (𝔓 X)`
- `TileStructure.Row`: `(X : Type u_1) (n : ℕ) : Type u_1`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `adjointCarlesonSum`: `(ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
- `dens₁`: `(𝔓' : Set (𝔓 X)) : ENNReal`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.forest_operator_f_inner` (theorem)
Lean: `(hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : eLpNorm (G.indicator (t.carlesonRowSum j f)) 2 volume ≤ ↑(Forest.C7_7_2_2 a n) * dens₂ (⋃ u ∈ t, (fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume`
Docstring: https://leanprover.zulipchat.com/#narrow/channel/442935-Carleson/topic/Problems.20in.20the.20forest.20operator.20proposition/near/522771057
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileStructure.Forest.indicator_row_bound`: `(hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) : eLpNorm (F.indicator (t.adjointCarlesonRowSum j g)) 2 volume ≤ ↑(Forest.C7_7_2_2 a n) * dens₂ (⋃ u ∈ t, (fun x => t.𝔗 x) u) ^ 2⁻…`
- `TileStructure.Forest.rowDecomp`: `(t : Forest X n) (j : ℕ) : Row X n`
- `TileStructure.Row`: `(X : Type u_1) (n : ℕ) : Type u_1`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `adjointCarlesonSum`: `(ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
- `adjointCarlesonSum_adjoint`: `(hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (ℭ : Set (𝔓 X)) : ∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ℭ f x = ∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ℭ g…`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
- `carlesonSum`: `(ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.forest_operator_g_main` (theorem)
Lean: `(hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : eLpNorm (fun x => ∑ u with u ∈ t, adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) 2 volume ^ 2 ≤ (↑(Forest.G2_0_4 a n) * eLpNorm g 2 volume) ^ 2`
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `Grid.dist_strictMono`: `(hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.adjoint_tree_estimate`: `(hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : eLpNorm (adjointCarlesonSum ((fun x => t.𝔗 x) u) g) 2 volume ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ …`
- `TileStructure.Forest.rowDecomp`: `(t : Forest X n) (j : ℕ) : Row X n`
- `TileStructure.Forest.rowDecomp_𝔘`: `(t : Forest X n) (j : ℕ) : Set (𝔓 X)`
- `TileStructure.Forest.row_correlation`: `(lj : j < 2 ^ n) (lj' : j' < 2 ^ n) (hn : j ≠ j') (hf₁ : BoundedCompactSupport f₁ volume) (nf₁ : Function.support f₁ ⊆ G) (hf₂ : BoundedCompactSupport f₂ volume) (nf₂ : Function.support f₂ ⊆ G) : ‖∫ …`
- `TileStructure.Forest.𝔖₀`: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) : Set (𝔓 X)`
- `TileStructure.Row`: `(X : Type u_1) (n : ℕ) : Type u_1`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.correlation_separated_trees_of_subset` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hg₁ : BoundedCompactSupport g₁ volume) (hg₂ : BoundedCompactSupport g₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁) g₁ x * (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u₂) g₂ x)‖ₑ ≤ ↑(Forest.C7_4_4 a n) * eLpNorm (fun x => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator u₁ g₁) x) 2 volume * eLpNorm (fun x => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator u₂ g₂) x) 2 volume`
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileStructure.Forest.correlation_distant_tree_parts`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf₁ : BoundedCompactSupport f₁ volume) (hf₂ : BoundedCompactSupport f₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁)…`
- `TileStructure.Forest.correlation_near_tree_parts`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf₁ : BoundedCompactSupport f₁ volume) (hf₂ : BoundedCompactSupport f₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁)…`
- `TileStructure.Forest.𝔖₀`: `(t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) : Set (𝔓 X)`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.correlation_separated_trees` (theorem)
Lean: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (hg₁ : BoundedCompactSupport g₁ volume) (hg₂ : BoundedCompactSupport g₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁) g₁ x * (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u₂) g₂ x)‖ₑ ≤ ↑(Forest.C7_4_4 a n) * eLpNorm (fun x => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator u₁ g₁) x) 2 volume * eLpNorm (fun x => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator u₂ g₂) x) 2 volume`
Docstring: Lemma 7.4.4
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.correlation_separated_trees_of_subset`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hg₁ : BoundedCompactSupport g₁ volume) (hg₂ : BoundedCompactSupport g₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁)…`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `D2`, `E_subset_𝓘`, `FunctionDistances`

### `TileStructure.Forest.row_correlation` (theorem)
Lean: `(lj : j < 2 ^ n) (lj' : j' < 2 ^ n) (hn : j ≠ j') (hf₁ : BoundedCompactSupport f₁ volume) (nf₁ : Function.support f₁ ⊆ G) (hf₂ : BoundedCompactSupport f₂ volume) (nf₂ : Function.support f₂ ⊆ G) : ‖∫ (x : X), t.adjointCarlesonRowSum j f₁ x * (starRingEnd ℂ) (t.adjointCarlesonRowSum j' f₂ x)‖ₑ ≤ ↑(Forest.C7_7_3 a n) * eLpNorm f₁ 2 volume * eLpNorm f₂ 2 volume`
Docstring: Lemma 7.7.3.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.adjoint_tree_control`: `(hu : u ∈ t) (hf : BoundedCompactSupport f volume) (h2f : Function.support f ⊆ G) : eLpNorm (fun x => t.adjointBoundaryOperator u f x) 2 volume ≤ ↑(Forest.C7_4_3 a) * eLpNorm f 2 volume`
- `TileStructure.Forest.correlation_separated_trees`: `(hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (hg₁ : BoundedCompactSupport g₁ volume) (hg₂ : BoundedCompactSupport g₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁) g₁ x * (starRingEnd…`
- `TileStructure.Forest.c𝓑`: `(z : ℕ × ℕ × Grid X) : X`
- `TileStructure.Forest.rowDecomp`: `(t : Forest X n) (j : ℕ) : Row X n`
- `TileStructure.Forest.rowDecomp_𝔘`: `(t : Forest X n) (j : ℕ) : Set (𝔓 X)`
- `TileStructure.Forest.r𝓑`: `(z : ℕ × ℕ × Grid X) : ℝ`
- `TileStructure.Forest.𝓑`: `Set (ℕ × ℕ × Grid X)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.forest_operator_g` (theorem)
Lean: `(t : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * ∑ u with u ∈ t, carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.G2_0_4 a n) * eLpNorm f 2 volume * eLpNorm g 2 volume`
Docstring: The `g` side of Proposition 2.0.4.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileStructure.Forest.forest_operator_g_main`: `(hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : eLpNorm (fun x => ∑ u with u ∈ t, adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) 2 volume ^ 2 ≤ (↑(Forest.G2_0_4 a n) * eLpNorm g 2 volu…`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `adjointCarlesonSum`: `(ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
- `adjointCarlesonSum_adjoint`: `(hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (ℭ : Set (𝔓 X)) : ∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ℭ f x = ∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ℭ g…`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `forest_operator` (theorem)
Lean: `(𝔉 : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * ∑ u with u ∈ 𝔉, carlesonSum ((fun x => 𝔉.𝔗 x) u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * dens₂ (⋃ u ∈ 𝔉, (fun x => 𝔉.𝔗 x) u) ^ (q⁻¹ - 2⁻¹) * eLpNorm f 2 volume * eLpNorm g 2 volume`
Proof uses:
- `TileStructure.Forest.forest_operator_f`: `(t : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * ∑ u with u ∈ t, ca…`
- `TileStructure.Forest.forest_operator_g`: `(t : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * ∑ u with u ∈ t, ca…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_0_4`, `C2_0_4_base`, `C2_0_4_base_def`, `C2_0_4_def`, `C_K`, `CompatibleFunctions`

### `forest_operator'` (theorem)
Lean: `(𝔉 : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hA : MeasurableSet A) (sA : A ⊆ G) : ∫⁻ (x : X) in A, ‖∑ u with u ∈ 𝔉, carlesonSum ((fun x => 𝔉.𝔗 x) u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * dens₂ (⋃ u ∈ 𝔉, (fun x => 𝔉.𝔗 x) u) ^ (q⁻¹ - 2⁻¹) * eLpNorm f 2 volume * volume A ^ (1 / 2)`
Docstring: Version of the forest operator theorem, but controlling the integral of the norm instead of the integral of the function multiplied by another function.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
- `forest_operator`: `(𝔉 : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * ∑ u with u ∈ 𝔉, ca…`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`
