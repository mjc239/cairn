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

#### `C10_0_2` (def)
Lean: `ℕ → NNReal`
Docstring: The constant used in `nontangential_from_simple`.
Definition: `wrapped✝.1`

#### `C_Ts` (def)
Lean: `ℕ → NNReal`
Docstring: A constant used on the boundedness of `T_Q^θ` and `T_*`. We generally assume `HasBoundedStrongType (linearizedNontangentialOperator Q θ K · ·) 2 2 volume volume (C_Ts a)` throughout this formalization.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ a ^ (3 : ℕ)`

#### `IsTwoSidedKernel` (structure or class)
Lean: `{X : Type u_1} → [PseudoMetricSpace X] → [MeasureSpace X] → outParam ℕ → (X → X → ℂ) → Prop`
Docstring: `K` is a two-sided Calderon-Zygmund kernel. In the formalization `K x y` is defined everywhere, even for `x = y`. The assumptions on `K` show that `K x x = 0`.
Fields: `2`, `β`

#### `MeasureTheory.DoublingMeasure` (structure or class)
Lean: `(X : Type u_3) → outParam NNReal → [PseudoMetricSpace X] → Type u_3`
Docstring: A metric space with a measure with some nice properties, including a doubling condition. This is called a "doubling metric measure space" in the blueprint. `A` will usually be `2 ^ a`.
Fields: `α`, `m0`, `X`, `R`

#### `MeasureTheory.DoublingMeasure.toMeasureSpace` (def)
Lean: `{X : Type u_3} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → [self : DoublingMeasure X A] → MeasureSpace X`
Definition: `fun (X : Type u_3) {A : outParam NNReal} {inst : PseudoMetricSpace X} [self : DoublingMeasure X A] => self.3`

#### `MeasureTheory.HasBoundedStrongType` (def)
Lean: `{ε₁ : Type u_3} → {ε₂ : Type u_4} → [ENorm ε₁] → [ENorm ε₂] → [TopologicalSpace ε₁] → [TopologicalSpace ε₂] → [Zero ε₁] → {α : Type u_5} → {α' : Type u_6} → {_x : MeasurableSpace α} → {_x' : MeasurableSpace α'} → ((α → ε₁) → α' → ε₂) → ENNReal → ENNReal → Measure α → Measure α' → ENNReal → Prop`
Docstring: A weaker version of `HasStrongType`. This is the same as `HasStrongType` if `T` is continuous w.r.t. the L^2 norm, but weaker in general.
Definition: `fun {ε₁ : Type u_3} {ε₂ : Type u_4} [ENorm ε₁] [ENorm ε₂] [TopologicalSpace ε₁] [TopologicalSpace ε₂] [Zero ε₁] {α : Type u_5} {α' : Type u_6} {_x : MeasurableSpace α} {_x' : MeasurableSpace α'} (T : (α → ε₁) → α' → ε₂) (p p' : ENNReal) (μ : Measure α) (ν : Measure α') (c : ENNReal) => ∀ (f : α → ε₁), BoundedFiniteSupport f μ → AEStronglyMeasurable (T f) ν ∧ eLpNorm (T f) p' ν ≤ c * eLpNorm f p μ`

#### `czOperator` (def)
Lean: `{X : Type u_2} → [PseudoMetricSpace X] → [MeasureSpace X] → (X → X → ℂ) → ℝ → (X → ℂ) → X → ℂ`
Docstring: The Calderon Zygmund operator `T_r` in chapter Two-sided Metric Space Carleson
Definition: `fun {X : Type u_2} [PseudoMetricSpace X] [MeasureSpace X] (K : X → X → ℂ) (r : ℝ) (f : X → ℂ) (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume (Metric.ball x r)ᶜ) fun (y : X) => K x y * f y`

#### `defaultA` (def)
Lean: `ℕ → ℕ`
Docstring: This is usually the value of the argument `A` in `DoublingMeasure` and `CompatibleFunctions`
Definition: `fun (a : ℕ) => (2 : ℕ) ^ a`

