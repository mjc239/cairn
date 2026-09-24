You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.sum_meas_smul_cond_fiber'`
Lean: `[MeasurableSingletonClass α] (hX : Measurable X) [FiniteRange X] (μ : Measure Ω) [IsFiniteMeasure μ] : ∑ x ∈ FiniteRange.toFinset X, μ (X ⁻¹' {x}) • μ[|X ⁻¹' {x}] = μ`
English: (Law of total probability.) Let $\alpha$ have measurable singletons, let $X:\Omega\to \alpha$ be a measurable random variable with finite range, and let $\mu$ be a finite measure on $\Omega$. Then $\sum_{x\in \mathrm{range}(X)} \mu(X^{-1}\{x\})\cdot \mu[\,\cdot \mid X^{-1}\{x\}] = \mu$, where $\mu[\,\cdot\mid A]$ denotes the conditional measure on $A$ and the sum runs over the finite range of $X$ (FiniteRange.toFinset $X$).
