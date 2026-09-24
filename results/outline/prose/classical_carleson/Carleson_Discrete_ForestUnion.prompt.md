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

## Chapter (Lean module `Carleson.Discrete.ForestUnion`)

### `𝔗₁` (definition)
Lean: `(k : ℕ) (n : ℕ) (j : ℕ) (u : 𝔓 X) : Set (𝔓 X)`
Docstring: The subset `𝔗₁(u)` of `ℭ₁(k, n, j)`, given in (5.4.1). In lemmas, we will assume `u ∈ 𝔘₁ k n l`

### `forest_union` (theorem)
Lean: `(hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C5_1_2 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Docstring: Lemma 5.1.2 in the blueprint: the integral of the Carleson sum over the set which can naturally be decomposed as a union of forests can be controlled, thanks to the estimate for a single forest.
Proof uses:
- `TileLike`: `(X : Type u_1) : Type u_1`
- `forest_union_optimized`: `(hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C5_1_2_optimized a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `toTileLike`: `(p : 𝔓 X) : TileLike X`
- `ℭ₂`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
- `𝔘₁`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_0_4_base`, `C2_0_4_base_def`, `C5_1_2`, `C5_1_2_optimized`, `C5_1_2_optimized_le`, `C5_1_2_optimized_le'`

### `forest_union_aux` (theorem)
Lean: `(hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C2_0_4_base a) * 2 ^ (↑a + 5 / 2) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹ * ∑ n ≤ maxℭ X, ∑ _k ≤ n, ∑ _j ≤ 2 * n + 3, ∑ _l < 4 * n + 12, 2 ^ (-(q - 1) / q * ↑n)`
Docstring: Putting all the above decompositions together, one obtains a control of the integral of the full Carleson sum over `𝔓₁`, as a sum over all the forests.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `URel`: `(k : ℕ) (n : ℕ) (j : ℕ) (u : 𝔓 X) (u' : 𝔓 X) : Prop`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
- `carlesonSum_ℭ₆_eq_sum`: `(hkn : k ≤ n) : carlesonSum (ℭ₆ k n j) f x = ∑ l < 4 * n + 12, carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x`
- `dens'`: `(k : ℕ) (P' : Set (𝔓 X)) : ENNReal`
- `equivalenceOn_urel`: `EquivalenceOn (URel k n j) (𝔘₂ k n j)`
- `forest`: `(k : ℕ) (n : ℕ) (j : ℕ) (l : ℕ) : Forest X n`
- `iteratedMaximalSubfamily`: `(A : Set (𝔓 X)) (n : ℕ) : Set (𝔓 X)`
- `lintegral_carlesonSum_forest'`: `(hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * 2 ^ (↑a + 5 / 2) * volume G ^ (1 - q⁻¹) * …`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `ℭ₆` (definition)
Lean: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Docstring: The subset `ℭ₆(k, n, j)` of `ℭ₅(k, n, j)`, given above (5.4.1).

### `URel` (definition)
Lean: `(k : ℕ) (n : ℕ) (j : ℕ) (u : 𝔓 X) (u' : 𝔓 X) : Prop`
Docstring: The relation `∼` defined below (5.4.2). It is an equivalence relation on `𝔘₂ k n j`.

### `equivalenceOn_urel` (theorem)
Lean: `EquivalenceOn (URel k n j) (𝔘₂ k n j)`
Docstring: Lemma 5.4.2.
Proof uses:
- `Grid.dist_strictMono`: `(hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `ℭ`: `(k : ℕ) (n : ℕ) : Set (𝔓 X)`
- `ℭ₁`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
- `𝔅`: `(k : ℕ) (n : ℕ) (p : 𝔓 X) : Set (𝔓 X)`
- `𝔐`: `(k : ℕ) (n : ℕ) : Set (𝔓 X)`
- `𝔠`: `(p : 𝔓 X) : X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_1_2`, `C2_1_2_le_inv_256`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `EquivalenceOn`

### `forest_inner` (theorem)
Lean: `(hu : u ∈ 𝔘₃ k n j) (hp : p ∈ 𝔗₂ k n j u) : Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p) ⊆ ↑(𝓘 u)`
Docstring: Lemma 5.4.7, verifying (2.0.37)
Proof uses:
- `Grid.dist_strictMono`: `(hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `aux𝓒`: `(k : ℕ) : Set (Grid X)`
- `dens₂`: `(𝔓' : Set (𝔓 X)) : ENNReal`
- `equivalenceOn_urel`: `EquivalenceOn (URel k n j) (𝔘₂ k n j)`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `stackSize`: `(C : Set (𝔓 X)) (x : X) : ℕ`
- `toTileLike`: `(p : 𝔓 X) : TileLike X`
- `ℭ`: `(k : ℕ) (n : ℕ) : Set (𝔓 X)`
- `ℭ₁`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_1_2`, `C2_1_2_le_inv_256`, `C2_1_2_lt_one`, `C5_3_3`, `C5_3_3_le`, `C_K`

### `forest_separation` (theorem)
Lean: `(hu : u ∈ 𝔘₃ k n j) (hu' : u' ∈ 𝔘₃ k n j) (huu' : u ≠ u') (hp : p ∈ 𝔗₂ k n j u') (h : 𝓘 p ≤ 𝓘 u) : 2 ^ (defaultZ a * (n + 1)) < dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) (𝒬 u)`
Docstring: Lemma 5.4.6, verifying (2.0.36) Note: swapped `u` and `u'` to match (2.0.36)
Proof uses:
- `Grid.dist_strictMono`: `(hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
- `aux𝓒`: `(k : ℕ) : Set (Grid X)`
- `dens₂`: `(𝔓' : Set (𝔓 X)) : ENNReal`
- `equivalenceOn_urel`: `EquivalenceOn (URel k n j) (𝔘₂ k n j)`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `stackSize`: `(C : Set (𝔓 X)) (x : X) : ℕ`
- `toTileLike`: `(p : 𝔓 X) : TileLike X`
- `ℭ₁`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
- `ℭ₂`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
- `ℭ₅`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_1_2`, `C2_1_2_le_inv_256`, `C2_1_2_le_one`, `C2_1_2_lt_one`, `C5_3_3`, `C5_3_3_le`

### `forest` (definition)
Lean: `(k : ℕ) (n : ℕ) (j : ℕ) (l : ℕ) : Forest X n`
Docstring: The forest based on `𝔘₄ k n j l`.

### `carlesonSum_ℭ₆_eq_sum` (theorem)
Lean: `(hkn : k ≤ n) : carlesonSum (ℭ₆ k n j) f x = ∑ l < 4 * n + 12, carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x`
Docstring: The Carleson sum over `ℭ₆` can be decomposed as a sum over `4 n + 12` forests based on `𝔘₄ k n j l`.
Proof uses:
- `Grid.dist_strictMono`: `(hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `aux𝓒`: `(k : ℕ) : Set (Grid X)`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
- `dens₂`: `(𝔓' : Set (𝔓 X)) : ENNReal`
- `equivalenceOn_urel`: `EquivalenceOn (URel k n j) (𝔘₂ k n j)`
- `exists_maximal_disjoint_covering_subfamily`: `(A : Set (𝔓 X)) : ∃ B, (B.PairwiseDisjoint fun p => ↑(𝓘 p)) ∧ B ⊆ A ∧ ∀ a_1 ∈ A, ∃ b ∈ B, ↑(𝓘 a_1) ⊆ ↑(𝓘 b)`
- `forest`: `(k : ℕ) (n : ℕ) (j : ℕ) (l : ℕ) : Forest X n`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_1_2`, `C2_1_2_le_inv_256`, `C5_4_8`, `C6_forest`, `C6_forest'`, `C_K`

### `lintegral_carlesonSum_forest` (theorem)
Lean: `(hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * (2 ^ (2 * a + 5) * volume F / volume G) ^ (q⁻¹ - 2⁻¹) * volume F ^ (1 / 2) * volume G ^ (1 / 2)`
Docstring: For each forest, the integral of the norm of the Carleson sum can be controlled thanks to the forest theorem and to the density control coming from the fact we are away from `G₁`.
Proof uses:
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest`: `(X : Type u_1) (n : ℕ) : Type u_1`
- `TileStructure.Forest.𝔗`: `(self : Forest X n) (_ : 𝔓 X) : Set (𝔓 X)`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
- `equivalenceOn_urel`: `EquivalenceOn (URel k n j) (𝔘₂ k n j)`
- `exists_maximal_disjoint_covering_subfamily`: `(A : Set (𝔓 X)) : ∃ B, (B.PairwiseDisjoint fun p => ↑(𝓘 p)) ∧ B ⊆ A ∧ ∀ a_1 ∈ A, ∃ b ∈ B, ↑(𝓘 a_1) ⊆ ↑(𝓘 b)`
- `forest`: `(k : ℕ) (n : ℕ) (j : ℕ) (l : ℕ) : Forest X n`
- `forest_operator_le_volume`: `(𝔉 : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hA : MeasurableSet A) (sA : A ⊆ G) : ∫⁻ (x : X) in A, ‖∑ u with u ∈ 𝔉, carlesonSum ((fun x => 𝔉.𝔗 x) u) f x‖ₑ ≤ ↑(C2_0…`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `toTileLike`: `(p : 𝔓 X) : TileLike X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_0_4`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `EquivalenceOn`, `EquivalenceOn.out`

### `lintegral_carlesonSum_forest'` (theorem)
Lean: `(hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * 2 ^ (↑a + 5 / 2) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Docstring: For each forest, the integral of the norm of the Carleson sum can be controlled thanks to the forest theorem and to the density control coming from the fact we are away from `G₁`. Second version, with the volume of `F`.
Proof uses:
- `TileLike`: `(X : Type u_1) : Type u_1`
- `equivalenceOn_urel`: `EquivalenceOn (URel k n j) (𝔘₂ k n j)`
- `lintegral_carlesonSum_forest`: `(hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * (2 ^ (2 * a + 5) * volume F / volume G) ^ …`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `toTileLike`: `(p : 𝔓 X) : TileLike X`
- `ℭ₂`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `forest_union_optimized` (theorem)
Lean: `(hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C5_1_2_optimized a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Docstring: Version of the forest union result with a better constant.
Proof uses:
- `TileLike`: `(X : Type u_1) : Type u_1`
- `dens'`: `(k : ℕ) (P' : Set (𝔓 X)) : ENNReal`
- `forest_union_aux`: `(hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C2_0_4_base a) * 2 ^ (↑a + 5 / 2) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹ * ∑ n ≤ maxℭ…`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `toTileLike`: `(p : 𝔓 X) : TileLike X`
- `ℭ`: `(k : ℕ) (n : ℕ) : Set (𝔓 X)`
- `ℭ₂`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
- `𝔘₁`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_0_4_base`, `C5_1_2_optimized`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `FunctionDistances`
