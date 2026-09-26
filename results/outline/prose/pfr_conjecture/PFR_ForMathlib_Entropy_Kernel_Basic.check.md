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
A definition whose body is shown must be described by what it defines (in words or a formula that agrees with the
body), not only by a paraphrase of its docstring. Stylistic choices are fine.

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
Constructor (every field with its type): `∀ {S : Type u_2} [inst : MeasurableSpace S] {μ : autoParam (Measure S) FiniteSupport._auto_1}, (∃ (A : Finset S), ∀ᵐ (x : S) ∂μ, x ∈ A) → FiniteSupport μ`

#### `FiniteRange` (inductive)
Lean: `{Ω : Type u_1} → {G : Type u_2} → (Ω → G) → Prop`
Docstring: The property of having a finite range.
Constructor (every field with its type): `∀ {Ω : Type u_1} {G : Type u_2} {X : Ω → G}, (Set.range X).Finite → FiniteRange X`

#### `ProbabilityTheory.Kernel.AEFiniteKernelSupport` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → Prop`
Docstring: A kernel `κ` has almost everywhere finite support wrt a measure `μ` if, for almost every point `t`, then `κ t` has finite support. Note that we don't require any uniformity wrt `t`.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) (μ : Measure T) => ∀ᵐ (t : T) ∂μ, ∃ (A : Finset S), (κ t : Measure S) (↑A)ᶜ = (0 : ENNReal)`

## Translations

### `ProbabilityTheory.Kernel.entropy`
Lean (short): `(κ : Kernel T S) (μ : Measure T) : ℝ`
Lean (full): `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → ℝ`
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) (μ : Measure T) => ∫ (x : T), (fun (y : T) => measureEntropy.{u_2} (S := S) (κ y)) x ∂μ`
Docstring: Entropy of a kernel with respect to a measure.
English: For a kernel $\kappa$ from $T$ to $S$ and a measure $\mu$ on $T$, $H_k[\kappa,\mu]$ denotes the entropy of the kernel $\kappa$ with respect to the measure $\mu$.

### `ProbabilityTheory.Kernel.entropy_prodMkLeft_unit`
Lean (short): `[MeasurableSingletonClass T] (κ : Kernel T S) [IsZeroOrProbabilityMeasure μ] [FiniteSupport μ] : Hk[Kernel.prodMkLeft Unit κ , Measure.map (Prod.mk ()) μ] = Hk[κ , μ]`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [MeasurableSingletonClass T] (κ : Kernel T S) {μ : Measure T} [IsZeroOrProbabilityMeasure μ] [FiniteSupport μ], Hk[Kernel.prodMkLeft Unit κ , Measure.map (Prod.mk ()) μ] = Hk[κ , μ]`
English: Let $S$ be a measurable space and $T$ a measurable space in which every singleton is measurable. Let $\kappa$ be a kernel from $T$ to $S$, and let $\mu$ be a measure on $T$ that is either the zero measure or a probability measure and that has finite support in the sense of `FiniteSupport` (docstring: there is a finite set whose complement has measure zero). Let $\kappa'$ = `Kernel.prodMkLeft Unit κ`, the kernel from $\mathrm{Unit} \times T$ to $S$ given by $\kappa'((), t) = \kappa(t)$, where $\mathrm{Unit}$ is the one-point type, and let $\mu'$ be the pushforward of $\mu$ under $t \mapsto ((), t)$, a measure on $\mathrm{Unit} \times T$. Then $H_k[\kappa', \mu'] = H_k[\kappa, \mu]$. Here, for measurable spaces $W, V$, a kernel $\rho$ from $W$ to $V$ and a measure $\nu$ on $W$, $H_k[\rho, \nu]$ = `Kernel.entropy ρ ν` (`Hk[ρ , ν]`; docstring: entropy of a kernel with respect to a measure) is defined as the Bochner integral $\int_W H(\rho(w))\, d\nu(w)$, where for a measure $m$ on $V$, $H(m)$ = `measureEntropy m` $= \sum_{v \in V} -m'(\{v\}) \log m'(\{v\})$ (an unconditional sum, taken as $0$ if not summable), with $m' = m(V)^{-1} m$ the normalized measure and $m'(\{v\})$ its real value (docstring: entropy of a measure, normalized by $m(V)^{-1}$ to extend the definition to finite measures).

