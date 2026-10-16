# 实际一手来源摘录

## HoTT/theory-schema/upstream/book-578b85cc/basics.tex
SHA-256: `516b469d7356e9d20df5539e726a0468760f9fa7b7f440b9c054981e803d7533`

### L859–889
```tex
859: \begin{lem}[Dependent map]\label{lem:mapdep}
860:   \indexdef{application!of dependent function to a path}%
861:   \indexdef{path!application of a dependent function to}%
862:   \indexdef{function!dependent!application to a path of}%
863:   \indexdef{action!of a dependent function on a path}%
864:   Suppose $f:\prd{x: A} P(x)$; then we have a map
865:   \[\apdfunc f : \prd{p:x=y}\big(\id[P(y)]{\trans p{f(x)}}{f(y)}\big).\]
866: \end{lem}
867: 
868: \begin{proof}[First proof]
869:   Let $D:\prd{x,y:A} (\id{x}{y}) \to \type$ be the type family defined by
870:   \begin{equation*}
871:     D(x,y,p)\defeq \trans p {f(x)}= f(y).
872:   \end{equation*}
873:   Then $D(x,x,\refl{x})$ is $\trans{(\refl{x})}{f(x)}= f(x)$.
874:   But since $\trans{(\refl{x})}{f(x)}\jdeq f(x)$, we get that $D(x,x,\refl{x})\jdeq (f(x)= f(x))$.
875:   Thus, we find the function
876:   \begin{equation*}
877:     d\defeq\lam{x} \refl{f(x)}:\prd{x:A} D(x,x,\refl{x})
878:   \end{equation*}
879:   and now path induction gives us $\apdfunc f(p):\trans p{f(x)}= f(y)$ for each $p:x= y$.
880: \end{proof}
881: 
882: \begin{proof}[Second proof]
883:   By induction, it suffices to assume $p$ is $\refl x$.
884:   But in this case, the desired equation is $\trans{(\refl{x})}{f(x)}= f(x)$, which holds judgmentally.
885: \end{proof}
886: 
887: We will refer generally to paths which ``lie over other paths'' in this sense as \emph{dependent paths}.
888: \indexsee{dependent!path}{path, dependent}%
889: \index{path!dependent}%
```

### L1426–1475
```tex
1426: \begin{thm}\label{thm:path-sigma}
1427: Suppose that $P:A\to\type$ is a type family over a type $A$ and let $w,w':\sm{x:A}P(x)$. Then there is an equivalence
1428: \begin{equation*}
1429: \eqvspaced{(w=w')}{\dsm{p:\proj{1}(w)=\proj{1}(w')} \trans{p}{\proj{2}(w)}=\proj{2}(w')}.
1430: \end{equation*}
1431: \end{thm}
1432: 
1433: \begin{proof}
1434: We define a function
1435: \begin{equation*}
1436: f : \prd{w,w':\sm{x:A}P(x)} (w=w') \to \dsm{p:\proj{1}(w)=\proj{1}(w')} \trans{p}{\proj{2}(w)}=\proj{2}(w')
1437: \end{equation*}
1438: by path induction, with
1439: \begin{equation*}
1440: f(w,w,\refl{w})\defeq(\refl{\proj{1}(w)},\refl{\proj{2}(w)}).
1441: \end{equation*}
1442: We want to show that $f$ is an equivalence.
1443: 
1444: In the reverse direction, we define
1445: \begin{narrowmultline*}
1446:   g : \prd{w,w':\sm{x:A}P(x)}
1447:       \Parens{\sm{p:\proj{1}(w)=\proj{1}(w')}\trans{p}{\proj{2}(w)}=\proj{2}(w')}
1448:       \to
1449:       \narrowbreak
1450:       (w=w')
1451: \end{narrowmultline*}
1452: by first inducting on $w$ and $w'$, which splits them into $(w_1,w_2)$ and
1453: $(w_1',w_2')$ respectively, so it suffices to show
1454: \begin{equation*}
1455: \Parens{\sm{p:w_1 = w_1'}\trans{p}{w_2}=w_2'} \to ((w_1,w_2)=(w_1',w_2')).
1456: \end{equation*}
1457: Next, given a pair $\sm{p:w_1 = w_1'}\trans{p}{w_2}=w_2'$, we can
1458: use $\Sigma$-induction to get $p : w_1 = w_1'$ and $q :
1459: \trans{p}{w_2}=w_2'$.  Inducting on $p$, we have $q :
1460: \trans{(\refl{w_1})}{w_2}=w_2'$, and it suffices to show
1461: $(w_1,w_2)=(w_1,w_2')$.  But $\trans{(\refl{w_1})}{w_2} \jdeq w_2$, so
1462: inducting on $q$ reduces the goal to
1463: $(w_1,w_2)=(w_1,w_2)$, which we can prove with $\refl{(w_1,w_2)}$.
1464: 
1465: Next we show that $f(g(r))=r$ for all $w$, $w'$ and
1466: $r$, where $r$ has type
1467: \[\dsm{p:\proj{1}(w)=\proj{1}(w')} (\trans{p}{\proj{2}(w)}=\proj{2}(w')).\]
1468: First, we break apart the pairs $w$, $w'$, and $r$ by pair induction, as in the
1469: definition of $g$, and then use two path inductions to reduce both components
1470: of $r$ to \refl{}.  Then it suffices to show that
1471: $f (g(\refl{w_1},\refl{w_2})) = (\refl{w_1},\refl{w_2})$, which is true by definition.
1472: 
1473: Similarly, to show that $g(f(p))=p$ for all $w$, $w'$,
1474: and $p : w = w'$, we can do path induction on $p$, and then pair induction to
1475: split $w$, at which point it suffices to show that
```

### L1763–1780
```tex
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

## HoTT/theory-schema/upstream/book-578b85cc/logic.tex
SHA-256: `76ac2e06ffa133ede0612584fef4b9c81d698d4e0b7a4ec683131448edfed2f2`

### L590–655
```tex
590: Sometimes this is very useful, but if we want a more classical sort of ``or'' that preserves mere propositions, we need a way to ``truncate'' this type into a mere proposition by forgetting this additional information.
591: 
592: \index{quantifier!existential}%
593: The same issue arises with the $\Sigma$-type $\sm{x:A} P(x)$, where $A$ is an arbitrary type.
594: This is a purely constructive interpretation of ``there exists an $x:A$ such that $P(x)$'' which remembers the witness $x$, and hence is not generally a mere proposition even if each type $P(x)$ is.
595: (Recall that we observed in \cref{subsec:prop-subsets} that $\sm{x:A} P(x)$ can also be regarded as ``the subset of those $x:A$ such that $P(x)$''.)
596: 
597: 
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
648:   We define \define{traditional logical notation}
649:   \indexdef{implication}%
650:   \indexdef{traditional logical notation}%
651:   \indexdef{logical notation, traditional}%
652:   \index{quantifier}%
653:   \indexsee{existential quantifier}{quantifier, existential}%
654:   \index{quantifier!existential}%
655:   \indexsee{universal!quantifier}{quantifier, universal}%
```

### L801–838
```tex
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
