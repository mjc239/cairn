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

#### `FiniteRange` (inductive)
Lean: `{Ω : Type u_1} → {G : Type u_2} → (Ω → G) → Prop`
Docstring: The property of having a finite range.

#### `ProbabilityTheory.condMutualInfo` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → {U : Type u_4} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace U] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → (Ω → U) → autoParam (Measure Ω) condMutualInfo._auto_1 → ℝ`
Docstring: The conditional mutual information `I[X : Y| Z]` is the mutual information of `X| Z=z` and `Y| Z=z`, integrated over `z`.
Definition: `fun {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [MeasurableSpace Ω] [MeasurableSpace S] [inst_1 : MeasurableSpace U] [MeasurableSpace T] (X : Ω → S) (Y : Ω → T) (Z : Ω → U) (μ : Measure Ω) => @integral _ _ _ _ inst_1 (Measure.map Z μ) fun (x : U) => (fun (z : U) => H[X | Z ← z; μ] + H[Y | Z ← z; μ] - H[⟨X, Y⟩ | Z ← z; μ]) x`

#### `condRuzsaDist` (def)
Lean: `{Ω : Type u_1} → {Ω' : Type u_2} → {G : Type u_5} → {S : Type u_6} → {T : Type u_7} → [mΩ : MeasurableSpace Ω] → [mΩ' : MeasurableSpace Ω'] → [hG : MeasurableSpace G] → [AddCommGroup G] → [MeasurableSpace S] → [MeasurableSpace T] → [Countable G] → [MeasurableSingletonClass G] → (Ω → G) → (Ω → S) → (Ω' → G) → (Ω' → T) → (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) → [IsFiniteMeasure μ] → (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) → [IsFiniteMeasure μ'] → ℝ`
Docstring: The conditional Ruzsa distance `d[X|Z ; Y|W]`.
Definition: `fun {Ω : Type u_1} {Ω' : Type u_2} {G : Type u_5} {S : Type u_6} {T : Type u_7} [MeasurableSpace Ω] [MeasurableSpace Ω'] [MeasurableSpace G] [AddCommGroup G] [MeasurableSpace S] [MeasurableSpace T] [Countable G] [MeasurableSingletonClass G] (X : Ω → G) (Z : Ω → S) (Y : Ω' → G) (W : Ω' → T) (μ : Measure Ω) [IsFiniteMeasure μ] (μ' : Measure Ω') [IsFiniteMeasure μ'] => dk[condDistrib X Z μ ; Measure.map Z μ # condDistrib Y W μ' ; Measure.map W μ']`

#### `prod` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → (Ω → S) → (Ω → T) → Ω → S × T`
Docstring: The pair of two random variables
Definition: `fun {Ω : Type u_1} {S : Type u_2} {T : Type u_3} (X : Ω → S) (Y : Ω → T) (ω : Ω) => (X ω, Y ω)`

#### `rdist` (def)
Lean: `{Ω : Type u_1} → {Ω' : Type u_2} → {G : Type u_5} → [mΩ : MeasurableSpace Ω] → [mΩ' : MeasurableSpace Ω'] → [hG : MeasurableSpace G] → [AddCommGroup G] → (Ω → G) → (Ω' → G) → autoParam (Measure Ω) rdist._auto_1 → autoParam (Measure Ω') rdist._auto_3 → ℝ`
Docstring: The Ruzsa distance `rdist X Y` or `d[X ; Y]` between two random variables is defined as `H[X'- Y'] - H[X']/2 - H[Y']/2`, where `X', Y'` are independent copies of `X, Y`.
Definition: `fun {Ω : Type u_1} {Ω' : Type u_2} {G : Type u_5} [MeasurableSpace Ω] [MeasurableSpace Ω'] [MeasurableSpace G] [AddCommGroup G] (X : Ω → G) (Y : Ω' → G) (μ : Measure Ω) (μ' : Measure Ω') => H[fun (x : G × G) => x.1 - x.2; Measure.prod (Measure.map X μ) (Measure.map Y μ')] - H[X; μ] / (2 : ℝ) - H[Y; μ'] / (2 : ℝ)`

