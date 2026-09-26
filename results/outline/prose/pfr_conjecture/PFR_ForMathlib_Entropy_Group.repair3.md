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

#### `ProbabilityTheory.entropy` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Definition: `fun {Ω : Type u_1} {S : Type u_2} [MeasurableSpace Ω] [MeasurableSpace S] (X : Ω → S) (μ : Measure Ω) => Hm[Measure.map X μ]`

#### `prod` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → (Ω → S) → (Ω → T) → Ω → S × T`
Docstring: The pair of two random variables
Definition: `fun {Ω : Type u_1} {S : Type u_2} {T : Type u_3} (X : Ω → S) (Y : Ω → T) (ω : Ω) => (X ω, Y ω)`

#### `FiniteRange` (inductive)
Lean: `{Ω : Type u_1} → {G : Type u_2} → (Ω → G) → Prop`
Docstring: The property of having a finite range.

#### `ProbabilityTheory.mutualInfo` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → autoParam (Measure Ω) mutualInfo._auto_1 → ℝ`
Docstring: The mutual information `I[X : Y]` of two random variables is defined to be `H[X] + H[Y] - H[X ; Y]`.
Definition: `fun {Ω : Type u_1} {S : Type u_2} {T : Type u_3} [MeasurableSpace Ω] [MeasurableSpace S] [MeasurableSpace T] (X : Ω → S) (Y : Ω → T) (μ : Measure Ω) => H[X; μ] + H[Y; μ] - H[⟨X, Y⟩; μ]`

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

## Flagged translations

### `ProbabilityTheory.entropy_add_right`
Lean (short): `[Countable G] [MeasurableSingletonClass G] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨X, X + Y⟩; μ] = H[⟨X, Y⟩; μ]`
Lean (full): `∀ {Ω : Type uΩ} {G : Type uS} [mΩ : MeasurableSpace Ω] [Countable G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] [inst : AddGroup G] {X Y : Ω → G}, Measurable X → Measurable Y → ∀ (μ : Measure Ω), H[⟨X, X + Y⟩; μ] = H[⟨X, Y⟩; μ]`
Docstring: `H[X, X + Y] = H[X, Y]`
Previous English: Let $G$ be a countable additive group in which singletons are measurable, let $\mu$ be a measure on $\Omega$, and let $X, Y : \Omega \to G$ be measurable random variables. Then $H[(X, X+Y);\mu] = H[(X, Y);\mu]$.
Checker's issue: The symbol H is not introduced (never named as Shannon entropy of the random variable with respect to μ); otherwise the statement matches.

### `ProbabilityTheory.entropy_add_left`
Lean (short): `[Countable G] [MeasurableSingletonClass G] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨Y + X, Y⟩; μ] = H[⟨X, Y⟩; μ]`
Lean (full): `∀ {Ω : Type uΩ} {G : Type uS} [mΩ : MeasurableSpace Ω] [Countable G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] [inst : AddGroup G] {X Y : Ω → G}, Measurable X → Measurable Y → ∀ (μ : Measure Ω), H[⟨Y + X, Y⟩; μ] = H[⟨X, Y⟩; μ]`
Docstring: `H[Y + X, Y] = H[X, Y]`
Previous English: Let $G$ be a countable additive group in which singletons are measurable, let $\mu$ be a measure on $\Omega$, and let $X, Y : \Omega \to G$ be measurable random variables. Then $H[(Y+X, Y);\mu] = H[(X, Y);\mu]$.
Checker's issue: The symbol H is not introduced (never named as Shannon entropy of the random variable with respect to μ); otherwise the statement matches.

### `ProbabilityTheory.entropy_sub_mutualInfo_le_entropy_sub`
Lean (short): `[Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] (hX : Measurable X) (hY : Measurable Y) : H[X; μ] - I[X : Y ; μ] ≤ H[X - Y; μ]`
Lean (full): `∀ {Ω : Type uΩ} {G : Type uS} [mΩ : MeasurableSpace Ω] [Countable G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] [inst : AddGroup G] {X : Ω → G} {μ : Measure Ω} [IsProbabilityMeasure μ] {Y : Ω → G} [FiniteRange X] [FiniteRange Y], Measurable X → Measurable Y → H[X; μ] - I[X : Y ; μ] ≤ H[X - Y; μ]`
Docstring: `H[X] - I[X : Y] ≤ H[X - Y]`
Previous English: Let $G$ be a countable additive group with measurable singletons, let $\mu$ be a probability measure on $\Omega$, and let $X, Y : \Omega \to G$ be measurable random variables, both of finite range. Then $H[X;\mu] - I[X:Y;\mu] \le H[X - Y;\mu]$.
Checker's issue: The symbols H and I are not introduced (never named as entropy / mutual information with respect to μ); otherwise the statement matches.
