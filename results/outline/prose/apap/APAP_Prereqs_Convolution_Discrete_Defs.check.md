You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. Compare the
English with the full statement; anything the English attributes to the docstring must actually be in it.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Definitions are held to the same standard: the English must name the setting the signature assumes
("for an abelian group $G$ and …, $\mathrm{rdist}$ is …"). Replacing an assumption by a stronger one (a metric
space where the Lean has a pseudometric space) is unfaithful too, and so is leaving a restrictive type unstated
(a natural number, a nonnegative real). Citations (theorem or lemma numbers) and remarks are claims too: each must
be supported by the docstring or the Lean. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ddconv`
Lean (short): `[Fintype G] (f : G → R) (g : G → R) (_ : G) : R`
Lean (full): `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [Fintype G] → [CommSemiring R] → (G → R) → (G → R) → G → R`
Docstring: Convolution
English: Let $G$ be a finite abelian group and $R$ a commutative semiring. For $f, g : G \to R$, $\mathrm{ddconv}(f, g)$ is a function $G \to R$; according to its docstring, it is the convolution of $f$ and $g$.

### `ddconv_eq_sum_sub`
Lean (short): `[Fintype G] (f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
Lean (full): `∀ {G : Type u_1} {R : Type u_3} [inst : DecidableEq G] [inst_1 : AddCommGroup G] [inst_2 : Fintype G] [inst_3 : CommSemiring R] (f g : G → R) (a : G), (f ∗ᵈ g) a = ∑ t : G, f (a - t) * g t`
English: Let $G$ be a finite abelian group and $R$ a commutative semiring. For $f, g : G \to R$ and $a \in G$, the discrete convolution satisfies $(f *_d g)(a) = \sum_{t \in G} f(a - t)\, g(t)$.

### `trivChar`
Lean (short): `(_ : G) : R`
Lean (full): `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [CommSemiring R] → G → R`
Docstring: The trivial character.
English: Let $G$ be an abelian group and $R$ a commutative semiring. $\mathrm{trivChar}$ is a function $G \to R$; according to its docstring, it is the trivial character.

### `iterConv`
Lean (short): `[Fintype G] (f : G → R) (_ : ℕ) (_ : G) : R`
Lean (full): `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [Fintype G] → [CommSemiring R] → (G → R) → ℕ → G → R`
Docstring: Iterated convolution.
English: Let $G$ be a finite abelian group and $R$ a commutative semiring. For $f : G \to R$ and a natural number $n$, $\mathrm{iterConv}(f, n)$ is a function $G \to R$; according to its docstring, it is the iterated convolution.

### `dddconv`
Lean (short): `[Fintype G] [StarRing R] (f : G → R) (g : G → R) (_ : G) : R`
Lean (full): `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [Fintype G] → [inst : CommSemiring R] → [StarRing R] → (G → R) → (G → R) → G → R`
Docstring: Difference convolution
English: Let $G$ be a finite abelian group and $R$ a commutative semiring equipped with a star-ring structure. For $f, g : G \to R$, $\mathrm{dddconv}(f, g)$ is a function $G \to R$; according to its docstring, it is the difference convolution of $f$ and $g$.
