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

## Flagged translations

### `nontangential_from_simple`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) : HasBoundedStrongType (nontangentialOperator K) 2 2 volume volume ↑(C10_0_2 a)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {K : X → X → ℂ} [IsTwoSidedKernel a K], (4 : ℕ) ≤ a → (∀ r > (0 : ℝ), HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (czOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (nontangentialOperator K) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C10_0_2 a)`
Docstring: Lemma 10.0.2. The formal statement includes the measurability of the operator.
Previous English: (Lemma 10.0.2.) Let $X$ be a metric space equipped with a doubling measure `volume` with doubling constant $A$ = `defaultA a` (for $a \in \mathbb{N}$), and let $K : X \times X \to \mathbb{C}$ be a two-sided Calderón–Zygmund kernel with parameter $a$ (`IsTwoSidedKernel a K`). Let $a \ge 4$ and suppose that for every $r > 0$, $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$. Then the nontangential operator $\mathrm{nontangentialOperator}(K)$ has bounded strong type $(2,2)$ with constant $C_{10.0.2}(a)$ (including measurability of the operator).
Checker's issue: The English calls K a 'Calderón–Zygmund kernel', a description of IsTwoSidedKernel that neither the prompt nor a docstring supports.

### `cotlar_estimate`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hg : BoundedFiniteSupport g volume) (hr : r ∈ Set.Ioc 0 R) : ‖czOperator K R g x‖ₑ ≤ 4 * globalMaximalFunction volume 1 (czOperator K r g) x + ↑(C10_1_5 a) * globalMaximalFunction volume 1 g x`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r R : ℝ} {K : X → X → ℂ} {x : X} [IsTwoSidedKernel a K], (4 : ℕ) ≤ a → (∀ r > (0 : ℝ), HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (czOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → ∀ {g : X → ℂ}, BoundedFiniteSupport g volume → r ∈ Set.Ioc (0 : ℝ) R → ‖czOperator K R g x‖ₑ ≤ (4 : ENNReal) * globalMaximalFunction volume (1 : ℝ) (czOperator K r g) x + ↑(C10_1_5 a) * globalMaximalFunction volume (1 : ℝ) g x`
Docstring: Lemma 10.1.5
Previous English: (Lemma 10.1.5, Cotlar's estimate.) Let $X$ be a metric space equipped with a doubling measure `volume` with doubling constant $A$ = `defaultA a` (for $a \in \mathbb{N}$), and let $K : X \times X \to \mathbb{C}$ be a two-sided Calderón–Zygmund kernel with parameter $a$ (`IsTwoSidedKernel a K`). Let $a \ge 4$, suppose $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$ for every $r > 0$, let $g : X \to \mathbb{C}$ be bounded with finite-measure support, and $r \in (0, R]$. Then $\|\mathrm{czOperator}(K, R)\, g(x)\| \le 4\, M(\mathrm{czOperator}(K, r)\, g)(x) + C_{10.1.5}(a)\, M g(x)$, where $M = \mathrm{globalMaximalFunction}(\mathrm{vol}, 1)$.
Checker's issue: The English calls K a 'Calderón–Zygmund kernel', a description of IsTwoSidedKernel that neither the prompt nor a docstring supports. The point x : X is never introduced, and r, R are not stated to be real. The name 'Cotlar's estimate' is not in the docstring.

### `cotlar_set_F₂`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hr : 0 < r) (hR : r ≤ R) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hg : BoundedFiniteSupport g volume) : (volume.restrict (Metric.ball x (R / 4))) {x' | ↑(C10_1_4 a) * globalMaximalFunction volume 1 g x < ‖czOperator K r ((Metric.ball x (R / 2)).indicator g) x'‖ₑ} ≤ volume (Metric.ball x (R / 4)) / 4`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r R : ℝ} {K : X → X → ℂ} {x : X} [IsTwoSidedKernel a K], (4 : ℕ) ≤ a → (0 : ℝ) < r → r ≤ R → (∀ r > (0 : ℝ), HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (czOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → ∀ {g : X → ℂ}, BoundedFiniteSupport g volume → (Measure.restrict volume (Metric.ball x (R / (4 : ℝ))) : Measure X) {x' : X | ↑(C10_1_4 a) * globalMaximalFunction volume (1 : ℝ) g x < ‖czOperator K r ((Metric.ball x (R / (2 : ℝ))).indicator g) x'‖ₑ} ≤ HDiv.hDiv (α := ENNReal) ((volume : Measure X) (Metric.ball x (R / (4 : ℝ))) : ENNReal) (4 : ENNReal)`
Docstring: Part 2 of Lemma 10.1.4 about `F₂`.
Previous English: (Lemma 10.1.4, part about $F_2$.) Let $X$ be a metric space equipped with a doubling measure `volume` with doubling constant $A$ = `defaultA a` (for $a \in \mathbb{N}$), and let $K : X \times X \to \mathbb{C}$ be a two-sided Calderón–Zygmund kernel with parameter $a$ (`IsTwoSidedKernel a K`). Let $a \ge 4$, $0 < r \le R$, suppose $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$ for every $r > 0$, and let $g : X \to \mathbb{C}$ be bounded with finite-measure support. Then $\mathrm{vol}\big(B(x, R/4) \cap \{x' : C_{10.1.4}(a)\, M g(x) < \|\mathrm{czOperator}(K, r)(\mathbf{1}_{B(x, R/2)} g)(x')\|\}\big) \le \mathrm{vol}(B(x, R/4))/4$, where $M = \mathrm{globalMaximalFunction}(\mathrm{vol}, 1)$.
Checker's issue: The English calls K a 'Calderón–Zygmund kernel', a description of IsTwoSidedKernel that neither the prompt nor a docstring supports. The point x : X is never introduced, and r, R are not stated to be real.

