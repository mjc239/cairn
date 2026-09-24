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

## Chapter (Lean module `Carleson.TileStructure`)

### `PreTileStructure.toGridStructure` (definition)
Lean: `(𝕜 : Type u_1) : GridStructure X D κ S o`

### `𝔓` (definition)
Lean: `(X : Type u) : Type u`

### `𝓘` (definition)
Lean: `(_ : 𝔓 X) : Grid X`

### `𝔠` (definition)
Lean: `(p : 𝔓 X) : X`

### `𝔰` (definition)
Lean: `(p : 𝔓 X) : ℤ`

### `TileStructure` (definition)
Lean: `(Q : outParam (SimpleFunc X (Θ X))) (D : outParam ℕ) (κ : outParam ℝ) (S : outParam ℕ) (o : outParam X) : Type (u + 1)`
Docstring: A tile structure.

### `TileStructure.toPreTileStructure` (definition)
Lean: `PreTileStructure Q D κ S o`

### `E` (definition)
Lean: `(p : 𝔓 X) : Set X`
Docstring: The set `E` defined in Proposition 2.0.2.

### `TileLike` (definition)
Lean: `(X : Type u_1) : Type u_1`

### `toTileLike` (definition)
Lean: `(p : 𝔓 X) : TileLike X`

### `smul` (definition)
Lean: `(l : ℝ) (p : 𝔓 X) : TileLike X`
Docstring: This is not defined as such in the blueprint, but `λp ≲ λ'p'` can be written using `smul l p ≤ smul l' p'`. Beware: `smul 1 p` is very different from `toTileLike p`.

### `E₂` (definition)
Lean: `(l : ℝ) (p : 𝔓 X) : Set X`

### `dens₁` (definition)
Lean: `(𝔓' : Set (𝔓 X)) : ENNReal`
Docstring: This density is defined to live in `ℝ≥0∞`. Use `ENNReal.toReal` to get a real number.

### `exists_maximal_disjoint_covering_subfamily` (theorem)
Lean: `(A : Set (𝔓 X)) : ∃ B, (B.PairwiseDisjoint fun p => ↑(𝓘 p)) ∧ B ⊆ A ∧ ∀ a_1 ∈ A, ∃ b ∈ B, ↑(𝓘 a_1) ⊆ ↑(𝓘 b)`
Docstring: Given any family of tiles, one can extract a maximal disjoint subfamily, covering everything.
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `FunctionDistances`, `FunctionDistances.coeΘ`, `FunctionDistances.metric`

### `iteratedMaximalSubfamily` (definition)
Lean: `(A : Set (𝔓 X)) (n : ℕ) : Set (𝔓 X)`
Docstring: Iterating `maximalSubfamily` to obtain disjoint subfamilies of `A`.

### `stackSize` (definition)
Lean: `(C : Set (𝔓 X)) (x : X) : ℕ`
Docstring: The number of tiles `p` in `s` whose underlying cube `𝓘 p` contains `x`.

### `dens₂` (definition)
Lean: `(𝔓' : Set (𝔓 X)) : ENNReal`
Docstring: This density is defined to live in `ℝ≥0∞`. Use `ENNReal.toReal` to get a real number.
