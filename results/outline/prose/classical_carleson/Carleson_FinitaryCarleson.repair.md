You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): TileStructure, MeasureTheory, Antichain.

### `finitary_carleson`
Lean (short): `(X : Type u_1) [ProofData a q K σ₁ σ₂ F G] : ∃ G', MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → ∫⁻ (x : X) in G \ G', ‖∑ s ∈ (Set.Icc (σ₁ x) (σ₂ x)).toFinset, ∫ (y : X), Ks s x y * f y * Complex.exp (Complex.I * ↑((Q x) y))‖ₑ ≤ ↑(C2_0_1 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ (X : Type u_1) {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G], ∃ G', MeasurableSet G' ∧ HMul.hMul (β := ENNReal) (2 : ENNReal) ((volume : Measure X) G' : ENNReal) ≤ (volume : Measure X) G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → ∫⁻ (x : X) in G \ G', enorm (E := ℂ) (∑ s ∈ (Set.Icc (σ₁ x) (σ₂ x)).toFinset, @integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => Ks s x y * f y * Complex.exp (Complex.I * ↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y))) ≤ ↑(C2_0_1 a (nnq X (F := F) (G := G))) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹`
Docstring: Proposition 2.0.1
Previous English: (Proposition 2.0.1) In the given setting on $X$ (with sets $F$, $G$, exponent $q$ = `nnq X`, scale functions $\sigma_1, \sigma_2$, kernels $K_s$ and the function $Q$), there exists a measurable set $G' \subseteq X$ with $2\mu(G') \le \mu(G)$ such that for every measurable $f : X \to \mathbb{C}$ with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$, $$\int_{G \setminus G'} \Big\| \sum_{s = \sigma_1(x)}^{\sigma_2(x)} \int_X K_s(x,y)\, f(y)\, e^{i Q(x)(y)}\,dy \Big\|\,dx \le C_{2.0.1}(a,q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where $C_{2.0.1}$ is the constant `C2_0_1`.
Checker's issue: The English says only 'the given setting on X', so it never names the ProofData standing-assumption bundle or the metric space structure on X.
