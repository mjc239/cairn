You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one. For a definition, name the setting its signature assumes. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

### `rdist_of_indep_eq_sum_fibre`
Lean (short): `[Countable H] [MeasurableSingletonClass H] [Countable H'] [MeasurableSingletonClass H'] (π : H →+ H') [IsProbabilityMeasure μ] (h : IndepFun Z_1 Z_2 μ) (h1 : Measurable Z_1) (h2 : Measurable Z_2) [FiniteRange Z_1] [FiniteRange Z_2] : d[Z_1; μ # Z_2; μ] = d[⇑π ∘ Z_1; μ # ⇑π ∘ Z_2; μ] + d[Z_1 | ⇑π ∘ Z_1 ; μ # Z_2 | ⇑π ∘ Z_2 ; μ] + I[Z_1 - Z_2 : ⟨⇑π ∘ Z_1, ⇑π ∘ Z_2⟩|⇑π ∘ (Z_1 - Z_2);μ]`
Lean (full): `∀ {H : Type u_1} [inst : AddCommGroup H] [inst_1 : Countable H] [hH : MeasurableSpace H] [inst_2 : MeasurableSingletonClass H] {H' : Type u_2} [inst_3 : AddCommGroup H'] [Countable H'] [hH' : MeasurableSpace H'] [MeasurableSingletonClass H'] (π : H →+ H') {Ω : Type u_3} [mΩ : MeasurableSpace Ω] {μ : Measure Ω} [inst_6 : IsProbabilityMeasure μ] {Z_1 Z_2 : Ω → H}, IndepFun Z_1 Z_2 μ → Measurable Z_1 → Measurable Z_2 → ∀ [FiniteRange Z_1] [FiniteRange Z_2], d[Z_1; μ # Z_2; μ] = d[⇑π ∘ Z_1; μ # ⇑π ∘ Z_2; μ] + d[Z_1 | ⇑π ∘ Z_1 ; μ # Z_2 | ⇑π ∘ Z_2 ; μ] + I[Z_1 - Z_2 : ⟨⇑π ∘ Z_1, ⇑π ∘ Z_2⟩|⇑π ∘ (Z_1 - Z_2);μ]`
Docstring: If $Z_1, Z_2$ are independent, then $d[Z_1; Z_2]$ is equal to $$ d[\pi(Z_1);\pi(Z_2)] + d[Z_1|\pi(Z_1); Z_2 |\pi(Z_2)]$$ plus $$I( Z_1 - Z_2 : (\pi(Z_1), \pi(Z_2)) | \pi(Z_1 - Z_2) ).$$
Previous English: Let $H$ and $H'$ be countable additive groups with measurable singletons, let $\pi : H \to H'$ be a homomorphism of additive groups, let $\mu$ be a probability measure, and let $Z_1, Z_2$ be measurable $H$-valued random variables, both of finite range, that are independent with respect to $\mu$. Then $$d[Z_1;Z_2] = d[\pi(Z_1);\pi(Z_2)] + d[Z_1\mid\pi(Z_1);\, Z_2\mid\pi(Z_2)] + I\big[Z_1 - Z_2 : (\pi(Z_1),\pi(Z_2)) \,\big|\, \pi(Z_1 - Z_2)\big],$$ all quantities taken with respect to $\mu$.
Checker's issue: Says 'additive groups' but the Lean requires H and H' to be abelian (AddCommGroup).

### `sum_of_rdist_eq_step_condMutualInfo`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : I[⟨Y 0 - Y 1, Y 2 - Y 3⟩ : ⟨Y 0 - Y 2, Y 1 - Y 3⟩|Y 0 - Y 1 - (Y 2 - Y 3);μ] = I[Y 0 - Y 1 : Y 1 - Y 3|Y 0 - Y 1 - Y 2 + Y 3;μ]`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [Finite G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] {Ω : Type u_2} [mΩ : MeasurableSpace Ω] {μ : Measure Ω} [IsProbabilityMeasure μ] {Y : Fin 4 → Ω → G}, (∀ (i : Fin 4), Measurable (Y i)) → I[⟨Y 0 - Y 1, Y 2 - Y 3⟩ : ⟨Y 0 - Y 2, Y 1 - Y 3⟩|Y 0 - Y 1 - (Y 2 - Y 3);μ] = I[Y 0 - Y 1 : Y 1 - Y 3|Y 0 - Y 1 - Y 2 + Y 3;μ]`
Docstring: The conditional mutual information step of `sum_of_rdist_eq`
Previous English: Let $G$ be a finite additive group with measurable singletons, let $\mu$ be a probability measure, and let $Y_0, Y_1, Y_2, Y_3$ be measurable $G$-valued random variables. Then, with respect to $\mu$, $$I\big[(Y_0 - Y_1,\ Y_2 - Y_3) : (Y_0 - Y_2,\ Y_1 - Y_3) \,\big|\, Y_0 - Y_1 - (Y_2 - Y_3)\big] = I\big[Y_0 - Y_1 : Y_1 - Y_3 \,\big|\, Y_0 - Y_1 - Y_2 + Y_3\big].$$
Checker's issue: Says 'finite additive group' but the Lean requires G to be abelian (AddCommGroup).

