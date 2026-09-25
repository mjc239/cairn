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
be supported by the docstring or the Lean. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `finitary_carleson`
Lean (short): `(X : Type u_1) [ProofData a q K σ₁ σ₂ F G] : ∃ G', MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → ∫⁻ (x : X) in G \ G', ‖∑ s ∈ (Set.Icc (σ₁ x) (σ₂ x)).toFinset, ∫ (y : X), Ks s x y * f y * Complex.exp (Complex.I * ↑((Q x) y))‖ₑ ≤ ↑(C2_0_1 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ (X : Type u_1) {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G], ∃ G', MeasurableSet G' ∧ HMul.hMul (β := ENNReal) (2 : ENNReal) ((volume : Measure X) G' : ENNReal) ≤ (volume : Measure X) G ∧ ∀ (f : X → ℂ), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → ∫⁻ (x : X) in G \ G', enorm (E := ℂ) (∑ s ∈ (Set.Icc (σ₁ x) (σ₂ x)).toFinset, @integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => Ks s x y * f y * Complex.exp (Complex.I * ↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y))) ≤ ↑(C2_0_1 a (nnq X (F := F) (G := G))) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹`
Docstring: Proposition 2.0.1
English: Let $X$ be a metric space, and assume the standing `ProofData` assumptions for parameters $a\in\mathbb N$, $q\in\mathbb R$, a complex-valued kernel $K : X\times X\to\mathbb C$, integer-valued scale functions $\sigma_1,\sigma_2 : X\to\mathbb Z$ and sets $F,G\subseteq X$ (making $X$ a doubling metric measure space). Then (the docstring labels this Proposition 2.0.1) there exists a measurable set $G'\subseteq X$ with $2\mu(G')\le\mu(G)$ (in $[0,\infty]$, $\mu$ the measure on $X$) such that for every measurable $f : X\to\mathbb C$ with $\|f(x)\|\le\mathbf 1_F(x)$ for all $x\in X$, $$\int_{G\setminus G'}\Big\|\sum_{s\in[\sigma_1(x),\sigma_2(x)]\cap\mathbb Z}\int_X K_s(x,y)\,f(y)\,e^{i\,Q(x)(y)}\,d\mu(y)\Big\|\,d\mu(x)\le C_{2.0.1}(a,q)\,\mu(G)^{1-q^{-1}}\,\mu(F)^{q^{-1}},$$ where the left side is a lower Lebesgue integral of extended norms, $K_s$ is the truncated kernel `Ks`, $C_{2.0.1}(a,q)$ is the nonnegative constant `C2_0_1 a (nnq X)` (with $q$ viewed as a nonnegative real), and the powers $1-q^{-1}$ and $q^{-1}$ are real exponents of extended nonnegative reals.
