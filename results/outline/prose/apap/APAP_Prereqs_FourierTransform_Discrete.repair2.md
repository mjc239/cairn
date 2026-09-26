You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one. For a definition, name the setting its signature assumes. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

### `dft`
Lean (short): `[Fintype G] (f : G → ℂ) (_ : AddChar G ℂ) : ℂ`
Lean (full): `{G : Type u_1} → [inst : AddCommGroup G] → [Fintype G] → (G → ℂ) → AddChar G ℂ → ℂ`
Docstring: The discrete Fourier transform.
Previous English: Let $G$ be a finite type (with its additive group structure). For $f : G \to \mathbb{C}$, $\mathrm{dft}(f)$ assigns a complex number $\mathrm{dft}(f)(\psi)$ to each additive character $\psi : G \to \mathbb{C}$; according to its docstring, it is the discrete Fourier transform of $f$.
Checker's issue: Says G has 'its additive group structure' but omits that the Lean requires G to be an abelian group (AddCommGroup).
