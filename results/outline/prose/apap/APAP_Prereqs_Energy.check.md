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
naturally. Definitions are held to the same standard: the English must name the setting the signature assumes
("for an abelian group $G$ and …, $\mathrm{rdist}$ is …"). Replacing an assumption by a stronger one (a metric
space where the Lean has a pseudometric space) is unfaithful too. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `energy`
Lean (short): `(n : ℕ) (s : Finset G) (ν : G → ℂ) : ℝ`
Lean (full): `{G : Type u_1} → [AddCommGroup G] → ℕ → Finset G → (G → ℂ) → ℝ`
English: For $n \in \mathbb{N}$, a finite set $s \subseteq G$ and a weight $\nu : G \to \mathbb{C}$, defines the real number $\mathrm{energy}_n(s, \nu)$, a weighted $n$-fold additive energy of $s$.

### `boringEnergy`
Lean (short): `(n : ℕ) (s : Finset G) : ℝ`
Lean (full): `{G : Type u_1} → [AddCommGroup G] → [DecidableEq G] → ℕ → Finset G → ℝ`
English: For $n \in \mathbb{N}$ and a finite set $s \subseteq G$, defines the real number $\mathrm{boringEnergy}_n(s)$, the unweighted $n$-fold additive energy of $s$.

### `cLpNorm_dft_indicator_one_pow`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (n : ℕ) (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[↑(2 * n)] ^ (2 * n) = boringEnergy n s`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : DecidableEq G] [inst_2 : Fintype G] [inst_3 : MeasurableSpace G] [inst_4 : DiscreteMeasurableSpace G] (n : ℕ) (s : Finset G), ‖dft ((↑s).indicator fun x => (1 : ℂ))‖ₙ_[↑((2 : ℕ) * n)] ^ ((2 : ℕ) * n) = boringEnergy n s`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. For every $n \in \mathbb{N}$ and finite $s \subseteq G$, $\|\widehat{1_s}\|_{2n}^{2n} = \mathrm{boringEnergy}_n(s)$, where $\widehat{1_s}$ is the discrete Fourier transform of the indicator of $s$ and the norm is taken with the compact (expectation) normalisation.

### `cL2Norm_dft_indicator_one`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[2] = √↑s.card`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : Fintype G] [inst_2 : MeasurableSpace G] [inst_3 : DiscreteMeasurableSpace G] (s : Finset G), ‖dft ((↑s).indicator fun x => (1 : ℂ))‖ₙ_[(2 : ENNReal)] = √↑s.card`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. For every finite $s \subseteq G$, $\|\widehat{1_s}\|_2 = \sqrt{|s|}$, where $\widehat{1_s}$ is the discrete Fourier transform of the indicator of $s$ and the norm has the compact (expectation) normalisation.
