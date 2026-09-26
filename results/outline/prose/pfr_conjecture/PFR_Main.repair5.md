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

#### `ProbabilityTheory.IsUniform` (structure or class)
Lean: `{Ω : Type uΩ} → {S : Type uS} → [mΩ : MeasurableSpace Ω] → Set S → (Ω → S) → autoParam (Measure Ω) IsUniform._auto_1 → Prop`
Docstring: The assertion that the law of $X$ is the uniform probability measure on a finite set $H$. While in applications $H$ will be non-empty finite set, $X$ measurable, and and $μ$ a probability measure, it could be technically convenient to have a definition that works even without these hypotheses. (For instance, `isUniform` would be well-defined, but false, for infinite `H`). This should probably be refactored, requiring instead that `μ.map X = uniformOn H`.
Constructor (every field with its type): `∀ {Ω : Type uΩ} {S : Type uS} [mΩ : MeasurableSpace Ω] {H : Set S} {X : Ω → S} {μ : autoParam (Measure Ω) IsUniform._auto_1}, (∀ ⦃x : S⦄, x ∈ H → ∀ ⦃y : S⦄, y ∈ H → Eq (α := ENNReal) (μ (X ⁻¹' {x}) : ENNReal) (μ (X ⁻¹' {y}) : ENNReal)) → μ (X ⁻¹' Hᶜ) = (0 : ENNReal) → IsUniform H X μ`

#### `rdist` (def)
Lean: `{Ω : Type u_1} → {Ω' : Type u_2} → {G : Type u_5} → [mΩ : MeasurableSpace Ω] → [mΩ' : MeasurableSpace Ω'] → [hG : MeasurableSpace G] → [AddCommGroup G] → (Ω → G) → (Ω' → G) → autoParam (Measure Ω) rdist._auto_1 → autoParam (Measure Ω') rdist._auto_3 → ℝ`
Docstring: The Ruzsa distance `rdist X Y` or `d[X ; Y]` between two random variables is defined as `H[X'- Y'] - H[X']/2 - H[Y']/2`, where `X', Y'` are independent copies of `X, Y`.
Definition: `fun {Ω : Type u_1} {Ω' : Type u_2} {G : Type u_5} [MeasurableSpace Ω] [MeasurableSpace Ω'] [MeasurableSpace G] [AddCommGroup G] (X : Ω → G) (Y : Ω' → G) (μ : Measure Ω) (μ' : Measure Ω') => H[fun (x : G × G) => x.1 - x.2; Measure.prod (Measure.map X μ) (Measure.map Y μ')] - H[X; μ] / (2 : ℝ) - H[Y; μ'] / (2 : ℝ)`

#### `ProbabilityTheory.entropy` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Definition: `fun {Ω : Type u_1} {S : Type u_2} [MeasurableSpace Ω] [MeasurableSpace S] (X : Ω → S) (μ : Measure Ω) => Hm[Measure.map X μ]`

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

## Flagged translations

### `rdist_le_of_isUniform_of_card_sub_le`
Lean (short): `[Countable G] [Finite ↑A] [MeasurableSingletonClass G] (hA₀ : A.Nonempty) (hA : ↑(A - A).ncard ≤ K * ↑A.ncard) [IsProbabilityMeasure volume] (U₀unif : IsUniform A U₀ volume) (U₀meas : Measurable U₀) : d[U₀ # U₀] ≤ Real.log K`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {A : Set G} {K : ℝ} [Countable G] [A_fin : Finite.{u_1 + 1} ↑A] [inst_2 : MeasurableSpace G] [MeasurableSingletonClass G], A.Nonempty → ↑(A - A).ncard ≤ K * ↑A.ncard → ∀ {Ω : Type u_2} [inst_4 : MeasureSpace Ω] [IsProbabilityMeasure.{u_2} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] {U₀ : Ω → G}, IsUniform A U₀ volume → Measurable U₀ → d[U₀ # U₀] ≤ Real.log K`
Docstring: A uniform distribution on a set whose difference set has relative size at most `K` has self Rusza distance at most `log K`.
Previous English: Let $G$ be a countable abelian group, equipped with a measurable structure in which singletons are measurable, let $K\in\mathbb R$, and let $A\subseteq G$ be a finite nonempty set with $|A-A|\le K|A|$. Let $\Omega$ be a measure space whose measure is a probability measure, and let $U_0 : \Omega \to G$ be a measurable random variable uniformly distributed on $A$. Then $d[U_0;U_0]\le \log K$.
Checker's issue: The symbol d[U_0;U_0] is never introduced: the English does not say it is the Ruzsa distance (rdist) or define it.
