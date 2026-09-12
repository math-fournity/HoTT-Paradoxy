# R021 本地固定规则摘录

这些是已有源码的定点回查，不声称本轮完整重审全书。

## HoTT/theory-schema/upstream/book-578b85cc/logic.tex

SHA-256: `76ac2e06ffa133ede0612584fef4b9c81d698d4e0b7a4ec683131448edfed2f2`

```text
358: With the notion of mere proposition in hand, we can now give the proper formulation of the \define{law of excluded middle}
359: \indexdef{excluded middle}%
360: \indexsee{axiom!excluded middle}{excluded middle}%
361: \indexsee{law!of excluded middle}{excluded middle}%
362: in homotopy type theory:
363: \begin{equation}
364:   \label{eq:lem}
365:   \LEM{}\;\defeq\;
366:   \prd{A:\UU} \Big(\isprop(A) \to (A + \neg A)\Big).
367: \end{equation}
368: Similarly, the \define{law of double negation}
369: \indexdef{double negation, law of}%
370: \indexdef{axiom!double negation}%
371: \indexdef{law!of double negation}%
372: is
373: \begin{equation}
374:   \label{eq:ldn}
375:   % \mathsf{DN}\;\defeq\;
376:   \prd{A:\UU} \Big(\isprop(A) \to (\neg\neg A \to A)\Big).
377: \end{equation}
378: The two are also easily seen to be equivalent to each other --- see \cref{ex:lem-ldn} --- so from now on we will generally speak only of \LEM{}.
379: 
380: This formulation of \LEM{} avoids the ``paradoxes'' of \cref{thm:not-dneg,thm:not-lem}, since \bool is not a mere proposition.
381: In order to distinguish it from the more general propositions-as-types formulation, we rename the latter:
382: \symlabel{lem-infty}
383: \begin{equation*}
384:   \LEM\infty \defeq \prd{A:\UU} (A + \neg A).
385: \end{equation*}
386: For emphasis, the proper version~\eqref{eq:lem}
387: may be denoted $\LEM{-1}$;
388: see also \cref{ex:lemnm}.
389: Although $\LEM{}$
390: is not a consequence of the basic type theory described in \cref{cha:typetheory}, it may be consistently assumed as an axiom (unlike its $\infty$-counterpart).
391: For instance, we will assume it in \cref{sec:wellorderings}.
392: 
393: However, it can be surprising how far we can get without using \LEM{}.
394: Quite often, a simple reformulation of a definition or theorem enables us to avoid invoking excluded middle.
395: While this takes a little getting used to sometimes, it is often worth the hassle, resulting in more elegant and more general proofs.
396: We discussed some of the benefits of this in the introduction.
397: 
398: For instance, in classical\index{mathematics!classical} mathematics, double negations are frequently used unnecessarily.
399: A very simple example is the common assumption that a set $A$ is ``nonempty'', which literally means it is \emph{not} the case that $A$ contains \emph{no} elements.
400: Almost always what is really meant is the positive assertion that $A$ \emph{does} contain at least one element, and by removing the double negation we make the statement less dependent on \LEM{}.
401: Recall that we say that a type $A$ is \emph{inhabited}
402: \index{inhabited type}%
403: when we assert $A$ itself as a proposition (i.e.\ we construct an element of $A$, usually unnamed).
404: Thus, often when translating a classical proof into constructive logic, we replace the word ``nonempty'' by ``inhabited'' (although sometimes we must replace it instead by ``merely inhabited''; see \cref{subsec:prop-trunc}).
405: 
406: Similarly, it is not uncommon in classical mathematics to find unnecessary proofs by contradiction.
407: \index{proof!by contradiction}%
408: Of course, the classical form of proof by contradiction proceeds by way of the law of double negation: we assume $\neg A$ and derive a contradiction, thereby deducing $\neg \neg A$, and thus by double negation we obtain $A$.
409: However, often the derivation of a contradiction from $\neg A$ can be rephrased slightly so as to yield a direct proof of $A$, avoiding the need for \LEM{}.
410: 
411: It is also important to note that if the goal is to prove a \emph{negation}\index{negation}, then ``proof by contradiction'' does not involve \LEM{}.
412: In fact, since $\neg A$ is by definition the type $A\to\emptyt$, by definition to prove $\neg A$ is to prove a contradiction (\emptyt) under the assumption of $A$.
413: Similarly, the law of double negation does hold for negated propositions: $\neg\neg\neg A \to \neg A$.
414: With practice, one learns to distinguish more carefully between negated and non-negated propositions and to notice when \LEM{} is being used and when it is not.
415: 
416: Thus, contrary to how it may appear on the surface, doing mathematics ``constructively'' does not usually involve giving up important theorems, but rather finding the best way to state the definitions so as to make the important theorems constructively provable.
417: That is, we may freely use the \LEM{} when first investigating a subject, but once that subject is better understood, we can hope to refine its definitions and proofs so as to avoid that axiom.
418: % For instance, the theory of ordinal numbers, which classically makes heavy use of \LEM{}, works quite well constructively once we choose the correct definition of ``ordinal''; see \cref{sec:ordinals}.
```

