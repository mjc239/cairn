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

#### `TauMinimizes` (def)
Lean: `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [AddCommGroup G] → [inst_3 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → {Ω : Type u_11} → [MeasureSpace Ω] → (Ω → G) → (Ω → G) → Prop`
Docstring: Property recording the fact that two random variables minimize the tau functional. Expressed in terms of measures on the group to avoid quantifying over all spaces, but this implies comparison with any pair of random variables, see Lemma `is_tau_min`.
Definition: `fun {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] {G : Type uG} [AddCommGroup G] [MeasurableSpace G] (p : refPackage Ω₀₁ Ω₀₂ G) {Ω : Type u_11} [MeasureSpace Ω] (X₁ X₂ : Ω → G) => ∀ (ν₁ : Measure G) [IsProbabilityMeasure ν₁] (ν₂ : Measure G) [IsProbabilityMeasure ν₂], τ[X₁ # X₂ | p] ≤ τ[id ; ν₁ # id ; ν₂ | p]`

#### `refPackage` (structure or class)
Lean: `(Ω₀₁ : Type u_1) → (Ω₀₂ : Type u_2) → [MeasureSpace Ω₀₁] → [MeasureSpace Ω₀₂] → (G : Type uG) → [MeasurableSpace G] → Type (max (max uG u_1) u_2)`
Docstring: A structure that packages all the fixed information in the main argument. In this way, when defining the τ functional, we will only only need to refer to the package once in the notation instead of stating the reference spaces, the reference measures and the reference random variables. The η parameter has now been incorporated into the package, in preparation for being able to manipulate the package.
Fields: `X₀₁`, `X₀₂`, `η`, `0`, `8`, `1`

#### `refPackage.X₀₁` (def)
Lean: `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [inst_2 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → Ω₀₁ → G`
Docstring: The first variable in a package.
Definition: `fun (Ω₀₁ : Type u_1) (Ω₀₂ : Type u_2) [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] (G : Type uG) [MeasurableSpace G] (self : refPackage Ω₀₁ Ω₀₂ G) => self.1`

#### `refPackage.X₀₂` (def)
Lean: `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [inst_2 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → Ω₀₂ → G`
Docstring: The second variable in a package.
Definition: `fun (Ω₀₁ : Type u_1) (Ω₀₂ : Type u_2) [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] (G : Type uG) [MeasurableSpace G] (self : refPackage Ω₀₁ Ω₀₂ G) => self.2`

#### `refPackage.η` (def)
Lean: `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [inst_2 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → ℝ`
Docstring: The constant that parameterizes how good the package is. The argument only works for small enough `η`, typically `≤ 1/9` or `< 1/8`.
Definition: `fun (Ω₀₁ : Type u_1) (Ω₀₂ : Type u_2) [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] (G : Type uG) [MeasurableSpace G] (self : refPackage Ω₀₁ Ω₀₂ G) => self.5`

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

#### `tau` (def)
Lean: `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [AddCommGroup G] → [inst_3 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → {Ω₁ : Type u_11} → {Ω₂ : Type u_12} → [inst : MeasurableSpace Ω₁] → [inst_4 : MeasurableSpace Ω₂] → (Ω₁ → G) → (Ω₂ → G) → Measure Ω₁ → Measure Ω₂ → ℝ`
Docstring: If $X_1,X_2$ are two $G$-valued random variables, then $$ \tau[X_1; X_2] := d[X_1; X_2] + \eta d[X^0_1; X_1] + \eta d[X^0_2; X_2].$$ Here, $X^0_1$ and $X^0_2$ are two random variables fixed once and for all in most of the argument. To lighten notation, We package `X^0_1` and `X^0_2` in a single object named `p`. We denote it as `τ[X₁ ; μ₁ # X₂ ; μ₂ | p]` where `p` is a fixed package containing the information of the reference random variables. When the measurable spaces have a canonical measure `ℙ`, we can use `τ[X₁ # X₂ | p]`
Definition: `fun {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] {G : Type uG} [AddCommGroup G] [MeasurableSpace G] (p : refPackage Ω₀₁ Ω₀₂ G) {Ω₁ : Type u_11} {Ω₂ : Type u_12} [MeasurableSpace Ω₁] [MeasurableSpace Ω₂] (X₁ : Ω₁ → G) (X₂ : Ω₂ → G) (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) => d[X₁; μ₁ # X₂; μ₂] + p.η * d[p.X₀₁; volume # X₁; μ₁] + p.η * d[p.X₀₂; volume # X₂; μ₂]`

## Flagged translations

