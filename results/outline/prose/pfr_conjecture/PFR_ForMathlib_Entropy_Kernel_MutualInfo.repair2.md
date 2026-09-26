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

### `ProbabilityTheory.Kernel.mutualInfo`
Lean (short): `(κ : Kernel T (S × U)) (μ : Measure T) : ℝ`
Lean (full): `{S : Type u_2} → {T : Type u_3} → {U : Type u_4} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → [inst_2 : MeasurableSpace U] → Kernel T (S × U) → Measure T → ℝ`
Docstring: Mutual information of a kernel into a product space with respect to a measure.
Previous English: For a kernel $\kappa$ from $T$ into a product space $S\times U$ and a measure $\mu$ on $T$, $I_k[\kappa,\mu]$ denotes the mutual information of the kernel $\kappa$ with respect to $\mu$.
Checker's issue: Does not state that S, T and U are measurable spaces (instance assumptions in the full statement).
