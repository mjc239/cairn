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

### `rcarleson_exceptional_set_estimate_specific`
Lean (short): `(Cpos : 0 < C) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ ↑C) (measurableSetE : MeasurableSet E) (E_subset : E ⊆ Set.Icc 0 (2 * Real.pi)) (hE : ∀ x ∈ E, ↑δ ≤ carlesonOperatorReal K f x) : ↑δ * volume E ≤ ↑C * ↑(C10_0_1 4 2) * ENNReal.ofReal (2 * Real.pi + 2) ^ 2⁻¹ * volume E ^ 2⁻¹`
Lean (full): `∀ {δ C : NNReal}, (0 : NNReal) < C → ∀ {f : ℝ → ℂ}, Measurable f → (∀ (x : ℝ), ‖f x‖ ≤ ↑C) → ∀ {E : Set ℝ}, MeasurableSet E → E ⊆ Set.Icc (0 : ℝ) ((2 : ℝ) * Real.pi) → (∀ x ∈ E, ↑δ ≤ carlesonOperatorReal K f x) → HMul.hMul (β := ENNReal) ↑δ (volume E : ENNReal) ≤ ↑C * ↑(C10_0_1 (4 : ℕ) (2 : NNReal)) * ENNReal.ofReal ((2 : ℝ) * Real.pi + (2 : ℝ)) ^ (2 : ℝ)⁻¹ * HPow.hPow (α := ENNReal) (volume E : ENNReal) (2 : ℝ)⁻¹`
English: Let $\delta, C$ be nonnegative real numbers with $C > 0$, let $f : \mathbb{R} \to \mathbb{C}$ be measurable with $\|f(x)\| \le C$ for all $x \in \mathbb{R}$, and let $E \subseteq \mathbb{R}$ be a measurable set with $E \subseteq [0, 2\pi]$ and $\delta \le T f(x)$ for all $x \in E$, where $T f(x)$ denotes `carlesonOperatorReal K f x` (an element of $[0,\infty]$) for the kernel `K` fixed in this file. Then, in $[0,\infty]$, $\delta \cdot |E| \le C \cdot C_{10.0.1}(4, 2) \cdot (2\pi + 2)^{1/2} \cdot |E|^{1/2}$, where $|E|$ is the Lebesgue measure of $E$ and $C_{10.0.1}(4,2)$ is the constant `C10_0_1 4 2`.

### `rcarleson_exceptional_set_estimate`
Lean (short): `(Cpos : 0 < C) (hmf : Measurable f) (measurableSetF : MeasurableSet F) (hf : ∀ (x : ℝ), ‖f x‖ ≤ ↑C * F.indicator 1 x) (measurableSetE : MeasurableSet E) (hE : ∀ x ∈ E, ↑δ ≤ carlesonOperatorReal K f x) : ↑δ * volume E ≤ ↑C * ↑(C10_0_1 4 2) * volume F ^ 2⁻¹ * volume E ^ 2⁻¹`
Lean (full): `∀ {δ C : NNReal}, (0 : NNReal) < C → ∀ {f : ℝ → ℂ}, Measurable f → ∀ {F : Set ℝ}, MeasurableSet F → (∀ (x : ℝ), ‖f x‖ ≤ ↑C * F.indicator (1 : ℝ → ℝ) x) → ∀ {E : Set ℝ}, MeasurableSet E → (∀ x ∈ E, ↑δ ≤ carlesonOperatorReal K f x) → HMul.hMul (β := ENNReal) ↑δ (volume E : ENNReal) ≤ ↑C * ↑(C10_0_1 (4 : ℕ) (2 : NNReal)) * HPow.hPow (α := ENNReal) (volume F : ENNReal) (2 : ℝ)⁻¹ * HPow.hPow (α := ENNReal) (volume E : ENNReal) (2 : ℝ)⁻¹`
English: Let $\delta, C$ be nonnegative real numbers with $C > 0$, let $f : \mathbb{R} \to \mathbb{C}$ be measurable, let $F \subseteq \mathbb{R}$ be a measurable set with $\|f(x)\| \le C \cdot \mathbf{1}_F(x)$ for all $x \in \mathbb{R}$, and let $E \subseteq \mathbb{R}$ be a measurable set with $\delta \le T f(x)$ for all $x \in E$, where $T f(x)$ denotes `carlesonOperatorReal K f x` (an element of $[0,\infty]$) for the kernel `K` fixed in this file. Then, in $[0,\infty]$, $\delta \cdot |E| \le C \cdot C_{10.0.1}(4, 2) \cdot |F|^{1/2} \cdot |E|^{1/2}$, where $|\cdot|$ is Lebesgue measure and $C_{10.0.1}(4,2)$ is the constant `C10_0_1 4 2`.
