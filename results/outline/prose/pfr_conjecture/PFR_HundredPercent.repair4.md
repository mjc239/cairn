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
type, introduce every symbol, and never use one letter for two things. When a definition's body is shown, say what
it defines, in words or a formula that agrees with the body.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `rdist` (def)
Lean: `{Ω : Type u_1} → {Ω' : Type u_2} → {G : Type u_5} → [mΩ : MeasurableSpace Ω] → [mΩ' : MeasurableSpace Ω'] → [hG : MeasurableSpace G] → [AddCommGroup G] → (Ω → G) → (Ω' → G) → autoParam (Measure Ω) rdist._auto_1 → autoParam (Measure Ω') rdist._auto_3 → ℝ`
Docstring: The Ruzsa distance `rdist X Y` or `d[X ; Y]` between two random variables is defined as `H[X'- Y'] - H[X']/2 - H[Y']/2`, where `X', Y'` are independent copies of `X, Y`.
Definition: `fun {Ω : Type u_1} {Ω' : Type u_2} {G : Type u_5} [MeasurableSpace Ω] [MeasurableSpace Ω'] [MeasurableSpace G] [AddCommGroup G] (X : Ω → G) (Y : Ω' → G) (μ : Measure Ω) (μ' : Measure Ω') => H[fun (x : G × G) => x.1 - x.2; Measure.prod (Measure.map X μ) (Measure.map Y μ')] - H[X; μ] / (2 : ℝ) - H[Y; μ'] / (2 : ℝ)`

#### `ProbabilityTheory.IsUniform` (structure or class)
Lean: `{Ω : Type uΩ} → {S : Type uS} → [mΩ : MeasurableSpace Ω] → Set S → (Ω → S) → autoParam (Measure Ω) IsUniform._auto_1 → Prop`
Docstring: The assertion that the law of $X$ is the uniform probability measure on a finite set $H$. While in applications $H$ will be non-empty finite set, $X$ measurable, and and $μ$ a probability measure, it could be technically convenient to have a definition that works even without these hypotheses. (For instance, `isUniform` would be well-defined, but false, for infinite `H`). This should probably be refactored, requiring instead that `μ.map X = uniformOn H`.
Constructor (every field with its type): `∀ {Ω : Type uΩ} {S : Type uS} [mΩ : MeasurableSpace Ω] {H : Set S} {X : Ω → S} {μ : autoParam (Measure Ω) IsUniform._auto_1}, (∀ ⦃x : S⦄, x ∈ H → ∀ ⦃y : S⦄, y ∈ H → Eq (α := ENNReal) (μ (X ⁻¹' {x}) : ENNReal) (μ (X ⁻¹' {y}) : ENNReal)) → μ (X ⁻¹' Hᶜ) = (0 : ENNReal) → IsUniform H X μ`

#### `ProbabilityTheory.entropy` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Definition: `fun {Ω : Type u_1} {S : Type u_2} [MeasurableSpace Ω] [MeasurableSpace S] (X : Ω → S) (μ : Measure Ω) => Hm[Measure.map X μ]`

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

## Flagged translations

