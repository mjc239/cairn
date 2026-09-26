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

#### `ProbabilityTheory.Kernel.rdist` (def)
Lean: `{T : Type u_1} → {T' : Type u_2} → {G : Type u_4} → [inst : MeasurableSpace T] → [inst_1 : MeasurableSpace T'] → [inst_2 : MeasurableSpace G] → [AddCommGroup G] → Kernel T G → Kernel T' G → Measure T → Measure T' → ℝ`
Docstring: The Rusza distance between two kernels taking values in the same space, defined as the average Rusza distance between the image measures.
Definition: `fun {T : Type u_1} {T' : Type u_2} {G : Type u_4} [MeasurableSpace T] [MeasurableSpace T'] [MeasurableSpace G] [AddCommGroup G] (κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') => ∫ (x : T × T'), (fun (p : T × T') => Kernel.rdistm.{u_4} (G := G) (κ p.1) (η p.2)) x ∂μ.prod ν`

#### `FiniteRange` (inductive)
Lean: `{Ω : Type u_1} → {G : Type u_2} → (Ω → G) → Prop`
Docstring: The property of having a finite range.

#### `ProbabilityTheory.entropy` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Definition: `fun {Ω : Type u_1} {S : Type u_2} [MeasurableSpace Ω] [MeasurableSpace S] (X : Ω → S) (μ : Measure Ω) => Hm[Measure.map X μ]`

#### `ProbabilityTheory.Kernel.rdistm` (def)
Lean: `{G : Type u_4} → [inst : MeasurableSpace G] → [AddCommGroup G] → Measure G → Measure G → ℝ`
Docstring: The Rusza distance between two measures, defined as `H[X - Y] - H[X]/2 - H[Y]/2` where `X` and `Y` are independent variables distributed according to the two measures.
Definition: `fun {G : Type u_4} [MeasurableSpace G] [AddCommGroup G] (μ ν : Measure G) => measureEntropy (S := G) (Measure.map (fun (x : G × G) => x.1 - x.2) (μ.prod ν)) - Hm[μ] / (2 : ℝ) - Hm[ν] / (2 : ℝ)`

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

## Flagged translations

### `condRuzsaDist`
Lean (short): `[Countable G] [MeasurableSingletonClass G] (X : Ω → G) (Z : Ω → S) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) [IsFiniteMeasure μ] (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) [IsFiniteMeasure μ'] : ℝ`
Lean (full): `{Ω : Type u_1} → {Ω' : Type u_2} → {G : Type u_5} → {S : Type u_6} → {T : Type u_7} → [mΩ : MeasurableSpace Ω] → [mΩ' : MeasurableSpace Ω'] → [hG : MeasurableSpace G] → [AddCommGroup G] → [MeasurableSpace S] → [MeasurableSpace T] → [Countable G] → [MeasurableSingletonClass G] → (Ω → G) → (Ω → S) → (Ω' → G) → (Ω' → T) → (μ : autoParam (Measure Ω) condRuzsaDist._auto_1) → [IsFiniteMeasure μ] → (μ' : autoParam (Measure Ω') condRuzsaDist._auto_3) → [IsFiniteMeasure μ'] → ℝ`
Docstring: The conditional Ruzsa distance `d[X|Z ; Y|W]`.
Previous English: Let $G$ be a countable abelian group in which singletons are measurable. For random variables $X:\Omega\to G$, $Z:\Omega\to S$ and $Y:\Omega'\to G$, $W:\Omega'\to T$, and finite measures $\mu$ on $\Omega$ and $\mu'$ on $\Omega'$ (by default the ambient measures), this defines the real number $d[X|Z \,;\, Y|W]$, the conditional Ruzsa distance of $X$ given $Z$ (with respect to $\mu$) and $Y$ given $W$ (with respect to $\mu'$).
Checker's issue: S and T (and Omega, Omega') are never introduced; the Lean requires S and T to be measurable spaces, which the English does not state.

### `condRuzsaDist'`
Lean (short): `[Countable G] [MeasurableSingletonClass G] (X : Ω → G) (Y : Ω' → G) (W : Ω' → T) (μ : autoParam (Measure Ω) condRuzsaDist'._auto_1) (μ' : autoParam (Measure Ω') condRuzsaDist'._auto_3) [IsFiniteMeasure μ'] : ℝ`
Lean (full): `{Ω : Type u_1} → {Ω' : Type u_2} → {G : Type u_5} → {T : Type u_7} → [mΩ : MeasurableSpace Ω] → [mΩ' : MeasurableSpace Ω'] → [hG : MeasurableSpace G] → [AddCommGroup G] → [MeasurableSpace T] → [Countable G] → [MeasurableSingletonClass G] → (Ω → G) → (Ω' → G) → (Ω' → T) → autoParam (Measure Ω) condRuzsaDist'._auto_1 → (μ' : autoParam (Measure Ω') condRuzsaDist'._auto_3) → [IsFiniteMeasure μ'] → ℝ`
Docstring: The conditional Ruzsa distance `d[X ; Y|W]`.
Previous English: Let $G$ be a countable abelian group in which singletons are measurable. For random variables $X:\Omega\to G$ and $Y:\Omega'\to G$, $W:\Omega'\to T$, a measure $\mu$ on $\Omega$ and a finite measure $\mu'$ on $\Omega'$ (by default the ambient measures), this defines the real number $d[X \,;\, Y|W]$, the conditional Ruzsa distance between $X$ (with respect to $\mu$) and $Y$ given $W$ (with respect to $\mu'$).
Checker's issue: T (and Omega') is never introduced; the Lean requires T to be a measurable space, which the English does not state.

### `kaimanovich_vershik`
Lean (short): `[Countable G] [MeasurableSingletonClass G] (h : iIndepFun ![X, Y, Z] μ) (hX : Measurable X) (hY : Measurable Y) (hZ : Measurable Z) [FiniteRange X] [FiniteRange Z] [FiniteRange Y] : H[X + Y + Z; μ] - H[X + Y; μ] ≤ H[Y + Z; μ] - H[Y; μ]`
Lean (full): `∀ {Ω : Type u_1} {G : Type u_5} [mΩ : MeasurableSpace Ω] {μ : Measure Ω} [hG : MeasurableSpace G] [inst : AddCommGroup G] [Countable G] [MeasurableSingletonClass G] {X Y Z : Ω → G}, iIndepFun (β := fun (a : Fin (Nat.succ (0 : ℕ)).succ.succ) => G) ![X, Y, Z] μ → Measurable X → Measurable Y → Measurable Z → ∀ [FiniteRange X] [FiniteRange Z] [FiniteRange Y], H[X + Y + Z; μ] - H[X + Y; μ] ≤ H[Y + Z; μ] - H[Y; μ]`
Docstring: The **Kaimanovich-Vershik inequality**. `H[X + Y + Z] - H[X + Y] ≤ H[Y + Z] - H[Y]`.
Previous English: (Kaimanovich–Vershik inequality.) Let $G$ be a countable abelian group with measurable singletons, and let $X,Y,Z:\Omega\to G$ be measurable random variables with finite range which are jointly independent under $\mu$. Then $H[X+Y+Z;\mu] - H[X+Y;\mu] \le H[Y+Z;\mu] - H[Y;\mu]$.
Checker's issue: The measure mu (an arbitrary measure on the measurable space Omega) is used without being introduced.
