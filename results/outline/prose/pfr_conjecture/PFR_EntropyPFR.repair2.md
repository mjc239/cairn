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
Fields: `X₀₁`, `X₀₂`, `η`, `0`, `8`, `1`

#### `refPackage.η` (def)
Lean: `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [inst_2 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → ℝ`
Docstring: The constant that parameterizes how good the package is. The argument only works for small enough `η`, typically `≤ 1/9` or `< 1/8`.
Definition: `fun (Ω₀₁ : Type u_1) (Ω₀₂ : Type u_2) [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] (G : Type uG) [MeasurableSpace G] (self : refPackage Ω₀₁ Ω₀₂ G) => self.5`

#### `ProbabilityTheory.IsUniform` (structure or class)
Lean: `{Ω : Type uΩ} → {S : Type uS} → [mΩ : MeasurableSpace Ω] → Set S → (Ω → S) → autoParam (Measure Ω) IsUniform._auto_1 → Prop`
Docstring: The assertion that the law of $X$ is the uniform probability measure on a finite set $H$. While in applications $H$ will be non-empty finite set, $X$ measurable, and and $μ$ a probability measure, it could be technically convenient to have a definition that works even without these hypotheses. (For instance, `isUniform` would be well-defined, but false, for infinite `H`). This should probably be refactored, requiring instead that `μ.map X = uniformOn H`.
Fields: `α`, `0`

#### `refPackage.X₀₁` (def)
Lean: `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [inst_2 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → Ω₀₁ → G`
Docstring: The first variable in a package.
Definition: `fun (Ω₀₁ : Type u_1) (Ω₀₂ : Type u_2) [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] (G : Type uG) [MeasurableSpace G] (self : refPackage Ω₀₁ Ω₀₂ G) => self.1`

#### `refPackage.X₀₂` (def)
Lean: `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [inst_2 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → Ω₀₂ → G`
Docstring: The second variable in a package.
Definition: `fun (Ω₀₁ : Type u_1) (Ω₀₂ : Type u_2) [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] (G : Type uG) [MeasurableSpace G] (self : refPackage Ω₀₁ Ω₀₂ G) => self.2`

#### `tau` (def)
Lean: `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [AddCommGroup G] → [inst_3 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → {Ω₁ : Type u_11} → {Ω₂ : Type u_12} → [inst : MeasurableSpace Ω₁] → [inst_4 : MeasurableSpace Ω₂] → (Ω₁ → G) → (Ω₂ → G) → Measure Ω₁ → Measure Ω₂ → ℝ`
Docstring: If $X_1,X_2$ are two $G$-valued random variables, then $$ \tau[X_1; X_2] := d[X_1; X_2] + \eta d[X^0_1; X_1] + \eta d[X^0_2; X_2].$$ Here, $X^0_1$ and $X^0_2$ are two random variables fixed once and for all in most of the argument. To lighten notation, We package `X^0_1` and `X^0_2` in a single object named `p`. We denote it as `τ[X₁ ; μ₁ # X₂ ; μ₂ | p]` where `p` is a fixed package containing the information of the reference random variables. When the measurable spaces have a canonical measure `ℙ`, we can use `τ[X₁ # X₂ | p]`
Definition: `fun {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] {G : Type uG} [AddCommGroup G] [MeasurableSpace G] (p : refPackage Ω₀₁ Ω₀₂ G) {Ω₁ : Type u_11} {Ω₂ : Type u_12} [MeasurableSpace Ω₁] [MeasurableSpace Ω₂] (X₁ : Ω₁ → G) (X₂ : Ω₂ → G) (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) => d[X₁; μ₁ # X₂; μ₂] + p.η * d[p.X₀₁; volume # X₁; μ₁] + p.η * d[p.X₀₂; volume # X₂; μ₂]`

#### `ProbabilityTheory.entropy` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Definition: `fun {Ω : Type u_1} {S : Type u_2} [MeasurableSpace Ω] [MeasurableSpace S] (X : Ω → S) (μ : Measure Ω) => Hm[Measure.map X μ]`

## Flagged translations

