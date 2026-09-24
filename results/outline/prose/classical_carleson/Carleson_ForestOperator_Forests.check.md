You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `forest_operator_le_volume`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔉 : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hA : MeasurableSet A) (sA : A ⊆ G) : ∫⁻ (x : X) in A, ‖∑ u with u ∈ 𝔉, carlesonSum ((fun x => 𝔉.𝔗 x) u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * dens₂ (⋃ u ∈ 𝔉, (fun x => 𝔉.𝔗 x) u) ^ (q⁻¹ - 2⁻¹) * volume F ^ (1 / 2) * volume A ^ (1 / 2)`
English: Let $\mathfrak{F}$ be an $n$-forest, $f$ measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$, and $A$ a measurable set with $A \subseteq G$. Then $$\int_A \Big\|\sum_{u \in \mathfrak{F}} \mathrm{carlesonSum}(\mathfrak{T}(u), f)(x)\Big\|\,dx \le C_{2.0.4}(a,q,n)\, \mathrm{dens}_2\Big(\bigcup_{u \in \mathfrak{F}} \mathfrak{T}(u)\Big)^{1/q - 1/2}\, \mu(F)^{1/2}\, \mu(A)^{1/2}.$$

### `TileStructure.Forest.forest_operator_f`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (t : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * ∑ u with u ∈ t, carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C2_0_4_aux a) * dens₂ (⋃ u ∈ t, (fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
English: (The $f$ side of Proposition 2.0.4) Let $t$ be an $n$-forest, $f$ measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ and $g$ measurable with $\|g(x)\| \le \mathbf{1}_G(x)$ for all $x$. Then $$\Big|\int_X \overline{g(x)} \sum_{u \in t} \mathrm{carlesonSum}(\mathfrak{T}(u), f)(x)\,dx\Big| \le C_{2.0.4}^{\mathrm{aux}}(a)\, \mathrm{dens}_2\Big(\bigcup_{u \in t}\mathfrak{T}(u)\Big)^{1/2}\, \|f\|_{L^2}\, \|g\|_{L^2},$$ where $C_{2.0.4}^{\mathrm{aux}}$ is `Forest.C2_0_4_aux`.

### `TileStructure.Forest.rowDecomp_𝔘`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (t : Forest X n) (j : ℕ) : Set (𝔓 X)`
English: For an $n$-forest $t$ and $j \in \mathbb{N}$, the set of tiles $\mathrm{rowDecomp}_{\mathfrak{U}}(t, j)$: the set of tree tops forming the $j$-th row in the row decomposition of $t$.

### `TileStructure.Forest.rowDecomp`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (t : Forest X n) (j : ℕ) : Row X n`
English: For an $n$-forest $t$ and $j \in \mathbb{N}$, the $j$-th $n$-row of the row decomposition of $t$, as defined in the proof of Lemma 7.7.1 (with indexing shifted by one relative to the blueprint).

### `TileStructure.Forest.indicator_row_bound`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) : eLpNorm (F.indicator (t.adjointCarlesonRowSum j g)) 2 volume ≤ ↑(Forest.C7_7_2_2 a n) * dens₂ (⋃ u ∈ t, (fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm g 2 volume`
English: Let $t$ be an $n$-forest, $j \in \mathbb{N}$, and let $g$ be bounded with compact support and $\operatorname{supp} g \subseteq G$. Then $$\big\|\mathbf{1}_F \cdot \mathrm{adjointCarlesonRowSum}_t(j, g)\big\|_{L^2} \le C_{7.7.2.2}(a,n)\, \mathrm{dens}_2\Big(\bigcup_{u \in t}\mathfrak{T}(u)\Big)^{1/2}\, \|g\|_{L^2},$$ where $C_{7.7.2.2}$ is `Forest.C7_7_2_2`.

### `TileStructure.Forest.forest_operator_f_inner`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : eLpNorm (G.indicator (t.carlesonRowSum j f)) 2 volume ≤ ↑(Forest.C7_7_2_2 a n) * dens₂ (⋃ u ∈ t, (fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume`
English: Let $t$ be an $n$-forest, $j \in \mathbb{N}$, and $f$ measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $$\big\|\mathbf{1}_G \cdot \mathrm{carlesonRowSum}_t(j, f)\big\|_{L^2} \le C_{7.7.2.2}(a,n)\, \mathrm{dens}_2\Big(\bigcup_{u \in t}\mathfrak{T}(u)\Big)^{1/2}\, \|f\|_{L^2}.$$

### `TileStructure.Forest.forest_operator_g_main`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : eLpNorm (fun x => ∑ u with u ∈ t, adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) 2 volume ^ 2 ≤ (↑(Forest.G2_0_4 a n) * eLpNorm g 2 volume) ^ 2`
English: Let $t$ be an $n$-forest and $g$ measurable with $\|g(x)\| \le \mathbf{1}_G(x)$ for all $x$. Then $$\Big\|\sum_{u \in t} \mathrm{adjointCarlesonSum}(\mathfrak{T}(u), g)\Big\|_{L^2}^2 \le \big(G_{2.0.4}(a,n)\, \|g\|_{L^2}\big)^2,$$ where $G_{2.0.4}$ is the constant `Forest.G2_0_4`.

### `TileStructure.Forest.correlation_separated_trees_of_subset`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hg₁ : BoundedCompactSupport g₁ volume) (hg₂ : BoundedCompactSupport g₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁) g₁ x * (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u₂) g₂ x)‖ₑ ≤ ↑(Forest.C7_4_4 a n) * eLpNorm (fun x => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator u₁ g₁) x) 2 volume * eLpNorm (fun x => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator u₂ g₂) x) 2 volume`
English: Let $t$ be an $n$-forest, $u_1, u_2 \in t$ with $u_1 \ne u_2$ and $\mathcal{I}(u_1) \le \mathcal{I}(u_2)$, and let $g_1, g_2$ be bounded with compact support. Then $$\Big|\int_X T^*_{\mathfrak{T}(u_1)} g_1(x)\, \overline{T^*_{\mathfrak{T}(u_2)} g_2(x)}\,dx\Big| \le C_{7.4.4}(a,n)\, \big\|\mathbf{1}_{\mathcal{I}(u_1)\cap\mathcal{I}(u_2)} \cdot \mathrm{adjointBoundaryOperator}_t(u_1, g_1)\big\|_{L^2}\, \big\|\mathbf{1}_{\mathcal{I}(u_1)\cap\mathcal{I}(u_2)} \cdot \mathrm{adjointBoundaryOperator}_t(u_2, g_2)\big\|_{L^2},$$ where $T^*_{\mathfrak{T}(u)}$ denotes `adjointCarlesonSum` over $\mathfrak{T}(u)$ and $C_{7.4.4}$ is `Forest.C7_4_4`.

### `TileStructure.Forest.correlation_separated_trees`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (hg₁ : BoundedCompactSupport g₁ volume) (hg₂ : BoundedCompactSupport g₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁) g₁ x * (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u₂) g₂ x)‖ₑ ≤ ↑(Forest.C7_4_4 a n) * eLpNorm (fun x => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator u₁ g₁) x) 2 volume * eLpNorm (fun x => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator u₂ g₂) x) 2 volume`
English: (Lemma 7.4.4) Let $t$ be an $n$-forest, $u_1, u_2 \in t$ with $u_1 \ne u_2$, and let $g_1, g_2$ be bounded with compact support. Then $$\Big|\int_X T^*_{\mathfrak{T}(u_1)} g_1(x)\, \overline{T^*_{\mathfrak{T}(u_2)} g_2(x)}\,dx\Big| \le C_{7.4.4}(a,n)\, \big\|\mathbf{1}_{\mathcal{I}(u_1)\cap\mathcal{I}(u_2)} \cdot \mathrm{adjointBoundaryOperator}_t(u_1, g_1)\big\|_{L^2}\, \big\|\mathbf{1}_{\mathcal{I}(u_1)\cap\mathcal{I}(u_2)} \cdot \mathrm{adjointBoundaryOperator}_t(u_2, g_2)\big\|_{L^2}.$$

### `TileStructure.Forest.row_correlation`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (lj : j < 2 ^ n) (lj' : j' < 2 ^ n) (hn : j ≠ j') (hf₁ : BoundedCompactSupport f₁ volume) (nf₁ : Function.support f₁ ⊆ G) (hf₂ : BoundedCompactSupport f₂ volume) (nf₂ : Function.support f₂ ⊆ G) : ‖∫ (x : X), t.adjointCarlesonRowSum j f₁ x * (starRingEnd ℂ) (t.adjointCarlesonRowSum j' f₂ x)‖ₑ ≤ ↑(Forest.C7_7_3 a n) * eLpNorm f₁ 2 volume * eLpNorm f₂ 2 volume`
English: (Lemma 7.7.3) Let $t$ be an $n$-forest, $j, j' < 2^n$ with $j \ne j'$, and let $f_1, f_2$ be bounded with compact support, with $\operatorname{supp} f_1 \subseteq G$ and $\operatorname{supp} f_2 \subseteq G$. Then $$\Big|\int_X \mathrm{adjointCarlesonRowSum}_t(j, f_1)(x)\, \overline{\mathrm{adjointCarlesonRowSum}_t(j', f_2)(x)}\,dx\Big| \le C_{7.7.3}(a,n)\, \|f_1\|_{L^2}\, \|f_2\|_{L^2},$$ where $C_{7.7.3}$ is `Forest.C7_7_3`.

### `TileStructure.Forest.forest_operator_g`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (t : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * ∑ u with u ∈ t, carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.G2_0_4 a n) * eLpNorm f 2 volume * eLpNorm g 2 volume`
English: (The $g$ side of Proposition 2.0.4) Let $t$ be an $n$-forest, $f$ measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ and $g$ measurable with $\|g(x)\| \le \mathbf{1}_G(x)$ for all $x$. Then $$\Big|\int_X \overline{g(x)} \sum_{u \in t} \mathrm{carlesonSum}(\mathfrak{T}(u), f)(x)\,dx\Big| \le G_{2.0.4}(a,n)\, \|f\|_{L^2}\, \|g\|_{L^2}.$$

### `forest_operator`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔉 : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * ∑ u with u ∈ 𝔉, carlesonSum ((fun x => 𝔉.𝔗 x) u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * dens₂ (⋃ u ∈ 𝔉, (fun x => 𝔉.𝔗 x) u) ^ (q⁻¹ - 2⁻¹) * eLpNorm f 2 volume * eLpNorm g 2 volume`
English: (Forest operator estimate) Let $\mathfrak{F}$ be an $n$-forest, $f$ measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ and $g$ measurable with $\|g(x)\| \le \mathbf{1}_G(x)$ for all $x$. Then $$\Big|\int_X \overline{g(x)} \sum_{u \in \mathfrak{F}} \mathrm{carlesonSum}(\mathfrak{T}(u), f)(x)\,dx\Big| \le C_{2.0.4}(a,q,n)\, \mathrm{dens}_2\Big(\bigcup_{u \in \mathfrak{F}} \mathfrak{T}(u)\Big)^{1/q - 1/2}\, \|f\|_{L^2}\, \|g\|_{L^2}.$$

### `forest_operator'`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔉 : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hA : MeasurableSet A) (sA : A ⊆ G) : ∫⁻ (x : X) in A, ‖∑ u with u ∈ 𝔉, carlesonSum ((fun x => 𝔉.𝔗 x) u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * dens₂ (⋃ u ∈ 𝔉, (fun x => 𝔉.𝔗 x) u) ^ (q⁻¹ - 2⁻¹) * eLpNorm f 2 volume * volume A ^ (1 / 2)`
English: Let $\mathfrak{F}$ be an $n$-forest, $f$ measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$, and $A$ a measurable set with $A \subseteq G$. Then $$\int_A \Big\|\sum_{u \in \mathfrak{F}} \mathrm{carlesonSum}(\mathfrak{T}(u), f)(x)\Big\|\,dx \le C_{2.0.4}(a,q,n)\, \mathrm{dens}_2\Big(\bigcup_{u \in \mathfrak{F}} \mathfrak{T}(u)\Big)^{1/q - 1/2}\, \|f\|_{L^2}\, \mu(A)^{1/2}.$$
