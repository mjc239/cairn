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

#### `C5_1_2` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant used in Lemma 5.1.2. Has value `2 ^ (441 * a ^ 3) / (q - 1) ^ 4` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => (2 : NNReal) ^ (((3 : ℕ) * 𝕔 + (16 : ℕ) + (5 : ℕ) * (𝕔 / (4 : ℕ))) * a ^ (3 : ℕ)) / (q - (1 : NNReal)) ^ (4 : ℕ)`

#### `CompatibleFunctions.toFunctionDistances` (def)
Lean: `{𝕜 : outParam (Type u_3)} → {X : Type u} → {A : outParam ℕ} → {inst : RCLike 𝕜} → {inst_1 : PseudoMetricSpace X} → [self : CompatibleFunctions 𝕜 X A] → FunctionDistances 𝕜 X`
Definition: `fun {𝕜 : outParam (Type u_3)} (X : Type u) {A : outParam ℕ} {inst : RCLike 𝕜} {inst_1 : PseudoMetricSpace X} [self : CompatibleFunctions 𝕜 X A] => self.1`

#### `G'` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set X`
Docstring: The set `G'`, defined below (5.1.28).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => G₁ (F := F) (G := G) ∪ G₂ (F := F) (G := G) ∪ G₃ (F := F) (G := G)`

#### `KernelProofData.cf` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → {inst : PseudoMetricSpace X} → [self : KernelProofData a K] → CompatibleFunctions ℝ X (defaultA a)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {K : outParam (X → X → ℂ)} {inst : PseudoMetricSpace X} [self : KernelProofData a K] => self.3`

#### `KernelProofData.d` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → {inst : PseudoMetricSpace X} → [self : KernelProofData a K] → DoublingMeasure X ↑(defaultA a)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {K : outParam (X → X → ℂ)} {inst : PseudoMetricSpace X} [self : KernelProofData a K] => self.1`

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

#### `cancelPt` (def)
Lean: `{𝕜 : Type u_1} → (X : Type u_2) → {A : ℕ} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [CompatibleFunctions 𝕜 X A] → X`
Docstring: The point `o` in the blueprint
Definition: `fun {𝕜 : Type u_1} (X : Type u_2) {A : ℕ} [RCLike 𝕜] [PseudoMetricSpace X] [CompatibleFunctions 𝕜 X A] => Exists.choose (p := fun (o : X) => ∀ (f : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), (coeΘ f) o = (0 : 𝕜)) ⋯`