#### `nontangentialOperator` (def)
Lean: `{X : Type u_2} → {A : ℕ} → [inst : PseudoMetricSpace X] → [DoublingMeasure X ↑A] → (X → X → ℂ) → (X → ℂ) → X → ENNReal`
Docstring: The maximally truncated nontangential Calderon–Zygmund operator `T_*`.
Definition: `fun {X : Type u_2} {A : ℕ} [PseudoMetricSpace X] [DoublingMeasure X ↑A] (K : X → X → ℂ) (f : X → ℂ) (x : X) => ⨆ (R₂ : ℝ), ⨆ R₁ ∈ Set.Ioo (0 : ℝ) R₂, ⨆ x' ∈ Metric.ball x R₁, enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume (Set.Annulus.oo x' R₁ R₂)) fun (y : X) => K x' y * f y)`

#### `BoundedFiniteSupport` (structure or class)
Lean: `{X : Type u_3} → {E : Type u_4} → [inst : MeasurableSpace X] → [TopologicalSpace E] → [ENorm E] → [Zero E] → (X → E) → autoParam (Measure X) BoundedFiniteSupport._auto_1 → Prop`
Docstring: Bounded measurable function $g$ on $X$ supported on a set of finite measure
Fields: `α`, `⊤`

#### `C10_1_5` (def)
Lean: `ℕ → NNReal`
Docstring: The constant used in `cotlar_estimate`.
Definition: `wrapped✝.1`

#### `globalMaximalFunction` (def)
Lean: `{X : Type u_1} → {ε : Type u_2} → [PseudoMetricSpace X] → [inst : MeasurableSpace X] → [ENorm ε] → Measure X → ℝ → (X → ε) → X → ENNReal`
Docstring: The uncentered Hardy-Littlewood maximal function.
Definition: `fun {X : Type u_1} {ε : Type u_2} [PseudoMetricSpace X] [MeasurableSpace X] [ENorm ε] (μ : Measure X) (p : ℝ) (u : X → ε) (x : X) => maximalFunction μ Set.univ (fun (x : X × ℝ) => x.1) (fun (x : X × ℝ) => x.2) p u x`

#### `C10_1_4` (def)
Lean: `ℕ → NNReal`
Docstring: The constant used in `cotlar_set_F₂`.
Definition: `wrapped✝.1`

#### `C10_1_6` (def)
Lean: `ℕ → NNReal`
Docstring: The constant used in `simple_nontangential_operator`. It is not tight and can be improved by some `a` + `constant`.
Definition: `wrapped✝.1`

#### `simpleNontangentialOperator` (def)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → [DoublingMeasure X ↑(defaultA a)] → (X → X → ℂ) → ℝ → (X → ℂ) → X → ENNReal`
Docstring: The operator `T_*^r g(x)`, defined in (10.1.31), above Lemma 10.1.6.
Definition: `fun {X : Type u_1} {a : ℕ} [MetricSpace X] [DoublingMeasure X ↑(defaultA a)] (K : X → X → ℂ) (r : ℝ) (g : X → ℂ) (x : X) => ⨆ (R : ℝ), ⨆ (_ : R > r), ⨆ x' ∈ Metric.ball x R, ‖czOperator K R g x'‖ₑ`

#### `partialFourierSum` (def)
Lean: `ℕ → (ℝ → ℂ) → ℝ → ℂ`
Docstring: The Nᵗʰ partial Fourier sum of `f : ℝ → ℂ` for `N : ℕ`.
Definition: `fun (N : ℕ) (f : ℝ → ℂ) (x : ℝ) => ∑ n ∈ Finset.Icc (-↑N) ↑N, HMul.hMul (β := ℂ) (fourierCoeffOn Real.two_pi_pos f n) ((fourier n) ↑x : ℂ)`

#### `C_K` (def)
Lean: `ℝ → NNReal`
Docstring: The constant used twice in the definition of the Calderon-Zygmund kernel.
Definition: `fun (a : ℝ) => (2 : NNReal) ^ a ^ (3 : ℕ)`

#### `IsOneSidedKernel` (structure or class)
Lean: `{X : Type u_1} → [PseudoMetricSpace X] → [MeasureSpace X] → outParam ℕ → (X → X → ℂ) → Prop`
Docstring: `K` is a one-sided Calderon-Zygmund kernel. In the formalization `K x y` is defined everywhere, even for `x = y`. The assumptions on `K` show that `K x x = 0`.
Fields: `2`, `β`