```text
797: 
798: \index{denial|)}%
799: \index{axiom!of choice|)}%
800: 
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
839: An example can be found in \cref{ex:decidable-choice}.
```

## HoTT/theory-schema/upstream/book-578b85cc/basics.tex

SHA-256: `516b469d7356e9d20df5539e726a0468760f9fa7b7f440b9c054981e803d7533`

```text
1626: \index{transport!in function types}%
1627: The rules for transport, however, are somewhat simpler in the non-dependent case.
1628: Given a type $X$, a path $p:\id[X]{x_1}{x_2}$, type families $A,B:X\to \type$, and a function $f : A(x_1) \to B(x_1)$,  we have
1629: \begin{align}\label{eq:transport-arrow}
1630:   \transfib{A\to B}{p}{f} &=
1631:   \Big(x \mapsto \transfib{B}{p}{f(\transfib{A}{\opp p}{x})}\Big)
1632: \end{align}
1633: where $A\to B$ denotes abusively the type family $X\to \type$ defined by
1634: \[(A\to B)(x) \defeq (A(x)\to B(x)).\]
1635: In other words, when we transport a function $f:A(x_1)\to B(x_1)$ along a path $p:x_1=x_2$, we obtain the function $A(x_2)\to B(x_2)$ which transports its argument backwards along $p$ (in the type family $A$), applies $f$, and then transports the result forwards along $p$ (in the type family $B$).
1636: This can be proven easily by path induction.
1637: 
1638: \index{transport!in dependent function types}%
1639: Transporting dependent functions is similar, but more complicated.
1640: Suppose given $X$ and $p$ as before, type families $A:X\to \type$ and $B:\prd{x:X} (A(x)\to\type)$, and also a dependent function $f : \prd{a:A(x_1)} B(x_1,a)$.
1641: Then for $a:A(x_2)$, we have
1642: \begin{narrowmultline*}
1643:   \transfib{\Pi_A(B)}{p}{f}(a) = \narrowbreak
1644:   \Transfib{\widehat{B}}{\opp{(\pairpath(\opp{p},\refl{ \trans{\opp p}{a} }))}}{f(\transfib{A}{\opp p}{a})}
1645: \end{narrowmultline*}
1646: where $\Pi_A(B)$ and $\widehat{B}$ denote respectively the type families
1647: \begin{equation}\label{eq:transport-arrow-families}
1648: \begin{array}{rclcl}
1649: \Pi_A(B) &\defeq& \big(x\mapsto \prd{a:A(x)} B(x,a) \big) &:& X\to \type\\
1650: \widehat{B} &\defeq& \big(w \mapsto B(\proj1w,\proj2w) \big) &:& \big(\sm{x:X} A(x)\big) \to \type.
1651: \end{array}
1652: \end{equation}
1653: If these formulas look a bit intimidating, don't worry about the details.
1654: The basic idea is just the same as for the non-dependent function type: we transport the argument backwards, apply the function, and then transport the result forwards again.
```

