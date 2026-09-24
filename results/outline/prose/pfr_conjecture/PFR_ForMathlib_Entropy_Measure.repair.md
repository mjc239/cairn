You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Keep every
hypothesis the Lean shows, including instance assumptions such as `[Finite G]` or `[IsProbabilityMeasure μ]`
(say them in words: "$G$ is finite", "$\mu$ is a probability measure"), and the exact conclusion. Do not add
claims the Lean does not make. Purely structural instances (e.g. `[AddCommGroup G]`) and implicit arguments are not
shown and may stay implicit.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

### `ProbabilityTheory.measureEntropy_of_isProbabilityMeasure`
Lean: `(μ : Measure S) [IsZeroOrProbabilityMeasure μ] : Hm[μ] = ∑' (s : S), (μ.real {s}).negMulLog`
Previous English: For a probability measure $\mu$ on $S$, $H_m[\mu] = \sum_{s\in S} \mathrm{negMulLog}(\mu(\{s\}))$ (a possibly infinite sum, $\mathrm{tsum}$), where $\mathrm{negMulLog}(x) = -x\log x$.
Checker's issue: Strengthens the hypothesis [IsZeroOrProbabilityMeasure μ] to μ being a probability measure, omitting the zero-measure case.

### `ProbabilityTheory.integrable_of_finiteSupport`
Lean: `[MeasurableSingletonClass S] (μ : Measure S) [FiniteSupport μ] [IsFiniteMeasure μ] [Countable S] : Integrable f μ`
Docstring: The countability hypothesis can probably be dropped here. Proof is unwieldy and can probably be golfed.
Previous English: If $\mu$ is a measure on $S$ with finite support (under the standing assumptions, including countability of $S$), then every function $f$ on $S$ is integrable with respect to $\mu$.
Checker's issue: Drops the hypothesis [IsFiniteMeasure μ] (only finite support and countability are mentioned).

### `ProbabilityTheory.measureEntropy_of_isProbabilityMeasure_finite`
Lean: `(hA : μ (↑A)ᶜ = 0) [IsZeroOrProbabilityMeasure μ] : Hm[μ] = ∑ s ∈ A, (μ.real {s}).negMulLog`
Previous English: Let $\mu$ be a probability measure on $S$ and $A\subseteq S$ a finite set with $\mu(A^c)=0$. Then $H_m[\mu] = \sum_{s\in A}\mathrm{negMulLog}(\mu(\{s\}))$, where $\mathrm{negMulLog}(x)=-x\log x$.
Checker's issue: Strengthens the hypothesis [IsZeroOrProbabilityMeasure μ] to μ being a probability measure, omitting the zero-measure case.

### `ProbabilityTheory.measureMutualInfo_nonneg_aux`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass U] [FiniteSupport μ] [IsZeroOrProbabilityMeasure μ] : 0 ≤ Im[μ] ∧ (Im[μ] = 0 ↔ ∀ (p : S × U), μ.real {p} = (Measure.map Prod.fst μ).real {p.1} * (Measure.map Prod.snd μ).real {p.2})`
Docstring: An ambitious goal would be to replace FiniteSupport with finite entropy. Proof is long and slow; needs to be optimized
Previous English: For a (finitely supported, under the standing assumptions) measure $\mu$ on $S\times U$: $0 \le I_m[\mu]$, and moreover $I_m[\mu]=0$ if and only if for every $p=(p_1,p_2)\in S\times U$, $\mu(\{p\}) = (\pi_1{}_*\mu)(\{p_1\})\cdot(\pi_2{}_*\mu)(\{p_2\})$, i.e. $\mu$ is the product of its marginals.
Checker's issue: Drops the hypothesis [IsZeroOrProbabilityMeasure μ]; English only mentions finite support.
