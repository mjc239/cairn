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
Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `boringEnergy` (def)
Lean: `{G : Type u_1} → [AddCommGroup G] → [DecidableEq G] → ℕ → Finset G → ℝ`
Definition: `fun {G : Type u_1} [AddCommGroup G] [DecidableEq G] (n : ℕ) (s : Finset G) => energy n s trivChar`

#### `MeasureTheory.dLpNorm` (def)
Lean: `{α : Type u_1} → {E : Type u_4} → [MeasurableSpace α] → [NormedAddCommGroup E] → ENNReal → (α → E) → ℝ`
Docstring: The Lp norm of a function with the compact normalisation.
Definition: `fun {α : Type u_1} {E : Type u_4} [inst : MeasurableSpace α] [NormedAddCommGroup E] (p : ENNReal) (f : α → E) => lpNorm (m0 := inst) f p Measure.count`

#### `dft` (def)
Lean: `{G : Type u_1} → [inst : AddCommGroup G] → [Fintype G] → (G → ℂ) → AddChar G ℂ → ℂ`
Docstring: The discrete Fourier transform.
Definition: `fun {G : Type u_1} [AddCommGroup G] [Fintype G] (f : G → ℂ) (ψ : AddChar G ℂ) => ⟪⇑ψ, f⟫_[ℂ]`

#### `energy` (def)
Lean: `{G : Type u_1} → [AddCommGroup G] → ℕ → Finset G → (G → ℂ) → ℝ`
Definition: `fun {G : Type u_1} [AddCommGroup G] (n : ℕ) (s : Finset G) (ν : G → ℂ) => ∑ γ ∈ Fintype.piFinset (δ := fun (x : Fin n) => G) fun (x : Fin n) => s, ∑ δ ∈ Fintype.piFinset (δ := fun (x : Fin n) => G) fun (x : Fin n) => s, ‖ν (HSub.hSub (α := G) (∑ i : Fin n, γ i) (∑ i : Fin n, δ i))‖`

#### `largeSpec` (def)
Lean: `{G : Type u_1} → [inst : AddCommGroup G] → [Fintype G] → [MeasurableSpace G] → (G → ℂ) → ℝ → Finset (AddChar G ℂ)`
Docstring: The `η`-large spectrum of a function.
Definition: `fun {G : Type u_1} [AddCommGroup G] [Fintype G] [MeasurableSpace G] (f : G → ℂ) (η : ℝ) => {ψ : AddChar G ℂ | η * ‖f‖_[(1 : ENNReal)] ≤ ‖dft f ψ‖}`

#### `trivChar` (def)
Lean: `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [CommSemiring R] → G → R`
Docstring: The trivial character.
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [CommSemiring R] (a : G) => if a = (0 : G) then (1 : R) else (0 : R)`

## Translations

### `changConst`
Lean: `ℝ`
English: $\mathrm{changConst}$ is a fixed real constant (a real number).

### `AddDissociated.boringEnergy_le`
Lean (short): `[DiscreteMeasurableSpace G] [Finite G] (hs : AddDissociated ↑s) (n : ℕ) : boringEnergy n s ≤ changConst ^ n * ↑n ^ n * ↑s.card ^ n`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : MeasurableSpace G] [DiscreteMeasurableSpace G] [inst_3 : DecidableEq G] [Finite G] {s : Finset G}, AddDissociated ↑s → ∀ (n : ℕ), boringEnergy n s ≤ changConst ^ n * HPow.hPow (α := ℝ) (↑n) n * HPow.hPow (α := ℝ) (↑s.card) n`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. If $s \subseteq G$ is a finite dissociated set, then for every $n \in \mathbb{N}$, $\mathrm{boringEnergy}_n(s) \le \mathrm{changConst}^n \cdot n^n \cdot |s|^n$.

### `general_hoelder`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hη : 0 ≤ η) (ν : G → NNReal) (hfν : ∀ (x : G), f x ≠ 0 → 1 ≤ ν x) (hΔ : Δ ⊆ largeSpec f η) (hm : m ≠ 0) : ↑Δ.card ^ (2 * m) * (η ^ (2 * m) * (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2)) ≤ energy m Δ (dft fun a => ↑↑(ν a))`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {f : G → ℂ} {η : ℝ} {Δ : Finset (AddChar G ℂ)} {m : ℕ} [inst_1 : Fintype G] [inst_2 : MeasurableSpace G] [DiscreteMeasurableSpace G], (0 : ℝ) ≤ η → ∀ (ν : G → NNReal), (∀ (x : G), f x ≠ (0 : ℂ) → (1 : NNReal) ≤ ν x) → Δ ⊆ largeSpec f η → m ≠ (0 : ℕ) → HPow.hPow (α := ℝ) (↑Δ.card) ((2 : ℕ) * m) * (η ^ ((2 : ℕ) * m) * (‖f‖_[(1 : ENNReal)] ^ (2 : ℕ) / ‖f‖_[(2 : ENNReal)] ^ (2 : ℕ))) ≤ energy m Δ (dft fun (a : G) => ↑↑(ν a))`
English: Let $G$ be a finite additive commutative group equipped with a measurable space structure that is discrete (every subset is measurable). Let $f : G \to \mathbb{C}$, let $\eta \in \mathbb{R}$ with $\eta \ge 0$, let $\Delta$ be a finite set of additive characters $G \to \mathbb{C}$, and let $m$ be a natural number with $m \ne 0$. Let $\nu : G \to \mathbb{R}_{\ge 0}$ satisfy $1 \le \nu(x)$ for every $x \in G$ with $f(x) \ne 0$, and suppose $\Delta \subseteq \operatorname{largeSpec}(f, \eta)$. Then $|\Delta|^{2m}\left(\eta^{2m}\,\frac{\|f\|_1^2}{\|f\|_2^2}\right) \le \operatorname{energy}_m(\Delta, \widehat{\nu})$, where $\|f\|_1, \|f\|_2$ are the $L^1$ and $L^2$ norms of $f$ and $\widehat{\nu} = \operatorname{dft}(\nu)$ is the discrete Fourier transform of $\nu$ viewed as a complex-valued function.

