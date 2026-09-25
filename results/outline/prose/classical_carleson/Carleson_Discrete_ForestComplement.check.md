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

#### `C5_1_3` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant used in Lemma 5.1.3. Has value `2 ^ (120 * a ^ 3) / (q - 1) ^ 5` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => (2 : NNReal) ^ ((𝕔 + (8 : ℕ) + 𝕔 / (8 : ℕ)) * a ^ (3 : ℕ)) / (q - (1 : NNReal)) ^ (5 : ℕ)`

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

#### `nnq` (def)
Lean: `(X : Type u_1) → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : PseudoMetricSpace X] → [ProofData a q K σ₁ σ₂ F G] → NNReal`
Docstring: `q` as an element of `ℝ≥0`.
Definition: `fun (X : Type u_1) {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [PseudoMetricSpace X] [ProofData a q K σ₁ σ₂ F G] => ⟨q, ⋯⟩`

#### `𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → (X : Type u) → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [PreTileStructure.{u, u_1, u_2} Q D κ S o] → Type u`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] (X : Type u) {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.𝔓.{u, u_1, u_2} 𝕜 X`

#### `𝔓₁` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X)`
Docstring: The set `𝔓₁`, defined in (5.1.30).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => ⋃ (n : ℕ), ⋃ (k : ℕ), ⋃ (_ : k ≤ n), ⋃ (j : ℕ), ⋃ (_ : j ≤ (2 : ℕ) * n + (3 : ℕ)), ℭ₅ (F := F) (G := G) k n j`

#### `GridStructure.coeGrid` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → Set X`
Docstring: The collection of dyadic cubes
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.3`

#### `PreTileStructure.toGridStructure` (def)
Lean: `(𝕜 : Type u_1) → {inst : RCLike 𝕜} → {X : Type u} → {A : outParam NNReal} → {inst_1 : PseudoMetricSpace X} → {inst_2 : DoublingMeasure X A} → {inst_3 : FunctionDistances 𝕜 X} → {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] → GridStructure.{u_2, u} X D κ S o`
Definition: `fun (𝕜 : Type u_1) {inst : RCLike 𝕜} (X : Type u) {A : outParam NNReal} {inst_1 : PseudoMetricSpace X} {inst_2 : DoublingMeasure X A} {inst_3 : FunctionDistances 𝕜 X} {Q : outParam (SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : PreTileStructure.{u, u_1, u_2} Q D κ S o] => self.1`

#### `𝓘` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → Grid X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] => PreTileStructure.𝓘`

#### `defaultZ` (def)
Lean: `ℕ → ℕ`
Docstring: The constant `Z` from (2.0.3).
Definition: `fun (a : ℕ) => (2 : ℕ) ^ ((12 : ℕ) * a)`

#### `maxℭ` (def)
Lean: `(X : Type u_1) → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ`
Definition: `fun (X : Type u_1) {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => (Exists.choose (p := fun (n : ℕ × ℕ) => ∀ (x : ℕ × ℕ), Membership.mem (γ := Set (ℕ × ℕ)) {kn : ℕ × ℕ | Set.Nonempty (α := 𝔓 X) (ℭ (F := F) (G := G) kn.1 kn.2)} x → x.2 ≤ n.2) ⋯).2`

#### `ℭ₂` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `ℭ₂(k, n, j)` of `ℭ₁(k, n, j)`, given in (5.1.13).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => Set.layersAbove (ℭ₁ (F := F) (G := G) k n j) (defaultZ a * (n + (1 : ℕ)))`

#### `𝔏₀'` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `𝔏₀(k, n, l)` of `𝔏₀(k, n)`, given in Lemma 5.5.3. We use the name `𝔏₀'` in Lean.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n l : ℕ) => Set.minLayer (𝔏₀ (F := F) (G := G) k n) l`

#### `𝔏₁` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: `𝔏₁(k, n, j, l)` consists of the minimal elements in `ℭ₁(k, n, j)` not in `𝔏₁(k, n, j, l')` for some `l' < l`. Defined near (5.1.11).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j l : ℕ) => Set.minLayer (ℭ₁ (F := F) (G := G) k n j) l`

#### `𝔏₂` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `𝔏₂(k, n, j)` of `ℭ₂(k, n, j)`, given in (5.1.15).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => {p : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (ℭ₂ (F := F) (G := G) k n j) p ∧ ¬∃ (u : 𝔓 X), Membership.mem (γ := Set (𝔓 X)) (𝔘₁ (F := F) (G := G) k n j) u ∧ 𝓘 p ≠ 𝓘 u ∧ smul (F := F) (G := G) (2 : ℝ) p ≤ smul (F := F) (G := G) (1 : ℝ) u}`

#### `𝔏₃` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: `𝔏₃(k, n, j, l)` consists of the maximal elements in `ℭ₃(k, n, j)` not in `𝔏₃(k, n, j, l')` for some `l' < l`. Defined near (5.1.17).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j l : ℕ) => Set.maxLayer (ℭ₃ (F := F) (G := G) k n j) l`

#### `C2_0_3` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: The constant appearing in Proposition 2.0.3. Has value `2 ^ (117 * a ^ 3)` in the blueprint.
Definition: `fun (a : ℕ) (q : NNReal) => (2 : NNReal) ^ ((𝕔 + (5 : ℕ) + 𝕔 / (8 : ℕ)) * a ^ (3 : ℕ)) / (q - (1 : NNReal))`

#### `instPartialOrder𝔓Real` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → PartialOrder (𝔓 X)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => PartialOrder.lift (toTileLike (F := F) (G := G)) ⋯`

#### `ℭ` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → Set (𝔓 X)`
Docstring: The partition `ℭ(k, n)` of `𝔓(k)` by density, given in (5.1.7).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n : ℕ) => {p : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (TilesAt (F := F) (G := G) k) p ∧ dens' (F := F) (G := G) k {p} ∈ Set.Ioc ((2 : ENNReal) ^ ((4 : ℤ) * ↑a - ↑n)) ((2 : ENNReal) ^ ((4 : ℤ) * ↑a - ↑n + (1 : ℤ)))}`

#### `C5_1_3_optimized` (def)
Lean: `ℕ → NNReal → NNReal`
Docstring: An optimized constant for Lemma 5.1.3.
Definition: `fun (a : ℕ) (q : NNReal) => C2_0_3 a q * (2 : NNReal) ^ ((29 : ℕ) * a + (23 : ℕ)) / (q - (1 : NNReal)) ^ (4 : ℕ)`

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

#### `Grid` (def)
Lean: `(X : Type u) → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [GridStructure X D κ S o] → Type u`
Docstring: The indexing type of the grid structure. Elements are called (dyadic) cubes. Note that this type has instances for both `≤` and `⊆`, but they do *not* coincide.
Definition: `fun (X : Type u) {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => @GridStructure.Grid X _ inst inst_1 _ _ _ _ _`

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

#### `instPartialOrderGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → PartialOrder (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => PartialOrder.lift (fun (i : @GridStructure.Grid X _ inst inst_1 _ _ _ _ _) => (↑i, GridStructure.s i)) ⋯`

#### `instPseudoMetricSpaceWithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → {x : X} → {r : ℝ} → PseudoMetricSpace (WithFunctionDistance x r)`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] {x : X} {r : ℝ} => FunctionDistances.metric x r`

#### `𝔠` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → X`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => c (𝓘 p)`

#### `𝔰` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure Q D κ S o] → 𝔓 X → ℤ`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure Q D κ S o] (p : 𝔓 X) => s (𝓘 p)`

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

#### `instFintype𝔓` (def)
Lean: `{𝕜 : Type u_1} → [inst : RCLike 𝕜] → {X : Type u} → {A : NNReal} → [inst_1 : PseudoMetricSpace X] → [inst_2 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_3 : FunctionDistances 𝕜 X] → {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} → [inst_4 : PreTileStructure.{u, u_1, u_2} Q D κ S o] → Fintype (𝔓.{u, u_1, u_2} X)`
Definition: `fun {𝕜 : Type u_1} [RCLike 𝕜] {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [FunctionDistances 𝕜 X] {Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)} [PreTileStructure.{u, u_1, u_2} Q D κ S o] => PreTileStructure.fintype_𝔓`

#### `ℭ₅` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `ℭ₅(k, n, j)` of `ℭ₄(k, n, j)`, given in (5.1.23).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => ℭ₄ (F := F) (G := G) k n j \ 𝔏₄ (F := F) (G := G) k n j`

#### `Set.layersAbove` (def)
Lean: `{α : Type u_1} → [PartialOrder α] → Set α → ℕ → Set α`
Docstring: The elements above `A`'s `n` minimal layers.
Definition: `fun {α : Type u_1} [PartialOrder α] (A : Set α) (n : ℕ) => A \ ⋃ (k : ℕ), ⋃ (_ : k ≤ n), A.minLayer k`

#### `ℭ₁` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `ℭ₁(k, n, j)` of `ℭ(k, n)`, given in (5.1.9). Together with `𝔏₀(k, n)` this forms a partition.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => preℭ₁ (F := F) (G := G) k n j \ preℭ₁ (F := F) (G := G) k n (j + (1 : ℕ))`

#### `Set.minLayer` (def)
Lean: `{α : Type u_1} → [PartialOrder α] → Set α → ℕ → Set α`
Docstring: The `n`th minimal layer of `A`.
Definition: `fun {α : Type u_1} [PartialOrder α] (A : Set α) => WellFounded.Nat.fix (motive := fun (n : ℕ) => Set α) (fun (x : ℕ) => x) fun (n : ℕ) (a : (y : ℕ) → InvImage (fun (x1 x2 : ℕ) => x1 < x2) (fun (x : ℕ) => x) y n → Set α) => {a_1 : α | Minimal (fun (x : α) => x ∈ A \ ⋃ (k : ℕ), ⋃ (h : k < n), a k ⋯) a_1}`

#### `𝔏₀` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `𝔏₀(k, n)` of `ℭ(k, n)`, given in (5.1.10). Not to be confused with `𝔏₀(k, n, j)` which is called `𝔏₀'` in Lean.
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n : ℕ) => {p : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (ℭ (F := F) (G := G) k n) p ∧ 𝔅 (F := F) (G := G) k n p = ∅}`

#### `TileLike` (def)
Lean: `(X : Type u_1) → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Type u_1`
Definition: `fun (X : Type u_1) [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => Grid X × (Set (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _))ᵒᵈ`

#### `aux𝓒` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → Set (Grid X)`
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k : ℕ) => {i : Grid X | ∃ (j : Grid X), i ≤ j ∧ HMul.hMul (β := ENNReal) (HPow.hPow (β := ℤ) (2 : ENNReal) (-↑k)) ((volume : Measure X) ↑j : ENNReal) < (volume : Measure X) (G ∩ ↑j)}`

#### `instPartialOrderTileLike` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → PartialOrder (TileLike X (F := F) (G := G))`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] => { le := instPartialOrderTileLike._aux_1, lt := instPartialOrderTileLike._aux_3, le_refl := ⋯, le_trans := ⋯, lt_iff_le_not_ge := ⋯, le_antisymm := ⋯ }`

#### `smul` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℝ → 𝔓 X → TileLike X (F := F) (G := G)`
Docstring: This is not defined as such in the blueprint, but `λp ≲ λ'p'` can be written using `smul l p ≤ smul l' p'`. Beware: `smul 1 p` is very different from `toTileLike p`.
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (l : ℝ) (p : 𝔓 X) => (𝓘 p, ball_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) l)`

#### `𝔘₁` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `𝔘₁(k, n, j)` of `ℭ₁(k, n, j)`, given in (5.1.14).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => {u : 𝔓 X | Membership.mem (γ := Set (𝔓 X)) (ℭ₁ (F := F) (G := G) k n j) u ∧ ∀ (p : 𝔓 X), Membership.mem (γ := Set (𝔓 X)) (ℭ₁ (F := F) (G := G) k n j) p → 𝓘 u < 𝓘 p → Disjoint (ball_{𝔠 u, ↑(defaultD a) ^ 𝔰 u / (4 : ℝ)} (𝒬 u) (100 : ℝ)) (ball_{𝔠 p, ↑(defaultD a) ^ 𝔰 p / (4 : ℝ)} (𝒬 p) (100 : ℝ))}`

