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

#### `CompatibleFunctions.toFunctionDistances` (def)
Lean: `{𝕜 : outParam (Type u_3)} → {X : Type u} → {A : outParam ℕ} → {inst : RCLike 𝕜} → {inst_1 : PseudoMetricSpace X} → [self : CompatibleFunctions 𝕜 X A] → FunctionDistances 𝕜 X`
Definition: `fun {𝕜 : outParam (Type u_3)} (X : Type u) {A : outParam ℕ} {inst : RCLike 𝕜} {inst_1 : PseudoMetricSpace X} [self : CompatibleFunctions 𝕜 X A] => self.1`

#### `KernelProofData.cf` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → {inst : PseudoMetricSpace X} → [self : KernelProofData a K] → CompatibleFunctions ℝ X (defaultA a)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {K : outParam (X → X → ℂ)} {inst : PseudoMetricSpace X} [self : KernelProofData a K] => self.3`

#### `KernelProofData.d` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → {inst : PseudoMetricSpace X} → [self : KernelProofData a K] → DoublingMeasure X ↑(defaultA a)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {K : outParam (X → X → ℂ)} {inst : PseudoMetricSpace X} [self : KernelProofData a K] => self.1`

#### `MeasureTheory.BoundedCompactSupport` (inductive)
Lean: `{X : Type u_1} → {E : Type u_2} → [TopologicalSpace X] → [inst : MeasurableSpace X] → [TopologicalSpace E] → [ENorm E] → [Zero E] → (X → E) → autoParam (Measure X) BoundedCompactSupport._auto_1 → Prop`
Docstring: Bounded compactly supported measurable functions

#### `MeasureTheory.DoublingMeasure.toMeasureSpace` (def)
Lean: `{X : Type u_3} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → [self : DoublingMeasure X A] → MeasureSpace X`
Definition: `fun (X : Type u_3) {A : outParam NNReal} {inst : PseudoMetricSpace X} [self : DoublingMeasure X A] => self.3`

#### `ProofData` (structure or class)
Lean: `{X : Type u_1} → outParam ℕ → outParam ℝ → outParam (X → X → ℂ) → outParam (X → ℤ) → outParam (X → ℤ) → outParam (Set X) → outParam (Set X) → [PseudoMetricSpace X] → Type (u_1 + 1)`
Docstring: Data common through most of chapters 2-7 (except 3).
Fields: `1`, `2`, `Q`, `θ`, `ε₁`, `ε₂`, `α`, `_x`, `_x'`, `x1`, `x2`

#### `ProofData.Q` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {q : outParam ℝ} → {K : outParam (X → X → ℂ)} → {σ₁ σ₂ : outParam (X → ℤ)} → {F G : outParam (Set X)} → {inst : PseudoMetricSpace X} → [self : ProofData a q K σ₁ σ₂ F G] → SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {q : outParam ℝ} {K : outParam (X → X → ℂ)} {σ₁ σ₂ : outParam (X → ℤ)} {F G : outParam (Set X)} {inst : PseudoMetricSpace X} [self : ProofData a q K σ₁ σ₂ F G] => self.13`

#### `ProofData.toKernelProofData` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {q : outParam ℝ} → {K : outParam (X → X → ℂ)} → {σ₁ σ₂ : outParam (X → ℤ)} → {F G : outParam (Set X)} → {inst : PseudoMetricSpace X} → [self : ProofData a q K σ₁ σ₂ F G] → KernelProofData a K`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {q : outParam ℝ} {K : outParam (X → X → ℂ)} {σ₁ σ₂ : outParam (X → ℤ)} {F G : outParam (Set X)} {inst : PseudoMetricSpace X} [self : ProofData a q K σ₁ σ₂ F G] => self.1`

#### `TileStructure` (structure or class)
Lean: `{X : Type u} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → [inst_2 : FunctionDistances ℝ X] → outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _)) → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (u + 1)`
Docstring: A tile structure.
Fields: `Ω`, `ι`, `p`, `_`, `γ`, `4`, `5`, `1`

#### `TileStructure.Forest` (structure or class)
Lean: `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → Type u_1`
Docstring: An `n`-forest
Fields: `F`, `G`, `𝔘`, `𝔗`, `4`, `1`, `2`, `8`, `α`

#### `TileStructure.Forest.C7_3_1_2` (def)
Lean: `ℕ → NNReal`
Docstring: The constant used in `density_tree_bound2` and `indicator_adjoint_tree_estimate`. Has value `2 ^ (282 * a ^ 3)` in the blueprint.
Definition: `Forest.wrapped✝.1`

#### `TileStructure.Forest.instMembership𝔓Real` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Membership (𝔓 X) (Forest X (F := F) (G := G) n)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} => { mem := fun (t : Forest X (F := F) (G := G) n) (x : 𝔓 X) => x ∈ t.𝔘 (F := F) (G := G) }`

#### `TileStructure.Forest.𝔗` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → 𝔓 X → Set (𝔓 X)`
Docstring: The value of `𝔗 u` only matters when `u ∈ 𝔘`.
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] (a : ℕ) (q : ℝ) (K : X → X → ℂ) (σ₁ σ₂ : X → ℤ) (F G : Set X) [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (n : ℕ) (self : Forest X (F := F) (G := G) n) => self.2`

#### `TileStructure.toPreTileStructure` (def)
Lean: `{X : Type u} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {inst_2 : FunctionDistances ℝ X} → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : TileStructure Q D κ S o] → PreTileStructure Q D κ S o`
Definition: `fun (X : Type u) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {inst_2 : FunctionDistances ℝ X} {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : TileStructure Q D κ S o] => self.1`

#### `adjointCarlesonSum` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → (X → ℂ) → X → ℂ`
Docstring: The definition of `T_ℭ*g(x)`, defined at the bottom of Section 7.4
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) => ∑ p : 𝔓 X with p ∈ ℭ, adjointCarleson (F := F) (G := G) p f x`

#### `cancelPt` (def)
Lean: `{𝕜 : Type u_1} → (X : Type u_2) → {A : ℕ} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [CompatibleFunctions 𝕜 X A] → X`
Docstring: The point `o` in the blueprint
Definition: `fun {𝕜 : Type u_1} (X : Type u_2) {A : ℕ} [RCLike 𝕜] [PseudoMetricSpace X] [CompatibleFunctions 𝕜 X A] => Exists.choose (p := fun (o : X) => ∀ (f : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), (coeΘ f) o = (0 : 𝕜)) ⋯`

#### `defaultA` (def)
Lean: `ℕ → ℕ`
Docstring: This is usually the value of the argument `A` in `DoublingMeasure` and `CompatibleFunctions`
Definition: `fun (a : ℕ) => (2 : ℕ) ^ a`

#### `defaultD` (def)
Lean: `ℕ → ℕ`
Docstring: The constant `D` from (2.0.1).
Definition: `fun (a : ℕ) => (2 : ℕ) ^ (𝕔 * a ^ (2 : ℕ))`

#### `defaultS` (def)
Lean: `(X : Type u_1) → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [ProofData a q K σ₁ σ₂ F G] → ℕ`
Definition: `fun (X : Type u_1) {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [PseudoMetricSpace X] [ProofData a q K σ₁ σ₂ F G] => Nat.find (p := fun (n : ℕ) => (∀ (x : X), -↑n ≤ σ₁ x ∧ σ₂ x ≤ ↑n) ∧ F ⊆ Metric.ball (cancelPt X) (HPow.hPow (α := ℝ) (↑(defaultD a)) n / (4 : ℝ)) ∧ G ⊆ Metric.ball (cancelPt X) (HPow.hPow (α := ℝ) (↑(defaultD a)) n / (4 : ℝ)) ∧ (0 : ℕ) < n) ⋯`

#### `defaultκ` (def)
Lean: `ℕ → ℝ`
Docstring: The constant `κ` from (2.0.2).
Definition: `fun (a : ℕ) => (2 : ℝ) ^ ((-10 : ℝ) * ↑a)`

#### `dens₁` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ENNReal`
Docstring: This density is defined to live in `ℝ≥0∞`. Use `ENNReal.toReal` to get a real number.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔓' : Set (𝔓 X)) => ⨆ p' ∈ 𝔓', ⨆ (l : NNReal), ⨆ (_ : l ≥ (2 : NNReal)), HPow.hPow (β := ℝ) (↑l) (-↑a) * ⨆ p ∈ lowerCubes (F := F) (G := G) 𝔓', ⨆ (_ : smul (F := F) (G := G) (↑l) p' ≤ smul (F := F) (G := G) (↑l) p), HDiv.hDiv (α := ENNReal) (β := ENNReal) ((volume : Measure X) (E₂ (F := F) (G := G) (↑l) p) : ENNReal) ((volume : Measure X) ↑(𝓘 p) : ENNReal)`

#### `dens₂` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ENNReal`
Docstring: This density is defined to live in `ℝ≥0∞`. Use `ENNReal.toReal` to get a real number.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔓' : Set (𝔓 X)) => ⨆ p ∈ 𝔓', ⨆ (r : ℝ), ⨆ (_ : r ≥ (4 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p)), HDiv.hDiv (α := ENNReal) (β := ENNReal) ((volume : Measure X) (F ∩ Metric.ball (𝔠 p) r) : ENNReal) ((volume : Measure X) (Metric.ball (𝔠 p) r) : ENNReal)`

#### `𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → (X : Type u) → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [PreTileStructure.{u, u_1, u_2} Q D κ S o] → Type u`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] (X : Type u) {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X`

#### `TileStructure.Forest.C7_4_3` (def)
Lean: `ℕ → NNReal`
Docstring: The constant used in `adjoint_tree_control`. Has value `2 ^ (182 * a ^ 3)` in the blueprint.
Definition: `Forest.wrapped✝.1`

#### `TileStructure.Forest.adjointBoundaryOperator` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → 𝔓 X → (X → ℂ) → X → ENNReal`
Docstring: The operator `S_{2,𝔲} f(x)`, given above Lemma 7.4.3.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (t : Forest X (F := F) (G := G) n) (u : 𝔓 X) (f : X → ℂ) (x : X) => ‖adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) f x‖ₑ + maximalFunction volume (Forest.𝓑 (F := F) (G := G)) (Forest.c𝓑 (F := F) (G := G)) (Forest.r𝓑 (F := F) (G := G)) (1 : ℝ) f x + ‖f x‖ₑ`

#### `PreTileStructure.𝒬` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X → @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.6`

#### `WithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → X → ℝ → Type u_2`
Docstring: Class used to endow `Θ X` with a pseudometric space structure.
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] (x : X) (r : ℝ) => @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`

#### `defaultZ` (def)
Lean: `ℕ → ℕ`
Docstring: The constant `Z` from (2.0.3).
Definition: `fun (a : ℕ) => (2 : ℕ) ^ ((12 : ℕ) * a)`

#### `instPseudoMetricSpaceWithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → {x : X} → {r : ℝ} → PseudoMetricSpace (WithFunctionDistance x r)`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] {x : X} {r : ℝ} => FunctionDistances.metric x r`

