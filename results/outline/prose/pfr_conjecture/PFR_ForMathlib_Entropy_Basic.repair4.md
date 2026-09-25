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

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

#### `prod` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → (Ω → S) → (Ω → T) → Ω → S × T`
Docstring: The pair of two random variables
Definition: `fun {Ω : Type u_1} {S : Type u_2} {T : Type u_3} (X : Ω → S) (Y : Ω → T) (ω : Ω) => (X ω, Y ω)`

#### `FiniteRange` (inductive)
Lean: `{Ω : Type u_1} → {G : Type u_2} → (Ω → G) → Prop`
Docstring: The property of having a finite range.

#### `ProbabilityTheory.Kernel.entropy` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → ℝ`
Docstring: Entropy of a kernel with respect to a measure.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) (μ : Measure T) => ∫ (x : T), (fun (y : T) => measureEntropy.{u_2} (S := S) (κ y)) x ∂μ`

#### `ProbabilityTheory.IsUniform` (structure or class)
Lean: `{Ω : Type uΩ} → {S : Type uS} → [mΩ : MeasurableSpace Ω] → Set S → (Ω → S) → autoParam (Measure Ω) IsUniform._auto_1 → Prop`
Docstring: The assertion that the law of $X$ is the uniform probability measure on a finite set $H$. While in applications $H$ will be non-empty finite set, $X$ measurable, and and $μ$ a probability measure, it could be technically convenient to have a definition that works even without these hypotheses. (For instance, `isUniform` would be well-defined, but false, for infinite `H`). This should probably be refactored, requiring instead that `μ.map X = uniformOn H`.
Fields: `α`, `0`

## Flagged translations

### `ProbabilityTheory.entropy`
Lean (short): `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
Lean (full): `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Previous English: Let $\Omega$ and $S$ be measurable spaces. Definition: for a function $X : \Omega \to S$ and a measure $\mu$ on $\Omega$ (by default the canonical measure on $\Omega$), the real number $H[X;\mu]$; according to the docstring, this is the entropy of the random variable $X$ with values in a finite measurable space.
Checker's issue: Says the measure defaults to 'the canonical measure on Ω'; state exactly what the Lean shows (the default is `volume` of the MeasureSpace instance on Ω), or omit.

### `ProbabilityTheory.condEntropy`
Lean (short): `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) condEntropy._auto_1) : ℝ`
Lean (full): `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → autoParam (Measure Ω) condEntropy._auto_1 → ℝ`
Docstring: Conditional entropy of a random variable w.r.t. another. This is the expectation under the law of `Y` of the entropy of the law of `X` conditioned on the event `Y = y`.
Previous English: Let $\Omega$, $S$ and $T$ be measurable spaces. Definition: for functions $X : \Omega \to S$, $Y : \Omega \to T$ and a measure $\mu$ on $\Omega$ (by default the canonical measure on $\Omega$), the real number $H[X \mid Y;\mu]$; according to the docstring, this is the conditional entropy of $X$ with respect to $Y$, namely the expectation under the law of $Y$ of the entropy of the law of $X$ conditioned on the event $Y = y$.
Checker's issue: Says the measure defaults to 'the canonical measure on Ω'; state exactly what the Lean shows (the default is `volume` of the MeasureSpace instance on Ω), or omit.

### `ProbabilityTheory.condMutualInfo`
Lean (short): `(X : Ω → S) (Y : Ω → T) (Z : Ω → U) (μ : autoParam (Measure Ω) condMutualInfo._auto_1) : ℝ`
Lean (full): `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → {U : Type u_4} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace U] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → (Ω → U) → autoParam (Measure Ω) condMutualInfo._auto_1 → ℝ`
Docstring: The conditional mutual information `I[X : Y| Z]` is the mutual information of `X| Z=z` and `Y| Z=z`, integrated over `z`.
Previous English: Let $\Omega$, $S$, $T$ and $U$ be measurable spaces. Definition: for functions $X : \Omega \to S$, $Y : \Omega \to T$, $Z : \Omega \to U$ and a measure $\mu$ on $\Omega$ (by default the canonical measure on $\Omega$), the real number $I[X : Y \mid Z;\mu]$; according to the docstring, this conditional mutual information is the mutual information of $X \mid Z = z$ and $Y \mid Z = z$, integrated over $z$.
Checker's issue: Says the measure defaults to 'the canonical measure on Ω'; state exactly what the Lean shows (the default is `volume` of the MeasureSpace instance on Ω), or omit.

### `ProbabilityTheory.mutualInfo`
Lean (short): `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) mutualInfo._auto_1) : ℝ`
Lean (full): `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → autoParam (Measure Ω) mutualInfo._auto_1 → ℝ`
Docstring: The mutual information `I[X : Y]` of two random variables is defined to be `H[X] + H[Y] - H[X ; Y]`.
Previous English: Let $\Omega$, $S$ and $T$ be measurable spaces. Definition: for functions $X : \Omega \to S$, $Y : \Omega \to T$ and a measure $\mu$ on $\Omega$ (by default the canonical measure on $\Omega$), the real number $I[X : Y;\mu]$; according to the docstring, the mutual information of $X$ and $Y$ is defined to be $H[X] + H[Y] - H[(X, Y)]$ (entropies taken with respect to $\mu$).
Checker's issue: Says the measure defaults to 'the canonical measure on Ω'; state exactly what the Lean shows (the default is `volume` of the MeasureSpace instance on Ω), or omit.

### `ProbabilityTheory.condEntropy_two_eq_kernel_entropy`
Lean (short): `[MeasurableSingletonClass T] [Countable T] [Nonempty T] [Nonempty S] [MeasurableSingletonClass S] [Countable S] [Countable U] [MeasurableSingletonClass U] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) [IsProbabilityMeasure μ] [FiniteRange Y] [FiniteRange Z] : H[X | ⟨Y, Z⟩ ; μ] = Hk[(condDistrib (fun a => (Y a, X a)) Z μ).condKernel , (Measure.map Z μ).compProd (condDistrib (fun a => (Y a, X a)) Z μ).fst]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] {Z : Ω → U} [inst_2 : MeasurableSpace T] {X : Ω → S} {Y : Ω → T} [inst_3 : MeasurableSingletonClass T] [inst_4 : Countable T] [inst_5 : Nonempty T] [inst_6 : Nonempty S] [inst_7 : MeasurableSingletonClass S] [inst_8 : Countable S] [Countable U] [MeasurableSingletonClass U], Measurable X → Measurable Y → Measurable Z → ∀ (μ : Measure Ω) [inst_11 : IsProbabilityMeasure μ] [FiniteRange Y] [FiniteRange Z], H[X | ⟨Y, Z⟩ ; μ] = Hk[Kernel.condKernel (condDistrib (fun (a : Ω) => (Y a, X a)) Z μ) , Measure.compProd (Measure.map Z μ) (Kernel.fst.{u_4, u_3, u_2} (γ := S) (mγ := inst) (condDistrib (fun (a : Ω) => (Y a, X a)) Z μ))]`
Previous English: Let $S$, $T$, $U$ be countable measurable spaces with measurable singletons, with $S$ and $T$ nonempty. Let $\mu$ be a probability measure on $\Omega$ and let $X : \Omega \to S$, $Y : \Omega \to T$, $Z : \Omega \to U$ be measurable random variables with $Y$ and $Z$ of finite range. Then $H[X \mid (Y,Z);\mu]$ equals the kernel entropy $H_k[\kappa.\mathrm{condKernel},\ Z_*\mu \otimes \kappa.\mathrm{fst}]$, where $\kappa := \mathrm{condDistrib}((Y,X) \mid Z;\mu)$ is the conditional distribution kernel of $(Y,X)$ given $Z$, $\kappa.\mathrm{fst}$ is its first marginal, and $Z_*\mu \otimes \kappa.\mathrm{fst}$ is the composition-product of the law of $Z$ with that marginal.
Checker's issue: kappa.condKernel is used without being introduced or explained (only fst is glossed); the symbol is unintroduced.

### `ProbabilityTheory.IsUniform.entropy_eq`
Lean (short): `[DiscreteMeasurableSpace S] [IsProbabilityMeasure μ] (hX : IsUniform (↑H) X μ) (hX' : Measurable X) : H[X; μ] = Real.log ↑(Nat.card ↥H)`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [DiscreteMeasurableSpace S] {H : Finset S} {X : Ω → S} {μ : Measure Ω} [IsProbabilityMeasure μ], IsUniform (↑H) X μ → Measurable X → H[X; μ] = Real.log ↑(Nat.card.{u_2} ↥H)`
Docstring: If `X` is uniformly distributed on `H`, then `H[X] = log |H|`.
Previous English: Let $S$ be a measurable space in which every set is measurable, let $\mu$ be a probability measure on $\Omega$, and let $X : \Omega \to S$ be a measurable random variable that is uniformly distributed on the finite set $H \subseteq S$ with respect to $\mu$. Then $H[X;\mu] = \log |H|$.
Checker's issue: The letter H denotes both the finite set H and the entropy H[X;mu]; no letter may mean two things.
