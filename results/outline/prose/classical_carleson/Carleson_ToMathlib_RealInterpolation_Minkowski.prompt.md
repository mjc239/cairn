You are writing the text of a mathematical outline generated from a verified Lean formalisation.
Below are the results of one chapter, in the order the outline presents them. For each you get its Lean name, its
statement in Lean (only explicit hypotheses are shown; implicit and type-class assumptions are omitted), its
docstring if there is one, and, for theorems, the named results its proof uses (with their statements) and the
helper lemmas folded into the proof.

Write:
1. `title`: a short chapter title (at most 8 words), as a mathematician would name this material.
2. For every result, `statement`: the statement in clear mathematical English, using LaTeX between $...$ for
   formulas. Be faithful: keep every hypothesis and the exact conclusion; do not add, drop, strengthen or weaken
   anything. If some notation's meaning is unclear, keep the notation rather than guessing. For a definition, say
   what is being defined.
3. For every theorem, `sketch`: one or two sentences on how the proof goes, based only on the listed results it
   uses and their statements. Do not invent steps; if the structure is not clear, just say which results it
   combines.

Reply with only a JSON object:
{"title": "...", "results": {"<lean name>": {"statement": "...", "sketch": "..."}}}
(omit "sketch" for definitions). Use every Lean name exactly as given.

Namespaces open (prefixes omitted): TileStructure, MeasureTheory, Antichain.

## Chapter (Lean module `Carleson.ToMathlib.RealInterpolation.Minkowski`)

### `MeasureTheory.estimate_trnc₁` (theorem)
Lean: `(ht : t ∈ Set.Ioo 0 1) (hp₀ : 0 < p₀) (hq₀ : 0 < q₀) (hp₁ : 0 < p₁) (hq₁ : 0 < q₁) (hpq : sel j p₀ p₁ ≤ sel j q₀ q₁) (hp' : sel j p₀ p₁ ≠ ⊤) (hq' : sel j q₀ q₁ ≠ ⊤) (hp₀p₁ : p₀ < p₁) (hq₀q₁ : q₀ ≠ q₁) (hp : p⁻¹ = (1 - t) * p₀⁻¹ + t * p₁⁻¹) (hq : q⁻¹ = (1 - t) * q₀⁻¹ + t * q₁⁻¹) (hf : AEStronglyMeasurable f μ) (hf₂ : SigmaFinite (μ.restrict (Function.support fun x => ‖f x‖ₑ))) (hspf : spf.σ = ComputationsChoiceExponent.ζ p₀ q₀ p₁ q₁ t.toReal) : ∫⁻ (s : ℝ) in Set.Ioi 0, eLpNorm (trnc j f ((spf_to_tc spf).ton (ENNReal.ofReal s))) (sel j p₀ p₁) μ ^ (sel j q₀ q₁).toReal * ENNReal.ofReal (s ^ (q.to…`
Docstring: One of the key estimates for the real interpolation theorem, now using the particular choice of exponent, but not yet using the particular choice of scale in the `ScaledPowerFunction`.
Proof uses:
- `MeasureTheory.estimate_trnc`: `(hp₀ : 0 < p₀) (hq₀ : 0 < q₀) (hp₀q₀ : p₀ ≤ q₀) (hf : AEStronglyMeasurable f μ) (hf₂ : SigmaFinite (μ.restrict (Function.support fun x => ‖f x‖ₑ))) (hpowers : if (j ^^ (spf_to_tc spf).mon) = true the…`
Helper lemmas folded into the proof: `ComputationsChoiceExponent.inv_toReal_iff`, `ComputationsChoiceExponent.ζ`, `ComputationsChoiceExponent.ζ_equality₁`, `ComputationsChoiceExponent.ζ_equality₃`, `ComputationsChoiceExponent.ζ_equality₅`, `ComputationsChoiceExponent.ζ_equality₆`, `ComputationsChoiceExponent.ζ_le_zero_iff_of_lt₀`, `ComputationsChoiceExponent.ζ_le_zero_iff_of_lt₁`

### `MeasureTheory.estimate_trnc` (theorem)
Lean: `(hp₀ : 0 < p₀) (hq₀ : 0 < q₀) (hp₀q₀ : p₀ ≤ q₀) (hf : AEStronglyMeasurable f μ) (hf₂ : SigmaFinite (μ.restrict (Function.support fun x => ‖f x‖ₑ))) (hpowers : if (j ^^ (spf_to_tc spf).mon) = true then q₀ < q else q < q₀) (hpow_pos : 0 < q₀ + spf.σ⁻¹ * (q - q₀)) : ∫⁻ (s : ℝ) in Set.Ioi 0, eLpNorm (trnc j f ((spf_to_tc spf).ton (ENNReal.ofReal s))) (ENNReal.ofReal p₀) μ ^ q₀ * ENNReal.ofReal (s ^ (q - q₀ - 1)) ≤ spf.d ^ (q - q₀) * ENNReal.ofReal |q - q₀|⁻¹ * (∫⁻ (a : α) in Function.support fun x => ‖f x‖ₑ, ‖f a‖ₑ ^ (p₀ + spf.σ⁻¹ * (q - q₀) * (p₀ / q₀)) ∂μ) ^ (p₀⁻¹ * q₀)`
Docstring: One of the key estimates for the real interpolation theorem, not yet using the particular choice of exponent and scale in the `ScaledPowerFunction`.
Helper lemmas folded into the proof: `ENNReal.div_lt_div`, `ENNReal.eq_of_le_of_le`, `ENNReal.le_of_rpow_le`, `ENNReal.map_toReal_ae_eq_map_toReal_comap_ofReal`, `ENNReal.map_toReal_eq_map_toReal_comap_ofReal`, `ENNReal.map_toReal_eq_map_toReal_comap_ofReal'`, `ENNReal.ofNNReal_preimage`, `ENNReal.rpow_add_of_pos`