#### `𝔠` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => c (𝓘 p)`

#### `𝔰` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → ℤ`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => s (𝓘 p)`

#### `Grid` (def)
Lean: `(X : Type u) → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [GridStructure X D κ S o] → Type u`
Docstring: The indexing type of the grid structure. Elements are called (dyadic) cubes. Note that this type has instances for both `≤` and `⊆`, but they do *not* coincide.
Definition: `fun (X : Type u) {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => @GridStructure.Grid X _ inst inst_1 _ _ _ _ _`

#### `GridStructure.coeGrid` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → Set X`
Docstring: The collection of dyadic cubes
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.3`

#### `PreTileStructure.toGridStructure` (def)
Lean: `(𝕜 : Type u_1) → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → GridStructure.{u_2, u} X D κ S o`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.1`

#### `instPartialOrderGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → PartialOrder (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => PartialOrder.lift (fun (i : @GridStructure.Grid X _ inst inst_1 _ _ _ _ _) => (↑i, GridStructure.s i)) ⋯`

#### `𝓘` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → Grid X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] => PreTileStructure.𝓘`

#### `TileStructure.Forest.C7_3_1_1` (def)
Lean: `ℕ → NNReal`
Docstring: The constant used in `density_tree_bound1` and `adjoint_tree_estimate`. Has value `2 ^ (181 * a ^ 3)` in the blueprint.
Definition: `Forest.wrapped✝.1`

#### `CompatibleFunctions` (structure or class)
Lean: `(𝕜 : outParam (Type u_3)) → (X : Type u) → outParam ℕ → [RCLike 𝕜] → [PseudoMetricSpace X] → Type (max (u + 1) u_3)`
Docstring: A set `Θ` of (continuous) functions is compatible. `A` will usually be `2 ^ a`.
Fields: `o`, `f`, `0`, `2`

#### `FunctionDistances` (structure or class)
Lean: `(𝕜 : outParam (Type u_1)) → (X : Type u) → [NormedField 𝕜] → [TopologicalSpace X] → Type (max (u + 1) u_1)`
Docstring: A class stating that continuous functions have distances associated to every ball. We use a separate type to conveniently index these functions.
Fields: `Θ`, `coeΘ`, `x`, `α`

#### `KernelProofData` (structure or class)
Lean: `{X : Type u_1} → outParam ℕ → outParam (X → X → ℂ) → [PseudoMetricSpace X] → Type (u_1 + 1)`
Docstring: Data common through most of chapters 2 through 7. These contain the minimal axioms for `kernel-summand`'s proof. This is used in Chapter 3 when we don't have all other fields from `ProofData`.
Fields: `d`, `4`

#### `MeasureTheory.DoublingMeasure` (structure or class)
Lean: `(X : Type u_3) → outParam NNReal → [PseudoMetricSpace X] → Type u_3`
Docstring: A metric space with a measure with some nice properties, including a doubling condition. This is called a "doubling metric measure space" in the blueprint. `A` will usually be `2 ^ a`.
Fields: `α`, `m0`, `X`, `R`

#### `C_Ts` (def)
Lean: `ℕ → NNReal`
Docstring: A constant used on the boundedness of `T_Q^θ` and `T_*`. We generally assume `HasBoundedStrongType (linearizedNontangentialOperator Q θ K · ·) 2 2 volume volume (C_Ts a)` throughout this formalization.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ a ^ (3 : ℕ)`

#### `FunctionDistances.Θ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → (X : Type u) → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → Type u`
Docstring: A type of continuous functions from `X` to `𝕜`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.1`

#### `IsCancellative` (structure or class)
Lean: `(X : Type u_2) → {A : ℕ} → [inst : PseudoMetricSpace X] → [DoublingMeasure X ↑A] → ℝ → [CompatibleFunctions ℝ X A] → Prop`
Docstring: Θ is τ-cancellative. `τ` will usually be `1 / a`
Fields: `0`, `E`, `x`, `α`, `β`, `↑A`, `MeasureTheory.volume`, `1`

#### `IsOneSidedKernel` (structure or class)
Lean: `{X : Type u_1} → [PseudoMetricSpace X] → [MeasureSpace X] → outParam ℕ → (X → X → ℂ) → Prop`
Docstring: `K` is a one-sided Calderon-Zygmund kernel. In the formalization `K x y` is defined everywhere, even for `x = y`. The assumptions on `K` show that `K x x = 0`.
Fields: `2`, `β`

#### `MeasureTheory.HasBoundedStrongType` (def)
Lean: `{ε₁ : Type u_3} → {ε₂ : Type u_4} → [ENorm ε₁] → [ENorm ε₂] → [TopologicalSpace ε₁] → [TopologicalSpace ε₂] → [Zero ε₁] → {α : Type u_5} → {α' : Type u_6} → {_x : MeasurableSpace α} → {_x' : MeasurableSpace α'} → ((α → ε₁) → α' → ε₂) → ENNReal → ENNReal → Measure α → Measure α' → ENNReal → Prop`
Docstring: A weaker version of `HasStrongType`. This is the same as `HasStrongType` if `T` is continuous w.r.t. the L^2 norm, but weaker in general.
Definition: `fun {ε₁ : Type u_3} {ε₂ : Type u_4} [ENorm ε₁] [ENorm ε₂] [TopologicalSpace ε₁] [TopologicalSpace ε₂] [Zero ε₁] {α : Type u_5} {α' : Type u_6} {_x : MeasurableSpace α} {_x' : MeasurableSpace α'} (T : (α → ε₁) → α' → ε₂) (p p' : ENNReal) (μ : Measure α) (ν : Measure α') (c : ENNReal) => ∀ (f : α → ε₁), BoundedFiniteSupport f μ → AEStronglyMeasurable (T f) ν ∧ eLpNorm (T f) p' ν ≤ c * eLpNorm f p μ`