#### `Set.maxLayer` (def)
Lean: `{α : Type u_1} → [PartialOrder α] → Set α → ℕ → Set α`
Docstring: The `n`th maximal layer of `A`.
Definition: `fun {α : Type u_1} [PartialOrder α] (A : Set α) (n : ℕ) => A.minLayer n`

#### `ℭ₃` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → ℕ → ℕ → Set (𝔓 X)`
Docstring: The subset `ℭ₃(k, n, j)` of `ℭ₂(k, n, j)`, given in (5.1.16).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k n j : ℕ) => ℭ₂ (F := F) (G := G) k n j \ 𝔏₂ (F := F) (G := G) k n j`

#### `dach` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X) → 𝔓 X → (X → ℂ) → ENNReal`
Docstring: `h(p)` in the proof of Lemma 6.1.4 (**d**ens₁ **a**nti**c**hain **h**).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (𝔄 : Set (𝔓 X)) (p : 𝔓 X) (g : X → ℂ) => HMul.hMul (α := ENNReal) (((volume : Measure X) (Metric.ball (𝔠 p) ((14 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p))))⁻¹ : ENNReal) (∫⁻ (x : X), ∑ p' : 𝔓 X with (p' ∈ 𝔄 ∧ 𝔰 p' ≤ 𝔰 p) ∧ ↑(𝓘 p') ⊆ Metric.ball (𝔠 p) ((14 : ℝ) * HPow.hPow (α := ℝ) (↑(defaultD a)) (𝔰 p)), ((1 : ENNReal) + edist_{𝔠 p', ↑(defaultD a) ^ 𝔰 p' / (4 : ℝ)} (𝒬 p') (𝒬 p)) ^ (-((2 : ℝ) * HPow.hPow (α := ℝ) ↑a (2 : ℕ) + HPow.hPow (α := ℝ) ↑a (3 : ℕ))⁻¹) * (E (F := F) (G := G) p').indicator (fun (x : X) => ‖g x‖ₑ) x)`

#### `toTileLike` (def)
Lean: `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → 𝔓 X → TileLike X (F := F) (G := G)`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (p : 𝔓 X) => (𝓘 p, Ω p)`

