You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. A "Project
definitions" section first lists the project notions the statements refer to (statement, docstring, body,
fields). Compare the English with the full statement; anything the English attributes to the docstring must
actually be in it.

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
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: a project
notion's description must agree with its entry under "Project definitions" (statement, docstring, definition body,
fields), and a library notion may only be given its standard mathematical meaning; otherwise flag it. Every variable
needs its type ("$f : G \to \mathbb{C}$", "$m$ a natural number"), every symbol must be introduced, by definition
or by name ("the Ruzsa distance $d[X;Y]$", "the maximal operator $M_{\mathcal B}$"), and no letter may mean two
things. When in doubt, flag it: a false alarm costs one repair, a missed error stays in the outline.
A definition whose body is shown must be described by what it defines (in words or a formula that agrees with the
body), not only by a paraphrase of its docstring. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `FiniteRange` (inductive)
Lean: `{Ω : Type u_1} → {G : Type u_2} → (Ω → G) → Prop`
Docstring: The property of having a finite range.
Constructor (every field with its type): `∀ {Ω : Type u_1} {G : Type u_2} {X : Ω → G}, (Set.range X).Finite → FiniteRange X`

## Translations

### `ProbabilityTheory.independent_copies3_nondep_finiteRange`
Lean (short): `[MeasurableSingletonClass α] (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₃ : Measurable X₃) [FiniteRange X₁] [FiniteRange X₂] [FiniteRange X₃] (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) (μ₃ : Measure Ω₃) [IsProbabilityMeasure μ₁] [IsProbabilityMeasure μ₂] [IsProbabilityMeasure μ₃] : ∃ A x μA X₁' X₂' X₃', IsProbabilityMeasure μA ∧ iIndepFun ![X₁', X₂', X₃'] μA ∧ Measurable X₁' ∧ Measurable X₂' ∧ Measurable X₃' ∧ IdentDistrib X₁' X₁ μA μ₁ ∧ IdentDistrib X₂' X₂ μA μ₂ ∧ IdentDistrib X₃' X₃ μA μ₃ ∧ FiniteRange X₁' ∧ FiniteRange X₂' ∧ FiniteRange X₃'`
Lean (full): `∀ {α : Type u} [mS : MeasurableSpace α] [MeasurableSingletonClass α] {Ω₁ : Type u_1} {Ω₂ : Type u_2} {Ω₃ : Type u_3} [inst : MeasurableSpace Ω₁] [inst_1 : MeasurableSpace Ω₂] [inst_2 : MeasurableSpace Ω₃] {X₁ : Ω₁ → α} {X₂ : Ω₂ → α} {X₃ : Ω₃ → α}, Measurable X₁ → Measurable X₂ → Measurable X₃ → ∀ [FiniteRange X₁] [FiniteRange X₂] [FiniteRange X₃] (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) (μ₃ : Measure Ω₃) [hμ₁ : IsProbabilityMeasure μ₁] [hμ₂ : IsProbabilityMeasure μ₂] [hμ₃ : IsProbabilityMeasure μ₃], ∃ (A : Type (max u_1 u_2 u_3)) (x : MeasurableSpace A) (μA : Measure A) (X₁' : A → α) (X₂' : A → α) (X₃' : A → α), IsProbabilityMeasure μA ∧ iIndepFun (β := fun (a : Fin (Nat.succ (0 : ℕ)).succ.succ) => α) ![X₁', X₂', X₃'] μA ∧ Measurable X₁' ∧ Measurable X₂' ∧ Measurable X₃' ∧ IdentDistrib X₁' X₁ μA μ₁ ∧ IdentDistrib X₂' X₂ μA μ₂ ∧ IdentDistrib X₃' X₃ μA μ₃ ∧ FiniteRange X₁' ∧ FiniteRange X₂' ∧ FiniteRange X₃'`
Docstring: A version of `independent_copies3_nondep` that guarantees that the copies have `FiniteRange` if the original variables do.
English: Let $\alpha$ be a measurable space with measurable singletons, and let $X_1:\Omega_1\to\alpha$, $X_2:\Omega_2\to\alpha$, $X_3:\Omega_3\to\alpha$ be measurable random variables, each of finite range, where $\mu_1,\mu_2,\mu_3$ are probability measures on $\Omega_1,\Omega_2,\Omega_3$ respectively. Then there exist a measurable space $A$, a probability measure $\mu_A$ on $A$ and measurable maps $X_1',X_2',X_3' : A \to \alpha$ that are jointly independent under $\mu_A$, such that $X_i'$ under $\mu_A$ has the same distribution as $X_i$ under $\mu_i$ for $i=1,2,3$, and each $X_i'$ has finite range.

### `ProbabilityTheory.independent_copies_finiteRange`
Lean (short): `(hX : Measurable X) (hY : Measurable Y) [FiniteRange X] [FiniteRange Y] [MeasurableSingletonClass α] [MeasurableSingletonClass β] (μ : Measure Ω) (μ' : Measure Ω') [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] : ∃ ν X' Y', IsProbabilityMeasure ν ∧ Measurable X' ∧ Measurable Y' ∧ IndepFun X' Y' ν ∧ IdentDistrib X' X ν μ ∧ IdentDistrib Y' Y ν μ' ∧ FiniteRange X' ∧ FiniteRange Y'`
Lean (full): `∀ {Ω : Type u_1} {Ω' : Type u_2} {α : Type u_3} {β : Type u_5} {mΩ : MeasurableSpace Ω} {mΩ' : MeasurableSpace Ω'} {mα : MeasurableSpace α} {mβ : MeasurableSpace β} {X : Ω → α} {Y : Ω' → β}, Measurable X → Measurable Y → ∀ [FiniteRange X] [FiniteRange Y] [MeasurableSingletonClass α] [MeasurableSingletonClass β] (μ : Measure Ω) (μ' : Measure Ω') [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'], ∃ (ν : Measure (α × β)) (X' : α × β → α) (Y' : α × β → β), IsProbabilityMeasure ν ∧ Measurable X' ∧ Measurable Y' ∧ IndepFun X' Y' ν ∧ IdentDistrib X' X ν μ ∧ IdentDistrib Y' Y ν μ' ∧ FiniteRange X' ∧ FiniteRange Y'`
Docstring: A version of `independent_copies` that guarantees that the copies have `FiniteRange` if the original variables do.
English: (A version of `independent_copies` guaranteeing finite range of the copies.) Let $\Omega$, $\Omega'$ be measurable spaces and let $\alpha$, $\beta$ be measurable spaces in which every singleton is measurable. Let $X:\Omega\to\alpha$ and $Y:\Omega'\to\beta$ be measurable functions, each with finite range, and let $\mu$ and $\mu'$ be probability measures on $\Omega$ and $\Omega'$ respectively. Then there exist a measure $\nu$ on $\alpha\times\beta$ and functions $X':\alpha\times\beta\to\alpha$ and $Y':\alpha\times\beta\to\beta$ such that $\nu$ is a probability measure, $X'$ and $Y'$ are measurable, $X'$ and $Y'$ are independent under $\nu$, $X'$ under $\nu$ has the same distribution as $X$ under $\mu$, $Y'$ under $\nu$ has the same distribution as $Y$ under $\mu'$, and $X'$ and $Y'$ both have finite range.
