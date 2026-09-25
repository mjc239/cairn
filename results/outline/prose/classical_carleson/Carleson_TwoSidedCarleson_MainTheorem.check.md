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

#### `C10_0_1` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant used in `two_sided_metric_carleson`. Has value `2 ^ (474 * a ^ 3) / (q - 1) ^ 6` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => C_K ↑a ^ (2 : ℕ) * C1_0_2 a q`

#### `C_Ts` (def)
Lean: `ℕ → NNReal`
Docstring: A constant used on the boundedness of `T_Q^θ` and `T_*`. We generally assume `HasBoundedStrongType (linearizedNontangentialOperator Q θ K · ·) 2 2 volume volume (C_Ts a)` throughout this formalization.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ a ^ (3 : ℕ)`

#### `CompatibleFunctions` (structure or class)
Lean: `(𝕜 : outParam (Type u_3)) → (X : Type u) → outParam ℕ → [RCLike 𝕜] → [PseudoMetricSpace X] → Type (max (u + 1) u_3)`
Docstring: A set `Θ` of (continuous) functions is compatible. `A` will usually be `2 ^ a`.
Constructor (every field with its type): `{𝕜 : outParam (Type u_3)} → {X : Type u} → {A : outParam ℕ} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [toFunctionDistances : FunctionDistances 𝕜 X] → (∃ (o : X), ∀ (f : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), (coeΘ f) o = (0 : 𝕜)) → (∀ {x : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, localOscillation (Metric.ball x r) (coeΘ f) (coeΘ g) ≤ ENNReal.ofReal (dist_{x, r} f g)) → (∀ {x₁ x₂ : X} {r₁ r₂ : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, Metric.ball x₁ r₁ ⊆ Metric.ball x₂ r₂ → dist_{x₁, r₁} f g ≤ dist_{x₂, r₂} f g) → (∀ {x₁ x₂ : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, dist x₁ x₂ < (2 : ℝ) * r → dist_{x₂, (2 : ℝ) * r} f g ≤ ↑A * dist_{x₁, r} f g) → (∀ {x₁ x₂ : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, Metric.ball x₁ r ⊆ Metric.ball x₂ (↑A * r) → (2 : ℝ) * dist_{x₁, r} f g ≤ dist_{x₂, ↑A * r} f g) → (∀ {x : X} {r : ℝ}, AllBallsCoverBalls.{u} (WithFunctionDistance x r) (2 : ℝ) A) → CompatibleFunctions 𝕜 X A`

#### `CompatibleFunctions.toFunctionDistances` (def)
Lean: `{𝕜 : outParam (Type u_3)} → {X : Type u} → {A : outParam ℕ} → {inst : RCLike 𝕜} → {inst_1 : PseudoMetricSpace X} → [self : CompatibleFunctions 𝕜 X A] → FunctionDistances 𝕜 X`
Definition: `fun {𝕜 : outParam (Type u_3)} (X : Type u) {A : outParam ℕ} {inst : RCLike 𝕜} {inst_1 : PseudoMetricSpace X} [self : CompatibleFunctions 𝕜 X A] => self.1`

#### `IsCancellative` (structure or class)
Lean: `(X : Type u_2) → {A : ℕ} → [inst : PseudoMetricSpace X] → [DoublingMeasure X ↑A] → ℝ → [CompatibleFunctions ℝ X A] → Prop`
Docstring: Θ is τ-cancellative. `τ` will usually be `1 / a`
Constructor (every field with its type): `∀ {X : Type u_2} {A : ℕ} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X ↑A] {τ : ℝ} [inst_2 : CompatibleFunctions ℝ X A], (∀ {x : X} {r : ℝ} {φ : X → ℂ}, (0 : ℝ) < r → iLipENorm φ x r ≠ ⊤ → Function.support φ ⊆ Metric.ball x r → ∀ {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => Complex.exp (Complex.I * (↑(f x) - ↑(g x))) * φ x) ≤ HMul.hMul (α := ENNReal) (β := ENNReal) (↑A : ENNReal) ((volume : Measure X) (Metric.ball x r) : ENNReal) * iLipENorm φ x r * ((1 : ENNReal) + edist_{x, r} f g) ^ (-τ)) → IsCancellative X τ`

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

#### `carlesonOperator` (def)
Lean: `{X : Type u_2} → {A : ℕ} → [inst : PseudoMetricSpace X] → [DoublingMeasure X ↑A] → [FunctionDistances ℝ X] → (X → X → ℂ) → (X → ℂ) → X → ENNReal`
Docstring: The generalized Carleson operator `T`, taking values in `ℝ≥0∞`. Use `ENNReal.toReal` to get the corresponding real number.
Definition: `fun {X : Type u_2} {A : ℕ} [PseudoMetricSpace X] [DoublingMeasure X ↑A] [FunctionDistances ℝ X] (K : X → X → ℂ) (f : X → ℂ) (x : X) => ⨆ (θ : @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _), linearizedCarlesonOperator (fun (x : X) => θ) K f x`

#### `czOperator` (def)
Lean: `{X : Type u_2} → [PseudoMetricSpace X] → [MeasureSpace X] → (X → X → ℂ) → ℝ → (X → ℂ) → X → ℂ`
Docstring: The Calderon Zygmund operator `T_r` in chapter Two-sided Metric Space Carleson
Definition: `fun {X : Type u_2} [PseudoMetricSpace X] [MeasureSpace X] (K : X → X → ℂ) (r : ℝ) (f : X → ℂ) (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume (Metric.ball x r)ᶜ) fun (y : X) => K x y * f y`

#### `defaultA` (def)
Lean: `ℕ → ℕ`
Docstring: This is usually the value of the argument `A` in `DoublingMeasure` and `CompatibleFunctions`
Definition: `fun (a : ℕ) => (2 : ℕ) ^ a`

#### `defaultτ` (def)
Lean: `ℕ → ℝ`
Docstring: `defaultτ` is the inverse of `a`.
Definition: `fun (a : ℕ) => (↑a)⁻¹`

#### `C1_0_2` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant used in `MetricSpaceCarleson` and `LinearizedMetricCarleson`. Has value `2 ^ (443 * a ^ 3) / (q - 1) ^ 6` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => (2 : NNReal) ^ (((3 : ℕ) * 𝕔 + (18 : ℕ) + (5 : ℕ) * (𝕔 / (4 : ℕ))) * a ^ (3 : ℕ)) / (q - (1 : NNReal)) ^ (6 : ℕ)`

#### `C_K` (def)
Lean: `ℝ → NNReal`
Docstring: The constant used twice in the definition of the Calderon-Zygmund kernel.
Definition: `fun (a : ℝ) => (2 : NNReal) ^ a ^ (3 : ℕ)`

#### `partialFourierSum` (def)
Lean: `ℕ → (ℝ → ℂ) → ℝ → ℂ`
Docstring: The Nᵗʰ partial Fourier sum of `f : ℝ → ℂ` for `N : ℕ`.
Definition: `fun (N : ℕ) (f : ℝ → ℂ) (x : ℝ) => ∑ n ∈ Finset.Icc (-↑N) ↑N, HMul.hMul (β := ℂ) (fourierCoeffOn Real.two_pi_pos f n) ((fourier n) ↑x : ℂ)`

#### `AllBallsCoverBalls` (def)
Lean: `(X : Type u_2) → [PseudoMetricSpace X] → ℝ → ℕ → Prop`
Docstring: For all `r`, balls of radius `r` in `X` are covered by `n` balls of radius `a * r`
Definition: `fun (X : Type u_2) [PseudoMetricSpace X] (a : ℝ) (n : ℕ) => ∀ (r : ℝ), BallsCoverBalls X (a * r) r n`

#### `FunctionDistances` (structure or class)
Lean: `(𝕜 : outParam (Type u_1)) → (X : Type u) → [NormedField 𝕜] → [TopologicalSpace X] → Type (max (u + 1) u_1)`
Docstring: A class stating that continuous functions have distances associated to every ball. We use a separate type to conveniently index these functions.
Constructor (every field with its type): `{𝕜 : outParam (Type u_1)} → {X : Type u} → [inst : NormedField 𝕜] → [inst_1 : TopologicalSpace X] → (Θ : Type u) → (coeΘ : Θ → C(X, 𝕜)) → (∀ {f g : Θ}, (∀ (x : X), Eq.{u_1 + 1} (α := 𝕜) ((coeΘ f) x : 𝕜) ((coeΘ g) x : 𝕜)) → f = g) → (X → ℝ → PseudoMetricSpace Θ) → FunctionDistances 𝕜 X`

#### `FunctionDistances.coeΘ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → @Θ _ X inst inst_1 _ → C(X, 𝕜)`
Docstring: The coercion map from `Θ` to `C(X, 𝕜)`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.2`

#### `FunctionDistances.Θ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → (X : Type u) → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → Type u`
Docstring: A type of continuous functions from `X` to `𝕜`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.1`

#### `WithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → X → ℝ → Type u_2`
Docstring: Class used to endow `Θ X` with a pseudometric space structure.
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] (x : X) (r : ℝ) => @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`

#### `instPseudoMetricSpaceWithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → {x : X} → {r : ℝ} → PseudoMetricSpace (WithFunctionDistance x r)`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] {x : X} {r : ℝ} => FunctionDistances.metric x r`

#### `localOscillation` (def)
Lean: `{𝕜 : Type u_3} → {X : Type u_4} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → Set X → C(X, 𝕜) → C(X, 𝕜) → ENNReal`
Docstring: The local oscillation of two functions w.r.t. a set `E`. This is `d_E` in the blueprint.
Definition: `fun {𝕜 : Type u_3} {X : Type u_4} [RCLike 𝕜] [PseudoMetricSpace X] (E : Set X) (f g : C(X, 𝕜)) => ⨆ z ∈ E ×ˢ E, ENNReal.ofReal ‖HAdd.hAdd (β := 𝕜) (HSub.hSub (β := 𝕜) (HSub.hSub (α := 𝕜) (β := 𝕜) (f z.1 : 𝕜) (g z.1 : 𝕜)) (f z.2 : 𝕜)) (g z.2 : 𝕜)‖`

#### `iLipENorm` (def)
Lean: `{𝕜 : Type u_3} → {X : Type u_4} → [NormedField 𝕜] → [PseudoMetricSpace X] → (X → 𝕜) → X → ℝ → ENNReal`
Docstring: The inhomogeneous Lipschitz norm on a ball.
Definition: `fun {𝕜 : Type u_3} {X : Type u_4} [NormedField 𝕜] [PseudoMetricSpace X] (φ : X → 𝕜) (x₀ : X) (R : ℝ) => (⨆ x ∈ Metric.ball x₀ R, ‖φ x‖ₑ) + ENNReal.ofReal R * ⨆ x ∈ Metric.ball x₀ R, ⨆ y ∈ Metric.ball x₀ R, ⨆ (_ : x ≠ y), ‖φ x - φ y‖ₑ / edist x y`

#### `instFunLikeΘ` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → FunLike (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) X 𝕜`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] => DFunLike.mk (β := fun (x : X) => 𝕜) (fun (f : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) => ⇑(coeΘ f)) ⋯`

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

#### `BoundedFiniteSupport` (structure or class)
Lean: `{X : Type u_3} → {E : Type u_4} → [inst : MeasurableSpace X] → [TopologicalSpace E] → [ENorm E] → [Zero E] → (X → E) → autoParam (Measure X) BoundedFiniteSupport._auto_1 → Prop`
Docstring: Bounded measurable function $g$ on $X$ supported on a set of finite measure
Constructor (every field with its type): `∀ {X : Type u_3} {E : Type u_4} [inst : MeasurableSpace X] [inst_1 : TopologicalSpace E] [inst_2 : ENorm E] [inst_3 : Zero E] {f : X → E} {μ : autoParam (Measure X) BoundedFiniteSupport._auto_1}, MemLp f ⊤ μ → LT.lt (α := ENNReal) (μ (Function.support f) : ENNReal) (⊤ : ENNReal) → BoundedFiniteSupport f μ`

#### `linearizedCarlesonOperator` (def)
Lean: `{X : Type u_2} → {A : ℕ} → [inst : PseudoMetricSpace X] → [DoublingMeasure X ↑A] → [inst_2 : FunctionDistances ℝ X] → (X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) → (X → X → ℂ) → (X → ℂ) → X → ENNReal`
Docstring: The linearized generalized Carleson operator `T_Q`, taking values in `ℝ≥0∞`. Use `ENNReal.toReal` to get the corresponding real number.
Definition: `fun {X : Type u_2} {A : ℕ} [PseudoMetricSpace X] [DoublingMeasure X ↑A] [FunctionDistances ℝ X] (Q : X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (K : X → X → ℂ) (f : X → ℂ) (x : X) => ⨆ (R₁ : ℝ), ⨆ (R₂ : ℝ), ⨆ (_ : (0 : ℝ) < R₁), ⨆ (_ : R₁ < R₂), ‖carlesonOperatorIntegrand K (Q x) R₁ R₂ f x‖ₑ`

#### `𝕔` (def)
Lean: `ℕ`
Docstring: The main constant in the blueprint, driving all the construction, is `D = 2 ^ (100 * a ^ 2)`. It turns out that the proof is robust, and works for other values of `100`, giving better constants in the end. We will formalize it using a parameter `𝕔` (that we fix equal to `100` to follow the blueprint) and having `D = 2 ^ (𝕔 * a ^ 2)`. We register two lemmas `seven_le_c` and `c_le_100` and will never unfold `𝕔` from this point on.
Definition: `wrapped✝.1`

#### `BallsCoverBalls` (def)
Lean: `(X : Type u_2) → [PseudoMetricSpace X] → ℝ → ℝ → ℕ → Prop`
Docstring: Balls of radius `r` in `X` are covered by `n` balls of radius `r'`
Definition: `fun (X : Type u_2) [PseudoMetricSpace X] (r r' : ℝ) (n : ℕ) => ∀ (x : X), CoveredByBalls (Metric.ball x r) n r'`

#### `FunctionDistances.metric` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → X → ℝ → PseudoMetricSpace (@Θ _ X inst inst_1 _)`
Docstring: For each `_x : X` and `_r : ℝ`, a `PseudoMetricSpace Θ`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.4`

#### `carlesonOperatorIntegrand` (def)
Lean: `{X : Type u_2} → {A : ℕ} → [inst : PseudoMetricSpace X] → [DoublingMeasure X ↑A] → [inst_2 : FunctionDistances ℝ X] → (X → X → ℂ) → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _ → ℝ → ℝ → (X → ℂ) → X → ℂ`
Docstring: The integrand in the (linearized) Carleson operator. This is `G` in Lemma 3.0.1.
Definition: `fun {X : Type u_2} {A : ℕ} [PseudoMetricSpace X] [DoublingMeasure X ↑A] [FunctionDistances ℝ X] (K : X → X → ℂ) (θ : @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (R₁ R₂ : ℝ) (f : X → ℂ) (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume (Set.Annulus.oo x R₁ R₂)) fun (y : X) => K x y * f y * Complex.exp (Complex.I * ↑(θ y))`

## Translations

### `two_sided_metric_carleson`
Lean (short): `[DoublingMeasure X ↑(defaultA a)] [IsTwoSidedKernel a K] [CompatibleFunctions ℝ X (defaultA a)] [IsCancellative X (defaultτ a)] (ha : 4 ≤ a) (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (hF : MeasurableSet F) (hG : MeasurableSet G) (hT : ∀ r > 0, HasBoundedStrongType (czOperator K r) 2 2 volume volume ↑(C_Ts a)) (hmf : Measurable f) (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G, carlesonOperator K f x ≤ ↑(C10_0_1 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] [inst_1 : DoublingMeasure X ↑(defaultA a)] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [IsTwoSidedKernel a K] [inst_3 : CompatibleFunctions ℝ X (defaultA a)] [IsCancellative X (defaultτ a)], (4 : ℕ) ≤ a → q ∈ Set.Ioc (1 : NNReal) (2 : NNReal) → q.HolderConjugate q' → MeasurableSet F → MeasurableSet G → (∀ r > (0 : ℝ), HasBoundedStrongType (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (czOperator K r) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → ∀ {f : X → ℂ}, Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → ∫⁻ (x : X) in G, carlesonOperator K f x ≤ ↑(C10_0_1 a q) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (↑q)⁻¹`
English: Let $X$ be a metric space and $a\in\mathbb N$, and suppose $X$ carries a doubling measure $\mu$ with doubling constant $\mathrm{defaultA}(a)$ (`DoublingMeasure X (defaultA a)`), a family $\Theta(X)$ of real-valued compatible functions with parameter $\mathrm{defaultA}(a)$ (`CompatibleFunctions ℝ X (defaultA a)`), and satisfies the cancellative property `IsCancellative X (defaultτ a)`. Let $K:X\times X\to\mathbb C$ be a two-sided Calderón–Zygmund kernel with parameter $a$ (`IsTwoSidedKernel a K`). Let $a \ge 4$, let $q,q'$ be nonnegative reals with $q \in (1, 2]$ and $q'$ its Hölder conjugate, let $F, G\subseteq X$ be measurable sets, and suppose that for every $r > 0$ the truncated Calderón–Zygmund operator $\mathrm{czOperator}(K, r)$ has bounded strong type $(2,2)$ with respect to $\mu$ with constant $C_{Ts}(a)$. If $f:X\to\mathbb C$ is measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$, then $$\int_G \mathrm{carlesonOperator}(K, f)(x)\, d\mu(x) \le C_{10.0.1}(a, q)\, \mu(G)^{1/q'}\, \mu(F)^{1/q}.$$