#### `defaultτ` (def)
Lean: `ℕ → ℝ`
Docstring: `defaultτ` is the inverse of `a`.
Definition: `fun (a : ℕ) => (↑a)⁻¹`

#### `linearizedNontangentialOperator` (def)
Lean: `{X : Type u_2} → {A : ℕ} → [inst : PseudoMetricSpace X] → [DoublingMeasure X ↑A] → [inst_2 : FunctionDistances ℝ X] → (X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _ → (X → X → ℂ) → (X → ℂ) → X → ENNReal`
Docstring: The linearized maximally truncated nontangential Calderon–Zygmund operator `T_Q^θ`.
Definition: `fun {X : Type u_2} {A : ℕ} [PseudoMetricSpace X] [DoublingMeasure X ↑A] [FunctionDistances ℝ X] (Q : X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (θ : @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (K : X → X → ℂ) (f : X → ℂ) (x : X) => ⨆ (R₂ : ℝ), ⨆ R₁ ∈ Set.Ioo (0 : ℝ) R₂, ⨆ x' ∈ Metric.ball x R₁, enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume (Set.EAnnulus.oo x' (ENNReal.ofReal R₁) (min (ENNReal.ofReal R₂) (upperRadius Q θ x')))) fun (y : X) => K x' y * f y)`

#### `GridStructure` (structure or class)
Lean: `(X : Type u_2) → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [DoublingMeasure X A] → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (max (u + 1) u_2)`
Docstring: A grid structure on `X`. We prefer `coeGrid : Grid → Set X` over `Grid : Set (Set X)` Note: the `s` in this paper is `-s` of Christ's paper.
Fields: `Grid`, `coeGrid`, `s`, `c`, `β`, `i`, `topCube`, `α`, `4`, `m`, `2`

#### `GridStructure.Grid` (def)
Lean: `(X : Type u_2) → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → Type u`
Docstring: indexing set for a grid structure
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.1`

#### `PreTileStructure` (structure or class)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : outParam NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → [inst_3 : FunctionDistances 𝕜 X] → outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)) → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (max (u + 1) (u_2 + 1))`
Fields: `𝔓`, `𝓘`, `𝒬`, `ι`

#### `PreTileStructure.𝓘` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X → @GridStructure.Grid X _ inst_1 inst_2 _ _ _ _ _`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.4`

#### `PreTileStructure.𝔓` (def)
Lean: `(𝕜 : Type u_1) → {inst : RCLike 𝕜} → (X : Type u) → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Type u`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.2`

#### `TileStructure.Ω` (def)
Lean: `{X : Type u} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {inst_2 : FunctionDistances ℝ X} → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : TileStructure Q D κ S o] → PreTileStructure.𝔓 ℝ X → Set (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _)`
Definition: `fun (X : Type u) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {inst_2 : FunctionDistances ℝ X} {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : TileStructure Q D κ S o] => self.2`

#### `TileLike` (def)
Lean: `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Type u_1`
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => Grid X × (Set (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))ᵒᵈ`

#### `instPartialOrderTileLike` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → PartialOrder (TileLike X (F := F) (G := G))`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => { le := instPartialOrderTileLike._aux_1, lt := instPartialOrderTileLike._aux_3, le_refl := ⋯, le_trans := ⋯, lt_iff_le_not_ge := ⋯, le_antisymm := ⋯ }`

#### `instPartialOrder𝔓Real` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → PartialOrder (𝔓 X)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => PartialOrder.lift (toTileLike (F := F) (G := G)) ⋯`

