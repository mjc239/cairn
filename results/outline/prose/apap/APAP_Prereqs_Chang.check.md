You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `changConst`
Lean: `ℝ`
English: The real constant $\mathrm{changConst}$ appearing in the bounds of Chang's lemma.

### `AddDissociated.boringEnergy_le`
Lean: `[DiscreteMeasurableSpace G] [Finite G] (hs : AddDissociated ↑s) (n : ℕ) : boringEnergy n s ≤ changConst ^ n * ↑n ^ n * ↑s.card ^ n`
English: Let $G$ be finite and carry the discrete measurable structure. If $s \subseteq G$ is a finite dissociated set, then for every $n \in \mathbb{N}$, $\mathrm{boringEnergy}_n(s) \le \mathrm{changConst}^n \cdot n^n \cdot |s|^n$.

### `general_hoelder`
Lean: `[Fintype G] [DiscreteMeasurableSpace G] (hη : 0 ≤ η) (ν : G → NNReal) (hfν : ∀ (x : G), f x ≠ 0 → 1 ≤ ν x) (hΔ : Δ ⊆ largeSpec f η) (hm : m ≠ 0) : ↑Δ.card ^ (2 * m) * (η ^ (2 * m) * (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2)) ≤ energy m Δ (dft fun a => ↑↑(ν a))`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. Let $\eta \ge 0$, let $\nu : G \to \mathbb{R}_{\ge 0}$ satisfy $1 \le \nu(x)$ whenever $f(x) \ne 0$, let $\Delta \subseteq \operatorname{largeSpec}(f, \eta)$, and let $m \ne 0$. Then $|\Delta|^{2m}\left(\eta^{2m}\,\frac{\|f\|_1^2}{\|f\|_2^2}\right) \le \mathrm{energy}_m(\Delta, \widehat{\nu})$, where $\widehat{\nu}$ is the discrete Fourier transform of $\nu$.

### `spec_hoelder`
Lean: `[Fintype G] [DiscreteMeasurableSpace G] (hη : 0 ≤ η) (hΔ : Δ ⊆ largeSpec f η) (hm : m ≠ 0) : ↑Δ.card ^ (2 * m) * (η ^ (2 * m) * (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))) ≤ boringEnergy m Δ`
English: Let $G$ be a finite abelian group carrying the discrete measurable structure. Let $\eta \ge 0$, $\Delta \subseteq \operatorname{largeSpec}(f, \eta)$ and $m \ne 0$. Then $|\Delta|^{2m}\left(\eta^{2m}\,\frac{\|f\|_1^2/\|f\|_2^2}{|G|}\right) \le \mathrm{boringEnergy}_m(\Delta)$.

### `chang`
Lean: `[Fintype G] [DiscreteMeasurableSpace G] (hf : f ≠ 0) (hη : 0 < η) : ∃ Δ ⊆ largeSpec f η, Δ.card ≤ ⌈changConst * Real.exp 1 * ↑⌈1 + Real.log (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))⁻¹⌉₊ / η ^ 2⌉₊ ∧ largeSpec f η ⊆ Δ.addSpan`
English: (Chang's lemma.) Let $G$ be a finite abelian group carrying the discrete measurable structure. If $f \ne 0$ and $\eta > 0$, then there is a finite set $\Delta \subseteq \operatorname{largeSpec}(f, \eta)$ such that $|\Delta| \le \left\lceil \mathrm{changConst}\cdot e \cdot \left\lceil 1 + \log\Big(1 \big/ \big(\|f\|_1^2 / \|f\|_2^2 / |G|\big)\Big)\right\rceil / \eta^2 \right\rceil$ (both ceilings being natural-number ceilings) and $\operatorname{largeSpec}(f, \eta)$ is contained in the additive span of $\Delta$.
