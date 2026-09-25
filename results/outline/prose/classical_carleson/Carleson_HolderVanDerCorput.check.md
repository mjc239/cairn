You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. Compare the
English with the full statement; anything the English attributes to the docstring must actually be in it.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Definitions are held to the same standard: the English must name the setting the signature assumes
("for an abelian group $G$ and …, $\mathrm{rdist}$ is …"). Replacing an assumption by a stronger one (a metric
space where the Lean has a pseudometric space) is unfaithful too, and so is leaving a restrictive type unstated
(a natural number, a nonnegative real). Citations (theorem or lemma numbers) and remarks are claims too: each must
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: when the
prompt shows neither its definition nor a docstring saying it, the English must not supply one. Every variable
needs its type ("$f : G \to \mathbb{C}$", "$m$ a natural number"), every symbol must be introduced (notation such
as $M_{\mathcal B}$ included), and no letter may mean two things. When in doubt, flag it: a false alarm costs one
repair, a missed error stays in the outline. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `holder_van_der_corput`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] (φ_supp : Function.support φ ⊆ Metric.ball z R) : ‖∫ (x : X), Complex.exp (Complex.I * (↑(f x) - ↑(g x))) * φ x‖ₑ ≤ ↑(C2_0_5 ↑a) * volume (Metric.ball z R) * iHolENorm φ z (2 * R) (defaultτ a) * (1 + edist_{z, R} f g) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] {z : X} {R : ℝ} {φ : X → ℂ}, Function.support φ ⊆ Metric.ball z R → ∀ {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => Complex.exp (Complex.I * (↑(f x) - ↑(g x))) * φ x) ≤ HMul.hMul (β := ENNReal) ↑(C2_0_5 ↑a) ((volume : Measure X) (Metric.ball z R) : ENNReal) * iHolENorm φ z ((2 : ℝ) * R) (defaultτ a) * ((1 : ENNReal) + edist_{z, R} f g) ^ (-((2 : ℝ) * HPow.hPow (α := ℝ) ↑a (2 : ℕ) + HPow.hPow (α := ℝ) ↑a (3 : ℕ))⁻¹)`
Docstring: Proposition 2.0.5.
English: (Proposition 2.0.5) Under the standing assumptions of the proof (the data $a\in\mathbb N$, $q$, $K$, $\sigma_1$, $\sigma_2$, $F$, $G$ of `ProofData` on the metric space $X$, which is then a doubling metric measure space with measure $\mu$ and a compatible family $\Theta(X)$ of functions), let $z\in X$, $R\in\mathbb R$, and let $\varphi:X\to\mathbb C$ with $\operatorname{supp}\varphi\subseteq B(z,R)$. Then for all $f,g\in\Theta(X)$, $$\Big\|\int_X e^{i(f(x)-g(x))}\varphi(x)\,d\mu(x)\Big\|\le C_{2.0.5}(a)\,\mu(B(z,R))\,\|\varphi\|_{\mathrm{iHol}(z,2R,\tau)}\,\big(1+d_{z,R}(f,g)\big)^{-1/(2a^2+a^3)},$$ where $\tau=\tau(a)$ is the default Hölder exponent, $\|\varphi\|_{\mathrm{iHol}(z,2R,\tau)}$ is the (extended) inhomogeneous $\tau$-Hölder norm $\mathrm{iHolENorm}\,\varphi\,z\,(2R)\,\tau$ on the ball $B(z,2R)$, and $d_{z,R}$ is the (extended) distance between $f$ and $g$ on $B(z,R)$.
