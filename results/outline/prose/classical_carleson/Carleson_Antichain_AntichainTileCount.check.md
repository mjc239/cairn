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

#### `FunctionDistances.Θ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → (X : Type u) → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → Type u`
Docstring: A type of continuous functions from `X` to `𝕜`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.1`

#### `KernelProofData.cf` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → {inst : PseudoMetricSpace X} → [self : KernelProofData a K] → CompatibleFunctions ℝ X (defaultA a)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {K : outParam (X → X → ℂ)} {inst : PseudoMetricSpace X} [self : KernelProofData a K] => self.3`

#### `KernelProofData.d` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → {inst : PseudoMetricSpace X} → [self : KernelProofData a K] → DoublingMeasure X ↑(defaultA a)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {K : outParam (X → X → ℂ)} {inst : PseudoMetricSpace X} [self : KernelProofData a K] => self.1`

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

#### `instPseudoMetricSpaceWithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → {x : X} → {r : ℝ} → PseudoMetricSpace (WithFunctionDistance x r)`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] {x : X} {r : ℝ} => FunctionDistances.metric x r`

#### `𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → (X : Type u) → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [PreTileStructure.{u, u_1, u_2} Q D κ S o] → Type u`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] (X : Type u) {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X`

#### `𝔠` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => c (𝓘 p)`

#### `𝔰` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → ℤ`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => s (𝓘 p)`

#### `Antichain.C6_1_6` (def)
Lean: `ℕ → NNReal`
Docstring: The constant appearing in Lemma 6.1.6.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ ((5 : ℕ) * a)`

#### `Antichain.p₆` (def)
Lean: `ℕ → ℝ`
Docstring: `p` in Lemma 6.1.6. We append a subscript `₆` to keep `p` available for tiles.
Definition: `fun (a : ℕ) => (4 : ℝ) * HPow.hPow (α := ℝ) ↑a (4 : ℕ)`

#### `E` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → Set X`
Docstring: The set `E` defined in Proposition 2.0.2.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) => {x : X | x ∈ 𝓘 p ∧ Membership.mem (α := @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) (Ω p) ((Q (F := F) (G := G)) x : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) ∧ 𝔰 p ∈ Set.Icc (σ₁ x) (σ₂ x)}`

#### `GridStructure.coeGrid` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → Set X`
Docstring: The collection of dyadic cubes
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.3`

#### `MeasureTheory.DoublingMeasure.toMeasureSpace` (def)
Lean: `{X : Type u_3} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → [self : DoublingMeasure X A] → MeasureSpace X`
Definition: `fun (X : Type u_3) {A : outParam NNReal} {inst : PseudoMetricSpace X} [self : DoublingMeasure X A] => self.3`

#### `PreTileStructure.toGridStructure` (def)
Lean: `(𝕜 : Type u_1) → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → GridStructure.{u_2, u} X D κ S o`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.1`

