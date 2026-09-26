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

#### `rdist` (def)
Lean: `{Ω : Type u_1} → {Ω' : Type u_2} → {G : Type u_5} → [mΩ : MeasurableSpace Ω] → [mΩ' : MeasurableSpace Ω'] → [hG : MeasurableSpace G] → [AddCommGroup G] → (Ω → G) → (Ω' → G) → autoParam (Measure Ω) rdist._auto_1 → autoParam (Measure Ω') rdist._auto_3 → ℝ`
Docstring: The Ruzsa distance `rdist X Y` or `d[X ; Y]` between two random variables is defined as `H[X'- Y'] - H[X']/2 - H[Y']/2`, where `X', Y'` are independent copies of `X, Y`.
Definition: `fun {Ω : Type u_1} {Ω' : Type u_2} {G : Type u_5} [MeasurableSpace Ω] [MeasurableSpace Ω'] [MeasurableSpace G] [AddCommGroup G] (X : Ω → G) (Y : Ω' → G) (μ : Measure Ω) (μ' : Measure Ω') => H[fun (x : G × G) => x.1 - x.2; Measure.prod (Measure.map X μ) (Measure.map Y μ')] - H[X; μ] / (2 : ℝ) - H[Y; μ'] / (2 : ℝ)`

#### `condRuzsaDist` (def)
Lean: `{Ω : Type u_1} → {Ω' : Type u_2} → {G : Type u_5} → {S : Type u_6} → {T : Type u_7} → [mΩ : MeasurableSpace Ω] → [mΩ' : MeasurableSpace Ω'] → [hG : MeasurableSpace G] → [AddCommGroup G] → [MeasurableSpace S] → [MeasurableSpace T] → [Countable G] → [MeasurableSingletonClass G] → (Ω → G) → (Ω → S) → (Ω' → G) → (Ω' → T) → (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) → [IsFiniteMeasure μ] → (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) → [IsFiniteMeasure μ'] → ℝ`
Docstring: The conditional Ruzsa distance `d[X|Z ; Y|W]`.
Definition: `fun {Ω : Type u_1} {Ω' : Type u_2} {G : Type u_5} {S : Type u_6} {T : Type u_7} [MeasurableSpace Ω] [MeasurableSpace Ω'] [MeasurableSpace G] [AddCommGroup G] [MeasurableSpace S] [MeasurableSpace T] [Countable G] [MeasurableSingletonClass G] (X : Ω → G) (Z : Ω → S) (Y : Ω' → G) (W : Ω' → T) (μ : Measure Ω) [IsFiniteMeasure μ] (μ' : Measure Ω') [IsFiniteMeasure μ'] => dk[condDistrib X Z μ ; Measure.map Z μ # condDistrib Y W μ' ; Measure.map W μ']`

#### `condRuzsaDist'` (def)
Lean: `{Ω : Type u_1} → {Ω' : Type u_2} → {G : Type u_5} → {T : Type u_7} → [mΩ : MeasurableSpace Ω] → [mΩ' : MeasurableSpace Ω'] → [hG : MeasurableSpace G] → [AddCommGroup G] → [MeasurableSpace T] → [Countable G] → [MeasurableSingletonClass G] → (Ω → G) → (Ω' → G) → (Ω' → T) → autoParam (Measure Ω) condRuzsaDist'._auto_1 → (μ' : autoParam (Measure Ω') condRuzsaDist'._auto_3) → [IsFiniteMeasure μ'] → ℝ`
Docstring: The conditional Ruzsa distance `d[X ; Y|W]`.
Definition: `fun {Ω : Type u_1} {Ω' : Type u_2} {G : Type u_5} {T : Type u_7} [MeasurableSpace Ω] [MeasurableSpace Ω'] [MeasurableSpace G] [AddCommGroup G] [MeasurableSpace T] [Countable G] [MeasurableSingletonClass G] (X : Ω → G) (Y : Ω' → G) (W : Ω' → T) (μ : Measure Ω) (μ' : Measure Ω') [IsFiniteMeasure μ'] => dk[Kernel.const Unit (Measure.map X μ) ; Measure.dirac () # condDistrib Y W μ' ; Measure.map W μ']`

