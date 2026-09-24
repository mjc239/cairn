You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `dach`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔄 : Set (𝔓 X)) (p : 𝔓 X) (g : X → ℂ) : ENNReal`
English: For a set of tiles $\mathfrak{A} \subseteq \mathfrak{P}(X)$, a tile $p$ and a function $g : X \to \mathbb{C}$, we define the quantity $h(p) = $ `dach 𝔄 p g` $\in [0, \infty]$ used in the proof of Lemma 6.1.4.

### `antichain_operator_le_volume`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (hf : Measurable f) (hfF : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hA : A ⊆ G) : ∫⁻ (x : X) in A, ‖carlesonSum 𝔄 f x‖ₑ ≤ ↑(C2_0_3 a (nnq X)) * dens₁ 𝔄 ^ ((q - 1) / (8 * ↑a ^ 4)) * dens₂ 𝔄 ^ (q⁻¹ - 2⁻¹) * volume F ^ (1 / 2) * volume G ^ (1 / 2)`
English: Let $\mathfrak{A} \subseteq \mathfrak{P}(X)$ be an antichain with respect to $\le$, let $f : X \to \mathbb{C}$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$, and let $A \subseteq G$. Then, with $q$ = `nnq X`,
$$\int_A |T_{\mathfrak{A}} f(x)|\,dx \le C_{2.0.3}(a, q)\, \operatorname{dens}_1(\mathfrak{A})^{\frac{q-1}{8a^4}}\, \operatorname{dens}_2(\mathfrak{A})^{\frac1q - \frac12}\, \mu(F)^{1/2}\, \mu(G)^{1/2},$$
where $T_{\mathfrak{A}} f$ is the Carleson sum `carlesonSum 𝔄 f`. This is a version of the antichain operator theorem controlling the integral of the norm, with the bound in terms of $\mu(F)$ and $\mu(G)$.

### `dens1_antichain_sq`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (hg : Measurable g) (hgG : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : eLpNorm (adjointCarlesonSum 𝔄 g) 2 volume ^ 2 ≤ (↑(C6_1_4 a) * dens₁ 𝔄 ^ (8 * ↑a ^ 4)⁻¹ * eLpNorm g 2 volume) ^ 2`
English: Let $\mathfrak{A} \subseteq \mathfrak{P}(X)$ be an antichain with respect to $\le$ and let $g : X \to \mathbb{C}$ be measurable with $\|g(x)\| \le \mathbf{1}_G(x)$ for all $x$. Then
$$\|T_{\mathfrak{A}}^* g\|_{L^2}^2 \le \big(C_{6.1.4}(a)\, \operatorname{dens}_1(\mathfrak{A})^{1/(8a^4)}\, \|g\|_{L^2}\big)^2,$$
where $T_{\mathfrak{A}}^* g$ is `adjointCarlesonSum 𝔄 g`.

### `dens1_antichain_dach`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hg : Measurable g) (hgG : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : eLpNorm (adjointCarlesonSum 𝔄 g) 2 volume ^ 2 ≤ ↑(Tile.C6_1_5 a) * 2 ^ (6 * a + 1) * ∑ p with p ∈ 𝔄, dach 𝔄 p g * ∫⁻ (y : X) in E p, ‖g y‖ₑ`
English: Let $g : X \to \mathbb{C}$ be measurable with $\|g(x)\| \le \mathbf{1}_G(x)$ for all $x$. Then for any set of tiles $\mathfrak{A}$,
$$\|T_{\mathfrak{A}}^* g\|_{L^2}^2 \le C_{6.1.5}(a)\, 2^{6a+1} \sum_{p \in \mathfrak{A}} h(p) \int_{E(p)} |g(y)|\,dy,$$
where $h(p)$ = `dach 𝔄 p g` and $T_{\mathfrak{A}}^* g$ is `adjointCarlesonSum 𝔄 g`.

