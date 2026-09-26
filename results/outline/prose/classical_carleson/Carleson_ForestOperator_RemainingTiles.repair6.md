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

#### `Grid` (def)
Lean: `(X : Type u) → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [GridStructure X D κ S o] → Type u`
Docstring: The indexing type of the grid structure. Elements are called (dyadic) cubes. Note that this type has instances for both `≤` and `⊆`, but they do *not* coincide.
Definition: `fun (X : Type u) {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => @GridStructure.Grid X _ inst inst_1 _ _ _ _ _`

#### `GridStructure.coeGrid` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → Set X`
Docstring: The collection of dyadic cubes
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.3`

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

#### `PreTileStructure.toGridStructure` (def)
Lean: `(𝕜 : Type u_1) → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → GridStructure.{u_2, u} X D κ S o`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.1`

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

#### `TileStructure.Forest.C7_4_6` (def)
Lean: `ℕ → ℕ → NNReal`
Docstring: The constant used in `correlation_near_tree_parts`. Has value `2 ^ (232 * a ^ 3 + 21 * a + 5- 25/(101a) * Z n κ)` in the blueprint.
Definition: `Forest.wrapped✝.1`

#### `TileStructure.Forest.adjointBoundaryOperator` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → 𝔓 X → (X → ℂ) → X → ENNReal`
Docstring: The operator `S_{2,𝔲} f(x)`, given above Lemma 7.4.3.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (t : Forest X (F := F) (G := G) n) (u : 𝔓 X) (f : X → ℂ) (x : X) => ‖adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) f x‖ₑ + maximalFunction volume (Forest.𝓑 (F := F) (G := G)) (Forest.c𝓑 (F := F) (G := G)) (Forest.r𝓑 (F := F) (G := G)) (1 : ℝ) f x + ‖f x‖ₑ`

#### `TileStructure.Forest.instMembership𝔓Real` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Membership (𝔓 X) (Forest X (F := F) (G := G) n)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} => { mem := fun (t : Forest X (F := F) (G := G) n) (x : 𝔓 X) => x ∈ t.𝔘 (F := F) (G := G) }`

