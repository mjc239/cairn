You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.CondIndepFun`
Lean: `(f : Ω → α) (g : Ω → β) (h : Ω → γ) (μ : autoParam (Measure Ω) CondIndepFun._auto_1) : Prop`
English: Given random variables $f : \Omega \to \alpha$, $g : \Omega \to \beta$, $h : \Omega \to \gamma$ and a measure $\mu$ on $\Omega$, `CondIndepFun f g h μ` is the assertion that $f$ and $g$ are conditionally independent relative to $h$ (with respect to $\mu$).

### `ProbabilityTheory.condIndep_copies`
Lean: `[MeasurableSingletonClass β] [Countable β] (X : Ω → α) (Y : Ω → β) (hX : Measurable X) (hY : Measurable Y) [FiniteRange Y] (μ : Measure Ω) [IsProbabilityMeasure μ] : ∃ Ω' x X₁ X₂ Y' ν, IsProbabilityMeasure ν ∧ Measurable X₁ ∧ Measurable X₂ ∧ Measurable Y' ∧ CondIndepFun X₁ X₂ Y' ν ∧ IdentDistrib (⟨X₁, Y'⟩) (⟨X, Y⟩) ν μ ∧ IdentDistrib (⟨X₂, Y'⟩) (⟨X, Y⟩) ν μ`
English: Let $\beta$ be a countable measurable space with measurable singletons, let $\mu$ be a probability measure on $\Omega$, and let $X : \Omega \to \alpha$ and $Y : \Omega \to \beta$ be measurable random variables with $Y$ of finite range. Then there exist a measurable space $\Omega'$, a probability measure $\nu$ on $\Omega'$ and measurable random variables $X_1, X_2 : \Omega' \to \alpha$, $Y' : \Omega' \to \beta$ such that $X_1$ and $X_2$ are conditionally independent given $Y'$ with respect to $\nu$, and both $(X_1, Y')$ and $(X_2, Y')$ under $\nu$ have the same distribution as $(X, Y)$ under $\mu$.
