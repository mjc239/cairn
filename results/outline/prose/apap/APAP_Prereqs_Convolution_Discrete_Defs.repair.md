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

### `ddconv`
Lean: `[Fintype G] (f : G → R) (g : G → R) (_ : G) : R`
Docstring: Convolution
Previous English: For $f, g : G \to R$, defines their (discrete) convolution $f * g : G \to R$.
Checker's issue: The English omits the [Fintype G] hypothesis that G is finite.

### `ddconv_eq_sum_sub`
Lean: `[Fintype G] (f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
Previous English: For $f, g : G \to R$ and $a \in G$, $(f * g)(a) = \sum_t f(a - t)\, g(t)$.
Checker's issue: The English omits the [Fintype G] hypothesis that G is finite.

### `iterConv`
Lean: `[Fintype G] (f : G → R) (_ : ℕ) (_ : G) : R`
Docstring: Iterated convolution.
Previous English: For $f : G \to R$ and $n \in \mathbb{N}$, defines the $n$-fold iterated convolution $f^{*n} : G \to R$.
Checker's issue: The English omits the [Fintype G] hypothesis that G is finite.

### `dddconv`
Lean: `[Fintype G] [StarRing R] (f : G → R) (g : G → R) (_ : G) : R`
Docstring: Difference convolution
Previous English: For a star ring $R$ and $f, g : G \to R$, defines their difference convolution $f \circ g : G \to R$.
Checker's issue: The English omits the [Fintype G] hypothesis that G is finite.
