You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.IsUniform`
Lean: `(H : Set S) (X : Ω → S) (μ : autoParam (Measure Ω) IsUniform._auto_1) : Prop`
English: For a set $H\subseteq S$, a random variable $X:\Omega\to S$ and a measure $\mu$ on $\Omega$ (by default the ambient measure), defines the predicate $\mathrm{IsUniform}(H,X,\mu)$ asserting that the law of $X$ under $\mu$ is the uniform probability measure on the finite set $H$. The predicate makes sense without assuming $H$ nonempty and finite, $X$ measurable or $\mu$ a probability measure (e.g. it is well-defined but false for infinite $H$).

### `ProbabilityTheory.exists_isUniform_measureSpace`
Lean: `[MeasurableSingletonClass S] (H : Finset S) (h : H.Nonempty) : ∃ Ω mΩ U, IsProbabilityMeasure volume ∧ Measurable U ∧ IsUniform (↑H) U volume ∧ (∀ (ω : Ω), U ω ∈ H) ∧ FiniteRange U`
English: Let $H$ be a nonempty finite subset of $S$. Then there exist a type $\Omega$ with a measurable-space structure and a random variable $U:\Omega\to S$ such that the ambient measure on $\Omega$ is a probability measure, $U$ is measurable, $U$ is uniformly distributed on $H$, $U(\omega)\in H$ for every $\omega\in\Omega$, and $U$ has finite range.

### `ProbabilityTheory.IsUniform.measureReal_preimage_of_mem`
Lean: `[DiscreteMeasurableSpace S] [IsProbabilityMeasure μ] (h : IsUniform (↑A) X μ) (hX : Measurable X) (hs : s ∈ A) : μ.real (X ⁻¹' {s}) = 1 / ↑A.card`
English: Let $S$ carry the discrete $\sigma$-algebra (every subset measurable), let $\mu$ be a probability measure, let $A\subseteq S$ be a finite set, and let $X$ be a measurable $S$-valued random variable that is uniformly distributed on $A$ with respect to $\mu$. Then for every $s\in A$, $\mu(X=s)=1/|A|$ (as a real number).
