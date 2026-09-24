You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `r432`: lemma. If $X,Y$ are $G$-valued random variables on $\Omega$, we have $$ \max(\bbH[X], \bbH[Y]) - \bbI[X:Y] \leq \bbH[X \pm Y].$$
- id `r934`: lemma. If $X$ is $G$-valued, then $\bbH[-X]=\bbH[X]$.
- id `r816`: lemma. If $X,Y$ are $G$-valued, then $\bbH[X \pm Y | Y]=\bbH[X|Y]$ and $\bbH[X \pm Y, Y] = \bbH[X, Y]$.
- id `r955`: corollary. If $X,Y$ are $G$-valued random variables on $\Omega$ and $Z$ is another random variable on $\Omega$ then \[ \max(\bbH[X|Z], \bbH[Y|Z]) - \bbI[X:Y|Z] \leq \bbH[X\pm Y|Z], \]
- id `r270`: lemma. Let $X_i : \Omega_i \to S_i$ be random variables for $i=1,\dots,k$. Then if one gives $\prod_{i=1}^k S_i$ the product measure of the laws of $X_i$, the coordinate functions $(x_j)_{j=1}^k \mapsto x_i$ are jointly independent random variables which are copies of the $X_1,\dots,X_k$.
- id `r997`: lemma. If $X,Y$ are independent $G$-valued random variables, then $$ \bbH[X-Y] - \bbH[X], \bbH[X-Y] - \bbH[Y] \leq 2d[X ;Y].$$
- id `r731`: corollary. If $X,Y$ are independent $G$-valued random variables, then $$\max(\bbH[X], \bbH[Y]) \leq \bbH[X\pm Y]. $$
- id `r374`: lemma. Let $X, Y, Z$ be random variables taking values in some abelian group of characteristic $2$, and with $Y, Z$ independent. Then we have \begin{align}\nonumber d[X ; Y + Z] -d[X ; Y] & \leq \tfrac{1}{2} (\bbH[Y+ Z] - \bbH[Y]) \\ & = \tfrac{1}{2} d[Y; Z] + \tfrac{1}{4} \bbH[Z] - \tfrac{1}{4} \bbH[Y]. \end{align} and \begin{align}\nonumber d[X ;Y|Y+ Z] - d[X ;Y] & \leq \tfrac{1}{2} \bigl(\bbH[Y+ Z] - \bbH[Z]\bigr) \\ & = \tfrac{1}{2} d[Y;Z] + \tfrac{1}{4} \bbH[Y] - \tfrac{1}{4} \bbH[Z]. \end{align}
- id `r891`: lemma. If $X',Y'$ are copies of $X,Y$ respectively then $d[X';Y']=d[X ;Y]$.
- id `r591`: definition. If $(X, Z)$ and $(Y, W)$ are random variables (where $X$ and $Y$ are $G$-valued) we define $$ d[X | Z; Y | W] := \sum_{z,w} \bbP[Z=z] \bbP[W=w] d[(X|Z=z); (Y|(W=w))].$$ similarly $$ d[X ; Y | W] := \sum_{w} \bbP[W=w] d[X ; (Y|(W=w))].$$
- id `r416`: lemma. If $X,Y$ are independent $G$-random variables then $$ d[X ;Y] := \bbH[X - Y] - \bbH[X]/2 - \bbH[Y]/2.$$
- id `r410`: lemma. Let $A,B$ be $G$-valued random variables on $\Omega$, and set $Z := A+B$. Then \begin{equation} \sum_{z} \bbP[Z=z] d[(A | Z = z); (B | Z = z)] \leq 3 \bbI[A:B] + 2 \bbH[Z] - \bbH[A] - \bbH[B]. \end{equation}
- id `r918`: lemma. For $X,Y$ random variables, there exist random variables $X_1,X_2,Y'$ on a common probability space with $(X_1, Y'), (X_2, Y')$ both having the distribution of $(X,Y)$, and $X_1, X_2$ conditionally independent over $Y'$ in the sense of [another result].
- id `r823`: lemma. Suppose that $X, Y, Z$ are independent $G$-valued random variables. Then \[ \bbH[X + Y + Z] - \bbH[X + Y] \leq \bbH[Y+ Z] - \bbH[Y]. \]
- id `r951`: lemma. The expression $d[X | Z;Y | W]$ is unchanged if $(X,Z)$ or $(Y,W)$ is replaced by a copy. Furthermore, if $(X,Z)$ and $(Y,W)$ are independent, then $$ d[X | Z;Y | W] = \bbH[X-Y|Z,W] - \bbH[X|Z]/2 - \bbH[Y|W]/2$$ and similarly $$ d[X ;Y | W] = \bbH[X-Y|W] - \bbH[X]/2 - \bbH[Y|W]/2.$$
- id `r616`: lemma. If $X,Y,Z$ are $G$-valued random variables, then $$ d[X ;Y] \leq d[X ;Z] + d[Z;Y].$$
- id `r675`: lemma. If $X$ is a $G$-valued random variable and $0$ is the random variable taking the value $0$ everywhere then \[d[X;0]=\mathbb{H}(X)/2.\]
- id `r630`: lemma. If $G$ is an additive group and $X$ is a $G$-valued random variable and $H\leq G$ is a finite subgroup then, with $\pi:G\to G/H$ the natural homomorphism we have (where $U_H$ is uniform on $H$) \[\mathbb{H}(\pi(X))\leq 2d[X;U_H].\]
- id `r619`: definition. Let $X,Y$ be $G$-valued random variables (not necessarily on the same sample space). The \emph{Ruzsa distance} $d[X ;Y]$ between $X$ and $Y$ is defined to be $$ d[X ;Y] := \bbH[X' - Y'] - \bbH[X']/2 - \bbH[Y']/2$$ where $X',Y'$ are (the canonical) independent copies of $X,Y$ from `r270`.
- id `r767`: lemma. If $X,Y,Z$ are $G$-valued random variables on $\Omega$ with $(X,Y)$ independent of $Z$, then \begin{equation} \bbH[X - Y] \leq \bbH[X-Z] + \bbH[Z-Y] - \bbH[Z]\end{equation}
- id `r730`: lemma. Suppose that $(X, Z)$ and $(Y, W)$ are random variables, where $X, Y$ take values in an abelian group. Then \[ d[X | Z;Y | W] \leq d[X ; Y] + \tfrac{1}{2} \bbI[X : Z] + \tfrac{1}{2} \bbI[Y : W].\] In particular, \[ d[X ;Y | W] \leq d[X ; Y] + \tfrac{1}{2} \bbI[Y : W].\]
- id `r702`: lemma. If $X,Y$ are $G$-valued random variables, then $$|\bbH[X]-H[Y]| \leq 2 d[X ;Y].$$
- id `r516`: lemma. If $X'$ is a copy of $X$ then $\bbH[X'] = \bbH[X]$.
- id `r419`: lemma. If $X,Y$ are $G$-valued random variables, then $$ d[X ;Y] \geq 0.$$
- id `r848`: lemma. Let $X, Y, Z, Z'$ be random variables taking values in some abelian group, and with $Y, Z, Z'$ independent. Then we have \begin{align}\nonumber & d[X ;Y + Z | Y + Z + Z'] - d[X ;Y] \\ & \qquad \leq \tfrac{1}{2} ( \bbH[Y + Z + Z'] + \bbH[Y + Z] - \bbH[Y] - \bbH[Z']). \end{align}
- id `r312`: lemma. If $X,Y$ are $G$-valued random variables, then $$ d[X ;Y] = d[Y;X].$$

## Constraints

- `r270` before `r374`
- `r270` before `r616`
- `r270` before `r630`
- `r270` before `r702`
- `r270` before `r730`
- `r374` before `r848`
- `r416` before `r374`
- `r416` before `r410`
- `r416` before `r616`
- `r416` before `r630`
- `r416` before `r702`
- `r416` before `r730`
- `r416` before `r997`
- `r432` before `r731`
- `r516` before `r374`
- `r516` before `r410`
- `r516` before `r630`
- `r516` before `r702`
- `r516` before `r730`
- `r516` before `r891`
- `r591` before `r374`
- `r591` before `r730`
- `r591` before `r848`
- `r591` before `r951`
- `r619` before `r312`
- `r619` before `r416`
- `r702` before `r419`
- `r702` before `r630`
- `r730` before `r374`
- `r731` before `r702`
- `r731` before `r997`
- `r767` before `r616`
- `r816` before `r432`
- `r816` before `r630`
- `r823` before `r374`
- `r891` before `r374`
- `r891` before `r616`
- `r891` before `r630`
- `r891` before `r702`
- `r891` before `r730`
- `r918` before `r410`
- `r934` before `r312`
- `r934` before `r374`
- `r934` before `r767`
- `r951` before `r730`
