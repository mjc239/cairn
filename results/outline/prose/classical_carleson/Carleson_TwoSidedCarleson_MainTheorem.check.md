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

### `two_sided_metric_carleson`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] [CompatibleFunctions ℝ X (defaultA a)] [IsCancellative X (defaultτ a)] (ha : 4 ≤ a) (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (hF : MeasurableSet F) (hG : MeasurableSet G) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hmf : Measurable f) (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G, carlesonOperator K f x ≤ ↑(C10_0_1 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [IsTwoSidedKernel a K] [inst_3 : CompatibleFunctions ℝ X (defaultA a)] [IsCancellative X (defaultτ a)], (4 : ℕ) ≤ a → q ∈ Set.Ioc (1 : NNReal) (2 : NNReal) → q.HolderConjugate q' → MeasurableSet F → MeasurableSet G → (∀ r > (0 : ℝ), HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (czOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → ∀ {f : X → ℂ}, Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → ∫⁻ (x : X) in G, carlesonOperator K f x ≤ ↑(C10_0_1 a q) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (↑q)⁻¹`
English: Let $X$ be a metric space and $a\in\mathbb N$, and suppose $X$ carries a doubling measure $\mu$ with doubling constant $\mathrm{defaultA}(a)$ (`DoublingMeasure X (defaultA a)`), a family $\Theta(X)$ of real-valued compatible functions with parameter $\mathrm{defaultA}(a)$ (`CompatibleFunctions ℝ X (defaultA a)`), and satisfies the cancellative property `IsCancellative X (defaultτ a)`. Let $K:X\times X\to\mathbb C$ be a two-sided Calderón–Zygmund kernel with parameter $a$ (`IsTwoSidedKernel a K`). Let $a \ge 4$, let $q,q'$ be nonnegative reals with $q \in (1, 2]$ and $q'$ its Hölder conjugate, let $F, G\subseteq X$ be measurable sets, and suppose that for every $r > 0$ the truncated Calderón–Zygmund operator $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with respect to $\mu$ with constant $C_{Ts}(a)$. If $f:X\to\mathbb C$ is measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$, then $$\int_G \mathrm{carlesonOperator}(K, f)(x)\, d\mu(x) \le C_{10.0.1}(a, q)\, \mu(G)^{1/q'}\, \mu(F)^{1/q}.$$