### `spec_hoelder`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hη : 0 ≤ η) (hΔ : Δ ⊆ largeSpec f η) (hm : m ≠ 0) : ↑Δ.card ^ (2 * m) * (η ^ (2 * m) * (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))) ≤ boringEnergy m Δ`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {f : G → ℂ} {η : ℝ} {Δ : Finset (AddChar G ℂ)} {m : ℕ} [inst_1 : Fintype G] [inst_2 : MeasurableSpace G] [DiscreteMeasurableSpace G], (0 : ℝ) ≤ η → Δ ⊆ largeSpec f η → m ≠ (0 : ℕ) → HPow.hPow (α := ℝ) (↑Δ.card) ((2 : ℕ) * m) * (η ^ ((2 : ℕ) * m) * (‖f‖_[(1 : ENNReal)] ^ (2 : ℕ) / ‖f‖_[(2 : ENNReal)] ^ (2 : ℕ) / ↑(Fintype.card G))) ≤ boringEnergy m Δ`
English: Let $G$ be a finite additive commutative group equipped with a measurable space structure that is discrete (every subset is measurable). Let $f : G \to \mathbb{C}$, let $\eta \in \mathbb{R}$ with $\eta \ge 0$, let $\Delta$ be a finite set of additive characters $G \to \mathbb{C}$ with $\Delta \subseteq \operatorname{largeSpec}(f, \eta)$, and let $m$ be a natural number with $m \ne 0$. Then $|\Delta|^{2m}\left(\eta^{2m}\,\frac{\|f\|_1^2/\|f\|_2^2}{|G|}\right) \le \operatorname{boringEnergy}_m(\Delta)$, where $\|f\|_1, \|f\|_2$ are the $L^1$ and $L^2$ norms of $f$ and $|G|$ is the cardinality of $G$.

### `chang`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hf : f ≠ 0) (hη : 0 < η) : ∃ Δ ⊆ largeSpec f η, Δ.card ≤ ⌈changConst * Real.exp 1 * ↑⌈1 + Real.log (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))⁻¹⌉₊ / η ^ 2⌉₊ ∧ largeSpec f η ⊆ Δ.addSpan`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {f : G → ℂ} {η : ℝ} [inst_1 : Fintype G] [inst_2 : MeasurableSpace G] [DiscreteMeasurableSpace G], f ≠ (0 : G → ℂ) → (0 : ℝ) < η → ∃ Δ ⊆ largeSpec f η, Δ.card ≤ ⌈changConst * Real.exp (1 : ℝ) * ↑⌈(1 : ℝ) + Real.log (‖f‖_[(1 : ENNReal)] ^ (2 : ℕ) / ‖f‖_[(2 : ENNReal)] ^ (2 : ℕ) / ↑(Fintype.card G))⁻¹⌉₊ / η ^ (2 : ℕ)⌉₊ ∧ largeSpec f η ⊆ Δ.addSpan`
Docstring: **Chang's lemma**.
English: (Chang's lemma.) Let $G$ be a finite additive commutative group equipped with a measurable space structure that is discrete (every subset is measurable). Let $f : G \to \mathbb{C}$ with $f \ne 0$ and let $\eta \in \mathbb{R}$ with $\eta > 0$. Then there is a finite set $\Delta$ of additive characters $G \to \mathbb{C}$ with $\Delta \subseteq \operatorname{largeSpec}(f, \eta)$ such that $|\Delta| \le \left\lceil \mathrm{changConst}\cdot e \cdot \left\lceil 1 + \log\Big(\big(\|f\|_1^2 / \|f\|_2^2 / |G|\big)^{-1}\Big)\right\rceil / \eta^2 \right\rceil$ (both ceilings being natural-number ceilings, $e = \exp(1)$, $\|f\|_1, \|f\|_2$ the $L^1$ and $L^2$ norms of $f$, and $|G|$ the cardinality of $G$) and $\operatorname{largeSpec}(f, \eta) \subseteq \operatorname{addSpan}(\Delta)$.
