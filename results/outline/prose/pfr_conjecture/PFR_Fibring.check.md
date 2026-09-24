You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `rdist_of_indep_eq_sum_fibre`
Lean: `[Countable H] [MeasurableSingletonClass H] [Countable H'] [MeasurableSingletonClass H'] (π : H →+ H') [IsProbabilityMeasure μ] (h : IndepFun Z_1 Z_2 μ) (h1 : Measurable Z_1) (h2 : Measurable Z_2) [FiniteRange Z_1] [FiniteRange Z_2] : d[Z_1; μ # Z_2; μ] = d[⇑π ∘ Z_1; μ # ⇑π ∘ Z_2; μ] + d[Z_1 | ⇑π ∘ Z_1 ; μ # Z_2 | ⇑π ∘ Z_2 ; μ] + I[Z_1 - Z_2 : ⟨⇑π ∘ Z_1, ⇑π ∘ Z_2⟩|⇑π ∘ (Z_1 - Z_2);μ]`
English: Let $\pi : H \to H'$ be a homomorphism of additive groups and let $Z_1, Z_2$ be measurable $H$-valued random variables that are independent (with respect to $\mu$). Then $$d[Z_1;Z_2] = d[\pi(Z_1);\pi(Z_2)] + d[Z_1\mid\pi(Z_1);\, Z_2\mid\pi(Z_2)] + I\big[Z_1 - Z_2 : (\pi(Z_1),\pi(Z_2)) \,\big|\, \pi(Z_1 - Z_2)\big].$$

### `sum_of_rdist_eq_step_condMutualInfo`
Lean: `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : I[⟨Y 0 - Y 1, Y 2 - Y 3⟩ : ⟨Y 0 - Y 2, Y 1 - Y 3⟩|Y 0 - Y 1 - (Y 2 - Y 3);μ] = I[Y 0 - Y 1 : Y 1 - Y 3|Y 0 - Y 1 - Y 2 + Y 3;μ]`
English: Let $Y_0, Y_1, Y_2, Y_3$ be measurable $G$-valued random variables. Then $$I\big[(Y_0 - Y_1,\ Y_2 - Y_3) : (Y_0 - Y_2,\ Y_1 - Y_3) \,\big|\, Y_0 - Y_1 - (Y_2 - Y_3)\big] = I\big[Y_0 - Y_1 : Y_1 - Y_3 \,\big|\, Y_0 - Y_1 - Y_2 + Y_3\big].$$

### `sum_of_rdist_eq_step_condRuzsaDist`
Lean: `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] (h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[⟨Y 0, Y 2⟩ | Y 0 - Y 2 ; μ # ⟨Y 1, Y 3⟩ | Y 1 - Y 3 ; μ] = d[Y 0 | Y 0 - Y 2 ; μ # Y 1 | Y 1 - Y 3 ; μ]`
English: Let $Y_0, Y_1, Y_2, Y_3$ be jointly independent measurable $G$-valued random variables. Then $$d\big[(Y_0,Y_2)\mid Y_0 - Y_2;\ (Y_1,Y_3)\mid Y_1 - Y_3\big] = d\big[Y_0 \mid Y_0 - Y_2;\ Y_1\mid Y_1 - Y_3\big].$$

### `sum_of_rdist_eq`
Lean: `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] (Y : Fin 4 → Ω → G) (h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[Y 0; μ # Y 1; μ] + d[Y 2; μ # Y 3; μ] = d[Y 0 - Y 2; μ # Y 1 - Y 3; μ] + d[Y 0 | Y 0 - Y 2 ; μ # Y 1 | Y 1 - Y 3 ; μ] + I[Y 0 - Y 1 : Y 1 - Y 3|Y 0 - Y 1 - Y 2 + Y 3;μ]`
English: Let $Y_0, Y_1, Y_2, Y_3$ be jointly independent measurable $G$-valued random variables. Then $$d[Y_0;Y_1] + d[Y_2;Y_3] = d[Y_0 - Y_2;\ Y_1 - Y_3] + d[Y_0\mid Y_0 - Y_2;\ Y_1 \mid Y_1 - Y_3] + I[Y_0 - Y_1 : Y_1 - Y_3 \mid Y_0 - Y_1 - Y_2 + Y_3].$$

### `sum_of_rdist_eq_char_2`
Lean: `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [Module (ZMod 2) G] (Y : Fin 4 → Ω → G) (h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[Y 0; μ # Y 1; μ] + d[Y 2; μ # Y 3; μ] = d[Y 0 + Y 2; μ # Y 1 + Y 3; μ] + d[Y 0 | Y 0 + Y 2 ; μ # Y 1 | Y 1 + Y 3 ; μ] + I[Y 0 + Y 1 : Y 1 + Y 3|Y 0 + Y 1 + Y 2 + Y 3;μ]`
English: Let $Y_0, Y_1, Y_2, Y_3$ be jointly independent measurable $G$-valued random variables (in the setting of this result $G$ is a group of characteristic $2$, as its name indicates). Then $$d[Y_0;Y_1] + d[Y_2;Y_3] = d[Y_0 + Y_2;\ Y_1 + Y_3] + d[Y_0\mid Y_0 + Y_2;\ Y_1 \mid Y_1 + Y_3] + I[Y_0 + Y_1 : Y_1 + Y_3 \mid Y_0 + Y_1 + Y_2 + Y_3].$$
