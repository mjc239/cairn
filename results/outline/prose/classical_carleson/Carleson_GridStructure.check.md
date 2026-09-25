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
be supported by the docstring or the Lean. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `Grid.dist_strictMono`
Lean (short): `[GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hpq : I < J) : dist_{c I, ↑(defaultD a) ^ s I / 4} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / 4} f g`
Lean (full): `∀ {X : Type u_1} [inst : PseudoMetricSpace X] {a : ℕ} {q : ℝ} {K : X → X → ℂ} {σ₁ σ₂ : X → ℤ} {F G : Set X} [inst_1 : ProofData a q K σ₁ σ₂ F G] [inst_2 : GridStructure X (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] {I J : Grid X}, I < J → ∀ {f g : @Θ _ X DenselyNormedField.toNormedField UniformSpace.toTopologicalSpace _}, dist_{c I, ↑(defaultD a) ^ s I / (4 : ℝ)} f g ≤ C2_1_2 a * dist_{c J, ↑(defaultD a) ^ s J / (4 : ℝ)} f g`
Docstring: Stronger version of Lemma 2.1.2.
English: (Stronger version of Lemma 2.1.2) Let $X$ be a pseudometric space carrying the standing data $a\in\mathbb N$, $q$, $K$, $\sigma_1$, $\sigma_2$, $F$, $G$ of `ProofData` (so in particular $X$ is a doubling measure space with a compatible family $\Theta(X)$ of functions), together with a grid structure `GridStructure` on $X$ with the default parameters $D=D(a)$, $\kappa(a)$, $S(X)$. If $I<J$ are grid cubes, then for all $f,g\in\Theta(X)$ $$d_{c(I),\,D^{s(I)}/4}(f,g)\le C_{2.1.2}(a)\,d_{c(J),\,D^{s(J)}/4}(f,g),$$ where $d_{x,r}$ denotes the distance between functions on the ball $B(x,r)$.

### `Grid.succ`
Lean (short): `[GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (i : Grid X) : Grid X`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : GridStructure X (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Grid X → Grid X`
Docstring: If `i` is not a maximal element, this is the (unique) minimal element greater than i. This is not a `SuccOrder` since an element can be the successor of multiple other elements.
English: Let $X$ be a pseudometric space equipped with the standing Carleson data $\mathrm{ProofData}(a, q, K, \sigma_1, \sigma_2, F, G)$ (with $a \in \mathbb{N}$, $q \in \mathbb{R}$, a kernel $K : X \times X \to \mathbb{C}$, functions $\sigma_1, \sigma_2 : X \to \mathbb{Z}$ and sets $F, G \subseteq X$), and with a grid structure $\mathrm{GridStructure}(X, \mathrm{defaultD}(a), \mathrm{default}\kappa(a), \mathrm{defaultS}(X), \mathrm{cancelPt}(X))$. Definition: for a dyadic cube $i \in \mathrm{Grid}(X)$, a cube $\mathrm{succ}(i) \in \mathrm{Grid}(X)$. According to the docstring, if $i$ is not a maximal element, this is the (unique) minimal element greater than $i$; and this does not form a successor order, since an element can be the successor of multiple other elements.
