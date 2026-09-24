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

- id `r122`: lemma; steps here: state and prove. We have $$ \bbI[X:Y|Z] := \bbH[X|Z] + \bbH[Y|Z] - \bbH[X,Y|Z]$$ and $$ \bbI[X:Y|Z] := \bbH[X|Z] - \bbH[X|Y,Z].$$
- id `r126`: lemma; steps here: state and prove. If $X,Y,Z$ are random variables, then $\bbI[X:Y|Z] = 0$ iff $X,Y$ are conditionally independent over $Z$.
- id `r765`: lemma; steps here: state and prove. If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, then $$ \bbH[X, Y] = \bbH[Y] + \bbH[X|Y].$$
- id `r654`: lemma; steps here: state and prove. If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, and $Y = f(X,Z)$ almost surely for some map $f: S \times U \to T$ that is injective for each fixed $U$, then $\bbH[X|Z] = \bbH[Y|Z]$. Similarly, if $g: T \to U$ is injective, then $\bbH[X|g(Y)] = \bbH[X|Y]$.
- id `r109`: definition; steps here: state only (no proof needed). If $X,Y,Z$ are random variables, with $Z$ $U$-valued, then $$ \bbI[X:Y|Z] := \sum_{z \in U} P[Z=z] \bbI[(X|Z=z): (Y|Z=z)].$$
- id `r490`: lemma; steps here: state and prove. \begin{itemize} \item[(i)] If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ for some injection $f: S \to T$, then $\bbH[X] = \bbH[Y]$. \item[(ii)] If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ and $X = g(Y)$ for some functions $f: S \to T$, $g: T \to S$, then $\bbH[X] = \bbH[Y]$. \end{itemize}
- id `r802`: lemma; steps here: state and prove. If $X$ is $S$-valued random variable, then $\bbH[X] = \log |S|$ if and only if $X$ is uniformly distributed on $S$.
- id `r321`: corollary; steps here: state and prove. If $X, Y$ are conditionally independent over $Z$, then $$ \bbH[X,Y,Z] =\bbH[X,Z] + \bbH[Y,Z] - \bbH[Z].$$
- id `r532`: corollary; steps here: state and prove. With three random variables $X,Y,Z$, one has $$ \bbH[X,Y,Z] + \bbH[Z] \leq \bbH[X,Z] + \bbH[Y,Z].$$
- id `r843`: definition; steps here: state only (no proof needed). If $X: \Omega \to S$, $Y: \Omega \to T$ are random variables, then $$\bbI[X : Y] := \bbH[X] + \bbH[Y] - \bbH[X,Y].$$
- id `r129`: definition; steps here: state only (no proof needed). If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, the conditional entropy $\bbH[X|Y]$ is defined as $$ \bbH[X|Y] := \sum_{y \in Y} \bbP[Y = y] \bbH[(X | Y=y)].$$
- id `r640`: corollary; steps here: state and prove. With notation as above, we have $\bbH[X|Y] \leq \bbH[X]$.
- id `r327`: corollary; steps here: state and prove. With notation as above, we have $\bbH[X,Y] \leq \bbH[X] + \bbH[Y]$.
- id `r882`: definition; steps here: state only (no proof needed). If $X$ is an $S$-valued random variable, the entropy $\bbH[X]$ of $X$ is defined $$ \bbH[X] := \sum_{s \in S} \bbP[X=x] \log \frac{1}{\bbP[X=x]}$$ with the convention that $0 \log \frac{1}{0} = 0$.
- id `r548`: lemma; steps here: state and prove. If $X$ is an $S$-valued random variable, then there exists $s \in S$ such that $\bbP[X=s] \geq \exp(-\bbH[X])$.
- id `r607`: corollary; steps here: state and prove. If $X,Y$ are random variables, then $\bbH[X,Y] = \bbH[X] + \bbH[Y]$ if and only if $X,Y$ are independent.
- id `r666`: lemma; steps here: state and prove. If $X$ is uniformly distributed on $H$, then, then $\bbH[X] = \log |H|$.
- id `r338`: lemma; steps here: state and prove. If $X: \Omega \to S$, $Y: \Omega \to T$, $Z: \Omega \to U$ are random variables, then $$ \bbH[X, Y | Z] = \bbH[Y | Z] + \bbH[X|Y, Z].$$
- id `r453`: lemma; steps here: state and prove. If $X,Y$ are random variables, then $\bbI[X:Y] = 0$ if and only if $X,Y$ are independent.
- id `r336`: lemma; steps here: state and prove. With notation as above, we have $$ \bbI[X : Y] = \bbI[Y:X]$$ $$ \bbI[X : Y] = \bbH[X] - \bbH[X|Y]$$ $$ \bbI[X : Y] = \bbH[Y] - \bbH[Y|X]$$
- id `r793`: lemma; steps here: state and prove. We have $\bbI[X:Y] \geq 0$.
- id `r324`: definition; steps here: state only (no proof needed). If $H$ is a subset of $S$, an $S$-random variable $X$ is said to be uniformly distributed on $H$ if $\bbP[X = s] = 1/|H|$ for $s \in X$ and $\bbP[X=s] = 0$ otherwise.
- id `r879`: lemma; steps here: state and prove. If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, then $\bbH[X, Y] = \bbH[Y, X]$ and $\bbH[X, (Y,Z)] = \bbH[(X,Y), Z]$.
- id `r570`: lemma; steps here: state and prove. If $X$ is an $S$-valued random variable, then $\bbH[X] \leq \log |S|$.
- id `r396`: lemma; steps here: state and prove. If $X,Y,Z$ are random variables, then $\bbI[X:Y|Z] \ge 0$.
- id `r526`: definition; steps here: state only (no proof needed). Two random variables $X: \Omega \to S$ and $Y: \Omega \to T$ are conditionally independent relative to another random variable $Z: \Omega \to U$ if $P[X = s \wedge Y = t| Z=u] = P[X=s|Z=u] P[Y=t|Z=u]$ for all $s \in S, t \in T, u \in U$. (We won't need conditional independence for more variables than this.)
- id `r957`: corollary; steps here: state and prove. With three random variables $X,Y,Z$, one has $\bbH[X|Y,Z] \leq \bbH[X|Z]$.
- id `r669`: lemma; steps here: state and prove. Given a finite non-empty subset $H$ of a set $S$, there exists a random variable $X$ (on some probability space) that is uniformly distributed on $H$.

## Constraints

When both are here, `S:x` must come before `P:x`. In addition:

- `S:r109` before `P:r321`
- `S:r109` before `S:r122`
- `S:r109` before `S:r126`
- `S:r109` before `S:r396`
- `S:r122` before `P:r321`
- `S:r126` before `P:r321`
- `S:r129` before `P:r321`
- `S:r129` before `P:r532`
- `S:r129` before `S:r122`
- `S:r129` before `S:r336`
- `S:r129` before `S:r338`
- `S:r129` before `S:r640`
- `S:r129` before `S:r654`
- `S:r129` before `S:r765`
- `S:r129` before `S:r957`
- `S:r324` before `S:r666`
- `S:r324` before `S:r669`
- `S:r324` before `S:r802`
- `S:r338` before `P:r122`
- `S:r453` before `P:r126`
- `S:r453` before `P:r607`
- `S:r490` before `P:r654`
- `S:r490` before `P:r879`
- `S:r490` before `P:r957`
- `S:r526` before `S:r126`
- `S:r526` before `S:r321`
- `S:r654` before `P:r338`
- `S:r765` before `P:r321`
- `S:r765` before `P:r336`
- `S:r765` before `P:r532`
- `S:r765` before `P:r640`
- `S:r765` before `P:r654`
- `S:r765` before `P:r957`
- `S:r793` before `P:r126`
- `S:r793` before `P:r327`
- `S:r793` before `P:r396`
- `S:r793` before `P:r640`
- `S:r843` before `P:r126`
- `S:r843` before `P:r607`
- `S:r843` before `P:r640`
- `S:r843` before `S:r336`
- `S:r843` before `S:r453`
- `S:r843` before `S:r793`
- `S:r879` before `P:r321`
- `S:r879` before `P:r336`
- `S:r879` before `P:r765`
- `S:r882` before `P:r122`
- `S:r882` before `P:r126`
- `S:r882` before `P:r338`
- `S:r882` before `P:r396`
- `S:r882` before `P:r453`
- `S:r882` before `P:r654`
- `S:r882` before `P:r793`
- `S:r882` before `P:r957`
- `S:r882` before `S:r109`
- `S:r882` before `S:r129`
- `S:r882` before `S:r321`
- `S:r882` before `S:r327`
- `S:r882` before `S:r336`
- `S:r882` before `S:r490`
- `S:r882` before `S:r532`
- `S:r882` before `S:r548`
- `S:r882` before `S:r570`
- `S:r882` before `S:r607`
- `S:r882` before `S:r640`
- `S:r882` before `S:r666`
- `S:r882` before `S:r765`
- `S:r882` before `S:r802`
- `S:r882` before `S:r843`
- `S:r882` before `S:r879`
- `S:r957` before `P:r532`