#### `dens₁` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ENNReal`
Docstring: This density is defined to live in `ℝ≥0∞`. Use `ENNReal.toReal` to get a real number.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔓' : Set (𝔓 X)) => ⨆ p' ∈ 𝔓', ⨆ (l : NNReal), ⨆ (_ : l ≥ (2 : NNReal)), HPow.hPow (β := ℝ) (↑l) (-↑a) * ⨆ p ∈ lowerCubes (F := F) (G := G) 𝔓', ⨆ (_ : smul (F := F) (G := G) (↑l) p' ≤ smul (F := F) (G := G) (↑l) p), HDiv.hDiv (α := ENNReal) (β := ENNReal) ((volume : Measure X) (E₂ (F := F) (G := G) (↑l) p) : ENNReal) ((volume : Measure X) ↑(𝓘 p) : ENNReal)`

#### `instFintype𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (𝔓.{u, u_1, u_2} X)`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.fintype_𝔓`

#### `instPartialOrder𝔓Real` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → PartialOrder (𝔓 X)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => PartialOrder.lift (toTileLike (F := F) (G := G)) ⋯`

#### `𝓘` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → Grid X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] => PreTileStructure.𝓘`

#### `Antichain.C6_3_4` (def)
Lean: `ℕ → ℕ → NNReal`
Docstring: The constant appearing in Lemma 6.3.4.
Definition: `fun (a N : ℕ) => (2 : NNReal) ^ ((𝕔 + (1 : ℕ)) * a ^ (3 : ℕ) + N * a)`

#### `Grid` (def)
Lean: `(X : Type u) → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [GridStructure X D κ S o] → Type u`
Docstring: The indexing type of the grid structure. Elements are called (dyadic) cubes. Note that this type has instances for both `≤` and `⊆`, but they do *not* coincide.
Definition: `fun (X : Type u) {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => @GridStructure.Grid X _ inst inst_1 _ _ _ _ _`

#### `instPartialOrderGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → PartialOrder (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => PartialOrder.lift (fun (i : @GridStructure.Grid X _ inst inst_1 _ _ _ _ _) => (↑i, GridStructure.s i)) ⋯`

#### `GridStructure` (structure or class)
Lean: `(X : Type u_2) → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [DoublingMeasure X A] → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (max (u + 1) u_2)`
Docstring: A grid structure on `X`. We prefer `coeGrid : Grid → Set X` over `Grid : Set (Set X)` Note: the `s` in this paper is `-s` of Christ's paper.
Constructor (every field with its type): `{X : Type u_2} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → (Grid : Type u) → Fintype Grid → (coeGrid : Grid → Set X) → (s : Grid → ℤ) → (c : Grid → X) → (Function.Injective.{u + 1, max 1 (u_2 + 1)} (β := Set X × ℤ) fun (i : Grid) => (coeGrid i, s i)) → Set.range s ⊆ Set.Icc (-↑S) ↑S → (topCube : Grid) → s topCube = ↑S → c topCube = o → (∀ {i : Grid}, coeGrid i ⊆ coeGrid topCube) → (∀ {i : Grid}, ∀ k ∈ Set.Ico (-↑S) (s i), coeGrid i ⊆ ⋃ j ∈ s ⁻¹' {k}, coeGrid j) → (∀ {i j : Grid}, s i ≤ s j → coeGrid i ⊆ coeGrid j ∨ Disjoint (coeGrid i) (coeGrid j)) → (∀ {i : Grid}, Metric.ball (c i) (HPow.hPow (α := ℝ) (↑D) (s i) / (4 : ℝ)) ⊆ coeGrid i) → (∀ {i : Grid}, coeGrid i ⊆ Metric.ball (c i) ((4 : ℝ) * HPow.hPow (α := ℝ) (↑D) (s i))) → (∀ {i : Grid} {t : NNReal}, HPow.hPow (α := NNReal) (↑D) (-↑S - s i) ≤ t → Measure.real.{u_2} (α := X) (m := MeasureSpace.toMeasurableSpace) volume {x : X | x ∈ coeGrid i ∧ Metric.infEDist x (coeGrid i)ᶜ ≤ ↑t * HPow.hPow (α := ENNReal) (↑D) (s i)} ≤ (2 : ℝ) * ↑t ^ κ * Measure.real (m := MeasureSpace.toMeasurableSpace) volume (coeGrid i)) → (∀ {i : Grid}, MeasurableSet (coeGrid i)) → GridStructure.{u, u_2} X D κ S o`

#### `MeasureTheory.DoublingMeasure` (structure or class)
Lean: `(X : Type u_3) → outParam NNReal → [PseudoMetricSpace X] → Type u_3`
Docstring: A metric space with a measure with some nice properties, including a doubling condition. This is called a "doubling metric measure space" in the blueprint. `A` will usually be `2 ^ a`.
Constructor (every field with its type): `{X : Type u_3} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [toCompleteSpace : CompleteSpace X] → [toLocallyCompactSpace : LocallyCompactSpace X] → [toMeasureSpace : MeasureSpace X] → [toBorelSpace : BorelSpace X] → [toIsLocallyFiniteMeasure : IsLocallyFiniteMeasure.{u_3} (α := X) (m0 := MeasureSpace.toMeasurableSpace) volume] → [toIsDoubling : Measure.IsDoubling.{u_3} (X := X) volume A] → [toNeZero : NeZero.{u_3} (R := Measure X) volume] → DoublingMeasure X A`

#### `s` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Grid X → ℤ`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.s`

#### `TileStructure.Ω` (def)
Lean: `{X : Type u} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {inst_2 : FunctionDistances ℝ X} → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : TileStructure Q D κ S o] → PreTileStructure.𝔓 ℝ X → Set (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _)`
Definition: `fun (X : Type u) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {inst_2 : FunctionDistances ℝ X} {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : TileStructure Q D κ S o] => self.2`

#### `CoveredByBalls` (structure or class)
Lean: `{X : Type u_2} → [PseudoMetricSpace X] → Set X → ℕ → ℝ → Prop`
Docstring: `s` can be covered by at most `N` balls with radius `r`.
Constructor (every field with its type): `∀ {X : Type u_2} [inst : PseudoMetricSpace X] {s : Set X} {n : ℕ} {r : ℝ} (balls : Finset X), balls.card ≤ n → s ⊆ ⋃ x ∈ balls, Metric.ball x r → CoveredByBalls s n r`

#### `TileLike` (def)
Lean: `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Type u_1`
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => Grid X × (Set (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))ᵒᵈ`

#### `TileLike.fst` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → TileLike X (F := F) (G := G) → Grid X`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (x : TileLike X (F := F) (G := G)) => x.1`

#### `TileLike.snd` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → TileLike X (F := F) (G := G) → Set (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (x : TileLike X (F := F) (G := G)) => x.2`

#### `instPartialOrderTileLike` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → PartialOrder (TileLike X (F := F) (G := G))`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => { le := instPartialOrderTileLike._aux_1, lt := instPartialOrderTileLike._aux_3, le_refl := ⋯, le_trans := ⋯, lt_iff_le_not_ge := ⋯, le_antisymm := ⋯ }`

#### `smul` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℝ → 𝔓 X → TileLike X (F := F) (G := G)`
Docstring: This is not defined as such in the blueprint, but `λp ≲ λ'p'` can be written using `smul l p ≤ smul l' p'`. Beware: `smul 1 p` is very different from `toTileLike p`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (l : ℝ) (p : 𝔓 X) => (𝓘 p, ball_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) l)`

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

#### `GridStructure.Grid` (def)
Lean: `(X : Type u_2) → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → Type u`
Docstring: indexing set for a grid structure
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.1`

#### `PreTileStructure.𝓘` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X → @GridStructure.Grid X _ inst_1 inst_2 _ _ _ _ _`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.4`

