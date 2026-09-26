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

#### `CompatibleFunctions.toFunctionDistances` (def)
Lean: `{𝕜 : outParam (Type u_3)} → {X : Type u} → {A : outParam ℕ} → {inst : RCLike 𝕜} → {inst_1 : PseudoMetricSpace X} → [self : CompatibleFunctions 𝕜 X A] → FunctionDistances 𝕜 X`
Definition: `fun {𝕜 : outParam (Type u_3)} (X : Type u) {A : outParam ℕ} {inst : RCLike 𝕜} {inst_1 : PseudoMetricSpace X} [self : CompatibleFunctions 𝕜 X A] => self.1`

#### `Grid` (def)
Lean: `(X : Type u) → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [GridStructure X D κ S o] → Type u`
Docstring: The indexing type of the grid structure. Elements are called (dyadic) cubes. Note that this type has instances for both `≤` and `⊆`, but they do *not* coincide.
Definition: `fun (X : Type u) {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => @GridStructure.Grid X _ inst inst_1 _ _ _ _ _`

#### `KernelProofData.cf` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → {inst : PseudoMetricSpace X} → [self : KernelProofData a K] → CompatibleFunctions ℝ X (defaultA a)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {K : outParam (X → X → ℂ)} {inst : PseudoMetricSpace X} [self : KernelProofData a K] => self.3`

#### `KernelProofData.d` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → {inst : PseudoMetricSpace X} → [self : KernelProofData a K] → DoublingMeasure X ↑(defaultA a)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {K : outParam (X → X → ℂ)} {inst : PseudoMetricSpace X} [self : KernelProofData a K] => self.1`

