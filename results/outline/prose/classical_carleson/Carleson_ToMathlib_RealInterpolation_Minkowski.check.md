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
Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `ComputationsChoiceExponent.ζ` (def)
Lean: `ENNReal → ENNReal → ENNReal → ENNReal → ℝ → ℝ`
Definition: `fun (p₀ q₀ p₁ q₁ : ENNReal) (t : ℝ) => (((1 : ℝ) - t) * p₀⁻¹.toReal + t * p₁⁻¹.toReal) * (q₁⁻¹.toReal - q₀⁻¹.toReal) / ((((1 : ℝ) - t) * q₀⁻¹.toReal + t * q₁⁻¹.toReal) * (p₁⁻¹.toReal - p₀⁻¹.toReal))`

#### `MeasureTheory.sel` (def)
Lean: `Bool → ENNReal → ENNReal → ENNReal`
Definition: `fun (j : Bool) (p₀ p₁ : ENNReal) => match j with | true => p₁ | false => p₀`

#### `MeasureTheory.trnc` (def)
Lean: `{α : Type u_1} → {ε' : Type u_5} → [ENorm ε'] → [Zero ε'] → Bool → (α → ε') → ENNReal → α → ε'`
Docstring: A function to deal with truncations and complement of truncations in one go.
Definition: `fun {α : Type u_1} {ε' : Type u_5} [ENorm ε'] [Zero ε'] (j : Bool) (f : α → ε') (t : ENNReal) => match (motive := Bool → α → ε') j with | false => truncCompl f t | true => trunc f t`

#### `ScaledPowerFunction` (structure or class)
Lean: `Type`
Docstring: A ScaledPowerFunction is meant to represent a function of the form `t ↦ (t / d)^σ`, where `d` is strictly positive and either `σ > 0` or `σ < 0`.
Fields: `σ`, `d`, `0`

#### `ScaledPowerFunction.d` (def)
Lean: `ScaledPowerFunction → ENNReal`
Definition: `fun (self : ScaledPowerFunction) => self.2`

#### `ScaledPowerFunction.σ` (def)
Lean: `ScaledPowerFunction → ℝ`
Definition: `fun (self : ScaledPowerFunction) => self.1`

#### `StrictRangeToneCouple.toToneCouple` (def)
Lean: `StrictRangeToneCouple → ToneCouple`
Definition: `fun (self : StrictRangeToneCouple) => self.1`

#### `ToneCouple.ton` (def)
Lean: `ToneCouple → ENNReal → ENNReal`
Definition: `fun (self : ToneCouple) => self.1`

#### `spf_to_tc` (def)
Lean: `ScaledPowerFunction → StrictRangeToneCouple`
Docstring: A scaled power function gives rise to a ToneCouple.
Definition: `fun (spf : ScaledPowerFunction) => { ton := fun (s : ENNReal) => (s / spf.d) ^ spf.σ, inv := fun (t : ENNReal) => spf.d * t ^ spf.σ⁻¹, mon := if (0 : ℝ) < spf.σ then true else false, ton_is_ton := ⋯, inv_pf := ⋯, ran_ton := ⋯, ran_inv := ⋯ }`

#### `ToneCouple.mon` (def)
Lean: `ToneCouple → Bool`
Definition: `fun (self : ToneCouple) => self.3`

#### `MeasureTheory.trunc` (def)
Lean: `{α : Type u_1} → {ε' : Type u_5} → [ENorm ε'] → [Zero ε'] → (α → ε') → ENNReal → α → ε'`
Docstring: The `t`-truncation of a function `f`.
Definition: `fun {α : Type u_1} {ε' : Type u_5} [ENorm ε'] [Zero ε'] (f : α → ε') (t : ENNReal) (x : α) => if ‖f x‖ₑ ≤ t then f x else (0 : ε')`

