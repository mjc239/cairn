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

#### `C2_1_2` (def)
Lean: `ℕ → ℝ`
Docstring: The constant appearing in Lemma 2.1.2, `2 ^ {-95a}`.
Definition: `fun (a : ℕ) => (2 : ℝ) ^ ((-↑𝕔 + (5 : ℝ)) * ↑a)`

#### `CompatibleFunctions.toFunctionDistances` (def)
Lean: `{𝕜 : outParam (Type u_3)} → {X : Type u} → {A : outParam ℕ} → {inst : RCLike 𝕜} → {inst_1 : PseudoMetricSpace X} → [self : CompatibleFunctions 𝕜 X A] → FunctionDistances 𝕜 X`
Definition: `fun {𝕜 : outParam (Type u_3)} (X : Type u) {A : outParam ℕ} {inst : RCLike 𝕜} {inst_1 : PseudoMetricSpace X} [self : CompatibleFunctions 𝕜 X A] => self.1`

#### `FunctionDistances.Θ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → (X : Type u) → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → Type u`
Docstring: A type of continuous functions from `X` to `𝕜`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.1`

#### `Grid` (def)
Lean: `(X : Type u) → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [GridStructure X D κ S o] → Type u`
Docstring: The indexing type of the grid structure. Elements are called (dyadic) cubes. Note that this type has instances for both `≤` and `⊆`, but they do *not* coincide.
Definition: `fun (X : Type u) {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => @GridStructure.Grid X _ inst inst_1 _ _ _ _ _`

#### `GridStructure` (structure or class)
Lean: `(X : Type u_2) → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [DoublingMeasure X A] → outParam ℕ → outParam ℝ → outParam ℕ → outParam X → Type (max (u + 1) u_2)`
Docstring: A grid structure on `X`. We prefer `coeGrid : Grid → Set X` over `Grid : Set (Set X)` Note: the `s` in this paper is `-s` of Christ's paper.
Constructor (every field with its type): `{X : Type u_2} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → (Grid : Type u) → Fintype Grid → (coeGrid : Grid → Set X) → (s : Grid → ℤ) → (c : Grid → X) → (Function.Injective.{u + 1, max 1 (u_2 + 1)} (β := Set X × ℤ) fun (i : Grid) => (coeGrid i, s i)) → Set.range s ⊆ Set.Icc (-↑S) ↑S → (topCube : Grid) → s topCube = ↑S → c topCube = o → (∀ {i : Grid}, coeGrid i ⊆ coeGrid topCube) → (∀ {i : Grid}, ∀ k ∈ Set.Ico (-↑S) (s i), coeGrid i ⊆ ⋃ j ∈ s ⁻¹' {k}, coeGrid j) → (∀ {i j : Grid}, s i ≤ s j → coeGrid i ⊆ coeGrid j ∨ Disjoint (coeGrid i) (coeGrid j)) → (∀ {i : Grid}, Metric.ball (c i) (HPow.hPow (α := ℝ) (↑D) (s i) / (4 : ℝ)) ⊆ coeGrid i) → (∀ {i : Grid}, coeGrid i ⊆ Metric.ball (c i) ((4 : ℝ) * HPow.hPow (α := ℝ) (↑D) (s i))) → (∀ {i : Grid} {t : NNReal}, HPow.hPow (α := NNReal) (↑D) (-↑S - s i) ≤ t → Measure.real.{u_2} (α := X) (m := MeasureSpace.toMeasurableSpace) volume {x : X | x ∈ coeGrid i ∧ Metric.infEDist x (coeGrid i)ᶜ ≤ ↑t * HPow.hPow (α := ENNReal) (↑D) (s i)} ≤ (2 : ℝ) * ↑t ^ κ * Measure.real (m := MeasureSpace.toMeasurableSpace) volume (coeGrid i)) → (∀ {i : Grid}, MeasurableSet (coeGrid i)) → GridStructure.{u, u_2} X D κ S o`

#### `KernelProofData.cf` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → {inst : PseudoMetricSpace X} → [self : KernelProofData a K] → CompatibleFunctions ℝ X (defaultA a)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {K : outParam (X → X → ℂ)} {inst : PseudoMetricSpace X} [self : KernelProofData a K] => self.3`

#### `KernelProofData.d` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → {inst : PseudoMetricSpace X} → [self : KernelProofData a K] → DoublingMeasure X ↑(defaultA a)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {K : outParam (X → X → ℂ)} {inst : PseudoMetricSpace X} [self : KernelProofData a K] => self.1`

#### `ProofData` (structure or class)
Lean: `{X : Type u_1} → outParam ℕ → outParam ℝ → outParam (X → X → ℂ) → outParam (X → ℤ) → outParam (X → ℤ) → outParam (Set X) → outParam (Set X) → [PseudoMetricSpace X] → Type (u_1 + 1)`
Docstring: Data common through most of chapters 2-7 (except 3).
Constructor (every field with its type): `{X : Type u_1} → {a : outParam ℕ} → {q : outParam ℝ} → {K : outParam (X → X → ℂ)} → {σ₁ σ₂ : outParam (X → ℤ)} → {F G : outParam (Set X)} → [inst : PseudoMetricSpace X] → [toKernelProofData : KernelProofData a K] → IsCancellative X (defaultτ a) → q ∈ Set.Ioc (1 : outParam ℝ) (2 : outParam ℝ) → Bornology.IsBounded F → Bornology.IsBounded G → MeasurableSet F → MeasurableSet G → Measurable σ₁ → Measurable σ₂ → Finite ↑(Set.range σ₁) → Finite ↑(Set.range σ₂) → σ₁ ≤ σ₂ → (Q : SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)) → (∀ (θ : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _), HasBoundedStrongType (ε₁ := ℂ) (ε₂ := ENNReal) (α := X) (_x := MeasureSpace.toMeasurableSpace) (_x' := MeasureSpace.toMeasurableSpace) (fun (x1 : X → ℂ) (x2 : X) => linearizedNontangentialOperator (⇑Q) θ K x1 x2) (2 : ENNReal) (2 : ENNReal) volume volume ↑(C_Ts a)) → ProofData a q K σ₁ σ₂ F G`

#### `ProofData.toKernelProofData` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {q : outParam ℝ} → {K : outParam (X → X → ℂ)} → {σ₁ σ₂ : outParam (X → ℤ)} → {F G : outParam (Set X)} → {inst : PseudoMetricSpace X} → [self : ProofData a q K σ₁ σ₂ F G] → KernelProofData a K`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {q : outParam ℝ} {K : outParam (X → X → ℂ)} {σ₁ σ₂ : outParam (X → ℤ)} {F G : outParam (Set X)} {inst : PseudoMetricSpace X} [self : ProofData a q K σ₁ σ₂ F G] => self.1`

#### `WithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → X → ℝ → Type u_2`
Docstring: Class used to endow `Θ X` with a pseudometric space structure.
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] (x : X) (r : ℝ) => @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _`

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

#### `instPartialOrderGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → PartialOrder (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => PartialOrder.lift (fun (i : @GridStructure.Grid X _ inst inst_1 _ _ _ _ _) => (↑i, GridStructure.s i)) ⋯`

#### `instPseudoMetricSpaceWithFunctionDistance` (def)
Lean: `{𝕜 : Type u_1} → {X : Type u_2} → [inst : RCLike 𝕜] → [inst_1 : PseudoMetricSpace X] → [d : FunctionDistances 𝕜 X] → {x : X} → {r : ℝ} → PseudoMetricSpace (WithFunctionDistance x r)`
Definition: `fun {𝕜 : Type u_1} {X : Type u_2} [RCLike 𝕜] [PseudoMetricSpace X] [FunctionDistances 𝕜 X] {x : X} {r : ℝ} => FunctionDistances.metric x r`

#### `s` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Grid X → ℤ`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.s`

#### `instFintypeGrid` (def)
Lean: `{X : Type u} → {A : NNReal} → [inst : PseudoMetricSpace X] → [inst_1 : DoublingMeasure X A] → {D : ℕ} → {κ : ℝ} → {S : ℕ} → {o : X} → [inst_2 : GridStructure X D κ S o] → Fintype (Grid X)`
Definition: `fun {X : Type u} {A : NNReal} [PseudoMetricSpace X] [DoublingMeasure X A] {D : ℕ} {κ : ℝ} {S : ℕ} {o : X} [GridStructure X D κ S o] => GridStructure.fintype_Grid`

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

#### `GridStructure.Grid` (def)
Lean: `(X : Type u_2) → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → Type u`
Docstring: indexing set for a grid structure
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.1`

#### `MeasureTheory.DoublingMeasure` (structure or class)
Lean: `(X : Type u_3) → outParam NNReal → [PseudoMetricSpace X] → Type u_3`
Docstring: A metric space with a measure with some nice properties, including a doubling condition. This is called a "doubling metric measure space" in the blueprint. `A` will usually be `2 ^ a`.
Constructor (every field with its type): `{X : Type u_3} → {A : outParam NNReal} → [inst : PseudoMetricSpace X] → [toCompleteSpace : CompleteSpace X] → [toLocallyCompactSpace : LocallyCompactSpace X] → [toMeasureSpace : MeasureSpace X] → [toBorelSpace : BorelSpace X] → [toIsLocallyFiniteMeasure : IsLocallyFiniteMeasure.{u_3} (α := X) (m0 := MeasureSpace.toMeasurableSpace) volume] → [toIsDoubling : Measure.IsDoubling.{u_3} (X := X) volume A] → [toNeZero : NeZero.{u_3} (R := Measure X) volume] → DoublingMeasure X A`

#### `GridStructure.coeGrid` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → Set X`
Docstring: The collection of dyadic cubes
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.3`

#### `GridStructure.s` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → ℤ`
Docstring: scale functions
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.4`

#### `MeasureTheory.DoublingMeasure.toMeasureSpace` (def)
Lean: `{X : Type u_3} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → [self : DoublingMeasure X A] → MeasureSpace X`
Definition: `fun (X : Type u_3) {A : outParam NNReal} {inst : PseudoMetricSpace X} [self : DoublingMeasure X A] => self.3`

#### `GridStructure.c` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _ → X`
Docstring: Center functions
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.5`

#### `GridStructure.topCube` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → @GridStructure.Grid X _ inst inst_1 _ _ _ _ _`
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.8`

#### `KernelProofData` (structure or class)
Lean: `{X : Type u_1} → outParam ℕ → outParam (X → X → ℂ) → [PseudoMetricSpace X] → Type (u_1 + 1)`
Docstring: Data common through most of chapters 2 through 7. These contain the minimal axioms for `kernel-summand`'s proof. This is used in Chapter 3 when we don't have all other fields from `ProofData`.
Constructor (every field with its type): `{X : Type u_1} → {a : outParam ℕ} → {K : outParam (X → X → ℂ)} → [inst : PseudoMetricSpace X] → (d : DoublingMeasure X ↑(defaultA a)) → (4 : ℕ) ≤ a → CompatibleFunctions ℝ X (defaultA a) → IsOneSidedKernel a K → KernelProofData a K`

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

#### `ProofData.Q` (def)
Lean: `{X : Type u_1} → {a : outParam ℕ} → {q : outParam ℝ} → {K : outParam (X → X → ℂ)} → {σ₁ σ₂ : outParam (X → ℤ)} → {F G : outParam (Set X)} → {inst : PseudoMetricSpace X} → [self : ProofData a q K σ₁ σ₂ F G] → SimpleFunc X (@Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _)`
Definition: `fun (X : Type u_1) {a : outParam ℕ} {q : outParam ℝ} {K : outParam (X → X → ℂ)} {σ₁ σ₂ : outParam (X → ℤ)} {F G : outParam (Set X)} {inst : PseudoMetricSpace X} [self : ProofData a q K σ₁ σ₂ F G] => self.13`

#### `FunctionDistances.coeΘ` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → @Θ _ X inst inst_1 _ → C(X, 𝕜)`
Docstring: The coercion map from `Θ` to `C(X, 𝕜)`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.2`

#### `FunctionDistances.metric` (def)
Lean: `{𝕜 : outParam (Type u_1)} → {X : Type u} → {inst : NormedField 𝕜} → {inst_1 : TopologicalSpace X} → [self : FunctionDistances 𝕜 X] → X → ℝ → PseudoMetricSpace (@Θ _ X inst inst_1 _)`
Docstring: For each `_x : X` and `_r : ℝ`, a `PseudoMetricSpace Θ`.
Definition: `fun {𝕜 : outParam (Type u_1)} (X : Type u) {inst : NormedField 𝕜} {inst_1 : TopologicalSpace X} [self : FunctionDistances 𝕜 X] => self.4`

#### `GridStructure.fintype_Grid` (def)
Lean: `{X : Type u_2} → {A : outParam NNReal} → {inst : PseudoMetricSpace X} → {inst_1 : DoublingMeasure X A} → {D : outParam ℕ} → {κ : outParam ℝ} → {S : outParam ℕ} → {o : outParam X} → [self : GridStructure.{u, u_2} X D κ S o] → Fintype (@GridStructure.Grid X _ inst inst_1 _ _ _ _ _)`
Definition: `fun (X : Type u_2) {A : outParam NNReal} {inst : PseudoMetricSpace X} {inst_1 : DoublingMeasure X A} {D : outParam ℕ} {κ : outParam ℝ} {S : outParam ℕ} {o : outParam X} [self : GridStructure.{u, u_2} X D κ S o] => self.2`

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

## Translations

### `Grid.dist_strictMono`
Lean (short): `[GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
Lean (full): `∀ {X : Type u_1} [inst : PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : GridStructure X (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {I J : Grid X}, I < J → ∀ {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, dist_{c I, ↑(defaultD a) ^ s I / (4 : ℝ)} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / (4 : ℝ)} f g`
Docstring: Stronger version of Lemma 2.1.2.
English: (Stronger version of Lemma 2.1.2.) Let $X$ be a pseudometric space, and let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\times X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, such that $X$ carries a `ProofData` structure with parameters $(a,q,K,\sigma_1,\sigma_2,F,G)$ (per its docstring, the data common through most of chapters 2-7). Through this structure $X$ carries a `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$ and a `CompatibleFunctions` structure over $\mathbb R$ with constant $2^a$. Let $\mathfrak c\in\mathbb N$ be the project's fixed constant `𝕔` (per its docstring, fixed equal to $100$), let $D=\mathrm{defaultD}(a)=2^{\mathfrak c a^2}\in\mathbb N$, $\kappa=\mathrm{default}\kappa(a)=2^{-10a}\in\mathbb R$, let $S=\mathrm{defaultS}(X)\in\mathbb N$ be the least natural number $n>0$ such that $-n\le\sigma_1(x)$ and $\sigma_2(x)\le n$ for all $x\in X$ and $F$ and $G$ are both contained in the open ball of radius $D^n/4$ about $o$, where $o=\mathrm{cancelPt}(X)\in X$ is a point chosen so that every function in $\Theta(X)$ (below) vanishes at $o$. Assume moreover that $X$ carries a `GridStructure` with parameters $(D,\kappa,S,o)$, and let $\mathrm{Grid}(X)$ be the indexing type of this grid structure. For $I\in\mathrm{Grid}(X)$ let $c(I)\in X$ and $s(I)\in\mathbb Z$ be the values at $I$ of the grid structure's center function $c$ and scale function $s$, and let $[I]\subseteq X$ be the set attached to $I$ by the grid structure's map `coeGrid`. Order $\mathrm{Grid}(X)$ by: $I\le J$ iff $[I]\subseteq[J]$ and $s(I)\le s(J)$ (the partial order lifted from the pair $([I],s(I))$), and $I<J$ iff $I\le J$ and $I\ne J$. Let $\Theta(X)$ be the type of functions of the `FunctionDistances` structure on $X$ (over $\mathbb R$) supplied by the compatible-functions structure (per its docstring, a type of continuous functions $X\to\mathbb R$), and for $x\in X$ and $r\in\mathbb R$ let $d_{x,r}$ denote the pseudometric on $\Theta(X)$ that this `FunctionDistances` structure associates with $(x,r)$. Let $C_{2.1.2}(a)=2^{(5-\mathfrak c)a}\in\mathbb R$. Let $I,J\in\mathrm{Grid}(X)$ with $I<J$. Then for all $f,g\in\Theta(X)$, $$d_{c(I),\,D^{s(I)}/4}(f,g)\le C_{2.1.2}(a)\,d_{c(J),\,D^{s(J)}/4}(f,g).$$

### `Grid.succ`
Lean (short): `[GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (i : Grid X) : Grid X`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : GridStructure X (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Grid X → Grid X`
Definition: `fun {X : Type u_1} [PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [ProofData a q K σ₁ σ₂ F G] [GridStructure X (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] (i : Grid X) => if h : IsMax i then i else Finset.choose (fun (a_1 : Grid X) => i < a_1 ∧ ∀ (j' : Grid X), i < j' → a_1 ≤ j') Finset.univ ⋯`
Docstring: If `i` is not a maximal element, this is the (unique) minimal element greater than i. This is not a `SuccOrder` since an element can be the successor of multiple other elements.
English: Let $X$ be a pseudometric space, and let $a\in\mathbb N$, $q\in\mathbb R$, $K : X\times X\to\mathbb C$, $\sigma_1,\sigma_2 : X\to\mathbb Z$ and $F,G\subseteq X$, such that $X$ carries a `ProofData` structure with parameters $(a,q,K,\sigma_1,\sigma_2,F,G)$ (per its docstring, the data common through most of chapters 2-7). Through this structure $X$ carries a `DoublingMeasure` structure with constant $\mathrm{defaultA}(a)=2^a$ and a `CompatibleFunctions` structure over $\mathbb R$ with constant $2^a$. Let $\mathfrak c\in\mathbb N$ be the project's fixed constant `𝕔` (per its docstring, fixed equal to $100$), let $D=\mathrm{defaultD}(a)=2^{\mathfrak c a^2}\in\mathbb N$, $\kappa=\mathrm{default}\kappa(a)=2^{-10a}\in\mathbb R$, let $S=\mathrm{defaultS}(X)\in\mathbb N$ be the least natural number $n>0$ such that $-n\le\sigma_1(x)$ and $\sigma_2(x)\le n$ for all $x\in X$ and $F$ and $G$ are both contained in the open ball of radius $D^n/4$ about $o$, where $o=\mathrm{cancelPt}(X)\in X$ is a point chosen so that every function in $\Theta(X)$ vanishes at $o$, $\Theta(X)$ being the type of functions of the `FunctionDistances` structure on $X$ supplied by the compatible-functions structure. Assume moreover that $X$ carries a `GridStructure` with parameters $(D,\kappa,S,o)$, and let $\mathrm{Grid}(X)$ be the indexing type of this grid structure. Order $\mathrm{Grid}(X)$ by its partial order: $i\le j$ iff the set attached to $i$ by the grid structure's map `coeGrid` is contained in the set attached to $j$ and $s(i)\le s(j)$, where $s$ is the grid structure's scale function. Definition: for $i\in\mathrm{Grid}(X)$, an element $\mathrm{succ}(i)\in\mathrm{Grid}(X)$. According to the docstring, if $i$ is not a maximal element, this is the (unique) minimal element greater than $i$; this is not a successor order, since an element can be the successor of multiple other elements.
