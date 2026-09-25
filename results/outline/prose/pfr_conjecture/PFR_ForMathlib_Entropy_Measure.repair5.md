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

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `ProbabilityTheory.measureMutualInfo` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → autoParam (Measure (S × T)) measureMutualInfo._auto_1 → ℝ`
Docstring: The mutual information between the marginals of a measure on a product space.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (μ : Measure (S × T)) => Hm[Measure.map Prod.fst μ] + Hm[Measure.map Prod.snd μ] - Hm[μ]`

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

## Flagged translations

### `ProbabilityTheory.measureMutualInfo_of_not_isFiniteMeasure`
Lean (short): `(h : ¬IsFiniteMeasure μ) : Im[μ] = 0`
Lean (full): `∀ {S : Type u_2} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] {μ : Measure (S × U)}, ¬IsFiniteMeasure μ → Im[μ] = (0 : ℝ)`
Previous English: If $\mu$ is not a finite measure, then $I_m[\mu]=0$.
Checker's issue: $\mu$ is never introduced: the English omits that $\mu$ is a measure on $S\times U$ for measurable spaces $S, U$, and $I_m$ is not introduced