#### `ProbabilityTheory.entropy` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Definition: `fun {Ω : Type u_1} {S : Type u_2} [MeasurableSpace Ω] [MeasurableSpace S] (X : Ω → S) (μ : Measure Ω) => Hm[Measure.map X μ]`

#### `ProbabilityTheory.Kernel.rdist` (def)
Lean: `{T : Type u_1} → {T' : Type u_2} → {G : Type u_4} → [inst : MeasurableSpace T] → [inst_1 : MeasurableSpace T'] → [inst_2 : MeasurableSpace G] → [AddCommGroup G] → Kernel T G → Kernel T' G → Measure T → Measure T' → ℝ`
Docstring: The Rusza distance between two kernels taking values in the same space, defined as the average Rusza distance between the image measures.
Definition: `fun {T : Type u_1} {T' : Type u_2} {G : Type u_4} [MeasurableSpace T] [MeasurableSpace T'] [MeasurableSpace G] [AddCommGroup G] (κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') => ∫ (x : T × T'), (fun (p : T × T') => Kernel.rdistm.{u_4} (G := G) (κ p.1) (η p.2)) x ∂μ.prod ν`

## Translations

### `rdist_of_indep_eq_sum_fibre`
Lean (short): `[Countable H] [MeasurableSingletonClass H] [Countable H'] [MeasurableSingletonClass H'] (π : H →+ H') [IsProbabilityMeasure μ] (h : IndepFun Z_1 Z_2 μ) (h1 : Measurable Z_1) (h2 : Measurable Z_2) [FiniteRange Z_1] [FiniteRange Z_2] : d[Z_1; μ # Z_2; μ] = d[⇑π ∘ Z_1; μ # ⇑π ∘ Z_2; μ] + d[Z_1 | ⇑π ∘ Z_1 ; μ # Z_2 | ⇑π ∘ Z_2 ; μ] + I[Z_1 - Z_2 : ⟨⇑π ∘ Z_1, ⇑π ∘ Z_2⟩|⇑π ∘ (Z_1 - Z_2);μ]`
Lean (full): `∀ {H : Type u_1} [inst : AddCommGroup H] [inst_1 : Countable H] [hH : MeasurableSpace H] [inst_2 : MeasurableSingletonClass H] {H' : Type u_2} [inst_3 : AddCommGroup H'] [Countable H'] [hH' : MeasurableSpace H'] [MeasurableSingletonClass H'] (π : H →+ H') {Ω : Type u_3} [mΩ : MeasurableSpace Ω] {μ : Measure Ω} [inst_6 : IsProbabilityMeasure μ] {Z_1 Z_2 : Ω → H}, IndepFun Z_1 Z_2 μ → Measurable Z_1 → Measurable Z_2 → ∀ [FiniteRange Z_1] [FiniteRange Z_2], d[Z_1; μ # Z_2; μ] = d[⇑π ∘ Z_1; μ # ⇑π ∘ Z_2; μ] + d[Z_1 | ⇑π ∘ Z_1 ; μ # Z_2 | ⇑π ∘ Z_2 ; μ] + I[Z_1 - Z_2 : ⟨⇑π ∘ Z_1, ⇑π ∘ Z_2⟩|⇑π ∘ (Z_1 - Z_2);μ]`
Docstring: If $Z_1, Z_2$ are independent, then $d[Z_1; Z_2]$ is equal to $$ d[\pi(Z_1);\pi(Z_2)] + d[Z_1|\pi(Z_1); Z_2 |\pi(Z_2)]$$ plus $$I( Z_1 - Z_2 : (\pi(Z_1), \pi(Z_2)) | \pi(Z_1 - Z_2) ).$$
English: Let $H$ and $H'$ be countable abelian groups, each equipped with a measurable structure in which singletons are measurable, let $\pi : H \to H'$ be a group homomorphism, let $\mu$ be a probability measure on a measurable space $\Omega$, and let $Z_1, Z_2:\Omega\to H$ be measurable random variables, both of finite range, that are independent with respect to $\mu$. Then $$d[Z_1;Z_2] = d[\pi(Z_1);\pi(Z_2)] + d[Z_1\mid\pi(Z_1);\, Z_2\mid\pi(Z_2)] + I\big[Z_1 - Z_2 : (\pi(Z_1),\pi(Z_2)) \,\big|\, \pi(Z_1 - Z_2)\big],$$ all quantities taken with respect to $\mu$.

