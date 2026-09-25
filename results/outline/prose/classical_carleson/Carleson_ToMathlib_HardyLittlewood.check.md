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

#### `C2_0_6` (def)
Lean: `NNReal → NNReal → NNReal → NNReal`
Docstring: The constant factor in the statement that `M_{𝓑, p}` has strong type.
Definition: `fun (A p₁ p₂ : NNReal) => CMB A (p₂ / p₁) ^ (↑p₁)⁻¹`

#### `MeasureTheory.HasStrongType` (def)
Lean: `{ε₁ : Type u_4} → {ε₂ : Type u_5} → [ENorm ε₁] → [ENorm ε₂] → [TopologicalSpace ε₁] → [TopologicalSpace ε₂] → {α : Type u_12} → {α' : Type u_13} → {_x : MeasurableSpace α} → {_x' : MeasurableSpace α'} → ((α → ε₁) → α' → ε₂) → ENNReal → ENNReal → Measure α → Measure α' → ENNReal → Prop`
Docstring: An operator has strong type `(p, q)` if it is bounded as an operator on `L^p → L^q`. `HasStrongType T p p' μ ν c` means that `T` has strong type (p, p') w.r.t. measures `μ`, `ν` and constant `c`.
Definition: `fun {ε₁ : Type u_4} {ε₂ : Type u_5} [ENorm ε₁] [ENorm ε₂] [TopologicalSpace ε₁] [TopologicalSpace ε₂] {α : Type u_12} {α' : Type u_13} {_x : MeasurableSpace α} {_x' : MeasurableSpace α'} (T : (α → ε₁) → α' → ε₂) (p p' : ENNReal) (μ : Measure α) (ν : Measure α') (c : ENNReal) => ∀ (f : α → ε₁), MemLp f p μ → AEStronglyMeasurable (T f) ν ∧ eLpNorm (T f) p' ν ≤ c * eLpNorm f p μ`

#### `MeasureTheory.Measure.IsDoubling` (structure or class)
Lean: `{X : Type u_3} → [inst : MeasurableSpace X] → [PseudoMetricSpace X] → Measure X → outParam NNReal → Prop`
Docstring: A doubling measure is a measure on a metric space with the condition that doubling the radius of a ball only increases the volume by a constant factor, independent of the ball.
Fields: `x`, `r`, `2`, `β`

#### `maximalFunction` (def)
Lean: `{X : Type u_1} → {ε : Type u_2} → [PseudoMetricSpace X] → [inst : MeasurableSpace X] → [ENorm ε] → {ι : Type u_4} → Measure X → Set ι → (ι → X) → (ι → ℝ) → ℝ → (X → ε) → X → ENNReal`
Docstring: The uncentered Hardy-Littlewood maximal function, for a family of balls.
Definition: `fun {X : Type u_1} {ε : Type u_2} [PseudoMetricSpace X] [MeasurableSpace X] [ENorm ε] {ι : Type u_4} (μ : Measure X) (𝓑 : Set ι) (c : ι → X) (r : ι → ℝ) (p : ℝ) (u : X → ε) (x : X) => ⨆ i ∈ 𝓑, (Metric.ball (c i) (r i)).indicator (fun (x : X) => (⨍⁻ (y : X) in Metric.ball (c i) (r i), ‖u y‖ₑ ^ p ∂μ) ^ p⁻¹) x`

#### `CMB` (def)
Lean: `NNReal → NNReal → NNReal`
Docstring: The constant factor in the statement that `M_𝓑` has strong type.
Definition: `fun (A p : NNReal) => C_realInterpolation ⊤ (1 : ENNReal) ⊤ (1 : ENNReal) ↑p (1 : NNReal) (A ^ (2 : ℕ)) (1 : NNReal) (↑p)⁻¹`

#### `instContinuousENormNNReal_carleson` (def)
Lean: `ContinuousENorm NNReal`
Definition: `{ toENorm := NNNorm.toENorm, continuous_enorm := instContinuousENormNNReal_carleson._proof_1 }`

#### `MeasureTheory.C_realInterpolation` (def)
Lean: `ENNReal → ENNReal → ENNReal → ENNReal → ENNReal → NNReal → NNReal → NNReal → ENNReal → NNReal`
Docstring: The constant occurring in the real interpolation theorem
Definition: `fun (p₀ p₁ q₀ q₁ q : ENNReal) (C₀ C₁ A : NNReal) (t : ENNReal) => (C_realInterpolation_ENNReal p₀ p₁ q₀ q₁ q C₀ C₁ A t).toNNReal`

## Translations

### `hasStrongType_maximalFunction`
Lean (short): `[μ.IsDoubling A] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] (hp₁ : 0 < p₁) (hp₁₂ : p₁ < p₂) : HasStrongType (maximalFunction μ 𝓑 c r ↑p₁) (↑p₂) (↑p₂) μ μ ↑(C2_0_6 A p₁ p₂)`
Lean (full): `∀ {X : Type u_1} {ε' : Type u_3} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : MeasurableSpace X] {μ : Measure X} [μ.IsDoubling A] {ι : Type u_4} {𝓑 : Set ι} {c : ι → X} {r : ι → ℝ} [inst_3 : TopologicalSpace ε'] [inst_4 : ContinuousENorm ε'] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] {p₁ p₂ : NNReal}, (0 : NNReal) < p₁ → p₁ < p₂ → HasStrongType.{u_3, 0, u_1, u_1} (ε₁ := ε') (maximalFunction μ 𝓑 c r ↑p₁) (↑p₂) (↑p₂) μ μ ↑(C2_0_6 A p₁ p₂)`
Docstring: The `maximalFunction` has strong type when `p₁ < p₂`.
English: Let $X$ be a proper pseudometric space with its Borel $\sigma$-algebra, and let $\mu$ be a measure on $X$ that is doubling with constant $A \ge 0$, finite on compact sets, and positive on nonempty open sets. Let $\mathcal{B}$ be a set of indices $i \in \iota$ with centers $c : \iota \to X$ and radii $r : \iota \to \mathbb{R}$. Let $\varepsilon'$ be a topological space with a continuous extended norm $\|\cdot\|_e$. If $p_1, p_2 \in \mathbb{R}_{\ge 0}$ satisfy $0 < p_1 < p_2$, then the maximal function $\mathrm{maximalFunction}(\mu, \mathcal{B}, c, r, p_1)$ (acting on $\varepsilon'$-valued functions) has strong type $(p_2, p_2)$ with respect to $\mu$ and $\mu$, with constant $C_{2.0.6}(A, p_1, p_2)$.

