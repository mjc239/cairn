You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption) and the English. Compare the English with the full statement.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `finitary_carleson`
Lean (short): `(X : Type u_1) [ProofData a q K σ₁ σ₂ F G] : ∃ G', MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → ∫⁻ (x : X) in G \ G', ‖∑ s ∈ (Set.Icc (σ₁ x) (σ₂ x)).toFinset, ∫ (y : X), Ks s x y * f y * Complex.exp (Complex.I * ↑((Q x) y))‖ₑ ≤ ↑(C2_0_1 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ (X : Type u_1) {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G], ∃ G', MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → ∫⁻ (x : X) in G \ G', ‖∑ s ∈ (Set.Icc (σ₁ x) (σ₂ x)).toFinset, ∫ (y : X), Ks s x y * f y * Complex.exp (Complex.I * ↑((Q x) y))‖ₑ ≤ ↑(C2_0_1 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
English: (Proposition 2.0.1) In the given setting on $X$ (with sets $F$, $G$, exponent $q$ = `nnq X`, scale functions $\sigma_1, \sigma_2$, kernels $K_s$ and the function $Q$), there exists a measurable set $G' \subseteq X$ with $2\mu(G') \le \mu(G)$ such that for every measurable $f : X \to \mathbb{C}$ with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$, $$\int_{G \setminus G'} \Big\| \sum_{s = \sigma_1(x)}^{\sigma_2(x)} \int_X K_s(x,y)\, f(y)\, e^{i Q(x)(y)}\,dy \Big\|\,dx \le C_{2.0.1}(a,q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where $C_{2.0.1}$ is the constant `C2_0_1`.