### `dach_bound`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (mp : p ∈ 𝔄) (hg : Measurable g) (hgG : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) (hx : x₀ ∈ Metric.ball (𝔠 p) (14 * ↑(defaultD a) ^ 𝔰 p)) : dach 𝔄 p g ≤ ↑(C6_1_6 a) * dens₁ 𝔄 ^ (p₆ a)⁻¹ * M14 𝔄 (q₆ a) g x₀`
English: (Equations (6.1.34)–(6.1.37) in Lemma 6.1.4.) Let $\mathfrak{A}$ be an antichain with respect to $\le$, let $p \in \mathfrak{A}$, let $g : X \to \mathbb{C}$ be measurable with $\|g(x)\| \le \mathbf{1}_G(x)$ for all $x$, and let $x_0 \in B(\mathfrak{c}(p), 14 D^{s(p)})$, where $D$ = `defaultD a`. Then
$$h(p) \le C_{6.1.6}(a)\, \operatorname{dens}_1(\mathfrak{A})^{1/p_6(a)}\, M_{14}(\mathfrak{A}, q_6(a), g)(x_0),$$
where $h(p)$ = `dach 𝔄 p g` and $M_{14}$ is the maximal operator `M14`.

### `dens1_antichain`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (hf : Measurable f) (hfF : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (hgG : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum 𝔄 f x‖ₑ ≤ ↑(C6_1_4 a) * dens₁ 𝔄 ^ (8 * ↑a ^ 4)⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
English: (Lemma 6.1.4.) Let $\mathfrak{A} \subseteq \mathfrak{P}(X)$ be an antichain with respect to $\le$, and let $f, g : X \to \mathbb{C}$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ and $\|g(x)\| \le \mathbf{1}_G(x)$ for all $x$. Then
$$\Big| \int_X \overline{g(x)}\, T_{\mathfrak{A}} f(x)\,dx \Big| \le C_{6.1.4}(a)\, \operatorname{dens}_1(\mathfrak{A})^{1/(8a^4)}\, \|f\|_{L^2}\, \|g\|_{L^2}.$$

### `antichain_operator`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (hf : Measurable f) (hf1 : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (hg1 : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum 𝔄 f x‖ₑ ≤ ↑(C2_0_3 a (nnq X)) * dens₁ 𝔄 ^ ((q - 1) / (8 * ↑a ^ 4)) * dens₂ 𝔄 ^ (q⁻¹ - 2⁻¹) * eLpNorm f 2 volume * eLpNorm g 2 volume`
English: (Proposition 2.0.3.) Let $\mathfrak{A} \subseteq \mathfrak{P}(X)$ be an antichain with respect to $\le$, and let $f, g : X \to \mathbb{C}$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ and $\|g(x)\| \le \mathbf{1}_G(x)$ for all $x$. Then, with $q$ = `nnq X`,
$$\Big| \int_X \overline{g(x)}\, T_{\mathfrak{A}} f(x)\,dx \Big| \le C_{2.0.3}(a, q)\, \operatorname{dens}_1(\mathfrak{A})^{\frac{q-1}{8a^4}}\, \operatorname{dens}_2(\mathfrak{A})^{\frac1q - \frac12}\, \|f\|_{L^2}\, \|g\|_{L^2}.$$

### `antichain_operator'`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (hf : Measurable f) (hfF : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hA : A ⊆ G) : ∫⁻ (x : X) in A, ‖carlesonSum 𝔄 f x‖ₑ ≤ ↑(C2_0_3 a (nnq X)) * dens₁ 𝔄 ^ ((q - 1) / (8 * ↑a ^ 4)) * dens₂ 𝔄 ^ (q⁻¹ - 2⁻¹) * eLpNorm f 2 volume * volume G ^ (1 / 2)`
English: Let $\mathfrak{A} \subseteq \mathfrak{P}(X)$ be an antichain with respect to $\le$, let $f : X \to \mathbb{C}$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$, and let $A \subseteq G$. Then, with $q$ = `nnq X`,
$$\int_A |T_{\mathfrak{A}} f(x)|\,dx \le C_{2.0.3}(a, q)\, \operatorname{dens}_1(\mathfrak{A})^{\frac{q-1}{8a^4}}\, \operatorname{dens}_2(\mathfrak{A})^{\frac1q - \frac12}\, \|f\|_{L^2}\, \mu(G)^{1/2}.$$
This is a version of the antichain operator theorem controlling the integral of the norm.