#### `FunctionDistances.coeΘ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → @Θ _ X inst inst_1 _ → C(X, 𝕜)`
Docstring: The coercion map from `Θ` to `C(X, 𝕜)`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.2`

#### `𝕔` (def)
Lean: `ℕ`
Docstring: The main constant in the blueprint, driving all the construction, is `D = 2 ^ (100 * a ^ 2)`. It turns out that the proof is robust, and works for other values of `100`, giving better constants in the end. We will formalize it using a parameter `𝕔` (that we fix equal to `100` to follow the blueprint) and having `D = 2 ^ (𝕔 * a ^ 2)`. We register two lemmas `seven_le_c` and `c_le_100` and will never unfold `𝕔` from this point on.
Definition: `wrapped✝.1`

#### `FunctionDistances.metric` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → X → ℝ → PseudoMetricSpace (@Θ _ X inst inst_1 _)`
Docstring: For each `_x : X` and `_r : ℝ`, a `PseudoMetricSpace Θ`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.4`

#### `c` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Grid X → X`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.c`

#### `instMembershipGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Membership X (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => { mem := fun (i : Grid X) (x : X) => x ∈ ↑i }`

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

#### `PreTileStructure.fintype_𝔓` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X)`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.3`

#### `toTileLike` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → TileLike X (F := F) (G := G)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) => (𝓘 p, Ω p)`

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

#### `AllBallsCoverBalls` (def)
Lean: `(X : Type u_2) → [PseudoMetricSpace X] → ℝ → ℕ → Prop`
Docstring: For all `r`, balls of radius `r` in `X` are covered by `n` balls of radius `a * r`
Definition: `fun (X : Type u_2) [PseudoMetricSpace X] (a : ℝ) (n : ℕ) => ∀ (r : ℝ), BallsCoverBalls X (a * r) r n`

#### `localOscillation` (def)
Lean: `{𝕜 : Type u_3} → {X : Type u_4} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → Set X → C(X, 𝕜) → C(X, 𝕜) → ENNReal`
Docstring: The local oscillation of two functions w.r.t. a set `E`. This is `d_E` in the blueprint.
Definition: `fun {𝕜 : Type u_3} {X : Type u_4} [RCLike 𝕜] [PseudoMetricSpace X] (E : Set X) (f g : C(X, 𝕜)) => ⨆ z ∈ E ×ˢ E, ENNReal.ofReal ‖HAdd.hAdd (β := 𝕜) (HSub.hSub (β := 𝕜) (HSub.hSub (α := 𝕜) (β := 𝕜) (f z.1 : 𝕜) (g z.1 : 𝕜)) (f z.2 : 𝕜)) (g z.2 : 𝕜)‖`

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

#### `TileLike.toSet` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → TileLike X (F := F) (G := G) → Set X`
Docstring: From a TileLike, we can construct a set. This is used in the definitions `E₁` and `E₂`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (t : TileLike X (F := F) (G := G)) => ↑(t.fst (F := F) (G := G)) ∩ G ∩ ⇑(Q (F := F) (G := G)) ⁻¹' t.snd (F := F) (G := G)`

## Translations

### `Antichain.𝔄_aux`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : Θ X) (N : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _ → ℕ → Set (𝔓 X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) (N : ℕ) => {p : 𝔓 X | p ∈ 𝔄 ∧ (1 : ℝ) + dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) ϑ ∈ Set.Ico ((2 : ℝ) ^ N) ((2 : ℝ) ^ (N + (1 : ℕ)))}`
Docstring: Def 6.3.15.
English: Let $X$ be a metric space satisfying the standing assumptions `ProofData a q K σ₁ σ₂ F G` (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and equipped with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`. For a set of tiles $\mathfrak{A} \subseteq \mathfrak{P}(X)$, an element $\vartheta \in \Theta(X)$ and a natural number $N$, `𝔄_aux 𝔄 ϑ N` is a set of tiles in $\mathfrak{P}(X)$; according to its docstring, this is Definition 6.3.15.

### `Antichain.tile_count`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (ϑ : ↑(Set.range ⇑Q)) : eLpNorm (fun x => ∑ p with p ∈ 𝔄, (1 + edist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) ↑ϑ) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) * (E p).indicator 1 x * G.indicator 1 x) (ENNReal.ofReal (p₆ a)) volume ≤ ↑(C6_1_6 a) * dens₁ 𝔄 ^ (p₆ a)⁻¹ * volume (⋃ p ∈ 𝔄, ↑(𝓘 p)) ^ (p₆ a)⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {𝔄 : Set (𝔓 X)}, IsAntichain (fun (x1 x2 : 𝔓 X) => x1 ≤ x2) 𝔄 → ∀ (ϑ : ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G)))), @eLpNorm _ ENNReal _ MeasureSpace.toMeasurableSpace (fun (x : X) => ∑ p : 𝔓 X with p ∈ 𝔄, ((1 : ENNReal) + edist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) ↑ϑ) ^ (-((2 : ℝ) * HPow.hPow (α := ℝ) ↑a (2 : ℕ) + HPow.hPow (α := ℝ) ↑a (3 : ℕ))⁻¹) * (E (F := F) (G := G) p).indicator (1 : X → ENNReal) x * G.indicator (1 : X → ENNReal) x) (ENNReal.ofReal (p₆ a)) volume ≤ ↑(C6_1_6 a) * dens₁ (F := F) (G := G) 𝔄 ^ (p₆ a)⁻¹ * HPow.hPow (α := ENNReal) ((volume : Measure X) (⋃ p ∈ 𝔄, ↑(𝓘 p)) : ENNReal) (p₆ a)⁻¹`
Docstring: Lemma 6.1.6.
English: (Lemma 6.1.6) Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \to X \to \mathbb{C}$ a function, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ subsets. Assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common through most of chapters 2-7 of the blueprint); through its `KernelProofData` component it equips $X$ with a doubling-measure structure `DoublingMeasure X (2^a)`, hence with a measure, denoted $\mu$ (the `volume` of $X$), and it provides $Q$ (`ProofData.Q`), a simple function from $X$ to the type $\Theta(X)$ of functions of the `FunctionDistances` structure. Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` (a natural number determined by the `ProofData`) and $o = $ `cancelPt X` (the point $o$ of the blueprint). Write $\mathfrak{P}$ for the (finite) type `𝔓 X` of tiles of this tile structure and `Grid X` for the type of grid cubes; each cube $I$ is regarded as a subset of $X$, and has a scale $s(I) \in \mathbb{Z}$ (`s I`). For a tile $t$, let $\mathcal{I}(t) = $ `𝓘 t` be its cube, $c(t) = $ `𝔠 t` $\in X$ the center of $\mathcal{I}(t)$, $s(t) = $ `𝔰 t` $= s(\mathcal{I}(t)) \in \mathbb{Z}$ its scale, and $\mathcal{Q}(t) = $ `𝒬 t` $\in \Theta(X)$ the element attached to $t$ by the tile structure. For $x \in X$ and $r \in \mathbb{R}$, let $d_{x,r}$ be the pseudometric on $\Theta(X)$ provided by the `FunctionDistances` structure for the ball of center $x$ and radius $r$ (and $d^e_{x,r}$ its extended, $[0,\infty]$-valued version); write $d_t = d_{c(t),\, D^{s(t)}/4}$ for a tile $t$, with $D$ regarded as a real number. Tiles are compared by the project's partial order `≤` on $\mathfrak{P}$. For a tile $t$, let $E(t) = \{x \in \mathcal{I}(t) : Q(x) \in \Omega(t),\ \sigma_1(x) \le s(t) \le \sigma_2(x)\}$ (the project set `E t`), where $\Omega(t) \subseteq \Theta(X)$ is the set `Ω t` of the tile structure. For a set of tiles $\mathfrak{A} \subseteq \mathfrak{P}$, let $\operatorname{dens}_1(\mathfrak{A}) \in [0,\infty]$ be the project density `dens₁ 𝔄`. Let $p_6 = 4a^4$ (the real number `p₆ a`) and $C_{6.1.6}(a) = 2^{5a}$ (the nonnegative real `C6_1_6 a`). Let $\mathfrak{A} \subseteq \mathfrak{P}$ be an antichain for $\le$, and let $\vartheta \in \Theta(X)$ lie in the range of $Q$. Define $g : X \to [0,\infty]$ by $$g(x) = \sum_{t \in \mathfrak{A}} \big(1 + d^e_t(\mathcal{Q}(t), \vartheta)\big)^{-1/(2a^2 + a^3)}\, \mathbf{1}_{E(t)}(x)\, \mathbf{1}_G(x).$$ Then $$\|g\|_{L^{p_6}(\mu)} \le C_{6.1.6}(a)\, \operatorname{dens}_1(\mathfrak{A})^{1/p_6}\, \mu\Big(\bigcup_{t \in \mathfrak{A}} \mathcal{I}(t)\Big)^{1/p_6},$$ where the $L^{p_6}$ norm is taken with exponent $p_6$ regarded as an element of $[0,\infty]$ and all quantities are in $[0,\infty]$.

### `Antichain.global_antichain_density`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h𝔄 : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : ∑ p ∈ (𝔄_aux 𝔄 (↑ϑ) N).toFinset, volume (E p ∩ G) ≤ ↑(C6_3_4 a N) * dens₁ 𝔄 * volume (⋃ p ∈ 𝔄, ↑(𝓘 p))`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {𝔄 : Set (𝔓 X)}, IsAntichain (fun (x1 x2 : 𝔓 X) => x1 ≤ x2) 𝔄 → ∀ (ϑ : ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G)))) (N : ℕ), ∑ p ∈ (𝔄_aux (F := F) (G := G) 𝔄 (↑ϑ) N).toFinset, (volume : Measure X) (E (F := F) (G := G) p ∩ G) ≤ HMul.hMul (β := ENNReal) (↑(C6_3_4 a N) * dens₁ (F := F) (G := G) 𝔄) ((volume : Measure X) (⋃ p ∈ 𝔄, ↑(𝓘 p)) : ENNReal)`
Docstring: Lemma 6.3.4.
English: (Lemma 6.3.4) Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \times X \to \mathbb{C}$ a function, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ subsets. Assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7, except 3). Through its `KernelProofData` component this equips $X$ with a doubling measure structure `DoublingMeasure X (2^a)` (with $2^a$ = `defaultA a`), hence with a measure $\mu$ (the `volume` of $X$), and with a `CompatibleFunctions ℝ X (2^a)` structure, hence a `FunctionDistances ℝ X` structure with its type $\Theta(X)$ (docstring: a type of continuous functions from $X$ to $\mathbb{R}$); the `ProofData` also provides $Q$ = `ProofData.Q`, a simple function from $X$ to $\Theta(X)$. Let $D$ = `defaultD a` $= 2^{𝕔 a^2}$, where $𝕔$ is the project's fixed natural-number constant `𝕔`; let $\kappa$ = `defaultκ a` $= 2^{-10a}$; let $S$ = `defaultS X`, the least natural number $n > 0$ such that $-n \le \sigma_1(x)$ and $\sigma_2(x) \le n$ for all $x \in X$ and $F$ and $G$ are both contained in the open ball of center $o$ and radius $D^n/4$; and let $o$ = `cancelPt X` (docstring: the point $o$ of the blueprint), a chosen point of $X$ at which every element of $\Theta(X)$ vanishes. Assume a tile structure `TileStructure Q D κ S o` on $X$. Let $\mathfrak{P}$ = `𝔓 X` be its (finite) type of tiles, and `Grid X` the type of cubes of the underlying grid structure; each cube $I$ is identified with a subset of $X$ (so we write $\mu(I)$), and has a scale $s(I) \in \mathbb{Z}$ (`s I`) and a center $c(I) \in X$. Cubes are ordered by the project partial order on `Grid X`: $I \le J$ iff $I \subseteq J$ as subsets of $X$ and $s(I) \le s(J)$. For a tile $p$, let $\mathcal{I}(p)$ = `𝓘 p` be its cube, $\mathfrak{c}(p)$ = `𝔠 p` $= c(\mathcal{I}(p))$, $\mathfrak{s}(p)$ = `𝔰 p` $= s(\mathcal{I}(p))$, $\mathcal{Q}(p)$ = `𝒬 p` $\in \Theta(X)$ and $\Omega(p)$ = `Ω p` $\subseteq \Theta(X)$ the element and the set attached to $p$ by the tile structure. For $x \in X$ and $r \in \mathbb{R}$, let $d_{x,r}$ be the pseudometric on $\Theta(X)$ given by the `FunctionDistances` structure for center $x$ and radius $r$ (the pseudometric of `WithFunctionDistance x r`). For a tile $p$, let $E(p)$ = `E p` $= \{x \in X : x \in \mathcal{I}(p),\ Q(x) \in \Omega(p),\ \sigma_1(x) \le \mathfrak{s}(p) \le \sigma_2(x)\}$. For a set of tiles $\mathfrak{A} \subseteq \mathfrak{P}$, let $\operatorname{dens}_1(\mathfrak{A}) \in [0,\infty]$ be the project density `dens₁ 𝔄`. For $\mathfrak{A} \subseteq \mathfrak{P}$, $\vartheta \in \Theta(X)$ and $N \in \mathbb{N}$, let $\mathfrak{A}_{\vartheta,N}$ = `𝔄_aux 𝔄 ϑ N` (Def. 6.3.15) be the set of tiles $p \in \mathfrak{A}$ with $2^N \le 1 + d_{\mathfrak{c}(p),\, D^{\mathfrak{s}(p)}/4}(\mathcal{Q}(p), \vartheta) < 2^{N+1}$ (here $D$ is regarded as a real number). Tiles are compared by the project partial order $\le$ on $\mathfrak{P}$, obtained by pulling back, along $p \mapsto (\mathcal{I}(p), \Omega(p))$ (`toTileLike`), the project partial order on `TileLike X` = `Grid X` $\times$ (sets of $\Theta(X)$ with the order dual). Let $\mathfrak{A} \subseteq \mathfrak{P}$ be an antichain for $\le$, let $\vartheta \in \Theta(X)$ lie in the range of $Q$, and let $N$ be a natural number. Then $$\sum_{p \in \mathfrak{A}_{\vartheta,N}} \mu(E(p) \cap G) \le C_{6.3.4}(a,N)\, \operatorname{dens}_1(\mathfrak{A})\, \mu\Big(\bigcup_{p \in \mathfrak{A}} \mathcal{I}(p)\Big)$$ in $[0,\infty]$, where $C_{6.3.4}(a,N)$ = `C6_3_4 a N` $= 2^{(𝕔+1)a^3 + Na}$, a nonnegative real number.

### `Antichain.𝔄'`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G))) → ℕ → Set (𝔓 X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G)))) (N : ℕ) => {p : 𝔓 X | p ∈ 𝔄_aux (F := F) (G := G) 𝔄 (↑ϑ) N ∧ ↑(𝓘 p) ∩ G ≠ ∅ ∧ 𝔰 p > -↑(defaultS X (F := F) (G := G))}`
Docstring: The set `𝔄'` defined in Lemma 6.3.4.
English: Let $X$ be a metric space satisfying the standing assumptions `ProofData a q K σ₁ σ₂ F G` (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and equipped with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`. For a set of tiles $\mathfrak{A} \subseteq \mathfrak{P}(X)$, an element $\vartheta$ of the range of $Q$ and a natural number $N$, `𝔄' 𝔄 ϑ N` is a set of tiles in $\mathfrak{P}(X)$; according to its docstring, it is the set $\mathfrak{A}'$ defined in Lemma 6.3.4.

### `Antichain.𝓛`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : Set (Grid X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G))) → ℕ → Set (Grid X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G)))) (N : ℕ) => {I : Grid X | (∃ (p : ↑(𝔄' (F := F) (G := G) 𝔄 ϑ N)), I ≤ 𝓘 ↑p) ∧ ∀ (p : ↑(𝔄' (F := F) (G := G) 𝔄 ϑ N)), 𝓘 ↑p ≤ I → 𝔰 ↑p = -↑(defaultS X (F := F) (G := G))}`
Docstring: The set `𝓛` defined in Lemma 6.3.4.
English: Let $X$ be a metric space satisfying the standing assumptions `ProofData a q K σ₁ σ₂ F G` (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and equipped with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`. For a set of tiles $\mathfrak{A} \subseteq \mathfrak{P}(X)$, an element $\vartheta$ of the range of $Q$ and a natural number $N$, `𝓛 𝔄 ϑ N` is a set of grid cubes (a subset of `Grid X`); according to its docstring, it is the set $\mathcal{L}$ defined in Lemma 6.3.4.

### `Antichain.𝓛'`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range ⇑Q)) (N : ℕ) : Set (Grid X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G))) → ℕ → Set (Grid X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G)))) (N : ℕ) => {I : Grid X | Maximal (fun (x : Grid X) => x ∈ 𝓛 (F := F) (G := G) 𝔄 ϑ N) I}`
Docstring: The set `𝓛*` defined in Lemma 6.3.4.
English: Let $X$ be a metric space satisfying the standing assumptions `ProofData a q K σ₁ σ₂ F G` (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and equipped with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`. For a set of tiles $\mathfrak{A} \subseteq \mathfrak{P}(X)$, an element $\vartheta$ of the range of $Q$ and a natural number $N$, `𝓛' 𝔄 ϑ N` is a set of grid cubes (a subset of `Grid X`); according to its docstring, it is the set $\mathcal{L}^*$ defined in Lemma 6.3.4.

### `Antichain.exists_larger_grid`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hL : L ∈ 𝓛' 𝔄 ϑ N) : ∃ L', L ≤ L' ∧ s L' = s L + 1`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {𝔄 : Set (𝔓 X)} {ϑ : ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G)))} {N : ℕ} {L : Grid X}, L ∈ 𝓛' (F := F) (G := G) 𝔄 ϑ N → ∃ (L' : Grid X), L ≤ L' ∧ s L' = s L + (1 : ℤ)`
English: Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \times X \to \mathbb{C}$ a function, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ subsets. Assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7, except 3). Through its `KernelProofData` component this equips $X$ with a doubling measure structure `DoublingMeasure X (2^a)` (with $2^a$ = `defaultA a`), hence with a measure $\mu$ (the `volume` of $X$), and with a `CompatibleFunctions ℝ X (2^a)` structure, hence a `FunctionDistances ℝ X` structure with its type $\Theta(X)$ (docstring: a type of continuous functions from $X$ to $\mathbb{R}$); the `ProofData` also provides $Q$ = `ProofData.Q`, a simple function from $X$ to $\Theta(X)$. Let $D$ = `defaultD a` $= 2^{𝕔 a^2}$, where $𝕔$ is the project's fixed natural-number constant `𝕔`; let $\kappa$ = `defaultκ a` $= 2^{-10a}$; let $S$ = `defaultS X`, the least natural number $n > 0$ such that $-n \le \sigma_1(x)$ and $\sigma_2(x) \le n$ for all $x \in X$ and $F$ and $G$ are both contained in the open ball of center $o$ and radius $D^n/4$; and let $o$ = `cancelPt X` (docstring: the point $o$ of the blueprint), a chosen point of $X$ at which every element of $\Theta(X)$ vanishes. Assume a tile structure `TileStructure Q D κ S o` on $X$. Let $\mathfrak{P}$ = `𝔓 X` be its (finite) type of tiles, and `Grid X` the type of cubes of the underlying grid structure; each cube $I$ is identified with a subset of $X$ (so we write $\mu(I)$), and has a scale $s(I) \in \mathbb{Z}$ (`s I`) and a center $c(I) \in X$. Cubes are ordered by the project partial order on `Grid X`: $I \le J$ iff $I \subseteq J$ as subsets of $X$ and $s(I) \le s(J)$. For a tile $p$, let $\mathcal{I}(p)$ = `𝓘 p` be its cube, $\mathfrak{c}(p)$ = `𝔠 p` $= c(\mathcal{I}(p))$, $\mathfrak{s}(p)$ = `𝔰 p` $= s(\mathcal{I}(p))$, $\mathcal{Q}(p)$ = `𝒬 p` $\in \Theta(X)$ and $\Omega(p)$ = `Ω p` $\subseteq \Theta(X)$ the element and the set attached to $p$ by the tile structure. Let $\mathfrak{A} \subseteq \mathfrak{P}$ be a set of tiles, let $\vartheta \in \Theta(X)$ lie in the range of $Q$, and let $N$ be a natural number. Let $\mathfrak{A}'$ = `𝔄' 𝔄 ϑ N` be the project set of tiles of that name. Let $\mathcal{L}(\mathfrak{A},\vartheta,N)$ = `𝓛 𝔄 ϑ N` (the set $\mathcal{L}$ of Lemma 6.3.4) be the set of cubes $I$ in `Grid X` such that $I \le \mathcal{I}(p)$ for some $p \in \mathfrak{A}'$, and such that every $p \in \mathfrak{A}'$ with $\mathcal{I}(p) \le I$ has $\mathfrak{s}(p) = -S$. Let $\mathcal{L}^*(\mathfrak{A},\vartheta,N)$ = `𝓛' 𝔄 ϑ N` (the set $\mathcal{L}^*$ of Lemma 6.3.4) be the set of maximal elements of $\mathcal{L}(\mathfrak{A},\vartheta,N)$ for $\le$, i.e. cubes $I \in \mathcal{L}(\mathfrak{A},\vartheta,N)$ such that every $J \in \mathcal{L}(\mathfrak{A},\vartheta,N)$ with $I \le J$ satisfies $J \le I$. Let $L$ be a cube in `Grid X` with $L \in \mathcal{L}^*(\mathfrak{A},\vartheta,N)$. Then there exists a cube $L'$ in `Grid X` with $L \le L'$ and $s(L') = s(L) + 1$.

### `Antichain.L'`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hL : L ∈ 𝓛' 𝔄 ϑ N) : Grid X`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {𝔄 : Set (𝔓 X)} → {ϑ : ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G)))} → {N : ℕ} → {L : Grid X} → L ∈ 𝓛' (F := F) (G := G) 𝔄 ϑ N → Grid X`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {𝔄 : Set (𝔓 X)} {ϑ : ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G)))} {N : ℕ} {L : Grid X} (hL : L ∈ 𝓛' (F := F) (G := G) 𝔄 ϑ N) => ⋯.choose (p := fun (L' : Grid X) => L ≤ L' ∧ s L' = s L + (1 : ℤ))`
Docstring: The `L'` introduced in the proof of Lemma 6.3.4.
English: Let $X$ be a metric space satisfying the standing assumptions `ProofData a q K σ₁ σ₂ F G` (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and equipped with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`. Let $\mathfrak{A} \subseteq \mathfrak{P}(X)$ be a set of tiles, $\vartheta$ an element of the range of $Q$, $N \in \mathbb{N}$, and $L \in \mathcal{L}^*(\mathfrak{A}, \vartheta, N)$ (i.e. $L$ in `𝓛' 𝔄 ϑ N`), a grid cube. Then `L' hL` is a grid cube in `Grid X`; according to its docstring, it is the cube $L'$ introduced in the proof of Lemma 6.3.4.

### `Antichain.p''`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hL : L ∈ 𝓛' 𝔄 ϑ N) : 𝔓 X`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {𝔄 : Set (𝔓 X)} → {ϑ : ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G)))} → {N : ℕ} → {L : Grid X} → L ∈ 𝓛' (F := F) (G := G) 𝔄 ϑ N → 𝔓 X`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {𝔄 : Set (𝔓 X)} {ϑ : ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G)))} {N : ℕ} {L : Grid X} (hL : L ∈ 𝓛' (F := F) (G := G) 𝔄 ϑ N) => ⋯.choose (p := fun (p : 𝔓 X) => p ∈ 𝔄' (F := F) (G := G) 𝔄 ϑ N ∧ 𝓘 p ≤ L' (F := F) (G := G) (𝔄 := 𝔄) hL)`
Docstring: p'' in the blueprint
English: Let $X$ be a metric space satisfying the standing assumptions `ProofData a q K σ₁ σ₂ F G` (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and equipped with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`. Let $\mathfrak{A} \subseteq \mathfrak{P}(X)$ be a set of tiles, $\vartheta$ an element of the range of $Q$, $N \in \mathbb{N}$, and $L \in \mathcal{L}^*(\mathfrak{A}, \vartheta, N)$ (i.e. $L$ in `𝓛' 𝔄 ϑ N`), a grid cube. Then `p'' hL` is a tile in $\mathfrak{P}(X)$; according to its docstring, it is the tile $p''$ of the blueprint.