#### `ProbabilityTheory.entropy` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Definition: `fun {Ω : Type u_1} {S : Type u_2} [MeasurableSpace Ω] [MeasurableSpace S] (X : Ω → S) (μ : Measure Ω) => Hm[Measure.map X μ]`

#### `ProbabilityTheory.Kernel.rdist` (def)
Lean: `{T : Type u_1} → {T' : Type u_2} → {G : Type u_4} → [inst : MeasurableSpace T] → [inst_1 : MeasurableSpace T'] → [inst_2 : MeasurableSpace G] → [AddCommGroup G] → Kernel T G → Kernel T' G → Measure T → Measure T' → ℝ`
Docstring: The Rusza distance between two kernels taking values in the same space, defined as the average Rusza distance between the image measures.
Definition: `fun {T : Type u_1} {T' : Type u_2} {G : Type u_4} [MeasurableSpace T] [MeasurableSpace T'] [MeasurableSpace G] [AddCommGroup G] (κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') => ∫ (x : T × T'), (fun (p : T × T') => Kernel.rdistm.{u_4} (G := G) (κ p.1) (η p.2)) x ∂μ.prod ν`

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

#### `ProbabilityTheory.Kernel.rdistm` (def)
Lean: `{G : Type u_4} → [inst : MeasurableSpace G] → [AddCommGroup G] → Measure G → Measure G → ℝ`
Docstring: The Rusza distance between two measures, defined as `H[X - Y] - H[X]/2 - H[Y]/2` where `X` and `Y` are independent variables distributed according to the two measures.
Definition: `fun {G : Type u_4} [MeasurableSpace G] [AddCommGroup G] (μ ν : Measure G) => measureEntropy (S := G) (Measure.map (fun (x : G × G) => x.1 - x.2) (μ.prod ν)) - Hm[μ] / (2 : ℝ) - Hm[ν] / (2 : ℝ)`

## Translations

### `refPackage`
Lean (short): `(Ω₀₁ : Type u_1) (Ω₀₂ : Type u_2) (G : Type uG) : Type (max (max uG u_1) u_2)`
Lean (full): `(Ω₀₁ : Type u_1) → (Ω₀₂ : Type u_2) → [MeasureSpace Ω₀₁] → [MeasureSpace Ω₀₂] → (G : Type uG) → [MeasurableSpace G] → Type (max (max uG u_1) u_2)`
Constructor (every field with its type): `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [inst_2 : MeasurableSpace G] → (X₀₁ : Ω₀₁ → G) → (X₀₂ : Ω₀₂ → G) → Measurable X₀₁ → Measurable X₀₂ → (η : ℝ) → (0 : ℝ) < η → (8 : ℝ) * η ≤ (1 : ℝ) → refPackage Ω₀₁ Ω₀₂ G`
Docstring: A structure that packages all the fixed information in the main argument. In this way, when defining the τ functional, we will only only need to refer to the package once in the notation instead of stating the reference spaces, the reference measures and the reference random variables. The η parameter has now been incorporated into the package, in preparation for being able to manipulate the package.
English: For measure spaces $\Omega_{01}$ and $\Omega_{02}$ (types each equipped with a canonical measure) and a measurable space $G$, `refPackage Ω₀₁ Ω₀₂ G` is a type (a structure). According to its docstring, it packages all the fixed information in the main argument, so that when defining the $\tau$ functional one only needs to refer to the package once in the notation instead of stating the reference spaces, the reference measures and the reference random variables; the docstring adds that the parameter $\eta$ has been incorporated into the package.

