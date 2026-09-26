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

#### `dddconv` (def)
Lean: `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [Fintype G] → [inst : CommSemiring R] → [StarRing R] → (G → R) → (G → R) → G → R`
Docstring: Difference convolution
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [Fintype G] [CommSemiring R] [StarRing R] (f g : G → R) (a : G) => ∑ x : G × G with x.1 - x.2 = a, HMul.hMul (β := R) (f x.1) ((starRingEnd (G → R)) g x.2 : R)`

#### `mu` (def)
Lean: `{K : Type u_1} → {α : Type u_3} → [DivisionSemiring K] → Finset α → α → K`
Docstring: The normalised indicator_one of a set.
Definition: `fun {K : Type u_1} {α : Type u_3} [DivisionSemiring K] (s : Finset α) => HSMul.hSMul (α := K) (β := α → K) (↑s.card)⁻¹ ((↑s).indicator fun (x : α) => (1 : K))`

#### `wLpNorm` (def)
Lean: `{α : Type u_1} → {E : Type u_3} → [MeasurableSpace α] → [NormedAddCommGroup E] → ENNReal → (α → NNReal) → (α → E) → ℝ`
Docstring: The weighted Lp norm of a function.
Definition: `fun {α : Type u_1} {E : Type u_3} [inst : MeasurableSpace α] [NormedAddCommGroup E] (p : ENNReal) (w : α → NNReal) (f : α → E) => lpNorm (m0 := inst) f p (Measure.sum fun (i : α) => HSMul.hSMul (β := Measure α) (w i) (Measure.dirac i))`

## Translations

### `unbalancing`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (p : ℕ) (hp : p ≠ 0) (ε : ℝ) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (f : G → ℝ) (g : G → ℂ) (h : G → ℂ) (hf : g ○ᵈ g = Complex.ofReal ∘ f) (hh : h ○ᵈ h = mu Finset.univ) (hε : ε ≤ ‖f‖_[↑p, mu Finset.univ]) : ∃ p', ↑p' ≤ 2 ^ 10 * ε⁻¹ ^ 2 * ↑p ∧ 1 + ε / 2 ≤ ‖f + 1‖_[↑p', mu Finset.univ]`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G] (p : ℕ), p ≠ (0 : ℕ) → ∀ (ε : ℝ), (0 : ℝ) < ε → ε ≤ (1 : ℝ) → ∀ (f : G → ℝ) (g h : G → ℂ), g ○ᵈ g = Complex.ofReal ∘ f → h ○ᵈ h = mu Finset.univ → ε ≤ ‖f‖_[↑p, mu Finset.univ] → ∃ (p' : ℕ), ↑p' ≤ (2 : ℝ) ^ (10 : ℕ) * ε⁻¹ ^ (2 : ℕ) * ↑p ∧ (1 : ℝ) + ε / (2 : ℝ) ≤ ‖f + (1 : G → ℝ)‖_[↑p', mu Finset.univ]`
Docstring: The unbalancing step. Note that we do the physical proof in order to avoid the Fourier transform.
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. Let $p \in \mathbb{N}$ with $p \ne 0$, $0 < \varepsilon \le 1$, $f : G \to \mathbb{R}$ and $g, h : G \to \mathbb{C}$ with $g \circ g = f$ (viewed as complex-valued) and $h \circ h = \mu_G$, and suppose $\varepsilon \le \|f\|_{p,\mu_G}$. Then there is $p' \in \mathbb{N}$ with $p' \le 2^{10}\varepsilon^{-2} p$ and $1 + \varepsilon/2 \le \|f + 1\|_{p',\mu_G}$. Here $\circ$ is the discrete difference convolution, $\mu_G$ is the normalised indicator of the whole group, and $\|\cdot\|_{q,\mu_G}$ is the $L^q$ norm weighted by $\mu_G$.
