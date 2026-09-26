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

### `BohrSet`
Lean: `(G : Type u_1) : Type u_1`
Docstring: A *Bohr set* `B` on an additive group `G` is a finite set of characters of `G`, called the *frequencies*, along with an extended non-negative real number for each frequency `ψ`, called the *width of `B` at `ψ`*. A Bohr set `B` is thought of as the set `{x | ∀ ψ ∈ B.frequencies, ‖1 - ψ x‖ ≤ B.width ψ}`. This is the *chord-length* convention. The arc-length convention would instead be `{x | ∀ ψ ∈ B…
Previous English: For an additive group $G$, a Bohr set on $G$ consists of a finite set of characters of $G$ (the frequencies) together with an extended nonnegative real width for each frequency $\psi$. It is thought of as the set $\{x : \|1 - \psi(x)\| \le \text{width}(\psi) \text{ for all frequencies } \psi\}$ (the chord-length convention).
Checker's issue: The signature is only `Type → Type`, yet the English asserts specific structure (finite character set, extended-nonnegative-real widths, chord-length membership condition) that cannot be read from it.
