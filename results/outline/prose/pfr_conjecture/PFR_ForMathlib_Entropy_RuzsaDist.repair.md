You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Keep every
hypothesis the Lean shows, including instance assumptions such as `[Finite G]` or `[IsProbabilityMeasure μ]`
(say them in words: "$G$ is finite", "$\mu$ is a probability measure"), and the exact conclusion. Do not add
claims the Lean does not make. Purely structural instances (e.g. `[AddCommGroup G]`) and implicit arguments are not
shown and may stay implicit.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

### `condRuzsaDist'_eq_sum`
Lean: `[Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass T] (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (μ' : Measure Ω') [IsFiniteMeasure μ'] [FiniteRange W] : d[X ; μ # Y | W ; μ'] = ∑ w ∈ FiniteRange.toFinset W, μ'.real (W ⁻¹' {w}) * d[X; μ # Y; μ'[|W ⁻¹' {w}]]`
Docstring: Explicit formula for conditional Ruzsa distance `d[X ; Y | W]`.
Previous English: Let $Y:\Omega'\to G$ and $W:\Omega'\to T$ be measurable (with $W$ of finite range), and let $\mu,\mu'$ be measures on $\Omega,\Omega'$. Then $d[X;\mu \,\#\, Y|W;\mu'] = \sum_{w\in\mathrm{range}(W)} \mu'(W^{-1}\{w\})\, d[X;\mu \,\#\, Y;\mu'[\,\cdot\mid W^{-1}\{w\}]]$, the sum being over the finite range of $W$.
Checker's issue: The English says only that mu' is a measure, dropping the hypothesis [IsFiniteMeasure mu'].

### `condRuzsaDist'_eq_integral`
Lean: `[Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass T] (X : Ω → G) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (μ' : Measure Ω') [IsFiniteMeasure μ'] [FiniteRange W] : d[X ; μ # Y | W ; μ'] = ∫ (x : T), (fun w => d[X; μ # Y; μ'[|W ⁻¹' {w}]]) x ∂Measure.map W μ'`
Docstring: Explicit formula for conditional Ruzsa distance `d[X ; Y | W]`, in integral form.
Previous English: Let $Y$, $W$ be measurable (with $W$ of finite range), $X:\Omega\to G$, and $\mu,\mu'$ measures. Then $d[X;\mu \,\#\, Y|W;\mu'] = \int_T d[X;\mu \,\#\, Y;\mu'[\,\cdot\mid W^{-1}\{w\}]]\, d(W_*\mu')(w)$.
Checker's issue: The English says only that mu, mu' are measures, dropping the hypothesis [IsFiniteMeasure mu'].

### `kaimanovich_vershik`
Lean: `[Countable G] [MeasurableSingletonClass G] (h : iIndepFun ![X, Y, Z] μ) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [FiniteRange X] [FiniteRange Z] [FiniteRange Y] : H[X + Y + Z; μ] - H[X + Y; μ] ≤ H[Y + Z; μ] - H[Y; μ]`
Docstring: The **Kaimanovich-Vershik inequality**. `H[X + Y + Z] - H[X + Y] ≤ H[Y + Z] - H[Y]`.
Previous English: (Kaimanovich–Vershik inequality.) Let $X,Y,Z$ be measurable random variables on $(\Omega,\mu)$ with values in an abelian group $G$, jointly independent under $\mu$. Then $H[X+Y+Z;\mu] - H[X+Y;\mu] \le H[Y+Z;\mu] - H[Y;\mu]$.
Checker's issue: The English drops the finite-range hypotheses [FiniteRange X], [FiniteRange Y], [FiniteRange Z].

### `comparison_of_ruzsa_distances`
Lean: `(μ : Measure Ω) [Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun Y Z μ') [FiniteRange X] [FiniteRange Z] [FiniteRange Y] : d[X; μ # Y + Z; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z; μ'] - H[Y; μ']) / 2 ∧ ∀ (a : Module (ZMod 2) G), H[Y + Z; μ'] - H[Y; μ'] = d[Y; μ' # Z; μ'] + H[Z; μ'] / 2 - H[Y; μ'] / 2`
Previous English: Let $X$ be measurable on $(\Omega,\mu)$ and $Y,Z$ measurable on $(\Omega',\mu')$ with $Y$ and $Z$ independent under $\mu'$. Then (i) $d[X;\mu \,\#\, Y+Z;\mu'] - d[X;\mu \,\#\, Y;\mu'] \le (H[Y+Z;\mu'] - H[Y;\mu'])/2$, and (ii) for every $\mathbb{Z}/2$-module structure on $G$, $H[Y+Z;\mu'] - H[Y;\mu'] = d[Y;\mu' \,\#\, Z;\mu'] + H[Z;\mu']/2 - H[Y;\mu']/2$.
Checker's issue: The English drops the hypotheses that mu and mu' are probability measures and that X, Y, Z have finite range.

### `condRuzsaDist_diff_le`
Lean: `(μ : Measure Ω) [Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun Y Z μ') [FiniteRange X] [FiniteRange Z] [FiniteRange Y] : d[X; μ # Y + Z; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z; μ'] - H[Y; μ']) / 2`
Docstring: Let `X, Y, Z` be random variables taking values in some abelian group, and with `Y, Z` independent. Then we have `d[X ; Y + Z] - d[X ; Y] ≤ 1/2 (H[Y+ Z] - H[Y])` $$= \tfrac{1}{2} d[Y ; Z] + \tfrac{1}{4} H[Z] - \tfrac{1}{4} H[Y]$$ and $$d[X ; Y|Y+ Z] - d[X ; Y] \leq \tfrac{1}{2} \bigl(H[Y+ Z] - H[Z]\bigr)$$ $$= \tfrac{1}{2} d[Y ; Z] + \tfrac{1}{4} H[Y] - \tfrac{1}{4} H[Z]$$
Previous English: Let $X$ be measurable on $(\Omega,\mu)$ and $Y,Z$ measurable $G$-valued variables on $(\Omega',\mu')$ with $Y$ and $Z$ independent under $\mu'$. Then $d[X;\mu \,\#\, Y+Z;\mu'] - d[X;\mu \,\#\, Y;\mu'] \le (H[Y+Z;\mu'] - H[Y;\mu'])/2$.
Checker's issue: The English drops the hypotheses that mu and mu' are probability measures and that X, Y, Z have finite range.

### `condRuzsaDist_of_copy`
Lean: `[Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass S] [MeasurableSingletonClass T] (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (hX' : Measurable X') (hZ' : Measurable Z') (hY' : Measurable Y') (hW' : Measurable W') [IsFiniteMeasure μ] [IsFiniteMeasure μ'] [IsFiniteMeasure μ''] [IsFiniteMeasure μ'''] (h1 : IdentDistrib (⟨X, Z⟩) (⟨X', Z'⟩) μ μ'') (h2 : IdentDistrib (⟨Y, W⟩) (⟨Y', W'⟩) μ' μ''') [FiniteRange Z] [FiniteRange W] [FiniteRange Z'] [FiniteRange W'] : d[X | Z ; μ # Y | W ; μ'] = d[X' | Z' ; μ'' # Y' | W' ; μ''']`
Docstring: The conditional Ruzsa distance is unchanged if the sets of random variables are replaced with copies.
Previous English: Let $X,Z,Y,W,X',Z',Y',W'$ be measurable, and suppose $(X,Z)$ under $\mu$ has the same distribution as $(X',Z')$ under $\mu''$, and $(Y,W)$ under $\mu'$ has the same distribution as $(Y',W')$ under $\mu'''$. Then $d[X|Z;\mu \,\#\, Y|W;\mu'] = d[X'|Z';\mu'' \,\#\, Y'|W';\mu''']$.
Checker's issue: The English drops the finite-measure hypotheses on mu, mu', mu'', mu''' and the finite-range hypotheses on Z, W, Z', W'.

### `condRuzsaDist_of_indep`
Lean: `[Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) [IsProbabilityMeasure μ] (h : IndepFun (⟨X, Z⟩) (⟨Y, W⟩) μ) [FiniteRange Z] [FiniteRange W] : d[X | Z ; μ # Y | W ; μ] = H[X - Y | ⟨Z, W⟩ ; μ] - H[X | Z ; μ] / 2 - H[Y | W ; μ] / 2`
Docstring: If `$(X,Z)$` and `$(Y,W)$` are independent, then `d[X | Z ; Y | W] = H[X'- Y' | Z', W'] - H[X'|Z']/2 - H[Y'|W']/2`.
Previous English: Let $X,Z,Y,W$ be measurable random variables on $(\Omega,\mu)$ such that $(X,Z)$ and $(Y,W)$ are independent under $\mu$. Then $d[X|Z;\mu \,\#\, Y|W;\mu] = H[X-Y \mid (Z,W);\mu] - H[X|Z;\mu]/2 - H[Y|W;\mu]/2$.
Checker's issue: The English drops the hypotheses that mu is a probability measure and that Z and W have finite range.

### `condRuzsaDist_le`
Lean: `(μ : Measure Ω) (μ' : Measure Ω') [Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) [FiniteRange X] [FiniteRange Z] [FiniteRange Y] [FiniteRange W] : d[X | Z ; μ # Y | W ; μ'] ≤ d[X; μ # Y; μ'] + I[X : Z ; μ] / 2 + I[Y : W ; μ'] / 2`
Docstring: Suppose that $(X, Z)$ and $(Y, W)$ are random variables, where $X, Y$ take values in an abelian group. Then $$d[X | Z ; Y | W] \leq d[X ; Y] + \tfrac{1}{2} I[X : Z] + \tfrac{1}{2} I[Y : W]$$
Previous English: Let $X,Z$ be measurable on $(\Omega,\mu)$ and $Y,W$ measurable on $(\Omega',\mu')$, with $X,Y$ valued in an abelian group. Then $d[X|Z;\mu \,\#\, Y|W;\mu'] \le d[X;\mu \,\#\, Y;\mu'] + I[X:Z;\mu]/2 + I[Y:W;\mu']/2$.
Checker's issue: The English drops the hypotheses that mu and mu' are probability measures and that X, Z, Y, W have finite range.

### `condRuzsaDist_of_const`
Lean: `[Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] (hX : Measurable X) (Y : Ω' → G) (W : Ω' → T) (c : S) [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] [FiniteRange W] : d[X | fun x => c ; μ # Y | W ; μ'] = d[X ; μ # Y | W ; μ']`
Docstring: Conditioning by a constant does not affect Ruzsa distance.
Previous English: Let $X$ be measurable, $Y:\Omega'\to G$, $W:\Omega'\to T$ and $c\in S$. Then conditioning on the constant variable $c$ does not change the distance: $d[X \mid c;\mu \,\#\, Y|W;\mu'] = d[X;\mu \,\#\, Y|W;\mu']$.
Checker's issue: The English drops the hypotheses that mu and mu' are probability measures and that W has finite range.

### `condRuzsaDist_diff_ofsum_le`
Lean: `(μ : Measure Ω) [Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (hZ' : Measurable Z') (h : iIndepFun ![Y, Z, Z'] μ') [FiniteRange X] [FiniteRange Z] [FiniteRange Y] [FiniteRange Z'] : d[X ; μ # Y + Z | Y + Z + Z' ; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z + Z'; μ'] + H[Y + Z; μ'] - H[Y; μ'] - H[Z'; μ']) / 2`
Previous English: Let $X$ be measurable on $(\Omega,\mu)$ and $Y,Z,Z'$ measurable on $(\Omega',\mu')$, jointly independent under $\mu'$. Then $d[X;\mu \,\#\, Y+Z \mid Y+Z+Z';\mu'] - d[X;\mu \,\#\, Y;\mu'] \le (H[Y+Z+Z';\mu'] + H[Y+Z;\mu'] - H[Y;\mu'] - H[Z';\mu'])/2$.
Checker's issue: The English drops the hypotheses that mu and mu' are probability measures and that X, Y, Z, Z' have finite range.

### `ent_of_diff_le`
Lean: `[Countable G] [MeasurableSingletonClass G] (X : Ω → G) (Y : Ω → G) (Z : Ω → G) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun (⟨X, Y⟩) Z μ) [IsProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : H[X - Y; μ] ≤ H[X - Z; μ] + H[Z - Y; μ] - H[Z; μ]`
Docstring: The **improved entropic Ruzsa triangle inequality**.
Previous English: (Improved entropic Ruzsa triangle inequality.) Let $X,Y,Z:\Omega\to G$ be measurable with $(X,Y)$ and $Z$ independent under $\mu$. Then $H[X-Y;\mu] \le H[X-Z;\mu] + H[Z-Y;\mu] - H[Z;\mu]$.
Checker's issue: The English drops the hypotheses that mu is a probability measure and that X, Y, Z have finite range.

### `rdist_triangle`
Lean: `[Countable G] [MeasurableSingletonClass G] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] [IsProbabilityMeasure μ''] [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : d[X; μ # Z; μ''] ≤ d[X; μ # Y; μ'] + d[Y; μ' # Z; μ'']`
Docstring: The **entropic Ruzsa triangle inequality**
Previous English: (Entropic Ruzsa triangle inequality.) Let $X$, $Y$, $Z$ be measurable $G$-valued random variables on $(\Omega,\mu)$, $(\Omega',\mu')$, $(\Omega'',\mu'')$ respectively. Then $d[X;\mu \,\#\, Z;\mu''] \le d[X;\mu \,\#\, Y;\mu'] + d[Y;\mu' \,\#\, Z;\mu'']$.
Checker's issue: The English drops the hypotheses that mu, mu', mu'' are probability measures and that X, Y, Z have finite range.

### `condRuzsaDist_eq_sum`
Lean: `[Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass S] [MeasurableSingletonClass T] (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) [IsFiniteMeasure μ] (μ' : Measure Ω') [IsFiniteMeasure μ'] [FiniteRange Z] [FiniteRange W] : d[X | Z ; μ # Y | W ; μ'] = ∑ z ∈ FiniteRange.toFinset Z, ∑ w ∈ FiniteRange.toFinset W, μ.real (Z ⁻¹' {z}) * μ'.real (W ⁻¹' {w}) * d[X; μ[|Z ⁻¹' {z}] # Y; μ'[|W ⁻¹' {w}]]`
Docstring: Explicit formula for conditional Ruzsa distance $d[X|Z; Y|W]$.
Previous English: Let $X,Z,Y,W$ be measurable (with $Z,W$ of finite range) and $\mu,\mu'$ measures. Then $d[X|Z;\mu \,\#\, Y|W;\mu'] = \sum_{z\in\mathrm{range}(Z)}\sum_{w\in\mathrm{range}(W)} \mu(Z^{-1}\{z\})\,\mu'(W^{-1}\{w\})\, d[X;\mu[\,\cdot\mid Z^{-1}\{z\}] \,\#\, Y;\mu'[\,\cdot\mid W^{-1}\{w\}]]$.
Checker's issue: The English says only that mu, mu' are measures, dropping the hypotheses [IsFiniteMeasure mu] and [IsFiniteMeasure mu'].

### `condRuzsaDist'_of_copy`
Lean: `[Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass T] (X : Ω → G) (hY : Measurable Y) (hW : Measurable W) (X' : Ω'' → G) (hY' : Measurable Y') (hW' : Measurable W') [IsFiniteMeasure μ'] [IsFiniteMeasure μ'''] (h1 : IdentDistrib X X' μ μ'') (h2 : IdentDistrib (⟨Y, W⟩) (⟨Y', W'⟩) μ' μ''') [FiniteRange W] [FiniteRange W'] : d[X ; μ # Y | W ; μ'] = d[X' ; μ'' # Y' | W' ; μ''']`
Previous English: Let $X:\Omega\to G$, $X':\Omega''\to G$, and let $Y,W,Y',W'$ be measurable. If $X$ under $\mu$ has the same distribution as $X'$ under $\mu''$, and $(Y,W)$ under $\mu'$ has the same distribution as $(Y',W')$ under $\mu'''$, then $d[X;\mu \,\#\, Y|W;\mu'] = d[X';\mu'' \,\#\, Y'|W';\mu''']$.
Checker's issue: The English drops the finite-measure hypotheses on mu' and mu''' and the finite-range hypotheses on W and W'.

### `condRuzsaDist_of_inj_map`
Lean: `[Countable G] [MeasurableSingletonClass G] [Countable G'] [MeasurableSingletonClass G'] [IsProbabilityMeasure μ] (Y : Fin 4 → Ω → G) (h_indep : IndepFun (⟨Y 0, Y 2⟩) (⟨Y 1, Y 3⟩) μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) (π : G × G →+ G') (hπ : ∀ (h : G), Function.Injective fun g => π (g, h)) [FiniteRange (Y 2)] [FiniteRange (Y 3)] : d[⇑π ∘ ⟨Y 0, Y 2⟩ | Y 2 ; μ # ⇑π ∘ ⟨Y 1, Y 3⟩ | Y 3 ; μ] = d[Y 0 | Y 2 ; μ # Y 1 | Y 3 ; μ]`
Previous English: Let $Y_0,Y_1,Y_2,Y_3:\Omega\to G$ be measurable with $(Y_0,Y_2)$ and $(Y_1,Y_3)$ independent under $\mu$, and let $\pi:G\times G\to G'$ be an additive group homomorphism such that $g\mapsto\pi(g,h)$ is injective for every $h\in G$. Then $d[\pi(Y_0,Y_2) \mid Y_2;\mu \,\#\, \pi(Y_1,Y_3)\mid Y_3;\mu] = d[Y_0|Y_2;\mu \,\#\, Y_1|Y_3;\mu]$.
Checker's issue: The English drops the hypotheses that mu is a probability measure and that Y 2 and Y 3 have finite range.

### `condRuzsaDist'_of_inj_map`
Lean: `[Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [Module (ZMod 2) G] (hX : Measurable X) (hB : Measurable B) (hC : Measurable C) (h_indep : IndepFun X (⟨B, C⟩) μ) [FiniteRange X] [FiniteRange B] [FiniteRange C] : d[X ; μ # B | B + C ; μ] = d[X ; μ # C | B + C ; μ]`
Previous English: Let $X,B,C:\Omega\to G$ be measurable with $X$ independent of $(B,C)$ under $\mu$. Then $d[X;\mu \,\#\, B \mid B+C;\mu] = d[X;\mu \,\#\, C\mid B+C;\mu]$.
Checker's issue: The English drops the characteristic-2 hypothesis [Module (ZMod 2) G], as well as the probability-measure and finite-range hypotheses.

### `condRuzsaDist'_of_inj_map'`
Lean: `[Countable G] [MeasurableSingletonClass G] [Module (ZMod 2) G] [IsProbabilityMeasure μ] [IsProbabilityMeasure μ''] (hA : Measurable A) (hB : Measurable B) (hC : Measurable C) [FiniteRange A] [FiniteRange B] [FiniteRange C] : d[A ; μ'' # B | B + C ; μ] = d[A ; μ'' # C | B + C ; μ]`
Previous English: Let $A$ (on $(\Omega'',\mu'')$), $B$ and $C$ (on $(\Omega,\mu)$) be measurable. Then $d[A;\mu'' \,\#\, B\mid B+C;\mu] = d[A;\mu''\,\#\, C\mid B+C;\mu]$.
Checker's issue: The English drops the characteristic-2 hypothesis [Module (ZMod 2) G], as well as the probability-measure and finite-range hypotheses.

### `rdist_add_const`
Lean: `[Countable G] [MeasurableSingletonClass G] [FiniteRange X] [FiniteRange Y] [IsZeroOrProbabilityMeasure μ] [IsZeroOrProbabilityMeasure μ'] (hX : Measurable X) (hY : Measurable Y) : d[X; μ # Y + fun x => c; μ'] = d[X; μ # Y; μ']`
Docstring: Adding a constant to a random variable does not change the Rusza distance.
Previous English: Let $X,Y$ be measurable and $c\in G$. Then $d[X;\mu \,\#\, Y+c;\mu'] = d[X;\mu \,\#\, Y;\mu']$: adding a constant to a random variable does not change the Ruzsa distance.
Checker's issue: The English drops the hypotheses that X and Y have finite range and that mu and mu' are zero-or-probability measures.

### `continuous_rdist_restrict_probabilityMeasure`
Lean: `[Finite G] [DiscreteTopology G] [BorelSpace G] : Continuous fun μ => d[id; ↑μ.1 # id; ↑μ.2]`
Docstring: Ruzsa distance depends continuously on the measure.
Previous English: On pairs $(\mu_1,\mu_2)$ of probability measures on $G$ (with the topology of the space of probability measures), the map $(\mu_1,\mu_2)\mapsto d[\mathrm{id};\mu_1 \,\#\, \mathrm{id};\mu_2]$ is continuous.
Checker's issue: The English drops the hypothesis [Finite G] (and the discrete topology on G).

### `diff_ent_le_rdist`
Lean: `[Countable G] [MeasurableSingletonClass G] [FiniteRange X] [FiniteRange Y] [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] (hX : Measurable X) (hY : Measurable Y) : |H[X; μ] - H[Y; μ']| ≤ 2 * d[X; μ # Y; μ']`
Docstring: `|H[X] - H[Y]| ≤ 2 d[X ; Y]`.
Previous English: Let $X,Y$ be measurable. Then $|H[X;\mu] - H[Y;\mu']| \le 2\, d[X;\mu \,\#\, Y;\mu']$.
Checker's issue: The English drops the hypotheses that mu and mu' are probability measures and that X and Y have finite range.

### `ent_bsg`
Lean: `[Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] (hA : Measurable A) (hB : Measurable B) [Finite G] : ∫ (x : G), (fun z => d[A; μ[|(A + B) ⁻¹' {z}] # B; μ[|(A + B) ⁻¹' {z}]]) x ∂Measure.map (A + B) μ ≤ 3 * I[A : B ; μ] + 2 * H[A + B; μ] - H[A; μ] - H[B; μ]`
Docstring: The **entropic Balog-Szemerédi-Gowers inequality**. Let `A, B` be `G`-valued random variables on `Ω`, and set `Z := A+B`. Then `∑ z, P[Z=z] d[(A | Z = z) ; (B | Z = z)] ≤ 3 I[A :B] + 2 H[Z] - H[A] - H[B].` TODO: remove the hypothesis of `Fintype G` from here and from `condIndep_copies'`
Previous English: (Entropic Balog–Szemerédi–Gowers inequality.) Let $A,B:\Omega\to G$ be measurable (with $G$ finite) and $Z=A+B$. Then $\int_G d[A;\mu[\,\cdot\mid Z^{-1}\{z\}] \,\#\, B;\mu[\,\cdot\mid Z^{-1}\{z\}]]\, d(Z_*\mu)(z) \le 3\,I[A:B;\mu] + 2\,H[A+B;\mu] - H[A;\mu] - H[B;\mu]$.
Checker's issue: The English drops the hypothesis that mu is a probability measure.
