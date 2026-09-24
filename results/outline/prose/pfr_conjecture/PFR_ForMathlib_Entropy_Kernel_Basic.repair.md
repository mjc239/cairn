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

### `ProbabilityTheory.Kernel.entropy_prodMkLeft_unit`
Lean: `[MeasurableSingletonClass T] (κ : Kernel T S) [IsZeroOrProbabilityMeasure μ] [FiniteSupport μ] : Hk[Kernel.prodMkLeft Unit κ , Measure.map (Prod.mk ()) μ] = Hk[κ , μ]`
Previous English: Let $\kappa$ be a kernel from $T$ to $S$ and $\mu$ a measure on $T$. Let $\kappa'$ be the kernel from $\mathrm{Unit}\times T$ to $S$ given by $\kappa'(( ), t) = \kappa(t)$ (`Kernel.prodMkLeft Unit κ`), and let $\mu'$ be the image of $\mu$ under $t \mapsto ((), t)$. Then $H_k[\kappa',\mu'] = H_k[\kappa,\mu]$.
Checker's issue: Drops the hypotheses [IsZeroOrProbabilityMeasure μ] and [FiniteSupport μ].

### `ProbabilityTheory.Kernel.aefiniteKernelSupport_condDistrib`
Lean: `[Nonempty S] [Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] (X : Ω → S) (Y : Ω → T) (μ : Measure Ω) [IsFiniteMeasure μ] (hX : Measurable X) (hY : Measurable Y) [FiniteRange X] : (condDistrib X Y μ).AEFiniteKernelSupport (Measure.map Y μ)`
Previous English: Let $X : \Omega \to S$ and $Y : \Omega \to T$ be measurable random variables and $\mu$ a measure on $\Omega$. Then the conditional distribution kernel $\mathrm{condDistrib}(X \mid Y;\mu)$ has almost everywhere finite kernel support with respect to the law $Y_*\mu$ of $Y$.
Checker's issue: Drops the hypotheses [IsFiniteMeasure μ] and [FiniteRange X].

### `ProbabilityTheory.Kernel.entropy_compProd`
Lean: `[Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [MeasurableSingletonClass U] [IsFiniteMeasure μ] [IsZeroOrMarkovKernel κ] [IsMarkovKernel η] [FiniteSupport μ] (hκ : κ.AEFiniteKernelSupport μ) (hη : η.AEFiniteKernelSupport (μ.compProd κ)) : Hk[κ.compProd η , μ] = Hk[κ , μ] + Hk[η , μ.compProd κ]`
Previous English: Let $\kappa$ be a kernel with almost everywhere finite kernel support with respect to $\mu$, and $\eta$ a kernel with almost everywhere finite kernel support with respect to $\mu \otimes \kappa$ (`μ.compProd κ`). Then $H_k[\kappa \otimes \eta,\ \mu] = H_k[\kappa,\mu] + H_k[\eta,\ \mu\otimes\kappa]$, where $\kappa\otimes\eta$ is the composition-product kernel `κ.compProd η`.
Checker's issue: Drops the hypotheses [IsFiniteMeasure μ], [FiniteSupport μ], [IsZeroOrMarkovKernel κ] and [IsMarkovKernel η].

### `ProbabilityTheory.Kernel.chain_rule`
Lean: `[Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [IsZeroOrMarkovKernel κ] [Nonempty U] [IsZeroOrProbabilityMeasure μ] [FiniteSupport μ] (hκ : κ.AEFiniteKernelSupport μ) : Hk[κ , μ] = Hk[κ.fst , μ] + Hk[κ.condKernel , μ.compProd κ.fst]`
Previous English: Let $\kappa$ be a kernel into a product space $S\times U$ that has almost everywhere finite kernel support with respect to $\mu$. Then $H_k[\kappa,\mu] = H_k[\kappa.\mathrm{fst},\mu] + H_k[\kappa.\mathrm{condKernel},\ \mu\otimes\kappa.\mathrm{fst}]$, where $\kappa.\mathrm{fst}$ is the first marginal of $\kappa$ and $\kappa.\mathrm{condKernel}$ its conditional kernel.
Checker's issue: Drops the hypotheses [IsZeroOrMarkovKernel κ], [IsZeroOrProbabilityMeasure μ] and [FiniteSupport μ].
