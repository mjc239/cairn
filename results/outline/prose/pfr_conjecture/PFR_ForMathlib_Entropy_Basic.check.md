You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.entropy`
Lean: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
English: For a random variable $X : \Omega \to S$ with values in a finite measurable space and a measure $\mu$ on $\Omega$, the entropy $H[X;\mu]$ is defined as the (measure) entropy of the law of $X$ under $\mu$.

### `ProbabilityTheory.condEntropy`
Lean: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) condEntropy._auto_1) : ℝ`
English: For random variables $X : \Omega \to S$, $Y : \Omega \to T$ and a measure $\mu$, the conditional entropy $H[X \mid Y;\mu]$ is defined as the expectation, under the law of $Y$, of the entropy of the law of $X$ conditioned on the event $Y = y$.

### `ProbabilityTheory.condEntropy_of_injective`
Lean: `[MeasurableSingletonClass T] [MeasurableSingletonClass S] [Countable S] [MeasurableSingletonClass U] (μ : Measure Ω) [IsFiniteMeasure μ] (hX : Measurable X) (hY : Measurable Y) (f : T → S → U) (hf : ∀ (t : T), Function.Injective (f t)) [FiniteRange Y] : H[fun ω => f (Y ω) (X ω) | Y ; μ] = H[X | Y ; μ]`
English: Let $\mu$ be a measure, $X : \Omega \to S$ and $Y : \Omega \to T$ measurable random variables, and $f : T \to S \to U$ such that $f(t,\cdot)$ is injective for every $t \in T$. Then $H[f(Y,X) \mid Y] = H[X \mid Y]$. For instance, $H[X - Y \mid Y] = H[X \mid Y]$.

### `ProbabilityTheory.condMutualInfo`
Lean: `(X : Ω → S) (Y : Ω → T) (Z : Ω → U) (μ : autoParam (Measure Ω) condMutualInfo._auto_1) : ℝ`
English: For random variables $X, Y, Z$ on $\Omega$ and a measure $\mu$, the conditional mutual information $I[X : Y \mid Z;\mu]$ is defined as the mutual information of $X$ and $Y$ under $\mu$ conditioned on $Z = z$, integrated over $z$ with respect to the law of $Z$.

### `ProbabilityTheory.condEntropy_eq_kernel_entropy`
Lean: `[MeasurableSingletonClass T] [Nonempty S] [Countable S] [MeasurableSingletonClass S] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) [IsFiniteMeasure μ] [FiniteRange Y] : H[X | Y ; μ] = Hk[condDistrib X Y μ , Measure.map Y μ]`
English: Let $X, Y$ be measurable random variables and $\mu$ a measure. Then the conditional entropy $H[X \mid Y;\mu]$ equals the kernel entropy $H_k[\mathrm{condDistrib}(X \mid Y;\mu),\ Y_*\mu]$ of the conditional distribution kernel of $X$ given $Y$, with respect to the law of $Y$.

### `ProbabilityTheory.condMutualInfo_eq_kernel_mutualInfo`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] [Countable U] [MeasurableSingletonClass U] [Nonempty S] [Nonempty T] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange Z] : I[X : Y|Z;μ] = Ik[condDistrib (⟨X, Y⟩) Z μ , Measure.map Z μ]`
English: Let $X, Y, Z$ be measurable random variables and $\mu$ a measure. Then $I[X : Y \mid Z;\mu] = I_k[\mathrm{condDistrib}((X,Y) \mid Z;\mu),\ Z_*\mu]$, the kernel mutual information of the conditional distribution of $(X,Y)$ given $Z$ with respect to the law of $Z$.

### `ProbabilityTheory.condMutualInfo_eq`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] [MeasurableSingletonClass U] [Countable U] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange Z] : I[X : Y|Z;μ] = H[X | Z ; μ] + H[Y | Z ; μ] - H[⟨X, Y⟩ | Z ; μ]`
English: Let $X, Y, Z$ be measurable random variables and $\mu$ a measure. Then $I[X : Y \mid Z] = H[X \mid Z] + H[Y \mid Z] - H[(X,Y) \mid Z]$.

