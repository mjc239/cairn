You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport`
Lean: `(κ : Kernel T S) (μ : Measure T) : Prop`
English: For a kernel $\kappa$ from $T$ to $S$ and a measure $\mu$ on $T$, defines the property that $\kappa$ has almost everywhere finite support with respect to $\mu$: for $\mu$-almost every $t$, the measure $\kappa(t)$ has finite support (with no uniformity in $t$ required).

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport.mk`
Lean: `[Countable T] [MeasurableSingletonClass T] (_hκ : κ.AEFiniteKernelSupport μ) : Kernel T S`
English: Given a proof that $\kappa$ has almost everywhere finite support with respect to $\mu$, defines an associated kernel $\mathrm{mk}$ from $T$ to $S$ (a modification of $\kappa$; the definition does not actually use the hypothesis).

### `ProbabilityTheory.Kernel.FiniteKernelSupport`
Lean: `(κ : Kernel T S) : Prop`
English: For a kernel $\kappa$ from $T$ to $S$, defines the property that $\kappa$ has finite kernel support, the analogue for kernels of a measure having finite support.

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport.finiteKernelSupport_mk`
Lean: `[Countable T] [MeasurableSingletonClass T] [MeasurableSingletonClass S] (hκ : κ.AEFiniteKernelSupport μ) : hκ.mk.FiniteKernelSupport`
English: If $\kappa$ has almost everywhere finite support with respect to $\mu$ (hypothesis $h\kappa$), then the kernel $h\kappa.\mathrm{mk}$ has finite kernel support.

### `ProbabilityTheory.Kernel.disintegration`
Lean: `[Countable S] [DiscreteMeasurableSpace S] [Countable U] [Nonempty U] [DiscreteMeasurableSpace U] (κ : Kernel T (S × U)) [IsFiniteKernel κ] : κ = κ.fst.compProd κ.condKernel`
English: For every kernel $\kappa$ from $T$ to $S\times U$, one has $\kappa=\kappa.\mathrm{fst}\otimes\kappa.\mathrm{condKernel}$, i.e. $\kappa$ equals the composition-product of its first marginal with its conditional kernel.

### `ProbabilityTheory.Kernel.aefiniteKernelSupport_of_cond`
Lean: `[Nonempty U] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [MeasurableSingletonClass U] [Countable U] [Countable S] [Countable T] (μ : Measure T) (hκ : κ.AEFiniteKernelSupport μ) [IsFiniteKernel κ] : κ.condKernel.AEFiniteKernelSupport (μ.compProd κ.fst)`
English: Let $\mu$ be a measure on $T$ and suppose $\kappa$ has almost everywhere finite support with respect to $\mu$. Then $\kappa.\mathrm{condKernel}$ has almost everywhere finite support with respect to $\mu\otimes\kappa.\mathrm{fst}$.

### `ProbabilityTheory.condDistrib_eq_prod_of_indepFun`
Lean: `[Countable S] [DiscreteMeasurableSpace S] [MeasurableSingletonClass T] [Countable U] [DiscreteMeasurableSpace U] [Countable T] [Nonempty T] [Countable V] [MeasurableSingletonClass V] [Nonempty S] (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) [IsProbabilityMeasure μ] (h : IndepFun (fun ω => (X ω, Z ω)) (fun ω => (Y ω, W ω)) μ) : ⇑(condDistrib (fun ω => (X ω, Y ω)) (fun ω => (Z ω, W ω)) μ) =ᵐ[Measure.map (fun ω => (Z ω, W ω)) μ] ⇑((Kernel.prodMkRight V (condDistrib X Z μ)).prod (Kernel.prodMkLeft U (condDistrib Y W μ)))`
English: Let $X,Y,Z,W$ be measurable random variables on $\Omega$, $\mu$ a measure on $\Omega$, and suppose the pairs $(X,Z)$ and $(Y,W)$ are independent under $\mu$. Then, almost everywhere with respect to the law of $(Z,W)$ under $\mu$, the conditional distribution of $(X,Y)$ given $(Z,W)$ equals the product kernel $(\mathrm{prodMkRight}_V\,\mathrm{condDistrib}(X|Z))\times(\mathrm{prodMkLeft}_U\,\mathrm{condDistrib}(Y|W))$, i.e. at $(z,w)$ it is the product of the conditional distribution of $X$ given $Z=z$ and that of $Y$ given $W=w$.

### `ProbabilityTheory.condKernel_condDistrib_ae_eq`
Lean: `[Countable S] [DiscreteMeasurableSpace S] [MeasurableSingletonClass T] [Countable U] [DiscreteMeasurableSpace U] [Countable T] [Nonempty T] [Nonempty S] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (μ : Measure Ω) [IsFiniteMeasure μ] : ⇑(condDistrib (fun a => (X a, Y a)) Z μ).condKernel =ᵐ[Measure.map (fun ω => (Z ω, X ω)) μ] ⇑(condDistrib Y (fun ω => (Z ω, X ω)) μ)`
English: Let $X,Y,Z$ be measurable random variables on $\Omega$ and $\mu$ a measure on $\Omega$. Then, almost everywhere with respect to the law of $(Z,X)$ under $\mu$, the conditional kernel of the conditional distribution of $(X,Y)$ given $Z$ equals the conditional distribution of $Y$ given $(Z,X)$.