### `tau`
Lean (short): `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω₁ → G) (X₂ : Ω₂ → G) (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) : ℝ`
Lean (full): `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [AddCommGroup G] → [inst_3 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → {Ω₁ : Type u_11} → {Ω₂ : Type u_12} → [inst : MeasurableSpace Ω₁] → [inst_4 : MeasurableSpace Ω₂] → (Ω₁ → G) → (Ω₂ → G) → Measure Ω₁ → Measure Ω₂ → ℝ`
Definition: `fun {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] {G : Type uG} [AddCommGroup G] [MeasurableSpace G] (p : refPackage Ω₀₁ Ω₀₂ G) {Ω₁ : Type u_11} {Ω₂ : Type u_12} [MeasurableSpace Ω₁] [MeasurableSpace Ω₂] (X₁ : Ω₁ → G) (X₂ : Ω₂ → G) (μ₁ : Measure Ω₁) (μ₂ : Measure Ω₂) => d[X₁; μ₁ # X₂; μ₂] + p.η * d[p.X₀₁; volume # X₁; μ₁] + p.η * d[p.X₀₂; volume # X₂; μ₂]`
Docstring: If $X_1,X_2$ are two $G$-valued random variables, then $$ \tau[X_1; X_2] := d[X_1; X_2] + \eta d[X^0_1; X_1] + \eta d[X^0_2; X_2].$$ Here, $X^0_1$ and $X^0_2$ are two random variables fixed once and for all in most of the argument. To lighten notation, We package `X^0_1` and `X^0_2` in a single object named `p`. We denote it as `τ[X₁ ; μ₁ # X₂ ; μ₂ | p]` where `p` is a fixed package containing the information of the reference random variables. When the measurable spaces have a canonical measure `ℙ`, we can use `τ[X₁ # X₂ | p]`
English: Let $\Omega_{01}$ and $\Omega_{02}$ be measure spaces, let $G$ be an abelian group (additive commutative group) equipped with a measurable space structure, and let $p$ be a reference package `refPackage Ω₀₁ Ω₀₂ G`. For measurable spaces $\Omega_1, \Omega_2$, functions $X_1 : \Omega_1 \to G$ and $X_2 : \Omega_2 \to G$, and measures $\mu_1$ on $\Omega_1$ and $\mu_2$ on $\Omega_2$, define a real number $\tau[X_1; \mu_1 \# X_2; \mu_2 \mid p]$. According to its docstring, $\tau[X_1; X_2] := d[X_1; X_2] + \eta\, d[X^0_1; X_1] + \eta\, d[X^0_2; X_2]$, where $X^0_1, X^0_2$ are reference random variables fixed once and for all and packaged in $p$.

### `TauMinimizes`
Lean (short): `(p : refPackage Ω₀₁ Ω₀₂ G) (X₁ : Ω → G) (X₂ : Ω → G) : Prop`
Lean (full): `{Ω₀₁ : Type u_1} → {Ω₀₂ : Type u_2} → [inst : MeasureSpace Ω₀₁] → [inst_1 : MeasureSpace Ω₀₂] → {G : Type uG} → [AddCommGroup G] → [inst_3 : MeasurableSpace G] → refPackage Ω₀₁ Ω₀₂ G → {Ω : Type u_11} → [MeasureSpace Ω] → (Ω → G) → (Ω → G) → Prop`
Definition: `fun {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [MeasureSpace Ω₀₁] [MeasureSpace Ω₀₂] {G : Type uG} [AddCommGroup G] [MeasurableSpace G] (p : refPackage Ω₀₁ Ω₀₂ G) {Ω : Type u_11} [MeasureSpace Ω] (X₁ X₂ : Ω → G) => ∀ (ν₁ : Measure G) [IsProbabilityMeasure ν₁] (ν₂ : Measure G) [IsProbabilityMeasure ν₂], τ[X₁ # X₂ | p] ≤ τ[id ; ν₁ # id ; ν₂ | p]`
Docstring: Property recording the fact that two random variables minimize the tau functional. Expressed in terms of measures on the group to avoid quantifying over all spaces, but this implies comparison with any pair of random variables, see Lemma `is_tau_min`.
English: Let $\Omega_{01}$ and $\Omega_{02}$ be measure spaces, let $G$ be an abelian group (additive commutative group) equipped with a measurable space structure, and let $p$ be a reference package `refPackage Ω₀₁ Ω₀₂ G`. For a measure space $\Omega$ and functions $X_1, X_2 : \Omega \to G$, `TauMinimizes p X₁ X₂` is a proposition. According to its docstring, it records the fact that $X_1, X_2$ minimize the $\tau$ functional; it is expressed in terms of measures on the group to avoid quantifying over all spaces, but it implies comparison with any pair of random variables (see Lemma `is_tau_min`).

### `distance_ge_of_min`
Lean (short): `(p : refPackage Ω₀₁ Ω₀₂ G) [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] (h : TauMinimizes p X₁ X₂) (h1 : Measurable X₁') (h2 : Measurable X₂') : d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁'] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂'] - d[p.X₀₂ # X₂]) ≤ d[X₁' # X₂']`
Lean (full): `∀ {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [inst : MeasureSpace Ω₀₁] [inst_1 : MeasureSpace Ω₀₂] {G : Type uG} [inst_2 : AddCommGroup G] [inst_3 : MeasurableSpace G] (p : refPackage Ω₀₁ Ω₀₂ G) {Ω : Type u_3} {Ω'₁ : Type u_7} {Ω'₂ : Type u_8} [inst_4 : MeasureSpace Ω] [hΩ₁ : MeasureSpace Ω'₁] [hΩ₂ : MeasureSpace Ω'₂] [IsProbabilityMeasure.{u_7} (α := Ω'₁) (m0 := MeasureSpace.toMeasurableSpace) volume] [IsProbabilityMeasure.{u_8} (α := Ω'₂) (m0 := MeasureSpace.toMeasurableSpace) volume] {X₁ X₂ : Ω → G} {X₁' : Ω'₁ → G} {X₂' : Ω'₂ → G}, TauMinimizes p X₁ X₂ → Measurable X₁' → Measurable X₂' → d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁'] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂'] - d[p.X₀₂ # X₂]) ≤ d[X₁' # X₂']`
Docstring: Let `X₁` and `X₂` be tau-minimizers associated to `p`, with $d[X_1,X_2]=k$, then $$ d[X'_1;X'_2] \geq k - \eta (d[X^0_1;X'_1] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2] - d[X^0_2;X_2] )$$ for any $G$-valued random variables $X'_1,X'_2$.
English: Let $G$ be an additive commutative group equipped with a measurable space structure, let $\Omega_{01}$ and $\Omega_{02}$ be measure spaces, and let $p$ be a reference package (`refPackage`) on $\Omega_{01}, \Omega_{02}, G$, with first and second reference random variables $X^0_1 = p.X_{01} : \Omega_{01} \to G$ and $X^0_2 = p.X_{02} : \Omega_{02} \to G$ and real parameter $\eta = p.\eta$. Let $\Omega$, $\Omega'_1$, $\Omega'_2$ be measure spaces, where the canonical measures of $\Omega'_1$ and $\Omega'_2$ are probability measures. Throughout, for random variables $Y : \Omega_Y \to G$ and $Z : \Omega_Z \to G$ on measure spaces, $d[Y;Z]$ denotes the Ruzsa distance (`rdist`) of $Y$ and $Z$ with respect to the canonical measures $\mathbb{P}_Y$, $\mathbb{P}_Z$ of their domains, namely $d[Y;Z] = H[\pi_{(Y_*\mathbb{P}_Y) \otimes (Z_*\mathbb{P}_Z)}] - H[Y]/2 - H[Z]/2$, where the first term is the entropy of the random variable $(x,y) \mapsto x - y$ on $G \times G$ under the product of the laws of $Y$ and $Z$, and $H[Y]$ is the entropy of (the law of) $Y$. Let $X_1, X_2 : \Omega \to G$ satisfy `TauMinimizes p X₁ X₂`, i.e. for all probability measures $\nu_1, \nu_2$ on $G$, $\tau[X_1 ; X_2 \mid p] \le \tau[\mathrm{id};\nu_1 ; \mathrm{id};\nu_2 \mid p]$, where the $\tau$ functional is $\tau[Y;\mu ; Z;\mu' \mid p] = d[Y;\mu \,\#\, Z;\mu'] + \eta\, d[X^0_1 ; Y;\mu] + \eta\, d[X^0_2 ; Z;\mu']$ (Ruzsa distances with respect to the indicated measures, the canonical measures being used for $X^0_1, X^0_2$ and, in $\tau[X_1 ; X_2 \mid p]$, for $X_1, X_2$). Let $X_1' : \Omega'_1 \to G$ and $X_2' : \Omega'_2 \to G$ be measurable. Then $$d[X_1;X_2]-\eta\left(d[X^0_1;X_1']-d[X^0_1;X_1]\right)-\eta\left(d[X^0_2;X_2']-d[X^0_2;X_2]\right)\le d[X_1';X_2'].$$

### `condRuzsaDistance_ge_of_min`
Lean (short): `[Finite G] (p : refPackage Ω₀₁ Ω₀₂ G) [IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [MeasurableSingletonClass G] [Finite S] [MeasurableSingletonClass S] [Finite T] [MeasurableSingletonClass T] (h : TauMinimizes p X₁ X₂) (h1 : Measurable X₁') (h2 : Measurable X₂') (Z : Ω'₁ → S) (W : Ω'₂ → T) (hZ : Measurable Z) (hW : Measurable W) : d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁' | Z] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂' | W] - d[p.X₀₂ # X₂]) ≤ d[X₁' | Z # X₂' | W]`
Lean (full): `∀ {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [inst : MeasureSpace Ω₀₁] [inst_1 : MeasureSpace Ω₀₂] {G : Type uG} [inst_2 : AddCommGroup G] [inst_3 : Finite G] [inst_4 : MeasurableSpace G] (p : refPackage Ω₀₁ Ω₀₂ G) {Ω : Type u_3} {Ω'₁ : Type u_7} {Ω'₂ : Type u_8} {S : Type u_9} {T : Type u_10} [inst_5 : MeasureSpace Ω] [hΩ₁ : MeasureSpace Ω'₁] [hΩ₂ : MeasureSpace Ω'₂] [inst_6 : IsProbabilityMeasure.{u_7} (α := Ω'₁) (m0 := MeasureSpace.toMeasurableSpace) volume] [inst_7 : IsProbabilityMeasure.{u_8} (α := Ω'₂) (m0 := MeasureSpace.toMeasurableSpace) volume] {X₁ X₂ : Ω → G} {X₁' : Ω'₁ → G} {X₂' : Ω'₂ → G} [inst_8 : MeasurableSingletonClass G] [Finite S] [inst_10 : MeasurableSpace S] [MeasurableSingletonClass S] [Finite T] [inst_13 : MeasurableSpace T] [MeasurableSingletonClass T], TauMinimizes p X₁ X₂ → Measurable X₁' → Measurable X₂' → ∀ (Z : Ω'₁ → S) (W : Ω'₂ → T), Measurable Z → Measurable W → d[X₁ # X₂] - p.η * (d[p.X₀₁ # X₁' | Z] - d[p.X₀₁ # X₁]) - p.η * (d[p.X₀₂ # X₂' | W] - d[p.X₀₂ # X₂]) ≤ d[X₁' | Z # X₂' | W]`
Docstring: For any $G$-valued random variables $X'_1,X'_2$ and random variables $Z,W$, one can lower bound $d[X'_1|Z;X'_2|W]$ by $$k - \eta (d[X^0_1;X'_1|Z] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2|W] - d[X^0_2;X_2] ).$$
English: Let $G$ be a finite additive commutative group equipped with a measurable space structure in which singletons are measurable. Let $\Omega_{01}$ and $\Omega_{02}$ be measure spaces (with measures $\mathbb{P}_{01}$, $\mathbb{P}_{02}$ respectively), and let $p$ be a reference package (`refPackage Ω₀₁ Ω₀₂ G`), with reference variables $X^0_1 : \Omega_{01} \to G$ (`p.X₀₁`), $X^0_2 : \Omega_{02} \to G$ (`p.X₀₂`) and real parameter $\eta$ (`p.η`). Let $\Omega$ be a measure space with measure $\mathbb{P}$, and let $X_1, X_2 : \Omega \to G$ be functions such that $(X_1, X_2)$ minimizes the $\tau$-functional for $p$ (`TauMinimizes p X₁ X₂`), i.e. $\tau[X_1; X_2 \mid p] \le \tau[\mathrm{id}; \nu_1 \,\#\, \mathrm{id}; \nu_2 \mid p]$ for all probability measures $\nu_1, \nu_2$ on $G$, where $\tau[Y_1; \mu_1 \# Y_2; \mu_2 \mid p] = d[Y_1;\mu_1 \# Y_2;\mu_2] + \eta\, d[X^0_1; \mathbb{P}_{01} \# Y_1; \mu_1] + \eta\, d[X^0_2; \mathbb{P}_{02} \# Y_2; \mu_2]$. Let $\Omega'_1$ and $\Omega'_2$ be measure spaces whose measures $\mathbb{P}'_1$, $\mathbb{P}'_2$ are probability measures, and let $X'_1 : \Omega'_1 \to G$ and $X'_2 : \Omega'_2 \to G$ be measurable. Let $S$ and $T$ be finite types, each equipped with a measurable space structure in which singletons are measurable, and let $Z : \Omega'_1 \to S$ and $W : \Omega'_2 \to T$ be measurable. Here $d[\cdot\,;\cdot]$ is the Ruzsa distance `rdist` (with respect to the measures of the respective spaces), $d[X^0_1; X'_1 \mid Z]$ is the conditional Ruzsa distance `condRuzsaDist'` of $X^0_1$ (on $\Omega_{01}$) and $X'_1$ given $Z$ (and similarly $d[X^0_2; X'_2 \mid W]$), and $d[X'_1 \mid Z; X'_2 \mid W]$ is the conditional Ruzsa distance `condRuzsaDist`. Then $$d[X_1;X_2]-\eta\left(d[X^0_1;X_1'\mid Z]-d[X^0_1;X_1]\right)-\eta\left(d[X^0_2;X_2'\mid W]-d[X^0_2;X_2]\right)\le d[X_1'\mid Z;X_2'\mid W].$$

### `tau_minimizer_exists`
Lean (short): `[IsProbabilityMeasure volume] [IsProbabilityMeasure volume] [Finite G] (p : refPackage Ω₀₁ Ω₀₂ G) [MeasurableSingletonClass G] : ∃ Ω x X₁ X₂, Measurable X₁ ∧ Measurable X₂ ∧ IsProbabilityMeasure volume ∧ TauMinimizes p X₁ X₂`
Lean (full): `∀ {Ω₀₁ : Type u_1} {Ω₀₂ : Type u_2} [inst : MeasureSpace Ω₀₁] [inst_1 : MeasureSpace Ω₀₂] [IsProbabilityMeasure.{u_1} (α := Ω₀₁) (m0 := MeasureSpace.toMeasurableSpace) volume] [IsProbabilityMeasure.{u_2} (α := Ω₀₂) (m0 := MeasureSpace.toMeasurableSpace) volume] {G : Type uG} [inst_4 : AddCommGroup G] [Finite G] [inst_6 : MeasurableSpace G] (p : refPackage Ω₀₁ Ω₀₂ G) [MeasurableSingletonClass G], ∃ (Ω : Type uG) (x : MeasureSpace Ω) (X₁ : Ω → G) (X₂ : Ω → G), Measurable X₁ ∧ Measurable X₂ ∧ IsProbabilityMeasure.{uG} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume ∧ TauMinimizes p X₁ X₂`
Docstring: A pair of random variables minimizing $τ$ exists.
English: Let $G$ be a finite abelian group with measurable singletons, and let $p$ be a reference package on $G$ whose underlying spaces $\Omega_{01},\Omega_{02}$ carry probability measures. Then there exist a measure space $\Omega$ whose measure is a probability measure and measurable random variables $X_1,X_2:\Omega\to G$ such that $(X_1,X_2)$ minimizes $\tau$ for $p$.
