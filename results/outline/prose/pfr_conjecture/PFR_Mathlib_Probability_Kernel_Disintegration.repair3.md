You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport`
Lean (short): `(κ : Kernel T S) (μ : Measure T) : Prop`
Lean (full): `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → Prop`
Docstring: A kernel `κ` has almost everywhere finite support wrt a measure `μ` if, for almost every point `t`, then `κ t` has finite support. Note that we don't require any uniformity wrt `t`.
Previous English: For a kernel $\kappa$ from $T$ to $S$ and a measure $\mu$ on $T$, defines the property that $\kappa$ has almost everywhere finite support with respect to $\mu$: for $\mu$-almost every $t$, the measure $\kappa(t)$ has finite support (with no uniformity in $t$ required).
Checker's issue: The explanation that kappa(t) has finite support for mu-almost every t, with no uniformity in t, is a gloss beyond the signature that is not attributed to the docstring.

### `ProbabilityTheory.Kernel.AEFiniteKernelSupport.mk`
Lean (short): `[Countable T] [MeasurableSingletonClass T] (_hκ : κ.AEFiniteKernelSupport μ) : Kernel T S`
Lean (full): `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → [Countable T] → [MeasurableSingletonClass T] → {μ : Measure T} → {κ : Kernel T S} → κ.AEFiniteKernelSupport μ → Kernel T S`
Docstring: The definition doesn't use `_hκ`, but we keep it here still as it doesn't give anything interesting otherwise.
Previous English: Let $T$ be a countable space in which singletons are measurable, and let $\kappa$ be a kernel from $T$ to $S$ that has almost everywhere finite kernel support with respect to a measure $\mu$ on $T$ (hypothesis $h\kappa$). This defines an associated kernel $h\kappa.\mathrm{mk}$ from $T$ to $S$ (the definition does not actually use the hypothesis $h\kappa$).
Checker's issue: The claim that the definition does not use the hypothesis h-kappa goes beyond the signature and is not attributed to the docstring.

### `ProbabilityTheory.Kernel.FiniteKernelSupport`
Lean (short): `(κ : Kernel T S) : Prop`
Lean (full): `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Prop`
Docstring: The analogue of FiniteSupport for probability kernels.
Previous English: For a kernel $\kappa$ from $T$ to $S$, defines the property that $\kappa$ has finite kernel support, the analogue for kernels of a measure having finite support.
Checker's issue: The gloss calling it the kernel analogue of a measure with finite support goes beyond the signature and is not attributed to the docstring.
