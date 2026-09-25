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

#### `E` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → Set X`
Docstring: The set `E` defined in Proposition 2.0.2.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) => {x : X | x ∈ 𝓘 p ∧ Membership.mem (α := @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) (Ω p) ((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) ∧ 𝔰 p ∈ Set.Icc (σ₁ x) (σ₂ x)}`

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

#### `MeasureTheory.DoublingMeasure.toMeasureSpace` (def)
Lean: `{X : Type u_3} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → [self : DoublingMeasure X A] → MeasureSpace X`
Definition: `fun (X : Type u_3) {A : outParam NNReal} {inst : PseudoMetricSpace X} [self : DoublingMeasure X A] => self.3`

#### `PreTileStructure.toGridStructure` (def)
Lean: `(𝕜 : Type u_1) → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → GridStructure.{u_2, u} X D κ S o`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.1`

#### `PreTileStructure.𝒬` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X → @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.6`

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

#### `WithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → X → ℝ → Type u_2`
Docstring: Class used to endow `Θ X` with a pseudometric space structure.
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] (x : X) (r : ℝ) => @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`

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

#### `instFintype𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (𝔓.{u, u_1, u_2} X)`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.fintype_𝔓`

#### `instPseudoMetricSpaceWithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → {x : X} → {r : ℝ} → PseudoMetricSpace (WithFunctionDistance x r)`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] {x : X} {r : ℝ} => FunctionDistances.metric x r`

#### `𝓘` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → Grid X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] => PreTileStructure.𝓘`

#### `𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → (X : Type u) → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [PreTileStructure.{u, u_1, u_2} Q D κ S o] → Type u`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] (X : Type u) {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X`

#### `𝔠` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => c (𝓘 p)`

#### `𝔰` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → ℤ`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => s (𝓘 p)`

#### `C2_0_3` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant appearing in Proposition 2.0.3. Has value `2 ^ (117 * a ^ 3)` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => (2 : NNReal) ^ ((𝕔 + (5 : ℕ) + 𝕔 / (8 : ℕ)) * a ^ (3 : ℕ)) / (q - (1 : NNReal))`

#### `carlesonSum` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → (X → ℂ) → X → ℂ`
Docstring: The operator `T_ℭ f` defined at the bottom of Section 7.4. We will use this in other places of the formalization as well.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [PseudoMetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) => ∑ p : 𝔓 X with p ∈ ℭ, carlesonOn (F := F) (G := G) p f x`

#### `dens₁` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ENNReal`
Docstring: This density is defined to live in `ℝ≥0∞`. Use `ENNReal.toReal` to get a real number.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔓' : Set (𝔓 X)) => ⨆ p' ∈ 𝔓', ⨆ (l : NNReal), ⨆ (_ : l ≥ (2 : NNReal)), HPow.hPow (β := ℝ) (↑l) (-↑a) * ⨆ p ∈ lowerCubes (F := F) (G := G) 𝔓', ⨆ (_ : smul (F := F) (G := G) (↑l) p' ≤ smul (F := F) (G := G) (↑l) p), HDiv.hDiv (α := ENNReal) (β := ENNReal) ((volume : Measure X) (E₂ (F := F) (G := G) (↑l) p) : ENNReal) ((volume : Measure X) ↑(𝓘 p) : ENNReal)`

#### `dens₂` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ENNReal`
Docstring: This density is defined to live in `ℝ≥0∞`. Use `ENNReal.toReal` to get a real number.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔓' : Set (𝔓 X)) => ⨆ p ∈ 𝔓', ⨆ (r : ℝ), ⨆ (_ : r ≥ (4 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p)), HDiv.hDiv (α := ENNReal) (β := ENNReal) ((volume : Measure X) (F ∩ Metric.ball (𝔠 p) r) : ENNReal) ((volume : Measure X) (Metric.ball (𝔠 p) r) : ENNReal)`

#### `instPartialOrder𝔓Real` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → PartialOrder (𝔓 X)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => PartialOrder.lift (toTileLike (F := F) (G := G)) ⋯`

#### `nnq` (def)
Lean: `(X : Type u_1) → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [ProofData a q K σ₁ σ₂ F G] → NNReal`
Docstring: `q` as an element of `ℝ≥0`.
Definition: `fun (X : Type u_1) {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [PseudoMetricSpace X] [ProofData a q K σ₁ σ₂ F G] => ⟨q, ⋯⟩`

#### `C6_1_4` (def)
Lean: `ℕ → NNReal`
Docstring: Constant appearing in Lemma 6.1.4. Has value `2 ^ (117 * a ^ 3)` in the blueprint.
Definition: `wrapped✝.1`

#### `adjointCarlesonSum` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → (X → ℂ) → X → ℂ`
Docstring: The definition of `T_ℭ*g(x)`, defined at the bottom of Section 7.4
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) => ∑ p : 𝔓 X with p ∈ ℭ, adjointCarleson (F := F) (G := G) p f x`

#### `Tile.C6_1_5` (def)
Lean: `ℕ → NNReal`
Docstring: The constant from lemma 6.1.5. Has value `2 ^ (232 * a ^ 3)` in the blueprint.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ (((2 : ℕ) * 𝕔 + (7 : ℕ) + 𝕔 / (4 : ℕ)) * a ^ (3 : ℕ))`

#### `Antichain.C6_1_6` (def)
Lean: `ℕ → NNReal`
Docstring: The constant appearing in Lemma 6.1.6.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ ((5 : ℕ) * a)`

#### `Antichain.p₆` (def)
Lean: `ℕ → ℝ`
Docstring: `p` in Lemma 6.1.6. We append a subscript `₆` to keep `p` available for tiles.
Definition: `fun (a : ℕ) => (4 : ℝ) * HPow.hPow (α := ℝ) ↑a (4 : ℕ)`

#### `Antichain.q₆` (def)
Lean: `ℕ → ℝ`
Docstring: `p'` in the proof of Lemma 6.1.4, the Hölder conjugate exponent of `p₆`.
Definition: `fun (a : ℕ) => ((1 : ℝ) - (p₆ a)⁻¹)⁻¹`

#### `M14` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ℝ → (X → ℂ) → X → ENNReal`
Docstring: The `maximalFunction` instance that appears in Lemma 6.1.4's proof.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔄 : Set (𝔓 X)) (p : ℝ) (g : X → ℂ) => maximalFunction volume 𝔄 𝔠 (fun (x : 𝔓 X) => (14 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 x)) p g`

#### `CompatibleFunctions` (structure or class)
Lean: `(𝕜 : outParam (Type u_3)) → (X : Type u) → outParam ℕ → [RCLike 𝕜] → [PseudoMetricSpace X] → Type (max (u + 1) u_3)`
Docstring: A set `Θ` of (continuous) functions is compatible. `A` will usually be `2 ^ a`.
Constructor (every field with its type): `{𝕜 : outParam (Type u_3)} → {X : Type u} → {A : outParam ℕ} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [toFunctionDistances : FunctionDistances 𝕜 X] → (∃ (o : X), ∀ (f : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), (coeΘ f) o = (0 : 𝕜)) → (∀ {x : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, localOscillation (Metric.ball x r) (coeΘ f) (coeΘ g) ≤ ENNReal.ofReal (dist_{x, r} f g)) → (∀ {x₁ x₂ : X} {r₁ r₂ : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, Metric.ball x₁ r₁ ⊆ Metric.ball x₂ r₂ → dist_{x₁, r₁} f g ≤ dist_{x₂, r₂} f g) → (∀ {x₁ x₂ : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, dist x₁ x₂ < (2 : ℝ) * r → dist_{x₂, (2 : ℝ) * r} f g ≤ ↑A * dist_{x₁, r} f g) → (∀ {x₁ x₂ : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, Metric.ball x₁ r ⊆ Metric.ball x₂ (↑A * r) → (2 : ℝ) * dist_{x₁, r} f g ≤ dist_{x₂, ↑A * r} f g) → (∀ {x : X} {r : ℝ}, AllBallsCoverBalls.{u} (WithFunctionDistance x r) (2 : ℝ) A) → CompatibleFunctions 𝕜 X A`

