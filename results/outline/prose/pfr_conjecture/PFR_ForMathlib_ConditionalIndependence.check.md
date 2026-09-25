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
Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `FiniteRange` (inductive)
Lean: `{Ω : Type u_1} → {G : Type u_2} → (Ω → G) → Prop`
Docstring: The property of having a finite range.

#### `prod` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → (Ω → S) → (Ω → T) → Ω → S × T`
Docstring: The pair of two random variables
Definition: `fun {Ω : Type u_1} {S : Type u_2} {T : Type u_3} (X : Ω → S) (Y : Ω → T) (ω : Ω) => (X ω, Y ω)`

## Translations

### `ProbabilityTheory.CondIndepFun`
Lean (short): `(f : Ω → α) (g : Ω → β) (h : Ω → γ) (μ : autoParam (Measure Ω) CondIndepFun._auto_1) : Prop`
Lean (full): `{Ω : Type u_1} → {α : Type u_3} → {β : Type u_4} → {γ : Type u_5} → [inst : MeasurableSpace Ω] → [MeasurableSpace α] → [MeasurableSpace β] → [MeasurableSpace γ] → (Ω → α) → (Ω → β) → (Ω → γ) → autoParam (Measure Ω) CondIndepFun._auto_1 → Prop`
Docstring: The assertion that `f` and `g` are conditionally independent relative to `h`.
English: Let $\Omega$, $\alpha$, $\beta$, $\gamma$ be types, each equipped with a measurable-space structure. Given functions (random variables) $f : \Omega \to \alpha$, $g : \Omega \to \beta$, $h : \Omega \to \gamma$ and a measure $\mu$ on $\Omega$ (an auto-filled argument that, when omitted, is supplied by Lean's default tactic, i.e. the ambient measure $\mathrm{volume}$ on $\Omega$), $\mathrm{CondIndepFun}\ f\ g\ h\ \mu$ is the proposition that $f$ and $g$ are conditionally independent relative to $h$ with respect to $\mu$.

### `ProbabilityTheory.condIndep_copies`
Lean (short): `[MeasurableSingletonClass β] [Countable β] (X : Ω → α) (Y : Ω → β) (hX : Measurable X) (hY : Measurable Y) [FiniteRange Y] (μ : Measure Ω) [IsProbabilityMeasure μ] : ∃ Ω' x X₁ X₂ Y' ν, IsProbabilityMeasure ν ∧ Measurable X₁ ∧ Measurable X₂ ∧ Measurable Y' ∧ CondIndepFun X₁ X₂ Y' ν ∧ IdentDistrib (⟨X₁, Y'⟩) (⟨X, Y⟩) ν μ ∧ IdentDistrib (⟨X₂, Y'⟩) (⟨X, Y⟩) ν μ`
Lean (full): `∀ {Ω : Type u_1} {α β : Type u} [inst : MeasurableSpace Ω] [inst_1 : MeasurableSpace α] [inst_2 : MeasurableSpace β] [MeasurableSingletonClass β] [Countable β] (X : Ω → α) (Y : Ω → β), Measurable X → Measurable Y → ∀ [finY : FiniteRange Y] (μ : Measure Ω) [IsProbabilityMeasure μ], ∃ (Ω' : Type u) (x : MeasurableSpace Ω') (X₁ : Ω' → α) (X₂ : Ω' → α) (Y' : Ω' → β) (ν : Measure Ω'), IsProbabilityMeasure ν ∧ Measurable X₁ ∧ Measurable X₂ ∧ Measurable Y' ∧ CondIndepFun X₁ X₂ Y' ν ∧ IdentDistrib (⟨X₁, Y'⟩) (⟨X, Y⟩) ν μ ∧ IdentDistrib (⟨X₂, Y'⟩) (⟨X, Y⟩) ν μ`
Docstring: For `X, Y` random variables, there exist conditionally independent trials `X_1, X_2, Y'`.
English: Let $\Omega$ be a type and $\alpha$, $\beta$ types in a common universe $u$, with $\Omega$, $\alpha$, $\beta$ each equipped with a measurable-space structure; assume $\beta$ is countable and has measurable singletons. Let $X : \Omega \to \alpha$ and $Y : \Omega \to \beta$ be measurable functions, with $Y$ having finite range ($\mathrm{FiniteRange}\ Y$), and let $\mu$ be a probability measure on $\Omega$. Then there exist a type $\Omega'$ in universe $u$, a measurable-space structure on $\Omega'$, functions $X_1, X_2 : \Omega' \to \alpha$ and $Y' : \Omega' \to \beta$, and a measure $\nu$ on $\Omega'$ such that $\nu$ is a probability measure, $X_1$, $X_2$ and $Y'$ are measurable, $X_1$ and $X_2$ are conditionally independent relative to $Y'$ with respect to $\nu$ ($\mathrm{CondIndepFun}\ X_1\ X_2\ Y'\ \nu$), the pair $\omega' \mapsto (X_1(\omega'), Y'(\omega'))$ under $\nu$ is identically distributed with the pair $\omega \mapsto (X(\omega), Y(\omega))$ under $\mu$, and the pair $\omega' \mapsto (X_2(\omega'), Y'(\omega'))$ under $\nu$ is identically distributed with $\omega \mapsto (X(\omega), Y(\omega))$ under $\mu$.
