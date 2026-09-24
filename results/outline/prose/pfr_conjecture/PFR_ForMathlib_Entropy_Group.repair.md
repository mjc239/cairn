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

### `ProbabilityTheory.entropy_sub_mutualInfo_le_entropy_sub`
Lean: `[Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] (hX : Measurable X) (hY : Measurable Y) : H[X; μ] - I[X : Y ; μ] ≤ H[X - Y; μ]`
Docstring: `H[X] - I[X : Y] ≤ H[X - Y]`
Previous English: Let $X, Y$ be measurable random variables with values in an additive group. Then $H[X] - I[X:Y] \le H[X - Y]$ (with respect to $\mu$).
Checker's issue: Drops the hypothesis [IsProbabilityMeasure μ] and the finite-range assumptions on X, Y.
