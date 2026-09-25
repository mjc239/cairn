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

### `unbalancing`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (p : ℕ) (hp : p ≠ 0) (ε : ℝ) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (f : G → ℝ) (g : G → ℂ) (h : G → ℂ) (hf : g ○ᵈ g = Complex.ofReal ∘ f) (hh : h ○ᵈ h = mu Finset.univ) (hε : ε ≤ ‖f‖_[↑p, mu Finset.univ]) : ∃ p', ↑p' ≤ 2 ^ 10 * ε⁻¹ ^ 2 * ↑p ∧ 1 + ε / 2 ≤ ‖f + 1‖_[↑p', mu Finset.univ]`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G] (p : ℕ), p ≠ 0 → ∀ (ε : ℝ), 0 < ε → ε ≤ 1 → ∀ (f : G → ℝ) (g h : G → ℂ), g ○ᵈ g = Complex.ofReal ∘ f → h ○ᵈ h = mu Finset.univ → ε ≤ ‖f‖_[↑p, mu Finset.univ] → ∃ p', ↑p' ≤ 2 ^ 10 * ε⁻¹ ^ 2 * ↑p ∧ 1 + ε / 2 ≤ ‖f + 1‖_[↑p', mu Finset.univ]`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. Let $p \in \mathbb{N}$ with $p \ne 0$, $0 < \varepsilon \le 1$, $f : G \to \mathbb{R}$ and $g, h : G \to \mathbb{C}$ with $g \circ g = f$ (viewed as complex-valued) and $h \circ h = \mu_G$, and suppose $\varepsilon \le \|f\|_{p,\mu_G}$. Then there is $p' \in \mathbb{N}$ with $p' \le 2^{10}\varepsilon^{-2} p$ and $1 + \varepsilon/2 \le \|f + 1\|_{p',\mu_G}$. Here $\circ$ is the discrete difference convolution, $\mu_G$ is the normalised indicator of the whole group, and $\|\cdot\|_{q,\mu_G}$ is the $L^q$ norm weighted by $\mu_G$.