#### `Real.vol` (def)
Lean: `{X : Type u_1} → [PseudoMetricSpace X] → [MeasureSpace X] → X → X → ℝ`
Docstring: The "volume function" `V`. Preferably use `vol` instead.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] [MeasureSpace X] (x y : X) => Measure.real (m := MeasureSpace.toMeasurableSpace) volume (Metric.ball x (dist x y))`

#### `vol` (def)
Lean: `{X : Type u_3} → [PseudoMetricSpace X] → [MeasureSpace X] → X → X → ENNReal`
Docstring: The "volume function" `V`. We will need to assume `IsFiniteMeasureOnCompacts` and `ProperSpace` to actually know that this volume is finite.
Definition: `fun {X : Type u_3} [PseudoMetricSpace X] [MeasureSpace X] (x y : X) => (volume : Measure X) (Metric.ball x (dist x y))`

#### `MeasureTheory.Measure.IsDoubling` (structure or class)
Lean: `{X : Type u_3} → [inst : MeasurableSpace X] → [PseudoMetricSpace X] → Measure X → outParam NNReal → Prop`
Docstring: A doubling measure is a measure on a metric space with the condition that doubling the radius of a ball only increases the volume by a constant factor, independent of the ball.
Fields: `x`, `r`, `2`, `β`

#### `Set.Annulus.oo` (def)
Lean: `{X : Type u_1} → [PseudoMetricSpace X] → X → ℝ → ℝ → Set X`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] (x : X) (r R : ℝ) => {y : X | dist x y ∈ Set.Ioo r R}`

#### `maximalFunction` (def)
Lean: `{X : Type u_1} → {ε : Type u_2} → [PseudoMetricSpace X] → [inst : MeasurableSpace X] → [ENorm ε] → {ι : Type u_4} → Measure X → Set ι → (ι → X) → (ι → ℝ) → ℝ → (X → ε) → X → ENNReal`
Docstring: The uncentered Hardy-Littlewood maximal function, for a family of balls.
Definition: `fun {X : Type u_1} {ε : Type u_2} [PseudoMetricSpace X] [MeasurableSpace X] [ENorm ε] {ι : Type u_4} (μ : Measure X) (𝓑 : Set ι) (c : ι → X) (r : ι → ℝ) (p : ℝ) (u : X → ε) (x : X) => ⨆ i ∈ 𝓑, (Metric.ball (c i) (r i)).indicator (fun (x : X) => (⨍⁻ (y : X) in Metric.ball (c i) (r i), ‖u y‖ₑ ^ p ∂μ) ^ p⁻¹) x`

## Translations

