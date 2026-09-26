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

## Flagged translations

### `cft`
Lean (short): `[Fintype G] (f : G → ℂ) (_ : AddChar G ℂ) : ℂ`
Lean (full): `{G : Type u_1} → [inst : AddCommGroup G] → [Fintype G] → (G → ℂ) → AddChar G ℂ → ℂ`
Definition: `fun {G : Type u_1} [AddCommGroup G] [Fintype G] (f : G → ℂ) (ψ : AddChar G ℂ) => ⟪⇑ψ, f⟫ₙ_[ℂ]`
Docstring: The discrete Fourier transform.
Previous English: Let $G$ be a finite abelian group. For $f : G \to \mathbb{C}$, $\mathrm{cft}(f)$ assigns to each additive character $\psi : G \to \mathbb{C}$ a complex number $\mathrm{cft}(f)(\psi)$; according to its docstring, it is the discrete Fourier transform of $f$.
Checker's issue: Definition body is shown (cft f ψ = ⟪ψ, f⟫ₙ_[ℂ], the normalised (expectation) inner product of ψ and f on G), but the English only gives the type and the docstring ('the discrete Fourier transform'); it does not describe the formula, and in particular omits the compact normalisation that distinguishes it from dft.
