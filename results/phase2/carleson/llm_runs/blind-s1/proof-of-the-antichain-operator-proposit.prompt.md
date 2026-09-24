You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `r536`: lemma. Let $-S\le s_1\le s_2\le S$ and let $x_1,x_2\in X$. Define \begin{equation} \varphi(y) := \overline{K_{s_1}(x_1, y)} K_{s_2}(x_2, y) \, . \end{equation} If $\varphi(y)\neq 0$, then \begin{equation} y\in B(x_1, D^{s_1})\, . \end{equation} Moreover, we have with $\tau = 1/a$ \begin{equation} \|\varphi\|_{C^\tau(B(x_1, 2 D^{s_1}))}\le \frac{2^{231 a^3}}{\mu(B(x_1, D^{s_1}))\mu(B(x_2, D^{s_2}))} \, . \end{equation}
- id `r157`: lemma. Let $\mfa\in\Mf$ and {$N$} be an integer. Let $\fp_{\mfa}$ be a tile with $\mfa\in B_{\fp_{\mfa}}(\fcc(\fp_{\mfa}), 2^{N+1})$. Then we have \begin{equation} \sum_{\fp\in\mathfrak{A}_{\mfa,N}: \ps(\fp_{\mfa})<\ps(\fp)}\mu(E(\fp)\cap G \cap \scI(\fp_{\mfa})) \le \mu (E_2(2^{N+3},\fp_{\mfa})) \, . \end{equation}
- id `r592`: lemma. We have that \begin{equation} \left|\int \overline{g(x)} \sum_{\fp \in \mathfrak{A}} T_{\fp} f(x)\, d\mu(x)\right|\le 2^{103a^3}({q}-1)^{-1} \dens_2(\mathfrak{A})^{\frac 1{\tilde{q}}-\frac 12} \|f\|_2\|g\|_2\, . \end{equation}
- id `r990`: lemma. Let $x\in X$. Then \begin{equation} | \sum_{\fp \in \mathfrak{A}}T_{\fp} f(x)|\le 2^{102 a^3} M_{\mathcal{B}} f (x) \, . \end{equation}
- id `r473`: lemma. Let $\fp_1, \fp_2\in \fP$ with $B(\pc(\fp_1),5D^{\ps(\fp_1)}) \cap B(\pc(\fp_2),5D^{\ps(\fp_2)}) \ne \emptyset$ and $\ps({\fp_1})\leq \ps({\fp_2})$. For each $x_1\in E(\fp_1)$ and $x_2\in E(\fp_2)$ we have \begin{equation} 1+d_{\fp_1}(\fcc(\fp_1), \fcc(\fp_2))\le 2^{8a}(1 + d_{B(x_1, D^{\ps(\fp_1)})}(\tQ(x_1),\tQ(x_2)))\, . \end{equation}
- id `r683`: lemma. Let $\mfa \in \Mf$, $N\ge 0$ and $L\in \mathcal{D}$. Then \begin{equation} \sum_{\fp\in\mathfrak{A}_{\mfa,N}:\scI(\fp)=L}\mu(E(\fp)\cap G)\le 2^{a(N+5)}\dens_1(\mathfrak{A})\mu(L)\, . \end{equation}
- id `r667`: lemma. Set $p:=4a^4$. We have \begin{equation} \left|\int \overline{g(x)} \sum_{\fp \in \mathfrak{A}} T_{\fp} f(x)\, d\mu(x)\right|\le 2^{117a^3}\dens_1(\mathfrak{A})^{\frac 1{2p}} \|f\|_2\|g\|_2\,. \end{equation}
- id `r304`: lemma. Let $\fp,\fp'\in \mathfrak{A}$. If there exists an $x\in X$ with $x\in E(\fp)\cap E(\fp')$, then $\fp= \fp'$.
- id `r616`: lemma. Let $\fp, \fp'\in \fP$ with $\ps({\fp'})\leq \ps({\fp})$. Then \begin{equation} \left|\int T^*_{\fp'}g\overline{T^*_{\fp}g}\right| \end{equation} \begin{equation} \le 2^{232a^3}\frac{(1+d_{\fp'}(\fcc(\fp'), \fcc(\fp))^{-1/(2a^2+a^3)}}{\mu(\scI(\fp))}\int_{E(\fp')}|g|\int_{E(\fp)}|g|\,. \end{equation} Moreover, the term `r616` vanishes unless \begin{equation} \scI(\fp') \subset B(\pc(\fp), 14D^{\ps(\fp)})\, . \end{equation}
- id `r523`: lemma. For each $\fp\in \fP$, and each $y\in X$, we have that \begin{equation} T_{\fp}^* g(y)\neq 0 \end{equation} implies \begin{equation} y\in B(\pc(\fp),5D^{\ps(\fp)})\, . \end{equation}
- id `r596`: lemma. Let $\mfa\in Q(X)$ and let $N\ge 0$ be an integer. Then we have \begin{equation} \sum_{\fp\in\mathfrak{A}_{\mfa,N}}\mu(E(\fp)\cap G) \le 2^{101a^3+Na}\dens_1(\mathfrak{A})\mu\left(\cup_{\fp\in\mathfrak{A}}I_{\fp}\right)\, . \end{equation}
- id `r932`: lemma. Let $\mfa\in \Mf$ and $N\ge0$ be an integer. Let $\fp, \fp'\in \fP$ with \begin{equation} d_{\fp}(\fcc(\fp), \mfa))\le 2^N\, \end{equation} \begin{equation} d_{\fp'}(\fcc(\fp'), \mfa))\le 2^N\, . \end{equation} Assume $\scI(\fp)\subset \scI(\fp')$ and $\ps(\fp)<\ps(\fp')$. Then \begin{equation}2^{N+2}\fp\lesssim 2^{N+2} \fp'\, . \end{equation}
- id `r465`: lemma. Set $p:=4a^4$. For every $\mfa\in\Mf$ and every antichain $\mathfrak{A}$ we have \begin{equation} \Big\|\sum_{\fp\in\mathfrak{A}}(1+d_{\fp}(\fcc(\fp), \mfa))^{-1/(2a^2+a^3)}\mathbf{1}_{E(\fp)}\mathbf{1}_G\Big\|_{p} \end{equation} \begin{equation} \le 2^{5a}\dens_1(\mathfrak{A})^{\frac 1p}\mu\left(\cup_{\fp\in\mathfrak{A}}I_{\fp}\right)^{\frac 1p}\, . \end{equation}

## Constraints

- `r157` before `r596`
- `r304` before `r157`
- `r304` before `r465`
- `r304` before `r667`
- `r304` before `r990`
- `r465` before `r667`
- `r473` before `r616`
- `r523` before `r616`
- `r536` before `r616`
- `r596` before `r465`
- `r616` before `r667`
- `r683` before `r596`
- `r932` before `r157`
- `r932` before `r596`
- `r990` before `r592`
