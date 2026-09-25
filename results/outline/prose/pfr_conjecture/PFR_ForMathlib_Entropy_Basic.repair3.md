You are correcting translations of verified Lean statements into mathematical English.
An independent checker found the English statements below unfaithful to the Lean. For each, write a corrected
statement in clear mathematical English (LaTeX between $...$), fixing the issue the checker raised. Be faithful to
the FULL Lean statement: keep every hypothesis, including the assumptions carried by instance arguments, stated in
words ("G is a finite abelian group", "μ is a probability measure", "X is a metric space"), and the exact
conclusion. Only instances with no mathematical content (decidability: `Decidable…`) may stay unstated. Never
replace an assumption by a stronger one, and state restrictive types (a natural number, a nonnegative real). For a
definition, name the setting its signature assumes. Keep citations and remarks only if the docstring or the Lean
supports them. Do not add
claims the Lean does not make; attribute anything beyond a definition's signature to its docstring.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): ProbabilityTheory, MeasureTheory.

### `ProbabilityTheory.entropy`
Lean (short): `(X : Ω → S) (μ : autoParam (Measure Ω) entropy._auto_1) : ℝ`
Lean (full): `{Ω : Type u_1} → {S : Type u_2} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → (Ω → S) → autoParam (Measure Ω) entropy._auto_1 → ℝ`
Docstring: Entropy of a random variable with values in a finite measurable space.
Previous English: For a random variable $X : \Omega \to S$ (with $S$ a measurable space) and a measure $\mu$ on $\Omega$ (by default the canonical measure on $\Omega$), the entropy $H[X;\mu] \in \mathbb{R}$ is defined as the measure entropy of the law $X_*\mu$ of $X$ under $\mu$.
Checker's issue: The gloss 'defined as the measure entropy of the law X_*mu' goes beyond the signature and is not attributed to the docstring.

### `ProbabilityTheory.condEntropy`
Lean (short): `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) condEntropy._auto_1) : ℝ`
Lean (full): `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → autoParam (Measure Ω) condEntropy._auto_1 → ℝ`
Docstring: Conditional entropy of a random variable w.r.t. another. This is the expectation under the law of `Y` of the entropy of the law of `X` conditioned on the event `Y = y`.
Previous English: For random variables $X : \Omega \to S$, $Y : \Omega \to T$ and a measure $\mu$, the conditional entropy $H[X \mid Y;\mu]$ is defined as the expectation, under the law of $Y$, of the entropy of the law of $X$ conditioned on the event $Y = y$.
Checker's issue: The gloss describing the definition as an expectation of conditional entropies is not attributed to the docstring, and the measurable-space structures on Omega, S, T are not stated.

### `ProbabilityTheory.condMutualInfo`
Lean (short): `(X : Ω → S) (Y : Ω → T) (Z : Ω → U) (μ : autoParam (Measure Ω) condMutualInfo._auto_1) : ℝ`
Lean (full): `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → {U : Type u_4} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace U] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → (Ω → U) → autoParam (Measure Ω) condMutualInfo._auto_1 → ℝ`
Docstring: The conditional mutual information `I[X : Y| Z]` is the mutual information of `X| Z=z` and `Y| Z=z`, integrated over `z`.
Previous English: For random variables $X, Y, Z$ on $\Omega$ and a measure $\mu$, the conditional mutual information $I[X : Y \mid Z;\mu]$ is defined as the mutual information of $X$ and $Y$ under $\mu$ conditioned on $Z = z$, integrated over $z$ with respect to the law of $Z$.
Checker's issue: The gloss describing the definition as an integral of conditional mutual informations is not attributed to the docstring, and the measurable-space structures on Omega, S, T, U are not stated.

### `ProbabilityTheory.mutualInfo`
Lean (short): `(X : Ω → S) (Y : Ω → T) (μ : autoParam (Measure Ω) mutualInfo._auto_1) : ℝ`
Lean (full): `{Ω : Type u_1} → {S : Type u_2} → {T : Type u_3} → [mΩ : MeasurableSpace Ω] → [MeasurableSpace S] → [MeasurableSpace T] → (Ω → S) → (Ω → T) → autoParam (Measure Ω) mutualInfo._auto_1 → ℝ`
Docstring: The mutual information `I[X : Y]` of two random variables is defined to be `H[X] + H[Y] - H[X ; Y]`.
Previous English: For random variables $X, Y$ on $\Omega$ and a measure $\mu$, the mutual information is defined as $I[X : Y] := H[X] + H[Y] - H[(X,Y)]$.
Checker's issue: The defining formula H[X]+H[Y]-H[(X,Y)] is a gloss beyond the signature not attributed to the docstring (and drops the dependence on mu), and the measurable-space structures are not stated.
