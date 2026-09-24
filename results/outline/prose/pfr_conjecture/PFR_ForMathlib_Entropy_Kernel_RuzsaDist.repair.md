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

### `ProbabilityTheory.Kernel.rdist_symm`
Lean: `[Countable T] [MeasurableSingletonClass T] [Countable T'] [MeasurableSingletonClass T'] [MeasurableSingletonClass G] [Countable G] [IsFiniteKernel κ] [IsFiniteKernel η] [IsProbabilityMeasure μ] [IsProbabilityMeasure ν] [FiniteSupport μ] [FiniteSupport ν] : dk[κ ; μ # η ; ν] = dk[η ; ν # κ ; μ]`
Previous English: The kernel Ruzsa distance is symmetric: $d_k[\kappa;\mu \,\#\, \eta;\nu] = d_k[\eta;\nu \,\#\, \kappa;\mu]$.
Checker's issue: The English states symmetry unconditionally, dropping the finite-kernel, probability-measure and finite-support hypotheses on kappa, eta, mu, nu.
