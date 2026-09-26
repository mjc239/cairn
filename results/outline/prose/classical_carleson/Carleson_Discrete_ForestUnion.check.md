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

#### `TileLike` (def)
Lean: `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Type u_1`
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => Grid X × (Set (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))ᵒᵈ`

#### `TileStructure` (structure or class)
Lean: `{X : Type u} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → [inst_2 : FunctionDistances ℝ X] → outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _)) → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (u + 1)`
Docstring: A tile structure.
Constructor (every field with its type): `{X : Type u} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → [inst_2 : FunctionDistances ℝ X] → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [toPreTileStructure : PreTileStructure Q D κ S o] → (Ω : PreTileStructure.𝔓 ℝ X → Set (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _)) → (∀ {i : @GridStructure.Grid X _ inst inst_1 _ _ _ _ _}, Set.range (ι := X) ⇑Q ⊆ ⋃ (p : PreTileStructure.𝔓 ℝ X), ⋃ (_ : Membership.mem (γ := Set (PreTileStructure.𝔓 ℝ X)) (PreTileStructure.𝓘 ⁻¹' {i}) p), Ω p) → (∀ {p p' : PreTileStructure.𝔓 ℝ X}, p ≠ p' → PreTileStructure.𝓘 p = PreTileStructure.𝓘 p' → Disjoint (Ω p) (Ω p')) → (∀ {p p' : 𝔓 X}, 𝓘 p ≤ 𝓘 p' → Disjoint (Ω p) (Ω p') ∨ Ω p' ⊆ Ω p) → (∀ {p : 𝔓 X}, ball_{𝔠 p, ↑D ^ 𝔰 p / (4 : ℝ)} (𝒬 p) (5 : ℝ)⁻¹ ⊆ Ω p) → (∀ {p : 𝔓 X}, Ω p ⊆ ball_{𝔠 p, ↑D ^ 𝔰 p / (4 : ℝ)} (𝒬 p) (1 : ℝ)) → TileStructure Q D κ S o`

#### `TileStructure.toPreTileStructure` (def)
Lean: `{X : Type u} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {inst_2 : FunctionDistances ℝ X} → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : TileStructure Q D κ S o] → PreTileStructure Q D κ S o`
Definition: `fun (X : Type u) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {inst_2 : FunctionDistances ℝ X} {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : TileStructure Q D κ S o] => self.1`

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

#### `instPartialOrderTileLike` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → PartialOrder (TileLike X (F := F) (G := G))`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => { le := instPartialOrderTileLike._aux_1, lt := instPartialOrderTileLike._aux_3, le_refl := ⋯, le_trans := ⋯, lt_iff_le_not_ge := ⋯, le_antisymm := ⋯ }`

#### `smul` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℝ → 𝔓 X → TileLike X (F := F) (G := G)`
Docstring: This is not defined as such in the blueprint, but `λp ≲ λ'p'` can be written using `smul l p ≤ smul l' p'`. Beware: `smul 1 p` is very different from `toTileLike p`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (l : ℝ) (p : 𝔓 X) => (𝓘 p, ball_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) l)`

#### `ℭ₁` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `ℭ₁(k, n, j)` of `ℭ(k, n)`, given in (5.1.9). Together with `𝔏₀(k, n)` this forms a partition.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => preℭ₁ (F := F) (G := G) k n j \ preℭ₁ (F := F) (G := G) k n (j + (1 : ℕ))`

#### `𝓘` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → Grid X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] => PreTileStructure.𝓘`

#### `𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → (X : Type u) → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [PreTileStructure.{u, u_1, u_2} Q D κ S o] → Type u`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] (X : Type u) {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X`

#### `C5_1_2` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant used in Lemma 5.1.2. Has value `2 ^ (441 * a ^ 3) / (q - 1) ^ 4` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => (2 : NNReal) ^ (((3 : ℕ) * 𝕔 + (16 : ℕ) + (5 : ℕ) * (𝕔 / (4 : ℕ))) * a ^ (3 : ℕ)) / (q - (1 : NNReal)) ^ (4 : ℕ)`

#### `G'` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set X`
Docstring: The set `G'`, defined below (5.1.28).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => G₁ (F := F) (G := G) ∪ G₂ (F := F) (G := G) ∪ G₃ (F := F) (G := G)`

#### `MeasureTheory.DoublingMeasure.toMeasureSpace` (def)
Lean: `{X : Type u_3} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → [self : DoublingMeasure X A] → MeasureSpace X`
Definition: `fun (X : Type u_3) {A : outParam NNReal} {inst : PseudoMetricSpace X} [self : DoublingMeasure X A] => self.3`

#### `carlesonSum` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → (X → ℂ) → X → ℂ`
Docstring: The operator `T_ℭ f` defined at the bottom of Section 7.4. We will use this in other places of the formalization as well.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [PseudoMetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) => ∑ p : 𝔓 X with p ∈ ℭ, carlesonOn (F := F) (G := G) p f x`

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

#### `GridStructure.coeGrid` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → Set X`
Docstring: The collection of dyadic cubes
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.3`

#### `ℭ₅` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `ℭ₅(k, n, j)` of `ℭ₄(k, n, j)`, given in (5.1.23).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => ℭ₄ (F := F) (G := G) k n j \ 𝔏₄ (F := F) (G := G) k n j`

#### `EquivalenceOn` (inductive)
Lean: `{α : Type u_1} → (α → α → Prop) → Set α → Prop`
Docstring: An equivalence relation on the set `s`.
Constructor (every field with its type): `∀ {α : Type u_1} {r : α → α → Prop} {s : Set α}, (∀ x ∈ s, r x x) → (∀ {x y : α}, x ∈ s → y ∈ s → r x y → r y x) → (∀ {x y z : α}, x ∈ s → y ∈ s → z ∈ s → r x y → r y z → r x z) → EquivalenceOn r s`

#### `𝔘₂` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `𝔘₂(k, n, j)` of `𝔘₁(k, n, j)`, given in (5.4.2).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => {u : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (𝔘₁ (F := F) (G := G) k n j) u ∧ ¬Disjoint (𝔗₁ (F := F) (G := G) k n j u) (ℭ₆ (F := F) (G := G) k n j)}`

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

#### `instPseudoMetricSpaceWithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → {x : X} → {r : ℝ} → PseudoMetricSpace (WithFunctionDistance x r)`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] {x : X} {r : ℝ} => FunctionDistances.metric x r`

