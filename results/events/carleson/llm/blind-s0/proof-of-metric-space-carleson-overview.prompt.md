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

- id `r588`: lemma; steps here: state and prove. Let $(\mathcal{D}, c, s)$ be a grid structure. Denote for cubes $I \in \mathcal{D}$ $$ I^\circ := B(c(I), \frac{1}{4} D^{s(I)})\,. $$ Let $I, J \in \mathcal{D}$ with $I \subset J$. Then for all $\mfa, \mfb \in\Mf$ we have $$ d_{I^\circ}(\mfa, \mfb) \le d_{J^\circ}(\mfa, \mfb)\,, $$ and if $I \ne J$ then we have $$ d_{I^\circ}(\mfa, \mfb) \le 2^{-95a} d_{J^\circ}(\mfa, \mfb)\,. $$
- id `r466`: proposition; steps here: state only (it is proved in a later section). Let $\mathcal{B}$ be a finite collection of balls in $X$. If for some $\lambda>0$ and some measurable function $u:X\to [0,\infty)$ we have \begin{equation} \int_{B} u(x)\, d\mu(x)\ge \lambda \mu(B) \end{equation} for each $B\in \mathcal{B}$, then \begin{equation} \lambda \mu(\bigcup \mathcal{B}) \le 2^{2a}\int_X u(x)\, d\mu(x)\, . \end{equation} For every measurable function $v$ and $1\le p_1<p_2$ we have \begin{equation} \|M_{\mathcal{B},p_1} v\|_{p_2}\le 2^{2a}\frac{p_2}{p_2-p_1} \|v\|_{p_2}\, . \end{equation} Moreover, given any measurable bounded function $w: X \to \C$ there exists a measurable function $Mw: X \to [0, \infty)$ such that the following `r466` and `r466` hold. For each ball $B \subset X$ and each $x \in B$ \begin{equation} \frac{1}{\mu(B)} \int_{B} |w(y)| \, \mathrm{d}\mu(y) \le Mw(x) \end{equation} and for all $1 \le p_1 < p_2 \le \infty$ \begin{equation} \|M(w^{p_1})^{\frac{1}{p_1}}\|_{p_2} \le 2^{4a} \frac{p_2}{p_2-p_1}\|w\|_{p_2}\,. \end{equation}
- id `r697`: proposition; steps here: state only (it is proved in a later section). Let $(\mathcal{D}, c, s)$ be a grid structure and \begin{equation*} (\fP,\scI,\fc,\fcc,\pc,\ps) \end{equation*} a tile structure for this grid structure. Define for $\fp\in \fP$ \begin{equation} E(\fp)=\{x\in \scI(\fp): \tQ(x)\in \fc(\fp) , {\sigma_1}(x)\le \ps(\fp)\le {\sigma_2}(x)\} \end{equation} and \begin{equation} T_{\fp} f(x)= \mathbf{1}_{E(\fp)}(x) \int K_{\ps(\fp)}(x,y) f(y) e(\tQ(x)(y)-\tQ(x)(x))\, d\mu(y). \end{equation} Then there exists a Borel set $G'$ with $2\mu(G') \leq \mu(G)$ such that for all Borel functions $f:X\to \C$ with $|f|\le \mathbf{1}_F$ we have \begin{equation} \int_{G \setminus G'} \left| \sum_{\fp \in \fP} T_{\fp} f (x) \right| \, \mathrm{d}\mu(x) \le \frac{2^{442a^3}}{(q-1)^5} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac{1}{q}}\,. \end{equation}
- id `r323`: proposition; steps here: state only (it is proved in a later section). For any $n\ge 0$ and any $n$-forest $(\fU,\fT)$ we have for all $f,g: X \to \mathbb{C}$ with $|f| \le \mathbf{1}_F$ and $|g| \le \mathbf{1}_G$ $$ | \int \overline{g(x)} \sum_{\fu\in \fU} \sum_{\fp\in \fT(\fu)} T_{\fp} f(x) \, \mathrm{d}\mu(x)| $$ $$ \le 2^{440a^3}2^{-\frac{q-1}{q} n} \dens_2\left(\bigcup_{\fu\in \fU}\fT(\fu)\right)^{\frac{1}{q}-\frac{1}{2}} \|f\|_2 \|g\|_2 \,. $$
- id `r616`: proposition; steps here: state only (it is proved in a later section). Let $z\in X$ and $R>0$ and set $B=B(z,R)$. Let $\varphi: X \to \mathbb{C}$ be supported on $B$ and satisfy $\|{\varphi}\|_{C^\tau(B(z, 2R))}<\infty$. Let $\mfa, \mfb \in \Mf$. Then \begin{equation} |\int e(\mfa(x)-{\mfb(x)})\varphi(x) dx|\le 2^{7a} \mu(B) \|{\varphi}\|_{C^\tau(B(z, 2R))} (1 + d_{B}(\mfa,\mfb))^{-\frac{1}{2a^2+a^3}} \,. \end{equation}
- id `r242`: proposition; steps here: state only (it is proved in a later section). For any antichain $\mathfrak{A} $ and for all $f:X\to \C$ with $|f|\le \mathbf{1}_F$ and all $g:X\to\C$ with $|g| \le \mathbf{1}_G$ \begin{equation} |\int \overline{g(x)} \sum_{\fp \in \mathfrak{A}} T_{\fp} f(x)\, d\mu(x)| \end{equation} \begin{equation} \le \frac{2^{117a^3}}{q-1} \dens_1(\mathfrak{A})^{\frac {q-1}{8a^4}}\dens_2(\mathfrak{A})^{\frac 1{q}-\frac 12} \|f\|_2 \|g\|_2\, . \end{equation}
- id `r388`: proposition; steps here: state only (it is proved in a later section). Let ${\sigma_1},\sigma_2\colon X\to \mathbb{Z}$ be measurable functions with finite range and ${\sigma_1}\leq \sigma_2$. Let $F,G$ be bounded Borel sets in $X$. Then there is a Borel set $G'$ in $X$ with $2\mu(G')\leq \mu(G)$ such that for all Borel functions $f:X\to \C$ with $|f|\le \mathbf{1}_F$. \begin{equation*} \int_{G \setminus G'} \left|\sum_{s={\sigma_1}(x)}^{{\sigma_2}(x)} \int K_s(x,y) f(y) e(\tQ(x)(y)) \, \mathrm{d}\mu(y) \right| \mathrm{d}\mu(x) \end{equation*} \begin{equation} \le \frac{2^{442a^3}}{(q-1)^5} \mu(G)^{1-\frac{1}{q}} \mu(F)^{\frac 1 q}\,. \end{equation}
- id `r243`: lemma; steps here: state and prove. Let $-S\le s\le S$ and $x,y,y'\in X$. If $K_s(x,y)\neq 0$, then we have \begin{equation} \frac{1}{4} D^{s-1} \leq \rho(x,y) \leq \frac{1}{2} D^s\, . \end{equation} We have \begin{equation} |K_s(x,y)|\le \frac{2^{102 a^3}}{\mu(B(x, D^{s}))}\, \end{equation} and \begin{equation} |K_s(x,y)-K_s(x, y')|\le \frac{2^{127a^3}}{\mu(B(x, D^{s}))} \left(\frac{ \rho(y,y')}{D^s}\right)^{\frac 1a}\,. \end{equation}
- id `r873`: lemma; steps here: state and prove. Let $B' \subset X$ be a ball. Let $r > 0$, $\mfa \in \Mf$ and $k \in \mathbb{N}$. Suppose that $\mathcal{Z} \subset B_{B'}(\mfa, r2^k)$ satisfies that $\{B_{B'}(z,r)\mid z \in \mathcal{Z}\}$ is a collection of pairwise disjoint sets. Then $$ |\mathcal{Z}| \le 2^{ka}\,. $$

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

None.
