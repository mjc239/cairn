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

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

### `largeSpec`
Lean (short): `[Fintype G] (f : G → ℂ) (η : ℝ) : Finset (AddChar G ℂ)`
Lean (full): `{G : Type u_1} → [inst : AddCommGroup G] → [Fintype G] → [MeasurableSpace G] → (G → ℂ) → ℝ → Finset (AddChar G ℂ)`
Docstring: The `η`-large spectrum of a function.
Previous English: Let $G$ be a finite type (with its additive group structure). For $f : G \to \mathbb{C}$ and $\eta \in \mathbb{R}$, $\mathrm{largeSpec}(f, \eta)$ is a finite set of additive characters $G \to \mathbb{C}$; according to its docstring, it is the $\eta$-large spectrum of $f$.
Checker's issue: Says only 'its additive group structure' where the Lean requires an abelian group, and omits the measurable structure on G.
