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

### `ProbabilityTheory.entropy`
Lean: `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Previous English: For a random variable $X : \Omega \to S$ with values in a finite measurable space and a measure $\mu$ on $\Omega$, the entropy $H[X;\mu]$ is defined as the (measure) entropy of the law of $X$ under $\mu$.
Checker's issue: Adds that S is a finite measurable space, which the Lean definition does not assume.

### `ProbabilityTheory.condEntropy_of_injective`
Lean: `[MeasurableSingletonClass T] [MeasurableSingletonClass S] [Countable S] [MeasurableSingletonClass U] (μ : Measure Ω) [IsFiniteMeasure μ] (hX : Measurable X) (hY : Measurable Y) (f : T → S → U) (hf : ∀ (t : T), Function.Injective (f t)) [FiniteRange Y] : H[fun ω => f (Y ω) (X ω) | Y ; μ] = H[X | Y ; μ]`
Docstring: If `X : Ω → S`, `Y : Ω → T` are random variables, and `f : T × S → U` is injective for each fixed `t ∈ T`, then `H[f(Y, X) | Y] = H[X | Y]`. Thus for instance `H[X-Y|Y] = H[X|Y]`.
Previous English: Let $\mu$ be a measure, $X : \Omega \to S$ and $Y : \Omega \to T$ measurable random variables, and $f : T \to S \to U$ such that $f(t,\cdot)$ is injective for every $t \in T$. Then $H[f(Y,X) \mid Y] = H[X \mid Y]$. For instance, $H[X - Y \mid Y] = H[X \mid Y]$.
Checker's issue: Drops the hypotheses that μ is a finite measure [IsFiniteMeasure μ] and that Y has finite range.

### `ProbabilityTheory.condEntropy_eq_kernel_entropy`
Lean: `[MeasurableSingletonClass T] [Nonempty S] [Countable S] [MeasurableSingletonClass S] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) [IsFiniteMeasure μ] [FiniteRange Y] : H[X | Y ; μ] = Hk[condDistrib X Y μ , Measure.map Y μ]`
Docstring: Conditional entropy of a random variable is equal to the entropy of its conditional kernel.
Previous English: Let $X, Y$ be measurable random variables and $\mu$ a measure. Then the conditional entropy $H[X \mid Y;\mu]$ equals the kernel entropy $H_k[\mathrm{condDistrib}(X \mid Y;\mu),\ Y_*\mu]$ of the conditional distribution kernel of $X$ given $Y$, with respect to the law of $Y$.
Checker's issue: Drops the hypotheses [IsFiniteMeasure μ] and [FiniteRange Y]; English allows an arbitrary measure.

### `ProbabilityTheory.condMutualInfo_eq_kernel_mutualInfo`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] [Countable U] [MeasurableSingletonClass U] [Nonempty S] [Nonempty T] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange Z] : I[X : Y|Z;μ] = Ik[condDistrib (⟨X, Y⟩) Z μ , Measure.map Z μ]`
Docstring: The conditional mutual information agrees with the information of the conditional kernel.
Previous English: Let $X, Y, Z$ be measurable random variables and $\mu$ a measure. Then $I[X : Y \mid Z;\mu] = I_k[\mathrm{condDistrib}((X,Y) \mid Z;\mu),\ Z_*\mu]$, the kernel mutual information of the conditional distribution of $(X,Y)$ given $Z$ with respect to the law of $Z$.
Checker's issue: Drops the hypothesis [IsZeroOrProbabilityMeasure μ] (English allows an arbitrary measure) and [FiniteRange Z].

### `ProbabilityTheory.condMutualInfo_eq`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] [MeasurableSingletonClass U] [Countable U] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange Z] : I[X : Y|Z;μ] = H[X | Z ; μ] + H[Y | Z ; μ] - H[⟨X, Y⟩ | Z ; μ]`
Docstring: `I[X : Y| Z] = H[X| Z] + H[Y| Z] - H[X, Y| Z]`.
Previous English: Let $X, Y, Z$ be measurable random variables and $\mu$ a measure. Then $I[X : Y \mid Z] = H[X \mid Z] + H[Y \mid Z] - H[(X,Y) \mid Z]$.
Checker's issue: Drops the hypothesis [IsZeroOrProbabilityMeasure μ] (English allows an arbitrary measure) and [FiniteRange Z].

