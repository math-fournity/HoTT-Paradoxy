# R020 本轮核对的固定书籍规则

原文件未改；以下为精确节选，不冒称全书复核。

## contexts

`HoTT/theory-schema/upstream/book-578b85cc/formal.tex` L487—555; SHA256 `e621484e2e457e70536a92367cca452f34df8ecfc9a17a3bdf0e4ee67e5f0cec`

```text
487: $\oftp{\emptyctx}{\lamu{x:\unit} x}{\unit\to\unit}$.
488: %
489: \begin{mathpar}
490: \inferrule*[right=$\Pi$-\rintro]
491:   {\inferrule*[right=$\Vble$]
492:     {\inferrule*[right=\ctx-\textsc{ext}]
493:       {\inferrule*[right=$\unit$-\rform]
494:         {\inferrule*[right=\ctx-\textsc{emp}]
495:           {\ }
496:           {\wfctx {\emptyctx}}}
497:         {\oftp{}{\unit}{\UU_0}}}
498:       {\wfctx {\tmtp x\unit}}}
499:    {\oftp{\tmtp x\unit}{x}{\unit}}}
500:  {\oftp{\emptyctx}{\lamu{x:\unit} x}{\unit\to\unit}}
501: \end{mathpar}
502: 
503: \subsection{Contexts}
504: \label{subsec:contexts}
505: 
506: \index{context}%
507: A context is a list
508: %
509: \begin{equation*}
510:   \tmtp{x_1}{A_1}, \tmtp{x_2}{A_2}, \ldots, \tmtp{x_n}{A_n}
511: \end{equation*}
512: %
513: which indicates that the distinct variables
514: \index{variable}%
515: $x_1, \ldots, x_n$ are assumed to have types $A_1, \ldots, A_n$, respectively. The list may be empty. We abbreviate contexts with the letters $\Gamma$ and $\Delta$, and we may juxtapose them to form larger contexts.
516: 
517: The judgment $\wfctx{\Gamma}$ formally expresses the fact that $\Gamma$ is a well-formed context, and is governed by the rules of inference
518: %
519: \begin{mathpar}
520:   \inferrule*[right=\ctx-\textsc{emp}]
521:   {\ }
522:   {\wfctx\emptyctx}
523: \and
524:   \inferrule*[right=\ctx-\textsc{ext}]
525:   {\oftp{\tmtp{x_1}{A_1}, \ldots, \tmtp{x_{n-1}}{A_{n-1}}}{A_n}{\UU_i}}
526:   {\wfctx{(\tmtp{x_1}{A_1}, \ldots, \tmtp{x_n}{A_n})}}
527: \end{mathpar}
528: %
529: with a side condition for the second rule: the variable $x_n$ must be distinct from the variables $x_1, \ldots, x_{n-1}$.
530: Note that the hypothesis and conclusion of $\ctx$-\textsc{ext} are judgments of different forms: the hypothesis says that in the context of variables $x_1, \ldots, x_{n-1}$, the expression $A_n$ has type $\UU_i$; while the conclusion says that the extended context $(\tmtp{x_1}{A_1}, \ldots, \tmtp{x_n}{A_n})$ is well-formed.
531: 
532: It is a meta-theoretic property of the system that if any judgment of the form $\oftp{\Gamma}{a}{A}$ or $\jdeqtp\Gamma{a}{a'}{A}$ is derivable, then so is the judgment $\wfctx\Gamma$ that the context $\Gamma$ is well-formed.
533: The premises of all the rules are chosen to include just enough well-formedness hypotheses to make this property provable, but no more.
534: For instance, it is not necessary for $\ctx$-\textsc{ext} to hypothesize well-formedness of $(\tmtp{x_1}{A_1}, \ldots, \tmtp{x_{n-1}}{A_{n-1}})$, as that will follow from the derivability of its premise; but it is necessary for the $\Vble$ rule in the next section to hypothesize well-formedness of its context.
535: This choice is only one of the many possible ways to formulate a type theory precisely, but a detailed investigation of such issues is beyond the scope of this appendix.
536: 
537: \subsection{Structural rules}
538: 
539: \index{structural!rules|(}%
540: \index{rule!structural|(}%
541: 
542: The fact that the context holds assumptions is expressed by the rule which says that we may derive those typing judgments which are listed in the context:
543: %
544: \begin{mathpar}
545:   \inferrule*[right=$\Vble$]
546:   {\wfctx {(\tmtp{x_1}{A_1}, \ldots, \tmtp{x_n}{A_n})} }
547:   {\oftp{\tmtp{x_1}{A_1}, \ldots, \tmtp{x_n}{A_n}}{x_i}{A_i}}
548: \end{mathpar}
549: %
550: As with $\ctx$-\textsc{ext}, the hypothesis and conclusion of the rule $\Vble$ are judgments of different forms, only now they are reversed: we start with a well-formed context and derive a typing judgment.
551: 
552: The following important principles, called \define{substitution}
553: \indexdef{rule!of substitution}%
554: and
555: \define{weakening},
```

