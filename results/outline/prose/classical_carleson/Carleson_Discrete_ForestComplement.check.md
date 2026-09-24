You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `forest_complement`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ ↑(C5_1_3 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
English: (Lemma 5.1.3) Let $f$ be a measurable function with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Then the integral over $G \setminus G'$ of the Carleson sum over the tiles not in $\mathfrak{P}_1$ satisfies $$\int_{G\setminus G'} \Big\|\sum_{p \in \mathfrak{P}_1^c} T_p f(x)\Big\|\,dx \le C_{5.1.3}(a, q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where $q$ is the exponent `nnq X` and $C_{5.1.3}(a,q)$ is the constant `C5_1_3`.

### `𝔓pos`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : Set (𝔓 X)`
English: The set $\mathfrak{P}_{G\setminus G'}$ of the blueprint: a distinguished subset of the tiles $\mathfrak{P}(X)$ (`𝔓pos`).

### `lintegral_carlesonSum_𝔓₁_compl_le_sum_lintegral`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ (((∑ n ≤ maxℭ X, ∑ k ≤ n, ∑ l < n, ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔏₀' k n l) f x‖ₑ) + ∑ n ≤ maxℭ X, ∑ k ≤ n, ∑ j ≤ 2 * n + 3, ∑ l ≤ defaultZ a * (n + 1), ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔏₁ k n j l) f x‖ₑ) + ∑ n ≤ maxℭ X, ∑ k ≤ n, ∑ j ≤ 2 * n + 3, ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔏₂ k n j) f x‖ₑ) + ∑ n ≤ maxℭ X, ∑ k ≤ n, ∑ j ≤ 2 * n + 3, ∑ l ≤ defaultZ a * (n + 1), ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔏₃ k n j l) f x‖ₑ`
English: Assume the standing data of the Carleson setup (ProofData with parameters $a,q,K,\sigma_1,\sigma_2,F,G$) and a tile structure with the default parameters $D$, $\kappa$, $S$ and $o$ = cancelPt. Let $f$ be measurable. Then $\int_{G\setminus G'} \|\mathrm{carlesonSum}(\mathfrak{P}_1^c, f)(x)\|\,dx$ (a lower Lebesgue integral of extended norms) is at most the sum of the following four terms, where every integral is over $G \setminus G'$ and $\mathfrak{P}_{pos}$ denotes `𝔓pos`: (i) $\sum_{n \le \mathrm{max}\mathfrak{C}} \sum_{k \le n} \sum_{l < n} \int \|\mathrm{carlesonSum}(\mathfrak{P}_{pos} \cap \mathfrak{P}_1^c \cap \mathfrak{L}_0'(k,n,l), f)(x)\|\,dx$; (ii) $\sum_{n \le \mathrm{max}\mathfrak{C}} \sum_{k \le n} \sum_{j \le 2n+3} \sum_{l \le Z(n+1)} \int \|\mathrm{carlesonSum}(\mathfrak{P}_{pos} \cap \mathfrak{P}_1^c \cap \mathfrak{L}_1(k,n,j,l), f)(x)\|\,dx$; (iii) $\sum_{n \le \mathrm{max}\mathfrak{C}} \sum_{k \le n} \sum_{j \le 2n+3} \int \|\mathrm{carlesonSum}(\mathfrak{P}_{pos} \cap \mathfrak{P}_1^c \cap \mathfrak{L}_2(k,n,j), f)(x)\|\,dx$; (iv) $\sum_{n \le \mathrm{max}\mathfrak{C}} \sum_{k \le n} \sum_{j \le 2n+3} \sum_{l \le Z(n+1)} \int \|\mathrm{carlesonSum}(\mathfrak{P}_{pos} \cap \mathfrak{P}_1^c \cap \mathfrak{L}_3(k,n,j,l), f)(x)\|\,dx$. Here $\mathrm{max}\mathfrak{C}$ is `maxℭ X` and $Z$ is `defaultZ a`.

### `lintegral_enorm_carlesonSum_le_of_isAntichain_subset_ℭ`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) (hA : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (h'A : 𝔄 ⊆ ℭ k n) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔄) f x‖ₑ ≤ ↑(C2_0_3 a (nnq X)) * 2 ^ (a + 3) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹ * 2 ^ (-((q - 1) / (8 * ↑a ^ 4) * ↑n))`
English: Let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$, and let $\mathfrak{A}$ be an antichain (for $\le$ on tiles) with $\mathfrak{A} \subseteq \mathfrak{C}(k,n)$. Then $$\int_{G\setminus G'} \|\mathrm{carlesonSum}(\mathfrak{P}_{pos} \cap \mathfrak{P}_1^c \cap \mathfrak{A}, f)(x)\|\,dx \le C_{2.0.3}(a,q)\, 2^{a+3}\, \mu(G)^{1-1/q}\, \mu(F)^{1/q}\, 2^{-\frac{q-1}{8a^4} n},$$ where $\mathfrak{P}_{pos}$ is `𝔓pos` and $q$ is `nnq X`.

### `forest_complement_optimized`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ ↑(C5_1_3_optimized a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
English: Let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Then $$\int_{G\setminus G'} \|\mathrm{carlesonSum}(\mathfrak{P}_1^c, f)(x)\|\,dx \le C^{\mathrm{opt}}_{5.1.3}(a, q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where $C^{\mathrm{opt}}_{5.1.3}$ is the constant `C5_1_3_optimized` and $q$ is `nnq X`.