```text
1738: \begin{axiom}[Univalence]\label{axiom:univalence}
1739:   \indexdef{univalence axiom}%
1740:   \indexsee{axiom!univalence}{univalence axiom}%
1741:   For any $A,B:\type$, the function~\eqref{eq:uidtoeqv} is an equivalence.
1742: \end{axiom}
1743: 
1744: In particular, therefore, we have
1745:   \[
1746: \eqv{(\id[\type]{A}{B})}{(\eqv A B)}.
1747: \]
1748: 
1749: Technically, the univalence axiom is a statement about a particular universe type $\UU$.
1750: If a universe $\UU$ satisfies this axiom, we say that it is \define{univalent}.
1751: \indexdef{type!universe!univalent}%
1752: \indexdef{univalent universe}%
1753: Except when otherwise noted (e.g.\ in \cref{sec:univalence-implies-funext}) we will assume that \emph{all} universes are univalent.
1754: 
1755: \begin{rmk}
1756:   It is important for the univalence axiom that we defined $\eqv AB$ using a ``good'' version of $\isequiv$ as described in \cref{sec:basics-equivalences}, rather than (say) as $\sm{f:A\to B} \qinv(f)$.
1757:   See \cref{ex:qinv-univalence}.
1758: \end{rmk}
1759: 
1760: In particular, univalence means that \emph{equivalent types may be identified}.
1761: As we did in previous sections, it is useful to break this equivalence into:
1762: %
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
1781:   \]
1782: \end{itemize}
1783: %
1784: We can also identify the reflexivity, concatenation, and inverses of equalities in the universe with the corresponding operations on equivalences:
1785: \begin{align*}
```

## HoTT/theory-schema/upstream/book-578b85cc/formal.tex

SHA-256: `e621484e2e457e70536a92367cca452f34df8ecfc9a17a3bdf0e4ee67e5f0cec`

```text
978: In this section we state the additional axioms of homotopy type theory which distinguish it from standard Martin-L\"{o}f type theory: function extensionality, the
979: univalence axiom, and higher inductive types. We state them in the style
980: of the second presentation \cref{sec:syntax-more-formally}, although the first presentation \cref{sec:syntax-informally} could be used just as well.
981: 
982: \subsection{Function extensionality and univalence}
983: 
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
1010: \end{mathparpagebreakable}
1011: %
1012: The definition of $\idtoeqv$ can be found in~\eqref{eq:uidtoeqv}.
1013: 
1014: \subsection{The circle}
1015: 
```

```text
1172: 
1173: \mentalpause
1174: 
1175: The above results do not apply to the extended system of homotopy type
1176: theory (i.e., the above system extended by \cref{sec:hott-features}), since
1177: occurrences of the univalence axiom and constructors of higher inductive types
1178: never simplify, breaking \cref{lem:normal-forms}. It is an open question\index{open!problem}
1179: whether one can simplify applications of these constants in order to restore
1180: canonicity. We also do not have a schema describing all permissible higher
1181: inductive types, nor are we certain how to correctly formulate their rules
1182: (e.g., whether the computation rules on higher constructors should be judgmental
1183: equalities).
1184: 
1185: The consistency\index{consistency} of Martin-L\"{o}f type theory extended with univalence and higher
1186: inductive types could be shown by inventing an appropriate normalization procedure, but currently
1187: the only proofs that these systems are consistent are via semantic models --- for
1188: univalence, a model in Kan\index{Kan complex} complexes due to Voevodsky \cite{klv:ssetmodel}, and
1189: for higher inductive types, a model due to Lumsdaine and Shulman \cite{ls:hits}.
1190: 
1191: Other metatheoretic issues, and a summary of our current results, are discussed
1192: in greater length in the ``Constructivity'' and ``Open problems'' sections of
```
