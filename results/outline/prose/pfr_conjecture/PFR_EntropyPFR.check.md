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
A definition whose body is shown must be described by what it defines (in words or a formula that agrees with the
body), not only by a paraphrase of its docstring. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

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
Constructor (every field with its type): `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [inst_2 : MeasurableSpace G] → (X₀₁ : Ω₀₁ → G) → (X₀₂ : Ω₀₂ → G) → Measurable X₀₁ → Measurable X₀₂ → (η : ℝ) → (0 : ℝ) < η → (8 : ℝ) * η ≤ (1 : ℝ) → refPackage Ω₀₁ Ω₀₂ G`

#### `refPackage.η` (def)
Lean: `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [inst_2 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → ℝ`
Docstring: The constant that parameterizes how good the package is. The argument only works for small enough `η`, typically `≤ 1/9` or `< 1/8`.
Definition: `fun (Ω₀₁ : Type u_1) (Ω₀₂ : Type u_2) [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] (G : Type uG) [MeasurableSpace G] (self : refPackage Ω₀₁ Ω₀₂ G) => self.5`

#### `ProbabilityTheory.IsUniform` (structure or class)
Lean: `{Ω : Type uΩ} → {S : Type uS} → [mΩ : MeasurableSpace Ω] → Set S → (Ω → S) → autoParam (Measure Ω) IsUniform._auto_1 → Prop`
Docstring: The assertion that the law of $X$ is the uniform probability measure on a finite set $H$. While in applications $H$ will be non-empty finite set, $X$ measurable, and and $μ$ a probability measure, it could be technically convenient to have a definition that works even without these hypotheses. (For instance, `isUniform` would be well-defined, but false, for infinite `H`). This should probably be refactored, requiring instead that `μ.map X = uniformOn H`.
Constructor (every field with its type): `∀ {Ω : Type uΩ} {S : Type uS} [mΩ : MeasurableSpace Ω] {H : Set S} {X : Ω → S} {μ : autoParam (Measure Ω) IsUniform._auto_1}, (∀ ⦃x : S⦄, x ∈ H → ∀ ⦃y : S⦄, y ∈ H → Eq (α := ENNReal) (μ (X ⁻¹' {x}) : ENNReal) (μ (X ⁻¹' {y}) : ENNReal)) → μ (X ⁻¹' Hᶜ) = (0 : ENNReal) → IsUniform H X μ`

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

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

## Translations

