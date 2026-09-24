You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `r772`: lemma. Let $\fu \in \fU$. Then we have for all $f, g$ bounded with bounded support $$ \Bigg|\int_X \sum_{\fp \in \fT(\fu)} \bar g(y) T_{\fp}f(y) \, \mathrm{d}\mu(y) \Bigg| $$ \begin{equation} \le 2^{130a^3}\|P_{\mathcal{J}(\fT(\fu))}|f|\|_{2}\|P_{\mathcal{L}(\fT(\fu))}|g|\|_{2}. \end{equation}
- id `r379`: lemma. We have for all bounded $f$ with bounded support $$ \|P_{\mathcal{J}'}|T_{\fT(\fu_2) \setminus \mathfrak{S}}^* g_2|\|_2 \le 2^{102a^3+21a+5} 2^{-\frac{25}{101a}Zn\kappa} \|\mathbf{1}_{\scI(\fu_1)} M_{\mathcal{B},1} |g_2|\|_2 $$
- id `r763`: lemma. Let $\fu \in \fU$ and $L \in \mathcal{L}(\fT(\fu))$. Then \begin{equation} \mu(L \cap G \cap \bigcup_{\fp \in \fT(\fu)} E(\fp)) \le 2^{101a^3} \dens_1(\fT(\fu)) \mu(L)\,. \end{equation}
- id `r828`: lemma. Let $\fu \in \fU$. Then for all bounded $f$ with bounded support and bounded $g$ supported on $G$ we have \begin{equation} \left|\int_X \bar g \sum_{\fp \in \fT(\fu)} T_{\fp }f \, \mathrm{d}\mu \right| \le 2^{181a^3} \dens_1(\fT(\fu))^{1/2} \|f\|_2\|g\|_2\,. \end{equation} If additionally $\text{support}(f) \subseteq F$, then we have \begin{equation} \left| \int_X \bar g \sum_{\fp \in \fT(\fu)} T_{\fp }f\, \mathrm{d}\mu \right| \le 2^{282a^3} \dens_1(\fT(\fu))^{1/2} \dens_2(\fT(\fu))^{1/2} \|f\|_2\|g\|_2\,. \end{equation}
- id `r401`: lemma. For every cube $I \in \mathcal{D}$, there exist at most $2^{9a}$ cubes $J \in \mathcal{D}$ with $s(J) = s(I)$ and $B(c(I), 16D^{s(I)}) \cap B(c(J), 16 D^{s(J)}) \ne \emptyset$.
- id `r565`: lemma. We have for all $\fu \in \fU$ and all bounded $g$ supported on $G$ $$ \|S_{2, \fu} g\|_2 \le 2^{182a^3} \|g\|_2\,. $$
- id `r819`: lemma. If $\fp \in \fT(\fu_2) \setminus \mathfrak{S}$ and $J \in \mathcal{J'}$ with $B(\scI(\fp)) \cap B(J) \ne \emptyset$, then $$ \ps(\fp) \le s(J) + 2 - \frac{Zn}{202a^3}\,. $$
- id `r429`: lemma. Let $\fu \in \fU$ and $\fp \in \fT(\fu)$. Then for all $y, y' \in X$ and all bounded $g$ with bounded support, we have $$ |e(\fcc(\fu)(y)) T_{\fp}^* g(y) - e(\fcc(\fu)(y')) T_{\fp}^* g(y')| $$ \begin{equation} \le \frac{2^{128a^3}}{\mu(B(\pc(\fp), 4D^{\ps(\fp)}))} \left(\frac{\rho(y, y')}{D^{\ps(\fp)}}\right)^{1/a} \int_{E(\fp)} |g(x)| \, \mathrm{d}\mu(x)\,. \end{equation}
- id `r608`: lemma. For all $J \in \mathcal{J}'$, we have that $$ d_{B(J)}(\fcc(\fu_1), \fcc(\fu_2)) \ge 2^{-201a^3} 2^{Zn/2}\,. $$
- id `r585`: lemma. Let $\fC_1 = \fT(\fu_1)$ and $\fC_2 = \fT(\fu_2) \cap \mathfrak{S}$. Then for $i = 1,2$ and each $J \in \mathcal{J}'$ and all bounded $g$ with bounded support, we have \begin{align} \sup_{B'(J)} |T_{\fC_i}^*g| \leq \inf_{B^\circ{}(J)} |T^*_{\fC_i} g| + 2^{128a^3+4a+3} \inf_{J} M_{\mathcal{B}, 1} |g| \end{align} and for all $y,y' \in B'(J)$ $$ |e(\fcc(\fu_i)(y)) T_{\fC_i}^* g(y) - e(\fcc(\fu_i)(y')) T_{\fC_i}^* g(y')| $$ \begin{equation} \le 2^{128a^3+4a+1} \left(\frac{\rho(y,y')}{D^{s(J)}}\right)^{1/a} \inf_J M_{\mathcal{B},1} |g|\,. \end{equation}
- id `r216`: lemma. For each $\fp \in \fP$, we have $$ T_{\fp}^* g = \mathbf{1}_{B(\pc(\fp), 5D^{\ps(\fp)})} T_{\fp}^* \mathbf{1}_{\scI(\fp)} g\,. $$ For each $\fu \in \fU$ and each $\fp \in \fT(\fu)$, we have $$ T_{\fp}^* g = \mathbf{1}_{\scI(\fu)} T_{\fp}^* \mathbf{1}_{\scI(\fu)} g\,. $$
- id `r124`: lemma. For all $\fu \in \fU$, all $L \in \mathcal{L}(\fT(\fu))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have $$ [another result] \le 10 \cdot 2^{104a^3} M_{\mathcal{B}, 1}P_{\mathcal{J}(\fT(\fu))}|f|(x')\,. $$
- id `r419`: lemma. For all $\fu \in \fU$, all $L \in \mathcal{L}(\fT(\fu))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have $$ \Bigg| \sum_{s \in \sigma(\fu, x)} \int K_s(x,y) P_{\mathcal{J}(\fT(\fu))} f(y) \, \mathrm{d}\mu(y) \Bigg| \le T_{\mathcal{N}}^{\fcc(\fu)} P_{\mathcal{J}(\fT(\fu))} f(x')\,. $$
- id `r495`: lemma. For any $\fu_1 \ne \fu_2 \in \fU$ and all bounded $g_1, g_2$ with bounded support, we have \begin{equation} \left| \int_X \sum_{\fp_1 \in \fT(\fu_1)} \sum_{\fp_2 \in \fT(\fu_2)} T^*_{\fp_1}g_1 \overline{T^*_{\fp_2}g_2 }\,\mathrm{d}\mu \right| \end{equation} \begin{equation} \le 2^{512a^3-4n} \prod_{j =1}^2 \| S_{2, \fu_j} g_j\|_{L^2(\scI(\fu_1) \cap \scI(\fu_2))}\,. \end{equation}
- id `r451`: lemma. Let $\fu \in \fU$ and $J \in \mathcal{J}(\fT(\fu))$. Then $$ \mu(F \cap J) \le 2^{201a^3} \dens_2(\fT(\fu)) \mu(J)\,. $$
- id `r531`: lemma. For all $1 \le j,j' \le 2^n$ with $j\ne j'$ and for all bounded $g_1, g_2$ supported on $G$, it holds that $$ \left| \int T_{\mathfrak{R}_j}^*g_1 \overline{T_{\mathfrak{R}_{j'}}^*g_2} \, \mathrm{d}\mu \right| \le 2^{876a^3-4n}\|g_1\|_2 \|g_2\|_2\,. $$
- id `r915`: lemma. For all bounded $g$ supported on $G$ we have that $$ \left\| \sum_{\fp \in \fT(\fu)} T_{\fp}^* g\right\|_2 \le 2^{181a^3} \dens_1(\fT(\fu))^{1/2} \|g\|_2\,, $$ $$ \left\| \mathbf{1}_F \sum_{\fp \in \fT(\fu)} T_{\fp}^* g\right\|_2 \le 2^{282a^3} \dens_1(\fT(\fu))^{1/2} \dens_2(\fT(\fu))^{1/2} \|g\|_2\,. $$
- id `r292`: lemma. For each $1 \le j \le 2^n$ and each bounded $g$ supported on $G$ we have \begin{equation} \left\| T_{\mathfrak{R}_j}^*g \right\|_2 \le 2^{182a^3} 2^{-n/2} \|g\|_2 \end{equation} and \begin{equation} \left\| \mathbf{1}_F T_{\mathfrak{R}_j}^*g \right\|_2 \le 2^{283a^3} 2^{-n/2} \dens_2(\bigcup_{\fu\in \fU}\fT(\fu))^{1/2} \|g\|_2\,. \end{equation}
- id `r364`: lemma. Let $\fu_1 \ne \fu_2 \in \fU$ with $\scI(\fu_1) \subset \scI(\fu_2)$. If $\fp \in \fT(\fu_1) \cup \fT(\fu_2)$ with $\scI(\fp) \cap \scI(\fu_1) \ne \emptyset$, then $\fp \in \mathfrak{S}$. In particular, we have $\fT(\fu_1) \subset \mathfrak{S}$.
- id `r211`: lemma. We have for all $J \in \mathcal{J}'$ that \begin{equation} \|h_J\|_{C^{\tau}(B(c(J), 16D^{s(J)}))} \le 2^{485a^3} \prod_{j = 1,2} (\inf_{B(c(J), \frac{1}{8}D^{s(J)})} |T_{\fT(\fu_j)}^* g_j| + \inf_J M_{\mathcal{B}, 1} |g_j|)\,. \end{equation}
- id `r359`: lemma. We have $$ \scI(\fu_1) = \dot{\bigcup_{J \in \mathcal{J}'}} J\,. $$
- id `r847`: lemma. For all $\fu \in \fU$ and all bounded functions $f$ with bounded support \begin{equation} \|S_{1,\fu}f\|_2 \le 2^{12a} \|f\|_2\,. \end{equation}
- id `r622`: lemma. The sets $E_j$, $1 \le j \le 2^n$ are pairwise disjoint.
- id `r314`: lemma. Let $\fu \in \fU$ and $L \in \mathcal{L}(\fT(\fu))$. Let $x, x' \in L$. Then for all bounded functions $f$ with bounded support $$ \left|\sum_{\fp \in \fT(\fu)} T_{\fp}[ e(-\fcc(\fu))f](x)\right| $$ \begin{equation} \leq 2^{129a^3}(M_{\mathcal{B},1}+S_{1,\fu})P_{\mathcal{J}(\fT(\fu))}|f|(x')+|T_{\mathcal{N}}^{\fcc(\fu)} P_{\mathcal{J}(\fT(\fu))}f(x')|, \end{equation}
- id `r720`: lemma. Let $\fC = \fT(\fu_1)$ or $\fC = \fT(\fu_2) \cap \mathfrak{S}$. Then for each $J \in \mathcal{J}'$ and $\fp \in \fC$ with $B(\scI(\fp)) \cap B'(J) \neq \emptyset$, we have $\ps(\fp) \ge s(J)$.
- id `r542`: lemma. We have for all $\fu_1 \ne \fu_2 \in \fU$ with $\scI(\fu_1) \subset \scI(\fu_2)$ and all bounded $g_1, g_2$ with bounded support \begin{equation} \left| \int_X \sum_{\fp_1 \in \fT(\fu_1)} \sum_{\fp_2 \in \fT(\fu_2) \setminus \mathfrak{S}} T^*_{\fp_1}g_1 \overline{T^*_{\fp_2}g_2 }\,\mathrm{d}\mu \right| \end{equation} \begin{equation} \le 2^{232a^3+21a+5} 2^{-\frac{25}{101a}Zn\kappa} \prod_{j=1}^2 \|S_{2, \fu_j} g_j\|_{L^2(\scI(\fu_1))}\,. \end{equation}
- id `r936`: lemma. We have for all $\fu_1 \ne \fu_2 \in \fU$ with $\scI(\fu_1) \subset \scI(\fu_2)$ and all bounded $g_1, g_2$ with bounded support \begin{equation} \left| \int_X \sum_{\fp_1 \in \fT(\fu_1)} \sum_{\fp_2 \in \fT(\fu_2) \cap \mathfrak{S}} T^*_{\fp_1}g_1 \overline{T^*_{\fp_2}g_2 }\,\mathrm{d}\mu \right| \end{equation} \begin{equation} \le 2^{511a^3} 2^{-Zn/(4a^2 + 2a^3)} \prod_{j =1}^2 \| S_{2, \fu_j} g_j\|_{L^2(\scI(\fu_1))}\,. \end{equation}
- id `r121`: lemma. For all $\fu \in \fU$, all $L \in \mathcal{L}(\fT(\fu))$, all $x, x' \in L$ and all bounded $f$ with bounded support, we have \begin{equation*} \Bigg| \sum_{s \in \sigma(\fu, x)} \int K_s(x,y) (f(y) - P_{\mathcal{J}(\fT(\fu))} f(y)) \, \mathrm{d}\mu(y) \Bigg| \end{equation*} \begin{equation*} \le 2^{128a^3} S_{1,\fu} P_{\mathcal{J}(\fT(\fu))}|f|(x')\,. \end{equation*}
- id `r330`: lemma. We have that $$ \scI(\fu_1) = \dot{\bigcup_{J \in \mathcal{J}'}} J\,. $$
- id `r118`: lemma. For all bounded $f$ with bounded support and all $\mfa \in \Mf$ $$ \|T_{\mathcal{N}}^{\mfa} f\|_2 \le 2^{102a^3} \|f\|_2\,. $$
- id `r506`: lemma. Let $\fp \in \fT(\fu_2) \setminus \mathfrak{S}$, $J \in \mathcal{J}'$ and suppose that $$ B(\scI(\fp)) \cap B^\circ(J) \ne \emptyset\,. $$ Then $$ s(J) \le \ps(\fp) \le s(J) +3\,. $$
- id `r249`: lemma. For each $\mathfrak{S} \subset \fP$, we have \begin{equation} \bigcup_{I \in \mathcal{D}} I = \dot{\bigcup_{J \in \mathcal{J}(\mathfrak{S})}} J \end{equation} and \begin{equation} \bigcup_{I \in \mathcal{D}} I = \dot{\bigcup_{L \in \mathcal{L}(\mathfrak{S})}} L\,. \end{equation}
- id `r136`: lemma. We have for all $J \in \mathcal{J}'$ and all bounded $g$ with bounded support $$ \sup_{B'(J)} |T^*_{\fT(\fu_2) \cap \mathfrak{S}} g| \le \inf_{B^\circ{}(J)} |T^*_{\fT(\fu_2)} g| + 2^{129a^3} \inf_{J} M_{\mathcal{B},1}|g|\,. $$
- id `r836`: lemma. There exists a family of functions $\chi_J$, $J \in \mathcal{J}'$ such that \begin{equation} \mathbf{1}_{\scI(\fu_1)} = \sum_{J \in \mathcal{J}'} \chi_J\,, \end{equation} and for all $J \in \mathcal{J}'$ and all $y,y' \in \scI(\fu_1)$ \begin{equation} 0 \leq \chi_J(y) \leq \mathbf{1}_{B(J)}(y)\,, \end{equation} \begin{equation} |\chi_J(y) - \chi_J(y')| \le 2^{227a^3} \frac{\rho(y,y')}{D^{s(J)}}\,. \end{equation}
- id `r264`: lemma. Let $(\fU, \fT)$ be an $n$-forest. Then there exists a decomposition $$ \fU = \dot{\bigcup_{1 \le j \le 2^n}} \fU_j $$ such that for all $j = 1, \dotsc, 2^n$ the pair $(\fU_j, \fT|_{\fU_j})$ is an $n$-row.
- id `r556`: lemma. For each $J \in \mathcal{J}'$ and all $s$, we have $$ \frac{1}{\mu(J)} \int_J \Bigg(\sum_{\substack{I \in \mathcal{D}, s(I) = s(J) - s\\ I \cap \scI(\fu_1) = \emptyset\\ J \cap B(I) \ne \emptyset}} \mathbf{1}_{B(I)}\bigg)^2 \, \mathrm{d}\mu \le 2^{14a+1} (8 D^{-s})^\kappa\,. $$
- id `r821`: lemma. For each $\fu \in \fU$, we have $$ \sigma(\fu, x) = \mathbb{Z} \cap [\underline{\sigma} (\fu, x), \overline{\sigma} (\fu, x)]\,. $$
- id `r618`: lemma. If $J, J' \in \mathcal{J'}$ with $$ B(J) \cap B(J') \ne \emptyset\,, $$ then $|s(J) - s(J')| \le 1$.
- id `r794`: lemma. For all $J \in \mathcal{J}'$ and all bounded $g$ with bounded support $$ \sup_{B^\circ{}(J)} |T_{\mathfrak{T}(\mathfrak{u}_2)\setminus\mathfrak{S}}^* g| \le 2^{104a^3} \inf_J M_{\mathcal{B},1}|g| $$

## Constraints

- `r118` before `r772`
- `r121` before `r314`
- `r124` before `r314`
- `r136` before `r211`
- `r211` before `r936`
- `r216` before `r211`
- `r216` before `r292`
- `r216` before `r379`
- `r216` before `r429`
- `r216` before `r495`
- `r216` before `r542`
- `r216` before `r585`
- `r216` before `r794`
- `r216` before `r936`
- `r249` before `r121`
- `r249` before `r124`
- `r249` before `r330`
- `r249` before `r359`
- `r249` before `r542`
- `r249` before `r772`
- `r249` before `r828`
- `r249` before `r847`
- `r264` before `r292`
- `r264` before `r531`
- `r264` before `r622`
- `r314` before `r772`
- `r330` before `r836`
- `r330` before `r936`
- `r359` before `r379`
- `r359` before `r542`
- `r364` before `r330`
- `r364` before `r379`
- `r364` before `r506`
- `r364` before `r608`
- `r364` before `r720`
- `r379` before `r542`
- `r401` before `r847`
- `r419` before `r314`
- `r429` before `r585`
- `r451` before `r828`
- `r495` before `r531`
- `r506` before `r794`
- `r542` before `r495`
- `r556` before `r379`
- `r565` before `r531`
- `r585` before `r136`
- `r585` before `r211`
- `r608` before `r936`
- `r618` before `r836`
- `r720` before `r585`
- `r763` before `r828`
- `r772` before `r542`
- `r772` before `r828`
- `r794` before `r136`
- `r819` before `r379`
- `r821` before `r419`
- `r828` before `r915`
- `r836` before `r211`
- `r836` before `r936`
- `r847` before `r772`
- `r915` before `r292`
- `r915` before `r565`
- `r936` before `r495`