#### `FunctionDistances` (structure or class)
Lean: `(𝕜 : outParam (Type u_1)) → (X : Type u) → [NormedField 𝕜] → [TopologicalSpace X] → Type (max (u + 1) u_1)`
Docstring: A class stating that continuous functions have distances associated to every ball. We use a separate type to conveniently index these functions.
Constructor (every field with its type): `{𝕜 : outParam (Type u_1)} → {X : Type u} → [inst : NormedField 𝕜] → [inst_1 : TopologicalSpace X] → (Θ : Type u) → (coeΘ : Θ → C(X, 𝕜)) → (∀ {f g : Θ}, (∀ (x : X), Eq.{u_1 + 1} (α := 𝕜) ((coeΘ f) x : 𝕜) ((coeΘ g) x : 𝕜)) → f = g) → (X → ℝ → PseudoMetricSpace Θ) → FunctionDistances 𝕜 X`

#### `FunctionDistances.Θ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → (X : Type u) → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → Type u`
Docstring: A type of continuous functions from `X` to `𝕜`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.1`

#### `Grid` (def)
Lean: `(X : Type u) → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [GridStructure X D κ S o] → Type u`
Docstring: The indexing type of the grid structure. Elements are called (dyadic) cubes. Note that this type has instances for both `≤` and `⊆`, but they do *not* coincide.
Definition: `fun (X : Type u) {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => @GridStructure.Grid X _ inst inst_1 _ _ _ _ _`

#### `TileStructure.Ω` (def)
Lean: `{X : Type u} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {inst_2 : FunctionDistances ℝ X} → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : TileStructure Q D κ S o] → PreTileStructure.𝔓 ℝ X → Set (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _)`
Definition: `fun (X : Type u) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {inst_2 : FunctionDistances ℝ X} {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : TileStructure Q D κ S o] => self.2`

#### `instMembershipGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Membership X (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => { mem := fun (i : Grid X) (x : X) => x ∈ ↑i }`

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

#### `PreTileStructure.𝔓` (def)
Lean: `(𝕜 : Type u_1) → {inst : RCLike 𝕜} → (X : Type u) → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Type u`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.2`

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

#### `instPartialOrderGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → PartialOrder (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => PartialOrder.lift (fun (i : @GridStructure.Grid X _ inst inst_1 _ _ _ _ _) => (↑i, GridStructure.s i)) ⋯`

#### `FunctionDistances.coeΘ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → @Θ _ X inst inst_1 _ → C(X, 𝕜)`
Docstring: The coercion map from `Θ` to `C(X, 𝕜)`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.2`

#### `𝕔` (def)
Lean: `ℕ`
Docstring: The main constant in the blueprint, driving all the construction, is `D = 2 ^ (100 * a ^ 2)`. It turns out that the proof is robust, and works for other values of `100`, giving better constants in the end. We will formalize it using a parameter `𝕔` (that we fix equal to `100` to follow the blueprint) and having `D = 2 ^ (𝕔 * a ^ 2)`. We register two lemmas `seven_le_c` and `c_le_100` and will never unfold `𝕔` from this point on.
Definition: `wrapped✝.1`

#### `PreTileStructure.fintype_𝔓` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X)`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.3`

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

#### `carlesonOn` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
Docstring: The operator `T_𝔭` defined in Proposition 2.0.2.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [PseudoMetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) => (E (F := F) (G := G) p).indicator fun (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => Complex.exp (Complex.I * (↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y) - ↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) x))) * Ks (𝔰 p) x y * f y`

#### `C5_3_2` (def)
Lean: `ℕ → ℝ`
Definition: `fun (a : ℕ) => (2 : ℝ) ^ ((-95 : ℝ) * ↑a)`

#### `E₂` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℝ → 𝔓 X → Set X`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (l : ℝ) (p : 𝔓 X) => (smul (F := F) (G := G) l p).toSet (F := F) (G := G)`

#### `TileLike` (def)
Lean: `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Type u_1`
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => Grid X × (Set (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))ᵒᵈ`

#### `instPartialOrderTileLike` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → PartialOrder (TileLike X (F := F) (G := G))`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => { le := instPartialOrderTileLike._aux_1, lt := instPartialOrderTileLike._aux_3, le_refl := ⋯, le_trans := ⋯, lt_iff_le_not_ge := ⋯, le_antisymm := ⋯ }`

#### `lowerCubes` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → Set (𝔓 X)`
Docstring: `𝔓(𝔓')` in the blueprint. The set of all tiles whose cubes are less than the cube of some tile in the given set.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔓' : Set (𝔓 X)) => {p : 𝔓 X | ∃ p' ∈ 𝔓', 𝓘 p ≤ 𝓘 p'}`

#### `smul` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℝ → 𝔓 X → TileLike X (F := F) (G := G)`
Docstring: This is not defined as such in the blueprint, but `λp ≲ λ'p'` can be written using `smul l p ≤ smul l' p'`. Beware: `smul 1 p` is very different from `toTileLike p`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (l : ℝ) (p : 𝔓 X) => (𝓘 p, ball_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) l)`

#### `toTileLike` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → TileLike X (F := F) (G := G)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) => (𝓘 p, Ω p)`