#### `carlesonSum` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → (X → ℂ) → X → ℂ`
Docstring: The operator `T_ℭ f` defined at the bottom of Section 7.4. We will use this in other places of the formalization as well.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [PseudoMetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) => ∑ p : 𝔓 X with p ∈ ℭ, carlesonOn (F := F) (G := G) p f x`

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

#### `nnq` (def)
Lean: `(X : Type u_1) → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [ProofData a q K σ₁ σ₂ F G] → NNReal`
Docstring: `q` as an element of `ℝ≥0`.
Definition: `fun (X : Type u_1) {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [PseudoMetricSpace X] [ProofData a q K σ₁ σ₂ F G] => ⟨q, ⋯⟩`

#### `𝔓₁` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X)`
Docstring: The set `𝔓₁`, defined in (5.1.30).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => ⋃ (n : ℕ), ⋃ (k : ℕ), ⋃ (_ : k ≤ n), ⋃ (j : ℕ), ⋃ (_ : j ≤ (2 : ℕ) * n + (3 : ℕ)), ℭ₅ (F := F) (G := G) k n j`

#### `C2_0_4_base` (def)
Lean: `ℕ → NNReal`
Definition: `wrapped✝.1`

#### `maxℭ` (def)
Lean: `(X : Type u_1) → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ`
Definition: `fun (X : Type u_1) {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => (Exists.choose (p := fun (n : ℕ × ℕ) => ∀ (x : ℕ × ℕ), Membership.mem (γ := Set (ℕ × ℕ)) {kn : ℕ × ℕ | Set.Nonempty (α := 𝔓 X) (ℭ (F := F) (G := G) kn.1 kn.2)} x → x.2 ≤ n.2) ⋯).2`

#### `EquivalenceOn` (inductive)
Lean: `{α : Type u_1} → (α → α → Prop) → Set α → Prop`
Docstring: An equivalence relation on the set `s`.

#### `TileStructure.toPreTileStructure` (def)
Lean: `{X : Type u} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {inst_2 : FunctionDistances ℝ X} → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : TileStructure Q D κ S o] → PreTileStructure Q D κ S o`
Definition: `fun (X : Type u) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {inst_2 : FunctionDistances ℝ X} {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : TileStructure Q D κ S o] => self.1`

#### `URel` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → 𝔓 X → 𝔓 X → Prop`
Docstring: The relation `∼` defined below (5.4.2). It is an equivalence relation on `𝔘₂ k n j`.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) (u u' : 𝔓 X) => u = u' ∨ ∃ p ∈ 𝔗₁ (F := F) (G := G) k n j u, smul (F := F) (G := G) (10 : ℝ) p ≤ smul (F := F) (G := G) (1 : ℝ) u'`

#### `𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → (X : Type u) → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [PreTileStructure.{u, u_1, u_2} Q D κ S o] → Type u`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] (X : Type u) {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X`

#### `𝔘₂` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `𝔘₂(k, n, j)` of `𝔘₁(k, n, j)`, given in (5.4.2).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => {u : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (𝔘₁ (F := F) (G := G) k n j) u ∧ ¬Disjoint (𝔗₁ (F := F) (G := G) k n j u) (ℭ₆ (F := F) (G := G) k n j)}`

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

#### `defaultZ` (def)
Lean: `ℕ → ℕ`
Docstring: The constant `Z` from (2.0.3).
Definition: `fun (a : ℕ) => (2 : ℕ) ^ ((12 : ℕ) * a)`

#### `instPartialOrderGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → PartialOrder (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => PartialOrder.lift (fun (i : @GridStructure.Grid X _ inst inst_1 _ _ _ _ _) => (↑i, GridStructure.s i)) ⋯`

#### `s` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Grid X → ℤ`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.s`

#### `𝓘` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → Grid X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] => PreTileStructure.𝓘`

#### `𝔗₂` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → 𝔓 X → Set (𝔓 X)`
Docstring: The subset `𝔗₂(u)` of `ℭ₆(k, n, j)`, given in (5.4.5). In lemmas, we will assume `u ∈ 𝔘₃ k n l`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) (u : 𝔓 X) => ℭ₆ (F := F) (G := G) k n j ∩ ⋃ (u' : 𝔓 X), ⋃ (_ : Membership.mem (γ := Set (𝔓 X)) (𝔘₂ (F := F) (G := G) k n j) u'), ⋃ (_ : URel (F := F) (G := G) k n j u u'), 𝔗₁ (F := F) (G := G) k n j u'`

#### `𝔘₃` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: `𝔘₃(k, n, j) ⊆ 𝔘₂ k n j` is an arbitary set of representatives of `URel` on `𝔘₂ k n j`, given above (5.4.5).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => EquivalenceOn.reprs (r := URel (F := F) (G := G) k n j) (s := 𝔘₂ (F := F) (G := G) k n j) ⋯`

#### `𝔠` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => c (𝓘 p)`

#### `𝔰` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → ℤ`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => s (𝓘 p)`

#### `FunctionDistances.Θ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → (X : Type u) → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → Type u`
Docstring: A type of continuous functions from `X` to `𝕜`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.1`

#### `PreTileStructure.𝒬` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X → @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.6`

#### `TileLike` (def)
Lean: `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Type u_1`
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => Grid X × (Set (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))ᵒᵈ`

#### `TileLike.fst` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → TileLike X (F := F) (G := G) → Grid X`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (x : TileLike X (F := F) (G := G)) => x.1`

#### `TileLike.snd` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → TileLike X (F := F) (G := G) → Set (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (x : TileLike X (F := F) (G := G)) => x.2`

#### `WithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → X → ℝ → Type u_2`
Docstring: Class used to endow `Θ X` with a pseudometric space structure.
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] (x : X) (r : ℝ) => @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`

#### `instPartialOrderTileLike` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → PartialOrder (TileLike X (F := F) (G := G))`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => { le := instPartialOrderTileLike._aux_1, lt := instPartialOrderTileLike._aux_3, le_refl := ⋯, le_trans := ⋯, lt_iff_le_not_ge := ⋯, le_antisymm := ⋯ }`

#### `instPseudoMetricSpaceWithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → {x : X} → {r : ℝ} → PseudoMetricSpace (WithFunctionDistance x r)`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] {x : X} {r : ℝ} => FunctionDistances.metric x r`

