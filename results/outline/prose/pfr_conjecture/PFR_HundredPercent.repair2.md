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

### `symmGroup`
Lean (short): `[MeasurableAdd₂ G] (X : Ω → G) (hX : Measurable X) : AddSubgroup G`
Lean (full): `{Ω : Type u_1} → {G : Type u_2} → [inst : MeasureSpace Ω] → [inst_1 : MeasurableSpace G] → [inst_2 : AddCommGroup G] → [MeasurableAdd₂ G] → (X : Ω → G) → Measurable X → AddSubgroup G`
Docstring: The symmetry group Sym of $X$: the set of all $h ∈ G$ such that $X + h$ has an identical distribution to $X$.
Previous English: For a measurable random variable $X:\Omega\to G$, defines the symmetry group $\mathrm{Sym}[X]$: the additive subgroup of $G$ consisting of all $h\in G$ such that $X+h$ has the same distribution as $X$.
Checker's issue: Omits the setting (G an abelian group with a measurable structure and measurable addition, Omega a measure space), and the description of the subgroup's elements is not attributed to the docstring.
