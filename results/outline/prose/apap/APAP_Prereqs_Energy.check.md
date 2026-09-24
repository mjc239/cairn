You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `energy`
Lean: `(n : ℕ) (s : Finset G) (ν : G → ℂ) : ℝ`
English: For $n \in \mathbb{N}$, a finite set $s \subseteq G$ and a weight $\nu : G \to \mathbb{C}$, defines the real number $\mathrm{energy}_n(s, \nu)$, a weighted $n$-fold additive energy of $s$.

### `boringEnergy`
Lean: `(n : ℕ) (s : Finset G) : ℝ`
English: For $n \in \mathbb{N}$ and a finite set $s \subseteq G$, defines the real number $\mathrm{boringEnergy}_n(s)$, the unweighted $n$-fold additive energy of $s$.

### `cLpNorm_dft_indicator_one_pow`
Lean: `[Fintype G] [DiscreteMeasurableSpace G] (n : ℕ) (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[↑(2 * n)] ^ (2 * n) = boringEnergy n s`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. For every $n \in \mathbb{N}$ and finite $s \subseteq G$, $\|\widehat{1_s}\|_{2n}^{2n} = \mathrm{boringEnergy}_n(s)$, where $\widehat{1_s}$ is the discrete Fourier transform of the indicator of $s$ and the norm is taken with the compact (expectation) normalisation.

### `cL2Norm_dft_indicator_one`
Lean: `[Fintype G] [DiscreteMeasurableSpace G] (s : Finset G) : ‖dft ((↑s).indicator fun x => 1)‖ₙ_[2] = √↑s.card`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. For every finite $s \subseteq G$, $\|\widehat{1_s}\|_2 = \sqrt{|s|}$, where $\widehat{1_s}$ is the discrete Fourier transform of the indicator of $s$ and the norm has the compact (expectation) normalisation.
