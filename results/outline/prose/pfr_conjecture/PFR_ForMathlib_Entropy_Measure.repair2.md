You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Keep every
hypothesis the Lean shows, including instance assumptions such as `[Finite G]` or `[IsProbabilityMeasure μ]`
(say them in words: "$G$ is finite", "$\mu$ is a probability measure"), and the exact conclusion. Do not add
claims the Lean does not make. Purely structural instances (e.g. `[AddCommGroup G]`) and implicit arguments are not
shown and may stay implicit.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

### `ProbabilityTheory.measureMutualInfo_nonneg`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass U] [FiniteSupport μ] : 0 ≤ Im[μ]`
Previous English: For a measure $\mu$ on $S\times U$ (under the standing finite-support assumptions), $0\le I_m[\mu]$.
Checker's issue: The English replaces the explicit hypotheses [MeasurableSingletonClass S], [MeasurableSingletonClass U] and [FiniteSupport μ] with a vague 'standing finite-support assumptions', which drops the measurable-singleton hypotheses.
