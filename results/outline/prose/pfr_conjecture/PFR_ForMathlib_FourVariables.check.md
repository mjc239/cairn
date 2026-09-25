You are checking translations of verified Lean statements into mathematical English.
For each result below you get a short form of the Lean statement, the FULL Lean statement (every implicit argument
and instance assumption, numerals with their types), the docstring if there is one, and the English. Compare the
English with the full statement; anything the English attributes to the docstring must actually be in it.

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
be supported by the docstring or the Lean. So is a formula or description of what a defined object is: when the
prompt shows neither its definition nor a docstring saying it, the English must not supply one. Every variable
needs its type ("$f : G \to \mathbb{C}$", "$m$ a natural number"), every symbol must be introduced (notation such
as $M_{\mathcal B}$ included), and no letter may mean two things. When in doubt, flag it: a false alarm costs one
repair, a missed error stays in the outline. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `ProbabilityTheory.iIndepFun.apply_two_last`
Lean (short): `(h_indep : iIndepFun ![Z₁, Z₂, Z₃, Z₄] volume) (hZ₁ : Measurable Z₁) (hZ₂ : Measurable Z₂) (hZ₃ : Measurable Z₃) (hZ₄ : Measurable Z₄) (hphi : Measurable (Function.uncurry phi)) : iIndepFun ![Z₁, Z₂, fun ω => phi (Z₃ ω) (Z₄ ω)] volume`
Lean (full): `∀ {Ω : Type u_1} [inst : MeasureSpace Ω] {G : Type u_2} [hG : MeasurableSpace G] {Z₁ Z₂ Z₃ Z₄ : Ω → G}, iIndepFun (_mΩ := MeasureSpace.toMeasurableSpace) (β := fun (a : Fin (Nat.succ (0 : ℕ)).succ.succ.succ) => G) ![Z₁, Z₂, Z₃, Z₄] volume → Measurable Z₁ → Measurable Z₂ → Measurable Z₃ → Measurable Z₄ → ∀ {phi : G → G → G}, Measurable (Function.uncurry phi) → iIndepFun (_mΩ := MeasureSpace.toMeasurableSpace) (β := fun (a : Fin (Nat.succ (0 : ℕ)).succ.succ) => G) ![Z₁, Z₂, fun (ω : Ω) => phi (Z₃ ω) (Z₄ ω)] volume`
Docstring: If `(Z₁, Z₂, Z₃, Z₄)` are independent, so are `(Z₁, Z₂, φ Z₃ Z₄)` for any measurable `φ`.
English: Let $\Omega$ be a measure space with measure $\mu$, and let $G$ be a measurable space. Let $Z_1,Z_2,Z_3,Z_4:\Omega\to G$ be measurable functions such that the family $(Z_1,Z_2,Z_3,Z_4)$ is jointly independent with respect to $\mu$, and let $\varphi:G\to G\to G$ be a function whose uncurried form $G\times G\to G$, $(a,b)\mapsto \varphi(a,b)$, is measurable. Then the family of three functions $Z_1$, $Z_2$ and $\omega\mapsto \varphi(Z_3(\omega),Z_4(\omega))$ (all $\Omega\to G$) is jointly independent with respect to $\mu$.
