You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `rcarleson`
Lean: `(hF : MeasurableSet F) (hG : MeasurableSet G) (f : ℝ → ℂ) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 4 2) * volume G ^ 2⁻¹ * volume F ^ 2⁻¹`
English: Let $F, G \subseteq \mathbb{R}$ be measurable and let $f : \mathbb{R} \to \mathbb{C}$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $\int_G T f(x)\,dx \le C_{10.0.1}(4, 2) \cdot |G|^{1/2} \cdot |F|^{1/2}$, where $T$ = `carlesonOperatorReal K` is the Carleson operator on $\mathbb{R}$ with kernel $K$ (a lower Lebesgue integral in $[0,\infty]$).

### `rcarleson_general`
Lean: `(hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (hF : MeasurableSet F) (hG : MeasurableSet G) (f : ℝ → ℂ) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 4 q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
English: Let $q \in (1, 2]$ and let $q'$ be its Hölder conjugate. Let $F, G \subseteq \mathbb{R}$ be measurable and let $f : \mathbb{R} \to \mathbb{C}$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $\int_G T f(x)\,dx \le C_{10.0.1}(4, q) \cdot |G|^{1/q'} \cdot |F|^{1/q}$, where $T$ = `carlesonOperatorReal K`.
