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
Stylistic choices are fine.

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
Fields: `1`, `2`, `Q`, `θ`, `ε₁`, `ε₂`, `α`, `_x`, `_x'`, `x1`, `x2`

#### `ProofData.Q` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {q : outParam ℝ} → {K : outParam (X → X → ℂ)} → {σ₁ σ₂ : outParam (X → ℤ)} → {F G : outParam (Set X)} → {inst : PseudoMetricSpace X} → [self : ProofData a q K σ₁ σ₂ F G] → SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {q : outParam ℝ} {K : outParam (X → X → ℂ)} {σ₁ σ₂ : outParam (X → ℤ)} {F G : outParam (Set X)} {inst : PseudoMetricSpace X} [self : ProofData a q K σ₁ σ₂ F G] => self.13`

#### `ProofData.toKernelProofData` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {q : outParam ℝ} → {K : outParam (X → X → ℂ)} → {σ₁ σ₂ : outParam (X → ℤ)} → {F G : outParam (Set X)} → {inst : PseudoMetricSpace X} → [self : ProofData a q K σ₁ σ₂ F G] → KernelProofData a K`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {q : outParam ℝ} {K : outParam (X → X → ℂ)} {σ₁ σ₂ : outParam (X → ℤ)} {F G : outParam (Set X)} {inst : PseudoMetricSpace X} [self : ProofData a q K σ₁ σ₂ F G] => self.1`

#### `Tile.C6_1_5` (def)
Lean: `ℕ → NNReal`
Docstring: The constant from lemma 6.1.5. Has value `2 ^ (232 * a ^ 3)` in the blueprint.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ (((2 : ℕ) * 𝕔 + (7 : ℕ) + 𝕔 / (4 : ℕ)) * a ^ (3 : ℕ))`

#### `TileStructure` (structure or class)
Lean: `{X : Type u} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → [inst_2 : FunctionDistances ℝ X] → outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _)) → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (u + 1)`
Docstring: A tile structure.
Fields: `Ω`, `ι`, `p`, `_`, `γ`, `4`, `5`, `1`

#### `TileStructure.toPreTileStructure` (def)
Lean: `{X : Type u} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {inst_2 : FunctionDistances ℝ X} → {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : TileStructure Q D κ S o] → PreTileStructure Q D κ S o`
Definition: `fun (X : Type u) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {inst_2 : FunctionDistances ℝ X} {Q : outParam (SimpleFunc X (@Θ _ X Real.normedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : TileStructure Q D κ S o] => self.1`

#### `WithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → X → ℝ → Type u_2`
Docstring: Class used to endow `Θ X` with a pseudometric space structure.
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] (x : X) (r : ℝ) => @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`

#### `adjointCarleson` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → (X → ℂ) → X → ℂ`
Docstring: The definition of `Tₚ*g(x)`, defined above Lemma 7.4.1
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) (x : X) => @integral _ _ _ _ MeasureSpace.toMeasurableSpace (Measure.restrict volume (E (F := F) (G := G) p)) fun (y : X) => HMul.hMul (α := ℂ) ((starRingEnd ℂ) (Ks (𝔰 p) y x) : ℂ) (Complex.exp (Complex.I * (↑(((Q (F := F) (G := G)) y : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y) - ↑(((Q (F := F) (G := G)) y : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) x)))) * f y`

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

#### `Tile.I12` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → 𝔓 X → (X → ℂ) → X → X → ENNReal`
Docstring: Definition (6.2.27).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p p' : 𝔓 X) (g : X → ℂ) (x1 x2 : X) => ‖(@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => Complex.exp (Complex.I * (-↑(((Q (F := F) (G := G)) x1 : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y) + ↑(((Q (F := F) (G := G)) x2 : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) y))) * Tile.correlation (F := F) (G := G) (𝔰 p') (𝔰 p) x1 x2 y) * g x1 * g x2‖ₑ`

#### `𝕔` (def)
Lean: `ℕ`
Docstring: The main constant in the blueprint, driving all the construction, is `D = 2 ^ (100 * a ^ 2)`. It turns out that the proof is robust, and works for other values of `100`, giving better constants in the end. We will formalize it using a parameter `𝕔` (that we fix equal to `100` to follow the blueprint) and having `D = 2 ^ (𝕔 * a ^ 2)`. We register two lemmas `seven_le_c` and `c_le_100` and will never unfold `𝕔` from this point on.
Definition: `wrapped✝.1`

#### `FunctionDistances.Θ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → (X : Type u) → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → Type u`
Docstring: A type of continuous functions from `X` to `𝕜`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.1`

