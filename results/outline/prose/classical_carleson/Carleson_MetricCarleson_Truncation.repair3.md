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

#### `C1_0_2` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant used in `MetricSpaceCarleson` and `LinearizedMetricCarleson`. Has value `2 ^ (443 * a ^ 3) / (q - 1) ^ 6` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => (2 : NNReal) ^ (((3 : ℕ) * 𝕔 + (18 : ℕ) + (5 : ℕ) * (𝕔 / (4 : ℕ))) * a ^ (3 : ℕ)) / (q - (1 : NNReal)) ^ (6 : ℕ)`

#### `C_Ts` (def)
Lean: `ℕ → NNReal`
Docstring: A constant used on the boundedness of `T_Q^θ` and `T_*`. We generally assume `HasBoundedStrongType (linearizedNontangentialOperator Q θ K · ·) 2 2 volume volume (C_Ts a)` throughout this formalization.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ a ^ (3 : ℕ)`

#### `CompatibleFunctions.toFunctionDistances` (def)
Lean: `{𝕜 : outParam (Type u_3)} → {X : Type u} → {A : outParam ℕ} → {inst : RCLike 𝕜} → {inst_1 : PseudoMetricSpace X} → [self : CompatibleFunctions 𝕜 X A] → FunctionDistances 𝕜 X`
Definition: `fun {𝕜 : outParam (Type u_3)} (X : Type u) {A : outParam ℕ} {inst : RCLike 𝕜} {inst_1 : PseudoMetricSpace X} [self : CompatibleFunctions 𝕜 X A] => self.1`

#### `FunctionDistances.Θ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → (X : Type u) → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → Type u`
Docstring: A type of continuous functions from `X` to `𝕜`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.1`

#### `IsCancellative` (structure or class)
Lean: `(X : Type u_2) → {A : ℕ} → [inst : PseudoMetricSpace X] → [DoublingMeasure X ↑A] → ℝ → [CompatibleFunctions ℝ X A] → Prop`
Docstring: Θ is τ-cancellative. `τ` will usually be `1 / a`
Fields: `0`, `E`, `x`, `α`, `β`, `↑A`, `MeasureTheory.volume`, `1`

#### `KernelProofData` (structure or class)
Lean: `{X : Type u_1} → outParam ℕ → outParam (X → X → ℂ) → [PseudoMetricSpace X] → Type (u_1 + 1)`
Docstring: Data common through most of chapters 2 through 7. These contain the minimal axioms for `kernel-summand`'s proof. This is used in Chapter 3 when we don't have all other fields from `ProofData`.
Fields: `d`, `4`

#### `KernelProofData.cf` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → {inst : PseudoMetricSpace X} → [self : KernelProofData a K] → CompatibleFunctions ℝ X (defaultA a)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {K : outParam (X → X → ℂ)} {inst : PseudoMetricSpace X} [self : KernelProofData a K] => self.3`

#### `KernelProofData.d` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → {inst : PseudoMetricSpace X} → [self : KernelProofData a K] → DoublingMeasure X ↑(defaultA a)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {K : outParam (X → X → ℂ)} {inst : PseudoMetricSpace X} [self : KernelProofData a K] => self.1`

#### `MeasureTheory.DoublingMeasure.toMeasureSpace` (def)
Lean: `{X : Type u_3} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → [self : DoublingMeasure X A] → MeasureSpace X`
Definition: `fun (X : Type u_3) {A : outParam NNReal} {inst : PseudoMetricSpace X} [self : DoublingMeasure X A] => self.3`

#### `MeasureTheory.HasBoundedStrongType` (def)
Lean: `{ε₁ : Type u_3} → {ε₂ : Type u_4} → [ENorm ε₁] → [ENorm ε₂] → [TopologicalSpace ε₁] → [TopologicalSpace ε₂] → [Zero ε₁] → {α : Type u_5} → {α' : Type u_6} → {_x : MeasurableSpace α} → {_x' : MeasurableSpace α'} → ((α → ε₁) → α' → ε₂) → ENNReal → ENNReal → Measure α → Measure α' → ENNReal → Prop`
Docstring: A weaker version of `HasStrongType`. This is the same as `HasStrongType` if `T` is continuous w.r.t. the L^2 norm, but weaker in general.
Definition: `fun {ε₁ : Type u_3} {ε₂ : Type u_4} [ENorm ε₁] [ENorm ε₂] [TopologicalSpace ε₁] [TopologicalSpace ε₂] [Zero ε₁] {α : Type u_5} {α' : Type u_6} {_x : MeasurableSpace α} {_x' : MeasurableSpace α'} (T : (α → ε₁) → α' → ε₂) (p p' : ENNReal) (μ : Measure α) (ν : Measure α') (c : ENNReal) => ∀ (f : α → ε₁), BoundedFiniteSupport f μ → AEStronglyMeasurable (T f) ν ∧ eLpNorm (T f) p' ν ≤ c * eLpNorm f p μ`

#### `T_R` (def)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → (X → X → ℂ) → SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) → ℝ → ℝ → ℝ → (X → ℂ) → X → ℂ`
Docstring: The operator T_{R₁, R₂, R} introduced in Lemma 3.0.2.
Definition: `fun {X : Type u_1} {a : ℕ} [MetricSpace X] {K : X → X → ℂ} [KernelProofData a K] (K_1 : X → X → ℂ) (Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)) (R₁ R₂ R : ℝ) (f : X → ℂ) (x : X) => (Metric.ball (cancelPt X) R).indicator (fun (x : X) => carlesonOperatorIntegrand K_1 (Q x) R₁ R₂ f x) x`

#### `defaultA` (def)
Lean: `ℕ → ℕ`
Docstring: This is usually the value of the argument `A` in `DoublingMeasure` and `CompatibleFunctions`
Definition: `fun (a : ℕ) => (2 : ℕ) ^ a`

#### `defaultτ` (def)
Lean: `ℕ → ℝ`
Docstring: `defaultτ` is the inverse of `a`.
Definition: `fun (a : ℕ) => (↑a)⁻¹`

