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

- id `r982`: lemma; steps here: state and prove. If $f$ is injective, then $\rho(X|f(Y))=\rho(X|Y)$.
- id `r362`: corollary; steps here: state and prove. If $|A+A| \leq K|A|$, then there exist a subgroup $H$ and a subset $c$ of $G$ with $A \subseteq c + H$, such that $|c| \leq K^{5} |A|^{1/2}/|H|^{1/2}$ and $|H|/|A|\in[K^{-8},K^8]$.
- id `r236`: definition; steps here: state only (no proof needed). For any $G$-valued random variable $X$, we define $\rho^-(X)$ to be the infimum of $D_{KL}(X \Vert U_A + T)$, where $U_A$ is uniform on $A$ and $T$ ranges over $G$-valued random variables independent of $U_A$.
- id `r769`: lemma; steps here: state and prove. $d[X_1;X_1]+d[X_2;X_2]= 2d[X_1;X_2]+(I_2-I_1)$.
- id `r633`: proposition; steps here: state and prove. If $X_1,X_2$ is a $\phi$-minimizer, then $d[X_1;X_2] = 0$.
- id `r936`: lemma; steps here: state and prove. If $X,Y$ are independent, then $$ \rho(X | X+Y) \leq \frac{1}{2}(\rho(X)+\rho(Y) + d[X;Y]).$$
- id `r766`: proposition; steps here: state and prove. For any random variables $Y_1,Y_2$, there exist a subgroup $H$ such that $$ 2\rho(U_H) \leq \rho(Y_1) + \rho(Y_2) + 8 d[Y_1;Y_2].$$
- id `r760`: lemma; steps here: state and prove. For any $s \in G$, $\rho(X+s) = \rho(X)$.
- id `r455`: lemma; steps here: state and prove. If $X, Y$ are independent $G$-valued random variables, and $Z$ is another random variable defined on the same sample space as $X$, then $$D_{KL}((X|Z)\Vert Y) = D_{KL}(X\Vert Y) + \bbH[X] - \bbH[X|Z].$$
- id `r217`: lemma; steps here: state and prove. If $X'$ is a copy of $X$, and $Y'$ is a copy of $Y$, then $D_{KL}(X'\Vert Y') = D_{KL}(X\Vert Y)$.
- id `r992`: lemma; steps here: state and prove. $D_{KL}(X\Vert Y) \geq 0$.
- id `r258`: lemma; steps here: state and prove. If $H$ is a finite subgroup of $G$, then $\rho^-(U_H) = \log |A| - \log \max_t |A \cap (H+t)|$.
- id `r385`: lemma; steps here: state and prove. If $H$ is a finite subgroup of $G$, and $\rho(U_H) \leq r$, then there exists $t$ such that $|A \cap (H+t)| \geq e^{-r} \sqrt{|A||H|}$, and $|H|/|A|\in[e^{-2r},e^{2r}]$.
- id `r971`: lemma; steps here: state and prove. If $S$ is a finite set, $\sum_{s \in S} w_s = 1$ for some non-negative $w_s$, and ${\bf P}(X=x) = \sum_{s\in S} w_s {\bf P}(X_s=x)$, ${\bf P}(Y=x) = \sum_{s\in S} w_s {\bf P}(Y_s=x)$ for all $x$, then $$D_{KL}(X\Vert Y) \le \sum_{s\in S} w_s D_{KL}(X_s\Vert Y_s).$$
- id `r119`: lemma; steps here: state and prove. $I_2\le 2\eta d[X_1;X_2] + \frac{\eta}{1-\eta}(2\eta d[X_1;X_2]-I_1)$.
- id `r143`: lemma; steps here: state and prove. If $X,Y$ are independent, one has $$ \rho^-(X+Y) \leq \rho^-(X)$$ $$ \rho^+(X+Y) \leq \rho^+(X) + \bbH[X+Y] - \bbH[X]$$ and $$ \rho(X+Y) \leq \rho(X) + \frac{1}{2}( \bbH[X+Y] - \bbH[X] ).$$
- id `r141`: definition; steps here: state only (no proof needed). We define $\rho(X|Y) := \sum_y {\bf P}(Y=y) \rho(X|Y=y)$.
- id `r310`: lemma; steps here: state and prove. For independent random variables $Y_1,Y_2,Y_3,Y_4$ over $G$, define $S:=Y_1+Y_2+Y_3+Y_4$, $T_1:=Y_1+Y_2$, $T_2:=Y_1+Y_3$. Then $$\rho(T_1|T_2,S)+\rho(T_2|T_1,S) - \frac{1}{2}\sum_{i} \rho(Y_i)\le \frac{1}{2}(d[Y_1;Y_2]+d[Y_3;Y_4]+d[Y_1;Y_3]+d[Y_2;Y_4]).$$
- id `r797`: lemma; steps here: state and prove. If $D_{KL}(X\Vert Y) = 0$, then $Y$ is a copy of $X$.
- id `r365`: lemma; steps here: state and prove. For any $s\in G$, $\rho(X+s|Y)=\rho(X|Y)$.
- id `r671`: lemma; steps here: state and prove. $\rho(X)$ depends continuously on the distribution of $X$.
- id `r422`: lemma; steps here: state and prove. If $G$-valued random variables $T_1,T_2,T_3$ satisfy $T_1+T_2+T_3=0$, then $$d[X_1;X_2]\le 3\bbI[T_1:T_2] + (2\bbH[T_3]-\bbH[T_1]-\bbH[T_2])+ \eta(\rho(T_1|T_3)+\rho(T_2|T_3)-\rho(X_1)-\rho(X_2)).$$
- id `r475`: definition; steps here: state only (no proof needed). Given $G$-valued random variables $X,Y$, define $$ \phi[X;Y] := d[X;Y] + \eta(\rho(X) + \rho(Y))$$ and define a \emph{$\phi$-minimizer} to be a pair of random variables $X,Y$ which minimizes $\phi[X;Y]$.
- id `r681`: lemma; steps here: state and prove. If $X,Y$ are independent, then $$ \rho(X+Y) \leq \frac{1}{2}(\rho(X)+\rho(Y) + d[X;Y]).$$
- id `r969`: theorem; steps here: state and prove. If $A \subset {\bf F}_2^n$ is finite non-empty with $|A+A| \leq K|A|$, then there exists a subgroup $H$ of ${\bf F}_2^n$ with $|H| \leq |A|$ such that $A$ can be covered by at most $2K^9$ translates of $H$.
- id `r966`: lemma; steps here: state and prove. If $X, Y, Z$ are independent $G$-valued random variables, then $$D_{KL}(X+Z\Vert Y+Z) \leq D_{KL}(X\Vert Y).$$
- id `r867`: lemma; steps here: state and prove. For independent random variables $Y_1,Y_2,Y_3,Y_4$ over $G$, define $T_1:=Y_1+Y_2,T_2:=Y_1+Y_3,T_3:=Y_2+Y_3$ and $S:=Y_1+Y_2+Y_3+Y_4$. Then $$\sum_{1 \leq i<j \leq 3} (\rho(T_i|T_j,S) + \rho(T_j|T_i,S) - \frac{1}{2}\sum_{i} \rho(Y_i))\le \sum_{1\leq i < j \leq 4}d[Y_i;Y_j]$$
- id `r818`: definition; steps here: state only (no proof needed). For any $G$-valued random variable $X$, we define $\rho^+(X) := \rho^-(X) + \bbH(X) - \bbH(U_A)$.
- id `r722`: definition; steps here: state only (no proof needed). We define $\rho(X) := (\rho^+(X) + \rho^-(X))/2$.
- id `r771`: lemma; steps here: state and prove. If $X,Z$ are defined on the same space, one has $$ \rho^-(X|Z) \leq \rho^-(X) + \bbH[X] - \bbH[X|Z]$$ $$ \rho^+(X|Z) \leq \rho^+(X)$$ and $$ \rho(X|Z) \leq \rho(X) + \frac{1}{2}( \bbH[X] - \bbH[X|Z] ).$$
- id `r606`: lemma; steps here: state and prove. If $G$-valued random variables $T_1,T_2,T_3$ satisfy $T_1+T_2+T_3=0$, then $$d[X_1;X_2] \leq \sum_{1 \leq i<j \leq 3} \bbI[T_i:T_j] + \frac{\eta}{3} \sum_{1 \leq i<j \leq 3} (\rho(T_i|T_j) + \rho(T_j|T_i) -\rho(X_1)-\rho(X_2))$$
- id `r829`: lemma; steps here: state and prove. There exists a $\phi$-minimizer.
- id `r759`: definition; steps here: state only (no proof needed). If $X,Y$ are two $G$-valued random variables, the Kullback--Leibler divergence is defined as $$ D_{KL}(X\Vert Y) := \sum_x \mathbf{P}(X=x) \log \frac{\mathbf{P}(X=x)}{\mathbf{P}(Y=x)}.$$
- id `r569`: lemma; steps here: state and prove. $D_{KL}((X|W)\Vert Y) \geq 0$.
- id `r755`: lemma; steps here: state and prove. If $f:G \to H$ is an injection, then $D_{KL}(f(X)\Vert f(Y)) = D_{KL}(X\Vert Y)$.
- id `r545`: corollary; steps here: state and prove. If $|A+A| \leq K|A|$, then there exists a subgroup $H$ and $t\in G$ such that $|A \cap (H+t)| \geq K^{-4} \sqrt{|A||H|}$, and $|H|/|A|\in[K^{-8},K^8]$.
- id `r481`: corollary; steps here: state and prove. If $H$ is a finite subgroup of $G$, then $\rho^+(U_H) = \log |H| - \log \max_t |A \cap (H+t)|$.
- id `r650`: lemma; steps here: state and prove. $I_1\le 2\eta d[X_1;X_2]$

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r119` before `P:r633`
- `S:r141` before `P:r119`
- `S:r141` before `P:r633`
- `S:r141` before `P:r650`
- `S:r141` before `S:r310`
- `S:r141` before `S:r365`
- `S:r141` before `S:r422`
- `S:r141` before `S:r606`
- `S:r141` before `S:r771`
- `S:r141` before `S:r867`
- `S:r141` before `S:r936`
- `S:r141` before `S:r982`
- `S:r143` before `P:r681`
- `S:r143` before `P:r760`
- `S:r217` before `P:r119`
- `S:r217` before `P:r143`
- `S:r217` before `P:r310`
- `S:r217` before `P:r422`
- `S:r217` before `P:r633`
- `S:r217` before `P:r650`
- `S:r217` before `P:r766`
- `S:r217` before `P:r829`
- `S:r217` before `P:r936`
- `S:r236` before `P:r119`
- `S:r236` before `P:r310`
- `S:r236` before `P:r422`
- `S:r236` before `P:r481`
- `S:r236` before `P:r545`
- `S:r236` before `P:r633`
- `S:r236` before `P:r650`
- `S:r236` before `P:r671`
- `S:r236` before `P:r766`
- `S:r236` before `P:r829`
- `S:r236` before `P:r936`
- `S:r236` before `S:r143`
- `S:r236` before `S:r258`
- `S:r236` before `S:r385`
- `S:r236` before `S:r722`
- `S:r236` before `S:r771`
- `S:r236` before `S:r818`
- `S:r258` before `P:r385`
- `S:r258` before `P:r481`
- `S:r310` before `P:r867`
- `S:r362` before `P:r969`
- `S:r385` before `P:r545`
- `S:r422` before `P:r606`
- `S:r422` before `P:r633`
- `S:r455` before `P:r771`
- `S:r475` before `P:r766`
- `S:r475` before `S:r119`
- `S:r475` before `S:r422`
- `S:r475` before `S:r606`
- `S:r475` before `S:r633`
- `S:r475` before `S:r650`
- `S:r475` before `S:r829`
- `S:r481` before `P:r385`
- `S:r545` before `P:r362`
- `S:r633` before `P:r766`
- `S:r650` before `P:r633`
- `S:r671` before `P:r766`
- `S:r671` before `P:r829`
- `S:r681` before `P:r119`
- `S:r681` before `P:r310`
- `S:r681` before `P:r650`
- `S:r722` before `P:r119`
- `S:r722` before `P:r365`
- `S:r722` before `P:r545`
- `S:r722` before `P:r633`
- `S:r722` before `P:r650`
- `S:r722` before `P:r829`
- `S:r722` before `P:r982`
- `S:r722` before `S:r141`
- `S:r722` before `S:r143`
- `S:r722` before `S:r310`
- `S:r722` before `S:r385`
- `S:r722` before `S:r422`
- `S:r722` before `S:r475`
- `S:r722` before `S:r606`
- `S:r722` before `S:r671`
- `S:r722` before `S:r681`
- `S:r722` before `S:r760`
- `S:r722` before `S:r766`
- `S:r722` before `S:r771`
- `S:r722` before `S:r867`
- `S:r722` before `S:r936`
- `S:r755` before `P:r966`
- `S:r759` before `P:r119`
- `S:r759` before `P:r143`
- `S:r759` before `P:r258`
- `S:r759` before `P:r310`
- `S:r759` before `P:r385`
- `S:r759` before `P:r422`
- `S:r759` before `P:r545`
- `S:r759` before `P:r633`
- `S:r759` before `P:r650`
- `S:r759` before `P:r671`
- `S:r759` before `P:r766`
- `S:r759` before `P:r771`
- `S:r759` before `P:r829`
- `S:r759` before `P:r936`
- `S:r759` before `S:r217`
- `S:r759` before `S:r236`
- `S:r759` before `S:r455`
- `S:r759` before `S:r569`
- `S:r759` before `S:r755`
- `S:r759` before `S:r797`
- `S:r759` before `S:r966`
- `S:r759` before `S:r971`
- `S:r759` before `S:r992`
- `S:r760` before `P:r365`
- `S:r760` before `P:r766`
- `S:r760` before `P:r936`
- `S:r766` before `P:r545`
- `S:r769` before `P:r119`
- `S:r769` before `P:r633`
- `S:r771` before `P:r310`
- `S:r771` before `P:r936`
- `S:r818` before `P:r119`
- `S:r818` before `P:r310`
- `S:r818` before `P:r385`
- `S:r818` before `P:r422`
- `S:r818` before `P:r545`
- `S:r818` before `P:r633`
- `S:r818` before `P:r650`
- `S:r818` before `P:r671`
- `S:r818` before `P:r766`
- `S:r818` before `P:r829`
- `S:r818` before `P:r936`
- `S:r818` before `S:r143`
- `S:r818` before `S:r481`
- `S:r818` before `S:r722`
- `S:r818` before `S:r771`
- `S:r829` before `P:r766`
- `S:r867` before `P:r633`
- `S:r936` before `P:r119`
- `S:r936` before `P:r310`
- `S:r936` before `P:r650`
- `S:r966` before `P:r143`
- `S:r971` before `P:r966`
- `S:r982` before `P:r310`
- `S:r992` before `P:r143`
- `S:r992` before `P:r258`
- `S:r992` before `P:r385`
- `S:r992` before `P:r545`
- `S:r992` before `P:r569`
- `S:r992` before `P:r671`
- `S:r992` before `P:r771`