## axiomatic univalence

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

## function transport

`HoTT/theory-schema/upstream/book-578b85cc/basics.tex` L1628—1636; SHA256 `516b469d7356e9d20df5539e726a0468760f9fa7b7f440b9c054981e803d7533`

```text
1628: Given a type $X$, a path $p:\id[X]{x_1}{x_2}$, type families $A,B:X\to \type$, and a function $f : A(x_1) \to B(x_1)$,  we have
1629: \begin{align}\label{eq:transport-arrow}
1630:   \transfib{A\to B}{p}{f} &=
1631:   \Big(x \mapsto \transfib{B}{p}{f(\transfib{A}{\opp p}{x})}\Big)
1632: \end{align}
1633: where $A\to B$ denotes abusively the type family $X\to \type$ defined by
1634: \[(A\to B)(x) \defeq (A(x)\to B(x)).\]
1635: In other words, when we transport a function $f:A(x_1)\to B(x_1)$ along a path $p:x_1=x_2$, we obtain the function $A(x_2)\to B(x_2)$ which transports its argument backwards along $p$ (in the type family $A$), applies $f$, and then transports the result forwards along $p$ (in the type family $B$).
1636: This can be proven easily by path induction.
```

## ua and computation

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

## truncation

`HoTT/theory-schema/upstream/book-578b85cc/logic.tex` L598—647; SHA256 `76ac2e06ffa133ede0612584fef4b9c81d698d4e0b7a4ec683131448edfed2f2`

