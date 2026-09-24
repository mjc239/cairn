You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `r462`: lemma. Let $-S\le k\le S$. Consider $Y\subset X$ such that for any $y\in Y$, we have \begin{equation} y\in B(o,4D^S-D^k), \end{equation} furthermore, for any $y'\in Y$ with $y\neq y'$, we have \begin{equation} B(y,D^k)\cap B(y',D^k)=\emptyset. \end{equation} Then the cardinality of $Y$ is bounded by \begin{equation} |Y|\le 2^{3a + 200Sa^3}\, . \end{equation}
- id `r544`: lemma. Let $-S\le l\le k\le S$ and $y\in Y_k$ and $y'\in Y_l$ with $I_3(y',l)\cap I_3(y,k)\neq \emptyset$. Then \begin{equation} I_3(y',l)\subset I_3(y,k). \end{equation}
- id `r423`: lemma. For each $I \in \mathcal{D}$, it holds that \begin{equation} \bigcup_{z \in \mathcal{Z}(I)} B_{I^\circ}(z, 0.7)\subset \bigcup_{\fp \in \fP(I)} \Omega_1(\fp)\,. \end{equation} For every $\fp \in \fP$, it holds that \begin{equation} B_{\fp}(\fcc(\fp), 0.3) \subset \Omega_1(\fp) \subset B_{\fp}(\fcc(\fp), 0.7)\,. \end{equation}
- id `r725`: lemma. Let $K = 2^{4a+1}$ and let $n\ge 0$ be an integer. Then for each $-S+nK\le k\le S$ we have \begin{equation} \sum_{y'\in Y_{k-nK}: (y',k-nK|y,k)}\mu(I_3(y',k-nK)) \le 2^{-n} \mu(I_3(y,k))\,. \end{equation}
- id `r755`: lemma. Let $-S\le l\le k\le S$ and $y\in Y_k$. We have \begin{equation} I_3(y,k)\subset \bigcup_{y'\in Y_l} I_3(y',l)\, . \end{equation}
- id `r309`: lemma. For each $-S\le k\le S$ and $1\le j\le 3$ the following holds. If $j\neq 2$ and for some $x\in X$ and $y_1,y_2\in Y_k$ we have \begin{equation} x\in I_j(y_1,k)\cap I_j(y_2,k), \end{equation} then $y_1=y_2$. If $j\neq 1$, then \begin{equation} B(o, 4D^S-2D^k)\subset \bigcup_{y\in Y_k} I_j(y,k)\, . \end{equation} We have for each $y\in Y_k$, \begin{equation} B(y,\frac 12 D^k) \subset I_3(y,k)\subset B(y,4D^k). \end{equation}
- id `r665`: lemma. There exists a grid structure $(\mathcal{D}, c,s)$.
- id `r588`: lemma. For each $-S\le k\le S$ and $y\in Y_k$ and $0<t<1$ with $tD^k\ge D^{-S}$ we have \begin{equation} \mu(\{x \in I_3(y,k) \ : \ \rho(x, X \setminus I_3(y,k)) \leq t D^{k}\}) \le 2 t^\kappa \mu(I_3(y,k))\,. \end{equation}
- id `r553`: lemma. We have for all $x\in G\setminus G'$ \begin{equation} \sum_{\fp\in \fP}T_{\fp} f(x)= \sum_{s=\sigma_1(x)}^{\sigma_2(x)} \int K_{s}(x,y) f(y) e(\tQ(x)(y)-\tQ(x)(x))\, d\mu(y). \end{equation}
- id `r986`: lemma. For each $I \in \mathcal{D}$, and $\fp_1, \fp_2\in \fP(I)$, if $$\Omega_1(\fp_1)\cap \Omega_1(\fp_2)\neq \emptyset,$$ then $\fp_1=\fp_2$.
- id `r633`: lemma. Assume $-S\le k''< k'< k\le S$ and $y''\in Y_{k''}$, $y'\in Y_{k'}$, $y\in Y_k$. Assume there is $x\in X$ such that \begin{equation} x\in I_3(y'',k'')\cap I_3(y',k')\cap I_3(y,k)\, . \end{equation} If $(y'',k''|y,k)$, the also $(y'',k''|y',k')$ and $(y',k'|y,k)$
- id `r366`: lemma. For each $-S\le k\le S$, the ball $B(o, 4D^S-D^k)$ is contained in the union of the balls $B(y,2D^k)$ with $y\in Y_k$.
- id `r163`: lemma. For each $I \in \mathcal{D}$, we have \begin{equation} \tQ(X) \subset \bigcup_{z \in \mathcal{Z}(I)} B_{I^\circ}(z, 0.7)\,. \end{equation}
- id `r924`: lemma. Let $K = 2^{4a+1}$. For each $-S+K\le k\le S$ and $y\in Y_k$ we have \begin{equation} \sum_{z\in Y_{k-K}: (z,k-K|y,k)}\mu(I_3(z,k-K)) \le \frac 12 \mu(I_3(y,k))\,. \end{equation}
- id `r661`: lemma. For a given grid structure $(\mathcal{D}, c,s)$, there exists a tile structure $(\fP,\scI,\fc,\fcc,\pc,\ps)$.

## Constraints

- `r163` before `r661`
- `r309` before `r163`
- `r309` before `r544`
- `r309` before `r588`
- `r309` before `r633`
- `r309` before `r661`
- `r309` before `r665`
- `r309` before `r725`
- `r309` before `r924`
- `r366` before `r309`
- `r423` before `r661`
- `r462` before `r665`
- `r544` before `r588`
- `r544` before `r633`
- `r544` before `r665`
- `r544` before `r924`
- `r588` before `r665`
- `r633` before `r725`
- `r633` before `r924`
- `r725` before `r588`
- `r755` before `r544`
- `r755` before `r588`
- `r755` before `r665`
- `r755` before `r725`
- `r755` before `r924`
- `r924` before `r725`
- `r986` before `r661`
