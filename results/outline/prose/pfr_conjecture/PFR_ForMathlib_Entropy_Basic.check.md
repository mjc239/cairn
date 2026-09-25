You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. Compare the
English with the full statement; anything the English attributes to the docstring must actually be in it.

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
be supported by the docstring or the Lean. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.entropy`
Lean (short): `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
Lean (full): `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
English: Let $\Omega$ and $S$ be measurable spaces. Definition: for a function $X : \Omega \to S$ and a measure $\mu$ on $\Omega$ (by default the canonical measure on $\Omega$), the real number $H[X;\mu]$; according to the docstring, this is the entropy of the random variable $X$ with values in a finite measurable space.

### `ProbabilityTheory.condEntropy`
Lean (short): `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) condEntropy._auto_1) : ℝ`
Lean (full): `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → autoParam (Measure Ω) condEntropy._auto_1 → ℝ`
Docstring: Conditional entropy of a random variable w.r.t. another. This is the expectation under the law of `Y` of the entropy of the law of `X` conditioned on the event `Y = y`.
English: Let $\Omega$, $S$ and $T$ be measurable spaces. Definition: for functions $X : \Omega \to S$, $Y : \Omega \to T$ and a measure $\mu$ on $\Omega$ (by default the canonical measure on $\Omega$), the real number $H[X \mid Y;\mu]$; according to the docstring, this is the conditional entropy of $X$ with respect to $Y$, namely the expectation under the law of $Y$ of the entropy of the law of $X$ conditioned on the event $Y = y$.

### `ProbabilityTheory.condEntropy_of_injective`
Lean (short): `[MeasurableSingletonClass T] [MeasurableSingletonClass S] [Countable S] [MeasurableSingletonClass U] (μ : Measure Ω) [IsFiniteMeasure μ] (hX : Measurable X) (hY : Measurable Y) (f : T → S → U) (hf : ∀ (t : T), Function.Injective (f t)) [FiniteRange Y] : H[fun ω => f (Y ω) (X ω) | Y ; μ] = H[X | Y ; μ]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] [inst_2 : MeasurableSpace T] {X : Ω → S} {Y : Ω → T} [MeasurableSingletonClass T] [MeasurableSingletonClass S] [Countable S] [MeasurableSingletonClass U] (μ : Measure Ω) [IsFiniteMeasure μ], Measurable X → Measurable Y → ∀ (f : T → S → U), (∀ (t : T), Function.Injective (f t)) → ∀ [FiniteRange Y], H[fun ω => f (Y ω) (X ω) | Y ; μ] = H[X | Y ; μ]`
Docstring: If `X : Ω → S`, `Y : Ω → T` are random variables, and `f : T × S → U` is injective for each fixed `t ∈ T`, then `H[f(Y, X) | Y] = H[X | Y]`. Thus for instance `H[X-Y|Y] = H[X|Y]`.
English: Let $S$, $T$, $U$ be measurable spaces with measurable singletons, with $S$ countable. Let $\mu$ be a finite measure on $\Omega$, let $X : \Omega \to S$ and $Y : \Omega \to T$ be measurable random variables with $Y$ of finite range, and let $f : T \to S \to U$ be such that $f(t,\cdot)$ is injective for every $t \in T$. Then $H[f(Y,X) \mid Y;\mu] = H[X \mid Y;\mu]$.

### `ProbabilityTheory.condMutualInfo`
Lean (short): `(X : Ω → S) (Y : Ω → T) (Z : Ω → U) (μ : autoParam (Measure Ω) condMutualInfo._auto_1) : ℝ`
Lean (full): `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → {U : Type u_4} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace U] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → (Ω → U) → autoParam (Measure Ω) condMutualInfo._auto_1 → ℝ`
Docstring: The conditional mutual information `I[X : Y| Z]` is the mutual information of `X| Z=z` and `Y| Z=z`, integrated over `z`.
English: Let $\Omega$, $S$, $T$ and $U$ be measurable spaces. Definition: for functions $X : \Omega \to S$, $Y : \Omega \to T$, $Z : \Omega \to U$ and a measure $\mu$ on $\Omega$ (by default the canonical measure on $\Omega$), the real number $I[X : Y \mid Z;\mu]$; according to the docstring, this conditional mutual information is the mutual information of $X \mid Z = z$ and $Y \mid Z = z$, integrated over $z$.

### `ProbabilityTheory.condEntropy_eq_kernel_entropy`
Lean (short): `[MeasurableSingletonClass T] [Nonempty S] [Countable S] [MeasurableSingletonClass S] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) [IsFiniteMeasure μ] [FiniteRange Y] : H[X | Y ; μ] = Hk[condDistrib X Y μ , Measure.map Y μ]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] {X : Ω → S} {Y : Ω → T} [MeasurableSingletonClass T] [inst_3 : Nonempty S] [inst_4 : Countable S] [inst_5 : MeasurableSingletonClass S], Measurable X → Measurable Y → ∀ (μ : Measure Ω) [inst_6 : IsFiniteMeasure μ] [FiniteRange Y], H[X | Y ; μ] = Hk[condDistrib X Y μ , Measure.map Y μ]`
Docstring: Conditional entropy of a random variable is equal to the entropy of its conditional kernel.
English: Let $S$ and $T$ be measurable spaces with measurable singletons, with $S$ countable and nonempty. Let $\mu$ be a finite measure on $\Omega$ and let $X : \Omega \to S$, $Y : \Omega \to T$ be measurable random variables with $Y$ of finite range. Then the conditional entropy $H[X \mid Y;\mu]$ equals the kernel entropy $H_k[\mathrm{condDistrib}(X \mid Y;\mu),\ Y_*\mu]$ of the conditional distribution kernel of $X$ given $Y$, with respect to the law $Y_*\mu$ of $Y$.

### `ProbabilityTheory.condMutualInfo_eq_kernel_mutualInfo`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] [Countable U] [MeasurableSingletonClass U] [Nonempty S] [Nonempty T] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange Z] : I[X : Y|Z;μ] = Ik[condDistrib (⟨X, Y⟩) Z μ , Measure.map Z μ]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] {X : Ω → S} {Y : Ω → T} {Z : Ω → U} [inst_2 : MeasurableSpace T] [inst_3 : MeasurableSingletonClass S] [inst_4 : MeasurableSingletonClass T] [inst_5 : Countable S] [inst_6 : Countable T] [Countable U] [MeasurableSingletonClass U] [inst_9 : Nonempty S] [inst_10 : Nonempty T], Measurable X → Measurable Y → Measurable Z → ∀ (μ : Measure Ω) [inst_11 : IsZeroOrProbabilityMeasure μ] [FiniteRange Z], I[X : Y|Z;μ] = Ik[condDistrib (⟨X, Y⟩) Z μ , Measure.map Z μ]`
Docstring: The conditional mutual information agrees with the information of the conditional kernel.
English: Let $S$, $T$, $U$ be countable measurable spaces with measurable singletons, with $S$ and $T$ nonempty. Let $\mu$ be a measure on $\Omega$ that is zero or a probability measure, and let $X : \Omega \to S$, $Y : \Omega \to T$, $Z : \Omega \to U$ be measurable random variables with $Z$ of finite range. Then $I[X : Y \mid Z;\mu] = I_k[\mathrm{condDistrib}((X,Y) \mid Z;\mu),\ Z_*\mu]$, the kernel mutual information of the conditional distribution of $(X,Y)$ given $Z$ with respect to the law of $Z$.

