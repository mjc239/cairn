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

## Chapter (Lean module `Carleson.Antichain.TileCorrelation`)

### `Tile.correlation_le` (theorem)
Lean: `(hle : 𝔰 p' ≤ 𝔰 p) (hg : Measurable g) (hg1 : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (y : X), adjointCarleson p' g y * (starRingEnd ℂ) (adjointCarleson p g y)‖ₑ ≤ (↑(Tile.C6_1_5 a) * (1 + edist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / 4} (𝒬 p') (𝒬 p)) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) / volume ↑(𝓘 p) * ∫⁻ (y : X) in E p', ‖g y‖ₑ) * ∫⁻ (y : X) in E p, ‖g y‖ₑ`
Docstring: Part 1 of Lemma 6.1.5 (eq. 6.1.43).
Proof uses:
- `Tile.correlation_le_of_nonempty_inter`: `(ha : 4 ≤ a) (hle : 𝔰 p' ≤ 𝔰 p) (hg : Measurable g) (hg1 : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) (hinter : (Metric.ball (𝔠 p') (5 * ↑(defaultD a) ^ 𝔰 p') ∩ Metric.ball (𝔠 p) (5 * ↑(defaultD a) ^ 𝔰 p)).…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CoveredByBalls`, `D2`, `FunctionDistances`, `FunctionDistances.coeΘ`

### `Tile.I12_le` (theorem)
Lean: `(ha : 4 ≤ a) (hle : 𝔰 p' ≤ 𝔰 p) (hinter : (Metric.ball (𝔠 p') (5 * ↑(defaultD a) ^ 𝔰 p') ∩ Metric.ball (𝔠 p) (5 * ↑(defaultD a) ^ 𝔰 p)).Nonempty) (x1 : ↑(E p')) (x2 : ↑(E p)) : Tile.I12 p p' g ↑x1 ↑x2 ≤ 2 ^ ((2 * 𝕔 + 6 + 𝕔 / 4) * a ^ 3 + 8 * a + 1) * (1 + edist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / 4} (𝒬 p') (𝒬 p)) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) / volume (Metric.ball (↑x2) (↑(defaultD a) ^ 𝔰 p)) * ‖g ↑x1‖ₑ * ‖g ↑x2‖ₑ`
Docstring: Inequality (6.2.29).
Proof uses:
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `Tile.I12_le'`: `(hle : 𝔰 p' ≤ 𝔰 p) (x1 : ↑(E p')) (x2 : ↑(E p)) : Tile.I12 p p' g ↑x1 ↑x2 ≤ 2 ^ ((2 * 𝕔 + 6 + 𝕔 / 4) * a ^ 3 + 8 * a) * (1 + edist_{↑x1, ↑(defaultD a) ^ 𝔰 p'} (Q ↑x1) (Q ↑x2)) ^ (-(2 * ↑a ^ 2 + ↑a ^ …`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CompatibleFunctions.cdist_le`, `CompatibleFunctions.cdist_mono`, `CoveredByBalls`, `ENNReal.rpow_le_rpow_iff_of_neg`

### `Tile.I12_le'` (theorem)
Lean: `(hle : 𝔰 p' ≤ 𝔰 p) (x1 : ↑(E p')) (x2 : ↑(E p)) : Tile.I12 p p' g ↑x1 ↑x2 ≤ 2 ^ ((2 * 𝕔 + 6 + 𝕔 / 4) * a ^ 3 + 8 * a) * (1 + edist_{↑x1, ↑(defaultD a) ^ 𝔰 p'} (Q ↑x1) (Q ↑x2)) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) / volume (Metric.ball (↑x2) (↑(defaultD a) ^ 𝔰 p)) * ‖g ↑x1‖ₑ * ‖g ↑x2‖ₑ`
Docstring: Inequality (6.2.28).
Proof uses:
- `holder_van_der_corput`: `(φ_supp : Function.support φ ⊆ Metric.ball z R) : ‖∫ (x : X), Complex.exp (Complex.I * (↑(f x) - ↑(g x))) * φ x‖ₑ ≤ ↑(C2_0_5 ↑a) * volume (Metric.ball z R) * iHolENorm φ z (2 * R) (defaultτ a) * (1 +…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `Tile.correlation_le_of_nonempty_inter` (theorem)
Lean: `(ha : 4 ≤ a) (hle : 𝔰 p' ≤ 𝔰 p) (hg : Measurable g) (hg1 : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) (hinter : (Metric.ball (𝔠 p') (5 * ↑(defaultD a) ^ 𝔰 p') ∩ Metric.ball (𝔠 p) (5 * ↑(defaultD a) ^ 𝔰 p)).Nonempty) : ‖∫ (y : X), adjointCarleson p' g y * (starRingEnd ℂ) (adjointCarleson p g y)‖ₑ ≤ (↑(Tile.C6_1_5 a) * (1 + edist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / 4} (𝒬 p') (𝒬 p)) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) / volume ↑(𝓘 p) * ∫⁻ (y : X) in E p', ‖g y‖ₑ) * ∫⁻ (y : X) in E p, ‖g y‖ₑ`
Proof uses:
- `Tile.I12_le`: `(ha : 4 ≤ a) (hle : 𝔰 p' ≤ 𝔰 p) (hinter : (Metric.ball (𝔠 p') (5 * ↑(defaultD a) ^ 𝔰 p') ∩ Metric.ball (𝔠 p) (5 * ↑(defaultD a) ^ 𝔰 p)).Nonempty) (x1 : ↑(E p')) (x2 : ↑(E p)) : Tile.I12 p p' g ↑x1 ↑x…`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`