#### `ℭ₆` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `ℭ₆(k, n, j)` of `ℭ₅(k, n, j)`, given above (5.4.1).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => {p : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (ℭ₅ (F := F) (G := G) k n j) p ∧ ¬↑(𝓘 p) ⊆ G' (F := F) (G := G)}`

#### `𝔘₄` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: Define `𝔘₄ k n j l` as the union of `2 ^ n` disjoint subfamilies in `𝔘₃ k n j`, to make sure the multiplicity is at most `2 ^ n` to get a forest.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j l : ℕ) => ⋃ i ∈ Set.Ico (l * (2 : ℕ) ^ n) ((l + (1 : ℕ)) * (2 : ℕ) ^ n), iteratedMaximalSubfamily (F := F) (G := G) (𝔘₃ (F := F) (G := G) k n j) i`

#### `C2_0_4` (def)
Lean: `ℕ → ℝ → ℕ → NNReal`
Docstring: The constant used in `forest_operator`. Has value `2 ^ (440 * a ^ 3 - (q - 1) / q * n)` in the blueprint.
Definition: `wrapped✝.1`

#### `C5_1_2_optimized` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: An optimized constant for the forest union theorem. The constant from the blueprint, defined as `C5_1_2` below, is slightly worse.
Definition: `fun (a : ℕ) (q : NNReal) => C2_0_4_base a * (2 : NNReal) ^ (↑a + (5 / 2 : ℝ)) * (13009 : NNReal) / (q - (1 : NNReal)) ^ (4 : ℕ)`

#### `𝔗₁` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → 𝔓 X → Set (𝔓 X)`
Docstring: The subset `𝔗₁(u)` of `ℭ₁(k, n, j)`, given in (5.4.1). In lemmas, we will assume `u ∈ 𝔘₁ k n l`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) (u : 𝔓 X) => {p : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (ℭ₁ (F := F) (G := G) k n j) p ∧ 𝓘 p ≠ 𝓘 u ∧ smul (F := F) (G := G) (2 : ℝ) p ≤ smul (F := F) (G := G) (1 : ℝ) u}`

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

#### `G₁` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set X`
Docstring: The exceptional set `G₁`, defined in (5.1.25).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => ⋃ (p : 𝔓 X), ⋃ (_ : Membership.mem (γ := Set (𝔓 X)) (highDensityTiles (F := F) (G := G)) p), ↑(𝓘 p)`

#### `G₂` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set X`
Docstring: The set `G₂`, defined in (5.1.27).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => ⋃ (n : ℕ), ⋃ (k : ℕ), ⋃ (_ : k ≤ n), setA (F := F) (G := G) ((2 : ℕ) * n + (6 : ℕ)) k n`

#### `G₃` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set X`
Docstring: The set `G₃`, defined in (5.1.28).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => ⋃ (n : ℕ), ⋃ (k : ℕ), ⋃ (_ : k ≤ n), ⋃ (j : ℕ), ⋃ (_ : j ≤ (2 : ℕ) * n + (3 : ℕ)), ⋃ (p : 𝔓 X), ⋃ (_ : Membership.mem (γ := Set (𝔓 X)) (𝔏₄ (F := F) (G := G) k n j) p), ↑(𝓘 p)`

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

#### `carlesonOn` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
Docstring: The operator `T_𝔭` defined in Proposition 2.0.2.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [PseudoMetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) => (E (F := F) (G := G) p).indicator fun (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => Complex.exp (Complex.I * (↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y) - ↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) x))) * Ks (𝔰 p) x y * f y`

#### `instFintype𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (𝔓.{u, u_1, u_2} X)`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.fintype_𝔓`

#### `ℭ₅` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `ℭ₅(k, n, j)` of `ℭ₄(k, n, j)`, given in (5.1.23).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => ℭ₄ (F := F) (G := G) k n j \ 𝔏₄ (F := F) (G := G) k n j`

