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

## Chapter (Lean module `Carleson.ForestOperator.PointwiseEstimate`)

### `TileStructure.Forest.𝓑` (definition)
Lean: `Set (ℕ × ℕ × Grid X)`
Docstring: The indexing set for the collection of balls 𝓑, defined above Lemma 7.1.3.

### `TileStructure.Forest.𝓙₀` (definition)
Lean: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
Docstring: The definition of `𝓙₀(𝔖), defined above Lemma 7.1.2

### `TileStructure.Forest.𝓙` (definition)
Lean: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
Docstring: The definition of `𝓙(𝔖), defined above Lemma 7.1.2

### `TileStructure.Forest.boundaryOperator` (definition)
Lean: `(t : Forest X n) (u : 𝔓 X) (f : X → ℂ) (x : X) : ENNReal`
Docstring: The operator `S_{1,𝔲} f(x)`, given in (7.1.4).

### `TileStructure.Forest.c𝓑` (definition)
Lean: `(z : ℕ × ℕ × Grid X) : X`
Docstring: The center function for the collection of balls 𝓑.

### `TileStructure.Forest.r𝓑` (definition)
Lean: `(z : ℕ × ℕ × Grid X) : ℝ`
Docstring: The radius function for the collection of balls 𝓑.

### `TileStructure.Forest.approxOnCube` (definition)
Lean: `(C : Set (Grid X)) (f : X → E') (x : X) : E'`
Docstring: The projection operator `P_𝓒 f(x)`, given above Lemma 7.1.3. In lemmas the `c` will be pairwise disjoint on `C`.

### `TileStructure.Forest.pointwise_tree_estimate` (theorem)
Lean: `(hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) (hx : x ∈ L) (hx' : x' ∈ L) (hf : BoundedCompactSupport f volume) : ‖carlesonSum ((fun x => t.𝔗 x) u) (fun y => Complex.exp (Complex.I * -↑((𝒬 u) y)) * f y) x‖ₑ ≤ ↑(Forest.C7_1_3 a) * (maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) fun x => ‖f x‖) x' + t.boundaryOperator u (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) fun x => ↑‖f x‖) x') + Forest.nontangentialMaximalFunction (𝒬 u) (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) f) x'`
Docstring: Lemma 7.1.3.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `TileStructure.Forest.first_tree_pointwise`: `(hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) (hx : x ∈ L) (hx' : x' ∈ L) (hf : BoundedCompactSupport f volume) : ‖∑ i ∈ t.σ u x, ∫ (y : X), (Complex.exp (Complex.I * (-↑((𝒬 u) y) + ↑((Q x) y…`
- `TileStructure.Forest.second_tree_pointwise`: `(hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) (hx : x ∈ L) (hx' : x' ∈ L) : ‖∑ i ∈ t.σ u x, ∫ (y : X), Ks i x y * Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) f y‖ₑ ≤ Forest.nontangent…`
- `TileStructure.Forest.third_tree_pointwise`: `(hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) (hx : x ∈ L) (hx' : x' ∈ L) (hf : BoundedCompactSupport f volume) : ‖∑ i ∈ t.σ u x, ∫ (y : X), Ks i x y * (f y - Forest.approxOnCube (Forest.𝓙 ((…`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.third_tree_pointwise` (theorem)
Lean: `(hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) (hx : x ∈ L) (hx' : x' ∈ L) (hf : BoundedCompactSupport f volume) : ‖∑ i ∈ t.σ u x, ∫ (y : X), Ks i x y * (f y - Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) f y)‖ₑ ≤ ↑(Forest.C7_1_6 a) * t.boundaryOperator u (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) fun x => ↑‖f x‖) x'`
Docstring: Lemma 7.1.6
Proof uses:
- `TileStructure.Forest.r𝓑`: `(z : ℕ × ℕ × Grid X) : ℝ`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `𝔠`: `(p : 𝔓 X) : X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.first_tree_pointwise` (theorem)
Lean: `(hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) (hx : x ∈ L) (hx' : x' ∈ L) (hf : BoundedCompactSupport f volume) : ‖∑ i ∈ t.σ u x, ∫ (y : X), (Complex.exp (Complex.I * (-↑((𝒬 u) y) + ↑((Q x) y) + ↑((𝒬 u) x) - ↑((Q x) x))) - 1) * Ks i x y * f y‖ₑ ≤ ↑(Forest.C7_1_4 a) * maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) fun x => ‖f x‖) x'`
Docstring: Lemma 7.1.4
Proof uses:
- `Grid.dist_strictMono`: `(hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `𝔠`: `(p : 𝔓 X) : X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.second_tree_pointwise` (theorem)
Lean: `(hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) (hx : x ∈ L) (hx' : x' ∈ L) : ‖∑ i ∈ t.σ u x, ∫ (y : X), Ks i x y * Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) f y‖ₑ ≤ Forest.nontangentialMaximalFunction (𝒬 u) (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) f) x'`
Docstring: Lemma 7.1.5
Proof uses:
- `TileLike`: `(X : Type u_1) : Type u_1`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `toTileLike`: `(p : 𝔓 X) : TileLike X`
- `𝔠`: `(p : 𝔓 X) : X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C_K`, `CompatibleFunctions`, `CompatibleFunctions.cdist_le`, `CompatibleFunctions.cdist_mono`, `CompatibleFunctions.le_cdist`, `CoveredByBalls`
