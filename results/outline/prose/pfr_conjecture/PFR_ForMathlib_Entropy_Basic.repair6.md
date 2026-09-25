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

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

#### `prod` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → (Ω → S) → (Ω → T) → Ω → S × T`
Docstring: The pair of two random variables
Definition: `fun {Ω : Type u_1} {S : Type u_2} {T : Type u_3} (X : Ω → S) (Y : Ω → T) (ω : Ω) => (X ω, Y ω)`

## Flagged translations

### `ProbabilityTheory.entropy`
Lean (short): `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
Lean (full): `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Definition: `fun {Ω : Type u_1} {S : Type u_2} [MeasurableSpace Ω] [MeasurableSpace S] (X : Ω → S) (μ : Measure Ω) => Hm[Measure.map X μ]`
Docstring: Entropy of a random variable with values in a finite measurable space.
Previous English: Let $\Omega$ and $S$ be measurable spaces. Definition: for a function $X : \Omega\to S$ and a measure $\mu$ on $\Omega$ (if omitted, $\mu$ is filled in automatically as `volume`, the measure of a `MeasureSpace` instance on $\Omega$), the real number $H[X;\mu]$. According to the docstring, this is the entropy of a random variable with values in a finite measurable space.
Checker's issue: Definition body is shown (H[X;μ] = Hm[X_*μ], the measure entropy of the pushforward: Σ_s negMulLog of the normalized mass ((μ.map X)(univ))⁻¹·(μ.map X)({s})), but the English gives only the type and a docstring paraphrase. The docstring's 'finite measurable space' is also not a hypothesis of the definition.

### `ProbabilityTheory.condMutualInfo`
Lean (short): `(X : Ω → S) (Y : Ω → T) (Z : Ω → U) (μ : autoParam (Measure Ω) condMutualInfo._auto_1) : ℝ`
Lean (full): `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → {U : Type u_4} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace U] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → (Ω → U) → autoParam (Measure Ω) condMutualInfo._auto_1 → ℝ`
Definition: `fun {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [MeasurableSpace Ω] [MeasurableSpace S] [inst_1 : MeasurableSpace U] [MeasurableSpace T] (X : Ω → S) (Y : Ω → T) (Z : Ω → U) (μ : Measure Ω) => @integral _ _ _ _ inst_1 (Measure.map Z μ) fun (x : U) => (fun (z : U) => H[X | Z ← z; μ] + H[Y | Z ← z; μ] - H[⟨X, Y⟩ | Z ← z; μ]) x`
Docstring: The conditional mutual information `I[X : Y| Z]` is the mutual information of `X| Z=z` and `Y| Z=z`, integrated over `z`.
Previous English: Let $\Omega$, $S$, $T$ and $U$ be measurable spaces. Definition: for functions $X : \Omega\to S$, $Y : \Omega\to T$, $Z : \Omega\to U$ and a measure $\mu$ on $\Omega$ (if omitted, $\mu$ is filled in automatically as `volume`, the measure of a `MeasureSpace` instance on $\Omega$), the real number $I[X : Y\mid Z;\mu]$. According to the docstring, this conditional mutual information is the mutual information of $X\mid Z=z$ and $Y\mid Z=z$, integrated over $z$.
Checker's issue: Definition body is shown but the English only paraphrases the docstring. It never gives the formula ∫ (H[X | Z←z; μ] + H[Y | Z←z; μ] − H[⟨X,Y⟩ | Z←z; μ]) d(Z_*μ)(z), and it does not say that the integral is taken against the law Z_*μ of Z ('integrated over z' leaves the measure unspecified).

### `ProbabilityTheory.entropy_eq_sum_finset`
Lean (short): `[IsZeroOrProbabilityMeasure μ] (hA : (Measure.map X μ) (↑A)ᶜ = 0) : H[X; μ] = ∑ x ∈ A, ((Measure.map X μ).real {x}).negMulLog`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] {X : Ω → S} {μ : Measure Ω} [IsZeroOrProbabilityMeasure μ] {A : Finset S}, (Measure.map X μ : Measure S) (↑A)ᶜ = (0 : ENNReal) → H[X; μ] = ∑ x ∈ A, (Measure.real (m := inst) (Measure.map X μ) {x}).negMulLog`
Previous English: Let $\mu$ be a measure on $\Omega$ that is zero or a probability measure, let $X : \Omega \to S$ be a random variable, and let $A$ be a finite subset of $S$ such that the law $X_*\mu$ gives measure $0$ to the complement of $A$. Then $H[X;\mu] = \sum_{x\in A} \mathrm{negMulLog}\big(X_*\mu(\{x\})\big)$, where $\mathrm{negMulLog}(t) = -t\log t$ and $X_*\mu(\{x\})$ is taken as a real number.
Checker's issue: S is never introduced: its type/measurable-space structure is not stated (and Ω's measurable space is not stated either). 'Random variable' is also ambiguous about measurability, which the Lean does not assume.
