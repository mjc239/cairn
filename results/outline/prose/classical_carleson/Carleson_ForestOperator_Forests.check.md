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

#### `C2_0_4` (def)
Lean: `ℕ → ℝ → ℕ → NNReal`
Docstring: The constant used in `forest_operator`. Has value `2 ^ (440 * a ^ 3 - (q - 1) / q * n)` in the blueprint.
Definition: `wrapped✝.1`

#### `CompatibleFunctions.toFunctionDistances` (def)
Lean: `{𝕜 : outParam (Type u_3)} → {X : Type u} → {A : outParam ℕ} → {inst : RCLike 𝕜} → {inst_1 : PseudoMetricSpace X} → [self : CompatibleFunctions 𝕜 X A] → FunctionDistances 𝕜 X`
Definition: `fun {𝕜 : outParam (Type u_3)} (X : Type u) {A : outParam ℕ} {inst : RCLike 𝕜} {inst_1 : PseudoMetricSpace X} [self : CompatibleFunctions 𝕜 X A] => self.1`

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

#### `TileStructure.Forest` (structure or class)
Lean: `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → Type u_1`
Docstring: An `n`-forest
Constructor (every field with its type): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → (𝔘 : Set (𝔓 X)) → (𝔗 : 𝔓 X → Set (𝔓 X)) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → (𝔗 u).Nonempty) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → (𝔗 u).OrdConnected) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → ∀ {p : 𝔓 X}, p ∈ 𝔗 u → 𝓘 p ≠ 𝓘 u) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → ∀ {p : 𝔓 X}, p ∈ 𝔗 u → smul (F := F) (G := G) (4 : ℝ) p ≤ smul (F := F) (G := G) (1 : ℝ) u) → (∀ {x : X}, stackSize (F := F) (G := G) 𝔘 x ≤ (2 : ℕ) ^ n) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → dens₁ (F := F) (G := G) (𝔗 u) ≤ (2 : ENNReal) ^ ((4 : ℝ) * ↑a - ↑n + (1 : ℝ))) → (∀ {u u' : 𝔓 X}, u ∈ 𝔘 → u' ∈ 𝔘 → u ≠ u' → ∀ {p : 𝔓 X}, p ∈ 𝔗 u' → 𝓘 p ≤ 𝓘 u → (2 : ℝ) ^ (defaultZ a * (n + (1 : ℕ))) < dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) (𝒬 u)) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → ∀ {p : 𝔓 X}, p ∈ 𝔗 u → Metric.ball (𝔠 p) ((8 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p)) ⊆ ↑(𝓘 u)) → Forest X (F := F) (G := G) n`

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

#### `dens₂` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ENNReal`
Docstring: This density is defined to live in `ℝ≥0∞`. Use `ENNReal.toReal` to get a real number.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔓' : Set (𝔓 X)) => ⨆ p ∈ 𝔓', ⨆ (r : ℝ), ⨆ (_ : r ≥ (4 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p)), HDiv.hDiv (α := ENNReal) (β := ENNReal) ((volume : Measure X) (F ∩ Metric.ball (𝔠 p) r) : ENNReal) ((volume : Measure X) (Metric.ball (𝔠 p) r) : ENNReal)`

#### `instFintype𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (𝔓.{u, u_1, u_2} X)`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.fintype_𝔓`

#### `𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → (X : Type u) → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [PreTileStructure.{u, u_1, u_2} Q D κ S o] → Type u`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] (X : Type u) {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X`

#### `TileStructure.Forest.C2_0_4_aux` (def)
Lean: `ℕ → NNReal`
Docstring: The constant in the `f` side of Proposition 2.0.4. Has value `2 ^ (283 * a ^ 3)` in the blueprint.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ (((2 : ℕ) * 𝕔 + (8 : ℕ) + 𝕔 / (2 : ℕ) + 𝕔 / (4 : ℕ)) * a ^ (3 : ℕ))`

#### `TileStructure.Forest.rowDecomp_zornset` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → Set (Set (𝔓 X))`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (s : Set (𝔓 X)) => {x : Set (𝔓 X) | x ⊆ s} ∩ {x : Set (𝔓 X) | x.PairwiseDisjoint (α := Set X) fun (x : 𝔓 X) => ↑(𝓘 x)} ∩ {x : Set (𝔓 X) | x ⊆ {u : 𝔓 X | Maximal (fun (x : Grid X) => x ∈ 𝓘 '' s) (𝓘 u)}}`

#### `TileStructure.Forest.𝔘` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → Set (𝔓 X)`
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] (a : ℕ) (q : ℝ) (K : X → X → ℂ) (σ₁ σ₂ : X → ℤ) (F G : Set X) [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (n : ℕ) (self : Forest X (F := F) (G := G) n) => self.1`

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

#### `PreTileStructure.𝒬` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X → @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.6`

#### `TileLike` (def)
Lean: `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Type u_1`
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => Grid X × (Set (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))ᵒᵈ`

#### `TileStructure.Row` (structure or class)
Lean: `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → Type u_1`
Docstring: An `n`-row
Constructor (every field with its type): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → (toForest : Forest X (F := F) (G := G) n) → (toForest.𝔘 (F := F) (G := G).PairwiseDisjoint (α := Set X) fun (u : 𝔓 X) => ↑(𝓘 u)) → Row X (F := F) (G := G) n`

#### `WithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → X → ℝ → Type u_2`
Docstring: Class used to endow `Θ X` with a pseudometric space structure.
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] (x : X) (r : ℝ) => @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`

#### `defaultZ` (def)
Lean: `ℕ → ℕ`
Docstring: The constant `Z` from (2.0.3).
Definition: `fun (a : ℕ) => (2 : ℕ) ^ ((12 : ℕ) * a)`

#### `dens₁` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ENNReal`
Docstring: This density is defined to live in `ℝ≥0∞`. Use `ENNReal.toReal` to get a real number.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔓' : Set (𝔓 X)) => ⨆ p' ∈ 𝔓', ⨆ (l : NNReal), ⨆ (_ : l ≥ (2 : NNReal)), HPow.hPow (β := ℝ) (↑l) (-↑a) * ⨆ p ∈ lowerCubes (F := F) (G := G) 𝔓', ⨆ (_ : smul (F := F) (G := G) (↑l) p' ≤ smul (F := F) (G := G) (↑l) p), HDiv.hDiv (α := ENNReal) (β := ENNReal) ((volume : Measure X) (E₂ (F := F) (G := G) (↑l) p) : ENNReal) ((volume : Measure X) ↑(𝓘 p) : ENNReal)`

#### `instPartialOrderGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → PartialOrder (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => PartialOrder.lift (fun (i : @GridStructure.Grid X _ inst inst_1 _ _ _ _ _) => (↑i, GridStructure.s i)) ⋯`

#### `instPartialOrderTileLike` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → PartialOrder (TileLike X (F := F) (G := G))`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => { le := instPartialOrderTileLike._aux_1, lt := instPartialOrderTileLike._aux_3, le_refl := ⋯, le_trans := ⋯, lt_iff_le_not_ge := ⋯, le_antisymm := ⋯ }`

#### `instPartialOrder𝔓Real` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → PartialOrder (𝔓 X)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => PartialOrder.lift (toTileLike (F := F) (G := G)) ⋯`

#### `instPseudoMetricSpaceWithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → {x : X} → {r : ℝ} → PseudoMetricSpace (WithFunctionDistance x r)`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] {x : X} {r : ℝ} => FunctionDistances.metric x r`

#### `smul` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℝ → 𝔓 X → TileLike X (F := F) (G := G)`
Docstring: This is not defined as such in the blueprint, but `λp ≲ λ'p'` can be written using `smul l p ≤ smul l' p'`. Beware: `smul 1 p` is very different from `toTileLike p`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (l : ℝ) (p : 𝔓 X) => (𝓘 p, ball_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) l)`

#### `stackSize` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → X → ℕ`
Docstring: The number of tiles `p` in `s` whose underlying cube `𝓘 p` contains `x`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (C : Set (𝔓 X)) (x : X) => ∑ p : 𝔓 X with p ∈ C, (↑(𝓘 p)).indicator (1 : X → ℕ) x`

#### `𝓘` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → Grid X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] => PreTileStructure.𝓘`

#### `𝔠` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => c (𝓘 p)`

#### `𝔰` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → ℤ`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => s (𝓘 p)`

#### `MeasureTheory.BoundedCompactSupport` (inductive)
Lean: `{X : Type u_1} → {E : Type u_2} → [TopologicalSpace X] → [inst : MeasurableSpace X] → [TopologicalSpace E] → [ENorm E] → [Zero E] → (X → E) → autoParam (Measure X) BoundedCompactSupport._auto_1 → Prop`
Docstring: Bounded compactly supported measurable functions
Constructor (every field with its type): `∀ {X : Type u_1} {E : Type u_2} [inst : TopologicalSpace X] [inst_1 : MeasurableSpace X] [inst_2 : TopologicalSpace E] [inst_3 : ENorm E] [inst_4 : Zero E] {f : X → E} {μ : autoParam (Measure X) BoundedCompactSupport._auto_1}, MemLp f ⊤ μ → HasCompactSupport f → BoundedCompactSupport f μ`

