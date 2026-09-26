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
docstring, definition body (under "Project definitions") or Lean supports a description of an object, name it
instead of describing it. Give every variable its
type, introduce every symbol, and never use one letter for two things. When a definition's body is shown, say what
it defines, in words or a formula that agrees with the body.

Reply with only a JSON object: {"<lean name>": {"statement": "..."}}
Use every Lean name exactly as given.

Namespaces open (prefixes omitted): AlmostPeriodicity, MeasureTheory.

## Project definitions these statements use
(What each project notion is. Any description of one in the English must agree with this.)

#### `trivChar` (def)
Lean: `{G : Type u_1} → {R : Type u_3} → [DecidableEq G] → [AddCommGroup G] → [CommSemiring R] → G → R`
Docstring: The trivial character.
Definition: `fun {G : Type u_1} {R : Type u_3} [DecidableEq G] [AddCommGroup G] [CommSemiring R] (a : G) => if a = (0 : G) then (1 : R) else (0 : R)`

## Flagged translations

### `energy`
Lean (short): `(n : ℕ) (s : Finset G) (ν : G → ℂ) : ℝ`
Lean (full): `{G : Type u_1} → [AddCommGroup G] → ℕ → Finset G → (G → ℂ) → ℝ`
Definition: `fun {G : Type u_1} [AddCommGroup G] (n : ℕ) (s : Finset G) (ν : G → ℂ) => ∑ γ ∈ Fintype.piFinset (δ := fun (x : Fin n) => G) fun (x : Fin n) => s, ∑ δ ∈ Fintype.piFinset (δ := fun (x : Fin n) => G) fun (x : Fin n) => s, ‖ν (HSub.hSub (α := G) (∑ i : Fin n, γ i) (∑ i : Fin n, δ i))‖`
Previous English: Let $G$ be an abelian group. For a natural number $n$, a finite set $s \subseteq G$ and a function $\nu : G \to \mathbb{C}$, $\mathrm{energy}_n(s, \nu)$ is a real number.
Checker's issue: Definition body is shown but the English only says energy_n(s,ν) 'is a real number'; it must state energy_n(s,ν) = Σ_{γ,δ ∈ s^n} ‖ν(Σ_i γ_i − Σ_i δ_i)‖.

### `boringEnergy`
Lean (short): `(n : ℕ) (s : Finset G) : ℝ`
Lean (full): `{G : Type u_1} → [AddCommGroup G] → [DecidableEq G] → ℕ → Finset G → ℝ`
Definition: `fun {G : Type u_1} [AddCommGroup G] [DecidableEq G] (n : ℕ) (s : Finset G) => energy n s trivChar`
Previous English: Let $G$ be an abelian group. For a natural number $n$ and a finite set $s \subseteq G$, $\mathrm{boringEnergy}_n(s)$ is a real number.
Checker's issue: Definition body is shown but the English only says boringEnergy_n(s) 'is a real number'; it must state boringEnergy_n(s) = energy_n(s, trivChar) (number of pairs (γ,δ) ∈ s^n × s^n with Σγ_i = Σδ_i), and G needs decidable equality only implicitly.
