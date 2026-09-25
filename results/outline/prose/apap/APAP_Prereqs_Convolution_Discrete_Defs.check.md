You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. A "Project
definitions" section first lists the project notions the statements refer to (statement, docstring, body,
fields). Compare the English with the full statement; anything the English attributes to the docstring must
actually be in it.

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
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: a project
notion's description must agree with its entry under "Project definitions" (statement, docstring, definition body,
fields), and a library notion may only be given its standard mathematical meaning; otherwise flag it. Every variable
needs its type ("$f : G \to \mathbb{C}$", "$m$ a natural number"), every symbol must be introduced, by definition
or by name ("the Ruzsa distance $d[X;Y]$", "the maximal operator $M_{\mathcal B}$"), and no letter may mean two
things. When in doubt, flag it: a false alarm costs one repair, a missed error stays in the outline.
A definition whose body is shown must be described by what it defines (in words or a formula that agrees with the
body), not only by a paraphrase of its docstring. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

## Translations

### `ddconv`
Lean (short): `[Fintype G] (f : G → R) (g : G → R) (_ : G) : R`
Lean (full): `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [Fintype G] → [CommSemiring R] → (G → R) → (G → R) → G → R`
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [Fintype G] [CommSemiring R] (f g : G → R) (a : G) => ∑ x : G × G with x.1 + x.2 = a, f x.1 * g x.2`
Docstring: Convolution
English: Let $G$ be a finite abelian group and $R$ a commutative semiring. For $f, g : G \to R$, $\mathrm{ddconv}(f, g)$ is a function $G \to R$; according to its docstring, it is the convolution of $f$ and $g$.

### `ddconv_eq_sum_sub`
Lean (short): `[Fintype G] (f : G → R) (g : G → R) (a : G) : (f ∗ᵈ g) a = ∑ t, f (a - t) * g t`
Lean (full): `∀ {G : Type u_1} {R : Type u_3} [inst : DecidableEq G] [inst_1 : AddCommGroup G] [inst_2 : Fintype G] [inst_3 : CommSemiring R] (f g : G → R) (a : G), (f ∗ᵈ g) a = ∑ t : G, f (a - t) * g t`
English: Let $G$ be a finite abelian group and $R$ a commutative semiring. For $f, g : G \to R$ and $a \in G$, the discrete convolution satisfies $(f *_d g)(a) = \sum_{t \in G} f(a - t)\, g(t)$.

### `trivChar`
Lean (short): `(_ : G) : R`
Lean (full): `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [CommSemiring R] → G → R`
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [CommSemiring R] (a : G) => if a = (0 : G) then (1 : R) else (0 : R)`
Docstring: The trivial character.
English: Let $G$ be an abelian group and $R$ a commutative semiring. $\mathrm{trivChar}$ is a function $G \to R$; according to its docstring, it is the trivial character.

### `iterConv`
Lean (short): `[Fintype G] (f : G → R) (_ : ℕ) (_ : G) : R`
Lean (full): `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [Fintype G] → [CommSemiring R] → (G → R) → ℕ → G → R`
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [Fintype G] [CommSemiring R] (f : G → R) (x : ℕ) => Nat.brecOn (motive := fun (x : ℕ) => G → R) x (iterConv._f f)`
Docstring: Iterated convolution.
English: Let $G$ be a finite abelian group and $R$ a commutative semiring. For $f : G \to R$ and a natural number $n$, $\mathrm{iterConv}(f, n)$ is a function $G \to R$; according to its docstring, it is the iterated convolution.

### `dddconv`
Lean (short): `[Fintype G] [StarRing R] (f : G → R) (g : G → R) (_ : G) : R`
Lean (full): `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [Fintype G] → [inst : CommSemiring R] → [StarRing R] → (G → R) → (G → R) → G → R`
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [Fintype G] [CommSemiring R] [StarRing R] (f g : G → R) (a : G) => ∑ x : G × G with x.1 - x.2 = a, HMul.hMul (β := R) (f x.1) ((starRingEnd (G → R)) g x.2 : R)`
Docstring: Difference convolution
English: Let $G$ be a finite abelian group and $R$ a commutative semiring equipped with a star-ring structure. For $f, g : G \to R$, $\mathrm{dddconv}(f, g)$ is a function $G \to R$; according to its docstring, it is the difference convolution of $f$ and $g$.
