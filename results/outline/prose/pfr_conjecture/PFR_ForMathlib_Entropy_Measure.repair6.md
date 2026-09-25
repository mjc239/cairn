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

#### `ProbabilityTheory.FiniteSupport` (structure or class)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) FiniteSupport._auto_1 → Prop`
Docstring: A measure has finite support if there exists a finite set whose complement has zero measure.
Fields: `A`, `x`

#### `ProbabilityTheory.measureMutualInfo` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → autoParam (Measure (S × T)) measureMutualInfo._auto_1 → ℝ`
Docstring: The mutual information between the marginals of a measure on a product space.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (μ : Measure (S × T)) => Hm[Measure.map Prod.fst μ] + Hm[Measure.map Prod.snd μ] - Hm[μ]`

## Flagged translations

### `ProbabilityTheory.measureEntropy_of_isProbabilityMeasure`
Lean (short): `(μ : Measure S) [IsZeroOrProbabilityMeasure μ] : Hm[μ] = ∑' (s : S), (μ.real {s}).negMulLog`
Lean (full): `∀ {S : Type u_2} [inst : MeasurableSpace S] (μ : Measure S) [IsZeroOrProbabilityMeasure μ], Hm[μ] = ∑' (s : S), (μ.real {s}).negMulLog`
Previous English: Let $\mu$ be a measure on $S$ that is zero or a probability measure. Then $H_m[\mu] = \sum_{s\in S} \mathrm{negMulLog}(\mu(\{s\}))$ (a possibly infinite sum, $\mathrm{tsum}$, of real numbers), where $\mathrm{negMulLog}(x) = -x\log x$.
Checker's issue: H_m[μ] is used without being introduced (not named as the measure entropy / measureEntropy); S is not stated to be a measurable space.

### `ProbabilityTheory.measureEntropy_of_isProbabilityMeasure_finite`
Lean (short): `(hA : μ (↑A)ᶜ = 0) [IsZeroOrProbabilityMeasure μ] : Hm[μ] = ∑ s ∈ A, (μ.real {s}).negMulLog`
Lean (full): `∀ {S : Type u_2} [inst : MeasurableSpace S] {μ : Measure S} {A : Finset S}, μ (↑A)ᶜ = (0 : ENNReal) → ∀ [IsZeroOrProbabilityMeasure μ], Hm[μ] = ∑ s ∈ A, (μ.real {s}).negMulLog`
Previous English: Let $\mu$ be a measure on $S$ that is zero or a probability measure, and let $A\subseteq S$ be a finite set with $\mu(A^c)=0$. Then $H_m[\mu] = \sum_{s\in A}\mathrm{negMulLog}(\mu(\{s\}))$, where $\mathrm{negMulLog}(x)=-x\log x$.
Checker's issue: H_m[μ] is used without being introduced (not named as the measure entropy / measureEntropy); S is not stated to be a measurable space.

### `ProbabilityTheory.measureMutualInfo_nonneg_aux`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass U] [FiniteSupport μ] [IsZeroOrProbabilityMeasure μ] : 0 ≤ Im[μ] ∧ (Im[μ] = 0 ↔ ∀ (p : S × U), μ.real {p} = (Measure.map Prod.fst μ).real {p.1} * (Measure.map Prod.snd μ).real {p.2})`
Lean (full): `∀ {S : Type u_2} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] [MeasurableSingletonClass S] [MeasurableSingletonClass U] {μ : Measure (S × U)} [FiniteSupport μ] [IsZeroOrProbabilityMeasure μ], (0 : ℝ) ≤ Im[μ] ∧ (Im[μ] = (0 : ℝ) ↔ ∀ (p : S × U), μ.real {p} = Measure.real (m := inst) (Measure.map Prod.fst μ) {p.1} * Measure.real (m := inst_1) (Measure.map Prod.snd μ) {p.2})`
Docstring: An ambitious goal would be to replace FiniteSupport with finite entropy. Proof is long and slow; needs to be optimized
Previous English: Let $S$ and $U$ have measurable singletons, and let $\mu$ be a measure on $S\times U$ with finite support that is zero or a probability measure. Then $0 \le I_m[\mu]$, and moreover $I_m[\mu]=0$ if and only if for every $p=(p_1,p_2)\in S\times U$, $\mu(\{p\}) = (\pi_1{}_*\mu)(\{p_1\})\cdot(\pi_2{}_*\mu)(\{p_2\})$, where $\pi_1,\pi_2$ are the coordinate projections.
Checker's issue: I_m[μ] is used without being introduced (not named as the mutual information of μ / measureMutualInfo).

### `ProbabilityTheory.measureMutualInfo_univ_smul`
Lean (short): `(μ : Measure (S × U)) : Im[(μ Set.univ)⁻¹ • μ] = Im[μ]`
Lean (full): `∀ {S : Type u_2} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] (μ : Measure (S × U)), Im[HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ] = Im[μ]`
Previous English: For every measure $\mu$ on $S\times U$, $I_m[(\mu(S\times U))^{-1}\,\mu] = I_m[\mu]$.
Checker's issue: I_m[·] is used without being introduced (not named as measure mutual information), and S, U are not stated to be measurable spaces.
