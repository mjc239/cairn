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

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport.mk`
Lean: `[Countable T] [MeasurableSingletonClass T] (_hκ : κ.AEFiniteKernelSupport μ) : Kernel T S`
Docstring: The definition doesn't use `_hκ`, but we keep it here still as it doesn't give anything interesting otherwise.
Previous English: Given a proof that $\kappa$ has almost everywhere finite support with respect to $\mu$, defines an associated kernel $\mathrm{mk}$ from $T$ to $S$ (a modification of $\kappa$; the definition does not actually use the hypothesis).
Checker's issue: The English omits the instance hypotheses that T is countable with measurable singletons.

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport.finiteKernelSupport_mk`
Lean: `[Countable T] [MeasurableSingletonClass T] [MeasurableSingletonClass S] (hκ : κ.AEFiniteKernelSupport μ) : hκ.mk.FiniteKernelSupport`
Previous English: If $\kappa$ has almost everywhere finite support with respect to $\mu$ (hypothesis $h\kappa$), then the kernel $h\kappa.\mathrm{mk}$ has finite kernel support.
Checker's issue: The English omits the hypotheses that T is countable and that T and S have measurable singletons.
