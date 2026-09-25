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

### `rcarleson`
Lean (short): `(hF : MeasurableSet F) (hG : MeasurableSet G) (f : ℝ → ℂ) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 4 2) * volume G ^ 2⁻¹ * volume F ^ 2⁻¹`
Lean (full): `∀ {F G : Set ℝ}, MeasurableSet F → MeasurableSet G → ∀ (f : ℝ → ℂ), Measurable f → (∀ (x : ℝ), ‖f x‖ ≤ F.indicator (1 : ℝ → ℝ) x) → ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 (4 : ℕ) (2 : NNReal)) * HPow.hPow (α := ENNReal) (volume G : ENNReal) (2 : ℝ)⁻¹ * HPow.hPow (α := ENNReal) (volume F : ENNReal) (2 : ℝ)⁻¹`
English: Let $F, G \subseteq \mathbb{R}$ be measurable and let $f : \mathbb{R} \to \mathbb{C}$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $\int_G T f(x)\,dx \le C_{10.0.1}(4, 2) \cdot |G|^{1/2} \cdot |F|^{1/2}$, where $T$ = `carlesonOperatorReal K` is the Carleson operator on $\mathbb{R}$ with kernel $K$ (a lower Lebesgue integral in $[0,\infty]$).

### `rcarleson_general`
Lean (short): `(hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (hF : MeasurableSet F) (hG : MeasurableSet G) (f : ℝ → ℂ) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 4 q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {q q' : NNReal}, q ∈ Set.Ioc (1 : NNReal) (2 : NNReal) → q.HolderConjugate q' → ∀ {F G : Set ℝ}, MeasurableSet F → MeasurableSet G → ∀ (f : ℝ → ℂ), Measurable f → (∀ (x : ℝ), ‖f x‖ ≤ F.indicator (1 : ℝ → ℝ) x) → ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 (4 : ℕ) q) * HPow.hPow (α := ENNReal) (volume G : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) (volume F : ENNReal) (↑q)⁻¹`
English: Let $q \in (1, 2]$ and let $q'$ be its Hölder conjugate. Let $F, G \subseteq \mathbb{R}$ be measurable and let $f : \mathbb{R} \to \mathbb{C}$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $\int_G T f(x)\,dx \le C_{10.0.1}(4, q) \cdot |G|^{1/q'} \cdot |F|^{1/q}$, where $T$ = `carlesonOperatorReal K`.
