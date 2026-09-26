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

#### `ProbabilityTheory.entropy` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Definition: `fun {Ω : Type u_1} {S : Type u_2} [MeasurableSpace Ω] [MeasurableSpace S] (X : Ω → S) (μ : Measure Ω) => Hm[Measure.map X μ]`

#### `prod` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → (Ω → S) → (Ω → T) → Ω → S × T`
Docstring: The pair of two random variables
Definition: `fun {Ω : Type u_1} {S : Type u_2} {T : Type u_3} (X : Ω → S) (Y : Ω → T) (ω : Ω) => (X ω, Y ω)`

#### `FiniteRange` (inductive)
Lean: `{Ω : Type u_1} → {G : Type u_2} → (Ω → G) → Prop`
Docstring: The property of having a finite range.
Constructor (every field with its type): `∀ {Ω : Type u_1} {G : Type u_2} {X : Ω → G}, (Set.range X).Finite → FiniteRange X`

#### `ProbabilityTheory.mutualInfo` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → autoParam (Measure Ω) mutualInfo._auto_1 → ℝ`
Docstring: The mutual information `I[X : Y]` of two random variables is defined to be `H[X] + H[Y] - H[X ; Y]`.
Definition: `fun {Ω : Type u_1} {S : Type u_2} {T : Type u_3} [MeasurableSpace Ω] [MeasurableSpace S] [MeasurableSpace T] (X : Ω → S) (Y : Ω → T) (μ : Measure Ω) => H[X; μ] + H[Y; μ] - H[⟨X, Y⟩; μ]`

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

## Translations

### `ProbabilityTheory.entropy_add_right`
Lean (short): `[Countable G] [MeasurableSingletonClass G] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨X, X + Y⟩; μ] = H[⟨X, Y⟩; μ]`
Lean (full): `∀ {Ω : Type uΩ} {G : Type uS} [mΩ : MeasurableSpace Ω] [Countable G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] [inst : AddGroup G] {X Y : Ω → G}, Measurable X → Measurable Y → ∀ (μ : Measure Ω), H[⟨X, X + Y⟩; μ] = H[⟨X, Y⟩; μ]`
Docstring: `H[X, X + Y] = H[X, Y]`
English: Let $\Omega$ be a measurable space and let $G$ be a countable additive group carrying a measurable-space structure in which all singletons are measurable. Let $X, Y : \Omega \to G$ be measurable functions and let $\mu$ be a measure on $\Omega$ (not necessarily a probability measure). Then $H[(X, X+Y);\mu] = H[(X, Y);\mu]$, where $X + Y$ is the pointwise sum. Here, for a measurable space $V$ and a function $Z : \Omega \to V$, $H[Z;\mu]$ = `entropy Z μ` is the entropy of $Z$ with respect to $\mu$ (docstring: entropy of a random variable with values in a finite measurable space), defined as the measure entropy of the pushforward $m = Z_*\mu$: $H[Z;\mu] = \sum_{v \in V} -m'(\{v\}) \log m'(\{v\})$ (an unconditional sum, taken as $0$ if not summable), where $m' = m(V)^{-1} m$ is the normalized measure and $m'(\{v\})$ its real value (`measureEntropy`); and $(Z_1, Z_2)$ denotes the pair $\omega \mapsto (Z_1(\omega), Z_2(\omega))$ (`prod`), with values in the product measurable space.

### `ProbabilityTheory.entropy_add_left`
Lean (short): `[Countable G] [MeasurableSingletonClass G] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) : H[⟨Y + X, Y⟩; μ] = H[⟨X, Y⟩; μ]`
Lean (full): `∀ {Ω : Type uΩ} {G : Type uS} [mΩ : MeasurableSpace Ω] [Countable G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] [inst : AddGroup G] {X Y : Ω → G}, Measurable X → Measurable Y → ∀ (μ : Measure Ω), H[⟨Y + X, Y⟩; μ] = H[⟨X, Y⟩; μ]`
Docstring: `H[Y + X, Y] = H[X, Y]`
English: Let $\Omega$ be a measurable space and let $G$ be a countable additive group carrying a measurable-space structure in which all singletons are measurable. Let $X, Y : \Omega \to G$ be measurable functions and let $\mu$ be a measure on $\Omega$ (not necessarily a probability measure). Then $H[(Y+X, Y);\mu] = H[(X, Y);\mu]$, where $Y + X$ is the pointwise sum. Here, for a measurable space $V$ and a function $Z : \Omega \to V$, $H[Z;\mu]$ = `entropy Z μ` is the entropy of $Z$ with respect to $\mu$ (docstring: entropy of a random variable with values in a finite measurable space), defined as the measure entropy of the pushforward $m = Z_*\mu$: $H[Z;\mu] = \sum_{v \in V} -m'(\{v\}) \log m'(\{v\})$ (an unconditional sum, taken as $0$ if not summable), where $m' = m(V)^{-1} m$ is the normalized measure and $m'(\{v\})$ its real value (`measureEntropy`); and $(Z_1, Z_2)$ denotes the pair $\omega \mapsto (Z_1(\omega), Z_2(\omega))$ (`prod`), with values in the product measurable space.

### `ProbabilityTheory.entropy_sub_mutualInfo_le_entropy_sub`
Lean (short): `[Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] (hX : Measurable X) (hY : Measurable Y) : H[X; μ] - I[X : Y ; μ] ≤ H[X - Y; μ]`
Lean (full): `∀ {Ω : Type uΩ} {G : Type uS} [mΩ : MeasurableSpace Ω] [Countable G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] [inst : AddGroup G] {X : Ω → G} {μ : Measure Ω} [IsProbabilityMeasure μ] {Y : Ω → G} [FiniteRange X] [FiniteRange Y], Measurable X → Measurable Y → H[X; μ] - I[X : Y ; μ] ≤ H[X - Y; μ]`
Docstring: `H[X] - I[X : Y] ≤ H[X - Y]`
English: Let $\Omega$ be a measurable space and let $G$ be a countable additive group carrying a measurable-space structure in which all singletons are measurable. Let $\mu$ be a probability measure on $\Omega$, and let $X, Y : \Omega \to G$ be measurable functions each having finite range (`FiniteRange`). Then $$H[X;\mu] - I[X : Y;\mu] \le H[X - Y;\mu],$$ where $X - Y$ is the pointwise difference and $I[X : Y;\mu]$ = `mutualInfo X Y μ` is the mutual information, defined as $H[X;\mu] + H[Y;\mu] - H[(X,Y);\mu]$. Here, for a measurable space $V$ and a function $Z : \Omega \to V$, $H[Z;\mu]$ = `entropy Z μ` is the entropy of $Z$ with respect to $\mu$ (docstring: entropy of a random variable with values in a finite measurable space), defined as the measure entropy of the pushforward $m = Z_*\mu$: $H[Z;\mu] = \sum_{v \in V} -m'(\{v\}) \log m'(\{v\})$ (an unconditional sum, taken as $0$ if not summable), where $m' = m(V)^{-1} m$ is the normalized measure and $m'(\{v\})$ its real value (`measureEntropy`); and $(Z_1, Z_2)$ denotes the pair $\omega \mapsto (Z_1(\omega), Z_2(\omega))$ (`prod`), with values in the product measurable space.
