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
Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

## Translations

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport`
Lean (short): `(κ : Kernel T S) (μ : Measure T) : Prop`
Lean (full): `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → Prop`
Docstring: A kernel `κ` has almost everywhere finite support wrt a measure `μ` if, for almost every point `t`, then `κ t` has finite support. Note that we don't require any uniformity wrt `t`.
English: Let $S$ and $T$ be measurable spaces. For a kernel $\kappa$ from $T$ to $S$ and a measure $\mu$ on $T$, this defines a proposition, ``$\kappa$ has almost everywhere finite kernel support with respect to $\mu$''. According to the docstring, this means that for $\mu$-almost every point $t$, the measure $\kappa(t)$ has finite support, with no uniformity in $t$ required.

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport.mk`
Lean (short): `[Countable T] [MeasurableSingletonClass T] (_hκ : κ.AEFiniteKernelSupport μ) : Kernel T S`
Lean (full): `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → [Countable T] → [MeasurableSingletonClass T] → {μ : Measure T} → {κ : Kernel T S} → κ.AEFiniteKernelSupport μ → Kernel T S`
Docstring: The definition doesn't use `_hκ`, but we keep it here still as it doesn't give anything interesting otherwise.
English: Let $S$ and $T$ be measurable spaces, with $T$ countable and with measurable singletons. Given a measure $\mu$ on $T$, a kernel $\kappa$ from $T$ to $S$, and a proof $h\kappa$ that $\kappa$ has almost everywhere finite kernel support with respect to $\mu$, this defines a kernel $h\kappa.\mathrm{mk}$ from $T$ to $S$. According to the docstring, the definition does not use the hypothesis $h\kappa$, which is kept only because the construction is otherwise uninteresting.

### `ProbabilityTheory.Kernel.FiniteKernelSupport`
Lean (short): `(κ : Kernel T S) : Prop`
Lean (full): `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Prop`
Docstring: The analogue of FiniteSupport for probability kernels.
English: Let $S$ and $T$ be measurable spaces. For a kernel $\kappa$ from $T$ to $S$, this defines a proposition, ``$\kappa$ has finite kernel support''. According to the docstring, it is the analogue of finite support (`FiniteSupport`) for probability kernels.

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport.finiteKernelSupport_mk`
Lean (short): `[Countable T] [MeasurableSingletonClass T] [MeasurableSingletonClass S] (hκ : κ.AEFiniteKernelSupport μ) : hκ.mk.FiniteKernelSupport`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [inst_2 : Countable T] [inst_3 : MeasurableSingletonClass T] {μ : Measure T} [MeasurableSingletonClass S] {κ : Kernel T S} (hκ : κ.AEFiniteKernelSupport μ), hκ.mk.FiniteKernelSupport`
English: Let $T$ be a countable measurable space in which singletons are measurable, let $S$ be a measurable space in which singletons are measurable, let $\mu$ be a measure on $T$, and let $\kappa$ be a kernel from $T$ to $S$. Suppose $\kappa$ has almost everywhere finite support with respect to $\mu$ (hypothesis $h\kappa$): for $\mu$-almost every $t\in T$ there is a finite set $A\subseteq S$ with $\kappa(t)(S\setminus A)=0$. Define the kernel $\kappa'=h\kappa.\mathrm{mk}$ from $T$ to $S$ as follows: if $S$ is nonempty, fix a point $s_0\in S$ and let $\kappa'(t)=\kappa(t)$ for those $t$ for which some finite $A\subseteq S$ has $\kappa(t)(S\setminus A)=0$, and $\kappa'(t)=\delta_{s_0}$ (the Dirac measure) otherwise; if $S$ is empty, $\kappa'=0$. Then $\kappa'$ has finite kernel support: for every $t\in T$ there is a finite set $A\subseteq S$ with $\kappa'(t)(S\setminus A)=0$.

