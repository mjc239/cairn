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
type, introduce every symbol, and never use one letter for two things. When a definition's body is shown, say what
it defines, in words or a formula that agrees with the body.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): MeasureTheory, TileStructure, Antichain.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `C2_0_1` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant used in Proposition 2.0.1. Has value `2 ^ (442 * a ^ 3) / (q - 1) ^ 5` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => C2_0_2 a q`

#### `CP304.Q` (def)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {q q' : NNReal} → {F : Set X} → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → {f : X → ℂ} → {σ₁ σ₂ : X → ℤ} → CP304 q q' F f σ₁ σ₂ → SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)`
Docstring: `Q` is the only non-`Prop` field of `CP304`.
Definition: `fun (X : Type u_1) (a : ℕ) [MetricSpace X] (q q' : NNReal) (F : Set X) (K : X → X → ℂ) [KernelProofData a K] (f : X → ℂ) (σ₁ σ₂ : X → ℤ) (self : CP304 q q' F f σ₁ σ₂) => self.1`

#### `IsCancellative` (structure or class)
Lean: `(X : Type u_2) → {A : ℕ} → [inst : PseudoMetricSpace X] → [DoublingMeasure X ↑A] → ℝ → [CompatibleFunctions ℝ X A] → Prop`
Docstring: Θ is τ-cancellative. `τ` will usually be `1 / a`
Constructor (every field with its type): `∀ {X : Type u_2} {A : ℕ} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X ↑A] {τ : ℝ} [inst_2 : CompatibleFunctions ℝ X A], (∀ {x : X} {r : ℝ} {φ : X → ℂ}, (0 : ℝ) < r → iLipENorm φ x r ≠ ⊤ → Function.support φ ⊆ Metric.ball x r → ∀ {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => Complex.exp (Complex.I * (↑(f x) - ↑(g x))) * φ x) ≤ HMul.hMul (α := ENNReal) (β := ENNReal) (↑A : ENNReal) ((volume : Measure X) (Metric.ball x r) : ENNReal) * iLipENorm φ x r * ((1 : ENNReal) + edist_{x, r} f g) ^ (-τ)) → IsCancellative X τ`

#### `KernelProofData` (structure or class)
Lean: `{X : Type u_1} → outParam ℕ → outParam (X → X → ℂ) → [PseudoMetricSpace X] → Type (u_1 + 1)`
Docstring: Data common through most of chapters 2 through 7. These contain the minimal axioms for `kernel-summand`'s proof. This is used in Chapter 3 when we don't have all other fields from `ProofData`.
Constructor (every field with its type): `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → [inst : PseudoMetricSpace X] → (d : DoublingMeasure X ↑(defaultA a)) → (4 : ℕ) ≤ a → CompatibleFunctions ℝ X (defaultA a) → IsOneSidedKernel a K → KernelProofData a K`

#### `KernelProofData.cf` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → {inst : PseudoMetricSpace X} → [self : KernelProofData a K] → CompatibleFunctions ℝ X (defaultA a)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {K : outParam (X → X → ℂ)} {inst : PseudoMetricSpace X} [self : KernelProofData a K] => self.3`

#### `KernelProofData.d` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → {inst : PseudoMetricSpace X} → [self : KernelProofData a K] → DoublingMeasure X ↑(defaultA a)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {K : outParam (X → X → ℂ)} {inst : PseudoMetricSpace X} [self : KernelProofData a K] => self.1`

#### `MeasureTheory.DoublingMeasure.toMeasureSpace` (def)
Lean: `{X : Type u_3} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → [self : DoublingMeasure X A] → MeasureSpace X`
Definition: `fun (X : Type u_3) {A : outParam NNReal} {inst : PseudoMetricSpace X} [self : DoublingMeasure X A] => self.3`

#### `P304` (structure or class)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → NNReal → NNReal → Set X → {K : X → X → ℂ} → [KernelProofData a K] → (X → ℂ) → (X → ℤ) → (X → ℤ) → Type u_1`
Docstring: All the parameters needed to apply the recursion of Lemma 3.0.4.
Constructor (every field with its type): `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {q q' : NNReal} → {F : Set X} → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → {f : X → ℂ} → {σ₁ σ₂ : X → ℤ} → CP304 q q' F f σ₁ σ₂ → (G : Set X) → Bornology.IsBounded G → MeasurableSet G → P304 q q' F f σ₁ σ₂`

