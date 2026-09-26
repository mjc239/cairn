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

#### `ProbabilityTheory.Kernel.AEFiniteKernelSupport` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → Prop`
Docstring: A kernel `κ` has almost everywhere finite support wrt a measure `μ` if, for almost every point `t`, then `κ t` has finite support. Note that we don't require any uniformity wrt `t`.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) (μ : Measure T) => ∀ᵐ (t : T) ∂μ, ∃ (A : Finset S), (κ t : Measure S) (↑A)ᶜ = (0 : ENNReal)`

#### `ProbabilityTheory.Kernel.mutualInfo` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → {U : Type u_4} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → [inst_2 : MeasurableSpace U] → Kernel T (S × U) → Measure T → ℝ`
Docstring: Mutual information of a kernel into a product space with respect to a measure.
Definition: `fun {S : Type u_2} {T : Type u_3} {U : Type u_4} [MeasurableSpace S] [MeasurableSpace T] [MeasurableSpace U] (κ : Kernel T (S × U)) (μ : Measure T) => Hk[κ.fst , μ] + Hk[κ.snd , μ] - Hk[κ , μ]`

#### `ProbabilityTheory.Kernel.entropy` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → ℝ`
Docstring: Entropy of a kernel with respect to a measure.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) (μ : Measure T) => ∫ (x : T), (fun (y : T) => measureEntropy.{u_2} (S := S) (κ y)) x ∂μ`

## Flagged translations

### `ProbabilityTheory.Kernel.mutualInfo_nonneg`
Lean (short): `[MeasurableSingletonClass S] [MeasurableSingletonClass U] [MeasurableSingletonClass T] [Countable T] [IsFiniteMeasure μ] [FiniteSupport μ] (hκ : κ.AEFiniteKernelSupport μ) : 0 ≤ Ik[κ , μ]`
Lean (full): `∀ {S : Type u_2} {T : Type u_3} {U : Type u_4} [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [inst_2 : MeasurableSpace U] [MeasurableSingletonClass S] [MeasurableSingletonClass U] [MeasurableSingletonClass T] [Countable T] {κ : Kernel T (S × U)} {μ : Measure T} [IsFiniteMeasure μ] [FiniteSupport μ], κ.AEFiniteKernelSupport μ → (0 : ℝ) ≤ Ik[κ , μ]`
Previous English: Let $S$, $U$, $T$ have measurable singletons, with $T$ countable. Let $\mu$ be a finite measure on $T$ with finite support, and let $\kappa$ be a kernel from $T$ into $S \times U$ that has almost everywhere finite kernel support with respect to $\mu$. Then $0 \le I_k[\kappa,\mu]$.
Checker's issue: The symbol I_k[κ,μ] is not introduced (never named as the mutual information of the kernel κ with respect to μ); S, U, T are also not explicitly said to be measurable spaces. Otherwise the statement matches.
