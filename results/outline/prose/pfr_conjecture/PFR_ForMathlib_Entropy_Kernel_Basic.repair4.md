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

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

#### `FiniteRange` (inductive)
Lean: `{Ω : Type u_1} → {G : Type u_2} → (Ω → G) → Prop`
Docstring: The property of having a finite range.
Constructor (every field with its type): `∀ {Ω : Type u_1} {G : Type u_2} {X : Ω → G}, (Set.range X).Finite → FiniteRange X`

#### `ProbabilityTheory.Kernel.AEFiniteKernelSupport` (def)
Lean: `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → Prop`
Docstring: A kernel `κ` has almost everywhere finite support wrt a measure `μ` if, for almost every point `t`, then `κ t` has finite support. Note that we don't require any uniformity wrt `t`.
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) (μ : Measure T) => ∀ᵐ (t : T) ∂μ, ∃ (A : Finset S), (κ t : Measure S) (↑A)ᶜ = (0 : ENNReal)`

## Flagged translations

### `ProbabilityTheory.Kernel.entropy`
Lean (short): `(κ : Kernel T S) (μ : Measure T) : ℝ`
Lean (full): `{S : Type u_2} → {T : Type u_3} → [inst : MeasurableSpace S] → [inst_1 : MeasurableSpace T] → Kernel T S → Measure T → ℝ`
Definition: `fun {S : Type u_2} {T : Type u_3} [MeasurableSpace S] [MeasurableSpace T] (κ : Kernel T S) (μ : Measure T) => ∫ (x : T), (fun (y : T) => measureEntropy.{u_2} (S := S) (κ y)) x ∂μ`
Docstring: Entropy of a kernel with respect to a measure.
Previous English: For a kernel $\kappa$ from $T$ to $S$ and a measure $\mu$ on $T$, $H_k[\kappa,\mu]$ denotes the entropy of the kernel $\kappa$ with respect to the measure $\mu$.
Checker's issue: A definition with its body shown, but the English only paraphrases the docstring ('the entropy of the kernel'). It does not give the body H_k[κ,μ] = ∫ H(κ(t)) dμ(t) (Bochner integral), with H = measureEntropy the normalized Shannon entropy. It also does not state that S and T are measurable spaces.

### `ProbabilityTheory.Kernel.aefiniteKernelSupport_condDistrib`
Lean (short): `[Nonempty S] [Countable S] [MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] (X : Ω → S) (Y : Ω → T) (μ : Measure Ω) [IsFiniteMeasure μ] (hX : Measurable X) (hY : Measurable Y) [FiniteRange X] : (condDistrib X Y μ).AEFiniteKernelSupport (Measure.map Y μ)`
Lean (full): `∀ {Ω : Type u_1} {S : Type u_2} {T : Type u_3} [mΩ : MeasurableSpace Ω] [inst : MeasurableSpace S] [inst_1 : MeasurableSpace T] [inst_2 : Nonempty S] [inst_3 : Countable S] [inst_4 : MeasurableSingletonClass S] [Countable T] [MeasurableSingletonClass T] (X : Ω → S) (Y : Ω → T) (μ : Measure Ω) [inst_7 : IsFiniteMeasure μ], Measurable X → Measurable Y → ∀ [FiniteRange X], Kernel.AEFiniteKernelSupport (condDistrib X Y μ) (Measure.map Y μ)`
Previous English: Let $S$ be a nonempty countable space and $T$ a countable space, both with measurable singletons. Let $\mu$ be a finite measure on $\Omega$, and let $X : \Omega \to S$ and $Y : \Omega \to T$ be measurable random variables, with $X$ having finite range. Then the conditional distribution kernel $\mathrm{condDistrib}(X \mid Y;\mu)$ has almost everywhere finite kernel support with respect to the law $Y_*\mu$ of $Y$.
Checker's issue: The conclusion is the project notion `AEFiniteKernelSupport`, stated only as 'has almost everywhere finite kernel support' with no meaning given. It should say: for Y_*μ-almost every t there is a finite A⊆S with condDistrib(X|Y;μ)(t)(Aᶜ)=0. Ω is also not explicitly introduced as a measurable space.
