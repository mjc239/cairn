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

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `trivChar` (def)
Lean: `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [CommSemiring R] → G → R`
Docstring: The trivial character.
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [CommSemiring R] (a : G) => if a = (0 : G) then (1 : R) else (0 : R)`

#### `MeasureTheory.cLpNorm` (def)
Lean: `{α : Type u_1} → {E : Type u_4} → [MeasurableSpace α] → [NormedAddCommGroup E] → ENNReal → (α → E) → ℝ`
Docstring: The Lp norm of a function with the compact normalisation.
Definition: `fun {α : Type u_1} {E : Type u_4} [inst : MeasurableSpace α] [NormedAddCommGroup E] (p : ENNReal) (f : α → E) => lpNorm (m0 := inst) f p (ProbabilityTheory.uniformOn Set.univ)`

#### `dft` (def)
Lean: `{G : Type u_1} → [inst : AddCommGroup G] → [Fintype G] → (G → ℂ) → AddChar G ℂ → ℂ`
Docstring: The discrete Fourier transform.
Definition: `fun {G : Type u_1} [AddCommGroup G] [Fintype G] (f : G → ℂ) (ψ : AddChar G ℂ) => ⟪⇑ψ, f⟫_[ℂ]`

## Translations

### `energy`
Lean (short): `(n : ℕ) (s : Finset G) (ν : G → ℂ) : ℝ`
Lean (full): `{G : Type u_1} → [AddCommGroup G] → ℕ → Finset G → (G → ℂ) → ℝ`
Definition: `fun {G : Type u_1} [AddCommGroup G] (n : ℕ) (s : Finset G) (ν : G → ℂ) => ∑ γ ∈ Fintype.piFinset (δ := fun (x : Fin n) => G) fun (x : Fin n) => s, ∑ δ ∈ Fintype.piFinset (δ := fun (x : Fin n) => G) fun (x : Fin n) => s, ‖ν (HSub.hSub (α := G) (∑ i : Fin n, γ i) (∑ i : Fin n, δ i))‖`
English: Let $G$ be an abelian group. For a natural number $n$, a finite set $s \subseteq G$ and a function $\nu : G \to \mathbb{C}$, $\mathrm{energy}_n(s, \nu)$ is a real number.

### `boringEnergy`
Lean (short): `(n : ℕ) (s : Finset G) : ℝ`
Lean (full): `{G : Type u_1} → [AddCommGroup G] → [DecidableEq G] → ℕ → Finset G → ℝ`
Definition: `fun {G : Type u_1} [AddCommGroup G] [DecidableEq G] (n : ℕ) (s : Finset G) => energy n s trivChar`
English: Let $G$ be an abelian group. For a natural number $n$ and a finite set $s \subseteq G$, $\mathrm{boringEnergy}_n(s)$ is a real number.

### `cLpNorm_dft_indicator_one_pow`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (n : ℕ) (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[↑(2 * n)] ^ (2 * n) = boringEnergy n s`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : DecidableEq G] [inst_2 : Fintype G] [inst_3 : MeasurableSpace G] [inst_4 : DiscreteMeasurableSpace G] (n : ℕ) (s : Finset G), cLpNorm (α := AddChar G ℂ) (↑((2 : ℕ) * n)) (dft ((↑s).indicator fun (x : G) => (1 : ℂ))) ^ ((2 : ℕ) * n) = boringEnergy n s`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. For every $n \in \mathbb{N}$ and finite $s \subseteq G$, $\|\widehat{1_s}\|_{2n}^{2n} = \mathrm{boringEnergy}_n(s)$, where $\widehat{1_s}$ is the discrete Fourier transform of the indicator of $s$ and the norm is taken with the compact (expectation) normalisation.

### `cL2Norm_dft_indicator_one`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[2] = √↑s.card`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : Fintype G] [inst_2 : MeasurableSpace G] [inst_3 : DiscreteMeasurableSpace G] (s : Finset G), cLpNorm (α := AddChar G ℂ) (2 : ENNReal) (dft ((↑s).indicator fun (x : G) => (1 : ℂ))) = √↑s.card`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. For every finite $s \subseteq G$, $\|\widehat{1_s}\|_2 = \sqrt{|s|}$, where $\widehat{1_s}$ is the discrete Fourier transform of the indicator of $s$ and the norm has the compact (expectation) normalisation.
