You are organising one chapter of a mathematical exposition. Below are its results
(definitions, lemmas, theorems) in an arbitrary order, each with an id and its statement. Some results use
others; the constraints list which must come first.

Choose the order in which you would present these results to a mathematician reading the chapter for the
first time, so that it is as easy as possible to follow. Respect every constraint.

Reply with only a JSON array containing every id exactly once, in your chosen order.

## Results

- id `r426`: definition. If $H$ is a subset of $S$, an $S$-random variable $X$ is said to be uniformly distributed on $H$ if $\bbP[X = s] = 1/|H|$ for $s \in X$ and $\bbP[X=s] = 0$ otherwise.
- id `r489`: lemma. If $X,Y$ are random variables, then $\bbI[X:Y] = 0$ if and only if $X,Y$ are independent.
- id `r533`: corollary. With notation as above, we have $\bbH[X|Y] \leq \bbH[X]$.
- id `r638`: lemma. We have $\bbI[X:Y] \geq 0$.
- id `r268`: definition. If $X$ is an $S$-valued random variable, the entropy $\bbH[X]$ of $X$ is defined $$ \bbH[X] := \sum_{s \in S} \bbP[X=x] \log \frac{1}{\bbP[X=x]}$$ with the convention that $0 \log \frac{1}{0} = 0$.
- id `r673`: lemma. If $X,Y,Z$ are random variables, then $\bbI[X:Y|Z] \ge 0$.
- id `r281`: lemma. Given a finite non-empty subset $H$ of a set $S$, there exists a random variable $X$ (on some probability space) that is uniformly distributed on $H$.
- id `r341`: lemma. If $X$ is an $S$-valued random variable, then there exists $s \in S$ such that $\bbP[X=s] \geq \exp(-\bbH[X])$.
- id `r336`: lemma. With notation as above, we have $$ \bbI[X : Y] = \bbI[Y:X]$$ $$ \bbI[X : Y] = \bbH[X] - \bbH[X|Y]$$ $$ \bbI[X : Y] = \bbH[Y] - \bbH[Y|X]$$
- id `r124`: corollary. With notation as above, we have $\bbH[X,Y] \leq \bbH[X] + \bbH[Y]$.
- id `r280`: corollary. With three random variables $X,Y,Z$, one has $$ \bbH[X,Y,Z] + \bbH[Z] \leq \bbH[X,Z] + \bbH[Y,Z].$$
- id `r432`: lemma. We have $$ \bbI[X:Y|Z] := \bbH[X|Z] + \bbH[Y|Z] - \bbH[X,Y|Z]$$ and $$ \bbI[X:Y|Z] := \bbH[X|Z] - \bbH[X|Y,Z].$$
- id `r277`: lemma. If $X: \Omega \to S$, $Y: \Omega \to T$, $Z: \Omega \to U$ are random variables, then $$ \bbH[X, Y | Z] = \bbH[Y | Z] + \bbH[X|Y, Z].$$
- id `r239`: corollary. With three random variables $X,Y,Z$, one has $\bbH[X|Y,Z] \leq \bbH[X|Z]$.
- id `r622`: lemma. If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, and $Y = f(X,Z)$ almost surely for some map $f: S \times U \to T$ that is injective for each fixed $U$, then $\bbH[X|Z] = \bbH[Y|Z]$. Similarly, if $g: T \to U$ is injective, then $\bbH[X|g(Y)] = \bbH[X|Y]$.
- id `r468`: definition. If $X: \Omega \to S$, $Y: \Omega \to T$ are random variables, then $$\bbI[X : Y] := \bbH[X] + \bbH[Y] - \bbH[X,Y].$$
- id `r626`: definition. If $X,Y,Z$ are random variables, with $Z$ $U$-valued, then $$ \bbI[X:Y|Z] := \sum_{z \in U} P[Z=z] \bbI[(X|Z=z): (Y|Z=z)].$$
- id `r790`: lemma. If $X,Y,Z$ are random variables, then $\bbI[X:Y|Z] = 0$ iff $X,Y$ are conditionally independent over $Z$.
- id `r286`: lemma. If $X$ is uniformly distributed on $H$, then, then $\bbH[X] = \log |H|$.
- id `r556`: lemma. If $X: \Omega \to S$, $Y: \Omega \to T$, and $Z: \Omega \to U$ are random variables, then $\bbH[X, Y] = \bbH[Y, X]$ and $\bbH[X, (Y,Z)] = \bbH[(X,Y), Z]$.
- id `r915`: definition. If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, the conditional entropy $\bbH[X|Y]$ is defined as $$ \bbH[X|Y] := \sum_{y \in Y} \bbP[Y = y] \bbH[(X | Y=y)].$$
- id `r524`: corollary. If $X,Y$ are random variables, then $\bbH[X,Y] = \bbH[X] + \bbH[Y]$ if and only if $X,Y$ are independent.
- id `r852`: lemma. If $X$ is $S$-valued random variable, then $\bbH[X] = \log |S|$ if and only if $X$ is uniformly distributed on $S$.
- id `r637`: lemma. If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, then $$ \bbH[X, Y] = \bbH[Y] + \bbH[X|Y].$$
- id `r881`: definition. Two random variables $X: \Omega \to S$ and $Y: \Omega \to T$ are conditionally independent relative to another random variable $Z: \Omega \to U$ if $P[X = s \wedge Y = t| Z=u] = P[X=s|Z=u] P[Y=t|Z=u]$ for all $s \in S, t \in T, u \in U$. (We won't need conditional independence for more variables than this.)
- id `r472`: lemma. If $X$ is an $S$-valued random variable, then $\bbH[X] \leq \log |S|$.
- id `r908`: lemma. \begin{itemize} \item[(i)] If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ for some injection $f: S \to T$, then $\bbH[X] = \bbH[Y]$. \item[(ii)] If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ and $X = g(Y)$ for some functions $f: S \to T$, $g: T \to S$, then $\bbH[X] = \bbH[Y]$. \end{itemize}
- id `r707`: corollary. If $X, Y$ are conditionally independent over $Z$, then $$ \bbH[X,Y,Z] =\bbH[X,Z] + \bbH[Y,Z] - \bbH[Z].$$

## Constraints

- `r239` before `r280`
- `r268` before `r124`
- `r268` before `r239`
- `r268` before `r277`
- `r268` before `r280`
- `r268` before `r286`
- `r268` before `r336`
- `r268` before `r341`
- `r268` before `r432`
- `r268` before `r468`
- `r268` before `r472`
- `r268` before `r489`
- `r268` before `r524`
- `r268` before `r533`
- `r268` before `r556`
- `r268` before `r622`
- `r268` before `r626`
- `r268` before `r637`
- `r268` before `r638`
- `r268` before `r673`
- `r268` before `r707`
- `r268` before `r790`
- `r268` before `r852`
- `r268` before `r908`
- `r268` before `r915`
- `r277` before `r432`
- `r426` before `r281`
- `r426` before `r286`
- `r426` before `r852`
- `r432` before `r707`
- `r468` before `r336`
- `r468` before `r489`
- `r468` before `r524`
- `r468` before `r533`
- `r468` before `r638`
- `r468` before `r790`
- `r489` before `r524`
- `r489` before `r790`
- `r556` before `r336`
- `r556` before `r637`
- `r556` before `r707`
- `r622` before `r277`
- `r626` before `r432`
- `r626` before `r673`
- `r626` before `r707`
- `r626` before `r790`
- `r637` before `r239`
- `r637` before `r280`
- `r637` before `r336`
- `r637` before `r533`
- `r637` before `r622`
- `r637` before `r707`
- `r638` before `r124`
- `r638` before `r533`
- `r638` before `r673`
- `r638` before `r790`
- `r790` before `r707`
- `r881` before `r707`
- `r881` before `r790`
- `r908` before `r239`
- `r908` before `r556`
- `r908` before `r622`
- `r915` before `r239`
- `r915` before `r277`
- `r915` before `r280`
- `r915` before `r336`
- `r915` before `r432`
- `r915` before `r533`
- `r915` before `r622`
- `r915` before `r637`
- `r915` before `r707`