### `ProbabilityTheory.condMutualInfo_of_inj_map`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] [MeasurableSingletonClass U] [Countable U] [IsZeroOrProbabilityMeasure μ] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [MeasurableSingletonClass V] [Countable V] (f : U → S → V) (hf : ∀ (t : U), Function.Injective (f t)) [FiniteRange Z] : I[fun ω => f (Z ω) (X ω) : Y|Z;μ] = I[X : Y|Z;μ]`
English: Let $X : \Omega \to S$, $Y$, $Z : \Omega \to U$ be measurable random variables and $f : U \to S \to V$ such that $f(u,\cdot)$ is injective for every $u \in U$. Then $I[f(Z,X) : Y \mid Z] = I[X : Y \mid Z]$ (with respect to $\mu$).

### `ProbabilityTheory.mutualInfo`
Lean: `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) mutualInfo._auto_1) : ℝ`
English: For random variables $X, Y$ on $\Omega$ and a measure $\mu$, the mutual information is defined as $I[X : Y] := H[X] + H[Y] - H[(X,Y)]$.

### `ProbabilityTheory.mutualInfo_eq_entropy_sub_condEntropy`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] : I[X : Y ; μ] = H[X; μ] - H[X | Y ; μ]`
English: Let $X, Y$ be measurable random variables and $\mu$ a measure. Then $I[X : Y] = H[X] - H[X \mid Y]$.

### `ProbabilityTheory.mutualInfo_eq_zero`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] (hX : Measurable X) (hY : Measurable Y) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] : I[X : Y ; μ] = 0 ↔ IndepFun X Y μ`
English: Let $X, Y$ be measurable random variables. Then $I[X : Y;\mu] = 0$ if and only if $X$ and $Y$ are independent with respect to $\mu$.

### `ProbabilityTheory.IndepFun.condEntropy_eq_entropy`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] (h : IndepFun X Y μ) (hX : Measurable X) (hY : Measurable Y) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] : H[X | Y ; μ] = H[X; μ]`
English: Let $X, Y$ be measurable random variables that are independent with respect to $\mu$. Then $H[X \mid Y;\mu] = H[X;\mu]$.

### `ProbabilityTheory.condEntropy_two_eq_kernel_entropy`
Lean: `[MeasurableSingletonClass T] [Countable T] [Nonempty T] [Nonempty S] [MeasurableSingletonClass S] [Countable S] [Countable U] [MeasurableSingletonClass U] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) [IsProbabilityMeasure μ] [FiniteRange Y] [FiniteRange Z] : H[X | ⟨Y, Z⟩ ; μ] = Hk[(condDistrib (fun a => (Y a, X a)) Z μ).condKernel , (Measure.map Z μ).compProd (condDistrib (fun a => (Y a, X a)) Z μ).fst]`
English: Let $X, Y, Z$ be measurable random variables and $\mu$ a measure. Then $H[X \mid (Y,Z);\mu]$ equals the kernel entropy $H_k[\kappa.\mathrm{condKernel},\ Z_*\mu \otimes \kappa.\mathrm{fst}]$, where $\kappa := \mathrm{condDistrib}((Y,X) \mid Z;\mu)$ is the conditional distribution of $(Y,X)$ given $Z$.

### `ProbabilityTheory.cond_chain_rule`
Lean: `[Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : H[⟨X, Y⟩ | Z ; μ] = H[Y | Z ; μ] + H[X | ⟨Y, Z⟩ ; μ]`
English: Let $\mu$ be a measure and $X, Y, Z$ measurable random variables. Then $H[(X,Y) \mid Z] = H[Y \mid Z] + H[X \mid (Y,Z)]$.

### `ProbabilityTheory.entropy_eq_sum_finset`
Lean: `[IsZeroOrProbabilityMeasure μ] (hA : (Measure.map X μ) (↑A)ᶜ = 0) : H[X; μ] = ∑ x ∈ A, ((Measure.map X μ).real {x}).negMulLog`
English: Let $X$ be a random variable, $\mu$ a measure and $A$ a finite set such that the law $X_*\mu$ of $X$ gives measure $0$ to the complement of $A$. Then $H[X;\mu] = \sum_{x\in A} \mathrm{negMulLog}\big(X_*\mu(\{x\})\big)$, where $\mathrm{negMulLog}(t) = -t\log t$.