#### `P304.CP` (def)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {q q' : NNReal} → {F : Set X} → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → {f : X → ℂ} → {σ₁ σ₂ : X → ℤ} → P304 q q' F f σ₁ σ₂ → CP304 q q' F f σ₁ σ₂`
Docstring: `CP` holds all constant parameters.
Definition: `fun (X : Type u_1) (a : ℕ) [MetricSpace X] (q q' : NNReal) (F : Set X) (K : X → X → ℂ) [KernelProofData a K] (f : X → ℂ) (σ₁ σ₂ : X → ℤ) (self : P304 q q' F f σ₁ σ₂) => self.1`

#### `P304.G` (def)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {q q' : NNReal} → {F : Set X} → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → {f : X → ℂ} → {σ₁ σ₂ : X → ℤ} → P304 q q' F f σ₁ σ₂ → Set X`
Docstring: `G` is the set being recursed on.
Definition: `fun (X : Type u_1) (a : ℕ) [MetricSpace X] (q q' : NNReal) (F : Set X) (K : X → X → ℂ) [KernelProofData a K] (f : X → ℂ) (σ₁ σ₂ : X → ℤ) (self : P304 q q' F f σ₁ σ₂) => self.2`

#### `T_lin` (def)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) → (X → ℤ) → (X → ℤ) → (X → ℂ) → X → ℂ`
Docstring: The operator T_{2, σ₁, σ₂} introduced in Lemma 3.0.4.
Definition: `fun {X : Type u_1} {a : ℕ} [MetricSpace X] {K : X → X → ℂ} [KernelProofData a K] (Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)) (σ₁ σ₂ : X → ℤ) (f : X → ℂ) (x : X) => T_S Q (σ₁ x) (σ₂ x) f x`

#### `defaultA` (def)
Lean: `ℕ → ℕ`
Docstring: This is usually the value of the argument `A` in `DoublingMeasure` and `CompatibleFunctions`
Definition: `fun (a : ℕ) => (2 : ℕ) ^ a`

#### `defaultτ` (def)
Lean: `ℕ → ℝ`
Docstring: `defaultτ` is the inverse of `a`.
Definition: `fun (a : ℕ) => (↑a)⁻¹`

#### `CP304` (structure or class)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → NNReal → NNReal → Set X → {K : X → X → ℂ} → [KernelProofData a K] → (X → ℂ) → (X → ℤ) → (X → ℤ) → Type u_1`
Docstring: Convenience structure for the parameters that stay constant throughout the recursive calls to finitary Carleson in the proof of Lemma 3.0.4.
Constructor (every field with its type): `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {q q' : NNReal} → {F : Set X} → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → {f : X → ℂ} → {σ₁ σ₂ : X → ℤ} → (Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)) → (∀ (θ : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), HasBoundedStrongType (ε₁ := ℂ) (ε₂ := ENNReal) (α := X) (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (fun (x1 : X → ℂ) (x2 : X) => linearizedNontangentialOperator (⇑Q) θ K x1 x2) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → q ∈ Set.Ioc (1 : NNReal) (2 : NNReal) → q.HolderConjugate q' → Bornology.IsBounded F → MeasurableSet F → Measurable f → (fun (x : X) => ‖f x‖) ≤ F.indicator (1 : X → ℝ) → Measurable σ₁ → Measurable σ₂ → (Set.range σ₁).Finite → (Set.range σ₂).Finite → σ₁ ≤ σ₂ → CP304 q q' F f σ₁ σ₂`

#### `slice` (def)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {q q' : NNReal} → {F G : Set X} → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → {f : X → ℂ} → {σ₁ σ₂ : X → ℤ} → [IsCancellative X (defaultτ a)] → CP304 q q' F f σ₁ σ₂ → Bornology.IsBounded G → MeasurableSet G → ℕ → P304 q q' F f σ₁ σ₂`
Docstring: `slice CP bG mG n` contains `G_n` and its associated data.
Definition: `fun {X : Type u_1} {a : ℕ} [MetricSpace X] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [KernelProofData a K] {f : X → ℂ} {σ₁ σ₂ : X → ℤ} [IsCancellative X (defaultτ a)] (CP : CP304 q q' F f σ₁ σ₂) (bG : Bornology.IsBounded G) (mG : MeasurableSet G) (n : ℕ) => P304.succ (F := F)^[n] (P304.mk (F := F) CP G bG mG)`

