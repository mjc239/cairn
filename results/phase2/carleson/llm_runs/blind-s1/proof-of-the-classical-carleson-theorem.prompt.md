You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `r388`: lemma. For any $x,x'\in \R$ and $R>0$ with $x\in B(x',2R)$ and any $n,m\in \mathbb{Z}$, we have \begin{equation} d_{B(x',2R)}(\mfa_n,\mfa_m)\le 2 d_{B(x,R)}(\mfa_n,\mfa_m) \, . \end{equation}
- id `r118`: lemma. For all $N\in\Z$ and $x\in [-\pi,\pi] \setminus \{0\}$, \begin{equation*} \left|K_N(x) - (e^{-iNx}\kappa(x) + \overline{e^{-iNx}\kappa(x)})\right| \le \pi \,. \end{equation*}
- id `r260`: lemma. Let $\eta>0$ and $-2\pi +\eta \le x\le 2\pi-\eta$ with $|x|\ge \eta$. Then \begin{equation} |1-e^{ix}|\ge \frac{2}{\pi} \eta \end{equation}
- id `r305`: lemma. The function $f_0$ is $2\pi$-periodic. The function $f_0$ is smooth (and therefore measurable). The function $f_0$ satisfies for all $x\in \R$: \begin{equation} |f(x)-f_0(x)|\le \epsilon' \, , \end{equation}
- id `r978`: lemma. We have for every bounded measurable $2\pi$-periodic function $g$ \begin{equation} \|L_Ng\|_{L^2[0, 2\pi]}\le \|g\|_{L^2[0, 2\pi]}\,. \end{equation}
- id `r435`: lemma. Let $F,G$ be Borel subsets of $\R$ with finite measure. Let $f$ be a bounded measurable function on $\R$ with $|f|\le \mathbf{1}_F$. Then \begin{equation} \left|\int _G Tf(x) \, dx\right| \le C_{4,2} |F|^{\frac 12} |G|^{\frac 12} \, , \end{equation} where \begin{equation} T f(x)=\sup_{n\in \mathbb{Z}} \sup_{r>0}\left|\int_{r<|x-y|<1} f(y)\kappa(x-y) e^{iny}\, dy\right|\, . \end{equation}
- id `r930`: lemma. There is a set $E \subset \R$ with Lebesgue measure $|E|\le \epsilon$ such that for all \begin{equation} x\in [0,2\pi)\setminus E \end{equation} we have \begin{equation} \sup_{N\ge 0} |S_Nf(x)-S_Nf_0(x)| \le \frac \epsilon 4\,. \end{equation}
- id `r676`: lemma. For every $R > 0$ and $x \in X$, and for all $n, m \in \mathbb{Z}$, we have \begin{equation} \sup_{y,y'\in B(x,R)}|ny-ny'-my+my'|\le 2|n-m|R\, . \end{equation}
- id `r901`: lemma. Let $g:\R\to\C$ be a measurable $2\pi$-periodic function such that for some $\delta>0$ and every $x\in\R$, \begin{equation} |g(x)|\le \delta \,. \end{equation} Then for every $\epsilon>0$, there exists a measurable set $E\subset [0,2\pi]$ with $|E|<\epsilon$ such that for every $x\in [0,2\pi]\setminus E$ and $N>0$, \begin{equation} |S_N g(x)|\le C_\epsilon \delta, \end{equation} where \begin{equation} C_\epsilon = \left(\frac{8}{\pi\epsilon}\right)^\frac{1}{2} C_{4,2} + \pi \,. \end{equation}
- id `r238`: lemma. We have for every $2\pi$-periodic bounded measurable $f$ and every $N\ge 0$ \begin{equation} S_Nf(x)=\frac 1{2\pi}\int_{0}^{2\pi}f(y) K_N(x-y)\, dy \end{equation} where $K_N$ is the $2\pi$-periodic continuous function of $\R$ given by \begin{equation} \sum_{n=-N}^N e^{in x'}\, . \end{equation} We have for $e^{ix'}\neq 1$ that \begin{equation} K_N(x')=\frac{e^{iNx'}}{1-e^{-ix'}} +\frac {e^{-iNx'}}{1-e^{ix'}} \, . \end{equation}
- id `r447`: lemma. We have for every $x\in \R$ and $R>0$ \begin{equation} \mu(B(x,2R))=2\mu(B(x,R))\, . \end{equation}
- id `r539`: lemma. For any $x,x'\in \R$ and $R>0$ with $B(x,R)\subset B(x',2R)$ and any $n,m\in \mathbb{Z}$, we have \begin{equation} 2d_{B(x,R)}(\mfa_n,\mfa_m)\le d_{B(x',2R)}(\mfa_n,\mfa_m) \, . \end{equation}
- id `r318`: lemma. Let $g,f$ be bounded measurable $2\pi$-periodic functions. Let $0<r<\pi$. Assume we have for all $x$ \begin{equation} |g(x)|\le k_r(x)\, . \end{equation} Let \begin{equation} h(x)= \int_0^{2\pi} f(y)g(x-y)\, dy \, . \end{equation} Then \begin{equation} \|h\|_{L^2[0, 2\pi]}\le 17\|f\|_{L^2[-\pi, \pi]} \, . \end{equation}
- id `r372`: lemma. For $x,y\in \R$ with $x\neq y$ we have \begin{equation} |\kappa(x-y)|\le 2^2(2|x-y|)^{-1}\, . \end{equation}
- id `r790`: lemma. Let $f$ be a bounded $2\pi$-periodic measurable function. Then, for all $N\ge 0$ \begin{equation} \|S_Nf\|_{L^2[0, 2\pi]} \le \|f\|_{L^2[0, 2\pi]}. \end{equation}
- id `r198`: lemma. For every $x\in \R$ and $R>0$ and every $n\in \mathbb{Z}$ and $R'>0$, there exist $m_1, m_2, m_3\in \mathbb{Z}$ such that \begin{equation} B'\subset B_1\cup B_2\cup B_3\, , \end{equation} where \begin{equation} B'= \{ \mfa \in \Mf: d_{B(x,R)}(\mfa, \mfa_n)<2R'\} \end{equation} and for $j=1,2,3$ \begin{equation} B_j= \{ \mfa \in \Mf: d_{B(x,R)}(\mfa, \mfa_{m_j})<R'\} \, . \end{equation}
- id `r957`: theorem. Let $f$ be a $2\pi$-periodic complex-valued continuous function on $\mathbb{R}$. For all $\epsilon>0$, there exists a Borel set $E\subset [0,2\pi]$ with Lebesgue measure $|E|\le \epsilon$ and a positive integer $N_0$ such that for all $x\in [0,2\pi]\setminus E$ and all integers $N>N_0$, we have \begin{equation} |f(x)-S_N f(x)|\le \epsilon. \end{equation}
- id `r488`: lemma. For $x,y,y'\in \R$ with $x\neq y,y'$ and \begin{equation} 2|y-y'|\le |x-y|\, , \end{equation} we have \begin{equation} |\kappa(x-y) - \kappa(x-y')|\le 2^{8}\frac{1}{|x-y|} \frac{|y-y'|}{|x-y|}\, . \end{equation}
- id `r660`: lemma. For any $x\in \R$ and $R>0$ and any function $\varphi: X\to \C$ supported on $B'=B(x,R)$ such that \begin{equation} \|\varphi\|_{\Lip(B')} = \sup_{x \in B'} |\varphi(x)| + R \sup_{x,y \in B', x \neq y} \frac{|\varphi(x) - \varphi(y)|}{\rho(x,y)} \end{equation} is finite and for any $n,m\in \mathbb{Z}$, we have \begin{equation} \left|\int_{B'} e(\mfa_n(x)-{\mfa_m(x)}) \varphi(x) d\mu(x)\right|\le 2\pi \mu(B')\frac{\|\varphi\|_{\Lip(B')}}{1+d_{B'}(\mfa_n,\mfa_m)} \, . \end{equation}
- id `r452`: lemma. Let $f:\R \to \C$ be $2\pi$-periodic and twice continuously differentiable. Then \begin{equation} \sup_{x\in [0,2\pi]} |f(x) - S_Nf(x)| \rightarrow 0 \end{equation} as $N \rightarrow \infty$.
- id `r803`: lemma. There exists some $N_0 \in \N$ such that for all $N>N_0$ and $x\in [0,2\pi]$ we have \begin{equation} |S_N f_0 (x)- f_0(x)|\le \frac \epsilon 4\, . \end{equation}
- id `r647`: lemma. Let $0<r<1$. Let $N$ be the smallest integer larger than $\frac 1r$. There is a $2\pi$-periodic continuous function ${L'}$ on $\R$ that satisfies for all $0\le x\le 2\pi$ and all $2\pi$-periodic bounded measurable functions $f$ on $\R$ \begin{equation} L_Nf(x)=\frac 1{2\pi}\int_{0}^{2\pi}f(y) {L'}(x-y)\, dy\,. \end{equation} Moreover, for all $-\pi \le x \le \pi$, \begin{equation} \left|L'(x)-\mathbf{1}_{\{y:\, r<|y|<1\}} \kappa(x)\right|\le 12 k_r(x)\, . \end{equation}
- id `r596`: lemma. Let $f$ be a bounded measurable function on $\R$. Then $Tf$ as defined in `r435` is measurable.
- id `r886`: lemma. For every $R > 0$ and $x \in X$, the function $d_{B(x,R)}$ is a metric on $\Mf$.
- id `r645`: lemma. For any $x, x' \in X$ and $R, R' > 0$ with $B(x,R) \subset B(x, R')$, and for any $n, m \in \mathbb{Z}$ $$ d_{B(x,R)}(\mfa_n, \mfa_m) \le d_{B(x',R')}(\mfa_n, \mfa_m)\,. $$
- id `r340`: lemma. Let $0<r$. Let $f$ be a bounded, measurable function on $\mathbb{R}$. Then \begin{equation} \|H_rf\|_{2}\leq 2^{9} \|f\|_2, \end{equation} where \begin{equation} H_r f(x) := T_r f(x) = \int_{r\le |x-y|} \kappa(x-y) f(y) \, dy \end{equation}
- id `r166`: lemma. Let $f$ and $g$ be two bounded non-negative measurable $2\pi$-periodic functions on $\R$. Then \begin{equation} \left(\int_0^{2\pi} \left(\int_0^{2\pi} f(y)g(x-y)\, dy\right)^2\, dx\right)^{\frac 12}\le \|f\|_{L^2[0, 2\pi]} \|g\|_{L^1[0, 2\pi]}\, . \end{equation}
- id `r842`: lemma. Let $g:\R\to\C$ be a measurable $2\pi$-periodic function such that for some $\delta>0$ and every $x\in\R$, \begin{equation} |g(x)|\le \delta \,. \end{equation} Then for every $x\in [0,2\pi]$ and $N>0$, \begin{equation*} |S_N g(x)| \le \frac{1}{2\pi} (Tg(x) + T\bar{g}(x)) + \pi\delta. \end{equation*}
- id `r141`: lemma. Let $\alpha\le\beta$ be real numbers. Let $g:\R\to \C$ be a measurable function and assume \begin{equation} \|g\|_{Lip(\alpha,\beta)}:=\sup_{\alpha\le x\le \beta}|g(x)|+\frac{|\beta-\alpha|}{2} \sup_{\alpha\le x<y\le \beta} \frac {|g(y)-g(x)|}{|y-x|}<\infty\, . \end{equation} Then for any $\alpha \le \beta$ and $n\in\Z$ we have \begin{equation} \int _{\alpha}^{\beta} g(x) e^{inx}\, dx\le 2\pi |\beta-\alpha|\|g\|_{Lip(\alpha,\beta)}(1+|n||\beta-\alpha|)^{-1}\, . \end{equation}

## Constraints

- `r118` before `r842`
- `r141` before `r660`
- `r166` before `r318`
- `r198` before `r435`
- `r198` before `r660`
- `r198` before `r901`
- `r198` before `r930`
- `r238` before `r647`
- `r238` before `r842`
- `r260` before `r118`
- `r260` before `r318`
- `r260` before `r372`
- `r260` before `r488`
- `r260` before `r647`
- `r305` before `r957`
- `r318` before `r340`
- `r340` before `r435`
- `r340` before `r901`
- `r340` before `r930`
- `r372` before `r435`
- `r372` before `r596`
- `r372` before `r842`
- `r372` before `r901`
- `r372` before `r930`
- `r388` before `r435`
- `r388` before `r660`
- `r388` before `r901`
- `r388` before `r930`
- `r447` before `r340`
- `r447` before `r435`
- `r447` before `r647`
- `r447` before `r660`
- `r447` before `r901`
- `r447` before `r930`
- `r488` before `r435`
- `r488` before `r901`
- `r488` before `r930`
- `r539` before `r435`
- `r539` before `r660`
- `r539` before `r901`
- `r539` before `r930`
- `r596` before `r901`
- `r596` before `r930`
- `r645` before `r435`
- `r645` before `r660`
- `r645` before `r901`
- `r645` before `r930`
- `r647` before `r340`
- `r660` before `r435`
- `r660` before `r901`
- `r660` before `r930`
- `r676` before `r435`
- `r676` before `r660`
- `r676` before `r901`
- `r676` before `r930`
- `r790` before `r978`
- `r803` before `r957`
- `r842` before `r901`
- `r842` before `r930`
- `r886` before `r198`
- `r886` before `r388`
- `r886` before `r435`
- `r886` before `r539`
- `r886` before `r645`
- `r886` before `r660`
- `r886` before `r676`
- `r886` before `r901`
- `r886` before `r930`
- `r930` before `r957`
- `r978` before `r340`
