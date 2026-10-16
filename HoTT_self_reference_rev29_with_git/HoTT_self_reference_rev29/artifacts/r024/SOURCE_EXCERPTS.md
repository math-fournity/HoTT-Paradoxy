# R024 targeted original-rule excerpts

## HoTT/theory-schema/upstream/book-578b85cc/hits.tex:110-153

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
150: Thus, we hybridize the notations, writing instead $\ap f \lloop \defid \ell$ for this sort of ``propositional equality by definition''.
151: \end{rmk}
152: \index{computation rule!for higher inductive types|)}%
153: \index{computation rule!propositional|)}%

## HoTT/theory-schema/upstream/book-578b85cc/formal.tex:978-1010

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

## HoTT/theory-schema/upstream/book-578b85cc/basics.tex:1624-1645

1624: 
1625: Since the non-dependent function type $A\to B$ is a special case of the dependent function type $\prd{x:A} B(x)$ when $B$ is independent of $x$, everything we have said above applies in non-dependent cases as well.
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

## HoTT/theory-schema/upstream/book-578b85cc/basics.tex:1760-1785

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

## HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex:320-352

320: \subsection{Getting started}
321: \label{sec:pi1s1-initial-thoughts}
322: 
323: It is not too hard to define functions in both directions between $\Omega(\Sn^1)$ and \Z.
324: By specializing \cref{thm:looptothe} to $\lloop:\base=\base$, we have a function $\lloop^{\blank} : \Z \rightarrow (\id{\base}{\base})$ defined (loosely speaking) by
325: \[
326:   \lloop^n =
327:   \begin{cases}
328:     \underbrace{\lloop \ct \lloop \ct \cdots \ct \lloop}_{n}  & \text{if $n > 0$,} \\
329:     \underbrace{\opp \lloop \ct \opp \lloop \ct \cdots \ct \opp \lloop}_{-n} & \text{if $n < 0$,} \\
330:     \refl{\base} & \text{if $n = 0$.}
331: \end{cases}
332: \]
333: %
334: Defining a function $g:\Omega(\Sn^1)\to\Z$ in the other direction is a bit trickier.
335: Note that the successor function $\Zsuc:\Z\to\Z$ is an equivalence,
336: \index{successor!isomorphism on Z@isomorphism on $\Z$}%
337: and hence induces a path $\ua(\Zsuc):\Z=\Z$ in the universe \type.
338: Thus, the recursion principle of $\Sn^1$ induces a map $c:\Sn^1\to\type$ by $c(\base)\defeq \Z$ and $\apfunc c (\lloop) \defid \ua(\Zsuc)$.
339: Then we have $\apfunc{c} : (\base=\base) \to (\Z=\Z)$, and we can define $g(p)\defeq \transfib{X\mapsto X}{\apfunc{c}(p)}{0}$.
340: 
341: With these definitions, we can even prove that $g(\lloop^n)=n$ for any $n:\Z$, using the induction principle \cref{thm:sign-induction} for $n$.
342: (We will prove something more general a little later on.)
343: However, the other equality $\lloop^{g(p)}=p$ is significantly harder.
344: The obvious thing to try is path induction, but path induction does not apply to loops such as $p:(\base=\base)$ that have \emph{both} endpoints fixed!
345: A new idea is required, one which can be explained both in terms of classical homotopy theory and in terms of type theory.
346: We begin with the former.
347: 
348: 
349: \subsection{The classical proof}
350: \label{sec:pi1s1-classical-proof}
351: 
352: \index{classical!homotopy theory|(}%

## HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex:420-461

420: 
421: \begin{defn}[Universal Cover of $\Sn^1$] \label{S1-universal-cover}
422:   Define $\code : \Sn ^1 \to \type$ by circle-recursion, with
423:   \begin{align*}
424:     \code(\base) &\defeq \Z \\
425:     \apfunc{\code}({\lloop}) &\defid \ua(\Zsuc).
426:   \end{align*}
427: \end{defn}
428: 
429: We emphasize briefly the definition of this family, since it is so different from how one usually defines covering spaces in classical homotopy theory.
430: To define a function by circle recursion, we need to find a point and a
431: loop in the codomain.  In this case, the codomain is $\type$, and the point
432: we choose is $\Z$, corresponding to our expectation that the
433: fiber of the universal cover should be the integers.  The loop we choose
434: is the successor/predecessor
435: \index{successor!isomorphism on Z@isomorphism on $\Z$}%
436: \index{predecessor!isomorphism on Z@isomorphism on $\Z$}%
437: isomorphism on $\Z$, which
438: corresponds to the fact that going around the loop in the base goes up
439: one level on the helix.  Univalence is necessary for this part of the
440: proof, because we need to convert a \emph{non-trivial} equivalence on $\Z$ into an identity.
441: 
442: We call this the fibration of ``codes'', because its elements are combinatorial data that act as codes for paths on the circle: the integer $n$ codes for the path which loops around the circle $n$ times.
443: 
444: From this definition, it is simple to calculate that transporting with
445: $\code$ takes $\lloop$ to the successor function, and
446: $\opp{\lloop}$ to the predecessor function:
447: \begin{lem} \label{lem:transport-s1-code}
448: \id{\transfib \code \lloop x} {x + 1} and
449: \id{\transfib \code {\opp \lloop} x} {x - 1}.
450: \end{lem}
451: \begin{proof}
452: For the first equation, we calculate as follows:
453: \begin{align}
454: {\transfib \code \lloop x}
455: &= \transfib {A \mapsto A} {(\ap{\code}{\lloop})} x \tag{by \cref{thm:transport-compose}}\\
456: &= \transfib {A \mapsto A} {\ua (\Zsuc)} x \tag{by computation for $\rec{\Sn^1}$}\\
457: &= x + 1 \tag{by computation for \ua}.
458: \end{align}
459: The second equation follows from the first, because $\transfib{B}{p}{\blank}$ and $\transfib{B}{\opp p}{\blank}$ are always inverses, so $\transfib\code {\opp \lloop}{\blank}$ must be the inverse of $\Zsuc$.
460: \end{proof}
461: 

## HoTT/theory-schema/upstream/book-578b85cc/logic.tex:800-842

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
840: 
841: A similar issue arises in set-theoretic mathematics, although it manifests slightly
842: differently. If we are trying to define a function $f: A \to B$, and depending on an