#### `linearizedNontangentialOperator` (def)
Lean: `{X : Type u_2} → {A : ℕ} → [inst : PseudoMetricSpace X] → [DoublingMeasure X ↑A] → [inst_2 : FunctionDistances ℝ X] → (X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _ → (X → X → ℂ) → (X → ℂ) → X → ENNReal`
Docstring: The linearized maximally truncated nontangential Calderon–Zygmund operator `T_Q^θ`.
Definition: `fun {X : Type u_2} {A : ℕ} [PseudoMetricSpace X] [DoublingMeasure X ↑A] [FunctionDistances ℝ X] (Q : X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (θ : @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (K : X → X → ℂ) (f : X → ℂ) (x : X) => ⨆ (R₂ : ℝ), ⨆ R₁ ∈ Set.Ioo (0 : ℝ) R₂, ⨆ x' ∈ Metric.ball x R₁, enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume (Set.EAnnulus.oo x' (ENNReal.ofReal R₁) (min (ENNReal.ofReal R₂) (upperRadius Q θ x')))) fun (y : X) => K x' y * f y)`

#### `cancelPt` (def)
Lean: `{𝕜 : Type u_1} → (X : Type u_2) → {A : ℕ} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [CompatibleFunctions 𝕜 X A] → X`
Docstring: The point `o` in the blueprint
Definition: `fun {𝕜 : Type u_1} (X : Type u_2) {A : ℕ} [RCLike 𝕜] [PseudoMetricSpace X] [CompatibleFunctions 𝕜 X A] => Exists.choose (p := fun (o : X) => ∀ (f : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), (coeΘ f) o = (0 : 𝕜)) ⋯`

#### `C2_0_1` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant used in Proposition 2.0.1. Has value `2 ^ (442 * a ^ 3) / (q - 1) ^ 5` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => C2_0_2 a q`

#### `CP304` (structure or class)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → NNReal → NNReal → Set X → {K : X → X → ℂ} → [KernelProofData a K] → (X → ℂ) → (X → ℤ) → (X → ℤ) → Type u_1`
Docstring: Convenience structure for the parameters that stay constant throughout the recursive calls to finitary Carleson in the proof of Lemma 3.0.4.
Fields: `Q`, `θ`, `ε₁`, `ε₂`, `α`, `_x`, `_x'`, `x1`, `x2`, `2`, `1`, `x`

#### `CP304.Q` (def)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {q q' : NNReal} → {F : Set X} → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → {f : X → ℂ} → {σ₁ σ₂ : X → ℤ} → CP304 q q' F f σ₁ σ₂ → SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)`
Docstring: `Q` is the only non-`Prop` field of `CP304`.
Definition: `fun (X : Type u_1) (a : ℕ) [MetricSpace X] (q q' : NNReal) (F : Set X) (K : X → X → ℂ) [KernelProofData a K] (f : X → ℂ) (σ₁ σ₂ : X → ℤ) (self : CP304 q q' F f σ₁ σ₂) => self.1`

#### `T_lin` (def)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) → (X → ℤ) → (X → ℤ) → (X → ℂ) → X → ℂ`
Docstring: The operator T_{2, σ₁, σ₂} introduced in Lemma 3.0.4.
Definition: `fun {X : Type u_1} {a : ℕ} [MetricSpace X] {K : X → X → ℂ} [KernelProofData a K] (Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)) (σ₁ σ₂ : X → ℤ) (f : X → ℂ) (x : X) => T_S Q (σ₁ x) (σ₂ x) f x`

#### `C2_1_3` (def)
Lean: `ℕ → NNReal`
Docstring: The constant appearing in part 2 of Lemma 2.1.3. Equal to `2 ^ (102 * a ^ 3)` in the blueprint.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ ((𝕔 + (2 : ℕ)) * a ^ (3 : ℕ))`

#### `L302` (def)
Lean: `ℕ → ℝ → ℤ`
Docstring: The largest integer `s₁` satisfying `D ^ (-(s₁ - 2)) * R₁ > 1 / 2`.
Definition: `fun (a : ℕ) (R₁ : ℝ) => ⌊Real.logb (↑(defaultD a)) ((2 : ℝ) * R₁)⌋ + (3 : ℤ)`

#### `T_S` (def)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) → ℤ → ℤ → (X → ℂ) → X → ℂ`
Docstring: The operator T_{s₁, s₂} introduced in Lemma 3.0.3.
Definition: `fun {X : Type u_1} {a : ℕ} [MetricSpace X] {K : X → X → ℂ} [KernelProofData a K] (Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)) (s₁ s₂ : ℤ) (f : X → ℂ) (x : X) => ∑ s ∈ Finset.Icc s₁ s₂, @integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => Ks s x y * f y * Complex.exp (Complex.I * ↑((Q x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y))`

#### `U302` (def)
Lean: `ℕ → ℝ → ℤ`
Docstring: The smallest integer `s₂` satisfying `D ^ (-(s₂ + 2)) * R₂ < 1 / (4 * D)`.
Definition: `fun (a : ℕ) (R₂ : ℝ) => ⌈Real.logb (↑(defaultD a)) ((4 : ℝ) * R₂)⌉ - (2 : ℤ)`

#### `carlesonOperatorIntegrand` (def)
Lean: `{X : Type u_2} → {A : ℕ} → [inst : PseudoMetricSpace X] → [DoublingMeasure X ↑A] → [inst_2 : FunctionDistances ℝ X] → (X → X → ℂ) → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _ → ℝ → ℝ → (X → ℂ) → X → ℂ`
Docstring: The integrand in the (linearized) Carleson operator. This is `G` in Lemma 3.0.1.
Definition: `fun {X : Type u_2} {A : ℕ} [PseudoMetricSpace X] [DoublingMeasure X ↑A] [FunctionDistances ℝ X] (K : X → X → ℂ) (θ : @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (R₁ R₂ : ℝ) (f : X → ℂ) (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume (Set.Annulus.oo x R₁ R₂)) fun (y : X) => K x y * f y * Complex.exp (Complex.I * ↑(θ y))`

