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

## Chapter (Lean module `Carleson.FinitaryCarleson`)

### `finitary_carleson` (theorem)
Lean: `(X : Type u_1) : ∃ G', MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → ∫⁻ (x : X) in G \ G', ‖∑ s ∈ (Set.Icc (σ₁ x) (σ₂ x)).toFinset, ∫ (y : X), Ks s x y * f y * Complex.exp (Complex.I * ↑((Q x) y))‖ₑ ≤ ↑(C2_0_1 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Docstring: Proposition 2.0.1
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileStructure`: `(Q : outParam (SimpleFunc X (Θ X))) (D : outParam ℕ) (κ : outParam ℝ) (S : outParam ℕ) (o : outParam X) : Type (u + 1)`
- `TileStructure.toPreTileStructure`: `PreTileStructure Q D κ S o`
- `cancelPt`: `(X : Type u_2) : X`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
- `carlesonSum`: `(ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
- `defaultS`: `(X : Type u_1) : ℕ`
- `discrete_carleson`: `(X : Type u_1) : ∃ G', MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → ∫⁻ (x : X) in G \ G', ‖carlesonSum Set.univ f x‖ₑ ≤ ↑(C2_0_2 …`
- `grid_existence`: `(X : Type u_1) : GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_0_1`, `C2_0_2`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `FunctionDistances`
