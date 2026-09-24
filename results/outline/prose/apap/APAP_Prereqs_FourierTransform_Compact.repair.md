You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Keep every
hypothesis the Lean shows, including instance assumptions such as `[Finite G]` or `[IsProbabilityMeasure μ]`
(say them in words: "$G$ is finite", "$\mu$ is a probability measure"), and the exact conclusion. Do not add
claims the Lean does not make. Purely structural instances (e.g. `[AddCommGroup G]`) and implicit arguments are not
shown and may stay implicit.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

### `cft`
Lean: `[Fintype G] (f : G → ℂ) (_ : AddChar G ℂ) : ℂ`
Docstring: The discrete Fourier transform.
Previous English: For $f : G \to \mathbb{C}$, the discrete Fourier transform (in this module's compact normalisation) assigns to each additive character $\psi : G \to \mathbb{C}$ a complex number $\widehat f(\psi)$.
Checker's issue: The English omits the [Fintype G] hypothesis that G is finite.