#### `globalMaximalFunction` (def)
Lean: `{X : Type u_1} → {ε : Type u_2} → [PseudoMetricSpace X] → [inst : MeasurableSpace X] → [ENorm ε] → Measure X → ℝ → (X → ε) → X → ENNReal`
Docstring: The uncentered Hardy-Littlewood maximal function.
Definition: `fun {X : Type u_1} {ε : Type u_2} [PseudoMetricSpace X] [MeasurableSpace X] [ENorm ε] (μ : Measure X) (p : ℝ) (u : X → ε) (x : X) => maximalFunction μ Set.univ (fun (x : X × ℝ) => x.1) (fun (x : X × ℝ) => x.2) p u x`

#### `C3_0_4` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant used in `linearized_truncation` and `S_truncation`. Has value `2 ^ (442 * a ^ 3 + 2)` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => (2 : NNReal) ^ (((3 : ℕ) * 𝕔 + (17 : ℕ) + (5 : ℕ) * (𝕔 / (4 : ℕ))) * a ^ (3 : ℕ) + (2 : ℕ)) / (q - (1 : NNReal)) ^ (6 : ℕ)`

#### `P304.G` (def)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {q q' : NNReal} → {F : Set X} → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → {f : X → ℂ} → {σ₁ σ₂ : X → ℤ} → P304 q q' F f σ₁ σ₂ → Set X`
Docstring: `G` is the set being recursed on.
Definition: `fun (X : Type u_1) (a : ℕ) [MetricSpace X] (q q' : NNReal) (F : Set X) (K : X → X → ℂ) [KernelProofData a K] (f : X → ℂ) (σ₁ σ₂ : X → ℤ) (self : P304 q q' F f σ₁ σ₂) => self.2`

#### `slice` (def)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {q q' : NNReal} → {F G : Set X} → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → {f : X → ℂ} → {σ₁ σ₂ : X → ℤ} → [IsCancellative X (defaultτ a)] → CP304 q q' F f σ₁ σ₂ → Bornology.IsBounded G → MeasurableSet G → ℕ → P304 q q' F f σ₁ σ₂`
Docstring: `slice CP bG mG n` contains `G_n` and its associated data.
Definition: `fun {X : Type u_1} {a : ℕ} [MetricSpace X] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [KernelProofData a K] {f : X → ℂ} {σ₁ σ₂ : X → ℤ} [IsCancellative X (defaultτ a)] (CP : CP304 q q' F f σ₁ σ₂) (bG : Bornology.IsBounded G) (mG : MeasurableSet G) (n : ℕ) => P304.succ (F := F)^[n] (P304.mk (F := F) CP G bG mG)`

#### `partialFourierSum` (def)
Lean: `ℕ → (ℝ → ℂ) → ℝ → ℂ`
Docstring: The Nᵗʰ partial Fourier sum of `f : ℝ → ℂ` for `N : ℕ`.
Definition: `fun (N : ℕ) (f : ℝ → ℂ) (x : ℝ) => ∑ n ∈ Finset.Icc (-↑N) ↑N, HMul.hMul (β := ℂ) (fourierCoeffOn Real.two_pi_pos f n) ((fourier n) ↑x : ℂ)`

#### `𝕔` (def)
Lean: `ℕ`
Docstring: The main constant in the blueprint, driving all the construction, is `D = 2 ^ (100 * a ^ 2)`. It turns out that the proof is robust, and works for other values of `100`, giving better constants in the end. We will formalize it using a parameter `𝕔` (that we fix equal to `100` to follow the blueprint) and having `D = 2 ^ (𝕔 * a ^ 2)`. We register two lemmas `seven_le_c` and `c_le_100` and will never unfold `𝕔` from this point on.
Definition: `wrapped✝.1`

#### `CompatibleFunctions` (structure or class)
Lean: `(𝕜 : outParam (Type u_3)) → (X : Type u) → outParam ℕ → [RCLike 𝕜] → [PseudoMetricSpace X] → Type (max (u + 1) u_3)`
Docstring: A set `Θ` of (continuous) functions is compatible. `A` will usually be `2 ^ a`.
Fields: `o`, `f`, `0`, `2`

#### `FunctionDistances` (structure or class)
Lean: `(𝕜 : outParam (Type u_1)) → (X : Type u) → [NormedField 𝕜] → [TopologicalSpace X] → Type (max (u + 1) u_1)`
Docstring: A class stating that continuous functions have distances associated to every ball. We use a separate type to conveniently index these functions.
Fields: `Θ`, `coeΘ`, `x`, `α`

#### `MeasureTheory.DoublingMeasure` (structure or class)
Lean: `(X : Type u_3) → outParam NNReal → [PseudoMetricSpace X] → Type u_3`
Docstring: A metric space with a measure with some nice properties, including a doubling condition. This is called a "doubling metric measure space" in the blueprint. `A` will usually be `2 ^ a`.
Fields: `α`, `m0`, `X`, `R`

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
Fields: `2`, `β`

#### `BoundedFiniteSupport` (structure or class)
Lean: `{X : Type u_3} → {E : Type u_4} → [inst : MeasurableSpace X] → [TopologicalSpace E] → [ENorm E] → [Zero E] → (X → E) → autoParam (Measure X) BoundedFiniteSupport._auto_1 → Prop`
Docstring: Bounded measurable function $g$ on $X$ supported on a set of finite measure
Fields: `α`, `⊤`