#### `TilesAt` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → Set (𝔓 X)`
Docstring: The definition `𝔓(k)` given in (5.1.3).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k : ℕ) => 𝓘 ⁻¹' 𝓒 (F := F) (G := G) k`

#### `dens'` (def)
Lean: `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → ℕ → Set (𝔓 X) → ENNReal`
Docstring: The definition `dens'_k(𝔓')` given in (5.1.6).
Definition: `fun {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [MetricSpace X] [ProofData a q K σ₁ σ₂ F G] [TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (k : ℕ) (P' : Set (𝔓 X)) => ⨆ p' ∈ P', ⨆ (l : NNReal), ⨆ (_ : (2 : NNReal) ≤ l), ⨆ (p : 𝔓 X), ⨆ (_ : Membership.mem (γ := Set (𝔓 X)) (TilesAt (F := F) (G := G) k) p), ⨆ (_ : smul (F := F) (G := G) (↑l) p' ≤ smul (F := F) (G := G) (↑l) p), HDiv.hDiv (β := ENNReal) (HMul.hMul (β := ENNReal) (HPow.hPow (β := ℤ) (↑l) (-↑a)) ((volume : Measure X) (E₂ (F := F) (G := G) (↑l) p) : ENNReal)) ((volume : Measure X) ↑(𝓘 p) : ENNReal)`

