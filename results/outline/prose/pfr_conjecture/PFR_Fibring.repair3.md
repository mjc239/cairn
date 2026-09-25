You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring, and when no
docstring, definition body (under "Project definitions") or Lean supports a description of an object, name it
instead of describing it. Give every variable its
type, introduce every symbol, and never use one letter for two things.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `ProbabilityTheory.condMutualInfo` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → {U : Type u_4} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace U] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → (Ω → U) → autoParam (Measure Ω) condMutualInfo._auto_1 → ℝ`
Docstring: The conditional mutual information `I[X : Y| Z]` is the mutual information of `X| Z=z` and `Y| Z=z`, integrated over `z`.
Definition: `fun {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [MeasurableSpace Ω] [MeasurableSpace S] [inst_1 : MeasurableSpace U] [MeasurableSpace T] (X : Ω → S) (Y : Ω → T) (Z : Ω → U) (μ : Measure Ω) => @integral _ _ _ _ inst_1 (Measure.map Z μ) fun (x : U) => (fun (z : U) => H[X | Z ← z; μ] + H[Y | Z ← z; μ] - H[⟨X, Y⟩ | Z ← z; μ]) x`

#### `condRuzsaDist` (def)
Lean: `{Ω : Type u_1} → {Ω' : Type u_2} → {G : Type u_5} → {S : Type u_6} → {T : Type u_7} → [mΩ : MeasurableSpace Ω] → [mΩ' : MeasurableSpace Ω'] → [hG : MeasurableSpace G] → [AddCommGroup G] → [MeasurableSpace S] → [MeasurableSpace T] → [Countable G] → [MeasurableSingletonClass G] → (Ω → G) → (Ω → S) → (Ω' → G) → (Ω' → T) → (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) → [IsFiniteMeasure μ] → (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) → [IsFiniteMeasure μ'] → ℝ`
Docstring: The conditional Ruzsa distance `d[X|Z ; Y|W]`.
Definition: `fun {Ω : Type u_1} {Ω' : Type u_2} {G : Type u_5} {S : Type u_6} {T : Type u_7} [MeasurableSpace Ω] [MeasurableSpace Ω'] [MeasurableSpace G] [AddCommGroup G] [MeasurableSpace S] [MeasurableSpace T] [Countable G] [MeasurableSingletonClass G] (X : Ω → G) (Z : Ω → S) (Y : Ω' → G) (W : Ω' → T) (μ : Measure Ω) [IsFiniteMeasure μ] (μ' : Measure Ω') [IsFiniteMeasure μ'] => dk[condDistrib X Z μ ; Measure.map Z μ # condDistrib Y W μ' ; Measure.map W μ']`

#### `rdist` (def)
Lean: `{Ω : Type u_1} → {Ω' : Type u_2} → {G : Type u_5} → [mΩ : MeasurableSpace Ω] → [mΩ' : MeasurableSpace Ω'] → [hG : MeasurableSpace G] → [AddCommGroup G] → (Ω → G) → (Ω' → G) → autoParam (Measure Ω) rdist._auto_1 → autoParam (Measure Ω') rdist._auto_3 → ℝ`
Docstring: The Ruzsa distance `rdist X Y` or `d[X ; Y]` between two random variables is defined as `H[X'- Y'] - H[X']/2 - H[Y']/2`, where `X', Y'` are independent copies of `X, Y`.
Definition: `fun {Ω : Type u_1} {Ω' : Type u_2} {G : Type u_5} [MeasurableSpace Ω] [MeasurableSpace Ω'] [MeasurableSpace G] [AddCommGroup G] (X : Ω → G) (Y : Ω' → G) (μ : Measure Ω) (μ' : Measure Ω') => H[fun (x : G × G) => x.1 - x.2; Measure.prod (Measure.map X μ) (Measure.map Y μ')] - H[X; μ] / (2 : ℝ) - H[Y; μ'] / (2 : ℝ)`

#### `ProbabilityTheory.entropy` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Definition: `fun {Ω : Type u_1} {S : Type u_2} [MeasurableSpace Ω] [MeasurableSpace S] (X : Ω → S) (μ : Measure Ω) => Hm[Measure.map X μ]`

#### `prod` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → (Ω → S) → (Ω → T) → Ω → S × T`
Docstring: The pair of two random variables
Definition: `fun {Ω : Type u_1} {S : Type u_2} {T : Type u_3} (X : Ω → S) (Y : Ω → T) (ω : Ω) => (X ω, Y ω)`

#### `ProbabilityTheory.Kernel.rdist` (def)
Lean: `{T : Type u_1} → {T' : Type u_2} → {G : Type u_4} → [inst : MeasurableSpace T] → [inst_1 : MeasurableSpace T'] → [inst_2 : MeasurableSpace G] → [AddCommGroup G] → Kernel T G → Kernel T' G → Measure T → Measure T' → ℝ`
Docstring: The Rusza distance between two kernels taking values in the same space, defined as the average Rusza distance between the image measures.
Definition: `fun {T : Type u_1} {T' : Type u_2} {G : Type u_4} [MeasurableSpace T] [MeasurableSpace T'] [MeasurableSpace G] [AddCommGroup G] (κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') => ∫ (x : T × T'), (fun (p : T × T') => Kernel.rdistm.{u_4} (G := G) (κ p.1) (η p.2)) x ∂μ.prod ν`

## Flagged translations

### `sum_of_rdist_eq_char_2`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure μ] [Module (ZMod 2) G] (Y : Fin 4 → Ω → G) (h_indep : iIndepFun Y μ) (h_meas : ∀ (i : Fin 4), Measurable (Y i)) : d[Y 0; μ # Y 1; μ] + d[Y 2; μ # Y 3; μ] = d[Y 0 + Y 2; μ # Y 1 + Y 3; μ] + d[Y 0 | Y 0 + Y 2 ; μ # Y 1 | Y 1 + Y 3 ; μ] + I[Y 0 + Y 1 : Y 1 + Y 3|Y 0 + Y 1 + Y 2 + Y 3;μ]`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [inst_1 : Finite G] [hG : MeasurableSpace G] [inst_2 : MeasurableSingletonClass G] {Ω : Type u_2} [mΩ : MeasurableSpace Ω] {μ : Measure Ω} [inst_3 : IsProbabilityMeasure μ] [Module (ZMod (2 : ℕ)) G] (Y : Fin (4 : ℕ) → Ω → G), iIndepFun (β := fun (x : Fin (4 : ℕ)) => G) Y μ → (∀ (i : Fin (4 : ℕ)), Measurable (Y i)) → d[Y (0 : Fin (4 : ℕ)); μ # Y (1 : Fin (4 : ℕ)); μ] + d[Y (2 : Fin (4 : ℕ)); μ # Y (3 : Fin (4 : ℕ)); μ] = d[Y (0 : Fin (4 : ℕ)) + Y (2 : Fin (4 : ℕ)); μ # Y (1 : Fin (4 : ℕ)) + Y (3 : Fin (4 : ℕ)); μ] + d[Y (0 : Fin (4 : ℕ)) | Y (0 : Fin (4 : ℕ)) + Y (2 : Fin (4 : ℕ)) ; μ # Y (1 : Fin (4 : ℕ)) | Y (1 : Fin (4 : ℕ)) + Y (3 : Fin (4 : ℕ)) ; μ] + I[Y (0 : Fin (4 : ℕ)) + Y (1 : Fin (4 : ℕ)) : Y (1 : Fin (4 : ℕ)) + Y (3 : Fin (4 : ℕ))|Y (0 : Fin (4 : ℕ)) + Y (1 : Fin (4 : ℕ)) + Y (2 : Fin (4 : ℕ)) + Y (3 : Fin (4 : ℕ));μ]`
Docstring: Let $Y_1,Y_2,Y_3$ and $Y_4$ be independent $G$-valued random variables. Then $$d[Y_1+Y_3; Y_2+Y_4] + d[Y_1|Y_1+Y_3; Y_2|Y_2+Y_4] $$ $$ + I[Y_1+Y_2 : Y_2 + Y_4 | Y_1+Y_2+Y_3+Y_4] = d[Y_1; Y_2] + d[Y_3; Y_4].$$
Previous English: Let $G$ be a finite elementary abelian $2$-group (i.e. a vector space over $\mathbb{F}_2$) with measurable singletons, let $\mu$ be a probability measure, and let $Y_0, Y_1, Y_2, Y_3$ be measurable $G$-valued random variables that are jointly independent with respect to $\mu$. Then, with respect to $\mu$, $$d[Y_0;Y_1] + d[Y_2;Y_3] = d[Y_0 + Y_2;\ Y_1 + Y_3] + d[Y_0\mid Y_0 + Y_2;\ Y_1 \mid Y_1 + Y_3] + I[Y_0 + Y_1 : Y_1 + Y_3 \mid Y_0 + Y_1 + Y_2 + Y_3].$$
Checker's issue: Omega (the sample space / measurable space on which mu lives and the Y_i are defined) is never introduced; mu is 'a probability measure' on an unstated space.
