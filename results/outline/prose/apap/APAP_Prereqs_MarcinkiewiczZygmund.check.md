You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `Real.marcinkiewicz_zygmund`
Lean: `(hm : m ≠ 0) (f : ι → ℝ) (hf : ∀ (i : Fin n), ∑ a ∈ Fintype.piFinset fun x => A, f (a i) = 0) : ∑ a ∈ Fintype.piFinset fun x => A, (∑ i, f (a i)) ^ (2 * m) ≤ (4 * ↑m) ^ m * ↑n ^ (m - 1) * ∑ a ∈ Fintype.piFinset fun x => A, ∑ i, f (a i) ^ (2 * m)`
English: Let $A$ be a finite subset of a type $\iota$, $n \in \mathbb{N}$, and $m \ne 0$. Let $f : \iota \to \mathbb{R}$ satisfy $\sum_{a \in A^n} f(a_i) = 0$ for every $i \in \{0,\dots,n-1\}$. Then $\sum_{a \in A^n}\bigl(\sum_i f(a_i)\bigr)^{2m} \le (4m)^m\, n^{m-1} \sum_{a \in A^n}\sum_i f(a_i)^{2m}$.

### `RCLike.marcinkiewicz_zygmund`
Lean: `(hm : m ≠ 0) (f : ι → 𝕜) (hf : ∀ (i : Fin n), ∑ a ∈ Fintype.piFinset fun x => A, f (a i) = 0) : ∑ a ∈ Fintype.piFinset fun x => A, ‖∑ i, f (a i)‖ ^ (2 * m) ≤ (8 * ↑m) ^ m * ↑n ^ (m - 1) * ∑ a ∈ Fintype.piFinset fun x => A, ∑ i, ‖f (a i)‖ ^ (2 * m)`
English: Let $A$ be a finite subset of a type $\iota$, $n \in \mathbb{N}$, and $m \ne 0$. Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let $f : \iota \to \mathbb{K}$ satisfy $\sum_{a \in A^n} f(a_i) = 0$ for every $i \in \{0,\dots,n-1\}$. Then $\sum_{a \in A^n}\bigl|\sum_i f(a_i)\bigr|^{2m} \le (8m)^m\, n^{m-1} \sum_{a \in A^n}\sum_i |f(a_i)|^{2m}$.
