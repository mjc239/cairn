You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.measureEntropy`
Lean: `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
English: For a measure $\mu$ on a measurable space $S$, the entropy $H_m[\mu]$ is the (Shannon) entropy of the normalized measure $(\mu(S))^{-1}\mu$; normalizing by $(\mu(S))^{-1}$ extends the definition from probability measures to finite measures.

### `ProbabilityTheory.measureEntropy_of_isProbabilityMeasure`
Lean: `(μ : Measure S) [IsZeroOrProbabilityMeasure μ] : Hm[μ] = ∑' (s : S), (μ.real {s}).negMulLog`
English: Let $\mu$ be a measure on $S$ that is zero or a probability measure. Then $H_m[\mu] = \sum_{s\in S} \mathrm{negMulLog}(\mu(\{s\}))$ (a possibly infinite sum, $\mathrm{tsum}$, of real numbers), where $\mathrm{negMulLog}(x) = -x\log x$.

### `ProbabilityTheory.FiniteSupport`
Lean: `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
English: A measure $\mu$ on $S$ has finite support if there exists a finite set $A\subseteq S$ whose complement has measure zero, $\mu(A^c)=0$.

### `ProbabilityTheory.integrable_of_finiteSupport`
Lean: `[MeasurableSingletonClass S] (μ : Measure S) [FiniteSupport μ] [IsFiniteMeasure μ] [Countable S] : Integrable f μ`
English: Let $S$ be a countable space with measurable singletons, and let $\mu$ be a finite measure on $S$ with finite support. Then every function $f$ on $S$ is integrable with respect to $\mu$.

### `ProbabilityTheory.measureMutualInfo`
Lean: `(μ : autoParam (Measure (S × T)) measureMutualInfo._auto_1) : ℝ`
English: For a measure $\mu$ on a product $S\times T$, the mutual information $I_m[\mu]$ between its two marginals, namely $I_m[\mu] = H_m[\pi_1{}_*\mu] + H_m[\pi_2{}_*\mu] - H_m[\mu]$ with $\pi_1,\pi_2$ the coordinate projections.

### `ProbabilityTheory.measureEntropy_of_isProbabilityMeasure_finite`
Lean: `(hA : μ (↑A)ᶜ = 0) [IsZeroOrProbabilityMeasure μ] : Hm[μ] = ∑ s ∈ A, (μ.real {s}).negMulLog`
English: Let $\mu$ be a measure on $S$ that is zero or a probability measure, and let $A\subseteq S$ be a finite set with $\mu(A^c)=0$. Then $H_m[\mu] = \sum_{s\in A}\mathrm{negMulLog}(\mu(\{s\}))$, where $\mathrm{negMulLog}(x)=-x\log x$.

### `ProbabilityTheory.measureMutualInfo_nonneg_aux`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass U] [FiniteSupport μ] [IsZeroOrProbabilityMeasure μ] : 0 ≤ Im[μ] ∧ (Im[μ] = 0 ↔ ∀ (p : S × U), μ.real {p} = (Measure.map Prod.fst μ).real {p.1} * (Measure.map Prod.snd μ).real {p.2})`
English: Let $S$ and $U$ have measurable singletons, and let $\mu$ be a measure on $S\times U$ with finite support that is zero or a probability measure. Then $0 \le I_m[\mu]$, and moreover $I_m[\mu]=0$ if and only if for every $p=(p_1,p_2)\in S\times U$, $\mu(\{p\}) = (\pi_1{}_*\mu)(\{p_1\})\cdot(\pi_2{}_*\mu)(\{p_2\})$, where $\pi_1,\pi_2$ are the coordinate projections.

### `ProbabilityTheory.measureMutualInfo_of_not_isFiniteMeasure`
Lean: `(h : ¬IsFiniteMeasure μ) : Im[μ] = 0`
English: If $\mu$ is not a finite measure, then $I_m[\mu]=0$.

### `ProbabilityTheory.measureMutualInfo_univ_smul`
Lean: `(μ : Measure (S × U)) : Im[(μ Set.univ)⁻¹ • μ] = Im[μ]`
English: For every measure $\mu$ on $S\times U$, $I_m[(\mu(S\times U))^{-1}\,\mu] = I_m[\mu]$.

### `ProbabilityTheory.measureMutualInfo_nonneg`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass U] [FiniteSupport μ] : 0 ≤ Im[μ]`
English: Let $S$ and $U$ be spaces in which singletons are measurable, and let $\mu$ be a measure on $S \times U$ with finite support. Then $0 \le I_m[\mu]$, the mutual information of the measure $\mu$.
