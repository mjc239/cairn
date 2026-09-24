You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Keep every
hypothesis the Lean shows, including instance assumptions such as `[Finite G]` or `[IsProbabilityMeasure μ]`
(say them in words: "$G$ is finite", "$\mu$ is a probability measure"), and the exact conclusion. Do not add
claims the Lean does not make. Purely structural instances (e.g. `[AddCommGroup G]`) and implicit arguments are not
shown and may stay implicit.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

### `general_hoelder`
Lean: `[Fintype G] [DiscreteMeasurableSpace G] (hη : 0 ≤ η) (ν : G → NNReal) (hfν : ∀ (x : G), f x ≠ 0 → 1 ≤ ν x) (hΔ : Δ ⊆ largeSpec f η) (hm : m ≠ 0) : ↑Δ.card ^ (2 * m) * (η ^ (2 * m) * (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2)) ≤ energy m Δ (dft fun a => ↑↑(ν a))`
Previous English: $G$ carries the discrete measurable structure. Let $\eta \ge 0$, let $\nu : G \to \mathbb{R}_{\ge 0}$ satisfy $1 \le \nu(x)$ whenever $f(x) \ne 0$, let $\Delta \subseteq \operatorname{largeSpec}(f, \eta)$, and let $m \ne 0$. Then $|\Delta|^{2m}\left(\eta^{2m}\,\frac{\|f\|_1^2}{\|f\|_2^2}\right) \le \mathrm{energy}_m(\Delta, \widehat{\nu})$, where $\widehat{\nu}$ is the discrete Fourier transform of $\nu$.
Checker's issue: The English omits the [Fintype G] hypothesis that G is finite.

### `spec_hoelder`
Lean: `[Fintype G] [DiscreteMeasurableSpace G] (hη : 0 ≤ η) (hΔ : Δ ⊆ largeSpec f η) (hm : m ≠ 0) : ↑Δ.card ^ (2 * m) * (η ^ (2 * m) * (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))) ≤ boringEnergy m Δ`
Previous English: $G$ carries the discrete measurable structure. Let $\eta \ge 0$, $\Delta \subseteq \operatorname{largeSpec}(f, \eta)$ and $m \ne 0$. Then $|\Delta|^{2m}\left(\eta^{2m}\,\frac{\|f\|_1^2/\|f\|_2^2}{|G|}\right) \le \mathrm{boringEnergy}_m(\Delta)$.
Checker's issue: The English omits the [Fintype G] hypothesis that G is finite (it only uses |G|).

### `chang`
Lean: `[Fintype G] [DiscreteMeasurableSpace G] (hf : f ≠ 0) (hη : 0 < η) : ∃ Δ ⊆ largeSpec f η, Δ.card ≤ ⌈changConst * Real.exp 1 * ↑⌈1 + Real.log (‖f‖_[1] ^ 2 / ‖f‖_[2] ^ 2 / ↑(Fintype.card G))⁻¹⌉₊ / η ^ 2⌉₊ ∧ largeSpec f η ⊆ Δ.addSpan`
Docstring: **Chang's lemma**.
Previous English: (Chang's lemma.) Suppose $G$ carries the discrete measurable structure. If $f \ne 0$ and $\eta > 0$, then there is a finite set $\Delta \subseteq \operatorname{largeSpec}(f, \eta)$ such that $|\Delta| \le \left\lceil \mathrm{changConst}\cdot e \cdot \left\lceil 1 + \log\Big(1 \big/ \big(\|f\|_1^2 / \|f\|_2^2 / |G|\big)\Big)\right\rceil / \eta^2 \right\rceil$ (both ceilings being natural-number ceilings) and $\operatorname{largeSpec}(f, \eta)$ is contained in the additive span of $\Delta$.
Checker's issue: The English omits the [Fintype G] hypothesis that G is finite.