### `simple_nontangential_operator`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hr : 0 < r) : HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r : ℝ} {K : X → X → ℂ} [IsTwoSidedKernel a K], (4 : ℕ) ≤ a → (∀ r > (0 : ℝ), HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (czOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → (0 : ℝ) < r → HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (simpleNontangentialOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C10_1_6 a)`
Docstring: Lemma 10.1.6. The formal statement includes the measurability of the operator. See also `simple_nontangential_operator_le`
Previous English: (Lemma 10.1.6.) Let $X$ be a metric space equipped with a doubling measure `volume` with doubling constant $A$ = `defaultA a` (for $a \in \mathbb{N}$), and let $K : X \times X \to \mathbb{C}$ be a two-sided Calderón–Zygmund kernel with parameter $a$ (`IsTwoSidedKernel a K`). Let $a \ge 4$, suppose $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$ for every $r > 0$, and let $r > 0$. Then $\mathrm{simpleNontangentialOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{10.1.6}(a)$ (including measurability of the operator).
Checker's issue: The English calls K a 'Calderón–Zygmund kernel', a description of IsTwoSidedKernel that neither the prompt nor a docstring supports.

### `simple_nontangential_operator_le`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] (ha : 4 ≤ a) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hr : 0 ≤ r) : HasBoundedStrongType (simpleNontangentialOperator K r) 2 2 volume volume ↑(C10_1_6 a)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {r : ℝ} {K : X → X → ℂ} [IsTwoSidedKernel a K], (4 : ℕ) ≤ a → (∀ r > (0 : ℝ), HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (czOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → (0 : ℝ) ≤ r → HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (simpleNontangentialOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C10_1_6 a)`
Docstring: This is the first step of the proof of Lemma 10.0.2, and should follow from 10.1.6 + monotone convergence theorem. (measurability should be proven without any restriction on `r`.)
Previous English: Let $X$ be a metric space equipped with a doubling measure `volume` with doubling constant $A$ = `defaultA a` (for $a \in \mathbb{N}$), and let $K : X \times X \to \mathbb{C}$ be a two-sided Calderón–Zygmund kernel with parameter $a$ (`IsTwoSidedKernel a K`). Let $a \ge 4$, suppose $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{Ts}(a)$ for every $r > 0$, and let $r \ge 0$. Then $\mathrm{simpleNontangentialOperator}(K, r)$ has bounded strong type $(2,2)$ with constant $C_{10.1.6}(a)$.
Checker's issue: The English calls K a 'Calderón–Zygmund kernel', a description of IsTwoSidedKernel that neither the prompt nor a docstring supports.
