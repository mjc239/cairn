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
type, introduce every symbol, and never use one letter for two things. When a definition's body is shown, say what
it defines, in words or a formula that agrees with the body.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

## Flagged translations

### `ProbabilityTheory.IsUniform`
Lean (short): `(H : Set S) (X : Ω → S) (μ : autoParam (Measure Ω) IsUniform._auto_1) : Prop`
Lean (full): `{Ω : Type uΩ} → {S : Type uS} → [mΩ : MeasurableSpace Ω] → Set S → (Ω → S) → autoParam (Measure Ω) IsUniform._auto_1 → Prop`
Constructor (every field with its type): `∀ {Ω : Type uΩ} {S : Type uS} [mΩ : MeasurableSpace Ω] {H : Set S} {X : Ω → S} {μ : autoParam (Measure Ω) IsUniform._auto_1}, (∀ ⦃x : S⦄, x ∈ H → ∀ ⦃y : S⦄, y ∈ H → Eq (α := ENNReal) (μ (X ⁻¹' {x}) : ENNReal) (μ (X ⁻¹' {y}) : ENNReal)) → μ (X ⁻¹' Hᶜ) = (0 : ENNReal) → IsUniform H X μ`
Docstring: The assertion that the law of $X$ is the uniform probability measure on a finite set $H$. While in applications $H$ will be non-empty finite set, $X$ measurable, and and $μ$ a probability measure, it could be technically convenient to have a definition that works even without these hypotheses. (For instance, `isUniform` would be well-defined, but false, for infinite `H`). This should probably be refactored, requiring instead that `μ.map X = uniformOn H`.
Previous English: Let $\Omega$ be a measurable space and $S$ a type. For a set $H\subseteq S$, a function $X:\Omega\to S$ and a measure $\mu$ on $\Omega$ (supplied automatically by default), $\mathrm{IsUniform}(H,X,\mu)$ is a proposition. According to its docstring, it asserts that the law of $X$ is the uniform probability measure on the finite set $H$; the definition itself makes no assumptions on $H$, $X$ or $\mu$ (the docstring notes it would be well-defined but false for infinite $H$).
Checker's issue: A structure with its constructor shown, but the English only paraphrases the docstring. It does not state the defining conditions: μ(X⁻¹{x}) = μ(X⁻¹{y}) for all x,y∈H, and μ(X⁻¹(Hᶜ)) = 0. The docstring's 'uniform probability measure' reading is also stronger than these conditions, since μ need not be a probability measure.
