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

### `holder_van_der_corput`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] (φ_supp : Function.support φ ⊆ Metric.ball z R) : ‖∫ (x : X), Complex.exp (Complex.I * (↑(f x) - ↑(g x))) * φ x‖ₑ ≤ ↑(C2_0_5 ↑a) * volume (Metric.ball z R) * iHolENorm φ z (2 * R) (defaultτ a) * (1 + edist_{z, R} f g) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] {z : X} {R : ℝ} {φ : X → ℂ}, Function.support φ ⊆ Metric.ball z R → ∀ {f g : Θ X}, ‖∫ (x : X), Complex.exp (Complex.I * (↑(f x) - ↑(g x))) * φ x‖ₑ ≤ ↑(C2_0_5 ↑a) * volume (Metric.ball z R) * iHolENorm φ z (2 * R) (defaultτ a) * (1 + edist_{z, R} f g) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹)`
Docstring: Proposition 2.0.5.
Previous English: (Proposition 2.0.5) Suppose $\operatorname{supp}\varphi\subseteq B(z,R)$. Then $$\Big\|\int_X e^{i(f(x)-g(x))}\varphi(x)\,dx\Big\|\le C_{2.0.5}(a)\,\mu(B(z,R))\,\|\varphi\|_{\mathrm{iHol}(z,2R,\tau)}\,\big(1+d_{z,R}(f,g)\big)^{-1/(2a^2+a^3)},$$ where $\tau=\tau(a)$ is the default Hölder exponent, $\|\varphi\|_{\mathrm{iHol}(z,2R,\tau)}$ is the (extended) inhomogeneous $\tau$-Hölder norm $\mathrm{iHolENorm}\,\varphi\,z\,(2R)\,\tau$ on the ball $B(z,2R)$, and $d_{z,R}$ is the (extended) distance between $f$ and $g$ on $B(z,R)$.
Checker's issue: Omits the standing assumptions (metric space X and ProofData instance) under which the statement is proved.
