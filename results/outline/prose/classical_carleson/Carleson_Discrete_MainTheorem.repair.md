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

### `discrete_carleson`
Lean (short): `(X : Type u_1) [ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : ∃ G', MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → ∫⁻ (x : X) in G \ G', ‖carlesonSum Set.univ f x‖ₑ ≤ ↑(C2_0_2 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ (X : Type u_1) {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)], ∃ G', MeasurableSet G' ∧ HMul.hMul (β := ENNReal) (2 : ENNReal) ((volume : Measure X) G' : ENNReal) ≤ (volume : Measure X) G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → ∫⁻ (x : X) in G \ G', ‖carlesonSum (F := F) (G := G) Set.univ f x‖ₑ ≤ ↑(C2_0_2 a (nnq X (F := F) (G := G))) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹`
Previous English: In the given setting on $X$ (with the sets $F$, $G$ and exponent $q$ = `nnq X`), there exists a measurable set $G' \subseteq X$ with $2\mu(G') \le \mu(G)$ such that for every measurable $f : X \to \mathbb{C}$ with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$, $$\int_{G\setminus G'} \Big\|\sum_{p \in \mathfrak{P}} T_p f(x)\Big\|\,dx \le C_{2.0.2}(a,q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where the sum is the Carleson sum over all tiles and $C_{2.0.2}$ is the constant `C2_0_2`.
Checker's issue: 'In the given setting on X' does not state the metric-space, ProofData and TileStructure standing assumptions, and it identifies the real exponent q with nnq X, which Lean uses only in the constant.
