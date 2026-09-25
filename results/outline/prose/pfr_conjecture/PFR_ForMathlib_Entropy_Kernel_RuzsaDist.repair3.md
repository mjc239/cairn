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

### `ProbabilityTheory.Kernel.rdistm`
Lean (short): `(μ : Measure G) (ν : Measure G) : ℝ`
Lean (full): `{G : Type u_4} → [inst : MeasurableSpace G] → [AddCommGroup G] → Measure G → Measure G → ℝ`
Docstring: The Rusza distance between two measures, defined as `H[X - Y] - H[X]/2 - H[Y]/2` where `X` and `Y` are independent variables distributed according to the two measures.
Previous English: For two measures $\mu,\nu$ on an abelian group $G$, the Ruzsa distance $\mathrm{rdistm}(\mu,\nu)$ is the real number $H[X-Y]-H[X]/2-H[Y]/2$, where $X$ and $Y$ are independent random variables distributed according to $\mu$ and $\nu$ respectively.
Checker's issue: The formula H[X-Y]-H[X]/2-H[Y]/2 with independent X and Y goes beyond the signature and is not attributed to the docstring.
