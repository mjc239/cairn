You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `r122`: lemma. We have $$ \bbI[X:Y|Z] := \bbH[X|Z] + \bbH[Y|Z] - \bbH[X,Y|Z]$$ and $$ \bbI[X:Y|Z] := \bbH[X|Z] - \bbH[X|Y,Z].$$
- id `r126`: lemma. If $X,Y,Z$ are random variables, then $\bbI[X:Y|Z] = 0$ iff $X,Y$ are conditionally independent over $Z$.
- id `r765`: lemma. If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, then $$ \bbH[X, Y] = \bbH[Y] + \bbH[X|Y].$$
- id `r654`: lemma. If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, and $Y = f(X,Z)$ almost surely for some map $f: S \times U \to T$ that is injective for each fixed $U$, then $\bbH[X|Z] = \bbH[Y|Z]$. Similarly, if $g: T \to U$ is injective, then $\bbH[X|g(Y)] = \bbH[X|Y]$.
- id `r109`: definition. If $X,Y,Z$ are random variables, with $Z$ $U$-valued, then $$ \bbI[X:Y|Z] := \sum_{z \in U} P[Z=z] \bbI[(X|Z=z): (Y|Z=z)].$$
- id `r490`: lemma. \begin{itemize} \item[(i)] If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ for some injection $f: S \to T$, then $\bbH[X] = \bbH[Y]$. \item[(ii)] If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ and $X = g(Y)$ for some functions $f: S \to T$, $g: T \to S$, then $\bbH[X] = \bbH[Y]$. \end{itemize}
- id `r802`: lemma. If $X$ is $S$-valued random variable, then $\bbH[X] = \log |S|$ if and only if $X$ is uniformly distributed on $S$.
- id `r321`: corollary. If $X, Y$ are conditionally independent over $Z$, then $$ \bbH[X,Y,Z] =\bbH[X,Z] + \bbH[Y,Z] - \bbH[Z].$$
- id `r532`: corollary. With three random variables $X,Y,Z$, one has $$ \bbH[X,Y,Z] + \bbH[Z] \leq \bbH[X,Z] + \bbH[Y,Z].$$
- id `r843`: definition. If $X: \Omega \to S$, $Y: \Omega \to T$ are random variables, then $$\bbI[X : Y] := \bbH[X] + \bbH[Y] - \bbH[X,Y].$$
- id `r129`: definition. If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, the conditional entropy $\bbH[X|Y]$ is defined as $$ \bbH[X|Y] := \sum_{y \in Y} \bbP[Y = y] \bbH[(X | Y=y)].$$
- id `r640`: corollary. With notation as above, we have $\bbH[X|Y] \leq \bbH[X]$.
- id `r327`: corollary. With notation as above, we have $\bbH[X,Y] \leq \bbH[X] + \bbH[Y]$.
- id `r882`: definition. If $X$ is an $S$-valued random variable, the entropy $\bbH[X]$ of $X$ is defined $$ \bbH[X] := \sum_{s \in S} \bbP[X=x] \log \frac{1}{\bbP[X=x]}$$ with the convention that $0 \log \frac{1}{0} = 0$.
- id `r548`: lemma. If $X$ is an $S$-valued random variable, then there exists $s \in S$ such that $\bbP[X=s] \geq \exp(-\bbH[X])$.
- id `r607`: corollary. If $X,Y$ are random variables, then $\bbH[X,Y] = \bbH[X] + \bbH[Y]$ if and only if $X,Y$ are independent.
- id `r666`: lemma. If $X$ is uniformly distributed on $H$, then, then $\bbH[X] = \log |H|$.
- id `r338`: lemma. If $X: \Omega \to S$, $Y: \Omega \to T$, $Z: \Omega \to U$ are random variables, then $$ \bbH[X, Y | Z] = \bbH[Y | Z] + \bbH[X|Y, Z].$$
- id `r453`: lemma. If $X,Y$ are random variables, then $\bbI[X:Y] = 0$ if and only if $X,Y$ are independent.
- id `r336`: lemma. With notation as above, we have $$ \bbI[X : Y] = \bbI[Y:X]$$ $$ \bbI[X : Y] = \bbH[X] - \bbH[X|Y]$$ $$ \bbI[X : Y] = \bbH[Y] - \bbH[Y|X]$$
- id `r793`: lemma. We have $\bbI[X:Y] \geq 0$.
- id `r324`: definition. If $H$ is a subset of $S$, an $S$-random variable $X$ is said to be uniformly distributed on $H$ if $\bbP[X = s] = 1/|H|$ for $s \in X$ and $\bbP[X=s] = 0$ otherwise.
- id `r879`: lemma. If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, then $\bbH[X, Y] = \bbH[Y, X]$ and $\bbH[X, (Y,Z)] = \bbH[(X,Y), Z]$.
- id `r570`: lemma. If $X$ is an $S$-valued random variable, then $\bbH[X] \leq \log |S|$.
- id `r396`: lemma. If $X,Y,Z$ are random variables, then $\bbI[X:Y|Z] \ge 0$.
- id `r526`: definition. Two random variables $X: \Omega \to S$ and $Y: \Omega \to T$ are conditionally independent relative to another random variable $Z: \Omega \to U$ if $P[X = s \wedge Y = t| Z=u] = P[X=s|Z=u] P[Y=t|Z=u]$ for all $s \in S, t \in T, u \in U$. (We won't need conditional independence for more variables than this.)
- id `r957`: corollary. With three random variables $X,Y,Z$, one has $\bbH[X|Y,Z] \leq \bbH[X|Z]$.
- id `r669`: lemma. Given a finite non-empty subset $H$ of a set $S$, there exists a random variable $X$ (on some probability space) that is uniformly distributed on $H$.

## Constraints

- `r109` before `r122`
- `r109` before `r126`
- `r109` before `r321`
- `r109` before `r396`
- `r122` before `r321`
- `r126` before `r321`
- `r129` before `r122`
- `r129` before `r321`
- `r129` before `r336`
- `r129` before `r338`
- `r129` before `r532`
- `r129` before `r640`
- `r129` before `r654`
- `r129` before `r765`
- `r129` before `r957`
- `r324` before `r666`
- `r324` before `r669`
- `r324` before `r802`
- `r338` before `r122`
- `r453` before `r126`
- `r453` before `r607`
- `r490` before `r654`
- `r490` before `r879`
- `r490` before `r957`
- `r526` before `r126`
- `r526` before `r321`
- `r654` before `r338`
- `r765` before `r321`
- `r765` before `r336`
- `r765` before `r532`
- `r765` before `r640`
- `r765` before `r654`
- `r765` before `r957`
- `r793` before `r126`
- `r793` before `r327`
- `r793` before `r396`
- `r793` before `r640`
- `r843` before `r126`
- `r843` before `r336`
- `r843` before `r453`
- `r843` before `r607`
- `r843` before `r640`
- `r843` before `r793`
- `r879` before `r321`
- `r879` before `r336`
- `r879` before `r765`
- `r882` before `r109`
- `r882` before `r122`
- `r882` before `r126`
- `r882` before `r129`
- `r882` before `r321`
- `r882` before `r327`
- `r882` before `r336`
- `r882` before `r338`
- `r882` before `r396`
- `r882` before `r453`
- `r882` before `r490`
- `r882` before `r532`
- `r882` before `r548`
- `r882` before `r570`
- `r882` before `r607`
- `r882` before `r640`
- `r882` before `r654`
- `r882` before `r666`
- `r882` before `r765`
- `r882` before `r793`
- `r882` before `r802`
- `r882` before `r843`
- `r882` before `r879`
- `r882` before `r957`
- `r957` before `r532`
