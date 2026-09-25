You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption) and the English. Compare the English with the full statement.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `iterCConv`
Lean (short): `[Fintype G] [CharZero R] (f : G → R) (_ : ℕ) (_ : G) : R`
Lean (full): `{G : Type u_1} → {R : Type u_3} → [Fintype G] → [DecidableEq G] → [AddCommGroup G] → [inst : Semifield R] → [CharZero R] → (G → R) → ℕ → G → R`
English: Let $G$ be a finite type (with its additive group structure) and $R$ a ring of characteristic zero. For $f : G \to R$ and $n \in \mathbb{N}$, $\mathrm{iterCConv}(f, n)$ is a function $G \to R$; according to its docstring, it is the (n-fold) iterated convolution of $f$.