### `sum_of_rdist_eq_step_condRuzsaDist`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] (h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[⟨Y 0, Y 2⟩ | Y 0 - Y 2 ; μ # ⟨Y 1, Y 3⟩ | Y 1 - Y 3 ; μ] = d[Y 0 | Y 0 - Y 2 ; μ # Y 1 | Y 1 - Y 3 ; μ]`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : Finite G] [hG : MeasurableSpace G] [inst_2 : MeasurableSingletonClass G] {Ω : Type u_2} [mΩ : MeasurableSpace Ω] {μ : Measure Ω} [inst_3 : IsProbabilityMeasure μ] {Y : Fin 4 → Ω → G}, iIndepFun Y μ → (∀ (i : Fin 4), Measurable (Y i)) → d[⟨Y 0, Y 2⟩ | Y 0 - Y 2 ; μ # ⟨Y 1, Y 3⟩ | Y 1 - Y 3 ; μ] = d[Y 0 | Y 0 - Y 2 ; μ # Y 1 | Y 1 - Y 3 ; μ]`
Docstring: The conditional Ruzsa Distance step of `sum_of_rdist_eq`
Previous English: Let $G$ be a finite additive group with measurable singletons, let $\mu$ be a probability measure, and let $Y_0, Y_1, Y_2, Y_3$ be measurable $G$-valued random variables that are jointly independent with respect to $\mu$. Then, with respect to $\mu$, $$d\big[(Y_0,Y_2)\mid Y_0 - Y_2;\ (Y_1,Y_3)\mid Y_1 - Y_3\big] = d\big[Y_0 \mid Y_0 - Y_2;\ Y_1\mid Y_1 - Y_3\big].$$
Checker's issue: Says 'finite additive group' but the Lean requires G to be abelian (AddCommGroup).

### `sum_of_rdist_eq`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] (Y : Fin 4 → Ω → G) (h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[Y 0; μ # Y 1; μ] + d[Y 2; μ # Y 3; μ] = d[Y 0 - Y 2; μ # Y 1 - Y 3; μ] + d[Y 0 | Y 0 - Y 2 ; μ # Y 1 | Y 1 - Y 3 ; μ] + I[Y 0 - Y 1 : Y 1 - Y 3|Y 0 - Y 1 - Y 2 + Y 3;μ]`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : Finite G] [hG : MeasurableSpace G] [inst_2 : MeasurableSingletonClass G] {Ω : Type u_2} [mΩ : MeasurableSpace Ω] {μ : Measure Ω} [inst_3 : IsProbabilityMeasure μ] (Y : Fin 4 → Ω → G), iIndepFun Y μ → (∀ (i : Fin 4), Measurable (Y i)) → d[Y 0; μ # Y 1; μ] + d[Y 2; μ # Y 3; μ] = d[Y 0 - Y 2; μ # Y 1 - Y 3; μ] + d[Y 0 | Y 0 - Y 2 ; μ # Y 1 | Y 1 - Y 3 ; μ] + I[Y 0 - Y 1 : Y 1 - Y 3|Y 0 - Y 1 - Y 2 + Y 3;μ]`
Docstring: Let $Y_1,Y_2,Y_3$ and $Y_4$ be independent $G$-valued random variables. Then $$d[Y_1-Y_3; Y_2-Y_4] + d[Y_1|Y_1-Y_3; Y_2|Y_2-Y_4] $$ $$ + I[Y_1-Y_2 : Y_2 - Y_4 | Y_1-Y_2-Y_3+Y_4] = d[Y_1; Y_2] + d[Y_3; Y_4].$$
Previous English: Let $G$ be a finite additive group with measurable singletons, let $\mu$ be a probability measure, and let $Y_0, Y_1, Y_2, Y_3$ be measurable $G$-valued random variables that are jointly independent with respect to $\mu$. Then, with respect to $\mu$, $$d[Y_0;Y_1] + d[Y_2;Y_3] = d[Y_0 - Y_2;\ Y_1 - Y_3] + d[Y_0\mid Y_0 - Y_2;\ Y_1 \mid Y_1 - Y_3] + I[Y_0 - Y_1 : Y_1 - Y_3 \mid Y_0 - Y_1 - Y_2 + Y_3].$$
Checker's issue: Says 'finite additive group' but the Lean requires G to be abelian (AddCommGroup).
