You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ap_in_ff`
Lean: `[Module (ZMod q) G] (S : Finset G) (hq : Nat.Prime q) (hα₀ : 0 < α) (hα₂ : α ≤ 2⁻¹) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (hαA₁ : α ≤ ↑A₁.dens) (hαA₂ : α ≤ ↑A₂.dens) : ∃ V x, ↑(Module.finrank (ZMod q) G - Module.finrank (ZMod q) ↥V) ≤ 2 ^ 32 * (1 + Real.log α⁻¹) ^ 2 * (1 + Real.log (ε * α)⁻¹) ^ 2 * ε⁻¹ ^ 2 ∧ |∑ x_1 ∈ S, (mu (↑V).toFinset ∗ᵈ mu A₁ ∗ᵈ mu A₂) x_1 - ∑ x ∈ S, (mu A₁ ∗ᵈ mu A₂) x| ≤ ε`
English: Let $q$ be a prime and let $G$ be a finite vector space over $\mathbb{Z}/q\mathbb{Z}$. Let $S, A_1, A_2 \subseteq G$ be finite sets, and let $0 < \alpha \le 1/2$ and $0 < \varepsilon \le 1$ with $\alpha \le \operatorname{dens}(A_1)$ and $\alpha \le \operatorname{dens}(A_2)$. Then there is a subspace $V \le G$ with $\dim G - \dim V \le 2^{32}\,(1 + \log \alpha^{-1})^2\,(1 + \log (\varepsilon\alpha)^{-1})^2\,\varepsilon^{-2}$ and $\left|\sum_{x \in S} (\mu_V * \mu_{A_1} * \mu_{A_2})(x) - \sum_{x \in S} (\mu_{A_1} * \mu_{A_2})(x)\right| \le \varepsilon$, where $\mu_X$ is the normalised indicator of $X$ and $*$ is discrete convolution.

### `global_dichotomy`
Lean: `[DiscreteMeasurableSpace G] (hA : A.Nonempty) (hγC : γ ≤ ↑C.dens) (hγ : 0 < γ) (hAC : ε ≤ |↑(Fintype.card G) * ⟪mu A ∗ᵈ mu A, mu C⟫_[ℝ] - 1|) : ε / (2 * ↑(Fintype.card G)) ≤ ‖Fintype.balance (mu A) ○ᵈ Fintype.balance (mu A)‖_[↑(2 * ⌈1 + Real.log γ⁻¹⌉₊), mu Finset.univ]`
English: $G$ carries the discrete measurable structure (and is finite). Let $A, C \subseteq G$ with $A$ nonempty, let $0 < \gamma \le \operatorname{dens}(C)$, and suppose $\varepsilon \le \left| |G|\,\langle \mu_A * \mu_A, \mu_C\rangle - 1 \right|$. Then $\dfrac{\varepsilon}{2|G|} \le \|\operatorname{bal}(\mu_A) \circ \operatorname{bal}(\mu_A)\|_{p, \mu_G}$, where $p = 2\lceil 1 + \log \gamma^{-1}\rceil$ (natural-number ceiling), $\operatorname{bal}(f) = f - \mathbb{E} f$ is the balanced function, $\circ$ is the discrete difference convolution, and $\|\cdot\|_{p,\mu_G}$ is the $L^p$ norm weighted by the uniform density $\mu_G$ on $G$.

### `di_in_ff`
Lean: `[Module (ZMod q) G] [DiscreteMeasurableSpace G] (hq : Nat.Prime q) (hε₀ : 0 < ε) (hε₁ : ε < 1) (hγC : γ ≤ ↑C.dens) (hγ : 0 < γ) (hAC : ε ≤ |↑(Fintype.card G) * ⟪mu A ∗ᵈ mu A, mu C⟫_[ℝ] - 1|) : ∃ V x, ↑(Module.finrank (ZMod q) G - Module.finrank (ZMod q) ↥V) ≤ 2 ^ 128 * (1 + Real.log (↑A.dens)⁻¹) ^ 4 * (1 + Real.log γ⁻¹) ^ 4 / ε ^ 12 ∧ (1 + ε / 32) * ↑A.dens ≤ ‖((↑A).indicator fun x => 1) ∗ᵈ mu (↑V).toFinset‖_[⊤]`
English: Let $q$ be a prime and let $G$ be a finite vector space over $\mathbb{Z}/q\mathbb{Z}$ carrying the discrete measurable structure. Let $A, C \subseteq G$, $0 < \varepsilon < 1$, $0 < \gamma \le \operatorname{dens}(C)$, and suppose $\varepsilon \le \left| |G|\,\langle \mu_A * \mu_A, \mu_C\rangle - 1 \right|$. Then there is a subspace $V \le G$ with $\dim G - \dim V \le 2^{128}\,(1 + \log \operatorname{dens}(A)^{-1})^4\,(1 + \log \gamma^{-1})^4 / \varepsilon^{12}$ and $(1 + \varepsilon/32)\operatorname{dens}(A) \le \|1_A * \mu_V\|_\infty$.

### `ff`
Lean: `[Module (ZMod q) G] (hq₃ : 3 ≤ q) (hq : Nat.Prime q) (hA₀ : A.Nonempty) (hA : ThreeAPFree ↑A) : ↑(Module.finrank (ZMod q) G) ≤ 2 ^ 148 * (1 + Real.log (↑A.dens)⁻¹) ^ 9`
English: Let $q \ge 3$ be a prime and let $G$ be a finite vector space over $\mathbb{Z}/q\mathbb{Z}$. If $A \subseteq G$ is nonempty and contains no nontrivial three-term arithmetic progression, then $\dim G \le 2^{148}\,(1 + \log \operatorname{dens}(A)^{-1})^9$.
