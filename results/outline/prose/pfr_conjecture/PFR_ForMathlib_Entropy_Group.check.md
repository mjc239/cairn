You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption) and the English. Compare the English with the full statement.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.entropy_add_right`
Lean (short): `[Countable G] [MeasurableSingletonClass G] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨X, X + Y⟩; μ] = H[⟨X, Y⟩; μ]`
Lean (full): `∀ {Ω : Type uΩ} {G : Type uS} [mΩ : MeasurableSpace Ω] [Countable G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] [inst : AddGroup G] {X Y : Ω → G}, Measurable X → Measurable Y → ∀ (μ : Measure Ω), H[⟨X, X + Y⟩; μ] = H[⟨X, Y⟩; μ]`
English: Let $G$ be a countable additive group in which singletons are measurable, let $\mu$ be a measure on $\Omega$, and let $X, Y : \Omega \to G$ be measurable random variables. Then $H[(X, X+Y);\mu] = H[(X, Y);\mu]$.

### `ProbabilityTheory.entropy_add_left`
Lean (short): `[Countable G] [MeasurableSingletonClass G] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨Y + X, Y⟩; μ] = H[⟨X, Y⟩; μ]`
Lean (full): `∀ {Ω : Type uΩ} {G : Type uS} [mΩ : MeasurableSpace Ω] [Countable G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] [inst : AddGroup G] {X Y : Ω → G}, Measurable X → Measurable Y → ∀ (μ : Measure Ω), H[⟨Y + X, Y⟩; μ] = H[⟨X, Y⟩; μ]`
English: Let $G$ be a countable additive group in which singletons are measurable, let $\mu$ be a measure on $\Omega$, and let $X, Y : \Omega \to G$ be measurable random variables. Then $H[(Y+X, Y);\mu] = H[(X, Y);\mu]$.

### `ProbabilityTheory.entropy_sub_mutualInfo_le_entropy_sub`
Lean (short): `[Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] (hX : Measurable X) (hY : Measurable Y) : H[X; μ] - I[X : Y ; μ] ≤ H[X - Y; μ]`
Lean (full): `∀ {Ω : Type uΩ} {G : Type uS} [mΩ : MeasurableSpace Ω] [Countable G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] [inst : AddGroup G] {X : Ω → G} {μ : Measure Ω} [IsProbabilityMeasure μ] {Y : Ω → G} [FiniteRange X] [FiniteRange Y], Measurable X → Measurable Y → H[X; μ] - I[X : Y ; μ] ≤ H[X - Y; μ]`
English: Let $G$ be a countable additive group with measurable singletons, let $\mu$ be a probability measure on $\Omega$, and let $X, Y : \Omega \to G$ be measurable random variables, both of finite range. Then $H[X;\mu] - I[X:Y;\mu] \le H[X - Y;\mu]$.
