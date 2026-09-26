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
type, introduce every symbol, and never use one letter for two things. When a definition's body is shown, say what
it defines, in words or a formula that agrees with the body.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `ProbabilityTheory.condMutualInfo` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → {U : Type u_4} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace U] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → (Ω → U) → autoParam (Measure Ω) condMutualInfo._auto_1 → ℝ`
Docstring: The conditional mutual information `I[X : Y| Z]` is the mutual information of `X| Z=z` and `Y| Z=z`, integrated over `z`.
Definition: `fun {Ω : Type u_1} {S : Type u_2} {T : Type u_3} {U : Type u_4} [MeasurableSpace Ω] [MeasurableSpace S] [inst_1 : MeasurableSpace U] [MeasurableSpace T] (X : Ω → S) (Y : Ω → T) (Z : Ω → U) (μ : Measure Ω) => @integral _ _ _ _ inst_1 (Measure.map Z μ) fun (x : U) => (fun (z : U) => H[X | Z ← z; μ] + H[Y | Z ← z; μ] - H[⟨X, Y⟩ | Z ← z; μ]) x`

#### `TauMinimizes` (def)
Lean: `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [AddCommGroup G] → [inst_3 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → {Ω : Type u_11} → [MeasureSpace Ω] → (Ω → G) → (Ω → G) → Prop`
Docstring: Property recording the fact that two random variables minimize the tau functional. Expressed in terms of measures on the group to avoid quantifying over all spaces, but this implies comparison with any pair of random variables, see Lemma `is_tau_min`.
Definition: `fun {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] {G : Type uG} [AddCommGroup G] [MeasurableSpace G] (p : refPackage Ω₀₁ Ω₀₂ G) {Ω : Type u_11} [MeasureSpace Ω] (X₁ X₂ : Ω → G) => ∀ (ν₁ : Measure G) [IsProbabilityMeasure ν₁] (ν₂ : Measure G) [IsProbabilityMeasure ν₂], τ[X₁ # X₂ | p] ≤ τ[id ; ν₁ # id ; ν₂ | p]`

#### `rdist` (def)
Lean: `{Ω : Type u_1} → {Ω' : Type u_2} → {G : Type u_5} → [mΩ : MeasurableSpace Ω] → [mΩ' : MeasurableSpace Ω'] → [hG : MeasurableSpace G] → [AddCommGroup G] → (Ω → G) → (Ω' → G) → autoParam (Measure Ω) rdist._auto_1 → autoParam (Measure Ω') rdist._auto_3 → ℝ`
Docstring: The Ruzsa distance `rdist X Y` or `d[X ; Y]` between two random variables is defined as `H[X'- Y'] - H[X']/2 - H[Y']/2`, where `X', Y'` are independent copies of `X, Y`.
Definition: `fun {Ω : Type u_1} {Ω' : Type u_2} {G : Type u_5} [MeasurableSpace Ω] [MeasurableSpace Ω'] [MeasurableSpace G] [AddCommGroup G] (X : Ω → G) (Y : Ω' → G) (μ : Measure Ω) (μ' : Measure Ω') => H[fun (x : G × G) => x.1 - x.2; Measure.prod (Measure.map X μ) (Measure.map Y μ')] - H[X; μ] / (2 : ℝ) - H[Y; μ'] / (2 : ℝ)`

#### `refPackage` (structure or class)
Lean: `(Ω₀₁ : Type u_1) → (Ω₀₂ : Type u_2) → [MeasureSpace Ω₀₁] → [MeasureSpace Ω₀₂] → (G : Type uG) → [MeasurableSpace G] → Type (max (max uG u_1) u_2)`
Docstring: A structure that packages all the fixed information in the main argument. In this way, when defining the τ functional, we will only only need to refer to the package once in the notation instead of stating the reference spaces, the reference measures and the reference random variables. The η parameter has now been incorporated into the package, in preparation for being able to manipulate the package.
Constructor (every field with its type): `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [inst_2 : MeasurableSpace G] → (X₀₁ : Ω₀₁ → G) → (X₀₂ : Ω₀₂ → G) → Measurable X₀₁ → Measurable X₀₂ → (η : ℝ) → (0 : ℝ) < η → (8 : ℝ) * η ≤ (1 : ℝ) → refPackage Ω₀₁ Ω₀₂ G`

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

#### `tau` (def)
Lean: `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [AddCommGroup G] → [inst_3 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → {Ω₁ : Type u_11} → {Ω₂ : Type u_12} → [inst : MeasurableSpace Ω₁] → [inst_4 : MeasurableSpace Ω₂] → (Ω₁ → G) → (Ω₂ → G) → Measure Ω₁ → Measure Ω₂ → ℝ`
Docstring: If $X_1,X_2$ are two $G$-valued random variables, then $$ \tau[X_1; X_2] := d[X_1; X_2] + \eta d[X^0_1; X_1] + \eta d[X^0_2; X_2].$$ Here, $X^0_1$ and $X^0_2$ are two random variables fixed once and for all in most of the argument. To lighten notation, We package `X^0_1` and `X^0_2` in a single object named `p`. We denote it as `τ[X₁ ; μ₁ # X₂ ; μ₂ | p]` where `p` is a fixed package containing the information of the reference random variables. When the measurable spaces have a canonical measure `ℙ`, we can use `τ[X₁ # X₂ | p]`
Definition: `fun {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] {G : Type uG} [AddCommGroup G] [MeasurableSpace G] (p : refPackage Ω₀₁ Ω₀₂ G) {Ω₁ : Type u_11} {Ω₂ : Type u_12} [MeasurableSpace Ω₁] [MeasurableSpace Ω₂] (X₁ : Ω₁ → G) (X₂ : Ω₂ → G) (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) => d[X₁; μ₁ # X₂; μ₂] + p.η * d[p.X₀₁; volume # X₁; μ₁] + p.η * d[p.X₀₂; volume # X₂; μ₂]`

#### `refPackage.X₀₁` (def)
Lean: `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [inst_2 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → Ω₀₁ → G`
Docstring: The first variable in a package.
Definition: `fun (Ω₀₁ : Type u_1) (Ω₀₂ : Type u_2) [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] (G : Type uG) [MeasurableSpace G] (self : refPackage Ω₀₁ Ω₀₂ G) => self.1`

#### `refPackage.X₀₂` (def)
Lean: `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [inst_2 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → Ω₀₂ → G`
Docstring: The second variable in a package.
Definition: `fun (Ω₀₁ : Type u_1) (Ω₀₂ : Type u_2) [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] (G : Type uG) [MeasurableSpace G] (self : refPackage Ω₀₁ Ω₀₂ G) => self.2`

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

## Flagged translations

### `second_estimate_aux`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [Module (ZMod 2) G] [MeasurableAdd₂ G] [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] (p : refPackage Ω₀₁ Ω₀₂ G) [IsProbabilityMeasure volume] (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₁', X₂'] volume) (h_min : TauMinimizes p X₁ X₂) : d[X₁ # X₁] + d[X₂ # X₂] ≤ 2 * (d[X₁ # X₂] + (2 * p.η * d[X₁ # X₂] - I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂']) / (1 - p.η))`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [Finite G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] [Module (ZMod (2 : ℕ)) G] [MeasurableAdd₂ G] {Ω₀₁ : Type u_2} {Ω₀₂ : Type u_3} [inst_5 : MeasureSpace Ω₀₁] [inst_6 : MeasureSpace Ω₀₂] [IsProbabilityMeasure.{u_2} (α := Ω₀₁) (m0 := MeasureSpace.toMeasurableSpace) volume] [IsProbabilityMeasure.{u_3} (α := Ω₀₂) (m0 := MeasureSpace.toMeasurableSpace) volume] (p : refPackage Ω₀₁ Ω₀₂ G) {Ω : Type u_4} [inst_9 : MeasureSpace Ω] [IsProbabilityMeasure.{u_4} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] (X₁ X₂ X₁' X₂' : Ω → G), Measurable X₁ → Measurable X₂ → Measurable X₁' → Measurable X₂' → IdentDistrib X₁ X₁' volume volume → IdentDistrib X₂ X₂' volume volume → iIndepFun (_mΩ := MeasureSpace.toMeasurableSpace) (β := fun (a : Fin (Nat.succ (0 : ℕ)).succ.succ.succ) => G) ![X₁, X₂, X₁', X₂'] volume → TauMinimizes p X₁ X₂ → d[X₁ # X₁] + d[X₂ # X₂] ≤ (2 : ℝ) * (d[X₁ # X₂] + ((2 : ℝ) * p.η * d[X₁ # X₂] - I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂']) / ((1 : ℝ) - p.η))`
Previous English: Let $G$ be a finite additive abelian group which is a module over $\mathbb{Z}/2\mathbb{Z}$, equipped with a measurable space structure in which singletons are measurable and addition $G \times G \to G$ is measurable. Let $\Omega_{01}$ and $\Omega_{02}$ be measure spaces whose measures are probability measures, and let $p$ be a reference package (the project structure `refPackage`) over $\Omega_{01}, \Omega_{02}, G$; it provides random variables $X^0_1 : \Omega_{01} \to G$, $X^0_2 : \Omega_{02} \to G$ and a real parameter $\eta$. Let $\Omega$ be a measure space whose measure $\mathbb{P}$ is a probability measure, and let $X_1, X_2, X_1', X_2' : \Omega \to G$ be measurable functions such that $X_1'$ has the same distribution as $X_1$, $X_2'$ has the same distribution as $X_2$, and the family $(X_1, X_2, X_1', X_2')$ is jointly independent under $\mathbb{P}$. Notation: $H[\cdot]$ denotes the entropy of (the distribution of) a random variable; for $G$-valued random variables $Y$ (with law $\alpha$) and $Z$ (with law $\beta$), on possibly different probability spaces, the Ruzsa distance is $d[Y; Z] = H[\text{law of } u - v \text{ for } (u,v) \sim \alpha \otimes \beta] - H[Y]/2 - H[Z]/2$; for random variables $A, B, C$ on $\Omega$, $I[A : B \mid C]$ is the conditional mutual information, the integral against the distribution of $C$ of $c \mapsto H[A \mid C = c] + H[B \mid C = c] - H[(A, B) \mid C = c]$; and $\tau[Y; Z] = d[Y; Z] + \eta\, d[X^0_1; Y] + \eta\, d[X^0_2; Z]$ (reference variables taken with the measures of $\Omega_{01}, \Omega_{02}$). Assume $(X_1, X_2)$ minimizes $\tau$ in the sense that $\tau[X_1; X_2] \le \tau[\mathrm{id}_G; \mathrm{id}_G]$ whenever the two identity maps are taken as random variables on $(G, \nu_1)$ and $(G, \nu_2)$ for arbitrary probability measures $\nu_1, \nu_2$ on $G$. Write $S = X_1 + X_2 + X_1' + X_2'$ (pointwise sum). Then $$d[X_1; X_1] + d[X_2; X_2] \le 2\left(d[X_1; X_2] + \frac{2\eta\, d[X_1; X_2] - I[X_1 + X_2 : X_1' + X_2 \mid S]}{1 - \eta}\right).$$
Checker's issue: The English describes the refPackage p as providing random variables X⁰₁, X⁰₂ and 'a real parameter η', omitting the structure's hypotheses that X⁰₁, X⁰₂ are measurable and 0 < η with 8η ≤ 1; the statement (with its division by 1-η) therefore reads as holding for arbitrary real η, which is more than was proved.

### `second_estimate`
Lean (short): `[Finite G] [MeasurableSingletonClass G] [Module (ZMod 2) G] [MeasurableAdd₂ G] [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] (p : refPackage Ω₀₁ Ω₀₂ G) [IsProbabilityMeasure volume] (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h₂ : IdentDistrib X₂ X₂' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₁', X₂'] volume) (h_min : TauMinimizes p X₁ X₂) : I[X₁ + X₂ : X₁' + X₁|X₁ + X₂ + X₁' + X₂'] ≤ 2 * p.η * d[X₁ # X₂] + 2 * p.η * (2 * p.η * d[X₁ # X₂] - I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂']) / (1 - p.η)`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [Finite G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] [Module (ZMod (2 : ℕ)) G] [MeasurableAdd₂ G] {Ω₀₁ : Type u_2} {Ω₀₂ : Type u_3} [inst_5 : MeasureSpace Ω₀₁] [inst_6 : MeasureSpace Ω₀₂] [IsProbabilityMeasure.{u_2} (α := Ω₀₁) (m0 := MeasureSpace.toMeasurableSpace) volume] [IsProbabilityMeasure.{u_3} (α := Ω₀₂) (m0 := MeasureSpace.toMeasurableSpace) volume] (p : refPackage Ω₀₁ Ω₀₂ G) {Ω : Type u_4} [inst_9 : MeasureSpace Ω] [IsProbabilityMeasure.{u_4} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] (X₁ X₂ X₁' X₂' : Ω → G), Measurable X₁ → Measurable X₂ → Measurable X₁' → Measurable X₂' → IdentDistrib X₁ X₁' volume volume → IdentDistrib X₂ X₂' volume volume → iIndepFun (_mΩ := MeasureSpace.toMeasurableSpace) (β := fun (a : Fin (Nat.succ (0 : ℕ)).succ.succ.succ) => G) ![X₁, X₂, X₁', X₂'] volume → TauMinimizes p X₁ X₂ → I[X₁ + X₂ : X₁' + X₁|X₁ + X₂ + X₁' + X₂'] ≤ (2 : ℝ) * p.η * d[X₁ # X₂] + (2 : ℝ) * p.η * ((2 : ℝ) * p.η * d[X₁ # X₂] - I[X₁ + X₂ : X₁' + X₂|X₁ + X₂ + X₁' + X₂']) / ((1 : ℝ) - p.η)`
Docstring: $$ I_2 \leq 2 \eta k + \frac{2 \eta (2 \eta k - I_1)}{1 - \eta}.$$
Previous English: Let $G$ be a finite additive abelian group which is a module over $\mathbb{Z}/2\mathbb{Z}$, equipped with a measurable space structure in which singletons are measurable and addition $G \times G \to G$ is measurable. Let $\Omega_{01}$ and $\Omega_{02}$ be measure spaces whose measures are probability measures, and let $p$ be a reference package (the project structure `refPackage`) over $\Omega_{01}, \Omega_{02}, G$; it provides random variables $X^0_1 : \Omega_{01} \to G$, $X^0_2 : \Omega_{02} \to G$ and a real parameter $\eta$. Let $\Omega$ be a measure space whose measure $\mathbb{P}$ is a probability measure, and let $X_1, X_2, X_1', X_2' : \Omega \to G$ be measurable functions such that $X_1'$ has the same distribution as $X_1$, $X_2'$ has the same distribution as $X_2$, and the family $(X_1, X_2, X_1', X_2')$ is jointly independent under $\mathbb{P}$. Notation: $H[\cdot]$ denotes the entropy of (the distribution of) a random variable; for $G$-valued random variables $Y$ (with law $\alpha$) and $Z$ (with law $\beta$), on possibly different probability spaces, the Ruzsa distance is $d[Y; Z] = H[\text{law of } u - v \text{ for } (u,v) \sim \alpha \otimes \beta] - H[Y]/2 - H[Z]/2$; for random variables $A, B, C$ on $\Omega$, $I[A : B \mid C]$ is the conditional mutual information, the integral against the distribution of $C$ of $c \mapsto H[A \mid C = c] + H[B \mid C = c] - H[(A, B) \mid C = c]$; and $\tau[Y; Z] = d[Y; Z] + \eta\, d[X^0_1; Y] + \eta\, d[X^0_2; Z]$ (reference variables taken with the measures of $\Omega_{01}, \Omega_{02}$). Assume $(X_1, X_2)$ minimizes $\tau$ in the sense that $\tau[X_1; X_2] \le \tau[\mathrm{id}_G; \mathrm{id}_G]$ whenever the two identity maps are taken as random variables on $(G, \nu_1)$ and $(G, \nu_2)$ for arbitrary probability measures $\nu_1, \nu_2$ on $G$. Write $S = X_1 + X_2 + X_1' + X_2'$ (pointwise sum). Then $$I[X_1 + X_2 : X_1' + X_1 \mid S] \le 2\eta\, d[X_1; X_2] + \frac{2\eta\left(2\eta\, d[X_1; X_2] - I[X_1 + X_2 : X_1' + X_2 \mid S]\right)}{1 - \eta}.$$
Checker's issue: The English describes the refPackage p as providing random variables X⁰₁, X⁰₂ and 'a real parameter η', omitting the structure's hypotheses that X⁰₁, X⁰₂ are measurable and 0 < η with 8η ≤ 1; the statement (with its division by 1-η) therefore reads as holding for arbitrary real η, which is more than was proved.
