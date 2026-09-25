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

### `forest_complement`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ ↑(C5_1_3 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {f : X → ℂ}, (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → Measurable f → ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ ↑(C5_1_3 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Docstring: Lemma 5.1.3, proving the bound on the integral of the Carleson sum over all leftover tiles which do not fit in a forest. It follows from a careful grouping of these tiles into finitely many antichains.
Previous English: (Lemma 5.1.3) Let $f$ be a measurable function with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Then the integral over $G \setminus G'$ of the Carleson sum over the tiles not in $\mathfrak{P}_1$ satisfies $$\int_{G\setminus G'} \Big\|\sum_{p \in \mathfrak{P}_1^c} T_p f(x)\Big\|\,dx \le C_{5.1.3}(a, q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where $q$ is the exponent `nnq X` and $C_{5.1.3}(a,q)$ is the constant `C5_1_3`.
Checker's issue: Omits the standing assumptions ProofData a q K σ₁ σ₂ F G and TileStructure (metric space X, doubling measure, tile structure).

### `lintegral_enorm_carlesonSum_le_of_isAntichain_subset_ℭ`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) (hA : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (h'A : 𝔄 ⊆ ℭ k n) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔄) f x‖ₑ ≤ ↑(C2_0_3 a (nnq X)) * 2 ^ (a + 3) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹ * 2 ^ (-((q - 1) / (8 * ↑a ^ 4) * ↑n))`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {k n : ℕ} {f : X → ℂ} {𝔄 : Set (𝔓 X)}, (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → Measurable f → IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄 → 𝔄 ⊆ ℭ k n → ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔄) f x‖ₑ ≤ ↑(C2_0_3 a (nnq X)) * 2 ^ (a + 3) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹ * 2 ^ (-((q - 1) / (8 * ↑a ^ 4) * ↑n))`
Docstring: Custom version of the antichain operator theorem, in the specific form we need to handle the various terms in the previous statement.
Previous English: Let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$, and let $\mathfrak{A}$ be an antichain (for $\le$ on tiles) with $\mathfrak{A} \subseteq \mathfrak{C}(k,n)$. Then $$\int_{G\setminus G'} \|\mathrm{carlesonSum}(\mathfrak{P}_{pos} \cap \mathfrak{P}_1^c \cap \mathfrak{A}, f)(x)\|\,dx \le C_{2.0.3}(a,q)\, 2^{a+3}\, \mu(G)^{1-1/q}\, \mu(F)^{1/q}\, 2^{-\frac{q-1}{8a^4} n},$$ where $\mathfrak{P}_{pos}$ is `𝔓pos` and $q$ is `nnq X`.
Checker's issue: Omits the standing assumptions ProofData a q K σ₁ σ₂ F G and TileStructure (metric space X, doubling measure, tile structure).

### `forest_complement_optimized`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ ↑(C5_1_3_optimized a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] {f : X → ℂ}, (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → Measurable f → ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ ↑(C5_1_3_optimized a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Previous English: Let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Then $$\int_{G\setminus G'} \|\mathrm{carlesonSum}(\mathfrak{P}_1^c, f)(x)\|\,dx \le C^{\mathrm{opt}}_{5.1.3}(a, q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where $C^{\mathrm{opt}}_{5.1.3}$ is the constant `C5_1_3_optimized` and $q$ is `nnq X`.
Checker's issue: Omits the standing assumptions ProofData a q K σ₁ σ₂ F G and TileStructure (metric space X, doubling measure, tile structure).
