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
docstring, definition body (under "Project definitions") or Lean supports a description of an object, name it
instead of describing it. Give every variable its
type, introduce every symbol, and never use one letter for two things.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): MeasureTheory, TileStructure, Antichain.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `C10_0_1` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant used in `two_sided_metric_carleson`. Has value `2 ^ (474 * a ^ 3) / (q - 1) ^ 6` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => C_K ↑a ^ (2 : ℕ) * C1_0_2 a q`

#### `K` (def)
Lean: `ℝ → ℝ → ℂ`
Definition: `fun (x y : ℝ) => k (x - y)`

#### `carlesonOperatorReal` (def)
Lean: `(ℝ → ℝ → ℂ) → (ℝ → ℂ) → ℝ → ENNReal`
Definition: `fun (K : ℝ → ℝ → ℂ) (f : ℝ → ℂ) (x : ℝ) => ⨆ (n : ℤ), ⨆ (r : ℝ), ⨆ (_ : (0 : ℝ) < r), ⨆ (_ : r < (1 : ℝ)), enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume {y : ℝ | dist x y ∈ Set.Ioo r (1 : ℝ)}) fun (y : ℝ) => f y * K x y * Complex.exp (Complex.I * ↑n * ↑y))`

#### `C1_0_2` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant used in `MetricSpaceCarleson` and `LinearizedMetricCarleson`. Has value `2 ^ (443 * a ^ 3) / (q - 1) ^ 6` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => (2 : NNReal) ^ (((3 : ℕ) * 𝕔 + (18 : ℕ) + (5 : ℕ) * (𝕔 / (4 : ℕ))) * a ^ (3 : ℕ)) / (q - (1 : NNReal)) ^ (6 : ℕ)`

#### `C_K` (def)
Lean: `ℝ → NNReal`
Docstring: The constant used twice in the definition of the Calderon-Zygmund kernel.
Definition: `fun (a : ℝ) => (2 : NNReal) ^ a ^ (3 : ℕ)`

#### `k` (def)
Lean: `ℝ → ℂ`
Definition: `fun (x : ℝ) => ↑(max ((1 : ℝ) - |x|) (0 : ℝ)) / ((1 : ℂ) - Complex.exp (Complex.I * ↑x))`

## Flagged translations

### `rcarleson`
Lean (short): `(hF : MeasurableSet F) (hG : MeasurableSet G) (f : ℝ → ℂ) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 4 2) * volume G ^ 2⁻¹ * volume F ^ 2⁻¹`
Lean (full): `∀ {F G : Set ℝ}, MeasurableSet F → MeasurableSet G → ∀ (f : ℝ → ℂ), Measurable f → (∀ (x : ℝ), ‖f x‖ ≤ F.indicator (1 : ℝ → ℝ) x) → ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 (4 : ℕ) (2 : NNReal)) * HPow.hPow (α := ENNReal) (volume G : ENNReal) (2 : ℝ)⁻¹ * HPow.hPow (α := ENNReal) (volume F : ENNReal) (2 : ℝ)⁻¹`
Previous English: Let $F, G \subseteq \mathbb{R}$ be measurable and let $f : \mathbb{R} \to \mathbb{C}$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $\int_G T f(x)\,dx \le C_{10.0.1}(4, 2) \cdot |G|^{1/2} \cdot |F|^{1/2}$, where $T$ = `carlesonOperatorReal K` is the Carleson operator on $\mathbb{R}$ with kernel $K$ (a lower Lebesgue integral in $[0,\infty]$).
Checker's issue: The kernel K is never introduced; it is a specific fixed object in the Lean. The description 'the Carleson operator on R with kernel K' is not supported by any definition or docstring in the prompt.

### `rcarleson_general`
Lean (short): `(hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (hF : MeasurableSet F) (hG : MeasurableSet G) (f : ℝ → ℂ) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 4 q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {q q' : NNReal}, q ∈ Set.Ioc (1 : NNReal) (2 : NNReal) → q.HolderConjugate q' → ∀ {F G : Set ℝ}, MeasurableSet F → MeasurableSet G → ∀ (f : ℝ → ℂ), Measurable f → (∀ (x : ℝ), ‖f x‖ ≤ F.indicator (1 : ℝ → ℝ) x) → ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 (4 : ℕ) q) * HPow.hPow (α := ENNReal) (volume G : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) (volume F : ENNReal) (↑q)⁻¹`
Previous English: Let $q \in (1, 2]$ and let $q'$ be its Hölder conjugate. Let $F, G \subseteq \mathbb{R}$ be measurable and let $f : \mathbb{R} \to \mathbb{C}$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $\int_G T f(x)\,dx \le C_{10.0.1}(4, q) \cdot |G|^{1/q'} \cdot |F|^{1/q}$, where $T$ = `carlesonOperatorReal K`.
Checker's issue: The kernel K in carlesonOperatorReal K is never introduced. q and q' are nonnegative reals (NNReal), which the English leaves implicit.
