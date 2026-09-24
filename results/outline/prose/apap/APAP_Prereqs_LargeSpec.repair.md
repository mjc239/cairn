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

### `largeSpec`
Lean: `[Fintype G] (f : G → ℂ) (η : ℝ) : Finset (AddChar G ℂ)`
Docstring: The `η`-large spectrum of a function.
Previous English: For $f : G \to \mathbb{C}$ and $\eta \in \mathbb{R}$, the $\eta$-large spectrum of $f$ is defined as a finite set of additive characters $G \to \mathbb{C}$.
Checker's issue: The English omits the [Fintype G] hypothesis that G is finite.