### `rdist_add_rdist_add_condMutual_eq`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [IsProbabilityMeasure volume] (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₂', X₁'] volume) [Module (ZMod 2) G] : d[X₁ + X₂' # X₂ + X₁'] + d[X₁ | X₁ + X₂' # X₂ | X₂ + X₁'] + I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂'] = 2 * d[X₁ # X₂]`
Lean (full): `∀ {G : Type u_1} [addgroup : AddCommGroup G] [inst : Finite G] [hG : MeasurableSpace G] [inst_1 : MeasurableSingletonClass G] {Ω : Type u_4} [inst_2 : MeasureSpace Ω] [inst_3 : IsProbabilityMeasure.{u_4} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] (X₁ X₂ X₁' X₂' : Ω → G), Measurable X₁ → Measurable X₂ → Measurable X₁' → Measurable X₂' → IdentDistrib X₁ X₁' volume volume → IdentDistrib X₂ X₂' volume volume → iIndepFun (_mΩ := MeasureSpace.toMeasurableSpace) (β := fun (a : Fin (Nat.succ (0 : ℕ)).succ.succ.succ) => G) ![X₁, X₂, X₂', X₁'] volume → ∀ [Module (ZMod (2 : ℕ)) G], d[X₁ + X₂' # X₂ + X₁'] + d[X₁ | X₁ + X₂' # X₂ | X₂ + X₁'] + I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂'] = (2 : ℝ) * d[X₁ # X₂]`
Docstring: The sum of $$ d[X_1+\tilde X_2;X_2+\tilde X_1] + d[X_1|X_1+\tilde X_2; X_2|X_2+\tilde X_1] $$ and $$ I[X_1+ X_2 : \tilde X_1 + X_2 \,|\, X_1 + X_2 + \tilde X_1 + \tilde X_2] $$ is equal to $2k$.
Previous English: Let $G$ be a finite abelian group which is a module over $\mathbb Z/2\mathbb Z$ (i.e. an elementary abelian $2$-group), equipped with a measurable structure in which singletons are measurable. Let $\Omega$ be a probability space, and let $X_1, X_2, \tilde X_1, \tilde X_2 : \Omega \to G$ be measurable random variables with $\tilde X_1$ identically distributed with $X_1$, $\tilde X_2$ identically distributed with $X_2$, and $X_1, X_2, \tilde X_2, \tilde X_1$ jointly independent. Then $$d[X_1+\tilde X_2;\ X_2+\tilde X_1] + d[X_1\mid X_1+\tilde X_2;\ X_2 \mid X_2+\tilde X_1] + I[X_1+X_2 : \tilde X_1 + X_2 \mid X_1+X_2+\tilde X_1+\tilde X_2] = 2\,d[X_1;X_2].$$
Checker's issue: the notations $d[\cdot;\cdot]$, $d[\cdot|\cdot;\cdot|\cdot]$ (Ruzsa distance, conditional) and $I[\cdot:\cdot|\cdot]$ (conditional mutual information) are used without being introduced

### `rdist_of_sums_ge`
Lean (short): `[Finite G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) [IsProbabilityMeasure volume] (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h_min : TauMinimizes p X₁ X₂) : d[X₁ + X₂' # X₂ + X₁'] ≥ d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁ + X₂'] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂ + X₁'] - d[p.X₀₂ # X₂])`
Lean (full): `∀ {G : Type u_1} [addgroup : AddCommGroup G] [Finite G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] {Ω₀₁ : Type u_2} {Ω₀₂ : Type u_3} [inst : MeasureSpace Ω₀₁] [inst_1 : MeasureSpace Ω₀₂] (p : refPackage Ω₀₁ Ω₀₂ G) {Ω : Type u_4} [inst_2 : MeasureSpace Ω] [IsProbabilityMeasure.{u_4} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] (X₁ X₂ X₁' X₂' : Ω → G), Measurable X₁ → Measurable X₂ → Measurable X₁' → Measurable X₂' → TauMinimizes p X₁ X₂ → d[X₁ + X₂' # X₂ + X₁'] ≥ d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁ + X₂'] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂ + X₁'] - d[p.X₀₂ # X₂])`
Docstring: The distance $d[X_1+\tilde X_2; X_2+\tilde X_1]$ is at least $$k - \eta (d[X^0_1; X_1+\tilde X_2] - d[X^0_1; X_1]) - \eta (d[X^0_2; X_2+\tilde X_1] - d[X^0_2; X_2]).$$
Previous English: Let $G$ be a finite abelian group, equipped with a measurable structure in which singletons are measurable. Let $\Omega_{01},\Omega_{02}$ be measure spaces and let $p$ be a reference package for $G$ over them, with reference random variables $X^0_1$ on $\Omega_{01}$ and $X^0_2$ on $\Omega_{02}$ and parameter $\eta$. Let $\Omega$ be a probability space, let $X_1, X_2, \tilde X_1, \tilde X_2 : \Omega \to G$ be measurable, and suppose $(X_1,X_2)$ minimizes $\tau$ for $p$. Then $$d[X_1+\tilde X_2;\ X_2+\tilde X_1] \ge d[X_1;X_2] - \eta\big(d[X^0_1; X_1+\tilde X_2] - d[X^0_1;X_1]\big) - \eta\big(d[X^0_2;X_2+\tilde X_1] - d[X^0_2;X_2]\big).$$
Checker's issue: the notation $d[\cdot;\cdot]$ (Ruzsa distance) is never introduced; $\eta$ is not stated to be real