### `ProbabilityTheory.condMutualInfo_eq`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] [MeasurableSingletonClass U] [Countable U] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange Z] : I[X : Y|Z;μ] = H[X | Z ; μ] + H[Y | Z ; μ] - H[⟨X, Y⟩ | Z ; μ]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] {X : Ω → S} {Y : Ω → T} {Z : Ω → U} [inst_2 : MeasurableSpace T] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] [MeasurableSingletonClass U] [Countable U], Measurable X → Measurable Y → Measurable Z → ∀ (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange Z], I[X : Y|Z;μ] = H[X | Z ; μ] + H[Y | Z ; μ] - H[⟨X, Y⟩ | Z ; μ]`
Docstring: `I[X : Y| Z] = H[X| Z] + H[Y| Z] - H[X, Y| Z]`.
English: Let $S$, $T$, $U$ be countable measurable spaces with measurable singletons. Let $\mu$ be a measure on $\Omega$ that is zero or a probability measure, and let $X : \Omega \to S$, $Y : \Omega \to T$, $Z : \Omega \to U$ be measurable random variables with $Z$ of finite range. Then $I[X : Y \mid Z;\mu] = H[X \mid Z;\mu] + H[Y \mid Z;\mu] - H[(X,Y) \mid Z;\mu]$.

