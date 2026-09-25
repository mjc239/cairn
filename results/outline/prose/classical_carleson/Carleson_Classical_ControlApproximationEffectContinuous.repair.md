You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring, and when no
docstring or Lean supports a description of an object, name it instead of describing it. Give every variable its
type, introduce every symbol, and never use one letter for two things.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): TileStructure, MeasureTheory, Antichain.

### `rcarleson_exceptional_set_estimate_specific`
Lean (short): `(Cpos : 0 < C) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ ↑C) (measurableSetE : MeasurableSet E) (E_subset : E ⊆ Set.Icc 0 (2 * Real.pi)) (hE : ∀ x ∈ E, ↑δ ≤ carlesonOperatorReal K f x) : ↑δ * volume E ≤ ↑C * ↑(C10_0_1 4 2) * ENNReal.ofReal (2 * Real.pi + 2) ^ 2⁻¹ * volume E ^ 2⁻¹`
Lean (full): `∀ {δ C : NNReal}, (0 : NNReal) < C → ∀ {f : ℝ → ℂ}, Measurable f → (∀ (x : ℝ), ‖f x‖ ≤ ↑C) → ∀ {E : Set ℝ}, MeasurableSet E → E ⊆ Set.Icc (0 : ℝ) ((2 : ℝ) * Real.pi) → (∀ x ∈ E, ↑δ ≤ carlesonOperatorReal K f x) → HMul.hMul (β := ENNReal) ↑δ (volume E : ENNReal) ≤ ↑C * ↑(C10_0_1 (4 : ℕ) (2 : NNReal)) * ENNReal.ofReal ((2 : ℝ) * Real.pi + (2 : ℝ)) ^ (2 : ℝ)⁻¹ * HPow.hPow (α := ENNReal) (volume E : ENNReal) (2 : ℝ)⁻¹`
Previous English: Let $C > 0$, let $f : \mathbb{R} \to \mathbb{C}$ be measurable with $\|f(x)\| \le C$ for all $x \in \mathbb{R}$, and let $E \subseteq [0, 2\pi]$ be measurable with $\delta \le T f(x)$ for all $x \in E$, where $T$ = `carlesonOperatorReal K` is the Carleson operator on $\mathbb{R}$ with kernel $K$. Then $\delta \cdot |E| \le C \cdot C_{10.0.1}(4, 2) \cdot (2\pi + 2)^{1/2} \cdot |E|^{1/2}$ (in $[0,\infty]$, with $|\cdot|$ Lebesgue measure).
Checker's issue: delta (and C) are nonnegative reals (NNReal) in the Lean; the English never states that delta is a nonnegative real, leaving a restrictive type unstated.

### `rcarleson_exceptional_set_estimate`
Lean (short): `(Cpos : 0 < C) (hmf : Measurable f) (measurableSetF : MeasurableSet F) (hf : ∀ (x : ℝ), ‖f x‖ ≤ ↑C * F.indicator 1 x) (measurableSetE : MeasurableSet E) (hE : ∀ x ∈ E, ↑δ ≤ carlesonOperatorReal K f x) : ↑δ * volume E ≤ ↑C * ↑(C10_0_1 4 2) * volume F ^ 2⁻¹ * volume E ^ 2⁻¹`
Lean (full): `∀ {δ C : NNReal}, (0 : NNReal) < C → ∀ {f : ℝ → ℂ}, Measurable f → ∀ {F : Set ℝ}, MeasurableSet F → (∀ (x : ℝ), ‖f x‖ ≤ ↑C * F.indicator (1 : ℝ → ℝ) x) → ∀ {E : Set ℝ}, MeasurableSet E → (∀ x ∈ E, ↑δ ≤ carlesonOperatorReal K f x) → HMul.hMul (β := ENNReal) ↑δ (volume E : ENNReal) ≤ ↑C * ↑(C10_0_1 (4 : ℕ) (2 : NNReal)) * HPow.hPow (α := ENNReal) (volume F : ENNReal) (2 : ℝ)⁻¹ * HPow.hPow (α := ENNReal) (volume E : ENNReal) (2 : ℝ)⁻¹`
Previous English: Let $C > 0$, let $f : \mathbb{R} \to \mathbb{C}$ be measurable, let $F \subseteq \mathbb{R}$ be measurable with $\|f(x)\| \le C \cdot \mathbf{1}_F(x)$ for all $x$, and let $E$ be measurable with $\delta \le T f(x)$ for all $x \in E$, where $T$ = `carlesonOperatorReal K`. Then $\delta \cdot |E| \le C \cdot C_{10.0.1}(4, 2) \cdot |F|^{1/2} \cdot |E|^{1/2}$.
Checker's issue: delta (and C) are nonnegative reals (NNReal) in the Lean; the English never states that delta is a nonnegative real, leaving a restrictive type unstated.
