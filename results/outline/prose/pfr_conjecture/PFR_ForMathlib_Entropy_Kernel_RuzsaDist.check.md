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

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

#### `ProbabilityTheory.FiniteSupport` (structure or class)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) FiniteSupport._auto_1 → Prop`
Docstring: A measure has finite support if there exists a finite set whose complement has zero measure.
Fields: `A`, `x`

## Translations

### `ProbabilityTheory.Kernel.rdistm`
Lean (short): `(μ : Measure G) (ν : Measure G) : ℝ`
Lean (full): `{G : Type u_4} → [inst : MeasurableSpace G] → [AddCommGroup G] → Measure G → Measure G → ℝ`
Docstring: The Rusza distance between two measures, defined as `H[X - Y] - H[X]/2 - H[Y]/2` where `X` and `Y` are independent variables distributed according to the two measures.
English: Let $G$ be an abelian group equipped with a measurable space structure. For two measures $\mu,\nu$ on $G$, this defines a real number $\mathrm{rdistm}(\mu,\nu)$. According to its docstring, it is the Ruzsa distance between the two measures, defined as $H[X-Y]-H[X]/2-H[Y]/2$ where $X$ and $Y$ are independent variables distributed according to $\mu$ and $\nu$.

### `ProbabilityTheory.Kernel.rdist`
Lean (short): `(κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') : ℝ`
Lean (full): `{T : Type u_1} → {T' : Type u_2} → {G : Type u_4} → [inst : MeasurableSpace T] → [inst_1 : MeasurableSpace T'] → [inst_2 : MeasurableSpace G] → [AddCommGroup G] → Kernel T G → Kernel T' G → Measure T → Measure T' → ℝ`
Docstring: The Rusza distance between two kernels taking values in the same space, defined as the average Rusza distance between the image measures.
English: Definition. Let $T$ and $T'$ be measurable spaces and let $G$ be an additive commutative group equipped with a measurable space structure. For a kernel $\kappa$ from $T$ to $G$, a kernel $\eta$ from $T'$ to $G$, a measure $\mu$ on $T$ and a measure $\nu$ on $T'$, the kernel Ruzsa distance $d_k[\kappa;\mu \,\#\, \eta;\nu]$ is a real number. According to its docstring, it is the average Ruzsa distance between the image measures.

### `ProbabilityTheory.Kernel.rdist_symm`
Lean (short): `[Countable T] [MeasurableSingletonClass T] [Countable T'] [MeasurableSingletonClass T'] [MeasurableSingletonClass G] [Countable G] [IsFiniteKernel κ] [IsFiniteKernel η] [IsProbabilityMeasure μ] [IsProbabilityMeasure ν] [FiniteSupport μ] [FiniteSupport ν] : dk[κ ; μ # η ; ν] = dk[η ; ν # κ ; μ]`
Lean (full): `∀ {T : Type u_1} {T' : Type u_2} {G : Type u_4} [inst : MeasurableSpace T] [inst_1 : MeasurableSpace T'] [inst_2 : MeasurableSpace G] [inst_3 : AddCommGroup G] [Countable T] [MeasurableSingletonClass T] [Countable T'] [MeasurableSingletonClass T'] [MeasurableSingletonClass G] [Countable G] {κ : Kernel T G} {η : Kernel T' G} [IsFiniteKernel κ] [IsFiniteKernel η] {μ : Measure T} {ν : Measure T'} [IsProbabilityMeasure μ] [IsProbabilityMeasure ν] [FiniteSupport μ] [FiniteSupport ν], dk[κ ; μ # η ; ν] = dk[η ; ν # κ ; μ]`
English: Let $T$, $T'$ and $G$ be countable with measurable singletons ($G$ an abelian group). Let $\kappa$ be a finite kernel from $T$ to $G$ and $\eta$ a finite kernel from $T'$ to $G$, and let $\mu$ on $T$ and $\nu$ on $T'$ be probability measures with finite support. Then the kernel Ruzsa distance is symmetric: $d_k[\kappa;\mu \,\#\, \eta;\nu] = d_k[\eta;\nu \,\#\, \kappa;\mu]$.