### `sum_of_rdist_eq_step_condMutualInfo`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : I[⟨Y 0 - Y 1, Y 2 - Y 3⟩ : ⟨Y 0 - Y 2, Y 1 - Y 3⟩|Y 0 - Y 1 - (Y 2 - Y 3);μ] = I[Y 0 - Y 1 : Y 1 - Y 3|Y 0 - Y 1 - Y 2 + Y 3;μ]`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [Finite G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] {Ω : Type u_2} [mΩ : MeasurableSpace Ω] {μ : Measure Ω} [IsProbabilityMeasure μ] {Y : Fin (4 : ℕ) → Ω → G}, (∀ (i : Fin (4 : ℕ)), Measurable (Y i)) → I[⟨Y (0 : Fin (4 : ℕ)) - Y (1 : Fin (4 : ℕ)), Y (2 : Fin (4 : ℕ)) - Y (3 : Fin (4 : ℕ))⟩ : ⟨Y (0 : Fin (4 : ℕ)) - Y (2 : Fin (4 : ℕ)), Y (1 : Fin (4 : ℕ)) - Y (3 : Fin (4 : ℕ))⟩|Y (0 : Fin (4 : ℕ)) - Y (1 : Fin (4 : ℕ)) - (Y (2 : Fin (4 : ℕ)) - Y (3 : Fin (4 : ℕ)));μ] = I[Y (0 : Fin (4 : ℕ)) - Y (1 : Fin (4 : ℕ)) : Y (1 : Fin (4 : ℕ)) - Y (3 : Fin (4 : ℕ))|Y (0 : Fin (4 : ℕ)) - Y (1 : Fin (4 : ℕ)) - Y (2 : Fin (4 : ℕ)) + Y (3 : Fin (4 : ℕ));μ]`
Docstring: The conditional mutual information step of `sum_of_rdist_eq`
English: Let $G$ be a finite abelian group equipped with a measurable structure in which singletons are measurable, let $\mu$ be a probability measure on a measurable space $\Omega$, and let $Y_0, Y_1, Y_2, Y_3:\Omega\to G$ be measurable random variables. Then, with respect to $\mu$, $$I\big[(Y_0 - Y_1,\ Y_2 - Y_3) : (Y_0 - Y_2,\ Y_1 - Y_3) \,\big|\, Y_0 - Y_1 - (Y_2 - Y_3)\big] = I\big[Y_0 - Y_1 : Y_1 - Y_3 \,\big|\, Y_0 - Y_1 - Y_2 + Y_3\big].$$

### `sum_of_rdist_eq_step_condRuzsaDist`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] (h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[⟨Y 0, Y 2⟩ | Y 0 - Y 2 ; μ # ⟨Y 1, Y 3⟩ | Y 1 - Y 3 ; μ] = d[Y 0 | Y 0 - Y 2 ; μ # Y 1 | Y 1 - Y 3 ; μ]`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : Finite G] [hG : MeasurableSpace G] [inst_2 : MeasurableSingletonClass G] {Ω : Type u_2} [mΩ : MeasurableSpace Ω] {μ : Measure Ω} [inst_3 : IsProbabilityMeasure μ] {Y : Fin (4 : ℕ) → Ω → G}, iIndepFun (β := fun (x : Fin (4 : ℕ)) => G) Y μ → (∀ (i : Fin (4 : ℕ)), Measurable (Y i)) → d[⟨Y (0 : Fin (4 : ℕ)), Y (2 : Fin (4 : ℕ))⟩ | Y (0 : Fin (4 : ℕ)) - Y (2 : Fin (4 : ℕ)) ; μ # ⟨Y (1 : Fin (4 : ℕ)), Y (3 : Fin (4 : ℕ))⟩ | Y (1 : Fin (4 : ℕ)) - Y (3 : Fin (4 : ℕ)) ; μ] = d[Y (0 : Fin (4 : ℕ)) | Y (0 : Fin (4 : ℕ)) - Y (2 : Fin (4 : ℕ)) ; μ # Y (1 : Fin (4 : ℕ)) | Y (1 : Fin (4 : ℕ)) - Y (3 : Fin (4 : ℕ)) ; μ]`
Docstring: The conditional Ruzsa Distance step of `sum_of_rdist_eq`
English: Let $G$ be a finite abelian group equipped with a measurable structure in which singletons are measurable, let $\mu$ be a probability measure on a measurable space $\Omega$, and let $Y_0, Y_1, Y_2, Y_3:\Omega\to G$ be measurable random variables that are jointly independent with respect to $\mu$. Then, with respect to $\mu$, $$d\big[(Y_0,Y_2)\mid Y_0 - Y_2;\ (Y_1,Y_3)\mid Y_1 - Y_3\big] = d\big[Y_0 \mid Y_0 - Y_2;\ Y_1\mid Y_1 - Y_3\big].$$