### `ProbabilityTheory.condMutualInfo_of_inj_map`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] [MeasurableSingletonClass U] [Countable U] [IsZeroOrProbabilityMeasure μ] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [MeasurableSingletonClass V] [Countable V] (f : U → S → V) (hf : ∀ (t : U), Function.Injective (f t)) [FiniteRange Z] : I[fun ω => f (Z ω) (X ω) : Y|Z;μ] = I[X : Y|Z;μ]`
Docstring: If `f(Z, X)` is injective for each fixed `Z`, then `I[f(Z, X) : Y| Z] = I[X : Y| Z]`.
Previous English: Let $X : \Omega \to S$, $Y$, $Z : \Omega \to U$ be measurable random variables and $f : U \to S \to V$ such that $f(u,\cdot)$ is injective for every $u \in U$. Then $I[f(Z,X) : Y \mid Z] = I[X : Y \mid Z]$ (with respect to $\mu$).
Checker's issue: Drops the hypothesis [IsZeroOrProbabilityMeasure μ] (English allows an arbitrary measure) and [FiniteRange Z].

### `ProbabilityTheory.mutualInfo_eq_entropy_sub_condEntropy`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] : I[X : Y ; μ] = H[X; μ] - H[X | Y ; μ]`
Docstring: `I[X : Y] = H[X] - H[X|Y]`.
Previous English: Let $X, Y$ be measurable random variables and $\mu$ a measure. Then $I[X : Y] = H[X] - H[X \mid Y]$.
Checker's issue: Drops the hypothesis [IsZeroOrProbabilityMeasure μ] (English allows an arbitrary measure) and the finite-range assumptions on X, Y.

### `ProbabilityTheory.mutualInfo_eq_zero`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] (hX : Measurable X) (hY : Measurable Y) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] : I[X : Y ; μ] = 0 ↔ IndepFun X Y μ`
Docstring: `I[X : Y] = 0` iff `X, Y` are independent.
Previous English: Let $X, Y$ be measurable random variables. Then $I[X : Y;\mu] = 0$ if and only if $X$ and $Y$ are independent with respect to $\mu$.
Checker's issue: Drops the hypothesis [IsZeroOrProbabilityMeasure μ] (English allows an arbitrary measure) and the finite-range assumptions on X, Y.

### `ProbabilityTheory.IndepFun.condEntropy_eq_entropy`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] (h : IndepFun X Y μ) (hX : Measurable X) (hY : Measurable Y) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] : H[X | Y ; μ] = H[X; μ]`
Previous English: Let $X, Y$ be measurable random variables that are independent with respect to $\mu$. Then $H[X \mid Y;\mu] = H[X;\mu]$.
Checker's issue: Drops the hypothesis [IsZeroOrProbabilityMeasure μ] (English allows an arbitrary measure) and the finite-range assumptions on X, Y.

### `ProbabilityTheory.condEntropy_two_eq_kernel_entropy`
Lean: `[MeasurableSingletonClass T] [Countable T] [Nonempty T] [Nonempty S] [MeasurableSingletonClass S] [Countable S] [Countable U] [MeasurableSingletonClass U] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) [IsProbabilityMeasure μ] [FiniteRange Y] [FiniteRange Z] : H[X | ⟨Y, Z⟩ ; μ] = Hk[(condDistrib (fun a => (Y a, X a)) Z μ).condKernel , (Measure.map Z μ).compProd (condDistrib (fun a => (Y a, X a)) Z μ).fst]`
Previous English: Let $X, Y, Z$ be measurable random variables and $\mu$ a measure. Then $H[X \mid (Y,Z);\mu]$ equals the kernel entropy $H_k[\kappa.\mathrm{condKernel},\ Z_*\mu \otimes \kappa.\mathrm{fst}]$, where $\kappa := \mathrm{condDistrib}((Y,X) \mid Z;\mu)$ is the conditional distribution of $(Y,X)$ given $Z$.
Checker's issue: Drops the hypothesis [IsProbabilityMeasure μ] (English says only 'a measure') and the finite-range assumptions on Y, Z.

### `ProbabilityTheory.cond_chain_rule`
Lean: `[Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : H[⟨X, Y⟩ | Z ; μ] = H[Y | Z ; μ] + H[X | ⟨Y, Z⟩ ; μ]`
Docstring: `H[X, Y | Z] = H[Y | Z] + H[X | Y, Z]`.
Previous English: Let $\mu$ be a measure and $X, Y, Z$ measurable random variables. Then $H[(X,Y) \mid Z] = H[Y \mid Z] + H[X \mid (Y,Z)]$.
Checker's issue: Drops the hypothesis [IsZeroOrProbabilityMeasure μ] (English allows an arbitrary measure) and the finite-range assumptions.

### `ProbabilityTheory.entropy_eq_sum_finset`
Lean: `[IsZeroOrProbabilityMeasure μ] (hA : (Measure.map X μ) (↑A)ᶜ = 0) : H[X; μ] = ∑ x ∈ A, ((Measure.map X μ).real {x}).negMulLog`
Previous English: Let $X$ be a random variable, $\mu$ a measure and $A$ a finite set such that the law $X_*\mu$ of $X$ gives measure $0$ to the complement of $A$. Then $H[X;\mu] = \sum_{x\in A} \mathrm{negMulLog}\big(X_*\mu(\{x\})\big)$, where $\mathrm{negMulLog}(t) = -t\log t$.
Checker's issue: Drops the hypothesis [IsZeroOrProbabilityMeasure μ] (English allows an arbitrary measure).

