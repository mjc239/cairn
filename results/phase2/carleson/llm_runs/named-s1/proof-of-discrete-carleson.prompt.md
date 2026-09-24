You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `C5-convex`: lemma (C5 convex). For each $k,n,j$, the collection $\fC_5(k,n,j)$ is convex.
- id `third-exception`: lemma (third exception). We have \begin{equation} \mu(G_3)\le 2^{-4} \mu(G)\, . \end{equation}
- id `forest-separation`: lemma (forest separation). For each $\fu,\fu'\in \fU_3(k,n,j)$ with $\fu\neq \fu'$ and each $\fp \in \fT_2(\fu)$ with $\scI(\fp)\subset \scI(\fu')$ we have \begin{equation} d_{\fp}(\fcc(\fp), \fcc(\fu')) > 2^{Z(n+1)}\,. \end{equation}
- id `first-exception`: lemma (first exception). We have \begin{equation} \mu(G_1)\le 2^{-5}\mu(G)\, . \end{equation}
- id `C2-convex`: lemma (C2 convex). For each $k,n,j$, the collection $\fC_2(k,n,j)$ is convex.
- id `pairwise-disjoint`: lemma (pairwise disjoint). If $\fp, \fp' \in {\mathfrak{M}}(k,n)$ and \begin{equation} {E_1}(\fp)\cap {E_1}(\fp')\neq \emptyset, \end{equation} then $\fp=\fp'$.
- id `forest-geometry`: lemma (forest geometry). For each $\fu\in \fU_3(k,n,j)$, the set $\mathfrak{T}_2(\fu)$ satisfies \eqref{forest1}.
- id `dense-cover`: lemma (dense cover). For each $k\ge 0$, the union of all dyadic cubes in $\mathcal{C}(G,k)$ has measure at most $2^{k+1} \mu(G)$ .
- id `forest-complement`: lemma (forest complement). Let \begin{equation} \fP_2 =\fP\setminus \fP_1\,. \end{equation} For all $f:X\to \C$ with $|f|\le \mathbf{1}_F$ we have \begin{equation} \int_{G \setminus G'} \left|\sum_{\fp \in \fP_2} T_{\fp} f\right| \, \mathrm{d}\mu \le \frac{2^{120a^3}}{(q-1)^5} \mu(G)^{1 - \frac{1}{q}} \mu(F)^{\frac{1}{q}}\,. \end{equation}
- id `antichain-decomposition`: lemma (antichain decomposition). We have that \begin{align} &\quad \fP_2 \cap \fP_{G \setminus G'}\\ &= \bigcup_{k \ge 0} \bigcup_{n \ge k} \fL_0(k,n) \cap \fP_{G \setminus G'} \\ &\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} \fL_2(k,n,j) \cap \fP_{G \setminus G'}\\ &\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} \bigcup_{0 \le l \le Z(n+1)} \fL_1(k,n,j,l) \cap \fP_{G \setminus G'}\\ &\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} \bigcup_{0 \le l \le Z(n+1)} \fL_3(k,n,j,l)\cap \fP_{G \setminus G'}\,. \end{align}
- id `tree-count`: lemma (tree count). Let $k,n,j\ge 0$. We have for every $x\in X$ \begin{equation} \sum_{\fu\in \fU_1(k,n,j)} \mathbf{1}_{\scI(\fu)}(x) \le 2^{-j} 2^{9a} \sum_{\mathfrak{m}\in \mathfrak{M}(k,n)} \mathbf{1}_{\scI(\mathfrak{m})}(x) \end{equation}
- id `second-exception`: lemma (second exception). We have \begin{equation} \mu(G_2)\le 2^{-2} \mu(G)\, . \end{equation}
- id `forest-convex`: lemma (forest convex). For each $\fu\in \fU_3(k,n,j)$, the set $\mathfrak{T}_2(\fu)$ satisfies the convexity condition \eqref{forest2}.
- id `equivalence-relation`: lemma (equivalence relation). For each $k,n,j$, the relation $\sim$ on $\fU_2(k,n,j)$ is an equivalence relation.
- id `relation-geometry`: lemma (relation geometry). If $\fu \sim \fu'$, then $\scI(u) = \scI(u')$ and \begin{equation*} B_{\fu}(\fcc(\fu), 100) \cap B_{\fu'}(\fcc(\fu'), 100) \neq \emptyset\ . \end{equation*}
- id `top-tiles`: lemma (top tiles). We have \begin{equation} \sum_{\mathfrak{m} \in \mathfrak{M}(k,n)} \mu(\scI(\mathfrak{m}))\le 2^{n+k+3}\mu(G). \end{equation}
- id `C6-forest`: lemma (C6 forest). We have \begin{equation} \fC_6(k,n,j)=\bigcup_{\fu\in \fU_3(k,n,j)}\mathfrak{T}_2(\fu)\, . \end{equation}
- id `C1-convex`: lemma (C1 convex). For each $k,n,j$, the collection $\fC_1(k,n,j)$ is convex.
- id `L1-L3-antichain`: lemma (L1 L3 antichain). Each of the sets $\fL_1(k,n,j,l)$ and $\fL_3(k,n,j,l)$ is an antichain.
- id `boundary-exception`: lemma (boundary exception). Let $\mathcal{L}(\fu)$ be as defined in \eqref{eq-L-def}. We have for each $\fu\in \fU_1(k,n,l)$, \begin{equation} \mu(\bigcup_{I\in \mathcal{L}(\fu)} I) \le D^{1-\kappa Z(n+1)} \mu(\scI(\mathfrak{u})). \end{equation}
- id `forest-inner`: lemma (forest inner). For each $\fu\in \fU_3(k,n,j)$ and each $\fp \in \mathfrak{T}_2(\fu)$ we have \begin{equation} B(\pc(\fp), 8 D^{\ps(\fp)}) \subset \scI(\fu). \end{equation}
- id `C-convex`: lemma (C convex). For each $k,n$, the collection $\fC(k,n)$ is convex.
- id `wiggle-order-3`: lemma (wiggle order 3). The following implications hold for all $\fq, \fq' \in \fP$: \begin{equation} \fq \le \fq' \ \text{and} \ \lambda \ge 1.1 \implies \lambda \fq \lesssim \lambda \fq'\,, \end{equation} \begin{equation} 10\fq \lesssim \fq' \ \text{and} \ \scI(\fq) \ne \scI(\fq') \implies 100 \fq \lesssim 100 \fq'\,, \end{equation} \begin{equation} 2\fq \lesssim \fq' \ \text{and} \ \scI(\fq) \ne \scI(\fq') \implies 4 \fq \lesssim 500 \fq'\,. \end{equation}
- id `wiggle-order-2`: lemma (wiggle order 2). Let $n, m \ge 1$ and $k > 0$. If $\fp, \fp' \in \fP$ with $\scI(\fp) \ne \scI(\fp')$ and \begin{equation} n \fp \lesssim k \fp' \end{equation} then \begin{equation} (n + 2^{-95 a} m) \fp \lesssim m\fp'\,. \end{equation}
- id `John-Nirenberg`: lemma (John Nirenberg). For all integers $k,n,\lambda\ge 0$, we have \begin{equation} \mu(A(\lambda,k,n)) \le 2^{k+1-\lambda}\mu(G)\,. \end{equation}
- id `P-convex`: lemma (P convex). For each $k$, the collection $\fP(k)$ is convex.
- id `forest-stacking`: lemma (forest stacking). It holds for $k\le n$ that \begin{equation} \sum_{\fu \in \fU_3(k,n,j)} \mathbf{1}_{\scI(\fu)} \le (4n+12)2^{n}\,. \end{equation}
- id `dens-compare`: lemma (dens compare). We have for every $k\ge 0$ and $\fP'\subset \fP(k)$ \begin{equation} \dens_1(\fP')\le \dens_k'(\fP')\, . \end{equation}
- id `wiggle-order-1`: lemma (wiggle order 1). If $n\fp \lesssim m\fp'$ and $n' \ge n$ and $m \ge m'$ then $n'\fp \lesssim m'\fp'$.
- id `dyadic-union`: lemma (dyadic union). For each $x\in A(\lambda,k,n)$, there is a dyadic cube $I$ that contains $x$ and is a subset of $A(\lambda,k,n)$.
- id `C4-convex`: lemma (C4 convex). For each $k,n,j$, the collection $\fC_4(k,n,j)$ is convex.
- id `C-dens1`: lemma (C dens1). For each set $\mathfrak{A} \subset \mathfrak{C}(k,n)$, we have $$ \dens_1(\mathfrak{A}) \le 2^{4a}2^{-n+1}\,. $$
- id `exceptional-set`: lemma (exceptional set). We have \begin{equation} \mu(G')\le 2^{-1}\mu(G)\, . \end{equation}
- id `L0-antichain`: lemma (L0 antichain). We have that $$ \fL_0(k,n) = \dot{\bigcup_{0 \le l < n}} \fL_0(k,n,l)\,, $$ where each $\fL_0(k,n,l)$ is an antichain.
- id `L2-antichain`: lemma (L2 antichain). Each of the sets $\fL_2(k,n,j)$ is an antichain.
- id `forest-union`: lemma (forest union). Let \begin{equation} \fP_1 =\bigcup_{k\ge 0}\bigcup_{n\ge k} \bigcup_{0\le j\le 2n+3}\fC_5(k,n,j) \end{equation} For all $f:X\to \C$ with $|f|\le \mathbf{1}_F$ we have \begin{equation} \int_{G \setminus G'} \left|\sum_{\fp \in \fP_1} T_{\fp} f \right|\, \mathrm{d}\mu \le \frac{2^{441a^3}}{(q-1)^4} \mu(G)^{1 - \frac{1}{q}} \mu(F)^{\frac{1}{q}}\,. \end{equation}
- id `C3-convex`: lemma (C3 convex). For each $k,n,j$, the collection $\fC_3(k,n,j)$ is convex.

## Constraints

- `C-convex` before `C1-convex`
- `C-dens1` before `forest-complement`
- `C-dens1` before `forest-union`
- `C1-convex` before `C2-convex`
- `C2-convex` before `C3-convex`
- `C3-convex` before `C4-convex`
- `C4-convex` before `C5-convex`
- `C5-convex` before `forest-convex`
- `C6-forest` before `forest-union`
- `John-Nirenberg` before `second-exception`
- `John-Nirenberg` before `top-tiles`
- `L0-antichain` before `forest-complement`
- `L1-L3-antichain` before `forest-complement`
- `L2-antichain` before `forest-complement`
- `P-convex` before `C-convex`
- `boundary-exception` before `third-exception`
- `dens-compare` before `C-dens1`
- `dense-cover` before `John-Nirenberg`
- `dyadic-union` before `John-Nirenberg`
- `equivalence-relation` before `C6-forest`
- `equivalence-relation` before `forest-geometry`
- `equivalence-relation` before `forest-inner`
- `equivalence-relation` before `forest-separation`
- `equivalence-relation` before `forest-stacking`
- `equivalence-relation` before `forest-union`
- `first-exception` before `exceptional-set`
- `forest-convex` before `forest-union`
- `forest-geometry` before `forest-union`
- `forest-inner` before `forest-union`
- `forest-separation` before `forest-union`
- `forest-stacking` before `forest-union`
- `pairwise-disjoint` before `John-Nirenberg`
- `relation-geometry` before `equivalence-relation`
- `relation-geometry` before `forest-geometry`
- `relation-geometry` before `forest-inner`
- `relation-geometry` before `forest-union`
- `second-exception` before `exceptional-set`
- `third-exception` before `exceptional-set`
- `top-tiles` before `third-exception`
- `tree-count` before `third-exception`
- `wiggle-order-1` before `forest-inner`
- `wiggle-order-1` before `forest-union`
- `wiggle-order-1` before `relation-geometry`
- `wiggle-order-2` before `L2-antichain`
- `wiggle-order-2` before `wiggle-order-3`
- `wiggle-order-3` before `C-convex`
- `wiggle-order-3` before `C1-convex`
- `wiggle-order-3` before `C3-convex`
- `wiggle-order-3` before `L2-antichain`
- `wiggle-order-3` before `equivalence-relation`
- `wiggle-order-3` before `forest-convex`
- `wiggle-order-3` before `forest-geometry`
- `wiggle-order-3` before `forest-inner`
- `wiggle-order-3` before `forest-separation`
- `wiggle-order-3` before `forest-stacking`
- `wiggle-order-3` before `relation-geometry`
