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

#### `CMB` (def)
Lean: `NNReal → NNReal → NNReal`
Docstring: The constant factor in the statement that `M_𝓑` has strong type.
Definition: `fun (A p : NNReal) => C_realInterpolation ⊤ (1 : ENNReal) ⊤ (1 : ENNReal) ↑p (1 : NNReal) (A ^ (2 : ℕ)) (1 : NNReal) (↑p)⁻¹`

#### `MeasureTheory.HasStrongType` (def)
Lean: `{ε₁ : Type u_4} → {ε₂ : Type u_5} → [ENorm ε₁] → [ENorm ε₂] → [TopologicalSpace ε₁] → [TopologicalSpace ε₂] → {α : Type u_12} → {α' : Type u_13} → {_x : MeasurableSpace α} → {_x' : MeasurableSpace α'} → ((α → ε₁) → α' → ε₂) → ENNReal → ENNReal → Measure α → Measure α' → ENNReal → Prop`
Docstring: An operator has strong type `(p, q)` if it is bounded as an operator on `L^p → L^q`. `HasStrongType T p p' μ ν c` means that `T` has strong type (p, p') w.r.t. measures `μ`, `ν` and constant `c`.
Definition: `fun {ε₁ : Type u_4} {ε₂ : Type u_5} [ENorm ε₁] [ENorm ε₂] [TopologicalSpace ε₁] [TopologicalSpace ε₂] {α : Type u_12} {α' : Type u_13} {_x : MeasurableSpace α} {_x' : MeasurableSpace α'} (T : (α → ε₁) → α' → ε₂) (p p' : ENNReal) (μ : Measure α) (ν : Measure α') (c : ENNReal) => ∀ (f : α → ε₁), MemLp f p μ → AEStronglyMeasurable (T f) ν ∧ eLpNorm (T f) p' ν ≤ c * eLpNorm f p μ`

#### `MeasureTheory.Measure.IsDoubling` (structure or class)
Lean: `{X : Type u_3} → [inst : MeasurableSpace X] → [PseudoMetricSpace X] → Measure X → outParam NNReal → Prop`
Docstring: A doubling measure is a measure on a metric space with the condition that doubling the radius of a ball only increases the volume by a constant factor, independent of the ball.
Fields: `x`, `r`, `2`, `β`

#### `instContinuousENormNNReal_carleson` (def)
Lean: `ContinuousENorm NNReal`
Definition: `{ toENorm := NNNorm.toENorm, continuous_enorm := instContinuousENormNNReal_carleson._proof_1 }`

#### `maximalFunction` (def)
Lean: `{X : Type u_1} → {ε : Type u_2} → [PseudoMetricSpace X] → [inst : MeasurableSpace X] → [ENorm ε] → {ι : Type u_4} → Measure X → Set ι → (ι → X) → (ι → ℝ) → ℝ → (X → ε) → X → ENNReal`
Docstring: The uncentered Hardy-Littlewood maximal function, for a family of balls.
Definition: `fun {X : Type u_1} {ε : Type u_2} [PseudoMetricSpace X] [MeasurableSpace X] [ENorm ε] {ι : Type u_4} (μ : Measure X) (𝓑 : Set ι) (c : ι → X) (r : ι → ℝ) (p : ℝ) (u : X → ε) (x : X) => ⨆ i ∈ 𝓑, (Metric.ball (c i) (r i)).indicator (fun (x : X) => (⨍⁻ (y : X) in Metric.ball (c i) (r i), ‖u y‖ₑ ^ p ∂μ) ^ p⁻¹) x`

#### `MeasureTheory.C_realInterpolation` (def)
Lean: `ENNReal → ENNReal → ENNReal → ENNReal → ENNReal → NNReal → NNReal → NNReal → ENNReal → NNReal`
Docstring: The constant occurring in the real interpolation theorem
Definition: `fun (p₀ p₁ q₀ q₁ q : ENNReal) (C₀ C₁ A : NNReal) (t : ENNReal) => (C_realInterpolation_ENNReal p₀ p₁ q₀ q₁ q C₀ C₁ A t).toNNReal`

## Flagged translations

### `hasStrongType_maximalFunction_one`
Lean (short): `[μ.IsDoubling A] [SMul NNReal ε'] [ENormSMulClass NNReal ε'] [TopologicalSpace.PseudoMetrizableSpace ε'] [BorelSpace ε'] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] (hp : 1 < p) : HasStrongType (maximalFunction μ 𝓑 c r 1) (↑p) (↑p) μ μ ↑(CMB A p)`
Lean (full): `∀ {X : Type u_1} {ε' : Type u_3} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : MeasurableSpace X] {μ : Measure X} [μ.IsDoubling A] {ι : Type u_4} {𝓑 : Set ι} {c : ι → X} {r : ι → ℝ} [inst_3 : TopologicalSpace ε'] [inst_4 : ESeminormedAddMonoid ε'] [inst_5 : SMul NNReal ε'] [ENormSMulClass NNReal ε'] [TopologicalSpace.PseudoMetrizableSpace ε'] [inst_8 : MeasurableSpace ε'] [BorelSpace ε'] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] {p : NNReal}, (1 : NNReal) < p → HasStrongType.{u_3, 0, u_1, u_1} (ε₁ := ε') (maximalFunction μ 𝓑 c r (1 : ℝ)) (↑p) (↑p) μ μ ↑(CMB A p)`
Docstring: Special case of equation (2.0.44). The proof is given between (9.0.12) and (9.0.34). Use the real interpolation theorem instead of following the blueprint.
Previous English: Let $X$ be a proper pseudometric space with its Borel $\sigma$-algebra, and let $\mu$ be a measure on $X$ that is doubling with constant $A \ge 0$, finite on compact sets, and positive on nonempty open sets. Let $\mathcal{B}$ be a set of indices $i \in \iota$ with centers $c : \iota \to X$ and radii $r : \iota \to \mathbb{R}$. Let the target space $\varepsilon'$ be an extended-seminormed additive monoid (with its topology), which is pseudo-metrizable, carries its Borel $\sigma$-algebra, and has a scalar action of $\mathbb{R}_{\ge 0}$ compatible with the extended norm ($\|c\cdot x\|_e = c\,\|x\|_e$). If $p \in \mathbb{R}_{\ge 0}$ satisfies $p > 1$, then the maximal function $\mathrm{maximalFunction}(\mu, \mathcal{B}, c, r, 1)$ (acting on $\varepsilon'$-valued functions) has strong type $(p, p)$ with respect to $\mu$ and $\mu$, with constant $C_{MB}(A, p)$ (a special case of (2.0.44)).
Checker's issue: The letter c means two things: the centers c : iota -> X and the scalar in ||c.x||_e = c||x||_e.