### `ProbabilityTheory.condMutualInfo_of_inj_map`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] [MeasurableSingletonClass U] [Countable U] [IsZeroOrProbabilityMeasure μ] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [MeasurableSingletonClass V] [Countable V] (f : U → S → V) (hf : ∀ (t : U), Function.Injective (f t)) [FiniteRange Z] : I[fun ω => f (Z ω) (X ω) : Y|Z;μ] = I[X : Y|Z;μ]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] {X : Ω → S} {Y : Ω → T} {Z : Ω → U} {μ : Measure Ω} [inst_2 : MeasurableSpace T] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] [MeasurableSingletonClass U] [Countable U] [IsZeroOrProbabilityMeasure μ], Measurable X → Measurable Y → Measurable Z → ∀ {V : Type u_6} [inst_10 : MeasurableSpace V] [MeasurableSingletonClass V] [Countable V] (f : U → S → V), (∀ (t : U), Function.Injective (f t)) → ∀ [FiniteRange Z], I[fun ω => f (Z ω) (X ω) : Y|Z;μ] = I[X : Y|Z;μ]`
Docstring: If `f(Z, X)` is injective for each fixed `Z`, then `I[f(Z, X) : Y| Z] = I[X : Y| Z]`.
English: Let $S$, $T$, $U$, $V$ be countable measurable spaces with measurable singletons. Let $\mu$ be a measure on $\Omega$ that is zero or a probability measure, let $X : \Omega \to S$, $Y : \Omega \to T$, $Z : \Omega \to U$ be measurable random variables with $Z$ of finite range, and let $f : U \to S \to V$ be such that $f(u,\cdot)$ is injective for every $u \in U$. Then $I[f(Z,X) : Y \mid Z;\mu] = I[X : Y \mid Z;\mu]$.

### `ProbabilityTheory.mutualInfo`
Lean (short): `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) mutualInfo._auto_1) : ℝ`
Lean (full): `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → autoParam (Measure Ω) mutualInfo._auto_1 → ℝ`
Docstring: The mutual information `I[X : Y]` of two random variables is defined to be `H[X] + H[Y] - H[X ; Y]`.
English: Let $\Omega$, $S$ and $T$ be measurable spaces. Definition: for functions $X : \Omega \to S$, $Y : \Omega \to T$ and a measure $\mu$ on $\Omega$ (by default the canonical measure on $\Omega$), the real number $I[X : Y;\mu]$; according to the docstring, the mutual information of $X$ and $Y$ is defined to be $H[X] + H[Y] - H[(X, Y)]$ (entropies taken with respect to $\mu$).

### `ProbabilityTheory.mutualInfo_eq_entropy_sub_condEntropy`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] : I[X : Y ; μ] = H[X; μ] - H[X | Y ; μ]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] {X : Ω → S} {Y : Ω → T} [inst_1 : MeasurableSpace T] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T], Measurable X → Measurable Y → ∀ (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y], I[X : Y ; μ] = H[X; μ] - H[X | Y ; μ]`
Docstring: `I[X : Y] = H[X] - H[X|Y]`.
English: Let $S$ and $T$ be countable measurable spaces with measurable singletons. Let $\mu$ be a measure on $\Omega$ that is zero or a probability measure, and let $X : \Omega \to S$, $Y : \Omega \to T$ be measurable random variables, both of finite range. Then $I[X : Y;\mu] = H[X;\mu] - H[X \mid Y;\mu]$.