### `symmGroup`
Lean (short): `[MeasurableAdd₂ G] (X : Ω → G) (hX : Measurable X) : AddSubgroup G`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → [inst : MeasureSpace Ω] → [inst_1 : MeasurableSpace G] → [inst_2 : AddCommGroup G] → [MeasurableAdd₂ G] → (X : Ω → G) → Measurable X → AddSubgroup G`
Definition: `fun {Ω : Type u_1} {G : Type u_2} [MeasureSpace Ω] [MeasurableSpace G] [AddCommGroup G] [MeasurableAdd₂ G] (X : Ω → G) (hX : Measurable X) => { carrier := {x : G | IdentDistrib X (fun (ω : Ω) => X ω + x) volume volume}, add_mem' := ⋯, zero_mem' := ⋯, neg_mem' := ⋯ }`
Docstring: The symmetry group Sym of $X$: the set of all $h ∈ G$ such that $X + h$ has an identical distribution to $X$.
Previous English: Let $\Omega$ be a measure space and let $G$ be an abelian group with a measurable space structure for which addition $G\times G\to G$ is measurable. For a measurable random variable $X:\Omega\to G$, this defines an additive subgroup $\mathrm{Sym}[X]$ of $G$. According to its docstring, it is the symmetry group of $X$: the set of all $h\in G$ such that $X+h$ has an identical distribution to $X$.
Checker's issue: Described only through its docstring; state what the body defines.

### `sub_mem_symmGroup`
Lean (short): `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X) (hdist : d[X # X] = 0) (hx : volume (X ⁻¹' {x}) ≠ 0) (hy : volume (X ⁻¹' {y}) ≠ 0) : x - y ∈ symmGroup X hX`
Lean (full): `∀ {Ω : Type u_1} {G : Type u_2} [inst : MeasureSpace Ω] [inst_1 : MeasurableSpace G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableAdd₂ G] {X : Ω → G} [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure.{u_1} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] (hX : Measurable X), d[X # X] = (0 : ℝ) → ∀ {x y : G}, (volume : Measure Ω) (X ⁻¹' {x}) ≠ (0 : ENNReal) → (volume : Measure Ω) (X ⁻¹' {y}) ≠ (0 : ENNReal) → Membership.mem (γ := AddSubgroup G) (symmGroup X hX) (x - y)`
Docstring: If $d[X ;X]=0$, and $x,y \in G$ are such that $P[X=x], P[X=y]>0$, then $x-y \in \mathrm{Sym}[X]$.
Previous English: Let $G$ be a finite abelian group with measurable singletons and measurable addition, and let $\Omega$ be a probability space (its measure $P$ is a probability measure). Let $X:\Omega\to G$ be a measurable random variable with $d[X;X]=0$, and let $x,y\in G$ satisfy $P[X=x]\neq 0$ and $P[X=y]\neq 0$. Then $x-y\in\mathrm{Sym}[X]$.
Checker's issue: Symbols not introduced: d[X;X] is never named as the Ruzsa distance, and Sym[X] is used without saying it is the symmetry group symmGroup X = {h ∈ G : X+h has the same distribution as X}.

### `isUniform_sub_const_of_rdist_eq_zero`
Lean (short): `[MeasurableAdd₂ G] [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (hX : Measurable X) (hdist : d[X # X] = 0) (hx₀ : volume (X ⁻¹' {x₀}) ≠ 0) : IsUniform (↑(symmGroup X hX)) (fun ω => X ω - x₀) volume`
Lean (full): `∀ {Ω : Type u_1} {G : Type u_2} [inst : MeasureSpace Ω] [inst_1 : MeasurableSpace G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableAdd₂ G] {X : Ω → G} [Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure.{u_1} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] (hX : Measurable X), d[X # X] = (0 : ℝ) → ∀ {x₀ : G}, (volume : Measure Ω) (X ⁻¹' {x₀}) ≠ (0 : ENNReal) → IsUniform (↑(symmGroup X hX)) (fun (ω : Ω) => X ω - x₀) volume`
Docstring: If `d[X # X] = 0`, then `X - x₀` is the uniform distribution on the subgroup of `G` stabilizing the distribution of `X`, for any `x₀` of positive probability.
Previous English: Let $G$ be a finite abelian group with measurable singletons and measurable addition, and let $\Omega$ be a probability space (its measure $P$ is a probability measure). Let $X:\Omega\to G$ be a measurable random variable with $d[X;X]=0$, and let $x_0\in G$ satisfy $P[X=x_0]\neq 0$. Then $X-x_0$ is uniformly distributed on the subgroup $\mathrm{Sym}[X]$ of $G$.
Checker's issue: Symbols not introduced: d[X;X] is never named as the Ruzsa distance, and Sym[X] is used without saying it is the symmetry group symmGroup X = {h ∈ G : X+h has the same distribution as X}.
