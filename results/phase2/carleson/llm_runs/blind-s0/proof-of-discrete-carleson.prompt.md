You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `r710`: lemma. We have \begin{equation} \fC_6(k,n,j)=\bigcup_{\fu\in \fU_3(k,n,j)}\mathfrak{T}_2(\fu)\, . \end{equation}
- id `r917`: lemma. We have that \begin{align} &\quad \fP_2 \cap \fP_{G \setminus G'}\\ &= \bigcup_{k \ge 0} \bigcup_{n \ge k} \fL_0(k,n) \cap \fP_{G \setminus G'} \\ &\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} \fL_2(k,n,j) \cap \fP_{G \setminus G'}\\ &\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} \bigcup_{0 \le l \le Z(n+1)} \fL_1(k,n,j,l) \cap \fP_{G \setminus G'}\\ &\quad\cup \bigcup_{k \ge 0} \bigcup_{n \ge k}\bigcup_{0 \le j \le 2n+3} \bigcup_{0 \le l \le Z(n+1)} \fL_3(k,n,j,l)\cap \fP_{G \setminus G'}\,. \end{align}
- id `r494`: lemma. For each $k$, the collection $\fP(k)$ is convex.
- id `r424`: lemma. For each $k,n,j$, the collection $\fC_3(k,n,j)$ is convex.
- id `r689`: lemma. We have \begin{equation} \sum_{\mathfrak{m} \in \mathfrak{M}(k,n)} \mu(\scI(\mathfrak{m}))\le 2^{n+k+3}\mu(G). \end{equation}
- id `r347`: lemma. Let $\mathcal{L}(\fu)$ be as defined in [another result]. We have for each $\fu\in \fU_1(k,n,l)$, \begin{equation} \mu(\bigcup_{I\in \mathcal{L}(\fu)} I) \le D^{1-\kappa Z(n+1)} \mu(\scI(\mathfrak{u})). \end{equation}
- id `r397`: lemma. We have that $$ \fL_0(k,n) = \dot{\bigcup_{0 \le l < n}} \fL_0(k,n,l)\,, $$ where each $\fL_0(k,n,l)$ is an antichain.
- id `r288`: lemma. We have \begin{equation} \mu(G_1)\le 2^{-5}\mu(G)\, . \end{equation}
- id `r293`: lemma. Each of the sets $\fL_2(k,n,j)$ is an antichain.
- id `r941`: lemma. We have \begin{equation} \mu(G_3)\le 2^{-4} \mu(G)\, . \end{equation}
- id `r291`: lemma. For each $k,n,j$, the collection $\fC_2(k,n,j)$ is convex.
- id `r133`: lemma. If $n\fp \lesssim m\fp'$ and $n' \ge n$ and $m \ge m'$ then $n'\fp \lesssim m'\fp'$.
- id `r727`: lemma. We have \begin{equation} \mu(G_2)\le 2^{-2} \mu(G)\, . \end{equation}
- id `r772`: lemma. It holds for $k\le n$ that \begin{equation} \sum_{\fu \in \fU_3(k,n,j)} \mathbf{1}_{\scI(\fu)} \le (4n+12)2^{n}\,. \end{equation}
- id `r366`: lemma. Let \begin{equation} \fP_1 =\bigcup_{k\ge 0}\bigcup_{n\ge k} \bigcup_{0\le j\le 2n+3}\fC_5(k,n,j) \end{equation} For all $f:X\to \C$ with $|f|\le \mathbf{1}_F$ we have \begin{equation} \int_{G \setminus G'} \left|\sum_{\fp \in \fP_1} T_{\fp} f \right|\, \mathrm{d}\mu \le \frac{2^{441a^3}}{(q-1)^4} \mu(G)^{1 - \frac{1}{q}} \mu(F)^{\frac{1}{q}}\,. \end{equation}
- id `r587`: lemma. The following implications hold for all $\fq, \fq' \in \fP$: \begin{equation} \fq \le \fq' \ \text{and} \ \lambda \ge 1.1 \implies \lambda \fq \lesssim \lambda \fq'\,, \end{equation} \begin{equation} 10\fq \lesssim \fq' \ \text{and} \ \scI(\fq) \ne \scI(\fq') \implies 100 \fq \lesssim 100 \fq'\,, \end{equation} \begin{equation} 2\fq \lesssim \fq' \ \text{and} \ \scI(\fq) \ne \scI(\fq') \implies 4 \fq \lesssim 500 \fq'\,. \end{equation}
- id `r170`: lemma. For each $\fu\in \fU_3(k,n,j)$, the set $\mathfrak{T}_2(\fu)$ satisfies [another result].
- id `r191`: lemma. For each set $\mathfrak{A} \subset \mathfrak{C}(k,n)$, we have $$ \dens_1(\mathfrak{A}) \le 2^{4a}2^{-n+1}\,. $$
- id `r795`: lemma. For each $k,n,j$, the relation $\sim$ on $\fU_2(k,n,j)$ is an equivalence relation.
- id `r875`: lemma. Let $n, m \ge 1$ and $k > 0$. If $\fp, \fp' \in \fP$ with $\scI(\fp) \ne \scI(\fp')$ and \begin{equation} n \fp \lesssim k \fp' \end{equation} then \begin{equation} (n + 2^{-95 a} m) \fp \lesssim m\fp'\,. \end{equation}
- id `r233`: lemma. For each $k,n$, the collection $\fC(k,n)$ is convex.
- id `r997`: lemma. For each $k\ge 0$, the union of all dyadic cubes in $\mathcal{C}(G,k)$ has measure at most $2^{k+1} \mu(G)$ .
- id `r253`: lemma. For each $\fu\in \fU_3(k,n,j)$, the set $\mathfrak{T}_2(\fu)$ satisfies the convexity condition [another result].
- id `r139`: lemma. For each $\fu,\fu'\in \fU_3(k,n,j)$ with $\fu\neq \fu'$ and each $\fp \in \fT_2(\fu)$ with $\scI(\fp)\subset \scI(\fu')$ we have \begin{equation} d_{\fp}(\fcc(\fp), \fcc(\fu')) > 2^{Z(n+1)}\,. \end{equation}
- id `r962`: lemma. For each $k,n,j$, the collection $\fC_1(k,n,j)$ is convex.
- id `r182`: lemma. For each $x\in A(\lambda,k,n)$, there is a dyadic cube $I$ that contains $x$ and is a subset of $A(\lambda,k,n)$.
- id `r816`: lemma. Let \begin{equation} \fP_2 =\fP\setminus \fP_1\,. \end{equation} For all $f:X\to \C$ with $|f|\le \mathbf{1}_F$ we have \begin{equation} \int_{G \setminus G'} \left|\sum_{\fp \in \fP_2} T_{\fp} f\right| \, \mathrm{d}\mu \le \frac{2^{120a^3}}{(q-1)^5} \mu(G)^{1 - \frac{1}{q}} \mu(F)^{\frac{1}{q}}\,. \end{equation}
- id `r949`: lemma. For each $k,n,j$, the collection $\fC_5(k,n,j)$ is convex.
- id `r653`: lemma. Let $k,n,j\ge 0$. We have for every $x\in X$ \begin{equation} \sum_{\fu\in \fU_1(k,n,j)} \mathbf{1}_{\scI(\fu)}(x) \le 2^{-j} 2^{9a} \sum_{\mathfrak{m}\in \mathfrak{M}(k,n)} \mathbf{1}_{\scI(\mathfrak{m})}(x) \end{equation}
- id `r799`: lemma. We have for every $k\ge 0$ and $\fP'\subset \fP(k)$ \begin{equation} \dens_1(\fP')\le \dens_k'(\fP')\, . \end{equation}
- id `r500`: lemma. For all integers $k,n,\lambda\ge 0$, we have \begin{equation} \mu(A(\lambda,k,n)) \le 2^{k+1-\lambda}\mu(G)\,. \end{equation}
- id `r957`: lemma. For each $k,n,j$, the collection $\fC_4(k,n,j)$ is convex.
- id `r822`: lemma. For each $\fu\in \fU_3(k,n,j)$ and each $\fp \in \mathfrak{T}_2(\fu)$ we have \begin{equation} B(\pc(\fp), 8 D^{\ps(\fp)}) \subset \scI(\fu). \end{equation}
- id `r637`: lemma. Each of the sets $\fL_1(k,n,j,l)$ and $\fL_3(k,n,j,l)$ is an antichain.
- id `r382`: lemma. If $\fu \sim \fu'$, then $\scI(u) = \scI(u')$ and \begin{equation*} B_{\fu}(\fcc(\fu), 100) \cap B_{\fu'}(\fcc(\fu'), 100) \neq \emptyset\ . \end{equation*}
- id `r634`: lemma. If $\fp, \fp' \in {\mathfrak{M}}(k,n)$ and \begin{equation} {E_1}(\fp)\cap {E_1}(\fp')\neq \emptyset, \end{equation} then $\fp=\fp'$.
- id `r931`: lemma. We have \begin{equation} \mu(G')\le 2^{-1}\mu(G)\, . \end{equation}

## Constraints

- `r133` before `r366`
- `r133` before `r382`
- `r133` before `r822`
- `r139` before `r366`
- `r170` before `r366`
- `r182` before `r500`
- `r191` before `r366`
- `r191` before `r816`
- `r233` before `r962`
- `r253` before `r366`
- `r288` before `r931`
- `r291` before `r424`
- `r293` before `r816`
- `r347` before `r941`
- `r382` before `r170`
- `r382` before `r366`
- `r382` before `r795`
- `r382` before `r822`
- `r397` before `r816`
- `r424` before `r957`
- `r494` before `r233`
- `r500` before `r689`
- `r500` before `r727`
- `r587` before `r139`
- `r587` before `r170`
- `r587` before `r233`
- `r587` before `r253`
- `r587` before `r293`
- `r587` before `r382`
- `r587` before `r424`
- `r587` before `r772`
- `r587` before `r795`
- `r587` before `r822`
- `r587` before `r962`
- `r634` before `r500`
- `r637` before `r816`
- `r653` before `r941`
- `r689` before `r941`
- `r710` before `r366`
- `r727` before `r931`
- `r772` before `r366`
- `r795` before `r139`
- `r795` before `r170`
- `r795` before `r366`
- `r795` before `r710`
- `r795` before `r772`
- `r795` before `r822`
- `r799` before `r191`
- `r822` before `r366`
- `r875` before `r293`
- `r875` before `r587`
- `r941` before `r931`
- `r949` before `r253`
- `r957` before `r949`
- `r962` before `r291`
- `r997` before `r500`
