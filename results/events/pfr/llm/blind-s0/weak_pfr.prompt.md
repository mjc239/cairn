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

- id `r816`: theorem; steps here: state and prove. If $A,B\subseteq \mathbb{Z}^d$ are finite non-empty sets then there exist non-empty $A'\subseteq A$ and $B'\subseteq B$ such that \[\log\frac{\lvert A\rvert\lvert B\rvert}{\lvert A'\rvert\lvert B'\rvert}\leq 34d[U_A;U_B]\] such that $\max(\dim A',\dim B')\leq \frac{40}{\log 2} d[U_A;U_B]$.
- id `r500`: lemma; steps here: state and prove. Let $G=\mathbb{F}_2^n$ and $\alpha\in (0,1)$ and let $X,Y$ be $G$-valued random variables such that \[\mathbb{H}(X)+\mathbb{H}(Y)> \frac{20}{\alpha} d[X;Y].\] There is a non-trivial subgroup $H\leq G$ such that \[\log \lvert H\rvert <\frac{1+\alpha}{2}(\mathbb{H}(X)+\mathbb{H}(Y))\] and \[\mathbb{H}(\psi(X))+\mathbb{H}(\psi(Y))< \alpha (\mathbb{H}(X)+\mathbb{H}(Y))\] where $\psi:G\to G/H$ is the natural projection homomorphism.
- id `r304`: theorem; steps here: state and prove. If $A\subseteq \mathbb{Z}^d$ is a finite non-empty set with $d[U_A;U_A]\leq \log K$ then there exists a non-empty $A'\subseteq A$ such that \[\lvert A'\rvert\geq K^{-17}\lvert A\rvert\] and $\dim A'\leq \frac{40}{\log 2} \log K$.
- id `r366`: lemma; steps here: state and prove. If $G=\mathbb{F}_2^d$ and $\alpha\in (0,1)$ and $X,Y$ are $G$-valued random variables then there is a subgroup $H\leq \mathbb{F}_2^d$ such that \[\log \lvert H\rvert \leq \frac{1+\alpha}{2(1-\alpha)} (\mathbb{H}(X)+\mathbb{H}(Y))\] and if $\psi:G \to G/H$ is the natural projection then \[\mathbb{H}(\psi(X))+\mathbb{H}(\psi(Y))\leq \frac{20}{\alpha} d[\psi(X);\psi(Y)].\]
- id `r467`: theorem; steps here: state and prove. Let $A\subseteq \mathbb{Z}^d$ and $\lvert A-A\rvert\leq K\lvert A\rvert$. There exists $A'\subseteq A$ such that $\lvert A'\rvert \geq K^{-17}\lvert A\rvert$ and $\dim A' \leq \frac{40}{\log 2}\log K$.
- id `r849`: lemma; steps here: state and prove. If $G$ is torsion-free and $X,Y$ are $G$-valued random variables then $d[X;2Y]\leq 5d[X;Y]$.
- id `r581`: lemma; steps here: state and prove. If $G$ is a torsion-free group and $X,Y$ are $G$-valued random variables and $\phi:G\to \mathbb{F}_2^d$ is a homomorphism then \[\mathbb{H}(\phi(X))\leq 10d[X;Y].\]
- id `r958`: definition; steps here: state only (no proof needed). If $A\subseteq \mathbb{Z}^{d}$ then by $\dim(A)$ we mean the dimension of the span of $A-A$ over the reals -- equivalently, the smallest $d'$ such that $A$ lies in a coset of a subgroup isomorphic to $\mathbb{Z}^{d'}$.
- id `r683`: lemma; steps here: state and prove. Let $\phi:G\to H$ be a homomorphism and $A,B\subseteq G$ be finite subsets. If $x,y\in H$ then let $A_x=A\cap \phi^{-1}(x)$ and $B_y=B\cap \phi^{-1}(y)$. There exist $x,y\in H$ such that $A_x,B_y$ are both non-empty and \[d[\phi(U_A);\phi(U_B)]\log \frac{\lvert A\rvert\lvert B\rvert}{\lvert A_x\rvert\lvert B_y\rvert}\leq (\mathbb{H}(\phi(U_A))+\mathbb{H}(\phi(U_B)))(d(U_A,U_B)-d(U_{A_x},U_{B_y})).\]
- id `r273`: lemma; steps here: state and prove. If $G=\mathbb{F}_2^d$ and $\alpha\in (0,1)$ and $X,Y$ are $G$-valued random variables then there is a subgroup $H\leq \mathbb{F}_2^d$ such that \[\log \lvert H\rvert \leq 2 (\mathbb{H}(X)+\mathbb{H}(Y))\] and if $\psi:G \to G/H$ is the natural projection then \[\mathbb{H}(\psi(X))+\mathbb{H}(\psi(Y))\leq 34 d[\psi(X);\psi(Y)].\]

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r273` before `P:r816`
- `S:r304` before `P:r467`
- `S:r366` before `P:r273`
- `S:r500` before `P:r366`
- `S:r581` before `P:r816`
- `S:r683` before `P:r816`
- `S:r816` before `P:r304`
- `S:r849` before `P:r581`
- `S:r958` before `P:r816`
- `S:r958` before `S:r304`
- `S:r958` before `S:r467`
