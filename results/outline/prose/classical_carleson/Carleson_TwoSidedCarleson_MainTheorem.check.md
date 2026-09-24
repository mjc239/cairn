You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `two_sided_metric_carleson`
Lean: `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] [CompatibleFunctions ℝ X (defaultA a)] [IsCancellative X (defaultτ a)] (ha : 4 ≤ a) (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (hF : MeasurableSet F) (hG : MeasurableSet G) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hmf : Measurable f) (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G, carlesonOperator K f x ≤ ↑(C10_0_1 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
English: Let $a \ge 4$, $q \in (1, 2]$ with Hölder conjugate $q'$, let $F, G$ be measurable sets, and suppose that for every $r > 0$ the truncated Calderón–Zygmund operator $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$. If $f$ is measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$, then $\int_G \mathrm{carlesonOperator}(K, f)(x)\, dx \le C_{10.0.1}(a, q)\, \mathrm{vol}(G)^{1/q'}\, \mathrm{vol}(F)^{1/q}$.