### `ProbabilityTheory.IsUniform.entropy_eq`
Lean: `[DiscreteMeasurableSpace S] [IsProbabilityMeasure μ] (hX : IsUniform (↑H) X μ) (hX' : Measurable X) : H[X; μ] = Real.log ↑(Nat.card ↥H)`
Docstring: If `X` is uniformly distributed on `H`, then `H[X] = log |H|`.
Previous English: Let $X$ be a measurable random variable that is uniformly distributed on the (finite) set $H$ with respect to $\mu$. Then $\mathbb{H}[X;\mu] = \log |H|$.
Checker's issue: Drops the hypothesis [IsProbabilityMeasure μ].

### `ProbabilityTheory.entropy_submodular`
Lean: `(μ : Measure Ω) [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [Countable S] [Countable T] [IsZeroOrProbabilityMeasure μ] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : H[X | ⟨Y, Z⟩ ; μ] ≤ H[X | Z ; μ]`
Docstring: `H[X | Y, Z] ≤ H[X | Z]`.
Previous English: Let $\mu$ be a measure and $X, Y, Z$ measurable random variables. Then $H[X \mid (Y,Z)] \le H[X \mid Z]$.
Checker's issue: Drops the hypothesis [IsZeroOrProbabilityMeasure μ] (English allows an arbitrary measure) and the finite-range assumptions.

### `ProbabilityTheory.entropy_triple_add_entropy_le`
Lean: `(μ : Measure Ω) [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [Countable S] [Countable T] [IsZeroOrProbabilityMeasure μ] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : H[⟨X, ⟨Y, Z⟩⟩; μ] + H[Z; μ] ≤ H[⟨X, Z⟩; μ] + H[⟨Y, Z⟩; μ]`
Docstring: The submodularity inequality: `H[X, Y, Z] + H[Z] ≤ H[X, Z] + H[Y, Z]`.
Previous English: Let $\mu$ be a measure and $X, Y, Z$ measurable random variables. Then $H[(X,(Y,Z))] + H[Z] \le H[(X,Z)] + H[(Y,Z)]$ (submodularity of entropy).
Checker's issue: Drops the hypothesis [IsZeroOrProbabilityMeasure μ] (English allows an arbitrary measure) and the finite-range assumptions.

### `ProbabilityTheory.entropy_sub_mutualInfo_eq_condEntropy`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] : H[X; μ] - I[X : Y ; μ] = H[X | Y ; μ]`
Docstring: `H[X] - I[X : Y] = H[X | Y]`.
Previous English: Let $X, Y$ be measurable random variables and $\mu$ a measure. Then $H[X] - I[X : Y] = H[X \mid Y]$.
Checker's issue: Drops the hypothesis [IsZeroOrProbabilityMeasure μ] (English allows an arbitrary measure) and the finite-range assumptions.

### `ProbabilityTheory.condMutualInfo_eq_zero`
Lean: `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] (hX : Measurable X) (hY : Measurable Y) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : I[X : Y|Z;μ] = 0 ↔ CondIndepFun X Y Z μ`
Docstring: `I[X : Y| Z]=0` iff `X, Y` are conditionally independent over `Z`.
Previous English: Let $X, Y$ be measurable random variables (and $Z$ a random variable). Then $I[X : Y \mid Z;\mu] = 0$ if and only if $X$ and $Y$ are conditionally independent relative to $Z$ with respect to $\mu$.
Checker's issue: Drops the hypothesis [IsZeroOrProbabilityMeasure μ] (English allows an arbitrary measure) and the finite-range assumptions.

### `ProbabilityTheory.ent_of_cond_indep`
Lean: `(μ : Measure Ω) [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [Countable S] [Countable T] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : CondIndepFun X Y Z μ) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : H[⟨X, ⟨Y, Z⟩⟩; μ] = H[⟨X, Z⟩; μ] + H[⟨Y, Z⟩; μ] - H[Z; μ]`
Docstring: If `X, Y` are conditionally independent over `Z`, then `H[X, Y, Z] = H[X, Z] + H[Y, Z] - H[Z]`.
Previous English: Let $\mu$ be a measure and $X, Y, Z$ measurable random variables such that $X$ and $Y$ are conditionally independent relative to $Z$. Then $H[(X,(Y,Z))] = H[(X,Z)] + H[(Y,Z)] - H[Z]$.
Checker's issue: Drops the hypothesis [IsZeroOrProbabilityMeasure μ] (English allows an arbitrary measure) and the finite-range assumptions.
