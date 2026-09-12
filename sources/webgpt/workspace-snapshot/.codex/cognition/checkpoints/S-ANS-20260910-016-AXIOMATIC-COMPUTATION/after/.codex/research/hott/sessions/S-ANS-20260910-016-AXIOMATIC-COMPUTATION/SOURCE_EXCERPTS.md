# R016 实际原始来源摘录

固定项目Book版本，不是2026领域现状调查。

## HoTT/theory-schema/upstream/book-578b85cc/formal.tex:984—1009

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

## HoTT/theory-schema/upstream/book-578b85cc/formal.tex:1135—1195

```text
1135:     k &\production x \mid k(v) \mid f(\vec{v})(k),
1136:   \end{align*}
1137:   % 
1138:   where $f(\vec{v})$ represents a partial application of the defined function $f$.
1139:   In particular, a type in normal form is of the form $k$ or $c(\vec{v})$.
1140: \end{lem}
1141: 
1142: \begin{thm}
1143:   If $A$ is in normal form then the 
1144:   judgment $A : \UU$ is decidable. If $A : \UU$ and $t$ is in normal form then the judgment
1145:   $t:A$ is decidable.
1146: \end{thm}
1147: 
1148: Logical consistency\index{consistency} (of the system in \cref{sec:syntax-informally}) follows
1149: immediately: if we had $a:\emptyt$ in the empty context, then by
1150: \cref{thm:conversion-preserves-typing,thm:strong-normalization}, $a$
1151: simplifies to a normal term $a':\emptyt$. But by
1152: \cref{lem:normal-forms} no such term exists.
1153: 
1154: \begin{cor}
1155:  The system in \cref{sec:syntax-informally} is logically consistent.
1156: \end{cor}
1157: 
1158: Similarly, we have the \emph{canonicity}\indexdef{canonicity} property that if $a:\N$ in the empty
1159: context, then $a$ simplifies to a normal term $\suc^k(0)$ for some numeral $k$.
1160: 
1161: \begin{cor}
1162:  The system in \cref{sec:syntax-informally} has the canonicity property.
1163: \end{cor}
1164: 
1165: Finally, if $a,A$ are in normal form, it is \emph{decidable} whether $a:A$; in
1166: other words, because type-checking amounts to verifying the correctness of a
1167: proof, this means we can always ``recognize a correct proof when we see one''.
1168: 
1169: \begin{cor}
1170: The property of being a proof in the system in \cref{sec:syntax-informally} is decidable.
1171: \end{cor}
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
1193: the introduction to this book.
1194: 
1195: \index{metatheory|)}%
```

## HoTT/theory-schema/upstream/book-578b85cc/basics.tex:1740—1788

```text
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
1786:   \refl{A} &= \ua(\idfunc[A]) \\
1787:   \ua(f) \ct \ua(g) &= \ua(g\circ f) \\
1788:   \opp{\ua(f)} &= \ua(f^{-1}).
```
