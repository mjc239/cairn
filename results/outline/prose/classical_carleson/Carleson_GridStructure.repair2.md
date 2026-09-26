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

Namespaces open (prefixes omitted): TileStructure, MeasureTheory, Antichain.

### `Grid.succ`
Lean (short): `[GridStructure X (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (i : Grid X) : Grid X`
Lean (full): `{X : Type u_1} → [inst : PseudoMetricSpace X] → {a : ℕ} → {q : ℝ} → {K : X → X → ℂ} → {σ₁ σ₂ : X → ℤ} → {F G : Set X} → [inst_1 : ProofData a q K σ₁ σ₂ F G] → [inst_2 : GridStructure X (defaultD a) (defaultκ a) (defaultS X (F := F) (G := G)) (cancelPt X)] → Grid X → Grid X`
Docstring: If `i` is not a maximal element, this is the (unique) minimal element greater than i. This is not a `SuccOrder` since an element can be the successor of multiple other elements.
Previous English: For a dyadic cube $i\in\mathrm{Grid}(X)$, defines $\mathrm{succ}(i)$: if $i$ is not maximal, the unique minimal cube strictly greater than $i$ (its parent). This is not a successor order, since a cube can be the successor of several cubes.
Checker's issue: The definition omits its setting (pseudometric space X with ProofData and GridStructure), and the parent/non-successor-order gloss is not attributed to the docstring.
