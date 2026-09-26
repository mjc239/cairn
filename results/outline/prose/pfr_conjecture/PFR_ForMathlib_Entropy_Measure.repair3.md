You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

### `ProbabilityTheory.integrable_of_finiteSupport`
Lean (short): `[MeasurableSingletonClass S] (μ : Measure S) [FiniteSupport μ] [IsFiniteMeasure μ] [Countable S] : Integrable f μ`
Lean (full): `∀ {S : Type u_2} [inst : MeasurableSpace S] [MeasurableSingletonClass S] (μ : Measure S) [FiniteSupport μ] {β : Type u_5} [inst_3 : NormedAddCommGroup β] [IsFiniteMeasure μ] [Countable S] {f : S → β}, Integrable f μ`
Docstring: The countability hypothesis can probably be dropped here. Proof is unwieldy and can probably be golfed.
Previous English: Let $S$ be a countable space with measurable singletons, and let $\mu$ be a finite measure on $S$ with finite support. Then every function $f$ on $S$ is integrable with respect to $\mu$.
Checker's issue: The English omits that f takes values in a normed abelian group β, saying only 'every function f on S'.
