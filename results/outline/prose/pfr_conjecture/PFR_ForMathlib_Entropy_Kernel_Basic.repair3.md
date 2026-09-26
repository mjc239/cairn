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
type, introduce every symbol, and never use one letter for two things. When a definition's body is shown, say what
it defines, in words or a formula that agrees with the body.

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
Previous English: Let $S$ be a measurable space and $T$ a measurable space in which every singleton is measurable. Let $\kappa$ be a kernel from $T$ to $S$, and let $\mu$ be a measure on $T$ that is either zero or a probability measure and that has finite support (there is a finite set whose complement has $\mu$-measure zero). Let $\kappa'$ be the kernel `Kernel.prodMkLeft Unit κ` from $\mathrm{Unit}\times T$ to $S$ (Mathlib's construction that turns $\kappa$ into a kernel with an extra, ignored, first argument in the one-point type $\mathrm{Unit}$), and let $\mu'$ be the pushforward of $\mu$ under $t\mapsto((),t)$, a measure on $\mathrm{Unit}\times T$. Then $H_k[\kappa',\mu']=H_k[\kappa,\mu]$, where for a kernel $\eta$ from $W$ to $S$ and a measure $\nu$ on $W$, $H_k[\eta,\nu]=\int H(\eta(w))\,d\nu(w)$ and $H(m)=\sum_{s\in S}-m'(\{s\})\log m'(\{s\})$ with $m'=m(S)^{-1}m$ the normalized measure.
Checker's issue: The English gives an explicit formula for the kernel entropy H_k (H_k[eta,nu] = integral of H(eta(w)) d nu(w), with H the normalized-measure entropy), but the prompt provides no definition body/docstring for ProbabilityTheory.Kernel.entropy supporting this formula (its only docstring is 'Entropy of a kernel with respect to a measure'); the description cannot be verified against the project definitions.

### `ProbabilityTheory.Kernel.entropy_compProd`
Lean (short): `[Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [MeasurableSingletonClass U] [IsFiniteMeasure μ] [IsZeroOrMarkovKernel κ] [IsMarkovKernel η] [FiniteSupport μ] (hκ : κ.AEFiniteKernelSupport μ) (hη : η.AEFiniteKernelSupport (μ.compProd κ)) : Hk[κ.compProd η , μ] = Hk[κ , μ] + Hk[η , μ.compProd κ]`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [inst_2 : MeasurableSpace U] [Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [MeasurableSingletonClass U] {μ : Measure T} [IsFiniteMeasure μ] {κ : Kernel T S} [IsZeroOrMarkovKernel κ] {η : Kernel (T × S) U} [IsMarkovKernel η] [FiniteSupport μ], κ.AEFiniteKernelSupport μ → η.AEFiniteKernelSupport (μ.compProd κ) → Hk[κ.compProd η , μ] = Hk[κ , μ] + Hk[η , μ.compProd κ]`
Previous English: Let $S$ and $T$ be countable measurable spaces in which every singleton is measurable, and let $U$ be a measurable space in which every singleton is measurable. Let $\mu$ be a finite measure on $T$ that has finite support (there is a finite set whose complement has $\mu$-measure zero). Let $\kappa$ be a kernel from $T$ to $S$ such that either $\kappa$ is the zero kernel or $\kappa$ is a Markov kernel, and such that $\kappa$ has almost everywhere finite kernel support with respect to $\mu$ (for $\mu$-almost every $t\in T$ there is a finite set $A\subseteq S$ with $\kappa(t)(S\setminus A)=0$). Let $\eta$ be a Markov kernel from $T\times S$ to $U$ with almost everywhere finite kernel support (in the same sense) with respect to the measure $\mu\otimes\kappa$ on $T\times S$ (the composition-product `μ.compProd κ`). Then $$H_k[\kappa\otimes\eta,\ \mu]=H_k[\kappa,\mu]+H_k[\eta,\ \mu\otimes\kappa],$$ where $\kappa\otimes\eta$ is the composition-product kernel `κ.compProd η` from $T$ to $S\times U$, and for a kernel $\rho$ from $W$ to $V$ and a measure $\nu$ on $W$, $H_k[\rho,\nu]=\int H(\rho(w))\,d\nu(w)$ with $H(m)=\sum_{v\in V}-m'(\{v\})\log m'(\{v\})$ for $m'=m(V)^{-1}m$ the normalized measure.
Checker's issue: The English gives an explicit formula for the kernel entropy H_k (H_k[eta,nu] = integral of H(eta(w)) d nu(w), with H the normalized-measure entropy), but the prompt provides no definition body/docstring for ProbabilityTheory.Kernel.entropy supporting this formula (its only docstring is 'Entropy of a kernel with respect to a measure'); the description cannot be verified against the project definitions.

### `ProbabilityTheory.Kernel.chain_rule`
Lean (short): `[Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [IsZeroOrMarkovKernel κ] [Nonempty U] [IsZeroOrProbabilityMeasure μ] [FiniteSupport μ] (hκ : κ.AEFiniteKernelSupport μ) : Hk[κ , μ] = Hk[κ.fst , μ] + Hk[κ.condKernel , μ.compProd κ.fst]`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [inst_2 : MeasurableSpace U] [inst_3 : Countable S] [inst_4 : MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [inst_7 : Countable U] [inst_8 : MeasurableSingletonClass U] {κ : Kernel T (S × U)} [inst_9 : IsZeroOrMarkovKernel κ] [hU : Nonempty U] {μ : Measure T} [IsZeroOrProbabilityMeasure μ] [FiniteSupport μ], κ.AEFiniteKernelSupport μ → Hk[κ , μ] = Hk[κ.fst , μ] + Hk[κ.condKernel , μ.compProd κ.fst]`
Previous English: Let $S$, $T$, $U$ be countable spaces with measurable singletons, with $U$ nonempty. Let $\mu$ be a measure on $T$ that is zero or a probability measure and has finite support, and let $\kappa$ be a kernel from $T$ to $S\times U$ that is zero or Markov and has almost everywhere finite kernel support with respect to $\mu$. Then $H_k[\kappa,\mu] = H_k[\kappa.\mathrm{fst},\mu] + H_k[\kappa.\mathrm{condKernel},\ \mu\otimes\kappa.\mathrm{fst}]$, where $\kappa.\mathrm{fst}$ is the first marginal of $\kappa$ and $\kappa.\mathrm{condKernel}$ its conditional kernel.
Checker's issue: The symbols H_k (kernel entropy Hk[.,.]) and the product mu (x) kappa.fst (Measure.compProd) are used without being introduced by definition or by name; also the measurable-space structures on S, T, U are only implicit. Name H_k as the entropy of a kernel with respect to a measure and state that mu (x) kappa.fst is the composition-product measure mu.compProd kappa.fst on T x S.
