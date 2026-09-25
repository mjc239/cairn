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

### `AddDissociated.boringEnergy_le`
Lean (short): `[DiscreteMeasurableSpace G] [Finite G] (hs : AddDissociated ↑s) (n : ℕ) : boringEnergy n s ≤ changConst ^ n * ↑n ^ n * ↑s.card ^ n`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : MeasurableSpace G] [DiscreteMeasurableSpace G] [inst_3 : DecidableEq G] [Finite G] {s : Finset G}, AddDissociated ↑s → ∀ (n : ℕ), boringEnergy n s ≤ changConst ^ n * ↑n ^ n * ↑s.card ^ n`
Previous English: Let $G$ be finite and carry the discrete measurable structure. If $s \subseteq G$ is a finite dissociated set, then for every $n \in \mathbb{N}$, $\mathrm{boringEnergy}_n(s) \le \mathrm{changConst}^n \cdot n^n \cdot |s|^n$.
Checker's issue: Says only 'G finite' and omits that G is an abelian group (AddCommGroup).
