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

#### `ProbabilityTheory.entropy` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Definition: `fun {Ω : Type u_1} {S : Type u_2} [MeasurableSpace Ω] [MeasurableSpace S] (X : Ω → S) (μ : Measure Ω) => Hm[Measure.map X μ]`

#### `prod` (def)
Lean: `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → (Ω → S) → (Ω → T) → Ω → S × T`
Docstring: The pair of two random variables
Definition: `fun {Ω : Type u_1} {S : Type u_2} {T : Type u_3} (X : Ω → S) (Y : Ω → T) (ω : Ω) => (X ω, Y ω)`

## Flagged translations

### `I₃_eq`
Lean (short): `[Finite G] [MeasurableSingletonClass G] (X₁ : Ω → G) (X₂ : Ω → G) (X₁' : Ω → G) (X₂' : Ω → G) (hX₁ : Measurable X₁) (hX₂ : Measurable X₂) (hX₁' : Measurable X₁') (hX₂' : Measurable X₂') (h₁ : IdentDistrib X₁ X₁' volume volume) (h_indep : iIndepFun ![X₁, X₂, X₁', X₂'] volume) [IsProbabilityMeasure volume] : I[X₁' + X₂ : X₁' + X₁|X₁ + X₂ + X₁' + X₂'] = I[X₁ + X₂ : X₁' + X₁|X₁ + X₂ + X₁' + X₂']`
Lean (full): `∀ {G : Type u_1} [inst : AddCommGroup G] [Finite G] [hG : MeasurableSpace G] [MeasurableSingletonClass G] {Ω : Type u_4} [mΩ : MeasureSpace Ω] (X₁ X₂ X₁' X₂' : Ω → G), Measurable X₁ → Measurable X₂ → Measurable X₁' → Measurable X₂' → IdentDistrib X₁ X₁' volume volume → iIndepFun (_mΩ := MeasureSpace.toMeasurableSpace) (β := fun (a : Fin (Nat.succ (0 : ℕ)).succ.succ.succ) => G) ![X₁, X₂, X₁', X₂'] volume → ∀ [IsProbabilityMeasure.{u_4} (α := Ω) (m0 := MeasureSpace.toMeasurableSpace) volume], I[X₁' + X₂ : X₁' + X₁|X₁ + X₂ + X₁' + X₂'] = I[X₁ + X₂ : X₁' + X₁|X₁ + X₂ + X₁' + X₂']`
Docstring: The quantity `I_3 = I[V:W|S]` is equal to `I_2`.
Previous English: Let $G$ be a finite abelian group with measurable singletons, and suppose the measure on $\Omega$ is a probability measure. Let $X_1, X_2, X_1', X_2' : \Omega \to G$ be measurable random variables, with $X_1'$ having the same distribution as $X_1$, and $X_1, X_2, X_1', X_2'$ jointly independent. Then $$I[X_1'+X_2 : X_1'+X_1 \mid X_1+X_2+X_1'+X_2'] = I[X_1+X_2 : X_1'+X_1 \mid X_1+X_2+X_1'+X_2'],$$ i.e. the quantity $I_3 = I[V:W\mid S]$ equals $I_2$.
Checker's issue: The closing remark 'i.e. I_3 = I[V:W|S] equals I_2' uses V, W, S and I_2 without introducing them.