### `hasStrongType_maximalFunction_one`
Lean (short): `[μ.IsDoubling A] [SMul NNReal ε'] [ENormSMulClass NNReal ε'] [TopologicalSpace.PseudoMetrizableSpace ε'] [BorelSpace ε'] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] (hp : 1 < p) : HasStrongType (maximalFunction μ 𝓑 c r 1) (↑p) (↑p) μ μ ↑(CMB A p)`
Lean (full): `∀ {X : Type u_1} {ε' : Type u_3} {A : NNReal} [inst : PseudoMetricSpace X] [inst_1 : MeasurableSpace X] {μ : Measure X} [μ.IsDoubling A] {ι : Type u_4} {𝓑 : Set ι} {c : ι → X} {r : ι → ℝ} [inst_3 : TopologicalSpace ε'] [inst_4 : ESeminormedAddMonoid ε'] [inst_5 : SMul NNReal ε'] [ENormSMulClass NNReal ε'] [TopologicalSpace.PseudoMetrizableSpace ε'] [inst_8 : MeasurableSpace ε'] [BorelSpace ε'] [BorelSpace X] [IsFiniteMeasureOnCompacts μ] [ProperSpace X] [μ.IsOpenPosMeasure] {p : NNReal}, (1 : NNReal) < p → HasStrongType.{u_3, 0, u_1, u_1} (ε₁ := ε') (maximalFunction μ 𝓑 c r (1 : ℝ)) (↑p) (↑p) μ μ ↑(CMB A p)`
Docstring: Special case of equation (2.0.44). The proof is given between (9.0.12) and (9.0.34). Use the real interpolation theorem instead of following the blueprint.
English: Let $X$ be a proper pseudometric space equipped with a measurable structure that is its Borel $\sigma$-algebra, and let $\mu$ be a measure on $X$ that is doubling with constant $A$ (a nonnegative real), finite on compact sets, and positive on nonempty open sets. Let $\iota$ be a type, $\mathcal{B}\subseteq\iota$ a set of indices, $c : \iota \to X$ (centers) and $r : \iota \to \mathbb{R}$ (radii). Let $E$ be a topological space which is an extended-seminormed additive monoid, pseudo-metrizable, carries a measurable structure that is its Borel $\sigma$-algebra, and has a scalar action of $\mathbb{R}_{\ge 0}$ compatible with the extended norm ($\|t\cdot v\|_e = t\,\|v\|_e$ for $t\in\mathbb R_{\ge0}$, $v\in E$). For $u:X\to E$ let $M u(x)=\sup_{i\in\mathcal B}\mathbf 1_{B(c(i),r(i))}(x)\,⨍_{B(c(i),r(i))}\|u(y)\|_e\,d\mu(y)\in[0,\infty]$ be the uncentered Hardy–Littlewood maximal function $\mathrm{maximalFunction}(\mu,\mathcal B,c,r,1)$ for this family of balls. Let $p$ be a nonnegative real with $p > 1$. Then $M$ has strong type $(p, p)$ with respect to $\mu$ and $\mu$ with constant $C_{MB}(A, p)$: for every $u\in L^p(\mu;E)$, $Mu$ is a.e. strongly measurable and $\|Mu\|_{L^p(\mu)}\le C_{MB}(A,p)\,\|u\|_{L^p(\mu)}$. Here $C_{MB}(A,p)=C_{\mathrm{realInterpolation}}(\infty,1,\infty,1,p,1,A^2,1,1/p)$ is the constant of the real interpolation theorem with these parameters (a special case of equation (2.0.44)).