#### `MeasureTheory.truncCompl` (def)
Lean: `{α : Type u_1} → {ε' : Type u_5} → [ENorm ε'] → [Zero ε'] → (α → ε') → ENNReal → α → ε'`
Docstring: The complement of a `t`-truncation of a function `f`.
Definition: `fun {α : Type u_1} {ε' : Type u_5} [ENorm ε'] [Zero ε'] (f : α → ε') (t : ENNReal) (x : α) => if ‖f x‖ₑ ≤ t then (0 : ε') else f x`

#### `StrictRangeToneCouple` (structure or class)
Lean: `Type`
Docstring: A StrictRangeToneCouple is a `ToneCouple` for which the functions in the couple, when restricted to `Ioo 0 ∞`, map to `Ioo 0 ∞`.
Fields: `toToneCouple`, `0`

#### `ToneCouple` (structure or class)
Lean: `Type`
Docstring: A `ToneCouple` is a couple of two monotone functions that are practically inverses of each other. It is used in the proof of the real interpolation theorem. Note: originally it seemed useful to make the possible choice of this function general in the proof of the real inteprolation theorem. However, in the end really only one function works for all the different cases. This infrastructure, however, could potentially still be useful, if one would like to try to improve the constant.
Fields: `mon`

## Translations

### `MeasureTheory.estimate_trnc₁`
Lean (short): `(ht : t ∈ Set.Ioo 0 1) (hp₀ : 0 < p₀) (hq₀ : 0 < q₀) (hp₁ : 0 < p₁) (hq₁ : 0 < q₁) (hpq : sel j p₀ p₁ ≤ sel j q₀ q₁) (hp' : sel j p₀ p₁ ≠ ⊤) (hq' : sel j q₀ q₁ ≠ ⊤) (hp₀p₁ : p₀ < p₁) (hq₀q₁ : q₀ ≠ q₁) (hp : p⁻¹ = (1 - t) * p₀⁻¹ + t * p₁⁻¹) (hq : q⁻¹ = (1 - t) * q₀⁻¹ + t * q₁⁻¹) (hf : AEStronglyMeasurable f μ) (hf₂ : SigmaFinite (μ.restrict (Function.support fun x => ‖f x‖ₑ))) (hspf : spf.σ = ComputationsChoiceExponent.ζ p₀ q₀ p₁ q₁ t.toReal) : ∫⁻ (s : ℝ) in Set.Ioi 0, eLpNorm (trnc j f ((spf_to_tc spf).ton (ENNReal.ofReal s))) (sel j p₀ p₁) μ ^ (sel j q₀ q₁).toReal * ENNReal.ofReal (s ^ (q.toReal - (sel j q₀ q₁).toReal - 1)) ≤ spf.d ^ (q.toReal - (sel j q₀ q₁).toReal) * ENNReal.ofReal |q.toReal - (sel j q₀ q₁).toReal|⁻¹ * (eLpNorm f p μ ^ p.toReal) ^ ((sel j p₀ p₁).toReal⁻¹ * (sel j q₀ q₁).toReal)`
Lean (full): `∀ {α : Type u_1} {E₁ : Type u_4} {m : MeasurableSpace α} {p q p₀ q₀ p₁ q₁ : ENNReal} {μ : Measure α} {f : α → E₁} {t : ENNReal} {spf : ScaledPowerFunction} {j : Bool} [inst : TopologicalSpace E₁] [inst_1 : ESeminormedAddMonoid E₁], t ∈ Set.Ioo (0 : ENNReal) (1 : ENNReal) → (0 : ENNReal) < p₀ → (0 : ENNReal) < q₀ → (0 : ENNReal) < p₁ → (0 : ENNReal) < q₁ → sel j p₀ p₁ ≤ sel j q₀ q₁ → sel j p₀ p₁ ≠ ⊤ → sel j q₀ q₁ ≠ ⊤ → p₀ < p₁ → q₀ ≠ q₁ → p⁻¹ = ((1 : ENNReal) - t) * p₀⁻¹ + t * p₁⁻¹ → q⁻¹ = ((1 : ENNReal) - t) * q₀⁻¹ + t * q₁⁻¹ → AEStronglyMeasurable f μ → SigmaFinite (μ.restrict (Function.support (M := ENNReal) fun (x : α) => ‖f x‖ₑ)) → spf.σ = ComputationsChoiceExponent.ζ p₀ q₀ p₁ q₁ t.toReal → ∫⁻ (s : ℝ) in Set.Ioi (0 : ℝ), eLpNorm (trnc j f ((spf_to_tc spf).ton (ENNReal.ofReal s))) (sel j p₀ p₁) μ ^ (sel j q₀ q₁).toReal * ENNReal.ofReal (s ^ (q.toReal - (sel j q₀ q₁).toReal - (1 : ℝ))) ≤ spf.d ^ (q.toReal - (sel j q₀ q₁).toReal) * ENNReal.ofReal |q.toReal - (sel j q₀ q₁).toReal|⁻¹ * (eLpNorm f p μ ^ p.toReal) ^ ((sel j p₀ p₁).toReal⁻¹ * (sel j q₀ q₁).toReal)`
Docstring: One of the key estimates for the real interpolation theorem, now using the particular choice of exponent, but not yet using the particular choice of scale in the `ScaledPowerFunction`.
English: Let $\alpha$ be a measurable space with a measure $\mu$, let $E_1$ be a topological space that is an extended-seminormed additive monoid (`ESeminormedAddMonoid`), let $f:\alpha\to E_1$, and let $j$ be a boolean. Let $\mathrm{spf}$ be a `ScaledPowerFunction` (a structure with a real field $\sigma$ and a field $d\in[0,\infty]$; per the docstring it represents $t\mapsto(t/d)^\sigma$ with $d>0$ and $\sigma\neq0$), and write $\sigma=\mathrm{spf}.\sigma$, $d=\mathrm{spf}.d$. Let $\mathrm{ton}:[0,\infty]\to[0,\infty]$ be the `ton` function of the tone couple `spf_to_tc spf`, which by definition is $\mathrm{ton}(u)=(u/d)^{\sigma}$. For $j\in\{\mathrm{true},\mathrm{false}\}$ and $u_0,u_1\in[0,\infty]$ let $\mathrm{sel}_j(u_0,u_1)$ be $u_1$ if $j=\mathrm{true}$ and $u_0$ if $j=\mathrm{false}$. For $\tau\in[0,\infty]$ let $\mathrm{trnc}_j(f,\tau):\alpha\to E_1$ be the function $x\mapsto f(x)$ if $\|f(x)\|_e\le\tau$ and $x\mapsto 0$ otherwise when $j=\mathrm{true}$, and $x\mapsto 0$ if $\|f(x)\|_e\le\tau$ and $x\mapsto f(x)$ otherwise when $j=\mathrm{false}$; here $\|\cdot\|_e\in[0,\infty]$ is the extended norm on $E_1$. Let $t,p,q,p_0,q_0,p_1,q_1\in[0,\infty]$, and write $\tilde p=\mathrm{sel}_j(p_0,p_1)$, $\tilde q=\mathrm{sel}_j(q_0,q_1)$. For a real number $r$ let $\zeta(r)=\dfrac{\big((1-r)\,a_0+r\,a_1\big)(b_1-b_0)}{\big((1-r)\,b_0+r\,b_1\big)(a_1-a_0)}\in\mathbb R$, where $a_i$ is the real number obtained from $p_i^{-1}\in[0,\infty]$ and $b_i$ the real number obtained from $q_i^{-1}$ (with $\infty\mapsto 0$), $i=0,1$ (this is `ComputationsChoiceExponent.ζ p₀ q₀ p₁ q₁ r`). Assume $0<t<1$; $0<p_0$, $0<q_0$, $0<p_1$, $0<q_1$; $\tilde p\le\tilde q$; $\tilde p\ne\infty$; $\tilde q\ne\infty$; $p_0<p_1$; $q_0\ne q_1$; $p^{-1}=(1-t)p_0^{-1}+t\,p_1^{-1}$ and $q^{-1}=(1-t)q_0^{-1}+t\,q_1^{-1}$ in $[0,\infty]$; $f$ is $\mu$-almost everywhere strongly measurable; the restriction of $\mu$ to the support of $x\mapsto\|f(x)\|_e$ is $\sigma$-finite; and $\sigma=\zeta(t)$, with $t$ regarded as a real number. Writing $q^\ast,\tilde p^\ast,\tilde q^\ast,p^\ast$ for the real numbers corresponding to $q,\tilde p,\tilde q,p$, we have $$\int^{-}_{(0,\infty)}\big\|\mathrm{trnc}_j\big(f,\mathrm{ton}(s)\big)\big\|_{L^{\tilde p}(\mu)}^{\tilde q^\ast}\; s^{\,q^\ast-\tilde q^\ast-1}\,ds\;\le\;d^{\,q^\ast-\tilde q^\ast}\cdot|q^\ast-\tilde q^\ast|^{-1}\cdot\Big(\|f\|_{L^{p}(\mu)}^{\,p^\ast}\Big)^{(\tilde p^\ast)^{-1}\tilde q^\ast},$$ where $s$ is a real variable, $\mathrm{ton}(s)$ means ton applied to $s$ viewed in $[0,\infty]$, the integral is a lower Lebesgue integral in $[0,\infty]$, $\|\cdot\|_{L^r(\mu)}$ denotes the $L^r$ (semi)norm with values in $[0,\infty]$, and $s^{\,q^\ast-\tilde q^\ast-1}$ and $|q^\ast-\tilde q^\ast|^{-1}$ are real numbers regarded in $[0,\infty]$. According to the docstring, this is one of the key estimates for the real interpolation theorem, using the particular choice of exponent but not yet the particular choice of scale in the scaled power function.