#### `Set.EAnnulus.oo` (def)
Lean: `{X : Type u_1} → [PseudoMetricSpace X] → X → ENNReal → ENNReal → Set X`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] (x : X) (r R : ENNReal) => {y : X | edist x y ∈ Set.Ioo r R}`

#### `upperRadius` (def)
Lean: `{X : Type u_2} → [inst : PseudoMetricSpace X] → [inst_1 : FunctionDistances ℝ X] → (X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _ → X → ENNReal`
Docstring: `R_Q(θ, x)` defined in (1.1.17).
Definition: `fun {X : Type u_2} [PseudoMetricSpace X] [FunctionDistances ℝ X] (Q : X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (θ : @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (x : X) => ⨆ (r : ℝ), ⨆ (_ : dist_{x, r} θ (Q x) < (1 : ℝ)), ENNReal.ofReal r`

#### `FunctionDistances.coeΘ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → @Θ _ X inst inst_1 _ → C(X, 𝕜)`
Docstring: The coercion map from `Θ` to `C(X, 𝕜)`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.2`

#### `C2_0_2` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant used in Proposition 2.0.2. Has value `2 ^ (442 * a ^ 3) / (q - 1) ^ 5` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => (2 : NNReal) ^ (((3 : ℕ) * 𝕔 + (17 : ℕ) + (5 : ℕ) * (𝕔 / (4 : ℕ))) * a ^ (3 : ℕ)) / (q - (1 : NNReal)) ^ (5 : ℕ)`

#### `ψ` (def)
Lean: `ℕ → ℝ → ℝ`
Docstring: The function `ψ` used as a basis for a dyadic partition of unity.
Definition: `fun (D : ℕ) (x : ℝ) => max (0 : ℝ) (min (1 : ℝ) (min ((4 : ℝ) * ↑D * x - (1 : ℝ)) ((2 : ℝ) - (4 : ℝ) * x)))`

#### `P304.succ` (def)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → {q q' : NNReal} → {F : Set X} → {K : X → X → ℂ} → [inst_1 : KernelProofData a K] → {f : X → ℂ} → {σ₁ σ₂ : X → ℤ} → [IsCancellative X (defaultτ a)] → P304 q q' F f σ₁ σ₂ → P304 q q' F f σ₁ σ₂`
Docstring: Construct `G_{n+1}` given `G_n`.
Definition: `fun {X : Type u_1} {a : ℕ} [MetricSpace X] {q q' : NNReal} {F : Set X} {K : X → X → ℂ} [KernelProofData a K] {f : X → ℂ} {σ₁ σ₂ : X → ℤ} [IsCancellative X (defaultτ a)] (P : P304 q q' F f σ₁ σ₂) => P304.mk (F := F) (P.CP (F := F)) (⋯.choose (p := fun (G' : Set X) => G' ⊆ P.G (F := F) ∧ Bornology.IsBounded G' ∧ MeasurableSet G' ∧ HMul.hMul (β := ENNReal) (2 : ENNReal) ((volume : Measure X) G' : ENNReal) ≤ (volume : Measure X) (P.G (F := F)) ∧ ∫⁻ (x : X) in P.G (F := F) \ G', ‖T_lin (P.CP (F := F).Q (F := F)) σ₁ σ₂ f x‖ₑ ≤ ↑(C2_0_1 a q) * HPow.hPow (α := ENNReal) ((volume : Measure X) (P.G (F := F)) : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (↑q)⁻¹)) ⋯ ⋯`

#### `defaultD` (def)
Lean: `ℕ → ℕ`
Docstring: The constant `D` from (2.0.1).
Definition: `fun (a : ℕ) => (2 : ℕ) ^ (𝕔 * a ^ (2 : ℕ))`

#### `Ks` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {K : X → X → ℂ} → [inst : PseudoMetricSpace X] → [KernelProofData a K] → ℤ → X → X → ℂ`
Docstring: K_s in the blueprint
Definition: `fun {X : Type u_1} {a : ℕ} {K : X → X → ℂ} [PseudoMetricSpace X] [KernelProofData a K] (s : ℤ) (x y : X) => K x y * ↑(ψ (defaultD a) (HPow.hPow (α := ℝ) (↑(defaultD a)) (-s) * dist x y))`

#### `Set.Annulus.oo` (def)
Lean: `{X : Type u_1} → [PseudoMetricSpace X] → X → ℝ → ℝ → Set X`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] (x : X) (r R : ℝ) => {y : X | dist x y ∈ Set.Ioo r R}`

#### `maximalFunction` (def)
Lean: `{X : Type u_1} → {ε : Type u_2} → [PseudoMetricSpace X] → [inst : MeasurableSpace X] → [ENorm ε] → {ι : Type u_4} → Measure X → Set ι → (ι → X) → (ι → ℝ) → ℝ → (X → ε) → X → ENNReal`
Docstring: The uncentered Hardy-Littlewood maximal function, for a family of balls.
Definition: `fun {X : Type u_1} {ε : Type u_2} [PseudoMetricSpace X] [MeasurableSpace X] [ENorm ε] {ι : Type u_4} (μ : Measure X) (𝓑 : Set ι) (c : ι → X) (r : ι → ℝ) (p : ℝ) (u : X → ε) (x : X) => ⨆ i ∈ 𝓑, (Metric.ball (c i) (r i)).indicator (fun (x : X) => (⨍⁻ (y : X) in Metric.ball (c i) (r i), ‖u y‖ₑ ^ p ∂μ) ^ p⁻¹) x`

#### `P304` (structure or class)
Lean: `{X : Type u_1} → {a : ℕ} → [inst : MetricSpace X] → NNReal → NNReal → Set X → {K : X → X → ℂ} → [KernelProofData a K] → (X → ℂ) → (X → ℤ) → (X → ℤ) → Type u_1`
Docstring: All the parameters needed to apply the recursion of Lemma 3.0.4.
Fields: `G`

## Flagged translations

### `R_truncation`
Lean (short): `[KernelProofData a K] [IsCancellative X (defaultτ a)] (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (hR : R = 2 ^ n) (BST_T_Q : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, ⨆ R₁ ∈ Set.Ioo R⁻¹ R, ⨆ R₂ ∈ Set.Ioo R₁ R, ‖T_R K Q R₁ R₂ R f x‖ₑ ≤ ↑(C1_0_2 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [inst_1 : KernelProofData a K] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} {f : X → ℂ} [IsCancellative X (defaultτ a)], q ∈ Set.Ioc (1 : NNReal) (2 : NNReal) → q.HolderConjugate q' → MeasurableSet F → MeasurableSet G → Measurable f → (fun (x : X) => ‖f x‖) ≤ F.indicator (1 : X → ℝ) → ∀ {n : ℕ} {R : ℝ}, R = (2 : ℝ) ^ n → (∀ (θ : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), HasBoundedStrongType (ε₁ := ℂ) (ε₂ := ENNReal) (α := X) (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (fun (x1 : X → ℂ) (x2 : X) => linearizedNontangentialOperator (⇑Q) θ K x1 x2) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → ∫⁻ (x : X) in G, ⨆ R₁ ∈ Set.Ioo R⁻¹ R, ⨆ R₂ ∈ Set.Ioo R₁ R, ‖T_R K Q R₁ R₂ R f x‖ₑ ≤ ↑(C1_0_2 a q) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (↑q)⁻¹`
Docstring: Lemma 3.0.2.
Previous English: Let $X$ be a metric space, $a\in\mathbb N$, and $K : X\times X\to\mathbb C$ a kernel satisfying the standing assumptions `KernelProofData a K` (so $X$ carries a doubling measure $\mu$ with parameter depending on $a$ and $K$ satisfies the kernel bounds), and assume the cancellative property `IsCancellative X (defaultτ a)` holds (with the default exponent $\tau=\mathrm{defaultτ}(a)$). Let $q,q'$ be nonnegative reals with $q\in(1,2]$ and $q'$ its Hölder conjugate, let $F,G\subseteq X$ be measurable, let $Q:X\to\Theta(X)$ be a simple function, and let $f:X\to\mathbb C$ be measurable with $|f|\le\mathbf 1_F$ pointwise. Let $n\in\mathbb N$ and $R=2^n\in\mathbb R$, and suppose that for every $\theta\in\Theta(X)$ the linearized nontangential operator associated with $Q$, $\theta$ and $K$ has bounded strong type $(2,2)$ (with respect to $\mu$) with constant $C_{T_s}(a)$. Then (Lemma 3.0.2) $$\int_G\sup_{R^{-1}<R_1<R}\ \sup_{R_1<R_2<R}\big\|T_R(K,Q,R_1,R_2,R)f(x)\big\|\,d\mu(x)\le C_{1.0.2}(a,q)\,\mu(G)^{1/q'}\,\mu(F)^{1/q}.$$
Checker's issue: The central operator T_R(K,Q,R_1,R_2,R) is never introduced: no definition and no name identifying it as the project operator `T_R` (Lemma 3.0.2's T_{R1,R2,R}: 1_{B(o,R)}(x) times the Carleson integrand over the annulus R1<d(x,y)<R2 with phase e^{iQ(x)(y)}). The constants C_{1.0.2}(a,q) and C_{T_s}(a), and Theta(X), are also used as bare symbols with no value or name.

### `R_truncation'`
Lean (short): `[KernelProofData a K] [IsCancellative X (defaultτ a)] (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (hR : R = 2 ^ n) (sF : F ⊆ Metric.ball (cancelPt X) (2 * R)) (sG : G ⊆ Metric.ball (cancelPt X) R) (BST_T_Q : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, ⨆ R₁ ∈ Set.Ioo R⁻¹ R, ⨆ R₂ ∈ Set.Ioo R₁ R, ‖T_R K Q R₁ R₂ R f x‖ₑ ≤ ↑(C1_0_2 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [inst_1 : KernelProofData a K] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} {f : X → ℂ} [IsCancellative X (defaultτ a)], q ∈ Set.Ioc (1 : NNReal) (2 : NNReal) → q.HolderConjugate q' → MeasurableSet F → MeasurableSet G → Measurable f → (fun (x : X) => ‖f x‖) ≤ F.indicator (1 : X → ℝ) → ∀ {n : ℕ} {R : ℝ}, R = (2 : ℝ) ^ n → F ⊆ Metric.ball (cancelPt X) ((2 : ℝ) * R) → G ⊆ Metric.ball (cancelPt X) R → (∀ (θ : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), HasBoundedStrongType (ε₁ := ℂ) (ε₂ := ENNReal) (α := X) (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (fun (x1 : X → ℂ) (x2 : X) => linearizedNontangentialOperator (⇑Q) θ K x1 x2) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → ∫⁻ (x : X) in G, ⨆ R₁ ∈ Set.Ioo R⁻¹ R, ⨆ R₂ ∈ Set.Ioo R₁ R, ‖T_R K Q R₁ R₂ R f x‖ₑ ≤ ↑(C1_0_2 a q) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (↑q)⁻¹`
Previous English: Let $X$ be a metric space, $a\in\mathbb N$, and $K : X\times X\to\mathbb C$ a kernel satisfying the standing assumptions `KernelProofData a K` (so $X$ carries a doubling measure $\mu$ with parameter depending on $a$ and $K$ satisfies the kernel bounds), and assume the cancellative property `IsCancellative X (defaultτ a)` holds (with the default exponent $\tau=\mathrm{defaultτ}(a)$). Let $q,q'$ be nonnegative reals with $q\in(1,2]$ and $q'$ its Hölder conjugate, let $F,G\subseteq X$ be measurable, let $Q:X\to\Theta(X)$ be a simple function, and let $f:X\to\mathbb C$ be measurable with $|f|\le\mathbf 1_F$ pointwise. Let $n\in\mathbb N$ and $R=2^n\in\mathbb R$, assume $F\subseteq B(o,2R)$ and $G\subseteq B(o,R)$ where $o=\mathrm{cancelPt}(X)$, and suppose that for every $\theta\in\Theta(X)$ the linearized nontangential operator associated with $Q$, $\theta$ and $K$ has bounded strong type $(2,2)$ (with respect to $\mu$) with constant $C_{T_s}(a)$. Then $$\int_G\sup_{R^{-1}<R_1<R}\ \sup_{R_1<R_2<R}\big\|T_R(K,Q,R_1,R_2,R)f(x)\big\|\,d\mu(x)\le C_{1.0.2}(a,q)\,\mu(G)^{1/q'}\,\mu(F)^{1/q}.$$
Checker's issue: Same as R_truncation: T_R(K,Q,R_1,R_2,R), C_{1.0.2}(a,q), C_{T_s}(a) and Theta(X) appear as bare symbols with no definition or name tying them to the project notions `T_R`, `C1_0_2`, `C_Ts`.

### `finitary_carleson_step`
Lean (short): `[KernelProofData a K] [IsCancellative X (defaultτ a)] (CP : CP304 q q' F f σ₁ σ₂) (bG : Bornology.IsBounded G) (mG : MeasurableSet G) : ∃ G' ⊆ G, Bornology.IsBounded G' ∧ MeasurableSet G' ∧ 2 * volume G' ≤ volume G ∧ ∫⁻ (x : X) in G \ G', ‖T_lin CP.Q σ₁ σ₂ f x‖ₑ ≤ ↑(C2_0_1 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [inst_1 : KernelProofData a K] {f : X → ℂ} {σ₁ σ₂ : X → ℤ} [IsCancellative X (defaultτ a)] (CP : CP304 q q' F f σ₁ σ₂), Bornology.IsBounded G → MeasurableSet G → ∃ G' ⊆ G, Bornology.IsBounded G' ∧ MeasurableSet G' ∧ HMul.hMul (β := ENNReal) (2 : ENNReal) ((volume : Measure X) G' : ENNReal) ≤ (volume : Measure X) G ∧ ∫⁻ (x : X) in G \ G', ‖T_lin (CP.Q (F := F)) σ₁ σ₂ f x‖ₑ ≤ ↑(C2_0_1 a q) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (↑q)⁻¹`
Previous English: Let $X$ be a metric space, $a\in\mathbb N$, and $K : X\times X\to\mathbb C$ a kernel satisfying the standing assumptions `KernelProofData a K` (so $X$ carries a doubling measure $\mu$ with parameter depending on $a$ and $K$ satisfies the kernel bounds), and assume the cancellative property `IsCancellative X (defaultτ a)` holds (with the default exponent $\tau=\mathrm{defaultτ}(a)$). Let $q,q'$ be nonnegative reals, $F,G\subseteq X$, $f:X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$, let $CP$ be data of type $\mathrm{CP304}(q,q',F,f,\sigma_1,\sigma_2)$ (with associated simple function $Q_{CP}$), and let $G$ be bounded and measurable. Then there exists a bounded measurable $G'\subseteq G$ with $2\mu(G')\le\mu(G)$ and $$\int_{G\setminus G'}\big\|T_{\mathrm{lin}}(Q_{CP},\sigma_1,\sigma_2)f(x)\big\|\,d\mu(x)\le C_{2.0.1}(a,q)\,\mu(G)^{1/q'}\,\mu(F)^{1/q}.$$
Checker's issue: T_lin(Q_CP,sigma_1,sigma_2) and C_{2.0.1}(a,q) are used as bare symbols with no definition or name (T_lin is the project operator `T_lin`, i.e. T_S Q (sigma_1 x) (sigma_2 x) f x). CP304 is also left opaque, so the hypotheses it carries are invisible.

### `enorm_carlesonOperatorIntegrand_le_T_S`
Lean (short): `[KernelProofData a K] (hR₁ : 0 < R₁) (hR₂ : R₁ < R₂) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) : ‖carlesonOperatorIntegrand K (Q x) R₁ R₂ f x‖ₑ ≤ ‖T_S Q (L302 a R₁) (U302 a R₂) f x‖ₑ + 4 * ↑(C2_1_3 a) * globalMaximalFunction volume 1 (F.indicator 1) x`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] {F : Set X} {K : X → X → ℂ} [inst_1 : KernelProofData a K] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} {f : X → ℂ} {R₁ R₂ : ℝ}, (0 : ℝ) < R₁ → R₁ < R₂ → Measurable f → (fun (x : X) => ‖f x‖) ≤ F.indicator (1 : X → ℝ) → ∀ {x : X}, ‖carlesonOperatorIntegrand K (Q x) R₁ R₂ f x‖ₑ ≤ ‖T_S Q (L302 a R₁) (U302 a R₂) f x‖ₑ + (4 : ENNReal) * ↑(C2_1_3 a) * globalMaximalFunction volume (1 : ℝ) (F.indicator (1 : X → ℝ)) x`
Previous English: Let $X$ be a metric space, $a\in\mathbb N$, and $K : X\times X\to\mathbb C$ a kernel satisfying the standing assumptions `KernelProofData a K` (so $X$ carries a doubling measure $\mu$ with parameter depending on $a$ and $K$ satisfies the kernel bounds). Let $F\subseteq X$, let $Q:X\to\Theta(X)$ be a simple function, let $R_1,R_2$ be reals with $0<R_1<R_2$, and let $f:X\to\mathbb C$ be measurable with $|f|\le\mathbf 1_F$ pointwise. Then for every $x\in X$, $$\big\|\mathrm{carlesonOperatorIntegrand}(K,Q(x),R_1,R_2,f)(x)\big\|\le\big\|T_S(Q,L_{302}(a,R_1),U_{302}(a,R_2))f(x)\big\|+4\,C_{2.1.3}(a)\,M(\mathbf 1_F)(x),$$ where $M$ is the global maximal function with respect to $\mu$ with exponent $1$.
Checker's issue: T_S(Q,L_302(a,R_1),U_302(a,R_2)), L_302, U_302 and C_{2.1.3}(a) appear as bare symbols with no definition or name (e.g. T_S = sum over s in [s1,s2] of the integral of K_s(x,y) f(y) e^{iQ(x)(y)}; L302 = floor(log_D(2R_1))+3; U302 = ceil(log_D(4R_2))-2). The integrand carlesonOperatorIntegrand is not described either.

### `linearized_truncation`
Lean (short): `[KernelProofData a K] [IsCancellative X (defaultτ a)] (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (bF : Bornology.IsBounded F) (bG : Bornology.IsBounded G) (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (mσ₁ : Measurable σ₁) (mσ₂ : Measurable σ₂) (rσ₁ : (Set.range σ₁).Finite) (rσ₂ : (Set.range σ₂).Finite) (lσ : σ₁ ≤ σ₂) (BST_T_Q : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, ‖T_lin Q σ₁ σ₂ f x‖ₑ ≤ ↑(C3_0_4 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [inst_1 : KernelProofData a K] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} {f : X → ℂ} {σ₁ σ₂ : X → ℤ} [IsCancellative X (defaultτ a)], q ∈ Set.Ioc (1 : NNReal) (2 : NNReal) → q.HolderConjugate q' → Bornology.IsBounded F → Bornology.IsBounded G → MeasurableSet F → MeasurableSet G → Measurable f → (fun (x : X) => ‖f x‖) ≤ F.indicator (1 : X → ℝ) → Measurable σ₁ → Measurable σ₂ → (Set.range σ₁).Finite → (Set.range σ₂).Finite → σ₁ ≤ σ₂ → (∀ (θ : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), HasBoundedStrongType (ε₁ := ℂ) (ε₂ := ENNReal) (α := X) (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (fun (x1 : X → ℂ) (x2 : X) => linearizedNontangentialOperator (⇑Q) θ K x1 x2) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → ∫⁻ (x : X) in G, ‖T_lin Q σ₁ σ₂ f x‖ₑ ≤ ↑(C3_0_4 a q) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (↑q)⁻¹`
Docstring: Lemma 3.0.4.
Previous English: Let $X$ be a metric space, $a\in\mathbb N$, and $K : X\times X\to\mathbb C$ a kernel satisfying the standing assumptions `KernelProofData a K` (so $X$ carries a doubling measure $\mu$ with parameter depending on $a$ and $K$ satisfies the kernel bounds), and assume the cancellative property `IsCancellative X (defaultτ a)` holds (with the default exponent $\tau=\mathrm{defaultτ}(a)$). Let $q,q'$ be nonnegative reals with $q\in(1,2]$ and $q'$ its Hölder conjugate, let $F,G\subseteq X$ be bounded measurable sets, let $Q:X\to\Theta(X)$ be a simple function, let $f:X\to\mathbb C$ be measurable with $|f|\le\mathbf 1_F$, let $\sigma_1,\sigma_2:X\to\mathbb Z$ be measurable with finite ranges and $\sigma_1\le\sigma_2$ pointwise, and suppose that for every $\theta\in\Theta(X)$ the linearized nontangential operator associated with $Q$, $\theta$ and $K$ has bounded strong type $(2,2)$ (with respect to $\mu$) with constant $C_{T_s}(a)$. Then (Lemma 3.0.4) $$\int_G\big\|T_{\mathrm{lin}}(Q,\sigma_1,\sigma_2)f(x)\big\|\,d\mu(x)\le C_{3.0.4}(a,q)\,\mu(G)^{1/q'}\,\mu(F)^{1/q}.$$
Checker's issue: T_lin(Q,sigma_1,sigma_2) and C_{3.0.4}(a,q) are used as bare symbols with no definition or name tying them to the project operator `T_lin` and constant `C3_0_4`.

### `slice_integral_bound`
Lean (short): `[KernelProofData a K] [IsCancellative X (defaultτ a)] : ∫⁻ (x : X) in (slice CP bG mG n).G \ (slice CP bG mG (n + 1)).G, ‖T_lin CP.Q σ₁ σ₂ f x‖ₑ ≤ ↑(C2_0_1 a q) * volume (slice CP bG mG n).G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [inst_1 : KernelProofData a K] {f : X → ℂ} {σ₁ σ₂ : X → ℤ} [inst_2 : IsCancellative X (defaultτ a)] {CP : CP304 q q' F f σ₁ σ₂} {bG : Bornology.IsBounded G} {mG : MeasurableSet G} {n : ℕ}, ∫⁻ (x : X) in (slice (F := F) (G := G) CP bG mG n).G (F := F) \ (slice (F := F) (G := G) CP bG mG (n + (1 : ℕ))).G (F := F), ‖T_lin (CP.Q (F := F)) σ₁ σ₂ f x‖ₑ ≤ ↑(C2_0_1 a q) * HPow.hPow (α := ENNReal) ((volume : Measure X) ((slice (F := F) (G := G) CP bG mG n).G (F := F)) : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (↑q)⁻¹`
Previous English: Let $X$ be a metric space, $a\in\mathbb N$, and $K : X\times X\to\mathbb C$ a kernel satisfying the standing assumptions `KernelProofData a K` (so $X$ carries a doubling measure $\mu$ with parameter depending on $a$ and $K$ satisfies the kernel bounds), and assume the cancellative property `IsCancellative X (defaultτ a)` holds (with the default exponent $\tau=\mathrm{defaultτ}(a)$). Let $q,q'\ge 0$ be nonnegative reals, $F,G\subseteq X$, $f:X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$, let $CP$ be data of type $\mathrm{CP304}(q,q',F,f,\sigma_1,\sigma_2)$ (with associated simple function $Q_{CP}$), and let $G$ be bounded (witness $bG$) and measurable (witness $mG$); write $G_n$ for the set $(\mathrm{slice}\,CP\,bG\,mG\,n).G$ of the $n$-th slice ($n\in\mathbb N$). Then $$\int_{G_n\setminus G_{n+1}}\big\|T_{\mathrm{lin}}(Q_{CP},\sigma_1,\sigma_2)f(x)\big\|\,d\mu(x)\le C_{2.0.1}(a,q)\,\mu(G_n)^{1/q'}\,\mu(F)^{1/q}.$$
Checker's issue: T_lin(Q_CP,sigma_1,sigma_2) and C_{2.0.1}(a,q) are used as bare symbols with no definition or name tying them to the project operator `T_lin` and constant `C2_0_1`.

### `slice_integral_bound_sum`
Lean (short): `[KernelProofData a K] [IsCancellative X (defaultτ a)] : ∫⁻ (x : X), (G \ (slice CP bG mG (n + 1)).G).indicator (fun x => ‖T_lin CP.Q σ₁ σ₂ f x‖ₑ) x ≤ (↑(C2_0_1 a q) * ∑ i ∈ Finset.range (n + 1), (2⁻¹ ^ i) ^ (↑q')⁻¹) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [inst_1 : KernelProofData a K] {f : X → ℂ} {σ₁ σ₂ : X → ℤ} [inst_2 : IsCancellative X (defaultτ a)] {CP : CP304 q q' F f σ₁ σ₂} {bG : Bornology.IsBounded G} {mG : MeasurableSet G} {n : ℕ}, ∫⁻ (x : X), (G \ (slice (F := F) (G := G) CP bG mG (n + (1 : ℕ))).G (F := F)).indicator (fun (x : X) => ‖T_lin (CP.Q (F := F)) σ₁ σ₂ f x‖ₑ) x ≤ (↑(C2_0_1 a q) * ∑ i ∈ Finset.range (n + (1 : ℕ)), ((2 : ENNReal)⁻¹ ^ i) ^ (↑q')⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (↑q)⁻¹`
Docstring: The slightly unusual way of writing the integrand is to facilitate applying the monotone convergence theorem.
Previous English: Let $X$ be a metric space, $a\in\mathbb N$, and $K : X\times X\to\mathbb C$ a kernel satisfying the standing assumptions `KernelProofData a K` (so $X$ carries a doubling measure $\mu$ with parameter depending on $a$ and $K$ satisfies the kernel bounds), and assume the cancellative property `IsCancellative X (defaultτ a)` holds (with the default exponent $\tau=\mathrm{defaultτ}(a)$). Let $q,q'\ge 0$ be nonnegative reals, $F,G\subseteq X$, $f:X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$, let $CP$ be data of type $\mathrm{CP304}(q,q',F,f,\sigma_1,\sigma_2)$ (with associated simple function $Q_{CP}$), and let $G$ be bounded (witness $bG$) and measurable (witness $mG$); write $G_n$ for the set $(\mathrm{slice}\,CP\,bG\,mG\,n).G$ of the $n$-th slice ($n\in\mathbb N$). Then $$\int_X\mathbf 1_{G\setminus G_{n+1}}(x)\,\big\|T_{\mathrm{lin}}(Q_{CP},\sigma_1,\sigma_2)f(x)\big\|\,d\mu(x)\le\Big(C_{2.0.1}(a,q)\sum_{i=0}^{n}(2^{-i})^{1/q'}\Big)\,\mu(G)^{1/q'}\,\mu(F)^{1/q}.$$ (Per the docstring, the integrand is written with an indicator to facilitate applying the monotone convergence theorem.)
Checker's issue: T_lin(Q_CP,sigma_1,sigma_2) and C_{2.0.1}(a,q) are used as bare symbols with no definition or name tying them to the project operator `T_lin` and constant `C2_0_1`.

### `S_truncation`
Lean (short): `[KernelProofData a K] [IsCancellative X (defaultτ a)] (hq : q ∈ Set.Ioc 1 2) (hqq' : q.HolderConjugate q') (bF : Bornology.IsBounded F) (bG : Bornology.IsBounded G) (mF : MeasurableSet F) (mG : MeasurableSet G) (mf : Measurable f) (nf : (fun x => ‖f x‖) ≤ F.indicator 1) (BST_T_Q : ∀ (θ : Θ X), HasBoundedStrongType (fun x1 x2 => linearizedNontangentialOperator (⇑Q) θ K x1 x2) 2 2 volume volume ↑(C_Ts a)) : ∫⁻ (x : X) in G, ⨆ s₁ ∈ Finset.Icc (-↑B) ↑B, ⨆ s₂ ∈ Finset.Icc s₁ ↑B, ‖T_S Q s₁ s₂ f x‖ₑ ≤ ↑(C3_0_4 a q) * volume G ^ (↑q')⁻¹ * volume F ^ (↑q)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} [inst : MetricSpace X] {q q' : NNReal} {F G : Set X} {K : X → X → ℂ} [inst_1 : KernelProofData a K] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} {f : X → ℂ} [IsCancellative X (defaultτ a)] {B : ℕ}, q ∈ Set.Ioc (1 : NNReal) (2 : NNReal) → q.HolderConjugate q' → Bornology.IsBounded F → Bornology.IsBounded G → MeasurableSet F → MeasurableSet G → Measurable f → (fun (x : X) => ‖f x‖) ≤ F.indicator (1 : X → ℝ) → (∀ (θ : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), HasBoundedStrongType (ε₁ := ℂ) (ε₂ := ENNReal) (α := X) (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (fun (x1 : X → ℂ) (x2 : X) => linearizedNontangentialOperator (⇑Q) θ K x1 x2) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → ∫⁻ (x : X) in G, ⨆ (s₁ : ℤ), ⨆ (_ : Membership.mem (γ := Finset ℤ) (Finset.Icc (-↑B) ↑B) s₁), ⨆ s₂ ∈ Finset.Icc s₁ ↑B, ‖T_S Q s₁ s₂ f x‖ₑ ≤ ↑(C3_0_4 a q) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) (↑q')⁻¹ * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (↑q)⁻¹`
Docstring: Lemma 3.0.3. `B` is the blueprint's `S`.
Previous English: Let $X$ be a metric space, $a\in\mathbb N$, and $K : X\times X\to\mathbb C$ a kernel satisfying the standing assumptions `KernelProofData a K` (so $X$ carries a doubling measure $\mu$ with parameter depending on $a$ and $K$ satisfies the kernel bounds), and assume the cancellative property `IsCancellative X (defaultτ a)` holds (with the default exponent $\tau=\mathrm{defaultτ}(a)$). Let $q,q'$ be nonnegative reals with $q\in(1,2]$ and $q'$ its Hölder conjugate, let $F,G\subseteq X$ be bounded measurable sets, let $Q:X\to\Theta(X)$ be a simple function, let $f:X\to\mathbb C$ be measurable with $|f|\le\mathbf 1_F$, let $B\in\mathbb N$ (the blueprint's $S$), and suppose that for every $\theta\in\Theta(X)$ the linearized nontangential operator associated with $Q$, $\theta$ and $K$ has bounded strong type $(2,2)$ (with respect to $\mu$) with constant $C_{T_s}(a)$. Then (Lemma 3.0.3) $$\int_G\sup_{s_1\in[-B,B]}\ \sup_{s_2\in[s_1,B]}\big\|T_S(Q,s_1,s_2)f(x)\big\|\,d\mu(x)\le C_{3.0.4}(a,q)\,\mu(G)^{1/q'}\,\mu(F)^{1/q},$$ where $s_1,s_2$ range over integers.
Checker's issue: T_S(Q,s_1,s_2) and C_{3.0.4}(a,q) are used as bare symbols with no definition or name (T_S is the project operator `T_S` of Lemma 3.0.3: the sum over s in [s1,s2] of the integral of K_s(x,y) f(y) e^{iQ(x)(y)}).
