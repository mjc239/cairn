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

### `forest_union`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C5_1_2 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {f : X → ℂ}, (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → Measurable f → ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C5_1_2 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Docstring: Lemma 5.1.2 in the blueprint: the integral of the Carleson sum over the set which can naturally be decomposed as a union of forests can be controlled, thanks to the estimate for a single forest.
Previous English: (Lemma 5.1.2) Let $f$ be a measurable function with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Then $$\int_{G\setminus G'} \|\mathrm{carlesonSum}(\mathfrak{P}_1, f)(x)\|\,dx \le C_{5.1.2}(a,q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where $C_{5.1.2}$ is the constant `C5_1_2` and $q$ is `nnq X`.
Checker's issue: Omits the standing assumptions (ProofData / TileStructure bundle), which carry mathematical content.

### `forest_union_aux`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C2_0_4_base a) * 2 ^ (↑a + 5 / 2) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹ * ∑ n ≤ maxℭ X, ∑ _k ≤ n, ∑ _j ≤ 2 * n + 3, ∑ _l < 4 * n + 12, 2 ^ (-(q - 1) / q * ↑n)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {f : X → ℂ}, (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → Measurable f → ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C2_0_4_base a) * 2 ^ (↑a + 5 / 2) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹ * ∑ n ≤ maxℭ X, ∑ _k ≤ n, ∑ _j ≤ 2 * n + 3, ∑ _l < 4 * n + 12, 2 ^ (-(q - 1) / q * ↑n)`
Docstring: Putting all the above decompositions together, one obtains a control of the integral of the full Carleson sum over `𝔓₁`, as a sum over all the forests.
Previous English: Let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $$\int_{G\setminus G'} \|\mathrm{carlesonSum}(\mathfrak{P}_1, f)(x)\|\,dx \le C_{2.0.4}^{\mathrm{base}}(a)\, 2^{a+5/2}\, \mu(G)^{1-1/q}\, \mu(F)^{1/q} \sum_{n \le \mathrm{max}\mathfrak{C}} \sum_{k \le n} \sum_{j \le 2n+3} \sum_{l < 4n+12} 2^{-\frac{q-1}{q} n},$$ where $C_{2.0.4}^{\mathrm{base}}$ is `C2_0_4_base` and $\mathrm{max}\mathfrak{C}$ is `maxℭ X`.
Checker's issue: Omits the standing assumptions (ProofData / TileStructure bundle), which carry mathematical content.

### `equivalenceOn_urel`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : EquivalenceOn (URel k n j) (𝔘₂ k n j)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {k n j : ℕ}, EquivalenceOn (URel k n j) (𝔘₂ k n j)`
Docstring: Lemma 5.4.2.
Previous English: (Lemma 5.4.2) The relation $\sim$ (`URel k n j`) is an equivalence relation on the set $\mathfrak{U}_2(k,n,j)$.
Checker's issue: Omits the standing assumptions (ProofData / TileStructure bundle), which carry mathematical content.

### `forest_inner`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ 𝔘₃ k n j) (hp : p ∈ 𝔗₂ k n j u) : Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p) ⊆ ↑(𝓘 u)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {k n j : ℕ} {p u : 𝔓 X}, u ∈ 𝔘₃ k n j → p ∈ 𝔗₂ k n j u → Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p) ⊆ ↑(𝓘 u)`
Docstring: Lemma 5.4.7, verifying (2.0.37)
Previous English: (Lemma 5.4.7, verifying (2.0.37)) If $u \in \mathfrak{U}_3(k,n,j)$ and $p \in \mathfrak{T}_2(k,n,j,u)$, then $B(c(p), 8 D^{s(p)}) \subseteq \mathcal{I}(u)$, where $D$ is `defaultD a`, $c(p)=𝔠 p$ and $s(p) = 𝔰 p$.
Checker's issue: Omits the standing assumptions (ProofData / TileStructure bundle), which carry mathematical content.

### `forest_separation`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ 𝔘₃ k n j) (hu' : u' ∈ 𝔘₃ k n j) (huu' : u ≠ u') (hp : p ∈ 𝔗₂ k n j u') (h : 𝓘 p ≤ 𝓘 u) : 2 ^ (defaultZ a * (n + 1)) < dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) (𝒬 u)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {k n j : ℕ} {p u u' : 𝔓 X}, u ∈ 𝔘₃ k n j → u' ∈ 𝔘₃ k n j → u ≠ u' → p ∈ 𝔗₂ k n j u' → 𝓘 p ≤ 𝓘 u → 2 ^ (defaultZ a * (n + 1)) < dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) (𝒬 u)`
Docstring: Lemma 5.4.6, verifying (2.0.36) Note: swapped `u` and `u'` to match (2.0.36)
Previous English: (Lemma 5.4.6, verifying (2.0.36)) Let $u, u' \in \mathfrak{U}_3(k,n,j)$ with $u \ne u'$, let $p \in \mathfrak{T}_2(k,n,j,u')$, and suppose $\mathcal{I}(p) \le \mathcal{I}(u)$. Then $$2^{Z(n+1)} < d_{c(p),\, D^{s(p)}/4}(\mathcal{Q}(p), \mathcal{Q}(u)),$$ where $Z$ is `defaultZ a` and $D$ is `defaultD a`.
Checker's issue: Omits the standing assumptions (ProofData / TileStructure bundle), which carry mathematical content.

### `carlesonSum_ℭ₆_eq_sum`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hkn : k ≤ n) : carlesonSum (ℭ₆ k n j) f x = ∑ l < 4 * n + 12, carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {f : X → ℂ} {x : X} {k n j : ℕ}, k ≤ n → carlesonSum (ℭ₆ k n j) f x = ∑ l < 4 * n + 12, carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x`
Docstring: The Carleson sum over `ℭ₆` can be decomposed as a sum over `4 n + 12` forests based on `𝔘₄ k n j l`.
Previous English: If $k \le n$, then for all $x$, $$\mathrm{carlesonSum}(\mathfrak{C}_6(k,n,j), f)(x) = \sum_{l < 4n+12} \mathrm{carlesonSum}\Big(\bigcup_{u \in \mathfrak{U}_4(k,n,j,l)} \mathfrak{T}_2(k,n,j,u), f\Big)(x).$$
Checker's issue: Omits the standing assumptions (ProofData / TileStructure bundle), which carry mathematical content.

### `lintegral_carlesonSum_forest`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * (2 ^ (2 * a + 5) * volume F / volume G) ^ (q⁻¹ - 2⁻¹) * volume F ^ (1 / 2) * volume G ^ (1 / 2)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {k n j l : ℕ} {f : X → ℂ}, Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → ∫⁻ (x : X) in G \ G', ‖carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * (2 ^ (2 * a + 5) * volume F / volume G) ^ (q⁻¹ - 2⁻¹) * volume F ^ (1 / 2) * volume G ^ (1 / 2)`
Docstring: For each forest, the integral of the norm of the Carleson sum can be controlled thanks to the forest theorem and to the density control coming from the fact we are away from `G₁`.
Previous English: Let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $$\int_{G\setminus G'} \Big\|\mathrm{carlesonSum}\Big(\bigcup_{u \in \mathfrak{U}_4(k,n,j,l)} \mathfrak{T}_2(k,n,j,u), f\Big)(x)\Big\|\,dx \le C_{2.0.4}(a,q,n) \Big(\frac{2^{2a+5}\mu(F)}{\mu(G)}\Big)^{1/q - 1/2} \mu(F)^{1/2}\, \mu(G)^{1/2}.$$
Checker's issue: Omits the standing assumptions (ProofData / TileStructure bundle), which carry mathematical content.

### `lintegral_carlesonSum_forest'`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * 2 ^ (↑a + 5 / 2) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {k n j l : ℕ} {f : X → ℂ}, Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → ∫⁻ (x : X) in G \ G', ‖carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * 2 ^ (↑a + 5 / 2) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Docstring: For each forest, the integral of the norm of the Carleson sum can be controlled thanks to the forest theorem and to the density control coming from the fact we are away from `G₁`. Second version, with the volume of `F`.
Previous English: Let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $$\int_{G\setminus G'} \Big\|\mathrm{carlesonSum}\Big(\bigcup_{u \in \mathfrak{U}_4(k,n,j,l)} \mathfrak{T}_2(k,n,j,u), f\Big)(x)\Big\|\,dx \le C_{2.0.4}(a,q,n)\, 2^{a+5/2}\, \mu(G)^{1-1/q}\, \mu(F)^{1/q}.$$
Checker's issue: Omits the standing assumptions (ProofData / TileStructure bundle), which carry mathematical content.

### `forest_union_optimized`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C5_1_2_optimized a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {f : X → ℂ}, (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → Measurable f → ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C5_1_2_optimized a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Docstring: Version of the forest union result with a better constant.
Previous English: Let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Then $$\int_{G\setminus G'} \|\mathrm{carlesonSum}(\mathfrak{P}_1, f)(x)\|\,dx \le C^{\mathrm{opt}}_{5.1.2}(a,q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where $C^{\mathrm{opt}}_{5.1.2}$ is `C5_1_2_optimized` and $q$ is `nnq X`.
Checker's issue: Omits the standing assumptions (ProofData / TileStructure bundle), which carry mathematical content.
