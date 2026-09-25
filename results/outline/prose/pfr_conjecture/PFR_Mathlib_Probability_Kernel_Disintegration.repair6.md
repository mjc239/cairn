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

## Flagged translations

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport`
Lean (short): `(κ : Kernel T S) (μ : Measure T) : Prop`
Lean (full): `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → Prop`
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) (μ : Measure T) => ∀ᵐ (t : T) ∂μ, ∃ (A : Finset S), (κ t : Measure S) (↑A)ᶜ = (0 : ENNReal)`
Docstring: A kernel `κ` has almost everywhere finite support wrt a measure `μ` if, for almost every point `t`, then `κ t` has finite support. Note that we don't require any uniformity wrt `t`.
Previous English: Let $S$ and $T$ be measurable spaces. For a kernel $\kappa$ from $T$ to $S$ and a measure $\mu$ on $T$, this defines a proposition, ``$\kappa$ has almost everywhere finite kernel support with respect to $\mu$''. According to the docstring, this means that for $\mu$-almost every point $t$, the measure $\kappa(t)$ has finite support, with no uniformity in $t$ required.
Checker's issue: Definition body is shown but the English only paraphrases the docstring. It should state the body: for μ-a.e. t there is a finite set A ⊆ S with κ(t)(Aᶜ) = 0. 'κ(t) has finite support' is only the docstring's gloss.

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport.mk`
Lean (short): `[Countable T] [MeasurableSingletonClass T] (_hκ : κ.AEFiniteKernelSupport μ) : Kernel T S`
Lean (full): `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → [Countable T] → [MeasurableSingletonClass T] → {μ : Measure T} → {κ : Kernel T S} → κ.AEFiniteKernelSupport μ → Kernel T S`
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] [Countable T] [MeasurableSingletonClass T] {μ : Measure T} {κ : Kernel T S} (_hκ : κ.AEFiniteKernelSupport μ) => if hS : Nonempty S then Kernel.piecewise (s := {t : T | ∃ (A : Finset S), (κ t : Measure S) (↑A)ᶜ = (0 : ENNReal)}) ⋯ κ (Kernel.const T (Measure.dirac hS.some)) else (0 : Kernel T S)`
Docstring: The definition doesn't use `_hκ`, but we keep it here still as it doesn't give anything interesting otherwise.
Previous English: Let $S$ and $T$ be measurable spaces, with $T$ countable and with measurable singletons. Given a measure $\mu$ on $T$, a kernel $\kappa$ from $T$ to $S$, and a proof $h\kappa$ that $\kappa$ has almost everywhere finite kernel support with respect to $\mu$, this defines a kernel $h\kappa.\mathrm{mk}$ from $T$ to $S$. According to the docstring, the definition does not use the hypothesis $h\kappa$, which is kept only because the construction is otherwise uninteresting.
Checker's issue: Definition body is shown but the English gives no description of the kernel, only the docstring remark that hκ is unused. It omits the body: if S is nonempty, the piecewise kernel equal to κ on {t | ∃ finite A, κ t Aᶜ = 0} and to the constant Dirac kernel at a chosen point elsewhere; otherwise the zero kernel.

### `ProbabilityTheory.Kernel.FiniteKernelSupport`
Lean (short): `(κ : Kernel T S) : Prop`
Lean (full): `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Prop`
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) => ∀ (t : T), ∃ (A : Finset S), (κ t : Measure S) (↑A)ᶜ = (0 : ENNReal)`
Docstring: The analogue of FiniteSupport for probability kernels.
Previous English: Let $S$ and $T$ be measurable spaces. For a kernel $\kappa$ from $T$ to $S$, this defines a proposition, ``$\kappa$ has finite kernel support''. According to the docstring, it is the analogue of finite support (`FiniteSupport`) for probability kernels.
Checker's issue: Definition body is shown but the English only repeats the docstring ('analogue of FiniteSupport for probability kernels'). It never states the body: for every t there is a finite A ⊆ S with κ(t)(Aᶜ) = 0. The docstring's 'probability kernels' is also misleading, since the definition applies to any kernel.

### `ProbabilityTheory.Kernel.aefiniteKernelSupport_of_cond`
Lean (short): `[Nonempty U] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [MeasurableSingletonClass U] [Countable U] [Countable S] [Countable T] (μ : Measure T) (hκ : κ.AEFiniteKernelSupport μ) [IsFiniteKernel κ] : κ.condKernel.AEFiniteKernelSupport (μ.compProd κ.fst)`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [inst_2 : MeasurableSpace U] {κ : Kernel T (S × U)} [hU : Nonempty U] [inst_3 : MeasurableSingletonClass S] [MeasurableSingletonClass T] [inst_5 : MeasurableSingletonClass U] [inst_6 : Countable U] [inst_7 : Countable S] [Countable T] (μ : Measure T), κ.AEFiniteKernelSupport μ → ∀ [inst_9 : IsFiniteKernel κ], κ.condKernel.AEFiniteKernelSupport (μ.compProd κ.fst)`
Docstring: Conditioning a kernel preserves finite kernel support.
Previous English: Let $S$, $T$, $U$ be countable measurable spaces with measurable singletons, with $U$ nonempty. Let $\mu$ be a measure on $T$ and let $\kappa$ be a finite kernel from $T$ to $S \times U$ that has almost everywhere finite support with respect to $\mu$. Then $\kappa.\mathrm{condKernel}$ has almost everywhere finite support with respect to $\mu\otimes\kappa.\mathrm{fst}$.
Checker's issue: The symbols κ.condKernel, κ.fst and μ⊗κ.fst are used without being introduced; the reader is not told that κ.fst is the first marginal, that condKernel is the conditional kernel T×S → U, or that ⊗ is the measure-kernel composition-product rather than a product measure. The project notion AEFiniteKernelSupport is also used without saying what it means (for a.e. point there is a finite set of full measure).
