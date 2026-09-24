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

## Chapter (Lean module `Carleson.TileExistence`)

### `grid_existence` (definition)
Lean: `(X : Type u_1) : GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`
Docstring: Proof that there exists a grid structure.

### `tileData_existence` (definition)
Lean: `PreTileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`

### `Construction.Ω` (definition)
Lean: `(p : 𝔓 X) : Set (Θ X)`

### `tile_existence` (definition)
Lean: `(X : Type u_1) : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`
