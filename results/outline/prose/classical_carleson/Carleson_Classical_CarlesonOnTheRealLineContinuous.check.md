You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. A "Project
definitions" section first lists the project notions the statements refer to (statement, docstring, body,
fields). Compare the English with the full statement; anything the English attributes to the docstring must
actually be in it.

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
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: a project
notion's description must agree with its entry under "Project definitions" (statement, docstring, definition body,
fields), and a library notion may only be given its standard mathematical meaning; otherwise flag it. Every variable
needs its type ("$f : G \to \mathbb{C}$", "$m$ a natural number"), every symbol must be introduced, by definition
or by name ("the Ruzsa distance $d[X;Y]$", "the maximal operator $M_{\mathcal B}$"), and no letter may mean two
things. When in doubt, flag it: a false alarm costs one repair, a missed error stays in the outline.
Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

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

## Translations

### `rcarleson`
Lean (short): `(hF : MeasurableSet F) (hG : MeasurableSet G) (f : ℝ → ℂ) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 4 2) * volume G ^ 2⁻¹ * volume F ^ 2⁻¹`
Lean (full): `∀ {F G : Set ℝ}, MeasurableSet F → MeasurableSet G → ∀ (f : ℝ → ℂ), Measurable f → (∀ (x : ℝ), ‖f x‖ ≤ F.indicator (1 : ℝ → ℝ) x) → ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 (4 : ℕ) (2 : NNReal)) * HPow.hPow (α := ENNReal) (volume G : ENNReal) (2 : ℝ)⁻¹ * HPow.hPow (α := ENNReal) (volume F : ENNReal) (2 : ℝ)⁻¹`
English: Let $k : \mathbb{R} \to \mathbb{C}$ be $k(x) = \max(1 - |x|, 0)/(1 - e^{ix})$ (with the convention that division by $0$ gives $0$), and let $K : \mathbb{R} \times \mathbb{R} \to \mathbb{C}$ be $K(x, y) = k(x - y)$. For $f : \mathbb{R} \to \mathbb{C}$ and $x \in \mathbb{R}$ define $$Tf(x) = \sup_{n \in \mathbb{Z}} \sup_{0 < r < 1} \left| \int_{\{y \in \mathbb{R} : r < |x - y| < 1\}} f(y)\, K(x, y)\, e^{i n y}\, dy \right| \in [0, \infty],$$ the integral being a Bochner integral with respect to Lebesgue measure (taken to be $0$ if the integrand is not integrable). Let $F, G \subseteq \mathbb{R}$ be measurable sets and let $f : \mathbb{R} \to \mathbb{C}$ be a measurable function with $|f(x)| \le \mathbf{1}_F(x)$ for all $x \in \mathbb{R}$. Then $$\int_G Tf(x)\, dx \le C_{10.0.1}(4, 2) \cdot |G|^{1/2} \cdot |F|^{1/2},$$ where the left side is a lower Lebesgue integral in $[0, \infty]$, $|\cdot|$ on sets denotes Lebesgue measure (in $[0, \infty]$), and $C_{10.0.1}(4, 2)$ is the nonnegative real constant given by the project's function `C10_0_1` at $a = 4$, $q = 2$.

### `rcarleson_general`
Lean (short): `(hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (hF : MeasurableSet F) (hG : MeasurableSet G) (f : ℝ → ℂ) (hmf : Measurable f) (hf : ∀ (x : ℝ), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 4 q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {q q' : NNReal}, q ∈ Set.Ioc (1 : NNReal) (2 : NNReal) → q.HolderConjugate q' → ∀ {F G : Set ℝ}, MeasurableSet F → MeasurableSet G → ∀ (f : ℝ → ℂ), Measurable f → (∀ (x : ℝ), ‖f x‖ ≤ F.indicator (1 : ℝ → ℝ) x) → ∫⁻ (x : ℝ) in G, carlesonOperatorReal K f x ≤ ↑(C10_0_1 (4 : ℕ) q) * HPow.hPow (α := ENNReal) (volume G : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) (volume F : ENNReal) (↑q)⁻¹`
English: Let $k : \mathbb{R} \to \mathbb{C}$ be $k(x) = \max(1 - |x|, 0)/(1 - e^{ix})$ (with the convention that division by $0$ gives $0$), and let $K : \mathbb{R} \times \mathbb{R} \to \mathbb{C}$ be $K(x, y) = k(x - y)$. For $f : \mathbb{R} \to \mathbb{C}$ and $x \in \mathbb{R}$ define $$Tf(x) = \sup_{n \in \mathbb{Z}} \sup_{0 < r < 1} \left| \int_{\{y \in \mathbb{R} : r < |x - y| < 1\}} f(y)\, K(x, y)\, e^{i n y}\, dy \right| \in [0, \infty],$$ the integral being a Bochner integral with respect to Lebesgue measure (taken to be $0$ if the integrand is not integrable). Let $q, q'$ be nonnegative real numbers with $1 < q \le 2$ and $\frac{1}{q} + \frac{1}{q'} = 1$ (i.e. $q, q'$ are Hölder conjugates). Let $F, G \subseteq \mathbb{R}$ be measurable sets and let $f : \mathbb{R} \to \mathbb{C}$ be a measurable function with $|f(x)| \le \mathbf{1}_F(x)$ for all $x \in \mathbb{R}$. Then $$\int_G Tf(x)\, dx \le C_{10.0.1}(4, q) \cdot |G|^{1/q'} \cdot |F|^{1/q},$$ where the left side is a lower Lebesgue integral in $[0, \infty]$, $|\cdot|$ on sets denotes Lebesgue measure (in $[0, \infty]$), and $C_{10.0.1}(4, q)$ is the nonnegative real constant given by the project's function `C10_0_1` at $a = 4$ and the given $q$.
