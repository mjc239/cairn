You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `condRuzsaDist`
Lean: `[Countable G] [MeasurableSingletonClass G] (X : Ω → G) (Z : Ω → S) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) [IsFiniteMeasure μ] (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) [IsFiniteMeasure μ'] : ℝ`
English: For random variables $X:\Omega\to G$, $Z:\Omega\to S$ on $(\Omega,\mu)$ and $Y:\Omega'\to G$, $W:\Omega'\to T$ on $(\Omega',\mu')$, with $G$ an abelian group, the conditional Ruzsa distance $d[X|Z \,;\, Y|W]$ (with respect to $\mu,\mu'$) is the kernel Ruzsa distance between the conditional distribution of $X$ given $Z$ and that of $Y$ given $W$, averaged against the laws of $Z$ and $W$.

### `condRuzsaDist'`
Lean: `[Countable G] [MeasurableSingletonClass G] (X : Ω → G) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist'._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist'._auto_3) [IsFiniteMeasure μ'] : ℝ`
English: For $X:\Omega\to G$ on $(\Omega,\mu)$ and $Y:\Omega'\to G$, $W:\Omega'\to T$ on $(\Omega',\mu')$, the conditional Ruzsa distance $d[X \,;\, Y|W]$ (with respect to $\mu,\mu'$) is the kernel Ruzsa distance between the (constant) law of $X$ and the conditional distribution of $Y$ given $W$, averaged against the law of $W$.

### `rdist`
Lean: `(X : Ω → G) (Y : Ω' → G) (μ : autoParam (Measure Ω) rdist._auto_1) (μ' : autoParam (Measure Ω') rdist._auto_3) : ℝ`
English: For $X:\Omega\to G$ on $(\Omega,\mu)$ and $Y:\Omega'\to G$ on $(\Omega',\mu')$, the Ruzsa distance $d[X;\mu \,\#\, Y;\mu']$ is $H[X'-Y'] - H[X']/2 - H[Y']/2$, where $X',Y'$ are independent copies of $X$ (under $\mu$) and $Y$ (under $\mu'$).

### `condRuzsaDist'_eq_sum`
Lean: `[Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass T] (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (μ' : Measure Ω') [IsFiniteMeasure μ'] [FiniteRange W] : d[X ; μ # Y | W ; μ'] = ∑ w ∈ FiniteRange.toFinset W, μ'.real (W ⁻¹' {w}) * d[X; μ # Y; μ'[|W ⁻¹' {w}]]`
English: Let $G$ be countable with measurable singletons, and let $T$ have measurable singletons. Let $X:\Omega\to G$, and let $Y:\Omega'\to G$ and $W:\Omega'\to T$ be measurable, with $W$ of finite range. Let $\mu$ be a measure on $\Omega$ and $\mu'$ a finite measure on $\Omega'$. Then $d[X;\mu \,\#\, Y|W;\mu'] = \sum_{w} \mu'(W^{-1}\{w\})\, d[X;\mu \,\#\, Y;\mu'[\,\cdot\mid W^{-1}\{w\}]]$, the sum being over the finite range of $W$ (with $\mu'(\cdot)$ taken as a real number).

### `condRuzsaDist'_eq_integral`
Lean: `[Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass T] (X : Ω → G) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) (μ' : Measure Ω') [IsFiniteMeasure μ'] [FiniteRange W] : d[X ; μ # Y | W ; μ'] = ∫ (x : T), (fun w => d[X; μ # Y; μ'[|W ⁻¹' {w}]]) x ∂Measure.map W μ'`
English: Let $G$ be countable with measurable singletons, and let $T$ have measurable singletons. Let $X:\Omega\to G$, and let $Y:\Omega'\to G$ and $W:\Omega'\to T$ be measurable, with $W$ of finite range. Let $\mu$ be a measure on $\Omega$ and $\mu'$ a finite measure on $\Omega'$. Then $d[X;\mu \,\#\, Y|W;\mu'] = \int_T d[X;\mu \,\#\, Y;\mu'[\,\cdot\mid W^{-1}\{w\}]]\, d(W_*\mu')(w)$.

### `kaimanovich_vershik`
Lean: `[Countable G] [MeasurableSingletonClass G] (h : iIndepFun ![X, Y, Z] μ) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [FiniteRange X] [FiniteRange Z] [FiniteRange Y] : H[X + Y + Z; μ] - H[X + Y; μ] ≤ H[Y + Z; μ] - H[Y; μ]`
English: (Kaimanovich–Vershik inequality.) Let $G$ be a countable abelian group with measurable singletons, and let $X,Y,Z:\Omega\to G$ be measurable random variables with finite range which are jointly independent under $\mu$. Then $H[X+Y+Z;\mu] - H[X+Y;\mu] \le H[Y+Z;\mu] - H[Y;\mu]$.

### `comparison_of_ruzsa_distances`
Lean: `(μ : Measure Ω) [Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun Y Z μ') [FiniteRange X] [FiniteRange Z] [FiniteRange Y] : d[X; μ # Y + Z; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z; μ'] - H[Y; μ']) / 2 ∧ ∀ (a : Module (ZMod 2) G), H[Y + Z; μ'] - H[Y; μ'] = d[Y; μ' # Z; μ'] + H[Z; μ'] / 2 - H[Y; μ'] / 2`
English: Let $G$ be a countable abelian group with measurable singletons. Let $\mu$ be a probability measure on $\Omega$ and $\mu'$ a probability measure on $\Omega'$. Let $X:\Omega\to G$ and $Y,Z:\Omega'\to G$ be measurable random variables with finite range, with $Y$ and $Z$ independent under $\mu'$. Then (i) $d[X;\mu \,\#\, Y+Z;\mu'] - d[X;\mu \,\#\, Y;\mu'] \le (H[Y+Z;\mu'] - H[Y;\mu'])/2$, and (ii) if $G$ admits a $\mathbb{Z}/2$-module structure (i.e. $G$ is an elementary abelian 2-group), then $H[Y+Z;\mu'] - H[Y;\mu'] = d[Y;\mu' \,\#\, Z;\mu'] + H[Z;\mu']/2 - H[Y;\mu']/2$.

### `condRuzsaDist_diff_le`
Lean: `(μ : Measure Ω) [Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun Y Z μ') [FiniteRange X] [FiniteRange Z] [FiniteRange Y] : d[X; μ # Y + Z; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z; μ'] - H[Y; μ']) / 2`
English: Let $G$ be a countable abelian group with measurable singletons. Let $\mu$ be a probability measure on $\Omega$ and $\mu'$ a probability measure on $\Omega'$. Let $X:\Omega\to G$ and $Y,Z:\Omega'\to G$ be measurable random variables with finite range, with $Y$ and $Z$ independent under $\mu'$. Then $d[X;\mu \,\#\, Y+Z;\mu'] - d[X;\mu \,\#\, Y;\mu'] \le (H[Y+Z;\mu'] - H[Y;\mu'])/2$.

### `condRuzsaDist_of_copy`
Lean: `[Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass S] [MeasurableSingletonClass T] (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (hX' : Measurable X') (hZ' : Measurable Z') (hY' : Measurable Y') (hW' : Measurable W') [IsFiniteMeasure μ] [IsFiniteMeasure μ'] [IsFiniteMeasure μ''] [IsFiniteMeasure μ'''] (h1 : IdentDistrib (⟨X, Z⟩) (⟨X', Z'⟩) μ μ'') (h2 : IdentDistrib (⟨Y, W⟩) (⟨Y', W'⟩) μ' μ''') [FiniteRange Z] [FiniteRange W] [FiniteRange Z'] [FiniteRange W'] : d[X | Z ; μ # Y | W ; μ'] = d[X' | Z' ; μ'' # Y' | W' ; μ''']`
English: Let $G$ be countable with measurable singletons, and let $S$, $T$ have measurable singletons. Let $X,Z$ (on $\Omega$), $Y,W$ (on $\Omega'$), $X',Z'$ (on $\Omega''$), $Y',W'$ (on $\Omega'''$) be measurable random variables, with $X,Y,X',Y'$ valued in $G$, $Z,Z'$ valued in $S$ and $W,W'$ valued in $T$, and with $Z,W,Z',W'$ of finite range. Let $\mu,\mu',\mu'',\mu'''$ be finite measures on $\Omega,\Omega',\Omega'',\Omega'''$. Suppose $(X,Z)$ under $\mu$ has the same distribution as $(X',Z')$ under $\mu''$, and $(Y,W)$ under $\mu'$ has the same distribution as $(Y',W')$ under $\mu'''$. Then $d[X|Z;\mu \,\#\, Y|W;\mu'] = d[X'|Z';\mu'' \,\#\, Y'|W';\mu''']$.

### `condRuzsaDist_of_indep`
Lean: `[Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) [IsProbabilityMeasure μ] (h : IndepFun (⟨X, Z⟩) (⟨Y, W⟩) μ) [FiniteRange Z] [FiniteRange W] : d[X | Z ; μ # Y | W ; μ] = H[X - Y | ⟨Z, W⟩ ; μ] - H[X | Z ; μ] / 2 - H[Y | W ; μ] / 2`
English: Let $G$ be a countable abelian group with measurable singletons, and let $S$, $T$ be countable with measurable singletons. Let $\mu$ be a probability measure on $\Omega$, and let $X,Y:\Omega\to G$, $Z:\Omega\to S$, $W:\Omega\to T$ be measurable, with $Z$ and $W$ of finite range, such that $(X,Z)$ and $(Y,W)$ are independent under $\mu$. Then $d[X|Z;\mu \,\#\, Y|W;\mu] = H[X-Y \mid (Z,W);\mu] - H[X|Z;\mu]/2 - H[Y|W;\mu]/2$.

### `condRuzsaDist_le`
Lean: `(μ : Measure Ω) (μ' : Measure Ω') [Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) [FiniteRange X] [FiniteRange Z] [FiniteRange Y] [FiniteRange W] : d[X | Z ; μ # Y | W ; μ'] ≤ d[X; μ # Y; μ'] + I[X : Z ; μ] / 2 + I[Y : W ; μ'] / 2`
English: Let $G$ be a countable abelian group with measurable singletons, and let $S$, $T$ be countable with measurable singletons. Let $\mu$ be a probability measure on $\Omega$ and $\mu'$ a probability measure on $\Omega'$. Let $X:\Omega\to G$, $Z:\Omega\to S$, $Y:\Omega'\to G$, $W:\Omega'\to T$ be measurable random variables, all of finite range. Then $d[X|Z;\mu \,\#\, Y|W;\mu'] \le d[X;\mu \,\#\, Y;\mu'] + I[X:Z;\mu]/2 + I[Y:W;\mu']/2$.

### `condRuzsaDist_of_const`
Lean: `[Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass S] [MeasurableSingletonClass T] [Countable S] [Countable T] (hX : Measurable X) (Y : Ω' → G) (W : Ω' → T) (c : S) [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] [FiniteRange W] : d[X | fun x => c ; μ # Y | W ; μ'] = d[X ; μ # Y | W ; μ']`
English: Let $G$ be countable with measurable singletons, and let $S$, $T$ be countable with measurable singletons. Let $\mu$ be a probability measure on $\Omega$ and $\mu'$ a probability measure on $\Omega'$. Let $X:\Omega\to G$ be measurable, $Y:\Omega'\to G$, $W:\Omega'\to T$ with $W$ of finite range, and $c\in S$. Then conditioning on the constant variable $c$ does not change the distance: $d[X \mid c;\mu \,\#\, Y|W;\mu'] = d[X;\mu \,\#\, Y|W;\mu']$.

### `condRuzsaDist_diff_ofsum_le`
Lean: `(μ : Measure Ω) [Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (hZ' : Measurable Z') (h : iIndepFun ![Y, Z, Z'] μ') [FiniteRange X] [FiniteRange Z] [FiniteRange Y] [FiniteRange Z'] : d[X ; μ # Y + Z | Y + Z + Z' ; μ'] - d[X; μ # Y; μ'] ≤ (H[Y + Z + Z'; μ'] + H[Y + Z; μ'] - H[Y; μ'] - H[Z'; μ']) / 2`
English: Let $G$ be a countable abelian group with measurable singletons. Let $\mu$ be a probability measure on $\Omega$ and $\mu'$ a probability measure on $\Omega'$. Let $X:\Omega\to G$ and $Y,Z,Z':\Omega'\to G$ be measurable random variables with finite range, with $Y,Z,Z'$ jointly independent under $\mu'$. Then $d[X;\mu \,\#\, Y+Z \mid Y+Z+Z';\mu'] - d[X;\mu \,\#\, Y;\mu'] \le (H[Y+Z+Z';\mu'] + H[Y+Z;\mu'] - H[Y;\mu'] - H[Z';\mu'])/2$.

### `ent_of_diff_le`
Lean: `[Countable G] [MeasurableSingletonClass G] (X : Ω → G) (Y : Ω → G) (Z : Ω → G) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) (h : IndepFun (⟨X, Y⟩) Z μ) [IsProbabilityMeasure μ] [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : H[X - Y; μ] ≤ H[X - Z; μ] + H[Z - Y; μ] - H[Z; μ]`
English: (Improved entropic Ruzsa triangle inequality.) Let $G$ be a countable abelian group with measurable singletons, let $\mu$ be a probability measure on $\Omega$, and let $X,Y,Z:\Omega\to G$ be measurable random variables with finite range such that $(X,Y)$ and $Z$ are independent under $\mu$. Then $H[X-Y;\mu] \le H[X-Z;\mu] + H[Z-Y;\mu] - H[Z;\mu]$.

### `rdist_triangle`
Lean: `[Countable G] [MeasurableSingletonClass G] (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] [IsProbabilityMeasure μ''] [FiniteRange X] [FiniteRange Y] [FiniteRange Z] : d[X; μ # Z; μ''] ≤ d[X; μ # Y; μ'] + d[Y; μ' # Z; μ'']`
English: (Entropic Ruzsa triangle inequality.) Let $G$ be a countable abelian group with measurable singletons. Let $X$, $Y$, $Z$ be measurable $G$-valued random variables with finite range on $(\Omega,\mu)$, $(\Omega',\mu')$, $(\Omega'',\mu'')$ respectively, where $\mu,\mu',\mu''$ are probability measures. Then $d[X;\mu \,\#\, Z;\mu''] \le d[X;\mu \,\#\, Y;\mu'] + d[Y;\mu' \,\#\, Z;\mu'']$.

### `condRuzsaDist_eq_sum`
Lean: `[Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass S] [MeasurableSingletonClass T] (hX : Measurable X) (hZ : Measurable Z) (hY : Measurable Y) (hW : Measurable W) (μ : Measure Ω) [IsFiniteMeasure μ] (μ' : Measure Ω') [IsFiniteMeasure μ'] [FiniteRange Z] [FiniteRange W] : d[X | Z ; μ # Y | W ; μ'] = ∑ z ∈ FiniteRange.toFinset Z, ∑ w ∈ FiniteRange.toFinset W, μ.real (Z ⁻¹' {z}) * μ'.real (W ⁻¹' {w}) * d[X; μ[|Z ⁻¹' {z}] # Y; μ'[|W ⁻¹' {w}]]`
English: Let $G$ be countable with measurable singletons, and let $S$, $T$ have measurable singletons. Let $X:\Omega\to G$, $Z:\Omega\to S$, $Y:\Omega'\to G$, $W:\Omega'\to T$ be measurable, with $Z$ and $W$ of finite range, and let $\mu$ and $\mu'$ be finite measures on $\Omega$ and $\Omega'$. Then $d[X|Z;\mu \,\#\, Y|W;\mu'] = \sum_{z}\sum_{w} \mu(Z^{-1}\{z\})\,\mu'(W^{-1}\{w\})\, d[X;\mu[\,\cdot\mid Z^{-1}\{z\}] \,\#\, Y;\mu'[\,\cdot\mid W^{-1}\{w\}]]$, where $z$ ranges over the finite range of $Z$ and $w$ over the finite range of $W$ (measures taken as real numbers).

### `condRuzsaDist'_of_copy`
Lean: `[Countable G] [MeasurableSingletonClass G] [MeasurableSingletonClass T] (X : Ω → G) (hY : Measurable Y) (hW : Measurable W) (X' : Ω'' → G) (hY' : Measurable Y') (hW' : Measurable W') [IsFiniteMeasure μ'] [IsFiniteMeasure μ'''] (h1 : IdentDistrib X X' μ μ'') (h2 : IdentDistrib (⟨Y, W⟩) (⟨Y', W'⟩) μ' μ''') [FiniteRange W] [FiniteRange W'] : d[X ; μ # Y | W ; μ'] = d[X' ; μ'' # Y' | W' ; μ''']`
English: Let $G$ be countable with measurable singletons, and let $T$ have measurable singletons. Let $X:\Omega\to G$ and $X':\Omega''\to G$, and let $Y:\Omega'\to G$, $W:\Omega'\to T$, $Y':\Omega'''\to G$, $W':\Omega'''\to T$ be measurable, with $W$ and $W'$ of finite range. Let $\mu'$ and $\mu'''$ be finite measures. If $X$ under $\mu$ has the same distribution as $X'$ under $\mu''$, and $(Y,W)$ under $\mu'$ has the same distribution as $(Y',W')$ under $\mu'''$, then $d[X;\mu \,\#\, Y|W;\mu'] = d[X';\mu'' \,\#\, Y'|W';\mu''']$.

### `condRuzsaDist_of_inj_map`
Lean: `[Countable G] [MeasurableSingletonClass G] [Countable G'] [MeasurableSingletonClass G'] [IsProbabilityMeasure μ] (Y : Fin 4 → Ω → G) (h_indep : IndepFun (⟨Y 0, Y 2⟩) (⟨Y 1, Y 3⟩) μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) (π : G × G →+ G') (hπ : ∀ (h : G), Function.Injective fun g => π (g, h)) [FiniteRange (Y 2)] [FiniteRange (Y 3)] : d[⇑π ∘ ⟨Y 0, Y 2⟩ | Y 2 ; μ # ⇑π ∘ ⟨Y 1, Y 3⟩ | Y 3 ; μ] = d[Y 0 | Y 2 ; μ # Y 1 | Y 3 ; μ]`
English: Let $G$ and $G'$ be countable abelian groups with measurable singletons, and let $\mu$ be a probability measure on $\Omega$. Let $Y_0,Y_1,Y_2,Y_3:\Omega\to G$ be measurable with $Y_2$ and $Y_3$ of finite range, such that $(Y_0,Y_2)$ and $(Y_1,Y_3)$ are independent under $\mu$, and let $\pi:G\times G\to G'$ be an additive group homomorphism such that $g\mapsto\pi(g,h)$ is injective for every $h\in G$. Then $d[\pi(Y_0,Y_2) \mid Y_2;\mu \,\#\, \pi(Y_1,Y_3)\mid Y_3;\mu] = d[Y_0|Y_2;\mu \,\#\, Y_1|Y_3;\mu]$.

### `condRuzsaDist'_of_inj_map`
Lean: `[Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [Module (ZMod 2) G] (hX : Measurable X) (hB : Measurable B) (hC : Measurable C) (h_indep : IndepFun X (⟨B, C⟩) μ) [FiniteRange X] [FiniteRange B] [FiniteRange C] : d[X ; μ # B | B + C ; μ] = d[X ; μ # C | B + C ; μ]`
English: Let $G$ be a countable elementary abelian 2-group (a vector space over $\mathbb{F}_2$) with measurable singletons, and let $\mu$ be a probability measure on $\Omega$. Let $X,B,C:\Omega\to G$ be measurable random variables with finite range, with $X$ independent of $(B,C)$ under $\mu$. Then $d[X;\mu \,\#\, B \mid B+C;\mu] = d[X;\mu \,\#\, C\mid B+C;\mu]$.

### `condRuzsaDist'_of_inj_map'`
Lean: `[Countable G] [MeasurableSingletonClass G] [Module (ZMod 2) G] [IsProbabilityMeasure μ] [IsProbabilityMeasure μ''] (hA : Measurable A) (hB : Measurable B) (hC : Measurable C) [FiniteRange A] [FiniteRange B] [FiniteRange C] : d[A ; μ'' # B | B + C ; μ] = d[A ; μ'' # C | B + C ; μ]`
English: Let $G$ be a countable elementary abelian 2-group (a vector space over $\mathbb{F}_2$) with measurable singletons. Let $\mu$ be a probability measure on $\Omega$ and $\mu''$ a probability measure on $\Omega''$. Let $A:\Omega''\to G$ and $B,C:\Omega\to G$ be measurable random variables with finite range. Then $d[A;\mu'' \,\#\, B\mid B+C;\mu] = d[A;\mu''\,\#\, C\mid B+C;\mu]$.

### `rdist_add_const`
Lean: `[Countable G] [MeasurableSingletonClass G] [FiniteRange X] [FiniteRange Y] [IsZeroOrProbabilityMeasure μ] [IsZeroOrProbabilityMeasure μ'] (hX : Measurable X) (hY : Measurable Y) : d[X; μ # Y + fun x => c; μ'] = d[X; μ # Y; μ']`
English: Let $G$ be a countable abelian group with measurable singletons. Let $\mu$ and $\mu'$ each be either the zero measure or a probability measure, let $X:\Omega\to G$ and $Y:\Omega'\to G$ be measurable random variables with finite range, and let $c\in G$. Then $d[X;\mu \,\#\, Y+c;\mu'] = d[X;\mu \,\#\, Y;\mu']$: adding a constant to a random variable does not change the Ruzsa distance.

### `continuous_rdist_restrict_probabilityMeasure`
Lean: `[Finite G] [DiscreteTopology G] [BorelSpace G] : Continuous fun μ => d[id; ↑μ.1 # id; ↑μ.2]`
English: Let $G$ be a finite abelian group with the discrete topology and its Borel $\sigma$-algebra. On pairs $(\mu_1,\mu_2)$ of probability measures on $G$ (with the product of the topologies on the space of probability measures), the map $(\mu_1,\mu_2)\mapsto d[\mathrm{id};\mu_1 \,\#\, \mathrm{id};\mu_2]$ is continuous.

### `diff_ent_le_rdist`
Lean: `[Countable G] [MeasurableSingletonClass G] [FiniteRange X] [FiniteRange Y] [IsProbabilityMeasure μ] [IsProbabilityMeasure μ'] (hX : Measurable X) (hY : Measurable Y) : |H[X; μ] - H[Y; μ']| ≤ 2 * d[X; μ # Y; μ']`
English: Let $G$ be a countable abelian group with measurable singletons. Let $\mu$ and $\mu'$ be probability measures, and let $X:\Omega\to G$ and $Y:\Omega'\to G$ be measurable random variables with finite range. Then $|H[X;\mu] - H[Y;\mu']| \le 2\, d[X;\mu \,\#\, Y;\mu']$.

### `ent_bsg`
Lean: `[Countable G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] (hA : Measurable A) (hB : Measurable B) [Finite G] : ∫ (x : G), (fun z => d[A; μ[|(A + B) ⁻¹' {z}] # B; μ[|(A + B) ⁻¹' {z}]]) x ∂Measure.map (A + B) μ ≤ 3 * I[A : B ; μ] + 2 * H[A + B; μ] - H[A; μ] - H[B; μ]`
English: (Entropic Balog–Szemerédi–Gowers inequality.) Let $G$ be a finite abelian group with measurable singletons, let $\mu$ be a probability measure on $\Omega$, let $A,B:\Omega\to G$ be measurable, and set $Z=A+B$. Then $\int_G d[A;\mu[\,\cdot\mid Z^{-1}\{z\}] \,\#\, B;\mu[\,\cdot\mid Z^{-1}\{z\}]]\, d(Z_*\mu)(z) \le 3\,I[A:B;\mu] + 2\,H[A+B;\mu] - H[A;\mu] - H[B;\mu]$.
