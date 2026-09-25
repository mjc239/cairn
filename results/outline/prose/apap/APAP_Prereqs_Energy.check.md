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
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: when the
prompt shows neither its definition nor a docstring saying it, the English must not supply one. Every variable
needs its type ("$f : G \to \mathbb{C}$", "$m$ a natural number"), every symbol must be introduced (notation such
as $M_{\mathcal B}$ included), and no letter may mean two things. When in doubt, flag it: a false alarm costs one
repair, a missed error stays in the outline. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `energy`
Lean (short): `(n : ℕ) (s : Finset G) (ν : G → ℂ) : ℝ`
Lean (full): `{G : Type u_1} → [AddCommGroup G] → ℕ → Finset G → (G → ℂ) → ℝ`
English: Let $G$ be an abelian group. For a natural number $n$, a finite set $s \subseteq G$ and a function $\nu : G \to \mathbb{C}$, $\mathrm{energy}_n(s, \nu)$ is a real number.

### `boringEnergy`
Lean (short): `(n : ℕ) (s : Finset G) : ℝ`
Lean (full): `{G : Type u_1} → [AddCommGroup G] → [DecidableEq G] → ℕ → Finset G → ℝ`
English: Let $G$ be an abelian group. For a natural number $n$ and a finite set $s \subseteq G$, $\mathrm{boringEnergy}_n(s)$ is a real number.

### `cLpNorm_dft_indicator_one_pow`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (n : ℕ) (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[↑(2 * n)] ^ (2 * n) = boringEnergy n s`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : DecidableEq G] [inst_2 : Fintype G] [inst_3 : MeasurableSpace G] [inst_4 : DiscreteMeasurableSpace G] (n : ℕ) (s : Finset G), cLpNorm (α := AddChar G ℂ) (↑((2 : ℕ) * n)) (dft ((↑s).indicator fun (x : G) => (1 : ℂ))) ^ ((2 : ℕ) * n) = boringEnergy n s`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. For every $n \in \mathbb{N}$ and finite $s \subseteq G$, $\|\widehat{1_s}\|_{2n}^{2n} = \mathrm{boringEnergy}_n(s)$, where $\widehat{1_s}$ is the discrete Fourier transform of the indicator of $s$ and the norm is taken with the compact (expectation) normalisation.

### `cL2Norm_dft_indicator_one`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[2] = √↑s.card`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : Fintype G] [inst_2 : MeasurableSpace G] [inst_3 : DiscreteMeasurableSpace G] (s : Finset G), cLpNorm (α := AddChar G ℂ) (2 : ENNReal) (dft ((↑s).indicator fun (x : G) => (1 : ℂ))) = √↑s.card`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. For every finite $s \subseteq G$, $\|\widehat{1_s}\|_2 = \sqrt{|s|}$, where $\widehat{1_s}$ is the discrete Fourier transform of the indicator of $s$ and the norm has the compact (expectation) normalisation.