#### `adjointCarleson` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
Docstring: The definition of `Tₚ*g(x)`, defined above Lemma 7.4.1
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume (E (F := F) (G := G) p)) fun (y : X) => HMul.hMul (α := ℂ) ((starRingEnd ℂ) (Ks (𝔰 p) y x) : ℂ) (Complex.exp (Complex.I * (↑(((Q (F := F) (G := G)) y : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y) - ↑(((Q (F := F) (G := G)) y : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) x)))) * f y`

#### `Tile.C6_2_1` (def)
Lean: `ℕ → NNReal`
Docstring: The constant from lemma 6.2.1. Has value `2 ^ (231 * a ^ 3)` in the blueprint.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ (((2 : ℕ) * 𝕔 + (6 : ℕ) + 𝕔 / (4 : ℕ)) * a ^ (3 : ℕ))`

#### `Antichain.𝔄_aux` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _ → ℕ → Set (𝔓 X)`
Docstring: Def 6.3.15.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) (N : ℕ) => {p : 𝔓 X | p ∈ 𝔄 ∧ (1 : ℝ) + dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) ϑ ∈ Set.Ico ((2 : ℝ) ^ N) ((2 : ℝ) ^ (N + (1 : ℕ)))}`

#### `maximalFunction` (def)
Lean: `{X : Type u_1} → {ε : Type u_2} → [PseudoMetricSpace X] → [inst : MeasurableSpace X] → [ENorm ε] → {ι : Type u_4} → Measure X → Set ι → (ι → X) → (ι → ℝ) → ℝ → (X → ε) → X → ENNReal`
Docstring: The uncentered Hardy-Littlewood maximal function, for a family of balls.
Definition: `fun {X : Type u_1} {ε : Type u_2} [PseudoMetricSpace X] [MeasurableSpace X] [ENorm ε] {ι : Type u_4} (μ : Measure X) (𝓑 : Set ι) (c : ι → X) (r : ι → ℝ) (p : ℝ) (u : X → ε) (x : X) => ⨆ i ∈ 𝓑, (Metric.ball (c i) (r i)).indicator (fun (x : X) => (⨍⁻ (y : X) in Metric.ball (c i) (r i), ‖u y‖ₑ ^ p ∂μ) ^ p⁻¹) x`

#### `AllBallsCoverBalls` (def)
Lean: `(X : Type u_2) → [PseudoMetricSpace X] → ℝ → ℕ → Prop`
Docstring: For all `r`, balls of radius `r` in `X` are covered by `n` balls of radius `a * r`
Definition: `fun (X : Type u_2) [PseudoMetricSpace X] (a : ℝ) (n : ℕ) => ∀ (r : ℝ), BallsCoverBalls X (a * r) r n`

#### `localOscillation` (def)
Lean: `{𝕜 : Type u_3} → {X : Type u_4} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → Set X → C(X, 𝕜) → C(X, 𝕜) → ENNReal`
Docstring: The local oscillation of two functions w.r.t. a set `E`. This is `d_E` in the blueprint.
Definition: `fun {𝕜 : Type u_3} {X : Type u_4} [RCLike 𝕜] [PseudoMetricSpace X] (E : Set X) (f g : C(X, 𝕜)) => ⨆ z ∈ E ×ˢ E, ENNReal.ofReal ‖HAdd.hAdd (β := 𝕜) (HSub.hSub (β := 𝕜) (HSub.hSub (α := 𝕜) (β := 𝕜) (f z.1 : 𝕜) (g z.1 : 𝕜)) (f z.2 : 𝕜)) (g z.2 : 𝕜)‖`

#### `GridStructure.s` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → ℤ`
Docstring: scale functions
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.4`

#### `GridStructure.c` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → X`
Docstring: Center functions
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.5`

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

#### `instFunLikeΘ` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → FunLike (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) X 𝕜`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] => DFunLike.mk (β := fun (x : X) => 𝕜) (fun (f : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) => ⇑(coeΘ f)) ⋯`

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

#### `upperRadius` (def)
Lean: `{X : Type u_2} → [inst : PseudoMetricSpace X] → [inst_1 : FunctionDistances ℝ X] → (X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _ → X → ENNReal`
Docstring: `R_Q(θ, x)` defined in (1.1.17).
Definition: `fun {X : Type u_2} [PseudoMetricSpace X] [FunctionDistances ℝ X] (Q : X → @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (θ : @Θ _ X Real.normedField UniformSpace.toTopologicalSpace _) (x : X) => ⨆ (r : ℝ), ⨆ (_ : dist_{x, r} θ (Q x) < (1 : ℝ)), ENNReal.ofReal r`

#### `Ks` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {K : X → X → ℂ} → [inst : PseudoMetricSpace X] → [KernelProofData a K] → ℤ → X → X → ℂ`
Docstring: K_s in the blueprint
Definition: `fun {X : Type u_1} {a : ℕ} {K : X → X → ℂ} [PseudoMetricSpace X] [KernelProofData a K] (s : ℤ) (x y : X) => K x y * ↑(ψ (defaultD a) (HPow.hPow (α := ℝ) (↑(defaultD a)) (-s) * dist x y))`

#### `TileLike.toSet` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → TileLike X (F := F) (G := G) → Set X`
Docstring: From a TileLike, we can construct a set. This is used in the definitions `E₁` and `E₂`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (t : TileLike X (F := F) (G := G)) => ↑(t.fst (F := F) (G := G)) ∩ G ∩ ⇑(Q (F := F) (G := G)) ⁻¹' t.snd (F := F) (G := G)`

## Translations

### `dach`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔄 : Set (𝔓 X)) (p : 𝔓 X) (g : X → ℂ) : ENNReal`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → 𝔓 X → (X → ℂ) → ENNReal`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔄 : Set (𝔓 X)) (p : 𝔓 X) (g : X → ℂ) => HMul.hMul (α := ENNReal) (((volume : Measure X) (Metric.ball (𝔠 p) ((14 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p))))⁻¹ : ENNReal) (∫⁻ (x : X), ∑ p' : 𝔓 X with (p' ∈ 𝔄 ∧ 𝔰 p' ≤ 𝔰 p) ∧ ↑(𝓘 p') ⊆ Metric.ball (𝔠 p) ((14 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p)), ((1 : ENNReal) + edist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / (4 : ℝ)} (𝒬 p') (𝒬 p)) ^ (-((2 : ℝ) * HPow.hPow (α := ℝ) ↑a (2 : ℕ) + HPow.hPow (α := ℝ) ↑a (3 : ℕ))⁻¹) * (E (F := F) (G := G) p').indicator (fun (x : X) => ‖g x‖ₑ) x)`
Docstring: `h(p)` in the proof of Lemma 6.1.4 (**d**ens₁ **a**nti**c**hain **h**).
English: Setting: let $X$ be a metric space, let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$, and $F, G \subseteq X$, and assume given a `ProofData a q K σ₁ σ₂ F G` structure (per its docstring, the data common through most of chapters 2-7); through its `KernelProofData` component it makes $X$ a doubling metric measure space with constant $2^a$ (`defaultA a`), and $\mathrm{volume}$ denotes the resulting measure on $X$. Let $Q := $ `ProofData.Q`, the simple function from $X$ to the type $\Theta(X)$ of functions supplied by this data (via its compatible-functions component). Assume further a tile structure `TileStructure Q D κ S o` with $D := \mathrm{defaultD}(a) = 2^{c_0 a^2}$ (where $c_0 \in \mathbb{N}$ is the project constant `𝕔`, per its docstring fixed equal to $100$), $\kappa := \mathrm{defaultκ}(a) = 2^{-10a}$, $S := \mathrm{defaultS}(X)$, the least positive natural number $n$ such that $-n \le \sigma_1(x)$ and $\sigma_2(x) \le n$ for all $x \in X$ and $F, G \subseteq B(o, D^n/4)$, and $o := \mathrm{cancelPt}(X)$ (per its docstring, the point $o$ of the blueprint; it is a chosen point at which every function in $\Theta(X)$ vanishes). Let $\mathfrak{P}(X)$ be the (finite) type of tiles of this structure; for a tile $\mathfrak{p}$ let $\mathcal{I}(\mathfrak{p})$ be its grid cube (viewed as a subset of $X$), $\mathfrak{c}(\mathfrak{p}) \in X$ the centre and $\mathfrak{s}(\mathfrak{p}) \in \mathbb{Z}$ the scale of $\mathcal{I}(\mathfrak{p})$, $\mathcal{Q}(\mathfrak{p}) \in \Theta(X)$ the tile's frequency (`𝒬 p`), $\Omega(\mathfrak{p}) \subseteq \Theta(X)$ its frequency set (`Ω p`), and $E(\mathfrak{p}) := \{x \in \mathcal{I}(\mathfrak{p}) : Q(x) \in \Omega(\mathfrak{p}),\ \sigma_1(x) \le \mathfrak{s}(\mathfrak{p}) \le \sigma_2(x)\}$. For $x \in X$ and $r \in \mathbb{R}$ let $d_{x,r}$ denote the extended distance on $\Theta(X)$ of the pseudometric attached to $(x, r)$ by the function-distance structure (`FunctionDistances.metric x r`).

Definition (`dach`): for a set of tiles $\mathfrak{A} \subseteq \mathfrak{P}(X)$, a tile $\mathfrak{p} \in \mathfrak{P}(X)$ and a function $g : X \to \mathbb{C}$, `dach 𝔄 p g` is the element of $[0,\infty]$ $$\mathrm{dach}(\mathfrak{A}, \mathfrak{p}, g) := \mathrm{volume}\big(B_{\mathfrak{p}}\big)^{-1} \int_X \sum_{\substack{\mathfrak{p}' \in \mathfrak{A},\ \mathfrak{s}(\mathfrak{p}') \le \mathfrak{s}(\mathfrak{p}),\\ \mathcal{I}(\mathfrak{p}') \subseteq B_{\mathfrak{p}}}} \Big(1 + d_{\mathfrak{c}(\mathfrak{p}'),\, D^{\mathfrak{s}(\mathfrak{p}')}/4}\big(\mathcal{Q}(\mathfrak{p}'), \mathcal{Q}(\mathfrak{p})\big)\Big)^{-1/(2a^2 + a^3)}\, \mathbf{1}_{E(\mathfrak{p}')}(x)\, \|g(x)\|_e \, d\mathrm{volume}(x),$$ where $B_{\mathfrak{p}} := B\big(\mathfrak{c}(\mathfrak{p}), 14 D^{\mathfrak{s}(\mathfrak{p})}\big)$ is the open ball, the integral is the Lebesgue integral (`∫⁻`) of a $[0,\infty]$-valued function, $\|g(x)\|_e \in [0,\infty]$ is the extended norm, and inversion and powers are taken in $[0,\infty]$. Per its docstring, this is the quantity $h(\mathfrak{p})$ in the proof of Lemma 6.1.4.

### `antichain_operator_le_volume`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (hf : Measurable f) (hfF : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hA : A ⊆ G) : ∫⁻ (x : X) in A, ‖carlesonSum 𝔄 f x‖ₑ ≤ ↑(C2_0_3 a (nnq X)) * dens₁ 𝔄 ^ ((q - 1) / (8 * ↑a ^ 4)) * dens₂ 𝔄 ^ (q⁻¹ - 2⁻¹) * volume F ^ (1 / 2) * volume G ^ (1 / 2)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {𝔄 : Set (𝔓 X)} {f : X → ℂ} {A : Set X}, IsAntichain (fun (x1 x2 : 𝔓 X) => x1 ≤ x2) 𝔄 → Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → A ⊆ G → ∫⁻ (x : X) in A, ‖carlesonSum (F := F) (G := G) 𝔄 f x‖ₑ ≤ ↑(C2_0_3 a (nnq X (F := F) (G := G))) * dens₁ (F := F) (G := G) 𝔄 ^ ((q - (1 : ℝ)) / ((8 : ℝ) * HPow.hPow (α := ℝ) ↑a (4 : ℕ))) * dens₂ (F := F) (G := G) 𝔄 ^ (q⁻¹ - (2 : ℝ)⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (1 / 2 : ℝ) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) (1 / 2 : ℝ)`
Docstring: Version of the antichain operator theorem, but controlling the integral of the norm instead of the integral of the function multiplied by another function, and with the upper bound in terms of `volume F` and `volume G`.
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7). Through this instance $X$ carries a `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$, whose measure (`volume`) we denote by $\mu$, and a `CompatibleFunctions ℝ X (2^a)` structure, which provides a type $\Theta(X)$ of continuous real-valued functions on $X$; let $Q : X\to\Theta(X)$ be the simple function given by the field `Q` of the `ProofData` instance. Let $\mathsf b\in\mathbb N$ be the project constant `𝕔` (per its docstring fixed equal to $100$), $D=\mathrm{defaultD}(a)=2^{\mathsf b a^2}$, $\kappa=\mathrm{default}\kappa(a)=2^{-10a}$, $S=\mathrm{defaultS}(X)\in\mathbb N$ (the natural number `defaultS` determined by the `ProofData`), and $o=\mathrm{cancelPt}(X)\in X$ (the point `cancelPt X`, chosen so that every function in $\Theta(X)$ vanishes at it). Assume a tile structure `TileStructure Q D κ S o` on $X$, and let $\mathfrak P(X)$ be its (finite) type of tiles, partially ordered by the project order `instPartialOrder𝔓Real`. For a tile $p\in\mathfrak P(X)$, let $\mathcal I(p)$ be its cube (the project map `𝓘`), $\mathfrak c(p)\in X$ and $\mathfrak s(p)\in\mathbb Z$ the project center and scale of $p$ (defined as the center `c` and scale `s` of the cube $\mathcal I(p)$ in the grid structure), and $E(p)\subseteq X$ the project set `E p` (docstring: the set $E$ defined in Proposition 2.0.2), namely the set of $x\in\mathcal I(p)$ with $Q(x)\in\Omega(p)$ and $\sigma_1(x)\le\mathfrak s(p)\le\sigma_2(x)$, where $\Omega(p)$ is the field `Ω` of the tile structure. For a set of tiles $\mathfrak A\subseteq\mathfrak P(X)$ let $\mathrm{dens}_1(\mathfrak A),\mathrm{dens}_2(\mathfrak A)\in[0,\infty]$ be the project densities `dens₁ 𝔄` and `dens₂ 𝔄`. For $\mathfrak A\subseteq\mathfrak P(X)$, $h : X\to\mathbb C$ and $x\in X$, let $T_{\mathfrak A}h(x)=\mathrm{carlesonSum}(\mathfrak A,h)(x)=\sum_{p\in\mathfrak A}\mathrm{carlesonOn}(p,h)(x)$, where $\mathrm{carlesonOn}(p,\cdot)$ is the project operator `carlesonOn` (docstring: the operator $T_p$ defined in Proposition 2.0.2). Let $\bar q\in\mathbb R_{\ge0}$ be $q$ regarded as a nonnegative real (the project value `nnq X`), and let $C_{2.0.3}(a,\bar q)\in\mathbb R_{\ge 0}$ be the project constant `C2_0_3 a (nnq X)`, namely $2^{(\mathsf b+5+\lfloor\mathsf b/8\rfloor)a^3}/(\bar q-1)$ computed in $\mathbb R_{\ge0}$ (with truncated subtraction). Here $\|\cdot\|_{L^2}\in[0,\infty]$ denotes the $L^2(\mu)$ norm (`eLpNorm · 2 volume`), $\|\cdot\|_e$ the extended norm in $[0,\infty]$, and all right-hand sides are computed in $[0,\infty]$. Let $\mathfrak A\subseteq\mathfrak P(X)$ be an antichain with respect to $\le$, let $f : X\to\mathbb C$ be measurable with $\|f(x)\|\le\mathbf 1_F(x)$ for all $x\in X$, and let $A\subseteq X$ with $A\subseteq G$. Then $$\int_A\|T_{\mathfrak A}f(x)\|_e\,d\mu(x)\le C_{2.0.3}(a,\bar q)\,\mathrm{dens}_1(\mathfrak A)^{\frac{q-1}{8a^4}}\,\mathrm{dens}_2(\mathfrak A)^{q^{-1}-2^{-1}}\,\mu(F)^{1/2}\,\mu(G)^{1/2},$$ the left side being a lower Lebesgue integral.

### `dens1_antichain_sq`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (hg : Measurable g) (hgG : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : eLpNorm (adjointCarlesonSum 𝔄 g) 2 volume ^ 2 ≤ (↑(C6_1_4 a) * dens₁ 𝔄 ^ (8 * ↑a ^ 4)⁻¹ * eLpNorm g 2 volume) ^ 2`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {𝔄 : Set (𝔓 X)} {g : X → ℂ}, IsAntichain (fun (x1 x2 : 𝔓 X) => x1 ≤ x2) 𝔄 → Measurable g → (∀ (x : X), ‖g x‖ ≤ G.indicator (1 : X → ℝ) x) → @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace (adjointCarlesonSum (F := F) (G := G) 𝔄 g) (2 : ENNReal) volume ^ (2 : ℕ) ≤ (↑(C6_1_4 a) * dens₁ (F := F) (G := G) 𝔄 ^ ((8 : ℝ) * HPow.hPow (α := ℝ) ↑a (4 : ℕ))⁻¹ * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace g (2 : ENNReal) volume) ^ (2 : ℕ)`
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7). Through this instance $X$ carries a `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$, whose measure (`volume`) we denote by $\mu$, and a `CompatibleFunctions ℝ X (2^a)` structure, which provides a type $\Theta(X)$ of continuous real-valued functions on $X$; let $Q : X\to\Theta(X)$ be the simple function given by the field `Q` of the `ProofData` instance. Let $\mathsf b\in\mathbb N$ be the project constant `𝕔` (per its docstring fixed equal to $100$), $D=\mathrm{defaultD}(a)=2^{\mathsf b a^2}$, $\kappa=\mathrm{default}\kappa(a)=2^{-10a}$, $S=\mathrm{defaultS}(X)\in\mathbb N$ (the natural number `defaultS` determined by the `ProofData`), and $o=\mathrm{cancelPt}(X)\in X$ (the point `cancelPt X`, chosen so that every function in $\Theta(X)$ vanishes at it). Assume a tile structure `TileStructure Q D κ S o` on $X$, and let $\mathfrak P(X)$ be its (finite) type of tiles, partially ordered by the project order `instPartialOrder𝔓Real`. For a tile $p\in\mathfrak P(X)$, let $\mathcal I(p)$ be its cube (the project map `𝓘`), $\mathfrak c(p)\in X$ and $\mathfrak s(p)\in\mathbb Z$ the project center and scale of $p$ (defined as the center `c` and scale `s` of the cube $\mathcal I(p)$ in the grid structure), and $E(p)\subseteq X$ the project set `E p` (docstring: the set $E$ defined in Proposition 2.0.2), namely the set of $x\in\mathcal I(p)$ with $Q(x)\in\Omega(p)$ and $\sigma_1(x)\le\mathfrak s(p)\le\sigma_2(x)$, where $\Omega(p)$ is the field `Ω` of the tile structure. For a set of tiles $\mathfrak A\subseteq\mathfrak P(X)$ let $\mathrm{dens}_1(\mathfrak A),\mathrm{dens}_2(\mathfrak A)\in[0,\infty]$ be the project densities `dens₁ 𝔄` and `dens₂ 𝔄`. For $\mathfrak A\subseteq\mathfrak P(X)$ and $h : X\to\mathbb C$, let $T^*_{\mathfrak A}h=\mathrm{adjointCarlesonSum}(\mathfrak A,h)=\sum_{p\in\mathfrak A}\mathrm{adjointCarleson}(p,h)$ (docstring: $T_{\mathfrak C}^*g$ defined at the bottom of Section 7.4), where $\mathrm{adjointCarleson}(p,\cdot)$ is the project operator `adjointCarleson` (docstring: $T_p^*g$, defined above Lemma 7.4.1). Let $C_{6.1.4}(a)\in\mathbb R_{\ge0}$ be the project constant `C6_1_4 a` (docstring: constant appearing in Lemma 6.1.4; value $2^{117a^3}$ in the blueprint). Here $\|\cdot\|_{L^2}\in[0,\infty]$ denotes the $L^2(\mu)$ norm (`eLpNorm · 2 volume`), $\|\cdot\|_e$ the extended norm in $[0,\infty]$, and all right-hand sides are computed in $[0,\infty]$. Let $\mathfrak A\subseteq\mathfrak P(X)$ be an antichain with respect to $\le$, and let $g : X\to\mathbb C$ be measurable with $\|g(x)\|\le\mathbf 1_G(x)$ for all $x\in X$. Then $$\|T^*_{\mathfrak A}g\|_{L^2}^2\le\Big(C_{6.1.4}(a)\,\mathrm{dens}_1(\mathfrak A)^{(8a^4)^{-1}}\,\|g\|_{L^2}\Big)^2.$$

### `dens1_antichain_dach`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hg : Measurable g) (hgG : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : eLpNorm (adjointCarlesonSum 𝔄 g) 2 volume ^ 2 ≤ ↑(Tile.C6_1_5 a) * 2 ^ (6 * a + 1) * ∑ p with p ∈ 𝔄, dach 𝔄 p g * ∫⁻ (y : X) in E p, ‖g y‖ₑ`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {𝔄 : Set (𝔓 X)} {g : X → ℂ}, Measurable g → (∀ (x : X), ‖g x‖ ≤ G.indicator (1 : X → ℝ) x) → @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace (adjointCarlesonSum (F := F) (G := G) 𝔄 g) (2 : ENNReal) volume ^ (2 : ℕ) ≤ ↑(Tile.C6_1_5 a) * (2 : ENNReal) ^ ((6 : ℕ) * a + (1 : ℕ)) * ∑ p : 𝔓 X with p ∈ 𝔄, dach (F := F) (G := G) 𝔄 p g * ∫⁻ (y : X) in E (F := F) (G := G) p, ‖g y‖ₑ`
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7). Through this instance $X$ carries a `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$, whose measure (`volume`) we denote by $\mu$, and a `CompatibleFunctions ℝ X (2^a)` structure, which provides a type $\Theta(X)$ of continuous real-valued functions on $X$; let $Q : X\to\Theta(X)$ be the simple function given by the field `Q` of the `ProofData` instance. Let $\mathsf b\in\mathbb N$ be the project constant `𝕔` (per its docstring fixed equal to $100$), $D=\mathrm{defaultD}(a)=2^{\mathsf b a^2}$, $\kappa=\mathrm{default}\kappa(a)=2^{-10a}$, $S=\mathrm{defaultS}(X)\in\mathbb N$ (the natural number `defaultS` determined by the `ProofData`), and $o=\mathrm{cancelPt}(X)\in X$ (the point `cancelPt X`, chosen so that every function in $\Theta(X)$ vanishes at it). Assume a tile structure `TileStructure Q D κ S o` on $X$, and let $\mathfrak P(X)$ be its (finite) type of tiles, partially ordered by the project order `instPartialOrder𝔓Real`. For a tile $p\in\mathfrak P(X)$, let $\mathcal I(p)$ be its cube (the project map `𝓘`), $\mathfrak c(p)\in X$ and $\mathfrak s(p)\in\mathbb Z$ the project center and scale of $p$ (defined as the center `c` and scale `s` of the cube $\mathcal I(p)$ in the grid structure), and $E(p)\subseteq X$ the project set `E p` (docstring: the set $E$ defined in Proposition 2.0.2), namely the set of $x\in\mathcal I(p)$ with $Q(x)\in\Omega(p)$ and $\sigma_1(x)\le\mathfrak s(p)\le\sigma_2(x)$, where $\Omega(p)$ is the field `Ω` of the tile structure. For a set of tiles $\mathfrak A\subseteq\mathfrak P(X)$ let $\mathrm{dens}_1(\mathfrak A),\mathrm{dens}_2(\mathfrak A)\in[0,\infty]$ be the project densities `dens₁ 𝔄` and `dens₂ 𝔄`. For $\mathfrak A\subseteq\mathfrak P(X)$ and $h : X\to\mathbb C$, let $T^*_{\mathfrak A}h=\mathrm{adjointCarlesonSum}(\mathfrak A,h)=\sum_{p\in\mathfrak A}\mathrm{adjointCarleson}(p,h)$ (docstring: $T_{\mathfrak C}^*g$ defined at the bottom of Section 7.4), where $\mathrm{adjointCarleson}(p,\cdot)$ is the project operator `adjointCarleson` (docstring: $T_p^*g$, defined above Lemma 7.4.1). Here $\|\cdot\|_{L^2}\in[0,\infty]$ denotes the $L^2(\mu)$ norm (`eLpNorm · 2 volume`), $\|\cdot\|_e$ the extended norm in $[0,\infty]$, and all right-hand sides are computed in $[0,\infty]$. Let $C_{6.1.5}(a)\in\mathbb R_{\ge 0}$ be the project constant `Tile.C6_1_5 a`, namely $2^{(2\mathsf b+7+\lfloor\mathsf b/4\rfloor)a^3}$. Let $\mathfrak A\subseteq\mathfrak P(X)$ be any set of tiles and $g : X\to\mathbb C$ measurable with $\|g(x)\|\le\mathbf 1_G(x)$ for all $x\in X$; for $p\in\mathfrak P(X)$ let $h(p)\in[0,\infty]$ be the project quantity `dach 𝔄 p g` (docstring: $h(p)$ in the proof of Lemma 6.1.4). Then $$\|T^*_{\mathfrak A}g\|_{L^2}^2\le C_{6.1.5}(a)\,2^{6a+1}\sum_{p\in\mathfrak A}h(p)\int_{E(p)}\|g(y)\|_e\,d\mu(y),$$ the integrals being lower Lebesgue integrals.

### `dach_bound`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (mp : p ∈ 𝔄) (hg : Measurable g) (hgG : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) (hx : x₀ ∈ Metric.ball (𝔠 p) (14 * ↑(defaultD a) ^ 𝔰 p)) : dach 𝔄 p g ≤ ↑(C6_1_6 a) * dens₁ 𝔄 ^ (p₆ a)⁻¹ * M14 𝔄 (q₆ a) g x₀`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {𝔄 : Set (𝔓 X)} {g : X → ℂ}, IsAntichain (fun (x1 x2 : 𝔓 X) => x1 ≤ x2) 𝔄 → ∀ {p : 𝔓 X}, p ∈ 𝔄 → Measurable g → (∀ (x : X), ‖g x‖ ≤ G.indicator (1 : X → ℝ) x) → ∀ {x₀ : X}, x₀ ∈ Metric.ball (𝔠 p) ((14 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p)) → dach (F := F) (G := G) 𝔄 p g ≤ ↑(C6_1_6 a) * dens₁ (F := F) (G := G) 𝔄 ^ (p₆ a)⁻¹ * M14 (F := F) (G := G) 𝔄 (q₆ a) g x₀`
Docstring: Equations (6.1.34) to (6.1.37) in Lemma 6.1.4.
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7). Through this instance $X$ carries a `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$, whose measure (`volume`) we denote by $\mu$, and a `CompatibleFunctions ℝ X (2^a)` structure, which provides a type $\Theta(X)$ of continuous real-valued functions on $X$; let $Q : X\to\Theta(X)$ be the simple function given by the field `Q` of the `ProofData` instance. Let $\mathsf b\in\mathbb N$ be the project constant `𝕔` (per its docstring fixed equal to $100$), $D=\mathrm{defaultD}(a)=2^{\mathsf b a^2}$, $\kappa=\mathrm{default}\kappa(a)=2^{-10a}$, $S=\mathrm{defaultS}(X)\in\mathbb N$ (the natural number `defaultS` determined by the `ProofData`), and $o=\mathrm{cancelPt}(X)\in X$ (the point `cancelPt X`, chosen so that every function in $\Theta(X)$ vanishes at it). Assume a tile structure `TileStructure Q D κ S o` on $X$, and let $\mathfrak P(X)$ be its (finite) type of tiles, partially ordered by the project order `instPartialOrder𝔓Real`. For a tile $p\in\mathfrak P(X)$, let $\mathcal I(p)$ be its cube (the project map `𝓘`), $\mathfrak c(p)\in X$ and $\mathfrak s(p)\in\mathbb Z$ the project center and scale of $p$ (defined as the center `c` and scale `s` of the cube $\mathcal I(p)$ in the grid structure), and $E(p)\subseteq X$ the project set `E p` (docstring: the set $E$ defined in Proposition 2.0.2), namely the set of $x\in\mathcal I(p)$ with $Q(x)\in\Omega(p)$ and $\sigma_1(x)\le\mathfrak s(p)\le\sigma_2(x)$, where $\Omega(p)$ is the field `Ω` of the tile structure. For a set of tiles $\mathfrak A\subseteq\mathfrak P(X)$ let $\mathrm{dens}_1(\mathfrak A),\mathrm{dens}_2(\mathfrak A)\in[0,\infty]$ be the project densities `dens₁ 𝔄` and `dens₂ 𝔄`. (Equations (6.1.34) to (6.1.37) in Lemma 6.1.4.) Let $C_{6.1.6}(a)=2^{5a}\in\mathbb R_{\ge0}$ (project constant `C6_1_6 a`), $r_6(a)=4a^4\in\mathbb R$ (project value `p₆ a`) and $r_6'(a)=(1-r_6(a)^{-1})^{-1}\in\mathbb R$ (project value `q₆ a`, its Hölder conjugate exponent). For $\mathfrak A\subseteq\mathfrak P(X)$, $t\in\mathbb R$, $h : X\to\mathbb C$ and $x\in X$ let $M_{14}(\mathfrak A,t,h)(x)\in[0,\infty]$ be the project maximal function `M14 𝔄 t h x`, i.e. $\sup_{p'\in\mathfrak A}\mathbf 1_{B_{p'}}(x)\big(⨍_{B_{p'}}\|h(y)\|_e^{t}\,d\mu(y)\big)^{1/t}$ with $B_{p'}=B(\mathfrak c(p'),14D^{\mathfrak s(p')})$. Let $\mathfrak A\subseteq\mathfrak P(X)$ be an antichain with respect to $\le$, let $p\in\mathfrak A$, let $g : X\to\mathbb C$ be measurable with $\|g(x)\|\le\mathbf 1_G(x)$ for all $x\in X$, and let $x_0\in X$ lie in the open ball $B(\mathfrak c(p),14D^{\mathfrak s(p)})$. Let $h(p)\in[0,\infty]$ be the project quantity `dach 𝔄 p g` (docstring: $h(p)$ in the proof of Lemma 6.1.4). Then $$h(p)\le C_{6.1.6}(a)\,\mathrm{dens}_1(\mathfrak A)^{r_6(a)^{-1}}\,M_{14}(\mathfrak A,r_6'(a),g)(x_0)$$ in $[0,\infty]$.

### `dens1_antichain`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (hf : Measurable f) (hfF : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (hgG : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum 𝔄 f x‖ₑ ≤ ↑(C6_1_4 a) * dens₁ 𝔄 ^ (8 * ↑a ^ 4)⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {𝔄 : Set (𝔓 X)} {f g : X → ℂ}, IsAntichain (fun (x1 x2 : 𝔓 X) => x1 ≤ x2) 𝔄 → Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable g → (∀ (x : X), ‖g x‖ ≤ G.indicator (1 : X → ℝ) x) → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (α := ℂ) ((starRingEnd ℂ) (g x) : ℂ) (carlesonSum (F := F) (G := G) 𝔄 f x)) ≤ ↑(C6_1_4 a) * dens₁ (F := F) (G := G) 𝔄 ^ ((8 : ℝ) * HPow.hPow (α := ℝ) ↑a (4 : ℕ))⁻¹ * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (2 : ENNReal) volume * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace g (2 : ENNReal) volume`
Docstring: Lemma 6.1.4.
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7). Through this instance $X$ carries a `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$, whose measure (`volume`) we denote by $\mu$, and a `CompatibleFunctions ℝ X (2^a)` structure, which provides a type $\Theta(X)$ of continuous real-valued functions on $X$; let $Q : X\to\Theta(X)$ be the simple function given by the field `Q` of the `ProofData` instance. Let $\mathsf b\in\mathbb N$ be the project constant `𝕔` (per its docstring fixed equal to $100$), $D=\mathrm{defaultD}(a)=2^{\mathsf b a^2}$, $\kappa=\mathrm{default}\kappa(a)=2^{-10a}$, $S=\mathrm{defaultS}(X)\in\mathbb N$ (the natural number `defaultS` determined by the `ProofData`), and $o=\mathrm{cancelPt}(X)\in X$ (the point `cancelPt X`, chosen so that every function in $\Theta(X)$ vanishes at it). Assume a tile structure `TileStructure Q D κ S o` on $X$, and let $\mathfrak P(X)$ be its (finite) type of tiles, partially ordered by the project order `instPartialOrder𝔓Real`. For a tile $p\in\mathfrak P(X)$, let $\mathcal I(p)$ be its cube (the project map `𝓘`), $\mathfrak c(p)\in X$ and $\mathfrak s(p)\in\mathbb Z$ the project center and scale of $p$ (defined as the center `c` and scale `s` of the cube $\mathcal I(p)$ in the grid structure), and $E(p)\subseteq X$ the project set `E p` (docstring: the set $E$ defined in Proposition 2.0.2), namely the set of $x\in\mathcal I(p)$ with $Q(x)\in\Omega(p)$ and $\sigma_1(x)\le\mathfrak s(p)\le\sigma_2(x)$, where $\Omega(p)$ is the field `Ω` of the tile structure. For a set of tiles $\mathfrak A\subseteq\mathfrak P(X)$ let $\mathrm{dens}_1(\mathfrak A),\mathrm{dens}_2(\mathfrak A)\in[0,\infty]$ be the project densities `dens₁ 𝔄` and `dens₂ 𝔄`. For $\mathfrak A\subseteq\mathfrak P(X)$, $h : X\to\mathbb C$ and $x\in X$, let $T_{\mathfrak A}h(x)=\mathrm{carlesonSum}(\mathfrak A,h)(x)=\sum_{p\in\mathfrak A}\mathrm{carlesonOn}(p,h)(x)$, where $\mathrm{carlesonOn}(p,\cdot)$ is the project operator `carlesonOn` (docstring: the operator $T_p$ defined in Proposition 2.0.2). Let $C_{6.1.4}(a)\in\mathbb R_{\ge0}$ be the project constant `C6_1_4 a` (docstring: constant appearing in Lemma 6.1.4; value $2^{117a^3}$ in the blueprint). Here $\|\cdot\|_{L^2}\in[0,\infty]$ denotes the $L^2(\mu)$ norm (`eLpNorm · 2 volume`), $\|\cdot\|_e$ the extended norm in $[0,\infty]$, and all right-hand sides are computed in $[0,\infty]$. (Lemma 6.1.4.) Let $\mathfrak A\subseteq\mathfrak P(X)$ be an antichain with respect to $\le$, and let $f,g : X\to\mathbb C$ be measurable with $\|f(x)\|\le\mathbf 1_F(x)$ and $\|g(x)\|\le\mathbf 1_G(x)$ for all $x\in X$. Then $$\Big\|\int_X\overline{g(x)}\,T_{\mathfrak A}f(x)\,d\mu(x)\Big\|_e\le C_{6.1.4}(a)\,\mathrm{dens}_1(\mathfrak A)^{(8a^4)^{-1}}\,\|f\|_{L^2}\,\|g\|_{L^2}.$$

### `antichain_operator`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (hf : Measurable f) (hf1 : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (hg1 : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum 𝔄 f x‖ₑ ≤ ↑(C2_0_3 a (nnq X)) * dens₁ 𝔄 ^ ((q - 1) / (8 * ↑a ^ 4)) * dens₂ 𝔄 ^ (q⁻¹ - 2⁻¹) * eLpNorm f 2 volume * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {𝔄 : Set (𝔓 X)} {f g : X → ℂ}, IsAntichain (fun (x1 x2 : 𝔓 X) => x1 ≤ x2) 𝔄 → Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable g → (∀ (x : X), ‖g x‖ ≤ G.indicator (1 : X → ℝ) x) → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (α := ℂ) ((starRingEnd ℂ) (g x) : ℂ) (carlesonSum (F := F) (G := G) 𝔄 f x)) ≤ ↑(C2_0_3 a (nnq X (F := F) (G := G))) * dens₁ (F := F) (G := G) 𝔄 ^ ((q - (1 : ℝ)) / ((8 : ℝ) * HPow.hPow (α := ℝ) ↑a (4 : ℕ))) * dens₂ (F := F) (G := G) 𝔄 ^ (q⁻¹ - (2 : ℝ)⁻¹) * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (2 : ENNReal) volume * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace g (2 : ENNReal) volume`
Docstring: Proposition 2.0.3.
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7). Through this instance $X$ carries a `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$, whose measure (`volume`) we denote by $\mu$, and a `CompatibleFunctions ℝ X (2^a)` structure, which provides a type $\Theta(X)$ of continuous real-valued functions on $X$; let $Q : X\to\Theta(X)$ be the simple function given by the field `Q` of the `ProofData` instance. Let $\mathsf b\in\mathbb N$ be the project constant `𝕔` (per its docstring fixed equal to $100$), $D=\mathrm{defaultD}(a)=2^{\mathsf b a^2}$, $\kappa=\mathrm{default}\kappa(a)=2^{-10a}$, $S=\mathrm{defaultS}(X)\in\mathbb N$ (the natural number `defaultS` determined by the `ProofData`), and $o=\mathrm{cancelPt}(X)\in X$ (the point `cancelPt X`, chosen so that every function in $\Theta(X)$ vanishes at it). Assume a tile structure `TileStructure Q D κ S o` on $X$, and let $\mathfrak P(X)$ be its (finite) type of tiles, partially ordered by the project order `instPartialOrder𝔓Real`. For a tile $p\in\mathfrak P(X)$, let $\mathcal I(p)$ be its cube (the project map `𝓘`), $\mathfrak c(p)\in X$ and $\mathfrak s(p)\in\mathbb Z$ the project center and scale of $p$ (defined as the center `c` and scale `s` of the cube $\mathcal I(p)$ in the grid structure), and $E(p)\subseteq X$ the project set `E p` (docstring: the set $E$ defined in Proposition 2.0.2), namely the set of $x\in\mathcal I(p)$ with $Q(x)\in\Omega(p)$ and $\sigma_1(x)\le\mathfrak s(p)\le\sigma_2(x)$, where $\Omega(p)$ is the field `Ω` of the tile structure. For a set of tiles $\mathfrak A\subseteq\mathfrak P(X)$ let $\mathrm{dens}_1(\mathfrak A),\mathrm{dens}_2(\mathfrak A)\in[0,\infty]$ be the project densities `dens₁ 𝔄` and `dens₂ 𝔄`. For $\mathfrak A\subseteq\mathfrak P(X)$, $h : X\to\mathbb C$ and $x\in X$, let $T_{\mathfrak A}h(x)=\mathrm{carlesonSum}(\mathfrak A,h)(x)=\sum_{p\in\mathfrak A}\mathrm{carlesonOn}(p,h)(x)$, where $\mathrm{carlesonOn}(p,\cdot)$ is the project operator `carlesonOn` (docstring: the operator $T_p$ defined in Proposition 2.0.2). Let $\bar q\in\mathbb R_{\ge0}$ be $q$ regarded as a nonnegative real (the project value `nnq X`), and let $C_{2.0.3}(a,\bar q)\in\mathbb R_{\ge 0}$ be the project constant `C2_0_3 a (nnq X)`, namely $2^{(\mathsf b+5+\lfloor\mathsf b/8\rfloor)a^3}/(\bar q-1)$ computed in $\mathbb R_{\ge0}$ (with truncated subtraction). Here $\|\cdot\|_{L^2}\in[0,\infty]$ denotes the $L^2(\mu)$ norm (`eLpNorm · 2 volume`), $\|\cdot\|_e$ the extended norm in $[0,\infty]$, and all right-hand sides are computed in $[0,\infty]$. (Proposition 2.0.3.) Let $\mathfrak A\subseteq\mathfrak P(X)$ be an antichain with respect to $\le$, and let $f,g : X\to\mathbb C$ be measurable with $\|f(x)\|\le\mathbf 1_F(x)$ and $\|g(x)\|\le\mathbf 1_G(x)$ for all $x\in X$. Then $$\Big\|\int_X\overline{g(x)}\,T_{\mathfrak A}f(x)\,d\mu(x)\Big\|_e\le C_{2.0.3}(a,\bar q)\,\mathrm{dens}_1(\mathfrak A)^{\frac{q-1}{8a^4}}\,\mathrm{dens}_2(\mathfrak A)^{q^{-1}-2^{-1}}\,\|f\|_{L^2}\,\|g\|_{L^2}.$$

### `antichain_operator'`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (hf : Measurable f) (hfF : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hA : A ⊆ G) : ∫⁻ (x : X) in A, ‖carlesonSum 𝔄 f x‖ₑ ≤ ↑(C2_0_3 a (nnq X)) * dens₁ 𝔄 ^ ((q - 1) / (8 * ↑a ^ 4)) * dens₂ 𝔄 ^ (q⁻¹ - 2⁻¹) * eLpNorm f 2 volume * volume G ^ (1 / 2)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {𝔄 : Set (𝔓 X)} {f : X → ℂ} {A : Set X}, IsAntichain (fun (x1 x2 : 𝔓 X) => x1 ≤ x2) 𝔄 → Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → A ⊆ G → ∫⁻ (x : X) in A, ‖carlesonSum (F := F) (G := G) 𝔄 f x‖ₑ ≤ ↑(C2_0_3 a (nnq X (F := F) (G := G))) * dens₁ (F := F) (G := G) 𝔄 ^ ((q - (1 : ℝ)) / ((8 : ℝ) * HPow.hPow (α := ℝ) ↑a (4 : ℕ))) * dens₂ (F := F) (G := G) 𝔄 ^ (q⁻¹ - (2 : ℝ)⁻¹) * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (2 : ENNReal) volume * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) (1 / 2 : ℝ)`
Docstring: Version of the antichain operator theorem, but controlling the integral of the norm instead of the integral of the function multiplied by another function.
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7). Through this instance $X$ carries a `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$, whose measure (`volume`) we denote by $\mu$, and a `CompatibleFunctions ℝ X (2^a)` structure, which provides a type $\Theta(X)$ of continuous real-valued functions on $X$; let $Q : X\to\Theta(X)$ be the simple function given by the field `Q` of the `ProofData` instance. Let $\mathsf b\in\mathbb N$ be the project constant `𝕔` (per its docstring fixed equal to $100$), $D=\mathrm{defaultD}(a)=2^{\mathsf b a^2}$, $\kappa=\mathrm{default}\kappa(a)=2^{-10a}$, $S=\mathrm{defaultS}(X)\in\mathbb N$ (the natural number `defaultS` determined by the `ProofData`), and $o=\mathrm{cancelPt}(X)\in X$ (the point `cancelPt X`, chosen so that every function in $\Theta(X)$ vanishes at it). Assume a tile structure `TileStructure Q D κ S o` on $X$, and let $\mathfrak P(X)$ be its (finite) type of tiles, partially ordered by the project order `instPartialOrder𝔓Real`. For a tile $p\in\mathfrak P(X)$, let $\mathcal I(p)$ be its cube (the project map `𝓘`), $\mathfrak c(p)\in X$ and $\mathfrak s(p)\in\mathbb Z$ the project center and scale of $p$ (defined as the center `c` and scale `s` of the cube $\mathcal I(p)$ in the grid structure), and $E(p)\subseteq X$ the project set `E p` (docstring: the set $E$ defined in Proposition 2.0.2), namely the set of $x\in\mathcal I(p)$ with $Q(x)\in\Omega(p)$ and $\sigma_1(x)\le\mathfrak s(p)\le\sigma_2(x)$, where $\Omega(p)$ is the field `Ω` of the tile structure. For a set of tiles $\mathfrak A\subseteq\mathfrak P(X)$ let $\mathrm{dens}_1(\mathfrak A),\mathrm{dens}_2(\mathfrak A)\in[0,\infty]$ be the project densities `dens₁ 𝔄` and `dens₂ 𝔄`. For $\mathfrak A\subseteq\mathfrak P(X)$, $h : X\to\mathbb C$ and $x\in X$, let $T_{\mathfrak A}h(x)=\mathrm{carlesonSum}(\mathfrak A,h)(x)=\sum_{p\in\mathfrak A}\mathrm{carlesonOn}(p,h)(x)$, where $\mathrm{carlesonOn}(p,\cdot)$ is the project operator `carlesonOn` (docstring: the operator $T_p$ defined in Proposition 2.0.2). Let $\bar q\in\mathbb R_{\ge0}$ be $q$ regarded as a nonnegative real (the project value `nnq X`), and let $C_{2.0.3}(a,\bar q)\in\mathbb R_{\ge 0}$ be the project constant `C2_0_3 a (nnq X)`, namely $2^{(\mathsf b+5+\lfloor\mathsf b/8\rfloor)a^3}/(\bar q-1)$ computed in $\mathbb R_{\ge0}$ (with truncated subtraction). Here $\|\cdot\|_{L^2}\in[0,\infty]$ denotes the $L^2(\mu)$ norm (`eLpNorm · 2 volume`), $\|\cdot\|_e$ the extended norm in $[0,\infty]$, and all right-hand sides are computed in $[0,\infty]$. Let $\mathfrak A\subseteq\mathfrak P(X)$ be an antichain with respect to $\le$, let $f : X\to\mathbb C$ be measurable with $\|f(x)\|\le\mathbf 1_F(x)$ for all $x\in X$, and let $A\subseteq X$ with $A\subseteq G$. Then $$\int_A\|T_{\mathfrak A}f(x)\|_e\,d\mu(x)\le C_{2.0.3}(a,\bar q)\,\mathrm{dens}_1(\mathfrak A)^{\frac{q-1}{8a^4}}\,\mathrm{dens}_2(\mathfrak A)^{q^{-1}-2^{-1}}\,\|f\|_{L^2}\,\mu(G)^{1/2},$$ the left side being a lower Lebesgue integral.