#### `C2_0_2` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant used in Proposition 2.0.2. Has value `2 ^ (442 * a ^ 3) / (q - 1) ^ 5` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => (2 : NNReal) ^ (((3 : ℕ) * 𝕔 + (17 : ℕ) + (5 : ℕ) * (𝕔 / (4 : ℕ))) * a ^ (3 : ℕ)) / (q - (1 : NNReal)) ^ (5 : ℕ)`

#### `CompatibleFunctions.toFunctionDistances` (def)
Lean: `{𝕜 : outParam (Type u_3)} → {X : Type u} → {A : outParam ℕ} → {inst : RCLike 𝕜} → {inst_1 : PseudoMetricSpace X} → [self : CompatibleFunctions 𝕜 X A] → FunctionDistances 𝕜 X`
Definition: `fun {𝕜 : outParam (Type u_3)} (X : Type u) {A : outParam ℕ} {inst : RCLike 𝕜} {inst_1 : PseudoMetricSpace X} [self : CompatibleFunctions 𝕜 X A] => self.1`

#### `FunctionDistances.Θ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → (X : Type u) → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → Type u`
Docstring: A type of continuous functions from `X` to `𝕜`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.1`

#### `CompatibleFunctions` (structure or class)
Lean: `(𝕜 : outParam (Type u_3)) → (X : Type u) → outParam ℕ → [RCLike 𝕜] → [PseudoMetricSpace X] → Type (max (u + 1) u_3)`
Docstring: A set `Θ` of (continuous) functions is compatible. `A` will usually be `2 ^ a`.
Constructor (every field with its type): `{𝕜 : outParam (Type u_3)} → {X : Type u} → {A : outParam ℕ} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [toFunctionDistances : FunctionDistances 𝕜 X] → (∃ (o : X), ∀ (f : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), (coeΘ f) o = (0 : 𝕜)) → (∀ {x : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, localOscillation (Metric.ball x r) (coeΘ f) (coeΘ g) ≤ ENNReal.ofReal (dist_{x, r} f g)) → (∀ {x₁ x₂ : X} {r₁ r₂ : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, Metric.ball x₁ r₁ ⊆ Metric.ball x₂ r₂ → dist_{x₁, r₁} f g ≤ dist_{x₂, r₂} f g) → (∀ {x₁ x₂ : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, dist x₁ x₂ < (2 : ℝ) * r → dist_{x₂, (2 : ℝ) * r} f g ≤ ↑A * dist_{x₁, r} f g) → (∀ {x₁ x₂ : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, Metric.ball x₁ r ⊆ Metric.ball x₂ (↑A * r) → (2 : ℝ) * dist_{x₁, r} f g ≤ dist_{x₂, ↑A * r} f g) → (∀ {x : X} {r : ℝ}, AllBallsCoverBalls.{u} (WithFunctionDistance x r) (2 : ℝ) A) → CompatibleFunctions 𝕜 X A`

#### `MeasureTheory.DoublingMeasure` (structure or class)
Lean: `(X : Type u_3) → outParam NNReal → [PseudoMetricSpace X] → Type u_3`
Docstring: A metric space with a measure with some nice properties, including a doubling condition. This is called a "doubling metric measure space" in the blueprint. `A` will usually be `2 ^ a`.
Constructor (every field with its type): `{X : Type u_3} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [toCompleteSpace : CompleteSpace X] → [toLocallyCompactSpace : LocallyCompactSpace X] → [toMeasureSpace : MeasureSpace X] → [toBorelSpace : BorelSpace X] → [toIsLocallyFiniteMeasure : IsLocallyFiniteMeasure.{u_3} (α := X) (m0 := MeasureSpace.toMeasurableSpace) volume] → [toIsDoubling : Measure.IsDoubling.{u_3} (X := X) volume A] → [toNeZero : NeZero.{u_3} (R := Measure X) volume] → DoublingMeasure X A`

#### `WithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → X → ℝ → Type u_2`
Docstring: Class used to endow `Θ X` with a pseudometric space structure.
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] (x : X) (r : ℝ) => @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`

#### `iLipENorm` (def)
Lean: `{𝕜 : Type u_3} → {X : Type u_4} → [NormedField 𝕜] → [PseudoMetricSpace X] → (X → 𝕜) → X → ℝ → ENNReal`
Docstring: The inhomogeneous Lipschitz norm on a ball.
Definition: `fun {𝕜 : Type u_3} {X : Type u_4} [NormedField 𝕜] [PseudoMetricSpace X] (φ : X → 𝕜) (x₀ : X) (R : ℝ) => (⨆ x ∈ Metric.ball x₀ R, ‖φ x‖ₑ) + ENNReal.ofReal R * ⨆ x ∈ Metric.ball x₀ R, ⨆ y ∈ Metric.ball x₀ R, ⨆ (_ : x ≠ y), ‖φ x - φ y‖ₑ / edist x y`

#### `instFunLikeΘ` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → FunLike (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) X 𝕜`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] => DFunLike.mk (β := fun (x : X) => 𝕜) (fun (f : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) => ⇑(coeΘ f)) ⋯`

#### `instPseudoMetricSpaceWithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → {x : X} → {r : ℝ} → PseudoMetricSpace (WithFunctionDistance x r)`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] {x : X} {r : ℝ} => FunctionDistances.metric x r`

#### `IsOneSidedKernel` (structure or class)
Lean: `{X : Type u_1} → [PseudoMetricSpace X] → [MeasureSpace X] → outParam ℕ → (X → X → ℂ) → Prop`
Docstring: `K` is a one-sided Calderon-Zygmund kernel. In the formalization `K x y` is defined everywhere, even for `x = y`. The assumptions on `K` show that `K x x = 0`.
Constructor (every field with its type): `∀ {X : Type u_1} [inst : PseudoMetricSpace X] [inst_1 : MeasureSpace X] {a : outParam ℕ} {K : X → X → ℂ}, Measurable (Function.uncurry K) → (∀ (x y : X), ‖K x y‖ ≤ ↑(C_K ↑a) / Real.vol x y) → (∀ {x y y' : X}, (2 : ℝ) * dist y y' ≤ dist x y → ‖K x y - K x y'‖ ≤ HPow.hPow (β := ℝ) (dist y y' / dist x y) (↑a)⁻¹ * (↑(C_K ↑a) / Real.vol x y)) → IsOneSidedKernel a K`

#### `T_S` (def)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) → ℤ → ℤ → (X → ℂ) → X → ℂ`
Docstring: The operator T_{s₁, s₂} introduced in Lemma 3.0.3.
Definition: `fun {X : Type u_1} {a : ℕ} [MetricSpace X] {K : X → X → ℂ} [KernelProofData a K] (Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)) (s₁ s₂ : ℤ) (f : X → ℂ) (x : X) => ∑ s ∈ Finset.Icc s₁ s₂, @integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => Ks s x y * f y * Complex.exp (Complex.I * ↑((Q x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y))`

#### `C_Ts` (def)
Lean: `ℕ → NNReal`
Docstring: A constant used on the boundedness of `T_Q^θ` and `T_*`. We generally assume `HasBoundedStrongType (linearizedNontangentialOperator Q θ K · ·) 2 2 volume volume (C_Ts a)` throughout this formalization.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ a ^ (3 : ℕ)`

#### `MeasureTheory.HasBoundedStrongType` (def)
Lean: `{ε₁ : Type u_3} → {ε₂ : Type u_4} → [ENorm ε₁] → [ENorm ε₂] → [TopologicalSpace ε₁] → [TopologicalSpace ε₂] → [Zero ε₁] → {α : Type u_5} → {α' : Type u_6} → {_x : MeasurableSpace α} → {_x' : MeasurableSpace α'} → ((α → ε₁) → α' → ε₂) → ENNReal → ENNReal → Measure α → Measure α' → ENNReal → Prop`
Docstring: A weaker version of `HasStrongType`. This is the same as `HasStrongType` if `T` is continuous w.r.t. the L^2 norm, but weaker in general.
Definition: `fun {ε₁ : Type u_3} {ε₂ : Type u_4} [ENorm ε₁] [ENorm ε₂] [TopologicalSpace ε₁] [TopologicalSpace ε₂] [Zero ε₁] {α : Type u_5} {α' : Type u_6} {_x : MeasurableSpace α} {_x' : MeasurableSpace α'} (T : (α → ε₁) → α' → ε₂) (p p' : ENNReal) (μ : Measure α) (ν : Measure α') (c : ENNReal) => ∀ (f : α → ε₁), BoundedFiniteSupport f μ → AEStronglyMeasurable (T f) ν ∧ eLpNorm (T f) p' ν ≤ c * eLpNorm f p μ`

#### `linearizedNontangentialOperator` (def)
Lean: `{X : Type u_2} → {A : ℕ} → [inst : PseudoMetricSpace X] → [DoublingMeasure X ↑A] → [inst_2 : FunctionDistances ℝ X] → (X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _ → (X → X → ℂ) → (X → ℂ) → X → ENNReal`
Docstring: The linearized maximally truncated nontangential Calderon–Zygmund operator `T_Q^θ`.
Definition: `fun {X : Type u_2} {A : ℕ} [PseudoMetricSpace X] [DoublingMeasure X ↑A] [FunctionDistances ℝ X] (Q : X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (θ : @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (K : X → X → ℂ) (f : X → ℂ) (x : X) => ⨆ (R₂ : ℝ), ⨆ R₁ ∈ Set.Ioo (0 : ℝ) R₂, ⨆ x' ∈ Metric.ball x R₁, enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume (Set.EAnnulus.oo x' (ENNReal.ofReal R₁) (min (ENNReal.ofReal R₂) (upperRadius Q θ x')))) fun (y : X) => K x' y * f y)`

#### `𝕔` (def)
Lean: `ℕ`
Docstring: The main constant in the blueprint, driving all the construction, is `D = 2 ^ (100 * a ^ 2)`. It turns out that the proof is robust, and works for other values of `100`, giving better constants in the end. We will formalize it using a parameter `𝕔` (that we fix equal to `100` to follow the blueprint) and having `D = 2 ^ (𝕔 * a ^ 2)`. We register two lemmas `seven_le_c` and `c_le_100` and will never unfold `𝕔` from this point on.
Definition: `wrapped✝.1`

#### `FunctionDistances` (structure or class)
Lean: `(𝕜 : outParam (Type u_1)) → (X : Type u) → [NormedField 𝕜] → [TopologicalSpace X] → Type (max (u + 1) u_1)`
Docstring: A class stating that continuous functions have distances associated to every ball. We use a separate type to conveniently index these functions.
Constructor (every field with its type): `{𝕜 : outParam (Type u_1)} → {X : Type u} → [inst : NormedField 𝕜] → [inst_1 : TopologicalSpace X] → (Θ : Type u) → (coeΘ : Θ → C(X, 𝕜)) → (∀ {f g : Θ}, (∀ (x : X), Eq.{u_1 + 1} (α := 𝕜) ((coeΘ f) x : 𝕜) ((coeΘ g) x : 𝕜)) → f = g) → (X → ℝ → PseudoMetricSpace Θ) → FunctionDistances 𝕜 X`

#### `AllBallsCoverBalls` (def)
Lean: `(X : Type u_2) → [PseudoMetricSpace X] → ℝ → ℕ → Prop`
Docstring: For all `r`, balls of radius `r` in `X` are covered by `n` balls of radius `a * r`
Definition: `fun (X : Type u_2) [PseudoMetricSpace X] (a : ℝ) (n : ℕ) => ∀ (r : ℝ), BallsCoverBalls X (a * r) r n`

#### `FunctionDistances.coeΘ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → @Θ _ X inst inst_1 _ → C(X, 𝕜)`
Docstring: The coercion map from `Θ` to `C(X, 𝕜)`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.2`

#### `localOscillation` (def)
Lean: `{𝕜 : Type u_3} → {X : Type u_4} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → Set X → C(X, 𝕜) → C(X, 𝕜) → ENNReal`
Docstring: The local oscillation of two functions w.r.t. a set `E`. This is `d_E` in the blueprint.
Definition: `fun {𝕜 : Type u_3} {X : Type u_4} [RCLike 𝕜] [PseudoMetricSpace X] (E : Set X) (f g : C(X, 𝕜)) => ⨆ z ∈ E ×ˢ E, ENNReal.ofReal ‖HAdd.hAdd (β := 𝕜) (HSub.hSub (β := 𝕜) (HSub.hSub (α := 𝕜) (β := 𝕜) (f z.1 : 𝕜) (g z.1 : 𝕜)) (f z.2 : 𝕜)) (g z.2 : 𝕜)‖`

#### `MeasureTheory.Measure.IsDoubling` (structure or class)
Lean: `{X : Type u_3} → [inst : MeasurableSpace X] → [PseudoMetricSpace X] → Measure X → outParam NNReal → Prop`
Docstring: A doubling measure is a measure on a metric space with the condition that doubling the radius of a ball only increases the volume by a constant factor, independent of the ball.
Constructor (every field with its type): `∀ {X : Type u_3} [inst : MeasurableSpace X] [inst_1 : PseudoMetricSpace X] {μ : Measure X} {A : outParam NNReal}, (∀ (x : X) (r : ℝ), μ (Metric.ball x ((2 : ℝ) * r)) ≤ HMul.hMul (β := ENNReal) ↑A (μ (Metric.ball x r) : ENNReal)) → μ.IsDoubling A`

#### `FunctionDistances.metric` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → X → ℝ → PseudoMetricSpace (@Θ _ X inst inst_1 _)`
Docstring: For each `_x : X` and `_r : ℝ`, a `PseudoMetricSpace Θ`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.4`

#### `C_K` (def)
Lean: `ℝ → NNReal`
Docstring: The constant used twice in the definition of the Calderon-Zygmund kernel.
Definition: `fun (a : ℝ) => (2 : NNReal) ^ a ^ (3 : ℕ)`

#### `Real.vol` (def)
Lean: `{X : Type u_1} → [PseudoMetricSpace X] → [MeasureSpace X] → X → X → ℝ`
Docstring: The "volume function" `V`. Preferably use `vol` instead.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] [MeasureSpace X] (x y : X) => Measure.real (m := MeasureSpace.toMeasurableSpace) volume (Metric.ball x (dist x y))`

#### `Ks` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {K : X → X → ℂ} → [inst : PseudoMetricSpace X] → [KernelProofData a K] → ℤ → X → X → ℂ`
Docstring: K_s in the blueprint
Definition: `fun {X : Type u_1} {a : ℕ} {K : X → X → ℂ} [PseudoMetricSpace X] [KernelProofData a K] (s : ℤ) (x y : X) => K x y * ↑(ψ (defaultD a) (HPow.hPow (α := ℝ) (↑(defaultD a)) (-s) * dist x y))`

#### `partialFourierSum` (def)
Lean: `ℕ → (ℝ → ℂ) → ℝ → ℂ`
Docstring: The Nᵗʰ partial Fourier sum of `f : ℝ → ℂ` for `N : ℕ`.
Definition: `fun (N : ℕ) (f : ℝ → ℂ) (x : ℝ) => ∑ n ∈ Finset.Icc (-↑N) ↑N, HMul.hMul (β := ℂ) (fourierCoeffOn Real.two_pi_pos f n) ((fourier n) ↑x : ℂ)`

#### `BoundedFiniteSupport` (structure or class)
Lean: `{X : Type u_3} → {E : Type u_4} → [inst : MeasurableSpace X] → [TopologicalSpace E] → [ENorm E] → [Zero E] → (X → E) → autoParam (Measure X) BoundedFiniteSupport._auto_1 → Prop`
Docstring: Bounded measurable function $g$ on $X$ supported on a set of finite measure
Constructor (every field with its type): `∀ {X : Type u_3} {E : Type u_4} [inst : MeasurableSpace X] [inst_1 : TopologicalSpace E] [inst_2 : ENorm E] [inst_3 : Zero E] {f : X → E} {μ : autoParam (Measure X) BoundedFiniteSupport._auto_1}, MemLp f ⊤ μ → LT.lt (α := ENNReal) (μ (Function.support f) : ENNReal) (⊤ : ENNReal) → BoundedFiniteSupport f μ`

#### `Set.EAnnulus.oo` (def)
Lean: `{X : Type u_1} → [PseudoMetricSpace X] → X → ENNReal → ENNReal → Set X`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] (x : X) (r R : ENNReal) => {y : X | edist x y ∈ Set.Ioo r R}`

#### `upperRadius` (def)
Lean: `{X : Type u_2} → [inst : PseudoMetricSpace X] → [inst_1 : FunctionDistances ℝ X] → (X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _ → X → ENNReal`
Docstring: `R_Q(θ, x)` defined in (1.1.17).
Definition: `fun {X : Type u_2} [PseudoMetricSpace X] [FunctionDistances ℝ X] (Q : X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (θ : @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (x : X) => ⨆ (r : ℝ), ⨆ (_ : dist_{x, r} θ (Q x) < (1 : ℝ)), ENNReal.ofReal r`

## Flagged translations

### `P304.succ`
Lean (short): `[KernelProofData a K] [IsCancellative X (defaultτ a)] (P : P304 q q' F f σ₁ σ₂) : P304 q q' F f σ₁ σ₂`
Lean (full): `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {q q' : NNReal} → {F : Set X} → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → {f : X → ℂ} → {σ₁ σ₂ : X → ℤ} → [IsCancellative X (defaultτ a)] → P304 q q' F f σ₁ σ₂ → P304 q q' F f σ₁ σ₂`
Definition: `fun {X : Type u_1} {a : ℕ} [MetricSpace X] {q q' : NNReal} {F : Set X} {K : X → X → ℂ} [KernelProofData a K] {f : X → ℂ} {σ₁ σ₂ : X → ℤ} [IsCancellative X (defaultτ a)] (P : P304 q q' F f σ₁ σ₂) => P304.mk (F := F) (P.CP (F := F)) (⋯.choose (p := fun (G' : Set X) => G' ⊆ P.G (F := F) ∧ Bornology.IsBounded G' ∧ MeasurableSet G' ∧ HMul.hMul (β := ENNReal) (2 : ENNReal) ((volume : Measure X) G' : ENNReal) ≤ (volume : Measure X) (P.G (F := F)) ∧ ∫⁻ (x : X) in P.G (F := F) \ G', ‖T_lin (P.CP (F := F).Q (F := F)) σ₁ σ₂ f x‖ₑ ≤ ↑(C2_0_1 a q) * HPow.hPow (α := ENNReal) ((volume : Measure X) (P.G (F := F)) : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (↑q)⁻¹)) ⋯ ⋯`
Docstring: Construct `G_{n+1}` given `G_n`.
Previous English: Let $X$ be a metric space, $a \in \mathbb{N}$, and $K : X \times X \to \mathbb{C}$ a kernel satisfying `KernelProofData a K`, and assume $X$ satisfies the cancellativity condition `IsCancellative X (defaultτ a)`. Let $q, q'$ be nonnegative reals, $F \subseteq X$, $f : X \to \mathbb{C}$ and $\sigma_1, \sigma_2 : X \to \mathbb{Z}$. Given data $P$ of type $\mathrm{P304}(q,q',F,f,\sigma_1,\sigma_2)$, `P304.succ P` is again data of type $\mathrm{P304}(q,q',F,f,\sigma_1,\sigma_2)$; according to its docstring, it constructs $G_{n+1}$ given $G_n$.
Checker's issue: Definition body is shown but the English only paraphrases the docstring ('constructs G_{n+1} given G_n'). It must say what the definition builds: the P304 with the same CP304 data and with G replaced by a chosen G' ⊆ P.G that is bounded and measurable, with 2·μ(G') ≤ μ(P.G) and ∫⁻ over P.G \ G' of ‖T_lin CP.Q σ₁ σ₂ f‖ₑ ≤ C2_0_1 a q · μ(P.G)^{1/q'} · μ(F)^{1/q}. P304 is also left unexplained (CP304 data together with a bounded measurable set G).

### `volume_slice`
Lean (short): `[KernelProofData a K] [IsCancellative X (defaultτ a)] : 2 * volume (slice CP bG mG (n + 1)).G ≤ volume (slice CP bG mG n).G`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [inst_1 : KernelProofData a K] {f : X → ℂ} {σ₁ σ₂ : X → ℤ} [inst_2 : IsCancellative X (defaultτ a)] {CP : CP304 q q' F f σ₁ σ₂} {bG : Bornology.IsBounded G} {mG : MeasurableSet G} {n : ℕ}, HMul.hMul (β := ENNReal) (2 : ENNReal) ((volume : Measure X) ((slice (F := F) (G := G) CP bG mG (n + (1 : ℕ))).G (F := F)) : ENNReal) ≤ (volume : Measure X) ((slice (F := F) (G := G) CP bG mG n).G (F := F))`
Previous English: Let $X$ be a metric space, $a\in\mathbb N$, and $K : X\times X\to\mathbb C$ a kernel satisfying the standing assumptions `KernelProofData a K` (so $X$ carries a doubling measure $\mu$ with parameter depending on $a$ and $K$ satisfies the kernel bounds), and assume the cancellative property `IsCancellative X (defaultτ a)` holds (with the default exponent $\tau=\mathrm{defaultτ}(a)$). Let $q,q'\ge 0$ be nonnegative reals, $F,G\subseteq X$, $f:X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$, let $CP$ be data of type $\mathrm{CP304}(q,q',F,f,\sigma_1,\sigma_2)$ (with associated simple function $Q_{CP}$), and let $G$ be bounded (witness $bG$) and measurable (witness $mG$); write $G_n$ for the set $(\mathrm{slice}\,CP\,bG\,mG\,n).G$ of the $n$-th slice ($n\in\mathbb N$). Then $2\mu(G_{n+1})\le\mu(G_n)$.
Checker's issue: The project notion `slice` (and P304/P304.succ) is introduced only as the Lean expression '(slice CP bG mG n).G' with no description. The English never says that G_0 = G and that G_{n+1} is the chosen subset of G_n given by P304.succ, so the claimed relation between G_n and G_{n+1} has no mathematical content for a reader. Compare slice_integral_bound, which does describe it. CP304 is also named without its docstring or contents.

### `slice_G_subset`
Lean (short): `[KernelProofData a K] [IsCancellative X (defaultτ a)] : (slice CP bG mG (n + 1)).G ⊆ (slice CP bG mG n).G`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [inst_1 : KernelProofData a K] {f : X → ℂ} {σ₁ σ₂ : X → ℤ} [inst_2 : IsCancellative X (defaultτ a)] {CP : CP304 q q' F f σ₁ σ₂} {bG : Bornology.IsBounded G} {mG : MeasurableSet G} {n : ℕ}, (slice (F := F) (G := G) CP bG mG (n + (1 : ℕ))).G (F := F) ⊆ (slice (F := F) (G := G) CP bG mG n).G (F := F)`
Previous English: Let $X$ be a metric space, $a\in\mathbb N$, and $K : X\times X\to\mathbb C$ a kernel satisfying the standing assumptions `KernelProofData a K` (so $X$ carries a doubling measure $\mu$ with parameter depending on $a$ and $K$ satisfies the kernel bounds), and assume the cancellative property `IsCancellative X (defaultτ a)` holds (with the default exponent $\tau=\mathrm{defaultτ}(a)$). Let $q,q'\ge 0$ be nonnegative reals, $F,G\subseteq X$, $f:X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$, let $CP$ be data of type $\mathrm{CP304}(q,q',F,f,\sigma_1,\sigma_2)$ (with associated simple function $Q_{CP}$), and let $G$ be bounded (witness $bG$) and measurable (witness $mG$); write $G_n$ for the set $(\mathrm{slice}\,CP\,bG\,mG\,n).G$ of the $n$-th slice ($n\in\mathbb N$). Then $G_{n+1}\subseteq G_n$.
Checker's issue: The project notion `slice` (and P304/P304.succ) is introduced only as the Lean expression '(slice CP bG mG n).G' with no description. The English never says that G_0 = G and that G_{n+1} is the chosen subset of G_n given by P304.succ, so the claimed relation between G_n and G_{n+1} has no mathematical content for a reader. Compare slice_integral_bound, which does describe it. CP304 is also named without its docstring or contents.
