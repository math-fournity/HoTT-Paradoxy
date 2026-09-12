# R019 实际回查的项目原始规则

## unique choice

`HoTT/theory-schema/upstream/book-578b85cc/logic.tex` L801—838; SHA256 `76ac2e06ffa133ede0612584fef4b9c81d698d4e0b7a4ec683131448edfed2f2`

```text
801: \section{The principle of unique choice}
802: \label{sec:unique-choice}
803: 
804: \index{unique!choice|(defstyle}%
805: \indexsee{axiom!of choice!unique}{unique choice}%
806: 
807: The following observation is trivial, but very useful.
808: 
809: \begin{lem}\label{thm:prop-equiv-trunc}
810:   If $P$ is a mere proposition, then $\eqv P {\brck P}$.
811: \end{lem}
812: \begin{proof}
813:   Of course, we have $P\to \brck{P}$ by definition.
814:   And since $P$ is a mere proposition, the universal property of $\brck P$ applied to $\idfunc[P] :P\to P$ yields $\brck P \to P$.
815:   These functions are quasi-inverses by \cref{lem:equiv-iff-hprop}.
816: \end{proof}
817: 
818: Among its important consequences is the following.
819: 
820: \begin{cor}[The principle of unique choice]\label{cor:UC}
821:   Suppose a type family $P:A\to \type$ such that
822:   \begin{enumerate}
823:   \item For each $x$, the type $P(x)$ is a mere proposition, and
824:   \item For each $x$ we have $\brck {P(x)}$.
825:   \end{enumerate}
826:   Then we have $\prd{x:A} P(x)$.
827: \end{cor}
828: \begin{proof}
829:   Immediate from the two assumptions and the previous lemma.
830: \end{proof}
831: 
832: The corollary also encapsulates a very useful technique of reasoning.
833: Namely, suppose we know that $\brck A$, and we want to use this to construct an element of some other type $B$.
834: We would like to use an element of $A$ in our construction of an element of $B$, but this is allowed only if $B$ is a mere proposition, so that we can apply the induction principle for the propositional truncation $\brck A$; the most we could hope to do in general is to show $\brck B$.
835: %
836: Instead, we can extend $B$ with additional data which characterizes \emph{uniquely} the object we wish to construct.
837: Specifically, we define a predicate $Q:B\to\type$ such that $\sm{x:B} Q(x)$ is a mere proposition.
838: Then from an element of $A$ we construct an element $b:B$ such that $Q(b)$, hence from $\brck A$ we can construct $\brck{\sm{x:B} Q(x)}$, and because $\brck{\sm{x:B} Q(x)}$ is equivalent to $\sm{x:B} Q(x)$ an element of $B$ may be projected from it.
```

## axioms and judgmental rules

`HoTT/theory-schema/upstream/book-578b85cc/formal.tex` L984—1009; SHA256 `e621484e2e457e70536a92367cca452f34df8ecfc9a17a3bdf0e4ee67e5f0cec`

```text
984: There are two basic ways of introducing axioms which do not introduce new syntax or judgmental equalities (function extensionality and univalence are of this form):
985: either add a primitive constant to inhabit the axiom, or prove all theorems which depend on the axiom by hypothesizing a variable that inhabits the axiom, cf.\ \cref{sec:axioms}.
986: While these are essentially equivalent, we opt for the former approach because we feel that the axioms of homotopy type theory are an essential part of the core theory.
987: 
988: \index{function extensionality}%
989: \cref{axiom:funext} is formalized by introduction of a constant $\funext$ which
990: asserts that $\happly$ is an equivalence:
991: %
992: \begin{mathparpagebreakable}
993:   \inferrule*[right=$\Pi$-\textsc{ext}]
994:   {\oftp\Gamma{f}{\tprd{x:A} B} \\
995:    \oftp\Gamma{g}{\tprd{x:A} B}}
996:   {\oftp\Gamma{\funext(f,g)}{\isequiv(\happly_{f,g})}}
997: \end{mathparpagebreakable}
998: %
999: The definitions of $\happly$ and $\isequiv$ can be found in~\eqref{eq:happly} and
1000: \cref{sec:concluding-remarks}, respectively.
1001: 
1002: \index{univalence axiom}%
1003: \cref{axiom:univalence} is formalized in a similar fashion, too:
1004: %
1005: \begin{mathparpagebreakable}
1006:   \inferrule*[right=$\UU_i$-\textsc{univ}]
1007:   {\oftp\Gamma{A}{\UU_i} \\
1008:    \oftp\Gamma{B}{\UU_i}}
1009:   {\oftp\Gamma{\univalence(A,B)}{\isequiv(\idtoeqv_{A,B})}}
```

## ua propositional computation

`HoTT/theory-schema/upstream/book-578b85cc/basics.tex` L1763—1780; SHA256 `516b469d7356e9d20df5539e726a0468760f9fa7b7f440b9c054981e803d7533`

```text
1763: \symlabel{ua}
1764: \begin{itemize}
1765: \item An introduction rule for {(\id[\type]{A}{B})}, denoted $\ua$ for ``univalence axiom'':
1766:   \[
1767:   \ua : ({\eqv A B}) \to (\id[\type]{A}{B}).
1768:   \]
1769: \item The elimination rule, which is $\idtoeqv$,
1770:   \[
1771:   \idtoeqv \jdeq \transfibf{X \mapsto X} : (\id[\type]{A}{B}) \to (\eqv A B).
1772:   \]
1773: \item The propositional computation rule\index{computation rule!propositional!for univalence},
1774:   \[
1775:   \transfib{X \mapsto X}{\ua(f)}{x} = f(x).
1776:   \]
1777: \item The propositional uniqueness principle: \index{uniqueness!principle, propositional!for univalence}
1778:   for any $p : \id A B$,
1779:   \[
1780:   \id{p}{\ua(\transfibf{X \mapsto X}(p))}.
```

## set quotient recursion

`HoTT/theory-schema/upstream/book-578b85cc/hits.tex` L1222—1236; SHA256 `d43dac381da7f978fb1d2ff6c2c2d3cca7f9b0dab90c96cd20815c13e7ab8454`

```text
1222: \begin{lem}\label{thm:quotient-ump}
1223:   For any set $B$, precomposing with $q$ yields an equivalence
1224:   \[ \eqvspaced{(A/R \to B)}{\Parens{\sm{f:A\to B} \prd{a,b:A} R(a,b) \to (f(a)=f(b))}}.\]
1225: \end{lem}
1226: \begin{proof}
1227:   The quasi-inverse of $\blank\circ q$, going from right to left, is just the recursion principle for $A/R$.
1228:   That is, given $f:A\to B$ such that
1229:   \narrowequation{\prd{a,b:A} R(a,b) \to (f(a)=f(b)),} we define $\bar f:A/R\to B$ by $\bar f(q(a))\defeq f(a)$.
1230:   This defining equation says precisely that $(f\mapsto \bar f)$ is a right inverse to $(\blank\circ q)$.
1231: 
1232:   For it to also be a left inverse, we must show that for any $g:A/R\to B$ and $x:A/R$ we have $g(x) = \overline{g\circ q}(x)$.
1233:   However, by \cref{thm:quotient-surjective} there merely exists $a$ such that $q(a)=x$.
1234:   Since our desired equality is a mere proposition, we may assume there purely exists such an $a$, in which case $g(x) = g(q(a)) = \overline{g\circ q}(q(a)) = \overline{g\circ q}(x)$.
1235: \end{proof}
1236: 
```
