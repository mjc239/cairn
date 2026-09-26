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
A definition whose body is shown must be described by what it defines (in words or a formula that agrees with the
body), not only by a paraphrase of its docstring. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `BoundedFiniteSupport` (structure or class)
Lean: `{X : Type u_3} → {E : Type u_4} → [inst : MeasurableSpace X] → [TopologicalSpace E] → [ENorm E] → [Zero E] → (X → E) → autoParam (Measure X) BoundedFiniteSupport._auto_1 → Prop`
Docstring: Bounded measurable function $g$ on $X$ supported on a set of finite measure
Constructor (every field with its type): `∀ {X : Type u_3} {E : Type u_4} [inst : MeasurableSpace X] [inst_1 : TopologicalSpace E] [inst_2 : ENorm E] [inst_3 : Zero E] {f : X → E} {μ : autoParam (Measure X) BoundedFiniteSupport._auto_1}, MemLp f ⊤ μ → LT.lt (α := ENNReal) (μ (Function.support f) : ENNReal) (⊤ : ENNReal) → BoundedFiniteSupport f μ`

#### `C10_0_3` (def)
Lean: `ℕ → NNReal`
Docstring: The constant used in `czOperator_weak_1_1`.
Definition: `wrapped✝.1`

#### `C_Ts` (def)
Lean: `ℕ → NNReal`
Docstring: A constant used on the boundedness of `T_Q^θ` and `T_*`. We generally assume `HasBoundedStrongType (linearizedNontangentialOperator Q θ K · ·) 2 2 volume volume (C_Ts a)` throughout this formalization.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ a ^ (3 : ℕ)`

#### `IsTwoSidedKernel` (structure or class)
Lean: `{X : Type u_1} → [PseudoMetricSpace X] → [MeasureSpace X] → outParam ℕ → (X → X → ℂ) → Prop`
Docstring: `K` is a two-sided Calderon-Zygmund kernel. In the formalization `K x y` is defined everywhere, even for `x = y`. The assumptions on `K` show that `K x x = 0`.
Constructor (every field with its type): `∀ {X : Type u_1} [inst : PseudoMetricSpace X] [inst_1 : MeasureSpace X] {a : outParam ℕ} {K : X → X → ℂ} [toIsOneSidedKernel : IsOneSidedKernel a K], (∀ {x x' y : X}, (2 : ℝ) * dist x x' ≤ dist x y → ‖K x y - K x' y‖ₑ ≤ HPow.hPow (β := ℝ) (edist x x' / edist x y) (↑a)⁻¹ * (↑(C_K ↑a) / vol x y)) → IsTwoSidedKernel a K`

#### `MeasureTheory.DoublingMeasure` (structure or class)
Lean: `(X : Type u_3) → outParam NNReal → [PseudoMetricSpace X] → Type u_3`
Docstring: A metric space with a measure with some nice properties, including a doubling condition. This is called a "doubling metric measure space" in the blueprint. `A` will usually be `2 ^ a`.
Constructor (every field with its type): `{X : Type u_3} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [toCompleteSpace : CompleteSpace X] → [toLocallyCompactSpace : LocallyCompactSpace X] → [toMeasureSpace : MeasureSpace X] → [toBorelSpace : BorelSpace X] → [toIsLocallyFiniteMeasure : IsLocallyFiniteMeasure.{u_3} (α := X) (m0 := MeasureSpace.toMeasurableSpace) volume] → [toIsDoubling : Measure.IsDoubling.{u_3} (X := X) volume A] → [toNeZero : NeZero.{u_3} (R := Measure X) volume] → DoublingMeasure X A`

#### `MeasureTheory.DoublingMeasure.toMeasureSpace` (def)
Lean: `{X : Type u_3} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → [self : DoublingMeasure X A] → MeasureSpace X`
Definition: `fun (X : Type u_3) {A : outParam NNReal} {inst : PseudoMetricSpace X} [self : DoublingMeasure X A] => self.3`

#### `MeasureTheory.HasBoundedStrongType` (def)
Lean: `{ε₁ : Type u_3} → {ε₂ : Type u_4} → [ENorm ε₁] → [ENorm ε₂] → [TopologicalSpace ε₁] → [TopologicalSpace ε₂] → [Zero ε₁] → {α : Type u_5} → {α' : Type u_6} → {_x : MeasurableSpace α} → {_x' : MeasurableSpace α'} → ((α → ε₁) → α' → ε₂) → ENNReal → ENNReal → Measure α → Measure α' → ENNReal → Prop`
Docstring: A weaker version of `HasStrongType`. This is the same as `HasStrongType` if `T` is continuous w.r.t. the L^2 norm, but weaker in general.
Definition: `fun {ε₁ : Type u_3} {ε₂ : Type u_4} [ENorm ε₁] [ENorm ε₂] [TopologicalSpace ε₁] [TopologicalSpace ε₂] [Zero ε₁] {α : Type u_5} {α' : Type u_6} {_x : MeasurableSpace α} {_x' : MeasurableSpace α'} (T : (α → ε₁) → α' → ε₂) (p p' : ENNReal) (μ : Measure α) (ν : Measure α') (c : ENNReal) => ∀ (f : α → ε₁), BoundedFiniteSupport f μ → AEStronglyMeasurable (T f) ν ∧ eLpNorm (T f) p' ν ≤ c * eLpNorm f p μ`

