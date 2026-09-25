You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one. For a definition, name the setting its signature assumes. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): MeasureTheory, TileStructure, Antichain.

### `TileStructure.Forest.indicator_adjoint_tree_estimate`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : eLpNorm (F.indicator (adjointCarlesonSum ((fun x => t.𝔗 x) u) g)) 2 volume ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * dens₂ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {n : ℕ} {t : Forest X n} {u : 𝔓 X} {g : X → ℂ}, BoundedCompactSupport g volume → Function.support g ⊆ G → u ∈ t → eLpNorm (F.indicator (adjointCarlesonSum ((fun x => t.𝔗 x) u) g)) 2 volume ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * dens₂ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm g 2 volume`
Docstring: Part 2 of Lemma 7.4.2.
Previous English: (Lemma 7.4.2, part 2) Let $t$ be a forest, $u \in t$, and let $g$ be bounded with compact support and $\operatorname{supp} g \subseteq G$. Then $$\big\|\mathbf{1}_F \cdot T^*_{\mathfrak{T}(u)} g\big\|_{L^2} \le C_{7.3.1.2}(a)\, \mathrm{dens}_1(\mathfrak{T}(u))^{1/2}\, \mathrm{dens}_2(\mathfrak{T}(u))^{1/2}\, \|g\|_{L^2},$$ where $T^*_{\mathfrak{T}(u)}$ is the adjoint Carleson sum over the tree $\mathfrak{T}(u)$ and $C_{7.3.1.2}$ is `Forest.C7_3_1_2`.
Checker's issue: English omits the standing assumptions (metric space X, ProofData and TileStructure instances).

### `TileStructure.Forest.adjoint_tree_control`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ t) (hf : BoundedCompactSupport f volume) (h2f : Function.support f ⊆ G) : eLpNorm (fun x => t.adjointBoundaryOperator u f x) 2 volume ≤ ↑(Forest.C7_4_3 a) * eLpNorm f 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {n : ℕ} {t : Forest X n} {u : 𝔓 X} {f : X → ℂ}, u ∈ t → BoundedCompactSupport f volume → Function.support f ⊆ G → eLpNorm (fun x => t.adjointBoundaryOperator u f x) 2 volume ≤ ↑(Forest.C7_4_3 a) * eLpNorm f 2 volume`
Docstring: Lemma 7.4.3.
Previous English: (Lemma 7.4.3) Let $t$ be a forest, $u \in t$, and let $f$ be bounded with compact support and $\operatorname{supp} f \subseteq G$. Then $$\|\text{adjointBoundaryOperator}_t(u, f)\|_{L^2} \le C_{7.4.3}(a)\, \|f\|_{L^2},$$ where $C_{7.4.3}$ is `Forest.C7_4_3`.
Checker's issue: English omits the standing assumptions (metric space X, ProofData and TileStructure instances).

### `TileStructure.Forest.overlap_implies_distance`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hp : p ∈ (fun x => t.𝔗 x) u₁ ∪ (fun x => t.𝔗 x) u₂) (hpu₁ : ¬Disjoint ↑(𝓘 p) ↑(𝓘 u₁)) : p ∈ t.𝔖₀ u₁ u₂`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {n : ℕ} {t : Forest X n} {u₁ u₂ p : 𝔓 X}, u₁ ∈ t → u₂ ∈ t → u₁ ≠ u₂ → 𝓘 u₁ ≤ 𝓘 u₂ → p ∈ (fun x => t.𝔗 x) u₁ ∪ (fun x => t.𝔗 x) u₂ → ¬Disjoint ↑(𝓘 p) ↑(𝓘 u₁) → p ∈ t.𝔖₀ u₁ u₂`
Docstring: Part 1 of Lemma 7.4.7.
Previous English: (Lemma 7.4.7, part 1) Let $t$ be a forest and $u_1, u_2 \in t$ with $u_1 \ne u_2$ and $\mathcal{I}(u_1) \le \mathcal{I}(u_2)$. If $p \in \mathfrak{T}(u_1) \cup \mathfrak{T}(u_2)$ and $\mathcal{I}(p)$ is not disjoint from $\mathcal{I}(u_1)$, then $p \in \mathfrak{S}_0(u_1,u_2)$.
Checker's issue: English omits the standing assumptions (metric space X, ProofData and TileStructure instances).