#### `TileStructure.Forest.C7_7_2_2` (def)
Lean: `ℕ → ℕ → NNReal`
Docstring: The constant used in `indicator_row_bound`. Has value `2 ^ (283 * a ^ 3 - n / 2)` in the blueprint.
Definition: `Forest.wrapped✝.1`

#### `TileStructure.Forest.adjointCarlesonRowSum` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → ℕ → (X → ℂ) → X → ℂ`
Docstring: The definition of `T_{ℜ_j}*f(x)`, defined above Lemma 7.7.2.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (t : Forest X (F := F) (G := G) n) (j : ℕ) (f : X → ℂ) (x : X) => ∑ u : 𝔓 X with u ∈ t.rowDecomp (F := F) (G := G) j, adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) f x`

#### `TileStructure.Forest.carlesonRowSum` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → ℕ → (X → ℂ) → X → ℂ`
Docstring: The definition of `T_{ℜ_j}f(x)`, defined above Lemma 7.7.2.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (t : Forest X (F := F) (G := G) n) (j : ℕ) (f : X → ℂ) (x : X) => ∑ u : 𝔓 X with u ∈ t.rowDecomp (F := F) (G := G) j, carlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) f x`

#### `TileStructure.Forest.G2_0_4` (def)
Lean: `ℕ → ℕ → NNReal`
Docstring: The constant on the `g` side of Proposition 2.0.4. Has value `2 ^ (440 * a ^ 3)` in the blueprint.
Definition: `fun (a n : ℕ) => (2 : NNReal) ^ (((3 : ℕ) * 𝕔 + (15 : ℕ) + (5 : ℕ) * (𝕔 / (4 : ℕ))) * a ^ (3 : ℕ)) * (2 : NNReal) ^ (-(↑n / (2 : ℝ)))`

#### `adjointCarlesonSum` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → (X → ℂ) → X → ℂ`
Docstring: The definition of `T_ℭ*g(x)`, defined at the bottom of Section 7.4
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) => ∑ p : 𝔓 X with p ∈ ℭ, adjointCarleson (F := F) (G := G) p f x`

#### `TileStructure.Forest.C7_4_4` (def)
Lean: `ℕ → ℕ → NNReal`
Docstring: The constant used in `correlation_separated_trees`. Has value `2 ^ (512 * a ^ 3 - 4 * n)` in the blueprint.
Definition: `Forest.wrapped✝.1`

#### `TileStructure.Forest.adjointBoundaryOperator` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → 𝔓 X → (X → ℂ) → X → ENNReal`
Docstring: The operator `S_{2,𝔲} f(x)`, given above Lemma 7.4.3.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (t : Forest X (F := F) (G := G) n) (u : 𝔓 X) (f : X → ℂ) (x : X) => ‖adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) f x‖ₑ + maximalFunction volume (Forest.𝓑 (F := F) (G := G)) (Forest.c𝓑 (F := F) (G := G)) (Forest.r𝓑 (F := F) (G := G)) (1 : ℝ) f x + ‖f x‖ₑ`

#### `TileStructure.Forest.C7_7_3` (def)
Lean: `ℕ → ℕ → NNReal`
Docstring: The constant used in `row_correlation`. Has value `2 ^ (876 * a ^ 3 - 4 * n)` in the blueprint.
Definition: `Forest.wrapped✝.1`

#### `𝕔` (def)
Lean: `ℕ`
Docstring: The main constant in the blueprint, driving all the construction, is `D = 2 ^ (100 * a ^ 2)`. It turns out that the proof is robust, and works for other values of `100`, giving better constants in the end. We will formalize it using a parameter `𝕔` (that we fix equal to `100` to follow the blueprint) and having `D = 2 ^ (𝕔 * a ^ 2)`. We register two lemmas `seven_le_c` and `c_le_100` and will never unfold `𝕔` from this point on.
Definition: `wrapped✝.1`

#### `CompatibleFunctions` (structure or class)
Lean: `(𝕜 : outParam (Type u_3)) → (X : Type u) → outParam ℕ → [RCLike 𝕜] → [PseudoMetricSpace X] → Type (max (u + 1) u_3)`
Docstring: A set `Θ` of (continuous) functions is compatible. `A` will usually be `2 ^ a`.
Constructor (every field with its type): `{𝕜 : outParam (Type u_3)} → {X : Type u} → {A : outParam ℕ} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [toFunctionDistances : FunctionDistances 𝕜 X] → (∃ (o : X), ∀ (f : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), (coeΘ f) o = (0 : 𝕜)) → (∀ {x : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, localOscillation (Metric.ball x r) (coeΘ f) (coeΘ g) ≤ ENNReal.ofReal (dist_{x, r} f g)) → (∀ {x₁ x₂ : X} {r₁ r₂ : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, Metric.ball x₁ r₁ ⊆ Metric.ball x₂ r₂ → dist_{x₁, r₁} f g ≤ dist_{x₂, r₂} f g) → (∀ {x₁ x₂ : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, dist x₁ x₂ < (2 : ℝ) * r → dist_{x₂, (2 : ℝ) * r} f g ≤ ↑A * dist_{x₁, r} f g) → (∀ {x₁ x₂ : X} {r : ℝ} {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, Metric.ball x₁ r ⊆ Metric.ball x₂ (↑A * r) → (2 : ℝ) * dist_{x₁, r} f g ≤ dist_{x₂, ↑A * r} f g) → (∀ {x : X} {r : ℝ}, AllBallsCoverBalls.{u} (WithFunctionDistance x r) (2 : ℝ) A) → CompatibleFunctions 𝕜 X A`

#### `FunctionDistances` (structure or class)
Lean: `(𝕜 : outParam (Type u_1)) → (X : Type u) → [NormedField 𝕜] → [TopologicalSpace X] → Type (max (u + 1) u_1)`
Docstring: A class stating that continuous functions have distances associated to every ball. We use a separate type to conveniently index these functions.
Constructor (every field with its type): `{𝕜 : outParam (Type u_1)} → {X : Type u} → [inst : NormedField 𝕜] → [inst_1 : TopologicalSpace X] → (Θ : Type u) → (coeΘ : Θ → C(X, 𝕜)) → (∀ {f g : Θ}, (∀ (x : X), Eq.{u_1 + 1} (α := 𝕜) ((coeΘ f) x : 𝕜) ((coeΘ g) x : 𝕜)) → f = g) → (X → ℝ → PseudoMetricSpace Θ) → FunctionDistances 𝕜 X`

#### `KernelProofData` (structure or class)
Lean: `{X : Type u_1} → outParam ℕ → outParam (X → X → ℂ) → [PseudoMetricSpace X] → Type (u_1 + 1)`
Docstring: Data common through most of chapters 2 through 7. These contain the minimal axioms for `kernel-summand`'s proof. This is used in Chapter 3 when we don't have all other fields from `ProofData`.
Constructor (every field with its type): `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → [inst : PseudoMetricSpace X] → (d : DoublingMeasure X ↑(defaultA a)) → (4 : ℕ) ≤ a → CompatibleFunctions ℝ X (defaultA a) → IsOneSidedKernel a K → KernelProofData a K`

#### `MeasureTheory.DoublingMeasure` (structure or class)
Lean: `(X : Type u_3) → outParam NNReal → [PseudoMetricSpace X] → Type u_3`
Docstring: A metric space with a measure with some nice properties, including a doubling condition. This is called a "doubling metric measure space" in the blueprint. `A` will usually be `2 ^ a`.
Constructor (every field with its type): `{X : Type u_3} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [toCompleteSpace : CompleteSpace X] → [toLocallyCompactSpace : LocallyCompactSpace X] → [toMeasureSpace : MeasureSpace X] → [toBorelSpace : BorelSpace X] → [toIsLocallyFiniteMeasure : IsLocallyFiniteMeasure.{u_3} (α := X) (m0 := MeasureSpace.toMeasurableSpace) volume] → [toIsDoubling : Measure.IsDoubling.{u_3} (X := X) volume A] → [toNeZero : NeZero.{u_3} (R := Measure X) volume] → DoublingMeasure X A`

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

#### `GridStructure` (structure or class)
Lean: `(X : Type u_2) → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [DoublingMeasure X A] → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (max (u + 1) u_2)`
Docstring: A grid structure on `X`. We prefer `coeGrid : Grid → Set X` over `Grid : Set (Set X)` Note: the `s` in this paper is `-s` of Christ's paper.
Constructor (every field with its type): `{X : Type u_2} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → (Grid : Type u) → Fintype Grid → (coeGrid : Grid → Set X) → (s : Grid → ℤ) → (c : Grid → X) → (Function.Injective.{u + 1, max 1 (u_2 + 1)} (β := Set X × ℤ) fun (i : Grid) => (coeGrid i, s i)) → Set.range s ⊆ Set.Icc (-↑S) ↑S → (topCube : Grid) → s topCube = ↑S → c topCube = o → (∀ {i : Grid}, coeGrid i ⊆ coeGrid topCube) → (∀ {i : Grid}, ∀ k ∈ Set.Ico (-↑S) (s i), coeGrid i ⊆ ⋃ j ∈ s ⁻¹' {k}, coeGrid j) → (∀ {i j : Grid}, s i ≤ s j → coeGrid i ⊆ coeGrid j ∨ Disjoint (coeGrid i) (coeGrid j)) → (∀ {i : Grid}, Metric.ball (c i) (HPow.hPow (α := ℝ) (↑D) (s i) / (4 : ℝ)) ⊆ coeGrid i) → (∀ {i : Grid}, coeGrid i ⊆ Metric.ball (c i) ((4 : ℝ) * HPow.hPow (α := ℝ) (↑D) (s i))) → (∀ {i : Grid} {t : NNReal}, HPow.hPow (α := NNReal) (↑D) (-↑S - s i) ≤ t → Measure.real.{u_2} (α := X) (m := MeasureSpace.toMeasurableSpace) volume {x : X | x ∈ coeGrid i ∧ Metric.infEDist x (coeGrid i)ᶜ ≤ ↑t * HPow.hPow (α := ENNReal) (↑D) (s i)} ≤ (2 : ℝ) * ↑t ^ κ * Measure.real (m := MeasureSpace.toMeasurableSpace) volume (coeGrid i)) → (∀ {i : Grid}, MeasurableSet (coeGrid i)) → GridStructure.{u, u_2} X D κ S o`

#### `GridStructure.Grid` (def)
Lean: `(X : Type u_2) → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → Type u`
Docstring: indexing set for a grid structure
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.1`

#### `PreTileStructure` (structure or class)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : outParam NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → [inst_3 : FunctionDistances 𝕜 X] → outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)) → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (max (u + 1) (u_2 + 1))`
Constructor (every field with its type): `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : outParam NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → [inst_3 : FunctionDistances 𝕜 X] → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [toGridStructure : GridStructure.{u_2, u} X D κ S o] → (𝔓 : Type u) → Fintype 𝔓 → (𝓘 : 𝔓 → @GridStructure.Grid X _ inst_1 inst_2 _ _ _ _ _) → Function.Surjective 𝓘 → (𝒬 : 𝔓 → @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) → Set.range 𝒬 ⊆ Set.range (ι := X) ⇑Q → PreTileStructure.{u, u_1, u_2} Q D κ S o`

#### `PreTileStructure.𝓘` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X → @GridStructure.Grid X _ inst_1 inst_2 _ _ _ _ _`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.4`

#### `PreTileStructure.𝔓` (def)
Lean: `(𝕜 : Type u_1) → {inst : RCLike 𝕜} → (X : Type u) → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Type u`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.2`

#### `TileStructure.Ω` (def)
Lean: `{X : Type u} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {inst_2 : FunctionDistances ℝ X} → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : TileStructure Q D κ S o] → PreTileStructure.𝔓 ℝ X → Set (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _)`
Definition: `fun (X : Type u) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {inst_2 : FunctionDistances ℝ X} {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : TileStructure Q D κ S o] => self.2`

#### `FunctionDistances.coeΘ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → @Θ _ X inst inst_1 _ → C(X, 𝕜)`
Docstring: The coercion map from `Θ` to `C(X, 𝕜)`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.2`

#### `carlesonOn` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
Docstring: The operator `T_𝔭` defined in Proposition 2.0.2.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [PseudoMetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) => (E (F := F) (G := G) p).indicator fun (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => Complex.exp (Complex.I * (↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y) - ↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) x))) * Ks (𝔰 p) x y * f y`

#### `PreTileStructure.fintype_𝔓` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X)`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.3`

#### `TileStructure.Row.toForest` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Row X (F := F) (G := G) n → Forest X (F := F) (G := G) n`
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] (a : ℕ) (q : ℝ) (K : X → X → ℂ) (σ₁ σ₂ : X → ℤ) (F G : Set X) [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (n : ℕ) (self : Row X (F := F) (G := G) n) => self.1`

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

#### `GridStructure.s` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → ℤ`
Docstring: scale functions
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.4`

#### `toTileLike` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → TileLike X (F := F) (G := G)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) => (𝓘 p, Ω p)`

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

#### `TileStructure.Row.instMembership𝔓Real` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Membership (𝔓 X) (Row X (F := F) (G := G) n)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} => { mem := fun (t : Row X (F := F) (G := G) n) (x : 𝔓 X) => x ∈ t.toForest (F := F) (G := G).𝔘 (F := F) (G := G) }`

#### `adjointCarleson` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
Docstring: The definition of `Tₚ*g(x)`, defined above Lemma 7.4.1
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume (E (F := F) (G := G) p)) fun (y : X) => HMul.hMul (α := ℂ) ((starRingEnd ℂ) (Ks (𝔰 p) y x) : ℂ) (Complex.exp (Complex.I * (↑(((Q (F := F) (G := G)) y : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y) - ↑(((Q (F := F) (G := G)) y : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) x)))) * f y`

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

#### `AllBallsCoverBalls` (def)
Lean: `(X : Type u_2) → [PseudoMetricSpace X] → ℝ → ℕ → Prop`
Docstring: For all `r`, balls of radius `r` in `X` are covered by `n` balls of radius `a * r`
Definition: `fun (X : Type u_2) [PseudoMetricSpace X] (a : ℝ) (n : ℕ) => ∀ (r : ℝ), BallsCoverBalls X (a * r) r n`

#### `localOscillation` (def)
Lean: `{𝕜 : Type u_3} → {X : Type u_4} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → Set X → C(X, 𝕜) → C(X, 𝕜) → ENNReal`
Docstring: The local oscillation of two functions w.r.t. a set `E`. This is `d_E` in the blueprint.
Definition: `fun {𝕜 : Type u_3} {X : Type u_4} [RCLike 𝕜] [PseudoMetricSpace X] (E : Set X) (f g : C(X, 𝕜)) => ⨆ z ∈ E ×ˢ E, ENNReal.ofReal ‖HAdd.hAdd (β := 𝕜) (HSub.hSub (β := 𝕜) (HSub.hSub (α := 𝕜) (β := 𝕜) (f z.1 : 𝕜) (g z.1 : 𝕜)) (f z.2 : 𝕜)) (g z.2 : 𝕜)‖`

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

#### `GridStructure.c` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → X`
Docstring: Center functions
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.5`

#### `GridStructure.topCube` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _`
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.8`

#### `E` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → Set X`
Docstring: The set `E` defined in Proposition 2.0.2.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) => {x : X | x ∈ 𝓘 p ∧ Membership.mem (α := @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) (Ω p) ((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) ∧ 𝔰 p ∈ Set.Icc (σ₁ x) (σ₂ x)}`

#### `Ks` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {K : X → X → ℂ} → [inst : PseudoMetricSpace X] → [KernelProofData a K] → ℤ → X → X → ℂ`
Docstring: K_s in the blueprint
Definition: `fun {X : Type u_1} {a : ℕ} {K : X → X → ℂ} [PseudoMetricSpace X] [KernelProofData a K] (s : ℤ) (x y : X) => K x y * ↑(ψ (defaultD a) (HPow.hPow (α := ℝ) (↑(defaultD a)) (-s) * dist x y))`

#### `TileLike.toSet` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → TileLike X (F := F) (G := G) → Set X`
Docstring: From a TileLike, we can construct a set. This is used in the definitions `E₁` and `E₂`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (t : TileLike X (F := F) (G := G)) => ↑(t.fst (F := F) (G := G)) ∩ G ∩ ⇑(Q (F := F) (G := G)) ⁻¹' t.snd (F := F) (G := G)`

## Translations

### `forest_operator_le_volume`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔉 : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hA : MeasurableSet A) (sA : A ⊆ G) : ∫⁻ (x : X) in A, ‖∑ u with u ∈ 𝔉, carlesonSum ((fun x => 𝔉.𝔗 x) u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * dens₂ (⋃ u ∈ 𝔉, (fun x => 𝔉.𝔗 x) u) ^ (q⁻¹ - 2⁻¹) * volume F ^ (1 / 2) * volume A ^ (1 / 2)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (𝔉 : Forest X (F := F) (G := G) n) {f : X → ℂ} {A : Set X}, Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → MeasurableSet A → A ⊆ G → ∫⁻ (x : X) in A, enorm (E := ℂ) (∑ u : 𝔓 X with u ∈ 𝔉, carlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => 𝔉.𝔗 (F := F) (G := G) x) u) f x) ≤ ↑(C2_0_4 a q n) * dens₂ (F := F) (G := G) (⋃ u ∈ 𝔉, (fun (x : 𝔓 X) => 𝔉.𝔗 (F := F) (G := G) x) u) ^ (q⁻¹ - (2 : ℝ)⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (1 / 2 : ℝ) * HPow.hPow (α := ENNReal) ((volume : Measure X) A : ENNReal) (1 / 2 : ℝ)`
Docstring: Version of the forest operator theorem, but controlling the integral of the norm instead of the integral of the function multiplied by another function, and with the upper bound in terms of `volume F` and `volume G`.
English: Let $X$ be a metric space. Let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common to chapters 2–7 of the blueprint). Write $\mu$ for the measure `volume` on $X$ provided through this instance, and $Q$ for the simple function from $X$ to the function family $\Theta(X)$ provided by the instance (`ProofData.Q`). Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (here and below $𝕔$ is the project's natural-number constant `𝕔`, whose docstring fixes it equal to $100$), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` and $o = $ `cancelPt X`; write $\mathfrak{P}$ for its type of tiles (`𝔓 X`) and $\mathcal{I}(p)$ for the grid cube `𝓘 p` of a tile $p$. For a set $\mathfrak{C} \subseteq \mathfrak{P}$ and $h : X \to \mathbb{C}$, $\mathrm{carlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p h(x)$, where $T_p$ is `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2), and $\mathrm{adjointCarlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p^* h(x)$, where $T_p^*$ is `adjointCarleson p`. $\mathrm{dens}_2$ denotes the project density `dens₂` of a set of tiles (a value in $[0,\infty]$). All $L^2$ norms $\|\cdot\|_{L^2}$ are taken with respect to $\mu$ (as values in $[0,\infty]$) and $|\cdot|$ is the modulus of a complex number. Let $n \in \mathbb{N}$ and let $\mathfrak{F}$ be an $n$-forest (a term of the project structure `Forest X n`); $u \in \mathfrak{F}$ means that the tile $u \in \mathfrak{P}$ belongs to the set `𝔉.𝔘` of the forest, and for $u \in \mathfrak{P}$, $\mathfrak{T}(u) \subseteq \mathfrak{P}$ denotes the set `𝔉.𝔗 u`. Let $f : X \to \mathbb{C}$ be measurable with $|f(x)| \le \mathbf{1}_F(x)$ for all $x \in X$. Let $A \subseteq X$ be a measurable set with $A \subseteq G$. Then $$\int_A \Big|\sum_{u \in \mathfrak{F}} \mathrm{carlesonSum}(\mathfrak{T}(u), f)(x)\Big|\,d\mu(x) \le C_{2.0.4}(a,q,n)\, \mathrm{dens}_2\Big(\bigcup_{u \in \mathfrak{F}} \mathfrak{T}(u)\Big)^{1/q - 1/2}\, \mu(F)^{1/2}\, \mu(A)^{1/2},$$ where $C_{2.0.4}(a,q,n)$ denotes the project constant `C2_0_4 a q n` (a nonnegative real). 

### `TileStructure.Forest.forest_operator_f`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (t : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * ∑ u with u ∈ t, carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.C2_0_4_aux a) * dens₂ (⋃ u ∈ t, (fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {f g : X → ℂ} (t : Forest X (F := F) (G := G) n), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable g → (∀ (x : X), ‖g x‖ ≤ G.indicator (1 : X → ℝ) x) → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (α := ℂ) (β := ℂ) ((starRingEnd ℂ) (g x) : ℂ) (∑ u : 𝔓 X with u ∈ t, carlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) f x : ℂ)) ≤ ↑(Forest.C2_0_4_aux a) * dens₂ (F := F) (G := G) (⋃ u ∈ t, (fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) ^ (2 : ℝ)⁻¹ * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (2 : ENNReal) volume * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace g (2 : ENNReal) volume`
Docstring: The `f` side of Proposition 2.0.4.
English: (The $f$ side of Proposition 2.0.4.) Let $X$ be a metric space. Let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common to chapters 2–7 of the blueprint). Write $\mu$ for the measure `volume` on $X$ provided through this instance, and $Q$ for the simple function from $X$ to the function family $\Theta(X)$ provided by the instance (`ProofData.Q`). Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (here and below $𝕔$ is the project's natural-number constant `𝕔`, whose docstring fixes it equal to $100$), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` and $o = $ `cancelPt X`; write $\mathfrak{P}$ for its type of tiles (`𝔓 X`) and $\mathcal{I}(p)$ for the grid cube `𝓘 p` of a tile $p$. For a set $\mathfrak{C} \subseteq \mathfrak{P}$ and $h : X \to \mathbb{C}$, $\mathrm{carlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p h(x)$, where $T_p$ is `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2), and $\mathrm{adjointCarlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p^* h(x)$, where $T_p^*$ is `adjointCarleson p`. $\mathrm{dens}_2$ denotes the project density `dens₂` of a set of tiles (a value in $[0,\infty]$). All $L^2$ norms $\|\cdot\|_{L^2}$ are taken with respect to $\mu$ (as values in $[0,\infty]$) and $|\cdot|$ is the modulus of a complex number. Let $n \in \mathbb{N}$ and let $t$ be an $n$-forest (a term of the project structure `Forest X n`); $u \in t$ means that the tile $u \in \mathfrak{P}$ belongs to the set `t.𝔘` of the forest, and for $u \in \mathfrak{P}$, $\mathfrak{T}(u) \subseteq \mathfrak{P}$ denotes the set `t.𝔗 u`. Let $f : X \to \mathbb{C}$ be measurable with $|f(x)| \le \mathbf{1}_F(x)$ for all $x \in X$. Let $g : X \to \mathbb{C}$ be measurable with $|g(x)| \le \mathbf{1}_G(x)$ for all $x \in X$. Then $$\Big|\int_X \overline{g(x)} \sum_{u \in t} \mathrm{carlesonSum}(\mathfrak{T}(u), f)(x)\,d\mu(x)\Big| \le C^{\mathrm{aux}}(a)\, \mathrm{dens}_2\Big(\bigcup_{u \in t}\mathfrak{T}(u)\Big)^{1/2}\, \|f\|_{L^2}\, \|g\|_{L^2},$$ where $C^{\mathrm{aux}}(a) = 2^{(2𝕔 + 8 + \lfloor 𝕔/2 \rfloor + \lfloor 𝕔/4 \rfloor) a^3}$ is the constant `Forest.C2_0_4_aux a`.

### `TileStructure.Forest.rowDecomp_𝔘`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (t : Forest X n) (j : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → ℕ → Set (𝔓 X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (t : Forest X (F := F) (G := G) n) => WellFounded.Nat.fix (motive := fun (j : ℕ) => Set (𝔓 X)) (fun (x : ℕ) => x) fun (j : ℕ) (a_1 : (y : ℕ) → InvImage (fun (x1 x2 : ℕ) => x1 < x2) (fun (x : ℕ) => x) y j → Set (𝔓 X)) => ⋯.choose (p := Maximal fun (x : Set (𝔓 X)) => x ∈ Forest.rowDecomp_zornset (F := F) (G := G) (t.𝔘 (F := F) (G := G) \ ⋃ (i : ℕ), ⋃ (h : i < j), a_1 i ⋯))`
English: Under the standing assumptions (a metric space $X$ with the `ProofData` bundle for parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K$, integer-valued functions $\sigma_1,\sigma_2$ and sets $F, G \subseteq X$, and the tile structure on $X$ with the default parameters), for a natural number $n$, an $n$-forest $t$ on $X$ and $j \in \mathbb{N}$, $\mathrm{rowDecomp}_{\mathfrak{U}}(t, j)$ is a set of tiles in $\mathfrak{P}(X)$.

### `TileStructure.Forest.rowDecomp`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (t : Forest X n) (j : ℕ) : Row X n`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → ℕ → Row X (F := F) (G := G) n`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (t : Forest X (F := F) (G := G) n) (j : ℕ) => Row.mk (F := F) (G := G) (Forest.mk (F := F) (G := G) (t.rowDecomp_𝔘 (F := F) (G := G) j) (fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) ⋯ ⋯ ⋯ ⋯ ⋯ ⋯ ⋯ ⋯) ⋯`
Docstring: The row-decomposition of a tree, defined in the proof of Lemma 7.7.1. The indexing is off-by-one compared to the blueprint.
English: Under the standing assumptions (a metric space $X$ with the `ProofData` bundle for parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K$, integer-valued functions $\sigma_1,\sigma_2$ and sets $F, G \subseteq X$, and the tile structure on $X$ with the default parameters), for a natural number $n$, an $n$-forest $t$ on $X$ and $j \in \mathbb{N}$, $\mathrm{rowDecomp}(t, j)$ is an $n$-row on $X$ (an element of `Row X n`). According to its docstring, it is the row-decomposition of a tree defined in the proof of Lemma 7.7.1, with indexing off by one compared to the blueprint.

### `TileStructure.Forest.indicator_row_bound`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hg : BoundedCompactSupport g volume) (h2g : Function.support g ⊆ G) : eLpNorm (F.indicator (t.adjointCarlesonRowSum j g)) 2 volume ≤ ↑(Forest.C7_7_2_2 a n) * dens₂ (⋃ u ∈ t, (fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n j : ℕ} {t : Forest X (F := F) (G := G) n} {g : X → ℂ}, BoundedCompactSupport g volume → Function.support g ⊆ G → @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace (F.indicator (t.adjointCarlesonRowSum (F := F) (G := G) j g)) (2 : ENNReal) volume ≤ ↑(Forest.C7_7_2_2 a n) * dens₂ (F := F) (G := G) (⋃ u ∈ t, (fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) ^ (2 : ℝ)⁻¹ * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace g (2 : ENNReal) volume`
English: Let $X$ be a metric space. Let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common to chapters 2–7 of the blueprint). Write $\mu$ for the measure `volume` on $X$ provided through this instance, and $Q$ for the simple function from $X$ to the function family $\Theta(X)$ provided by the instance (`ProofData.Q`). Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (here and below $𝕔$ is the project's natural-number constant `𝕔`, whose docstring fixes it equal to $100$), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` and $o = $ `cancelPt X`; write $\mathfrak{P}$ for its type of tiles (`𝔓 X`) and $\mathcal{I}(p)$ for the grid cube `𝓘 p` of a tile $p$. For a set $\mathfrak{C} \subseteq \mathfrak{P}$ and $h : X \to \mathbb{C}$, $\mathrm{carlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p h(x)$, where $T_p$ is `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2), and $\mathrm{adjointCarlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p^* h(x)$, where $T_p^*$ is `adjointCarleson p`. $\mathrm{dens}_2$ denotes the project density `dens₂` of a set of tiles (a value in $[0,\infty]$). All $L^2$ norms $\|\cdot\|_{L^2}$ are taken with respect to $\mu$ (as values in $[0,\infty]$) and $|\cdot|$ is the modulus of a complex number. Let $n \in \mathbb{N}$ and let $t$ be an $n$-forest (a term of the project structure `Forest X n`); $u \in t$ means that the tile $u \in \mathfrak{P}$ belongs to the set `t.𝔘` of the forest, and for $u \in \mathfrak{P}$, $\mathfrak{T}(u) \subseteq \mathfrak{P}$ denotes the set `t.𝔗 u`. Let $j \in \mathbb{N}$ and let $g : X \to \mathbb{C}$ be bounded, measurable and compactly supported (`BoundedCompactSupport g μ`) with $\operatorname{supp} g \subseteq G$. Let $T^*_{t,j} g$ denote `t.adjointCarlesonRowSum j g`, i.e. $T^*_{t,j} g(x) = \sum_{u \in \mathrm{row}_j} \mathrm{adjointCarlesonSum}(\mathfrak{T}(u), g)(x)$, where $\mathrm{row}_j$ is the $j$-th row `t.rowDecomp j` of the forest. Then $$\big\|\mathbf{1}_F \cdot T^*_{t,j} g\big\|_{L^2} \le C_{7.7.2.2}(a,n)\, \mathrm{dens}_2\Big(\bigcup_{u \in t}\mathfrak{T}(u)\Big)^{1/2}\, \|g\|_{L^2},$$ where $C_{7.7.2.2}(a,n)$ is the project constant `Forest.C7_7_2_2 a n` (a nonnegative real).

### `TileStructure.Forest.forest_operator_f_inner`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : eLpNorm (G.indicator (t.carlesonRowSum j f)) 2 volume ≤ ↑(Forest.C7_7_2_2 a n) * dens₂ (⋃ u ∈ t, (fun x => t.𝔗 x) u) ^ 2⁻¹ * eLpNorm f 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n j : ℕ} {t : Forest X (F := F) (G := G) n} {f : X → ℂ}, Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace (G.indicator (t.carlesonRowSum (F := F) (G := G) j f)) (2 : ENNReal) volume ≤ ↑(Forest.C7_7_2_2 a n) * dens₂ (F := F) (G := G) (⋃ u ∈ t, (fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) ^ (2 : ℝ)⁻¹ * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (2 : ENNReal) volume`
Docstring: https://leanprover.zulipchat.com/#narrow/channel/442935-Carleson/topic/Problems.20in.20the.20forest.20operator.20proposition/near/522771057
English: Let $X$ be a metric space. Let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common to chapters 2–7 of the blueprint). Write $\mu$ for the measure `volume` on $X$ provided through this instance, and $Q$ for the simple function from $X$ to the function family $\Theta(X)$ provided by the instance (`ProofData.Q`). Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (here and below $𝕔$ is the project's natural-number constant `𝕔`, whose docstring fixes it equal to $100$), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` and $o = $ `cancelPt X`; write $\mathfrak{P}$ for its type of tiles (`𝔓 X`) and $\mathcal{I}(p)$ for the grid cube `𝓘 p` of a tile $p$. For a set $\mathfrak{C} \subseteq \mathfrak{P}$ and $h : X \to \mathbb{C}$, $\mathrm{carlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p h(x)$, where $T_p$ is `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2), and $\mathrm{adjointCarlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p^* h(x)$, where $T_p^*$ is `adjointCarleson p`. $\mathrm{dens}_2$ denotes the project density `dens₂` of a set of tiles (a value in $[0,\infty]$). All $L^2$ norms $\|\cdot\|_{L^2}$ are taken with respect to $\mu$ (as values in $[0,\infty]$) and $|\cdot|$ is the modulus of a complex number. Let $n \in \mathbb{N}$ and let $t$ be an $n$-forest (a term of the project structure `Forest X n`); $u \in t$ means that the tile $u \in \mathfrak{P}$ belongs to the set `t.𝔘` of the forest, and for $u \in \mathfrak{P}$, $\mathfrak{T}(u) \subseteq \mathfrak{P}$ denotes the set `t.𝔗 u`. Let $j \in \mathbb{N}$. Let $f : X \to \mathbb{C}$ be measurable with $|f(x)| \le \mathbf{1}_F(x)$ for all $x \in X$. Let $T_{t,j} f$ denote `t.carlesonRowSum j f`, i.e. $T_{t,j} f(x) = \sum_{u \in \mathrm{row}_j} \mathrm{carlesonSum}(\mathfrak{T}(u), f)(x)$, where $\mathrm{row}_j$ is the $j$-th row `t.rowDecomp j` of the forest. Then $$\big\|\mathbf{1}_G \cdot T_{t,j} f\big\|_{L^2} \le C_{7.7.2.2}(a,n)\, \mathrm{dens}_2\Big(\bigcup_{u \in t}\mathfrak{T}(u)\Big)^{1/2}\, \|f\|_{L^2},$$ where $C_{7.7.2.2}(a,n)$ is the project constant `Forest.C7_7_2_2 a n` (a nonnegative real).

### `TileStructure.Forest.forest_operator_g_main`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : eLpNorm (fun x => ∑ u with u ∈ t, adjointCarlesonSum ((fun x => t.𝔗 x) u) g x) 2 volume ^ 2 ≤ (↑(Forest.G2_0_4 a n) * eLpNorm g 2 volume) ^ 2`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {g : X → ℂ}, Measurable g → (∀ (x : X), ‖g x‖ ≤ G.indicator (1 : X → ℝ) x) → @eLpNorm _ ℂ _ MeasureSpace.toMeasurableSpace (fun (x : X) => ∑ u : 𝔓 X with u ∈ t, adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) g x) (2 : ENNReal) volume ^ (2 : ℕ) ≤ (↑(Forest.G2_0_4 a n) * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace g (2 : ENNReal) volume) ^ (2 : ℕ)`
English: Let $X$ be a metric space. Let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common to chapters 2–7 of the blueprint). Write $\mu$ for the measure `volume` on $X$ provided through this instance, and $Q$ for the simple function from $X$ to the function family $\Theta(X)$ provided by the instance (`ProofData.Q`). Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (here and below $𝕔$ is the project's natural-number constant `𝕔`, whose docstring fixes it equal to $100$), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` and $o = $ `cancelPt X`; write $\mathfrak{P}$ for its type of tiles (`𝔓 X`) and $\mathcal{I}(p)$ for the grid cube `𝓘 p` of a tile $p$. For a set $\mathfrak{C} \subseteq \mathfrak{P}$ and $h : X \to \mathbb{C}$, $\mathrm{carlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p h(x)$, where $T_p$ is `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2), and $\mathrm{adjointCarlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p^* h(x)$, where $T_p^*$ is `adjointCarleson p`. $\mathrm{dens}_2$ denotes the project density `dens₂` of a set of tiles (a value in $[0,\infty]$). All $L^2$ norms $\|\cdot\|_{L^2}$ are taken with respect to $\mu$ (as values in $[0,\infty]$) and $|\cdot|$ is the modulus of a complex number. Let $n \in \mathbb{N}$ and let $t$ be an $n$-forest (a term of the project structure `Forest X n`); $u \in t$ means that the tile $u \in \mathfrak{P}$ belongs to the set `t.𝔘` of the forest, and for $u \in \mathfrak{P}$, $\mathfrak{T}(u) \subseteq \mathfrak{P}$ denotes the set `t.𝔗 u`. Let $g : X \to \mathbb{C}$ be measurable with $|g(x)| \le \mathbf{1}_G(x)$ for all $x \in X$. Then $$\Big\|x \mapsto \sum_{u \in t} \mathrm{adjointCarlesonSum}(\mathfrak{T}(u), g)(x)\Big\|_{L^2}^2 \le \big(B(a,n)\, \|g\|_{L^2}\big)^2,$$ where $B(a,n) = 2^{(3𝕔 + 15 + 5\lfloor 𝕔/4 \rfloor) a^3}\, 2^{-n/2}$ is the constant `Forest.G2_0_4 a n`.

### `TileStructure.Forest.correlation_separated_trees_of_subset`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (h2u : 𝓘 u₁ ≤ 𝓘 u₂) (hg₁ : BoundedCompactSupport g₁ volume) (hg₂ : BoundedCompactSupport g₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁) g₁ x * (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u₂) g₂ x)‖ₑ ≤ ↑(Forest.C7_4_4 a n) * eLpNorm (fun x => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator u₁ g₁) x) 2 volume * eLpNorm (fun x => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator u₂ g₂) x) 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u₁ u₂ : 𝔓 X} {g₁ g₂ : X → ℂ}, u₁ ∈ t → u₂ ∈ t → u₁ ≠ u₂ → 𝓘 u₁ ≤ 𝓘 u₂ → BoundedCompactSupport g₁ volume → BoundedCompactSupport g₂ volume → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (β := ℂ) (adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₁) g₁ x) ((starRingEnd ℂ) (adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₂) g₂ x) : ℂ)) ≤ ↑(Forest.C7_4_4 a n) * @eLpNorm _ ENNReal _ MeasureSpace.toMeasurableSpace (fun (x : X) => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator (F := F) (G := G) u₁ g₁) x) (2 : ENNReal) volume * @eLpNorm _ ENNReal _ MeasureSpace.toMeasurableSpace (fun (x : X) => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator (F := F) (G := G) u₂ g₂) x) (2 : ENNReal) volume`
English: Let $X$ be a metric space. Let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common to chapters 2–7 of the blueprint). Write $\mu$ for the measure `volume` on $X$ provided through this instance, and $Q$ for the simple function from $X$ to the function family $\Theta(X)$ provided by the instance (`ProofData.Q`). Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (here and below $𝕔$ is the project's natural-number constant `𝕔`, whose docstring fixes it equal to $100$), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` and $o = $ `cancelPt X`; write $\mathfrak{P}$ for its type of tiles (`𝔓 X`) and $\mathcal{I}(p)$ for the grid cube `𝓘 p` of a tile $p$. For a set $\mathfrak{C} \subseteq \mathfrak{P}$ and $h : X \to \mathbb{C}$, $\mathrm{carlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p h(x)$, where $T_p$ is `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2), and $\mathrm{adjointCarlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p^* h(x)$, where $T_p^*$ is `adjointCarleson p`. $\mathrm{dens}_2$ denotes the project density `dens₂` of a set of tiles (a value in $[0,\infty]$). All $L^2$ norms $\|\cdot\|_{L^2}$ are taken with respect to $\mu$ (as values in $[0,\infty]$) and $|\cdot|$ is the modulus of a complex number. Let $n \in \mathbb{N}$ and let $t$ be an $n$-forest (a term of the project structure `Forest X n`); $u \in t$ means that the tile $u \in \mathfrak{P}$ belongs to the set `t.𝔘` of the forest, and for $u \in \mathfrak{P}$, $\mathfrak{T}(u) \subseteq \mathfrak{P}$ denotes the set `t.𝔗 u`. Let $u_1, u_2 \in \mathfrak{P}$ be tiles with $u_1 \in t$, $u_2 \in t$, $u_1 \ne u_2$ and $\mathcal{I}(u_1) \le \mathcal{I}(u_2)$ in the partial order on grid cubes. Let $g_1, g_2 : X \to \mathbb{C}$ be bounded, measurable and compactly supported (`BoundedCompactSupport` with respect to $\mu$). For $u \in \mathfrak{P}$ and $h : X \to \mathbb{C}$, let $S_u h : X \to [0,\infty]$ be `t.adjointBoundaryOperator u h`, i.e. $S_u h(x) = |\mathrm{adjointCarlesonSum}(\mathfrak{T}(u), h)(x)| + M h(x) + |h(x)|$, where $M$ is the uncentered maximal function `maximalFunction μ 𝓑 c𝓑 r𝓑 1` over the project family of balls $\mathcal{B}$. Then $$\Big|\int_X \mathrm{adjointCarlesonSum}(\mathfrak{T}(u_1), g_1)(x)\, \overline{\mathrm{adjointCarlesonSum}(\mathfrak{T}(u_2), g_2)(x)}\,d\mu(x)\Big| \le C_{7.4.4}(a,n)\, \big\|\mathbf{1}_{\mathcal{I}(u_1)\cap\mathcal{I}(u_2)} \cdot S_{u_1} g_1\big\|_{L^2}\, \big\|\mathbf{1}_{\mathcal{I}(u_1)\cap\mathcal{I}(u_2)} \cdot S_{u_2} g_2\big\|_{L^2},$$ where $C_{7.4.4}(a,n)$ is the project constant `Forest.C7_4_4 a n` (a nonnegative real).

### `TileStructure.Forest.correlation_separated_trees`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu₁ : u₁ ∈ t) (hu₂ : u₂ ∈ t) (hu : u₁ ≠ u₂) (hg₁ : BoundedCompactSupport g₁ volume) (hg₂ : BoundedCompactSupport g₂ volume) : ‖∫ (x : X), adjointCarlesonSum ((fun x => t.𝔗 x) u₁) g₁ x * (starRingEnd ℂ) (adjointCarlesonSum ((fun x => t.𝔗 x) u₂) g₂ x)‖ₑ ≤ ↑(Forest.C7_4_4 a n) * eLpNorm (fun x => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator u₁ g₁) x) 2 volume * eLpNorm (fun x => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator u₂ g₂) x) 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {t : Forest X (F := F) (G := G) n} {u₁ u₂ : 𝔓 X} {g₁ g₂ : X → ℂ}, u₁ ∈ t → u₂ ∈ t → u₁ ≠ u₂ → BoundedCompactSupport g₁ volume → BoundedCompactSupport g₂ volume → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (β := ℂ) (adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₁) g₁ x) ((starRingEnd ℂ) (adjointCarlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u₂) g₂ x) : ℂ)) ≤ ↑(Forest.C7_4_4 a n) * @eLpNorm _ ENNReal _ MeasureSpace.toMeasurableSpace (fun (x : X) => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator (F := F) (G := G) u₁ g₁) x) (2 : ENNReal) volume * @eLpNorm _ ENNReal _ MeasureSpace.toMeasurableSpace (fun (x : X) => (↑(𝓘 u₁) ∩ ↑(𝓘 u₂)).indicator (t.adjointBoundaryOperator (F := F) (G := G) u₂ g₂) x) (2 : ENNReal) volume`
Docstring: Lemma 7.4.4
English: (Lemma 7.4.4.) Let $X$ be a metric space. Let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common to chapters 2–7 of the blueprint). Write $\mu$ for the measure `volume` on $X$ provided through this instance, and $Q$ for the simple function from $X$ to the function family $\Theta(X)$ provided by the instance (`ProofData.Q`). Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (here and below $𝕔$ is the project's natural-number constant `𝕔`, whose docstring fixes it equal to $100$), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` and $o = $ `cancelPt X`; write $\mathfrak{P}$ for its type of tiles (`𝔓 X`) and $\mathcal{I}(p)$ for the grid cube `𝓘 p` of a tile $p$. For a set $\mathfrak{C} \subseteq \mathfrak{P}$ and $h : X \to \mathbb{C}$, $\mathrm{carlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p h(x)$, where $T_p$ is `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2), and $\mathrm{adjointCarlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p^* h(x)$, where $T_p^*$ is `adjointCarleson p`. $\mathrm{dens}_2$ denotes the project density `dens₂` of a set of tiles (a value in $[0,\infty]$). All $L^2$ norms $\|\cdot\|_{L^2}$ are taken with respect to $\mu$ (as values in $[0,\infty]$) and $|\cdot|$ is the modulus of a complex number. Let $n \in \mathbb{N}$ and let $t$ be an $n$-forest (a term of the project structure `Forest X n`); $u \in t$ means that the tile $u \in \mathfrak{P}$ belongs to the set `t.𝔘` of the forest, and for $u \in \mathfrak{P}$, $\mathfrak{T}(u) \subseteq \mathfrak{P}$ denotes the set `t.𝔗 u`. Let $u_1, u_2 \in \mathfrak{P}$ be tiles with $u_1 \in t$, $u_2 \in t$ and $u_1 \ne u_2$. Let $g_1, g_2 : X \to \mathbb{C}$ be bounded, measurable and compactly supported (`BoundedCompactSupport` with respect to $\mu$). For $u \in \mathfrak{P}$ and $h : X \to \mathbb{C}$, let $S_u h : X \to [0,\infty]$ be `t.adjointBoundaryOperator u h`, i.e. $S_u h(x) = |\mathrm{adjointCarlesonSum}(\mathfrak{T}(u), h)(x)| + M h(x) + |h(x)|$, where $M$ is the uncentered maximal function `maximalFunction μ 𝓑 c𝓑 r𝓑 1` over the project family of balls $\mathcal{B}$. Then $$\Big|\int_X \mathrm{adjointCarlesonSum}(\mathfrak{T}(u_1), g_1)(x)\, \overline{\mathrm{adjointCarlesonSum}(\mathfrak{T}(u_2), g_2)(x)}\,d\mu(x)\Big| \le C_{7.4.4}(a,n)\, \big\|\mathbf{1}_{\mathcal{I}(u_1)\cap\mathcal{I}(u_2)} \cdot S_{u_1} g_1\big\|_{L^2}\, \big\|\mathbf{1}_{\mathcal{I}(u_1)\cap\mathcal{I}(u_2)} \cdot S_{u_2} g_2\big\|_{L^2},$$ where $C_{7.4.4}(a,n)$ is the project constant `Forest.C7_4_4 a n` (a nonnegative real).

### `TileStructure.Forest.row_correlation`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (lj : j < 2 ^ n) (lj' : j' < 2 ^ n) (hn : j ≠ j') (hf₁ : BoundedCompactSupport f₁ volume) (nf₁ : Function.support f₁ ⊆ G) (hf₂ : BoundedCompactSupport f₂ volume) (nf₂ : Function.support f₂ ⊆ G) : ‖∫ (x : X), t.adjointCarlesonRowSum j f₁ x * (starRingEnd ℂ) (t.adjointCarlesonRowSum j' f₂ x)‖ₑ ≤ ↑(Forest.C7_7_3 a n) * eLpNorm f₁ 2 volume * eLpNorm f₂ 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n j j' : ℕ} {t : Forest X (F := F) (G := G) n} {f₁ f₂ : X → ℂ}, j < (2 : ℕ) ^ n → j' < (2 : ℕ) ^ n → j ≠ j' → BoundedCompactSupport f₁ volume → Function.support f₁ ⊆ G → BoundedCompactSupport f₂ volume → Function.support f₂ ⊆ G → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (β := ℂ) (t.adjointCarlesonRowSum (F := F) (G := G) j f₁ x) ((starRingEnd ℂ) (t.adjointCarlesonRowSum (F := F) (G := G) j' f₂ x) : ℂ)) ≤ ↑(Forest.C7_7_3 a n) * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f₁ (2 : ENNReal) volume * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f₂ (2 : ENNReal) volume`
Docstring: Lemma 7.7.3.
English: (Lemma 7.7.3.) Let $X$ be a metric space. Let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common to chapters 2–7 of the blueprint). Write $\mu$ for the measure `volume` on $X$ provided through this instance, and $Q$ for the simple function from $X$ to the function family $\Theta(X)$ provided by the instance (`ProofData.Q`). Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (here and below $𝕔$ is the project's natural-number constant `𝕔`, whose docstring fixes it equal to $100$), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` and $o = $ `cancelPt X`; write $\mathfrak{P}$ for its type of tiles (`𝔓 X`) and $\mathcal{I}(p)$ for the grid cube `𝓘 p` of a tile $p$. For a set $\mathfrak{C} \subseteq \mathfrak{P}$ and $h : X \to \mathbb{C}$, $\mathrm{carlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p h(x)$, where $T_p$ is `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2), and $\mathrm{adjointCarlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p^* h(x)$, where $T_p^*$ is `adjointCarleson p`. $\mathrm{dens}_2$ denotes the project density `dens₂` of a set of tiles (a value in $[0,\infty]$). All $L^2$ norms $\|\cdot\|_{L^2}$ are taken with respect to $\mu$ (as values in $[0,\infty]$) and $|\cdot|$ is the modulus of a complex number. Let $n \in \mathbb{N}$ and let $t$ be an $n$-forest (a term of the project structure `Forest X n`); $u \in t$ means that the tile $u \in \mathfrak{P}$ belongs to the set `t.𝔘` of the forest, and for $u \in \mathfrak{P}$, $\mathfrak{T}(u) \subseteq \mathfrak{P}$ denotes the set `t.𝔗 u`. Let $j, j' \in \mathbb{N}$ with $j < 2^n$, $j' < 2^n$ and $j \ne j'$. Let $f_1, f_2 : X \to \mathbb{C}$ be bounded, measurable and compactly supported (`BoundedCompactSupport` with respect to $\mu$) with $\operatorname{supp} f_1 \subseteq G$ and $\operatorname{supp} f_2 \subseteq G$. For $i \in \mathbb{N}$ and $h : X \to \mathbb{C}$ let $T^*_{t,i} h$ denote `t.adjointCarlesonRowSum i h`, i.e. $T^*_{t,i} h(x) = \sum_{u \in \mathrm{row}_i} \mathrm{adjointCarlesonSum}(\mathfrak{T}(u), h)(x)$, where $\mathrm{row}_i$ is the $i$-th row `t.rowDecomp i` of the forest. Then $$\Big|\int_X T^*_{t,j} f_1(x)\, \overline{T^*_{t,j'} f_2(x)}\,d\mu(x)\Big| \le C_{7.7.3}(a,n)\, \|f_1\|_{L^2}\, \|f_2\|_{L^2},$$ where $C_{7.7.3}(a,n)$ is the project constant `Forest.C7_7_3 a n` (a nonnegative real).

### `TileStructure.Forest.forest_operator_g`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (t : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * ∑ u with u ∈ t, carlesonSum ((fun x => t.𝔗 x) u) f x‖ₑ ≤ ↑(Forest.G2_0_4 a n) * eLpNorm f 2 volume * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} {f g : X → ℂ} (t : Forest X (F := F) (G := G) n), Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable g → (∀ (x : X), ‖g x‖ ≤ G.indicator (1 : X → ℝ) x) → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (α := ℂ) (β := ℂ) ((starRingEnd ℂ) (g x) : ℂ) (∑ u : 𝔓 X with u ∈ t, carlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => t.𝔗 (F := F) (G := G) x) u) f x : ℂ)) ≤ ↑(Forest.G2_0_4 a n) * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (2 : ENNReal) volume * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace g (2 : ENNReal) volume`
Docstring: The `g` side of Proposition 2.0.4.
English: (The $g$ side of Proposition 2.0.4.) Let $X$ be a metric space. Let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common to chapters 2–7 of the blueprint). Write $\mu$ for the measure `volume` on $X$ provided through this instance, and $Q$ for the simple function from $X$ to the function family $\Theta(X)$ provided by the instance (`ProofData.Q`). Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (here and below $𝕔$ is the project's natural-number constant `𝕔`, whose docstring fixes it equal to $100$), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` and $o = $ `cancelPt X`; write $\mathfrak{P}$ for its type of tiles (`𝔓 X`) and $\mathcal{I}(p)$ for the grid cube `𝓘 p` of a tile $p$. For a set $\mathfrak{C} \subseteq \mathfrak{P}$ and $h : X \to \mathbb{C}$, $\mathrm{carlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p h(x)$, where $T_p$ is `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2), and $\mathrm{adjointCarlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p^* h(x)$, where $T_p^*$ is `adjointCarleson p`. $\mathrm{dens}_2$ denotes the project density `dens₂` of a set of tiles (a value in $[0,\infty]$). All $L^2$ norms $\|\cdot\|_{L^2}$ are taken with respect to $\mu$ (as values in $[0,\infty]$) and $|\cdot|$ is the modulus of a complex number. Let $n \in \mathbb{N}$ and let $t$ be an $n$-forest (a term of the project structure `Forest X n`); $u \in t$ means that the tile $u \in \mathfrak{P}$ belongs to the set `t.𝔘` of the forest, and for $u \in \mathfrak{P}$, $\mathfrak{T}(u) \subseteq \mathfrak{P}$ denotes the set `t.𝔗 u`. Let $f : X \to \mathbb{C}$ be measurable with $|f(x)| \le \mathbf{1}_F(x)$ for all $x \in X$. Let $g : X \to \mathbb{C}$ be measurable with $|g(x)| \le \mathbf{1}_G(x)$ for all $x \in X$. Then $$\Big|\int_X \overline{g(x)} \sum_{u \in t} \mathrm{carlesonSum}(\mathfrak{T}(u), f)(x)\,d\mu(x)\Big| \le B(a,n)\, \|f\|_{L^2}\, \|g\|_{L^2},$$ where $B(a,n) = 2^{(3𝕔 + 15 + 5\lfloor 𝕔/4 \rfloor) a^3}\, 2^{-n/2}$ is the constant `Forest.G2_0_4 a n`.

### `forest_operator`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔉 : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hg : Measurable g) (h2g : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (x : X), (starRingEnd ℂ) (g x) * ∑ u with u ∈ 𝔉, carlesonSum ((fun x => 𝔉.𝔗 x) u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * dens₂ (⋃ u ∈ 𝔉, (fun x => 𝔉.𝔗 x) u) ^ (q⁻¹ - 2⁻¹) * eLpNorm f 2 volume * eLpNorm g 2 volume`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (𝔉 : Forest X (F := F) (G := G) n) {f g : X → ℂ}, Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable g → (∀ (x : X), ‖g x‖ ≤ G.indicator (1 : X → ℝ) x) → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (x : X) => HMul.hMul (α := ℂ) (β := ℂ) ((starRingEnd ℂ) (g x) : ℂ) (∑ u : 𝔓 X with u ∈ 𝔉, carlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => 𝔉.𝔗 (F := F) (G := G) x) u) f x : ℂ)) ≤ ↑(C2_0_4 a q n) * dens₂ (F := F) (G := G) (⋃ u ∈ 𝔉, (fun (x : 𝔓 X) => 𝔉.𝔗 (F := F) (G := G) x) u) ^ (q⁻¹ - (2 : ℝ)⁻¹) * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (2 : ENNReal) volume * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace g (2 : ENNReal) volume`
English: Let $X$ be a metric space. Let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common to chapters 2–7 of the blueprint). Write $\mu$ for the measure `volume` on $X$ provided through this instance, and $Q$ for the simple function from $X$ to the function family $\Theta(X)$ provided by the instance (`ProofData.Q`). Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (here and below $𝕔$ is the project's natural-number constant `𝕔`, whose docstring fixes it equal to $100$), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` and $o = $ `cancelPt X`; write $\mathfrak{P}$ for its type of tiles (`𝔓 X`) and $\mathcal{I}(p)$ for the grid cube `𝓘 p` of a tile $p$. For a set $\mathfrak{C} \subseteq \mathfrak{P}$ and $h : X \to \mathbb{C}$, $\mathrm{carlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p h(x)$, where $T_p$ is `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2), and $\mathrm{adjointCarlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p^* h(x)$, where $T_p^*$ is `adjointCarleson p`. $\mathrm{dens}_2$ denotes the project density `dens₂` of a set of tiles (a value in $[0,\infty]$). All $L^2$ norms $\|\cdot\|_{L^2}$ are taken with respect to $\mu$ (as values in $[0,\infty]$) and $|\cdot|$ is the modulus of a complex number. Let $n \in \mathbb{N}$ and let $\mathfrak{F}$ be an $n$-forest (a term of the project structure `Forest X n`); $u \in \mathfrak{F}$ means that the tile $u \in \mathfrak{P}$ belongs to the set `𝔉.𝔘` of the forest, and for $u \in \mathfrak{P}$, $\mathfrak{T}(u) \subseteq \mathfrak{P}$ denotes the set `𝔉.𝔗 u`. Let $f : X \to \mathbb{C}$ be measurable with $|f(x)| \le \mathbf{1}_F(x)$ for all $x \in X$. Let $g : X \to \mathbb{C}$ be measurable with $|g(x)| \le \mathbf{1}_G(x)$ for all $x \in X$. Then $$\Big|\int_X \overline{g(x)} \sum_{u \in \mathfrak{F}} \mathrm{carlesonSum}(\mathfrak{T}(u), f)(x)\,d\mu(x)\Big| \le C_{2.0.4}(a,q,n)\, \mathrm{dens}_2\Big(\bigcup_{u \in \mathfrak{F}} \mathfrak{T}(u)\Big)^{1/q - 1/2}\, \|f\|_{L^2}\, \|g\|_{L^2},$$ where $C_{2.0.4}(a,q,n)$ denotes the project constant `C2_0_4 a q n` (a nonnegative real). 

### `forest_operator'`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔉 : Forest X n) (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (hA : MeasurableSet A) (sA : A ⊆ G) : ∫⁻ (x : X) in A, ‖∑ u with u ∈ 𝔉, carlesonSum ((fun x => 𝔉.𝔗 x) u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * dens₂ (⋃ u ∈ 𝔉, (fun x => 𝔉.𝔗 x) u) ^ (q⁻¹ - 2⁻¹) * eLpNorm f 2 volume * volume A ^ (1 / 2)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {n : ℕ} (𝔉 : Forest X (F := F) (G := G) n) {f : X → ℂ} {A : Set X}, Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → MeasurableSet A → A ⊆ G → ∫⁻ (x : X) in A, enorm (E := ℂ) (∑ u : 𝔓 X with u ∈ 𝔉, carlesonSum (F := F) (G := G) ((fun (x : 𝔓 X) => 𝔉.𝔗 (F := F) (G := G) x) u) f x) ≤ ↑(C2_0_4 a q n) * dens₂ (F := F) (G := G) (⋃ u ∈ 𝔉, (fun (x : 𝔓 X) => 𝔉.𝔗 (F := F) (G := G) x) u) ^ (q⁻¹ - (2 : ℝ)⁻¹) * @eLpNorm _ _ _ MeasureSpace.toMeasurableSpace f (2 : ENNReal) volume * HPow.hPow (α := ENNReal) ((volume : Measure X) A : ENNReal) (1 / 2 : ℝ)`
Docstring: Version of the forest operator theorem, but controlling the integral of the norm instead of the integral of the function multiplied by another function.
English: Let $X$ be a metric space. Let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common to chapters 2–7 of the blueprint). Write $\mu$ for the measure `volume` on $X$ provided through this instance, and $Q$ for the simple function from $X$ to the function family $\Theta(X)$ provided by the instance (`ProofData.Q`). Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (here and below $𝕔$ is the project's natural-number constant `𝕔`, whose docstring fixes it equal to $100$), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` and $o = $ `cancelPt X`; write $\mathfrak{P}$ for its type of tiles (`𝔓 X`) and $\mathcal{I}(p)$ for the grid cube `𝓘 p` of a tile $p$. For a set $\mathfrak{C} \subseteq \mathfrak{P}$ and $h : X \to \mathbb{C}$, $\mathrm{carlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p h(x)$, where $T_p$ is `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2), and $\mathrm{adjointCarlesonSum}(\mathfrak{C}, h)(x) = \sum_{p \in \mathfrak{C}} T_p^* h(x)$, where $T_p^*$ is `adjointCarleson p`. $\mathrm{dens}_2$ denotes the project density `dens₂` of a set of tiles (a value in $[0,\infty]$). All $L^2$ norms $\|\cdot\|_{L^2}$ are taken with respect to $\mu$ (as values in $[0,\infty]$) and $|\cdot|$ is the modulus of a complex number. Let $n \in \mathbb{N}$ and let $\mathfrak{F}$ be an $n$-forest (a term of the project structure `Forest X n`); $u \in \mathfrak{F}$ means that the tile $u \in \mathfrak{P}$ belongs to the set `𝔉.𝔘` of the forest, and for $u \in \mathfrak{P}$, $\mathfrak{T}(u) \subseteq \mathfrak{P}$ denotes the set `𝔉.𝔗 u`. Let $f : X \to \mathbb{C}$ be measurable with $|f(x)| \le \mathbf{1}_F(x)$ for all $x \in X$. Let $A \subseteq X$ be a measurable set with $A \subseteq G$. Then $$\int_A \Big|\sum_{u \in \mathfrak{F}} \mathrm{carlesonSum}(\mathfrak{T}(u), f)(x)\Big|\,d\mu(x) \le C_{2.0.4}(a,q,n)\, \mathrm{dens}_2\Big(\bigcup_{u \in \mathfrak{F}} \mathfrak{T}(u)\Big)^{1/q - 1/2}\, \|f\|_{L^2}\, \mu(A)^{1/2},$$ where $C_{2.0.4}(a,q,n)$ denotes the project constant `C2_0_4 a q n` (a nonnegative real). 
