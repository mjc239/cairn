You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring, and when no
docstring, definition body (under "Project definitions") or Lean supports a description of an object, name it
instead of describing it. Give every variable its
type, introduce every symbol, and never use one letter for two things.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `ProbabilityTheory.FiniteSupport` (structure or class)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) FiniteSupport._auto_1 → Prop`
Docstring: A measure has finite support if there exists a finite set whose complement has zero measure.
Fields: `A`, `x`

#### `ProbabilityTheory.Kernel.entropy` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → ℝ`
Docstring: Entropy of a kernel with respect to a measure.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) (μ : Measure T) => ∫ (x : T), (fun (y : T) => measureEntropy.{u_2} (S := S) (κ y)) x ∂μ`

#### `ProbabilityTheory.Kernel.AEFiniteKernelSupport` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → Prop`
Docstring: A kernel `κ` has almost everywhere finite support wrt a measure `μ` if, for almost every point `t`, then `κ t` has finite support. Note that we don't require any uniformity wrt `t`.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) (μ : Measure T) => ∀ᵐ (t : T) ∂μ, ∃ (A : Finset S), (κ t : Measure S) (↑A)ᶜ = (0 : ENNReal)`

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

## Flagged translations

### `ProbabilityTheory.Kernel.entropy_prodMkLeft_unit`
Lean (short): `[MeasurableSingletonClass T] (κ : Kernel T S) [IsZeroOrProbabilityMeasure μ] [FiniteSupport μ] : Hk[Kernel.prodMkLeft Unit κ , Measure.map (Prod.mk ()) μ] = Hk[κ , μ]`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [MeasurableSingletonClass T] (κ : Kernel T S) {μ : Measure T} [IsZeroOrProbabilityMeasure μ] [FiniteSupport μ], Hk[Kernel.prodMkLeft Unit κ , Measure.map (Prod.mk ()) μ] = Hk[κ , μ]`
Previous English: Let $T$ have measurable singletons, let $\kappa$ be a kernel from $T$ to $S$, and let $\mu$ be a measure on $T$ that is zero or a probability measure and has finite support. Let $\kappa'$ be the kernel from $\mathrm{Unit}\times T$ to $S$ given by $\kappa'((), t) = \kappa(t)$ (`Kernel.prodMkLeft Unit κ`), and let $\mu'$ be the image of $\mu$ under $t \mapsto ((), t)$. Then $H_k[\kappa',\mu'] = H_k[\kappa,\mu]$.
Checker's issue: Supplies a formula for Kernel.prodMkLeft (kappa'((),t)=kappa(t)) not shown in the prompt; also S is not introduced as a measurable space.

### `ProbabilityTheory.Kernel.entropy_compProd`
Lean (short): `[Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [MeasurableSingletonClass U] [IsFiniteMeasure μ] [IsZeroOrMarkovKernel κ] [IsMarkovKernel η] [FiniteSupport μ] (hκ : κ.AEFiniteKernelSupport μ) (hη : η.AEFiniteKernelSupport (μ.compProd κ)) : Hk[κ.compProd η , μ] = Hk[κ , μ] + Hk[η , μ.compProd κ]`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [inst_2 : MeasurableSpace U] [Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [MeasurableSingletonClass U] {μ : Measure T} [IsFiniteMeasure μ] {κ : Kernel T S} [IsZeroOrMarkovKernel κ] {η : Kernel (T × S) U} [IsMarkovKernel η] [FiniteSupport μ], κ.AEFiniteKernelSupport μ → η.AEFiniteKernelSupport (μ.compProd κ) → Hk[κ.compProd η , μ] = Hk[κ , μ] + Hk[η , μ.compProd κ]`
Previous English: Let $S$ and $T$ be countable spaces with measurable singletons and let $U$ have measurable singletons. Let $\mu$ be a finite measure on $T$ with finite support, let $\kappa$ be a kernel from $T$ to $S$ that is zero or Markov (each $\kappa(t)$ is zero or a probability measure, uniformly), with almost everywhere finite kernel support with respect to $\mu$, and let $\eta$ be a Markov kernel from $T\times S$ to $U$ with almost everywhere finite kernel support with respect to $\mu \otimes \kappa$ (`μ.compProd κ`). Then $H_k[\kappa \otimes \eta,\ \mu] = H_k[\kappa,\mu] + H_k[\eta,\ \mu\otimes\kappa]$, where $\kappa\otimes\eta$ is the composition-product kernel `κ.compProd η`.
Checker's issue: Gloss of IsZeroOrMarkovKernel as 'each kappa(t) is zero or a probability measure, uniformly' is ambiguous and can be read as the weaker pointwise condition; Lean requires kappa = 0 or kappa Markov.