### `ProbabilityTheory.Kernel.aefiniteKernelSupport_condDistrib`
Lean (short): `[Nonempty S] [Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] (X : Ω → S) (Y : Ω → T) (μ : Measure Ω) [IsFiniteMeasure μ] (hX : Measurable X) (hY : Measurable Y) [FiniteRange X] : (condDistrib X Y μ).AEFiniteKernelSupport (Measure.map Y μ)`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [inst_2 : Nonempty S] [inst_3 : Countable S] [inst_4 : MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] (X : Ω → S) (Y : Ω → T) (μ : Measure Ω) [inst_7 : IsFiniteMeasure μ], Measurable X → Measurable Y → ∀ [FiniteRange X], Kernel.AEFiniteKernelSupport (condDistrib X Y μ) (Measure.map Y μ)`
English: Let $S$ be a nonempty countable space and $T$ a countable space, both with measurable singletons. Let $\mu$ be a finite measure on $\Omega$, and let $X : \Omega \to S$ and $Y : \Omega \to T$ be measurable random variables, with $X$ having finite range. Then the conditional distribution kernel $\mathrm{condDistrib}(X \mid Y;\mu)$ has almost everywhere finite kernel support with respect to the law $Y_*\mu$ of $Y$.

### `ProbabilityTheory.Kernel.entropy_compProd`
Lean (short): `[Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [MeasurableSingletonClass U] [IsFiniteMeasure μ] [IsZeroOrMarkovKernel κ] [IsMarkovKernel η] [FiniteSupport μ] (hκ : κ.AEFiniteKernelSupport μ) (hη : η.AEFiniteKernelSupport (μ.compProd κ)) : Hk[κ.compProd η , μ] = Hk[κ , μ] + Hk[η , μ.compProd κ]`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [inst_2 : MeasurableSpace U] [Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [MeasurableSingletonClass U] {μ : Measure T} [IsFiniteMeasure μ] {κ : Kernel T S} [IsZeroOrMarkovKernel κ] {η : Kernel (T × S) U} [IsMarkovKernel η] [FiniteSupport μ], κ.AEFiniteKernelSupport μ → η.AEFiniteKernelSupport (μ.compProd κ) → Hk[κ.compProd η , μ] = Hk[κ , μ] + Hk[η , μ.compProd κ]`
English: Let $S$, $T$, $U$ be measurable spaces; assume $S$ and $T$ are countable with all singletons measurable, and all singletons of $U$ are measurable. Let $\mu$ be a finite measure on $T$ that has finite support in the sense of `FiniteSupport` (docstring: there is a finite set whose complement has measure zero). Let $\kappa$ be a kernel from $T$ to $S$ that is either the zero kernel or a Markov kernel, and let $\eta$ be a Markov kernel from $T \times S$ to $U$. Assume $\kappa$ has almost everywhere finite kernel support (`AEFiniteKernelSupport`): for $\mu$-almost every $t$ there is a finite set $A$ with $A \subseteq S$ and $\kappa(t)(S \setminus A) = 0$; and assume $\eta$ has almost everywhere finite kernel support with respect to the measure $\mu \otimes \kappa$ = `μ.compProd κ` on $T \times S$ (the composition-product of $\mu$ and $\kappa$), i.e. for $(\mu \otimes \kappa)$-almost every $(t,s)$ there is a finite $B \subseteq U$ with $\eta(t,s)(U \setminus B) = 0$. Then $$H_k[\kappa \otimes \eta,\ \mu] = H_k[\kappa, \mu] + H_k[\eta,\ \mu \otimes \kappa],$$ where $\kappa \otimes \eta$ = `κ.compProd η` is the composition-product kernel from $T$ to $S \times U$. Here, for measurable spaces $W, V$, a kernel $\rho$ from $W$ to $V$ and a measure $\nu$ on $W$, $H_k[\rho, \nu]$ = `Kernel.entropy ρ ν` (`Hk[ρ , ν]`; docstring: entropy of a kernel with respect to a measure) is defined as the Bochner integral $\int_W H(\rho(w))\, d\nu(w)$, where for a measure $m$ on $V$, $H(m)$ = `measureEntropy m` $= \sum_{v \in V} -m'(\{v\}) \log m'(\{v\})$ (an unconditional sum, taken as $0$ if not summable), with $m' = m(V)^{-1} m$ the normalized measure and $m'(\{v\})$ its real value (docstring: entropy of a measure, normalized by $m(V)^{-1}$ to extend the definition to finite measures).

### `ProbabilityTheory.Kernel.chain_rule`
Lean (short): `[Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [Countable U] [MeasurableSingletonClass U] [IsZeroOrMarkovKernel κ] [Nonempty U] [IsZeroOrProbabilityMeasure μ] [FiniteSupport μ] (hκ : κ.AEFiniteKernelSupport μ) : Hk[κ , μ] = Hk[κ.fst , μ] + Hk[κ.condKernel , μ.compProd κ.fst]`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [inst_2 : MeasurableSpace U] [inst_3 : Countable S] [inst_4 : MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] [inst_7 : Countable U] [inst_8 : MeasurableSingletonClass U] {κ : Kernel T (S × U)} [inst_9 : IsZeroOrMarkovKernel κ] [hU : Nonempty U] {μ : Measure T} [IsZeroOrProbabilityMeasure μ] [FiniteSupport μ], κ.AEFiniteKernelSupport μ → Hk[κ , μ] = Hk[κ.fst , μ] + Hk[κ.condKernel , μ.compProd κ.fst]`
English: Let $S$, $T$, $U$ be measurable spaces, each countable with all singletons measurable, and let $U$ be nonempty. Let $\kappa$ be a kernel from $T$ to $S \times U$ that is either the zero kernel or a Markov kernel, and let $\mu$ be a measure on $T$ that is either the zero measure or a probability measure and that has finite support in the sense of `FiniteSupport` (docstring: there is a finite set whose complement has measure zero). Assume $\kappa$ has almost everywhere finite kernel support (`AEFiniteKernelSupport`): for $\mu$-almost every $t$ there is a finite set $A$ with $A \subseteq S \times U$ and $\kappa(t)((S \times U) \setminus A) = 0$. Let $\kappa_1$ = `κ.fst` be the first marginal of $\kappa$ (the kernel from $T$ to $S$ with $\kappa_1(t)$ the pushforward of $\kappa(t)$ under the first projection), let $\kappa_c$ = `κ.condKernel` be the conditional kernel of $\kappa$ (Mathlib's kernel from $T \times S$ to $U$), and let $\mu \otimes \kappa_1$ = `μ.compProd κ.fst` be the composition-product measure on $T \times S$. Then $$H_k[\kappa, \mu] = H_k[\kappa_1, \mu] + H_k[\kappa_c,\ \mu \otimes \kappa_1].$$ Here, for measurable spaces $W, V$, a kernel $\rho$ from $W$ to $V$ and a measure $\nu$ on $W$, $H_k[\rho, \nu]$ = `Kernel.entropy ρ ν` (`Hk[ρ , ν]`; docstring: entropy of a kernel with respect to a measure) is defined as the Bochner integral $\int_W H(\rho(w))\, d\nu(w)$, where for a measure $m$ on $V$, $H(m)$ = `measureEntropy m` $= \sum_{v \in V} -m'(\{v\}) \log m'(\{v\})$ (an unconditional sum, taken as $0$ if not summable), with $m' = m(V)^{-1} m$ the normalized measure and $m'(\{v\})$ its real value (docstring: entropy of a measure, normalized by $m(V)^{-1}$ to extend the definition to finite measures).
