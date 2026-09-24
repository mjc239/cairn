You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `sumset-lower`: corollary (Independent lower bound on sumset). If $X,Y$ are independent $G$-valued random variables, then $$\max(\bbH[X], \bbH[Y]) \leq \bbH[X\pm Y]. $$
- id `first-useful`: lemma (Comparison of Ruzsa distances, I). Let $X, Y, Z$ be random variables taking values in some abelian group of characteristic $2$, and with $Y, Z$ independent. Then we have \begin{align}\nonumber d[X ; Y + Z] -d[X ; Y] & \leq \tfrac{1}{2} (\bbH[Y+ Z] - \bbH[Y]) \\ & = \tfrac{1}{2} d[Y; Z] + \tfrac{1}{4} \bbH[Z] - \tfrac{1}{4} \bbH[Y]. \end{align} and \begin{align}\nonumber d[X ;Y|Y+ Z] - d[X ;Y] & \leq \tfrac{1}{2} \bigl(\bbH[Y+ Z] - \bbH[Z]\bigr) \\ & = \tfrac{1}{2} d[Y;Z] + \tfrac{1}{4} \bbH[Y] - \tfrac{1}{4} \bbH[Z]. \end{align}
- id `sumset-lower-gen-cond`: corollary (Conditional lower bound on sumset). If $X,Y$ are $G$-valued random variables on $\Omega$ and $Z$ is another random variable on $\Omega$ then \[ \max(\bbH[X|Z], \bbH[Y|Z]) - \bbI[X:Y|Z] \leq \bbH[X\pm Y|Z], \]
- id `copy-ent`: lemma (Copy preserves entropy). If $X'$ is a copy of $X$ then $\bbH[X'] = \bbH[X]$.
- id `cond-dist-fact`: lemma (Upper bound on conditioned Ruzsa distance). Suppose that $(X, Z)$ and $(Y, W)$ are random variables, where $X, Y$ take values in an abelian group. Then \[ d[X | Z;Y | W] \leq d[X ; Y] + \tfrac{1}{2} \bbI[X : Z] + \tfrac{1}{2} \bbI[Y : W].\] In particular, \[ d[X ;Y | W] \leq d[X ; Y] + \tfrac{1}{2} \bbI[Y : W].\]
- id `sumset-lower-gen`: lemma (Lower bound of sumset). If $X,Y$ are $G$-valued random variables on $\Omega$, we have $$ \max(\bbH[X], \bbH[Y]) - \bbI[X:Y] \leq \bbH[X \pm Y].$$
- id `ruz-copy`: lemma (Copy preserves Ruzsa distance). If $X',Y'$ are copies of $X,Y$ respectively then $d[X';Y']=d[X ;Y]$.
- id `ruz-dist-def`: definition (Ruzsa distance). Let $X,Y$ be $G$-valued random variables (not necessarily on the same sample space). The \emph{Ruzsa distance} $d[X ;Y]$ between $X$ and $Y$ is defined to be $$ d[X ;Y] := \bbH[X' - Y'] - \bbH[X']/2 - \bbH[Y']/2$$ where $X',Y'$ are (the canonical) independent copies of $X,Y$ from \Cref{independent-exist}.
- id `second-useful`: lemma (Comparison of Ruzsa distances, II). Let $X, Y, Z, Z'$ be random variables taking values in some abelian group, and with $Y, Z, Z'$ independent. Then we have \begin{align}\nonumber & d[X ;Y + Z | Y + Z + Z'] - d[X ;Y] \\ & \qquad \leq \tfrac{1}{2} ( \bbH[Y + Z + Z'] + \bbH[Y + Z] - \bbH[Y] - \bbH[Z']). \end{align}
- id `cond-indep-exist`: lemma (Existence of conditional independent trials). For $X,Y$ random variables, there exist random variables $X_1,X_2,Y'$ on a common probability space with $(X_1, Y'), (X_2, Y')$ both having the distribution of $(X,Y)$, and $X_1, X_2$ conditionally independent over $Y'$ in the sense of \Cref{conditional-independent-def}.
- id `shear-ent`: lemma (Shearing preserves entropy). If $X,Y$ are $G$-valued, then $\bbH[X \pm Y | Y]=\bbH[X|Y]$ and $\bbH[X \pm Y, Y] = \bbH[X, Y]$.
- id `entropic-bsg`: lemma (Balog-Szemer\'edi-Gowers). Let $A,B$ be $G$-valued random variables on $\Omega$, and set $Z := A+B$. Then \begin{equation} \sum_{z} \bbP[Z=z] d[(A | Z = z); (B | Z = z)] \leq 3 \bbI[A:B] + 2 \bbH[Z] - \bbH[A] - \bbH[B]. \end{equation}
- id `cond-dist-def`: definition (Conditioned Ruzsa distance). If $(X, Z)$ and $(Y, W)$ are random variables (where $X$ and $Y$ are $G$-valued) we define $$ d[X | Z; Y | W] := \sum_{z,w} \bbP[Z=z] \bbP[W=w] d[(X|Z=z); (Y|(W=w))].$$ similarly $$ d[X ; Y | W] := \sum_{w} \bbP[W=w] d[X ; (Y|(W=w))].$$
- id `ruzsa-diff`: lemma (Distance controls entropy difference). If $X,Y$ are $G$-valued random variables, then $$|\bbH[X]-H[Y]| \leq 2 d[X ;Y].$$
- id `neg-ent`: lemma (Negation preserves entropy). If $X$ is $G$-valued, then $\bbH[-X]=\bbH[X]$.
- id `dist-zero`: lemma (Distance from zero). If $X$ is a $G$-valued random variable and $0$ is the random variable taking the value $0$ everywhere then \[d[X;0]=\mathbb{H}(X)/2.\]
- id `ruzsa-triangle-improved`: lemma (Improved Ruzsa triangle inequality). If $X,Y,Z$ are $G$-valued random variables on $\Omega$ with $(X,Y)$ independent of $Z$, then \begin{equation} \bbH[X - Y] \leq \bbH[X-Z] + \bbH[Z-Y] - \bbH[Z]\end{equation}
- id `ruzsa-nonneg`: lemma (Distance nonnegative). If $X,Y$ are $G$-valued random variables, then $$ d[X ;Y] \geq 0.$$
- id `dist-projection`: lemma (Projection entropy and distance). If $G$ is an additive group and $X$ is a $G$-valued random variable and $H\leq G$ is a finite subgroup then, with $\pi:G\to G/H$ the natural homomorphism we have (where $U_H$ is uniform on $H$) \[\mathbb{H}(\pi(X))\leq 2d[X;U_H].\]
- id `ruzsa-triangle`: lemma (Ruzsa triangle inequality). If $X,Y,Z$ are $G$-valued random variables, then $$ d[X ;Y] \leq d[X ;Z] + d[Z;Y].$$
- id `independent-exist`: lemma (Existence of independent copies). Let $X_i : \Omega_i \to S_i$ be random variables for $i=1,\dots,k$. Then if one gives $\prod_{i=1}^k S_i$ the product measure of the laws of $X_i$, the coordinate functions $(x_j)_{j=1}^k \mapsto x_i$ are jointly independent random variables which are copies of the $X_1,\dots,X_k$.
- id `kv`: lemma (Kaimanovich-Vershik-Madiman inequality). Suppose that $X, Y, Z$ are independent $G$-valued random variables. Then \[ \bbH[X + Y + Z] - \bbH[X + Y] \leq \bbH[Y+ Z] - \bbH[Y]. \]
- id `cond-dist-alt`: lemma (Alternate form of distance). The expression $d[X | Z;Y | W]$ is unchanged if $(X,Z)$ or $(Y,W)$ is replaced by a copy. Furthermore, if $(X,Z)$ and $(Y,W)$ are independent, then $$ d[X | Z;Y | W] = \bbH[X-Y|Z,W] - \bbH[X|Z]/2 - \bbH[Y|W]/2$$ and similarly $$ d[X ;Y | W] = \bbH[X-Y|W] - \bbH[X]/2 - \bbH[Y|W]/2.$$
- id `ruz-indep`: lemma (Ruzsa distance in independent case). If $X,Y$ are independent $G$-random variables then $$ d[X ;Y] := \bbH[X - Y] - \bbH[X]/2 - \bbH[Y]/2.$$
- id `ruzsa-growth`: lemma (Distance controls entropy growth). If $X,Y$ are independent $G$-valued random variables, then $$ \bbH[X-Y] - \bbH[X], \bbH[X-Y] - \bbH[Y] \leq 2d[X ;Y].$$
- id `ruzsa-symm`: lemma (Distance symmetric). If $X,Y$ are $G$-valued random variables, then $$ d[X ;Y] = d[Y;X].$$

## Constraints

- `cond-dist-alt` before `cond-dist-fact`
- `cond-dist-def` before `cond-dist-alt`
- `cond-dist-def` before `cond-dist-fact`
- `cond-dist-def` before `first-useful`
- `cond-dist-def` before `second-useful`
- `cond-dist-fact` before `first-useful`
- `cond-indep-exist` before `entropic-bsg`
- `copy-ent` before `cond-dist-fact`
- `copy-ent` before `dist-projection`
- `copy-ent` before `entropic-bsg`
- `copy-ent` before `first-useful`
- `copy-ent` before `ruz-copy`
- `copy-ent` before `ruzsa-diff`
- `first-useful` before `second-useful`
- `independent-exist` before `cond-dist-fact`
- `independent-exist` before `dist-projection`
- `independent-exist` before `first-useful`
- `independent-exist` before `ruzsa-diff`
- `independent-exist` before `ruzsa-triangle`
- `kv` before `first-useful`
- `neg-ent` before `first-useful`
- `neg-ent` before `ruzsa-symm`
- `neg-ent` before `ruzsa-triangle-improved`
- `ruz-copy` before `cond-dist-fact`
- `ruz-copy` before `dist-projection`
- `ruz-copy` before `first-useful`
- `ruz-copy` before `ruzsa-diff`
- `ruz-copy` before `ruzsa-triangle`
- `ruz-dist-def` before `ruz-indep`
- `ruz-dist-def` before `ruzsa-symm`
- `ruz-indep` before `cond-dist-fact`
- `ruz-indep` before `dist-projection`
- `ruz-indep` before `entropic-bsg`
- `ruz-indep` before `first-useful`
- `ruz-indep` before `ruzsa-diff`
- `ruz-indep` before `ruzsa-growth`
- `ruz-indep` before `ruzsa-triangle`
- `ruzsa-diff` before `dist-projection`
- `ruzsa-diff` before `ruzsa-nonneg`
- `ruzsa-triangle-improved` before `ruzsa-triangle`
- `shear-ent` before `dist-projection`
- `shear-ent` before `sumset-lower-gen`
- `sumset-lower` before `ruzsa-diff`
- `sumset-lower` before `ruzsa-growth`
- `sumset-lower-gen` before `sumset-lower`
