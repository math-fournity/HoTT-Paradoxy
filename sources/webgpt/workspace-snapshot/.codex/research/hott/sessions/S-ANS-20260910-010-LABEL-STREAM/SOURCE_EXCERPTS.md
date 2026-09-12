# 本轮使用的固定原规则摘录

类型：定点读取的一手原文；不是全书语义审查。全文件路径、SHA和实际行区间如下。

## `HoTT/theory-schema/upstream/book-578b85cc/basics.tex` L1628—L1636

全文件SHA-256：`516b469d7356e9d20df5539e726a0468760f9fa7b7f440b9c054981e803d7533`。

```tex
Given a type $X$, a path $p:\id[X]{x_1}{x_2}$, type families $A,B:X\to \type$, and a function $f : A(x_1) \to B(x_1)$,  we have
\begin{align}\label{eq:transport-arrow}
  \transfib{A\to B}{p}{f} &=
  \Big(x \mapsto \transfib{B}{p}{f(\transfib{A}{\opp p}{x})}\Big)
\end{align}
where $A\to B$ denotes abusively the type family $X\to \type$ defined by
\[(A\to B)(x) \defeq (A(x)\to B(x)).\]
In other words, when we transport a function $f:A(x_1)\to B(x_1)$ along a path $p:x_1=x_2$, we obtain the function $A(x_2)\to B(x_2)$ which transports its argument backwards along $p$ (in the type family $A$), applies $f$, and then transports the result forwards along $p$ (in the type family $B$).
This can be proven easily by path induction.
```

## `HoTT/theory-schema/upstream/book-578b85cc/basics.tex` L1763—L1780

全文件SHA-256：`516b469d7356e9d20df5539e726a0468760f9fa7b7f440b9c054981e803d7533`。

```tex
\symlabel{ua}
\begin{itemize}
\item An introduction rule for {(\id[\type]{A}{B})}, denoted $\ua$ for ``univalence axiom'':
  \[
  \ua : ({\eqv A B}) \to (\id[\type]{A}{B}).
  \]
\item The elimination rule, which is $\idtoeqv$,
  \[
  \idtoeqv \jdeq \transfibf{X \mapsto X} : (\id[\type]{A}{B}) \to (\eqv A B).
  \]
\item The propositional computation rule\index{computation rule!propositional!for univalence},
  \[
  \transfib{X \mapsto X}{\ua(f)}{x} = f(x).
  \]
\item The propositional uniqueness principle: \index{uniqueness!principle, propositional!for univalence}
  for any $p : \id A B$,
  \[
  \id{p}{\ua(\transfibf{X \mapsto X}(p))}.
```

## `HoTT/theory-schema/upstream/book-578b85cc/logic.tex` L598—L641

全文件SHA-256：`76ac2e06ffa133ede0612584fef4b9c81d698d4e0b7a4ec683131448edfed2f2`。

```tex
\section{Propositional truncation}
\label{subsec:prop-trunc}

\index{truncation!propositional|(defstyle}%
\indexsee{type!squash}{truncation, propositional}%
\indexsee{squash type}{truncation, propositional}%
\indexsee{bracket type}{truncation, propositional}%
\indexsee{type!bracket}{truncation, propositional}%
The \emph{propositional truncation}, also called the \emph{$(-1)$-truncation}, \emph{bracket type}, or \emph{squash type}, is an additional type former which ``squashes'' or ``truncates'' a type down to a mere proposition, forgetting all information contained in inhabitants of that type other than their existence.

More precisely, for any type $A$, there is a type $\brck{A}$.
It has two constructors:
\begin{itemize}
\item For any $a:A$ we have $\bproj a : \brck A$.
\item For any $x,y:\brck A$, we have $x=y$.
\end{itemize}
The first constructor means that if $A$ is inhabited, so is $\brck A$.
The second ensures that $\brck A$ is a mere proposition; usually we leave the witness of this fact nameless.

\index{recursion principle!for truncation}%
The recursion principle of $\brck A$ says that:
\begin{itemize}
\item If $B$ is a mere proposition and we have $f:A\to B$, then there is an induced $g:\brck A \to B$ such that $g(\bproj a) \jdeq f(a)$ for all $a:A$.
\end{itemize}
In other words, any mere proposition which follows from (the inhabitedness of) $A$ already follows from $\brck A$.
Thus, $\brck A$, as a mere proposition, contains no more information than the inhabitedness of $A$.
(There is also an induction principle for $\brck A$, but it is not especially useful; see \cref{ex:prop-trunc-ind}.)

In \cref{ex:lem-brck,ex:impred-brck,sec:hittruncations} we will describe some ways to construct $\brck{A}$ in terms of more general things.
For now, we simply assume it as an additional rule alongside those of \cref{cha:typetheory}.

With the propositional truncation, we can extend the ``logic of mere propositions'' to cover disjunction and the existential quantifier.
Specifically, $\brck{A+B}$ is a mere propositional version of ``$A$ or $B$'', which does not ``remember'' the information of which disjunct is true.

The recursion principle of truncation implies that we can still do a case analysis on $\brck{A+B}$ \emph{when attempting to prove a mere proposition}.
That is, suppose we have an assumption $u:\brck{A+B}$ and we are trying to prove a mere proposition $Q$.
In other words, we are trying to define an element of $\brck{A+B} \to Q$.
Since $Q$ is a mere proposition, by the recursion principle for propositional truncation, it suffices to construct a function $A+B\to Q$.
But now we can use case analysis on $A+B$.

Similarly, for a type family $P:A\to\type$, we can consider $\brck{\sm{x:A} P(x)}$, which is a mere propositional version of ``there exists an $x:A$ such that $P(x)$''.
As for disjunction, by combining the induction principles of truncation and $\Sigma$-types, if we have an assumption of type $\brck{\sm{x:A} P(x)}$, we may introduce new assumptions $x:A$ and $y:P(x)$ \emph{when attempting to prove a mere proposition}.
In other words, if we know that there exists some $x:A$ such that $P(x)$, but we don't have a particular such $x$ in hand, then we are free to make use of such an $x$ as long as we aren't trying to construct anything which might depend on the particular value of $x$.
Requiring the codomain to be a mere proposition expresses this independence of the result on the witness, since all possible inhabitants of such a type must be equal.
```

## `HoTT/theory-schema/upstream/book-578b85cc/logic.tex` L801—L838

全文件SHA-256：`76ac2e06ffa133ede0612584fef4b9c81d698d4e0b7a4ec683131448edfed2f2`。

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