#### `TileStructure.Forest.𝔖₀` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → 𝔓 X → 𝔓 X → Set (𝔓 X)`
Docstring: The set `𝔖` defined in the proof of Lemma 7.4.4. We append a subscript 0 to distinguish it from the section variable.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (t : Forest X (F := F) (G := G) n) (u₁ u₂ : 𝔓 X) => {p : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₁ ∪ (fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₂) p ∧ (2 : ℝ) ^ (HMul.hMul (α := ℝ) ↑(defaultZ a) ↑n / (2 : ℝ)) ≤ dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 u₁) (𝒬 u₂)}`

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

#### `instPartialOrderGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → PartialOrder (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => PartialOrder.lift (fun (i : @GridStructure.Grid X _ inst inst_1 _ _ _ _ _) => (↑i, GridStructure.s i)) ⋯`

#### `𝓘` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → Grid X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] => PreTileStructure.𝓘`

#### `𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → (X : Type u) → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [PreTileStructure.{u, u_1, u_2} Q D κ S o] → Type u`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] (X : Type u) {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X`

#### `TileStructure.Forest.𝓙` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → Set (Grid X)`
Docstring: The definition of `𝓙(𝔖), defined above Lemma 7.1.2
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔖 : Set (𝔓 X)) => {x : Grid X | Maximal (fun (x : Grid X) => x ∈ Forest.𝓙₀ (F := F) (G := G) 𝔖) x}`

#### `TileStructure.Forest.C7_6_3` (def)
Lean: `ℕ → ℕ → ℝ`
Docstring: The constant used in `thin_scale_impact`. This is denoted `s₁` in the proof of Lemma 7.6.3. Has value `Z * n / (202 * a ^ 3) - 2` in the blueprint.
Definition: `Forest.wrapped✝.1`

#### `c` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Grid X → X`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.c`

#### `s` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Grid X → ℤ`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.s`

#### `𝔠` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => c (𝓘 p)`

#### `𝔰` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → ℤ`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => s (𝓘 p)`

#### `defaultZ` (def)
Lean: `ℕ → ℕ`
Docstring: The constant `Z` from (2.0.3).
Definition: `fun (a : ℕ) => (2 : ℕ) ^ ((12 : ℕ) * a)`

#### `𝕔` (def)
Lean: `ℕ`
Docstring: The main constant in the blueprint, driving all the construction, is `D = 2 ^ (100 * a ^ 2)`. It turns out that the proof is robust, and works for other values of `100`, giving better constants in the end. We will formalize it using a parameter `𝕔` (that we fix equal to `100` to follow the blueprint) and having `D = 2 ^ (𝕔 * a ^ 2)`. We register two lemmas `seven_le_c` and `c_le_100` and will never unfold `𝕔` from this point on.
Definition: `wrapped✝.1`

#### `TileStructure.Forest.approxOnCube` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {E' : Type u_2} → [inst_3 : NormedAddCommGroup E'] → [NormedSpace ℝ E'] → Set (Grid X) → (X → E') → X → E'`
Docstring: The projection operator `P_𝓒 f(x)`, given above Lemma 7.1.3. In lemmas the `c` will be pairwise disjoint on `C`.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {E' : Type u_2} [NormedAddCommGroup E'] [NormedSpace ℝ E'] (C : Set (Grid X)) (f : X → E') (x : X) => ∑ J : Grid X with J ∈ C, (↑J).indicator (fun (x : X) => ⨍ (y : X) in ↑J, f y) x`

#### `adjointCarleson` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
Docstring: The definition of `Tₚ*g(x)`, defined above Lemma 7.4.1
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume (E (F := F) (G := G) p)) fun (y : X) => HMul.hMul (α := ℂ) ((starRingEnd ℂ) (Ks (𝔰 p) y x) : ℂ) (Complex.exp (Complex.I * (↑(((Q (F := F) (G := G)) y : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y) - ↑(((Q (F := F) (G := G)) y : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) x)))) * f y`

#### `instFintypeGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Fintype (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.fintype_Grid`

#### `instFintype𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (𝔓.{u, u_1, u_2} X)`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.fintype_𝔓`

#### `C2_1_3` (def)
Lean: `ℕ → NNReal`
Docstring: The constant appearing in part 2 of Lemma 2.1.3. Equal to `2 ^ (102 * a ^ 3)` in the blueprint.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ ((𝕔 + (2 : ℕ)) * a ^ (3 : ℕ))`

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

#### `TileStructure.Forest.C7_6_2` (def)
Lean: `ℕ → ℕ → NNReal`
Docstring: The constant used in `bound_for_tree_projection`.
Definition: `Forest.wrapped✝.1`

#### `CompatibleFunctions` (structure or class)
Lean: `(𝕜 : outParam (Type u_3)) → (X : Type u) → outParam ℕ → [RCLike 𝕜] → [PseudoMetricSpace X] → Type (max (u + 1) u_3)`
Docstring: A set `Θ` of (continuous) functions is compatible. `A` will usually be `2 ^ a`.
Fields: `o`, `f`, `0`, `2`

#### `FunctionDistances` (structure or class)
Lean: `(𝕜 : outParam (Type u_1)) → (X : Type u) → [NormedField 𝕜] → [TopologicalSpace X] → Type (max (u + 1) u_1)`
Docstring: A class stating that continuous functions have distances associated to every ball. We use a separate type to conveniently index these functions.
Fields: `Θ`, `coeΘ`, `x`, `α`

#### `GridStructure` (structure or class)
Lean: `(X : Type u_2) → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [DoublingMeasure X A] → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (max (u + 1) u_2)`
Docstring: A grid structure on `X`. We prefer `coeGrid : Grid → Set X` over `Grid : Set (Set X)` Note: the `s` in this paper is `-s` of Christ's paper.
Fields: `Grid`, `coeGrid`, `s`, `c`, `β`, `i`, `topCube`, `α`, `4`, `m`, `2`

#### `GridStructure.Grid` (def)
Lean: `(X : Type u_2) → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → Type u`
Docstring: indexing set for a grid structure
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.1`

#### `MeasureTheory.DoublingMeasure` (structure or class)
Lean: `(X : Type u_3) → outParam NNReal → [PseudoMetricSpace X] → Type u_3`
Docstring: A metric space with a measure with some nice properties, including a doubling condition. This is called a "doubling metric measure space" in the blueprint. `A` will usually be `2 ^ a`.
Fields: `α`, `m0`, `X`, `R`

#### `KernelProofData` (structure or class)
Lean: `{X : Type u_1} → outParam ℕ → outParam (X → X → ℂ) → [PseudoMetricSpace X] → Type (u_1 + 1)`
Docstring: Data common through most of chapters 2 through 7. These contain the minimal axioms for `kernel-summand`'s proof. This is used in Chapter 3 when we don't have all other fields from `ProofData`.
Fields: `d`, `4`

#### `FunctionDistances.Θ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → (X : Type u) → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → Type u`
Docstring: A type of continuous functions from `X` to `𝕜`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.1`

#### `PreTileStructure` (structure or class)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : outParam NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → [inst_3 : FunctionDistances 𝕜 X] → outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)) → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (max (u + 1) (u_2 + 1))`
Fields: `𝔓`, `𝓘`, `𝒬`, `ι`

#### `C_Ts` (def)
Lean: `ℕ → NNReal`
Docstring: A constant used on the boundedness of `T_Q^θ` and `T_*`. We generally assume `HasBoundedStrongType (linearizedNontangentialOperator Q θ K · ·) 2 2 volume volume (C_Ts a)` throughout this formalization.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ a ^ (3 : ℕ)`

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

#### `PreTileStructure.𝒬` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X → @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.6`

#### `PreTileStructure.𝓘` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X → @GridStructure.Grid X _ inst_1 inst_2 _ _ _ _ _`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.4`

#### `PreTileStructure.𝔓` (def)
Lean: `(𝕜 : Type u_1) → {inst : RCLike 𝕜} → (X : Type u) → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Type u`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.2`

#### `WithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → X → ℝ → Type u_2`
Docstring: Class used to endow `Θ X` with a pseudometric space structure.
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] (x : X) (r : ℝ) => @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`

#### `instPseudoMetricSpaceWithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → {x : X} → {r : ℝ} → PseudoMetricSpace (WithFunctionDistance x r)`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] {x : X} {r : ℝ} => FunctionDistances.metric x r`

#### `TileStructure.Ω` (def)
Lean: `{X : Type u} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {inst_2 : FunctionDistances ℝ X} → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : TileStructure Q D κ S o] → PreTileStructure.𝔓 ℝ X → Set (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _)`
Definition: `fun (X : Type u) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {inst_2 : FunctionDistances ℝ X} {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : TileStructure Q D κ S o] => self.2`

#### `TileLike` (def)
Lean: `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Type u_1`
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => Grid X × (Set (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))ᵒᵈ`

#### `dens₁` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ENNReal`
Docstring: This density is defined to live in `ℝ≥0∞`. Use `ENNReal.toReal` to get a real number.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔓' : Set (𝔓 X)) => ⨆ p' ∈ 𝔓', ⨆ (l : NNReal), ⨆ (_ : l ≥ (2 : NNReal)), HPow.hPow (β := ℝ) (↑l) (-↑a) * ⨆ p ∈ lowerCubes (F := F) (G := G) 𝔓', ⨆ (_ : smul (F := F) (G := G) (↑l) p' ≤ smul (F := F) (G := G) (↑l) p), HDiv.hDiv (α := ENNReal) (β := ENNReal) ((volume : Measure X) (E₂ (F := F) (G := G) (↑l) p) : ENNReal) ((volume : Measure X) ↑(𝓘 p) : ENNReal)`

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

#### `FunctionDistances.coeΘ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → @Θ _ X inst inst_1 _ → C(X, 𝕜)`
Docstring: The coercion map from `Θ` to `C(X, 𝕜)`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.2`

#### `GridStructure.s` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → ℤ`
Docstring: scale functions
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.4`

#### `TileStructure.Forest.𝓙₀` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → Set (Grid X)`
Docstring: The definition of `𝓙₀(𝔖), defined above Lemma 7.1.2
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔖 : Set (𝔓 X)) => {J : Grid X | s J = -↑(defaultS X (F := F) (G := G)) ∨ ∀ p ∈ 𝔖, ¬↑(𝓘 p) ⊆ Metric.ball (c J) ((100 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (s J + (1 : ℤ)))}`

#### `GridStructure.c` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → X`
Docstring: Center functions
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.5`

#### `E` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → Set X`
Docstring: The set `E` defined in Proposition 2.0.2.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) => {x : X | x ∈ 𝓘 p ∧ Membership.mem (α := @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) (Ω p) ((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) ∧ 𝔰 p ∈ Set.Icc (σ₁ x) (σ₂ x)}`

#### `Ks` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {K : X → X → ℂ} → [inst : PseudoMetricSpace X] → [KernelProofData a K] → ℤ → X → X → ℂ`
Docstring: K_s in the blueprint
Definition: `fun {X : Type u_1} {a : ℕ} {K : X → X → ℂ} [PseudoMetricSpace X] [KernelProofData a K] (s : ℤ) (x y : X) => K x y * ↑(ψ (defaultD a) (HPow.hPow (α := ℝ) (↑(defaultD a)) (-s) * dist x y))`

#### `instFunLikeΘ` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → FunLike (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) X 𝕜`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] => DFunLike.mk (β := fun (x : X) => 𝕜) (fun (f : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) => ⇑(coeΘ f)) ⋯`

#### `GridStructure.fintype_Grid` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → Fintype (@GridStructure.Grid X _ inst inst_1 _ _ _ _ _)`
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.2`

#### `PreTileStructure.fintype_𝔓` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X)`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.3`

#### `ψ` (def)
Lean: `ℕ → ℝ → ℝ`
Docstring: The function `ψ` used as a basis for a dyadic partition of unity.
Definition: `fun (D : ℕ) (x : ℝ) => max (0 : ℝ) (min (1 : ℝ) (min ((4 : ℝ) * ↑D * x - (1 : ℝ)) ((2 : ℝ) - (4 : ℝ) * x)))`

## Flagged translations

### `TileStructure.Forest.correlation_near_tree_parts`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf₁ : BoundedCompactSupport f₁ volume) (hf₂ : BoundedCompactSupport f₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁) f₁ x * (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) f₂ x)‖ₑ ≤ ↑(Forest.C7_4_6 a n) * eLpNorm (fun x => (↑(𝓘 u₁)).indicator (t.adjointBoundaryOperator u₁ f₁) x) 2 volume * eLpNorm (fun x => (↑(𝓘 u₁)).indicator (t.adjointBoundaryOperator u₂ f₂) x) 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u₁ u₂ : 𝔓 X} {f₁ f₂ : X → ℂ}, u₁ ∈ t → u₂ ∈ t → u₁ ≠ u₂ → 𝓘 u₁ ≤ 𝓘 u₂ → BoundedCompactSupport f₁ volume → BoundedCompactSupport f₂ volume → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (β := ℂ) (adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₁) f₁ x) ((starRingEnd ℂ) (adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₂ \ t.𝔖₀ (F := F) (G := G) u₁ u₂) f₂ x) : ℂ)) ≤ ↑(Forest.C7_4_6 a n) * @eLpNorm _ ENNReal _ MeasureSpace.toMeasurableSpace (fun (x : X) => (↑(𝓘 u₁)).indicator (t.adjointBoundaryOperator (F := F) (G := G) u₁ f₁) x) (2 : ENNReal) volume * @eLpNorm _ ENNReal _ MeasureSpace.toMeasurableSpace (fun (x : X) => (↑(𝓘 u₁)).indicator (t.adjointBoundaryOperator (F := F) (G := G) u₂ f₂) x) (2 : ENNReal) volume`
Docstring: Lemma 7.4.6
Previous English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume given an instance of the project structure `ProofData` $a\,q\,K\,\sigma_1\,\sigma_2\,F\,G$ on $X$ (per its docstring, the data common through most of chapters 2–7). Through its `KernelProofData` component this provides a `DoublingMeasure` $X\,(2^a)$ structure on $X$ (per its docstring, a measure with nice properties including a doubling condition), whose measure we write $\mu$ (Lean's `volume`), and a `CompatibleFunctions` $\mathbb R\,X\,(2^a)$ structure, hence a `FunctionDistances` $\mathbb R\,X$ structure, which gives a type $\Theta(X)$ of functions $X\to\mathbb R$ (per its docstring, continuous functions) and, for each $x\in X$ and $r\in\mathbb R$, a pseudometric $d_{x,r}$ on $\Theta(X)$. Let $Q : X\to\Theta(X)$ be the simple function given by the field `ProofData.Q`. Put $D=2^{𝕔 a^2}\in\mathbb N$ (`defaultD a`), where $𝕔\in\mathbb N$ is the project constant `𝕔` (per its docstring, fixed equal to $100$); $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`); $Z=2^{12a}\in\mathbb N$ (`defaultZ a`); $o\in X$ the point `cancelPt X`, chosen so that every element of $\Theta(X)$ vanishes at $o$; and $S\in\mathbb N$ (`defaultS X`) the least natural number $m>0$ such that $-m\le\sigma_1(x)$ and $\sigma_2(x)\le m$ for all $x\in X$ and $F\cup G\subseteq B(o,D^m/4)$. Assume given a tile structure `TileStructure` $Q\,D\,\kappa\,S\,o$ on $X$. Write $\mathfrak P$ for its finite type of tiles and $\mathrm{Grid}(X)$ for its finite type of dyadic cubes; we identify a cube $J$ with its underlying subset of $X$, write $c(J)\in X$ for its center and $s(J)\in\mathbb Z$ for its scale, and order cubes by $J\le J'$ iff $J\subseteq J'$ and $s(J)\le s(J')$ (so $J<J'$ means $J\le J'$ and $J\ne J'$). Each tile $\mathfrak p\in\mathfrak P$ has a cube $\mathcal I(\mathfrak p)\in\mathrm{Grid}(X)$, with $c(\mathfrak p):=c(\mathcal I(\mathfrak p))$ and $s(\mathfrak p):=s(\mathcal I(\mathfrak p))$, an element $\mathcal Q(\mathfrak p)\in\Theta(X)$ and a set $\Omega(\mathfrak p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (`Forest` $X\,n$); it has a set of tiles $\mathfrak U(t)\subseteq\mathfrak P$ (we write $u\in t$ for $u\in\mathfrak U(t)$) and assigns to each tile $u$ a set of tiles $\mathfrak T(u)\subseteq\mathfrak P$. For tiles $u_1,u_2$ let $\mathfrak S_0(u_1,u_2)=\{\mathfrak p\in\mathfrak T(u_1)\cup\mathfrak T(u_2) : 2^{Zn/2}\le d_{c(\mathfrak p),\,D^{s(\mathfrak p)}/4}(\mathcal Q(u_1),\mathcal Q(u_2))\}$ (`t.𝔖₀ u₁ u₂`). For a tile $\mathfrak p$, a function $g:X\to\mathbb C$ and $x\in X$ let $T^*_{\mathfrak p}g(x)=\int_{E(\mathfrak p)}\overline{K_{s(\mathfrak p)}(y,x)}\,e^{i(Q(y)(y)-Q(y)(x))}\,g(y)\,d\mu(y)$ (`adjointCarleson`), where $E(\mathfrak p)=\{y\in\mathcal I(\mathfrak p) : Q(y)\in\Omega(\mathfrak p),\ \sigma_1(y)\le s(\mathfrak p)\le\sigma_2(y)\}$, $K_s(x,y)=K(x,y)\,\psi(D^{-s}d(x,y))$ for $s\in\mathbb Z$, and $\psi(r)=\max(0,\min(1,4Dr-1,2-4r))$ for $r\in\mathbb R$; and for a set of tiles $\mathfrak C$ let $T^*_{\mathfrak C}g(x)=\sum_{\mathfrak p\in\mathfrak C}T^*_{\mathfrak p}g(x)$ (`adjointCarlesonSum`). For $g:X\to\mathbb C$ and $x\in X$ let $Mg(x)=\sup\{\,\frac{1}{\mu(B_{k,l,J})}\int_{B_{k,l,J}}|g|\,d\mu : k,l\in\mathbb N,\ k\le S+5,\ l\le 2S+3,\ J\in\mathrm{Grid}(X),\ x\in B_{k,l,J}\}\in[0,\infty]$ (the supremum of the empty set being $0$), where $B_{k,l,J}$ is the open ball of center $c(J)$ and radius $2^kD^{s(J)+l}$; this is `maximalFunction volume 𝓑 c𝓑 r𝓑 1 g`, the uncentered Hardy–Littlewood maximal function over this family of balls with exponent $1$. For a tile $u$ let $S^*_u g(x)=|T^*_{\mathfrak T(u)}g(x)|+Mg(x)+|g(x)|\in[0,\infty]$ (`t.adjointBoundaryOperator u g x`). Let $C_{7.4.6}(a,n)\in\mathbb R_{\ge0}$ be the project constant `Forest.C7_4_6 a n` (per its docstring, of value $2^{232a^3+21a+5-\frac{25}{101a}Zn\kappa}$ in the blueprint). Here $\|\cdot\|_{L^2(\mu)}\in[0,\infty]$ is the (extended) $L^2$ norm with respect to $\mu$ (`eLpNorm · 2 volume`), and "bounded with compact support" means `BoundedCompactSupport` with respect to $\mu$ (per its docstring, bounded, compactly supported, measurable). (Lemma 7.4.6.) Let $u_1,u_2\in\mathfrak P$ with $u_1\in t$, $u_2\in t$, $u_1\ne u_2$ and $\mathcal I(u_1)\le\mathcal I(u_2)$, and let $f_1,f_2:X\to\mathbb C$ be bounded with compact support. Then $$\Big|\int_X T^*_{\mathfrak T(u_1)}f_1(x)\,\overline{T^*_{\mathfrak T(u_2)\setminus\mathfrak S_0(u_1,u_2)}f_2(x)}\,d\mu(x)\Big|\le C_{7.4.6}(a,n)\,\big\|\mathbf 1_{\mathcal I(u_1)}S^*_{u_1}f_1\big\|_{L^2(\mu)}\,\big\|\mathbf 1_{\mathcal I(u_1)}S^*_{u_2}f_2\big\|_{L^2(\mu)},$$ the inequality holding in $[0,\infty]$ (the left side is the extended norm of the Bochner integral).
Checker's issue: Calls Grid(X) a finite type, which the prompt does not support (only the tile type has a finiteness instance).

### `TileStructure.Forest.𝓙₆`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (t : Forest X n) (u₁ : 𝔓 X) : Set (Grid X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → 𝔓 X → Set (Grid X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (t : Forest X (F := F) (G := G) n) (u₁ : 𝔓 X) => Forest.𝓙 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₁) ∩ Set.Iic (𝓘 u₁)`
Docstring: The definition `𝓙'` at the start of Section 7.6. We use a different notation to distinguish it from the 𝓙' used in Section 7.5
Previous English: Definition. Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume given an instance of the project structure `ProofData` $a\,q\,K\,\sigma_1\,\sigma_2\,F\,G$ on $X$ (per its docstring, the data common through most of chapters 2–7). Through its `KernelProofData` component this provides a `DoublingMeasure` $X\,(2^a)$ structure on $X$ (per its docstring, a measure with nice properties including a doubling condition), whose measure we write $\mu$ (Lean's `volume`), and a `CompatibleFunctions` $\mathbb R\,X\,(2^a)$ structure, hence a `FunctionDistances` $\mathbb R\,X$ structure, which gives a type $\Theta(X)$ of functions $X\to\mathbb R$ (per its docstring, continuous functions) and, for each $x\in X$ and $r\in\mathbb R$, a pseudometric $d_{x,r}$ on $\Theta(X)$. Let $Q : X\to\Theta(X)$ be the simple function given by the field `ProofData.Q`. Put $D=2^{𝕔 a^2}\in\mathbb N$ (`defaultD a`), where $𝕔\in\mathbb N$ is the project constant `𝕔` (per its docstring, fixed equal to $100$); $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`); $Z=2^{12a}\in\mathbb N$ (`defaultZ a`); $o\in X$ the point `cancelPt X`, chosen so that every element of $\Theta(X)$ vanishes at $o$; and $S\in\mathbb N$ (`defaultS X`) the least natural number $m>0$ such that $-m\le\sigma_1(x)$ and $\sigma_2(x)\le m$ for all $x\in X$ and $F\cup G\subseteq B(o,D^m/4)$. Assume given a tile structure `TileStructure` $Q\,D\,\kappa\,S\,o$ on $X$. Write $\mathfrak P$ for its finite type of tiles and $\mathrm{Grid}(X)$ for its finite type of dyadic cubes; we identify a cube $J$ with its underlying subset of $X$, write $c(J)\in X$ for its center and $s(J)\in\mathbb Z$ for its scale, and order cubes by $J\le J'$ iff $J\subseteq J'$ and $s(J)\le s(J')$ (so $J<J'$ means $J\le J'$ and $J\ne J'$). Each tile $\mathfrak p\in\mathfrak P$ has a cube $\mathcal I(\mathfrak p)\in\mathrm{Grid}(X)$, with $c(\mathfrak p):=c(\mathcal I(\mathfrak p))$ and $s(\mathfrak p):=s(\mathcal I(\mathfrak p))$, an element $\mathcal Q(\mathfrak p)\in\Theta(X)$ and a set $\Omega(\mathfrak p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (`Forest` $X\,n$); it has a set of tiles $\mathfrak U(t)\subseteq\mathfrak P$ (we write $u\in t$ for $u\in\mathfrak U(t)$) and assigns to each tile $u$ a set of tiles $\mathfrak T(u)\subseteq\mathfrak P$. For a tile $u_1\in\mathfrak P$, `t.𝓙₆ u₁` is a set of cubes $\mathcal J_6(t,u_1)\subseteq\mathrm{Grid}(X)$. According to its docstring, it is the set $\mathcal J'$ defined at the start of Section 7.6, given a different name to distinguish it from the $\mathcal J'$ used in Section 7.5.
Checker's issue: Calls Grid(X) a finite type, which the prompt does not support (only the tile type has a finiteness instance).

### `TileStructure.Forest.thin_scale_impact_prelims`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu₁ : u₁ ∈ t) (hJ : J ∈ t.𝓙₆ u₁) (hd : ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (8 * ↑(defaultD a) ^ s J))) (h : ↑(s J) - Forest.C7_6_3 a n < ↑(𝔰 p)) : dist (𝔠 p) (c J) < 16 * ↑(defaultD a) ^ (↑(𝔰 p) + Forest.C7_6_3 a n + 2) ∧ ∃ J', J < J' ∧ s J' = s J + 1 ∧ ∃ p ∈ (fun x => t.𝔗 x) u₁, ↑(𝓘 p) ⊆ Metric.ball (c J') (100 * ↑(defaultD a) ^ (s J' + 1))`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u₁ p : 𝔓 X} {J : Grid X}, u₁ ∈ t → J ∈ t.𝓙₆ (F := F) (G := G) u₁ → ¬Disjoint (Metric.ball (𝔠 p) ((8 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p))) (Metric.ball (c J) ((8 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (s J))) → ↑(s J) - Forest.C7_6_3 a n < ↑(𝔰 p) → dist (𝔠 p) (c J) < (16 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (↑(𝔰 p) + Forest.C7_6_3 a n + (2 : ℝ)) ∧ ∃ (J' : Grid X), J < J' ∧ s J' = s J + (1 : ℤ) ∧ ∃ (p : 𝔓 X), Membership.mem (γ := Set (𝔓 X)) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₁) p ∧ ↑(𝓘 p) ⊆ Metric.ball (c J') ((100 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (s J' + (1 : ℤ)))`
Docstring: Some preliminary relations for Lemma 7.6.3.
Previous English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume given an instance of the project structure `ProofData` $a\,q\,K\,\sigma_1\,\sigma_2\,F\,G$ on $X$ (per its docstring, the data common through most of chapters 2–7). Through its `KernelProofData` component this provides a `DoublingMeasure` $X\,(2^a)$ structure on $X$ (per its docstring, a measure with nice properties including a doubling condition), whose measure we write $\mu$ (Lean's `volume`), and a `CompatibleFunctions` $\mathbb R\,X\,(2^a)$ structure, hence a `FunctionDistances` $\mathbb R\,X$ structure, which gives a type $\Theta(X)$ of functions $X\to\mathbb R$ (per its docstring, continuous functions) and, for each $x\in X$ and $r\in\mathbb R$, a pseudometric $d_{x,r}$ on $\Theta(X)$. Let $Q : X\to\Theta(X)$ be the simple function given by the field `ProofData.Q`. Put $D=2^{𝕔 a^2}\in\mathbb N$ (`defaultD a`), where $𝕔\in\mathbb N$ is the project constant `𝕔` (per its docstring, fixed equal to $100$); $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`); $Z=2^{12a}\in\mathbb N$ (`defaultZ a`); $o\in X$ the point `cancelPt X`, chosen so that every element of $\Theta(X)$ vanishes at $o$; and $S\in\mathbb N$ (`defaultS X`) the least natural number $m>0$ such that $-m\le\sigma_1(x)$ and $\sigma_2(x)\le m$ for all $x\in X$ and $F\cup G\subseteq B(o,D^m/4)$. Assume given a tile structure `TileStructure` $Q\,D\,\kappa\,S\,o$ on $X$. Write $\mathfrak P$ for its finite type of tiles and $\mathrm{Grid}(X)$ for its finite type of dyadic cubes; we identify a cube $J$ with its underlying subset of $X$, write $c(J)\in X$ for its center and $s(J)\in\mathbb Z$ for its scale, and order cubes by $J\le J'$ iff $J\subseteq J'$ and $s(J)\le s(J')$ (so $J<J'$ means $J\le J'$ and $J\ne J'$). Each tile $\mathfrak p\in\mathfrak P$ has a cube $\mathcal I(\mathfrak p)\in\mathrm{Grid}(X)$, with $c(\mathfrak p):=c(\mathcal I(\mathfrak p))$ and $s(\mathfrak p):=s(\mathcal I(\mathfrak p))$, an element $\mathcal Q(\mathfrak p)\in\Theta(X)$ and a set $\Omega(\mathfrak p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (`Forest` $X\,n$); it has a set of tiles $\mathfrak U(t)\subseteq\mathfrak P$ (we write $u\in t$ for $u\in\mathfrak U(t)$) and assigns to each tile $u$ a set of tiles $\mathfrak T(u)\subseteq\mathfrak P$. Let $C_{7.6.3}(a,n)\in\mathbb R$ be the project constant `Forest.C7_6_3 a n` (per its docstring, denoted $s_1$ in the proof of Lemma 7.6.3, with value $Zn/(202a^3)-2$ in the blueprint). Let $\mathcal J_6(u_1)\subseteq\mathrm{Grid}(X)$ denote the project set of cubes `t.𝓙₆ u₁` (per its docstring, the set $\mathcal J'$ at the start of Section 7.6). Let $u_1,\mathfrak p\in\mathfrak P$ with $u_1\in t$, and let $J\in\mathrm{Grid}(X)$ with $J\in\mathcal J_6(u_1)$. Suppose the open balls $B(c(\mathfrak p),8D^{s(\mathfrak p)})$ and $B(c(J),8D^{s(J)})$ are not disjoint, and that $s(J)-C_{7.6.3}(a,n)<s(\mathfrak p)$ (in $\mathbb R$). Then $d(c(\mathfrak p),c(J))<16\,D^{s(\mathfrak p)+C_{7.6.3}(a,n)+2}$ (real exponent), and there exist a cube $J'\in\mathrm{Grid}(X)$ with $J<J'$ and $s(J')=s(J)+1$, and a tile $\mathfrak p'\in\mathfrak T(u_1)$ such that $\mathcal I(\mathfrak p')\subseteq B(c(J'),100\,D^{s(J')+1})$.
Checker's issue: Calls Grid(X) a finite type, which the prompt does not support (only the tile type has a finiteness instance).

### `TileStructure.Forest.thin_scale_impact_key`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hp : p ∈ (fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) (hJ : J ∈ t.𝓙₆ u₁) (hd : ¬Disjoint (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) (Metric.ball (c J) (8 * ↑(defaultD a) ^ s J))) (h : ↑(s J) - Forest.C7_6_3 a n < ↑(𝔰 p)) : 2 ^ (defaultZ a * (n + 1) - 1) < 2 ^ (↑a * (↑𝕔 * ↑a ^ 2 * (Forest.C7_6_3 a n + 2 + 1) + 9)) * 2 ^ (↑(defaultZ a) * ↑n / 2)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u₁ u₂ p : 𝔓 X} {J : Grid X}, u₁ ∈ t → u₂ ∈ t → u₁ ≠ u₂ → 𝓘 u₁ ≤ 𝓘 u₂ → p ∈ (fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₂ \ t.𝔖₀ (F := F) (G := G) u₁ u₂ → J ∈ t.𝓙₆ (F := F) (G := G) u₁ → ¬Disjoint (Metric.ball (𝔠 p) ((8 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p))) (Metric.ball (c J) ((8 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (s J))) → ↑(s J) - Forest.C7_6_3 a n < ↑(𝔰 p) → (2 : ℝ) ^ (defaultZ a * (n + (1 : ℕ)) - (1 : ℕ)) < (2 : ℝ) ^ (↑a * (↑𝕔 * HPow.hPow (α := ℝ) ↑a (2 : ℕ) * (Forest.C7_6_3 a n + (2 : ℝ) + (1 : ℝ)) + (9 : ℝ))) * (2 : ℝ) ^ (HMul.hMul (α := ℝ) ↑(defaultZ a) ↑n / (2 : ℝ))`
Docstring: The key relation of Lemma 7.6.3, which will eventually be shown to lead to a contradiction.
Previous English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume given an instance of the project structure `ProofData` $a\,q\,K\,\sigma_1\,\sigma_2\,F\,G$ on $X$ (per its docstring, the data common through most of chapters 2–7). Through its `KernelProofData` component this provides a `DoublingMeasure` $X\,(2^a)$ structure on $X$ (per its docstring, a measure with nice properties including a doubling condition), whose measure we write $\mu$ (Lean's `volume`), and a `CompatibleFunctions` $\mathbb R\,X\,(2^a)$ structure, hence a `FunctionDistances` $\mathbb R\,X$ structure, which gives a type $\Theta(X)$ of functions $X\to\mathbb R$ (per its docstring, continuous functions) and, for each $x\in X$ and $r\in\mathbb R$, a pseudometric $d_{x,r}$ on $\Theta(X)$. Let $Q : X\to\Theta(X)$ be the simple function given by the field `ProofData.Q`. Put $D=2^{𝕔 a^2}\in\mathbb N$ (`defaultD a`), where $𝕔\in\mathbb N$ is the project constant `𝕔` (per its docstring, fixed equal to $100$); $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`); $Z=2^{12a}\in\mathbb N$ (`defaultZ a`); $o\in X$ the point `cancelPt X`, chosen so that every element of $\Theta(X)$ vanishes at $o$; and $S\in\mathbb N$ (`defaultS X`) the least natural number $m>0$ such that $-m\le\sigma_1(x)$ and $\sigma_2(x)\le m$ for all $x\in X$ and $F\cup G\subseteq B(o,D^m/4)$. Assume given a tile structure `TileStructure` $Q\,D\,\kappa\,S\,o$ on $X$. Write $\mathfrak P$ for its finite type of tiles and $\mathrm{Grid}(X)$ for its finite type of dyadic cubes; we identify a cube $J$ with its underlying subset of $X$, write $c(J)\in X$ for its center and $s(J)\in\mathbb Z$ for its scale, and order cubes by $J\le J'$ iff $J\subseteq J'$ and $s(J)\le s(J')$ (so $J<J'$ means $J\le J'$ and $J\ne J'$). Each tile $\mathfrak p\in\mathfrak P$ has a cube $\mathcal I(\mathfrak p)\in\mathrm{Grid}(X)$, with $c(\mathfrak p):=c(\mathcal I(\mathfrak p))$ and $s(\mathfrak p):=s(\mathcal I(\mathfrak p))$, an element $\mathcal Q(\mathfrak p)\in\Theta(X)$ and a set $\Omega(\mathfrak p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (`Forest` $X\,n$); it has a set of tiles $\mathfrak U(t)\subseteq\mathfrak P$ (we write $u\in t$ for $u\in\mathfrak U(t)$) and assigns to each tile $u$ a set of tiles $\mathfrak T(u)\subseteq\mathfrak P$. For tiles $u_1,u_2$ let $\mathfrak S_0(u_1,u_2)=\{\mathfrak p\in\mathfrak T(u_1)\cup\mathfrak T(u_2) : 2^{Zn/2}\le d_{c(\mathfrak p),\,D^{s(\mathfrak p)}/4}(\mathcal Q(u_1),\mathcal Q(u_2))\}$ (`t.𝔖₀ u₁ u₂`). Let $C_{7.6.3}(a,n)\in\mathbb R$ be the project constant `Forest.C7_6_3 a n` (per its docstring, denoted $s_1$ in the proof of Lemma 7.6.3, with value $Zn/(202a^3)-2$ in the blueprint). Let $\mathcal J_6(u_1)\subseteq\mathrm{Grid}(X)$ denote the project set of cubes `t.𝓙₆ u₁` (per its docstring, the set $\mathcal J'$ at the start of Section 7.6). Let $u_1,u_2,\mathfrak p\in\mathfrak P$ with $u_1\in t$, $u_2\in t$, $u_1\ne u_2$, $\mathcal I(u_1)\le\mathcal I(u_2)$ and $\mathfrak p\in\mathfrak T(u_2)\setminus\mathfrak S_0(u_1,u_2)$, and let $J\in\mathrm{Grid}(X)$ with $J\in\mathcal J_6(u_1)$. Suppose the open balls $B(c(\mathfrak p),8D^{s(\mathfrak p)})$ and $B(c(J),8D^{s(J)})$ are not disjoint, and that $s(J)-C_{7.6.3}(a,n)<s(\mathfrak p)$ (in $\mathbb R$). Then, in $\mathbb R$, $$2^{Z(n+1)-1}<2^{a\,(𝕔\,a^2\,(C_{7.6.3}(a,n)+2+1)+9)}\cdot 2^{Zn/2},$$ where the exponent $Z(n+1)-1$ is computed in $\mathbb N$ (truncated subtraction) and the other two exponents are real numbers. (Per its docstring, this is the key relation of Lemma 7.6.3, later shown to lead to a contradiction.)
Checker's issue: Calls Grid(X) a finite type, which the prompt does not support (only the tile type has a finiteness instance).

### `TileStructure.Forest.e763`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf : BoundedCompactSupport f volume) : eLpNorm (Forest.approxOnCube (t.𝓙₆ u₁) fun x => ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) f x‖) 2 volume ≤ ∑ k ∈ Finset.Icc ⌊Forest.C7_6_3 a n⌋ (2 * ↑(defaultS X)), (∑ J ∈ (t.𝓙₆ u₁).toFinset, (volume ↑J)⁻¹ * (∫⁻ (y : X) in ↑J, ∑ p ∈ ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂).toFinset with ¬Disjoint (↑J) (Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p)) ∧ 𝔰 p = s J - k, ‖adjointCarleson p f y‖ₑ) ^ 2) ^ 2⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u₁ u₂ : 𝔓 X} {f : X → ℂ}, u₁ ∈ t → u₂ ∈ t → u₁ ≠ u₂ → 𝓘 u₁ ≤ 𝓘 u₂ → BoundedCompactSupport f volume → @eLpNorm _ ℝ _ MeasureSpace.toMeasurableSpace (Forest.approxOnCube (F := F) (G := G) (t.𝓙₆ (F := F) (G := G) u₁) fun (x : X) => ‖adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₂ \ t.𝔖₀ (F := F) (G := G) u₁ u₂) f x‖) (2 : ENNReal) volume ≤ ∑ k ∈ Finset.Icc ⌊Forest.C7_6_3 a n⌋ ((2 : ℤ) * ↑(defaultS X (F := F) (G := G))), HPow.hPow (α := ENNReal) (∑ J ∈ (t.𝓙₆ (F := F) (G := G) u₁).toFinset, HMul.hMul (α := ENNReal) (((volume : Measure X) ↑J)⁻¹ : ENNReal) ((∫⁻ (y : X) in ↑J, ∑ p ∈ ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₂ \ t.𝔖₀ (F := F) (G := G) u₁ u₂).toFinset with ¬Disjoint (↑J) (Metric.ball (𝔠 p) ((8 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p))) ∧ 𝔰 p = s J - k, ‖adjointCarleson (F := F) (G := G) p f y‖ₑ) ^ (2 : ℕ))) (2 : ℝ)⁻¹`
Docstring: Equation (7.6.3) of Lemma 7.6.2.
Previous English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume given an instance of the project structure `ProofData` $a\,q\,K\,\sigma_1\,\sigma_2\,F\,G$ on $X$ (per its docstring, the data common through most of chapters 2–7). Through its `KernelProofData` component this provides a `DoublingMeasure` $X\,(2^a)$ structure on $X$ (per its docstring, a measure with nice properties including a doubling condition), whose measure we write $\mu$ (Lean's `volume`), and a `CompatibleFunctions` $\mathbb R\,X\,(2^a)$ structure, hence a `FunctionDistances` $\mathbb R\,X$ structure, which gives a type $\Theta(X)$ of functions $X\to\mathbb R$ (per its docstring, continuous functions) and, for each $x\in X$ and $r\in\mathbb R$, a pseudometric $d_{x,r}$ on $\Theta(X)$. Let $Q : X\to\Theta(X)$ be the simple function given by the field `ProofData.Q`. Put $D=2^{𝕔 a^2}\in\mathbb N$ (`defaultD a`), where $𝕔\in\mathbb N$ is the project constant `𝕔` (per its docstring, fixed equal to $100$); $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`); $Z=2^{12a}\in\mathbb N$ (`defaultZ a`); $o\in X$ the point `cancelPt X`, chosen so that every element of $\Theta(X)$ vanishes at $o$; and $S\in\mathbb N$ (`defaultS X`) the least natural number $m>0$ such that $-m\le\sigma_1(x)$ and $\sigma_2(x)\le m$ for all $x\in X$ and $F\cup G\subseteq B(o,D^m/4)$. Assume given a tile structure `TileStructure` $Q\,D\,\kappa\,S\,o$ on $X$. Write $\mathfrak P$ for its finite type of tiles and $\mathrm{Grid}(X)$ for its finite type of dyadic cubes; we identify a cube $J$ with its underlying subset of $X$, write $c(J)\in X$ for its center and $s(J)\in\mathbb Z$ for its scale, and order cubes by $J\le J'$ iff $J\subseteq J'$ and $s(J)\le s(J')$ (so $J<J'$ means $J\le J'$ and $J\ne J'$). Each tile $\mathfrak p\in\mathfrak P$ has a cube $\mathcal I(\mathfrak p)\in\mathrm{Grid}(X)$, with $c(\mathfrak p):=c(\mathcal I(\mathfrak p))$ and $s(\mathfrak p):=s(\mathcal I(\mathfrak p))$, an element $\mathcal Q(\mathfrak p)\in\Theta(X)$ and a set $\Omega(\mathfrak p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (`Forest` $X\,n$); it has a set of tiles $\mathfrak U(t)\subseteq\mathfrak P$ (we write $u\in t$ for $u\in\mathfrak U(t)$) and assigns to each tile $u$ a set of tiles $\mathfrak T(u)\subseteq\mathfrak P$. For tiles $u_1,u_2$ let $\mathfrak S_0(u_1,u_2)=\{\mathfrak p\in\mathfrak T(u_1)\cup\mathfrak T(u_2) : 2^{Zn/2}\le d_{c(\mathfrak p),\,D^{s(\mathfrak p)}/4}(\mathcal Q(u_1),\mathcal Q(u_2))\}$ (`t.𝔖₀ u₁ u₂`). For a tile $\mathfrak p$, a function $g:X\to\mathbb C$ and $x\in X$ let $T^*_{\mathfrak p}g(x)=\int_{E(\mathfrak p)}\overline{K_{s(\mathfrak p)}(y,x)}\,e^{i(Q(y)(y)-Q(y)(x))}\,g(y)\,d\mu(y)$ (`adjointCarleson`), where $E(\mathfrak p)=\{y\in\mathcal I(\mathfrak p) : Q(y)\in\Omega(\mathfrak p),\ \sigma_1(y)\le s(\mathfrak p)\le\sigma_2(y)\}$, $K_s(x,y)=K(x,y)\,\psi(D^{-s}d(x,y))$ for $s\in\mathbb Z$, and $\psi(r)=\max(0,\min(1,4Dr-1,2-4r))$ for $r\in\mathbb R$; and for a set of tiles $\mathfrak C$ let $T^*_{\mathfrak C}g(x)=\sum_{\mathfrak p\in\mathfrak C}T^*_{\mathfrak p}g(x)$ (`adjointCarlesonSum`). For a set $\mathcal C$ of cubes and $h:X\to\mathbb R$ let $P_{\mathcal C}h(x)=\sum_{J\in\mathcal C}\mathbf 1_J(x)\,\frac{1}{\mu(J)}\int_J h\,d\mu$ (`Forest.approxOnCube`). Let $\mathcal J_6(u_1)\subseteq\mathrm{Grid}(X)$ denote the project set of cubes `t.𝓙₆ u₁` (per its docstring, the set $\mathcal J'$ at the start of Section 7.6). Let $C_{7.6.3}(a,n)\in\mathbb R$ be the project constant `Forest.C7_6_3 a n` (per its docstring, denoted $s_1$ in the proof of Lemma 7.6.3, with value $Zn/(202a^3)-2$ in the blueprint). Here $\|\cdot\|_{L^2(\mu)}\in[0,\infty]$ is the (extended) $L^2$ norm with respect to $\mu$ (`eLpNorm · 2 volume`), and "bounded with compact support" means `BoundedCompactSupport` with respect to $\mu$ (per its docstring, bounded, compactly supported, measurable). (Equation (7.6.3) of Lemma 7.6.2.) Let $u_1,u_2\in\mathfrak P$ with $u_1\in t$, $u_2\in t$, $u_1\ne u_2$ and $\mathcal I(u_1)\le\mathcal I(u_2)$, and let $f:X\to\mathbb C$ be bounded with compact support. Then, in $[0,\infty]$, $$\Big\|P_{\mathcal J_6(u_1)}\big(x\mapsto|T^*_{\mathfrak T(u_2)\setminus\mathfrak S_0(u_1,u_2)}f(x)|\big)\Big\|_{L^2(\mu)}\le\sum_{k\in\mathbb Z,\ \lfloor C_{7.6.3}(a,n)\rfloor\le k\le 2S}\Bigg(\sum_{J\in\mathcal J_6(u_1)}\mu(J)^{-1}\Big(\int_J\ \sum_{\mathfrak p\in A_{J,k}}|T^*_{\mathfrak p}f(y)|\,d\mu(y)\Big)^2\Bigg)^{1/2},$$ where $A_{J,k}$ is the set of tiles $\mathfrak p\in\mathfrak T(u_2)\setminus\mathfrak S_0(u_1,u_2)$ such that $J$ is not disjoint from the open ball $B(c(\mathfrak p),8D^{s(\mathfrak p)})$ and $s(\mathfrak p)=s(J)-k$; the integral is a lower Lebesgue integral and $\mu(J)^{-1}$ is the inverse in $[0,\infty]$.
Checker's issue: Calls Grid(X) a finite type, which the prompt does not support (only the tile type has a finiteness instance).

### `TileStructure.Forest.e764_postCS`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf : BoundedCompactSupport f volume) : eLpNorm (Forest.approxOnCube (t.𝓙₆ u₁) fun x => ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) f x‖) 2 volume ≤ (↑(C2_1_3 a) * 2 ^ (11 * a + 2) * ∑ k ∈ Finset.Icc ⌊Forest.C7_6_3 a n⌋ (2 * ↑(defaultS X)), ↑(defaultD a) ^ (-↑k * defaultκ a / 2)) * eLpNorm ((↑(𝓘 u₁)).indicator fun x => maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f x) 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u₁ u₂ : 𝔓 X} {f : X → ℂ}, u₁ ∈ t → u₂ ∈ t → u₁ ≠ u₂ → 𝓘 u₁ ≤ 𝓘 u₂ → BoundedCompactSupport f volume → @eLpNorm _ ℝ _ MeasureSpace.toMeasurableSpace (Forest.approxOnCube (F := F) (G := G) (t.𝓙₆ (F := F) (G := G) u₁) fun (x : X) => ‖adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₂ \ t.𝔖₀ (F := F) (G := G) u₁ u₂) f x‖) (2 : ENNReal) volume ≤ (↑(C2_1_3 a) * (2 : ENNReal) ^ ((11 : ℕ) * a + (2 : ℕ)) * ∑ k ∈ Finset.Icc ⌊Forest.C7_6_3 a n⌋ ((2 : ℤ) * ↑(defaultS X (F := F) (G := G))), HPow.hPow (α := ENNReal) (↑(defaultD a)) (-↑k * defaultκ a / (2 : ℝ))) * @eLpNorm _ ENNReal _ MeasureSpace.toMeasurableSpace ((↑(𝓘 u₁)).indicator fun (x : X) => maximalFunction volume (Forest.𝓑 (F := F) (G := G)) (Forest.c𝓑 (F := F) (G := G)) (Forest.r𝓑 (F := F) (G := G)) (1 : ℝ) f x) (2 : ENNReal) volume`
Docstring: Equation (7.6.4) of Lemma 7.6.2 (after applying Cauchy–Schwarz and simplification).
Previous English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume given an instance of the project structure `ProofData` $a\,q\,K\,\sigma_1\,\sigma_2\,F\,G$ on $X$ (per its docstring, the data common through most of chapters 2–7). Through its `KernelProofData` component this provides a `DoublingMeasure` $X\,(2^a)$ structure on $X$ (per its docstring, a measure with nice properties including a doubling condition), whose measure we write $\mu$ (Lean's `volume`), and a `CompatibleFunctions` $\mathbb R\,X\,(2^a)$ structure, hence a `FunctionDistances` $\mathbb R\,X$ structure, which gives a type $\Theta(X)$ of functions $X\to\mathbb R$ (per its docstring, continuous functions) and, for each $x\in X$ and $r\in\mathbb R$, a pseudometric $d_{x,r}$ on $\Theta(X)$. Let $Q : X\to\Theta(X)$ be the simple function given by the field `ProofData.Q`. Put $D=2^{𝕔 a^2}\in\mathbb N$ (`defaultD a`), where $𝕔\in\mathbb N$ is the project constant `𝕔` (per its docstring, fixed equal to $100$); $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`); $Z=2^{12a}\in\mathbb N$ (`defaultZ a`); $o\in X$ the point `cancelPt X`, chosen so that every element of $\Theta(X)$ vanishes at $o$; and $S\in\mathbb N$ (`defaultS X`) the least natural number $m>0$ such that $-m\le\sigma_1(x)$ and $\sigma_2(x)\le m$ for all $x\in X$ and $F\cup G\subseteq B(o,D^m/4)$. Assume given a tile structure `TileStructure` $Q\,D\,\kappa\,S\,o$ on $X$. Write $\mathfrak P$ for its finite type of tiles and $\mathrm{Grid}(X)$ for its finite type of dyadic cubes; we identify a cube $J$ with its underlying subset of $X$, write $c(J)\in X$ for its center and $s(J)\in\mathbb Z$ for its scale, and order cubes by $J\le J'$ iff $J\subseteq J'$ and $s(J)\le s(J')$ (so $J<J'$ means $J\le J'$ and $J\ne J'$). Each tile $\mathfrak p\in\mathfrak P$ has a cube $\mathcal I(\mathfrak p)\in\mathrm{Grid}(X)$, with $c(\mathfrak p):=c(\mathcal I(\mathfrak p))$ and $s(\mathfrak p):=s(\mathcal I(\mathfrak p))$, an element $\mathcal Q(\mathfrak p)\in\Theta(X)$ and a set $\Omega(\mathfrak p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (`Forest` $X\,n$); it has a set of tiles $\mathfrak U(t)\subseteq\mathfrak P$ (we write $u\in t$ for $u\in\mathfrak U(t)$) and assigns to each tile $u$ a set of tiles $\mathfrak T(u)\subseteq\mathfrak P$. For tiles $u_1,u_2$ let $\mathfrak S_0(u_1,u_2)=\{\mathfrak p\in\mathfrak T(u_1)\cup\mathfrak T(u_2) : 2^{Zn/2}\le d_{c(\mathfrak p),\,D^{s(\mathfrak p)}/4}(\mathcal Q(u_1),\mathcal Q(u_2))\}$ (`t.𝔖₀ u₁ u₂`). For a tile $\mathfrak p$, a function $g:X\to\mathbb C$ and $x\in X$ let $T^*_{\mathfrak p}g(x)=\int_{E(\mathfrak p)}\overline{K_{s(\mathfrak p)}(y,x)}\,e^{i(Q(y)(y)-Q(y)(x))}\,g(y)\,d\mu(y)$ (`adjointCarleson`), where $E(\mathfrak p)=\{y\in\mathcal I(\mathfrak p) : Q(y)\in\Omega(\mathfrak p),\ \sigma_1(y)\le s(\mathfrak p)\le\sigma_2(y)\}$, $K_s(x,y)=K(x,y)\,\psi(D^{-s}d(x,y))$ for $s\in\mathbb Z$, and $\psi(r)=\max(0,\min(1,4Dr-1,2-4r))$ for $r\in\mathbb R$; and for a set of tiles $\mathfrak C$ let $T^*_{\mathfrak C}g(x)=\sum_{\mathfrak p\in\mathfrak C}T^*_{\mathfrak p}g(x)$ (`adjointCarlesonSum`). For $g:X\to\mathbb C$ and $x\in X$ let $Mg(x)=\sup\{\,\frac{1}{\mu(B_{k,l,J})}\int_{B_{k,l,J}}|g|\,d\mu : k,l\in\mathbb N,\ k\le S+5,\ l\le 2S+3,\ J\in\mathrm{Grid}(X),\ x\in B_{k,l,J}\}\in[0,\infty]$ (the supremum of the empty set being $0$), where $B_{k,l,J}$ is the open ball of center $c(J)$ and radius $2^kD^{s(J)+l}$; this is `maximalFunction volume 𝓑 c𝓑 r𝓑 1 g`, the uncentered Hardy–Littlewood maximal function over this family of balls with exponent $1$. For a set $\mathcal C$ of cubes and $h:X\to\mathbb R$ let $P_{\mathcal C}h(x)=\sum_{J\in\mathcal C}\mathbf 1_J(x)\,\frac{1}{\mu(J)}\int_J h\,d\mu$ (`Forest.approxOnCube`). Let $\mathcal J_6(u_1)\subseteq\mathrm{Grid}(X)$ denote the project set of cubes `t.𝓙₆ u₁` (per its docstring, the set $\mathcal J'$ at the start of Section 7.6). Let $C_{7.6.3}(a,n)\in\mathbb R$ be the project constant `Forest.C7_6_3 a n` (per its docstring, denoted $s_1$ in the proof of Lemma 7.6.3, with value $Zn/(202a^3)-2$ in the blueprint). Let $C_{2.1.3}(a)=2^{(𝕔+2)a^3}$ (`C2_1_3 a`). Here $\|\cdot\|_{L^2(\mu)}\in[0,\infty]$ is the (extended) $L^2$ norm with respect to $\mu$ (`eLpNorm · 2 volume`), and "bounded with compact support" means `BoundedCompactSupport` with respect to $\mu$ (per its docstring, bounded, compactly supported, measurable). (Equation (7.6.4) of Lemma 7.6.2, after applying Cauchy–Schwarz and simplification.) Let $u_1,u_2\in\mathfrak P$ with $u_1\in t$, $u_2\in t$, $u_1\ne u_2$ and $\mathcal I(u_1)\le\mathcal I(u_2)$, and let $f:X\to\mathbb C$ be bounded with compact support. Then, in $[0,\infty]$, $$\Big\|P_{\mathcal J_6(u_1)}\big(x\mapsto|T^*_{\mathfrak T(u_2)\setminus\mathfrak S_0(u_1,u_2)}f(x)|\big)\Big\|_{L^2(\mu)}\le\Big(C_{2.1.3}(a)\cdot 2^{11a+2}\cdot\sum_{k\in\mathbb Z,\ \lfloor C_{7.6.3}(a,n)\rfloor\le k\le 2S}D^{-k\kappa/2}\Big)\,\big\|\mathbf 1_{\mathcal I(u_1)}Mf\big\|_{L^2(\mu)}.$$
Checker's issue: Calls Grid(X) a finite type, which the prompt does not support (only the tile type has a finiteness instance).

### `TileStructure.Forest.bound_for_tree_projection`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hf : BoundedCompactSupport f volume) : eLpNorm (Forest.approxOnCube (t.𝓙₆ u₁) fun x => ‖adjointCarlesonSum ((fun x => t.𝔗 x) u₂ \ t.𝔖₀ u₁ u₂) f x‖) 2 volume ≤ ↑(Forest.C7_6_2 a n) * eLpNorm ((↑(𝓘 u₁)).indicator fun x => maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 f x) 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u₁ u₂ : 𝔓 X} {f : X → ℂ}, u₁ ∈ t → u₂ ∈ t → u₁ ≠ u₂ → 𝓘 u₁ ≤ 𝓘 u₂ → BoundedCompactSupport f volume → @eLpNorm _ ℝ _ MeasureSpace.toMeasurableSpace (Forest.approxOnCube (F := F) (G := G) (t.𝓙₆ (F := F) (G := G) u₁) fun (x : X) => ‖adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₂ \ t.𝔖₀ (F := F) (G := G) u₁ u₂) f x‖) (2 : ENNReal) volume ≤ ↑(Forest.C7_6_2 a n) * @eLpNorm _ ENNReal _ MeasureSpace.toMeasurableSpace ((↑(𝓘 u₁)).indicator fun (x : X) => maximalFunction volume (Forest.𝓑 (F := F) (G := G)) (Forest.c𝓑 (F := F) (G := G)) (Forest.r𝓑 (F := F) (G := G)) (1 : ℝ) f x) (2 : ENNReal) volume`
Docstring: Lemma 7.6.2.
Previous English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume given an instance of the project structure `ProofData` $a\,q\,K\,\sigma_1\,\sigma_2\,F\,G$ on $X$ (per its docstring, the data common through most of chapters 2–7). Through its `KernelProofData` component this provides a `DoublingMeasure` $X\,(2^a)$ structure on $X$ (per its docstring, a measure with nice properties including a doubling condition), whose measure we write $\mu$ (Lean's `volume`), and a `CompatibleFunctions` $\mathbb R\,X\,(2^a)$ structure, hence a `FunctionDistances` $\mathbb R\,X$ structure, which gives a type $\Theta(X)$ of functions $X\to\mathbb R$ (per its docstring, continuous functions) and, for each $x\in X$ and $r\in\mathbb R$, a pseudometric $d_{x,r}$ on $\Theta(X)$. Let $Q : X\to\Theta(X)$ be the simple function given by the field `ProofData.Q`. Put $D=2^{𝕔 a^2}\in\mathbb N$ (`defaultD a`), where $𝕔\in\mathbb N$ is the project constant `𝕔` (per its docstring, fixed equal to $100$); $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`); $Z=2^{12a}\in\mathbb N$ (`defaultZ a`); $o\in X$ the point `cancelPt X`, chosen so that every element of $\Theta(X)$ vanishes at $o$; and $S\in\mathbb N$ (`defaultS X`) the least natural number $m>0$ such that $-m\le\sigma_1(x)$ and $\sigma_2(x)\le m$ for all $x\in X$ and $F\cup G\subseteq B(o,D^m/4)$. Assume given a tile structure `TileStructure` $Q\,D\,\kappa\,S\,o$ on $X$. Write $\mathfrak P$ for its finite type of tiles and $\mathrm{Grid}(X)$ for its finite type of dyadic cubes; we identify a cube $J$ with its underlying subset of $X$, write $c(J)\in X$ for its center and $s(J)\in\mathbb Z$ for its scale, and order cubes by $J\le J'$ iff $J\subseteq J'$ and $s(J)\le s(J')$ (so $J<J'$ means $J\le J'$ and $J\ne J'$). Each tile $\mathfrak p\in\mathfrak P$ has a cube $\mathcal I(\mathfrak p)\in\mathrm{Grid}(X)$, with $c(\mathfrak p):=c(\mathcal I(\mathfrak p))$ and $s(\mathfrak p):=s(\mathcal I(\mathfrak p))$, an element $\mathcal Q(\mathfrak p)\in\Theta(X)$ and a set $\Omega(\mathfrak p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (`Forest` $X\,n$); it has a set of tiles $\mathfrak U(t)\subseteq\mathfrak P$ (we write $u\in t$ for $u\in\mathfrak U(t)$) and assigns to each tile $u$ a set of tiles $\mathfrak T(u)\subseteq\mathfrak P$. For tiles $u_1,u_2$ let $\mathfrak S_0(u_1,u_2)=\{\mathfrak p\in\mathfrak T(u_1)\cup\mathfrak T(u_2) : 2^{Zn/2}\le d_{c(\mathfrak p),\,D^{s(\mathfrak p)}/4}(\mathcal Q(u_1),\mathcal Q(u_2))\}$ (`t.𝔖₀ u₁ u₂`). For a tile $\mathfrak p$, a function $g:X\to\mathbb C$ and $x\in X$ let $T^*_{\mathfrak p}g(x)=\int_{E(\mathfrak p)}\overline{K_{s(\mathfrak p)}(y,x)}\,e^{i(Q(y)(y)-Q(y)(x))}\,g(y)\,d\mu(y)$ (`adjointCarleson`), where $E(\mathfrak p)=\{y\in\mathcal I(\mathfrak p) : Q(y)\in\Omega(\mathfrak p),\ \sigma_1(y)\le s(\mathfrak p)\le\sigma_2(y)\}$, $K_s(x,y)=K(x,y)\,\psi(D^{-s}d(x,y))$ for $s\in\mathbb Z$, and $\psi(r)=\max(0,\min(1,4Dr-1,2-4r))$ for $r\in\mathbb R$; and for a set of tiles $\mathfrak C$ let $T^*_{\mathfrak C}g(x)=\sum_{\mathfrak p\in\mathfrak C}T^*_{\mathfrak p}g(x)$ (`adjointCarlesonSum`). For $g:X\to\mathbb C$ and $x\in X$ let $Mg(x)=\sup\{\,\frac{1}{\mu(B_{k,l,J})}\int_{B_{k,l,J}}|g|\,d\mu : k,l\in\mathbb N,\ k\le S+5,\ l\le 2S+3,\ J\in\mathrm{Grid}(X),\ x\in B_{k,l,J}\}\in[0,\infty]$ (the supremum of the empty set being $0$), where $B_{k,l,J}$ is the open ball of center $c(J)$ and radius $2^kD^{s(J)+l}$; this is `maximalFunction volume 𝓑 c𝓑 r𝓑 1 g`, the uncentered Hardy–Littlewood maximal function over this family of balls with exponent $1$. For a set $\mathcal C$ of cubes and $h:X\to\mathbb R$ let $P_{\mathcal C}h(x)=\sum_{J\in\mathcal C}\mathbf 1_J(x)\,\frac{1}{\mu(J)}\int_J h\,d\mu$ (`Forest.approxOnCube`). Let $\mathcal J_6(u_1)\subseteq\mathrm{Grid}(X)$ denote the project set of cubes `t.𝓙₆ u₁` (per its docstring, the set $\mathcal J'$ at the start of Section 7.6). Let $C_{7.6.2}(a,n)\in\mathbb R_{\ge0}$ be the project constant `Forest.C7_6_2 a n` (per its docstring, the constant used in this lemma). Here $\|\cdot\|_{L^2(\mu)}\in[0,\infty]$ is the (extended) $L^2$ norm with respect to $\mu$ (`eLpNorm · 2 volume`), and "bounded with compact support" means `BoundedCompactSupport` with respect to $\mu$ (per its docstring, bounded, compactly supported, measurable). (Lemma 7.6.2.) Let $u_1,u_2\in\mathfrak P$ with $u_1\in t$, $u_2\in t$, $u_1\ne u_2$ and $\mathcal I(u_1)\le\mathcal I(u_2)$, and let $f:X\to\mathbb C$ be bounded with compact support. Then, in $[0,\infty]$, $$\Big\|P_{\mathcal J_6(u_1)}\big(x\mapsto|T^*_{\mathfrak T(u_2)\setminus\mathfrak S_0(u_1,u_2)}f(x)|\big)\Big\|_{L^2(\mu)}\le C_{7.6.2}(a,n)\,\big\|\mathbf 1_{\mathcal I(u_1)}Mf\big\|_{L^2(\mu)}.$$
Checker's issue: Calls Grid(X) a finite type, which the prompt does not support (only the tile type has a finiteness instance).
