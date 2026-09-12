# 本轮实际使用的源规则

## `HoTT/theory-schema/upstream/book-578b85cc/logic.tex` 第801—844行

SHA-256 `76ac2e06ffa133ede0612584fef4b9c81d698d4e0b7a4ec683131448edfed2f2`。

```text
801|\section{The principle of unique choice}
802|\label{sec:unique-choice}
803|
804|\index{unique!choice|(defstyle}%
805|\indexsee{axiom!of choice!unique}{unique choice}%
806|
807|The following observation is trivial, but very useful.
808|
809|\begin{lem}\label{thm:prop-equiv-trunc}
810|  If $P$ is a mere proposition, then $\eqv P {\brck P}$.
811|\end{lem}
812|\begin{proof}
813|  Of course, we have $P\to \brck{P}$ by definition.
814|  And since $P$ is a mere proposition, the universal property of $\brck P$ applied to $\idfunc[P] :P\to P$ yields $\brck P \to P$.
815|  These functions are quasi-inverses by \cref{lem:equiv-iff-hprop}.
816|\end{proof}
817|
818|Among its important consequences is the following.
819|
820|\begin{cor}[The principle of unique choice]\label{cor:UC}
821|  Suppose a type family $P:A\to \type$ such that
822|  \begin{enumerate}
823|  \item For each $x$, the type $P(x)$ is a mere proposition, and
824|  \item For each $x$ we have $\brck {P(x)}$.
825|  \end{enumerate}
826|  Then we have $\prd{x:A} P(x)$.
827|\end{cor}
828|\begin{proof}
829|  Immediate from the two assumptions and the previous lemma.
830|\end{proof}
831|
832|The corollary also encapsulates a very useful technique of reasoning.
833|Namely, suppose we know that $\brck A$, and we want to use this to construct an element of some other type $B$.
834|We would like to use an element of $A$ in our construction of an element of $B$, but this is allowed only if $B$ is a mere proposition, so that we can apply the induction principle for the propositional truncation $\brck A$; the most we could hope to do in general is to show $\brck B$.
835|%
836|Instead, we can extend $B$ with additional data which characterizes \emph{uniquely} the object we wish to construct.
837|Specifically, we define a predicate $Q:B\to\type$ such that $\sm{x:B} Q(x)$ is a mere proposition.
838|Then from an element of $A$ we construct an element $b:B$ such that $Q(b)$, hence from $\brck A$ we can construct $\brck{\sm{x:B} Q(x)}$, and because $\brck{\sm{x:B} Q(x)}$ is equivalent to $\sm{x:B} Q(x)$ an element of $B$ may be projected from it.
839|An example can be found in \cref{ex:decidable-choice}.
840|
841|A similar issue arises in set-theoretic mathematics, although it manifests slightly
842|differently. If we are trying to define a function $f: A \to B$, and depending on an
843|element $a : A$ we are able to prove mere existence of some $b : B$, we are not done yet
844|because we need to actually pinpoint an element of~$B$, not just prove its existence.
```

## `HoTT/theory-schema/upstream/book-578b85cc/basics.tex` 第1628—1636行

SHA-256 `516b469d7356e9d20df5539e726a0468760f9fa7b7f440b9c054981e803d7533`。

```text
1628|Given a type $X$, a path $p:\id[X]{x_1}{x_2}$, type families $A,B:X\to \type$, and a function $f : A(x_1) \to B(x_1)$,  we have
1629|\begin{align}\label{eq:transport-arrow}
1630|  \transfib{A\to B}{p}{f} &=
1631|  \Big(x \mapsto \transfib{B}{p}{f(\transfib{A}{\opp p}{x})}\Big)
1632|\end{align}
1633|where $A\to B$ denotes abusively the type family $X\to \type$ defined by
1634|\[(A\to B)(x) \defeq (A(x)\to B(x)).\]
1635|In other words, when we transport a function $f:A(x_1)\to B(x_1)$ along a path $p:x_1=x_2$, we obtain the function $A(x_2)\to B(x_2)$ which transports its argument backwards along $p$ (in the type family $A$), applies $f$, and then transports the result forwards along $p$ (in the type family $B$).
1636|This can be proven easily by path induction.
```

## `HoTT/theory-schema/upstream/book-578b85cc/basics.tex` 第1763—1780行

SHA-256 `516b469d7356e9d20df5539e726a0468760f9fa7b7f440b9c054981e803d7533`。

```text
1763|\symlabel{ua}
1764|\begin{itemize}
1765|\item An introduction rule for {(\id[\type]{A}{B})}, denoted $\ua$ for ``univalence axiom'':
1766|  \[
1767|  \ua : ({\eqv A B}) \to (\id[\type]{A}{B}).
1768|  \]
1769|\item The elimination rule, which is $\idtoeqv$,
1770|  \[
1771|  \idtoeqv \jdeq \transfibf{X \mapsto X} : (\id[\type]{A}{B}) \to (\eqv A B).
1772|  \]
1773|\item The propositional computation rule\index{computation rule!propositional!for univalence},
1774|  \[
1775|  \transfib{X \mapsto X}{\ua(f)}{x} = f(x).
1776|  \]
1777|\item The propositional uniqueness principle: \index{uniqueness!principle, propositional!for univalence}
1778|  for any $p : \id A B$,
1779|  \[
1780|  \id{p}{\ua(\transfibf{X \mapsto X}(p))}.
```

这些是固定源规则，不是本轮机器证明。第11版论证另有明确前提；纸笔正确性仍待独立复核。
