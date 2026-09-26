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
docstring or Lean supports a description of an object, name it instead of describing it. Give every variable its
type, introduce every symbol, and never use one letter for two things.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

### `ProbabilityTheory.iIndepFun.apply_two_last`
Lean (short): `(h_indep : iIndepFun ![Z₁, Z₂, Z₃, Z₄] volume) (hZ₁ : Measurable Z₁) (hZ₂ : Measurable Z₂) (hZ₃ : Measurable Z₃) (hZ₄ : Measurable Z₄) (hphi : Measurable (Function.uncurry phi)) : iIndepFun ![Z₁, Z₂, fun ω => phi (Z₃ ω) (Z₄ ω)] volume`
Lean (full): `∀ {Ω : Type u_1} [inst : MeasureSpace Ω] {G : Type u_2} [hG : MeasurableSpace G] {Z₁ Z₂ Z₃ Z₄ : Ω → G}, iIndepFun (_mΩ := MeasureSpace.toMeasurableSpace) (β := fun a => G) ![Z₁, Z₂, Z₃, Z₄] volume → Measurable Z₁ → Measurable Z₂ → Measurable Z₃ → Measurable Z₄ → ∀ {phi : G → G → G}, Measurable (Function.uncurry phi) → iIndepFun (_mΩ := MeasureSpace.toMeasurableSpace) (β := fun a => G) ![Z₁, Z₂, fun ω => phi (Z₃ ω) (Z₄ ω)] volume`
Docstring: If `(Z₁, Z₂, Z₃, Z₄)` are independent, so are `(Z₁, Z₂, φ Z₃ Z₄)` for any measurable `φ`.
Previous English: Let $Z_1,Z_2,Z_3,Z_4$ be measurable random variables that are jointly independent (as the family $(Z_1,Z_2,Z_3,Z_4)$) with respect to the ambient measure, and let $\varphi$ be a two-argument function whose uncurried form $(a,b)\mapsto \varphi(a,b)$ is measurable. Then the three random variables $Z_1$, $Z_2$ and $\omega\mapsto \varphi(Z_3(\omega),Z_4(\omega))$ are jointly independent.
Checker's issue: The English omits that Z₁,…,Z₄ all take values in a single measurable space G and that φ : G → G → G; it describes φ only as 'a two-argument function' with an unspecified codomain, which suggests more generality than the Lean proves.
