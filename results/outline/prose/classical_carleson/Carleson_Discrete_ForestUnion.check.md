You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `𝔗₁`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) (u : 𝔓 X) : Set (𝔓 X)`
English: For $k, n, j \in \mathbb{N}$ and a tile $u$, the set $\mathfrak{T}_1(u) = \mathfrak{T}_1(k,n,j,u)$, a subset of $\mathfrak{C}_1(k,n,j)$, defined in (5.4.1). (In lemmas one assumes $u \in \mathfrak{U}_1(k,n,l)$.)

### `forest_union`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C5_1_2 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
English: (Lemma 5.1.2) Let $f$ be a measurable function with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Then $$\int_{G\setminus G'} \|\mathrm{carlesonSum}(\mathfrak{P}_1, f)(x)\|\,dx \le C_{5.1.2}(a,q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where $C_{5.1.2}$ is the constant `C5_1_2` and $q$ is `nnq X`.

### `forest_union_aux`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C2_0_4_base a) * 2 ^ (↑a + 5 / 2) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹ * ∑ n ≤ maxℭ X, ∑ _k ≤ n, ∑ _j ≤ 2 * n + 3, ∑ _l < 4 * n + 12, 2 ^ (-(q - 1) / q * ↑n)`
English: Let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $$\int_{G\setminus G'} \|\mathrm{carlesonSum}(\mathfrak{P}_1, f)(x)\|\,dx \le C_{2.0.4}^{\mathrm{base}}(a)\, 2^{a+5/2}\, \mu(G)^{1-1/q}\, \mu(F)^{1/q} \sum_{n \le \mathrm{max}\mathfrak{C}} \sum_{k \le n} \sum_{j \le 2n+3} \sum_{l < 4n+12} 2^{-\frac{q-1}{q} n},$$ where $C_{2.0.4}^{\mathrm{base}}$ is `C2_0_4_base` and $\mathrm{max}\mathfrak{C}$ is `maxℭ X`.

### `ℭ₆`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
English: For $k, n, j \in \mathbb{N}$, the set of tiles $\mathfrak{C}_6(k,n,j)$, a subset of $\mathfrak{C}_5(k,n,j)$, defined just above (5.4.1).

### `URel`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) (u : 𝔓 X) (u' : 𝔓 X) : Prop`
English: For $k,n,j \in \mathbb{N}$ and tiles $u, u'$, the relation $u \sim u'$ (`URel k n j u u'`) defined below (5.4.2); it is an equivalence relation on $\mathfrak{U}_2(k,n,j)$.

### `equivalenceOn_urel`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : EquivalenceOn (URel k n j) (𝔘₂ k n j)`
English: (Lemma 5.4.2) The relation $\sim$ (`URel k n j`) is an equivalence relation on the set $\mathfrak{U}_2(k,n,j)$.

### `forest_inner`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ 𝔘₃ k n j) (hp : p ∈ 𝔗₂ k n j u) : Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p) ⊆ ↑(𝓘 u)`
English: (Lemma 5.4.7, verifying (2.0.37)) If $u \in \mathfrak{U}_3(k,n,j)$ and $p \in \mathfrak{T}_2(k,n,j,u)$, then $B(c(p), 8 D^{s(p)}) \subseteq \mathcal{I}(u)$, where $D$ is `defaultD a`, $c(p)=𝔠 p$ and $s(p) = 𝔰 p$.

### `forest_separation`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ 𝔘₃ k n j) (hu' : u' ∈ 𝔘₃ k n j) (huu' : u ≠ u') (hp : p ∈ 𝔗₂ k n j u') (h : 𝓘 p ≤ 𝓘 u) : 2 ^ (defaultZ a * (n + 1)) < dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) (𝒬 u)`
English: (Lemma 5.4.6, verifying (2.0.36)) Let $u, u' \in \mathfrak{U}_3(k,n,j)$ with $u \ne u'$, let $p \in \mathfrak{T}_2(k,n,j,u')$, and suppose $\mathcal{I}(p) \le \mathcal{I}(u)$. Then $$2^{Z(n+1)} < d_{c(p),\, D^{s(p)}/4}(\mathcal{Q}(p), \mathcal{Q}(u)),$$ where $Z$ is `defaultZ a` and $D$ is `defaultD a`.

### `forest`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) (l : ℕ) : Forest X n`
English: For $k,n,j,l \in \mathbb{N}$, the forest (of type `Forest X n`) whose set of tree tops is $\mathfrak{U}_4(k,n,j,l)$.

### `carlesonSum_ℭ₆_eq_sum`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hkn : k ≤ n) : carlesonSum (ℭ₆ k n j) f x = ∑ l < 4 * n + 12, carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x`
English: If $k \le n$, then for all $x$, $$\mathrm{carlesonSum}(\mathfrak{C}_6(k,n,j), f)(x) = \sum_{l < 4n+12} \mathrm{carlesonSum}\Big(\bigcup_{u \in \mathfrak{U}_4(k,n,j,l)} \mathfrak{T}_2(k,n,j,u), f\Big)(x).$$

### `lintegral_carlesonSum_forest`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * (2 ^ (2 * a + 5) * volume F / volume G) ^ (q⁻¹ - 2⁻¹) * volume F ^ (1 / 2) * volume G ^ (1 / 2)`
English: Let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $$\int_{G\setminus G'} \Big\|\mathrm{carlesonSum}\Big(\bigcup_{u \in \mathfrak{U}_4(k,n,j,l)} \mathfrak{T}_2(k,n,j,u), f\Big)(x)\Big\|\,dx \le C_{2.0.4}(a,q,n) \Big(\frac{2^{2a+5}\mu(F)}{\mu(G)}\Big)^{1/q - 1/2} \mu(F)^{1/2}\, \mu(G)^{1/2}.$$

### `lintegral_carlesonSum_forest'`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * 2 ^ (↑a + 5 / 2) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
English: Let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $$\int_{G\setminus G'} \Big\|\mathrm{carlesonSum}\Big(\bigcup_{u \in \mathfrak{U}_4(k,n,j,l)} \mathfrak{T}_2(k,n,j,u), f\Big)(x)\Big\|\,dx \le C_{2.0.4}(a,q,n)\, 2^{a+5/2}\, \mu(G)^{1-1/q}\, \mu(F)^{1/q}.$$

### `forest_union_optimized`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C5_1_2_optimized a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
English: Let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Then $$\int_{G\setminus G'} \|\mathrm{carlesonSum}(\mathfrak{P}_1, f)(x)\|\,dx \le C^{\mathrm{opt}}_{5.1.2}(a,q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where $C^{\mathrm{opt}}_{5.1.2}$ is `C5_1_2_optimized` and $q$ is `nnq X`.
