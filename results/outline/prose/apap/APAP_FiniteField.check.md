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

#### `ddconv` (def)
Lean: `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [Fintype G] → [CommSemiring R] → (G → R) → (G → R) → G → R`
Docstring: Convolution
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [Fintype G] [CommSemiring R] (f g : G → R) (a : G) => ∑ x : G × G with x.1 + x.2 = a, f x.1 * g x.2`

#### `mu` (def)
Lean: `{K : Type u_1} → {α : Type u_3} → [DivisionSemiring K] → Finset α → α → K`
Docstring: The normalised indicator_one of a set.
Definition: `fun {K : Type u_1} {α : Type u_3} [DivisionSemiring K] (s : Finset α) => HSMul.hSMul (α := K) (β := α → K) (↑s.card)⁻¹ ((↑s).indicator fun (x : α) => (1 : K))`

#### `dddconv` (def)
Lean: `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [Fintype G] → [inst : CommSemiring R] → [StarRing R] → (G → R) → (G → R) → G → R`
Docstring: Difference convolution
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [Fintype G] [CommSemiring R] [StarRing R] (f g : G → R) (a : G) => ∑ x : G × G with x.1 - x.2 = a, HMul.hMul (β := R) (f x.1) ((starRingEnd (G → R)) g x.2 : R)`

#### `wLpNorm` (def)
Lean: `{α : Type u_1} → {E : Type u_3} → [MeasurableSpace α] → [NormedAddCommGroup E] → ENNReal → (α → NNReal) → (α → E) → ℝ`
Docstring: The weighted Lp norm of a function.
Definition: `fun {α : Type u_1} {E : Type u_3} [inst : MeasurableSpace α] [NormedAddCommGroup E] (p : ENNReal) (w : α → NNReal) (f : α → E) => lpNorm (m0 := inst) f p (Measure.sum fun (i : α) => HSMul.hSMul (β := Measure α) (w i) (Measure.dirac i))`

#### `MeasureTheory.dLpNorm` (def)
Lean: `{α : Type u_1} → {E : Type u_4} → [MeasurableSpace α] → [NormedAddCommGroup E] → ENNReal → (α → E) → ℝ`
Docstring: The Lp norm of a function with the compact normalisation.
Definition: `fun {α : Type u_1} {E : Type u_4} [inst : MeasurableSpace α] [NormedAddCommGroup E] (p : ENNReal) (f : α → E) => lpNorm (m0 := inst) f p Measure.count`

#### `s` (def)
Lean: `{G : Type u_1} → [DecidableEq G] → [Fintype G] → [AddCommGroup G] → [MeasurableSpace G] → NNReal → ℝ → Finset G → Finset G → Finset G → Finset G`
Definition: `fun {G : Type u_1} [DecidableEq G] [Fintype G] [AddCommGroup G] [MeasurableSpace G] (p : NNReal) (ε : ℝ) (B₁ B₂ A : Finset G) => {x : G | ((1 : ℝ) - ε) * wLpNorm (E := ℝ) (↑p) (mu B₁ ○ᵈ mu B₂) (((↑A).indicator fun (x : G) => (1 : ℝ)) ○ᵈ (↑A).indicator fun (x : G) => (1 : ℝ)) < (((↑A).indicator fun (x : G) => (1 : ℝ)) ○ᵈ (↑A).indicator fun (x : G) => (1 : ℝ)) x}`

## Translations

