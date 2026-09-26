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
Definition: `(32 : ℝ) * Real.exp (1 : ℝ)`
English: $\mathrm{changConst}$ is a fixed real constant (a real number).

### `AddDissociated.boringEnergy_le`
Lean (short): `[DiscreteMeasurableSpace G] [Finite G] (hs : AddDissociated ↑s) (n : ℕ) : boringEnergy n s ≤ changConst ^ n * ↑n ^ n * ↑s.card ^ n`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : MeasurableSpace G] [DiscreteMeasurableSpace G] [inst_3 : DecidableEq G] [Finite G] {s : Finset G}, AddDissociated ↑s → ∀ (n : ℕ), boringEnergy n s ≤ changConst ^ n * HPow.hPow (α := ℝ) (↑n) n * HPow.hPow (α := ℝ) (↑s.card) n`
English: Let $G$ be a finite additive commutative group equipped with a measurable space structure that is discrete (every subset is measurable). Let $s\subseteq G$ be a finite set that is dissociated (in the additive sense: distinct subsets of $s$ have distinct sums). For $n\in\mathbb N$ let $\mathrm{boringEnergy}_n(s)=\operatorname{energy}_n(s,\mathbf 1_{\{0\}})=\sum_{\gamma\in s^n}\sum_{\delta\in s^n}\big|\mathbf 1_{\{0\}}\big(\sum_{i<n}\gamma_i-\sum_{i<n}\delta_i\big)\big|$, where $\mathbf 1_{\{0\}}:G\to\mathbb C$ is the trivial character `trivChar` ($1$ at $0$ and $0$ elsewhere); thus $\mathrm{boringEnergy}_n(s)$ is the number of pairs $(\gamma,\delta)$ of $n$-tuples in $s^n$ with $\sum_i\gamma_i=\sum_i\delta_i$. Let $\mathrm{changConst}=32e\in\mathbb R$. Then for every $n\in\mathbb N$, $\mathrm{boringEnergy}_n(s)\le\mathrm{changConst}^n\cdot n^n\cdot|s|^n$ (in $\mathbb R$, with $|s|$ the cardinality of $s$).

### `general_hoelder`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hη : 0 ≤ η) (ν : G → NNReal) (hfν : ∀ (x : G), f x ≠ 0 → 1 ≤ ν x) (hΔ : Δ ⊆ largeSpec f η) (hm : m ≠ 0) : ↑Δ.card ^ (2 * m) * (η ^ (2 * m) * (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2)) ≤ energy m Δ (dft fun a => ↑↑(ν a))`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {f : G → ℂ} {η : ℝ} {Δ : Finset (AddChar G ℂ)} {m : ℕ} [inst_1 : Fintype G] [inst_2 : MeasurableSpace G] [DiscreteMeasurableSpace G], (0 : ℝ) ≤ η → ∀ (ν : G → NNReal), (∀ (x : G), f x ≠ (0 : ℂ) → (1 : NNReal) ≤ ν x) → Δ ⊆ largeSpec f η → m ≠ (0 : ℕ) → HPow.hPow (α := ℝ) (↑Δ.card) ((2 : ℕ) * m) * (η ^ ((2 : ℕ) * m) * (‖f‖_[(1 : ENNReal)] ^ (2 : ℕ) / ‖f‖_[(2 : ENNReal)] ^ (2 : ℕ))) ≤ energy m Δ (dft fun (a : G) => ↑↑(ν a))`
English: Let $G$ be a finite additive commutative group equipped with a measurable space structure that is discrete (every subset is measurable). Let $f:G\to\mathbb C$, let $\eta\in\mathbb R$ with $\eta\ge0$, let $\Delta$ be a finite set of additive characters $G\to\mathbb C$, and let $m$ be a natural number with $m\ne0$. Let $\nu:G\to\mathbb R_{\ge0}$ satisfy $1\le\nu(x)$ for every $x\in G$ with $f(x)\ne0$, and suppose $\Delta\subseteq\operatorname{largeSpec}(f,\eta)$. Then $$|\Delta|^{2m}\Big(\eta^{2m}\,\frac{\|f\|_1^2}{\|f\|_2^2}\Big)\le\operatorname{energy}_m(\Delta,\widehat{\nu}),$$ where $\widehat\nu$ is the discrete Fourier transform of $\nu$ viewed as a complex-valued function. Here, for $h:G\to\mathbb C$, $\|h\|_1=\sum_{x\in G}|h(x)|$ and $\|h\|_2=\big(\sum_{x\in G}|h(x)|^2\big)^{1/2}$ are the $L^1$ and $L^2$ norms with respect to counting measure on $G$ (`dLpNorm`, by its docstring the $L^p$ norm with the compact normalisation). For $h:G\to\mathbb C$ and an additive character $\psi:G\to\mathbb C$, $\widehat h(\psi)=\langle\psi,h\rangle$ is the discrete Fourier transform of $h$ (`dft`), the inner product of $\psi$ and $h$ as functions on $G$ (`⟪ψ, h⟫_[ℂ]`). For $h:G\to\mathbb C$ and $\eta\in\mathbb R$, $\operatorname{largeSpec}(h,\eta)$ (by its docstring, the $\eta$-large spectrum) is the finite set of additive characters $\psi:G\to\mathbb C$ with $\eta\,\|h\|_1\le|\widehat h(\psi)|$. For $m\in\mathbb N$, a finite set $\Delta$ of additive characters and $\nu':\widehat G\to\mathbb C$, where $\widehat G$ is the group of additive characters $G\to\mathbb C$ (written additively), $\operatorname{energy}_m(\Delta,\nu')=\sum_{\gamma\in\Delta^m}\sum_{\delta\in\Delta^m}\big|\nu'\big(\sum_{i<m}\gamma_i-\sum_{i<m}\delta_i\big)\big|$. 

### `spec_hoelder`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hη : 0 ≤ η) (hΔ : Δ ⊆ largeSpec f η) (hm : m ≠ 0) : ↑Δ.card ^ (2 * m) * (η ^ (2 * m) * (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))) ≤ boringEnergy m Δ`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {f : G → ℂ} {η : ℝ} {Δ : Finset (AddChar G ℂ)} {m : ℕ} [inst_1 : Fintype G] [inst_2 : MeasurableSpace G] [DiscreteMeasurableSpace G], (0 : ℝ) ≤ η → Δ ⊆ largeSpec f η → m ≠ (0 : ℕ) → HPow.hPow (α := ℝ) (↑Δ.card) ((2 : ℕ) * m) * (η ^ ((2 : ℕ) * m) * (‖f‖_[(1 : ENNReal)] ^ (2 : ℕ) / ‖f‖_[(2 : ENNReal)] ^ (2 : ℕ) / ↑(Fintype.card G))) ≤ boringEnergy m Δ`
English: Let $G$ be a finite additive commutative group equipped with a measurable space structure that is discrete (every subset is measurable). Let $f:G\to\mathbb C$, let $\eta\in\mathbb R$ with $\eta\ge0$, let $\Delta$ be a finite set of additive characters $G\to\mathbb C$ with $\Delta\subseteq\operatorname{largeSpec}(f,\eta)$, and let $m$ be a natural number with $m\ne0$. Then $$|\Delta|^{2m}\Big(\eta^{2m}\,\frac{\|f\|_1^2/\|f\|_2^2}{|G|}\Big)\le\operatorname{boringEnergy}_m(\Delta),$$ where $|G|$ is the cardinality of $G$. Here, for $h:G\to\mathbb C$, $\|h\|_1=\sum_{x\in G}|h(x)|$ and $\|h\|_2=\big(\sum_{x\in G}|h(x)|^2\big)^{1/2}$ are the $L^1$ and $L^2$ norms with respect to counting measure on $G$ (`dLpNorm`, by its docstring the $L^p$ norm with the compact normalisation). For $h:G\to\mathbb C$ and an additive character $\psi:G\to\mathbb C$, $\widehat h(\psi)=\langle\psi,h\rangle$ is the discrete Fourier transform of $h$ (`dft`), the inner product of $\psi$ and $h$ as functions on $G$ (`⟪ψ, h⟫_[ℂ]`). For $h:G\to\mathbb C$ and $\eta\in\mathbb R$, $\operatorname{largeSpec}(h,\eta)$ (by its docstring, the $\eta$-large spectrum) is the finite set of additive characters $\psi:G\to\mathbb C$ with $\eta\,\|h\|_1\le|\widehat h(\psi)|$. For $m\in\mathbb N$, a finite set $\Delta$ of additive characters and $\nu':\widehat G\to\mathbb C$, where $\widehat G$ is the group of additive characters $G\to\mathbb C$ (written additively), $\operatorname{energy}_m(\Delta,\nu')=\sum_{\gamma\in\Delta^m}\sum_{\delta\in\Delta^m}\big|\nu'\big(\sum_{i<m}\gamma_i-\sum_{i<m}\delta_i\big)\big|$; and $\operatorname{boringEnergy}_m(\Delta)=\operatorname{energy}_m(\Delta,\mathbf 1_{\{0\}})$, where $\mathbf 1_{\{0\}}$ is the trivial character `trivChar` (value $1$ at $0$ and $0$ elsewhere), i.e. the number of pairs $(\gamma,\delta)\in\Delta^m\times\Delta^m$ with $\sum_i\gamma_i=\sum_i\delta_i$. 

### `chang`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hf : f ≠ 0) (hη : 0 < η) : ∃ Δ ⊆ largeSpec f η, Δ.card ≤ ⌈changConst * Real.exp 1 * ↑⌈1 + Real.log (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))⁻¹⌉₊ / η ^ 2⌉₊ ∧ largeSpec f η ⊆ Δ.addSpan`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] {f : G → ℂ} {η : ℝ} [inst_1 : Fintype G] [inst_2 : MeasurableSpace G] [DiscreteMeasurableSpace G], f ≠ (0 : G → ℂ) → (0 : ℝ) < η → ∃ Δ ⊆ largeSpec f η, Δ.card ≤ ⌈changConst * Real.exp (1 : ℝ) * ↑⌈(1 : ℝ) + Real.log (‖f‖_[(1 : ENNReal)] ^ (2 : ℕ) / ‖f‖_[(2 : ENNReal)] ^ (2 : ℕ) / ↑(Fintype.card G))⁻¹⌉₊ / η ^ (2 : ℕ)⌉₊ ∧ largeSpec f η ⊆ Δ.addSpan`
Docstring: **Chang's lemma**.
English: (Chang's lemma.) Let $G$ be a finite additive commutative group equipped with a measurable space structure that is discrete (every subset is measurable). Let $f:G\to\mathbb C$ with $f\ne0$ and let $\eta\in\mathbb R$ with $\eta>0$. Then there is a finite set $\Delta$ of additive characters $G\to\mathbb C$ with $\Delta\subseteq\operatorname{largeSpec}(f,\eta)$ such that $$|\Delta|\le\left\lceil\frac{\mathrm{changConst}\cdot e\cdot\left\lceil 1+\log\Big(\big(\|f\|_1^2/\|f\|_2^2/|G|\big)^{-1}\Big)\right\rceil}{\eta^2}\right\rceil$$ and $\operatorname{largeSpec}(f,\eta)\subseteq\operatorname{addSpan}(\Delta)$. Here both ceilings are natural-number ceilings (negative reals round up to $0$), $e=\exp(1)$, $\mathrm{changConst}=32e\in\mathbb R$, $|G|$ is the cardinality of $G$, and $\operatorname{addSpan}(\Delta)$ is the set of all sums $\sum_{\psi\in\Delta}\varepsilon_\psi\,\psi$ with each $\varepsilon_\psi\in\{-1,0,1\}$, computed in the group of additive characters of $G$ (written additively). Here, for $h:G\to\mathbb C$, $\|h\|_1=\sum_{x\in G}|h(x)|$ and $\|h\|_2=\big(\sum_{x\in G}|h(x)|^2\big)^{1/2}$ are the $L^1$ and $L^2$ norms with respect to counting measure on $G$ (`dLpNorm`, by its docstring the $L^p$ norm with the compact normalisation). For $h:G\to\mathbb C$ and an additive character $\psi:G\to\mathbb C$, $\widehat h(\psi)=\langle\psi,h\rangle$ is the discrete Fourier transform of $h$ (`dft`), the inner product of $\psi$ and $h$ as functions on $G$ (`⟪ψ, h⟫_[ℂ]`). For $h:G\to\mathbb C$ and $\eta\in\mathbb R$, $\operatorname{largeSpec}(h,\eta)$ (by its docstring, the $\eta$-large spectrum) is the finite set of additive characters $\psi:G\to\mathbb C$ with $\eta\,\|h\|_1\le|\widehat h(\psi)|$. 
