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

### `ProbabilityTheory.sum_meas_smul_cond_fiber'`
Lean: `[MeasurableSingletonClass α] (hX : Measurable X) [FiniteRange X] (μ : Measure Ω) [IsFiniteMeasure μ] : ∑ x ∈ FiniteRange.toFinset X, μ (X ⁻¹' {x}) • μ[|X ⁻¹' {x}] = μ`
Docstring: The **law of total probability** for a random variable taking finitely many values: a measure `μ` can be expressed as a linear combination of its conditional measures `μ[|X ← x]` on fibers of a random variable `X` valued in a fintype.
Previous English: (Law of total probability.) Let $X:\Omega\to G$ be a measurable random variable with finite range and $\mu$ a measure on $\Omega$. Then $\sum_{x\in \mathrm{range}(X)} \mu(X^{-1}\{x\})\cdot \mu[\,\cdot \mid X^{-1}\{x\}] = \mu$, where $\mu[\,\cdot\mid A]$ denotes the conditional measure on $A$ and the sum runs over the finite range of $X$ (FiniteRange.toFinset $X$).
Checker's issue: The English says only that mu is a measure, dropping the hypothesis [IsFiniteMeasure mu].
