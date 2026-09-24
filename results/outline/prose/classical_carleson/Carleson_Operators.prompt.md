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

## Chapter (Lean module `Carleson.Operators`)

### `carlesonOn` (definition)
Lean: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
Docstring: The operator `T_𝔭` defined in Proposition 2.0.2.

### `carlesonSum` (definition)
Lean: `(ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
Docstring: The operator `T_ℭ f` defined at the bottom of Section 7.4. We will use this in other places of the formalization as well.

### `adjointCarleson` (definition)
Lean: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
Docstring: The definition of `Tₚ*g(x)`, defined above Lemma 7.4.1

### `adjointCarlesonSum` (definition)
Lean: `(ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
Docstring: The definition of `T_ℭ*g(x)`, defined at the bottom of Section 7.4

### `adjointCarlesonSum_adjoint` (theorem)
Lean: `(hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (ℭ : Set (𝔓 X)) : ∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ℭ f x = ∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ℭ g x) * f x`
Docstring: `adjointCarlesonSum` is the adjoint of `carlesonSum`.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `adjointCarleson`: `(p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`
