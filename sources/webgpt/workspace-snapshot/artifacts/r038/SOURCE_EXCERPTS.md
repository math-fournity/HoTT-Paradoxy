# R038 exact local source excerpts

Source bytes are pinned by the manifest; quotations do not certify our new proofs.

## hits.tex L1210–1234, sha256=d43dac381da7f978fb1d2ff6c2c2d3cca7f9b0dab90c96cd20815c13e7ab8454

```tex
\begin{lem}\label{thm:quotient-surjective}
  The function $q:A\to A/R$ is surjective.
\end{lem}
\begin{proof}
  We must show that for any $x:A/R$ there merely exists an $a:A$ with $q(a)=x$.
  We use the induction principle of $A/R$.
  The first case is trivial: if $x$ is $q(a)$, then of course there merely exists an $a$ such that $q(a)=q(a)$.
  And since the goal is a mere proposition, it automatically respects all path constructors, so we are done.
\end{proof}

We can now prove that the set-quotient has the expected universal property of a (set-)coequalizer.

\begin{lem}\label{thm:quotient-ump}
  For any set $B$, precomposing with $q$ yields an equivalence
  \[ \eqvspaced{(A/R \to B)}{\Parens{\sm{f:A\to B} \prd{a,b:A} R(a,b) \to (f(a)=f(b))}}.\]
\end{lem}
\begin{proof}
  The quasi-inverse of $\blank\circ q$, going from right to left, is just the recursion principle for $A/R$.
  That is, given $f:A\to B$ such that
  \narrowequation{\prd{a,b:A} R(a,b) \to (f(a)=f(b)),} we define $\bar f:A/R\to B$ by $\bar f(q(a))\defeq f(a)$.
  This defining equation says precisely that $(f\mapsto \bar f)$ is a right inverse to $(\blank\circ q)$.

  For it to also be a left inverse, we must show that for any $g:A/R\to B$ and $x:A/R$ we have $g(x) = \overline{g\circ q}(x)$.
  However, by \cref{thm:quotient-surjective} there merely exists $a$ such that $q(a)=x$.
  Since our desired equality is a mere proposition, we may assume there purely exists such an $a$, in which case $g(x) = g(q(a)) = \overline{g\circ q}(q(a)) = \overline{g\circ q}(x)$.
```

## logic.tex L801–838, sha256=76ac2e06ffa133ede0612584fef4b9c81d698d4e0b7a4ec683131448edfed2f2

```tex
\section{The principle of unique choice}
\label{sec:unique-choice}

\index{unique!choice|(defstyle}%
\indexsee{axiom!of choice!unique}{unique choice}%

The following observation is trivial, but very useful.

\begin{lem}\label{thm:prop-equiv-trunc}
  If $P$ is a mere proposition, then $\eqv P {\brck P}$.
\end{lem}
\begin{proof}
  Of course, we have $P\to \brck{P}$ by definition.
  And since $P$ is a mere proposition, the universal property of $\brck P$ applied to $\idfunc[P] :P\to P$ yields $\brck P \to P$.
  These functions are quasi-inverses by \cref{lem:equiv-iff-hprop}.
\end{proof}

Among its important consequences is the following.

\begin{cor}[The principle of unique choice]\label{cor:UC}
  Suppose a type family $P:A\to \type$ such that
  \begin{enumerate}
  \item For each $x$, the type $P(x)$ is a mere proposition, and
  \item For each $x$ we have $\brck {P(x)}$.
  \end{enumerate}
  Then we have $\prd{x:A} P(x)$.
\end{cor}
\begin{proof}
  Immediate from the two assumptions and the previous lemma.
\end{proof}

The corollary also encapsulates a very useful technique of reasoning.
Namely, suppose we know that $\brck A$, and we want to use this to construct an element of some other type $B$.
We would like to use an element of $A$ in our construction of an element of $B$, but this is allowed only if $B$ is a mere proposition, so that we can apply the induction principle for the propositional truncation $\brck A$; the most we could hope to do in general is to show $\brck B$.
%
Instead, we can extend $B$ with additional data which characterizes \emph{uniquely} the object we wish to construct.
Specifically, we define a predicate $Q:B\to\type$ such that $\sm{x:B} Q(x)$ is a mere proposition.
Then from an element of $A$ we construct an element $b:B$ such that $Q(b)$, hence from $\brck A$ we can construct $\brck{\sm{x:B} Q(x)}$, and because $\brck{\sm{x:B} Q(x)}$ is equivalent to $\sm{x:B} Q(x)$ an element of $B$ may be projected from it.
```
