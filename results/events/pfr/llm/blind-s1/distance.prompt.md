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

- id `r475`: lemma; steps here: state and prove. If $X,Y$ are $G$-valued random variables, then $$|\bbH[X]-H[Y]| \leq 2 d[X ;Y].$$
- id `r661`: lemma; steps here: state and prove. The expression $d[X | Z;Y | W]$ is unchanged if $(X,Z)$ or $(Y,W)$ is replaced by a copy. Furthermore, if $(X,Z)$ and $(Y,W)$ are independent, then $$ d[X | Z;Y | W] = \bbH[X-Y|Z,W] - \bbH[X|Z]/2 - \bbH[Y|W]/2$$ and similarly $$ d[X ;Y | W] = \bbH[X-Y|W] - \bbH[X]/2 - \bbH[Y|W]/2.$$
- id `r819`: lemma; steps here: state and prove. If $X,Y$ are $G$-valued random variables on $\Omega$, we have $$ \max(\bbH[X], \bbH[Y]) - \bbI[X:Y] \leq \bbH[X \pm Y].$$
- id `r894`: lemma; steps here: state and prove. If $X,Y,Z$ are $G$-valued random variables, then $$ d[X ;Y] \leq d[X ;Z] + d[Z;Y].$$
- id `r790`: lemma; steps here: state and prove. Let $A,B$ be $G$-valued random variables on $\Omega$, and set $Z := A+B$. Then \begin{equation} \sum_{z} \bbP[Z=z] d[(A | Z = z); (B | Z = z)] \leq 3 \bbI[A:B] + 2 \bbH[Z] - \bbH[A] - \bbH[B]. \end{equation}
- id `r855`: lemma; steps here: state and prove. Suppose that $(X, Z)$ and $(Y, W)$ are random variables, where $X, Y$ take values in an abelian group. Then \[ d[X | Z;Y | W] \leq d[X ; Y] + \tfrac{1}{2} \bbI[X : Z] + \tfrac{1}{2} \bbI[Y : W].\] In particular, \[ d[X ;Y | W] \leq d[X ; Y] + \tfrac{1}{2} \bbI[Y : W].\]
- id `r483`: lemma; steps here: state and prove. If $X,Y$ are $G$-valued, then $\bbH[X \pm Y | Y]=\bbH[X|Y]$ and $\bbH[X \pm Y, Y] = \bbH[X, Y]$.
- id `r188`: lemma; steps here: state and prove. If $X,Y$ are $G$-valued random variables, then $$ d[X ;Y] = d[Y;X].$$
- id `r549`: lemma; steps here: state and prove. If $X$ is $G$-valued, then $\bbH[-X]=\bbH[X]$.
- id `r779`: lemma; steps here: state and prove. If $G$ is an additive group and $X$ is a $G$-valued random variable and $H\leq G$ is a finite subgroup then, with $\pi:G\to G/H$ the natural homomorphism we have (where $U_H$ is uniform on $H$) \[\mathbb{H}(\pi(X))\leq 2d[X;U_H].\]
- id `r620`: lemma; steps here: state and prove. If $X$ is a $G$-valued random variable and $0$ is the random variable taking the value $0$ everywhere then \[d[X;0]=\mathbb{H}(X)/2.\]
- id `r210`: definition; steps here: state only (no proof needed). Let $X,Y$ be $G$-valued random variables (not necessarily on the same sample space). The \emph{Ruzsa distance} $d[X ;Y]$ between $X$ and $Y$ is defined to be $$ d[X ;Y] := \bbH[X' - Y'] - \bbH[X']/2 - \bbH[Y']/2$$ where $X',Y'$ are (the canonical) independent copies of $X,Y$ from `r960`.
- id `r897`: lemma; steps here: state and prove. For $X,Y$ random variables, there exist random variables $X_1,X_2,Y'$ on a common probability space with $(X_1, Y'), (X_2, Y')$ both having the distribution of $(X,Y)$, and $X_1, X_2$ conditionally independent over $Y'$ in the sense of [another result].
- id `r267`: lemma; steps here: state and prove. If $X,Y$ are $G$-valued random variables, then $$ d[X ;Y] \geq 0.$$
- id `r633`: corollary; steps here: state and prove. If $X,Y$ are independent $G$-valued random variables, then $$\max(\bbH[X], \bbH[Y]) \leq \bbH[X\pm Y]. $$
- id `r960`: lemma; steps here: state and prove. Let $X_i : \Omega_i \to S_i$ be random variables for $i=1,\dots,k$. Then if one gives $\prod_{i=1}^k S_i$ the product measure of the laws of $X_i$, the coordinate functions $(x_j)_{j=1}^k \mapsto x_i$ are jointly independent random variables which are copies of the $X_1,\dots,X_k$.
- id `r502`: definition; steps here: state only (no proof needed). If $(X, Z)$ and $(Y, W)$ are random variables (where $X$ and $Y$ are $G$-valued) we define $$ d[X | Z; Y | W] := \sum_{z,w} \bbP[Z=z] \bbP[W=w] d[(X|Z=z); (Y|(W=w))].$$ similarly $$ d[X ; Y | W] := \sum_{w} \bbP[W=w] d[X ; (Y|(W=w))].$$
- id `r479`: lemma; steps here: state and prove. If $X,Y$ are independent $G$-valued random variables, then $$ \bbH[X-Y] - \bbH[X], \bbH[X-Y] - \bbH[Y] \leq 2d[X ;Y].$$
- id `r601`: lemma; steps here: state and prove. If $X,Y,Z$ are $G$-valued random variables on $\Omega$ with $(X,Y)$ independent of $Z$, then \begin{equation} \bbH[X - Y] \leq \bbH[X-Z] + \bbH[Z-Y] - \bbH[Z]\end{equation}
- id `r850`: lemma; steps here: state and prove. If $X,Y$ are independent $G$-random variables then $$ d[X ;Y] := \bbH[X - Y] - \bbH[X]/2 - \bbH[Y]/2.$$
- id `r130`: lemma; steps here: state and prove. Let $X, Y, Z$ be random variables taking values in some abelian group of characteristic $2$, and with $Y, Z$ independent. Then we have \begin{align}\nonumber d[X ; Y + Z] -d[X ; Y] & \leq \tfrac{1}{2} (\bbH[Y+ Z] - \bbH[Y]) \\ & = \tfrac{1}{2} d[Y; Z] + \tfrac{1}{4} \bbH[Z] - \tfrac{1}{4} \bbH[Y]. \end{align} and \begin{align}\nonumber d[X ;Y|Y+ Z] - d[X ;Y] & \leq \tfrac{1}{2} \bigl(\bbH[Y+ Z] - \bbH[Z]\bigr) \\ & = \tfrac{1}{2} d[Y;Z] + \tfrac{1}{4} \bbH[Y] - \tfrac{1}{4} \bbH[Z]. \end{align}
- id `r580`: lemma; steps here: state and prove. If $X',Y'$ are copies of $X,Y$ respectively then $d[X';Y']=d[X ;Y]$.
- id `r144`: lemma; steps here: state and prove. Let $X, Y, Z, Z'$ be random variables taking values in some abelian group, and with $Y, Z, Z'$ independent. Then we have \begin{align}\nonumber & d[X ;Y + Z | Y + Z + Z'] - d[X ;Y] \\ & \qquad \leq \tfrac{1}{2} ( \bbH[Y + Z + Z'] + \bbH[Y + Z] - \bbH[Y] - \bbH[Z']). \end{align}
- id `r415`: lemma; steps here: state and prove. If $X'$ is a copy of $X$ then $\bbH[X'] = \bbH[X]$.
- id `r820`: corollary; steps here: state and prove. If $X,Y$ are $G$-valued random variables on $\Omega$ and $Z$ is another random variable on $\Omega$ then \[ \max(\bbH[X|Z], \bbH[Y|Z]) - \bbI[X:Y|Z] \leq \bbH[X\pm Y|Z], \]
- id `r968`: lemma; steps here: state and prove. Suppose that $X, Y, Z$ are independent $G$-valued random variables. Then \[ \bbH[X + Y + Z] - \bbH[X + Y] \leq \bbH[Y+ Z] - \bbH[Y]. \]

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r130` before `P:r144`
- `S:r210` before `P:r188`
- `S:r210` before `P:r850`
- `S:r415` before `P:r130`
- `S:r415` before `P:r475`
- `S:r415` before `P:r580`
- `S:r415` before `P:r779`
- `S:r415` before `P:r790`
- `S:r415` before `P:r855`
- `S:r475` before `P:r267`
- `S:r475` before `P:r779`
- `S:r483` before `P:r779`
- `S:r483` before `P:r819`
- `S:r502` before `P:r130`
- `S:r502` before `P:r144`
- `S:r502` before `S:r661`
- `S:r502` before `S:r855`
- `S:r549` before `P:r130`
- `S:r549` before `P:r188`
- `S:r549` before `P:r601`
- `S:r580` before `P:r130`
- `S:r580` before `P:r475`
- `S:r580` before `P:r779`
- `S:r580` before `P:r855`
- `S:r580` before `P:r894`
- `S:r601` before `P:r894`
- `S:r633` before `P:r475`
- `S:r633` before `P:r479`
- `S:r661` before `P:r855`
- `S:r819` before `P:r633`
- `S:r850` before `P:r130`
- `S:r850` before `P:r475`
- `S:r850` before `P:r479`
- `S:r850` before `P:r779`
- `S:r850` before `P:r790`
- `S:r850` before `P:r855`
- `S:r850` before `P:r894`
- `S:r855` before `P:r130`
- `S:r897` before `P:r790`
- `S:r960` before `P:r130`
- `S:r960` before `P:r475`
- `S:r960` before `P:r779`
- `S:r960` before `P:r855`
- `S:r960` before `P:r894`
- `S:r968` before `P:r130`
