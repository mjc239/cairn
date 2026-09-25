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

## Translations

### `Real.marcinkiewicz_zygmund`
Lean (short): `(hm : m ≠ 0) (f : ι → ℝ) (hf : ∀ (i : Fin n), ∑ a ∈ Fintype.piFinset fun x => A, f (a i) = 0) : ∑ a ∈ Fintype.piFinset fun x => A, (∑ i, f (a i)) ^ (2 * m) ≤ (4 * ↑m) ^ m * ↑n ^ (m - 1) * ∑ a ∈ Fintype.piFinset fun x => A, ∑ i, f (a i) ^ (2 * m)`
Lean (full): `∀ {ι : Type u_1} {A : Finset ι} {m n : ℕ}, m ≠ (0 : ℕ) → ∀ (f : ι → ℝ), (∀ (i : Fin n), ∑ a ∈ Fintype.piFinset (δ := fun (x : Fin n) => ι) fun (x : Fin n) => A, f (a i) = (0 : ℝ)) → ∑ a ∈ Fintype.piFinset (δ := fun (x : Fin n) => ι) fun (x : Fin n) => A, HPow.hPow (α := ℝ) (∑ i : Fin n, f (a i)) ((2 : ℕ) * m) ≤ ((4 : ℝ) * ↑m) ^ m * HPow.hPow (α := ℝ) (↑n) (m - (1 : ℕ)) * ∑ a ∈ Fintype.piFinset (δ := fun (x : Fin n) => ι) fun (x : Fin n) => A, ∑ i : Fin n, f (a i) ^ ((2 : ℕ) * m)`
Docstring: The **Marcinkiewicz-Zygmund inequality** for real-valued functions, with a slightly easier to bound constant than `Real.marcinkiewicz_zygmund'`. Note that `RCLike.marcinkiewicz_zygmund` is another version that works for both `ℝ` and `ℂ` at the expense of a slightly worse constant.
English: (The Marcinkiewicz–Zygmund inequality for real-valued functions, per the docstring.) Let $\iota$ be a type, let $A \subseteq \iota$ be a finite set, and let $m, n$ be natural numbers with $m \ne 0$. Let $f : \iota \to \mathbb{R}$ satisfy $\sum_{a \in A^n} f(a_i) = 0$ for every $i \in \{0,\dots,n-1\}$, where $A^n$ denotes the finite set of $n$-tuples $a : \{0,\dots,n-1\} \to \iota$ with every entry in $A$. Then $\sum_{a \in A^n}\bigl(\sum_{i=0}^{n-1} f(a_i)\bigr)^{2m} \le (4m)^m\, n^{m-1} \sum_{a \in A^n}\sum_{i=0}^{n-1} f(a_i)^{2m}$, where $m-1$ is truncated subtraction of natural numbers.

### `RCLike.marcinkiewicz_zygmund`
Lean (short): `(hm : m ≠ 0) (f : ι → 𝕜) (hf : ∀ (i : Fin n), ∑ a ∈ Fintype.piFinset fun x => A, f (a i) = 0) : ∑ a ∈ Fintype.piFinset fun x => A, ‖∑ i, f (a i)‖ ^ (2 * m) ≤ (8 * ↑m) ^ m * ↑n ^ (m - 1) * ∑ a ∈ Fintype.piFinset fun x => A, ∑ i, ‖f (a i)‖ ^ (2 * m)`
Lean (full): `∀ {ι : Type u_1} {A : Finset ι} {m n : ℕ} {𝕜 : Type u_2} [inst : RCLike 𝕜], m ≠ (0 : ℕ) → ∀ (f : ι → 𝕜), (∀ (i : Fin n), ∑ a ∈ Fintype.piFinset (δ := fun (x : Fin n) => ι) fun (x : Fin n) => A, f (a i) = (0 : 𝕜)) → ∑ a ∈ Fintype.piFinset (δ := fun (x : Fin n) => ι) fun (x : Fin n) => A, norm.{u_2} (E := 𝕜) (∑ i : Fin n, f (a i)) ^ ((2 : ℕ) * m) ≤ ((8 : ℝ) * ↑m) ^ m * HPow.hPow (α := ℝ) (↑n) (m - (1 : ℕ)) * ∑ a ∈ Fintype.piFinset (δ := fun (x : Fin n) => ι) fun (x : Fin n) => A, ∑ i : Fin n, ‖f (a i)‖ ^ ((2 : ℕ) * m)`
Docstring: The **Marcinkiewicz-Zygmund inequality** for real- or complex-valued functions.
English: (The Marcinkiewicz–Zygmund inequality for real- or complex-valued functions, per the docstring.) Let $\iota$ be a type, let $A \subseteq \iota$ be a finite set, let $m, n$ be natural numbers with $m \ne 0$, and let $\mathbb{K}$ be an `RCLike` field (i.e. $\mathbb{R}$ or $\mathbb{C}$). Let $f : \iota \to \mathbb{K}$ satisfy $\sum_{a \in A^n} f(a_i) = 0$ for every $i \in \{0,\dots,n-1\}$, where $A^n$ denotes the finite set of $n$-tuples $a : \{0,\dots,n-1\} \to \iota$ with every entry in $A$. Then $\sum_{a \in A^n}\bigl\|\sum_{i=0}^{n-1} f(a_i)\bigr\|^{2m} \le (8m)^m\, n^{m-1} \sum_{a \in A^n}\sum_{i=0}^{n-1} \|f(a_i)\|^{2m}$, where $\|\cdot\|$ is the norm on $\mathbb{K}$ and $m-1$ is truncated subtraction of natural numbers.