#### `CompatibleFunctions` (structure or class)
Lean: `(𝕜 : outParam (Type u_3)) → (X : Type u) → outParam ℕ → [RCLike 𝕜] → [PseudoMetricSpace X] → Type (max (u + 1) u_3)`
Docstring: A set `Θ` of (continuous) functions is compatible. `A` will usually be `2 ^ a`.
Fields: `o`, `f`, `0`, `2`

#### `FunctionDistances` (structure or class)
Lean: `(𝕜 : outParam (Type u_1)) → (X : Type u) → [NormedField 𝕜] → [TopologicalSpace X] → Type (max (u + 1) u_1)`
Docstring: A class stating that continuous functions have distances associated to every ball. We use a separate type to conveniently index these functions.
Fields: `Θ`, `coeΘ`, `x`, `α`

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

#### `PreTileStructure` (structure or class)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : outParam NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → [inst_3 : FunctionDistances 𝕜 X] → outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)) → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (max (u + 1) (u_2 + 1))`
Fields: `𝔓`, `𝓘`, `𝒬`, `ι`

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

#### `Tile.C6_2_1` (def)
Lean: `ℕ → NNReal`
Docstring: The constant from lemma 6.2.1. Has value `2 ^ (231 * a ^ 3)` in the blueprint.
Definition: `fun (a : ℕ) => (2 : NNReal) ^ (((2 : ℕ) * 𝕔 + (6 : ℕ) + 𝕔 / (4 : ℕ)) * a ^ (3 : ℕ))`