#### `TileStructure.Forest` (structure or class)
Lean: `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → Type u_1`
Docstring: An `n`-forest
Constructor (every field with its type): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → (𝔘 : Set (𝔓 X)) → (𝔗 : 𝔓 X → Set (𝔓 X)) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → (𝔗 u).Nonempty) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → (𝔗 u).OrdConnected) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → ∀ {p : 𝔓 X}, p ∈ 𝔗 u → 𝓘 p ≠ 𝓘 u) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → ∀ {p : 𝔓 X}, p ∈ 𝔗 u → smul (F := F) (G := G) (4 : ℝ) p ≤ smul (F := F) (G := G) (1 : ℝ) u) → (∀ {x : X}, stackSize (F := F) (G := G) 𝔘 x ≤ (2 : ℕ) ^ n) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → dens₁ (F := F) (G := G) (𝔗 u) ≤ (2 : ENNReal) ^ ((4 : ℝ) * ↑a - ↑n + (1 : ℝ))) → (∀ {u u' : 𝔓 X}, u ∈ 𝔘 → u' ∈ 𝔘 → u ≠ u' → ∀ {p : 𝔓 X}, p ∈ 𝔗 u' → 𝓘 p ≤ 𝓘 u → (2 : ℝ) ^ (defaultZ a * (n + (1 : ℕ))) < dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) (𝒬 u)) → (∀ {u : 𝔓 X}, u ∈ 𝔘 → ∀ {p : 𝔓 X}, p ∈ 𝔗 u → Metric.ball (𝔠 p) ((8 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p)) ⊆ ↑(𝓘 u)) → Forest X (F := F) (G := G) n`

#### `dens₁` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ENNReal`
Docstring: This density is defined to live in `ℝ≥0∞`. Use `ENNReal.toReal` to get a real number.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔓' : Set (𝔓 X)) => ⨆ p' ∈ 𝔓', ⨆ (l : NNReal), ⨆ (_ : l ≥ (2 : NNReal)), HPow.hPow (β := ℝ) (↑l) (-↑a) * ⨆ p ∈ lowerCubes (F := F) (G := G) 𝔓', ⨆ (_ : smul (F := F) (G := G) (↑l) p' ≤ smul (F := F) (G := G) (↑l) p), HDiv.hDiv (α := ENNReal) (β := ENNReal) ((volume : Measure X) (E₂ (F := F) (G := G) (↑l) p) : ENNReal) ((volume : Measure X) ↑(𝓘 p) : ENNReal)`

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

#### `TileStructure.Ω` (def)
Lean: `{X : Type u} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {inst_2 : FunctionDistances ℝ X} → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : TileStructure Q D κ S o] → PreTileStructure.𝔓 ℝ X → Set (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _)`
Definition: `fun (X : Type u) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {inst_2 : FunctionDistances ℝ X} {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : TileStructure Q D κ S o] => self.2`

#### `FunctionDistances.coeΘ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → @Θ _ X inst inst_1 _ → C(X, 𝕜)`
Docstring: The coercion map from `Θ` to `C(X, 𝕜)`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.2`

#### `𝕔` (def)
Lean: `ℕ`
Docstring: The main constant in the blueprint, driving all the construction, is `D = 2 ^ (100 * a ^ 2)`. It turns out that the proof is robust, and works for other values of `100`, giving better constants in the end. We will formalize it using a parameter `𝕔` (that we fix equal to `100` to follow the blueprint) and having `D = 2 ^ (𝕔 * a ^ 2)`. We register two lemmas `seven_le_c` and `c_le_100` and will never unfold `𝕔` from this point on.
Definition: `wrapped✝.1`

#### `preℭ₁` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => {p : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (ℭ (F := F) (G := G) k n) p ∧ (2 : ℕ) ^ j ≤ Finset.card.{u_1} (α := 𝔓 X) {q_1 : 𝔓 X | q_1 ∈ 𝔅 (F := F) (G := G) k n p}}`

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

#### `carlesonOn` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
Docstring: The operator `T_𝔭` defined in Proposition 2.0.2.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [PseudoMetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) => (E (F := F) (G := G) p).indicator fun (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => Complex.exp (Complex.I * (↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y) - ↑(((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) x))) * Ks (𝔰 p) x y * f y`

#### `instFintype𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (𝔓.{u, u_1, u_2} X)`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.fintype_𝔓`

#### `ℭ` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → Set (𝔓 X)`
Docstring: The partition `ℭ(k, n)` of `𝔓(k)` by density, given in (5.1.7).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n : ℕ) => {p : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (TilesAt (F := F) (G := G) k) p ∧ dens' (F := F) (G := G) k {p} ∈ Set.Ioc ((2 : ENNReal) ^ ((4 : ℤ) * ↑a - ↑n)) ((2 : ENNReal) ^ ((4 : ℤ) * ↑a - ↑n + (1 : ℤ)))}`

#### `ℭ₄` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `ℭ₄(k, n, j)` of `ℭ₃(k, n, j)`, given in (5.1.19).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => Set.layersBelow (ℭ₃ (F := F) (G := G) k n j) (defaultZ a * (n + (1 : ℕ)))`

#### `𝔏₄` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `𝔏₄(k, n, j)` of `ℭ₄(k, n, j)`, given near (5.1.22). Todo: we may need to change the definition to say that `p` is at most the least upper bound of `𝓛 n u` in `Grid X`.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => {p : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (ℭ₄ (F := F) (G := G) k n j) p ∧ ∃ (u : 𝔓 X), Membership.mem (γ := Set (𝔓 X)) (𝔘₁ (F := F) (G := G) k n j) u ∧ ↑(𝓘 p) ⊆ ⋃ i ∈ 𝓛 (F := F) (G := G) n u, ↑i}`

#### `𝔘₁` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `𝔘₁(k, n, j)` of `ℭ₁(k, n, j)`, given in (5.1.14).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => {u : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (ℭ₁ (F := F) (G := G) k n j) u ∧ ∀ (p : 𝔓 X), Membership.mem (γ := Set (𝔓 X)) (ℭ₁ (F := F) (G := G) k n j) p → 𝓘 u < 𝓘 p → Disjoint (ball_{𝔠 u, ↑(defaultD a) ^ 𝔰 u / (4 : ℝ)} (𝒬 u) (100 : ℝ)) (ball_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) (100 : ℝ))}`

#### `GridStructure.s` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → ℤ`
Docstring: scale functions
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.4`

#### `EquivalenceOn.reprs` (def)
Lean: `{α : Type u_1} → {r : α → α → Prop} → {s : Set α} → EquivalenceOn r s → Set α`
Docstring: The set of representatives of an equivalence relation on a set.
Definition: `fun {α : Type u_1} {r : α → α → Prop} {s : Set α} (hr : EquivalenceOn r s) => hr.out (r := r) (s := s) '' s`

#### `c` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Grid X → X`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.c`

#### `FunctionDistances.metric` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → X → ℝ → PseudoMetricSpace (@Θ _ X inst inst_1 _)`
Docstring: For each `_x : X` and `_r : ℝ`, a `PseudoMetricSpace Θ`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.4`

#### `instPartialOrder𝔓Real` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → PartialOrder (𝔓 X)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => PartialOrder.lift (toTileLike (F := F) (G := G)) ⋯`

#### `stackSize` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → X → ℕ`
Docstring: The number of tiles `p` in `s` whose underlying cube `𝓘 p` contains `x`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (C : Set (𝔓 X)) (x : X) => ∑ p : 𝔓 X with p ∈ C, (↑(𝓘 p)).indicator (1 : X → ℕ) x`

#### `TileStructure.Forest.𝔘` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → Set (𝔓 X)`
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] (a : ℕ) (q : ℝ) (K : X → X → ℂ) (σ₁ σ₂ : X → ℤ) (F G : Set X) [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (n : ℕ) (self : Forest X (F := F) (G := G) n) => self.1`

#### `TileStructure.Forest.𝔗` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {n : ℕ} → Forest X (F := F) (G := G) n → 𝔓 X → Set (𝔓 X)`
Docstring: The value of `𝔗 u` only matters when `u ∈ 𝔘`.
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] (a : ℕ) (q : ℝ) (K : X → X → ℂ) (σ₁ σ₂ : X → ℤ) (F G : Set X) [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (n : ℕ) (self : Forest X (F := F) (G := G) n) => self.2`

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

#### `iteratedMaximalSubfamily` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ℕ → Set (𝔓 X)`
Docstring: Iterating `maximalSubfamily` to obtain disjoint subfamilies of `A`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (A : Set (𝔓 X)) => WellFounded.Nat.fix (motive := fun (n : ℕ) => Set (𝔓 X)) (fun (x : ℕ) => x) fun (n : ℕ) (a_1 : (y : ℕ) → InvImage (fun (x1 x2 : ℕ) => x1 < x2) (fun (x : ℕ) => x) y n → Set (𝔓 X)) => maximalSubfamily (F := F) (G := G) (A \ ⋃ (i : ↑{i : ℕ | i < n}), have this := ⋯; a_1 ↑i ⋯)`

#### `AllBallsCoverBalls` (def)
Lean: `(X : Type u_2) → [PseudoMetricSpace X] → ℝ → ℕ → Prop`
Docstring: For all `r`, balls of radius `r` in `X` are covered by `n` balls of radius `a * r`
Definition: `fun (X : Type u_2) [PseudoMetricSpace X] (a : ℝ) (n : ℕ) => ∀ (r : ℝ), BallsCoverBalls X (a * r) r n`

#### `localOscillation` (def)
Lean: `{𝕜 : Type u_3} → {X : Type u_4} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → Set X → C(X, 𝕜) → C(X, 𝕜) → ENNReal`
Docstring: The local oscillation of two functions w.r.t. a set `E`. This is `d_E` in the blueprint.
Definition: `fun {𝕜 : Type u_3} {X : Type u_4} [RCLike 𝕜] [PseudoMetricSpace X] (E : Set X) (f g : C(X, 𝕜)) => ⨆ z ∈ E ×ˢ E, ENNReal.ofReal ‖HAdd.hAdd (β := 𝕜) (HSub.hSub (β := 𝕜) (HSub.hSub (α := 𝕜) (β := 𝕜) (f z.1 : 𝕜) (g z.1 : 𝕜)) (f z.2 : 𝕜)) (g z.2 : 𝕜)‖`

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

#### `𝔅` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → 𝔓 X → Set (𝔓 X)`
Docstring: The subset `𝔅(p)` of `𝔐(k, n)`, given in (5.1.8).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n : ℕ) (p : 𝔓 X) => {m : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (𝔐 (F := F) (G := G) k n) m ∧ smul (F := F) (G := G) (100 : ℝ) p ≤ smul (F := F) (G := G) (1 : ℝ) m}`

#### `highDensityTiles` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X)`
Docstring: The set $\mathcal{P}_{F,G}$, defined in (5.1.24).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => {p : 𝔓 X | HDiv.hDiv (β := ENNReal) (HMul.hMul (β := ENNReal) ((2 : ENNReal) ^ ((2 : ℕ) * a + (5 : ℕ))) ((volume : Measure X) F : ENNReal)) ((volume : Measure X) G : ENNReal) < dens₂ (F := F) (G := G) {p}}`

#### `setA` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set X`
Docstring: The set `A(λ, k, n)`, defined in (5.1.26).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (l k n : ℕ) => {x : X | l * (2 : ℕ) ^ (n + (1 : ℕ)) < stackSize (F := F) (G := G) (𝔐 (F := F) (G := G) k n) x}`

#### `E` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → Set X`
Docstring: The set `E` defined in Proposition 2.0.2.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) => {x : X | x ∈ 𝓘 p ∧ Membership.mem (α := @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) (Ω p) ((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) ∧ 𝔰 p ∈ Set.Icc (σ₁ x) (σ₂ x)}`

#### `Ks` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {K : X → X → ℂ} → [inst : PseudoMetricSpace X] → [KernelProofData a K] → ℤ → X → X → ℂ`
Docstring: K_s in the blueprint
Definition: `fun {X : Type u_1} {a : ℕ} {K : X → X → ℂ} [PseudoMetricSpace X] [KernelProofData a K] (s : ℤ) (x y : X) => K x y * ↑(ψ (defaultD a) (HPow.hPow (α := ℝ) (↑(defaultD a)) (-s) * dist x y))`

#### `PreTileStructure.fintype_𝔓` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X)`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.3`

#### `TilesAt` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → Set (𝔓 X)`
Docstring: The definition `𝔓(k)` given in (5.1.3).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k : ℕ) => 𝓘 ⁻¹' 𝓒 (F := F) (G := G) k`

