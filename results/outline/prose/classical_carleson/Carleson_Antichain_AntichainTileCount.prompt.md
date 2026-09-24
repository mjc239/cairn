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

## Chapter (Lean module `Carleson.Antichain.AntichainTileCount`)

### `Antichain.𝔄_aux` (definition)
Lean: `(𝔄 : Set (𝔓 X)) (ϑ : Θ X) (N : ℕ) : Set (𝔓 X)`
Docstring: Def 6.3.15.

### `Antichain.tile_count` (theorem)
Lean: `(h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (ϑ : ↑(Set.range ⇑Q)) : eLpNorm (fun x => ∑ p with p ∈ 𝔄, (1 + edist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) ↑ϑ) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) * (E p).indicator 1 x * G.indicator 1 x) (ENNReal.ofReal (p₆ a)) volume ≤ ↑(C6_1_6 a) * dens₁ 𝔄 ^ (p₆ a)⁻¹ * volume (⋃ p ∈ 𝔄, ↑(𝓘 p)) ^ (p₆ a)⁻¹`
Docstring: Lemma 6.1.6.
Proof uses:
- `Antichain.global_antichain_density`: `(h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : ∑ p ∈ (𝔄_aux 𝔄 (↑ϑ) N).toFinset, volume (E p ∩ G) ≤ ↑(C6_3_4 a N) * dens₁ 𝔄 * volume (⋃ p ∈ 𝔄, ↑(𝓘 p))`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `toTileLike`: `(p : 𝔓 X) : TileLike X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `Antichain.C6_1_6`, `Antichain.C6_3_4`, `Antichain.biUnion_𝔄_aux`, `Antichain.le_C6_1_6`, `Antichain.one_lt_p₆`, `Antichain.pairwiseDisjoint_𝔄_aux`, `Antichain.p₆`

### `Antichain.global_antichain_density` (theorem)
Lean: `(h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : ∑ p ∈ (𝔄_aux 𝔄 (↑ϑ) N).toFinset, volume (E p ∩ G) ≤ ↑(C6_3_4 a N) * dens₁ 𝔄 * volume (⋃ p ∈ 𝔄, ↑(𝓘 p))`
Docstring: Lemma 6.3.4.
Proof uses:
- `Antichain.L'`: `(hL : L ∈ 𝓛' 𝔄 ϑ N) : Grid X`
- `Antichain.exists_larger_grid`: `(hL : L ∈ 𝓛' 𝔄 ϑ N) : ∃ L', L ≤ L' ∧ s L' = s L + 1`
- `Antichain.p''`: `(hL : L ∈ 𝓛' 𝔄 ϑ N) : 𝔓 X`
- `Antichain.pΘ`: `(hL : L ∈ 𝓛' 𝔄 ϑ N) : 𝔓 X`
- `Antichain.stack_density`: `(𝔄 : Set (𝔓 X)) (ϑ : Θ X) (N : ℕ) (L : Grid X) : ∑ p ∈ (𝔄_aux 𝔄 ϑ N).toFinset with 𝓘 p = L, volume (E p ∩ G) ≤ 2 ^ (a * (N + 5)) * dens₁ 𝔄 * volume ↑L`
- `Antichain.tile_reach`: `(hp : dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) ϑ ≤ 2 ^ N) (hp' : dist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / 4} (𝒬 p') ϑ ≤ 2 ^ N) (hI : 𝓘 p ≤ 𝓘 p') (hs : 𝔰 p < 𝔰 p') : smul (2 ^ (N + 2)) p ≤ smul (2 ^ (N + 2…`
- `Antichain.𝓛`: `(𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : Set (Grid X)`
- `Antichain.𝓛'`: `(𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : Set (Grid X)`
- `Antichain.𝔄'`: `(𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : Set (𝔓 X)`
- `E₂`: `(l : ℝ) (p : 𝔓 X) : Set X`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `Antichain.C6_3_4`, `Antichain.C6_3_4'`, `Antichain.Ep_inter_G_inter_Ip'_subset_E2`, `Antichain.I_p''_le_L'`

### `Antichain.𝔄'` (definition)
Lean: `(𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : Set (𝔓 X)`
Docstring: The set `𝔄'` defined in Lemma 6.3.4.

### `Antichain.𝓛` (definition)
Lean: `(𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : Set (Grid X)`
Docstring: The set `𝓛` defined in Lemma 6.3.4.

### `Antichain.𝓛'` (definition)
Lean: `(𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : Set (Grid X)`
Docstring: The set `𝓛*` defined in Lemma 6.3.4.

### `Antichain.exists_larger_grid` (theorem)
Lean: `(hL : L ∈ 𝓛' 𝔄 ϑ N) : ∃ L', L ≤ L' ∧ s L' = s L + 1`
Proof uses:
- `Antichain.𝓛`: `(𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : Set (Grid X)`
- `Antichain.𝔄'`: `(𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : Set (𝔓 X)`
- `Antichain.𝔄_aux`: `(𝔄 : Set (𝔓 X)) (ϑ : Θ X) (N : ℕ) : Set (𝔓 X)`
- `Grid.succ`: `(i : Grid X) : Grid X`
- `𝓘`: `(_ : 𝔓 X) : Grid X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `Antichain.SL`, `Antichain.SL_nonempty`, `Antichain.exists_p'_ge_L`, `Antichain.not_I_p'_le_L`, `Antichain.p'`, `Antichain.p'_mem`, `Antichain.s_L_le_s_p'`

### `Antichain.L'` (definition)
Lean: `(hL : L ∈ 𝓛' 𝔄 ϑ N) : Grid X`
Docstring: The `L'` introduced in the proof of Lemma 6.3.4.

### `Antichain.tile_reach` (theorem)
Lean: `(hp : dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) ϑ ≤ 2 ^ N) (hp' : dist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / 4} (𝒬 p') ϑ ≤ 2 ^ N) (hI : 𝓘 p ≤ 𝓘 p') (hs : 𝔰 p < 𝔰 p') : smul (2 ^ (N + 2)) p ≤ smul (2 ^ (N + 2)) p'`
Docstring: Lemma 6.3.1.
Proof uses:
- `Grid.dist_strictMono`: `(hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `BallsCoverBalls`, `C2_1_2`, `C2_1_2_le_inv_256`, `C2_1_2_le_one`, `C_K`, `CompatibleFunctions`, `CompatibleFunctions.cdist_le`

### `Antichain.stack_density` (theorem)
Lean: `(𝔄 : Set (𝔓 X)) (ϑ : Θ X) (N : ℕ) (L : Grid X) : ∑ p ∈ (𝔄_aux 𝔄 ϑ N).toFinset with 𝓘 p = L, volume (E p ∩ G) ≤ 2 ^ (a * (N + 5)) * dens₁ 𝔄 * volume ↑L`
Docstring: Lemma 6.3.2.
Proof uses:
- `E₂`: `(l : ℝ) (p : 𝔓 X) : Set X`
- `TileLike`: `(X : Type u_1) : Type u_1`
- `smul`: `(l : ℝ) (p : 𝔓 X) : TileLike X`
- `𝔠`: `(p : 𝔓 X) : X`
- `𝔰`: `(p : 𝔓 X) : ℤ`
Helper lemmas folded into the proof: `AllBallsCoverBalls`, `AllBallsCoverBalls.ballsCoverBalls`, `AllBallsCoverBalls.mk`, `AllBallsCoverBalls.pow`, `As`, `BallsCoverBalls`, `BallsCoverBalls.mono`, `BallsCoverBalls.nonpos`

### `Antichain.p''` (definition)
Lean: `(hL : L ∈ 𝓛' 𝔄 ϑ N) : 𝔓 X`
Docstring: p'' in the blueprint

### `Antichain.pΘ` (definition)
Lean: `(hL : L ∈ 𝓛' 𝔄 ϑ N) : 𝔓 X`
Docstring: p_Θ in the blueprint