### `ap_in_ff`
Lean (short): `[Fintype G] [Module (ZMod q) G] (S : Finset G) (hq : Nat.Prime q) (hα₀ : 0 < α) (hα₂ : α ≤ 2⁻¹) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (hαA₁ : α ≤ ↑A₁.dens) (hαA₂ : α ≤ ↑A₂.dens) : ∃ V x, ↑(Module.finrank (ZMod q) G - Module.finrank (ZMod q) ↥V) ≤ 2 ^ 32 * (1 + Real.log α⁻¹) ^ 2 * (1 + Real.log (ε * α)⁻¹) ^ 2 * ε⁻¹ ^ 2 ∧ |∑ x_1 ∈ S, (mu (↑V).toFinset ∗ᵈ mu A₁ ∗ᵈ mu A₂) x_1 - ∑ x ∈ S, (mu A₁ ∗ᵈ mu A₂) x| ≤ ε`
Lean (full): `∀ {G : Type u} [inst : AddCommGroup G] [inst_1 : Fintype G] {ε : ℝ} {q : ℕ} [inst_2 : Module (ZMod q) G] {A₁ A₂ : Finset G} (S : Finset G) {α : ℝ} [inst_3 : DecidableEq G], Nat.Prime q → (0 : ℝ) < α → α ≤ (2 : ℝ)⁻¹ → (0 : ℝ) < ε → ε ≤ (1 : ℝ) → α ≤ ↑A₁.dens → α ≤ ↑A₂.dens → ∃ (V : Submodule (ZMod q) G) (x : DecidablePred fun (x : G) => x ∈ V), ↑(Module.finrank (ZMod q) G - Module.finrank.{0, u} (ZMod q) ↥V) ≤ (2 : ℝ) ^ (32 : ℕ) * ((1 : ℝ) + Real.log α⁻¹) ^ (2 : ℕ) * ((1 : ℝ) + Real.log (ε * α)⁻¹) ^ (2 : ℕ) * ε⁻¹ ^ (2 : ℕ) ∧ |HSub.hSub (α := ℝ) (∑ x_1 ∈ S, (mu (↑V).toFinset ∗ᵈ mu A₁ ∗ᵈ mu A₂) x_1) (∑ x ∈ S, (mu A₁ ∗ᵈ mu A₂) x)| ≤ ε`
English: Let $q$ be a prime and let $G$ be a finite vector space over $\mathbb{Z}/q\mathbb{Z}$. Let $S, A_1, A_2 \subseteq G$ be finite sets, and let $0 < \alpha \le 1/2$ and $0 < \varepsilon \le 1$ with $\alpha \le \operatorname{dens}(A_1)$ and $\alpha \le \operatorname{dens}(A_2)$. Then there is a subspace $V \le G$ with $\dim G - \dim V \le 2^{32}\,(1 + \log \alpha^{-1})^2\,(1 + \log (\varepsilon\alpha)^{-1})^2\,\varepsilon^{-2}$ and $\left|\sum_{x \in S} (\mu_V * \mu_{A_1} * \mu_{A_2})(x) - \sum_{x \in S} (\mu_{A_1} * \mu_{A_2})(x)\right| \le \varepsilon$, where $\mu_X$ is the normalised indicator of $X$ and $*$ is discrete convolution.

