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

## Chapter (Lean module `Carleson.Discrete.ForestComplement`)

### `forest_complement` (theorem)
Lean: `(hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ ↑(C5_1_3 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Docstring: Lemma 5.1.3, proving the bound on the integral of the Carleson sum over all leftover tiles which do not fit in a forest. It follows from a careful grouping of these tiles into finitely many antichains.
Proof uses:
- `TileLike`: `(X : Type u_1) : Type u_1`
- `forest_complement_optimized`: `(hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ ↑(C5_1_3_optimized a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `toTileLike`: `(p : 𝔓 X) : TileLike X`
- `ℭ₂`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
- `𝔘₁`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_0_3`, `C5_1_3`, `C5_1_3_optimized`, `C5_1_3_optimized_le_C5_1_3`, `C_K`, `CompatibleFunctions`

### `𝔓pos` (definition)
Lean: `Set (𝔓 X)`
Docstring: The set 𝔓_{G\G'} in the blueprint

### `lintegral_carlesonSum_𝔓₁_compl_le_sum_lintegral` (theorem)
Lean: `(h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ (((∑ n ≤ maxℭ X, ∑ k ≤ n, ∑ l < n, ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔏₀' k n l) f x‖ₑ) + ∑ n ≤ maxℭ X, ∑ k ≤ n, ∑ j ≤ 2 * n + 3, ∑ l ≤ defaultZ a * (n + 1), ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔏₁ k n j l) f x‖ₑ) + ∑ n ≤ maxℭ X, ∑ k ≤ n, ∑ j ≤ 2 * n + 3, ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔏₂ k n j) f x‖ₑ) + ∑ n ≤ maxℭ X, ∑ k ≤ n, ∑ j ≤ 2 * n + 3, ∑ l ≤ defaultZ a * (n + 1), ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔏₃ k n j l) f x‖ₑ`
Docstring: Putting together all the previous decomposition lemmas, one gets an estimate of the integral of `‖carlesonSum 𝔓₁ᶜ f x‖ₑ` by a sum of integrals of the same form over various subsets of `𝔓`, which are all antichains by design.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `E₂`: `(l : ℝ) (p : 𝔓 X) : Set X`
- `Grid.dist_strictMono`: `(hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
- `dens'`: `(k : ℕ) (P' : Set (𝔓 X)) : ENNReal`
- `toTileLike`: `(p : 𝔓 X) : TileLike X`
- `ℭ`: `(k : ℕ) (n : ℕ) : Set (𝔓 X)`
- `𝔅`: `(k : ℕ) (n : ℕ) (p : 𝔓 X) : Set (𝔓 X)`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `lintegral_enorm_carlesonSum_le_of_isAntichain_subset_ℭ` (theorem)
Lean: `(hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) (hA : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (h'A : 𝔄 ⊆ ℭ k n) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔄) f x‖ₑ ≤ ↑(C2_0_3 a (nnq X)) * 2 ^ (a + 3) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹ * 2 ^ (-((q - 1) / (8 * ↑a ^ 4) * ↑n))`
Docstring: Custom version of the antichain operator theorem, in the specific form we need to handle the various terms in the previous statement.
Proof uses:
- `E₂`: `(l : ℝ) (p : 𝔓 X) : Set X`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `antichain_operator_le_volume`: `(h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (hf : Measurable f) (hfF : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hA : A ⊆ G) : ∫⁻ (x : X) in A, ‖carlesonSum 𝔄 f x‖ₑ ≤ ↑(C2_0_3 a (nnq X)) * dens₁ 𝔄 ^ ((q -…`
- `dens'`: `(k : ℕ) (P' : Set (𝔓 X)) : ENNReal`
- `dens₁`: `(𝔓' : Set (𝔓 X)) : ENNReal`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `toTileLike`: `(p : 𝔓 X) : TileLike X`
- `ℭ₂`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
- `𝔘₁`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
- `𝔠`: `(p : 𝔓 X) : X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `forest_complement_optimized` (theorem)
Lean: `(hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ ↑(C5_1_3_optimized a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Proof uses:
- `Grid.dist_strictMono`: `(hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `dens'`: `(k : ℕ) (P' : Set (𝔓 X)) : ENNReal`
- `lintegral_carlesonSum_𝔓₁_compl_le_sum_lintegral`: `(h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ (((∑ n ≤ maxℭ X, ∑ k ≤ n, ∑ l < n, ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔏₀' k n l) f x‖ₑ) + ∑ n ≤ maxℭ X, ∑ k ≤ n, ∑ …`
- `lintegral_enorm_carlesonSum_le_of_isAntichain_subset_ℭ`: `(hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) (hA : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (h'A : 𝔄 ⊆ ℭ k n) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔄) f x‖ₑ ≤ ↑(C2_0_3 a (…`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `toTileLike`: `(p : 𝔓 X) : TileLike X`
- `ℭ`: `(k : ℕ) (n : ℕ) : Set (𝔓 X)`
- `ℭ₁`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
- `ℭ₂`: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_0_3`, `C2_1_2`, `C2_1_2_le_inv_256`, `C2_1_2_lt_one`, `C5_1_3_optimized`, `C5_3_3`