### `ProbabilityTheory.IsUniform.entropy_eq`
Lean: `[DiscreteMeasurableSpace S] [IsProbabilityMeasure μ] (hX : IsUniform (↑H) X μ) (hX' : Measurable X) : H[X; μ] = Real.log ↑(Nat.card ↥H)`
English: Let $X$ be a measurable random variable that is uniformly distributed on the (finite) set $H$ with respect to $\mu$. Then $\mathbb{H}[X;\mu] = \log |H|$.

### `ProbabilityTheory.entropy_submodular`
Lean: `(μ : Measure Ω) [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [Countable S] [Countable T] [IsZeroOrProbabilityMeasure μ] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : H[X | ⟨Y, Z⟩ ; μ] ≤ H[X | Z ; μ]`
English: Let $\mu$ be a measure and $X, Y, Z$ measurable random variables. Then $H[X \mid (Y,Z)] \le H[X \mid Z]$.

### `ProbabilityTheory.entropy_triple_add_entropy_le`
Lean: `(μ : Measure Ω) [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [Countable S] [Countable T] [IsZeroOrProbabilityMeasure μ] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : H[⟨X, ⟨Y, Z⟩⟩; μ] + H[Z; μ] ≤ H[⟨X, Z⟩; μ] + H[⟨Y, Z⟩; μ]`
English: Let $\mu$ be a measure and $X, Y, Z$ measurable random variables. Then $H[(X,(Y,Z))] + H[Z] \le H[(X,Z)] + H[(Y,Z)]$ (submodularity of entropy).

### `ProbabilityTheory.entropy_sub_mutualInfo_eq_condEntropy`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] : H[X; μ] - I[X : Y ; μ] = H[X | Y ; μ]`
English: Let $X, Y$ be measurable random variables and $\mu$ a measure. Then $H[X] - I[X : Y] = H[X \mid Y]$.

### `ProbabilityTheory.prob_ge_exp_neg_entropy`
Lean: `[MeasurableSingletonClass S] [Nonempty S] (X : Ω → S) (μ : Measure Ω) (hX : Measurable X) [FiniteRange X] : ∃ s, μ Set.univ * ↑(Real.exp (-H[X; μ])).toNNReal ≤ (Measure.map X μ) {s}`
English: Let $X : \Omega \to S$ be a measurable random variable and $\mu$ a measure on $\Omega$. Then there exists $s \in S$ such that $\mu(\Omega)\cdot e^{-H[X;\mu]} \le X_*\mu(\{s\})$; in particular (for a probability measure) $\mathbb{P}[X = s] \ge e^{-H[X]}$.

### `ProbabilityTheory.mutualInfo_nonneg`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) [FiniteRange X] [FiniteRange Y] : 0 ≤ I[X : Y ; μ]`
English: Let $X, Y$ be measurable random variables and $\mu$ a measure. Then $0 \le I[X : Y;\mu]$.

### `ProbabilityTheory.condMutualInfo_eq_zero`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] (hX : Measurable X) (hY : Measurable Y) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : I[X : Y|Z;μ] = 0 ↔ CondIndepFun X Y Z μ`
English: Let $X, Y$ be measurable random variables (and $Z$ a random variable). Then $I[X : Y \mid Z;\mu] = 0$ if and only if $X$ and $Y$ are conditionally independent relative to $Z$ with respect to $\mu$.

### `ProbabilityTheory.ent_of_cond_indep`
Lean: `(μ : Measure Ω) [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [Countable S] [Countable T] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : CondIndepFun X Y Z μ) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : H[⟨X, ⟨Y, Z⟩⟩; μ] = H[⟨X, Z⟩; μ] + H[⟨Y, Z⟩; μ] - H[Z; μ]`
English: Let $\mu$ be a measure and $X, Y, Z$ measurable random variables such that $X$ and $Y$ are conditionally independent relative to $Z$. Then $H[(X,(Y,Z))] = H[(X,Z)] + H[(Y,Z)] - H[Z]$.