### `tau_strictly_decreases`
Lean (short): `[IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [Module (ZMod 2) G] [Finite G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (h_min : TauMinimizes p X₁ X₂) (hpη : p.η = 1 / 9) : d[X₁ # X₂] = 0`
Lean (full): `∀ {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [inst : MeasureSpace Ω₀₁] [inst_1 : MeasureSpace Ω₀₂] {Ω : Type u_3} [mΩ : MeasureSpace Ω] [IsProbabilityMeasure.{u_3} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume] [IsProbabilityMeasure.{u_1} (α := Ω₀₁) (m0 := MeasureSpace.toMeasurableSpace) volume] [IsProbabilityMeasure.{u_2} (α := Ω₀₂) (m0 := MeasureSpace.toMeasurableSpace) volume] {G : Type uG} [inst_5 : AddCommGroup G] [Module (ZMod (2 : ℕ)) G] [Finite G] [inst_8 : MeasurableSpace G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) {X₁ X₂ : Ω → G}, Measurable X₁ → Measurable X₂ → TauMinimizes p X₁ X₂ → p.η = (1 / 9 : ℝ) → d[X₁ # X₂] = (0 : ℝ)`
Docstring: If $d[X_1;X_2] > 0$ then there are $G$-valued random variables $X'_1, X'_2$ such that $\tau[X'_1;X'_2] < \tau[X_1;X_2]$. Phrased in the contrapositive form for convenience of proof.
English: Let $G$ be an additive commutative group which is a module over $\mathbb{Z}/2\mathbb{Z}$ (`ZMod 2`), is finite, and carries a measurable-space structure in which all singletons are measurable. Let $\Omega_{01}$ and $\Omega_{02}$ be measure spaces whose measures (`volume`) are probability measures. Let $\Omega$ be a measure space whose measure $\mathbb{P}$ (`volume`) is a probability measure. For a measurable space $\Omega'$ with measure $\nu$ and $Z : \Omega' \to G$, write $H[Z;\nu]$ = `entropy Z ν` for the entropy of $Z$, defined as the measure entropy `Hm` of the law (pushforward measure) $Z_*\nu$ on $G$ (docstring: entropy of a random variable with values in a finite measurable space). For $Z_1 : \Omega_1 \to G$ with measure $\nu_1$ on $\Omega_1$ and $Z_2 : \Omega_2 \to G$ with measure $\nu_2$ on $\Omega_2$, let $d[Z_1;\nu_1 \# Z_2;\nu_2]$ = `rdist Z₁ Z₂ ν₁ ν₂` be the Ruzsa distance, defined as $H[(x,y) \mapsto x - y;\ (Z_1)_*\nu_1 \otimes (Z_2)_*\nu_2] - H[Z_1;\nu_1]/2 - H[Z_2;\nu_2]/2$, the first term being the entropy of the difference map on $G \times G$ under the product of the two laws (docstring: $H[X'-Y'] - H[X']/2 - H[Y']/2$ for independent copies $X', Y'$ of $X, Y$); when the spaces carry their canonical measures we omit them and write $d[Z_1 \# Z_2]$. Let $p$ be an element of the project structure `refPackage Ω₀₁ Ω₀₂ G` (docstring: a structure that packages all the fixed information in the main argument: the reference spaces, measures and random variables, and the parameter $\eta$); let $X^0_1 = $ `p.X₀₁` $: \Omega_{01} \to G$ and $X^0_2 = $ `p.X₀₂` $: \Omega_{02} \to G$ be its first and second random variables and $\eta = $ `p.η` $\in \mathbb{R}$ its parameter. For $Z_1 : \Omega_1 \to G$, $Z_2 : \Omega_2 \to G$ with measures $\nu_1, \nu_2$, let $\tau[Z_1;\nu_1 \# Z_2;\nu_2 \mid p]$ = `tau p Z₁ Z₂ ν₁ ν₂` $= d[Z_1;\nu_1 \# Z_2;\nu_2] + \eta\, d[X^0_1 \# Z_1;\nu_1] + \eta\, d[X^0_2 \# Z_2;\nu_2]$ (with $\Omega_{01}, \Omega_{02}$ carrying their measures). Let $X_1, X_2 : \Omega \to G$ be measurable functions such that `TauMinimizes p X₁ X₂` holds, i.e. for all probability measures $\nu_1, \nu_2$ on $G$, $\tau[X_1;\mathbb{P} \# X_2;\mathbb{P} \mid p] \le \tau[\mathrm{id}_G;\nu_1 \# \mathrm{id}_G;\nu_2 \mid p]$. If $\eta = 1/9$, then $d[X_1 \# X_2] = 0$ (the Ruzsa distance with respect to $\mathbb{P}$). (Per the docstring, this is the contrapositive form of: if $d[X_1;X_2] > 0$ then there are $G$-valued random variables $X'_1, X'_2$ with $\tau[X'_1;X'_2] < \tau[X_1;X_2]$.)

### `entropic_PFR_conjecture`
Lean (short): `[IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [Module (ZMod 2) G] [Finite G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G) (hpη : p.η = 1 / 9) : ∃ H Ω mΩ U, IsProbabilityMeasure volume ∧ Measurable U ∧ IsUniform (↑H) U volume ∧ d[p.X₀₁ # U] + d[p.X₀₂ # U] ≤ 11 * d[p.X₀₁ # p.X₀₂]`
Lean (full): `∀ {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [inst : MeasureSpace Ω₀₁] [inst_1 : MeasureSpace Ω₀₂] [IsProbabilityMeasure.{u_1} (α := Ω₀₁) (m0 := MeasureSpace.toMeasurableSpace) volume] [IsProbabilityMeasure.{u_2} (α := Ω₀₂) (m0 := MeasureSpace.toMeasurableSpace) volume] {G : Type uG} [inst_4 : AddCommGroup G] [inst_5 : Module (ZMod (2 : ℕ)) G] [Finite G] [inst_7 : MeasurableSpace G] [MeasurableSingletonClass G] (p : refPackage Ω₀₁ Ω₀₂ G), p.η = (1 / 9 : ℝ) → ∃ (H : Submodule (ZMod (2 : ℕ)) G) (Ω : Type uG) (mΩ : MeasureSpace Ω) (U : Ω → G), IsProbabilityMeasure.{uG} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume ∧ Measurable U ∧ IsUniform (↑H) U volume ∧ d[p.X₀₁ # U] + d[p.X₀₂ # U] ≤ (11 : ℝ) * d[p.X₀₁ # p.X₀₂]`
Docstring: `entropic_PFR_conjecture`: For two $G$-valued random variables $X^0_1, X^0_2$, there is some subgroup $H \leq G$ such that $d[X^0_1;U_H] + d[X^0_2;U_H] \le 11 d[X^0_1;X^0_2]$.
English: Let $G$ be an additive commutative group which is a module over $\mathbb{Z}/2\mathbb{Z}$ (`ZMod 2`), is finite, and carries a measurable-space structure in which all singletons are measurable. Let $\Omega_{01}$ and $\Omega_{02}$ be measure spaces whose measures (`volume`) are probability measures. For a measurable space $\Omega'$ with measure $\nu$ and $Z : \Omega' \to G$, write $H[Z;\nu]$ = `entropy Z ν` for the entropy of $Z$, defined as the measure entropy `Hm` of the law (pushforward measure) $Z_*\nu$ on $G$ (docstring: entropy of a random variable with values in a finite measurable space). For $Z_1 : \Omega_1 \to G$ with measure $\nu_1$ on $\Omega_1$ and $Z_2 : \Omega_2 \to G$ with measure $\nu_2$ on $\Omega_2$, let $d[Z_1;\nu_1 \# Z_2;\nu_2]$ = `rdist Z₁ Z₂ ν₁ ν₂` be the Ruzsa distance, defined as $H[(x,y) \mapsto x - y;\ (Z_1)_*\nu_1 \otimes (Z_2)_*\nu_2] - H[Z_1;\nu_1]/2 - H[Z_2;\nu_2]/2$, the first term being the entropy of the difference map on $G \times G$ under the product of the two laws (docstring: $H[X'-Y'] - H[X']/2 - H[Y']/2$ for independent copies $X', Y'$ of $X, Y$); when the spaces carry their canonical measures we omit them and write $d[Z_1 \# Z_2]$. Let $p$ be an element of the project structure `refPackage Ω₀₁ Ω₀₂ G` (docstring: a structure that packages all the fixed information in the main argument: the reference spaces, measures and random variables, and the parameter $\eta$); let $X^0_1 = $ `p.X₀₁` $: \Omega_{01} \to G$ and $X^0_2 = $ `p.X₀₂` $: \Omega_{02} \to G$ be its first and second random variables and $\eta = $ `p.η` $\in \mathbb{R}$ its parameter. Assume $\eta = 1/9$. Then there exist a $\mathbb{Z}/2\mathbb{Z}$-submodule $H_0$ of $G$, a measure space $\Omega$ with measure $\mathbb{P}$, and a function $U : \Omega \to G$ such that $\mathbb{P}$ is a probability measure, $U$ is measurable, $U$ is uniformly distributed on $H_0$ with respect to $\mathbb{P}$ (`IsUniform H₀ U`; docstring: the law of $U$ is the uniform probability measure on the finite set $H_0$), and $$d[X^0_1 \# U] + d[X^0_2 \# U] \le 11\, d[X^0_1 \# X^0_2].$$
