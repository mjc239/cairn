You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.Kernel.entropy`
Lean: `(κ : Kernel T S) (μ : Measure T) : ℝ`
English: For a kernel $\kappa$ from $T$ to $S$ and a measure $\mu$ on $T$, $H_k[\kappa,\mu]$ denotes the entropy of the kernel $\kappa$ with respect to the measure $\mu$.

### `ProbabilityTheory.Kernel.entropy_prodMkLeft_unit`
Lean: `[MeasurableSingletonClass T] (κ : Kernel T S) [IsZeroOrProbabilityMeasure μ] [FiniteSupport μ] : Hk[Kernel.prodMkLeft Unit κ , Measure.map (Prod.mk ()) μ] = Hk[κ , μ]`
English: Let $T$ have measurable singletons, let $\kappa$ be a kernel from $T$ to $S$, and let $\mu$ be a measure on $T$ that is zero or a probability measure and has finite support. Let $\kappa'$ be the kernel from $\mathrm{Unit}\times T$ to $S$ given by $\kappa'((), t) = \kappa(t)$ (`Kernel.prodMkLeft Unit κ`), and let $\mu'$ be the image of $\mu$ under $t \mapsto ((), t)$. Then $H_k[\kappa',\mu'] = H_k[\kappa,\mu]$.

### `ProbabilityTheory.Kernel.aefiniteKernelSupport_condDistrib`
Lean: `[Nonempty S] [Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] (X : Ω → S) (Y : Ω → T) (μ : Measure Ω) [IsFiniteMeasure μ] (hX : Measurable X) (hY : Measurable Y) [FiniteRange X] : (condDistrib X Y μ).AEFiniteKernelSupport (Measure.map Y μ)`
English: Let $S$ be a nonempty countable space and $T$ a countable space, both with measurable singletons. Let $\mu$ be a finite measure on $\Omega$, and let $X : \Omega \to S$ and $Y : \Omega \to T$ be measurable random variables, with $X$ having finite range. Then the conditional distribution kernel $\mathrm{condDistrib}(X \mid Y;\mu)$ has almost everywhere finite kernel support with respect to the law $Y_*\mu$ of $Y$.

### `ProbabilityTheory.Kernel.entropy_compProd`
Lean: `[Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [MeasurableSingletonClass U] [IsFiniteMeasure μ] [IsZeroOrMarkovKernel κ] [IsMarkovKernel η] [FiniteSupport μ] (hκ : κ.AEFiniteKernelSupport μ) (hη : η.AEFiniteKernelSupport (μ.compProd κ)) : Hk[κ.compProd η , μ] = Hk[κ , μ] + Hk[η , μ.compProd κ]`
English: Let $S$ and $T$ be countable spaces with measurable singletons and let $U$ have measurable singletons. Let $\mu$ be a finite measure on $T$ with finite support, let $\kappa$ be a kernel from $T$ to $S$ that is zero or Markov (each $\kappa(t)$ is zero or a probability measure, uniformly), with almost everywhere finite kernel support with respect to $\mu$, and let $\eta$ be a Markov kernel from $T\times S$ to $U$ with almost everywhere finite kernel support with respect to $\mu \otimes \kappa$ (`μ.compProd κ`). Then $H_k[\kappa \otimes \eta,\ \mu] = H_k[\kappa,\mu] + H_k[\eta,\ \mu\otimes\kappa]$, where $\kappa\otimes\eta$ is the composition-product kernel `κ.compProd η`.

### `ProbabilityTheory.Kernel.chain_rule`
Lean: `[Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [IsZeroOrMarkovKernel κ] [Nonempty U] [IsZeroOrProbabilityMeasure μ] [FiniteSupport μ] (hκ : κ.AEFiniteKernelSupport μ) : Hk[κ , μ] = Hk[κ.fst , μ] + Hk[κ.condKernel , μ.compProd κ.fst]`
English: Let $S$, $T$, $U$ be countable spaces with measurable singletons, with $U$ nonempty. Let $\mu$ be a measure on $T$ that is zero or a probability measure and has finite support, and let $\kappa$ be a kernel from $T$ to $S\times U$ that is zero or Markov and has almost everywhere finite kernel support with respect to $\mu$. Then $H_k[\kappa,\mu] = H_k[\kappa.\mathrm{fst},\mu] + H_k[\kappa.\mathrm{condKernel},\ \mu\otimes\kappa.\mathrm{fst}]$, where $\kappa.\mathrm{fst}$ is the first marginal of $\kappa$ and $\kappa.\mathrm{condKernel}$ its conditional kernel.
