You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `tile-structure`: lemma (tile structure). For a given grid structure $(\mathcal{D}, c,s)$, there exists a tile structure $(\fP,\scI,\fc,\fcc,\pc,\ps)$.
- id `disjoint-frequency-cubes`: lemma (disjoint frequency cubes). For each $I \in \mathcal{D}$, and $\fp_1, \fp_2\in \fP(I)$, if $$\Omega_1(\fp_1)\cap \Omega_1(\fp_2)\neq \emptyset,$$ then $\fp_1=\fp_2$.
- id `boundary-measure`: lemma (boundary measure). For each $-S\le k\le S$ and $y\in Y_k$ and $0<t<1$ with $tD^k\ge D^{-S}$ we have \begin{equation} \mu(\{x \in I_3(y,k) \ : \ \rho(x, X \setminus I_3(y,k)) \leq t D^{k}\}) \le 2 t^\kappa \mu(I_3(y,k))\,. \end{equation}
- id `frequency-cube-cover`: lemma (frequency cube cover). For each $I \in \mathcal{D}$, it holds that \begin{equation} \bigcup_{z \in \mathcal{Z}(I)} B_{I^\circ}(z, 0.7)\subset \bigcup_{\fp \in \fP(I)} \Omega_1(\fp)\,. \end{equation} For every $\fp \in \fP$, it holds that \begin{equation} B_{\fp}(\fcc(\fp), 0.3) \subset \Omega_1(\fp) \subset B_{\fp}(\fcc(\fp), 0.7)\,. \end{equation}
- id `smaller-boundary`: lemma (smaller boundary). Let $K = 2^{4a+1}$ and let $n\ge 0$ be an integer. Then for each $-S+nK\le k\le S$ we have \begin{equation} \sum_{y'\in Y_{k-nK}: (y',k-nK|y,k)}\mu(I_3(y',k-nK)) \le 2^{-n} \mu(I_3(y,k))\,. \end{equation}
- id `grid-existence`: lemma (grid existence). There exists a grid structure $(\mathcal{D}, c,s)$.
- id `cover-by-cubes`: lemma (cover by cubes). Let $-S\le l\le k\le S$ and $y\in Y_k$. We have \begin{equation} I_3(y,k)\subset \bigcup_{y'\in Y_l} I_3(y',l)\, . \end{equation}
- id `frequency-ball-cover`: lemma (frequency ball cover). For each $I \in \mathcal{D}$, we have \begin{equation} \tQ(X) \subset \bigcup_{z \in \mathcal{Z}(I)} B_{I^\circ}(z, 0.7)\,. \end{equation}
- id `cover-big-ball`: lemma (cover big ball). For each $-S\le k\le S$, the ball $B(o, 4D^S-D^k)$ is contained in the union of the balls $B(y,2D^k)$ with $y\in Y_k$.
- id `tile-sum-operator`: lemma (tile sum operator). We have for all $x\in G\setminus G'$ \begin{equation} \sum_{\fp\in \fP}T_{\fp} f(x)= \sum_{s=\sigma_1(x)}^{\sigma_2(x)} \int K_{s}(x,y) f(y) e(\tQ(x)(y)-\tQ(x)(x))\, d\mu(y). \end{equation}
- id `transitive-boundary`: lemma (transitive boundary). Assume $-S\le k''< k'< k\le S$ and $y''\in Y_{k''}$, $y'\in Y_{k'}$, $y\in Y_k$. Assume there is $x\in X$ such that \begin{equation} x\in I_3(y'',k'')\cap I_3(y',k')\cap I_3(y,k)\, . \end{equation} If $(y'',k''|y,k)$, the also $(y'',k''|y',k')$ and $(y',k'|y,k)$
- id `counting-balls`: lemma (counting balls). Let $-S\le k\le S$. Consider $Y\subset X$ such that for any $y\in Y$, we have \begin{equation} y\in B(o,4D^S-D^k), \end{equation} furthermore, for any $y'\in Y$ with $y\neq y'$, we have \begin{equation} B(y,D^k)\cap B(y',D^k)=\emptyset. \end{equation} Then the cardinality of $Y$ is bounded by \begin{equation} |Y|\le 2^{3a + 200Sa^3}\, . \end{equation}
- id `small-boundary`: lemma (small boundary). Let $K = 2^{4a+1}$. For each $-S+K\le k\le S$ and $y\in Y_k$ we have \begin{equation} \sum_{z\in Y_{k-K}: (z,k-K|y,k)}\mu(I_3(z,k-K)) \le \frac 12 \mu(I_3(y,k))\,. \end{equation}
- id `basic-grid-structure`: lemma (basic grid structure). For each $-S\le k\le S$ and $1\le j\le 3$ the following holds. If $j\neq 2$ and for some $x\in X$ and $y_1,y_2\in Y_k$ we have \begin{equation} x\in I_j(y_1,k)\cap I_j(y_2,k), \end{equation} then $y_1=y_2$. If $j\neq 1$, then \begin{equation} B(o, 4D^S-2D^k)\subset \bigcup_{y\in Y_k} I_j(y,k)\, . \end{equation} We have for each $y\in Y_k$, \begin{equation} B(y,\frac 12 D^k) \subset I_3(y,k)\subset B(y,4D^k). \end{equation}
- id `dyadic-property`: lemma (dyadic property). Let $-S\le l\le k\le S$ and $y\in Y_k$ and $y'\in Y_l$ with $I_3(y',l)\cap I_3(y,k)\neq \emptyset$. Then \begin{equation} I_3(y',l)\subset I_3(y,k). \end{equation}

## Constraints

- `basic-grid-structure` before `boundary-measure`
- `basic-grid-structure` before `dyadic-property`
- `basic-grid-structure` before `frequency-ball-cover`
- `basic-grid-structure` before `grid-existence`
- `basic-grid-structure` before `small-boundary`
- `basic-grid-structure` before `smaller-boundary`
- `basic-grid-structure` before `tile-structure`
- `basic-grid-structure` before `transitive-boundary`
- `boundary-measure` before `grid-existence`
- `counting-balls` before `grid-existence`
- `cover-big-ball` before `basic-grid-structure`
- `cover-by-cubes` before `boundary-measure`
- `cover-by-cubes` before `dyadic-property`
- `cover-by-cubes` before `grid-existence`
- `cover-by-cubes` before `small-boundary`
- `cover-by-cubes` before `smaller-boundary`
- `disjoint-frequency-cubes` before `tile-structure`
- `dyadic-property` before `boundary-measure`
- `dyadic-property` before `grid-existence`
- `dyadic-property` before `small-boundary`
- `dyadic-property` before `transitive-boundary`
- `frequency-ball-cover` before `tile-structure`
- `frequency-cube-cover` before `tile-structure`
- `small-boundary` before `smaller-boundary`
- `smaller-boundary` before `boundary-measure`
- `transitive-boundary` before `small-boundary`
- `transitive-boundary` before `smaller-boundary`
