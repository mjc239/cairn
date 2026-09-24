You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, propositions, theorems), in an arbitrary order, each with an id and its statement.

You decide the order of two kinds of step:
- `S:<id>` means *state* the result;
- `P:<id>` means *prove* it.
Each result says which of its steps belong to this chapter; include exactly those.

You may prove a result immediately after stating it, or state it early (for instance, announce the goal of
the chapter first) and prove it later, once the lemmas its proof needs have been developed. Whichever you
choose, respect every constraint below. A proof may use any result that has already been *stated*, even if
that result's own proof comes later.

Choose the order that makes the chapter clearest for a mathematician reading it for the first time.

Reply with only a JSON array containing every step exactly once, in your chosen order,
e.g. ["S:a", "S:b", "P:b", "P:a"].

## Results

- id `bsg`: lemma (Balog--Szemer\'edi--Gowers lemma); steps here: state and prove. Let $G$ be a finite abelian group, and let $A$ be a non-empty subset of $G$ with $E(A) \geq \frac{1}{K} \left( \frac{|A|}{|G|} \right)^3$ for some $K \geq 1$. Then there is a subset $A'$ of $A$ with $|A'| \geq |A| / (C_1 K^{C_2})$ and $|A'-A'| \leq C_3 K^{C_4} |A|$, where $$C_1 = 2^4, C_2 = 1, C_3 = 2^{10}, C_4 = 5.$$ The Lean statement gives the two conclusions as inequalities between densities; these are equivalent to the ones above, the common factor $|G|$ cancelling.
- id `cs-bound`: lemma (Cauchy--Schwarz bound); steps here: state and prove. If $G$ is a finite additive group and $A,B$ are subsets of $G$, then $$ \left( \frac{|\{ (a,a') \in A \times A: a+a' \in B \}|}{|G|^2} \right)^2 \leq \frac{|B|}{|G|}\, E(A). $$ The left-hand side is the square of the density of a subset of $G \times G$, and the right-hand side involves the density of a subset of $G$.
- id `gdual`: lemma (Duality); steps here: state and prove. Let $G$ be a finite abelian $2$-group. Then the finite abelian $2$-group $\mathrm{Hom}(G,\Z/2\Z)$ of homomorphisms from $G$ to $\Z/2\Z$ has the same order as $G$.
- id `gslice`: lemma (Slicing); steps here: state and prove. Let $G$ be a finite abelian $2$-group, and let $A$ be a subset of $G$. Then there exists a homomorphism $\phi: G \to \Z/2\Z$ such that $|A \cap \phi^{-1}(1)| \geq (|A|-1)/2$.
- id `energy-def`: definition (Additive energy); steps here: state only (no proof needed). If $G$ is a finite additive group and $A$ is a subset of $G$, the \emph{additive energy} $E(A)$ of $A$ is the normalized count $$ E(A) := \frac{|\{(a_1,a_2,a_3,a_4) \in A^4 : a_1+a_2 = a_3+a_4\}|}{|G|^3}. $$ The normalization by $|G|^3$ is the convention of \texttt{Finset.addEnergy'}, and every statement in this chapter that mentions $E(A)$ uses it.
- id `approx-hom-pfr-no-const`: corollary (Approximate homomorphism form of PFR, no constant term); steps here: state and prove. Let $G,G'$ be finite abelian $2$-groups. Let $f: G \to G'$ be a function, and suppose that there are at least $|G|^2 / K$ pairs $(x,y) \in G^2$ such that $$ f(x+y) = f(x) + f(y).$$ Then there exists a homomorphism $\phi'': G \to G'$ such that $f(x) = \phi''(x)$ for at least $(|G| / (2 ^ {144} * K ^ {122}) - 1)/2$ values of $x \in G$.
- id `approx-hom-pfr`: theorem (Approximate homomorphism form of PFR); steps here: state and prove. Let $G,G'$ be finite abelian $2$-groups. Let $f: G \to G'$ be a function, and suppose that there are at least $|G|^2 / K$ pairs $(x,y) \in G^2$ such that $$ f(x+y) = f(x) + f(y).$$ Then there exists a homomorphism $\phi: G \to G'$ and a constant $c \in G'$ such that $f(x) = \phi(x)+c$ for at least $|G| / (2 ^ {144} * K ^ {122})$ values of $x \in G$.
- id `gcount`: lemma (Counting); steps here: state and prove. Let $G$ be a finite abelian $2$-group, and let $x \in G$ be non-zero. Then there are $|G|/2$ homomorphisms $\phi: G \to \Z/2\Z$ such that $\phi(x) = 1$.

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:approx-hom-pfr` before `P:approx-hom-pfr-no-const`
- `S:bsg` before `P:approx-hom-pfr`
- `S:cs-bound` before `P:approx-hom-pfr`
- `S:energy-def` before `P:approx-hom-pfr`
- `S:energy-def` before `S:bsg`
- `S:energy-def` before `S:cs-bound`
- `S:gcount` before `P:gslice`
- `S:gdual` before `P:gcount`
- `S:gdual` before `P:gslice`
- `S:gslice` before `P:approx-hom-pfr-no-const`