### `ProbabilityTheory.mutualInfo_eq_zero`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass T] (hX : Measurable X) (hY : Measurable Y) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] : I[X : Y ; μ] = 0 ↔ IndepFun X Y μ`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] {X : Ω → S} {Y : Ω → T} [inst_1 : MeasurableSpace T] [MeasurableSingletonClass S] [MeasurableSingletonClass T], Measurable X → Measurable Y → ∀ {μ : Measure Ω} [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y], I[X : Y ; μ] = (0 : ℝ) ↔ IndepFun X Y μ`
Docstring: `I[X : Y] = 0` iff `X, Y` are independent.
English: Let $S$ and $T$ be measurable spaces with measurable singletons. Let $\mu$ be a measure on $\Omega$ that is zero or a probability measure, and let $X : \Omega \to S$, $Y : \Omega \to T$ be measurable random variables, both of finite range. Then $I[X : Y;\mu] = 0$ if and only if $X$ and $Y$ are independent with respect to $\mu$.

### `ProbabilityTheory.IndepFun.condEntropy_eq_entropy`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] (h : IndepFun X Y μ) (hX : Measurable X) (hY : Measurable Y) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] : H[X | Y ; μ] = H[X; μ]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] {X : Ω → S} {Y : Ω → T} [inst_1 : MeasurableSpace T] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] {μ : Measure Ω}, IndepFun X Y μ → Measurable X → Measurable Y → ∀ [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y], H[X | Y ; μ] = H[X; μ]`
English: Let $S$ and $T$ be countable measurable spaces with measurable singletons. Let $\mu$ be a measure on $\Omega$ that is zero or a probability measure, and let $X : \Omega \to S$, $Y : \Omega \to T$ be measurable random variables, both of finite range, that are independent with respect to $\mu$. Then $H[X \mid Y;\mu] = H[X;\mu]$.

### `ProbabilityTheory.condEntropy_two_eq_kernel_entropy`
Lean (short): `[MeasurableSingletonClass T] [Countable T] [Nonempty T] [Nonempty S] [MeasurableSingletonClass S] [Countable S] [Countable U] [MeasurableSingletonClass U] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) [IsProbabilityMeasure μ] [FiniteRange Y] [FiniteRange Z] : H[X | ⟨Y, Z⟩ ; μ] = Hk[(condDistrib (fun a => (Y a, X a)) Z μ).condKernel , (Measure.map Z μ).compProd (condDistrib (fun a => (Y a, X a)) Z μ).fst]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] {Z : Ω → U} [inst_2 : MeasurableSpace T] {X : Ω → S} {Y : Ω → T} [inst_3 : MeasurableSingletonClass T] [inst_4 : Countable T] [inst_5 : Nonempty T] [inst_6 : Nonempty S] [inst_7 : MeasurableSingletonClass S] [inst_8 : Countable S] [Countable U] [MeasurableSingletonClass U], Measurable X → Measurable Y → Measurable Z → ∀ (μ : Measure Ω) [inst_11 : IsProbabilityMeasure μ] [FiniteRange Y] [FiniteRange Z], H[X | ⟨Y, Z⟩ ; μ] = Hk[Kernel.condKernel (condDistrib (fun a => (Y a, X a)) Z μ) , Measure.compProd (Measure.map Z μ) (Kernel.fst.{u_4, u_3, u_2} (γ := S) (mγ := inst) (condDistrib (fun a => (Y a, X a)) Z μ))]`
English: Let $S$, $T$, $U$ be countable measurable spaces with measurable singletons, with $S$ and $T$ nonempty. Let $\mu$ be a probability measure on $\Omega$ and let $X : \Omega \to S$, $Y : \Omega \to T$, $Z : \Omega \to U$ be measurable random variables with $Y$ and $Z$ of finite range. Then $H[X \mid (Y,Z);\mu]$ equals the kernel entropy $H_k[\kappa.\mathrm{condKernel},\ Z_*\mu \otimes \kappa.\mathrm{fst}]$, where $\kappa := \mathrm{condDistrib}((Y,X) \mid Z;\mu)$ is the conditional distribution kernel of $(Y,X)$ given $Z$, $\kappa.\mathrm{fst}$ is its first marginal, and $Z_*\mu \otimes \kappa.\mathrm{fst}$ is the composition-product of the law of $Z$ with that marginal.

