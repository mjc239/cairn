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

- id `r532`: lemma; steps here: state and prove. We have for all $x\in G\setminus G'$ \begin{equation} \sum_{\fp\in \fP}T_{\fp} f(x)= \sum_{s=\sigma_1(x)}^{\sigma_2(x)} \int K_{s}(x,y) f(y) e(\tQ(x)(y)-\tQ(x)(x))\, d\mu(y). \end{equation}
- id `r843`: lemma; steps here: state and prove. Let $K = 2^{4a+1}$. For each $-S+K\le k\le S$ and $y\in Y_k$ we have \begin{equation} \sum_{z\in Y_{k-K}: (z,k-K|y,k)}\mu(I_3(z,k-K)) \le \frac 12 \mu(I_3(y,k))\,. \end{equation}
- id `r129`: lemma; steps here: state and prove. Let $-S\le l\le k\le S$ and $y\in Y_k$ and $y'\in Y_l$ with $I_3(y',l)\cap I_3(y,k)\neq \emptyset$. Then \begin{equation} I_3(y',l)\subset I_3(y,k). \end{equation}
- id `r640`: lemma; steps here: state and prove. For each $-S\le k\le S$ and $y\in Y_k$ and $0<t<1$ with $tD^k\ge D^{-S}$ we have \begin{equation} \mu(\{x \in I_3(y,k) \ : \ \rho(x, X \setminus I_3(y,k)) \leq t D^{k}\}) \le 2 t^\kappa \mu(I_3(y,k))\,. \end{equation}
- id `r327`: lemma; steps here: state and prove. For each $I \in \mathcal{D}$, we have \begin{equation} \tQ(X) \subset \bigcup_{z \in \mathcal{Z}(I)} B_{I^\circ}(z, 0.7)\,. \end{equation}
- id `r882`: lemma; steps here: state and prove. For each $-S\le k\le S$ and $1\le j\le 3$ the following holds. If $j\neq 2$ and for some $x\in X$ and $y_1,y_2\in Y_k$ we have \begin{equation} x\in I_j(y_1,k)\cap I_j(y_2,k), \end{equation} then $y_1=y_2$. If $j\neq 1$, then \begin{equation} B(o, 4D^S-2D^k)\subset \bigcup_{y\in Y_k} I_j(y,k)\, . \end{equation} We have for each $y\in Y_k$, \begin{equation} B(y,\frac 12 D^k) \subset I_3(y,k)\subset B(y,4D^k). \end{equation}
- id `r548`: lemma; steps here: state and prove. For each $I \in \mathcal{D}$, it holds that \begin{equation} \bigcup_{z \in \mathcal{Z}(I)} B_{I^\circ}(z, 0.7)\subset \bigcup_{\fp \in \fP(I)} \Omega_1(\fp)\,. \end{equation} For every $\fp \in \fP$, it holds that \begin{equation} B_{\fp}(\fcc(\fp), 0.3) \subset \Omega_1(\fp) \subset B_{\fp}(\fcc(\fp), 0.7)\,. \end{equation}
- id `r607`: lemma; steps here: state and prove. For each $-S\le k\le S$, the ball $B(o, 4D^S-D^k)$ is contained in the union of the balls $B(y,2D^k)$ with $y\in Y_k$.
- id `r666`: lemma; steps here: state and prove. For a given grid structure $(\mathcal{D}, c,s)$, there exists a tile structure $(\fP,\scI,\fc,\fcc,\pc,\ps)$.
- id `r338`: lemma; steps here: state and prove. Assume $-S\le k''< k'< k\le S$ and $y''\in Y_{k''}$, $y'\in Y_{k'}$, $y\in Y_k$. Assume there is $x\in X$ such that \begin{equation} x\in I_3(y'',k'')\cap I_3(y',k')\cap I_3(y,k)\, . \end{equation} If $(y'',k''|y,k)$, the also $(y'',k''|y',k')$ and $(y',k'|y,k)$
- id `r453`: proposition; steps here: prove only (it was stated in an earlier section). Let ${\sigma_1},\sigma_2\colon X\to \mathbb{Z}$ be measurable functions with finite range and ${\sigma_1}\leq \sigma_2$. Let $F,G$ be bounded Borel sets in $X$. Then there is a Borel set $G'$ in $X$ with $2\mu(G')\leq \mu(G)$ such that for all Borel functions $f:X\to \C$ with $|f|\le \mathbf{1}_F$. \begin{equation*} \int_{G \setminus G'} \left|\sum_{s={\sigma_1}(x)}^{{\sigma_2}(x)} \int K_s(x,y) f(y) e(\tQ(x)(y)) \, \mathrm{d}\mu(y) \right| \mathrm{d}\mu(x) \end{equation*} \begin{equation} \le \frac{2^{442a^3}}{(q-1)^5} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac 1 q}\,. \end{equation}
- id `r336`: lemma; steps here: state and prove. For each $I \in \mathcal{D}$, and $\fp_1, \fp_2\in \fP(I)$, if $$\Omega_1(\fp_1)\cap \Omega_1(\fp_2)\neq \emptyset,$$ then $\fp_1=\fp_2$.
- id `r793`: lemma; steps here: state and prove. Let $-S\le k\le S$. Consider $Y\subset X$ such that for any $y\in Y$, we have \begin{equation} y\in B(o,4D^S-D^k), \end{equation} furthermore, for any $y'\in Y$ with $y\neq y'$, we have \begin{equation} B(y,D^k)\cap B(y',D^k)=\emptyset. \end{equation} Then the cardinality of $Y$ is bounded by \begin{equation} |Y|\le 2^{3a + 200Sa^3}\, . \end{equation}
- id `r324`: lemma; steps here: state and prove. Let $-S\le l\le k\le S$ and $y\in Y_k$. We have \begin{equation} I_3(y,k)\subset \bigcup_{y'\in Y_l} I_3(y',l)\, . \end{equation}
- id `r879`: lemma; steps here: state and prove. Let $K = 2^{4a+1}$ and let $n\ge 0$ be an integer. Then for each $-S+nK\le k\le S$ we have \begin{equation} \sum_{y'\in Y_{k-nK}: (y',k-nK|y,k)}\mu(I_3(y',k-nK)) \le 2^{-n} \mu(I_3(y,k))\,. \end{equation}
- id `r570`: lemma; steps here: state and prove. There exists a grid structure $(\mathcal{D}, c,s)$.

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r129` before `P:r338`
- `S:r129` before `P:r570`
- `S:r129` before `P:r640`
- `S:r129` before `P:r843`
- `S:r324` before `P:r129`
- `S:r324` before `P:r570`
- `S:r324` before `P:r640`
- `S:r324` before `P:r843`
- `S:r324` before `P:r879`
- `S:r327` before `P:r666`
- `S:r336` before `P:r666`
- `S:r338` before `P:r843`
- `S:r338` before `P:r879`
- `S:r532` before `P:r453`
- `S:r548` before `P:r666`
- `S:r570` before `P:r453`
- `S:r607` before `P:r882`
- `S:r640` before `P:r570`
- `S:r666` before `P:r453`
- `S:r793` before `P:r570`
- `S:r843` before `P:r879`
- `S:r879` before `P:r640`
- `S:r882` before `P:r129`
- `S:r882` before `P:r327`
- `S:r882` before `P:r338`
- `S:r882` before `P:r570`
- `S:r882` before `P:r640`
- `S:r882` before `P:r666`
- `S:r882` before `P:r843`
- `S:r882` before `P:r879`