## Translations

### `forest_complement`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ ↑(C5_1_3 a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {f : X → ℂ}, (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable f → ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (𝔓₁ (F := F) (G := G))ᶜ f x‖ₑ ≤ ↑(C5_1_3 a (nnq X (F := F) (G := G))) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹`
Docstring: Lemma 5.1.3, proving the bound on the integral of the Carleson sum over all leftover tiles which do not fit in a forest. It follows from a careful grouping of these tiles into finitely many antichains.
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7). Through this instance $X$ carries a `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$, whose measure (`volume`) we denote by $\mu$, and a `CompatibleFunctions ℝ X (2^a)` structure, which provides a type $\Theta(X)$ of continuous real-valued functions on $X$; let $Q : X\to\Theta(X)$ be the simple function given by the field `Q` of the `ProofData` instance. Let $\mathsf b\in\mathbb N$ be the project constant `𝕔` (per its docstring fixed equal to $100$), $D=\mathrm{defaultD}(a)=2^{\mathsf b a^2}$, $\kappa=\mathrm{default}\kappa(a)=2^{-10a}$, $S=\mathrm{defaultS}(X)\in\mathbb N$ (the natural number `defaultS` determined by the `ProofData`), and $o=\mathrm{cancelPt}(X)\in X$ (the point `cancelPt X`, chosen so that every function in $\Theta(X)$ vanishes at it). Assume a tile structure `TileStructure Q D κ S o` on $X$, and let $\mathfrak P(X)$ be its (finite) type of tiles, partially ordered by the project order `instPartialOrder𝔓Real`. Let $G'\subseteq X$ be the project set `G'` (docstring: the set $G'$ defined below (5.1.28)), defined as $G_1\cup G_2\cup G_3$ for the project sets `G₁`, `G₂`, `G₃`. Let $\mathfrak P_1\subseteq\mathfrak P(X)$ be the project set `𝔓₁` (docstring: the set $\mathfrak P_1$ defined in (5.1.30)), defined as $\bigcup_{n\in\mathbb N}\bigcup_{k\le n}\bigcup_{j\le 2n+3}\mathfrak C_5(k,n,j)$, where $\mathfrak C_5(k,n,j)$ is the project set `ℭ₅ k n j`, and write $\mathfrak P_1^c$ for its complement in $\mathfrak P(X)$. For a set of tiles $\mathfrak C\subseteq\mathfrak P(X)$, a function $g : X\to\mathbb C$ and $x\in X$, let $\mathrm{carlesonSum}(\mathfrak C, g)(x)=\sum_{p\in\mathfrak C}\mathrm{carlesonOn}(p, g)(x)$, where $\mathrm{carlesonOn}(p,\cdot)$ is the project operator `carlesonOn` (docstring: the operator $T_p$ defined in Proposition 2.0.2). Let $\mathfrak P_{\mathrm{pos}}\subseteq\mathfrak P(X)$ be the project set `𝔓pos` (docstring: the set $\mathfrak P_{G\setminus G'}$ in the blueprint). All integrals below are lower Lebesgue integrals with respect to $\mu$ of extended nonnegative norms $\|\cdot\|_e\in[0,\infty]$, and all right-hand sides are computed in $[0,\infty]$. Let $\bar q\in\mathbb R_{\ge 0}$ denote $q$ regarded as a nonnegative real (the project value `nnq X`). Let $C_{5.1.3}(a,\bar q)\in\mathbb R_{\ge0}$ be the project constant `C5_1_3 a (nnq X)`, namely $2^{(\mathsf b+8+\lfloor \mathsf b/8\rfloor)a^3}/(\bar q-1)^5$ computed in $\mathbb R_{\ge 0}$ (with truncated subtraction). (Lemma 5.1.3.) Let $f : X\to\mathbb C$ be a measurable function with $\|f(x)\|\le\mathbf 1_F(x)$ for all $x\in X$. Then $$\int_{G\setminus G'}\big\|\mathrm{carlesonSum}(\mathfrak P_1^c, f)(x)\big\|_e\,d\mu(x)\le C_{5.1.3}(a,\bar q)\,\mu(G)^{1-q^{-1}}\,\mu(F)^{q^{-1}}.$$

### `𝔓pos`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] : Set (𝔓 X)`
Lean (full): `{X : Type u_1} → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst : MetricSpace X] → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Set (𝔓 X)`
Docstring: The set 𝔓_{G\G'} in the blueprint
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7). Through this instance $X$ carries a `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$, whose measure (`volume`) we denote by $\mu$, and a `CompatibleFunctions ℝ X (2^a)` structure, which provides a type $\Theta(X)$ of continuous real-valued functions on $X$; let $Q : X\to\Theta(X)$ be the simple function given by the field `Q` of the `ProofData` instance. Let $\mathsf b\in\mathbb N$ be the project constant `𝕔` (per its docstring fixed equal to $100$), $D=\mathrm{defaultD}(a)=2^{\mathsf b a^2}$, $\kappa=\mathrm{default}\kappa(a)=2^{-10a}$, $S=\mathrm{defaultS}(X)\in\mathbb N$ (the natural number `defaultS` determined by the `ProofData`), and $o=\mathrm{cancelPt}(X)\in X$ (the point `cancelPt X`, chosen so that every function in $\Theta(X)$ vanishes at it). Assume a tile structure `TileStructure Q D κ S o` on $X$, and let $\mathfrak P(X)$ be its (finite) type of tiles, partially ordered by the project order `instPartialOrder𝔓Real`. Definition: `𝔓pos` is a set of tiles $\mathfrak P_{\mathrm{pos}}\subseteq\mathfrak P(X)$ depending on this data; according to its docstring, it is the set $\mathfrak P_{G\setminus G'}$ in the blueprint.

### `lintegral_carlesonSum_𝔓₁_compl_le_sum_lintegral`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ (((∑ n ≤ maxℭ X, ∑ k ≤ n, ∑ l < n, ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔏₀' k n l) f x‖ₑ) + ∑ n ≤ maxℭ X, ∑ k ≤ n, ∑ j ≤ 2 * n + 3, ∑ l ≤ defaultZ a * (n + 1), ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔏₁ k n j l) f x‖ₑ) + ∑ n ≤ maxℭ X, ∑ k ≤ n, ∑ j ≤ 2 * n + 3, ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔏₂ k n j) f x‖ₑ) + ∑ n ≤ maxℭ X, ∑ k ≤ n, ∑ j ≤ 2 * n + 3, ∑ l ≤ defaultZ a * (n + 1), ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔏₃ k n j l) f x‖ₑ`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {f : X → ℂ}, Measurable f → ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (𝔓₁ (F := F) (G := G))ᶜ f x‖ₑ ≤ (HAdd.hAdd (α := ENNReal) (∑ n ≤ maxℭ X (F := F) (G := G), ∑ k ≤ n, ∑ l < n, ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (𝔓pos (F := F) (G := G) ∩ (𝔓₁ (F := F) (G := G))ᶜ ∩ 𝔏₀' (F := F) (G := G) k n l) f x‖ₑ) (∑ n ≤ maxℭ X (F := F) (G := G), ∑ k ≤ n, ∑ j ≤ (2 : ℕ) * n + (3 : ℕ), ∑ l ≤ defaultZ a * (n + (1 : ℕ)), ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (𝔓pos (F := F) (G := G) ∩ (𝔓₁ (F := F) (G := G))ᶜ ∩ 𝔏₁ (F := F) (G := G) k n j l) f x‖ₑ) + ∑ n ≤ maxℭ X (F := F) (G := G), ∑ k ≤ n, ∑ j ≤ (2 : ℕ) * n + (3 : ℕ), ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (𝔓pos (F := F) (G := G) ∩ (𝔓₁ (F := F) (G := G))ᶜ ∩ 𝔏₂ (F := F) (G := G) k n j) f x‖ₑ) + ∑ n ≤ maxℭ X (F := F) (G := G), ∑ k ≤ n, ∑ j ≤ (2 : ℕ) * n + (3 : ℕ), ∑ l ≤ defaultZ a * (n + (1 : ℕ)), ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (𝔓pos (F := F) (G := G) ∩ (𝔓₁ (F := F) (G := G))ᶜ ∩ 𝔏₃ (F := F) (G := G) k n j l) f x‖ₑ`
Docstring: Putting together all the previous decomposition lemmas, one gets an estimate of the integral of `‖carlesonSum 𝔓₁ᶜ f x‖ₑ` by a sum of integrals of the same form over various subsets of `𝔓`, which are all antichains by design.
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7). Through this instance $X$ carries a `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$, whose measure (`volume`) we denote by $\mu$, and a `CompatibleFunctions ℝ X (2^a)` structure, which provides a type $\Theta(X)$ of continuous real-valued functions on $X$; let $Q : X\to\Theta(X)$ be the simple function given by the field `Q` of the `ProofData` instance. Let $\mathsf b\in\mathbb N$ be the project constant `𝕔` (per its docstring fixed equal to $100$), $D=\mathrm{defaultD}(a)=2^{\mathsf b a^2}$, $\kappa=\mathrm{default}\kappa(a)=2^{-10a}$, $S=\mathrm{defaultS}(X)\in\mathbb N$ (the natural number `defaultS` determined by the `ProofData`), and $o=\mathrm{cancelPt}(X)\in X$ (the point `cancelPt X`, chosen so that every function in $\Theta(X)$ vanishes at it). Assume a tile structure `TileStructure Q D κ S o` on $X$, and let $\mathfrak P(X)$ be its (finite) type of tiles, partially ordered by the project order `instPartialOrder𝔓Real`. Let $G'\subseteq X$ be the project set `G'` (docstring: the set $G'$ defined below (5.1.28)), defined as $G_1\cup G_2\cup G_3$ for the project sets `G₁`, `G₂`, `G₃`. Let $\mathfrak P_1\subseteq\mathfrak P(X)$ be the project set `𝔓₁` (docstring: the set $\mathfrak P_1$ defined in (5.1.30)), defined as $\bigcup_{n\in\mathbb N}\bigcup_{k\le n}\bigcup_{j\le 2n+3}\mathfrak C_5(k,n,j)$, where $\mathfrak C_5(k,n,j)$ is the project set `ℭ₅ k n j`, and write $\mathfrak P_1^c$ for its complement in $\mathfrak P(X)$. For a set of tiles $\mathfrak C\subseteq\mathfrak P(X)$, a function $g : X\to\mathbb C$ and $x\in X$, let $\mathrm{carlesonSum}(\mathfrak C, g)(x)=\sum_{p\in\mathfrak C}\mathrm{carlesonOn}(p, g)(x)$, where $\mathrm{carlesonOn}(p,\cdot)$ is the project operator `carlesonOn` (docstring: the operator $T_p$ defined in Proposition 2.0.2). Let $\mathfrak P_{\mathrm{pos}}\subseteq\mathfrak P(X)$ be the project set `𝔓pos` (docstring: the set $\mathfrak P_{G\setminus G'}$ in the blueprint). All integrals below are lower Lebesgue integrals with respect to $\mu$ of extended nonnegative norms $\|\cdot\|_e\in[0,\infty]$, and all right-hand sides are computed in $[0,\infty]$. Let $\bar q\in\mathbb R_{\ge 0}$ denote $q$ regarded as a nonnegative real (the project value `nnq X`). Let $N\in\mathbb N$ be the project number `maxℭ X`, defined (by choice) so that $n\le N$ whenever the project set $\mathfrak C(k,n)$ (`ℭ k n`) is nonempty for some $k$; let $Z=\mathrm{defaultZ}(a)=2^{12a}$. For $k,n,j,l\in\mathbb N$ let: $\mathfrak L_0'(k,n,l)$ be the $l$-th minimal layer of the project set $\mathfrak L_0(k,n)$ (`𝔏₀ k n`), i.e. the project set `𝔏₀' k n l`; $\mathfrak L_1(k,n,j,l)$ be the $l$-th minimal layer of the project set $\mathfrak C_1(k,n,j)$ (`ℭ₁ k n j`), i.e. `𝔏₁ k n j l`; $\mathfrak L_2(k,n,j)$ be the project set `𝔏₂ k n j` (docstring: the subset of $\mathfrak C_2(k,n,j)$ given in (5.1.15)); and $\mathfrak L_3(k,n,j,l)$ be the $l$-th maximal layer of the project set $\mathfrak C_3(k,n,j)$ (`ℭ₃ k n j`), i.e. `𝔏₃ k n j l`. Let $f : X\to\mathbb C$ be measurable, and for $\mathfrak A\subseteq\mathfrak P(X)$ write $I(\mathfrak A)=\int_{G\setminus G'}\|\mathrm{carlesonSum}(\mathfrak P_{\mathrm{pos}}\cap\mathfrak P_1^c\cap\mathfrak A, f)(x)\|_e\,d\mu(x)$. Then, with all summation indices ranging over natural numbers, $$\int_{G\setminus G'}\|\mathrm{carlesonSum}(\mathfrak P_1^c, f)(x)\|_e\,d\mu(x)\le \sum_{n\le N}\sum_{k\le n}\sum_{l<n} I(\mathfrak L_0'(k,n,l)) + \sum_{n\le N}\sum_{k\le n}\sum_{j\le 2n+3}\sum_{l\le Z(n+1)} I(\mathfrak L_1(k,n,j,l)) + \sum_{n\le N}\sum_{k\le n}\sum_{j\le 2n+3} I(\mathfrak L_2(k,n,j)) + \sum_{n\le N}\sum_{k\le n}\sum_{j\le 2n+3}\sum_{l\le Z(n+1)} I(\mathfrak L_3(k,n,j,l)).$$

### `lintegral_enorm_carlesonSum_le_of_isAntichain_subset_ℭ`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) (hA : IsAntichain (fun x1 x2 => x1 ≤ x2) 𝔄) (h'A : 𝔄 ⊆ ℭ k n) : ∫⁻ (x : X) in G \ G', ‖carlesonSum (𝔓pos ∩ 𝔓₁ᶜ ∩ 𝔄) f x‖ₑ ≤ ↑(C2_0_3 a (nnq X)) * 2 ^ (a + 3) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹ * 2 ^ (-((q - 1) / (8 * ↑a ^ 4) * ↑n))`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {k n : ℕ} {f : X → ℂ} {𝔄 : Set (𝔓 X)}, (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable f → IsAntichain (fun (x1 x2 : 𝔓 X) => x1 ≤ x2) 𝔄 → 𝔄 ⊆ ℭ (F := F) (G := G) k n → ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (𝔓pos (F := F) (G := G) ∩ (𝔓₁ (F := F) (G := G))ᶜ ∩ 𝔄) f x‖ₑ ≤ ↑(C2_0_3 a (nnq X (F := F) (G := G))) * (2 : ENNReal) ^ (a + (3 : ℕ)) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹ * (2 : ENNReal) ^ (-((q - (1 : ℝ)) / ((8 : ℝ) * HPow.hPow (α := ℝ) ↑a (4 : ℕ)) * ↑n))`
Docstring: Custom version of the antichain operator theorem, in the specific form we need to handle the various terms in the previous statement.
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7). Through this instance $X$ carries a `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$, whose measure (`volume`) we denote by $\mu$, and a `CompatibleFunctions ℝ X (2^a)` structure, which provides a type $\Theta(X)$ of continuous real-valued functions on $X$; let $Q : X\to\Theta(X)$ be the simple function given by the field `Q` of the `ProofData` instance. Let $\mathsf b\in\mathbb N$ be the project constant `𝕔` (per its docstring fixed equal to $100$), $D=\mathrm{defaultD}(a)=2^{\mathsf b a^2}$, $\kappa=\mathrm{default}\kappa(a)=2^{-10a}$, $S=\mathrm{defaultS}(X)\in\mathbb N$ (the natural number `defaultS` determined by the `ProofData`), and $o=\mathrm{cancelPt}(X)\in X$ (the point `cancelPt X`, chosen so that every function in $\Theta(X)$ vanishes at it). Assume a tile structure `TileStructure Q D κ S o` on $X$, and let $\mathfrak P(X)$ be its (finite) type of tiles, partially ordered by the project order `instPartialOrder𝔓Real`. Let $G'\subseteq X$ be the project set `G'` (docstring: the set $G'$ defined below (5.1.28)), defined as $G_1\cup G_2\cup G_3$ for the project sets `G₁`, `G₂`, `G₃`. Let $\mathfrak P_1\subseteq\mathfrak P(X)$ be the project set `𝔓₁` (docstring: the set $\mathfrak P_1$ defined in (5.1.30)), defined as $\bigcup_{n\in\mathbb N}\bigcup_{k\le n}\bigcup_{j\le 2n+3}\mathfrak C_5(k,n,j)$, where $\mathfrak C_5(k,n,j)$ is the project set `ℭ₅ k n j`, and write $\mathfrak P_1^c$ for its complement in $\mathfrak P(X)$. For a set of tiles $\mathfrak C\subseteq\mathfrak P(X)$, a function $g : X\to\mathbb C$ and $x\in X$, let $\mathrm{carlesonSum}(\mathfrak C, g)(x)=\sum_{p\in\mathfrak C}\mathrm{carlesonOn}(p, g)(x)$, where $\mathrm{carlesonOn}(p,\cdot)$ is the project operator `carlesonOn` (docstring: the operator $T_p$ defined in Proposition 2.0.2). Let $\mathfrak P_{\mathrm{pos}}\subseteq\mathfrak P(X)$ be the project set `𝔓pos` (docstring: the set $\mathfrak P_{G\setminus G'}$ in the blueprint). All integrals below are lower Lebesgue integrals with respect to $\mu$ of extended nonnegative norms $\|\cdot\|_e\in[0,\infty]$, and all right-hand sides are computed in $[0,\infty]$. Let $\bar q\in\mathbb R_{\ge 0}$ denote $q$ regarded as a nonnegative real (the project value `nnq X`). For $k,n\in\mathbb N$ let $\mathfrak C(k,n)\subseteq\mathfrak P(X)$ be the project set `ℭ k n` (docstring: the partition $\mathfrak C(k,n)$ of $\mathfrak P(k)$ by density, (5.1.7)), i.e. the set of tiles $p$ in the project set `TilesAt k` whose project density `dens' k {p}` lies in $(2^{4a-n}, 2^{4a-n+1}]$. Let $C_{2.0.3}(a,\bar q)\in\mathbb R_{\ge0}$ be the project constant `C2_0_3 a (nnq X)`, namely $2^{(\mathsf b+5+\lfloor\mathsf b/8\rfloor)a^3}/(\bar q-1)$ computed in $\mathbb R_{\ge0}$ (with truncated subtraction). Let $k,n\in\mathbb N$, let $f : X\to\mathbb C$ be measurable with $\|f(x)\|\le\mathbf 1_F(x)$ for all $x\in X$, and let $\mathfrak A\subseteq\mathfrak P(X)$ be an antichain for the partial order $\le$ on $\mathfrak P(X)$ with $\mathfrak A\subseteq\mathfrak C(k,n)$. Then $$\int_{G\setminus G'}\big\|\mathrm{carlesonSum}(\mathfrak P_{\mathrm{pos}}\cap\mathfrak P_1^c\cap\mathfrak A, f)(x)\big\|_e\,d\mu(x)\le C_{2.0.3}(a,\bar q)\,2^{a+3}\,\mu(G)^{1-q^{-1}}\,\mu(F)^{q^{-1}}\,2^{-\frac{q-1}{8a^4}n}.$$

### `forest_complement_optimized`
Lean (short): `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : ∀ (x : X), ‖f x‖ ≤ F.indicator 1 x) (h'f : Measurable f) : ∫⁻ (x : X) in G \ G', ‖carlesonSum 𝔓₁ᶜ f x‖ₑ ≤ ↑(C5_1_3_optimized a (nnq X)) * volume G ^ (1 - q⁻¹) * volume F ^ q⁻¹`
Lean (full): `∀ {X : Type u_1} {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst : MetricSpace X] [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : TileStructure (Q (F := F) (G := G)) (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {f : X → ℂ}, (∀ (x : X), ‖f x‖ ≤ F.indicator (1 : X → ℝ) x) → Measurable f → ∫⁻ (x : X) in G \ G' (F := F) (G := G), ‖carlesonSum (F := F) (G := G) (𝔓₁ (F := F) (G := G))ᶜ f x‖ₑ ≤ ↑(C5_1_3_optimized a (nnq X (F := F) (G := G))) * HPow.hPow (α := ENNReal) ((volume : Measure X) G : ENNReal) ((1 : ℝ) - q⁻¹) * HPow.hPow (α := ENNReal) ((volume : Measure X) F : ENNReal) q⁻¹`
English: Let $X$ be a metric space. Let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\to X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, and assume an instance of the project structure `ProofData a q K σ₁ σ₂ F G` (docstring: data common through most of chapters 2-7). Through this instance $X$ carries a `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$, whose measure (`volume`) we denote by $\mu$, and a `CompatibleFunctions ℝ X (2^a)` structure, which provides a type $\Theta(X)$ of continuous real-valued functions on $X$; let $Q : X\to\Theta(X)$ be the simple function given by the field `Q` of the `ProofData` instance. Let $\mathsf b\in\mathbb N$ be the project constant `𝕔` (per its docstring fixed equal to $100$), $D=\mathrm{defaultD}(a)=2^{\mathsf b a^2}$, $\kappa=\mathrm{default}\kappa(a)=2^{-10a}$, $S=\mathrm{defaultS}(X)\in\mathbb N$ (the natural number `defaultS` determined by the `ProofData`), and $o=\mathrm{cancelPt}(X)\in X$ (the point `cancelPt X`, chosen so that every function in $\Theta(X)$ vanishes at it). Assume a tile structure `TileStructure Q D κ S o` on $X$, and let $\mathfrak P(X)$ be its (finite) type of tiles, partially ordered by the project order `instPartialOrder𝔓Real`. Let $G'\subseteq X$ be the project set `G'` (docstring: the set $G'$ defined below (5.1.28)), defined as $G_1\cup G_2\cup G_3$ for the project sets `G₁`, `G₂`, `G₃`. Let $\mathfrak P_1\subseteq\mathfrak P(X)$ be the project set `𝔓₁` (docstring: the set $\mathfrak P_1$ defined in (5.1.30)), defined as $\bigcup_{n\in\mathbb N}\bigcup_{k\le n}\bigcup_{j\le 2n+3}\mathfrak C_5(k,n,j)$, where $\mathfrak C_5(k,n,j)$ is the project set `ℭ₅ k n j`, and write $\mathfrak P_1^c$ for its complement in $\mathfrak P(X)$. For a set of tiles $\mathfrak C\subseteq\mathfrak P(X)$, a function $g : X\to\mathbb C$ and $x\in X$, let $\mathrm{carlesonSum}(\mathfrak C, g)(x)=\sum_{p\in\mathfrak C}\mathrm{carlesonOn}(p, g)(x)$, where $\mathrm{carlesonOn}(p,\cdot)$ is the project operator `carlesonOn` (docstring: the operator $T_p$ defined in Proposition 2.0.2). Let $\mathfrak P_{\mathrm{pos}}\subseteq\mathfrak P(X)$ be the project set `𝔓pos` (docstring: the set $\mathfrak P_{G\setminus G'}$ in the blueprint). All integrals below are lower Lebesgue integrals with respect to $\mu$ of extended nonnegative norms $\|\cdot\|_e\in[0,\infty]$, and all right-hand sides are computed in $[0,\infty]$. Let $\bar q\in\mathbb R_{\ge 0}$ denote $q$ regarded as a nonnegative real (the project value `nnq X`). Let $C^{\mathrm{opt}}(a,\bar q)\in\mathbb R_{\ge0}$ be the project constant `C5_1_3_optimized a (nnq X)`, namely $C_{2.0.3}(a,\bar q)\cdot 2^{29a+23}/(\bar q-1)^4$ computed in $\mathbb R_{\ge 0}$ (with truncated subtraction), where $C_{2.0.3}(a,\bar q)=2^{(\mathsf b+5+\lfloor\mathsf b/8\rfloor)a^3}/(\bar q-1)$ is the project constant `C2_0_3`. Let $f : X\to\mathbb C$ be measurable with $\|f(x)\|\le\mathbf 1_F(x)$ for all $x\in X$. Then $$\int_{G\setminus G'}\big\|\mathrm{carlesonSum}(\mathfrak P_1^c, f)(x)\big\|_e\,d\mu(x)\le C^{\mathrm{opt}}(a,\bar q)\,\mu(G)^{1-q^{-1}}\,\mu(F)^{q^{-1}}.$$
