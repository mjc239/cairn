You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring, and when no
docstring, definition body (under "Project definitions") or Lean supports a description of an object, name it
instead of describing it. Give every variable its
type, introduce every symbol, and never use one letter for two things.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `ProbabilityTheory.IsUniform` (structure or class)
Lean: `{Ω : Type uΩ} → {S : Type uS} → [mΩ : MeasurableSpace Ω] → Set S → (Ω → S) → autoParam (Measure Ω) IsUniform._auto_1 → Prop`
Docstring: The assertion that the law of $X$ is the uniform probability measure on a finite set $H$. While in applications $H$ will be non-empty finite set, $X$ measurable, and and $μ$ a probability measure, it could be technically convenient to have a definition that works even without these hypotheses. (For instance, `isUniform` would be well-defined, but false, for infinite `H`). This should probably be refactored, requiring instead that `μ.map X = uniformOn H`.
Fields: `α`, `0`

## Flagged translations

### `ProbabilityTheory.IsUniform.measureReal_preimage_of_mem`
Lean (short): `[DiscreteMeasurableSpace S] [IsProbabilityMeasure μ] (h : IsUniform (↑A) X μ) (hX : Measurable X) (hs : s ∈ A) : μ.real (X ⁻¹' {s}) = 1 / ↑A.card`
Lean (full): `∀ {Ω : Type uΩ} {S : Type uS} [mΩ : MeasurableSpace Ω] {X : Ω → S} {μ : Measure Ω} [inst : MeasurableSpace S] [DiscreteMeasurableSpace S] {A : Finset S} [IsProbabilityMeasure μ], IsUniform (↑A) X μ → Measurable X → ∀ {s : S}, s ∈ A → μ.real (X ⁻¹' {s}) = (1 : ℝ) / ↑A.card`
Docstring: A "unit test" for the definition of uniform distribution.
Previous English: Let $S$ carry the discrete $\sigma$-algebra (every subset measurable), let $\mu$ be a probability measure, let $A\subseteq S$ be a finite set, and let $X$ be a measurable $S$-valued random variable that is uniformly distributed on $A$ with respect to $\mu$. Then for every $s\in A$, $\mu(X=s)=1/|A|$ (as a real number).
Checker's issue: The sample space Omega (a measurable space carrying mu, with X : Omega -> S) is never introduced; the English only says 'a probability measure' and 'an S-valued random variable'. S is also not stated to be a measurable space.