### `global_dichotomy`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hA : A.Nonempty) (hγC : γ ≤ ↑C.dens) (hγ : 0 < γ) (hAC : ε ≤ |↑(Fintype.card G) * ⟪mu A ∗ᵈ mu A, mu C⟫_[ℝ] - 1|) : ε / (2 * ↑(Fintype.card G)) ≤ ‖Fintype.balance (mu A) ○ᵈ Fintype.balance (mu A)‖_[↑(2 * ⌈1 + Real.log γ⁻¹⌉₊), mu Finset.univ]`
Lean (full): `∀ {G : Type u} [inst : AddCommGroup G] [inst_1 : Fintype G] {A C : Finset G} {γ ε : ℝ} [inst_2 : DecidableEq G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G], A.Nonempty → γ ≤ ↑C.dens → (0 : ℝ) < γ → ε ≤ |HMul.hMul (α := ℝ) ↑(Fintype.card G) ⟪mu A ∗ᵈ mu A, mu C⟫_[ℝ] - (1 : ℝ)| → ε / ((2 : ℝ) * ↑(Fintype.card G)) ≤ wLpNorm (E := ℝ) (↑((2 : ℕ) * ⌈(1 : ℝ) + Real.log γ⁻¹⌉₊)) (mu Finset.univ) (Fintype.balance (mu A) ○ᵈ Fintype.balance (mu A))`
English: Let $G$ be a finite additive abelian group equipped with a measurable space structure that is discrete (every subset is measurable). Let $A, C$ be finite subsets of $G$ with $A$ nonempty, and let $\gamma, \varepsilon$ be real numbers with $0 < \gamma \le \operatorname{dens}(C)$, where $\operatorname{dens}(C) = |C|/|G|$. For a finite set $B \subseteq G$ let $\mu_B : G \to \mathbb{R}$ be its normalised indicator, $\mu_B(x) = 1/|B|$ if $x \in B$ and $\mu_B(x) = 0$ otherwise. For $f, g : G \to \mathbb{R}$ let $(f * g)(a) = \sum_{x + y = a} f(x) g(y)$ be their convolution and $(f \circ g)(a) = \sum_{x - y = a} f(x) g(y)$ their difference convolution, and let $\operatorname{bal}(f) = f - \frac{1}{|G|}\sum_{y \in G} f(y)$ be the balanced version of $f$. Suppose $\varepsilon \le \left| |G| \cdot \langle \mu_A * \mu_A, \mu_C \rangle_{\mathbb{R}} - 1 \right|$, where $\langle \cdot, \cdot \rangle_{\mathbb{R}}$ is the real inner product of functions $G \to \mathbb{R}$. Let $p = 2\lceil 1 + \log \gamma^{-1} \rceil$, a natural number (with $\lceil\cdot\rceil$ the natural-number ceiling). Then $$\frac{\varepsilon}{2|G|} \le \|\operatorname{bal}(\mu_A) \circ \operatorname{bal}(\mu_A)\|_{p, \mu_G},$$ where $\|h\|_{p, \mu_G}$ denotes the $L^p$ norm of $h$ with respect to the measure on $G$ that gives each point $x$ mass $\mu_G(x) = 1/|G|$.