### `sum_of_rdist_eq`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] (Y : Fin 4 → Ω → G) (h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[Y 0; μ # Y 1; μ] + d[Y 2; μ # Y 3; μ] = d[Y 0 - Y 2; μ # Y 1 - Y 3; μ] + d[Y 0 | Y 0 - Y 2 ; μ # Y 1 | Y 1 - Y 3 ; μ] + I[Y 0 - Y 1 : Y 1 - Y 3|Y 0 - Y 1 - Y 2 + Y 3;μ]`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : Finite G] [hG : MeasurableSpace G] [inst_2 : MeasurableSingletonClass G] {Ω : Type u_2} [mΩ : MeasurableSpace Ω] {μ : Measure Ω} [inst_3 : IsProbabilityMeasure μ] (Y : Fin (4 : ℕ) → Ω → G), iIndepFun (β := fun (x : Fin (4 : ℕ)) => G) Y μ → (∀ (i : Fin (4 : ℕ)), Measurable (Y i)) → d[Y (0 : Fin (4 : ℕ)); μ # Y (1 : Fin (4 : ℕ)); μ] + d[Y (2 : Fin (4 : ℕ)); μ # Y (3 : Fin (4 : ℕ)); μ] = d[Y (0 : Fin (4 : ℕ)) - Y (2 : Fin (4 : ℕ)); μ # Y (1 : Fin (4 : ℕ)) - Y (3 : Fin (4 : ℕ)); μ] + d[Y (0 : Fin (4 : ℕ)) | Y (0 : Fin (4 : ℕ)) - Y (2 : Fin (4 : ℕ)) ; μ # Y (1 : Fin (4 : ℕ)) | Y (1 : Fin (4 : ℕ)) - Y (3 : Fin (4 : ℕ)) ; μ] + I[Y (0 : Fin (4 : ℕ)) - Y (1 : Fin (4 : ℕ)) : Y (1 : Fin (4 : ℕ)) - Y (3 : Fin (4 : ℕ))|Y (0 : Fin (4 : ℕ)) - Y (1 : Fin (4 : ℕ)) - Y (2 : Fin (4 : ℕ)) + Y (3 : Fin (4 : ℕ));μ]`
Docstring: Let $Y_1,Y_2,Y_3$ and $Y_4$ be independent $G$-valued random variables. Then $$d[Y_1-Y_3; Y_2-Y_4] + d[Y_1|Y_1-Y_3; Y_2|Y_2-Y_4] $$ $$ + I[Y_1-Y_2 : Y_2 - Y_4 | Y_1-Y_2-Y_3+Y_4] = d[Y_1; Y_2] + d[Y_3; Y_4].$$
English: Let $G$ be a finite abelian group equipped with a measurable structure in which singletons are measurable, let $\mu$ be a probability measure on a measurable space $\Omega$, and let $Y_0, Y_1, Y_2, Y_3:\Omega\to G$ be measurable random variables that are jointly independent with respect to $\mu$. Then, with respect to $\mu$, $$d[Y_0;Y_1] + d[Y_2;Y_3] = d[Y_0 - Y_2;\ Y_1 - Y_3] + d[Y_0\mid Y_0 - Y_2;\ Y_1 \mid Y_1 - Y_3] + I[Y_0 - Y_1 : Y_1 - Y_3 \mid Y_0 - Y_1 - Y_2 + Y_3].$$