### `TileStructure.Forest.adjoint_density_tree_bound2`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (h2f : Function.support f ⊆ F) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) * f x‖ₑ ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * dens₂ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {n : ℕ} {t : Forest X n} {u : 𝔓 X} {f g : X → ℂ}, BoundedCompactSupport f volume → Function.support f ⊆ F → BoundedCompactSupport g volume → Function.support g ⊆ G → u ∈ t → ‖∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) * f x‖ₑ ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * dens₂ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Previous English: Let $t$ be a forest and $u \in t$. Let $f, g$ be bounded with compact support, with $\operatorname{supp} f \subseteq F$ and $\operatorname{supp} g \subseteq G$. Then $$\Big|\int_X \overline{T^*_{\mathfrak{T}(u)} g(x)}\, f(x)\,dx\Big| \le C_{7.3.1.2}(a)\, \mathrm{dens}_1(\mathfrak{T}(u))^{1/2}\, \mathrm{dens}_2(\mathfrak{T}(u))^{1/2}\, \|f\|_{L^2}\, \|g\|_{L^2},$$ where $T^*_{\mathfrak{T}(u)}$ is `adjointCarlesonSum` over $\mathfrak{T}(u)$.
Checker's issue: English omits the standing assumptions (metric space X, ProofData and TileStructure instances).

### `TileStructure.Forest.adjoint_density_tree_bound1`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) * f x‖ₑ ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {n : ℕ} {t : Forest X n} {u : 𝔓 X} {f g : X → ℂ}, BoundedCompactSupport f volume → BoundedCompactSupport g volume → Function.support g ⊆ G → u ∈ t → ‖∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) * f x‖ₑ ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Previous English: Let $t$ be a forest and $u \in t$. Let $f, g$ be bounded with compact support, with $\operatorname{supp} g \subseteq G$. Then $$\Big|\int_X \overline{T^*_{\mathfrak{T}(u)} g(x)}\, f(x)\,dx\Big| \le C_{7.3.1.1}(a)\, \mathrm{dens}_1(\mathfrak{T}(u))^{1/2}\, \|f\|_{L^2}\, \|g\|_{L^2},$$ where $T^*_{\mathfrak{T}(u)}$ is `adjointCarlesonSum` over $\mathfrak{T}(u)$ and $C_{7.3.1.1}$ is `Forest.C7_3_1_1`.
Checker's issue: English omits the standing assumptions (metric space X, ProofData and TileStructure instances).

### `TileStructure.Forest.adjoint_tree_estimate`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : eLpNorm (adjointCarlesonSum ((fun x => t.𝔗 x) u) g) 2 volume ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {n : ℕ} {t : Forest X n} {u : 𝔓 X} {g : X → ℂ}, BoundedCompactSupport g volume → Function.support g ⊆ G → u ∈ t → eLpNorm (adjointCarlesonSum ((fun x => t.𝔗 x) u) g) 2 volume ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm g 2 volume`
Docstring: Part 1 of Lemma 7.4.2.
Previous English: (Lemma 7.4.2, part 1) Let $t$ be a forest, $u \in t$, and let $g$ be bounded with compact support and $\operatorname{supp} g \subseteq G$. Then $$\big\|T^*_{\mathfrak{T}(u)} g\big\|_{L^2} \le C_{7.3.1.1}(a)\, \mathrm{dens}_1(\mathfrak{T}(u))^{1/2}\, \|g\|_{L^2},$$ where $T^*_{\mathfrak{T}(u)}$ is `adjointCarlesonSum` over $\mathfrak{T}(u)$.
Checker's issue: English omits the standing assumptions (metric space X, ProofData and TileStructure instances).