#### `PreTileStructure.𝓘` (def)
Lean: `{𝕜 : Type u_1} → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X → @GridStructure.Grid X _ inst_1 inst_2 _ _ _ _ _`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.4`

#### `instPartialOrderGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → PartialOrder (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => PartialOrder.lift (fun (i : @GridStructure.Grid X _ inst inst_1 _ _ _ _ _) => (↑i, GridStructure.s i)) ⋯`

#### `Ks` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {K : X → X → ℂ} → [inst : PseudoMetricSpace X] → [KernelProofData a K] → ℤ → X → X → ℂ`
Docstring: K_s in the blueprint
Definition: `fun {X : Type u_1} {a : ℕ} {K : X → X → ℂ} [PseudoMetricSpace X] [KernelProofData a K] (s : ℤ) (x y : X) => K x y * ↑(ψ (defaultD a) (HPow.hPow (α := ℝ) (↑(defaultD a)) (-s) * dist x y))`

#### `instFunLikeΘ` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → FunLike (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) X 𝕜`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] => DFunLike.mk (β := fun (x : X) => 𝕜) (fun (f : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) => ⇑(coeΘ f)) ⋯`

#### `FunctionDistances.coeΘ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → @Θ _ X inst inst_1 _ → C(X, 𝕜)`
Docstring: The coercion map from `Θ` to `C(X, 𝕜)`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.2`

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

#### `Tile.correlation` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [ProofData a q K σ₁ σ₂ F G] → ℤ → ℤ → X → X → X → ℂ`
Docstring: Def 6.2.1 (from Lemma 6.2.1), denoted by `φ(y)` in the blueprint.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] (s₁ s₂ : ℤ) (x₁ x₂ y : X) => HMul.hMul (α := ℂ) ((starRingEnd ℂ) (Ks s₁ x₁ y) : ℂ) (Ks s₂ x₂ y)`

## Translations

### `Tile.correlation_le`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hle : 𝔰 p' ≤ 𝔰 p) (hg : Measurable g) (hg1 : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) : ‖∫ (y : X), adjointCarleson p' g y * (starRingEnd ℂ) (adjointCarleson p g y)‖ₑ ≤ (↑(Tile.C6_1_5 a) * (1 + edist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / 4} (𝒬 p') (𝒬 p)) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) / volume ↑(𝓘 p) * ∫⁻ (y : X) in E p', ‖g y‖ₑ) * ∫⁻ (y : X) in E p, ‖g y‖ₑ`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {p p' : 𝔓 X}, 𝔰 p' ≤ 𝔰 p → ∀ {g : X → ℂ}, Measurable g → (∀ (x : X), ‖g x‖ ≤ G.indicator (1 : X → ℝ) x) → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => HMul.hMul (β := ℂ) (adjointCarleson (F := F) (G := G) p' g y) ((starRingEnd ℂ) (adjointCarleson (F := F) (G := G) p g y) : ℂ)) ≤ (HDiv.hDiv (β := ENNReal) (↑(Tile.C6_1_5 a) * ((1 : ENNReal) + edist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / (4 : ℝ)} (𝒬 p') (𝒬 p)) ^ (-((2 : ℝ) * HPow.hPow (α := ℝ) ↑a (2 : ℕ) + HPow.hPow (α := ℝ) ↑a (3 : ℕ))⁻¹)) ((volume : Measure X) ↑(𝓘 p) : ENNReal) * ∫⁻ (y : X) in E (F := F) (G := G) p', ‖g y‖ₑ) * ∫⁻ (y : X) in E (F := F) (G := G) p, ‖g y‖ₑ`
Docstring: Part 1 of Lemma 6.1.5 (eq. 6.1.43).
English: (Part 1 of Lemma 6.1.5, eq. (6.1.43).) Let $X$ be a metric space. Let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common to chapters 2–7 of the blueprint). Write $\mu$ for the measure `volume` on $X$ provided through this instance, and $Q$ for the simple function from $X$ to the function family $\Theta(X)$ provided by the instance (`ProofData.Q`); each $\vartheta \in \Theta(X)$ is viewed as a function $X \to \mathbb{R}$. Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{N a^2}$, $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` and $o = $ `cancelPt X`, where $N$ denotes the project's natural-number constant `𝕔` (whose docstring fixes it equal to $100$). Write $\mathfrak{P}$ for the type of tiles `𝔓 X` of this structure. For a tile $p \in \mathfrak{P}$: $\mathcal{I}(p)$ is its grid cube `𝓘 p` (a subset of $X$), $\mathfrak{c}(p) = c(\mathcal{I}(p)) \in X$ and $\mathfrak{s}(p) = s(\mathcal{I}(p)) \in \mathbb{Z}$ are the point and the integer the grid structure assigns to that cube (`𝔠 p`, `𝔰 p`), $\mathcal{Q}(p) \in \Theta(X)$ is the element assigned to $p$ by the tile structure (`𝒬 p`), and $E(p) = \{x \in \mathcal{I}(p) : Q(x) \in \Omega(p),\ \sigma_1(x) \le \mathfrak{s}(p) \le \sigma_2(x)\}$ is the set `E p` of Proposition 2.0.2, with $\Omega(p) \subseteq \Theta(X)$ the set `Ω p` of the tile structure. For $x \in X$ and $r \in \mathbb{R}$, $d_{x,r}$ denotes the extended distance `edist_{x, r}` on $\Theta(X)$ associated by the `FunctionDistances` structure to the ball with centre $x$ and radius $r$. For $h : X \to \mathbb{C}$, $T_p^* h : X \to \mathbb{C}$ denotes `adjointCarleson p h` (the operator $T_p^*$ defined above Lemma 7.4.1), namely $T_p^* h(x) = \int_{E(p)} \overline{K_{\mathfrak{s}(p)}(y,x)}\, e^{i(Q(y)(y) - Q(y)(x))}\, h(y)\,d\mu(y)$, where $K_s$ is the truncated kernel `Ks s`. Let $p, p' \in \mathfrak{P}$ be tiles with $\mathfrak{s}(p') \le \mathfrak{s}(p)$. Let $g : X \to \mathbb{C}$ be measurable with $|g(x)| \le \mathbf{1}_G(x)$ for all $x \in X$. Then, with values in $[0,\infty]$, $$\Big| \int_X T_{p'}^* g(y)\, \overline{T_p^* g(y)}\,d\mu(y) \Big| \le \left(\frac{C_{6.1.5}(a)\,\big(1 + d_{\mathfrak{c}(p'),\, D^{\mathfrak{s}(p')}/4}(\mathcal{Q}(p'), \mathcal{Q}(p))\big)^{-1/(2a^2 + a^3)}}{\mu(\mathcal{I}(p))} \int_{E(p')} |g(y)|\,d\mu(y)\right) \int_{E(p)} |g(y)|\,d\mu(y),$$ where $C_{6.1.5}(a) = 2^{(2N + 7 + \lfloor N/4 \rfloor) a^3}$ is the constant `Tile.C6_1_5 a`.

### `Tile.I12_le`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (ha : 4 ≤ a) (hle : 𝔰 p' ≤ 𝔰 p) (hinter : (Metric.ball (𝔠 p') (5 * ↑(defaultD a) ^ 𝔰 p') ∩ Metric.ball (𝔠 p) (5 * ↑(defaultD a) ^ 𝔰 p)).Nonempty) (x1 : ↑(E p')) (x2 : ↑(E p)) : Tile.I12 p p' g ↑x1 ↑x2 ≤ 2 ^ ((2 * 𝕔 + 6 + 𝕔 / 4) * a ^ 3 + 8 * a + 1) * (1 + edist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / 4} (𝒬 p') (𝒬 p)) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) / volume (Metric.ball (↑x2) (↑(defaultD a) ^ 𝔰 p)) * ‖g ↑x1‖ₑ * ‖g ↑x2‖ₑ`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)], (4 : ℕ) ≤ a → ∀ {p p' : 𝔓 X}, 𝔰 p' ≤ 𝔰 p → ∀ {g : X → ℂ}, (Metric.ball (𝔠 p') ((5 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p')) ∩ Metric.ball (𝔠 p) ((5 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p))).Nonempty → ∀ (x1 : ↑(E (F := F) (G := G) p')) (x2 : ↑(E (F := F) (G := G) p)), Tile.I12 (F := F) (G := G) p p' g ↑x1 ↑x2 ≤ HDiv.hDiv (β := ENNReal) ((2 : ENNReal) ^ (((2 : ℕ) * 𝕔 + (6 : ℕ) + 𝕔 / (4 : ℕ)) * a ^ (3 : ℕ) + (8 : ℕ) * a + (1 : ℕ)) * ((1 : ENNReal) + edist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / (4 : ℝ)} (𝒬 p') (𝒬 p)) ^ (-((2 : ℝ) * HPow.hPow (α := ℝ) ↑a (2 : ℕ) + HPow.hPow (α := ℝ) ↑a (3 : ℕ))⁻¹)) ((volume : Measure X) (Metric.ball (↑x2) (HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p))) : ENNReal) * ‖g ↑x1‖ₑ * ‖g ↑x2‖ₑ`
Docstring: Inequality (6.2.29).
English: (Inequality (6.2.29).) Let $X$ be a metric space. Let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common to chapters 2–7 of the blueprint). Write $\mu$ for the measure `volume` on $X$ provided through this instance, and $Q$ for the simple function from $X$ to the function family $\Theta(X)$ provided by the instance (`ProofData.Q`); each $\vartheta \in \Theta(X)$ is viewed as a function $X \to \mathbb{R}$. Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{N a^2}$, $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` and $o = $ `cancelPt X`, where $N$ denotes the project's natural-number constant `𝕔` (whose docstring fixes it equal to $100$). Write $\mathfrak{P}$ for the type of tiles `𝔓 X` of this structure. For a tile $p \in \mathfrak{P}$: $\mathcal{I}(p)$ is its grid cube `𝓘 p` (a subset of $X$), $\mathfrak{c}(p) = c(\mathcal{I}(p)) \in X$ and $\mathfrak{s}(p) = s(\mathcal{I}(p)) \in \mathbb{Z}$ are the point and the integer the grid structure assigns to that cube (`𝔠 p`, `𝔰 p`), $\mathcal{Q}(p) \in \Theta(X)$ is the element assigned to $p$ by the tile structure (`𝒬 p`), and $E(p) = \{x \in \mathcal{I}(p) : Q(x) \in \Omega(p),\ \sigma_1(x) \le \mathfrak{s}(p) \le \sigma_2(x)\}$ is the set `E p` of Proposition 2.0.2, with $\Omega(p) \subseteq \Theta(X)$ the set `Ω p` of the tile structure. For $x \in X$ and $r \in \mathbb{R}$, $d_{x,r}$ denotes the extended distance `edist_{x, r}` on $\Theta(X)$ associated by the `FunctionDistances` structure to the ball with centre $x$ and radius $r$. For $h : X \to \mathbb{C}$, $T_p^* h : X \to \mathbb{C}$ denotes `adjointCarleson p h` (the operator $T_p^*$ defined above Lemma 7.4.1), namely $T_p^* h(x) = \int_{E(p)} \overline{K_{\mathfrak{s}(p)}(y,x)}\, e^{i(Q(y)(y) - Q(y)(x))}\, h(y)\,d\mu(y)$, where $K_s$ is the truncated kernel `Ks s`. Assume $a \ge 4$. Let $p, p' \in \mathfrak{P}$ be tiles with $\mathfrak{s}(p') \le \mathfrak{s}(p)$. Let $g : X \to \mathbb{C}$ be any function. Assume that $B(\mathfrak{c}(p'), 5D^{\mathfrak{s}(p')}) \cap B(\mathfrak{c}(p), 5D^{\mathfrak{s}(p)})$ is nonempty (open balls in $X$). For $x_1, x_2 \in X$ let $I_{12}(x_1,x_2) \in [0,\infty]$ be `Tile.I12 p p' g x₁ x₂` (Definition (6.2.27)), i.e. $$I_{12}(x_1,x_2) = \Big| \Big(\int_X e^{i(-Q(x_1)(y) + Q(x_2)(y))}\, \overline{K_{\mathfrak{s}(p')}(x_1,y)}\, K_{\mathfrak{s}(p)}(x_2,y)\,d\mu(y)\Big)\, g(x_1)\, g(x_2) \Big|.$$ Then for all $x_1 \in E(p')$ and $x_2 \in E(p)$, with values in $[0,\infty]$, $$I_{12}(x_1, x_2) \le \frac{2^{(2N + 6 + \lfloor N/4 \rfloor)a^3 + 8a + 1}\,\big(1 + d_{\mathfrak{c}(p'),\, D^{\mathfrak{s}(p')}/4}(\mathcal{Q}(p'), \mathcal{Q}(p))\big)^{-1/(2a^2 + a^3)}}{\mu(B(x_2, D^{\mathfrak{s}(p)}))}\, |g(x_1)|\, |g(x_2)|.$$

