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

## Translations

### `ProbabilityTheory.measureEntropy`
Lean (short): `(μ : autoParam (Measure S) measureEntropy._auto_1) : ℝ`
Lean (full): `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
English: For a measure $\mu$ on a measurable space $S$, the entropy $H_m[\mu]$ is the (Shannon) entropy of the normalized measure $(\mu(S))^{-1}\mu$; normalizing by $(\mu(S))^{-1}$ extends the definition from probability measures to finite measures.

### `ProbabilityTheory.measureEntropy_of_isProbabilityMeasure`
Lean (short): `(μ : Measure S) [IsZeroOrProbabilityMeasure μ] : Hm[μ] = ∑' (s : S), (μ.real {s}).negMulLog`
Lean (full): `∀ {S : Type u_2} [inst : MeasurableSpace S] (μ : Measure S) [IsZeroOrProbabilityMeasure μ], Hm[μ] = ∑' (s : S), (μ.real {s}).negMulLog`
English: Let $S$ be a measurable space and let $\mu$ be a measure on $S$ that is either the zero measure or a probability measure. Then $H_m[\mu] = \sum_{s\in S} \mathrm{negMulLog}(\mu(\{s\}))$ (an unconditional sum `tsum` of real numbers), where $\mu(\{s\})$ is taken as a real number. Here, for a measure $\nu$ on a measurable space $Y$, $H_m[\nu] \in \mathbb{R}$ denotes the measure entropy `measureEntropy ν`, defined as $H_m[\nu] = \sum_{y \in Y} \mathrm{negMulLog}\big(\tilde\nu(\{y\})\big)$ (an unconditional sum `tsum` of reals), where $\tilde\nu = (\nu(Y))^{-1}\,\nu$ is $\nu$ rescaled by the inverse of its total mass (inverse taken in $[0,\infty]$), $\tilde\nu(\{y\})$ is taken as a real number (`Measure.real`), and $\mathrm{negMulLog}(x) = -x \log x$.

### `ProbabilityTheory.FiniteSupport`
Lean (short): `(μ : autoParam (Measure S) FiniteSupport._auto_1) : Prop`
Lean (full): `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) FiniteSupport._auto_1 → Prop`
Constructor (every field with its type): `∀ {S : Type u_2} [inst : MeasurableSpace S] {μ : autoParam (Measure S) FiniteSupport._auto_1}, (∃ (A : Finset S), ∀ᵐ (x : S) ∂μ, x ∈ A) → FiniteSupport μ`
Docstring: A measure has finite support if there exists a finite set whose complement has zero measure.
English: A measure $\mu$ on $S$ has finite support if there exists a finite set $A\subseteq S$ whose complement has measure zero, $\mu(A^c)=0$.

### `ProbabilityTheory.integrable_of_finiteSupport`
Lean (short): `[MeasurableSingletonClass S] (μ : Measure S) [FiniteSupport μ] [IsFiniteMeasure μ] [Countable S] : Integrable f μ`
Lean (full): `∀ {S : Type u_2} [inst : MeasurableSpace S] [MeasurableSingletonClass S] (μ : Measure S) [FiniteSupport μ] {β : Type u_5} [inst_3 : NormedAddCommGroup β] [IsFiniteMeasure μ] [Countable S] {f : S → β}, Integrable f μ`
Docstring: The countability hypothesis can probably be dropped here. Proof is unwieldy and can probably be golfed.
English: Let $S$ be a countable measurable space in which singletons are measurable, let $\mu$ be a finite measure on $S$ with finite support, and let $\beta$ be a normed additive commutative group. Then every function $f : S \to \beta$ is integrable with respect to $\mu$.