### `ProbabilityTheory.cond_chain_rule`
Lean (short): `[Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : H[⟨X, Y⟩ | Z ; μ] = H[Y | Z ; μ] + H[X | ⟨Y, Z⟩ ; μ]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] {X : Ω → S} {Y : Ω → T} {Z : Ω → U} [inst_2 : MeasurableSpace T] [Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ], Measurable X → Measurable Y → Measurable Z → ∀ [FiniteRange X] [FiniteRange Y] [FiniteRange Z], H[⟨X, Y⟩ | Z ; μ] = H[Y | Z ; μ] + H[X | ⟨Y, Z⟩ ; μ]`
Docstring: `H[X, Y | Z] = H[Y | Z] + H[X | Y, Z]`.
English: Let $S$, $T$, $U$ be countable measurable spaces with measurable singletons. Let $\mu$ be a measure on $\Omega$ that is zero or a probability measure, and let $X : \Omega \to S$, $Y : \Omega \to T$, $Z : \Omega \to U$ be measurable random variables, each of finite range. Then $H[(X,Y) \mid Z;\mu] = H[Y \mid Z;\mu] + H[X \mid (Y,Z);\mu]$.

### `ProbabilityTheory.entropy_eq_sum_finset`
Lean (short): `[IsZeroOrProbabilityMeasure μ] (hA : (Measure.map X μ) (↑A)ᶜ = 0) : H[X; μ] = ∑ x ∈ A, ((Measure.map X μ).real {x}).negMulLog`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] {X : Ω → S} {μ : Measure Ω} [IsZeroOrProbabilityMeasure μ] {A : Finset S}, (Measure.map X μ : Measure S) (↑A)ᶜ = (0 : ENNReal) → H[X; μ] = ∑ x ∈ A, (Measure.real (m := inst) (Measure.map X μ) {x}).negMulLog`
English: Let $\mu$ be a measure on $\Omega$ that is zero or a probability measure, let $X : \Omega \to S$ be a random variable, and let $A$ be a finite subset of $S$ such that the law $X_*\mu$ gives measure $0$ to the complement of $A$. Then $H[X;\mu] = \sum_{x\in A} \mathrm{negMulLog}\big(X_*\mu(\{x\})\big)$, where $\mathrm{negMulLog}(t) = -t\log t$ and $X_*\mu(\{x\})$ is taken as a real number.

### `ProbabilityTheory.IsUniform.entropy_eq`
Lean (short): `[DiscreteMeasurableSpace S] [IsProbabilityMeasure μ] (hX : IsUniform (↑H) X μ) (hX' : Measurable X) : H[X; μ] = Real.log ↑(Nat.card ↥H)`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [DiscreteMeasurableSpace S] {H : Finset S} {X : Ω → S} {μ : Measure Ω} [IsProbabilityMeasure μ], IsUniform (↑H) X μ → Measurable X → H[X; μ] = Real.log ↑(Nat.card.{u_2} ↥H)`
Docstring: If `X` is uniformly distributed on `H`, then `H[X] = log |H|`.
English: Let $S$ be a measurable space in which every set is measurable, let $\mu$ be a probability measure on $\Omega$, and let $X : \Omega \to S$ be a measurable random variable that is uniformly distributed on the finite set $H \subseteq S$ with respect to $\mu$. Then $H[X;\mu] = \log |H|$.

### `ProbabilityTheory.entropy_submodular`
Lean (short): `(μ : Measure Ω) [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [Countable S] [Countable T] [IsZeroOrProbabilityMeasure μ] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : H[X | ⟨Y, Z⟩ ; μ] ≤ H[X | Z ; μ]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] {X : Ω → S} {Y : Ω → T} {Z : Ω → U} (μ : Measure Ω) [inst_2 : MeasurableSpace T] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [Countable S] [Countable T] [IsZeroOrProbabilityMeasure μ], Measurable X → Measurable Y → Measurable Z → ∀ [FiniteRange X] [FiniteRange Y] [FiniteRange Z], H[X | ⟨Y, Z⟩ ; μ] ≤ H[X | Z ; μ]`
Docstring: `H[X | Y, Z] ≤ H[X | Z]`.
English: Let $S$, $T$, $U$ be countable measurable spaces with measurable singletons. Let $\mu$ be a measure on $\Omega$ that is zero or a probability measure, and let $X : \Omega \to S$, $Y : \Omega \to T$, $Z : \Omega \to U$ be measurable random variables, each of finite range. Then $H[X \mid (Y,Z);\mu] \le H[X \mid Z;\mu]$.

### `ProbabilityTheory.entropy_triple_add_entropy_le`
Lean (short): `(μ : Measure Ω) [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [Countable S] [Countable T] [IsZeroOrProbabilityMeasure μ] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : H[⟨X, ⟨Y, Z⟩⟩; μ] + H[Z; μ] ≤ H[⟨X, Z⟩; μ] + H[⟨Y, Z⟩; μ]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] {X : Ω → S} {Y : Ω → T} {Z : Ω → U} (μ : Measure Ω) [inst_2 : MeasurableSpace T] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [Countable S] [Countable T] [IsZeroOrProbabilityMeasure μ], Measurable X → Measurable Y → Measurable Z → ∀ [FiniteRange X] [FiniteRange Y] [FiniteRange Z], H[⟨X, ⟨Y, Z⟩⟩; μ] + H[Z; μ] ≤ H[⟨X, Z⟩; μ] + H[⟨Y, Z⟩; μ]`
Docstring: The submodularity inequality: `H[X, Y, Z] + H[Z] ≤ H[X, Z] + H[Y, Z]`.
English: Let $S$, $T$, $U$ be countable measurable spaces with measurable singletons. Let $\mu$ be a measure on $\Omega$ that is zero or a probability measure, and let $X : \Omega \to S$, $Y : \Omega \to T$, $Z : \Omega \to U$ be measurable random variables, each of finite range. Then $H[(X,(Y,Z));\mu] + H[Z;\mu] \le H[(X,Z);\mu] + H[(Y,Z);\mu]$ (submodularity of entropy).

### `ProbabilityTheory.entropy_sub_mutualInfo_eq_condEntropy`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] : H[X; μ] - I[X : Y ; μ] = H[X | Y ; μ]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] {X : Ω → S} {Y : Ω → T} [inst_1 : MeasurableSpace T] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T], Measurable X → Measurable Y → ∀ (μ : Measure Ω) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y], H[X; μ] - I[X : Y ; μ] = H[X | Y ; μ]`
Docstring: `H[X] - I[X : Y] = H[X | Y]`.
English: Let $S$ and $T$ be countable measurable spaces with measurable singletons. Let $\mu$ be a measure on $\Omega$ that is zero or a probability measure, and let $X : \Omega \to S$, $Y : \Omega \to T$ be measurable random variables, both of finite range. Then $H[X;\mu] - I[X : Y;\mu] = H[X \mid Y;\mu]$.

### `ProbabilityTheory.prob_ge_exp_neg_entropy`
Lean (short): `[MeasurableSingletonClass S] [Nonempty S] (X : Ω → S) (μ : Measure Ω) (hX : Measurable X) [FiniteRange X] : ∃ s, μ Set.univ * ↑(Real.exp (-H[X; μ])).toNNReal ≤ (Measure.map X μ) {s}`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [MeasurableSingletonClass S] [Nonempty S] (X : Ω → S) (μ : Measure Ω), Measurable X → ∀ [hX' : FiniteRange X], ∃ s, HMul.hMul (α := ENNReal) (μ Set.univ : ENNReal) ↑(Real.exp (-H[X; μ])).toNNReal ≤ (Measure.map X μ : Measure S) {s}`
Docstring: If `X` is an `S`-valued random variable, then there exists `s ∈ S` such that `P[X = s] ≥ \exp(- H[X])`.
English: Let $S$ be a nonempty space in which singletons are measurable, let $\mu$ be a measure on $\Omega$, and let $X : \Omega \to S$ be a measurable random variable taking finitely many values. Then there exists $s \in S$ such that $\mu(\Omega)\cdot e^{-H[X;\mu]} \le (X_*\mu)(\{s\})$, where $e^{-H[X;\mu]}$ is viewed as a nonnegative real.

### `ProbabilityTheory.mutualInfo_nonneg`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass T] (hX : Measurable X) (hY : Measurable Y) (μ : Measure Ω) [FiniteRange X] [FiniteRange Y] : 0 ≤ I[X : Y ; μ]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] {X : Ω → S} {Y : Ω → T} [inst_1 : MeasurableSpace T] [MeasurableSingletonClass S] [MeasurableSingletonClass T], Measurable X → Measurable Y → ∀ (μ : Measure Ω) [FiniteRange X] [FiniteRange Y], (0 : ℝ) ≤ I[X : Y ; μ]`
Docstring: Mutual information is non-negative.
English: Let $S$ and $T$ be spaces in which singletons are measurable, let $\mu$ be a measure on $\Omega$, and let $X : \Omega \to S$ and $Y : \Omega \to T$ be measurable random variables, each taking finitely many values. Then $0 \le I[X : Y;\mu]$.

### `ProbabilityTheory.condMutualInfo_eq_zero`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] (hX : Measurable X) (hY : Measurable Y) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : I[X : Y|Z;μ] = 0 ↔ CondIndepFun X Y Z μ`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] {X : Ω → S} {Y : Ω → T} {Z : Ω → U} {μ : Measure Ω} [inst_2 : MeasurableSpace T] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U], Measurable X → Measurable Y → ∀ [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] [FiniteRange Z], I[X : Y|Z;μ] = (0 : ℝ) ↔ CondIndepFun X Y Z μ`
Docstring: `I[X : Y| Z]=0` iff `X, Y` are conditionally independent over `Z`.
English: Let $S$, $T$, $U$ be measurable spaces with measurable singletons, with $U$ countable. Let $\mu$ be a measure on $\Omega$ that is zero or a probability measure, let $X : \Omega \to S$ and $Y : \Omega \to T$ be measurable random variables, and let $Z : \Omega \to U$ be a random variable, with $X$, $Y$, $Z$ each of finite range. Then $I[X : Y \mid Z;\mu] = 0$ if and only if $X$ and $Y$ are conditionally independent given $Z$ with respect to $\mu$.

### `ProbabilityTheory.ent_of_cond_indep`
Lean (short): `(μ : Measure Ω) [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [Countable S] [Countable T] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : CondIndepFun X Y Z μ) [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : H[⟨X, ⟨Y, Z⟩⟩; μ] = H[⟨X, Z⟩; μ] + H[⟨Y, Z⟩; μ] - H[Z; μ]`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [inst_1 : MeasurableSpace U] {X : Ω → S} {Y : Ω → T} {Z : Ω → U} (μ : Measure Ω) [inst_2 : MeasurableSpace T] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [Countable S] [Countable T], Measurable X → Measurable Y → Measurable Z → CondIndepFun X Y Z μ → ∀ [IsZeroOrProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] [FiniteRange Z], H[⟨X, ⟨Y, Z⟩⟩; μ] = H[⟨X, Z⟩; μ] + H[⟨Y, Z⟩; μ] - H[Z; μ]`
Docstring: If `X, Y` are conditionally independent over `Z`, then `H[X, Y, Z] = H[X, Z] + H[Y, Z] - H[Z]`.
English: Let $S$, $T$, $U$ be countable measurable spaces with measurable singletons. Let $\mu$ be a measure on $\Omega$ that is zero or a probability measure, and let $X : \Omega \to S$, $Y : \Omega \to T$, $Z : \Omega \to U$ be measurable random variables, each of finite range, such that $X$ and $Y$ are conditionally independent given $Z$ with respect to $\mu$. Then $H[(X,(Y,Z));\mu] = H[(X,Z);\mu] + H[(Y,Z);\mu] - H[Z;\mu]$.
