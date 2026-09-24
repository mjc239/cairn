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

## Chapter (Lean module `Carleson.ForestOperator.QuantativeEstimate`)

### `TileStructure.Forest.density_tree_bound2` (theorem)
Lean: `(hf : BoundedCompactSupport f volume) (h2f : Function.support f ⊆ F) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * dens₂ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Docstring: Second part of Lemma 7.3.1.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `Grid.succ`: `(i : Grid X) : Grid X`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileStructure.Forest.approxOnCube`: `(C : Set (Grid X)) (f : X → E') (x : X) : E'`
- `TileStructure.Forest.local_dens1_tree_bound`: `(hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) : volume (↑L ∩ G ∩ ⋃ p ∈ (fun x => t.𝔗 x) u, E p) ≤ ↑(Forest.C7_3_2 a) * dens₁ ((fun x => t.𝔗 x) u) * volume ↑L`
- `TileStructure.Forest.tree_projection_estimate`: `(hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_2_1 a) * eLpNorm (F…`
- `TileStructure.Forest.𝓙`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.density_tree_bound1` (theorem)
Lean: `(hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Docstring: First part of Lemma 7.3.1.
Proof uses:
- `E`: `(p : 𝔓 X) : Set X`
- `PreTileStructure.toGridStructure`: `(𝕜 : Type u_1) : GridStructure X D κ S o`
- `TileStructure.Forest.approxOnCube`: `(C : Set (Grid X)) (f : X → E') (x : X) : E'`
- `TileStructure.Forest.local_dens1_tree_bound`: `(hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) : volume (↑L ∩ G ∩ ⋃ p ∈ (fun x => t.𝔗 x) u, E p) ≤ ↑(Forest.C7_3_2 a) * dens₁ ((fun x => t.𝔗 x) u) * volume ↑L`
- `TileStructure.Forest.tree_projection_estimate`: `(hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C7_2_1 a) * eLpNorm (F…`
- `TileStructure.Forest.𝓙`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `TileStructure.Forest.𝓙₀`: `(𝔖 : Set (𝔓 X)) : Set (Grid X)`
- `carlesonOn`: `(p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `TileStructure.Forest.local_dens1_tree_bound` (theorem)
Lean: `(hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) : volume (↑L ∩ G ∩ ⋃ p ∈ (fun x => t.𝔗 x) u, E p) ≤ ↑(Forest.C7_3_2 a) * dens₁ ((fun x => t.𝔗 x) u) * volume ↑L`
Docstring: Lemma 7.3.2.
Proof uses:
- `E₂`: `(l : ℝ) (p : 𝔓 X) : Set X`
- `Grid.dist_strictMono`: `(hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
- `Grid.succ`: `(i : Grid X) : Grid X`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `𝔠`: `(p : 𝔓 X) : X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`
