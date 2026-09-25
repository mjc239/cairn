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

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

### `Real.marcinkiewicz_zygmund`
Lean (short): `(hm : m ≠ 0) (f : ι → ℝ) (hf : ∀ (i : Fin n), ∑ a ∈ Fintype.piFinset fun x => A, f (a i) = 0) : ∑ a ∈ Fintype.piFinset fun x => A, (∑ i, f (a i)) ^ (2 * m) ≤ (4 * ↑m) ^ m * ↑n ^ (m - 1) * ∑ a ∈ Fintype.piFinset fun x => A, ∑ i, f (a i) ^ (2 * m)`
Lean (full): `∀ {ι : Type u_1} {A : Finset ι} {m n : ℕ}, m ≠ (0 : ℕ) → ∀ (f : ι → ℝ), (∀ (i : Fin n), ∑ a ∈ Fintype.piFinset (δ := fun x => ι) fun x => A, f (a i) = (0 : ℝ)) → ∑ a ∈ Fintype.piFinset (δ := fun x => ι) fun x => A, HPow.hPow (α := ℝ) (∑ i : Fin n, f (a i)) ((2 : ℕ) * m) ≤ ((4 : ℝ) * ↑m) ^ m * HPow.hPow (α := ℝ) (↑n) (m - (1 : ℕ)) * ∑ a ∈ Fintype.piFinset (δ := fun x => ι) fun x => A, ∑ i : Fin n, f (a i) ^ ((2 : ℕ) * m)`
Docstring: The **Marcinkiewicz-Zygmund inequality** for real-valued functions, with a slightly easier to bound constant than `Real.marcinkiewicz_zygmund'`. Note that `RCLike.marcinkiewicz_zygmund` is another version that works for both `ℝ` and `ℂ` at the expense of a slightly worse constant.
Previous English: Let $A$ be a finite subset of a type $\iota$, $n \in \mathbb{N}$, and $m \ne 0$. Let $f : \iota \to \mathbb{R}$ satisfy $\sum_{a \in A^n} f(a_i) = 0$ for every $i \in \{0,\dots,n-1\}$. Then $\sum_{a \in A^n}\bigl(\sum_i f(a_i)\bigr)^{2m} \le (4m)^m\, n^{m-1} \sum_{a \in A^n}\sum_i f(a_i)^{2m}$.
Checker's issue: The English never states that m is a natural number (only 'n ∈ ℕ, and m ≠ 0'); in the Lean m : ℕ, and this restrictive type matters for the exponent 2m, (m-1) and the constant.

### `RCLike.marcinkiewicz_zygmund`
Lean (short): `(hm : m ≠ 0) (f : ι → 𝕜) (hf : ∀ (i : Fin n), ∑ a ∈ Fintype.piFinset fun x => A, f (a i) = 0) : ∑ a ∈ Fintype.piFinset fun x => A, ‖∑ i, f (a i)‖ ^ (2 * m) ≤ (8 * ↑m) ^ m * ↑n ^ (m - 1) * ∑ a ∈ Fintype.piFinset fun x => A, ∑ i, ‖f (a i)‖ ^ (2 * m)`
Lean (full): `∀ {ι : Type u_1} {A : Finset ι} {m n : ℕ} {𝕜 : Type u_2} [inst : RCLike 𝕜], m ≠ (0 : ℕ) → ∀ (f : ι → 𝕜), (∀ (i : Fin n), ∑ a ∈ Fintype.piFinset (δ := fun x => ι) fun x => A, f (a i) = (0 : 𝕜)) → ∑ a ∈ Fintype.piFinset (δ := fun x => ι) fun x => A, norm.{u_2} (E := 𝕜) (∑ i : Fin n, f (a i)) ^ ((2 : ℕ) * m) ≤ ((8 : ℝ) * ↑m) ^ m * HPow.hPow (α := ℝ) (↑n) (m - (1 : ℕ)) * ∑ a ∈ Fintype.piFinset (δ := fun x => ι) fun x => A, ∑ i : Fin n, ‖f (a i)‖ ^ ((2 : ℕ) * m)`
Docstring: The **Marcinkiewicz-Zygmund inequality** for real- or complex-valued functions.
Previous English: Let $A$ be a finite subset of a type $\iota$, $n \in \mathbb{N}$, and $m \ne 0$. Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let $f : \iota \to \mathbb{K}$ satisfy $\sum_{a \in A^n} f(a_i) = 0$ for every $i \in \{0,\dots,n-1\}$. Then $\sum_{a \in A^n}\bigl|\sum_i f(a_i)\bigr|^{2m} \le (8m)^m\, n^{m-1} \sum_{a \in A^n}\sum_i |f(a_i)|^{2m}$.
Checker's issue: The English never states that m is a natural number (only 'n ∈ ℕ, and m ≠ 0'); in the Lean m : ℕ, and this restrictive type matters for the exponent 2m, (m-1) and the constant.