#### `aux𝓒` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → Set (Grid X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k : ℕ) => {i : Grid X | ∃ (j : Grid X), i ≤ j ∧ HMul.hMul (β := ENNReal) (HPow.hPow (β := ℤ) (2 : ENNReal) (-↑k)) ((volume : Measure X) ↑j : ENNReal) < (volume : Measure X) (G ∩ ↑j)}`

#### `dens'` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → Set (𝔓 X) → ENNReal`
Docstring: The definition `dens'_k(𝔓')` given in (5.1.6).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k : ℕ) (P' : Set (𝔓 X)) => ⨆ p' ∈ P', ⨆ (l : NNReal), ⨆ (_ : (2 : NNReal) ≤ l), ⨆ (p : 𝔓 X), ⨆ (_ : Membership.mem (γ := Set (𝔓 X)) (TilesAt (F := F) (G := G) k) p), ⨆ (_ : smul (F := F) (G := G) (↑l) p' ≤ smul (F := F) (G := G) (↑l) p), HDiv.hDiv (β := ENNReal) (HMul.hMul (β := ENNReal) (HPow.hPow (β := ℤ) (↑l) (-↑a)) ((volume : Measure X) (E₂ (F := F) (G := G) (↑l) p) : ENNReal)) ((volume : Measure X) ↑(𝓘 p) : ENNReal)`

#### `Set.layersBelow` (def)
Lean: `{α : Type u_1} → [PartialOrder α] → Set α → ℕ → Set α`
Docstring: The elements below `A`'s `n` maximal layers.
Definition: `fun {α : Type u_1} [PartialOrder α] (A : Set α) (n : ℕ) => A \ ⋃ (k : ℕ), ⋃ (_ : k ≤ n), A.maxLayer k`

#### `ℭ₃` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `ℭ₃(k, n, j)` of `ℭ₂(k, n, j)`, given in (5.1.16).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => ℭ₂ (F := F) (G := G) k n j \ 𝔏₂ (F := F) (G := G) k n j`