#### `PreTileStructure.toGridStructure` (def)
Lean: `(𝕜 : Type u_1) → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → GridStructure.{u_2, u} X D κ S o`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.1`

#### `ProofData` (structure or class)
Lean: `{X : Type u_1} → outParam ℕ → outParam ℝ → outParam (X → X → ℂ) → outParam (X → ℤ) → outParam (X → ℤ) → outParam (Set X) → outParam (Set X) → [PseudoMetricSpace X] → Type (u_1 + 1)`
Docstring: Data common through most of chapters 2-7 (except 3).
Constructor (every field with its type): `{X : Type u_1} → {a : outParam ℕ} → {q : outParam ℝ} → {K : outParam (X → X → ℂ)} → {σ₁ σ₂ : outParam (X → ℤ)} → {F G : outParam (Set X)} → [inst : PseudoMetricSpace X] → [toKernelProofData : KernelProofData a K] → IsCancellative X (defaultτ a) → q ∈ Set.Ioc (1 : outParam ℝ) (2 : outParam ℝ) → Bornology.IsBounded F → Bornology.IsBounded G → MeasurableSet F → MeasurableSet G → Measurable σ₁ → Measurable σ₂ → Finite ↑(Set.range σ₁) → Finite ↑(Set.range σ₂) → σ₁ ≤ σ₂ → (Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)) → (∀ (θ : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), HasBoundedStrongType (ε₁ := ℂ) (ε₂ := ENNReal) (α := X) (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (fun (x1 : X → ℂ) (x2 : X) => linearizedNontangentialOperator (⇑Q) θ K x1 x2) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → ProofData a q K σ₁ σ₂ F G`

#### `ProofData.Q` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {q : outParam ℝ} → {K : outParam (X → X → ℂ)} → {σ₁ σ₂ : outParam (X → ℤ)} → {F G : outParam (Set X)} → {inst : PseudoMetricSpace X} → [self : ProofData a q K σ₁ σ₂ F G] → SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {q : outParam ℝ} {K : outParam (X → X → ℂ)} {σ₁ σ₂ : outParam (X → ℤ)} {F G : outParam (Set X)} {inst : PseudoMetricSpace X} [self : ProofData a q K σ₁ σ₂ F G] => self.13`

#### `ProofData.toKernelProofData` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {q : outParam ℝ} → {K : outParam (X → X → ℂ)} → {σ₁ σ₂ : outParam (X → ℤ)} → {F G : outParam (Set X)} → {inst : PseudoMetricSpace X} → [self : ProofData a q K σ₁ σ₂ F G] → KernelProofData a K`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {q : outParam ℝ} {K : outParam (X → X → ℂ)} {σ₁ σ₂ : outParam (X → ℤ)} {F G : outParam (Set X)} {inst : PseudoMetricSpace X} [self : ProofData a q K σ₁ σ₂ F G] => self.1`

#### `TileStructure` (structure or class)
Lean: `{X : Type u} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → [inst_2 : FunctionDistances ℝ X] → outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _)) → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (u + 1)`
Docstring: A tile structure.
Constructor (every field with its type): `{X : Type u} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → [inst_2 : FunctionDistances ℝ X] → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [toPreTileStructure : PreTileStructure Q D κ S o] → (Ω : PreTileStructure.𝔓 ℝ X → Set (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _)) → (∀ {i : @GridStructure.Grid X _ inst inst_1 _ _ _ _ _}, Set.range (ι := X) ⇑Q ⊆ ⋃ (p : PreTileStructure.𝔓 ℝ X), ⋃ (_ : Membership.mem (γ := Set (PreTileStructure.𝔓 ℝ X)) (PreTileStructure.𝓘 ⁻¹' {i}) p), Ω p) → (∀ {p p' : PreTileStructure.𝔓 ℝ X}, p ≠ p' → PreTileStructure.𝓘 p = PreTileStructure.𝓘 p' → Disjoint (Ω p) (Ω p')) → (∀ {p p' : 𝔓 X}, 𝓘 p ≤ 𝓘 p' → Disjoint (Ω p) (Ω p') ∨ Ω p' ⊆ Ω p) → (∀ {p : 𝔓 X}, ball_{𝔠 p, ↑D ^ 𝔰 p / (4 : ℝ)} (𝒬 p) (5 : ℝ)⁻¹ ⊆ Ω p) → (∀ {p : 𝔓 X}, Ω p ⊆ ball_{𝔠 p, ↑D ^ 𝔰 p / (4 : ℝ)} (𝒬 p) (1 : ℝ)) → TileStructure Q D κ S o`

#### `TileStructure.toPreTileStructure` (def)
Lean: `{X : Type u} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {inst_2 : FunctionDistances ℝ X} → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : TileStructure Q D κ S o] → PreTileStructure Q D κ S o`
Definition: `fun (X : Type u) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {inst_2 : FunctionDistances ℝ X} {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : TileStructure Q D κ S o] => self.1`

#### `c` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Grid X → X`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.c`

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

#### `GridStructure.coeGrid` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → Set X`
Docstring: The collection of dyadic cubes
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.3`

#### `s` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Grid X → ℤ`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.s`

#### `𝓘` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → Grid X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] => PreTileStructure.𝓘`

#### `𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → (X : Type u) → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [PreTileStructure.{u, u_1, u_2} Q D κ S o] → Type u`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] (X : Type u) {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X`

#### `instPartialOrderGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → PartialOrder (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => PartialOrder.lift (fun (i : @GridStructure.Grid X _ inst inst_1 _ _ _ _ _) => (↑i, GridStructure.s i)) ⋯`

#### `TileStructure.Forest` (structure or class)
Lean: `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → Type u_1`
Docstring: An `n`-forest
Constructor (every field with its type): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → (𝔘 : Set (𝔓 X)) → (𝔗 : 𝔓 X → Set (𝔓 X)) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → (𝔗 u).Nonempty) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → (𝔗 u).OrdConnected) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → ∀ {p : 𝔓 X}, p ∈ 𝔗 u → 𝓘 p ≠ 𝓘 u) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → ∀ {p : 𝔓 X}, p ∈ 𝔗 u → smul (F := F) (G := G) (4 : ℝ) p ≤ smul (F := F) (G := G) (1 : ℝ) u) → (∀ {x : X}, stackSize (F := F) (G := G) 𝔘 x ≤ (2 : ℕ) ^ n) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → dens₁ (F := F) (G := G) (𝔗 u) ≤ (2 : ENNReal) ^ ((4 : ℝ) * ↑a - ↑n + (1 : ℝ))) → (∀ {u u' : 𝔓 X}, u ∈ 𝔘 → u' ∈ 𝔘 → u ≠ u' → ∀ {p : 𝔓 X}, p ∈ 𝔗 u' → 𝓘 p ≤ 𝓘 u → (2 : ℝ) ^ (defaultZ a * (n + (1 : ℕ))) < dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) (𝒬 u)) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → ∀ {p : 𝔓 X}, p ∈ 𝔗 u → Metric.ball (𝔠 p) ((8 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p)) ⊆ ↑(𝓘 u)) → Forest X (F := F) (G := G) n`

#### `TileStructure.Forest.ijIntegral` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → (X → ℂ) → Grid X → Grid X → ENNReal`
Docstring: Scaled integral appearing in the definition of `boundaryOperator`.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (f : X → ℂ) (I J : Grid X) => HDiv.hDiv (β := ENNReal) (HPow.hPow (α := ENNReal) (↑(defaultD a)) (HSub.hSub (α := ℝ) ↑(s J) ↑(s I) / ↑a)) ((volume : Measure X) (Metric.ball (c I) ((16 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (s I))) : ENNReal) * ∫⁻ (y : X) in ↑J, ‖f y‖ₑ`

#### `TileStructure.Forest.𝓙'` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → 𝔓 X → X → ℤ → Finset (Grid X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (t : Forest X (F := F) (G := G) n) (u : 𝔓 X) (x : X) (i : ℤ) => {J : Grid X | Membership.mem (γ := Set (Grid X)) (Forest.𝓙 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) J ∧ ↑J ⊆ Metric.ball x ((16 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) i) ∧ s J ≤ i}`

#### `instFintypeGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Fintype (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.fintype_Grid`

#### `MeasureTheory.DoublingMeasure.toMeasureSpace` (def)
Lean: `{X : Type u_3} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → [self : DoublingMeasure X A] → MeasureSpace X`
Definition: `fun (X : Type u_3) {A : outParam NNReal} {inst : PseudoMetricSpace X} [self : DoublingMeasure X A] => self.3`

#### `FunctionDistances.Θ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → (X : Type u) → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → Type u`
Docstring: A type of continuous functions from `X` to `𝕜`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.1`

#### `MeasureTheory.BoundedCompactSupport` (inductive)
Lean: `{X : Type u_1} → {E : Type u_2} → [TopologicalSpace X] → [inst : MeasurableSpace X] → [TopologicalSpace E] → [ENorm E] → [Zero E] → (X → E) → autoParam (Measure X) BoundedCompactSupport._auto_1 → Prop`
Docstring: Bounded compactly supported measurable functions
Constructor (every field with its type): `∀ {X : Type u_1} {E : Type u_2} [inst : TopologicalSpace X] [inst_1 : MeasurableSpace X] [inst_2 : TopologicalSpace E] [inst_3 : ENorm E] [inst_4 : Zero E] {f : X → E} {μ : autoParam (Measure X) BoundedCompactSupport._auto_1}, MemLp f ⊤ μ → HasCompactSupport f → BoundedCompactSupport f μ`

#### `PreTileStructure.𝒬` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X → @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.6`

#### `TileStructure.Forest.C7_1_3` (def)
Lean: `ℕ → NNReal`
Docstring: The constant used in `pointwise_tree_estimate`. Has value `2 ^ (129 * a ^ 3)` in the blueprint.
Definition: `Forest.wrapped✝.1`

#### `TileStructure.Forest.instMembership𝔓Real` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Membership (𝔓 X) (Forest X (F := F) (G := G) n)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} => { mem := fun (t : Forest X (F := F) (G := G) n) (x : 𝔓 X) => x ∈ t.𝔘 (F := F) (G := G) }`

#### `TileStructure.Forest.nontangentialMaximalFunction` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _ → (X → ℂ) → X → ENNReal`
Docstring: The definition `T_𝓝^θ f(x)`, given in (7.1.3). For convenience, the suprema are written a bit differently than in the blueprint (avoiding `cubeOf`), but this should be equivalent. This is `0` if `x` doesn't lie in a cube.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (θ : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) (f : X → ℂ) (x : X) => ⨆ (I : Grid X), ⨆ (_ : x ∈ I), ⨆ x' ∈ I, ⨆ s₂ ∈ Set.Icc (s I) ↑(defaultS X (F := F) (G := G)), ⨆ (_ : ENNReal.ofReal (HPow.hPow (α := ℝ) (↑(defaultD a)) (s₂ - (1 : ℤ))) ≤ upperRadius (⇑(Q (F := F) (G := G))) θ x'), enorm (E := ℂ) (∑ i ∈ (Set.Icc (s I) s₂).toFinset, @integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => Ks i x' y * f y)`

#### `TileStructure.Forest.𝓛` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → Set (Grid X)`
Docstring: The definition of `𝓛(𝔖), defined above Lemma 7.1.2
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔖 : Set (𝔓 X)) => {x : Grid X | Maximal (fun (x : Grid X) => x ∈ Forest.𝓛₀ (F := F) (G := G) 𝔖) x}`

#### `TileStructure.Forest.𝔗` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → 𝔓 X → Set (𝔓 X)`
Docstring: The value of `𝔗 u` only matters when `u ∈ 𝔘`.
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] (a : ℕ) (q : ℝ) (K : X → X → ℂ) (σ₁ σ₂ : X → ℤ) (F G : Set X) [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (n : ℕ) (self : Forest X (F := F) (G := G) n) => self.2`

#### `carlesonSum` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → (X → ℂ) → X → ℂ`
Docstring: The operator `T_ℭ f` defined at the bottom of Section 7.4. We will use this in other places of the formalization as well.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [PseudoMetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) => ∑ p : 𝔓 X with p ∈ ℭ, carlesonOn (F := F) (G := G) p f x`

#### `instFunLikeΘ` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → FunLike (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) X 𝕜`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] => DFunLike.mk (β := fun (x : X) => 𝕜) (fun (f : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) => ⇑(coeΘ f)) ⋯`

#### `instMembershipGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Membership X (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => { mem := fun (i : Grid X) (x : X) => x ∈ ↑i }`

#### `maximalFunction` (def)
Lean: `{X : Type u_1} → {ε : Type u_2} → [PseudoMetricSpace X] → [inst : MeasurableSpace X] → [ENorm ε] → {ι : Type u_4} → Measure X → Set ι → (ι → X) → (ι → ℝ) → ℝ → (X → ε) → X → ENNReal`
Docstring: The uncentered Hardy-Littlewood maximal function, for a family of balls.
Definition: `fun {X : Type u_1} {ε : Type u_2} [PseudoMetricSpace X] [MeasurableSpace X] [ENorm ε] {ι : Type u_4} (μ : Measure X) (𝓑 : Set ι) (c : ι → X) (r : ι → ℝ) (p : ℝ) (u : X → ε) (x : X) => ⨆ i ∈ 𝓑, (Metric.ball (c i) (r i)).indicator (fun (x : X) => (⨍⁻ (y : X) in Metric.ball (c i) (r i), ‖u y‖ₑ ^ p ∂μ) ^ p⁻¹) x`

#### `E` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → Set X`
Docstring: The set `E` defined in Proposition 2.0.2.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) => {x : X | x ∈ 𝓘 p ∧ Membership.mem (α := @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) (Ω p) ((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) ∧ 𝔰 p ∈ Set.Icc (σ₁ x) (σ₂ x)}`

#### `Ks` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {K : X → X → ℂ} → [inst : PseudoMetricSpace X] → [KernelProofData a K] → ℤ → X → X → ℂ`
Docstring: K_s in the blueprint
Definition: `fun {X : Type u_1} {a : ℕ} {K : X → X → ℂ} [PseudoMetricSpace X] [KernelProofData a K] (s : ℤ) (x y : X) => K x y * ↑(ψ (defaultD a) (HPow.hPow (α := ℝ) (↑(defaultD a)) (-s) * dist x y))`

#### `TileStructure.Forest.C7_1_4` (def)
Lean: `ℕ → NNReal`
Docstring: The constant used in `first_tree_pointwise`. Has value `10 * 2 ^ (104 * a ^ 3)` in the blueprint.
Definition: `Forest.wrapped✝.1`

#### `TileStructure.Forest.σ` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → 𝔓 X → X → Finset ℤ`
Docstring: The definition `σ(u, x)` given in Section 7.1. We may assume `u ∈ t` whenever proving things about this definition.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (t : Forest X (F := F) (G := G) n) (u : 𝔓 X) (x : X) => Finset.image (α := 𝔓 X) 𝔰 {p : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) p ∧ x ∈ E (F := F) (G := G) p}`

#### `𝔰` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → ℤ`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => s (𝓘 p)`

#### `TileStructure.Forest.C7_1_6` (def)
Lean: `ℕ → NNReal`
Docstring: The constant used in `third_tree_pointwise`. Has value `2 ^ (128 * a ^ 3)` in the blueprint.
Definition: `Forest.wrapped✝.1`

#### `CompatibleFunctions` (structure or class)
Lean: `(𝕜 : outParam (Type u_3)) → (X : Type u) → outParam ℕ → [RCLike 𝕜] → [PseudoMetricSpace X] → Type (max (u + 1) u_3)`
Docstring: A set `Θ` of (continuous) functions is compatible. `A` will usually be `2 ^ a`.
Constructor (every field with its type): `{𝕜 : outParam (Type u_3)} → {X : Type u} → {A : outParam ℕ} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [toFunctionDistances : FunctionDistances 𝕜 X] → (∃ (o : X), ∀ (f : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), (coeΘ f) o = (0 : 𝕜)) → (∀ {x : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, localOscillation (Metric.ball x r) (coeΘ f) (coeΘ g) ≤ ENNReal.ofReal (dist_{x, r} f g)) → (∀ {x₁ x₂ : X} {r₁ r₂ : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, Metric.ball x₁ r₁ ⊆ Metric.ball x₂ r₂ → dist_{x₁, r₁} f g ≤ dist_{x₂, r₂} f g) → (∀ {x₁ x₂ : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, dist x₁ x₂ < (2 : ℝ) * r → dist_{x₂, (2 : ℝ) * r} f g ≤ ↑A * dist_{x₁, r} f g) → (∀ {x₁ x₂ : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, Metric.ball x₁ r ⊆ Metric.ball x₂ (↑A * r) → (2 : ℝ) * dist_{x₁, r} f g ≤ dist_{x₂, ↑A * r} f g) → (∀ {x : X} {r : ℝ}, AllBallsCoverBalls.{u} (WithFunctionDistance x r) (2 : ℝ) A) → CompatibleFunctions 𝕜 X A`

#### `FunctionDistances` (structure or class)
Lean: `(𝕜 : outParam (Type u_1)) → (X : Type u) → [NormedField 𝕜] → [TopologicalSpace X] → Type (max (u + 1) u_1)`
Docstring: A class stating that continuous functions have distances associated to every ball. We use a separate type to conveniently index these functions.
Constructor (every field with its type): `{𝕜 : outParam (Type u_1)} → {X : Type u} → [inst : NormedField 𝕜] → [inst_1 : TopologicalSpace X] → (Θ : Type u) → (coeΘ : Θ → C(X, 𝕜)) → (∀ {f g : Θ}, (∀ (x : X), Eq.{u_1 + 1} (α := 𝕜) ((coeΘ f) x : 𝕜) ((coeΘ g) x : 𝕜)) → f = g) → (X → ℝ → PseudoMetricSpace Θ) → FunctionDistances 𝕜 X`

#### `GridStructure` (structure or class)
Lean: `(X : Type u_2) → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [DoublingMeasure X A] → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (max (u + 1) u_2)`
Docstring: A grid structure on `X`. We prefer `coeGrid : Grid → Set X` over `Grid : Set (Set X)` Note: the `s` in this paper is `-s` of Christ's paper.
Constructor (every field with its type): `{X : Type u_2} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → (Grid : Type u) → Fintype Grid → (coeGrid : Grid → Set X) → (s : Grid → ℤ) → (c : Grid → X) → (Function.Injective.{u + 1, max 1 (u_2 + 1)} (β := Set X × ℤ) fun (i : Grid) => (coeGrid i, s i)) → Set.range s ⊆ Set.Icc (-↑S) ↑S → (topCube : Grid) → s topCube = ↑S → c topCube = o → (∀ {i : Grid}, coeGrid i ⊆ coeGrid topCube) → (∀ {i : Grid}, ∀ k ∈ Set.Ico (-↑S) (s i), coeGrid i ⊆ ⋃ j ∈ s ⁻¹' {k}, coeGrid j) → (∀ {i j : Grid}, s i ≤ s j → coeGrid i ⊆ coeGrid j ∨ Disjoint (coeGrid i) (coeGrid j)) → (∀ {i : Grid}, Metric.ball (c i) (HPow.hPow (α := ℝ) (↑D) (s i) / (4 : ℝ)) ⊆ coeGrid i) → (∀ {i : Grid}, coeGrid i ⊆ Metric.ball (c i) ((4 : ℝ) * HPow.hPow (α := ℝ) (↑D) (s i))) → (∀ {i : Grid} {t : NNReal}, HPow.hPow (α := NNReal) (↑D) (-↑S - s i) ≤ t → Measure.real.{u_2} (α := X) (m := MeasureSpace.toMeasurableSpace) volume {x : X | x ∈ coeGrid i ∧ Metric.infEDist x (coeGrid i)ᶜ ≤ ↑t * HPow.hPow (α := ENNReal) (↑D) (s i)} ≤ (2 : ℝ) * ↑t ^ κ * Measure.real (m := MeasureSpace.toMeasurableSpace) volume (coeGrid i)) → (∀ {i : Grid}, MeasurableSet (coeGrid i)) → GridStructure.{u, u_2} X D κ S o`

#### `GridStructure.Grid` (def)
Lean: `(X : Type u_2) → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → Type u`
Docstring: indexing set for a grid structure
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.1`

#### `MeasureTheory.DoublingMeasure` (structure or class)
Lean: `(X : Type u_3) → outParam NNReal → [PseudoMetricSpace X] → Type u_3`
Docstring: A metric space with a measure with some nice properties, including a doubling condition. This is called a "doubling metric measure space" in the blueprint. `A` will usually be `2 ^ a`.
Constructor (every field with its type): `{X : Type u_3} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [toCompleteSpace : CompleteSpace X] → [toLocallyCompactSpace : LocallyCompactSpace X] → [toMeasureSpace : MeasureSpace X] → [toBorelSpace : BorelSpace X] → [toIsLocallyFiniteMeasure : IsLocallyFiniteMeasure.{u_3} (α := X) (m0 := MeasureSpace.toMeasurableSpace) volume] → [toIsDoubling : Measure.IsDoubling.{u_3} (X := X) volume A] → [toNeZero : NeZero.{u_3} (R := Measure X) volume] → DoublingMeasure X A`

#### `KernelProofData` (structure or class)
Lean: `{X : Type u_1} → outParam ℕ → outParam (X → X → ℂ) → [PseudoMetricSpace X] → Type (u_1 + 1)`
Docstring: Data common through most of chapters 2 through 7. These contain the minimal axioms for `kernel-summand`'s proof. This is used in Chapter 3 when we don't have all other fields from `ProofData`.
Constructor (every field with its type): `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → [inst : PseudoMetricSpace X] → (d : DoublingMeasure X ↑(defaultA a)) → (4 : ℕ) ≤ a → CompatibleFunctions ℝ X (defaultA a) → IsOneSidedKernel a K → KernelProofData a K`

#### `PreTileStructure` (structure or class)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : outParam NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → [inst_3 : FunctionDistances 𝕜 X] → outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)) → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (max (u + 1) (u_2 + 1))`
Constructor (every field with its type): `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : outParam NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → [inst_3 : FunctionDistances 𝕜 X] → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [toGridStructure : GridStructure.{u_2, u} X D κ S o] → (𝔓 : Type u) → Fintype 𝔓 → (𝓘 : 𝔓 → @GridStructure.Grid X _ inst_1 inst_2 _ _ _ _ _) → Function.Surjective 𝓘 → (𝒬 : 𝔓 → @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) → Set.range 𝒬 ⊆ Set.range (ι := X) ⇑Q → PreTileStructure.{u, u_1, u_2} Q D κ S o`

#### `C_Ts` (def)
Lean: `ℕ → NNReal`
Docstring: A constant used on the boundedness of `T_Q^θ` and `T_*`. We generally assume `HasBoundedStrongType (linearizedNontangentialOperator Q θ K · ·) 2 2 volume volume (C_Ts a)` throughout this formalization.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ a ^ (3 : ℕ)`

#### `IsCancellative` (structure or class)
Lean: `(X : Type u_2) → {A : ℕ} → [inst : PseudoMetricSpace X] → [DoublingMeasure X ↑A] → ℝ → [CompatibleFunctions ℝ X A] → Prop`
Docstring: Θ is τ-cancellative. `τ` will usually be `1 / a`
Constructor (every field with its type): `∀ {X : Type u_2} {A : ℕ} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X ↑A] {τ : ℝ} [inst_2 : CompatibleFunctions ℝ X A], (∀ {x : X} {r : ℝ} {φ : X → ℂ}, (0 : ℝ) < r → iLipENorm φ x r ≠ ⊤ → Function.support φ ⊆ Metric.ball x r → ∀ {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => Complex.exp (Complex.I * (↑(f x) - ↑(g x))) * φ x) ≤ HMul.hMul (α := ENNReal) (β := ENNReal) (↑A : ENNReal) ((volume : Measure X) (Metric.ball x r) : ENNReal) * iLipENorm φ x r * ((1 : ENNReal) + edist_{x, r} f g) ^ (-τ)) → IsCancellative X τ`

#### `IsOneSidedKernel` (structure or class)
Lean: `{X : Type u_1} → [PseudoMetricSpace X] → [MeasureSpace X] → outParam ℕ → (X → X → ℂ) → Prop`
Docstring: `K` is a one-sided Calderon-Zygmund kernel. In the formalization `K x y` is defined everywhere, even for `x = y`. The assumptions on `K` show that `K x x = 0`.
Constructor (every field with its type): `∀ {X : Type u_1} [inst : PseudoMetricSpace X] [inst_1 : MeasureSpace X] {a : outParam ℕ} {K : X → X → ℂ}, Measurable (Function.uncurry K) → (∀ (x y : X), ‖K x y‖ ≤ ↑(C_K ↑a) / Real.vol x y) → (∀ {x y y' : X}, (2 : ℝ) * dist y y' ≤ dist x y → ‖K x y - K x y'‖ ≤ HPow.hPow (β := ℝ) (dist y y' / dist x y) (↑a)⁻¹ * (↑(C_K ↑a) / Real.vol x y)) → IsOneSidedKernel a K`

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

#### `𝔠` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => c (𝓘 p)`

#### `TileStructure.Ω` (def)
Lean: `{X : Type u} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {inst_2 : FunctionDistances ℝ X} → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : TileStructure Q D κ S o] → PreTileStructure.𝔓 ℝ X → Set (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _)`
Definition: `fun (X : Type u) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {inst_2 : FunctionDistances ℝ X} {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : TileStructure Q D κ S o] => self.2`

#### `GridStructure.c` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → X`
Docstring: Center functions
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.5`

#### `FunctionDistances.coeΘ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → @Θ _ X inst inst_1 _ → C(X, 𝕜)`
Docstring: The coercion map from `Θ` to `C(X, 𝕜)`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.2`

#### `𝕔` (def)
Lean: `ℕ`
Docstring: The main constant in the blueprint, driving all the construction, is `D = 2 ^ (100 * a ^ 2)`. It turns out that the proof is robust, and works for other values of `100`, giving better constants in the end. We will formalize it using a parameter `𝕔` (that we fix equal to `100` to follow the blueprint) and having `D = 2 ^ (𝕔 * a ^ 2)`. We register two lemmas `seven_le_c` and `c_le_100` and will never unfold `𝕔` from this point on.
Definition: `wrapped✝.1`

#### `GridStructure.s` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → ℤ`
Docstring: scale functions
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.4`

#### `TileLike` (def)
Lean: `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Type u_1`
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => Grid X × (Set (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))ᵒᵈ`

#### `defaultZ` (def)
Lean: `ℕ → ℕ`
Docstring: The constant `Z` from (2.0.3).
Definition: `fun (a : ℕ) => (2 : ℕ) ^ ((12 : ℕ) * a)`

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

#### `GridStructure.fintype_Grid` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → Fintype (@GridStructure.Grid X _ inst inst_1 _ _ _ _ _)`
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.2`

#### `upperRadius` (def)
Lean: `{X : Type u_2} → [inst : PseudoMetricSpace X] → [inst_1 : FunctionDistances ℝ X] → (X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _ → X → ENNReal`
Docstring: `R_Q(θ, x)` defined in (1.1.17).
Definition: `fun {X : Type u_2} [PseudoMetricSpace X] [FunctionDistances ℝ X] (Q : X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (θ : @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (x : X) => ⨆ (r : ℝ), ⨆ (_ : dist_{x, r} θ (Q x) < (1 : ℝ)), ENNReal.ofReal r`

#### `TileStructure.Forest.𝓛₀` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → Set (Grid X)`
Docstring: The definition of `𝓛₀(𝔖), defined above Lemma 7.1.2
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔖 : Set (𝔓 X)) => {L : Grid X | s L = -↑(defaultS X (F := F) (G := G)) ∨ (∃ p ∈ 𝔖, L ≤ 𝓘 p) ∧ ∀ p ∈ 𝔖, ¬𝓘 p ≤ L}`

#### `carlesonOn` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
Docstring: The operator `T_𝔭` defined in Proposition 2.0.2.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [PseudoMetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) => (E (F := F) (G := G) p).indicator fun (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => Complex.exp (Complex.I * (↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y) - ↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) x))) * Ks (𝔰 p) x y * f y`

#### `instFintype𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (𝔓.{u, u_1, u_2} X)`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.fintype_𝔓`

#### `ψ` (def)
Lean: `ℕ → ℝ → ℝ`
Docstring: The function `ψ` used as a basis for a dyadic partition of unity.
Definition: `fun (D : ℕ) (x : ℝ) => max (0 : ℝ) (min (1 : ℝ) (min ((4 : ℝ) * ↑D * x - (1 : ℝ)) ((2 : ℝ) - (4 : ℝ) * x)))`

#### `AllBallsCoverBalls` (def)
Lean: `(X : Type u_2) → [PseudoMetricSpace X] → ℝ → ℕ → Prop`
Docstring: For all `r`, balls of radius `r` in `X` are covered by `n` balls of radius `a * r`
Definition: `fun (X : Type u_2) [PseudoMetricSpace X] (a : ℝ) (n : ℕ) => ∀ (r : ℝ), BallsCoverBalls X (a * r) r n`

#### `localOscillation` (def)
Lean: `{𝕜 : Type u_3} → {X : Type u_4} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → Set X → C(X, 𝕜) → C(X, 𝕜) → ENNReal`
Docstring: The local oscillation of two functions w.r.t. a set `E`. This is `d_E` in the blueprint.
Definition: `fun {𝕜 : Type u_3} {X : Type u_4} [RCLike 𝕜] [PseudoMetricSpace X] (E : Set X) (f g : C(X, 𝕜)) => ⨆ z ∈ E ×ˢ E, ENNReal.ofReal ‖HAdd.hAdd (β := 𝕜) (HSub.hSub (β := 𝕜) (HSub.hSub (α := 𝕜) (β := 𝕜) (f z.1 : 𝕜) (g z.1 : 𝕜)) (f z.2 : 𝕜)) (g z.2 : 𝕜)‖`

#### `GridStructure.topCube` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _`
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.8`

#### `MeasureTheory.Measure.IsDoubling` (structure or class)
Lean: `{X : Type u_3} → [inst : MeasurableSpace X] → [PseudoMetricSpace X] → Measure X → outParam NNReal → Prop`
Docstring: A doubling measure is a measure on a metric space with the condition that doubling the radius of a ball only increases the volume by a constant factor, independent of the ball.
Constructor (every field with its type): `∀ {X : Type u_3} [inst : MeasurableSpace X] [inst_1 : PseudoMetricSpace X] {μ : Measure X} {A : outParam NNReal}, (∀ (x : X) (r : ℝ), μ (Metric.ball x ((2 : ℝ) * r)) ≤ HMul.hMul (β := ENNReal) ↑A (μ (Metric.ball x r) : ENNReal)) → μ.IsDoubling A`

#### `partialFourierSum` (def)
Lean: `ℕ → (ℝ → ℂ) → ℝ → ℂ`
Docstring: The Nᵗʰ partial Fourier sum of `f : ℝ → ℂ` for `N : ℕ`.
Definition: `fun (N : ℕ) (f : ℝ → ℂ) (x : ℝ) => ∑ n ∈ Finset.Icc (-↑N) ↑N, HMul.hMul (β := ℂ) (fourierCoeffOn Real.two_pi_pos f n) ((fourier n) ↑x : ℂ)`

#### `iLipENorm` (def)
Lean: `{𝕜 : Type u_3} → {X : Type u_4} → [NormedField 𝕜] → [PseudoMetricSpace X] → (X → 𝕜) → X → ℝ → ENNReal`
Docstring: The inhomogeneous Lipschitz norm on a ball.
Definition: `fun {𝕜 : Type u_3} {X : Type u_4} [NormedField 𝕜] [PseudoMetricSpace X] (φ : X → 𝕜) (x₀ : X) (R : ℝ) => (⨆ x ∈ Metric.ball x₀ R, ‖φ x‖ₑ) + ENNReal.ofReal R * ⨆ x ∈ Metric.ball x₀ R, ⨆ y ∈ Metric.ball x₀ R, ⨆ (_ : x ≠ y), ‖φ x - φ y‖ₑ / edist x y`

#### `C_K` (def)
Lean: `ℝ → NNReal`
Docstring: The constant used twice in the definition of the Calderon-Zygmund kernel.
Definition: `fun (a : ℝ) => (2 : NNReal) ^ a ^ (3 : ℕ)`

#### `Real.vol` (def)
Lean: `{X : Type u_1} → [PseudoMetricSpace X] → [MeasureSpace X] → X → X → ℝ`
Docstring: The "volume function" `V`. Preferably use `vol` instead.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] [MeasureSpace X] (x y : X) => Measure.real (m := MeasureSpace.toMeasurableSpace) volume (Metric.ball x (dist x y))`

#### `BoundedFiniteSupport` (structure or class)
Lean: `{X : Type u_3} → {E : Type u_4} → [inst : MeasurableSpace X] → [TopologicalSpace E] → [ENorm E] → [Zero E] → (X → E) → autoParam (Measure X) BoundedFiniteSupport._auto_1 → Prop`
Docstring: Bounded measurable function $g$ on $X$ supported on a set of finite measure
Constructor (every field with its type): `∀ {X : Type u_3} {E : Type u_4} [inst : MeasurableSpace X] [inst_1 : TopologicalSpace E] [inst_2 : ENorm E] [inst_3 : Zero E] {f : X → E} {μ : autoParam (Measure X) BoundedFiniteSupport._auto_1}, MemLp f ⊤ μ → LT.lt (α := ENNReal) (μ (Function.support f) : ENNReal) (⊤ : ENNReal) → BoundedFiniteSupport f μ`

#### `Set.EAnnulus.oo` (def)
Lean: `{X : Type u_1} → [PseudoMetricSpace X] → X → ENNReal → ENNReal → Set X`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] (x : X) (r R : ENNReal) => {y : X | edist x y ∈ Set.Ioo r R}`

#### `FunctionDistances.metric` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → X → ℝ → PseudoMetricSpace (@Θ _ X inst inst_1 _)`
Docstring: For each `_x : X` and `_r : ℝ`, a `PseudoMetricSpace Θ`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.4`

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

#### `toTileLike` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → TileLike X (F := F) (G := G)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) => (𝓘 p, Ω p)`

#### `PreTileStructure.fintype_𝔓` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X)`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.3`

## Translations

### `TileStructure.Forest.c𝓑`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (z : ℕ × ℕ × Grid X) : X`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ × ℕ × Grid X → X`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (z : ℕ × ℕ × Grid X) => c z.2.2`
Docstring: The center function for the collection of balls 𝓑.
English: Let $X$ be a metric space satisfying the standing assumptions `ProofData a q K σ₁ σ₂ F G` (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and equipped with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`. Define the function $c_{\mathcal B} : \mathbb{N} \times \mathbb{N} \times \mathrm{Grid}(X) \to X$ (pairs of natural numbers together with a grid cube, mapped to a point of $X$); according to its docstring, it is the center function for the collection of balls $\mathcal{B}$.

### `TileStructure.Forest.𝓑`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : Set (ℕ × ℕ × Grid X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (ℕ × ℕ × Grid X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => Set.Iic (defaultS X (F := F) (G := G) + (5 : ℕ)) ×ˢ SProd.sprod (β := Set (Grid X)) (Set.Iic ((2 : ℕ) * defaultS X (F := F) (G := G) + (3 : ℕ))) Set.univ`
Docstring: The indexing set for the collection of balls 𝓑, defined above Lemma 7.1.3.
English: Let $X$ be a metric space satisfying the standing assumptions `ProofData a q K σ₁ σ₂ F G` (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and equipped with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`. Define $\mathcal{B}$, a set of triples in $\mathbb{N} \times \mathbb{N} \times \mathrm{Grid}(X)$ (two natural numbers and a grid cube); according to its docstring, it is the indexing set for the collection of balls $\mathcal{B}$, defined above Lemma 7.1.3.

### `TileStructure.Forest.𝓙₀`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔖 : Set (𝔓 X)) : Set (Grid X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → Set (Grid X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔖 : Set (𝔓 X)) => {J : Grid X | s J = -↑(defaultS X (F := F) (G := G)) ∨ ∀ p ∈ 𝔖, ¬↑(𝓘 p) ⊆ Metric.ball (c J) ((100 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (s J + (1 : ℤ)))}`
Docstring: The definition of `𝓙₀(𝔖), defined above Lemma 7.1.2
English: Let $X$ be a metric space satisfying the standing assumptions `ProofData a q K σ₁ σ₂ F G` (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and equipped with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`. For a set of tiles $\mathfrak{S} \subseteq \mathfrak{P}(X)$, define a set of grid cubes $\mathcal{J}_0(\mathfrak{S}) \subseteq \mathrm{Grid}(X)$; according to its docstring, this is $\mathcal{J}_0(\mathfrak{S})$ as defined above Lemma 7.1.2.

### `TileStructure.Forest.𝓙`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔖 : Set (𝔓 X)) : Set (Grid X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → Set (Grid X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔖 : Set (𝔓 X)) => {x : Grid X | Maximal (fun (x : Grid X) => x ∈ Forest.𝓙₀ (F := F) (G := G) 𝔖) x}`
Docstring: The definition of `𝓙(𝔖), defined above Lemma 7.1.2
English: Let $X$ be a metric space satisfying the standing assumptions `ProofData a q K σ₁ σ₂ F G` (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and equipped with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`. For a set of tiles $\mathfrak{S} \subseteq \mathfrak{P}(X)$, define a set of grid cubes $\mathcal{J}(\mathfrak{S}) \subseteq \mathrm{Grid}(X)$; according to its docstring, this is $\mathcal{J}(\mathfrak{S})$ as defined above Lemma 7.1.2.

### `TileStructure.Forest.boundaryOperator`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (t : Forest X n) (u : 𝔓 X) (f : X → ℂ) (x : X) : ENNReal`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → 𝔓 X → (X → ℂ) → X → ENNReal`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (t : Forest X (F := F) (G := G) n) (u : 𝔓 X) (f : X → ℂ) (x : X) => ∑ I : Grid X, (↑I).indicator (fun (x : X) => ∑ J ∈ t.𝓙' (F := F) (G := G) u (c I) (s I), Forest.ijIntegral (F := F) (G := G) f I J) x`
Docstring: The operator `S_{1,𝔲} f(x)`, given in (7.1.4).
English: Let $X$ be a metric space satisfying the standing assumptions `ProofData a q K σ₁ σ₂ F G` (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and equipped with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`. For a natural number $n$, a forest $t$ of `Forest X n`, a tile $u \in \mathfrak{P}(X)$, a complex-valued function $f : X \to \mathbb{C}$ and a point $x \in X$, define an extended nonnegative real number $S_{1,u} f(x) \in [0, \infty]$; according to its docstring, this is the operator $S_{1,\mathfrak{u}} f(x)$ given in (7.1.4).

### `TileStructure.Forest.r𝓑`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (z : ℕ × ℕ × Grid X) : ℝ`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ × ℕ × Grid X → ℝ`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (z : ℕ × ℕ × Grid X) => (2 : ℝ) ^ z.1 * HPow.hPow (α := ℝ) (↑(defaultD a)) (s z.2.2 + ↑z.2.1)`
Docstring: The radius function for the collection of balls 𝓑.
English: Let $X$ be a metric space satisfying the standing assumptions `ProofData a q K σ₁ σ₂ F G` (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and equipped with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`. Define the real-valued function $r_{\mathcal B} : \mathbb{N} \times \mathbb{N} \times \mathrm{Grid}(X) \to \mathbb{R}$; according to its docstring, it is the radius function for the collection of balls $\mathcal{B}$.

### `TileStructure.Forest.approxOnCube`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] [NormedSpace ℝ E'] (C : Set (Grid X)) (f : X → E') (x : X) : E'`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {E' : Type u_2} → [inst_3 : NormedAddCommGroup E'] → [NormedSpace ℝ E'] → Set (Grid X) → (X → E') → X → E'`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {E' : Type u_2} [NormedAddCommGroup E'] [NormedSpace ℝ E'] (C : Set (Grid X)) (f : X → E') (x : X) => ∑ J : Grid X with J ∈ C, (↑J).indicator (fun (x : X) => ⨍ (y : X) in ↑J, f y) x`
Docstring: The projection operator `P_𝓒 f(x)`, given above Lemma 7.1.3. In lemmas the `c` will be pairwise disjoint on `C`.
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\to X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume a `ProofData a q K σ₁ σ₂ F G` instance (by its docstring, the data common through most of chapters 2–7 of the blueprint). Through its `KernelProofData` component this provides a doubling-measure structure `DoublingMeasure X (2^a)` on $X$, whose measure we denote by $\mu$ (the measure `volume`), and a `CompatibleFunctions ℝ X (2^a)` structure, hence a `FunctionDistances ℝ X` structure with its type $\Theta(X)$ (by its docstring, a type of continuous functions $X\to\mathbb R$; each $\theta\in\Theta(X)$ is applied to points of $X$ via the coercion `coeΘ`) and, for each $w\in X$ and $r\in\mathbb R$, a pseudometric $d_{w,r}$ on $\Theta(X)$ (`dist_{w, r}`); it also provides a simple function $Q:X\to\Theta(X)$ (`ProofData.Q`). Write $D=2^{𝕔\,a^2}\in\mathbb N$ (`defaultD a`, where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`), $o\in X$ for `cancelPt X` (a chosen point at which every function in $\Theta(X)$ vanishes), and $S\in\mathbb N$ for `defaultS X`, the least natural number $m>0$ such that $-m\le\sigma_1(y)$ and $\sigma_2(y)\le m$ for all $y\in X$ and both $F$ and $G$ are contained in the open ball $B(o,D^m/4)$. Assume a tile structure `TileStructure Q D κ S o`. Through its grid structure this provides a type $\mathrm{Grid}(X)$ of (dyadic) cubes, which is finite (the instance `instFintypeGrid`, from the grid-structure field `fintype_Grid`), each cube $I$ having an underlying set $I\subseteq X$ (`coeGrid`; $z\in I$ means membership in it), an integer $s(I)$ and a point $c(I)\in X$ (the grid-structure fields `s` and `c`), with the partial order $I\le J$ iff $I\subseteq J$ as sets and $s(I)\le s(J)$ (`instPartialOrderGrid`); and it provides a finite type $\mathfrak P(X)$ of tiles (`instFintype𝔓`), each tile $p$ having a cube $\mathcal I(p)\in\mathrm{Grid}(X)$, the integer $\mathfrak s(p)=s(\mathcal I(p))$, an element $\mathcal Q(p)\in\Theta(X)$ (`𝒬 p`) and a set $\Omega(p)\subseteq\Theta(X)$. Let $V$ be a normed additive commutative group that is a normed space over $\mathbb R$. Definition: for a set $\mathcal C\subseteq\mathrm{Grid}(X)$ of cubes, a function $g:X\to V$ and a point $z\in X$, `approxOnCube C g z` is the element $P_{\mathcal C}g(z)=\sum_{J\in\mathcal C}\mathbf 1_J(z)\,⨍_J g\,d\mu\in V$, i.e. the sum, over the cubes $J\in\mathcal C$ whose underlying set contains $z$, of the average of $g$ over $J$ with respect to $\mu$ (Bochner integral over $J$ divided by $\mu(J)$). By its docstring, this is the projection operator $P_{\mathcal C}g(z)$ given above Lemma 7.1.3, and in lemmas the `c` will be pairwise disjoint on $\mathcal C$.

### `TileStructure.Forest.pointwise_tree_estimate`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) (hx : x ∈ L) (hx' : x' ∈ L) (hf : BoundedCompactSupport f volume) : ‖carlesonSum ((fun x => t.𝔗 x) u) (fun y => Complex.exp (Complex.I * -↑((𝒬 u) y)) * f y) x‖ₑ ≤ ↑(Forest.C7_1_3 a) * (maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) fun x => ‖f x‖) x' + t.boundaryOperator u (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) fun x => ↑‖f x‖) x') + Forest.nontangentialMaximalFunction (𝒬 u) (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) f) x'`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u : 𝔓 X} {x x' : X} {f : X → ℂ} {L : Grid X}, u ∈ t → Membership.mem (γ := Set (Grid X)) (Forest.𝓛 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) L → x ∈ L → x' ∈ L → BoundedCompactSupport f volume → ‖carlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) (fun (y : X) => Complex.exp (Complex.I * -↑((𝒬 u) y)) * f y) x‖ₑ ≤ ↑(Forest.C7_1_3 a) * (maximalFunction (ε := ℝ) volume (Forest.𝓑 (F := F) (G := G)) (Forest.c𝓑 (F := F) (G := G)) (Forest.r𝓑 (F := F) (G := G)) (1 : ℝ) (Forest.approxOnCube (F := F) (G := G) (Forest.𝓙 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) fun (x : X) => ‖f x‖) x' + t.boundaryOperator (F := F) (G := G) u (Forest.approxOnCube (F := F) (G := G) (Forest.𝓙 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) fun (x : X) => ↑‖f x‖) x') + Forest.nontangentialMaximalFunction (F := F) (G := G) (𝒬 u) (Forest.approxOnCube (F := F) (G := G) (Forest.𝓙 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) f) x'`
Docstring: Lemma 7.1.3.
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\to X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume a `ProofData a q K σ₁ σ₂ F G` instance (by its docstring, the data common through most of chapters 2–7 of the blueprint). Through its `KernelProofData` component this provides a doubling-measure structure `DoublingMeasure X (2^a)` on $X$, whose measure we denote by $\mu$ (the measure `volume`), and a `CompatibleFunctions ℝ X (2^a)` structure, hence a `FunctionDistances ℝ X` structure with its type $\Theta(X)$ (by its docstring, a type of continuous functions $X\to\mathbb R$; each $\theta\in\Theta(X)$ is applied to points of $X$ via the coercion `coeΘ`) and, for each $w\in X$ and $r\in\mathbb R$, a pseudometric $d_{w,r}$ on $\Theta(X)$ (`dist_{w, r}`); it also provides a simple function $Q:X\to\Theta(X)$ (`ProofData.Q`). Write $D=2^{𝕔\,a^2}\in\mathbb N$ (`defaultD a`, where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`), $o\in X$ for `cancelPt X` (a chosen point at which every function in $\Theta(X)$ vanishes), and $S\in\mathbb N$ for `defaultS X`, the least natural number $m>0$ such that $-m\le\sigma_1(y)$ and $\sigma_2(y)\le m$ for all $y\in X$ and both $F$ and $G$ are contained in the open ball $B(o,D^m/4)$. Assume a tile structure `TileStructure Q D κ S o`. Through its grid structure this provides a type $\mathrm{Grid}(X)$ of (dyadic) cubes, which is finite (the instance `instFintypeGrid`, from the grid-structure field `fintype_Grid`), each cube $I$ having an underlying set $I\subseteq X$ (`coeGrid`; $z\in I$ means membership in it), an integer $s(I)$ and a point $c(I)\in X$ (the grid-structure fields `s` and `c`), with the partial order $I\le J$ iff $I\subseteq J$ as sets and $s(I)\le s(J)$ (`instPartialOrderGrid`); and it provides a finite type $\mathfrak P(X)$ of tiles (`instFintype𝔓`), each tile $p$ having a cube $\mathcal I(p)\in\mathrm{Grid}(X)$, the integer $\mathfrak s(p)=s(\mathcal I(p))$, an element $\mathcal Q(p)\in\Theta(X)$ (`𝒬 p`) and a set $\Omega(p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (a term of the project structure `Forest X n`). It has a set $\mathfrak U(t)\subseteq\mathfrak P(X)$ of tiles (field `𝔘`; $u\in t$ means $u\in\mathfrak U(t)$) and a map $\mathfrak T_t$ assigning to each tile $v$ a set of tiles $\mathfrak T_t(v)\subseteq\mathfrak P(X)$ (field `𝔗`; by its docstring its value at $v$ only matters when $v\in\mathfrak U(t)$). By the definition bodies of the project notions `Forest.𝓛₀`, `Forest.𝓛`, `Forest.𝓙₀` and `Forest.𝓙`: for $\mathfrak S\subseteq\mathfrak P(X)$, $\mathcal L_0(\mathfrak S)$ is the set of cubes $L'$ such that $s(L')=-S$, or [$L'\le\mathcal I(p)$ for some $p\in\mathfrak S$ and $\mathcal I(p)\not\le L'$ for every $p\in\mathfrak S$]; $\mathcal L(\mathfrak S)$ is the set of maximal elements of $\mathcal L_0(\mathfrak S)$ for $\le$; $\mathcal J_0(\mathfrak S)$ is the set of cubes $J$ such that $s(J)=-S$ or $\mathcal I(p)\not\subseteq B(c(J),100\,D^{s(J)+1})$ for every $p\in\mathfrak S$; and $\mathcal J(\mathfrak S)$ is the set of maximal elements of $\mathcal J_0(\mathfrak S)$ for $\le$. For a set $\mathcal C\subseteq\mathrm{Grid}(X)$ of cubes and a function $g:X\to V$ into a real normed space $V$, $P_{\mathcal C}g:X\to V$ (`Forest.approxOnCube C g`) is defined by $P_{\mathcal C}g(z)=\sum_{J\in\mathcal C}\mathbf 1_J(z)\,⨍_J g\,d\mu$, where $⨍_J g\,d\mu$ is the average (Bochner integral divided by measure) of $g$ over $J$ with respect to $\mu$ (by its docstring, the projection operator given above Lemma 7.1.3). For $\iota\in\mathbb Z$ and $w,y\in X$ let $K_\iota(w,y)=K(w,y)\,\psi_D\big(D^{-\iota}d(w,y)\big)$ (`Ks ι w y`), where $\psi_D(r)=\max\big(0,\min(1,\,4Dr-1,\,2-4r)\big)$ for $r\in\mathbb R$ (the project function `ψ D`). For a tile $p$ let $\mathsf E(p)=\{y\in X: y\in\mathcal I(p),\ Q(y)\in\Omega(p),\ \sigma_1(y)\le\mathfrak s(p)\le\sigma_2(y)\}$ (the project set `E p`). For $\mathfrak C\subseteq\mathfrak P(X)$ and $g:X\to\mathbb C$ let $T_{\mathfrak C}g(z)=\sum_{p\in\mathfrak C}\mathbf 1_{\mathsf E(p)}(z)\int_X e^{\mathrm i\,(Q(z)(y)-Q(z)(z))}K_{\mathfrak s(p)}(z,y)\,g(y)\,d\mu(y)$ (with $\mathrm i$ the imaginary unit; `carlesonSum`, a sum of the operators `carlesonOn p`). By the definition bodies of `Forest.𝓑`, `Forest.c𝓑` and `Forest.r𝓑`, $\mathcal B=\{0,\dots,S+5\}\times\{0,\dots,2S+3\}\times\mathrm{Grid}(X)\subseteq\mathbb N\times\mathbb N\times\mathrm{Grid}(X)$ and, for $\beta=(k,l,I)$, $c_\beta=c(I)$ and $r_\beta=2^kD^{s(I)+l}$. For $h:X\to\mathbb R$ let $M_{\mathcal B}h(z)=\sup_{\beta\in\mathcal B}\mathbf 1_{B(c_\beta,r_\beta)}(z)\,⨍^{-}_{B(c_\beta,r_\beta)}\|h(y)\|\,d\mu(y)\in[0,\infty]$, with $⨍^{-}$ the average of the lower Lebesgue integral (`maximalFunction volume 𝓑 c𝓑 r𝓑 1 h`; by its docstring the uncentered Hardy–Littlewood maximal function for a family of balls, here with exponent $1$). By the definition bodies of `Forest.boundaryOperator`, `Forest.ijIntegral` and `Forest.𝓙'`: for $u\in\mathfrak P(X)$ and $h:X\to\mathbb C$, the boundary operator $\mathrm{Bd}_{t,u}h:X\to[0,\infty]$ (`t.boundaryOperator u h`) is $\mathrm{Bd}_{t,u}h(z)=\sum_{I\in\mathrm{Grid}(X)}\mathbf 1_{I}(z)\sum_{J}\frac{D^{(s(J)-s(I))/a}}{\mu\big(B(c(I),16D^{s(I)})\big)}\int^{-}_J\|h(y)\|\,d\mu(y)$ (lower Lebesgue integral), where the inner sum runs over the cubes $J\in\mathcal J(\mathfrak T_t(u))$ with $J\subseteq B(c(I),16D^{s(I)})$ and $s(J)\le s(I)$. By the definition bodies of `upperRadius` and `Forest.nontangentialMaximalFunction`: for $\theta\in\Theta(X)$ and $w\in X$, $R_Q(\theta,w)=\sup\{r\in\mathbb R: d_{w,r}(\theta,Q(w))<1\}\in[0,\infty]$ (`upperRadius Q θ w`, with negative $r$ contributing $0$); and for $h:X\to\mathbb C$, $T^{\theta}_{\mathrm{nt}}h:X\to[0,\infty]$ is $T^{\theta}_{\mathrm{nt}}h(z)=\sup\big\|\sum_{\iota=s(I)}^{s_2}\int_X K_\iota(w,y)h(y)\,d\mu(y)\big\|$, the supremum (in $[0,\infty]$, empty supremum $0$) over all $I\in\mathrm{Grid}(X)$ with $z\in I$, all $w\in I$ and all integers $s_2$ with $s(I)\le s_2\le S$ and $D^{s_2-1}\le R_Q(\theta,w)$. Let $C_{7.1.3}(a)\in\mathbb R_{\ge0}$ be the project constant `Forest.C7_1_3 a` (by its docstring it has value $2^{129a^3}$ in the blueprint). (Lemma 7.1.3.) Let $u\in\mathfrak P(X)$ with $u\in t$, let $x,x'\in X$, let $f:X\to\mathbb C$, and let $L\in\mathrm{Grid}(X)$ with $L\in\mathcal L(\mathfrak T_t(u))$, $x\in L$ and $x'\in L$. Write $\mathcal J_u=\mathcal J(\mathfrak T_t(u))$. Suppose moreover that $f$ satisfies `BoundedCompactSupport f volume` (by its docstring: $f$ is a bounded, compactly supported, measurable function, with respect to $\mu$). Then $$\Big\|T_{\mathfrak T_t(u)}\big[y\mapsto e^{-\mathrm i\,\mathcal Q(u)(y)}f(y)\big](x)\Big\|_e\le C_{7.1.3}(a)\Big(M_{\mathcal B}\big(P_{\mathcal J_u}|f|\big)(x')+\mathrm{Bd}_{t,u}\big(P_{\mathcal J_u}|f|\big)(x')\Big)+T^{\mathcal Q(u)}_{\mathrm{nt}}\big(P_{\mathcal J_u}f\big)(x'),$$ where in the first term $|f|$ is the real-valued function $y\mapsto\|f(y)\|$ and in the second term it is the same function viewed as complex-valued; $\|\cdot\|_e\in[0,\infty]$ is the extended norm and the inequality is in $[0,\infty]$.

### `TileStructure.Forest.first_tree_pointwise`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) (hx : x ∈ L) (hx' : x' ∈ L) (hf : BoundedCompactSupport f volume) : ‖∑ i ∈ t.σ u x, ∫ (y : X), (Complex.exp (Complex.I * (-↑((𝒬 u) y) + ↑((Q x) y) + ↑((𝒬 u) x) - ↑((Q x) x))) - 1) * Ks i x y * f y‖ₑ ≤ ↑(Forest.C7_1_4 a) * maximalFunction volume Forest.𝓑 Forest.c𝓑 Forest.r𝓑 1 (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) fun x => ‖f x‖) x'`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u : 𝔓 X} {x x' : X} {f : X → ℂ} {L : Grid X}, u ∈ t → Membership.mem (γ := Set (Grid X)) (Forest.𝓛 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) L → x ∈ L → x' ∈ L → BoundedCompactSupport f volume → enorm (E := ℂ) (∑ i ∈ t.σ (F := F) (G := G) u x, @integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => (Complex.exp (Complex.I * (-↑((𝒬 u) y) + ↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y) + ↑((𝒬 u) x) - ↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) x))) - (1 : ℂ)) * Ks i x y * f y) ≤ ↑(Forest.C7_1_4 a) * maximalFunction (ε := ℝ) volume (Forest.𝓑 (F := F) (G := G)) (Forest.c𝓑 (F := F) (G := G)) (Forest.r𝓑 (F := F) (G := G)) (1 : ℝ) (Forest.approxOnCube (F := F) (G := G) (Forest.𝓙 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) fun (x : X) => ‖f x‖) x'`
Docstring: Lemma 7.1.4
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\to X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume a `ProofData a q K σ₁ σ₂ F G` instance (by its docstring, the data common through most of chapters 2–7 of the blueprint). Through its `KernelProofData` component this provides a doubling-measure structure `DoublingMeasure X (2^a)` on $X$, whose measure we denote by $\mu$ (the measure `volume`), and a `CompatibleFunctions ℝ X (2^a)` structure, hence a `FunctionDistances ℝ X` structure with its type $\Theta(X)$ (by its docstring, a type of continuous functions $X\to\mathbb R$; each $\theta\in\Theta(X)$ is applied to points of $X$ via the coercion `coeΘ`) and, for each $w\in X$ and $r\in\mathbb R$, a pseudometric $d_{w,r}$ on $\Theta(X)$ (`dist_{w, r}`); it also provides a simple function $Q:X\to\Theta(X)$ (`ProofData.Q`). Write $D=2^{𝕔\,a^2}\in\mathbb N$ (`defaultD a`, where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`), $o\in X$ for `cancelPt X` (a chosen point at which every function in $\Theta(X)$ vanishes), and $S\in\mathbb N$ for `defaultS X`, the least natural number $m>0$ such that $-m\le\sigma_1(y)$ and $\sigma_2(y)\le m$ for all $y\in X$ and both $F$ and $G$ are contained in the open ball $B(o,D^m/4)$. Assume a tile structure `TileStructure Q D κ S o`. Through its grid structure this provides a type $\mathrm{Grid}(X)$ of (dyadic) cubes, which is finite (the instance `instFintypeGrid`, from the grid-structure field `fintype_Grid`), each cube $I$ having an underlying set $I\subseteq X$ (`coeGrid`; $z\in I$ means membership in it), an integer $s(I)$ and a point $c(I)\in X$ (the grid-structure fields `s` and `c`), with the partial order $I\le J$ iff $I\subseteq J$ as sets and $s(I)\le s(J)$ (`instPartialOrderGrid`); and it provides a finite type $\mathfrak P(X)$ of tiles (`instFintype𝔓`), each tile $p$ having a cube $\mathcal I(p)\in\mathrm{Grid}(X)$, the integer $\mathfrak s(p)=s(\mathcal I(p))$, an element $\mathcal Q(p)\in\Theta(X)$ (`𝒬 p`) and a set $\Omega(p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (a term of the project structure `Forest X n`). It has a set $\mathfrak U(t)\subseteq\mathfrak P(X)$ of tiles (field `𝔘`; $u\in t$ means $u\in\mathfrak U(t)$) and a map $\mathfrak T_t$ assigning to each tile $v$ a set of tiles $\mathfrak T_t(v)\subseteq\mathfrak P(X)$ (field `𝔗`; by its docstring its value at $v$ only matters when $v\in\mathfrak U(t)$). By the definition bodies of the project notions `Forest.𝓛₀`, `Forest.𝓛`, `Forest.𝓙₀` and `Forest.𝓙`: for $\mathfrak S\subseteq\mathfrak P(X)$, $\mathcal L_0(\mathfrak S)$ is the set of cubes $L'$ such that $s(L')=-S$, or [$L'\le\mathcal I(p)$ for some $p\in\mathfrak S$ and $\mathcal I(p)\not\le L'$ for every $p\in\mathfrak S$]; $\mathcal L(\mathfrak S)$ is the set of maximal elements of $\mathcal L_0(\mathfrak S)$ for $\le$; $\mathcal J_0(\mathfrak S)$ is the set of cubes $J$ such that $s(J)=-S$ or $\mathcal I(p)\not\subseteq B(c(J),100\,D^{s(J)+1})$ for every $p\in\mathfrak S$; and $\mathcal J(\mathfrak S)$ is the set of maximal elements of $\mathcal J_0(\mathfrak S)$ for $\le$. For a set $\mathcal C\subseteq\mathrm{Grid}(X)$ of cubes and a function $g:X\to V$ into a real normed space $V$, $P_{\mathcal C}g:X\to V$ (`Forest.approxOnCube C g`) is defined by $P_{\mathcal C}g(z)=\sum_{J\in\mathcal C}\mathbf 1_J(z)\,⨍_J g\,d\mu$, where $⨍_J g\,d\mu$ is the average (Bochner integral divided by measure) of $g$ over $J$ with respect to $\mu$ (by its docstring, the projection operator given above Lemma 7.1.3). For $\iota\in\mathbb Z$ and $w,y\in X$ let $K_\iota(w,y)=K(w,y)\,\psi_D\big(D^{-\iota}d(w,y)\big)$ (`Ks ι w y`), where $\psi_D(r)=\max\big(0,\min(1,\,4Dr-1,\,2-4r)\big)$ for $r\in\mathbb R$ (the project function `ψ D`). For a tile $p$ let $\mathsf E(p)=\{y\in X: y\in\mathcal I(p),\ Q(y)\in\Omega(p),\ \sigma_1(y)\le\mathfrak s(p)\le\sigma_2(y)\}$ (the project set `E p`). For $u\in\mathfrak P(X)$ and $y\in X$ let $\sigma_t(u,y)=\{\mathfrak s(p): p\in\mathfrak T_t(u),\ y\in\mathsf E(p)\}$, a finite set of integers (`t.σ u y`). By the definition bodies of `Forest.𝓑`, `Forest.c𝓑` and `Forest.r𝓑`, $\mathcal B=\{0,\dots,S+5\}\times\{0,\dots,2S+3\}\times\mathrm{Grid}(X)\subseteq\mathbb N\times\mathbb N\times\mathrm{Grid}(X)$ and, for $\beta=(k,l,I)$, $c_\beta=c(I)$ and $r_\beta=2^kD^{s(I)+l}$. For $h:X\to\mathbb R$ let $M_{\mathcal B}h(z)=\sup_{\beta\in\mathcal B}\mathbf 1_{B(c_\beta,r_\beta)}(z)\,⨍^{-}_{B(c_\beta,r_\beta)}\|h(y)\|\,d\mu(y)\in[0,\infty]$, with $⨍^{-}$ the average of the lower Lebesgue integral (`maximalFunction volume 𝓑 c𝓑 r𝓑 1 h`; by its docstring the uncentered Hardy–Littlewood maximal function for a family of balls, here with exponent $1$). Let $C_{7.1.4}(a)\in\mathbb R_{\ge0}$ be the project constant `Forest.C7_1_4 a` (by its docstring it has value $10\cdot2^{104a^3}$ in the blueprint). (Lemma 7.1.4.) Let $u\in\mathfrak P(X)$ with $u\in t$, let $x,x'\in X$, let $f:X\to\mathbb C$, and let $L\in\mathrm{Grid}(X)$ with $L\in\mathcal L(\mathfrak T_t(u))$, $x\in L$ and $x'\in L$. Write $\mathcal J_u=\mathcal J(\mathfrak T_t(u))$. Suppose moreover that $f$ satisfies `BoundedCompactSupport f volume` (by its docstring: $f$ is a bounded, compactly supported, measurable function, with respect to $\mu$). Then, writing $\mathrm i$ for the imaginary unit, $$\Big\|\sum_{\iota\in\sigma_t(u,x)}\int_X\Big(\exp\big(\mathrm i\,(-\mathcal Q(u)(y)+Q(x)(y)+\mathcal Q(u)(x)-Q(x)(x))\big)-1\Big)K_\iota(x,y)\,f(y)\,d\mu(y)\Big\|_e\le C_{7.1.4}(a)\cdot M_{\mathcal B}\big(P_{\mathcal J_u}|f|\big)(x'),$$ where $|f|$ is the real-valued function $y\mapsto\|f(y)\|$, $\|\cdot\|_e\in[0,\infty]$ is the extended norm and the inequality is in $[0,\infty]$.

### `TileStructure.Forest.second_tree_pointwise`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) (hx : x ∈ L) (hx' : x' ∈ L) : ‖∑ i ∈ t.σ u x, ∫ (y : X), Ks i x y * Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) f y‖ₑ ≤ Forest.nontangentialMaximalFunction (𝒬 u) (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) f) x'`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u : 𝔓 X} {x x' : X} {f : X → ℂ} {L : Grid X}, u ∈ t → Membership.mem (γ := Set (Grid X)) (Forest.𝓛 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) L → x ∈ L → x' ∈ L → enorm (E := ℂ) (∑ i ∈ t.σ (F := F) (G := G) u x, @integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => Ks i x y * Forest.approxOnCube (F := F) (G := G) (Forest.𝓙 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) f y) ≤ Forest.nontangentialMaximalFunction (F := F) (G := G) (𝒬 u) (Forest.approxOnCube (F := F) (G := G) (Forest.𝓙 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) f) x'`
Docstring: Lemma 7.1.5
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\to X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume a `ProofData a q K σ₁ σ₂ F G` instance (by its docstring, the data common through most of chapters 2–7 of the blueprint). Through its `KernelProofData` component this provides a doubling-measure structure `DoublingMeasure X (2^a)` on $X$, whose measure we denote by $\mu$ (the measure `volume`), and a `CompatibleFunctions ℝ X (2^a)` structure, hence a `FunctionDistances ℝ X` structure with its type $\Theta(X)$ (by its docstring, a type of continuous functions $X\to\mathbb R$; each $\theta\in\Theta(X)$ is applied to points of $X$ via the coercion `coeΘ`) and, for each $w\in X$ and $r\in\mathbb R$, a pseudometric $d_{w,r}$ on $\Theta(X)$ (`dist_{w, r}`); it also provides a simple function $Q:X\to\Theta(X)$ (`ProofData.Q`). Write $D=2^{𝕔\,a^2}\in\mathbb N$ (`defaultD a`, where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`), $o\in X$ for `cancelPt X` (a chosen point at which every function in $\Theta(X)$ vanishes), and $S\in\mathbb N$ for `defaultS X`, the least natural number $m>0$ such that $-m\le\sigma_1(y)$ and $\sigma_2(y)\le m$ for all $y\in X$ and both $F$ and $G$ are contained in the open ball $B(o,D^m/4)$. Assume a tile structure `TileStructure Q D κ S o`. Through its grid structure this provides a type $\mathrm{Grid}(X)$ of (dyadic) cubes, which is finite (the instance `instFintypeGrid`, from the grid-structure field `fintype_Grid`), each cube $I$ having an underlying set $I\subseteq X$ (`coeGrid`; $z\in I$ means membership in it), an integer $s(I)$ and a point $c(I)\in X$ (the grid-structure fields `s` and `c`), with the partial order $I\le J$ iff $I\subseteq J$ as sets and $s(I)\le s(J)$ (`instPartialOrderGrid`); and it provides a finite type $\mathfrak P(X)$ of tiles (`instFintype𝔓`), each tile $p$ having a cube $\mathcal I(p)\in\mathrm{Grid}(X)$, the integer $\mathfrak s(p)=s(\mathcal I(p))$, an element $\mathcal Q(p)\in\Theta(X)$ (`𝒬 p`) and a set $\Omega(p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (a term of the project structure `Forest X n`). It has a set $\mathfrak U(t)\subseteq\mathfrak P(X)$ of tiles (field `𝔘`; $u\in t$ means $u\in\mathfrak U(t)$) and a map $\mathfrak T_t$ assigning to each tile $v$ a set of tiles $\mathfrak T_t(v)\subseteq\mathfrak P(X)$ (field `𝔗`; by its docstring its value at $v$ only matters when $v\in\mathfrak U(t)$). By the definition bodies of the project notions `Forest.𝓛₀`, `Forest.𝓛`, `Forest.𝓙₀` and `Forest.𝓙`: for $\mathfrak S\subseteq\mathfrak P(X)$, $\mathcal L_0(\mathfrak S)$ is the set of cubes $L'$ such that $s(L')=-S$, or [$L'\le\mathcal I(p)$ for some $p\in\mathfrak S$ and $\mathcal I(p)\not\le L'$ for every $p\in\mathfrak S$]; $\mathcal L(\mathfrak S)$ is the set of maximal elements of $\mathcal L_0(\mathfrak S)$ for $\le$; $\mathcal J_0(\mathfrak S)$ is the set of cubes $J$ such that $s(J)=-S$ or $\mathcal I(p)\not\subseteq B(c(J),100\,D^{s(J)+1})$ for every $p\in\mathfrak S$; and $\mathcal J(\mathfrak S)$ is the set of maximal elements of $\mathcal J_0(\mathfrak S)$ for $\le$. For a set $\mathcal C\subseteq\mathrm{Grid}(X)$ of cubes and a function $g:X\to V$ into a real normed space $V$, $P_{\mathcal C}g:X\to V$ (`Forest.approxOnCube C g`) is defined by $P_{\mathcal C}g(z)=\sum_{J\in\mathcal C}\mathbf 1_J(z)\,⨍_J g\,d\mu$, where $⨍_J g\,d\mu$ is the average (Bochner integral divided by measure) of $g$ over $J$ with respect to $\mu$ (by its docstring, the projection operator given above Lemma 7.1.3). For $\iota\in\mathbb Z$ and $w,y\in X$ let $K_\iota(w,y)=K(w,y)\,\psi_D\big(D^{-\iota}d(w,y)\big)$ (`Ks ι w y`), where $\psi_D(r)=\max\big(0,\min(1,\,4Dr-1,\,2-4r)\big)$ for $r\in\mathbb R$ (the project function `ψ D`). For a tile $p$ let $\mathsf E(p)=\{y\in X: y\in\mathcal I(p),\ Q(y)\in\Omega(p),\ \sigma_1(y)\le\mathfrak s(p)\le\sigma_2(y)\}$ (the project set `E p`). For $u\in\mathfrak P(X)$ and $y\in X$ let $\sigma_t(u,y)=\{\mathfrak s(p): p\in\mathfrak T_t(u),\ y\in\mathsf E(p)\}$, a finite set of integers (`t.σ u y`). By the definition bodies of `upperRadius` and `Forest.nontangentialMaximalFunction`: for $\theta\in\Theta(X)$ and $w\in X$, $R_Q(\theta,w)=\sup\{r\in\mathbb R: d_{w,r}(\theta,Q(w))<1\}\in[0,\infty]$ (`upperRadius Q θ w`, with negative $r$ contributing $0$); and for $h:X\to\mathbb C$, $T^{\theta}_{\mathrm{nt}}h:X\to[0,\infty]$ is $T^{\theta}_{\mathrm{nt}}h(z)=\sup\big\|\sum_{\iota=s(I)}^{s_2}\int_X K_\iota(w,y)h(y)\,d\mu(y)\big\|$, the supremum (in $[0,\infty]$, empty supremum $0$) over all $I\in\mathrm{Grid}(X)$ with $z\in I$, all $w\in I$ and all integers $s_2$ with $s(I)\le s_2\le S$ and $D^{s_2-1}\le R_Q(\theta,w)$. (Lemma 7.1.5.) Let $u\in\mathfrak P(X)$ with $u\in t$, let $x,x'\in X$, let $f:X\to\mathbb C$, and let $L\in\mathrm{Grid}(X)$ with $L\in\mathcal L(\mathfrak T_t(u))$, $x\in L$ and $x'\in L$. Write $\mathcal J_u=\mathcal J(\mathfrak T_t(u))$. Then $$\Big\|\sum_{\iota\in\sigma_t(u,x)}\int_X K_\iota(x,y)\,P_{\mathcal J_u}f(y)\,d\mu(y)\Big\|_e\le T^{\mathcal Q(u)}_{\mathrm{nt}}\big(P_{\mathcal J_u}f\big)(x'),$$ where $\|\cdot\|_e\in[0,\infty]$ is the extended norm and the inequality is in $[0,\infty]$.

### `TileStructure.Forest.third_tree_pointwise`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ t) (hL : L ∈ Forest.𝓛 ((fun x => t.𝔗 x) u)) (hx : x ∈ L) (hx' : x' ∈ L) (hf : BoundedCompactSupport f volume) : ‖∑ i ∈ t.σ u x, ∫ (y : X), Ks i x y * (f y - Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) f y)‖ₑ ≤ ↑(Forest.C7_1_6 a) * t.boundaryOperator u (Forest.approxOnCube (Forest.𝓙 ((fun x => t.𝔗 x) u)) fun x => ↑‖f x‖) x'`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u : 𝔓 X} {x x' : X} {f : X → ℂ} {L : Grid X}, u ∈ t → Membership.mem (γ := Set (Grid X)) (Forest.𝓛 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) L → x ∈ L → x' ∈ L → BoundedCompactSupport f volume → enorm (E := ℂ) (∑ i ∈ t.σ (F := F) (G := G) u x, @integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => Ks i x y * (f y - Forest.approxOnCube (F := F) (G := G) (Forest.𝓙 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) f y)) ≤ ↑(Forest.C7_1_6 a) * t.boundaryOperator (F := F) (G := G) u (Forest.approxOnCube (F := F) (G := G) (Forest.𝓙 (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u)) fun (x : X) => ↑‖f x‖) x'`
Docstring: Lemma 7.1.6
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K:X\to X\to\mathbb C$, $\sigma_1,\sigma_2:X\to\mathbb Z$ and $F,G\subseteq X$, and assume a `ProofData a q K σ₁ σ₂ F G` instance (by its docstring, the data common through most of chapters 2–7 of the blueprint). Through its `KernelProofData` component this provides a doubling-measure structure `DoublingMeasure X (2^a)` on $X$, whose measure we denote by $\mu$ (the measure `volume`), and a `CompatibleFunctions ℝ X (2^a)` structure, hence a `FunctionDistances ℝ X` structure with its type $\Theta(X)$ (by its docstring, a type of continuous functions $X\to\mathbb R$; each $\theta\in\Theta(X)$ is applied to points of $X$ via the coercion `coeΘ`) and, for each $w\in X$ and $r\in\mathbb R$, a pseudometric $d_{w,r}$ on $\Theta(X)$ (`dist_{w, r}`); it also provides a simple function $Q:X\to\Theta(X)$ (`ProofData.Q`). Write $D=2^{𝕔\,a^2}\in\mathbb N$ (`defaultD a`, where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa=2^{-10a}\in\mathbb R$ (`defaultκ a`), $o\in X$ for `cancelPt X` (a chosen point at which every function in $\Theta(X)$ vanishes), and $S\in\mathbb N$ for `defaultS X`, the least natural number $m>0$ such that $-m\le\sigma_1(y)$ and $\sigma_2(y)\le m$ for all $y\in X$ and both $F$ and $G$ are contained in the open ball $B(o,D^m/4)$. Assume a tile structure `TileStructure Q D κ S o`. Through its grid structure this provides a type $\mathrm{Grid}(X)$ of (dyadic) cubes, which is finite (the instance `instFintypeGrid`, from the grid-structure field `fintype_Grid`), each cube $I$ having an underlying set $I\subseteq X$ (`coeGrid`; $z\in I$ means membership in it), an integer $s(I)$ and a point $c(I)\in X$ (the grid-structure fields `s` and `c`), with the partial order $I\le J$ iff $I\subseteq J$ as sets and $s(I)\le s(J)$ (`instPartialOrderGrid`); and it provides a finite type $\mathfrak P(X)$ of tiles (`instFintype𝔓`), each tile $p$ having a cube $\mathcal I(p)\in\mathrm{Grid}(X)$, the integer $\mathfrak s(p)=s(\mathcal I(p))$, an element $\mathcal Q(p)\in\Theta(X)$ (`𝒬 p`) and a set $\Omega(p)\subseteq\Theta(X)$. Let $n\in\mathbb N$ and let $t$ be an $n$-forest (a term of the project structure `Forest X n`). It has a set $\mathfrak U(t)\subseteq\mathfrak P(X)$ of tiles (field `𝔘`; $u\in t$ means $u\in\mathfrak U(t)$) and a map $\mathfrak T_t$ assigning to each tile $v$ a set of tiles $\mathfrak T_t(v)\subseteq\mathfrak P(X)$ (field `𝔗`; by its docstring its value at $v$ only matters when $v\in\mathfrak U(t)$). By the definition bodies of the project notions `Forest.𝓛₀`, `Forest.𝓛`, `Forest.𝓙₀` and `Forest.𝓙`: for $\mathfrak S\subseteq\mathfrak P(X)$, $\mathcal L_0(\mathfrak S)$ is the set of cubes $L'$ such that $s(L')=-S$, or [$L'\le\mathcal I(p)$ for some $p\in\mathfrak S$ and $\mathcal I(p)\not\le L'$ for every $p\in\mathfrak S$]; $\mathcal L(\mathfrak S)$ is the set of maximal elements of $\mathcal L_0(\mathfrak S)$ for $\le$; $\mathcal J_0(\mathfrak S)$ is the set of cubes $J$ such that $s(J)=-S$ or $\mathcal I(p)\not\subseteq B(c(J),100\,D^{s(J)+1})$ for every $p\in\mathfrak S$; and $\mathcal J(\mathfrak S)$ is the set of maximal elements of $\mathcal J_0(\mathfrak S)$ for $\le$. For a set $\mathcal C\subseteq\mathrm{Grid}(X)$ of cubes and a function $g:X\to V$ into a real normed space $V$, $P_{\mathcal C}g:X\to V$ (`Forest.approxOnCube C g`) is defined by $P_{\mathcal C}g(z)=\sum_{J\in\mathcal C}\mathbf 1_J(z)\,⨍_J g\,d\mu$, where $⨍_J g\,d\mu$ is the average (Bochner integral divided by measure) of $g$ over $J$ with respect to $\mu$ (by its docstring, the projection operator given above Lemma 7.1.3). For $\iota\in\mathbb Z$ and $w,y\in X$ let $K_\iota(w,y)=K(w,y)\,\psi_D\big(D^{-\iota}d(w,y)\big)$ (`Ks ι w y`), where $\psi_D(r)=\max\big(0,\min(1,\,4Dr-1,\,2-4r)\big)$ for $r\in\mathbb R$ (the project function `ψ D`). For a tile $p$ let $\mathsf E(p)=\{y\in X: y\in\mathcal I(p),\ Q(y)\in\Omega(p),\ \sigma_1(y)\le\mathfrak s(p)\le\sigma_2(y)\}$ (the project set `E p`). For $u\in\mathfrak P(X)$ and $y\in X$ let $\sigma_t(u,y)=\{\mathfrak s(p): p\in\mathfrak T_t(u),\ y\in\mathsf E(p)\}$, a finite set of integers (`t.σ u y`). By the definition bodies of `Forest.boundaryOperator`, `Forest.ijIntegral` and `Forest.𝓙'`: for $u\in\mathfrak P(X)$ and $h:X\to\mathbb C$, the boundary operator $\mathrm{Bd}_{t,u}h:X\to[0,\infty]$ (`t.boundaryOperator u h`) is $\mathrm{Bd}_{t,u}h(z)=\sum_{I\in\mathrm{Grid}(X)}\mathbf 1_{I}(z)\sum_{J}\frac{D^{(s(J)-s(I))/a}}{\mu\big(B(c(I),16D^{s(I)})\big)}\int^{-}_J\|h(y)\|\,d\mu(y)$ (lower Lebesgue integral), where the inner sum runs over the cubes $J\in\mathcal J(\mathfrak T_t(u))$ with $J\subseteq B(c(I),16D^{s(I)})$ and $s(J)\le s(I)$. Let $C_{7.1.6}(a)\in\mathbb R_{\ge0}$ be the project constant `Forest.C7_1_6 a` (by its docstring it has value $2^{128a^3}$ in the blueprint). (Lemma 7.1.6.) Let $u\in\mathfrak P(X)$ with $u\in t$, let $x,x'\in X$, let $f:X\to\mathbb C$, and let $L\in\mathrm{Grid}(X)$ with $L\in\mathcal L(\mathfrak T_t(u))$, $x\in L$ and $x'\in L$. Write $\mathcal J_u=\mathcal J(\mathfrak T_t(u))$. Suppose moreover that $f$ satisfies `BoundedCompactSupport f volume` (by its docstring: $f$ is a bounded, compactly supported, measurable function, with respect to $\mu$). Then $$\Big\|\sum_{\iota\in\sigma_t(u,x)}\int_X K_\iota(x,y)\big(f(y)-P_{\mathcal J_u}f(y)\big)\,d\mu(y)\Big\|_e\le C_{7.1.6}(a)\,\mathrm{Bd}_{t,u}\big(P_{\mathcal J_u}|f|\big)(x'),$$ where $|f|$ is the function $y\mapsto\|f(y)\|$ viewed as complex-valued, $\|\cdot\|_e\in[0,\infty]$ is the extended norm and the inequality is in $[0,\infty]$.
