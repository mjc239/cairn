You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Keep every
hypothesis the Lean shows, including instance assumptions such as `[Finite G]` or `[IsProbabilityMeasure μ]`
(say them in words: "$G$ is finite", "$\mu$ is a probability measure"), and the exact conclusion. Do not add
claims the Lean does not make. Purely structural instances (e.g. `[AddCommGroup G]`) and implicit arguments are not
shown and may stay implicit.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): TileStructure, MeasureTheory, Antichain.

### `MeasureTheory.estimate_trnc₁`
Lean: `(ht : t ∈ Set.Ioo 0 1) (hp₀ : 0 < p₀) (hq₀ : 0 < q₀) (hp₁ : 0 < p₁) (hq₁ : 0 < q₁) (hpq : sel j p₀ p₁ ≤ sel j q₀ q₁) (hp' : sel j p₀ p₁ ≠ ⊤) (hq' : sel j q₀ q₁ ≠ ⊤) (hp₀p₁ : p₀ < p₁) (hq₀q₁ : q₀ ≠ q₁) (hp : p⁻¹ = (1 - t) * p₀⁻¹ + t * p₁⁻¹) (hq : q⁻¹ = (1 - t) * q₀⁻¹ + t * q₁⁻¹) (hf : AEStronglyMeasurable f μ) (hf₂ : SigmaFinite (μ.restrict (Function.support fun x => ‖f x‖ₑ))) (hspf : spf.σ = ComputationsChoiceExponent.ζ p₀ q₀ p₁ q₁ t.toReal) : ∫⁻ (s : ℝ) in Set.Ioi 0, eLpNorm (trnc j f ((spf_to_tc spf).ton (ENNReal.ofReal s))) (sel j p₀ p₁) μ ^ (sel j q₀ q₁).toReal * ENNReal.ofReal (s ^ (q.toReal - (sel j q₀ q₁).toReal - 1)) ≤ spf.d ^ (q.toReal - (sel j q₀ q₁).toReal) * ENNReal.ofReal |q.toReal - (sel j q₀ q₁).toReal|⁻¹ * (eLpNorm f p μ ^ p.toReal) ^ ((sel j p₀ p₁).toReal⁻¹ * (sel j q₀ q₁).toReal)`
Docstring: One of the key estimates for the real interpolation theorem, now using the particular choice of exponent, but not yet using the particular choice of scale in the `ScaledPowerFunction`.
Previous English: Let $t \in (0,1)$, $p_0, q_0, p_1, q_1 > 0$, and write $\mathrm{sel}\ j$ for the selection of the $j$-indexed exponent. Assume $\mathrm{sel}\ j\ p_0\ p_1 \le \mathrm{sel}\ j\ q_0\ q_1$, both of these are finite, $p_0 < p_1$, $q_0 \ne q_1$, $p^{-1} = (1-t)p_0^{-1} + t p_1^{-1}$, $q^{-1} = (1-t)q_0^{-1} + t q_1^{-1}$, $f$ is $\mu$-a.e. strongly measurable, $\mu$ restricted to the support of $\|f\|$ is $\sigma$-finite, and the exponent $\mathrm{spf}.\sigma$ of the scaled power function $\mathrm{spf}$ equals $\zeta(p_0, q_0, p_1, q_1, t)$. Then the integral $\int_0^\infty \|\mathrm{trnc}_j(f, \mathrm{ton}(s))\|_{L^{\mathrm{sel}\,j\,p_0\,p_1}(\mu)}^{\mathrm{sel}\,j\,q_0\,q_1} \cdot s^{(q \ldots)}\, ds$ (where $\mathrm{ton}$ is the truncation scale determined by $\mathrm{spf}$) is bounded by an explicit expression; the rest of the statement is truncated in the source.
Checker's issue: The English claims the Lean statement is truncated, but it is complete, and the English omits the integrand's power of s and the entire right-hand side spf.d^(q - sel j q₀ q₁) * |q - sel j q₀ q₁|⁻¹ * (‖f‖_p^p)^(sel j q₀ q₁ / sel j p₀ p₁).