#### `𝓛` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → 𝔓 X → Set (Grid X)`
Docstring: The subset `𝓛(u)` of `Grid X`, given near (5.1.20). Note: It seems to also depend on `n`.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (n : ℕ) (u : 𝔓 X) => {i : Grid X | i ≤ 𝓘 u ∧ s i + ↑(defaultZ a * (n + (1 : ℕ))) + (1 : ℤ) = 𝔰 u ∧ ¬Metric.ball (c i) ((8 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (s i)) ⊆ ↑(𝓘 u)}`

#### `EquivalenceOn.out` (def)
Lean: `{α : Type u_1} → {r : α → α → Prop} → {s : Set α} → EquivalenceOn r s → α → α`
Docstring: An arbitrary representative of `x` w.r.t. the equivalence relation `r`.
Definition: `fun {α : Type u_1} {r : α → α → Prop} {s : Set α} (hr : EquivalenceOn r s) (x : α) => if hx : x ∈ s then ↑⟦(⟨x, hx⟩ : { x : α // x ∈ s })⟧.out else x`

#### `toTileLike` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → TileLike X (F := F) (G := G)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) => (𝓘 p, Ω p)`

#### `TileLike.toSet` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → TileLike X (F := F) (G := G) → Set X`
Docstring: From a TileLike, we can construct a set. This is used in the definitions `E₁` and `E₂`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (t : TileLike X (F := F) (G := G)) => ↑(t.fst (F := F) (G := G)) ∩ G ∩ ⇑(Q (F := F) (G := G)) ⁻¹' t.snd (F := F) (G := G)`

#### `maximalSubfamily` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → Set (𝔓 X)`
Docstring: A disjoint subfamily of `A` covering everything.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (A : Set (𝔓 X)) => ⋯.choose (p := fun (B : Set (𝔓 X)) => (B.PairwiseDisjoint (α := Set X) fun (p : 𝔓 X) => ↑(𝓘 p)) ∧ B ⊆ A ∧ ∀ a_1 ∈ A, ∃ b ∈ B, ↑(𝓘 a_1) ⊆ ↑(𝓘 b))`

## Translations

### `𝔗₁`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) (u : 𝔓 X) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → 𝔓 X → Set (𝔓 X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) (u : 𝔓 X) => {p : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (ℭ₁ (F := F) (G := G) k n j) p ∧ 𝓘 p ≠ 𝓘 u ∧ smul (F := F) (G := G) (2 : ℝ) p ≤ smul (F := F) (G := G) (1 : ℝ) u}`
Docstring: The subset `𝔗₁(u)` of `ℭ₁(k, n, j)`, given in (5.4.1). In lemmas, we will assume `u ∈ 𝔘₁ k n l`
English: Under the standing assumptions (a metric space $X$ with the `ProofData` bundle for parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K$, integer-valued functions $\sigma_1,\sigma_2$ and sets $F, G \subseteq X$, and the tile structure on $X$ with the default parameters), for natural numbers $k, n, j$ and a tile $u \in \mathfrak{P}(X)$, $\mathfrak{T}_1(k,n,j,u)$ is a set of tiles. According to its docstring, it is the subset $\mathfrak{T}_1(u)$ of $\mathfrak{C}_1(k,n,j)$ given in (5.4.1), and in lemmas one assumes $u \in \mathfrak{U}_1(k,n,l)$.

### `forest_union`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C5_1_2 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {f : X → ℂ}, (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable f → ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (𝔓₁ (F := F) (G := G)) f x‖ₑ ≤ ↑(C5_1_2 a (nnq X (F := F) (G := G))) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹`
Docstring: Lemma 5.1.2 in the blueprint: the integral of the Carleson sum over the set which can naturally be decomposed as a union of forests can be controlled, thanks to the estimate for a single forest.
English: (Lemma 5.1.2) Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \to X \to \mathbb{C}$ a function, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ subsets. Assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common through most of chapters 2-7 of the blueprint); through its `KernelProofData` component it equips $X$ with a doubling-measure structure `DoublingMeasure X (2^a)`, hence with a measure, denoted $\mu$ (the `volume` of $X$), and it provides $Q$ (`ProofData.Q`), a simple function from $X$ to the type $\Theta(X)$ of functions of the `FunctionDistances` structure. Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` (a natural number determined by the `ProofData`) and $o = $ `cancelPt X` (the point $o$ of the blueprint). Write $\mathfrak{P}$ for the (finite) type `𝔓 X` of tiles of this tile structure. For a set $\mathfrak{C} \subseteq \mathfrak{P}$, a function $g : X \to \mathbb{C}$ and $x \in X$, write $T_{\mathfrak{C}} g(x) = $ `carlesonSum ℭ g x` $= \sum_{p \in \mathfrak{C}} T_p g(x)$, where $T_p$ is the project operator `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2). Let $G' = G_1 \cup G_2 \cup G_3 \subseteq X$ be the project set `G'`, where $G_1, G_2, G_3$ are the project sets `G₁`, `G₂`, `G₃` (defined in (5.1.25), (5.1.27), (5.1.28) of the blueprint). Let $\mathfrak{P}_1 = $ `𝔓₁` $= \bigcup_{n \in \mathbb{N}} \bigcup_{k \le n} \bigcup_{j \le 2n+3} \mathfrak{C}_5(k,n,j)$, where $\mathfrak{C}_5(k,n,j)$ is the project set of tiles `ℭ₅ k n j`. Let $\tilde q$ denote $q$ regarded as a nonnegative real number (the project's `nnq X`). Let $f : X \to \mathbb{C}$ be a measurable function with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Integrals below are lower Lebesgue integrals, with respect to $\mu$, of the extended nonnegative real norm $\|\cdot\|_e$, and all quantities on the right-hand side are computed in $[0,\infty]$. Then $$\int^{-}_{G \setminus G'} \|T_{\mathfrak{P}_1} f(x)\|_e \, d\mu(x) \le C_{5.1.2}(a, \tilde q)\, \mu(G)^{1 - q^{-1}}\, \mu(F)^{q^{-1}},$$ where $C_{5.1.2}(a,\tilde q) = 2^{(3𝕔 + 16 + 5\lfloor 𝕔/4 \rfloor) a^3} / (\tilde q - 1)^4$ is the nonnegative real constant `C5_1_2 a (nnq X)` (with truncated subtraction in $\mathbb{R}_{\ge 0}$).

### `forest_union_aux`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C2_0_4_base a) * 2 ^ (↑a + 5 / 2) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹ * ∑ n ≤ maxℭ X, ∑ _k ≤ n, ∑ _j ≤ 2 * n + 3, ∑ _l < 4 * n + 12, 2 ^ (-(q - 1) / q * ↑n)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {f : X → ℂ}, (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable f → ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (𝔓₁ (F := F) (G := G)) f x‖ₑ ≤ ↑(C2_0_4_base a) * (2 : ENNReal) ^ (↑a + (5 / 2 : ℝ)) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹ * ∑ n ≤ maxℭ X (F := F) (G := G), ∑ _k ≤ n, ∑ _j ≤ (2 : ℕ) * n + (3 : ℕ), ∑ _l < (4 : ℕ) * n + (12 : ℕ), (2 : ENNReal) ^ (-(q - (1 : ℝ)) / q * ↑n)`
Docstring: Putting all the above decompositions together, one obtains a control of the integral of the full Carleson sum over `𝔓₁`, as a sum over all the forests.
English: Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \to X \to \mathbb{C}$ a function, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ subsets. Assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common through most of chapters 2-7 of the blueprint); through its `KernelProofData` component it equips $X$ with a doubling-measure structure `DoublingMeasure X (2^a)`, hence with a measure, denoted $\mu$ (the `volume` of $X$), and it provides $Q$ (`ProofData.Q`), a simple function from $X$ to the type $\Theta(X)$ of functions of the `FunctionDistances` structure. Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` (a natural number determined by the `ProofData`) and $o = $ `cancelPt X` (the point $o$ of the blueprint). Write $\mathfrak{P}$ for the (finite) type `𝔓 X` of tiles of this tile structure. For a set $\mathfrak{C} \subseteq \mathfrak{P}$, a function $g : X \to \mathbb{C}$ and $x \in X$, write $T_{\mathfrak{C}} g(x) = $ `carlesonSum ℭ g x` $= \sum_{p \in \mathfrak{C}} T_p g(x)$, where $T_p$ is the project operator `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2). Let $G' = G_1 \cup G_2 \cup G_3 \subseteq X$ be the project set `G'`, where $G_1, G_2, G_3$ are the project sets `G₁`, `G₂`, `G₃` (defined in (5.1.25), (5.1.27), (5.1.28) of the blueprint). Let $\mathfrak{P}_1 = $ `𝔓₁` $= \bigcup_{n \in \mathbb{N}} \bigcup_{k \le n} \bigcup_{j \le 2n+3} \mathfrak{C}_5(k,n,j)$, where $\mathfrak{C}_5(k,n,j)$ is the project set of tiles `ℭ₅ k n j`. Let $f : X \to \mathbb{C}$ be a measurable function with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Integrals below are lower Lebesgue integrals, with respect to $\mu$, of the extended nonnegative real norm $\|\cdot\|_e$, and all quantities on the right-hand side are computed in $[0,\infty]$. Let $N = $ `maxℭ X`, a natural number defined by the project from the tile structure. Let $C^{\mathrm{base}}_{2.0.4}(a)$ be the nonnegative real constant `C2_0_4_base a`. Then $$\int^{-}_{G \setminus G'} \|T_{\mathfrak{P}_1} f(x)\|_e \, d\mu(x) \le C^{\mathrm{base}}_{2.0.4}(a)\, 2^{a + 5/2}\, \mu(G)^{1 - q^{-1}}\, \mu(F)^{q^{-1}} \sum_{n=0}^{N} \sum_{k=0}^{n} \sum_{j=0}^{2n+3} \sum_{l=0}^{4n+11} 2^{-\frac{q-1}{q} n}.$$

### `ℭ₆`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => {p : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (ℭ₅ (F := F) (G := G) k n j) p ∧ ¬↑(𝓘 p) ⊆ G' (F := F) (G := G)}`
Docstring: The subset `ℭ₆(k, n, j)` of `ℭ₅(k, n, j)`, given above (5.4.1).
English: Under the standing assumptions (a metric space $X$ with the `ProofData` bundle for parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K$, integer-valued functions $\sigma_1,\sigma_2$ and sets $F, G \subseteq X$, and the tile structure on $X$ with the default parameters), for natural numbers $k, n, j$, $\mathfrak{C}_6(k,n,j)$ is a set of tiles. According to its docstring, it is the subset $\mathfrak{C}_6(k,n,j)$ of $\mathfrak{C}_5(k,n,j)$ given above (5.4.1).