### `ProbabilityTheory.Kernel.disintegration`
Lean (short): `[Countable S] [DiscreteMeasurableSpace S] [Countable U] [Nonempty U] [DiscreteMeasurableSpace U] (κ : Kernel T (S × U)) [IsFiniteKernel κ] : κ = κ.fst.compProd κ.condKernel`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} {U : Type u_4} [inst : Countable S] [inst_1 : MeasurableSpace S] [inst_2 : DiscreteMeasurableSpace S] [inst_3 : MeasurableSpace T] [inst_4 : MeasurableSpace U] [inst_5 : Countable U] [inst_6 : Nonempty U] [inst_7 : DiscreteMeasurableSpace U] (κ : Kernel T (S × U)) [inst_8 : IsFiniteKernel κ], κ = κ.fst.compProd κ.condKernel`
English: Let $S$ be a countable measurable space with the discrete $\sigma$-algebra (every subset measurable), let $T$ be a measurable space, and let $U$ be a nonempty countable measurable space with the discrete $\sigma$-algebra. Let $\kappa$ be a finite kernel from $T$ to $S\times U$. Let $\kappa_{\mathrm{fst}}$ be the kernel from $T$ to $S$ given by the first marginal of $\kappa$ (the pushforward of $\kappa(t)$ under the projection $S\times U\to S$), and let $\kappa_{\mathrm{cond}}$ be the conditional kernel of $\kappa$ (Mathlib's $\kappa.\mathrm{condKernel}$), a kernel from $T\times S$ to $U$. Then $\kappa=\kappa_{\mathrm{fst}}\otimes_k\kappa_{\mathrm{cond}}$, where $\otimes_k$ denotes the composition-product of kernels.

### `ProbabilityTheory.Kernel.aefiniteKernelSupport_of_cond`
Lean (short): `[Nonempty U] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [MeasurableSingletonClass U] [Countable U] [Countable S] [Countable T] (μ : Measure T) (hκ : κ.AEFiniteKernelSupport μ) [IsFiniteKernel κ] : κ.condKernel.AEFiniteKernelSupport (μ.compProd κ.fst)`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [inst_2 : MeasurableSpace U] {κ : Kernel T (S × U)} [hU : Nonempty U] [inst_3 : MeasurableSingletonClass S] [MeasurableSingletonClass T] [inst_5 : MeasurableSingletonClass U] [inst_6 : Countable U] [inst_7 : Countable S] [Countable T] (μ : Measure T), κ.AEFiniteKernelSupport μ → ∀ [inst_9 : IsFiniteKernel κ], κ.condKernel.AEFiniteKernelSupport (μ.compProd κ.fst)`
Docstring: Conditioning a kernel preserves finite kernel support.
English: Let $S$, $T$, $U$ be countable measurable spaces with measurable singletons, with $U$ nonempty. Let $\mu$ be a measure on $T$ and let $\kappa$ be a finite kernel from $T$ to $S \times U$ that has almost everywhere finite support with respect to $\mu$. Then $\kappa.\mathrm{condKernel}$ has almost everywhere finite support with respect to $\mu\otimes\kappa.\mathrm{fst}$.

