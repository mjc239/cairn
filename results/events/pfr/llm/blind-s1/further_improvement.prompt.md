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

- id `r988`: theorem; steps here: state and prove. If $A \subset {\bf F}_2^n$ is finite non-empty with $|A+A| \leq K|A|$, then there exists a subgroup $H$ of ${\bf F}_2^n$ with $|H| \leq |A|$ such that $A$ can be covered by at most $2K^9$ translates of $H$.
- id `r718`: corollary; steps here: state and prove. If $|A+A| \leq K|A|$, then there exists a subgroup $H$ and $t\in G$ such that $|A \cap (H+t)| \geq K^{-4} \sqrt{|A||H|}$, and $|H|/|A|\in[K^{-8},K^8]$.
- id `r898`: lemma; steps here: state and prove. $\rho(X)$ depends continuously on the distribution of $X$.
- id `r832`: definition; steps here: state only (no proof needed). If $X,Y$ are two $G$-valued random variables, the Kullback--Leibler divergence is defined as $$ D_{KL}(X\Vert Y) := \sum_x \mathbf{P}(X=x) \log \frac{\mathbf{P}(X=x)}{\mathbf{P}(Y=x)}.$$
- id `r600`: lemma; steps here: state and prove. If $X,Y$ are independent, then $$ \rho(X | X+Y) \leq \frac{1}{2}(\rho(X)+\rho(Y) + d[X;Y]).$$
- id `r238`: lemma; steps here: state and prove. If $G$-valued random variables $T_1,T_2,T_3$ satisfy $T_1+T_2+T_3=0$, then $$d[X_1;X_2]\le 3\bbI[T_1:T_2] + (2\bbH[T_3]-\bbH[T_1]-\bbH[T_2])+ \eta(\rho(T_1|T_3)+\rho(T_2|T_3)-\rho(X_1)-\rho(X_2)).$$
- id `r693`: lemma; steps here: state and prove. There exists a $\phi$-minimizer.
- id `r664`: definition; steps here: state only (no proof needed). For any $G$-valued random variable $X$, we define $\rho^-(X)$ to be the infimum of $D_{KL}(X \Vert U_A + T)$, where $U_A$ is uniform on $A$ and $T$ ranges over $G$-valued random variables independent of $U_A$.
- id `r888`: lemma; steps here: state and prove. If $f:G \to H$ is an injection, then $D_{KL}(f(X)\Vert f(Y)) = D_{KL}(X\Vert Y)$.
- id `r206`: lemma; steps here: state and prove. If $S$ is a finite set, $\sum_{s \in S} w_s = 1$ for some non-negative $w_s$, and ${\bf P}(X=x) = \sum_{s\in S} w_s {\bf P}(X_s=x)$, ${\bf P}(Y=x) = \sum_{s\in S} w_s {\bf P}(Y_s=x)$ for all $x$, then $$D_{KL}(X\Vert Y) \le \sum_{s\in S} w_s D_{KL}(X_s\Vert Y_s).$$
- id `r428`: lemma; steps here: state and prove. $I_1\le 2\eta d[X_1;X_2]$
- id `r140`: lemma; steps here: state and prove. $I_2\le 2\eta d[X_1;X_2] + \frac{\eta}{1-\eta}(2\eta d[X_1;X_2]-I_1)$.
- id `r516`: lemma; steps here: state and prove. If $G$-valued random variables $T_1,T_2,T_3$ satisfy $T_1+T_2+T_3=0$, then $$d[X_1;X_2] \leq \sum_{1 \leq i<j \leq 3} \bbI[T_i:T_j] + \frac{\eta}{3} \sum_{1 \leq i<j \leq 3} (\rho(T_i|T_j) + \rho(T_j|T_i) -\rho(X_1)-\rho(X_2))$$
- id `r174`: lemma; steps here: state and prove. If $H$ is a finite subgroup of $G$, and $\rho(U_H) \leq r$, then there exists $t$ such that $|A \cap (H+t)| \geq e^{-r} \sqrt{|A||H|}$, and $|H|/|A|\in[e^{-2r},e^{2r}]$.
- id `r489`: proposition; steps here: state and prove. If $X_1,X_2$ is a $\phi$-minimizer, then $d[X_1;X_2] = 0$.
- id `r986`: lemma; steps here: state and prove. For any $s\in G$, $\rho(X+s|Y)=\rho(X|Y)$.
- id `r907`: corollary; steps here: state and prove. If $|A+A| \leq K|A|$, then there exist a subgroup $H$ and a subset $c$ of $G$ with $A \subseteq c + H$, such that $|c| \leq K^{5} |A|^{1/2}/|H|^{1/2}$ and $|H|/|A|\in[K^{-8},K^8]$.
- id `r250`: lemma; steps here: state and prove. $D_{KL}(X\Vert Y) \geq 0$.
- id `r948`: lemma; steps here: state and prove. If $X, Y$ are independent $G$-valued random variables, and $Z$ is another random variable defined on the same sample space as $X$, then $$D_{KL}((X|Z)\Vert Y) = D_{KL}(X\Vert Y) + \bbH[X] - \bbH[X|Z].$$
- id `r228`: lemma; steps here: state and prove. If $X,Y$ are independent, then $$ \rho(X+Y) \leq \frac{1}{2}(\rho(X)+\rho(Y) + d[X;Y]).$$
- id `r449`: lemma; steps here: state and prove. For any $s \in G$, $\rho(X+s) = \rho(X)$.
- id `r217`: definition; steps here: state only (no proof needed). Given $G$-valued random variables $X,Y$, define $$ \phi[X;Y] := d[X;Y] + \eta(\rho(X) + \rho(Y))$$ and define a \emph{$\phi$-minimizer} to be a pair of random variables $X,Y$ which minimizes $\phi[X;Y]$.
- id `r729`: lemma; steps here: state and prove. $d[X_1;X_1]+d[X_2;X_2]= 2d[X_1;X_2]+(I_2-I_1)$.
- id `r701`: lemma; steps here: state and prove. If $H$ is a finite subgroup of $G$, then $\rho^-(U_H) = \log |A| - \log \max_t |A \cap (H+t)|$.
- id `r900`: lemma; steps here: state and prove. If $X,Y$ are independent, one has $$ \rho^-(X+Y) \leq \rho^-(X)$$ $$ \rho^+(X+Y) \leq \rho^+(X) + \bbH[X+Y] - \bbH[X]$$ and $$ \rho(X+Y) \leq \rho(X) + \frac{1}{2}( \bbH[X+Y] - \bbH[X] ).$$
- id `r487`: proposition; steps here: state and prove. For any random variables $Y_1,Y_2$, there exist a subgroup $H$ such that $$ 2\rho(U_H) \leq \rho(Y_1) + \rho(Y_2) + 8 d[Y_1;Y_2].$$
- id `r178`: lemma; steps here: state and prove. If $D_{KL}(X\Vert Y) = 0$, then $Y$ is a copy of $X$.
- id `r684`: lemma; steps here: state and prove. For independent random variables $Y_1,Y_2,Y_3,Y_4$ over $G$, define $S:=Y_1+Y_2+Y_3+Y_4$, $T_1:=Y_1+Y_2$, $T_2:=Y_1+Y_3$. Then $$\rho(T_1|T_2,S)+\rho(T_2|T_1,S) - \frac{1}{2}\sum_{i} \rho(Y_i)\le \frac{1}{2}(d[Y_1;Y_2]+d[Y_3;Y_4]+d[Y_1;Y_3]+d[Y_2;Y_4]).$$
- id `r663`: lemma; steps here: state and prove. For independent random variables $Y_1,Y_2,Y_3,Y_4$ over $G$, define $T_1:=Y_1+Y_2,T_2:=Y_1+Y_3,T_3:=Y_2+Y_3$ and $S:=Y_1+Y_2+Y_3+Y_4$. Then $$\sum_{1 \leq i<j \leq 3} (\rho(T_i|T_j,S) + \rho(T_j|T_i,S) - \frac{1}{2}\sum_{i} \rho(Y_i))\le \sum_{1\leq i < j \leq 4}d[Y_i;Y_j]$$
- id `r329`: lemma; steps here: state and prove. If $X, Y, Z$ are independent $G$-valued random variables, then $$D_{KL}(X+Z\Vert Y+Z) \leq D_{KL}(X\Vert Y).$$
- id `r679`: definition; steps here: state only (no proof needed). We define $\rho(X) := (\rho^+(X) + \rho^-(X))/2$.
- id `r183`: lemma; steps here: state and prove. If $X,Z$ are defined on the same space, one has $$ \rho^-(X|Z) \leq \rho^-(X) + \bbH[X] - \bbH[X|Z]$$ $$ \rho^+(X|Z) \leq \rho^+(X)$$ and $$ \rho(X|Z) \leq \rho(X) + \frac{1}{2}( \bbH[X] - \bbH[X|Z] ).$$
- id `r373`: lemma; steps here: state and prove. $D_{KL}((X|W)\Vert Y) \geq 0$.
- id `r473`: lemma; steps here: state and prove. If $f$ is injective, then $\rho(X|f(Y))=\rho(X|Y)$.
- id `r402`: corollary; steps here: state and prove. If $H$ is a finite subgroup of $G$, then $\rho^+(U_H) = \log |H| - \log \max_t |A \cap (H+t)|$.
- id `r677`: definition; steps here: state only (no proof needed). For any $G$-valued random variable $X$, we define $\rho^+(X) := \rho^-(X) + \bbH(X) - \bbH(U_A)$.
- id `r647`: lemma; steps here: state and prove. If $X'$ is a copy of $X$, and $Y'$ is a copy of $Y$, then $D_{KL}(X'\Vert Y') = D_{KL}(X\Vert Y)$.
- id `r568`: definition; steps here: state only (no proof needed). We define $\rho(X|Y) := \sum_y {\bf P}(Y=y) \rho(X|Y=y)$.

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r140` before `P:r489`
- `S:r174` before `P:r718`
- `S:r183` before `P:r600`
- `S:r183` before `P:r684`
- `S:r206` before `P:r329`
- `S:r217` before `P:r487`
- `S:r217` before `S:r140`
- `S:r217` before `S:r238`
- `S:r217` before `S:r428`
- `S:r217` before `S:r489`
- `S:r217` before `S:r516`
- `S:r217` before `S:r693`
- `S:r228` before `P:r140`
- `S:r228` before `P:r428`
- `S:r228` before `P:r684`
- `S:r238` before `P:r489`
- `S:r238` before `P:r516`
- `S:r250` before `P:r174`
- `S:r250` before `P:r183`
- `S:r250` before `P:r373`
- `S:r250` before `P:r701`
- `S:r250` before `P:r718`
- `S:r250` before `P:r898`
- `S:r250` before `P:r900`
- `S:r329` before `P:r900`
- `S:r402` before `P:r174`
- `S:r428` before `P:r489`
- `S:r449` before `P:r487`
- `S:r449` before `P:r600`
- `S:r449` before `P:r986`
- `S:r473` before `P:r684`
- `S:r487` before `P:r718`
- `S:r489` before `P:r487`
- `S:r568` before `P:r140`
- `S:r568` before `P:r428`
- `S:r568` before `P:r489`
- `S:r568` before `S:r183`
- `S:r568` before `S:r238`
- `S:r568` before `S:r473`
- `S:r568` before `S:r516`
- `S:r568` before `S:r600`
- `S:r568` before `S:r663`
- `S:r568` before `S:r684`
- `S:r568` before `S:r986`
- `S:r600` before `P:r140`
- `S:r600` before `P:r428`
- `S:r600` before `P:r684`
- `S:r647` before `P:r140`
- `S:r647` before `P:r238`
- `S:r647` before `P:r428`
- `S:r647` before `P:r487`
- `S:r647` before `P:r489`
- `S:r647` before `P:r600`
- `S:r647` before `P:r684`
- `S:r647` before `P:r693`
- `S:r647` before `P:r900`
- `S:r663` before `P:r489`
- `S:r664` before `P:r140`
- `S:r664` before `P:r238`
- `S:r664` before `P:r402`
- `S:r664` before `P:r428`
- `S:r664` before `P:r487`
- `S:r664` before `P:r489`
- `S:r664` before `P:r600`
- `S:r664` before `P:r684`
- `S:r664` before `P:r693`
- `S:r664` before `P:r718`
- `S:r664` before `P:r898`
- `S:r664` before `S:r174`
- `S:r664` before `S:r183`
- `S:r664` before `S:r677`
- `S:r664` before `S:r679`
- `S:r664` before `S:r701`
- `S:r664` before `S:r900`
- `S:r677` before `P:r140`
- `S:r677` before `P:r174`
- `S:r677` before `P:r238`
- `S:r677` before `P:r428`
- `S:r677` before `P:r487`
- `S:r677` before `P:r489`
- `S:r677` before `P:r600`
- `S:r677` before `P:r684`
- `S:r677` before `P:r693`
- `S:r677` before `P:r718`
- `S:r677` before `P:r898`
- `S:r677` before `S:r183`
- `S:r677` before `S:r402`
- `S:r677` before `S:r679`
- `S:r677` before `S:r900`
- `S:r679` before `P:r140`
- `S:r679` before `P:r428`
- `S:r679` before `P:r473`
- `S:r679` before `P:r489`
- `S:r679` before `P:r693`
- `S:r679` before `P:r718`
- `S:r679` before `P:r986`
- `S:r679` before `S:r174`
- `S:r679` before `S:r183`
- `S:r679` before `S:r217`
- `S:r679` before `S:r228`
- `S:r679` before `S:r238`
- `S:r679` before `S:r449`
- `S:r679` before `S:r487`
- `S:r679` before `S:r516`
- `S:r679` before `S:r568`
- `S:r679` before `S:r600`
- `S:r679` before `S:r663`
- `S:r679` before `S:r684`
- `S:r679` before `S:r898`
- `S:r679` before `S:r900`
- `S:r684` before `P:r663`
- `S:r693` before `P:r487`
- `S:r701` before `P:r174`
- `S:r701` before `P:r402`
- `S:r718` before `P:r907`
- `S:r729` before `P:r140`
- `S:r729` before `P:r489`
- `S:r832` before `P:r140`
- `S:r832` before `P:r174`
- `S:r832` before `P:r183`
- `S:r832` before `P:r238`
- `S:r832` before `P:r428`
- `S:r832` before `P:r487`
- `S:r832` before `P:r489`
- `S:r832` before `P:r600`
- `S:r832` before `P:r684`
- `S:r832` before `P:r693`
- `S:r832` before `P:r701`
- `S:r832` before `P:r718`
- `S:r832` before `P:r898`
- `S:r832` before `P:r900`
- `S:r832` before `S:r178`
- `S:r832` before `S:r206`
- `S:r832` before `S:r250`
- `S:r832` before `S:r329`
- `S:r832` before `S:r373`
- `S:r832` before `S:r647`
- `S:r832` before `S:r664`
- `S:r832` before `S:r888`
- `S:r832` before `S:r948`
- `S:r888` before `P:r329`
- `S:r898` before `P:r487`
- `S:r898` before `P:r693`
- `S:r900` before `P:r228`
- `S:r900` before `P:r449`
- `S:r907` before `P:r988`
- `S:r948` before `P:r183`
