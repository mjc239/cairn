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

## Chapter (Lean module `Carleson.Antichain.Basic`)

### `dens2_antichain` (theorem)
Lean: `(h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (hfF : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hf : Measurable f) (hgG : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) (hg : Measurable g) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum 𝔄 f x‖ₑ ≤ ↑(C6_1_3 a (nnq X)) * dens₂ 𝔄 ^ ((2 * ↑(nnq X) / (↑(nnq X) + 1))⁻¹ - 2⁻¹) * eLpNorm f 2 volume * eLpNorm g 2 volume`
Docstring: Lemma 6.1.3 (inequality 6.1.11).
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `Lemma6_1_3.eLpNorm_𝓜p_le`: `(𝔄 : Set (𝔓 X)) (hf : MemLp f 2 volume) : eLpNorm (Lemma6_1_3.𝓜p 𝔄 (Lemma6_1_3.p X) f) 2 volume ≤ ↑(C2_0_6 (↑(defaultA a)) (Lemma6_1_3.p X).toNNReal 2) * eLpNorm f 2 volume`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `toTileLike`: `(p : 𝔓 X) : TileLike X`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `Lemma6_1_3.eLpNorm_𝓜p_le` (theorem)
Lean: `(𝔄 : Set (𝔓 X)) (hf : MemLp f 2 volume) : eLpNorm (Lemma6_1_3.𝓜p 𝔄 (Lemma6_1_3.p X) f) 2 volume ≤ ↑(C2_0_6 (↑(defaultA a)) (Lemma6_1_3.p X).toNNReal 2) * eLpNorm f 2 volume`
Docstring: Maximal function bound needed in the proof
Proof uses:
- `hasStrongType_maximalFunction`: `(hp₁ : 0 < p₁) (hp₁₂ : p₁ < p₂) : HasStrongType (maximalFunction μ 𝓑 c r ↑p₁) (↑p₂) (↑p₂) μ μ ↑(C2_0_6 A p₁ p₂)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`
