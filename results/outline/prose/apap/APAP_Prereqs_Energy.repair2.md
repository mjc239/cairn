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

### `energy`
Lean (short): `(n : ℕ) (s : Finset G) (ν : G → ℂ) : ℝ`
Lean (full): `{G : Type u_1} → [AddCommGroup G] → ℕ → Finset G → (G → ℂ) → ℝ`
Previous English: For $n \in \mathbb{N}$, a finite set $s \subseteq G$ and a weight $\nu : G \to \mathbb{C}$, defines the real number $\mathrm{energy}_n(s, \nu)$, a weighted $n$-fold additive energy of $s$.
Checker's issue: The definition does not state that G is an abelian group.

### `boringEnergy`
Lean (short): `(n : ℕ) (s : Finset G) : ℝ`
Lean (full): `{G : Type u_1} → [AddCommGroup G] → [DecidableEq G] → ℕ → Finset G → ℝ`
Previous English: For $n \in \mathbb{N}$ and a finite set $s \subseteq G$, defines the real number $\mathrm{boringEnergy}_n(s)$, the unweighted $n$-fold additive energy of $s$.
Checker's issue: The definition does not state that G is an abelian group.
