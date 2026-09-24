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

## Chapter (Lean module `Carleson.Discrete.Defs`)

### `aux𝓒` (definition)
Lean: `(k : ℕ) : Set (Grid X)`

### `dens'` (definition)
Lean: `(k : ℕ) (P' : Set (𝔓 X)) : ENNReal`
Docstring: The definition `dens'_k(𝔓')` given in (5.1.6).

### `ℭ` (definition)
Lean: `(k : ℕ) (n : ℕ) : Set (𝔓 X)`
Docstring: The partition `ℭ(k, n)` of `𝔓(k)` by density, given in (5.1.7).

### `𝔐` (definition)
Lean: `(k : ℕ) (n : ℕ) : Set (𝔓 X)`
Docstring: The definition `𝔐(k, n)` given in (5.1.4) and (5.1.5).

### `𝔅` (definition)
Lean: `(k : ℕ) (n : ℕ) (p : 𝔓 X) : Set (𝔓 X)`
Docstring: The subset `𝔅(p)` of `𝔐(k, n)`, given in (5.1.8).

### `ℭ₁` (definition)
Lean: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Docstring: The subset `ℭ₁(k, n, j)` of `ℭ(k, n)`, given in (5.1.9). Together with `𝔏₀(k, n)` this forms a partition.

### `ℭ₂` (definition)
Lean: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Docstring: The subset `ℭ₂(k, n, j)` of `ℭ₁(k, n, j)`, given in (5.1.13).

### `𝔘₁` (definition)
Lean: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Docstring: The subset `𝔘₁(k, n, j)` of `ℭ₁(k, n, j)`, given in (5.1.14).

### `ℭ₅` (definition)
Lean: `(k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Docstring: The subset `ℭ₅(k, n, j)` of `ℭ₄(k, n, j)`, given in (5.1.23).
