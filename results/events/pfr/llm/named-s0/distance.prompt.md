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

- id `sumset-lower`: corollary (Independent lower bound on sumset); steps here: state and prove. If $X,Y$ are independent $G$-valued random variables, then $$\max(\bbH[X], \bbH[Y]) \leq \bbH[X\pm Y]. $$
- id `first-useful`: lemma (Comparison of Ruzsa distances, I); steps here: state and prove. Let $X, Y, Z$ be random variables taking values in some abelian group of characteristic $2$, and with $Y, Z$ independent. Then we have \begin{align}\nonumber d[X ; Y + Z] -d[X ; Y] & \leq \tfrac{1}{2} (\bbH[Y+ Z] - \bbH[Y]) \\ & = \tfrac{1}{2} d[Y; Z] + \tfrac{1}{4} \bbH[Z] - \tfrac{1}{4} \bbH[Y]. \end{align} and \begin{align}\nonumber d[X ;Y|Y+ Z] - d[X ;Y] & \leq \tfrac{1}{2} \bigl(\bbH[Y+ Z] - \bbH[Z]\bigr) \\ & = \tfrac{1}{2} d[Y;Z] + \tfrac{1}{4} \bbH[Y] - \tfrac{1}{4} \bbH[Z]. \end{align}
- id `sumset-lower-gen-cond`: corollary (Conditional lower bound on sumset); steps here: state and prove. If $X,Y$ are $G$-valued random variables on $\Omega$ and $Z$ is another random variable on $\Omega$ then \[ \max(\bbH[X|Z], \bbH[Y|Z]) - \bbI[X:Y|Z] \leq \bbH[X\pm Y|Z], \]
- id `copy-ent`: lemma (Copy preserves entropy); steps here: state and prove. If $X'$ is a copy of $X$ then $\bbH[X'] = \bbH[X]$.
- id `cond-dist-fact`: lemma (Upper bound on conditioned Ruzsa distance); steps here: state and prove. Suppose that $(X, Z)$ and $(Y, W)$ are random variables, where $X, Y$ take values in an abelian group. Then \[ d[X | Z;Y | W] \leq d[X ; Y] + \tfrac{1}{2} \bbI[X : Z] + \tfrac{1}{2} \bbI[Y : W].\] In particular, \[ d[X ;Y | W] \leq d[X ; Y] + \tfrac{1}{2} \bbI[Y : W].\]
- id `sumset-lower-gen`: lemma (Lower bound of sumset); steps here: state and prove. If $X,Y$ are $G$-valued random variables on $\Omega$, we have $$ \max(\bbH[X], \bbH[Y]) - \bbI[X:Y] \leq \bbH[X \pm Y].$$
- id `ruz-copy`: lemma (Copy preserves Ruzsa distance); steps here: state and prove. If $X',Y'$ are copies of $X,Y$ respectively then $d[X';Y']=d[X ;Y]$.
- id `ruz-dist-def`: definition (Ruzsa distance); steps here: state only (no proof needed). Let $X,Y$ be $G$-valued random variables (not necessarily on the same sample space). The \emph{Ruzsa distance} $d[X ;Y]$ between $X$ and $Y$ is defined to be $$ d[X ;Y] := \bbH[X' - Y'] - \bbH[X']/2 - \bbH[Y']/2$$ where $X',Y'$ are (the canonical) independent copies of $X,Y$ from \Cref{independent-exist}.
- id `second-useful`: lemma (Comparison of Ruzsa distances, II); steps here: state and prove. Let $X, Y, Z, Z'$ be random variables taking values in some abelian group, and with $Y, Z, Z'$ independent. Then we have \begin{align}\nonumber & d[X ;Y + Z | Y + Z + Z'] - d[X ;Y] \\ & \qquad \leq \tfrac{1}{2} ( \bbH[Y + Z + Z'] + \bbH[Y + Z] - \bbH[Y] - \bbH[Z']). \end{align}
- id `cond-indep-exist`: lemma (Existence of conditional independent trials); steps here: state and prove. For $X,Y$ random variables, there exist random variables $X_1,X_2,Y'$ on a common probability space with $(X_1, Y'), (X_2, Y')$ both having the distribution of $(X,Y)$, and $X_1, X_2$ conditionally independent over $Y'$ in the sense of \Cref{conditional-independent-def}.
- id `shear-ent`: lemma (Shearing preserves entropy); steps here: state and prove. If $X,Y$ are $G$-valued, then $\bbH[X \pm Y | Y]=\bbH[X|Y]$ and $\bbH[X \pm Y, Y] = \bbH[X, Y]$.
- id `entropic-bsg`: lemma (Balog-Szemer\'edi-Gowers); steps here: state and prove. Let $A,B$ be $G$-valued random variables on $\Omega$, and set $Z := A+B$. Then \begin{equation} \sum_{z} \bbP[Z=z] d[(A | Z = z); (B | Z = z)] \leq 3 \bbI[A:B] + 2 \bbH[Z] - \bbH[A] - \bbH[B]. \end{equation}
- id `cond-dist-def`: definition (Conditioned Ruzsa distance); steps here: state only (no proof needed). If $(X, Z)$ and $(Y, W)$ are random variables (where $X$ and $Y$ are $G$-valued) we define $$ d[X | Z; Y | W] := \sum_{z,w} \bbP[Z=z] \bbP[W=w] d[(X|Z=z); (Y|(W=w))].$$ similarly $$ d[X ; Y | W] := \sum_{w} \bbP[W=w] d[X ; (Y|(W=w))].$$
- id `ruzsa-diff`: lemma (Distance controls entropy difference); steps here: state and prove. If $X,Y$ are $G$-valued random variables, then $$|\bbH[X]-H[Y]| \leq 2 d[X ;Y].$$
- id `neg-ent`: lemma (Negation preserves entropy); steps here: state and prove. If $X$ is $G$-valued, then $\bbH[-X]=\bbH[X]$.
- id `dist-zero`: lemma (Distance from zero); steps here: state and prove. If $X$ is a $G$-valued random variable and $0$ is the random variable taking the value $0$ everywhere then \[d[X;0]=\mathbb{H}(X)/2.\]
- id `ruzsa-triangle-improved`: lemma (Improved Ruzsa triangle inequality); steps here: state and prove. If $X,Y,Z$ are $G$-valued random variables on $\Omega$ with $(X,Y)$ independent of $Z$, then \begin{equation} \bbH[X - Y] \leq \bbH[X-Z] + \bbH[Z-Y] - \bbH[Z]\end{equation}
- id `ruzsa-nonneg`: lemma (Distance nonnegative); steps here: state and prove. If $X,Y$ are $G$-valued random variables, then $$ d[X ;Y] \geq 0.$$
- id `dist-projection`: lemma (Projection entropy and distance); steps here: state and prove. If $G$ is an additive group and $X$ is a $G$-valued random variable and $H\leq G$ is a finite subgroup then, with $\pi:G\to G/H$ the natural homomorphism we have (where $U_H$ is uniform on $H$) \[\mathbb{H}(\pi(X))\leq 2d[X;U_H].\]
- id `ruzsa-triangle`: lemma (Ruzsa triangle inequality); steps here: state and prove. If $X,Y,Z$ are $G$-valued random variables, then $$ d[X ;Y] \leq d[X ;Z] + d[Z;Y].$$
- id `independent-exist`: lemma (Existence of independent copies); steps here: state and prove. Let $X_i : \Omega_i \to S_i$ be random variables for $i=1,\dots,k$. Then if one gives $\prod_{i=1}^k S_i$ the product measure of the laws of $X_i$, the coordinate functions $(x_j)_{j=1}^k \mapsto x_i$ are jointly independent random variables which are copies of the $X_1,\dots,X_k$.
- id `kv`: lemma (Kaimanovich-Vershik-Madiman inequality); steps here: state and prove. Suppose that $X, Y, Z$ are independent $G$-valued random variables. Then \[ \bbH[X + Y + Z] - \bbH[X + Y] \leq \bbH[Y+ Z] - \bbH[Y]. \]
- id `cond-dist-alt`: lemma (Alternate form of distance); steps here: state and prove. The expression $d[X | Z;Y | W]$ is unchanged if $(X,Z)$ or $(Y,W)$ is replaced by a copy. Furthermore, if $(X,Z)$ and $(Y,W)$ are independent, then $$ d[X | Z;Y | W] = \bbH[X-Y|Z,W] - \bbH[X|Z]/2 - \bbH[Y|W]/2$$ and similarly $$ d[X ;Y | W] = \bbH[X-Y|W] - \bbH[X]/2 - \bbH[Y|W]/2.$$
- id `ruz-indep`: lemma (Ruzsa distance in independent case); steps here: state and prove. If $X,Y$ are independent $G$-random variables then $$ d[X ;Y] := \bbH[X - Y] - \bbH[X]/2 - \bbH[Y]/2.$$
- id `ruzsa-growth`: lemma (Distance controls entropy growth); steps here: state and prove. If $X,Y$ are independent $G$-valued random variables, then $$ \bbH[X-Y] - \bbH[X], \bbH[X-Y] - \bbH[Y] \leq 2d[X ;Y].$$
- id `ruzsa-symm`: lemma (Distance symmetric); steps here: state and prove. If $X,Y$ are $G$-valued random variables, then $$ d[X ;Y] = d[Y;X].$$

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:cond-dist-alt` before `P:cond-dist-fact`
- `S:cond-dist-def` before `P:first-useful`
- `S:cond-dist-def` before `P:second-useful`
- `S:cond-dist-def` before `S:cond-dist-alt`
- `S:cond-dist-def` before `S:cond-dist-fact`
- `S:cond-dist-fact` before `P:first-useful`
- `S:cond-indep-exist` before `P:entropic-bsg`
- `S:copy-ent` before `P:cond-dist-fact`
- `S:copy-ent` before `P:dist-projection`
- `S:copy-ent` before `P:entropic-bsg`
- `S:copy-ent` before `P:first-useful`
- `S:copy-ent` before `P:ruz-copy`
- `S:copy-ent` before `P:ruzsa-diff`
- `S:first-useful` before `P:second-useful`
- `S:independent-exist` before `P:cond-dist-fact`
- `S:independent-exist` before `P:dist-projection`
- `S:independent-exist` before `P:first-useful`
- `S:independent-exist` before `P:ruzsa-diff`
- `S:independent-exist` before `P:ruzsa-triangle`
- `S:kv` before `P:first-useful`
- `S:neg-ent` before `P:first-useful`
- `S:neg-ent` before `P:ruzsa-symm`
- `S:neg-ent` before `P:ruzsa-triangle-improved`
- `S:ruz-copy` before `P:cond-dist-fact`
- `S:ruz-copy` before `P:dist-projection`
- `S:ruz-copy` before `P:first-useful`
- `S:ruz-copy` before `P:ruzsa-diff`
- `S:ruz-copy` before `P:ruzsa-triangle`
- `S:ruz-dist-def` before `P:ruz-indep`
- `S:ruz-dist-def` before `P:ruzsa-symm`
- `S:ruz-indep` before `P:cond-dist-fact`
- `S:ruz-indep` before `P:dist-projection`
- `S:ruz-indep` before `P:entropic-bsg`
- `S:ruz-indep` before `P:first-useful`
- `S:ruz-indep` before `P:ruzsa-diff`
- `S:ruz-indep` before `P:ruzsa-growth`
- `S:ruz-indep` before `P:ruzsa-triangle`
- `S:ruzsa-diff` before `P:dist-projection`
- `S:ruzsa-diff` before `P:ruzsa-nonneg`
- `S:ruzsa-triangle-improved` before `P:ruzsa-triangle`
- `S:shear-ent` before `P:dist-projection`
- `S:shear-ent` before `P:sumset-lower-gen`
- `S:sumset-lower` before `P:ruzsa-diff`
- `S:sumset-lower` before `P:ruzsa-growth`
- `S:sumset-lower-gen` before `P:sumset-lower`
