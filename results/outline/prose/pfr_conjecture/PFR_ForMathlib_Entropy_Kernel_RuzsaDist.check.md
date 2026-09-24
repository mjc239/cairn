You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.Kernel.rdistm`
Lean: `(μ : Measure G) (ν : Measure G) : ℝ`
English: For two measures $\mu,\nu$ on an abelian group $G$, the Ruzsa distance $\mathrm{rdistm}(\mu,\nu)$ is the real number $H[X-Y]-H[X]/2-H[Y]/2$, where $X$ and $Y$ are independent random variables distributed according to $\mu$ and $\nu$ respectively.

### `ProbabilityTheory.Kernel.rdist`
Lean: `(κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') : ℝ`
English: For kernels $\kappa$ from $T$ to $G$ and $\eta$ from $T'$ to $G$ (with values in the same group $G$) and measures $\mu$ on $T$ and $\nu$ on $T'$, the kernel Ruzsa distance $d_k[\kappa;\mu \,\#\, \eta;\nu]$ is the average of the Ruzsa distances $\mathrm{rdistm}(\kappa(t),\eta(t'))$ between the image measures, averaged over $(t,t')$ with respect to $\mu\times\nu$.

### `ProbabilityTheory.Kernel.rdist_symm`
Lean: `[Countable T] [MeasurableSingletonClass T] [Countable T'] [MeasurableSingletonClass T'] [MeasurableSingletonClass G] [Countable G] [IsFiniteKernel κ] [IsFiniteKernel η] [IsProbabilityMeasure μ] [IsProbabilityMeasure ν] [FiniteSupport μ] [FiniteSupport ν] : dk[κ ; μ # η ; ν] = dk[η ; ν # κ ; μ]`
English: Let $T$, $T'$ and $G$ be countable with measurable singletons ($G$ an abelian group). Let $\kappa$ be a finite kernel from $T$ to $G$ and $\eta$ a finite kernel from $T'$ to $G$, and let $\mu$ on $T$ and $\nu$ on $T'$ be probability measures with finite support. Then the kernel Ruzsa distance is symmetric: $d_k[\kappa;\mu \,\#\, \eta;\nu] = d_k[\eta;\nu \,\#\, \kappa;\mu]$.