### `tau_strictly_decreases`
Lean (short): `[IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [Module (ZMod 2) G] [Finite G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (h_min : TauMinimizes p X₁ X₂) (hpη : p.η = 1 / 9) : d[X₁ # X₂] = 0`
Lean (full): `∀ {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [inst : MeasureSpace Ω₀₁] [inst_1 : MeasureSpace Ω₀₂] {Ω : Type u_3} [mΩ : MeasureSpace Ω] [IsProbabilityMeasure.{u_3} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] [IsProbabilityMeasure.{u_1} (α := Ω₀₁) (m0 := MeasureSpace.toMeasurableSpace) volume] [IsProbabilityMeasure.{u_2} (α := Ω₀₂) (m0 := MeasureSpace.toMeasurableSpace) volume] {G : Type uG} [inst_5 : AddCommGroup G] [Module (ZMod (2 : ℕ)) G] [Finite G] [inst_8 : MeasurableSpace G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) {X₁ X₂ : Ω → G}, Measurable X₁ → Measurable X₂ → TauMinimizes p X₁ X₂ → p.η = (1 / 9 : ℝ) → d[X₁ # X₂] = (0 : ℝ)`
Docstring: If $d[X_1;X_2] > 0$ then there are $G$-valued random variables $X'_1, X'_2$ such that $\tau[X'_1;X'_2] < \tau[X_1;X_2]$. Phrased in the contrapositive form for convenience of proof.
Previous English: Let $G$ be a finite elementary abelian 2-group (i.e. a finite vector space over $\mathbb{F}_2$) with measurable singletons, and suppose the measures on $\Omega_{01}$, $\Omega_{02}$ and $\Omega$ are probability measures. Let $p$ be a reference package with parameter $\eta$, and let $X_1, X_2 : \Omega \to G$ be measurable random variables such that $(X_1,X_2)$ minimizes $\tau$ for $p$. If $\eta = 1/9$, then $d[X_1;X_2] = 0$. (This is the contrapositive of: if $d[X_1;X_2] > 0$ then there are $G$-valued $X_1', X_2'$ with $\tau[X_1';X_2'] < \tau[X_1;X_2]$.)
Checker's issue: The symbol d[X₁;X₂] is never introduced (not named as the Ruzsa distance nor defined), nor is τ defined; 'minimizes τ' is left unexplained although TauMinimizes only compares against identity random variables on (G, ν₁), (G, ν₂) for probability measures ν₁, ν₂.

### `entropic_PFR_conjecture`
Lean (short): `[IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [Module (ZMod 2) G] [Finite G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) (hpη : p.η = 1 / 9) : ∃ H Ω mΩ U, IsProbabilityMeasure volume ∧ Measurable U ∧ IsUniform (↑H) U volume ∧ d[p.X₀₁ # U] + d[p.X₀₂ # U] ≤ 11 * d[p.X₀₁ # p.X₀₂]`
Lean (full): `∀ {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [inst : MeasureSpace Ω₀₁] [inst_1 : MeasureSpace Ω₀₂] [IsProbabilityMeasure.{u_1} (α := Ω₀₁) (m0 := MeasureSpace.toMeasurableSpace) volume] [IsProbabilityMeasure.{u_2} (α := Ω₀₂) (m0 := MeasureSpace.toMeasurableSpace) volume] {G : Type uG} [inst_4 : AddCommGroup G] [inst_5 : Module (ZMod (2 : ℕ)) G] [Finite G] [inst_7 : MeasurableSpace G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G), p.η = (1 / 9 : ℝ) → ∃ (H : Submodule (ZMod (2 : ℕ)) G) (Ω : Type uG) (mΩ : MeasureSpace Ω) (U : Ω → G), IsProbabilityMeasure.{uG} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume ∧ Measurable U ∧ IsUniform (↑H) U volume ∧ d[p.X₀₁ # U] + d[p.X₀₂ # U] ≤ (11 : ℝ) * d[p.X₀₁ # p.X₀₂]`
Docstring: `entropic_PFR_conjecture`: For two $G$-valued random variables $X^0_1, X^0_2$, there is some subgroup $H \leq G$ such that $d[X^0_1;U_H] + d[X^0_2;U_H] \le 11 d[X^0_1;X^0_2]$.
Previous English: Let $G$ be a finite elementary abelian 2-group (i.e. a finite vector space over $\mathbb{F}_2$) with measurable singletons, and suppose the measures on $\Omega_{01}$ and $\Omega_{02}$ are probability measures. Let $p$ be a reference package with reference random variables $X^0_1, X^0_2$ (valued in $G$) and parameter $\eta = 1/9$. Then there exist a subgroup $H \le G$, a probability space $\Omega$ and a measurable random variable $U : \Omega \to G$ uniformly distributed on $H$ such that $$d[X^0_1;U] + d[X^0_2;U] \le 11\, d[X^0_1;X^0_2].$$
Checker's issue: The symbol d[·;·] is never introduced (not named as the Ruzsa distance nor defined).