### `nontangential_from_simple`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) : HasBoundedStrongType (nontangentialOperator K) 2 2 volume volume ↑(C10_0_2 a)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {K : X → X → ℂ} [IsTwoSidedKernel a K], (4 : ℕ) ≤ a → (∀ r > (0 : ℝ), HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (czOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (nontangentialOperator K) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C10_0_2 a)`
Docstring: Lemma 10.0.2. The formal statement includes the measurability of the operator.
English: (Lemma 10.0.2; per the docstring, the formal statement includes measurability of the operator.) Let $X$ be a metric space and $a\in\mathbb N$, and assume $X$ carries a project `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$ (docstring: a metric space with a measure with some nice properties, including a doubling condition); denote its measure (`volume`) by $\mu$. Let $K : X\to X\to\mathbb C$ satisfy the project predicate `IsTwoSidedKernel a K` (docstring: $K$ is a two-sided Calderón–Zygmund kernel), and assume $a\ge 4$. For $t\in\mathbb R$, $h : X\to\mathbb C$ and $z\in X$ let $T_t h(z)=\mathrm{czOperator}(K,t,h)(z)=\int_{X\setminus B(z,t)}K(z,y)\,h(y)\,d\mu(y)$. Say that an operator $T$ taking functions $X\to\mathbb C$ to functions on $X$ (with values in $\mathbb C$ or $[0,\infty]$) has bounded strong type $(2,2)$ with constant $C\in[0,\infty]$ (project `HasBoundedStrongType T 2 2 μ μ C`) if for every $h : X\to\mathbb C$ that is bounded, measurable and supported on a set of finite measure (`BoundedFiniteSupport h μ`), $Th$ is almost everywhere strongly measurable and $\|Th\|_{L^2(\mu)}\le C\,\|h\|_{L^2(\mu)}$. Let $C_{Ts}(a)=2^{a^3}$ (project constant `C_Ts a`), and assume that for every real $t>0$ the operator $T_t$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$. Let $T_*$ be the project operator `nontangentialOperator K` (docstring: the maximally truncated nontangential Calderón–Zygmund operator $T_*$), $T_*h(z)=\sup_{R_2\in\mathbb R}\ \sup_{0<R_1<R_2}\ \sup_{z'\in B(z,R_1)}\Big\|\int_{\{y:\,R_1<d(z',y)<R_2\}}K(z',y)\,h(y)\,d\mu(y)\Big\|_e\in[0,\infty]$. Let $C_{10.0.2}(a)\in\mathbb R_{\ge0}$ be the project constant `C10_0_2 a` (docstring: the constant used in `nontangential_from_simple`). Then $T_*$ has bounded strong type $(2,2)$ with constant $C_{10.0.2}(a)$.

### `cotlar_estimate`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hg : BoundedFiniteSupport g volume) (hr : r ∈ Set.Ioc 0 R) : ‖czOperator K R g x‖ₑ ≤ 4 * globalMaximalFunction volume 1 (czOperator K r g) x + ↑(C10_1_5 a) * globalMaximalFunction volume 1 g x`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r R : ℝ} {K : X → X → ℂ} {x : X} [IsTwoSidedKernel a K], (4 : ℕ) ≤ a → (∀ r > (0 : ℝ), HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (czOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → ∀ {g : X → ℂ}, BoundedFiniteSupport g volume → r ∈ Set.Ioc (0 : ℝ) R → ‖czOperator K R g x‖ₑ ≤ (4 : ENNReal) * globalMaximalFunction volume (1 : ℝ) (czOperator K r g) x + ↑(C10_1_5 a) * globalMaximalFunction volume (1 : ℝ) g x`
Docstring: Lemma 10.1.5
English: (Lemma 10.1.5.) Let $X$ be a metric space and $a\in\mathbb N$, and assume $X$ carries a project `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$ (docstring: a metric space with a measure with some nice properties, including a doubling condition); denote its measure (`volume`) by $\mu$. Let $K : X\to X\to\mathbb C$ satisfy the project predicate `IsTwoSidedKernel a K` (docstring: $K$ is a two-sided Calderón–Zygmund kernel), and assume $a\ge 4$. For $t\in\mathbb R$, $h : X\to\mathbb C$ and $z\in X$ let $T_t h(z)=\mathrm{czOperator}(K,t,h)(z)=\int_{X\setminus B(z,t)}K(z,y)\,h(y)\,d\mu(y)$. Say that an operator $T$ taking functions $X\to\mathbb C$ to functions on $X$ (with values in $\mathbb C$ or $[0,\infty]$) has bounded strong type $(2,2)$ with constant $C\in[0,\infty]$ (project `HasBoundedStrongType T 2 2 μ μ C`) if for every $h : X\to\mathbb C$ that is bounded, measurable and supported on a set of finite measure (`BoundedFiniteSupport h μ`), $Th$ is almost everywhere strongly measurable and $\|Th\|_{L^2(\mu)}\le C\,\|h\|_{L^2(\mu)}$. Let $C_{Ts}(a)=2^{a^3}$ (project constant `C_Ts a`), and assume that for every real $t>0$ the operator $T_t$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$. Let $M h(z)\in[0,\infty]$ denote the project maximal function `globalMaximalFunction μ 1 h z` (docstring: the uncentered Hardy–Littlewood maximal function), with exponent $1$. Let $C_{10.1.5}(a)\in\mathbb R_{\ge0}$ be the project constant `C10_1_5 a` (docstring: the constant used in `cotlar_estimate`). Let $r,R\in\mathbb R$ with $0<r\le R$, let $x\in X$, and let $g : X\to\mathbb C$ be bounded, measurable and supported on a set of finite $\mu$-measure (`BoundedFiniteSupport g μ`). Then $$\|T_R g(x)\|_e\le 4\,M(T_r g)(x)+C_{10.1.5}(a)\,Mg(x)$$ in $[0,\infty]$.

### `cotlar_set_F₂`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hr : 0 < r) (hR : r ≤ R) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hg : BoundedFiniteSupport g volume) : (volume.restrict (Metric.ball x (R / 4))) {x' | ↑(C10_1_4 a) * globalMaximalFunction volume 1 g x < ‖czOperator K r ((Metric.ball x (R / 2)).indicator g) x'‖ₑ} ≤ volume (Metric.ball x (R / 4)) / 4`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r R : ℝ} {K : X → X → ℂ} {x : X} [IsTwoSidedKernel a K], (4 : ℕ) ≤ a → (0 : ℝ) < r → r ≤ R → (∀ r > (0 : ℝ), HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (czOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → ∀ {g : X → ℂ}, BoundedFiniteSupport g volume → (Measure.restrict volume (Metric.ball x (R / (4 : ℝ))) : Measure X) {x' : X | ↑(C10_1_4 a) * globalMaximalFunction volume (1 : ℝ) g x < ‖czOperator K r ((Metric.ball x (R / (2 : ℝ))).indicator g) x'‖ₑ} ≤ HDiv.hDiv (α := ENNReal) ((volume : Measure X) (Metric.ball x (R / (4 : ℝ))) : ENNReal) (4 : ENNReal)`
Docstring: Part 2 of Lemma 10.1.4 about `F₂`.
English: (Part 2 of Lemma 10.1.4, about $F_2$.) Let $X$ be a metric space and $a\in\mathbb N$, and assume $X$ carries a project `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$ (docstring: a metric space with a measure with some nice properties, including a doubling condition); denote its measure (`volume`) by $\mu$. Let $K : X\to X\to\mathbb C$ satisfy the project predicate `IsTwoSidedKernel a K` (docstring: $K$ is a two-sided Calderón–Zygmund kernel), and assume $a\ge 4$. For $t\in\mathbb R$, $h : X\to\mathbb C$ and $z\in X$ let $T_t h(z)=\mathrm{czOperator}(K,t,h)(z)=\int_{X\setminus B(z,t)}K(z,y)\,h(y)\,d\mu(y)$. Say that an operator $T$ taking functions $X\to\mathbb C$ to functions on $X$ (with values in $\mathbb C$ or $[0,\infty]$) has bounded strong type $(2,2)$ with constant $C\in[0,\infty]$ (project `HasBoundedStrongType T 2 2 μ μ C`) if for every $h : X\to\mathbb C$ that is bounded, measurable and supported on a set of finite measure (`BoundedFiniteSupport h μ`), $Th$ is almost everywhere strongly measurable and $\|Th\|_{L^2(\mu)}\le C\,\|h\|_{L^2(\mu)}$. Let $C_{Ts}(a)=2^{a^3}$ (project constant `C_Ts a`), and assume that for every real $t>0$ the operator $T_t$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$. Let $M h(z)\in[0,\infty]$ denote the project maximal function `globalMaximalFunction μ 1 h z` (docstring: the uncentered Hardy–Littlewood maximal function), with exponent $1$. Let $C_{10.1.4}(a)\in\mathbb R_{\ge0}$ be the project constant `C10_1_4 a` (docstring: the constant used in `cotlar_set_F₂`). Let $r,R\in\mathbb R$ with $0<r\le R$, let $x\in X$, and let $g : X\to\mathbb C$ be bounded, measurable and supported on a set of finite $\mu$-measure (`BoundedFiniteSupport g μ`). Then $$\mu\Big(B(x,R/4)\cap\big\{x'\in X : C_{10.1.4}(a)\,Mg(x)<\|T_r(\mathbf 1_{B(x,R/2)}\,g)(x')\|_e\big\}\Big)\le\frac{\mu(B(x,R/4))}{4}.$$

### `simple_nontangential_operator`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hr : 0 < r) : HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r : ℝ} {K : X → X → ℂ} [IsTwoSidedKernel a K], (4 : ℕ) ≤ a → (∀ r > (0 : ℝ), HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (czOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → (0 : ℝ) < r → HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (simpleNontangentialOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C10_1_6 a)`
Docstring: Lemma 10.1.6. The formal statement includes the measurability of the operator. See also `simple_nontangential_operator_le`
English: (Lemma 10.1.6; per the docstring, the formal statement includes measurability of the operator.) Let $X$ be a metric space and $a\in\mathbb N$, and assume $X$ carries a project `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$ (docstring: a metric space with a measure with some nice properties, including a doubling condition); denote its measure (`volume`) by $\mu$. Let $K : X\to X\to\mathbb C$ satisfy the project predicate `IsTwoSidedKernel a K` (docstring: $K$ is a two-sided Calderón–Zygmund kernel), and assume $a\ge 4$. For $t\in\mathbb R$, $h : X\to\mathbb C$ and $z\in X$ let $T_t h(z)=\mathrm{czOperator}(K,t,h)(z)=\int_{X\setminus B(z,t)}K(z,y)\,h(y)\,d\mu(y)$. Say that an operator $T$ taking functions $X\to\mathbb C$ to functions on $X$ (with values in $\mathbb C$ or $[0,\infty]$) has bounded strong type $(2,2)$ with constant $C\in[0,\infty]$ (project `HasBoundedStrongType T 2 2 μ μ C`) if for every $h : X\to\mathbb C$ that is bounded, measurable and supported on a set of finite measure (`BoundedFiniteSupport h μ`), $Th$ is almost everywhere strongly measurable and $\|Th\|_{L^2(\mu)}\le C\,\|h\|_{L^2(\mu)}$. Let $C_{Ts}(a)=2^{a^3}$ (project constant `C_Ts a`), and assume that for every real $t>0$ the operator $T_t$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$. For real $t$ let $T_*^t$ be the project operator `simpleNontangentialOperator K t` (docstring: the operator $T_*^r g(x)$ defined in (10.1.31)), $T_*^t h(z)=\sup_{R\in\mathbb R,\,R>t}\ \sup_{z'\in B(z,R)}\|T_R h(z')\|_e\in[0,\infty]$. Let $C_{10.1.6}(a)\in\mathbb R_{\ge0}$ be the project constant `C10_1_6 a` (docstring: the constant used in `simple_nontangential_operator`). Let $r\in\mathbb R$ with $r>0$. Then $T_*^r$ has bounded strong type $(2,2)$ with constant $C_{10.1.6}(a)$.

### `simple_nontangential_operator_le`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hr : 0 ≤ r) : HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r : ℝ} {K : X → X → ℂ} [IsTwoSidedKernel a K], (4 : ℕ) ≤ a → (∀ r > (0 : ℝ), HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (czOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → (0 : ℝ) ≤ r → HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (simpleNontangentialOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C10_1_6 a)`
Docstring: This is the first step of the proof of Lemma 10.0.2, and should follow from 10.1.6 + monotone convergence theorem. (measurability should be proven without any restriction on `r`.)
English: Let $X$ be a metric space and $a\in\mathbb N$, and assume $X$ carries a project `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$ (docstring: a metric space with a measure with some nice properties, including a doubling condition); denote its measure (`volume`) by $\mu$. Let $K : X\to X\to\mathbb C$ satisfy the project predicate `IsTwoSidedKernel a K` (docstring: $K$ is a two-sided Calderón–Zygmund kernel), and assume $a\ge 4$. For $t\in\mathbb R$, $h : X\to\mathbb C$ and $z\in X$ let $T_t h(z)=\mathrm{czOperator}(K,t,h)(z)=\int_{X\setminus B(z,t)}K(z,y)\,h(y)\,d\mu(y)$. Say that an operator $T$ taking functions $X\to\mathbb C$ to functions on $X$ (with values in $\mathbb C$ or $[0,\infty]$) has bounded strong type $(2,2)$ with constant $C\in[0,\infty]$ (project `HasBoundedStrongType T 2 2 μ μ C`) if for every $h : X\to\mathbb C$ that is bounded, measurable and supported on a set of finite measure (`BoundedFiniteSupport h μ`), $Th$ is almost everywhere strongly measurable and $\|Th\|_{L^2(\mu)}\le C\,\|h\|_{L^2(\mu)}$. Let $C_{Ts}(a)=2^{a^3}$ (project constant `C_Ts a`), and assume that for every real $t>0$ the operator $T_t$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$. For real $t$ let $T_*^t$ be the project operator `simpleNontangentialOperator K t` (docstring: the operator $T_*^r g(x)$ defined in (10.1.31)), $T_*^t h(z)=\sup_{R\in\mathbb R,\,R>t}\ \sup_{z'\in B(z,R)}\|T_R h(z')\|_e\in[0,\infty]$. Let $C_{10.1.6}(a)\in\mathbb R_{\ge0}$ be the project constant `C10_1_6 a` (docstring: the constant used in `simple_nontangential_operator`). Let $r\in\mathbb R$ with $r\ge 0$. Then $T_*^r$ has bounded strong type $(2,2)$ with constant $C_{10.1.6}(a)$.
