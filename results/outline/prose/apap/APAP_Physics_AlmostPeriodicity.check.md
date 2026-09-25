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

#### `MeasureTheory.dLpNorm` (def)
Lean: `{α : Type u_1} → {E : Type u_4} → [MeasurableSpace α] → [NormedAddCommGroup E] → ENNReal → (α → E) → ℝ`
Docstring: The Lp norm of a function with the compact normalisation.
Definition: `fun {α : Type u_1} {E : Type u_4} [inst : MeasurableSpace α] [NormedAddCommGroup E] (p : ENNReal) (f : α → E) => lpNorm (m0 := inst) f p Measure.count`

#### `ddconv` (def)
Lean: `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [Fintype G] → [CommSemiring R] → (G → R) → (G → R) → G → R`
Docstring: Convolution
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [Fintype G] [CommSemiring R] (f g : G → R) (a : G) => ∑ x : G × G with x.1 + x.2 = a, f x.1 * g x.2`

#### `mu` (def)
Lean: `{K : Type u_1} → {α : Type u_3} → [DivisionSemiring K] → Finset α → α → K`
Docstring: The normalised indicator_one of a set.
Definition: `fun {K : Type u_1} {α : Type u_3} [DivisionSemiring K] (s : Finset α) => HSMul.hSMul (α := K) (β := α → K) (↑s.card)⁻¹ ((↑s).indicator fun (x : α) => (1 : K))`

#### `iterConv` (def)
Lean: `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [Fintype G] → [CommSemiring R] → (G → R) → ℕ → G → R`
Docstring: Iterated convolution.
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [Fintype G] [CommSemiring R] (f : G → R) (x : ℕ) => Nat.brecOn (motive := fun (x : ℕ) => G → R) x (iterConv._f f)`

