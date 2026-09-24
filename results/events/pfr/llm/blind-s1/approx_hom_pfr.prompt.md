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

- id `r114`: lemma; steps here: state and prove. Let $G$ be a finite abelian group, and let $A$ be a non-empty subset of $G$ with $E(A) \geq \frac{1}{K} \left( \frac{|A|}{|G|} \right)^3$ for some $K \geq 1$. Then there is a subset $A'$ of $A$ with $|A'| \geq |A| / (C_1 K^{C_2})$ and $|A'-A'| \leq C_3 K^{C_4} |A|$, where $$C_1 = 2^4, C_2 = 1, C_3 = 2^{10}, C_4 = 5.$$ The Lean statement gives the two conclusions as inequalities between densities; these are equivalent to the ones above, the common factor $|G|$ cancelling.
- id `r872`: lemma; steps here: state and prove. If $G$ is a finite additive group and $A,B$ are subsets of $G$, then $$ \left( \frac{|\{ (a,a') \in A \times A: a+a' \in B \}|}{|G|^2} \right)^2 \leq \frac{|B|}{|G|}\, E(A). $$ The left-hand side is the square of the density of a subset of $G \times G$, and the right-hand side involves the density of a subset of $G$.
- id `r873`: theorem; steps here: state and prove. Let $G,G'$ be finite abelian $2$-groups. Let $f: G \to G'$ be a function, and suppose that there are at least $|G|^2 / K$ pairs $(x,y) \in G^2$ such that $$ f(x+y) = f(x) + f(y).$$ Then there exists a homomorphism $\phi: G \to G'$ and a constant $c \in G'$ such that $f(x) = \phi(x)+c$ for at least $|G| / (2 ^ {144} * K ^ {122})$ values of $x \in G$.
- id `r387`: corollary; steps here: state and prove. Let $G,G'$ be finite abelian $2$-groups. Let $f: G \to G'$ be a function, and suppose that there are at least $|G|^2 / K$ pairs $(x,y) \in G^2$ such that $$ f(x+y) = f(x) + f(y).$$ Then there exists a homomorphism $\phi'': G \to G'$ such that $f(x) = \phi''(x)$ for at least $(|G| / (2 ^ {144} * K ^ {122}) - 1)/2$ values of $x \in G$.
- id `r355`: lemma; steps here: state and prove. Let $G$ be a finite abelian $2$-group, and let $A$ be a subset of $G$. Then there exists a homomorphism $\phi: G \to \Z/2\Z$ such that $|A \cap \phi^{-1}(1)| \geq (|A|-1)/2$.
- id `r375`: lemma; steps here: state and prove. Let $G$ be a finite abelian $2$-group, and let $x \in G$ be non-zero. Then there are $|G|/2$ homomorphisms $\phi: G \to \Z/2\Z$ such that $\phi(x) = 1$.
- id `r212`: definition; steps here: state only (no proof needed). If $G$ is a finite additive group and $A$ is a subset of $G$, the \emph{additive energy} $E(A)$ of $A$ is the normalized count $$ E(A) := \frac{|\{(a_1,a_2,a_3,a_4) \in A^4 : a_1+a_2 = a_3+a_4\}|}{|G|^3}. $$ The normalization by $|G|^3$ is the convention of \texttt{Finset.addEnergy'}, and every statement in this chapter that mentions $E(A)$ uses it.
- id `r916`: lemma; steps here: state and prove. Let $G$ be a finite abelian $2$-group. Then the finite abelian $2$-group $\mathrm{Hom}(G,\Z/2\Z)$ of homomorphisms from $G$ to $\Z/2\Z$ has the same order as $G$.

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r114` before `P:r873`
- `S:r212` before `P:r873`
- `S:r212` before `S:r114`
- `S:r212` before `S:r872`
- `S:r355` before `P:r387`
- `S:r375` before `P:r355`
- `S:r872` before `P:r873`
- `S:r873` before `P:r387`
- `S:r916` before `P:r355`
- `S:r916` before `P:r375`
