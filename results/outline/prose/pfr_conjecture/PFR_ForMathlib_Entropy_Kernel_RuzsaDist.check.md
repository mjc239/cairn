You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption) and the English. Compare the English with the full statement.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Definitions are held to the same standard: the English must name the setting the signature assumes
("for an abelian group $G$ and …, $\mathrm{rdist}$ is …"). Replacing an assumption by a stronger one (a metric
space where the Lean has a pseudometric space) is unfaithful too. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.Kernel.rdistm`
Lean (short): `(μ : Measure G) (ν : Measure G) : ℝ`
Lean (full): `{G : Type u_4} → [inst : MeasurableSpace G] → [AddCommGroup G] → Measure G → Measure G → ℝ`
English: For two measures $\mu,\nu$ on an abelian group $G$, the Ruzsa distance $\mathrm{rdistm}(\mu,\nu)$ is the real number $H[X-Y]-H[X]/2-H[Y]/2$, where $X$ and $Y$ are independent random variables distributed according to $\mu$ and $\nu$ respectively.

### `ProbabilityTheory.Kernel.rdist`
Lean (short): `(κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') : ℝ`
Lean (full): `{T : Type u_1} → {T' : Type u_2} → {G : Type u_4} → [inst : MeasurableSpace T] → [inst_1 : MeasurableSpace T'] → [inst_2 : MeasurableSpace G] → [AddCommGroup G] → Kernel T G → Kernel T' G → Measure T → Measure T' → ℝ`
English: Definition. Let $T$, $T'$ be measurable spaces and let $G$ be an abelian group equipped with a measurable space structure. For kernels $\kappa$ from $T$ to $G$ and $\eta$ from $T'$ to $G$ (with values in the same abelian group $G$) and measures $\mu$ on $T$ and $\nu$ on $T'$, the kernel Ruzsa distance $d_k[\kappa;\mu \,\#\, \eta;\nu]$ is a real number. According to its docstring, it is the average of the Ruzsa distances between the image measures $\kappa(t)$ and $\eta(t')$, averaged over $(t,t')$ with respect to $\mu\times\nu$.

### `ProbabilityTheory.Kernel.rdist_symm`
Lean (short): `[Countable T] [MeasurableSingletonClass T] [Countable T'] [MeasurableSingletonClass T'] [MeasurableSingletonClass G] [Countable G] [IsFiniteKernel κ] [IsFiniteKernel η] [IsProbabilityMeasure μ] [IsProbabilityMeasure ν] [FiniteSupport μ] [FiniteSupport ν] : dk[κ ; μ # η ; ν] = dk[η ; ν # κ ; μ]`
Lean (full): `∀ {T : Type u_1} {T' : Type u_2} {G : Type u_4} [inst : MeasurableSpace T] [inst_1 : MeasurableSpace T'] [inst_2 : MeasurableSpace G] [inst_3 : AddCommGroup G] [Countable T] [MeasurableSingletonClass T] [Countable T'] [MeasurableSingletonClass T'] [MeasurableSingletonClass G] [Countable G] {κ : Kernel T G} {η : Kernel T' G} [IsFiniteKernel κ] [IsFiniteKernel η] {μ : Measure T} {ν : Measure T'} [IsProbabilityMeasure μ] [IsProbabilityMeasure ν] [FiniteSupport μ] [FiniteSupport ν], dk[κ ; μ # η ; ν] = dk[η ; ν # κ ; μ]`
English: Let $T$, $T'$ and $G$ be countable with measurable singletons ($G$ an abelian group). Let $\kappa$ be a finite kernel from $T$ to $G$ and $\eta$ a finite kernel from $T'$ to $G$, and let $\mu$ on $T$ and $\nu$ on $T'$ be probability measures with finite support. Then the kernel Ruzsa distance is symmetric: $d_k[\kappa;\mu \,\#\, \eta;\nu] = d_k[\eta;\nu \,\#\, \kappa;\mu]$.