### `URel`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) (u : 𝔓 X) (u' : 𝔓 X) : Prop`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → 𝔓 X → 𝔓 X → Prop`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) (u u' : 𝔓 X) => u = u' ∨ ∃ p ∈ 𝔗₁ (F := F) (G := G) k n j u, smul (F := F) (G := G) (10 : ℝ) p ≤ smul (F := F) (G := G) (1 : ℝ) u'`
Docstring: The relation `∼` defined below (5.4.2). It is an equivalence relation on `𝔘₂ k n j`.
English: Under the standing assumptions (a metric space $X$ with the `ProofData` bundle for parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K$, integer-valued functions $\sigma_1,\sigma_2$ and sets $F, G \subseteq X$, and the tile structure on $X$ with the default parameters), for natural numbers $k, n, j$ and tiles $u, u' \in \mathfrak{P}(X)$, $\mathrm{URel}(k,n,j,u,u')$ is a proposition (a relation between $u$ and $u'$). According to its docstring, it is the relation $\sim$ defined below (5.4.2), and it is an equivalence relation on $\mathfrak{U}_2(k,n,j)$.

### `equivalenceOn_urel`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : EquivalenceOn (URel k n j) (𝔘₂ k n j)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {k n j : ℕ}, EquivalenceOn (URel (F := F) (G := G) k n j) (𝔘₂ (F := F) (G := G) k n j)`
Docstring: Lemma 5.4.2.
English: (Lemma 5.4.2) Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \to X \to \mathbb{C}$ a function, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ subsets. Assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (per its docstring, the data common through most of chapters 2-7); through its `KernelProofData` component it equips $X$ with a doubling-measure structure `DoublingMeasure X (2^a)` and with compatible functions `CompatibleFunctions ℝ X (2^a)` (hence a `FunctionDistances ℝ X` structure with its type $\Theta(X)$ of functions), and it provides $Q$ (`ProofData.Q`), a simple function from $X$ to $\Theta(X)$. Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` (the least positive natural number $n$ such that $-n\le\sigma_1(x)$ and $\sigma_2(x)\le n$ for all $x\in X$ and $F$ and $G$ are contained in the open ball of radius $D^n/4$ about $o$) and $o = $ `cancelPt X` (a chosen point of $X$ at which every function of $\Theta(X)$ vanishes). Write $\mathfrak{P}$ for the type `𝔓 X` of tiles of this tile structure; each tile $p$ has a grid cube $\mathcal I(p)$ (`𝓘 p`), a point $\mathfrak c(p)=c(\mathcal I(p))\in X$ and an integer $\mathfrak s(p)=s(\mathcal I(p))$ (given by the grid-structure fields `c` and `s` applied to the cube $\mathcal I(p)$), and a function $\mathcal Q(p)\in\Theta(X)$ (`𝒬 p`). For a real $l$ and a tile $p$, `smul l p` is the pair $(\mathcal I(p),\ B_p(\mathcal Q(p), l))$ in the project type `TileLike X` (the product of the grid cubes with the order dual of the sets of elements of $\Theta(X)$), where $B_p(\mathcal Q(p),l)$ is the ball of radius $l$ around $\mathcal Q(p)$ in $\Theta(X)$ for the function-distance pseudometric attached to the point $\mathfrak c(p)$ and radius $D^{\mathfrak s(p)}/4$; `smul l p ≤ smul l' p'` refers to the project's partial order on `TileLike X`. Let $k, n, j$ be natural numbers. For a tile $u$, $\mathfrak T_1(k,n,j,u)$ (`𝔗₁ k n j u`) is the set of tiles $p$ in the project set $\mathfrak C_1(k,n,j)$ (`ℭ₁ k n j`) with $\mathcal I(p)\ne\mathcal I(u)$ and `smul 2 p ≤ smul 1 u`. Let $\mathfrak{U}_2(k,n,j) \subseteq \mathfrak{P}$ be the project set `𝔘₂ k n j` (per its docstring, the subset of $\mathfrak U_1(k,n,j)$ given in (5.4.2)). Let $\sim$ be the project relation `URel k n j` on $\mathfrak{P}$, whose definition body is: $u \sim u'$ iff $u = u'$ or there is $p \in \mathfrak{T}_1(k,n,j,u)$ with `smul 10 p ≤ smul 1 u'`. Then $\sim$ is an equivalence relation on the set $\mathfrak{U}_2(k,n,j)$ (the project predicate `EquivalenceOn (URel k n j) (𝔘₂ k n j)`, per its docstring: an equivalence relation on the set).

### `forest_inner`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ 𝔘₃ k n j) (hp : p ∈ 𝔗₂ k n j u) : Metric.ball (𝔠 p) (8 * ↑(defaultD a) ^ 𝔰 p) ⊆ ↑(𝓘 u)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {k n j : ℕ} {p u : 𝔓 X}, Membership.mem (γ := Set (𝔓 X)) (𝔘₃ (F := F) (G := G) k n j) u → p ∈ 𝔗₂ (F := F) (G := G) k n j u → Metric.ball (𝔠 p) ((8 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p)) ⊆ ↑(𝓘 u)`
Docstring: Lemma 5.4.7, verifying (2.0.37)
English: (Lemma 5.4.7, verifying (2.0.37)) Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \to X \to \mathbb{C}$ a function, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ subsets. Assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common through most of chapters 2-7 of the blueprint); through its `KernelProofData` component it equips $X$ with a doubling-measure structure `DoublingMeasure X (2^a)`, hence with a measure, denoted $\mu$ (the `volume` of $X$), and it provides $Q$ (`ProofData.Q`), a simple function from $X$ to the type $\Theta(X)$ of functions of the `FunctionDistances` structure. Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` (a natural number determined by the `ProofData`) and $o = $ `cancelPt X` (the point $o$ of the blueprint). Write $\mathfrak{P}$ for the (finite) type `𝔓 X` of tiles of this tile structure. Let $k, n, j$ be natural numbers and $p, u \in \mathfrak{P}$ tiles. For a tile $t$, let $\mathcal{I}(t) = $ `𝓘 t` be its cube in the grid `Grid X`, regarded as a subset of $X$, let $c(t) = $ `𝔠 t` $\in X$ be the center of $\mathcal{I}(t)$ and $s(t) = $ `𝔰 t` $\in \mathbb{Z}$ its scale. Suppose $u \in \mathfrak{U}_3(k,n,j)$, the project set `𝔘₃ k n j`, and $p \in \mathfrak{T}_2(k,n,j,u)$, the project set `𝔗₂ k n j u`. Then the open ball $B\big(c(p), 8 D^{s(p)}\big) \subseteq \mathcal{I}(u)$, where $D = 2^{𝕔 a^2}$ is regarded as a real number.

### `forest_separation`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hu : u ∈ 𝔘₃ k n j) (hu' : u' ∈ 𝔘₃ k n j) (huu' : u ≠ u') (hp : p ∈ 𝔗₂ k n j u') (h : 𝓘 p ≤ 𝓘 u) : 2 ^ (defaultZ a * (n + 1)) < dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) (𝒬 u)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {k n j : ℕ} {p u u' : 𝔓 X}, Membership.mem (γ := Set (𝔓 X)) (𝔘₃ (F := F) (G := G) k n j) u → Membership.mem (γ := Set (𝔓 X)) (𝔘₃ (F := F) (G := G) k n j) u' → u ≠ u' → p ∈ 𝔗₂ (F := F) (G := G) k n j u' → 𝓘 p ≤ 𝓘 u → (2 : ℝ) ^ (defaultZ a * (n + (1 : ℕ))) < dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) (𝒬 u)`
Docstring: Lemma 5.4.6, verifying (2.0.36) Note: swapped `u` and `u'` to match (2.0.36)
English: (Lemma 5.4.6, verifying (2.0.36)) Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \to X \to \mathbb{C}$ a function, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ subsets. Assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common through most of chapters 2-7 of the blueprint); through its `KernelProofData` component it equips $X$ with a doubling-measure structure `DoublingMeasure X (2^a)`, hence with a measure, denoted $\mu$ (the `volume` of $X$), and it provides $Q$ (`ProofData.Q`), a simple function from $X$ to the type $\Theta(X)$ of functions of the `FunctionDistances` structure. Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` (a natural number determined by the `ProofData`) and $o = $ `cancelPt X` (the point $o$ of the blueprint). Write $\mathfrak{P}$ for the (finite) type `𝔓 X` of tiles of this tile structure. Let $k, n, j$ be natural numbers and $p, u, u' \in \mathfrak{P}$ tiles. For a tile $t$, let $\mathcal{I}(t) = $ `𝓘 t` be its cube in the grid `Grid X`, let $c(t) = $ `𝔠 t` $\in X$ be the center of $\mathcal{I}(t)$, $s(t) = $ `𝔰 t` $\in \mathbb{Z}$ its scale, and $\mathcal{Q}(t) = $ `𝒬 t` $\in \Theta(X)$ the element of $\Theta(X)$ attached to $t$ by the tile structure. For $x \in X$ and $r \in \mathbb{R}$, let $d_{x,r}$ be the pseudometric on $\Theta(X)$ provided by the `FunctionDistances` structure for the ball of center $x$ and radius $r$. Suppose $u, u' \in \mathfrak{U}_3(k,n,j)$ (the project set `𝔘₃ k n j`), $u \ne u'$, $p \in \mathfrak{T}_2(k,n,j,u')$ (the project set `𝔗₂ k n j u'`), and $\mathcal{I}(p) \le \mathcal{I}(u)$ in the project partial order on `Grid X`. Then $$2^{Z(n+1)} < d_{c(p),\, D^{s(p)}/4}\big(\mathcal{Q}(p), \mathcal{Q}(u)\big),$$ where $Z = $ `defaultZ a` $= 2^{12a}$ and $D = 2^{𝕔 a^2}$ is regarded as a real number.