### `ProbabilityTheory.condDistrib_eq_prod_of_indepFun`
Lean (short): `[Countable S] [DiscreteMeasurableSpace S] [MeasurableSingletonClass T] [Countable U] [DiscreteMeasurableSpace U] [Countable T] [Nonempty T] [Countable V] [MeasurableSingletonClass V] [Nonempty S] (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) [IsProbabilityMeasure μ] (h : IndepFun (fun ω => (X ω, Z ω)) (fun ω => (Y ω, W ω)) μ) : ⇑(condDistrib (fun ω => (X ω, Y ω)) (fun ω => (Z ω, W ω)) μ) =ᵐ[Measure.map (fun ω => (Z ω, W ω)) μ] ⇑((Kernel.prodMkRight V (condDistrib X Z μ)).prod (Kernel.prodMkLeft U (condDistrib Y W μ)))`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [mΩ : MeasurableSpace Ω] [inst : Countable S] [inst_1 : MeasurableSpace S] [inst_2 : DiscreteMeasurableSpace S] [inst_3 : MeasurableSpace T] [inst_4 : MeasurableSpace U] [inst_5 : MeasurableSingletonClass T] [Countable U] [DiscreteMeasurableSpace U] {X : Ω → S} {Y : Ω → T} {Z : Ω → U} [inst_8 : Countable T] [inst_9 : Nonempty T] {V : Type u_5} [Countable V] [inst_11 : MeasurableSpace V] [MeasurableSingletonClass V] {W : Ω → V} [inst_13 : Nonempty S], Measurable X → Measurable Z → Measurable Y → Measurable W → ∀ (μ : Measure Ω) [inst_14 : IsProbabilityMeasure μ], IndepFun (β := S × U) (γ := T × V) (fun (ω : Ω) => (X ω, Z ω)) (fun (ω : Ω) => (Y ω, W ω)) μ → ⇑(condDistrib (fun (ω : Ω) => (X ω, Y ω)) (fun (ω : Ω) => (Z ω, W ω)) μ) =ᵐ[Measure.map (fun (ω : Ω) => (Z ω, W ω)) μ] ⇑(Kernel.prod (Kernel.prodMkRight V (condDistrib X Z μ)) (Kernel.prodMkLeft U (condDistrib Y W μ)))`
English: Let $S$ and $U$ be countable measurable spaces in which every set is measurable, with $S$ nonempty; let $T$ be a nonempty countable measurable space with measurable singletons, and $V$ a countable measurable space with measurable singletons. Let $X : \Omega\to S$, $Y : \Omega \to T$, $Z : \Omega \to U$, $W : \Omega \to V$ be measurable random variables, $\mu$ a probability measure on $\Omega$, and suppose the pairs $(X,Z)$ and $(Y,W)$ are independent under $\mu$. Then, almost everywhere with respect to the law of $(Z,W)$ under $\mu$, the conditional distribution of $(X,Y)$ given $(Z,W)$ equals the product kernel $(\mathrm{prodMkRight}_V\,\mathrm{condDistrib}(X|Z;\mu))\times(\mathrm{prodMkLeft}_U\,\mathrm{condDistrib}(Y|W;\mu))$, i.e. at $(z,w)$ it is the product of the conditional distribution of $X$ given $Z=z$ and that of $Y$ given $W=w$.

### `ProbabilityTheory.condKernel_condDistrib_ae_eq`
Lean (short): `[Countable S] [DiscreteMeasurableSpace S] [MeasurableSingletonClass T] [Countable U] [DiscreteMeasurableSpace U] [Countable T] [Nonempty T] [Nonempty S] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) [IsFiniteMeasure μ] : ⇑(condDistrib (fun a => (X a, Y a)) Z μ).condKernel =ᵐ[Measure.map (fun ω => (Z ω, X ω)) μ] ⇑(condDistrib Y (fun ω => (Z ω, X ω)) μ)`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [mΩ : MeasurableSpace Ω] [inst : Countable S] [inst_1 : MeasurableSpace S] [inst_2 : DiscreteMeasurableSpace S] [inst_3 : MeasurableSpace T] [inst_4 : MeasurableSpace U] [inst_5 : MeasurableSingletonClass T] [Countable U] [DiscreteMeasurableSpace U] {X : Ω → S} {Y : Ω → T} {Z : Ω → U} [inst_8 : Countable T] [inst_9 : Nonempty T] [inst_10 : Nonempty S], Measurable X → Measurable Y → Measurable Z → ∀ (μ : Measure Ω) [inst_11 : IsFiniteMeasure μ], ⇑(Kernel.condKernel (condDistrib (fun (a : Ω) => (X a, Y a)) Z μ)) =ᵐ[Measure.map (fun (ω : Ω) => (Z ω, X ω)) μ] ⇑(condDistrib Y (fun (ω : Ω) => (Z ω, X ω)) μ)`
English: Let $S$ and $U$ be countable measurable spaces in which every set is measurable, with $S$ nonempty, and let $T$ be a nonempty countable measurable space with measurable singletons. Let $X : \Omega \to S$, $Y : \Omega \to T$, $Z : \Omega \to U$ be measurable random variables and $\mu$ a finite measure on $\Omega$. Then, almost everywhere with respect to the law of $(Z,X)$ under $\mu$, the conditional kernel of the conditional distribution of $(X,Y)$ given $Z$ equals the conditional distribution of $Y$ given $(Z,X)$.