### `sum_of_rdist_eq_char_2`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [Module (ZMod 2) G] (Y : Fin 4 → Ω → G) (h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[Y 0; μ # Y 1; μ] + d[Y 2; μ # Y 3; μ] = d[Y 0 + Y 2; μ # Y 1 + Y 3; μ] + d[Y 0 | Y 0 + Y 2 ; μ # Y 1 | Y 1 + Y 3 ; μ] + I[Y 0 + Y 1 : Y 1 + Y 3|Y 0 + Y 1 + Y 2 + Y 3;μ]`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : Finite G] [hG : MeasurableSpace G] [inst_2 : MeasurableSingletonClass G] {Ω : Type u_2} [mΩ : MeasurableSpace Ω] {μ : Measure Ω} [inst_3 : IsProbabilityMeasure μ] [Module (ZMod (2 : ℕ)) G] (Y : Fin (4 : ℕ) → Ω → G), iIndepFun (β := fun (x : Fin (4 : ℕ)) => G) Y μ → (∀ (i : Fin (4 : ℕ)), Measurable (Y i)) → d[Y (0 : Fin (4 : ℕ)); μ # Y (1 : Fin (4 : ℕ)); μ] + d[Y (2 : Fin (4 : ℕ)); μ # Y (3 : Fin (4 : ℕ)); μ] = d[Y (0 : Fin (4 : ℕ)) + Y (2 : Fin (4 : ℕ)); μ # Y (1 : Fin (4 : ℕ)) + Y (3 : Fin (4 : ℕ)); μ] + d[Y (0 : Fin (4 : ℕ)) | Y (0 : Fin (4 : ℕ)) + Y (2 : Fin (4 : ℕ)) ; μ # Y (1 : Fin (4 : ℕ)) | Y (1 : Fin (4 : ℕ)) + Y (3 : Fin (4 : ℕ)) ; μ] + I[Y (0 : Fin (4 : ℕ)) + Y (1 : Fin (4 : ℕ)) : Y (1 : Fin (4 : ℕ)) + Y (3 : Fin (4 : ℕ))|Y (0 : Fin (4 : ℕ)) + Y (1 : Fin (4 : ℕ)) + Y (2 : Fin (4 : ℕ)) + Y (3 : Fin (4 : ℕ));μ]`
Docstring: Let $Y_1,Y_2,Y_3$ and $Y_4$ be independent $G$-valued random variables. Then $$d[Y_1+Y_3; Y_2+Y_4] + d[Y_1|Y_1+Y_3; Y_2|Y_2+Y_4] $$ $$ + I[Y_1+Y_2 : Y_2 + Y_4 | Y_1+Y_2+Y_3+Y_4] = d[Y_1; Y_2] + d[Y_3; Y_4].$$
English: Let $G$ be a finite abelian group that is a module over $\mathbb Z/2\mathbb Z$ (i.e. $2g=0$ for all $g\in G$), equipped with a measurable structure in which singletons are measurable. Let $(\Omega,\mu)$ be a measurable space with a probability measure $\mu$, and let $Y_0,Y_1,Y_2,Y_3:\Omega\to G$ be measurable random variables that are jointly independent under $\mu$. Then, all quantities being taken with respect to $\mu$, $$d[Y_0;Y_1]+d[Y_2;Y_3]=d[Y_0+Y_2;\,Y_1+Y_3]+d[Y_0\mid Y_0+Y_2;\,Y_1\mid Y_1+Y_3]+I[Y_0+Y_1:Y_1+Y_3\mid Y_0+Y_1+Y_2+Y_3],$$ where, for random variables $U,V,Z,W$ on $\Omega$, $d[U;V]=H[U'-V']-H[U]/2-H[V]/2$ is the Ruzsa distance ($H$ denoting Shannon entropy and $U',V'$ independent copies of $U,V$), $d[U\mid Z;V\mid W]$ is the conditional Ruzsa distance, and $I[U:V\mid Z]=\int\big(H[U\mid Z=z]+H[V\mid Z=z]-H[(U,V)\mid Z=z]\big)\,d(Z_*\mu)(z)$ is the conditional mutual information.