### `forest`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (k : ℕ) (n : ℕ) (j : ℕ) (l : ℕ) : Forest X n`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → (n : ℕ) → ℕ → ℕ → Forest X (F := F) (G := G) n`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j l : ℕ) => Forest.mk (F := F) (G := G) (𝔘₄ (F := F) (G := G) k n j l) (𝔗₂ (F := F) (G := G) k n j) ⋯ ⋯ ⋯ ⋯ ⋯ ⋯ ⋯ ⋯`
Docstring: The forest based on `𝔘₄ k n j l`.
English: Under the standing assumptions (a metric space $X$ with the `ProofData` bundle for parameters $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K$, integer-valued functions $\sigma_1,\sigma_2$ and sets $F, G \subseteq X$, and the tile structure on $X$ with the default parameters), for natural numbers $k, n, j, l$, $\mathrm{forest}(k,n,j,l)$ is an $n$-forest on $X$ (an element of `Forest X n`). According to its docstring, it is the forest based on $\mathfrak{U}_4(k,n,j,l)$.

### `carlesonSum_ℭ₆_eq_sum`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hkn : k ≤ n) : carlesonSum (ℭ₆ k n j) f x = ∑ l < 4 * n + 12, carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {f : X → ℂ} {x : X} {k n j : ℕ}, k ≤ n → carlesonSum (F := F) (G := G) (ℭ₆ (F := F) (G := G) k n j) f x = ∑ l < (4 : ℕ) * n + (12 : ℕ), carlesonSum (F := F) (G := G) (⋃ (u : 𝔓 X), ⋃ (_ : Membership.mem (γ := Set (𝔓 X)) (𝔘₄ (F := F) (G := G) k n j l) u), 𝔗₂ (F := F) (G := G) k n j u) f x`
Docstring: The Carleson sum over `ℭ₆` can be decomposed as a sum over `4 n + 12` forests based on `𝔘₄ k n j l`.
English: Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \to X \to \mathbb{C}$ a function, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ subsets. Assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common through most of chapters 2-7 of the blueprint); through its `KernelProofData` component it equips $X$ with a doubling-measure structure `DoublingMeasure X (2^a)`, hence with a measure, denoted $\mu$ (the `volume` of $X$), and it provides $Q$ (`ProofData.Q`), a simple function from $X$ to the type $\Theta(X)$ of functions of the `FunctionDistances` structure. Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` (a natural number determined by the `ProofData`) and $o = $ `cancelPt X` (the point $o$ of the blueprint). Write $\mathfrak{P}$ for the (finite) type `𝔓 X` of tiles of this tile structure. For a set $\mathfrak{C} \subseteq \mathfrak{P}$, a function $g : X \to \mathbb{C}$ and $x \in X$, write $T_{\mathfrak{C}} g(x) = $ `carlesonSum ℭ g x` $= \sum_{p \in \mathfrak{C}} T_p g(x)$, where $T_p$ is the project operator `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2). For natural numbers $k, n, j, l$, let $\mathfrak{F}_{k,n,j,l} = \bigcup_{u \in \mathfrak{U}_4(k,n,j,l)} \mathfrak{T}_2(k,n,j,u) \subseteq \mathfrak{P}$, where $\mathfrak{U}_4(k,n,j,l)$ is the project set `𝔘₄ k n j l` (by its docstring, a union of $2^n$ disjoint subfamilies of $\mathfrak{U}_3(k,n,j)$ = `𝔘₃ k n j`) and $\mathfrak{T}_2(k,n,j,u)$ is the project set `𝔗₂ k n j u` (the subset $\mathfrak{T}_2(u)$ of $\mathfrak{C}_6(k,n,j)$ given in (5.4.5)). Let $f : X \to \mathbb{C}$, $x \in X$, and let $k, n, j$ be natural numbers with $k \le n$. Let $\mathfrak{C}_6(k,n,j) \subseteq \mathfrak{P}$ be the project set `ℭ₆ k n j`. Then $$T_{\mathfrak{C}_6(k,n,j)} f(x) = \sum_{l=0}^{4n+11} T_{\mathfrak{F}_{k,n,j,l}} f(x).$$