#### `smul` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℝ → 𝔓 X → TileLike X (F := F) (G := G)`
Docstring: This is not defined as such in the blueprint, but `λp ≲ λ'p'` can be written using `smul l p ≤ smul l' p'`. Beware: `smul 1 p` is very different from `toTileLike p`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (l : ℝ) (p : 𝔓 X) => (𝓘 p, ball_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) l)`

#### `stackSize` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → X → ℕ`
Docstring: The number of tiles `p` in `s` whose underlying cube `𝓘 p` contains `x`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (C : Set (𝔓 X)) (x : X) => ∑ p : 𝔓 X with p ∈ C, (↑(𝓘 p)).indicator (1 : X → ℕ) x`

#### `TileStructure.Forest.𝔘` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → Set (𝔓 X)`
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] (a : ℕ) (q : ℝ) (K : X → X → ℂ) (σ₁ σ₂ : X → ℤ) (F G : Set X) [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (n : ℕ) (self : Forest X (F := F) (G := G) n) => self.1`

#### `adjointCarleson` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
Docstring: The definition of `Tₚ*g(x)`, defined above Lemma 7.4.1
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume (E (F := F) (G := G) p)) fun (y : X) => HMul.hMul (α := ℂ) ((starRingEnd ℂ) (Ks (𝔰 p) y x) : ℂ) (Complex.exp (Complex.I * (↑(((Q (F := F) (G := G)) y : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y) - ↑(((Q (F := F) (G := G)) y : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) x)))) * f y`

#### `instFintype𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (𝔓.{u, u_1, u_2} X)`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.fintype_𝔓`

#### `FunctionDistances.coeΘ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → @Θ _ X inst inst_1 _ → C(X, 𝕜)`
Docstring: The coercion map from `Θ` to `C(X, 𝕜)`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.2`

#### `𝕔` (def)
Lean: `ℕ`
Docstring: The main constant in the blueprint, driving all the construction, is `D = 2 ^ (100 * a ^ 2)`. It turns out that the proof is robust, and works for other values of `100`, giving better constants in the end. We will formalize it using a parameter `𝕔` (that we fix equal to `100` to follow the blueprint) and having `D = 2 ^ (𝕔 * a ^ 2)`. We register two lemmas `seven_le_c` and `c_le_100` and will never unfold `𝕔` from this point on.
Definition: `wrapped✝.1`

#### `C5_3_2` (def)
Lean: `ℕ → ℝ`
Definition: `fun (a : ℕ) => (2 : ℝ) ^ ((-95 : ℝ) * ↑a)`

#### `E₂` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℝ → 𝔓 X → Set X`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (l : ℝ) (p : 𝔓 X) => (smul (F := F) (G := G) l p).toSet (F := F) (G := G)`

#### `lowerCubes` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → Set (𝔓 X)`
Docstring: `𝔓(𝔓')` in the blueprint. The set of all tiles whose cubes are less than the cube of some tile in the given set.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔓' : Set (𝔓 X)) => {p : 𝔓 X | ∃ p' ∈ 𝔓', 𝓘 p ≤ 𝓘 p'}`

#### `TileStructure.Forest.c𝓑` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ × ℕ × Grid X → X`
Docstring: The center function for the collection of balls 𝓑.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (z : ℕ × ℕ × Grid X) => c z.2.2`

#### `TileStructure.Forest.r𝓑` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ × ℕ × Grid X → ℝ`
Docstring: The radius function for the collection of balls 𝓑.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (z : ℕ × ℕ × Grid X) => (2 : ℝ) ^ z.1 * HPow.hPow (α := ℝ) (↑(defaultD a)) (s z.2.2 + ↑z.2.1)`

#### `TileStructure.Forest.𝓑` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (ℕ × ℕ × Grid X)`
Docstring: The indexing set for the collection of balls 𝓑, defined above Lemma 7.1.3.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => Set.Iic (defaultS X (F := F) (G := G) + (5 : ℕ)) ×ˢ SProd.sprod (β := Set (Grid X)) (Set.Iic ((2 : ℕ) * defaultS X (F := F) (G := G) + (3 : ℕ))) Set.univ`

#### `maximalFunction` (def)
Lean: `{X : Type u_1} → {ε : Type u_2} → [PseudoMetricSpace X] → [inst : MeasurableSpace X] → [ENorm ε] → {ι : Type u_4} → Measure X → Set ι → (ι → X) → (ι → ℝ) → ℝ → (X → ε) → X → ENNReal`
Docstring: The uncentered Hardy-Littlewood maximal function, for a family of balls.
Definition: `fun {X : Type u_1} {ε : Type u_2} [PseudoMetricSpace X] [MeasurableSpace X] [ENorm ε] {ι : Type u_4} (μ : Measure X) (𝓑 : Set ι) (c : ι → X) (r : ι → ℝ) (p : ℝ) (u : X → ε) (x : X) => ⨆ i ∈ 𝓑, (Metric.ball (c i) (r i)).indicator (fun (x : X) => (⨍⁻ (y : X) in Metric.ball (c i) (r i), ‖u y‖ₑ ^ p ∂μ) ^ p⁻¹) x`

#### `FunctionDistances.metric` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → X → ℝ → PseudoMetricSpace (@Θ _ X inst inst_1 _)`
Docstring: For each `_x : X` and `_r : ℝ`, a `PseudoMetricSpace Θ`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.4`

#### `c` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Grid X → X`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.c`

#### `s` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Grid X → ℤ`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.s`

#### `GridStructure.s` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → ℤ`
Docstring: scale functions
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.4`

## Flagged translations

### `TileStructure.Forest.indicator_adjoint_tree_estimate`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : eLpNorm (F.indicator (adjointCarlesonSum ((fun x => t.𝔗 x) u) g)) 2 volume ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * dens₂ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u : 𝔓 X} {g : X → ℂ}, BoundedCompactSupport g volume → Function.support g ⊆ G → u ∈ t → @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace (F.indicator (adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) g)) (2 : ENNReal) volume ≤ ↑(Forest.C7_3_1_2 a) * dens₁ (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) ^ (2 : ℝ)⁻¹ * dens₂ (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) ^ (2 : ℝ)⁻¹ * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace g (2 : ENNReal) volume`
Docstring: Part 2 of Lemma 7.4.2.
Previous English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\times X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume $X$ carries a `ProofData a q K σ₁ σ₂ F G` structure (by its docstring, the data common through most of chapters 2–7 of the blueprint). Among other things this structure provides a doubling measure on $X$ with constant $2^a$, whose measure we denote by $\mu$ (the measure `volume`); a type $\Theta(X)$ of continuous functions $X\to\mathbb R$ (from the compatible-functions structure it carries); and a simple function $Q:X\to\Theta(X)$. Write $D=2^{\mathfrak c\,a^2}\in\mathbb N$ (`defaultD a`, where $\mathfrak c$ is the fixed natural-number constant `𝕔` of the project), $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`), $o\in X$ for `cancelPt X` (a chosen point at which every function in $\Theta(X)$ vanishes), and $S\in\mathbb N$ for `defaultS X`, the least natural number $m>0$ such that $-m\le\sigma_1(y)$ and $\sigma_2(y)\le m$ for all $y\in X$ and $F\cup G\subseteq B(o,D^m/4)$. Assume $X$ carries a tile structure `TileStructure Q D κ S o`. This provides a finite type $\mathrm{Grid}(X)$ of (dyadic) cubes, each cube $I$ having an underlying set $I\subseteq X$, a scale $s(I)\in\mathbb Z$ and a center $c(I)\in X$, with the partial order $I\le J$ iff ($I\subseteq J$ as sets and $s(I)\le s(J)$); and a finite type $\mathfrak P(X)$ of tiles, each tile $p$ having a cube $\mathcal I(p)\in\mathrm{Grid}(X)$, scale $\mathfrak s(p)=s(\mathcal I(p))$, an element $\mathcal Q(p)\in\Theta(X)$ and a set $\Omega(p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (a term of `Forest X n`). It has a set $\mathfrak U(t)\subseteq\mathfrak P(X)$ of tiles (and $u\in t$ means $u\in\mathfrak U(t)$) and a map $\mathfrak T_t$ assigning to each tile $v\in\mathfrak P(X)$ a set of tiles $\mathfrak T_t(v)\subseteq\mathfrak P(X)$ (the field `𝔗`; by its docstring its value at $u$ only matters when $u\in\mathfrak U(t)$). For $i\in\mathbb Z$ and $w,y\in X$ let $K_i(w,y)=K(w,y)\,\psi\big(D^{-i}d(w,y)\big)$ (`Ks i w y`), where $\psi(r)=\max\big(0,\min(1,\,4Dr-1,\,2-4r)\big)$ for $r\in\mathbb R$. For a tile $p$ let $\mathsf E(p)=\{y\in X: y\in\mathcal I(p),\ Q(y)\in\Omega(p),\ \sigma_1(y)\le\mathfrak s(p)\le\sigma_2(y)\}$. For a tile $p$ and $h:X\to\mathbb C$ let $T_p^*h(z)=\int_{\mathsf E(p)}\overline{K_{\mathfrak s(p)}(y,z)}\,e^{i\,(Q(y)(y)-Q(y)(z))}\,h(y)\,d\mu(y)$ (`adjointCarleson`), and for $\mathfrak C\subseteq\mathfrak P(X)$ let $T_{\mathfrak C}^*h(z)=\sum_{p\in\mathfrak C}T_p^*h(z)$ (`adjointCarlesonSum`; by its docstring, $T_{\mathfrak C}^*$ as defined at the bottom of Section 7.4). For $\mathfrak C\subseteq\mathfrak P(X)$, $\mathrm{dens}_1(\mathfrak C)\in[0,\infty]$ is the project's density `dens₁`: the supremum over $p'\in\mathfrak C$ and real $l\ge2$ of $l^{-a}\sup\frac{\mu(\mathsf E_2(l,p))}{\mu(\mathcal I(p))}$, the inner supremum over tiles $p$ with $\mathcal I(p)\le\mathcal I(p'')$ for some $p''\in\mathfrak C$ and with `smul l p' ≤ smul l p` (the project's comparison $lp'\lesssim lp$ of the pairs `smul l p` $=(\mathcal I(p),\text{the ball of radius }l\text{ around }\mathcal Q(p)\text{ in }\Theta(X)\text{ for the function distance attached to }(c(\mathcal I(p)),D^{\mathfrak s(p)}/4))$), where $\mathsf E_2(l,p)\subseteq X$ is the project's set `E₂ l p` (the set attached to `smul l p`). For $\mathfrak C\subseteq\mathfrak P(X)$, $\mathrm{dens}_2(\mathfrak C)\in[0,\infty]$ is the project's density `dens₂`: $\mathrm{dens}_2(\mathfrak C)=\sup_{p\in\mathfrak C}\sup_{r\ge4D^{\mathfrak s(p)}}\frac{\mu(F\cap B(c(\mathcal I(p)),r))}{\mu(B(c(\mathcal I(p)),r))}$. Let $C_{7.3.1.2}(a)\in\mathbb R_{\ge0}$ be the project constant `Forest.C7_3_1_2 a` (by its docstring, of value $2^{282 a^3}$ in the blueprint). Let $u\in\mathfrak P(X)$ with $u\in t$, and write $\mathfrak T_t(u)\subseteq\mathfrak P(X)$ for the value of the forest's map $\mathfrak T_t$ at $u$ (`t.𝔗 u`). Let $g:X\to\mathbb C$ be bounded, measurable and compactly supported with respect to $\mu$ (`BoundedCompactSupport g volume`) with support contained in $G$. (Part 2 of Lemma 7.4.2.) Then $$\big\|\mathbf 1_F\cdot T^*_{\mathfrak T_t(u)}g\big\|_{L^2(\mu)}\le C_{7.3.1.2}(a)\,\mathrm{dens}_1(\mathfrak T_t(u))^{1/2}\,\mathrm{dens}_2(\mathfrak T_t(u))^{1/2}\,\|g\|_{L^2(\mu)}.$$ Here $\|\cdot\|_{L^2(\mu)}\in[0,\infty]$ denotes the $L^2(\mu)$ (semi)norm `eLpNorm · 2 volume`, and all inequalities are in $[0,\infty]$.
Checker's issue: Calls Grid(X) a finite type, which the prompt does not support (only the tile type has a finiteness instance).

