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

#### `ProbabilityTheory.measureEntropy` (def)
Lean: `{S : Type u_2} → [inst : MeasurableSpace S] → autoParam (Measure S) measureEntropy._auto_1 → ℝ`
Docstring: Entropy of a measure on a measurable space. We normalize the measure by `(μ Set.univ)⁻¹` to extend the entropy definition to finite measures. What we really want to do is deal with `μ=0` or `IsProbabilityMeasure μ`, but we don't have a typeclass for that (we could create one though). The added complexity ∈ the expression is not an issue because if `μ` is a probability measure, a call to `simp` will simplify `(μ Set.univ)⁻¹ • μ` to `μ`.
Definition: `fun {S : Type u_2} [MeasurableSpace S] (μ : Measure S) => ∑' (s : S), ((HSMul.hSMul (α := ENNReal) ((μ Set.univ)⁻¹ : ENNReal) μ).real {s}).negMulLog`

## Flagged translations

### `ProbabilityTheory.Kernel.rdistm`
Lean (short): `(μ : Measure G) (ν : Measure G) : ℝ`
Lean (full): `{G : Type u_4} → [inst : MeasurableSpace G] → [AddCommGroup G] → Measure G → Measure G → ℝ`
Definition: `fun {G : Type u_4} [MeasurableSpace G] [AddCommGroup G] (μ ν : Measure G) => measureEntropy (S := G) (Measure.map (fun (x : G × G) => x.1 - x.2) (μ.prod ν)) - Hm[μ] / (2 : ℝ) - Hm[ν] / (2 : ℝ)`
Docstring: The Rusza distance between two measures, defined as `H[X - Y] - H[X]/2 - H[Y]/2` where `X` and `Y` are independent variables distributed according to the two measures.
Previous English: Let $G$ be an abelian group equipped with a measurable space structure. For two measures $\mu,\nu$ on $G$, this defines a real number $\mathrm{rdistm}(\mu,\nu)$. According to its docstring, it is the Ruzsa distance between the two measures, defined as $H[X-Y]-H[X]/2-H[Y]/2$ where $X$ and $Y$ are independent variables distributed according to $\mu$ and $\nu$.
Checker's issue: Definition body is shown (measureEntropy of the pushforward of μ ⊗ ν under (x,y) ↦ x − y, minus Hm[μ]/2 minus Hm[ν]/2, with measureEntropy normalising by total mass), but the English only states the type and repeats the docstring ('according to its docstring ... independent variables distributed according to μ and ν'), which for arbitrary (non-probability) measures is not an accurate description of the body.

### `ProbabilityTheory.Kernel.rdist`
Lean (short): `(κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') : ℝ`
Lean (full): `{T : Type u_1} → {T' : Type u_2} → {G : Type u_4} → [inst : MeasurableSpace T] → [inst_1 : MeasurableSpace T'] → [inst_2 : MeasurableSpace G] → [AddCommGroup G] → Kernel T G → Kernel T' G → Measure T → Measure T' → ℝ`
Definition: `fun {T : Type u_1} {T' : Type u_2} {G : Type u_4} [MeasurableSpace T] [MeasurableSpace T'] [MeasurableSpace G] [AddCommGroup G] (κ : Kernel T G) (η : Kernel T' G) (μ : Measure T) (ν : Measure T') => ∫ (x : T × T'), (fun (p : T × T') => Kernel.rdistm.{u_4} (G := G) (κ p.1) (η p.2)) x ∂μ.prod ν`
Docstring: The Rusza distance between two kernels taking values in the same space, defined as the average Rusza distance between the image measures.
Previous English: Definition. Let $T$ and $T'$ be measurable spaces and let $G$ be an additive commutative group equipped with a measurable space structure. For a kernel $\kappa$ from $T$ to $G$, a kernel $\eta$ from $T'$ to $G$, a measure $\mu$ on $T$ and a measure $\nu$ on $T'$, the kernel Ruzsa distance $d_k[\kappa;\mu \,\#\, \eta;\nu]$ is a real number. According to its docstring, it is the average Ruzsa distance between the image measures.
Checker's issue: Definition body is shown (the integral over T × T' with respect to μ.prod ν of rdistm(κ t, η t')), but the English only says it is a real number and, per the docstring, 'the average Ruzsa distance between the image measures', without specifying the averaging measure μ ⊗ ν or the formula.