### `Antichain.pΘ`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hL : L ∈ 𝓛' 𝔄 ϑ N) : 𝔓 X`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → {𝔄 : Set (𝔓 X)} → {ϑ : ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G)))} → {N : ℕ} → {L : Grid X} → L ∈ 𝓛' (F := F) (G := G) 𝔄 ϑ N → 𝔓 X`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {𝔄 : Set (𝔓 X)} {ϑ : ↑(Set.range (ι := X) ⇑(Q (F := F) (G := G)))} {N : ℕ} {L : Grid X} (hL : L ∈ 𝓛' (F := F) (G := G) 𝔄 ϑ N) => if 𝓘 (p'' (F := F) (G := G) (𝔄 := 𝔄) hL) = L' (F := F) (G := G) (𝔄 := 𝔄) hL then p'' (F := F) (G := G) (𝔄 := 𝔄) hL else Exists.choose (p := fun (x : 𝔓 X) => (fun (p : 𝔓 X) => 𝓘 p = L' (F := F) (G := G) (𝔄 := 𝔄) hL ∧ ↑ϑ ∈ Ω p) x ∧ ∀ (y : 𝔓 X), 𝓘 y = L' (F := F) (G := G) (𝔄 := 𝔄) hL ∧ ↑ϑ ∈ Ω y → y = x) ⋯`
Docstring: p_Θ in the blueprint
English: Let $X$ be a metric space satisfying the standing assumptions `ProofData a q K σ₁ σ₂ F G` (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and equipped with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`. Let $\mathfrak{A} \subseteq \mathfrak{P}(X)$ be a set of tiles, $\vartheta$ an element of the range of $Q$, $N \in \mathbb{N}$, and $L \in \mathcal{L}^*(\mathfrak{A}, \vartheta, N)$ (i.e. $L$ in `𝓛' 𝔄 ϑ N`), a grid cube. Then `pΘ hL` is a tile in $\mathfrak{P}(X)$; according to its docstring, it is the tile $p_\Theta$ of the blueprint.

### `Antichain.stack_density`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : Θ X) (N : ℕ) (L : Grid X) : ∑ p ∈ (𝔄_aux 𝔄 ϑ N).toFinset with 𝓘 p = L, volume (E p ∩ G) ≤ 2 ^ (a * (N + 5)) * dens₁ 𝔄 * volume ↑L`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔄 : Set (𝔓 X)) (ϑ : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) (N : ℕ) (L : Grid X), ∑ p ∈ (𝔄_aux (F := F) (G := G) 𝔄 ϑ N).toFinset with 𝓘 p = L, (volume : Measure X) (E (F := F) (G := G) p ∩ G) ≤ HMul.hMul (β := ENNReal) ((2 : ENNReal) ^ (a * (N + (5 : ℕ))) * dens₁ (F := F) (G := G) 𝔄) ((volume : Measure X) ↑L : ENNReal)`
Docstring: Lemma 6.3.2.
English: (Lemma 6.3.2) Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \times X \to \mathbb{C}$ a function, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ subsets. Assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7, except 3). Through its `KernelProofData` component this equips $X$ with a doubling measure structure `DoublingMeasure X (2^a)` (with $2^a$ = `defaultA a`), hence with a measure $\mu$ (the `volume` of $X$), and with a `CompatibleFunctions ℝ X (2^a)` structure, hence a `FunctionDistances ℝ X` structure with its type $\Theta(X)$ (docstring: a type of continuous functions from $X$ to $\mathbb{R}$); the `ProofData` also provides $Q$ = `ProofData.Q`, a simple function from $X$ to $\Theta(X)$. Let $D$ = `defaultD a` $= 2^{𝕔 a^2}$, where $𝕔$ is the project's fixed natural-number constant `𝕔`; let $\kappa$ = `defaultκ a` $= 2^{-10a}$; let $S$ = `defaultS X`, the least natural number $n > 0$ such that $-n \le \sigma_1(x)$ and $\sigma_2(x) \le n$ for all $x \in X$ and $F$ and $G$ are both contained in the open ball of center $o$ and radius $D^n/4$; and let $o$ = `cancelPt X` (docstring: the point $o$ of the blueprint), a chosen point of $X$ at which every element of $\Theta(X)$ vanishes. Assume a tile structure `TileStructure Q D κ S o` on $X$. Let $\mathfrak{P}$ = `𝔓 X` be its (finite) type of tiles, and `Grid X` the type of cubes of the underlying grid structure; each cube $I$ is identified with a subset of $X$ (so we write $\mu(I)$), and has a scale $s(I) \in \mathbb{Z}$ (`s I`) and a center $c(I) \in X$. Cubes are ordered by the project partial order on `Grid X`: $I \le J$ iff $I \subseteq J$ as subsets of $X$ and $s(I) \le s(J)$. For a tile $p$, let $\mathcal{I}(p)$ = `𝓘 p` be its cube, $\mathfrak{c}(p)$ = `𝔠 p` $= c(\mathcal{I}(p))$, $\mathfrak{s}(p)$ = `𝔰 p` $= s(\mathcal{I}(p))$, $\mathcal{Q}(p)$ = `𝒬 p` $\in \Theta(X)$ and $\Omega(p)$ = `Ω p` $\subseteq \Theta(X)$ the element and the set attached to $p$ by the tile structure. For $x \in X$ and $r \in \mathbb{R}$, let $d_{x,r}$ be the pseudometric on $\Theta(X)$ given by the `FunctionDistances` structure for center $x$ and radius $r$ (the pseudometric of `WithFunctionDistance x r`). For a tile $p$, let $E(p)$ = `E p` $= \{x \in X : x \in \mathcal{I}(p),\ Q(x) \in \Omega(p),\ \sigma_1(x) \le \mathfrak{s}(p) \le \sigma_2(x)\}$. For a set of tiles $\mathfrak{A} \subseteq \mathfrak{P}$, let $\operatorname{dens}_1(\mathfrak{A}) \in [0,\infty]$ be the project density `dens₁ 𝔄`. For $\mathfrak{A} \subseteq \mathfrak{P}$, $\vartheta \in \Theta(X)$ and $N \in \mathbb{N}$, let $\mathfrak{A}_{\vartheta,N}$ = `𝔄_aux 𝔄 ϑ N` (Def. 6.3.15) be the set of tiles $p \in \mathfrak{A}$ with $2^N \le 1 + d_{\mathfrak{c}(p),\, D^{\mathfrak{s}(p)}/4}(\mathcal{Q}(p), \vartheta) < 2^{N+1}$ (here $D$ is regarded as a real number). Let $\mathfrak{A} \subseteq \mathfrak{P}$ be any set of tiles, $\vartheta \in \Theta(X)$ any element, $N$ a natural number and $L$ a cube in `Grid X`. Then $$\sum_{p \in \mathfrak{A}_{\vartheta,N},\ \mathcal{I}(p) = L} \mu(E(p) \cap G) \le 2^{a(N+5)}\, \operatorname{dens}_1(\mathfrak{A})\, \mu(L)$$ in $[0,\infty]$.