### `MeasureTheory.estimate_trnc`
Lean (short): `(hp₀ : 0 < p₀) (hq₀ : 0 < q₀) (hp₀q₀ : p₀ ≤ q₀) (hf : AEStronglyMeasurable f μ) (hf₂ : SigmaFinite (μ.restrict (Function.support fun x => ‖f x‖ₑ))) (hpowers : if (j ^^ (spf_to_tc spf).mon) = true then q₀ < q else q < q₀) (hpow_pos : 0 < q₀ + spf.σ⁻¹ * (q - q₀)) : ∫⁻ (s : ℝ) in Set.Ioi 0, eLpNorm (trnc j f ((spf_to_tc spf).ton (ENNReal.ofReal s))) (ENNReal.ofReal p₀) μ ^ q₀ * ENNReal.ofReal (s ^ (q - q₀ - 1)) ≤ spf.d ^ (q - q₀) * ENNReal.ofReal |q - q₀|⁻¹ * (∫⁻ (a : α) in Function.support fun x => ‖f x‖ₑ, ‖f a‖ₑ ^ (p₀ + spf.σ⁻¹ * (q - q₀) * (p₀ / q₀)) ∂μ) ^ (p₀⁻¹ * q₀)`
Lean (full): `∀ {α : Type u_1} {E₁ : Type u_4} {m : MeasurableSpace α} {μ : Measure α} {f : α → E₁} {p₀ q₀ q : ℝ} {spf : ScaledPowerFunction} {j : Bool} [inst : TopologicalSpace E₁] [inst_1 : ESeminormedAddMonoid E₁], (0 : ℝ) < p₀ → (0 : ℝ) < q₀ → p₀ ≤ q₀ → AEStronglyMeasurable f μ → SigmaFinite (μ.restrict (Function.support (M := ENNReal) fun (x : α) => ‖f x‖ₑ)) → (if (j ^^ (spf_to_tc spf).mon) = true then q₀ < q else q < q₀) → (0 : ℝ) < q₀ + spf.σ⁻¹ * (q - q₀) → ∫⁻ (s : ℝ) in Set.Ioi (0 : ℝ), eLpNorm (trnc j f ((spf_to_tc spf).ton (ENNReal.ofReal s))) (ENNReal.ofReal p₀) μ ^ q₀ * ENNReal.ofReal (s ^ (q - q₀ - (1 : ℝ))) ≤ spf.d ^ (q - q₀) * ENNReal.ofReal |q - q₀|⁻¹ * (∫⁻ (a : α) in Function.support (M := ENNReal) fun (x : α) => ‖f x‖ₑ, ‖f a‖ₑ ^ (p₀ + spf.σ⁻¹ * (q - q₀) * (p₀ / q₀)) ∂μ) ^ (p₀⁻¹ * q₀)`
Docstring: One of the key estimates for the real interpolation theorem, not yet using the particular choice of exponent and scale in the `ScaledPowerFunction`.
English: Let $\alpha$ be a measurable space with a measure $\mu$, let $E_1$ be a topological space that is an extended-seminormed additive monoid (`ESeminormedAddMonoid`), let $f:\alpha\to E_1$, and let $j$ be a boolean. Let $\mathrm{spf}$ be a `ScaledPowerFunction` (a structure with a real field $\sigma$ and a field $d\in[0,\infty]$; per the docstring it represents $t\mapsto(t/d)^\sigma$ with $d>0$ and $\sigma\neq0$), and write $\sigma=\mathrm{spf}.\sigma$, $d=\mathrm{spf}.d$. Let $\mathrm{ton}:[0,\infty]\to[0,\infty]$ be the `ton` function of the tone couple `spf_to_tc spf`, which by definition is $\mathrm{ton}(u)=(u/d)^{\sigma}$. Let $\mathrm{mon}$ be the `mon` boolean of the tone couple `spf_to_tc spf`, which by definition is true if $0<\sigma$ and false otherwise. For $\tau\in[0,\infty]$ let $\mathrm{trnc}_j(f,\tau):\alpha\to E_1$ be the function $x\mapsto f(x)$ if $\|f(x)\|_e\le\tau$ and $x\mapsto 0$ otherwise when $j=\mathrm{true}$, and $x\mapsto 0$ if $\|f(x)\|_e\le\tau$ and $x\mapsto f(x)$ otherwise when $j=\mathrm{false}$; here $\|\cdot\|_e\in[0,\infty]$ is the extended norm on $E_1$. Let $p_0,q_0,q$ be real numbers with $0<p_0$, $0<q_0$ and $p_0\le q_0$. Assume $f$ is $\mu$-almost everywhere strongly measurable, the restriction of $\mu$ to the support $S=\{x\in\alpha:\|f(x)\|_e\ne0\}$ of $x\mapsto\|f(x)\|_e$ is $\sigma$-finite, $q_0<q$ if $j\oplus\mathrm{mon}=\mathrm{true}$ (exclusive or) and $q<q_0$ otherwise, and $0<q_0+\sigma^{-1}(q-q_0)$. Then $$\int^{-}_{(0,\infty)}\big\|\mathrm{trnc}_j(f,\mathrm{ton}(s))\big\|_{L^{p_0}(\mu)}^{q_0}\,s^{\,q-q_0-1}\,ds\;\le\;d^{\,q-q_0}\,|q-q_0|^{-1}\Big(\int^{-}_{S}\|f(a)\|_e^{\,p_0+\sigma^{-1}(q-q_0)(p_0/q_0)}\,d\mu(a)\Big)^{p_0^{-1}q_0},$$ where $s$ is a real variable, $\mathrm{ton}(s)$ means ton applied to $s$ viewed in $[0,\infty]$, the integrals are lower Lebesgue integrals in $[0,\infty]$, $\|\cdot\|_{L^{p_0}(\mu)}$ is the $L^{p_0}$ (semi)norm with values in $[0,\infty]$, and $s^{q-q_0-1}$ and $|q-q_0|^{-1}$ are real numbers regarded in $[0,\infty]$. According to the docstring, this is one of the key estimates for the real interpolation theorem, not yet using the particular choice of exponent and scale in the scaled power function.