#### `MeasureTheory.distribution` (def)
Lean: `{α : Type u_1} → {ε : Type u_3} → {m : MeasurableSpace α} → [ENorm ε] → (α → ε) → ENNReal → Measure α → ENNReal`
Docstring: The distribution function of a function `f`. Todo: rename to something more Mathlib-appropriate.
Definition: `fun {α : Type u_1} {ε : Type u_3} {m : MeasurableSpace α} [ENorm ε] (f : α → ε) (t : ENNReal) (μ : Measure α) => μ {x : α | t < ‖f x‖ₑ}`

#### `czOperator` (def)
Lean: `{X : Type u_2} → [PseudoMetricSpace X] → [MeasureSpace X] → (X → X → ℂ) → ℝ → (X → ℂ) → X → ℂ`
Docstring: The Calderon Zygmund operator `T_r` in chapter Two-sided Metric Space Carleson
Definition: `fun {X : Type u_2} [PseudoMetricSpace X] [MeasureSpace X] (K : X → X → ℂ) (r : ℝ) (f : X → ℂ) (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume (Metric.ball x r)ᶜ) fun (y : X) => K x y * f y`

#### `defaultA` (def)
Lean: `ℕ → ℕ`
Docstring: This is usually the value of the argument `A` in `DoublingMeasure` and `CompatibleFunctions`
Definition: `fun (a : ℕ) => (2 : ℕ) ^ a`

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
Constructor (every field with its type): `∀ {X : Type u_1} [inst : PseudoMetricSpace X] [inst_1 : MeasureSpace X] {a : outParam ℕ} {K : X → X → ℂ}, Measurable (Function.uncurry K) → (∀ (x y : X), ‖K x y‖ ≤ ↑(C_K ↑a) / Real.vol x y) → (∀ {x y y' : X}, (2 : ℝ) * dist y y' ≤ dist x y → ‖K x y - K x y'‖ ≤ HPow.hPow (β := ℝ) (dist y y' / dist x y) (↑a)⁻¹ * (↑(C_K ↑a) / Real.vol x y)) → IsOneSidedKernel a K`

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
Constructor (every field with its type): `∀ {X : Type u_3} [inst : MeasurableSpace X] [inst_1 : PseudoMetricSpace X] {μ : Measure X} {A : outParam NNReal}, (∀ (x : X) (r : ℝ), μ (Metric.ball x ((2 : ℝ) * r)) ≤ HMul.hMul (β := ENNReal) ↑A (μ (Metric.ball x r) : ENNReal)) → μ.IsDoubling A`

## Translations

### `estimate_czOperator`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hr : 0 < r) (hf : BoundedFiniteSupport f volume) (hT : HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) : distribution (czOperator K r f) α volume ≤ ↑(C10_0_3 a) / α * eLpNorm f 1 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r : ℝ} {K : X → X → ℂ} [IsTwoSidedKernel a K] {f : X → ℂ} {α : ENNReal}, (4 : ℕ) ≤ a → (0 : ℝ) < r → BoundedFiniteSupport f volume → HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (czOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a) → distribution (m := MeasureSpace.toMeasurableSpace) (czOperator K r f) α volume ≤ ↑(C10_0_3 a) / α * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (1 : ENNReal) volume`
Docstring: Lemma 10.0.3, blueprint form.
English: (Lemma 10.0.3, blueprint form.) Let $a$ be a natural number and let $X$ be a metric space equipped with a $\mathrm{DoublingMeasure}$ structure with constant $\mathrm{defaultA}(a) = 2^a$ (per its docstring, a measure on $X$ with some nice properties including a doubling condition, i.e. a doubling metric measure space); write $\mathrm{vol}$ for this measure (Lean's $\mathrm{volume}$). Let $K : X \to X \to \mathbb{C}$ satisfy $\mathrm{IsTwoSidedKernel}\ a\ K$ (per its docstring, $K$ is a two-sided Calderón–Zygmund kernel, with parameter $a$). Let $r$ be a real number, $f : X \to \mathbb{C}$, and $\alpha \in [0,\infty]$. For $g : X \to \mathbb{C}$ and $x \in X$ let $T_r g(x) = \mathrm{czOperator}\ K\ r\ g\ x = \int_{X \setminus B(x,r)} K(x,y)\,g(y)\,d\mathrm{vol}(y)$, where $B(x,r)$ is the open ball. Assume $4 \le a$, $0 < r$, and that $f$ satisfies $\mathrm{BoundedFiniteSupport}\ f\ \mathrm{vol}$ (per its docstring, $f$ is a bounded measurable function supported on a set of finite measure). Assume $\mathrm{HasBoundedStrongType}\ T_r\ 2\ 2\ \mathrm{vol}\ \mathrm{vol}\ C_{Ts}(a)$ with $C_{Ts}(a) = 2^{a^3}$, i.e. for every $g : X \to \mathbb{C}$ with $\mathrm{BoundedFiniteSupport}\ g\ \mathrm{vol}$, $T_r g$ is a.e. strongly measurable and $\|T_r g\|_{L^2(\mathrm{vol})} \le C_{Ts}(a)\,\|g\|_{L^2(\mathrm{vol})}$. Then
$$\mathrm{vol}\{x \in X : \alpha < \|T_r f(x)\|_e\} \le \frac{C_{10.0.3}(a)}{\alpha}\,\|f\|_{L^1(\mathrm{vol})},$$
where the left side is $\mathrm{distribution}(T_r f, \alpha, \mathrm{vol})$, $\|\cdot\|_e$ is the extended norm (here the absolute value in $[0,\infty]$), $C_{10.0.3}(a) = \mathrm{C10\_0\_3}\ a$ is a nonnegative real constant (the constant of $\mathrm{czOperator\_weak\_1\_1}$), $\|\cdot\|_{L^p}$ is $\mathrm{eLpNorm}$, and the division and product are computed in $[0,\infty]$.