### `di_in_ff`
Lean (short): `[Fintype G] [Module (ZMod q) G] [DiscreteMeasurableSpace G] (hq : Nat.Prime q) (hε₀ : 0 < ε) (hε₁ : ε < 1) (hγC : γ ≤ ↑C.dens) (hγ : 0 < γ) (hAC : ε ≤ |↑(Fintype.card G) * ⟪mu A ∗ᵈ mu A, mu C⟫_[ℝ] - 1|) : ∃ V x, ↑(Module.finrank (ZMod q) G - Module.finrank (ZMod q) ↥V) ≤ 2 ^ 128 * (1 + Real.log (↑A.dens)⁻¹) ^ 4 * (1 + Real.log γ⁻¹) ^ 4 / ε ^ 12 ∧ (1 + ε / 32) * ↑A.dens ≤ ‖((↑A).indicator fun x => 1) ∗ᵈ mu (↑V).toFinset‖_[⊤]`
Lean (full): `∀ {G : Type u} [inst : AddCommGroup G] [inst_1 : Fintype G] {A C : Finset G} {γ ε : ℝ} {q : ℕ} [inst_2 : Module (ZMod q) G] [inst_3 : DecidableEq G] [inst_4 : MeasurableSpace G] [DiscreteMeasurableSpace G], Nat.Prime q → (0 : ℝ) < ε → ε < (1 : ℝ) → γ ≤ ↑C.dens → (0 : ℝ) < γ → ε ≤ |HMul.hMul (α := ℝ) ↑(Fintype.card G) ⟪mu A ∗ᵈ mu A, mu C⟫_[ℝ] - (1 : ℝ)| → ∃ (V : Submodule (ZMod q) G) (x : DecidablePred fun (x : G) => x ∈ V), ↑(Module.finrank (ZMod q) G - Module.finrank.{0, u} (ZMod q) ↥V) ≤ (2 : ℝ) ^ (128 : ℕ) * ((1 : ℝ) + Real.log (↑A.dens)⁻¹) ^ (4 : ℕ) * ((1 : ℝ) + Real.log γ⁻¹) ^ (4 : ℕ) / ε ^ (12 : ℕ) ∧ ((1 : ℝ) + ε / (32 : ℝ)) * ↑A.dens ≤ dLpNorm (E := ℝ) ⊤ (((↑A).indicator fun (x : G) => (1 : ℝ)) ∗ᵈ mu (↑V).toFinset)`
English: Let $q$ be a natural number that is prime, and let $G$ be a finite additive abelian group that is a module over $\mathbb{Z}/q\mathbb{Z}$, equipped with a measurable space structure that is discrete (every subset is measurable). Let $A, C$ be finite subsets of $G$ and let $\gamma, \varepsilon$ be real numbers with $0 < \varepsilon < 1$ and $0 < \gamma \le \operatorname{dens}(C)$, where $\operatorname{dens}(B) = |B|/|G|$ for a finite set $B \subseteq G$. For a finite set $B \subseteq G$ let $\mu_B : G \to \mathbb{R}$ be its normalised indicator, $\mu_B(x) = 1/|B|$ if $x \in B$ and $0$ otherwise, and let $1_B : G \to \mathbb{R}$ be its indicator function. For $f, g : G \to \mathbb{R}$ let $(f * g)(a) = \sum_{x + y = a} f(x) g(y)$ be their convolution. Suppose $\varepsilon \le \left| |G| \cdot \langle \mu_A * \mu_A, \mu_C \rangle_{\mathbb{R}} - 1 \right|$, where $\langle \cdot, \cdot \rangle_{\mathbb{R}}$ is the real inner product of functions $G \to \mathbb{R}$. Then there exists a $\mathbb{Z}/q\mathbb{Z}$-submodule $V$ of $G$ such that $$\dim G - \dim V \le \frac{2^{128}\,(1 + \log \operatorname{dens}(A)^{-1})^4\,(1 + \log \gamma^{-1})^4}{\varepsilon^{12}}$$ (dimensions over $\mathbb{Z}/q\mathbb{Z}$, the difference taken in the natural numbers) and $$\left(1 + \frac{\varepsilon}{32}\right)\operatorname{dens}(A) \le \|1_A * \mu_V\|_\infty,$$ where $\mu_V$ is the normalised indicator of the finite set $V$ and $\|h\|_\infty$ is the $L^\infty$ norm of $h : G \to \mathbb{R}$ with respect to the counting measure on $G$.

### `ff`
Lean (short): `[Fintype G] [Module (ZMod q) G] (hq₃ : 3 ≤ q) (hq : Nat.Prime q) (hA₀ : A.Nonempty) (hA : ThreeAPFree ↑A) : ↑(Module.finrank (ZMod q) G) ≤ 2 ^ 148 * (1 + Real.log (↑A.dens)⁻¹) ^ 9`
Lean (full): `∀ {G : Type u} [inst : AddCommGroup G] [inst_1 : Fintype G] {A : Finset G} {q : ℕ} [inst_2 : Module (ZMod q) G], (3 : ℕ) ≤ q → Nat.Prime q → A.Nonempty → ThreeAPFree ↑A → ↑(Module.finrank (ZMod q) G) ≤ (2 : ℝ) ^ (148 : ℕ) * ((1 : ℝ) + Real.log (↑A.dens)⁻¹) ^ (9 : ℕ)`
English: Let $q \ge 3$ be a prime and let $G$ be a finite vector space over $\mathbb{Z}/q\mathbb{Z}$. If $A \subseteq G$ is nonempty and contains no nontrivial three-term arithmetic progression, then $\dim G \le 2^{148}\,(1 + \log \operatorname{dens}(A)^{-1})^9$.
