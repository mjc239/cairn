You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `holder_van_der_corput`
Lean: `[ProofData a q K σ₁ σ₂ F G] (φ_supp : Function.support φ ⊆ Metric.ball z R) : ‖∫ (x : X), Complex.exp (Complex.I * (↑(f x) - ↑(g x))) * φ x‖ₑ ≤ ↑(C2_0_5 ↑a) * volume (Metric.ball z R) * iHolENorm φ z (2 * R) (defaultτ a) * (1 + edist_{z, R} f g) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹)`
English: (Proposition 2.0.5) Suppose $\operatorname{supp}\varphi\subseteq B(z,R)$. Then $$\Big\|\int_X e^{i(f(x)-g(x))}\varphi(x)\,dx\Big\|\le C_{2.0.5}(a)\,\mu(B(z,R))\,\|\varphi\|_{\mathrm{iHol}(z,2R,\tau)}\,\big(1+d_{z,R}(f,g)\big)^{-1/(2a^2+a^3)},$$ where $\tau=\tau(a)$ is the default Hölder exponent, $\|\varphi\|_{\mathrm{iHol}(z,2R,\tau)}$ is the (extended) inhomogeneous $\tau$-Hölder norm $\mathrm{iHolENorm}\,\varphi\,z\,(2R)\,\tau$ on the ball $B(z,2R)$, and $d_{z,R}$ is the (extended) distance between $f$ and $g$ on $B(z,R)$.