#### `trivChar` (def)
Lean: `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [CommSemiring R] → G → R`
Docstring: The trivial character.
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [CommSemiring R] (a : G) => if a = (0 : G) then (1 : R) else (0 : R)`

## Translations

### `AlmostPeriodicity.LProp`
Lean (short): `[Fintype G] (k : ℕ) (m : ℕ) (ε : ℝ) (f : G → ℂ) (A : Finset G) (a : Fin k → G) : Prop`
Lean (full): `{G : Type u_1} → [Fintype G] → [DecidableEq G] → [AddCommGroup G] → [MeasurableSpace G] → (k : ℕ) → ℕ → ℝ → (G → ℂ) → Finset G → (Fin k → G) → Prop`
Definition: `fun {G : Type u_1} [Fintype G] [DecidableEq G] [AddCommGroup G] [MeasurableSpace G] (k m : ℕ) (ε : ℝ) (f : G → ℂ) (A : Finset G) (a : Fin k → G) => (dLpNorm (E := ℂ) ((2 : ENNReal) * ↑m) fun (x : G) => ∑ i : Fin k, f (x - a i) - (k • (mu A ∗ᵈ f)) x) ≤ ↑k * ε * ‖f‖_[(2 : ENNReal) * ↑m]`
English: Let $G$ be a finite additive commutative group equipped with a measurable space structure. For natural numbers $k, m \in \mathbb{N}$, a real number $\varepsilon \in \mathbb{R}$, a function $f : G \to \mathbb{C}$, a finite set $A \subseteq G$ and a $k$-tuple $a : \mathrm{Fin}\,k \to G$, $\mathrm{LProp}(k,m,\varepsilon,f,A,a)$ is a proposition.

### `AlmostPeriodicity.l`
Lean (short): `[Fintype G] (k : ℕ) (m : ℕ) (ε : ℝ) (f : G → ℂ) (A : Finset G) : Finset (Fin k → G)`
Lean (full): `{G : Type u_1} → [Fintype G] → [DecidableEq G] → [AddCommGroup G] → [MeasurableSpace G] → (k : ℕ) → ℕ → ℝ → (G → ℂ) → Finset G → Finset (Fin k → G)`
Definition: `fun {G : Type u_1} [Fintype G] [DecidableEq G] [AddCommGroup G] [MeasurableSpace G] (k m : ℕ) (ε : ℝ) (f : G → ℂ) (A : Finset G) => {x ∈ Fintype.piFinset (δ := fun (a : Fin k) => G) fun (x : Fin k) => A | LProp✝ k m ε f A x}`
English: Let $G$ be a finite additive commutative group equipped with a measurable space structure. For natural numbers $k, m \in \mathbb{N}$, a real number $\varepsilon \in \mathbb{R}$, a function $f : G \to \mathbb{C}$ and a finite set $A \subseteq G$, $l(k,m,\varepsilon,f,A)$ is a finite set of $k$-tuples $a : \mathrm{Fin}\,k \to G$.

### `AlmostPeriodicity.just_the_triangle_inequality`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (ha : a ∈ l k m ε f A) (ha' : (a + fun x => t) ∈ l k m ε f A) (hk : 0 < k) (hm : 1 ≤ m) : ‖translate (-t) (mu A ∗ᵈ f) - mu A ∗ᵈ f‖_[2 * ↑m] ≤ 2 * ε * ‖f‖_[2 * ↑m]`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] {A : Finset G} {f : G → ℂ} {ε : ℝ} {k m : ℕ} [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G] {t : G} {a : Fin k → G}, a ∈ l k m ε f A → (a + fun (x : Fin k) => t) ∈ l k m ε f A → (0 : ℕ) < k → (1 : ℕ) ≤ m → ‖translate (-t) (mu A ∗ᵈ f) - mu A ∗ᵈ f‖_[(2 : ENNReal) * ↑m] ≤ (2 : ℝ) * ε * ‖f‖_[(2 : ENNReal) * ↑m]`
English: Let $G$ be a finite additive commutative group (with decidable equality), equipped with a measurable-space structure that is discrete (every subset of $G$ is measurable). Let $A$ be a finite subset of $G$, $f : G \to \mathbb{C}$, $\varepsilon \in \mathbb{R}$, and $k, m \in \mathbb{N}$. Write $L := $ `AlmostPeriodicity.l k m ε f A`, a finite set of $k$-tuples $x : \mathrm{Fin}\ k \to G$ (the project set named `l`). Let $t \in G$ and $a : \mathrm{Fin}\ k \to G$. Suppose $a \in L$, the shifted tuple $i \mapsto a_i + t$ also lies in $L$, $k > 0$ and $m \ge 1$. Then
$$\|\tau_{-t}(\mu_A \ast f) - \mu_A \ast f\|_{[2m]} \le 2\varepsilon\,\|f\|_{[2m]},$$
where: $\mu_A : G \to \mathbb{C}$ (`mu A`) is the normalised indicator $\mu_A = |A|^{-1}\,\mathbf{1}_A$, with $\mathbf{1}_A$ equal to $1$ on $A$ and $0$ elsewhere; for $g, h : G \to \mathbb{C}$, $g \ast h$ (`ddconv`, $\ast^{d}$) is the convolution $(g \ast h)(z) = \sum_{(x,y) \in G \times G,\ x + y = z} g(x)\,h(y)$; for $s \in G$ and $g : G \to \mathbb{C}$, $\tau_s g$ denotes the function `translate s g`; and for $g : G \to \mathbb{C}$ and $r \in [0,\infty]$, $\|g\|_{[r]}$ denotes `dLpNorm r g`, the real-valued $L^r$ norm of $g$ with respect to the counting measure on $G$ (here $r = 2m \in [0,\infty]$).

### `AlmostPeriodicity.lemma28`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (hε : 0 < ε) (hm : 1 ≤ m) (hk : 64 * ↑m / ε ^ 2 ≤ ↑k) : ↑A.card ^ k / 2 ≤ ↑(l k m ε f A).card`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] {A : Finset G} {f : G → ℂ} {ε : ℝ} {k m : ℕ} [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G], (0 : ℝ) < ε → (1 : ℕ) ≤ m → (64 : ℝ) * ↑m / ε ^ (2 : ℕ) ≤ ↑k → HPow.hPow (α := ℝ) (↑A.card) k / (2 : ℝ) ≤ ↑(l k m ε f A).card`
English: Let $G$ be a finite additive commutative group (with decidable equality), equipped with a measurable-space structure that is discrete (every subset of $G$ is measurable). Let $A$ be a finite subset of $G$, $f : G \to \mathbb{C}$, $\varepsilon \in \mathbb{R}$, and $k, m \in \mathbb{N}$. Write $L := $ `AlmostPeriodicity.l k m ε f A`, a finite set of $k$-tuples $x : \mathrm{Fin}\ k \to G$ (the project set named `l`). If $\varepsilon > 0$, $m \ge 1$ and $64m/\varepsilon^2 \le k$ (in $\mathbb{R}$), then $|A|^k/2 \le |L|$ (as real numbers), where $|\cdot|$ denotes the cardinality of a finite set.

### `AlmostPeriodicity.almost_periodicity`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (ε : ℝ) (hε : 0 < ε) (hε' : ε ≤ 1) (m : ℕ) (f : G → ℂ) (hK₂ : 2 ≤ K) (hK : ↑(A.addConst S) ≤ K) : ∃ T, K ^ (-512 * ↑m / ε ^ 2) * ↑S.card ≤ ↑T.card ∧ ∀ t ∈ T, ‖translate t (mu A ∗ᵈ f) - mu A ∗ᵈ f‖_[2 * ↑m] ≤ ε * ‖f‖_[2 * ↑m]`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] {A S : Finset G} {K : ℝ} [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G] (ε : ℝ), (0 : ℝ) < ε → ε ≤ (1 : ℝ) → ∀ (m : ℕ) (f : G → ℂ), (2 : ℝ) ≤ K → ↑(A.addConst S) ≤ K → ∃ (T : Finset G), K ^ ((-512 : ℝ) * ↑m / ε ^ (2 : ℕ)) * ↑S.card ≤ ↑T.card ∧ ∀ t ∈ T, ‖translate t (mu A ∗ᵈ f) - mu A ∗ᵈ f‖_[(2 : ENNReal) * ↑m] ≤ ε * ‖f‖_[(2 : ENNReal) * ↑m]`
English: Let $G$ be a finite additive commutative group (with decidable equality) equipped with a measurable-space structure that is discrete (every subset of $G$ is measurable). Let $A$ and $S$ be finite subsets of $G$ and $K$ a real number, and let $\sigma[A,S]$ denotes $\mathrm{Finset.addConst}\ A\ S = |A+S|/|A|$ (a nonnegative rational, viewed as a real number), with $A + S = \{x+y : x \in A, y \in S\}$ the sumset. Let $\varepsilon$ be a real number with $0 < \varepsilon \le 1$, let $m$ be a natural number and $f : G \to \mathbb{C}$. Suppose $2 \le K$ and $\sigma[A,S] \le K$. Then there is a finite set $T \subseteq G$ with $K^{-512m/\varepsilon^2}\,|S| \le |T|$ (real power) such that for every $t \in T$,
$$\|\tau_t(\mu_A \ast f) - \mu_A \ast f\|_{[2m]} \le \varepsilon\,\|f\|_{[2m]},$$
where $\mu_X : G \to \mathbb{C}$ (Lean's $\mathrm{mu}\ X$) is the function $\mu_X = |X|^{-1}\,\mathbf{1}_X$ for a finite set $X \subseteq G$, where $\mathbf{1}_X$ is the indicator function of $X$ with value $1$ on $X$ and $0$ elsewhere; for $g, h : G \to \mathbb{C}$, $g \ast h$ (Lean's $\mathrm{ddconv}$, $\ast^{d}$) is the function $(g \ast h)(z) = \sum_{(x,y) \in G \times G,\ x + y = z} g(x)\,h(y)$; for $s \in G$ and $g : G \to \mathbb{C}$, $\tau_s g$ denotes $\mathrm{translate}\ s\ g$, the translate of $g$ by $s$; and for $g : G \to \mathbb{C}$ and $r \in [0,\infty]$, $\|g\|_{[r]}$ denotes $\mathrm{dLpNorm}\ r\ g$, the $L^r$ norm of $g$ taken with respect to the counting measure on $G$.

### `AlmostPeriodicity.linfty_almost_periodicity`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (ε : ℝ) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (hK₂ : 2 ≤ K) (hK : ↑(A.addConst S) ≤ K) (B : Finset G) (C : Finset G) (hB : B.Nonempty) (hC : C.Nonempty) : ∃ T, K ^ (-4096 * ↑⌈1 + Real.log (min 1 (↑C.card / ↑B.card))⁻¹⌉ / ε ^ 2) * ↑S.card ≤ ↑T.card ∧ ∀ t ∈ T, ‖translate t ((mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C) - (mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C‖_[⊤] ≤ ε`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] {A S : Finset G} {K : ℝ} [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G] (ε : ℝ), (0 : ℝ) < ε → ε ≤ (1 : ℝ) → (2 : ℝ) ≤ K → ↑(A.addConst S) ≤ K → ∀ (B C : Finset G), B.Nonempty → C.Nonempty → ∃ (T : Finset G), K ^ ((-4096 : ℝ) * ↑⌈(1 : ℝ) + Real.log (min (1 : ℝ) (HDiv.hDiv (α := ℝ) ↑C.card ↑B.card))⁻¹⌉ / ε ^ (2 : ℕ)) * ↑S.card ≤ ↑T.card ∧ ∀ t ∈ T, ‖HSub.hSub (α := G → ℂ) (translate t ((mu A ∗ᵈ (↑B).indicator fun (x : G) => (1 : ℂ)) ∗ᵈ mu C)) ((mu A ∗ᵈ (↑B).indicator fun (x : G) => (1 : ℂ)) ∗ᵈ mu C)‖_[⊤] ≤ ε`
English: Let $G$ be a finite additive commutative group (with decidable equality) equipped with a measurable-space structure that is discrete (every subset of $G$ is measurable). Let $A$ and $S$ be finite subsets of $G$ and $K$ a real number, and let $\sigma[A,S]$ denotes $\mathrm{Finset.addConst}\ A\ S = |A+S|/|A|$ (a nonnegative rational, viewed as a real number), with $A + S = \{x+y : x \in A, y \in S\}$ the sumset. Let $\varepsilon$ be a real number with $0 < \varepsilon \le 1$, and suppose $2 \le K$ and $\sigma[A,S] \le K$. Let $B$ and $C$ be nonempty finite subsets of $G$, and put $F = (\mu_A \ast \mathbf{1}_B) \ast \mu_C : G \to \mathbb{C}$ and $L = \big\lceil 1 + \log\big((\min(1, |C|/|B|))^{-1}\big)\big\rceil$ (integer ceiling, $\log$ the real natural logarithm). Then there is a finite set $T \subseteq G$ with $K^{-4096 L/\varepsilon^2}\,|S| \le |T|$ (real power) such that for every $t \in T$, $\|\tau_t F - F\|_{[\infty]} \le \varepsilon$. Here $\mu_X : G \to \mathbb{C}$ (Lean's $\mathrm{mu}\ X$) is the function $\mu_X = |X|^{-1}\,\mathbf{1}_X$ for a finite set $X \subseteq G$, where $\mathbf{1}_X$ is the indicator function of $X$ with value $1$ on $X$ and $0$ elsewhere; for $g, h : G \to \mathbb{C}$, $g \ast h$ (Lean's $\mathrm{ddconv}$, $\ast^{d}$) is the function $(g \ast h)(z) = \sum_{(x,y) \in G \times G,\ x + y = z} g(x)\,h(y)$; for $s \in G$ and $g : G \to \mathbb{C}$, $\tau_s g$ denotes $\mathrm{translate}\ s\ g$, the translate of $g$ by $s$; and for $g : G \to \mathbb{C}$ and $r \in [0,\infty]$, $\|g\|_{[r]}$ denotes $\mathrm{dLpNorm}\ r\ g$, the $L^r$ norm of $g$ taken with respect to the counting measure on $G$.

### `AlmostPeriodicity.linfty_almost_periodicity_boosted`
Lean (short): `[Fintype G] [DiscreteMeasurableSpace G] (ε : ℝ) (hε₀ : 0 < ε) (hε₁ : ε ≤ 1) (k : ℕ) (hk : k ≠ 0) (hK₂ : 2 ≤ K) (hK : ↑(A.addConst S) ≤ K) (hS : S.Nonempty) (B : Finset G) (C : Finset G) (hB : B.Nonempty) (hC : C.Nonempty) : ∃ T, K ^ (-4096 * ↑⌈1 + Real.log (min 1 (↑C.card / ↑B.card))⁻¹⌉ * ↑k ^ 2 / ε ^ 2) * ↑S.card ≤ ↑T.card ∧ ‖mu T ∗ᵈ^ k ∗ᵈ ((mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C) - (mu A ∗ᵈ (↑B).indicator fun x => 1) ∗ᵈ mu C‖_[⊤] ≤ ε`
Lean (full): `∀ {G : Type u_1} [inst : Fintype G] {A S : Finset G} {K : ℝ} [inst_1 : DecidableEq G] [inst_2 : AddCommGroup G] [inst_3 : MeasurableSpace G] [DiscreteMeasurableSpace G] (ε : ℝ), (0 : ℝ) < ε → ε ≤ (1 : ℝ) → ∀ (k : ℕ), k ≠ (0 : ℕ) → (2 : ℝ) ≤ K → ↑(A.addConst S) ≤ K → S.Nonempty → ∀ (B C : Finset G), B.Nonempty → C.Nonempty → ∃ (T : Finset G), K ^ ((-4096 : ℝ) * ↑⌈(1 : ℝ) + Real.log (min (1 : ℝ) (HDiv.hDiv (α := ℝ) ↑C.card ↑B.card))⁻¹⌉ * HPow.hPow (α := ℝ) ↑k (2 : ℕ) / ε ^ (2 : ℕ)) * ↑S.card ≤ ↑T.card ∧ ‖HSub.hSub (α := G → ℂ) (mu T ∗ᵈ^ k ∗ᵈ ((mu A ∗ᵈ (↑B).indicator fun (x : G) => (1 : ℂ)) ∗ᵈ mu C)) ((mu A ∗ᵈ (↑B).indicator fun (x : G) => (1 : ℂ)) ∗ᵈ mu C)‖_[⊤] ≤ ε`
English: Let $G$ be a finite additive commutative group (with decidable equality) equipped with a measurable-space structure that is discrete (every subset of $G$ is measurable). Let $A$ and $S$ be finite subsets of $G$ and $K$ a real number, and let $\sigma[A,S]$ denotes $\mathrm{Finset.addConst}\ A\ S = |A+S|/|A|$ (a nonnegative rational, viewed as a real number), with $A + S = \{x+y : x \in A, y \in S\}$ the sumset. Let $\varepsilon$ be a real number with $0 < \varepsilon \le 1$ and $k$ a natural number with $k \ne 0$; suppose $2 \le K$, $\sigma[A,S] \le K$, and $S$ is nonempty. Let $B$ and $C$ be nonempty finite subsets of $G$, and put $F = (\mu_A \ast \mathbf{1}_B) \ast \mu_C : G \to \mathbb{C}$ and $L = \big\lceil 1 + \log\big((\min(1, |C|/|B|))^{-1}\big)\big\rceil$ (integer ceiling, $\log$ the real natural logarithm). Then there is a finite set $T \subseteq G$ with $K^{-4096 L k^2/\varepsilon^2}\,|S| \le |T|$ (real power) and
$$\|\mu_T^{\ast k} \ast F - F\|_{[\infty]} \le \varepsilon,$$
where $\mu_T^{\ast k}$ is the $k$-th iterated convolution of $\mu_T$ (Lean's $\mathrm{iterConv}\ \mu_T\ k$, $\ast^{d\,k}$). Here $\mu_X : G \to \mathbb{C}$ (Lean's $\mathrm{mu}\ X$) is the function $\mu_X = |X|^{-1}\,\mathbf{1}_X$ for a finite set $X \subseteq G$, where $\mathbf{1}_X$ is the indicator function of $X$ with value $1$ on $X$ and $0$ elsewhere; for $g, h : G \to \mathbb{C}$, $g \ast h$ (Lean's $\mathrm{ddconv}$, $\ast^{d}$) is the function $(g \ast h)(z) = \sum_{(x,y) \in G \times G,\ x + y = z} g(x)\,h(y)$; and for $g : G \to \mathbb{C}$ and $r \in [0,\infty]$, $\|g\|_{[r]}$ denotes $\mathrm{dLpNorm}\ r\ g$, the $L^r$ norm of $g$ taken with respect to the counting measure on $G$.
