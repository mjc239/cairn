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

### `ProbabilityTheory.Kernel.disintegration`
Lean: `[Countable S] [DiscreteMeasurableSpace S] [Countable U] [Nonempty U] [DiscreteMeasurableSpace U] (κ : Kernel T (S × U)) [IsFiniteKernel κ] : κ = κ.fst.compProd κ.condKernel`
Previous English: For every kernel $\kappa$ from $T$ to $S\times U$, one has $\kappa=\kappa.\mathrm{fst}\otimes\kappa.\mathrm{condKernel}$, i.e. $\kappa$ equals the composition-product of its first marginal with its conditional kernel.
Checker's issue: Drops the hypothesis [IsFiniteKernel κ]; English claims it for every kernel.

### `ProbabilityTheory.Kernel.aefiniteKernelSupport_of_cond`
Lean: `[Nonempty U] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [MeasurableSingletonClass U] [Countable U] [Countable S] [Countable T] (μ : Measure T) (hκ : κ.AEFiniteKernelSupport μ) [IsFiniteKernel κ] : κ.condKernel.AEFiniteKernelSupport (μ.compProd κ.fst)`
Docstring: Conditioning a kernel preserves finite kernel support.
Previous English: Let $\mu$ be a measure on $T$ and suppose $\kappa$ has almost everywhere finite support with respect to $\mu$. Then $\kappa.\mathrm{condKernel}$ has almost everywhere finite support with respect to $\mu\otimes\kappa.\mathrm{fst}$.
Checker's issue: Drops the hypothesis [IsFiniteKernel κ].

### `ProbabilityTheory.condDistrib_eq_prod_of_indepFun`
Lean: `[Countable S] [DiscreteMeasurableSpace S] [MeasurableSingletonClass T] [Countable U] [DiscreteMeasurableSpace U] [Countable T] [Nonempty T] [Countable V] [MeasurableSingletonClass V] [Nonempty S] (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) [IsProbabilityMeasure μ] (h : IndepFun (fun ω => (X ω, Z ω)) (fun ω => (Y ω, W ω)) μ) : ⇑(condDistrib (fun ω => (X ω, Y ω)) (fun ω => (Z ω, W ω)) μ) =ᵐ[Measure.map (fun ω => (Z ω, W ω)) μ] ⇑((Kernel.prodMkRight V (condDistrib X Z μ)).prod (Kernel.prodMkLeft U (condDistrib Y W μ)))`
Previous English: Let $X,Y,Z,W$ be measurable random variables on $\Omega$, $\mu$ a measure on $\Omega$, and suppose the pairs $(X,Z)$ and $(Y,W)$ are independent under $\mu$. Then, almost everywhere with respect to the law of $(Z,W)$ under $\mu$, the conditional distribution of $(X,Y)$ given $(Z,W)$ equals the product kernel $(\mathrm{prodMkRight}_V\,\mathrm{condDistrib}(X|Z))\times(\mathrm{prodMkLeft}_U\,\mathrm{condDistrib}(Y|W))$, i.e. at $(z,w)$ it is the product of the conditional distribution of $X$ given $Z=z$ and that of $Y$ given $W=w$.
Checker's issue: Drops the hypothesis [IsProbabilityMeasure μ]; English says only 'a measure'.

### `ProbabilityTheory.condKernel_condDistrib_ae_eq`
Lean: `[Countable S] [DiscreteMeasurableSpace S] [MeasurableSingletonClass T] [Countable U] [DiscreteMeasurableSpace U] [Countable T] [Nonempty T] [Nonempty S] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) [IsFiniteMeasure μ] : ⇑(condDistrib (fun a => (X a, Y a)) Z μ).condKernel =ᵐ[Measure.map (fun ω => (Z ω, X ω)) μ] ⇑(condDistrib Y (fun ω => (Z ω, X ω)) μ)`
Previous English: Let $X,Y,Z$ be measurable random variables on $\Omega$ and $\mu$ a measure on $\Omega$. Then, almost everywhere with respect to the law of $(Z,X)$ under $\mu$, the conditional kernel of the conditional distribution of $(X,Y)$ given $Z$ equals the conditional distribution of $Y$ given $(Z,X)$.
Checker's issue: Drops the hypothesis [IsFiniteMeasure μ]; English says only 'a measure'.
