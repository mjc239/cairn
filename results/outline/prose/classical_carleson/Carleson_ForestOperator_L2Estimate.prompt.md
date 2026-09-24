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

## Chapter (Lean module `Carleson.ForestOperator.L2Estimate`)

### `TileStructure.Forest.tree_projection_estimate` (theorem)
Lean: `(hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_2_1 a) * eLpNorm (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) fun x => ‖f x‖) 2 volume * eLpNorm (Forest.approxOnCube (Forest.𝓛 ((fun x => t.𝔗 x) u)) fun x => ‖g x‖) 2 volume`
Docstring: Lemma 7.2.1.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileStructure.Forest.boundaryOperator`: `(t : Forest X n) (u : 𝔓 X) (f : X → ℂ) (x : X) : ENNReal`
- `TileStructure.Forest.boundary_operator_bound`: `(hf : BoundedCompactSupport f volume) : eLpNorm (t.boundaryOperator u f) 2 volume ≤ ↑(Forest.C7_2_3 a) * eLpNorm f 2 volume`
- `TileStructure.Forest.c𝓑`: `(z : ℕ × ℕ × Grid X) : X`
- `TileStructure.Forest.eLpNorm_MB_le`: `(hf : BoundedCompactSupport f volume) : eLpNorm (maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f) 2 volume ≤ ↑(CMB (↑(defaultA a)) 2) * eLpNorm f 2 volume`
- `TileStructure.Forest.nontangential_operator_bound`: `(hf : BoundedCompactSupport f volume) (θ : Θ X) : eLpNorm (Forest.nontangentialMaximalFunction θ f) 2 volume ≤ ↑(Forest.C7_2_2 a) * eLpNorm f 2 volume`
- `TileStructure.Forest.pointwise_tree_estimate`: `(hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) (hx : x ∈ L) (hx' : x' ∈ L) (hf : BoundedCompactSupport f volume) : ‖carlesonSum ((fun x => t.𝔗 x) u) (fun y => Complex.exp (Complex.I * -↑((𝒬 u)…`
- `TileStructure.Forest.r𝓑`: `(z : ℕ × ℕ × Grid X) : ℝ`
- `TileStructure.Forest.𝓑`: `Set (ℕ × ℕ × Grid X)`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.boundary_operator_bound` (theorem)
Lean: `(hf : BoundedCompactSupport f volume) : eLpNorm (t.boundaryOperator u f) 2 volume ≤ ↑(Forest.C7_2_3 a) * eLpNorm f 2 volume`
Docstring: Lemma 7.2.3.
Proof uses:
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileStructure.Forest.c𝓑`: `(z : ℕ × ℕ × Grid X) : X`
- `TileStructure.Forest.r𝓑`: `(z : ℕ × ℕ × Grid X) : ℝ`
- `TileStructure.Forest.𝓑`: `Set (ℕ × ℕ × Grid X)`
- `TileStructure.Forest.𝓙`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝔗`: `(self : Forest X n) (_ : 𝔓 X) : Set (𝔓 X)`
- `hasStrongType_maximalFunction_one`: `(hp : 1 < p) : HasStrongType (maximalFunction μ 𝓑 c r 1) (↑p) (↑p) μ μ ↑(CMB A p)`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
Helper lemmas folded into the proof: `AEMeasurable.ite`, `AEMeasurable.piecewise`, `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`

### `TileStructure.Forest.eLpNorm_MB_le` (theorem)
Lean: `(hf : BoundedCompactSupport f volume) : eLpNorm (maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f) 2 volume ≤ ↑(CMB (↑(defaultA a)) 2) * eLpNorm f 2 volume`
Proof uses:
- `hasStrongType_maximalFunction_one`: `(hp : 1 < p) : HasStrongType (maximalFunction μ 𝓑 c r 1) (↑p) (↑p) μ μ ↑(CMB A p)`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.nontangential_operator_bound` (theorem)
Lean: `(hf : BoundedCompactSupport f volume) (θ : Θ X) : eLpNorm (Forest.nontangentialMaximalFunction θ f) 2 volume ≤ ↑(Forest.C7_2_2 a) * eLpNorm f 2 volume`
Docstring: Lemma 7.2.2.
Proof uses:
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileStructure.Forest.c𝓑`: `(z : ℕ × ℕ × Grid X) : X`
- `TileStructure.Forest.eLpNorm_MB_le`: `(hf : BoundedCompactSupport f volume) : eLpNorm (maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f) 2 volume ≤ ↑(CMB (↑(defaultA a)) 2) * eLpNorm f 2 volume`
- `TileStructure.Forest.r𝓑`: `(z : ℕ × ℕ × Grid X) : ℝ`
- `TileStructure.Forest.𝓑`: `Set (ℕ × ℕ × Grid X)`
- `TileStructure.toPreTileStructure`: `PreTileStructure Q D κ S o`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`