### `Antichain.tile_reach`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hp : dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / 4} (𝒬 p) ϑ ≤ 2 ^ N) (hp' : dist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / 4} (𝒬 p') ϑ ≤ 2 ^ N) (hI : 𝓘 p ≤ 𝓘 p') (hs : 𝔰 p < 𝔰 p') : smul (2 ^ (N + 2)) p ≤ smul (2 ^ (N + 2)) p'`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {ϑ : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _} {N : ℕ} {p p' : 𝔓 X}, dist_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) ϑ ≤ (2 : ℝ) ^ N → dist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / (4 : ℝ)} (𝒬 p') ϑ ≤ (2 : ℝ) ^ N → 𝓘 p ≤ 𝓘 p' → 𝔰 p < 𝔰 p' → smul (F := F) (G := G) ((2 : ℝ) ^ (N + (2 : ℕ))) p ≤ smul (F := F) (G := G) ((2 : ℝ) ^ (N + (2 : ℕ))) p'`
Docstring: Lemma 6.3.1.
English: (Lemma 6.3.1) Let $X$ be a metric space, let $a$ be a natural number, $q$ a real number, $K : X \to X \to \mathbb{C}$ a function, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ functions and $F, G \subseteq X$ subsets. Assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common through most of chapters 2-7 of the blueprint); through its `KernelProofData` component it equips $X$ with a doubling-measure structure `DoublingMeasure X (2^a)`, hence with a measure, denoted $\mu$ (the `volume` of $X$), and it provides $Q$ (`ProofData.Q`), a simple function from $X$ to the type $\Theta(X)$ of functions of the `FunctionDistances` structure. Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{𝕔 a^2}$ (where $𝕔$ is the project's fixed natural-number constant `𝕔`), $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` (a natural number determined by the `ProofData`) and $o = $ `cancelPt X` (the point $o$ of the blueprint). Write $\mathfrak{P}$ for the (finite) type `𝔓 X` of tiles of this tile structure and `Grid X` for the type of grid cubes; each cube $I$ is regarded as a subset of $X$, and has a scale $s(I) \in \mathbb{Z}$ (`s I`). For a tile $t$, let $\mathcal{I}(t) = $ `𝓘 t` be its cube, $c(t) = $ `𝔠 t` $\in X$ the center of $\mathcal{I}(t)$, $s(t) = $ `𝔰 t` $= s(\mathcal{I}(t)) \in \mathbb{Z}$ its scale, and $\mathcal{Q}(t) = $ `𝒬 t` $\in \Theta(X)$ the element attached to $t$ by the tile structure. For $x \in X$ and $r \in \mathbb{R}$, let $d_{x,r}$ be the pseudometric on $\Theta(X)$ provided by the `FunctionDistances` structure for the ball of center $x$ and radius $r$ (and $d^e_{x,r}$ its extended, $[0,\infty]$-valued version); write $d_t = d_{c(t),\, D^{s(t)}/4}$ for a tile $t$, with $D$ regarded as a real number. Cubes are compared by the project's partial order on `Grid X`: $I \le J$ iff $I \subseteq J$ as subsets of $X$ and $s(I) \le s(J)$. For a real number $\lambda$ and a tile $t$, let $\lambda t$ denote `smul λ t`, the pair consisting of the cube $\mathcal{I}(t)$ and the ball $\{\vartheta' \in \Theta(X) : d_t(\mathcal{Q}(t), \vartheta') < \lambda\}$, an element of the project type `TileLike X` $= $ `Grid X` $\times$ (sets of $\Theta(X)$ with the reversed order), compared by the project's partial order on `TileLike X`. Let $\vartheta \in \Theta(X)$, let $N$ be a natural number, and let $p, p' \in \mathfrak{P}$ be tiles with $d_p(\mathcal{Q}(p), \vartheta) \le 2^N$, $d_{p'}(\mathcal{Q}(p'), \vartheta) \le 2^N$, $\mathcal{I}(p) \le \mathcal{I}(p')$ and $s(p) < s(p')$. Then $2^{N+2} p \le 2^{N+2} p'$.
