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

#### `ProbabilityTheory.Kernel.AEFiniteKernelSupport` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → Prop`
Docstring: A kernel `κ` has almost everywhere finite support wrt a measure `μ` if, for almost every point `t`, then `κ t` has finite support. Note that we don't require any uniformity wrt `t`.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) (μ : Measure T) => ∀ᵐ (t : T) ∂μ, ∃ (A : Finset S), (κ t : Measure S) (↑A)ᶜ = (0 : ENNReal)`

#### `ProbabilityTheory.Kernel.AEFiniteKernelSupport.mk` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → [Countable T] → [MeasurableSingletonClass T] → {μ : Measure T} → {κ : Kernel T S} → κ.AEFiniteKernelSupport μ → Kernel T S`
Docstring: The definition doesn't use `_hκ`, but we keep it here still as it doesn't give anything interesting otherwise.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] [Countable T] [MeasurableSingletonClass T] {μ : Measure T} {κ : Kernel T S} (_hκ : κ.AEFiniteKernelSupport μ) => if hS : Nonempty S then Kernel.piecewise (s := {t : T | ∃ (A : Finset S), (κ t : Measure S) (↑A)ᶜ = (0 : ENNReal)}) ⋯ κ (Kernel.const T (Measure.dirac hS.some)) else (0 : Kernel T S)`

#### `ProbabilityTheory.Kernel.FiniteKernelSupport` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Prop`
Docstring: The analogue of FiniteSupport for probability kernels.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) => ∀ (t : T), ∃ (A : Finset S), (κ t : Measure S) (↑A)ᶜ = (0 : ENNReal)`

## Flagged translations

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport.finiteKernelSupport_mk`
Lean (short): `[Countable T] [MeasurableSingletonClass T] [MeasurableSingletonClass S] (hκ : κ.AEFiniteKernelSupport μ) : hκ.mk.FiniteKernelSupport`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [inst_2 : Countable T] [inst_3 : MeasurableSingletonClass T] {μ : Measure T} [MeasurableSingletonClass S] {κ : Kernel T S} (hκ : κ.AEFiniteKernelSupport μ), hκ.mk.FiniteKernelSupport`
Previous English: Let $T$ be a countable space in which singletons are measurable, and let $S$ be a space in which singletons are measurable. If the kernel $\kappa$ from $T$ to $S$ has almost everywhere finite kernel support with respect to $\mu$ (hypothesis $h\kappa$), then the kernel $h\kappa.\mathrm{mk}$ has finite kernel support.
Checker's issue: $\mu$ is used without being introduced (a measure on $T$)

### `ProbabilityTheory.Kernel.disintegration`
Lean (short): `[Countable S] [DiscreteMeasurableSpace S] [Countable U] [Nonempty U] [DiscreteMeasurableSpace U] (κ : Kernel T (S × U)) [IsFiniteKernel κ] : κ = κ.fst.compProd κ.condKernel`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} {U : Type u_4} [inst : Countable S] [inst_1 : MeasurableSpace S] [inst_2 : DiscreteMeasurableSpace S] [inst_3 : MeasurableSpace T] [inst_4 : MeasurableSpace U] [inst_5 : Countable U] [inst_6 : Nonempty U] [inst_7 : DiscreteMeasurableSpace U] (κ : Kernel T (S × U)) [inst_8 : IsFiniteKernel κ], κ = κ.fst.compProd κ.condKernel`
Previous English: Let $S$ be a countable measurable space in which every set is measurable, and $U$ a nonempty countable measurable space in which every set is measurable. For every finite kernel $\kappa$ from $T$ to $S\times U$, one has $\kappa=\kappa.\mathrm{fst}\otimes\kappa.\mathrm{condKernel}$, i.e. $\kappa$ equals the composition-product of its first marginal with its conditional kernel.
Checker's issue: $T$ is never introduced (a measurable space); also $\kappa.\mathrm{fst}$ and $\kappa.\mathrm{condKernel}$ are described informally without support in the prompt
