You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption) and the English. Compare the English with the full statement.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Assumptions carried by instance
arguments count as hypotheses: `[AddCommGroup G]` (G is an abelian group), `[Field K]`, `[MetricSpace X]`,
`[IsProbabilityMeasure μ]`, a bundle of standing assumptions such as `[ProofData …]`, and so on. The English must
state each one, or make it unmistakable from context (e.g. "a finite abelian group G"); an English statement that
says "a group" where the Lean requires an abelian group claims more than was proved. Only instances with no
mathematical content (decidability: `Decidable…`) may go unstated. Implicit type arguments may be introduced
naturally. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.iIndepFun.apply_two_last`
Lean (short): `(h_indep : iIndepFun ![Z₁, Z₂, Z₃, Z₄] volume) (hZ₁ : Measurable Z₁) (hZ₂ : Measurable Z₂) (hZ₃ : Measurable Z₃) (hZ₄ : Measurable Z₄) (hphi : Measurable (Function.uncurry phi)) : iIndepFun ![Z₁, Z₂, fun ω => phi (Z₃ ω) (Z₄ ω)] volume`
Lean (full): `∀ {Ω : Type u_1} [inst : MeasureSpace Ω] {G : Type u_2} [hG : MeasurableSpace G] {Z₁ Z₂ Z₃ Z₄ : Ω → G}, iIndepFun ![Z₁, Z₂, Z₃, Z₄] volume → Measurable Z₁ → Measurable Z₂ → Measurable Z₃ → Measurable Z₄ → ∀ {phi : G → G → G}, Measurable (Function.uncurry phi) → iIndepFun ![Z₁, Z₂, fun ω => phi (Z₃ ω) (Z₄ ω)] volume`
English: Let $Z_1,Z_2,Z_3,Z_4$ be measurable random variables that are jointly independent (as the family $(Z_1,Z_2,Z_3,Z_4)$) with respect to the ambient measure, and let $\varphi$ be a two-argument function whose uncurried form $(a,b)\mapsto \varphi(a,b)$ is measurable. Then the three random variables $Z_1$, $Z_2$ and $\omega\mapsto \varphi(Z_3(\omega),Z_4(\omega))$ are jointly independent.
