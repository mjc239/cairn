You are checking translations of verified Lean statements into mathematical English.
For each result below, compare the English statement with the Lean statement. The Lean statement shows explicit
hypotheses and meaningful instance assumptions (e.g. `[Finite G]`); implicit arguments and purely structural
instances (e.g. `[AddCommGroup G]`) are omitted, and the English may leave them implicit too.

Mark `faithful: false` if the English adds, drops, strengthens or weakens a hypothesis or the conclusion, gets a
quantifier, inequality direction or constant wrong, or misreads the notation. Stylistic choices are fine.

Reply with only a JSON object: {"<lean name>": {"faithful": true | false, "issue": "<empty, or what is wrong>"}}
Use every Lean name exactly as given.

### `carlesonOn`
Lean: `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) (_ : X) : ℂ`
English: For a tile $\mathfrak p$ and $f:X\to\mathbb C$, defines the function $T_{\mathfrak p}f:X\to\mathbb C$, the operator of Proposition 2.0.2.

### `carlesonSum`
Lean: `[TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
English: For a set of tiles $\mathfrak C$ and $f:X\to\mathbb C$, defines $T_{\mathfrak C}f:X\to\mathbb C$, the operator defined at the end of Section 7.4.

### `adjointCarleson`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (p : 𝔓 X) (f : X → ℂ) (x : X) : ℂ`
English: For a tile $\mathfrak p$ and $f:X\to\mathbb C$, defines the adjoint operator $T^*_{\mathfrak p}f:X\to\mathbb C$, as defined above Lemma 7.4.1.

### `adjointCarlesonSum`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (ℭ : Set (𝔓 X)) (f : X → ℂ) (x : X) : ℂ`
English: For a set of tiles $\mathfrak C$ and $f:X\to\mathbb C$, defines $T^*_{\mathfrak C}f:X\to\mathbb C$, as defined at the end of Section 7.4.

### `adjointCarlesonSum_adjoint`
Lean: `[ProofData a q K σ₁ σ₂ F G] [TileStructure Q (defaultD a) (defaultκ a) (defaultS X) (cancelPt X)] (hf : BoundedCompactSupport f volume) (hg : BoundedCompactSupport g volume) (ℭ : Set (𝔓 X)) : ∫ (x : X), (starRingEnd ℂ) (g x) * carlesonSum ℭ f x = ∫ (x : X), (starRingEnd ℂ) (adjointCarlesonSum ℭ g x) * f x`
English: Let $f,g$ be bounded with compact support and let $\mathfrak C$ be a set of tiles. Then $$\int_X\overline{g(x)}\,T_{\mathfrak C}f(x)\,dx=\int_X\overline{T^*_{\mathfrak C}g(x)}\,f(x)\,dx,$$ i.e. $T^*_{\mathfrak C}$ is the adjoint of $T_{\mathfrak C}$.