#### `smul` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℝ → 𝔓 X → TileLike X (F := F) (G := G)`
Docstring: This is not defined as such in the blueprint, but `λp ≲ λ'p'` can be written using `smul l p ≤ smul l' p'`. Beware: `smul 1 p` is very different from `toTileLike p`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (l : ℝ) (p : 𝔓 X) => (𝓘 p, ball_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) l)`

#### `𝔘₁` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `𝔘₁(k, n, j)` of `ℭ₁(k, n, j)`, given in (5.1.14).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => {u : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (ℭ₁ (F := F) (G := G) k n j) u ∧ ∀ (p : 𝔓 X), Membership.mem (γ := Set (𝔓 X)) (ℭ₁ (F := F) (G := G) k n j) p → 𝓘 u < 𝓘 p → Disjoint (ball_{𝔠 u, ↑(defaultD a) ^ 𝔰 u / (4 : ℝ)} (𝒬 u) (100 : ℝ)) (ball_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) (100 : ℝ))}`

#### `GridStructure.s` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → ℤ`
Docstring: scale functions
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.4`

#### `c` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Grid X → X`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.c`

#### `iteratedMaximalSubfamily` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ℕ → Set (𝔓 X)`
Docstring: Iterating `maximalSubfamily` to obtain disjoint subfamilies of `A`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (A : Set (𝔓 X)) => WellFounded.Nat.fix (motive := fun (n : ℕ) => Set (𝔓 X)) (fun (x : ℕ) => x) fun (n : ℕ) (a_1 : (y : ℕ) → InvImage (fun (x1 x2 : ℕ) => x1 < x2) (fun (x : ℕ) => x) y n → Set (𝔓 X)) => maximalSubfamily (F := F) (G := G) (A \ ⋃ (i : ↑{i : ℕ | i < n}), have this := ⋯; a_1 ↑i ⋯)`

## Flagged translations

### `forest_union`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C5_1_2 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {f : X → ℂ}, (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable f → ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (𝔓₁ (F := F) (G := G)) f x‖ₑ ≤ ↑(C5_1_2 a (nnq X (F := F) (G := G))) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹`
Docstring: Lemma 5.1.2 in the blueprint: the integral of the Carleson sum over the set which can naturally be decomposed as a union of forests can be controlled, thanks to the estimate for a single forest.
Previous English: (Lemma 5.1.2) Let $X$ be a metric space and assume the standing assumptions of the proof: the `ProofData` bundle for the data $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \times X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$ (making $X$ a doubling metric measure space with the kernel $K$), together with a tile structure (`TileStructure`) for $Q$ with the default parameters $D = $ `defaultD a`, $\kappa = $ `defaultκ a`, $S = $ `defaultS X` and $o = $ `cancelPt X`. Under these assumptions, let $f$ be a measurable function with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Then $$\int_{G\setminus G'} \|\mathrm{carlesonSum}(\mathfrak{P}_1, f)(x)\|\,dx \le C_{5.1.2}(a,q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where $C_{5.1.2}$ is the constant `C5_1_2` and $q$ is `nnq X`.
Checker's issue: The codomain of f (X -> C) is not stated. G', P_1 and mu are not introduced. The letter q is used both for the real parameter and for nnq X. Parenthetical says ProofData makes X 'a doubling metric measure space with the kernel K', which the prompt does not support.

### `forest_union_aux`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C2_0_4_base a) * 2 ^ (↑a + 5 / 2) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹ * ∑ n ≤ maxℭ X, ∑ _k ≤ n, ∑ _j ≤ 2 * n + 3, ∑ _l < 4 * n + 12, 2 ^ (-(q - 1) / q * ↑n)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {f : X → ℂ}, (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable f → ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (𝔓₁ (F := F) (G := G)) f x‖ₑ ≤ ↑(C2_0_4_base a) * (2 : ENNReal) ^ (↑a + (5 / 2 : ℝ)) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹ * ∑ n ≤ maxℭ X (F := F) (G := G), ∑ _k ≤ n, ∑ _j ≤ (2 : ℕ) * n + (3 : ℕ), ∑ _l < (4 : ℕ) * n + (12 : ℕ), (2 : ENNReal) ^ (-(q - (1 : ℝ)) / q * ↑n)`
Docstring: Putting all the above decompositions together, one obtains a control of the integral of the full Carleson sum over `𝔓₁`, as a sum over all the forests.
Previous English: Let $X$ be a metric space and assume the standing assumptions of the proof: the `ProofData` bundle for the data $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \times X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$ (making $X$ a doubling metric measure space with the kernel $K$), together with a tile structure (`TileStructure`) for $Q$ with the default parameters $D = $ `defaultD a`, $\kappa = $ `defaultκ a`, $S = $ `defaultS X` and $o = $ `cancelPt X`. Under these assumptions, let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $$\int_{G\setminus G'} \|\mathrm{carlesonSum}(\mathfrak{P}_1, f)(x)\|\,dx \le C_{2.0.4}^{\mathrm{base}}(a)\, 2^{a+5/2}\, \mu(G)^{1-1/q}\, \mu(F)^{1/q} \sum_{n \le \mathrm{max}\mathfrak{C}} \sum_{k \le n} \sum_{j \le 2n+3} \sum_{l < 4n+12} 2^{-\frac{q-1}{q} n},$$ where $C_{2.0.4}^{\mathrm{base}}$ is `C2_0_4_base` and $\mathrm{max}\mathfrak{C}$ is `maxℭ X`.
Checker's issue: The type of f (X -> C) is not stated. G', P_1 and mu are not introduced. Parenthetical says ProofData makes X 'a doubling metric measure space with the kernel K', which the prompt does not support.

### `equivalenceOn_urel`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : EquivalenceOn (URel k n j) (𝔘₂ k n j)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {k n j : ℕ}, EquivalenceOn (URel (F := F) (G := G) k n j) (𝔘₂ (F := F) (G := G) k n j)`
Docstring: Lemma 5.4.2.
Previous English: (Lemma 5.4.2) Let $X$ be a metric space and assume the standing assumptions of the proof: the `ProofData` bundle for the data $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \times X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$ (making $X$ a doubling metric measure space with the kernel $K$), together with a tile structure (`TileStructure`) for $Q$ with the default parameters $D = $ `defaultD a`, $\kappa = $ `defaultκ a`, $S = $ `defaultS X` and $o = $ `cancelPt X`. Under these assumptions, the relation $\sim$ (`URel k n j`) is an equivalence relation on the set $\mathfrak{U}_2(k,n,j)$.
Checker's issue: k, n, j are not introduced as natural numbers. Parenthetical says ProofData makes X 'a doubling metric measure space with the kernel K', which the prompt does not support.

### `forest_inner`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ 𝔘₃ k n j) (hp : p ∈ 𝔗₂ k n j u) : Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p) ⊆ ↑(𝓘 u)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {k n j : ℕ} {p u : 𝔓 X}, Membership.mem (γ := Set (𝔓 X)) (𝔘₃ (F := F) (G := G) k n j) u → p ∈ 𝔗₂ (F := F) (G := G) k n j u → Metric.ball (𝔠 p) ((8 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p)) ⊆ ↑(𝓘 u)`
Docstring: Lemma 5.4.7, verifying (2.0.37)
Previous English: (Lemma 5.4.7, verifying (2.0.37)) Let $X$ be a metric space and assume the standing assumptions of the proof: the `ProofData` bundle for the data $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \times X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$ (making $X$ a doubling metric measure space with the kernel $K$), together with a tile structure (`TileStructure`) for $Q$ with the default parameters $D = $ `defaultD a`, $\kappa = $ `defaultκ a`, $S = $ `defaultS X` and $o = $ `cancelPt X`. Under these assumptions, if $u \in \mathfrak{U}_3(k,n,j)$ and $p \in \mathfrak{T}_2(k,n,j,u)$, then $B(c(p), 8 D^{s(p)}) \subseteq \mathcal{I}(u)$, where $D$ is `defaultD a`, $c(p)=𝔠 p$ and $s(p) = 𝔰 p$.
Checker's issue: k, n, j (natural numbers) and p, u (tiles) are not introduced with types. Parenthetical says ProofData makes X 'a doubling metric measure space with the kernel K', which the prompt does not support.

### `forest_separation`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ 𝔘₃ k n j) (hu' : u' ∈ 𝔘₃ k n j) (huu' : u ≠ u') (hp : p ∈ 𝔗₂ k n j u') (h : 𝓘 p ≤ 𝓘 u) : 2 ^ (defaultZ a * (n + 1)) < dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) (𝒬 u)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {k n j : ℕ} {p u u' : 𝔓 X}, Membership.mem (γ := Set (𝔓 X)) (𝔘₃ (F := F) (G := G) k n j) u → Membership.mem (γ := Set (𝔓 X)) (𝔘₃ (F := F) (G := G) k n j) u' → u ≠ u' → p ∈ 𝔗₂ (F := F) (G := G) k n j u' → 𝓘 p ≤ 𝓘 u → (2 : ℝ) ^ (defaultZ a * (n + (1 : ℕ))) < dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) (𝒬 u)`
Docstring: Lemma 5.4.6, verifying (2.0.36) Note: swapped `u` and `u'` to match (2.0.36)
Previous English: (Lemma 5.4.6, verifying (2.0.36)) Let $X$ be a metric space and assume the standing assumptions of the proof: the `ProofData` bundle for the data $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \times X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$ (making $X$ a doubling metric measure space with the kernel $K$), together with a tile structure (`TileStructure`) for $Q$ with the default parameters $D = $ `defaultD a`, $\kappa = $ `defaultκ a`, $S = $ `defaultS X` and $o = $ `cancelPt X`. Under these assumptions, let $u, u' \in \mathfrak{U}_3(k,n,j)$ with $u \ne u'$, let $p \in \mathfrak{T}_2(k,n,j,u')$, and suppose $\mathcal{I}(p) \le \mathcal{I}(u)$. Then $$2^{Z(n+1)} < d_{c(p),\, D^{s(p)}/4}(\mathcal{Q}(p), \mathcal{Q}(u)),$$ where $Z$ is `defaultZ a` and $D$ is `defaultD a`.
Checker's issue: k, n, j, p, u, u' have no stated types. The notation d_{c,r} and the map Q(p) are not introduced. Parenthetical says ProofData makes X 'a doubling metric measure space with the kernel K', which the prompt does not support.

### `carlesonSum_ℭ₆_eq_sum`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hkn : k ≤ n) : carlesonSum (ℭ₆ k n j) f x = ∑ l < 4 * n + 12, carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {f : X → ℂ} {x : X} {k n j : ℕ}, k ≤ n → carlesonSum (F := F) (G := G) (ℭ₆ (F := F) (G := G) k n j) f x = ∑ l < (4 : ℕ) * n + (12 : ℕ), carlesonSum (F := F) (G := G) (⋃ (u : 𝔓 X), ⋃ (_ : Membership.mem (γ := Set (𝔓 X)) (𝔘₄ (F := F) (G := G) k n j l) u), 𝔗₂ (F := F) (G := G) k n j u) f x`
Docstring: The Carleson sum over `ℭ₆` can be decomposed as a sum over `4 n + 12` forests based on `𝔘₄ k n j l`.
Previous English: Let $X$ be a metric space and assume the standing assumptions of the proof: the `ProofData` bundle for the data $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \times X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$ (making $X$ a doubling metric measure space with the kernel $K$), together with a tile structure (`TileStructure`) for $Q$ with the default parameters $D = $ `defaultD a`, $\kappa = $ `defaultκ a`, $S = $ `defaultS X` and $o = $ `cancelPt X`. Under these assumptions, if $k \le n$, then for all $x$, $$\mathrm{carlesonSum}(\mathfrak{C}_6(k,n,j), f)(x) = \sum_{l < 4n+12} \mathrm{carlesonSum}\Big(\bigcup_{u \in \mathfrak{U}_4(k,n,j,l)} \mathfrak{T}_2(k,n,j,u), f\Big)(x).$$
Checker's issue: f : X -> C and the natural numbers k, n, j are not introduced. Parenthetical says ProofData makes X 'a doubling metric measure space with the kernel K', which the prompt does not support.

### `lintegral_carlesonSum_forest`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * (2 ^ (2 * a + 5) * volume F / volume G) ^ (q⁻¹ - 2⁻¹) * volume F ^ (1 / 2) * volume G ^ (1 / 2)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {k n j l : ℕ} {f : X → ℂ}, Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (⋃ (u : 𝔓 X), ⋃ (_ : Membership.mem (γ := Set (𝔓 X)) (𝔘₄ (F := F) (G := G) k n j l) u), 𝔗₂ (F := F) (G := G) k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * HDiv.hDiv (β := ENNReal) (HMul.hMul (β := ENNReal) ((2 : ENNReal) ^ ((2 : ℕ) * a + (5 : ℕ))) ((volume : Measure X) F : ENNReal)) ((volume : Measure X) G : ENNReal) ^ (q⁻¹ - (2 : ℝ)⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (1 / 2 : ℝ) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) (1 / 2 : ℝ)`
Docstring: For each forest, the integral of the norm of the Carleson sum can be controlled thanks to the forest theorem and to the density control coming from the fact we are away from `G₁`.
Previous English: Let $X$ be a metric space and assume the standing assumptions of the proof: the `ProofData` bundle for the data $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \times X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$ (making $X$ a doubling metric measure space with the kernel $K$), together with a tile structure (`TileStructure`) for $Q$ with the default parameters $D = $ `defaultD a`, $\kappa = $ `defaultκ a`, $S = $ `defaultS X` and $o = $ `cancelPt X`. Under these assumptions, let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $$\int_{G\setminus G'} \Big\|\mathrm{carlesonSum}\Big(\bigcup_{u \in \mathfrak{U}_4(k,n,j,l)} \mathfrak{T}_2(k,n,j,u), f\Big)(x)\Big\|\,dx \le C_{2.0.4}(a,q,n) \Big(\frac{2^{2a+5}\mu(F)}{\mu(G)}\Big)^{1/q - 1/2} \mu(F)^{1/2}\, \mu(G)^{1/2}.$$
Checker's issue: The type of f (X -> C) and the natural numbers k, n, j, l are not stated. G' and mu are not introduced. Parenthetical says ProofData makes X 'a doubling metric measure space with the kernel K', which the prompt does not support.

### `lintegral_carlesonSum_forest'`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * 2 ^ (↑a + 5 / 2) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {k n j l : ℕ} {f : X → ℂ}, Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (⋃ (u : 𝔓 X), ⋃ (_ : Membership.mem (γ := Set (𝔓 X)) (𝔘₄ (F := F) (G := G) k n j l) u), 𝔗₂ (F := F) (G := G) k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * (2 : ENNReal) ^ (↑a + (5 / 2 : ℝ)) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹`
Docstring: For each forest, the integral of the norm of the Carleson sum can be controlled thanks to the forest theorem and to the density control coming from the fact we are away from `G₁`. Second version, with the volume of `F`.
Previous English: Let $X$ be a metric space and assume the standing assumptions of the proof: the `ProofData` bundle for the data $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \times X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$ (making $X$ a doubling metric measure space with the kernel $K$), together with a tile structure (`TileStructure`) for $Q$ with the default parameters $D = $ `defaultD a`, $\kappa = $ `defaultκ a`, $S = $ `defaultS X` and $o = $ `cancelPt X`. Under these assumptions, let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x$. Then $$\int_{G\setminus G'} \Big\|\mathrm{carlesonSum}\Big(\bigcup_{u \in \mathfrak{U}_4(k,n,j,l)} \mathfrak{T}_2(k,n,j,u), f\Big)(x)\Big\|\,dx \le C_{2.0.4}(a,q,n)\, 2^{a+5/2}\, \mu(G)^{1-1/q}\, \mu(F)^{1/q}.$$
Checker's issue: The type of f (X -> C) and the natural numbers k, n, j, l are not stated. G' and mu are not introduced. Parenthetical says ProofData makes X 'a doubling metric measure space with the kernel K', which the prompt does not support.

### `forest_union_optimized`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C5_1_2_optimized a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {f : X → ℂ}, (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable f → ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (𝔓₁ (F := F) (G := G)) f x‖ₑ ≤ ↑(C5_1_2_optimized a (nnq X (F := F) (G := G))) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹`
Docstring: Version of the forest union result with a better constant.
Previous English: Let $X$ be a metric space and assume the standing assumptions of the proof: the `ProofData` bundle for the data $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \times X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$ (making $X$ a doubling metric measure space with the kernel $K$), together with a tile structure (`TileStructure`) for $Q$ with the default parameters $D = $ `defaultD a`, $\kappa = $ `defaultκ a`, $S = $ `defaultS X` and $o = $ `cancelPt X`. Under these assumptions, let $f$ be measurable with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Then $$\int_{G\setminus G'} \|\mathrm{carlesonSum}(\mathfrak{P}_1, f)(x)\|\,dx \le C^{\mathrm{opt}}_{5.1.2}(a,q)\, \mu(G)^{1-1/q}\, \mu(F)^{1/q},$$ where $C^{\mathrm{opt}}_{5.1.2}$ is `C5_1_2_optimized` and $q$ is `nnq X`.
Checker's issue: The codomain of f is not stated. G', P_1 and mu are not introduced. The letter q is used both for the real parameter and for nnq X. Parenthetical says ProofData makes X 'a doubling metric measure space with the kernel K', which the prompt does not support.