### `ProbabilityTheory.measureMutualInfo`
Lean (short): `(μ : autoParam (Measure (S × T)) measureMutualInfo._auto_1) : ℝ`
Lean (full): `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → autoParam (Measure (S × T)) measureMutualInfo._auto_1 → ℝ`
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (μ : Measure (S × T)) => Hm[Measure.map Prod.fst μ] + Hm[Measure.map Prod.snd μ] - Hm[μ]`
Docstring: The mutual information between the marginals of a measure on a product space.
English: Definition. Let $S$ and $T$ be measurable spaces. For a measure $\mu$ on the product $S\times T$ (an argument that Lean fills in automatically when omitted), $I_m[\mu]$ is a real number; according to its docstring, it is the mutual information between the marginals of $\mu$.

### `ProbabilityTheory.measureEntropy_of_isProbabilityMeasure_finite`
Lean (short): `(hA : μ (↑A)ᶜ = 0) [IsZeroOrProbabilityMeasure μ] : Hm[μ] = ∑ s ∈ A, (μ.real {s}).negMulLog`
Lean (full): `∀ {S : Type u_2} [inst : MeasurableSpace S] {μ : Measure S} {A : Finset S}, μ (↑A)ᶜ = (0 : ENNReal) → ∀ [IsZeroOrProbabilityMeasure μ], Hm[μ] = ∑ s ∈ A, (μ.real {s}).negMulLog`
English: Let $S$ be a measurable space, let $\mu$ be a measure on $S$ that is either the zero measure or a probability measure, and let $A \subseteq S$ be a finite set (a `Finset`) with $\mu(S \setminus A) = 0$. Then $H_m[\mu] = \sum_{s\in A}\mathrm{negMulLog}(\mu(\{s\}))$, where $\mu(\{s\})$ is taken as a real number. Here, for a measure $\nu$ on a measurable space $Y$, $H_m[\nu] \in \mathbb{R}$ denotes the measure entropy `measureEntropy ν`, defined as $H_m[\nu] = \sum_{y \in Y} \mathrm{negMulLog}\big(\tilde\nu(\{y\})\big)$ (an unconditional sum `tsum` of reals), where $\tilde\nu = (\nu(Y))^{-1}\,\nu$ is $\nu$ rescaled by the inverse of its total mass (inverse taken in $[0,\infty]$), $\tilde\nu(\{y\})$ is taken as a real number (`Measure.real`), and $\mathrm{negMulLog}(x) = -x \log x$.

### `ProbabilityTheory.measureMutualInfo_nonneg_aux`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass U] [FiniteSupport μ] [IsZeroOrProbabilityMeasure μ] : 0 ≤ Im[μ] ∧ (Im[μ] = 0 ↔ ∀ (p : S × U), μ.real {p} = (Measure.map Prod.fst μ).real {p.1} * (Measure.map Prod.snd μ).real {p.2})`
Lean (full): `∀ {S : Type u_2} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] [MeasurableSingletonClass S] [MeasurableSingletonClass U] {μ : Measure (S × U)} [FiniteSupport μ] [IsZeroOrProbabilityMeasure μ], (0 : ℝ) ≤ Im[μ] ∧ (Im[μ] = (0 : ℝ) ↔ ∀ (p : S × U), μ.real {p} = Measure.real (m := inst) (Measure.map Prod.fst μ) {p.1} * Measure.real (m := inst_1) (Measure.map Prod.snd μ) {p.2})`
Docstring: An ambitious goal would be to replace FiniteSupport with finite entropy. Proof is long and slow; needs to be optimized
English: Let $S$ and $U$ be measurable spaces in which all singletons are measurable, and let $\mu$ be a measure on $S\times U$ (with the product $\sigma$-algebra) that has finite support (there is a finite set whose complement has $\mu$-measure zero) and is either the zero measure or a probability measure. Then $0 \le I_m[\mu]$, and moreover $I_m[\mu]=0$ if and only if for every $p=(p_1,p_2)\in S\times U$, $\mu(\{p\}) = ((\pi_1)_*\mu)(\{p_1\})\cdot((\pi_2)_*\mu)(\{p_2\})$, all measures of singletons being taken as real numbers. Here, for a measure $\nu$ on a measurable space $Y$, $H_m[\nu] \in \mathbb{R}$ denotes the measure entropy `measureEntropy ν`, defined as $H_m[\nu] = \sum_{y \in Y} \mathrm{negMulLog}\big(\tilde\nu(\{y\})\big)$ (an unconditional sum `tsum` of reals), where $\tilde\nu = (\nu(Y))^{-1}\,\nu$ is $\nu$ rescaled by the inverse of its total mass (inverse taken in $[0,\infty]$), $\tilde\nu(\{y\})$ is taken as a real number (`Measure.real`), and $\mathrm{negMulLog}(x) = -x \log x$. For measurable spaces $S$, $U$ and a measure $\rho$ on $S \times U$, $I_m[\rho] \in \mathbb{R}$ denotes the mutual information `measureMutualInfo ρ` between the marginals of $\rho$, defined as $I_m[\rho] = H_m[(\pi_1)_*\rho] + H_m[(\pi_2)_*\rho] - H_m[\rho]$, where $\pi_1 : S \times U \to S$ and $\pi_2 : S \times U \to U$ are the coordinate projections and $(\pi_i)_*$ denotes the pushforward (`Measure.map`).

