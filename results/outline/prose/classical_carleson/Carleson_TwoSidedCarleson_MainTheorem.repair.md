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

### `two_sided_metric_carleson`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] [CompatibleFunctions ℝ X (defaultA a)] [IsCancellative X (defaultτ a)] (ha : 4 ≤ a) (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (hF : MeasurableSet F) (hG : MeasurableSet G) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hmf : Measurable f) (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G, carlesonOperator K f x ≤ ↑(C10_0_1 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [IsTwoSidedKernel a K] [inst_3 : CompatibleFunctions ℝ X (defaultA a)] [IsCancellative X (defaultτ a)], 4 ≤ a → q ∈ Set.Ioc 1 2 → q.HolderConjugate q' → MeasurableSet F → MeasurableSet G → (∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) → ∀ {f : X → ℂ}, Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) → ∫⁻ (x : X) in G, carlesonOperator K f x ≤ ↑(C10_0_1 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Previous English: Let $a \ge 4$, $q \in (1, 2]$ with Hölder conjugate $q'$, let $F, G$ be measurable sets, and suppose that for every $r > 0$ the truncated Calderón–Zygmund operator $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$. If $f$ is measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$, then $\int_G \mathrm{carlesonOperator}(K, f)(x)\, dx \le C_{10.0.1}(a, q)\, \mathrm{vol}(G)^{1/q'}\, \mathrm{vol}(F)^{1/q}$.
Checker's issue: English omits the instance hypotheses: metric space X with doubling measure, K a two-sided kernel, compatible functions, and the cancellative condition.
