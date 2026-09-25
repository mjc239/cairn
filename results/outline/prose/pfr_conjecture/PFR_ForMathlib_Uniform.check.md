You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. Compare the
English with the full statement; anything the English attributes to the docstring must actually be in it.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Definitions are held to the same standard: the English must name the setting the signature assumes
("for an abelian group $G$ and …, $\mathrm{rdist}$ is …"). Replacing an assumption by a stronger one (a metric
space where the Lean has a pseudometric space) is unfaithful too, and so is leaving a restrictive type unstated
(a natural number, a nonnegative real). Citations (theorem or lemma numbers) and remarks are claims too: each must
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: when the
prompt shows neither its definition nor a docstring saying it, the English must not supply one. Every variable
needs its type ("$f : G \to \mathbb{C}$", "$m$ a natural number"), every symbol must be introduced (notation such
as $M_{\mathcal B}$ included), and no letter may mean two things. When in doubt, flag it: a false alarm costs one
repair, a missed error stays in the outline. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.IsUniform`
Lean (short): `(H : Set S) (X : Ω → S) (μ : autoParam (Measure Ω) IsUniform._auto_1) : Prop`
Lean (full): `{Ω : Type uΩ} → {S : Type uS} → [mΩ : MeasurableSpace Ω] → Set S → (Ω → S) → autoParam (Measure Ω) IsUniform._auto_1 → Prop`
Docstring: The assertion that the law of $X$ is the uniform probability measure on a finite set $H$. While in applications $H$ will be non-empty finite set, $X$ measurable, and and $μ$ a probability measure, it could be technically convenient to have a definition that works even without these hypotheses. (For instance, `isUniform` would be well-defined, but false, for infinite `H`). This should probably be refactored, requiring instead that `μ.map X = uniformOn H`.
English: Let $\Omega$ be a measurable space and $S$ a type. For a set $H\subseteq S$, a function $X:\Omega\to S$ and a measure $\mu$ on $\Omega$ (supplied automatically by default), $\mathrm{IsUniform}(H,X,\mu)$ is a proposition. According to its docstring, it asserts that the law of $X$ is the uniform probability measure on the finite set $H$; the definition itself makes no assumptions on $H$, $X$ or $\mu$ (the docstring notes it would be well-defined but false for infinite $H$).

### `ProbabilityTheory.exists_isUniform_measureSpace`
Lean (short): `[MeasurableSingletonClass S] (H : Finset S) (h : H.Nonempty) : ∃ Ω mΩ U, IsProbabilityMeasure volume ∧ Measurable U ∧ IsUniform (↑H) U volume ∧ (∀ (ω : Ω), U ω ∈ H) ∧ FiniteRange U`
Lean (full): `∀ {S : Type uS} [inst : MeasurableSpace S] [MeasurableSingletonClass S] (H : Finset S), H.Nonempty → ∃ (Ω : Type uS) (mΩ : MeasureSpace Ω) (U : Ω → S), IsProbabilityMeasure.{uS} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume ∧ Measurable U ∧ IsUniform (↑H) U volume ∧ (∀ (ω : Ω), U ω ∈ H) ∧ FiniteRange U`
Docstring: Uniform distributions exist, version giving a measure space
English: Let $S$ be a space in which singletons are measurable, and let $H$ be a nonempty finite subset of $S$. Then there exist a type $\Omega$ with a measure-space structure and a random variable $U:\Omega\to S$ such that the ambient measure on $\Omega$ is a probability measure, $U$ is measurable, $U$ is uniformly distributed on $H$, $U(\omega)\in H$ for every $\omega\in\Omega$, and $U$ takes finitely many values.

### `ProbabilityTheory.IsUniform.measureReal_preimage_of_mem`
Lean (short): `[DiscreteMeasurableSpace S] [IsProbabilityMeasure μ] (h : IsUniform (↑A) X μ) (hX : Measurable X) (hs : s ∈ A) : μ.real (X ⁻¹' {s}) = 1 / ↑A.card`
Lean (full): `∀ {Ω : Type uΩ} {S : Type uS} [mΩ : MeasurableSpace Ω] {X : Ω → S} {μ : Measure Ω} [inst : MeasurableSpace S] [DiscreteMeasurableSpace S] {A : Finset S} [IsProbabilityMeasure μ], IsUniform (↑A) X μ → Measurable X → ∀ {s : S}, s ∈ A → μ.real (X ⁻¹' {s}) = (1 : ℝ) / ↑A.card`
Docstring: A "unit test" for the definition of uniform distribution.
English: Let $S$ carry the discrete $\sigma$-algebra (every subset measurable), let $\mu$ be a probability measure, let $A\subseteq S$ be a finite set, and let $X$ be a measurable $S$-valued random variable that is uniformly distributed on $A$ with respect to $\mu$. Then for every $s\in A$, $\mu(X=s)=1/|A|$ (as a real number).
