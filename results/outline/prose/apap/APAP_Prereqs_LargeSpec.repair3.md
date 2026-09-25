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

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `MeasureTheory.dLpNorm` (def)
Lean: `{α : Type u_1} → {E : Type u_4} → [MeasurableSpace α] → [NormedAddCommGroup E] → ENNReal → (α → E) → ℝ`
Docstring: The Lp norm of a function with the compact normalisation.
Definition: `fun {α : Type u_1} {E : Type u_4} [inst : MeasurableSpace α] [NormedAddCommGroup E] (p : ENNReal) (f : α → E) => lpNorm (m0 := inst) f p Measure.count`

#### `dft` (def)
Lean: `{G : Type u_1} → [inst : AddCommGroup G] → [Fintype G] → (G → ℂ) → AddChar G ℂ → ℂ`
Docstring: The discrete Fourier transform.
Definition: `fun {G : Type u_1} [AddCommGroup G] [Fintype G] (f : G → ℂ) (ψ : AddChar G ℂ) => ⟪⇑ψ, f⟫_[ℂ]`

## Flagged translations

### `largeSpec`
Lean (short): `[Fintype G] (f : G → ℂ) (η : ℝ) : Finset (AddChar G ℂ)`
Lean (full): `{G : Type u_1} → [inst : AddCommGroup G] → [Fintype G] → [MeasurableSpace G] → (G → ℂ) → ℝ → Finset (AddChar G ℂ)`
Definition: `fun {G : Type u_1} [AddCommGroup G] [Fintype G] [MeasurableSpace G] (f : G → ℂ) (η : ℝ) => {ψ : AddChar G ℂ | η * ‖f‖_[(1 : ENNReal)] ≤ ‖dft f ψ‖}`
Docstring: The `η`-large spectrum of a function.
Previous English: Let $G$ be a finite abelian group (an additive commutative group with finitely many elements) equipped with a measurable space structure. For $f : G \to \mathbb{C}$ and $\eta \in \mathbb{R}$, $\mathrm{largeSpec}(f, \eta)$ is a finite set of additive characters $G \to \mathbb{C}$; according to its docstring, it is the $\eta$-large spectrum of $f$.
Checker's issue: Definition body is shown but the English only paraphrases the docstring ('the η-large spectrum'). It should state that largeSpec(f, η) is the set of characters ψ with η·‖f‖₁ ≤ |f̂(ψ)|, where ‖f‖₁ = Σ_x |f(x)| is the L¹ norm with counting measure (dLpNorm) and f̂(ψ) = dft f ψ = ⟪ψ, f⟫.
