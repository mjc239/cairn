You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption) and the English. Compare the English with the full statement.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `Antichain.𝔄_aux`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : Θ X) (N : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → Set (𝔓 X) → Θ X → ℕ → Set (𝔓 X)`
English: (Definition 6.3.15.) For a set of tiles $\mathfrak{A} \subseteq \mathfrak{P}(X)$, a frequency $\vartheta \in \Theta(X)$ and $N \in \mathbb{N}$, we define the auxiliary subset $\mathfrak{A}_{\vartheta, N}$ = `𝔄_aux 𝔄 ϑ N` of $\mathfrak{A}$ as in Definition 6.3.15.

### `Antichain.tile_count`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (ϑ : ↑(Set.range ⇑Q)) : eLpNorm (fun x => ∑ p with p ∈ 𝔄, (1 + edist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) ↑ϑ) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) * (E p).indicator 1 x * G.indicator 1 x) (ENNReal.ofReal (p₆ a)) volume ≤ ↑(C6_1_6 a) * dens₁ 𝔄 ^ (p₆ a)⁻¹ * volume (⋃ p ∈ 𝔄, ↑(𝓘 p)) ^ (p₆ a)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {𝔄 : Set (𝔓 X)}, IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄 → ∀ (ϑ : ↑(Set.range ⇑Q)), eLpNorm (fun x => ∑ p with p ∈ 𝔄, (1 + edist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) ↑ϑ) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) * (E p).indicator 1 x * G.indicator 1 x) (ENNReal.ofReal (p₆ a)) volume ≤ ↑(C6_1_6 a) * dens₁ 𝔄 ^ (p₆ a)⁻¹ * volume (⋃ p ∈ 𝔄, ↑(𝓘 p)) ^ (p₆ a)⁻¹`
English: (Lemma 6.1.6.) Let $\mathfrak{A} \subseteq \mathfrak{P}(X)$ be an antichain with respect to $\le$ and let $\vartheta$ lie in the range of $Q$. Write $p_6 = p_6(a)$ and $D$ = `defaultD a`. Then
$$\Big\| x \mapsto \sum_{p \in \mathfrak{A}} \big(1 + d_{\mathfrak{c}(p),\, D^{s(p)}/4}(\mathcal{Q}(p), \vartheta)\big)^{-1/(2a^2 + a^3)}\, \mathbf{1}_{E(p)}(x)\, \mathbf{1}_G(x) \Big\|_{L^{p_6}} \le C_{6.1.6}(a)\, \operatorname{dens}_1(\mathfrak{A})^{1/p_6}\, \mu\Big(\bigcup_{p \in \mathfrak{A}} I(p)\Big)^{1/p_6}.$$

### `Antichain.global_antichain_density`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : ∑ p ∈ (𝔄_aux 𝔄 (↑ϑ) N).toFinset, volume (E p ∩ G) ≤ ↑(C6_3_4 a N) * dens₁ 𝔄 * volume (⋃ p ∈ 𝔄, ↑(𝓘 p))`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {𝔄 : Set (𝔓 X)}, IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄 → ∀ (ϑ : ↑(Set.range ⇑Q)) (N : ℕ), ∑ p ∈ (𝔄_aux 𝔄 (↑ϑ) N).toFinset, volume (E p ∩ G) ≤ ↑(C6_3_4 a N) * dens₁ 𝔄 * volume (⋃ p ∈ 𝔄, ↑(𝓘 p))`
English: (Lemma 6.3.4.) Let $\mathfrak{A} \subseteq \mathfrak{P}(X)$ be an antichain with respect to $\le$, let $\vartheta$ lie in the range of $Q$, and let $N \in \mathbb{N}$. Then
$$\sum_{p \in \mathfrak{A}_{\vartheta, N}} \mu(E(p) \cap G) \le C_{6.3.4}(a, N)\, \operatorname{dens}_1(\mathfrak{A})\, \mu\Big(\bigcup_{p \in \mathfrak{A}} I(p)\Big).$$

### `Antichain.𝔄'`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → Set (𝔓 X) → ↑(Set.range ⇑Q) → ℕ → Set (𝔓 X)`
English: For a set of tiles $\mathfrak{A}$, $\vartheta$ in the range of $Q$ and $N \in \mathbb{N}$, we define the set of tiles $\mathfrak{A}'$ introduced in Lemma 6.3.4.

### `Antichain.𝓛`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : Set (Grid X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → Set (𝔓 X) → ↑(Set.range ⇑Q) → ℕ → Set (Grid X)`
English: For a set of tiles $\mathfrak{A}$, $\vartheta$ in the range of $Q$ and $N \in \mathbb{N}$, we define the collection of cubes $\mathcal{L}$ introduced in Lemma 6.3.4.

### `Antichain.𝓛'`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : Set (Grid X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → Set (𝔓 X) → ↑(Set.range ⇑Q) → ℕ → Set (Grid X)`
English: For a set of tiles $\mathfrak{A}$, $\vartheta$ in the range of $Q$ and $N \in \mathbb{N}$, we define the collection of cubes $\mathcal{L}^*$ introduced in Lemma 6.3.4.

### `Antichain.exists_larger_grid`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hL : L ∈ 𝓛' 𝔄 ϑ N) : ∃ L', L ≤ L' ∧ s L' = s L + 1`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {𝔄 : Set (𝔓 X)} {ϑ : ↑(Set.range ⇑Q)} {N : ℕ} {L : Grid X}, L ∈ 𝓛' 𝔄 ϑ N → ∃ L', L ≤ L' ∧ s L' = s L + 1`
English: If $L \in \mathcal{L}^*(\mathfrak{A}, \vartheta, N)$, then there is a cube $L'$ with $L \le L'$ and $s(L') = s(L) + 1$.

### `Antichain.L'`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hL : L ∈ 𝓛' 𝔄 ϑ N) : Grid X`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → {𝔄 : Set (𝔓 X)} → {ϑ : ↑(Set.range ⇑Q)} → {N : ℕ} → {L : Grid X} → L ∈ 𝓛' 𝔄 ϑ N → Grid X`
English: For $L \in \mathcal{L}^*(\mathfrak{A}, \vartheta, N)$, we define the cube $L'$ introduced in the proof of Lemma 6.3.4.

### `Antichain.p''`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hL : L ∈ 𝓛' 𝔄 ϑ N) : 𝔓 X`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → {𝔄 : Set (𝔓 X)} → {ϑ : ↑(Set.range ⇑Q)} → {N : ℕ} → {L : Grid X} → L ∈ 𝓛' 𝔄 ϑ N → 𝔓 X`
English: For $L \in \mathcal{L}^*(\mathfrak{A}, \vartheta, N)$, we define the tile $p''$ of the blueprint.

### `Antichain.pΘ`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hL : L ∈ 𝓛' 𝔄 ϑ N) : 𝔓 X`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] → {𝔄 : Set (𝔓 X)} → {ϑ : ↑(Set.range ⇑Q)} → {N : ℕ} → {L : Grid X} → L ∈ 𝓛' 𝔄 ϑ N → 𝔓 X`
English: For $L \in \mathcal{L}^*(\mathfrak{A}, \vartheta, N)$, we define the tile $p_\Theta$ of the blueprint.

### `Antichain.stack_density`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : Θ X) (N : ℕ) (L : Grid X) : ∑ p ∈ (𝔄_aux 𝔄 ϑ N).toFinset with 𝓘 p = L, volume (E p ∩ G) ≤ 2 ^ (a * (N + 5)) * dens₁ 𝔄 * volume ↑L`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : Θ X) (N : ℕ) (L : Grid X), ∑ p ∈ (𝔄_aux 𝔄 ϑ N).toFinset with 𝓘 p = L, volume (E p ∩ G) ≤ 2 ^ (a * (N + 5)) * dens₁ 𝔄 * volume ↑L`
English: (Lemma 6.3.2.) For every set of tiles $\mathfrak{A}$, every $\vartheta \in \Theta(X)$, every $N \in \mathbb{N}$ and every cube $L$,
$$\sum_{p \in \mathfrak{A}_{\vartheta, N},\ I(p) = L} \mu(E(p) \cap G) \le 2^{a(N+5)}\, \operatorname{dens}_1(\mathfrak{A})\, \mu(L).$$

### `Antichain.tile_reach`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hp : dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) ϑ ≤ 2 ^ N) (hp' : dist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / 4} (𝒬 p') ϑ ≤ 2 ^ N) (hI : 𝓘 p ≤ 𝓘 p') (hs : 𝔰 p < 𝔰 p') : smul (2 ^ (N + 2)) p ≤ smul (2 ^ (N + 2)) p'`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {ϑ : Θ X} {N : ℕ} {p p' : 𝔓 X}, dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) ϑ ≤ 2 ^ N → dist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / 4} (𝒬 p') ϑ ≤ 2 ^ N → 𝓘 p ≤ 𝓘 p' → 𝔰 p < 𝔰 p' → smul (2 ^ (N + 2)) p ≤ smul (2 ^ (N + 2)) p'`
English: (Lemma 6.3.1.) Let $p, p'$ be tiles with $d_{\mathfrak{c}(p),\, D^{s(p)}/4}(\mathcal{Q}(p), \vartheta) \le 2^N$ and $d_{\mathfrak{c}(p'),\, D^{s(p')}/4}(\mathcal{Q}(p'), \vartheta) \le 2^N$, where $D$ = `defaultD a`, and suppose $I(p) \le I(p')$ and $s(p) < s(p')$. Then $2^{N+2} p \le 2^{N+2} p'$ (as dilated tiles, via `smul`).
