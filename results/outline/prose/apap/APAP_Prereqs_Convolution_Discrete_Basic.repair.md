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

### `balance_dddconv`
Lean: `[Fintype G] [CharZero R] [StarRing R] (f : G → R) (g : G → R) : Fintype.balance (f ○ᵈ g) = Fintype.balance f ○ᵈ Fintype.balance g`
Previous English: Let $R$ have characteristic zero and a star operation. For $f, g : G \to R$, the balanced (mean-subtracted) version of the difference convolution is the difference convolution of the balanced functions: $\operatorname{balance}(f \circ g) = \operatorname{balance}(f) \circ \operatorname{balance}(g)$, where $\operatorname{balance}(h) = h - \mathbb{E}\,h$.
Checker's issue: The English omits the [Fintype G] hypothesis that G is finite.

### `balance_ddconv`
Lean: `[Fintype G] [CharZero R] (f : G → R) (g : G → R) : Fintype.balance (f ∗ᵈ g) = Fintype.balance f ∗ᵈ Fintype.balance g`
Previous English: Let $R$ have characteristic zero. For $f, g : G \to R$, $\operatorname{balance}(f \ast g) = \operatorname{balance}(f) \ast \operatorname{balance}(g)$, where $\ast$ is discrete convolution and $\operatorname{balance}(h) = h - \mathbb{E}\,h$.
Checker's issue: The English omits the [Fintype G] hypothesis that G is finite.