### `TileStructure.Forest.adjoint_tree_control`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ t) (hf : BoundedCompactSupport f volume) (h2f : Function.support f ⊆ G) : eLpNorm (fun x => t.adjointBoundaryOperator u f x) 2 volume ≤ ↑(Forest.C7_4_3 a) * eLpNorm f 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u : 𝔓 X} {f : X → ℂ}, u ∈ t → BoundedCompactSupport f volume → Function.support f ⊆ G → @eLpNorm _ ENNReal _ MeasureSpace.toMeasurableSpace (fun (x : X) => t.adjointBoundaryOperator (F := F) (G := G) u f x) (2 : ENNReal) volume ≤ ↑(Forest.C7_4_3 a) * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (2 : ENNReal) volume`
Docstring: Lemma 7.4.3.
Previous English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\times X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume $X$ carries a `ProofData a q K σ₁ σ₂ F G` structure (by its docstring, the data common through most of chapters 2–7 of the blueprint). Among other things this structure provides a doubling measure on $X$ with constant $2^a$, whose measure we denote by $\mu$ (the measure `volume`); a type $\Theta(X)$ of continuous functions $X\to\mathbb R$ (from the compatible-functions structure it carries); and a simple function $Q:X\to\Theta(X)$. Write $D=2^{\mathfrak c\,a^2}\in\mathbb N$ (`defaultD a`, where $\mathfrak c$ is the fixed natural-number constant `𝕔` of the project), $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`), $o\in X$ for `cancelPt X` (a chosen point at which every function in $\Theta(X)$ vanishes), and $S\in\mathbb N$ for `defaultS X`, the least natural number $m>0$ such that $-m\le\sigma_1(y)$ and $\sigma_2(y)\le m$ for all $y\in X$ and $F\cup G\subseteq B(o,D^m/4)$. Assume $X$ carries a tile structure `TileStructure Q D κ S o`. This provides a finite type $\mathrm{Grid}(X)$ of (dyadic) cubes, each cube $I$ having an underlying set $I\subseteq X$, a scale $s(I)\in\mathbb Z$ and a center $c(I)\in X$, with the partial order $I\le J$ iff ($I\subseteq J$ as sets and $s(I)\le s(J)$); and a finite type $\mathfrak P(X)$ of tiles, each tile $p$ having a cube $\mathcal I(p)\in\mathrm{Grid}(X)$, scale $\mathfrak s(p)=s(\mathcal I(p))$, an element $\mathcal Q(p)\in\Theta(X)$ and a set $\Omega(p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (a term of `Forest X n`). It has a set $\mathfrak U(t)\subseteq\mathfrak P(X)$ of tiles (and $u\in t$ means $u\in\mathfrak U(t)$) and a map $\mathfrak T_t$ assigning to each tile $v\in\mathfrak P(X)$ a set of tiles $\mathfrak T_t(v)\subseteq\mathfrak P(X)$ (the field `𝔗`; by its docstring its value at $u$ only matters when $u\in\mathfrak U(t)$). For $i\in\mathbb Z$ and $w,y\in X$ let $K_i(w,y)=K(w,y)\,\psi\big(D^{-i}d(w,y)\big)$ (`Ks i w y`), where $\psi(r)=\max\big(0,\min(1,\,4Dr-1,\,2-4r)\big)$ for $r\in\mathbb R$. For a tile $p$ let $\mathsf E(p)=\{y\in X: y\in\mathcal I(p),\ Q(y)\in\Omega(p),\ \sigma_1(y)\le\mathfrak s(p)\le\sigma_2(y)\}$. For a tile $p$ and $h:X\to\mathbb C$ let $T_p^*h(z)=\int_{\mathsf E(p)}\overline{K_{\mathfrak s(p)}(y,z)}\,e^{i\,(Q(y)(y)-Q(y)(z))}\,h(y)\,d\mu(y)$ (`adjointCarleson`), and for $\mathfrak C\subseteq\mathfrak P(X)$ let $T_{\mathfrak C}^*h(z)=\sum_{p\in\mathfrak C}T_p^*h(z)$ (`adjointCarlesonSum`; by its docstring, $T_{\mathfrak C}^*$ as defined at the bottom of Section 7.4). Let $C_{7.4.3}(a)\in\mathbb R_{\ge0}$ be the project constant `Forest.C7_4_3 a` (by its docstring, of value $2^{182 a^3}$ in the blueprint). Let $u\in\mathfrak P(X)$ with $u\in t$, and write $\mathfrak T_t(u)\subseteq\mathfrak P(X)$ for the value of the forest's map $\mathfrak T_t$ at $u$ (`t.𝔗 u`). For $h:X\to\mathbb C$ let $\mathrm{Bd}^*_{t,u}h(z)=\|T^*_{\mathfrak T_t(u)}h(z)\|+M_{\mathcal B}h(z)+\|h(z)\|\in[0,\infty]$ (`t.adjointBoundaryOperator u h z`; by its docstring the operator $S_{2,u}$ given above Lemma 7.4.3), where $M_{\mathcal B}$ is as follows. Let $\mathcal B=\{0,\dots,S+5\}\times\{0,\dots,2S+3\}\times\mathrm{Grid}(X)$ and, for $\beta=(k,l,I)\in\mathcal B$, let $c_\beta=c(I)$ and $r_\beta=2^kD^{s(I)+l}$. For $h:X\to\mathbb C$ let $M_{\mathcal B}h(z)=\sup_{\beta\in\mathcal B}\mathbf 1_{B(c_\beta,r_\beta)}(z)\,\frac{1}{\mu(B(c_\beta,r_\beta))}\int_{B(c_\beta,r_\beta)}\|h\|\,d\mu\in[0,\infty]$ (`maximalFunction volume 𝓑 c𝓑 r𝓑 1 h`, the uncentered Hardy–Littlewood maximal function with exponent 1). Let $f:X\to\mathbb C$ be bounded, measurable and compactly supported with respect to $\mu$ (`BoundedCompactSupport f volume`) with support contained in $G$. (Lemma 7.4.3.) Then $$\big\|\mathrm{Bd}^*_{t,u}f\big\|_{L^2(\mu)}\le C_{7.4.3}(a)\,\|f\|_{L^2(\mu)}.$$ Here $\|\cdot\|_{L^2(\mu)}\in[0,\infty]$ denotes the $L^2(\mu)$ (semi)norm `eLpNorm · 2 volume`, and all inequalities are in $[0,\infty]$.
Checker's issue: Calls Grid(X) a finite type, which the prompt does not support (only the tile type has a finiteness instance).

### `TileStructure.Forest.𝔖₀`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (t : Forest X n) (u₁ : 𝔓 X) (u₂ : 𝔓 X) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → 𝔓 X → 𝔓 X → Set (𝔓 X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (t : Forest X (F := F) (G := G) n) (u₁ u₂ : 𝔓 X) => {p : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₁ ∪ (fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₂) p ∧ (2 : ℝ) ^ (HMul.hMul (α := ℝ) ↑(defaultZ a) ↑n / (2 : ℝ)) ≤ dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 u₁) (𝒬 u₂)}`
Docstring: The set `𝔖` defined in the proof of Lemma 7.4.4. We append a subscript 0 to distinguish it from the section variable.
Previous English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\times X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume $X$ carries a `ProofData a q K σ₁ σ₂ F G` structure (by its docstring, the data common through most of chapters 2–7 of the blueprint). Among other things this structure provides a doubling measure on $X$ with constant $2^a$, whose measure we denote by $\mu$ (the measure `volume`); a type $\Theta(X)$ of continuous functions $X\to\mathbb R$ (from the compatible-functions structure it carries); and a simple function $Q:X\to\Theta(X)$. Write $D=2^{\mathfrak c\,a^2}\in\mathbb N$ (`defaultD a`, where $\mathfrak c$ is the fixed natural-number constant `𝕔` of the project), $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`), $o\in X$ for `cancelPt X` (a chosen point at which every function in $\Theta(X)$ vanishes), and $S\in\mathbb N$ for `defaultS X`, the least natural number $m>0$ such that $-m\le\sigma_1(y)$ and $\sigma_2(y)\le m$ for all $y\in X$ and $F\cup G\subseteq B(o,D^m/4)$. Assume $X$ carries a tile structure `TileStructure Q D κ S o`. This provides a finite type $\mathrm{Grid}(X)$ of (dyadic) cubes, each cube $I$ having an underlying set $I\subseteq X$, a scale $s(I)\in\mathbb Z$ and a center $c(I)\in X$, with the partial order $I\le J$ iff ($I\subseteq J$ as sets and $s(I)\le s(J)$); and a finite type $\mathfrak P(X)$ of tiles, each tile $p$ having a cube $\mathcal I(p)\in\mathrm{Grid}(X)$, scale $\mathfrak s(p)=s(\mathcal I(p))$, an element $\mathcal Q(p)\in\Theta(X)$ and a set $\Omega(p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (a term of `Forest X n`). It has a set $\mathfrak U(t)\subseteq\mathfrak P(X)$ of tiles (and $u\in t$ means $u\in\mathfrak U(t)$) and a map $\mathfrak T_t$ assigning to each tile $v\in\mathfrak P(X)$ a set of tiles $\mathfrak T_t(v)\subseteq\mathfrak P(X)$ (the field `𝔗`; by its docstring its value at $u$ only matters when $u\in\mathfrak U(t)$). For tiles $u_1,u_2\in\mathfrak P(X)$, this defines a set of tiles $\mathfrak S_0(t,u_1,u_2)\subseteq\mathfrak P(X)$ (`t.𝔖₀ u₁ u₂`). By its docstring, it is the set $\mathfrak S$ defined in the proof of Lemma 7.4.4, with a subscript $0$ appended to distinguish it from the section variable.
Checker's issue: Calls Grid(X) a finite type, which the prompt does not support (only the tile type has a finiteness instance).

### `TileStructure.Forest.overlap_implies_distance`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hp : p ∈ (fun x => t.𝔗 x) u₁ ∪ (fun x => t.𝔗 x) u₂) (hpu₁ : ¬Disjoint ↑(𝓘 p) ↑(𝓘 u₁)) : p ∈ t.𝔖₀ u₁ u₂`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u₁ u₂ p : 𝔓 X}, u₁ ∈ t → u₂ ∈ t → u₁ ≠ u₂ → 𝓘 u₁ ≤ 𝓘 u₂ → Membership.mem (γ := Set (𝔓 X)) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₁ ∪ (fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₂) p → ¬Disjoint ↑(𝓘 p) ↑(𝓘 u₁) → p ∈ t.𝔖₀ (F := F) (G := G) u₁ u₂`
Docstring: Part 1 of Lemma 7.4.7.
Previous English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\times X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume $X$ carries a `ProofData a q K σ₁ σ₂ F G` structure (by its docstring, the data common through most of chapters 2–7 of the blueprint). Among other things this structure provides a doubling measure on $X$ with constant $2^a$, whose measure we denote by $\mu$ (the measure `volume`); a type $\Theta(X)$ of continuous functions $X\to\mathbb R$ (from the compatible-functions structure it carries); and a simple function $Q:X\to\Theta(X)$. Write $D=2^{\mathfrak c\,a^2}\in\mathbb N$ (`defaultD a`, where $\mathfrak c$ is the fixed natural-number constant `𝕔` of the project), $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`), $o\in X$ for `cancelPt X` (a chosen point at which every function in $\Theta(X)$ vanishes), and $S\in\mathbb N$ for `defaultS X`, the least natural number $m>0$ such that $-m\le\sigma_1(y)$ and $\sigma_2(y)\le m$ for all $y\in X$ and $F\cup G\subseteq B(o,D^m/4)$. Assume $X$ carries a tile structure `TileStructure Q D κ S o`. This provides a finite type $\mathrm{Grid}(X)$ of (dyadic) cubes, each cube $I$ having an underlying set $I\subseteq X$, a scale $s(I)\in\mathbb Z$ and a center $c(I)\in X$, with the partial order $I\le J$ iff ($I\subseteq J$ as sets and $s(I)\le s(J)$); and a finite type $\mathfrak P(X)$ of tiles, each tile $p$ having a cube $\mathcal I(p)\in\mathrm{Grid}(X)$, scale $\mathfrak s(p)=s(\mathcal I(p))$, an element $\mathcal Q(p)\in\Theta(X)$ and a set $\Omega(p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (a term of `Forest X n`). It has a set $\mathfrak U(t)\subseteq\mathfrak P(X)$ of tiles (and $u\in t$ means $u\in\mathfrak U(t)$) and a map $\mathfrak T_t$ assigning to each tile $v\in\mathfrak P(X)$ a set of tiles $\mathfrak T_t(v)\subseteq\mathfrak P(X)$ (the field `𝔗`; by its docstring its value at $u$ only matters when $u\in\mathfrak U(t)$). Let $\mathfrak S_0(t,u_1,u_2)\subseteq\mathfrak P(X)$ denote the project's set `t.𝔖₀ u₁ u₂` (by its docstring, the set $\mathfrak S$ of the proof of Lemma 7.4.4). (Part 1 of Lemma 7.4.7.) Let $u_1,u_2,p\in\mathfrak P(X)$ with $u_1\in t$, $u_2\in t$, $u_1\neq u_2$ and $\mathcal I(u_1)\le\mathcal I(u_2)$ in $\mathrm{Grid}(X)$. Suppose $p\in\mathfrak T_t(u_1)\cup\mathfrak T_t(u_2)$, where $\mathfrak T_t(u_j)$ is the value of the forest's map at $u_j$ (`t.𝔗 u_j`), and that the underlying sets of $\mathcal I(p)$ and $\mathcal I(u_1)$ are not disjoint. Then $p\in\mathfrak S_0(t,u_1,u_2)$.
Checker's issue: Calls Grid(X) a finite type, which the prompt does not support (only the tile type has a finiteness instance).

### `TileStructure.Forest.adjoint_density_tree_bound2`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (h2f : Function.support f ⊆ F) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) * f x‖ₑ ≤ ↑(Forest.C7_3_1_2 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * dens₂ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u : 𝔓 X} {f g : X → ℂ}, BoundedCompactSupport f volume → Function.support f ⊆ F → BoundedCompactSupport g volume → Function.support g ⊆ G → u ∈ t → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (α := ℂ) ((starRingEnd ℂ) (adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) g x) : ℂ) (f x)) ≤ ↑(Forest.C7_3_1_2 a) * dens₁ (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) ^ (2 : ℝ)⁻¹ * dens₂ (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) ^ (2 : ℝ)⁻¹ * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (2 : ENNReal) volume * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace g (2 : ENNReal) volume`
Previous English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\times X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume $X$ carries a `ProofData a q K σ₁ σ₂ F G` structure (by its docstring, the data common through most of chapters 2–7 of the blueprint). Among other things this structure provides a doubling measure on $X$ with constant $2^a$, whose measure we denote by $\mu$ (the measure `volume`); a type $\Theta(X)$ of continuous functions $X\to\mathbb R$ (from the compatible-functions structure it carries); and a simple function $Q:X\to\Theta(X)$. Write $D=2^{\mathfrak c\,a^2}\in\mathbb N$ (`defaultD a`, where $\mathfrak c$ is the fixed natural-number constant `𝕔` of the project), $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`), $o\in X$ for `cancelPt X` (a chosen point at which every function in $\Theta(X)$ vanishes), and $S\in\mathbb N$ for `defaultS X`, the least natural number $m>0$ such that $-m\le\sigma_1(y)$ and $\sigma_2(y)\le m$ for all $y\in X$ and $F\cup G\subseteq B(o,D^m/4)$. Assume $X$ carries a tile structure `TileStructure Q D κ S o`. This provides a finite type $\mathrm{Grid}(X)$ of (dyadic) cubes, each cube $I$ having an underlying set $I\subseteq X$, a scale $s(I)\in\mathbb Z$ and a center $c(I)\in X$, with the partial order $I\le J$ iff ($I\subseteq J$ as sets and $s(I)\le s(J)$); and a finite type $\mathfrak P(X)$ of tiles, each tile $p$ having a cube $\mathcal I(p)\in\mathrm{Grid}(X)$, scale $\mathfrak s(p)=s(\mathcal I(p))$, an element $\mathcal Q(p)\in\Theta(X)$ and a set $\Omega(p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (a term of `Forest X n`). It has a set $\mathfrak U(t)\subseteq\mathfrak P(X)$ of tiles (and $u\in t$ means $u\in\mathfrak U(t)$) and a map $\mathfrak T_t$ assigning to each tile $v\in\mathfrak P(X)$ a set of tiles $\mathfrak T_t(v)\subseteq\mathfrak P(X)$ (the field `𝔗`; by its docstring its value at $u$ only matters when $u\in\mathfrak U(t)$). For $i\in\mathbb Z$ and $w,y\in X$ let $K_i(w,y)=K(w,y)\,\psi\big(D^{-i}d(w,y)\big)$ (`Ks i w y`), where $\psi(r)=\max\big(0,\min(1,\,4Dr-1,\,2-4r)\big)$ for $r\in\mathbb R$. For a tile $p$ let $\mathsf E(p)=\{y\in X: y\in\mathcal I(p),\ Q(y)\in\Omega(p),\ \sigma_1(y)\le\mathfrak s(p)\le\sigma_2(y)\}$. For a tile $p$ and $h:X\to\mathbb C$ let $T_p^*h(z)=\int_{\mathsf E(p)}\overline{K_{\mathfrak s(p)}(y,z)}\,e^{i\,(Q(y)(y)-Q(y)(z))}\,h(y)\,d\mu(y)$ (`adjointCarleson`), and for $\mathfrak C\subseteq\mathfrak P(X)$ let $T_{\mathfrak C}^*h(z)=\sum_{p\in\mathfrak C}T_p^*h(z)$ (`adjointCarlesonSum`; by its docstring, $T_{\mathfrak C}^*$ as defined at the bottom of Section 7.4). For $\mathfrak C\subseteq\mathfrak P(X)$, $\mathrm{dens}_1(\mathfrak C)\in[0,\infty]$ is the project's density `dens₁`: the supremum over $p'\in\mathfrak C$ and real $l\ge2$ of $l^{-a}\sup\frac{\mu(\mathsf E_2(l,p))}{\mu(\mathcal I(p))}$, the inner supremum over tiles $p$ with $\mathcal I(p)\le\mathcal I(p'')$ for some $p''\in\mathfrak C$ and with `smul l p' ≤ smul l p` (the project's comparison $lp'\lesssim lp$ of the pairs `smul l p` $=(\mathcal I(p),\text{the ball of radius }l\text{ around }\mathcal Q(p)\text{ in }\Theta(X)\text{ for the function distance attached to }(c(\mathcal I(p)),D^{\mathfrak s(p)}/4))$), where $\mathsf E_2(l,p)\subseteq X$ is the project's set `E₂ l p` (the set attached to `smul l p`). For $\mathfrak C\subseteq\mathfrak P(X)$, $\mathrm{dens}_2(\mathfrak C)\in[0,\infty]$ is the project's density `dens₂`: $\mathrm{dens}_2(\mathfrak C)=\sup_{p\in\mathfrak C}\sup_{r\ge4D^{\mathfrak s(p)}}\frac{\mu(F\cap B(c(\mathcal I(p)),r))}{\mu(B(c(\mathcal I(p)),r))}$. Let $C_{7.3.1.2}(a)\in\mathbb R_{\ge0}$ be the project constant `Forest.C7_3_1_2 a` (by its docstring, of value $2^{282 a^3}$ in the blueprint). Let $u\in\mathfrak P(X)$ with $u\in t$, and write $\mathfrak T_t(u)\subseteq\mathfrak P(X)$ for the value of the forest's map $\mathfrak T_t$ at $u$ (`t.𝔗 u`). Let $f:X\to\mathbb C$ be bounded, measurable and compactly supported with respect to $\mu$ (`BoundedCompactSupport f volume`) with support contained in $F$. Let $g:X\to\mathbb C$ be bounded, measurable and compactly supported with respect to $\mu$ (`BoundedCompactSupport g volume`) with support contained in $G$. Then $$\Big\|\int_X\overline{T^*_{\mathfrak T_t(u)}g(x)}\,f(x)\,d\mu(x)\Big\|\le C_{7.3.1.2}(a)\,\mathrm{dens}_1(\mathfrak T_t(u))^{1/2}\,\mathrm{dens}_2(\mathfrak T_t(u))^{1/2}\,\|f\|_{L^2(\mu)}\,\|g\|_{L^2(\mu)},$$ where the left side is the extended norm in $[0,\infty]$ of the (Bochner) integral. Here $\|\cdot\|_{L^2(\mu)}\in[0,\infty]$ denotes the $L^2(\mu)$ (semi)norm `eLpNorm · 2 volume`, and all inequalities are in $[0,\infty]$.
Checker's issue: Calls Grid(X) a finite type, which the prompt does not support (only the tile type has a finiteness instance).

### `TileStructure.Forest.adjoint_density_tree_bound1`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : ‖∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) * f x‖ₑ ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u : 𝔓 X} {f g : X → ℂ}, BoundedCompactSupport f volume → BoundedCompactSupport g volume → Function.support g ⊆ G → u ∈ t → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (α := ℂ) ((starRingEnd ℂ) (adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) g x) : ℂ) (f x)) ≤ ↑(Forest.C7_3_1_1 a) * dens₁ (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) ^ (2 : ℝ)⁻¹ * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (2 : ENNReal) volume * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace g (2 : ENNReal) volume`
Previous English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\times X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume $X$ carries a `ProofData a q K σ₁ σ₂ F G` structure (by its docstring, the data common through most of chapters 2–7 of the blueprint). Among other things this structure provides a doubling measure on $X$ with constant $2^a$, whose measure we denote by $\mu$ (the measure `volume`); a type $\Theta(X)$ of continuous functions $X\to\mathbb R$ (from the compatible-functions structure it carries); and a simple function $Q:X\to\Theta(X)$. Write $D=2^{\mathfrak c\,a^2}\in\mathbb N$ (`defaultD a`, where $\mathfrak c$ is the fixed natural-number constant `𝕔` of the project), $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`), $o\in X$ for `cancelPt X` (a chosen point at which every function in $\Theta(X)$ vanishes), and $S\in\mathbb N$ for `defaultS X`, the least natural number $m>0$ such that $-m\le\sigma_1(y)$ and $\sigma_2(y)\le m$ for all $y\in X$ and $F\cup G\subseteq B(o,D^m/4)$. Assume $X$ carries a tile structure `TileStructure Q D κ S o`. This provides a finite type $\mathrm{Grid}(X)$ of (dyadic) cubes, each cube $I$ having an underlying set $I\subseteq X$, a scale $s(I)\in\mathbb Z$ and a center $c(I)\in X$, with the partial order $I\le J$ iff ($I\subseteq J$ as sets and $s(I)\le s(J)$); and a finite type $\mathfrak P(X)$ of tiles, each tile $p$ having a cube $\mathcal I(p)\in\mathrm{Grid}(X)$, scale $\mathfrak s(p)=s(\mathcal I(p))$, an element $\mathcal Q(p)\in\Theta(X)$ and a set $\Omega(p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (a term of `Forest X n`). It has a set $\mathfrak U(t)\subseteq\mathfrak P(X)$ of tiles (and $u\in t$ means $u\in\mathfrak U(t)$) and a map $\mathfrak T_t$ assigning to each tile $v\in\mathfrak P(X)$ a set of tiles $\mathfrak T_t(v)\subseteq\mathfrak P(X)$ (the field `𝔗`; by its docstring its value at $u$ only matters when $u\in\mathfrak U(t)$). For $i\in\mathbb Z$ and $w,y\in X$ let $K_i(w,y)=K(w,y)\,\psi\big(D^{-i}d(w,y)\big)$ (`Ks i w y`), where $\psi(r)=\max\big(0,\min(1,\,4Dr-1,\,2-4r)\big)$ for $r\in\mathbb R$. For a tile $p$ let $\mathsf E(p)=\{y\in X: y\in\mathcal I(p),\ Q(y)\in\Omega(p),\ \sigma_1(y)\le\mathfrak s(p)\le\sigma_2(y)\}$. For a tile $p$ and $h:X\to\mathbb C$ let $T_p^*h(z)=\int_{\mathsf E(p)}\overline{K_{\mathfrak s(p)}(y,z)}\,e^{i\,(Q(y)(y)-Q(y)(z))}\,h(y)\,d\mu(y)$ (`adjointCarleson`), and for $\mathfrak C\subseteq\mathfrak P(X)$ let $T_{\mathfrak C}^*h(z)=\sum_{p\in\mathfrak C}T_p^*h(z)$ (`adjointCarlesonSum`; by its docstring, $T_{\mathfrak C}^*$ as defined at the bottom of Section 7.4). For $\mathfrak C\subseteq\mathfrak P(X)$, $\mathrm{dens}_1(\mathfrak C)\in[0,\infty]$ is the project's density `dens₁`: the supremum over $p'\in\mathfrak C$ and real $l\ge2$ of $l^{-a}\sup\frac{\mu(\mathsf E_2(l,p))}{\mu(\mathcal I(p))}$, the inner supremum over tiles $p$ with $\mathcal I(p)\le\mathcal I(p'')$ for some $p''\in\mathfrak C$ and with `smul l p' ≤ smul l p` (the project's comparison $lp'\lesssim lp$ of the pairs `smul l p` $=(\mathcal I(p),\text{the ball of radius }l\text{ around }\mathcal Q(p)\text{ in }\Theta(X)\text{ for the function distance attached to }(c(\mathcal I(p)),D^{\mathfrak s(p)}/4))$), where $\mathsf E_2(l,p)\subseteq X$ is the project's set `E₂ l p` (the set attached to `smul l p`). Let $C_{7.3.1.1}(a)\in\mathbb R_{\ge0}$ be the project constant `Forest.C7_3_1_1 a` (by its docstring, of value $2^{181 a^3}$ in the blueprint). Let $u\in\mathfrak P(X)$ with $u\in t$, and write $\mathfrak T_t(u)\subseteq\mathfrak P(X)$ for the value of the forest's map $\mathfrak T_t$ at $u$ (`t.𝔗 u`). Let $f:X\to\mathbb C$ be bounded, measurable and compactly supported with respect to $\mu$ (`BoundedCompactSupport f volume`). Let $g:X\to\mathbb C$ be bounded, measurable and compactly supported with respect to $\mu$ (`BoundedCompactSupport g volume`) with support contained in $G$. Then $$\Big\|\int_X\overline{T^*_{\mathfrak T_t(u)}g(x)}\,f(x)\,d\mu(x)\Big\|\le C_{7.3.1.1}(a)\,\mathrm{dens}_1(\mathfrak T_t(u))^{1/2}\,\|f\|_{L^2(\mu)}\,\|g\|_{L^2(\mu)},$$ where the left side is the extended norm in $[0,\infty]$ of the (Bochner) integral. Here $\|\cdot\|_{L^2(\mu)}\in[0,\infty]$ denotes the $L^2(\mu)$ (semi)norm `eLpNorm · 2 volume`, and all inequalities are in $[0,\infty]$.
Checker's issue: Calls Grid(X) a finite type, which the prompt does not support (only the tile type has a finiteness instance).

### `TileStructure.Forest.adjoint_tree_estimate`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) (hu : u ∈ t) : eLpNorm (adjointCarlesonSum ((fun x => t.𝔗 x) u) g) 2 volume ≤ ↑(Forest.C7_3_1_1 a) * dens₁ ((fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u : 𝔓 X} {g : X → ℂ}, BoundedCompactSupport g volume → Function.support g ⊆ G → u ∈ t → @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace (adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) g) (2 : ENNReal) volume ≤ ↑(Forest.C7_3_1_1 a) * dens₁ (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) ^ (2 : ℝ)⁻¹ * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace g (2 : ENNReal) volume`
Docstring: Part 1 of Lemma 7.4.2.
Previous English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\times X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume $X$ carries a `ProofData a q K σ₁ σ₂ F G` structure (by its docstring, the data common through most of chapters 2–7 of the blueprint). Among other things this structure provides a doubling measure on $X$ with constant $2^a$, whose measure we denote by $\mu$ (the measure `volume`); a type $\Theta(X)$ of continuous functions $X\to\mathbb R$ (from the compatible-functions structure it carries); and a simple function $Q:X\to\Theta(X)$. Write $D=2^{\mathfrak c\,a^2}\in\mathbb N$ (`defaultD a`, where $\mathfrak c$ is the fixed natural-number constant `𝕔` of the project), $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`), $o\in X$ for `cancelPt X` (a chosen point at which every function in $\Theta(X)$ vanishes), and $S\in\mathbb N$ for `defaultS X`, the least natural number $m>0$ such that $-m\le\sigma_1(y)$ and $\sigma_2(y)\le m$ for all $y\in X$ and $F\cup G\subseteq B(o,D^m/4)$. Assume $X$ carries a tile structure `TileStructure Q D κ S o`. This provides a finite type $\mathrm{Grid}(X)$ of (dyadic) cubes, each cube $I$ having an underlying set $I\subseteq X$, a scale $s(I)\in\mathbb Z$ and a center $c(I)\in X$, with the partial order $I\le J$ iff ($I\subseteq J$ as sets and $s(I)\le s(J)$); and a finite type $\mathfrak P(X)$ of tiles, each tile $p$ having a cube $\mathcal I(p)\in\mathrm{Grid}(X)$, scale $\mathfrak s(p)=s(\mathcal I(p))$, an element $\mathcal Q(p)\in\Theta(X)$ and a set $\Omega(p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (a term of `Forest X n`). It has a set $\mathfrak U(t)\subseteq\mathfrak P(X)$ of tiles (and $u\in t$ means $u\in\mathfrak U(t)$) and a map $\mathfrak T_t$ assigning to each tile $v\in\mathfrak P(X)$ a set of tiles $\mathfrak T_t(v)\subseteq\mathfrak P(X)$ (the field `𝔗`; by its docstring its value at $u$ only matters when $u\in\mathfrak U(t)$). For $i\in\mathbb Z$ and $w,y\in X$ let $K_i(w,y)=K(w,y)\,\psi\big(D^{-i}d(w,y)\big)$ (`Ks i w y`), where $\psi(r)=\max\big(0,\min(1,\,4Dr-1,\,2-4r)\big)$ for $r\in\mathbb R$. For a tile $p$ let $\mathsf E(p)=\{y\in X: y\in\mathcal I(p),\ Q(y)\in\Omega(p),\ \sigma_1(y)\le\mathfrak s(p)\le\sigma_2(y)\}$. For a tile $p$ and $h:X\to\mathbb C$ let $T_p^*h(z)=\int_{\mathsf E(p)}\overline{K_{\mathfrak s(p)}(y,z)}\,e^{i\,(Q(y)(y)-Q(y)(z))}\,h(y)\,d\mu(y)$ (`adjointCarleson`), and for $\mathfrak C\subseteq\mathfrak P(X)$ let $T_{\mathfrak C}^*h(z)=\sum_{p\in\mathfrak C}T_p^*h(z)$ (`adjointCarlesonSum`; by its docstring, $T_{\mathfrak C}^*$ as defined at the bottom of Section 7.4). For $\mathfrak C\subseteq\mathfrak P(X)$, $\mathrm{dens}_1(\mathfrak C)\in[0,\infty]$ is the project's density `dens₁`: the supremum over $p'\in\mathfrak C$ and real $l\ge2$ of $l^{-a}\sup\frac{\mu(\mathsf E_2(l,p))}{\mu(\mathcal I(p))}$, the inner supremum over tiles $p$ with $\mathcal I(p)\le\mathcal I(p'')$ for some $p''\in\mathfrak C$ and with `smul l p' ≤ smul l p` (the project's comparison $lp'\lesssim lp$ of the pairs `smul l p` $=(\mathcal I(p),\text{the ball of radius }l\text{ around }\mathcal Q(p)\text{ in }\Theta(X)\text{ for the function distance attached to }(c(\mathcal I(p)),D^{\mathfrak s(p)}/4))$), where $\mathsf E_2(l,p)\subseteq X$ is the project's set `E₂ l p` (the set attached to `smul l p`). Let $C_{7.3.1.1}(a)\in\mathbb R_{\ge0}$ be the project constant `Forest.C7_3_1_1 a` (by its docstring, of value $2^{181 a^3}$ in the blueprint). Let $u\in\mathfrak P(X)$ with $u\in t$, and write $\mathfrak T_t(u)\subseteq\mathfrak P(X)$ for the value of the forest's map $\mathfrak T_t$ at $u$ (`t.𝔗 u`). Let $g:X\to\mathbb C$ be bounded, measurable and compactly supported with respect to $\mu$ (`BoundedCompactSupport g volume`) with support contained in $G$. (Part 1 of Lemma 7.4.2.) Then $$\big\|T^*_{\mathfrak T_t(u)}g\big\|_{L^2(\mu)}\le C_{7.3.1.1}(a)\,\mathrm{dens}_1(\mathfrak T_t(u))^{1/2}\,\|g\|_{L^2(\mu)}.$$ Here $\|\cdot\|_{L^2(\mu)}\in[0,\infty]$ denotes the $L^2(\mu)$ (semi)norm `eLpNorm · 2 volume`, and all inequalities are in $[0,\infty]$.
Checker's issue: Calls Grid(X) a finite type, which the prompt does not support (only the tile type has a finiteness instance).