### `Tile.I12_le'`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hle : 𝔰 p' ≤ 𝔰 p) (x1 : ↑(E p')) (x2 : ↑(E p)) : Tile.I12 p p' g ↑x1 ↑x2 ≤ 2 ^ ((2 * 𝕔 + 6 + 𝕔 / 4) * a ^ 3 + 8 * a) * (1 + edist_{↑x1, ↑(defaultD a) ^ 𝔰 p'} (Q ↑x1) (Q ↑x2)) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) / volume (Metric.ball (↑x2) (↑(defaultD a) ^ 𝔰 p)) * ‖g ↑x1‖ₑ * ‖g ↑x2‖ₑ`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {p p' : 𝔓 X}, 𝔰 p' ≤ 𝔰 p → ∀ {g : X → ℂ} (x1 : ↑(E (F := F) (G := G) p')) (x2 : ↑(E (F := F) (G := G) p)), Tile.I12 (F := F) (G := G) p p' g ↑x1 ↑x2 ≤ HDiv.hDiv (β := ENNReal) ((2 : ENNReal) ^ (((2 : ℕ) * 𝕔 + (6 : ℕ) + 𝕔 / (4 : ℕ)) * a ^ (3 : ℕ) + (8 : ℕ) * a) * ((1 : ENNReal) + edist_{↑x1, HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p')} ((Q (F := F) (G := G)) ↑x1 : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _) ((Q (F := F) (G := G)) ↑x2 : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)) ^ (-((2 : ℝ) * HPow.hPow (α := ℝ) ↑a (2 : ℕ) + HPow.hPow (α := ℝ) ↑a (3 : ℕ))⁻¹)) ((volume : Measure X) (Metric.ball (↑x2) (HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p))) : ENNReal) * ‖g ↑x1‖ₑ * ‖g ↑x2‖ₑ`
Docstring: Inequality (6.2.28).
English: (According to its docstring, this is Inequality (6.2.28).) Let $X$ be a metric space satisfying the standing assumptions `ProofData a q K σ₁ σ₂ F G` (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a complex-valued kernel $K : X \times X \to \mathbb{C}$, integer-valued functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), equipped with a tile structure `TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)`, and let $\mu$ denote the volume measure on $X$. Let $p, p' \in \mathfrak{P}(X)$ be tiles with $s(p') \le s(p)$, and let $g : X \to \mathbb{C}$ be complex-valued. Then for all $x_1 \in E(p')$ and $x_2 \in E(p)$, in the extended nonnegative reals,\n$$I_{12}(p, p', g)(x_1, x_2) \le \frac{2^{(2\mathfrak{c} + 6 + \lfloor \mathfrak{c}/4 \rfloor)a^3 + 8a}\,\big(1 + d_{x_1,\, D^{s(p')}}(Q(x_1), Q(x_2))\big)^{-1/(2a^2 + a^3)}}{\mu(B(x_2, D^{s(p)}))}\, \|g(x_1)\|\, \|g(x_2)\|,$$\nwhere $I_{12}$ is `Tile.I12`, $D$ = `defaultD a` (so $D^{s(p')}$, $D^{s(p)}$ are real numbers raised to integer powers), $\mathfrak{c}$ is the natural-number constant `𝕔`, the exponent $(2\mathfrak{c} + 6 + \lfloor \mathfrak{c}/4 \rfloor)a^3 + 8a$ is a natural number in which $\lfloor \mathfrak{c}/4 \rfloor$ is floor (natural-number) division, the exponent $-1/(2a^2 + a^3)$ is a real number, and $d_{x_1, r}$ is the extended distance `edist_{x_1, r}` on $\Theta(X)$.

### `Tile.correlation_le_of_nonempty_inter`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (ha : 4 ≤ a) (hle : 𝔰 p' ≤ 𝔰 p) (hg : Measurable g) (hg1 : ∀ (x : X), ‖g x‖ ≤ G.indicator 1 x) (hinter : (Metric.ball (𝔠 p') (5 * ↑(defaultD a) ^ 𝔰 p') ∩ Metric.ball (𝔠 p) (5 * ↑(defaultD a) ^ 𝔰 p)).Nonempty) : ‖∫ (y : X), adjointCarleson p' g y * (starRingEnd ℂ) (adjointCarleson p g y)‖ₑ ≤ (↑(Tile.C6_1_5 a) * (1 + edist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / 4} (𝒬 p') (𝒬 p)) ^ (-(2 * ↑a ^ 2 + ↑a ^ 3)⁻¹) / volume ↑(𝓘 p) * ∫⁻ (y : X) in E p', ‖g y‖ₑ) * ∫⁻ (y : X) in E p, ‖g y‖ₑ`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)], (4 : ℕ) ≤ a → ∀ {p p' : 𝔓 X}, 𝔰 p' ≤ 𝔰 p → ∀ {g : X → ℂ}, Measurable g → (∀ (x : X), ‖g x‖ ≤ G.indicator (1 : X → ℝ) x) → (Metric.ball (𝔠 p') ((5 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p')) ∩ Metric.ball (𝔠 p) ((5 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p))).Nonempty → enorm (E := ℂ) (@integral _ _ _ _ MeasureSpace.toMeasurableSpace volume fun (y : X) => HMul.hMul (β := ℂ) (adjointCarleson (F := F) (G := G) p' g y) ((starRingEnd ℂ) (adjointCarleson (F := F) (G := G) p g y) : ℂ)) ≤ (HDiv.hDiv (β := ENNReal) (↑(Tile.C6_1_5 a) * ((1 : ENNReal) + edist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / (4 : ℝ)} (𝒬 p') (𝒬 p)) ^ (-((2 : ℝ) * HPow.hPow (α := ℝ) ↑a (2 : ℕ) + HPow.hPow (α := ℝ) ↑a (3 : ℕ))⁻¹)) ((volume : Measure X) ↑(𝓘 p) : ENNReal) * ∫⁻ (y : X) in E (F := F) (G := G) p', ‖g y‖ₑ) * ∫⁻ (y : X) in E (F := F) (G := G) p, ‖g y‖ₑ`
English: Let $X$ be a metric space. Let $a \in \mathbb{N}$, $q \in \mathbb{R}$, $K : X \to X \to \mathbb{C}$, $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and $F, G \subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (the data common to chapters 2–7 of the blueprint). Write $\mu$ for the measure `volume` on $X$ provided through this instance, and $Q$ for the simple function from $X$ to the function family $\Theta(X)$ provided by the instance (`ProofData.Q`); each $\vartheta \in \Theta(X)$ is viewed as a function $X \to \mathbb{R}$. Assume moreover a tile structure `TileStructure Q D κ S o` with $D = $ `defaultD a` $= 2^{N a^2}$, $\kappa = $ `defaultκ a` $= 2^{-10a}$, $S = $ `defaultS X` and $o = $ `cancelPt X`, where $N$ denotes the project's natural-number constant `𝕔` (whose docstring fixes it equal to $100$). Write $\mathfrak{P}$ for the type of tiles `𝔓 X` of this structure. For a tile $p \in \mathfrak{P}$: $\mathcal{I}(p)$ is its grid cube `𝓘 p` (a subset of $X$), $\mathfrak{c}(p) = c(\mathcal{I}(p)) \in X$ and $\mathfrak{s}(p) = s(\mathcal{I}(p)) \in \mathbb{Z}$ are the point and the integer the grid structure assigns to that cube (`𝔠 p`, `𝔰 p`), $\mathcal{Q}(p) \in \Theta(X)$ is the element assigned to $p$ by the tile structure (`𝒬 p`), and $E(p) = \{x \in \mathcal{I}(p) : Q(x) \in \Omega(p),\ \sigma_1(x) \le \mathfrak{s}(p) \le \sigma_2(x)\}$ is the set `E p` of Proposition 2.0.2, with $\Omega(p) \subseteq \Theta(X)$ the set `Ω p` of the tile structure. For $x \in X$ and $r \in \mathbb{R}$, $d_{x,r}$ denotes the extended distance `edist_{x, r}` on $\Theta(X)$ associated by the `FunctionDistances` structure to the ball with centre $x$ and radius $r$. For $h : X \to \mathbb{C}$, $T_p^* h : X \to \mathbb{C}$ denotes `adjointCarleson p h` (the operator $T_p^*$ defined above Lemma 7.4.1), namely $T_p^* h(x) = \int_{E(p)} \overline{K_{\mathfrak{s}(p)}(y,x)}\, e^{i(Q(y)(y) - Q(y)(x))}\, h(y)\,d\mu(y)$, where $K_s$ is the truncated kernel `Ks s`. Assume $a \ge 4$. Let $p, p' \in \mathfrak{P}$ be tiles with $\mathfrak{s}(p') \le \mathfrak{s}(p)$. Let $g : X \to \mathbb{C}$ be measurable with $|g(x)| \le \mathbf{1}_G(x)$ for all $x \in X$. Assume that $B(\mathfrak{c}(p'), 5D^{\mathfrak{s}(p')}) \cap B(\mathfrak{c}(p), 5D^{\mathfrak{s}(p)})$ is nonempty (open balls in $X$). Then, with values in $[0,\infty]$, $$\Big| \int_X T_{p'}^* g(y)\, \overline{T_p^* g(y)}\,d\mu(y) \Big| \le \left(\frac{C_{6.1.5}(a)\,\big(1 + d_{\mathfrak{c}(p'),\, D^{\mathfrak{s}(p')}/4}(\mathcal{Q}(p'), \mathcal{Q}(p))\big)^{-1/(2a^2 + a^3)}}{\mu(\mathcal{I}(p))} \int_{E(p')} |g(y)|\,d\mu(y)\right) \int_{E(p)} |g(y)|\,d\mu(y),$$ where $C_{6.1.5}(a) = 2^{(2N + 7 + \lfloor N/4 \rfloor) a^3}$ is the constant `Tile.C6_1_5 a`.