```text
598: \section{Propositional truncation}
599: \label{subsec:prop-trunc}
600: 
601: \index{truncation!propositional|(defstyle}%
602: \indexsee{type!squash}{truncation, propositional}%
603: \indexsee{squash type}{truncation, propositional}%
604: \indexsee{bracket type}{truncation, propositional}%
605: \indexsee{type!bracket}{truncation, propositional}%
606: The \emph{propositional truncation}, also called the \emph{$(-1)$-truncation}, \emph{bracket type}, or \emph{squash type}, is an additional type former which ``squashes'' or ``truncates'' a type down to a mere proposition, forgetting all information contained in inhabitants of that type other than their existence.
607: 
608: More precisely, for any type $A$, there is a type $\brck{A}$.
609: It has two constructors:
610: \begin{itemize}
611: \item For any $a:A$ we have $\bproj a : \brck A$.
612: \item For any $x,y:\brck A$, we have $x=y$.
613: \end{itemize}
614: The first constructor means that if $A$ is inhabited, so is $\brck A$.
615: The second ensures that $\brck A$ is a mere proposition; usually we leave the witness of this fact nameless.
616: 
617: \index{recursion principle!for truncation}%
618: The recursion principle of $\brck A$ says that:
619: \begin{itemize}
620: \item If $B$ is a mere proposition and we have $f:A\to B$, then there is an induced $g:\brck A \to B$ such that $g(\bproj a) \jdeq f(a)$ for all $a:A$.
621: \end{itemize}
622: In other words, any mere proposition which follows from (the inhabitedness of) $A$ already follows from $\brck A$.
623: Thus, $\brck A$, as a mere proposition, contains no more information than the inhabitedness of $A$.
624: (There is also an induction principle for $\brck A$, but it is not especially useful; see \cref{ex:prop-trunc-ind}.)
625: 
626: In \cref{ex:lem-brck,ex:impred-brck,sec:hittruncations} we will describe some ways to construct $\brck{A}$ in terms of more general things.
627: For now, we simply assume it as an additional rule alongside those of \cref{cha:typetheory}.
628: 
629: With the propositional truncation, we can extend the ``logic of mere propositions'' to cover disjunction and the existential quantifier.
630: Specifically, $\brck{A+B}$ is a mere propositional version of ``$A$ or $B$'', which does not ``remember'' the information of which disjunct is true.
631: 
632: The recursion principle of truncation implies that we can still do a case analysis on $\brck{A+B}$ \emph{when attempting to prove a mere proposition}.
633: That is, suppose we have an assumption $u:\brck{A+B}$ and we are trying to prove a mere proposition $Q$.
634: In other words, we are trying to define an element of $\brck{A+B} \to Q$.
635: Since $Q$ is a mere proposition, by the recursion principle for propositional truncation, it suffices to construct a function $A+B\to Q$.
636: But now we can use case analysis on $A+B$.
637: 
638: Similarly, for a type family $P:A\to\type$, we can consider $\brck{\sm{x:A} P(x)}$, which is a mere propositional version of ``there exists an $x:A$ such that $P(x)$''.
639: As for disjunction, by combining the induction principles of truncation and $\Sigma$-types, if we have an assumption of type $\brck{\sm{x:A} P(x)}$, we may introduce new assumptions $x:A$ and $y:P(x)$ \emph{when attempting to prove a mere proposition}.
640: In other words, if we know that there exists some $x:A$ such that $P(x)$, but we don't have a particular such $x$ in hand, then we are free to make use of such an $x$ as long as we aren't trying to construct anything which might depend on the particular value of $x$.
641: Requiring the codomain to be a mere proposition expresses this independence of the result on the witness, since all possible inhabitants of such a type must be equal.
642: 
643: For the purposes of set-level mathematics in \cref{cha:real-numbers,cha:set-math},
644: where we deal mostly with sets and mere propositions, it is convenient to use the
645: traditional logical notations to refer only to ``propositionally truncated logic''.
646: 
647: \begin{defn} \label{defn:logical-notation}
```

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

## circle constructors

`HoTT/theory-schema/upstream/book-578b85cc/hits.tex` L13—35; SHA256 `d43dac381da7f978fb1d2ff6c2c2d3cca7f9b0dab90c96cd20815c13e7ab8454`

```text
13: Like the general inductive types we discussed in \cref{cha:induction}, \emph{higher inductive types} are a general schema for defining new types generated by some constructors.
14: But unlike ordinary inductive types, in defining a higher inductive type we may have ``constructors'' which generate not only \emph{points} of that type, but also \emph{paths} and higher paths in that type.
15: \index{type!circle}%
16: \indexsee{circle type}{type,circle}%
17: For instance, we can consider the higher inductive type $\Sn^1$ generated by
18: \begin{itemize}
19: \item A point $\base:\Sn^1$, and
20: \item A path $\lloop : {\id[\Sn^1]\base\base}$.
21: \end{itemize}
22: This should be regarded as entirely analogous to the definition of, for instance, $\bool$, as being generated by
23: \begin{itemize}
24: \item A point $\bfalse:\bool$ and
25: \item A point $\btrue:\bool$,
26: \end{itemize}
27: or the definition of $\nat$ as generated by
28: \begin{itemize}
29: \item A point $0:\nat$ and
30: \item A function $\suc:\nat\to\nat$.
31: \end{itemize}
32: When we think of types as higher groupoids, the more general notion of ``generation'' is very natural:
33: since a higher groupoid is a ``multi-sorted object'' with paths and higher paths as well as points, we should allow ``generators'' in all dimensions.
34: 
35: We will refer to the ordinary sort of constructors (such as $\base$) as \define{point constructors}
```

## HIT computation

`HoTT/theory-schema/upstream/book-578b85cc/hits.tex` L108—149; SHA256 `d43dac381da7f978fb1d2ff6c2c2d3cca7f9b0dab90c96cd20815c13e7ab8454`

