You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `rcarleson_exceptional_set_estimate_specific`
Lean: `(Cpos : 0 < C) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ ↑C) (measurableSetE : MeasurableSet E) (E_subset : E ⊆ Set.Icc 0 (2 * Real.pi)) (hE : ∀ x ∈ E, ↑δ ≤ carlesonOperatorReal K f x) : ↑δ * volume E ≤ ↑C * ↑(C10_0_1 4 2) * ENNReal.ofReal (2 * Real.pi + 2) ^ 2⁻¹ * volume E ^ 2⁻¹`
English: Let $C > 0$, let $f : \mathbb{R} \to \mathbb{C}$ be measurable with $\|f(x)\| \le C$ for all $x \in \mathbb{R}$, and let $E \subseteq [0, 2\pi]$ be measurable with $\delta \le T f(x)$ for all $x \in E$, where $T$ = `carlesonOperatorReal K` is the Carleson operator on $\mathbb{R}$ with kernel $K$. Then $\delta \cdot |E| \le C \cdot C_{10.0.1}(4, 2) \cdot (2\pi + 2)^{1/2} \cdot |E|^{1/2}$ (in $[0,\infty]$, with $|\cdot|$ Lebesgue measure).

### `rcarleson_exceptional_set_estimate`
Lean: `(Cpos : 0 < C) (hmf : Measurable f) (measurableSetF : MeasurableSet F) (hf : ∀ (x : ℝ), ‖f x‖ ≤ ↑C * F.indicator 1 x) (measurableSetE : MeasurableSet E) (hE : ∀ x ∈ E, ↑δ ≤ carlesonOperatorReal K f x) : ↑δ * volume E ≤ ↑C * ↑(C10_0_1 4 2) * volume F ^ 2⁻¹ * volume E ^ 2⁻¹`
English: Let $C > 0$, let $f : \mathbb{R} \to \mathbb{C}$ be measurable, let $F \subseteq \mathbb{R}$ be measurable with $\|f(x)\| \le C \cdot \mathbf{1}_F(x)$ for all $x$, and let $E$ be measurable with $\delta \le T f(x)$ for all $x \in E$, where $T$ = `carlesonOperatorReal K`. Then $\delta \cdot |E| \le C \cdot C_{10.0.1}(4, 2) \cdot |F|^{1/2} \cdot |E|^{1/2}$.
