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

#### `ProbabilityTheory.FiniteSupport` (structure or class)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) FiniteSupport._auto_1 → Prop`
Docstring: A measure has finite support if there exists a finite set whose complement has zero measure.
Constructor (every field with its type): `∀ {S : Type u_2} [inst : MeasurableSpace S] {μ : autoParam (Measure S) FiniteSupport._auto_1}, (∃ (A : Finset S), ∀ᵐ (x : S) ∂μ, x ∈ A) → FiniteSupport μ`

## Flagged translations

### `ProbabilityTheory.measureEntropy`
Lean (short): `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Lean (full): `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Previous English: For a measure $\mu$ on a measurable space $S$, the entropy $H_m[\mu]$ is the (Shannon) entropy of the normalized measure $(\mu(S))^{-1}\mu$; normalizing by $(\mu(S))^{-1}$ extends the definition from probability measures to finite measures.
Checker's issue: The definition body is shown, but the English only calls it the '(Shannon) entropy' of the normalised measure. It never gives the formula H_m[μ] = Σ'_{s∈S} negMulLog(((μ univ)⁻¹•μ).real {s}), a real-valued tsum over singletons (which is 0 when the sum is not summable). For a general measure this is not a standard notion.

### `ProbabilityTheory.measureMutualInfo`
Lean (short): `(μ : autoParam (Measure (S × T)) measureMutualInfo._auto_1) : ℝ`
Lean (full): `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → autoParam (Measure (S × T)) measureMutualInfo._auto_1 → ℝ`
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (μ : Measure (S × T)) => Hm[Measure.map Prod.fst μ] + Hm[Measure.map Prod.snd μ] - Hm[μ]`
Docstring: The mutual information between the marginals of a measure on a product space.
Previous English: Definition. Let $S$ and $T$ be measurable spaces. For a measure $\mu$ on the product $S\times T$ (an argument that Lean fills in automatically when omitted), $I_m[\mu]$ is a real number; according to its docstring, it is the mutual information between the marginals of $\mu$.
Checker's issue: The definition body is shown (Hm[fst_*μ] + Hm[snd_*μ] − Hm[μ]), but the English only gives the docstring paraphrase 'mutual information between the marginals'. It does not state the formula.

### `ProbabilityTheory.measureMutualInfo_nonneg`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass U] [FiniteSupport μ] : 0 ≤ Im[μ]`
Lean (full): `∀ {S : Type u_2} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] [MeasurableSingletonClass S] [MeasurableSingletonClass U] {μ : Measure (S × U)} [FiniteSupport μ], (0 : ℝ) ≤ Im[μ]`
Previous English: Let $S$ and $U$ be spaces in which singletons are measurable, and let $\mu$ be a measure on $S \times U$ with finite support. Then $0 \le I_m[\mu]$, the mutual information of the measure $\mu$.
Checker's issue: I_m[μ] is only called 'the mutual information of the measure μ' and is never defined. The project notion is Hm[fst_*μ] + Hm[snd_*μ] − Hm[μ], with Hm normalising by (μ univ)⁻¹. Here μ is an arbitrary measure with finite support (it need not be a probability measure, or even finite), so the standard meaning of mutual information does not determine it. The spaces S and U are also only called 'spaces', not measurable spaces.