```text
108: When we describe a higher inductive type such as the circle as being generated by certain constructors, we have to explain what this means by giving rules analogous to those for the basic type constructors from \cref{cha:typetheory}.
109: The constructors themselves give the \emph{introduction} rules, but it requires a bit more thought to explain the \emph{elimination} rules, i.e.\ the induction and recursion principles.
110: In this book we do not attempt to give a general formulation of what constitutes a ``higher inductive definition'' and how to extract the elimination rule from such a definition --- indeed, this is a subtle question and the subject of current research.
111: Instead we will rely on some general informal discussion and numerous examples.
112: 
113: \index{type!circle}%
114: \index{recursion principle!for S1@for $\Sn^1$}%
115: The recursion principle is usually easy to describe: given any type equipped with the same structure with which the constructors equip the higher inductive type in question, there is a function which maps the constructors to that structure.
116: For instance, in the case of $\Sn^1$, the recursion principle says that given any type $B$ equipped with a point $b:B$ and a path $\ell:b=b$, there is a function $f:\Sn^1\to B$ such that $f(\base)=b$ and $\apfunc f (\lloop) = \ell$.
117: 
118: \index{computation rule!for S1@for $\Sn^1$}%
119: \index{equality!definitional}%
120: The latter two equalities are the \emph{computation rules}.
121: \index{computation rule!for higher inductive types|(}%
122: \index{computation rule!propositional|(}%
123: There is, however, a question of whether these computation rules are judgmental\index{judgmental equality} equalities or propositional equalities (paths).
124: For ordinary inductive types, we had no qualms about making them judgmental, although we saw in \cref{cha:induction} that making them propositional would still yield the same type up to equivalence.
125: In the ordinary case, one may argue that the computation rules are really \emph{definitional} equalities, in the intuitive sense described in the Introduction.
126: 
127: \index{equality!judgmental}%
128: For higher inductive types, this is less clear. %, and it is likewise less clear to what extent these equalities can be made judgmental in the known set-theoretic models.
129: Moreover, since the operation $\apfunc f$ is not really a fundamental part of the type theory, but something that we \emph{defined} using the induction principle of identity types (and which we might have defined in some other, equivalent, way), it seems inappropriate to refer to it explicitly in a \emph{judgmental} equality.
130: Judgmental equalities are part of the deductive system, which should not depend on particular choices of definitions that we may make \emph{within} that system.
131: There are also semantic and implementation issues to consider; see the Notes.
132: 
133: It does seem unproblematic to make the computational rules for the \emph{point} constructors of a higher inductive type judgmental.
134: In the example above, this means we have $f(\base)\jdeq b$, judgmentally.
135: This choice facilitates a computational view of higher inductive types.
136: Moreover, it also greatly simplifies our lives, since otherwise the second computation rule $\apfunc f (\lloop) = \ell$ would not even be well-typed as a propositional equality; we would have to compose one side or the other with the specified identification of $f(\base)$ with $b$.
137: (Such problems do arise eventually, of course, when we come to talk about paths of higher dimension, but that will not be of great concern to us here.
138: See also \cref{sec:hubs-spokes}.)
139: Thus, we take the computation rules for point constructors to be judgmental, and those for paths and higher paths to be propositional.%
140: \footnote{In particular, in the language of \cref{sec:types-vs-sets}, this means that our higher inductive types are a mix of \emph{rules} (specifying how we can introduce such types and their elements, their induction principle, and their computation rules for point constructors) and \emph{axioms} (the computation rules for path constructors, which assert that certain identity types are inhabited by otherwise unspecified terms).
141: We may hope that eventually, there will be a better type theory in which higher inductive types, like univalence, will be presented using only rules and no axioms.%
142: \indexfoot{axiom!versus rules}%
143: \indexfoot{rule!versus axioms}%
144: }
145: 
146: \begin{rmk}\label{rmk:defid}
147: Recall that for ordinary inductive types, we regard the computation rules for a recursively defined function as not merely judgmental equalities, but \emph{definitional} ones, and thus we may use the notation $\defeq$ for them.
148: For instance, the truncated predecessor\index{predecessor!function, truncated} function $p:\nat\to\nat$ is defined by $p(0)\defeq 0$ and $p(\suc(n))\defeq n$.
149: In the case of higher inductive types, this sort of notation is reasonable for the point constructors (e.g.\ $f(\base)\defeq b$), but for the path constructors it could be misleading, since equalities such as $\ap f \lloop = \ell$ are not judgmental.
```

## quotient recursor

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