### `ProbabilityTheory.measureMutualInfo_of_not_isFiniteMeasure`
Lean (short): `(h : ¬IsFiniteMeasure μ) : Im[μ] = 0`
Lean (full): `∀ {S : Type u_2} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] {μ : Measure (S × U)}, ¬IsFiniteMeasure μ → Im[μ] = (0 : ℝ)`
English: Let $S$ and $U$ be types equipped with measurable-space structures, and let $\mu$ be a measure on the product $S \times U$. Write $H_m[\nu] = \mathrm{measureEntropy}\ \nu = \sum_{s} \phi\big(((\nu(\mathrm{univ}))^{-1}\nu)(\{s\})\big)$ (a sum over all points $s$ of the space, with $\phi(x) = -x\log x$) for a measure $\nu$ on a measurable space, and let $I_m[\mu] = \mathrm{measureMutualInfo}\ \mu = H_m[(\mathrm{fst})_*\mu] + H_m[(\mathrm{snd})_*\mu] - H_m[\mu]$, the mutual information between the marginals of $\mu$, where $(\mathrm{fst})_*\mu$ and $(\mathrm{snd})_*\mu$ are the pushforwards of $\mu$ under the projections onto $S$ and $U$. If $\mu$ is not a finite measure, then $I_m[\mu] = 0$.

### `ProbabilityTheory.measureMutualInfo_univ_smul`
Lean (short): `(μ : Measure (S × U)) : Im[(μ Set.univ)⁻¹ • μ] = Im[μ]`
Lean (full): `∀ {S : Type u_2} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] (μ : Measure (S × U)), Im[HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ] = Im[μ]`
English: Let $S$ and $U$ be measurable spaces and let $\mu$ be any measure on $S\times U$ (with the product $\sigma$-algebra). Then $I_m[(\mu(S\times U))^{-1}\,\mu] = I_m[\mu]$, where the inverse $(\mu(S\times U))^{-1}$ is taken in $[0,\infty]$ and scales the measure $\mu$. Here, for a measure $\nu$ on a measurable space $Y$, $H_m[\nu] \in \mathbb{R}$ denotes the measure entropy `measureEntropy ν`, defined as $H_m[\nu] = \sum_{y \in Y} \mathrm{negMulLog}\big(\tilde\nu(\{y\})\big)$ (an unconditional sum `tsum` of reals), where $\tilde\nu = (\nu(Y))^{-1}\,\nu$ is $\nu$ rescaled by the inverse of its total mass (inverse taken in $[0,\infty]$), $\tilde\nu(\{y\})$ is taken as a real number (`Measure.real`), and $\mathrm{negMulLog}(x) = -x \log x$. For measurable spaces $S$, $U$ and a measure $\rho$ on $S \times U$, $I_m[\rho] \in \mathbb{R}$ denotes the mutual information `measureMutualInfo ρ` between the marginals of $\rho$, defined as $I_m[\rho] = H_m[(\pi_1)_*\rho] + H_m[(\pi_2)_*\rho] - H_m[\rho]$, where $\pi_1 : S \times U \to S$ and $\pi_2 : S \times U \to U$ are the coordinate projections and $(\pi_i)_*$ denotes the pushforward (`Measure.map`).

### `ProbabilityTheory.measureMutualInfo_nonneg`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass U] [FiniteSupport μ] : 0 ≤ Im[μ]`
Lean (full): `∀ {S : Type u_2} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] [MeasurableSingletonClass S] [MeasurableSingletonClass U] {μ : Measure (S × U)} [FiniteSupport μ], (0 : ℝ) ≤ Im[μ]`
English: Let $S$ and $U$ be spaces in which singletons are measurable, and let $\mu$ be a measure on $S \times U$ with finite support. Then $0 \le I_m[\mu]$, the mutual information of the measure $\mu$.