### `lintegral_carlesonSum_forest`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * (2 ^ (2 * a + 5) * volume F / volume G) ^ (q⁻¹ - 2⁻¹) * volume F ^ (1 / 2) * volume G ^ (1 / 2)`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {k n j l : ℕ} {f : X → ℂ}, Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (⋃ (u : 𝔓 X), ⋃ (_ : Membership.mem (γ := Set (𝔓 X)) (𝔘₄ (F := F) (G := G) k n j l) u), 𝔗₂ (F := F) (G := G) k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * HDiv.hDiv (β := ENNReal) (HMul.hMul (β := ENNReal) ((2 : ENNReal) ^ ((2 : ℕ) * a + (5 : ℕ))) ((volume : Measure X) F : ENNReal)) ((volume : Measure X) G : ENNReal) ^ (q⁻¹ - (2 : ℝ)⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) (1 / 2 : ℝ) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) (1 / 2 : ℝ)`
Docstring: For each forest, the integral of the norm of the Carleson sum can be controlled thanks to the forest theorem and to the density control coming from the fact we are away from `G₁`.
English: Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \to X \to \mathbb{C}$ a function, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ subsets. Assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common through most of chapters 2-7 of the blueprint); through its `KernelProofData` component it equips $X$ with a doubling-measure structure `DoublingMeasure X (2^a)`, hence with a measure, denoted $\mu$ (the `volume` of $X$), and it provides $Q$ (`ProofData.Q`), a simple function from $X$ to the type $\Theta(X)$ of functions of the `FunctionDistances` structure. Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` (a natural number determined by the `ProofData`) and $o = $ `cancelPt X` (the point $o$ of the blueprint). Write $\mathfrak{P}$ for the (finite) type `𝔓 X` of tiles of this tile structure. For a set $\mathfrak{C} \subseteq \mathfrak{P}$, a function $g : X \to \mathbb{C}$ and $x \in X$, write $T_{\mathfrak{C}} g(x) = $ `carlesonSum ℭ g x` $= \sum_{p \in \mathfrak{C}} T_p g(x)$, where $T_p$ is the project operator `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2). Let $G' = G_1 \cup G_2 \cup G_3 \subseteq X$ be the project set `G'`, where $G_1, G_2, G_3$ are the project sets `G₁`, `G₂`, `G₃` (defined in (5.1.25), (5.1.27), (5.1.28) of the blueprint). For natural numbers $k, n, j, l$, let $\mathfrak{F}_{k,n,j,l} = \bigcup_{u \in \mathfrak{U}_4(k,n,j,l)} \mathfrak{T}_2(k,n,j,u) \subseteq \mathfrak{P}$, where $\mathfrak{U}_4(k,n,j,l)$ is the project set `𝔘₄ k n j l` (by its docstring, a union of $2^n$ disjoint subfamilies of $\mathfrak{U}_3(k,n,j)$ = `𝔘₃ k n j`) and $\mathfrak{T}_2(k,n,j,u)$ is the project set `𝔗₂ k n j u` (the subset $\mathfrak{T}_2(u)$ of $\mathfrak{C}_6(k,n,j)$ given in (5.4.5)). Let $k, n, j, l$ be natural numbers and let $f : X \to \mathbb{C}$ be a measurable function with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Integrals below are lower Lebesgue integrals, with respect to $\mu$, of the extended nonnegative real norm $\|\cdot\|_e$, and all quantities on the right-hand side are computed in $[0,\infty]$. Then $$\int^{-}_{G \setminus G'} \|T_{\mathfrak{F}_{k,n,j,l}} f(x)\|_e \, d\mu(x) \le C_{2.0.4}(a,q,n) \left(\frac{2^{2a+5}\mu(F)}{\mu(G)}\right)^{q^{-1} - 2^{-1}} \mu(F)^{1/2}\, \mu(G)^{1/2},$$ where $C_{2.0.4}(a,q,n)$ is the nonnegative real constant `C2_0_4 a q n` (the constant used in `forest_operator`) and the division is in $[0,\infty]$.

### `lintegral_carlesonSum_forest'`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : Measurable f) (h2f : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (⋃ u ∈ 𝔘₄ k n j l, 𝔗₂ k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * 2 ^ (↑a + 5 / 2) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {k n j l : ℕ} {f : X → ℂ}, Measurable f → (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (⋃ (u : 𝔓 X), ⋃ (_ : Membership.mem (γ := Set (𝔓 X)) (𝔘₄ (F := F) (G := G) k n j l) u), 𝔗₂ (F := F) (G := G) k n j u) f x‖ₑ ≤ ↑(C2_0_4 a q n) * (2 : ENNReal) ^ (↑a + (5 / 2 : ℝ)) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹`
Docstring: For each forest, the integral of the norm of the Carleson sum can be controlled thanks to the forest theorem and to the density control coming from the fact we are away from `G₁`. Second version, with the volume of `F`.
English: Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \to X \to \mathbb{C}$ a function, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ subsets. Assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common through most of chapters 2-7 of the blueprint); through its `KernelProofData` component it equips $X$ with a doubling-measure structure `DoublingMeasure X (2^a)`, hence with a measure, denoted $\mu$ (the `volume` of $X$), and it provides $Q$ (`ProofData.Q`), a simple function from $X$ to the type $\Theta(X)$ of functions of the `FunctionDistances` structure. Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` (a natural number determined by the `ProofData`) and $o = $ `cancelPt X` (the point $o$ of the blueprint). Write $\mathfrak{P}$ for the (finite) type `𝔓 X` of tiles of this tile structure. For a set $\mathfrak{C} \subseteq \mathfrak{P}$, a function $g : X \to \mathbb{C}$ and $x \in X$, write $T_{\mathfrak{C}} g(x) = $ `carlesonSum ℭ g x` $= \sum_{p \in \mathfrak{C}} T_p g(x)$, where $T_p$ is the project operator `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2). Let $G' = G_1 \cup G_2 \cup G_3 \subseteq X$ be the project set `G'`, where $G_1, G_2, G_3$ are the project sets `G₁`, `G₂`, `G₃` (defined in (5.1.25), (5.1.27), (5.1.28) of the blueprint). For natural numbers $k, n, j, l$, let $\mathfrak{F}_{k,n,j,l} = \bigcup_{u \in \mathfrak{U}_4(k,n,j,l)} \mathfrak{T}_2(k,n,j,u) \subseteq \mathfrak{P}$, where $\mathfrak{U}_4(k,n,j,l)$ is the project set `𝔘₄ k n j l` (by its docstring, a union of $2^n$ disjoint subfamilies of $\mathfrak{U}_3(k,n,j)$ = `𝔘₃ k n j`) and $\mathfrak{T}_2(k,n,j,u)$ is the project set `𝔗₂ k n j u` (the subset $\mathfrak{T}_2(u)$ of $\mathfrak{C}_6(k,n,j)$ given in (5.4.5)). Let $k, n, j, l$ be natural numbers and let $f : X \to \mathbb{C}$ be a measurable function with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Integrals below are lower Lebesgue integrals, with respect to $\mu$, of the extended nonnegative real norm $\|\cdot\|_e$, and all quantities on the right-hand side are computed in $[0,\infty]$. Then $$\int^{-}_{G \setminus G'} \|T_{\mathfrak{F}_{k,n,j,l}} f(x)\|_e \, d\mu(x) \le C_{2.0.4}(a,q,n)\, 2^{a + 5/2}\, \mu(G)^{1 - q^{-1}}\, \mu(F)^{q^{-1}},$$ where $C_{2.0.4}(a,q,n)$ is the nonnegative real constant `C2_0_4 a q n` (the constant used in `forest_operator`).

### `forest_union_optimized`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ f x‖ₑ ≤ ↑(C5_1_2_optimized a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {f : X → ℂ}, (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable f → ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (𝔓₁ (F := F) (G := G)) f x‖ₑ ≤ ↑(C5_1_2_optimized a (nnq X (F := F) (G := G))) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹`
Docstring: Version of the forest union result with a better constant.
English: Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \to X \to \mathbb{C}$ a function, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ subsets. Assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common through most of chapters 2-7 of the blueprint); through its `KernelProofData` component it equips $X$ with a doubling-measure structure `DoublingMeasure X (2^a)`, hence with a measure, denoted $\mu$ (the `volume` of $X$), and it provides $Q$ (`ProofData.Q`), a simple function from $X$ to the type $\Theta(X)$ of functions of the `FunctionDistances` structure. Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` (a natural number determined by the `ProofData`) and $o = $ `cancelPt X` (the point $o$ of the blueprint). Write $\mathfrak{P}$ for the (finite) type `𝔓 X` of tiles of this tile structure. For a set $\mathfrak{C} \subseteq \mathfrak{P}$, a function $g : X \to \mathbb{C}$ and $x \in X$, write $T_{\mathfrak{C}} g(x) = $ `carlesonSum ℭ g x` $= \sum_{p \in \mathfrak{C}} T_p g(x)$, where $T_p$ is the project operator `carlesonOn p` (the operator $T_{\mathfrak{p}}$ of Proposition 2.0.2). Let $G' = G_1 \cup G_2 \cup G_3 \subseteq X$ be the project set `G'`, where $G_1, G_2, G_3$ are the project sets `G₁`, `G₂`, `G₃` (defined in (5.1.25), (5.1.27), (5.1.28) of the blueprint). Let $\mathfrak{P}_1 = $ `𝔓₁` $= \bigcup_{n \in \mathbb{N}} \bigcup_{k \le n} \bigcup_{j \le 2n+3} \mathfrak{C}_5(k,n,j)$, where $\mathfrak{C}_5(k,n,j)$ is the project set of tiles `ℭ₅ k n j`. Let $\tilde q$ denote $q$ regarded as a nonnegative real number (the project's `nnq X`). Let $f : X \to \mathbb{C}$ be a measurable function with $\|f(x)\| \le \mathbf{1}_F(x)$ for all $x \in X$. Integrals below are lower Lebesgue integrals, with respect to $\mu$, of the extended nonnegative real norm $\|\cdot\|_e$, and all quantities on the right-hand side are computed in $[0,\infty]$. Then $$\int^{-}_{G \setminus G'} \|T_{\mathfrak{P}_1} f(x)\|_e \, d\mu(x) \le C^{\mathrm{opt}}(a, \tilde q)\, \mu(G)^{1 - q^{-1}}\, \mu(F)^{q^{-1}},$$ where $C^{\mathrm{opt}}(a,\tilde q) = C^{\mathrm{base}}_{2.0.4}(a) \cdot 2^{a + 5/2} \cdot 13009 / (\tilde q - 1)^4$ is the nonnegative real constant `C5_1_2_optimized a (nnq X)`, with $C^{\mathrm{base}}_{2.0.4}(a)$ the nonnegative real constant `C2_0_4_base a` and truncated subtraction in $\mathbb{R}_{\ge 0}$.
