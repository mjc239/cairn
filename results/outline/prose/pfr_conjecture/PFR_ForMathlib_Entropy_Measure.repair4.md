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
docstring or Lean supports a description of an object, name it instead of describing it. Give every variable its
type, introduce every symbol, and never use one letter for two things.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

### `ProbabilityTheory.measureMutualInfo`
Lean (short): `(μ : autoParam (Measure (S × T)) measureMutualInfo._auto_1) : ℝ`
Lean (full): `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → autoParam (Measure (S × T)) measureMutualInfo._auto_1 → ℝ`
Docstring: The mutual information between the marginals of a measure on a product space.
Previous English: For a measure $\mu$ on a product $S\times T$, the mutual information $I_m[\mu]$ between its two marginals, namely $I_m[\mu] = H_m[\pi_1{}_*\mu] + H_m[\pi_2{}_*\mu] - H_m[\mu]$ with $\pi_1,\pi_2$ the coordinate projections.
Checker's issue: The formula given is not shown by the Lean signature or the docstring; attribute it correctly or state only what the signature/docstring supports.
