You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `TileStructure.Forest.indicator_adjoint_tree_estimate`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : eLpNorm (F.indicator (adjointCarlesonSum ((fun x => t.𝔗 x) u) g)) 2 volume ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * dens₂ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm g 2 volume`
English: (Lemma 7.4.2, part 2) Let $t$ be a forest, $u \in t$, and let $g$ be bounded with compact support and $\operatorname{supp} g \subseteq G$. Then $$\big\|\mathbf{1}_F \cdot T^*_{\mathfrak{T}(u)} g\big\|_{L^2} \le C_{7.3.1.2}(a)\, \mathrm{dens}_1(\mathfrak{T}(u))^{1/2}\, \mathrm{dens}_2(\mathfrak{T}(u))^{1/2}\, \|g\|_{L^2},$$ where $T^*_{\mathfrak{T}(u)}$ is the adjoint Carleson sum over the tree $\mathfrak{T}(u)$ and $C_{7.3.1.2}$ is `Forest.C7_3_1_2`.

### `TileStructure.Forest.adjoint_tree_control`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ t) (hf : BoundedCompactSupport f volume) (h2f : Function.support f ⊆ G) : eLpNorm (fun x => t.adjointBoundaryOperator u f x) 2 volume ≤ ↑(Forest.C7_4_3 a) * eLpNorm f 2 volume`
English: (Lemma 7.4.3) Let $t$ be a forest, $u \in t$, and let $f$ be bounded with compact support and $\operatorname{supp} f \subseteq G$. Then $$\|\text{adjointBoundaryOperator}_t(u, f)\|_{L^2} \le C_{7.4.3}(a)\, \|f\|_{L^2},$$ where $C_{7.4.3}$ is `Forest.C7_4_3`.

### `TileStructure.Forest.𝔖₀`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) : Set (𝔓 X)`
English: For a forest $t$ and tiles $u_1, u_2$, the set of tiles $\mathfrak{S}_0(u_1,u_2)$: the set $\mathfrak{S}$ defined in the proof of Lemma 7.4.4.

### `TileStructure.Forest.overlap_implies_distance`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hp : p ∈ (fun x => t.𝔗 x) u₁ ∪ (fun x => t.𝔗 x) u₂) (hpu₁ : ¬Disjoint ↑(𝓘 p) ↑(𝓘 u₁)) : p ∈ t.𝔖₀ u₁ u₂`
English: (Lemma 7.4.7, part 1) Let $t$ be a forest and $u_1, u_2 \in t$ with $u_1 \ne u_2$ and $\mathcal{I}(u_1) \le \mathcal{I}(u_2)$. If $p \in \mathfrak{T}(u_1) \cup \mathfrak{T}(u_2)$ and $\mathcal{I}(p)$ is not disjoint from $\mathcal{I}(u_1)$, then $p \in \mathfrak{S}_0(u_1,u_2)$.

### `TileStructure.Forest.adjoint_density_tree_bound2`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (h2f : Function.support f ⊆ F) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) * f x‖ₑ ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * dens₂ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
English: Let $t$ be a forest and $u \in t$. Let $f, g$ be bounded with compact support, with $\operatorname{supp} f \subseteq F$ and $\operatorname{supp} g \subseteq G$. Then $$\Big|\int_X \overline{T^*_{\mathfrak{T}(u)} g(x)}\, f(x)\,dx\Big| \le C_{7.3.1.2}(a)\, \mathrm{dens}_1(\mathfrak{T}(u))^{1/2}\, \mathrm{dens}_2(\mathfrak{T}(u))^{1/2}\, \|f\|_{L^2}\, \|g\|_{L^2},$$ where $T^*_{\mathfrak{T}(u)}$ is `adjointCarlesonSum` over $\mathfrak{T}(u)$.

### `TileStructure.Forest.adjoint_density_tree_bound1`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) * f x‖ₑ ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
English: Let $t$ be a forest and $u \in t$. Let $f, g$ be bounded with compact support, with $\operatorname{supp} g \subseteq G$. Then $$\Big|\int_X \overline{T^*_{\mathfrak{T}(u)} g(x)}\, f(x)\,dx\Big| \le C_{7.3.1.1}(a)\, \mathrm{dens}_1(\mathfrak{T}(u))^{1/2}\, \|f\|_{L^2}\, \|g\|_{L^2},$$ where $T^*_{\mathfrak{T}(u)}$ is `adjointCarlesonSum` over $\mathfrak{T}(u)$ and $C_{7.3.1.1}$ is `Forest.C7_3_1_1`.

### `TileStructure.Forest.adjoint_tree_estimate`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : eLpNorm (adjointCarlesonSum ((fun x => t.𝔗 x) u) g) 2 volume ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm g 2 volume`
English: (Lemma 7.4.2, part 1) Let $t$ be a forest, $u \in t$, and let $g$ be bounded with compact support and $\operatorname{supp} g \subseteq G$. Then $$\big\|T^*_{\mathfrak{T}(u)} g\big\|_{L^2} \le C_{7.3.1.1}(a)\, \mathrm{dens}_1(\mathfrak{T}(u))^{1/2}\, \|g\|_{L^2},$$ where $T^*_{\mathfrak{T}(u)}$ is `adjointCarlesonSum` over $\mathfrak{T}(u)$.
