

===== SOURCE HoTT/theory-schema/upstream/book-578b85cc/setmath.tex | SHA256 c9684dffba31892b12839e60eac769706faa2301b7fba7b930f5acf4b097563e | LINES 1-1970/1970 =====
\chapter{Set theory}
\label{cha:set-math}

\index{set|(}%

Our conception of sets as types with particularly simple homotopical character, cf.\
\cref{sec:basics-sets}, is quite different from the sets of Zermelo--Fraenkel\index{set theory!Zermelo--Fraenkel} set theory, which form a
cumulative hierarchy with an intricate nested membership structure.
For many mathematical purposes, the homotopy-the\-o\-ret\-ic sets are just as good as
the Zermelo--Fraenkel ones, but there are important differences.

We begin this chapter in \cref{sec:piw-pretopos} by showing that the category $\uset$ has (most of) the usual properties of the category of sets.
\index{mathematics!constructive}%
\index{mathematics!predicative}%
In constructive, predicative, univalent foundations, it is a ``$\Pi\mathsf{W}$-pretopos''; whereas if we assume propositional resizing
\index{propositional!resizing}%
(\cref{subsec:prop-subsets}) it is an elementary topos,\index{topos} and if we assume \LEM{} and \choice{} then it is a model of Lawvere's \emph{Elementary Theory of the Category of Sets}\index{Lawvere}.
\index{Elementary Theory of the Category of Sets}%
This is sufficient to ensure that the sets in homotopy type theory behave like sets as used by most mathematicians outside of set theory.

In the rest of the chapter, we investigate some subjects that traditionally belong to ``set theory''.
In \cref{sec:cardinals,sec:ordinals,sec:wellorderings} we study cardinal and ordinal numbers.
These are traditionally defined in set theory using the global membership relation, but we will see that the univalence axiom enables an equally convenient, more ``structural'' approach.

Finally, in \cref{sec:cumulative-hierarchy} we consider the possibility of constructing \emph{inside} of homotopy type theory a cumulative hierarchy of sets, equipped with a binary membership relation akin to that of Zermelo--Fraenkel set theory.
This combines higher inductive types with ideas from the field of algebraic set theory.
\index{algebraic set theory}%
\index{set theory!algebraic}%

In this chapter we will often use the traditional logical notation described in \cref{subsec:prop-trunc}.
In addition to the basic theory of \cref{cha:basics,cha:logic}, we use higher inductive types for colimits and quotients as in \cref{sec:colimits,sec:set-quotients}, as well as some of the theory of truncation from \cref{cha:hlevels}, particularly the factorization system of \cref{sec:image-factorization} in the case $n=-1$.
In \cref{sec:ordinals} we use an inductive family (\cref{sec:generalizations}) to describe well-foundedness, and in \cref{sec:cumulative-hierarchy} we use a more complicated higher inductive type to present the cumulative hierarchy.


%\section{\texorpdfstring{$\set$}{Set} is a \texorpdfstring{$\Pi$}{Π}W-pretopos}
\section{The category of sets}
\label{sec:piw-pretopos}

Recall that in \cref{cha:category-theory} we defined the category \uset to consist of all $0$-types (in some universe \UU) and maps between them, and observed that it is a category (not just a precategory).
We consider successively the levels of structure which \uset possesses.

\subsection{Limits and colimits}
\label{subsec:limits-sets}

\index{limit!of sets}%
\index{colimit!of sets}%

Since sets are closed under products, the universal property of products in \cref{thm:prod-ump} shows immediately that \uset has finite products.
In fact, infinite products follow just as easily from the equivalence
\[ \Parens{X\to \prd{a:A} B(a)} \eqvsym \Parens{\prd{a:A} (X\to B(a))}.\]
And we saw in \cref{ex:pullback}\index{pullback} that the pullback of $f:A\to C$ and $g:B\to C$ can be defined as $\sm{a:A}{b:B} f(a)=g(b)$; this is a set if $A,B,C$ are and inherits the correct universal property.
Thus, \uset is a \emph{complete} category in the obvious sense.
\index{category!complete}%
\index{complete!category}%

Since sets are closed under $+$ and contain \emptyt, \uset has finite coproducts.
Similarly, since $\sm{a:A}B(a)$ is a set whenever $A$ and each $B(a)$ are, it yields a coproduct of the family $B$ in \uset.
Finally, we showed in \cref{sec:pushouts} that pushouts exist in $n$-types, which includes \uset in particular.
Thus, \uset is also \emph{cocomplete}.
\index{category!cocomplete}%
\index{cocomplete category}%

\subsection{Images}
\label{sec:image}

%We will show that $\uset$ is a $\Pi$W-pretopos.
Next, we show that $\uset$ is a \define{regular category}, i.e.:
\indexdef{category!regular}%
\indexdef{regular!category}%
%
\begin{enumerate}
\item $\uset$ is finitely complete.\label{item:reg1}
\item The kernel pair $\proj1,\proj2: (\sm{x,y:A} f(x)= f(y)) \to A$ of any
  function $f : A \to B$ has a coequalizer.\label{item:reg2}
  \indexdef{kernel!pair}
\item Pullbacks of regular epimorphisms are again regular epimorphisms.\label{item:reg3}
\end{enumerate}
%
Recall that a \define{regular epimorphism}
\indexdef{epimorphism!regular}%
\indexdef{regular!epimorphism}%
is a morphism that is the coequalizer of \emph{some} pair of maps.
Thus in~\ref{item:reg3} the pullback of a coequalizer is required to again be a coequalizer, but not necessarily of the pulled-back pair.

\index{set-coequalizer}%
\index{image}
The obvious candidate for the coequalizer of the kernel pair of $f:A\to B$ is the \emph{image} of $f$, as defined in \cref{sec:image-factorization}.
Recall that we defined $\im(f)\defeq \sm{b:B} \brck{\hfib f b}$, with functions
$\tilde{f}:A\to\im(f)$ and $i_f:\im(f)\to B$ defined by
\begin{align*}
  \tilde{f} & \defeq \lam{a} \Pairr{f(a),\,\bproj{\pairr{a,\refl{f(a)}}}}\\
i_f & \defeq \proj1
\end{align*}
fitting into a diagram:
\begin{equation*}
  \xymatrix{
    **[l]{\sm{x,y:A} f(x)= f(y)}
    \ar@<0.25em>[r]^{\proj1}
    \ar@<-0.25em>[r]_{\proj2}
    &
    {A}
    \ar[r]^(0.4){\tilde{f}}
    \ar[rd]_{f}
    &
    {\im(f)}
    \ar@{..>}[d]^{i_f}
    \\ & &
    B
  }
\end{equation*}

Recall that a function $f:A\to B$ is called \emph{surjective} if
\index{function!surjective}%
\narrowequation{\fall{b:B}\brck{\hfib f b},}
or equivalently $\fall{b:B} \exis{a:A} f(a)=b$.
We have also said that a function $f:A\to B$ between sets is called \emph{injective} if
\index{function!injective}%
$\fall{a,a':A} (f(a) = f(a')) \Rightarrow (a=a')$, or equivalently if each of its fibers is a mere proposition.
Since these are the $(-1)$-connected and $(-1)$-truncated maps in the sense of \cref{cha:hlevels}, the general theory there implies that $\tilde f$ above is surjective and $i_f$ is injective, and that this factorization is stable under pullback.

We now identify surjectivity and injectivity with the appropriate cat\-e\-go\-ry-theoretic notions.
First we observe that categorical monomorphisms and epimorphisms have a slightly stronger equivalent formulation.

\begin{lem}\label{thm:mono}
  For a morphism $f:\hom_A(a,b)$ in a category $A$, the following are equivalent.
  \begin{enumerate}
  \item $f$ is a \define{monomorphism}:
    \indexdef{monomorphism}%
    for all $x:A$ and ${g,h:\hom_A(x,a)}$, if $f\circ g = f\circ h$ then $g=h$.\label{item:mono1}
  \item (If $A$ has pullbacks) the diagonal map $a\to a\times_b a$ is an isomorphism.\label{item:mono4}
  \item For all $x:A$ and $k:\hom_A(x,b)$, the type $\sm{h:\hom_A(x,a)} (k = f\circ h)$ is a mere proposition.\label{item:mono2}
  \item For all $x:A$ and ${g:\hom_A(x,a)}$, the type $\sm{h:\hom_A(x,a)} (f\circ g = f\circ h)$ is contractible.\label{item:mono3}
  \end{enumerate}
\end{lem}
\begin{proof}
  The equivalence of conditions~\ref{item:mono1} and~\ref{item:mono4} is standard category theory.
  Now consider the function $(f\circ \blank ):\hom_A(x,a) \to \hom_A(x,b)$ between sets.
  Condition~\ref{item:mono1} says that it is injective, while~\ref{item:mono2} says that its fibers are mere propositions; hence they are equivalent.
  And~\ref{item:mono2} implies~\ref{item:mono3} by taking $k\defeq f\circ g$ and recalling that an inhabited mere proposition is contractible.
  Finally,~\ref{item:mono3} implies~\ref{item:mono1} since if $p:f\circ g= f\circ h$, then $(g,\refl{})$ and $(h,p)$ both inhabit the type in~\ref{item:mono3}, hence are equal and so $g=h$.
\end{proof}

\begin{lem}\label{thm:inj-mono}
  A function $f:A\to B$ between sets is injective if and only if it is a monomorphism\index{monomorphism} in \uset.
\end{lem}
\begin{proof}
  Left to the reader.
\end{proof}

Of course, an \define{epimorphism}
\indexdef{epimorphism}%
\indexsee{epi}{epimorphism}%
is a monomorphism in the opposite category.
We now show that in \uset, the epimorphisms are precisely the surjections, and also precisely the coequalizers (regular epimorphisms).

The coequalizer of a pair of maps $f,g:A\to B$ in $\uset$ is defined as the 0-truncation of a general (homotopy) coequalizer.
For clarity, we may call this the \define{set-coequalizer}.
\indexdef{set-coequalizer}%
\indexsee{coequalizer!of sets}{set-coequalizer}%
It is convenient to express its universal property as follows.

\begin{lem}
\index{universal!property!of set-coequalizer}%
Let $f,g:A\to B$ be functions between sets $A$ and $B$. The
{set-co}equalizer $c_{f,g}:B\to Q$ has the property that, for any set $C$ and any $h:B\to C$ with $h\circ f = h\circ g$, the type
\begin{equation*}
\sm{k:Q\to C} (k\circ c_{f,g} = h)
\end{equation*}
is contractible.
\end{lem}

\begin{lem}\label{epis-surj}
For any function $f:A\to B$ between sets, the following are equivalent:
\begin{enumerate}
\item $f$ is an epimorphism.
\item Consider the pushout diagram
\begin{equation*}
  \xymatrix{
    {A}
    \ar[r]^{f}
    \ar[d]
    &
    {B}
    \ar[d]^{\iota}
    \\
    {\unit}
    \ar[r]_{t}
    &
    {C_f}
  }
\end{equation*}
in $\uset$ defining the mapping cone\index{cone!of a function}. Then the type $C_f$ is contractible.
\item $f$ is surjective.
\end{enumerate}
\end{lem}

\begin{proof}
Let $f:A\to B$ be a function between sets, and suppose it to be an epimorphism; we show $C_f$ is contractible.
The constructor $\unit\to C_f$ of $C_f$ gives us an element $t:C_f$.
We have to show that
\begin{equation*}
\prd{x:C_f} x= t.
\end{equation*}
Note that $x= t$ is a mere proposition, hence we can use induction on $C_f$.
Of course when $x$ is $t$ we have $\refl{t}:t=t$, so it suffices to find
\begin{align*}
I_0 & : \prd{b:B} \iota(b)= t\\
I_1 & : \prd{a:A} \opp{\alpha_1(a)} \ct I_0(f(a))=\refl{t}
\end{align*}
where $\iota:B\to C_f$ and $\alpha_1:\prd{a:A} \iota(f(a))= t$ are the other constructors
of $C_f$. Note that $\alpha_1$ is a homotopy from $\iota\circ f$ to
$\mathsf{const}_t\circ f$, so we find the elements
\begin{equation*}
\pairr{\iota,\refl{\iota\circ f}},\pairr{\mathsf{const}_t,\alpha_1}:
\sm{h:B\to C_f} \iota\circ f \htpy h\circ f.
\end{equation*}
By the dual of \cref{thm:mono}\ref{item:mono3} (and function extensionality), there is a path
\begin{equation*}
\gamma:\pairr{\iota,\refl{\iota\circ f}}=\pairr{\mathsf{const}_t,\alpha_1}.
\end{equation*}
Hence, we may define $I_0(b)\defeq \happly(\projpath1(\gamma),b):\iota(b)=t$.
We also have
\[\projpath2(\gamma) : \trans{\projpath1(\gamma)}{\refl{\iota\circ f}} = \alpha_1. \]
This transport involves precomposition with $f$, which commutes with $\happly$.
Thus, from transport in path types we obtain $I_0(f(a)) = \alpha_1(a)$ for any $a:A$, which gives us $I_1$.

Now suppose $C_f$ is contractible; we show $f$ is surjective.
We first construct a type family $P:C_f\to\prop$ by recursion on $C_f$, which is valid since \prop is a set.
On the point constructors, we define
\begin{align*}
P(t) & \defeq \unit\\
P(\iota(b)) & \defeq \brck{\hfiber{f}b}.
\end{align*}
To complete the construction of $P$, it remains to give a path
\narrowequation{\brck{\hfiber{f}{f(a)}} =_\prop \unit}
for all $a:A$.
However, $\brck{\hfiber{f}{f(a)}}$ is inhabited by $(f(a),\refl{f(a)})$.
Since it is a mere proposition, this means it is contractible --- and thus equivalent, hence equal, to \unit.
This completes the definition of $P$.
Now, since $C_f$ is assumed to be contractible, it follows that $P(x)$ is equivalent to $P(t)$ for any $x:C_f$.
In particular, $P(\iota(b))\jdeq \brck{\hfiber{f}b}$ is equivalent to $P(t)\jdeq \unit$ for each $b:B$, and hence contractible.
Thus, $f$ is surjective.

Finally, suppose $f:A\to B$ to be surjective, and consider a set $C$ and two functions
$g,h:B\to C$ with the property that $g\circ f = h\circ f$. Since $f$
is assumed to be surjective, for all $b:B$ the type $\brck{\hfib f b}$ is contractible.
Thus we have the following equivalences:
\begin{align*}
\prd{b:B} (g(b)= h(b))
& \eqvsym \prd{b:B} \Parens{\brck{\hfib f b} \to (g(b)= h(b))}\\
& \eqvsym \prd{b:B} \Parens{\hfib f b \to (g(b)= h(b))}\\
& \eqvsym \prd{b:B}{a:A}{p:f(a)= b} g(b)= h(b)\\
& \eqvsym \prd{a:A} g(f(a))= h(f(a))
\end{align*}
using on the second line the fact that $g(b)=h(b)$ is a mere proposition, since $C$ is a set.
But by assumption, there is an element of the latter type.
\end{proof}

% \begin{rem}
% The above theorem is not true when we replace $\set$ by $\type$
% (replacing it also in the definition of $\mathsf{epi}$ and $\mathsf{epi}'$).
% However, we do
% get the implications $\textit{ii.}\Rightarrow\textit{iii.}\Rightarrow
% \textit{iv.}$
% \end{rem}

\begin{thm}\label{thm:set_regular}\label{lem:images_are_coequalizers}
The category $\uset$ is regular. Moreover, surjective functions between sets are regular epimorphisms.
\end{thm}

\begin{proof}
It is a standard lemma in category theory that a category is regular as soon as it admits finite limits and a pullback-stable orthogonal
factorization system\index{orthogonal factorization system} $(\mathcal{E},\mathcal{M})$ with $\mathcal{M}$ the monomorphisms, in which case $\mathcal{E}$ consists automatically of
the regular epimorphisms.
(See e.g.~\cite[A1.3.4]{elephant}.)
The existence of the factorization system was proved in \cref{thm:orth-fact}.
\end{proof}

\begin{lem}\label{lem:pb_of_coeq_is_coeq}
Pullbacks of regular epis in \uset are regular epis.
\end{lem}
\begin{proof}
  We showed in \cref{thm:stable-images} that pullbacks of $n$-connected functions are $n$-connected.
  By \cref{lem:images_are_coequalizers}, it suffices to apply this when $n=-1$.
\end{proof}

\indexdef{image!of a subset}
One of the consequences of \uset being a regular category is that we have an ``image'' operation on subsets.
That is, given $f:A\to B$, any subset $P:\power A$ (i.e.\ a predicate $P:A\to \prop$) has an \define{image} which is a subset of $B$.
This can be defined directly as $\setof{ y:B | \exis{x:A} f(x)=y \land P(x)}$, or indirectly as the image (in the previous sense) of the composite function
\[ \setof{ x:A | P(x) } \to A \xrightarrow{f} B.\]
\symlabel{subset-image}
We will also sometimes use the common notation $\setof{f(x) | P(x)}$ for the image of $P$.


\subsection{Quotients}\label{subsec:quotients}

\index{set-quotient|(}%
Now that we know that $\uset$ is regular, to show that $\uset$ is exact, we need to show that every
equivalence relation is effective.
\index{effective!equivalence relation|(}%
\index{relation!effective equivalence|(}%
In other words, given an equivalence
relation $R:A\to A\to\prop$, there is a coequalizer $c_R$ of the pair
$\proj1,\proj2:\sm{x,y:A} R(x,y)\to A$ and, moreover, the $\proj1$ and $\proj2$
form the kernel\index{kernel!pair} pair of $c_R$.

We have already seen, in \cref{sec:set-quotients}, two general ways to construct the quotient of a set by an equivalence relation $R:A\to A\to\prop$.
The first can be described as the set-coequalizer of the two projections
\[\proj1,\proj2:\Parens{\sm{x,y:A} R(x,y)} \to A.\]
The important property of such a quotient is the following.

\begin{defn}
  A relation $R:A\to A\to\prop$ is said to be \define{effective}
  \indexdef{effective!relation}
  \indexdef{effective!equivalence relation}%
  \indexdef{relation!effective equivalence}%
  if the square
\begin{equation*}
  \xymatrix{
    {\sm{x,y:A} R (x,y)}
    \ar[r]^(0.7){\proj1}
    \ar[d]_{\proj2}
    &
    {A}
    \ar[d]^{c_R}
    \\
    {A}
    \ar[r]_{c_R}
    &
    {A/R}
    }
\end{equation*}
is a pullback.
\end{defn}

Since the standard pullback of $c_R$ and itself is $\sm{x,y:A} (c_R(x)=c_R(y))$, by \cref{thm:total-fiber-equiv} this is equivalent to asking that the canonical transformation $\prd{x,y:A} R(x,y) \to (c_R(x)=c_R(y))$ be a fiberwise equivalence.

\begin{lem}\label{lem:sets_exact}
Suppose $\pairr{A,R}$ is an equivalence relation. Then there is an equivalence
\begin{equation*}
(c_R(x)= c_R(y))\eqvsym R(x,y)
\end{equation*}
for any $x,y:A$. In other words, equivalence relations are effective.
\end{lem}

\begin{proof}
We begin by extending $R$ to a relation $\widetilde{R}:A/R\to A/R\to\prop$, which we will then show is equivalent
to the identity type on $A/R$. We define $\widetilde{R}$ by double induction on
$A/R$ (note that $\prop$ is a set by univalence for mere propositions). We
define $\widetilde{R}(c_R(x),c_R(y)) \defeq R(x,y)$. For $r:R(x,x')$ and $s:R(y,y')$,
the transitivity and symmetry
of $R$ gives an equivalence from $R(x,y)$ to $R(x',y')$. This completes the
definition of $\widetilde{R}$.

It remains to show that $\widetilde{R}(w,w')\eqvsym (w= w')$ for every $w,w':A/R$.
The direction $(w=w')\to \widetilde{R}(w,w')$ follows by transport once we show that $\widetilde{R}$ is reflexive, which is an easy induction.
The other direction $\widetilde{R}(w,w')\to (w= w')$ is a mere proposition, so since $c_R:A\to A/R$ is surjective, it suffices to assume that $w$ and $w'$ are of the form $c_R(x)$ and $c_R(y)$.
But in this case, we have the canonical map $\widetilde{R}(c_R(x),c_R(y)) \defeq R(x,y) \to (c_R(x)=c_R(y))$.
(Note again the appearance of the encode-decode method.\index{encode-decode method})
\end{proof}

The second construction of quotients is as the set of equivalence classes of $R$ (a subset
of its power set\index{power set}):
\[ A\sslash R \defeq \setof{ P:A\to\prop | P \text{ is an equivalence class of } R}. \]
This requires propositional resizing\index{propositional resizing}\index{impredicative!quotient}\index{resizing} in order to remain in the same universe as $A$ and $R$.

Note that if we regard $R$ as a function from $A$ to $A\to \prop$, then $A\sslash R$ is equivalent to $\im(R)$, as constructed in \cref{sec:image}.
Now in \cref{lem:images_are_coequalizers} we have shown that images are
coequalizers. In particular, we immediately get the coequalizer diagram
\begin{equation*}
  \xymatrix{
    **[l]{\sm{x,y:A} R (x)= R (y)}
    \ar@<0.25em>[r]^{\proj1}
    \ar@<-0.25em>[r]_{\proj2}
    &
    {A}
    \ar[r]
    &
    {A \sslash R.}
  }
\end{equation*}
We can use this to give an alternative proof that any equivalence relation is effective and that the two definitions of quotients agree.

\begin{thm}\label{prop:kernels_are_effective}
For any function $f:A\to B$ between any two sets,
the relation $\ker(f):A\to A\to\prop$ given by
$\ker(f,x,y)\defeq (f(x)= f(y))$ is effective.
\end{thm}

\begin{proof}
We will use that $\im(f)$ is the coequalizer of $\proj1,\proj2:
(\sm{x,y:A} f(x)= f(y))\to A$.
%we get this equivalence from~\cref{prop:images_are_coequalizers}
Note that the kernel pair of the function
\[c_f\defeq\lam{a} \Parens{f(a),\brck{\pairr{a,\refl{f(a)}}}}
: A \to \im(f)
\]
consists of the two projections
\begin{equation*}
\proj1,\proj2:\Parens{\sm{x,y:A} c_f(x)= c_f(y)}\to A.
\end{equation*}
For any $x,y:A$, we have equivalences
\begin{align*}
  (c_f(x)= c_f(y))
  & \eqvsym \Parens{\sm{p:f(x)= f(y)} \trans{p}{\brck{\pairr{x,\refl{f(x)}}}} =\brck{\pairr{y,\refl{f(x)}}}}\\
  & \eqvsym (f(x)= f(y)),
\end{align*}
where the last equivalence holds because
$\brck{\hfiber{f}b}$ is a mere proposition for any $b:B$.
Therefore, we get that
\begin{equation*}
\Parens{\sm{x,y:A} c_f(x)= c_f(y)}\eqvsym \Parens{\sm{x,y:A} f(x)= f(y)}
\end{equation*}
and hence we may conclude that $\ker f$ is an effective relation
for any function $f$.
\end{proof}

\begin{thm}
Equivalence relations are effective and there is an equivalence $A/R \eqvsym A\sslash  R $.
\end{thm}

\begin{proof}
We need to analyze the coequalizer diagram
\begin{equation*}
  \xymatrix{
    **[l]{\sm{x,y:A} R (x)= R (y)}
    \ar@<0.25em>[r]^{\proj1}
    \ar@<-0.25em>[r]_{\proj2}
    &
    {A}
    \ar[r]
    &
    {A \sslash R}
  }
\end{equation*}
By the univalence axiom, the type $R(x) = R(y)$ is equivalent to the type of homotopies from $R(x)$ to $R(y)$, which is
equivalent to
\narrowequation{\prd{z:A} R (x,z)\eqvsym R (y,z).}
Since $R$ is an equivalence relation, the latter space is equivalent to $R(x,y)$. To
summarize, we get that $(R(x) = R(y)) \eqvsym R(x,y)$, so $R $ is effective since it is equivalent to an effective relation. Also,
the diagram
\begin{equation*}
  \xymatrix{
    **[l]{\sm{x,y:A} R(x, y)}
    \ar@<0.25em>[r]^{\proj1}
    \ar@<-0.25em>[r]_{\proj2}
    &
    {A}
    \ar[r]
    &
    {A \sslash R.}
  }
\end{equation*}
is a coequalizer diagram. Since coequalizers are unique up to equivalence, it follows that $A/R \eqvsym A\sslash  R $.
\end{proof}

We finish this section by mentioning a possible third construction of the quotient of a set $A$ by an equivalence relation $R$.
Consider the precategory with objects $A$ and hom-sets $R$; the type of objects of the Rezk completion
\index{completion!Rezk}%
(see \cref{sec:rezk}) of this precategory will then be the
quotient. The reader is invited to check the details.

\index{effective!equivalence relation|)}%
\index{relation!effective equivalence|)}%
\index{set-quotient|)}%

\subsection{\texorpdfstring{$\uset$}{Set} is a \texorpdfstring{$\Pi\mathsf{W}$}{ΠW}-pretopos}
\label{subsec:piw}

\index{structural!set theory|(}%

The notion of a \emph{$\Pi\mathsf{W}$-pretopos}
\index{PiW-pretopos@$\Pi\mathsf{W}$-pretopos}%
\indexsee{pretopos}{$\Pi\mathsf{W}$-pretopos}
--- that is, a locally cartesian closed category
\index{locally cartesian closed category}%
\index{category!locally cartesian closed}%
with disjoint finite coproducts, effective equivalence relations, and initial algebras for polynomial endofunctors --- is intended as a ``predicative''
\index{mathematics!predicative}%
notion of topos, i.e.\ a category of ``predicative sets'', which can serve the purpose for constructive mathematics
\index{mathematics!constructive}%
that the usual category of sets does for classical
\index{mathematics!classical}%
mathematics.

Typically, in constructive type theory, one resorts to an external construction of ``setoids'' --- an exact completion --- to obtain a category with such closure properties.
\index{setoid}\index{completion!exact}%
  In particular, the well-behaved quotients are required for many constructions in mathematics that usually involve (non-constructive) power sets.  It is noteworthy that univalent foundations provides these constructions \emph{internally} (via higher inductive types), without requiring such external constructions.  This represents a powerful advantage of our approach, as we shall see in subsequent examples.

\begin{thm}
  \index{PiW-pretopos@$\Pi\mathsf{W}$-pretopos}
  The category $\uset$ is a $\Pi\mathsf{W}$-pretopos.
\end{thm}
\begin{proof}
  We have an initial object
  \index{initial!set}%
  $\emptyt$ and finite, disjoint sums $A+B$.  These are stable under pullback, simply because pullback has a right adjoint\index{adjoint!functor}.  Indeed, $\uset$ is locally cartesian closed, since for any map $f:A\to B$ between sets, the ``fibrant replacement'' \index{fibrant replacement} $\sm{a:A}f(a)=b$ is equivalent to $A$ (over $B$), and we have dependent function types for the replacement.
We've just shown that $\uset$ is regular (\cref{thm:set_regular}) and that quotients are effective (\cref{lem:sets_exact}). We thus have a locally cartesian closed pretopos. Finally, since the $n$-types are closed under the formation of $W$-types by \cref{ex:ntypes-closed-under-wtypes}, and by \cref{thm:w-hinit} $W$-types are initial algebras for polynomial endofunctors, we see that $\uset$ is a $\Pi\mathsf{W}$-pretopos.
\end{proof}


\index{topos|(}
One naturally wonders what, if anything, prevents $\uset$ from being an (elementary) topos?
In addition to the structure already mentioned, a topos has a
\emph{subobject classifier}:
\indexdef{subobject classifier}%
\index{classifier!subobject}%
\index{power set}%
a pointed object classifying (equivalence classes of) monomorphisms\index{monomorphism}.  (In fact, in the presence of a subobject
classifier, things become somewhat simpler: one merely needs cartesian closure in order to get the colimits.)
In homotopy type theory, univalence implies that the type $\prop \defeq \sm{X:\UU}\isprop(X)$ does classify monomorphisms (by an argument similar to \cref{sec:object-classification}), but in general it is as large as the ambient universe $\UU$.
Thus, it is a ``set'' in the sense of being a $0$-type, but it is not ``small'' in the sense of being an object of $\UU$, hence not an object of the category \uset.
However, if we assume an appropriate form of propositional resizing (see \cref{subsec:prop-subsets}), then we can find a small version of $\prop$, so that \uset becomes an elementary topos.

\begin{thm}\label{thm:settopos}
  \index{propositional!resizing}%
  If there is a type $\Omega:\UU$ of all mere propositions, then the category $\uset_\UU$ is an elementary topos.
\end{thm}
\index{topos|)}

A sufficient condition for this is the law of excluded middle, in the ``mere-propositional'' form that we have called \LEM{}; for then we have $\prop = \bool$, which \emph{is} small, and which then also classifies all mere propositions.
Moreover, in topos theory a well-known sufficient condition for \LEM{} is the axiom of choice, which is of course often assumed as an axiom in classical\index{mathematics!classical} set theory.
In the next section, we briefly investigate the relation between these conditions in our setting.

\index{structural!set theory|)}%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\subsection{The axiom of choice implies excluded middle}
\label{subsec:emacinsets}

% In this section we prove a classic result that the axiom of choice implies excluded
% middle.

We begin with the following lemma.

\begin{lem}\label{prop:trunc_of_prop_is_set}
If $A$ is a mere proposition then its suspension $\susp(A)$ is a set,
and $A$ is equivalent to $\id[\susp(A)]{\north}{\south}$.
\end{lem}

\begin{proof}
To show that $\susp(A)$ is a set, we define a
family $P:\susp(A)\to\susp(A)\to\type$ with the
property that $P(x,y)$ is a mere proposition for each $x,y:\susp(A)$,
and which is equivalent to its identity type $\idtypevar{\susp(A)}$.
%
We make the following definitions:
\begin{align*}
P(\north,\north) & \defeq \unit &
P(\south,\north) & \defeq A\\
P(\north,\south) & \defeq A &
P(\south,\south) & \defeq \unit.
\end{align*}
We have to check that the definition preserves paths.
Given any $a : A$, there is a meridian $\merid(a) : \north = \south$,
so we should also have
%
\begin{equation*}
  P(\north, \north) = P(\north, \south) = P(\south, \north) = P(\south, \south).
\end{equation*}
%
But since $A$ is inhabited by $a$, it is equivalent to $\unit$, so we have
%
\begin{equation*}
  P(\north, \north) \eqvsym P(\north, \south) \eqvsym P(\south, \north) \eqvsym P(\south, \south).
\end{equation*}
%
The univalence axiom turns these into the desired equalities. Also, $P(x,y)$ is a mere
proposition for all $x, y : \susp(A)$, which is proved by induction on $x$ and $y$, and
using the fact that being a mere proposition is a mere proposition.

Note that $P$ is a reflexive relation.
Therefore we may apply \cref{thm:h-set-refrel-in-paths-sets}, so it suffices to
construct $\tau : \prd{x,y:\susp(A)}P(x,y)\to(x=y)$. We do this by a double induction.
When $x$ is $\north$, we define $\tau(\north)$ by
%
\begin{equation*}
  \tau(\north,\north,u) \defeq \refl{\north}
  \qquad\text{and}\qquad
  \tau(\north,\south,a) \defeq \merid(a).
\end{equation*}
%
If $A$ is inhabited by $a$ then $\merid(a) : \north = \south$ so we also need
\narrowequation{
  \trans{\merid(a)}{\tau(\north, \north)} = \tau(\north, \south).
}
This we get by function extensionality using the fact that, for all $x : A$,
%
\begin{multline*}
  \trans{\merid(a)}{\tau(\north,\north,x)} =
  \tau(\north,\north,x) \ct \opp{\merid(a)} \jdeq \\
  \refl{\north} \ct \merid(a) =
  \merid(a) =
  \merid(x) \jdeq
  \tau(\north, \south, x).
\end{multline*}
In a symmetric fashion we may define $\tau(\south)$ by
%
\begin{equation*}
  \tau(\south,\north, a) \defeq \opp{\merid(a)}
  \qquad\text{and}\qquad
  \tau(\south,\south, u) \defeq \refl{\south}.
\end{equation*}
%
To complete the construction of $\tau$, we need to check $\trans{\merid(a)}{\tau(\north)} = \tau(\south)$,
given any $a : A$. The verification proceeds much along the same lines by induction on the
second argument of $\tau$.

Thus, by \cref{thm:h-set-refrel-in-paths-sets} we have that $\susp(A)$ is a set and that $P(x,y) \eqvsym (\id{x}{y})$ for all $x,y:\susp(A)$.
Taking $x\defeq \north$ and $y\defeq \south$ yields $\eqv{A}{(\id[\susp(A)]\north\south)}$ as desired.
\end{proof}

\begin{thm}[Diaconescu]\label{thm:1surj_to_surj_to_pem}
  \index{axiom!of choice}%
  \index{excluded middle}%
  \index{Diaconescu's theorem}\index{theorem!Diaconescu's}%
  The axiom of choice implies the law of excluded middle.
\end{thm}

\begin{proof}
We use the equivalent form of choice given in \cref{thm:ac-epis-split}.
Consider a mere proposition $A$.
The function $f:\bool\to\susp(A)$ defined by
$f(\bfalse) \defeq \north$ and $f(\btrue) \defeq \south$
is surjective.
Indeed, we have
$\pairr{\bfalse,\refl{\north}} : \hfiber{f}{\north}$
and $\pairr{\btrue,\refl{\south}} :\hfiber{f}{\south}$.
Since $\bbrck{\hfiber{f}{x}}$ is a mere proposition, by induction the claimed surjectivity follows.

By \cref{prop:trunc_of_prop_is_set} the suspension $\susp(A)$
is a set, so by the axiom of choice there merely exists a
section $g: \susp(A) \to \bool$ of $f$.
As equality on $\bool$ is decidable we get
\begin{equation*}
 (g(f(\bfalse))= g(f(\btrue))) +
 \lnot (g(f(\bfalse))= g(f(\btrue))),
\end{equation*}
and, since $g$ is a section of $f$, hence injective,
\begin{equation*}
(f(\bfalse) = f(\btrue)) +
\lnot (f(\bfalse) = f(\btrue)).
\end{equation*}
Finally, since $(f(\bfalse)=f(\btrue)) = (\north=\south) = A$ by \cref{prop:trunc_of_prop_is_set}, we have $A+\neg A$.
\end{proof}

% This conclusion needs only \LEM{}, see \cref{ex:lemnm}.

% \begin{cor}\label{cor:ACtoLEM0}
%   If the axiom of choice \choice{} holds then $\brck{A + \neg A}$ for every set $A$.
% \end{cor}

% \begin{proof}
%   There is a surjection
%   \[
%   A + \neg A \epi \brck{A} + \brck{\neg A} \epi
%   \brck{(\brck{A} + \brck{\neg A})} = \brck{A} \vee \brck{\neg A} = \brck{A} \vee \neg \brck{A} = \unit,
%   \]
%   %
%   where in the last step excluded middle is available as a consequence of the axiom of choice.
%   Again by the axiom of choice there merely exists a section of the surjection, but this
%   is none other than an inhabitant of $A + \neg A$. Therefore $\brck{A+\neg A}$.
% \end{proof}

\index{denial}
\begin{thm}\label{thm:ETCS}
  \index{Elementary Theory of the Category of Sets}%
  \index{category!well-pointed}%
  If the axiom of choice holds then the category $\uset$ is a well-pointed boolean\index{topos!boolean}\index{boolean!topos} elementary topos\index{topos} with choice.
\end{thm}

\begin{proof}
  Since \choice{} implies \LEM{}, we have a boolean elementary topos with choice by \cref{thm:settopos} and the remark following it.  We leave the proof of well-pointedness as
an exercise for the reader (\cref{ex:well-pointed}).
\end{proof}

\begin{rmk}
  The conditions on a category mentioned in the theorem are known as Lawvere's\index{Lawvere}
  axioms for the \emph{Elementary Theory of the Category of Sets}~\cite{lawvere:etcs-long}.
\end{rmk}

\section{Cardinal numbers}
\label{sec:cardinals}

\begin{defn}\label{defn:card}
  The \define{type of cardinal numbers}
  \indexdef{type!of cardinal numbers}%
  \indexdef{cardinal number}%
  \indexsee{number!cardinal}{cardinal number}%
  is the 0-truncation of the type \set of sets:
  \[ \card \defeq \pizero{\set} \]
  Thus, a \define{cardinal number}, or \define{cardinal}, is an inhabitant of $\card\jdeq \pizero\set$.
  Technically, of course, there is a separate type $\card_\UU$ associated to each universe \type.
\end{defn}

%\begin{rmk}

  % , but with these conventions we can state theorems beginning with ``for all cardinal numbers\dots''\ and give them exactly the same sort of meaning as those beginning ``for all types\dots''.
%\end{rmk}

As usual for truncations, if $A$ is a set, then $\cd{A}$ denotes its image under the canonical projection $\set \to \trunc0\set \jdeq \card$; we call $\cd{A}$ the \define{cardinality}\indexdef{cardinality} of $A$.
By definition, \card is a set.
It also inherits the structure of a semiring from \set.

\begin{defn}
  The operation of \define{cardinal addition}
  \indexdef{addition!of cardinal numbers}%
  \index{cardinal number!addition of}%
  \[ (\blank+\blank) : \card \to \card \to \card \]
  is defined by induction on truncation:
  \[ \cd{A} + \cd{B} \defeq \cd{A+B}.\]
\end{defn}
\begin{proof}
  Since $\card\to\card$ is a set, to define $(\alpha+\blank):\card\to\card$ for all $\alpha:\card$, by induction it suffices to assume that $\alpha$ is $\cd{A}$ for some $A:\set$.
  Now we want to define $(\cd{A}+\blank) :\card\to\card$, i.e.\ we want to define $\cd{A}+\beta :\card$ for all $\beta:\card$.
  However, since $\card$ is a set, by induction it suffices to assume that $\beta$ is $\cd{B}$ for some $B:\set$.
  But now we can define $\cd{A}+\cd{B}$ to be $\cd{A+B}$.
\end{proof}

\begin{defn}
  Similarly, the operation of \define{cardinal multiplication}
  \indexdef{multiplication!of cardinal numbers}%
  \index{cardinal number!multiplication of}%
  \[ (\blank\cdot\blank) : \card \to \card \to \card \]
  is defined by induction on truncation:
  \[ \cd{A} \cdot \cd{B} \defeq \cd{A\times B} \]
\end{defn}

\begin{lem}\label{card:semiring}
  \card is a commutative semiring\index{semiring}, i.e.\ for $\alpha,\beta,\gamma:\card$ we have the following.
  \begin{align*}
    (\alpha+\beta)+\gamma &= \alpha+(\beta+\gamma)\\
    \alpha+0 &= \alpha\\
    \alpha + \beta &= \beta + \alpha\\
    (\alpha \cdot \beta) \cdot \gamma &= \alpha \cdot (\beta\cdot\gamma)\\
    \alpha \cdot 1 &= \alpha\\
    \alpha\cdot\beta &= \beta\cdot\alpha\\
    \alpha\cdot(\beta+\gamma) &= \alpha\cdot\beta + \alpha\cdot\gamma
  \end{align*}
  where $0 \defeq \cd{\emptyt}$ and $1\defeq\cd{\unit}$.
\end{lem}
\begin{proof}
  We prove the commutativity of multiplication, $\alpha\cdot\beta = \beta\cdot\alpha$; the others are exactly analogous.
  Since \card is a set, the type $\alpha\cdot\beta = \beta\cdot\alpha$ is a mere proposition, and in particular a set.
  Thus, by induction it suffices to assume $\alpha$ and $\beta$ are of the form $\cd{A}$ and $\cd{B}$ respectively, for some $A,B:\set$.
  Now $\cd{A}\cdot \cd{B} \jdeq \cd{A\times B}$ and $\cd{B}\cdot\cd{A} \jdeq \cd{B\times A}$, so it suffices to show $A\times B = B\times A$.
  Finally, by univalence, it suffices to give an equivalence $A\times B \eqvsym B\times A$.
  But this is easy: take $(a,b) \mapsto (b,a)$ and its obvious inverse.
\end{proof}

\begin{defn}
  The operation of \define{cardinal exponentiation} is also defined by induction on truncation:
  \indexdef{exponentiation, of cardinal numbers}%
  \index{cardinal number!exponentiation of}%
  \[ \cd{A}^{\cd{B}} \defeq \cd{B\to A}. \]
\end{defn}

\begin{lem}\label{card:exp}
  For $\alpha,\beta,\gamma:\card$ we have
  \begin{align*}
    \alpha^0 &= 1\\
    1^\alpha &= 1\\
    \alpha^1 &= \alpha\\
    \alpha^{\beta+\gamma} &= \alpha^\beta \cdot \alpha^\gamma\\
    \alpha^{\beta\cdot \gamma} &= (\alpha^{\beta})^\gamma\\
    (\alpha\cdot\beta)^\gamma &= \alpha^\gamma \cdot \beta^\gamma
  \end{align*}
\end{lem}
\begin{proof}
  Exactly like \cref{card:semiring}.
\end{proof}

\begin{defn}
  The relation of \define{cardinal inequality}
  \index{order!non-strict}%
  \index{cardinal number!inequality of}%
  \[ (\blank\le\blank) : \card\to\card\to\prop \]
  is defined by induction on truncation:
  \symlabel{inj}
  \[ \cd{A} \le \cd{B} \defeq \brck{\inj(A,B)} \]
  where $\inj(A,B)$ is the type of injections from $A$ to $B$.
  \index{function!injective}%
  In other words, $\cd{A} \le \cd{B}$ means that there merely exists an injection from $A$ to $B$.
\end{defn}

\begin{lem}
  Cardinal inequality is a preorder, i.e.\ for $\alpha,\beta:\card$ we have
  \index{preorder!of cardinal numbers}%
  \begin{gather*}
    \alpha \le \alpha\\
    (\alpha \le \beta) \to (\beta\le\gamma) \to (\alpha\le\gamma)
  \end{gather*}
\end{lem}
\begin{proof}
  As before, by induction on truncation.
  For instance, since $(\alpha \le \beta) \to (\beta\le\gamma) \to (\alpha\le\gamma)$ is a mere proposition, by induction on 0-truncation we may assume $\alpha$, $\beta$, and $\gamma$ are $\cd{A}$, $\cd{B}$, and $\cd{C}$ respectively.
  Now since $\cd{A} \le \cd{C}$ is a mere proposition, by induction on $(-1)$-truncation we may assume given injections $f:A\to B$ and $g:B\to C$.
  But then $g\circ f$ is an injection from $A$ to $C$, so $\cd{A} \le \cd{C}$ holds.
  Reflexivity is even easier.
\end{proof}

We may likewise show that cardinal inequality is compatible with the semiring operations.

\begin{lem}\label{thm:injsurj}
  \index{function!injective}%
  \index{function!surjective}%
  Consider the following statements:
  \begin{enumerate}
  \item There is an injection $A\to B$.\label{item:cle-inj}
  \item There is a surjection $B\to A$.\label{item:cle-surj}
  \end{enumerate}
  Then, assuming excluded middle:
  \index{excluded middle}%
  \index{axiom!of choice}%
  \begin{itemize}
  \item Given $a_0:A$, we have~\ref{item:cle-inj}$\to$\ref{item:cle-surj}.
  \item Therefore, if $A$ is merely inhabited, we have~\ref{item:cle-inj} $\to$ merely \ref{item:cle-surj}.
  \item Assuming the axiom of choice, we have~\ref{item:cle-surj} $\to$ merely \ref{item:cle-inj}.
  \end{itemize}
\end{lem}
\begin{proof}
  If $f:A\to B$ is an injection, define $g:B\to A$ at $b:B$ as follows.
  Since $f$ is injective, the fiber of $f$ at $b$ is a mere proposition.
  Therefore, by excluded middle, either there is an $a:A$ with $f(a)=b$, or not.
  In the first case, define $g(b)\defeq a$; otherwise set $g(b)\defeq a_0$.
  Then for any $a:A$, we have $a = g(f(a))$, so $g$ is surjective.

  The second statement follows from this by induction on truncation.
  For the third, if $g:B\to A$ is surjective, then by the axiom of choice, there merely exists a function $f:A\to B$ with $g(f(a)) = a$ for all $a$.
  But then $f$ must be injective.
\end{proof}

\begin{thm}[Schroeder--Bernstein]
  \index{theorem!Schroeder--Bernstein}%
  \index{Schroeder--Bernstein theorem}%
  Assuming excluded middle, for sets $A$ and $B$ we have
  \[ \inj(A,B) \to \inj(B,A) \to (A\cong B) \]
\end{thm}
\begin{proof}
  The usual ``back-and-forth'' argument applies without significant changes.
  Note that it actually constructs an isomorphism $A\cong B$ (assuming excluded middle so that we can decide whether a given element belongs to a cycle, an infinite chain, a chain beginning in $A$, or a chain beginning in $B$).
\end{proof}

\begin{cor}
  Assuming excluded middle, cardinal inequality is a partial order, i.e.\ for $\alpha,\beta:\card$ we have
  \[ (\alpha\le\beta) \to (\beta\le\alpha) \to (\alpha=\beta). \]
\end{cor}
\begin{proof}
  Since $\alpha=\beta$ is a mere proposition, by induction on truncation we may assume $\alpha$ and $\beta$ are $\cd{A}$ and $\cd{B}$, respectively, and that we have injections $f:A\to B$ and $g:B\to A$.
  But then the Schroeder--Bernstein theorem gives an isomorphism $A\cong B$, hence an equality $\cd{A}=\cd{B}$.
\end{proof}

Finally, we can reproduce Cantor's theorem, showing that for every cardinal there is a greater one.

\begin{thm}[Cantor]
  \index{Cantor's theorem}%
  \index{theorem!Cantor's}%
  For $A:\set$, there is no surjection $A \to (A\to \bool)$.
\end{thm}
\begin{proof}
  Suppose $f:A \to (A\to \bool)$ is any function, and define $g:A\to \bool$ by $g(a) \defeq \neg f(a)(a)$.
  If $g = f(a_0)$, then $g(a_0) = f(a_0)(a_0)$ but $g(a_0) = \neg f(a_0)(a_0)$, a contradiction.
  Thus, $f$ is not surjective.
\end{proof}

\begin{cor}
  Assuming excluded middle, for any $\alpha:\card$, there is a cardinal $\beta$ such that $\alpha\le\beta$ and $\alpha\neq\beta$.
\end{cor}
\begin{proof}
  Let $\beta = 2^\alpha$.
  Now we want to show a mere proposition, so by induction we may assume $\alpha$ is $\cd{A}$, so that $\beta\jdeq \cd{A\to \bool}$.
  Using excluded middle, we have a function $f:A\to (A\to \bool)$ defined by
  \[f(a)(a') \defeq
  \begin{cases}
    \btrue &\quad a=a'\\
    \bfalse &\quad a\neq a'.
  \end{cases}
  \]
  And if $f(a)=f(a')$, then $f(a')(a) = f(a)(a) = \btrue$, so $a=a'$; hence $f$ is injective.
  Thus, $\alpha \jdeq \cd{A} \le \cd{A\to \bool} \jdeq 2^\alpha$.

  On the other hand, if $2^\alpha \le \alpha$, then we would have an injection $(A\to\bool)\to A$.
  By \cref{thm:injsurj}, since we have $(\lam{x} \bfalse):A\to \bool$ and excluded middle, there would then be a surjection $A \to (A\to \bool)$, contradicting Cantor's theorem.
\end{proof}

\section{Ordinal numbers}
\label{sec:ordinals}

\index{ordinal|(}%

\begin{defn}\label{defn:accessibility}
  Let $A$ be a set and
  \[(\blank<\blank):A\to A\to \prop\]
  a binary relation on $A$.
  We define by induction what it means for an element $a:A$ to be \define{accessible}
  \indexdef{accessibility}%
  \indexsee{accessible}{accessibility}%
  by $<$:
  \begin{itemize}
  \item If $b$ is accessible for every $b<a$, then $a$ is accessible.
  \end{itemize}
  We write $\acc(a)$ to mean that $a$ is accessible.
\end{defn}

It may seem that such an inductive definition can never get off the ground, but of course if $a$ has the property that there are \emph{no} $b$ such that $b<a$, then $a$ is vacuously accessible.

Note that this is an inductive definition of a family of types, like the type of vectors considered in \cref{sec:generalizations}.
More precisely, it has one constructor, say $\acc_<$, with type
\[ \acc_< : \prd{a:A} \Parens{\prd{b:A} (b<a) \to \acc(b)} \to \acc(a). \]
\index{induction principle!for accessibility}%
The induction principle for $\acc$ says that for any $P:\prd{a:A} \acc(a) \to \type$, if we have
\[f:\prd{a:A}{h:\prd{b:A} (b<a) \to \acc(b)}
\Parens{\prd{b:A}{l:b<a} P(b,h(b,l))} \to
P(a,\acc_<(a,h)),
\]
then we have $g:\prd{a:A}{c:\acc(a)} P(a,c)$ defined by induction, with
\[g(a,\acc_<(a,h)) \jdeq f(a,\,h,\,\lam{b}{l} g(b,h(b,l))).\]
This is a mouthful, but generally we apply it only in the simpler case where $P:A\to\type$ depends only on $A$.
In this case the second and third arguments of $f$ may be combined, so that what we have to prove is
\[f:\prd{a:A} \Parens{\prd{b:A} (b<a) \to \acc(b) \times P(b)}
\to P(a).
\]
That is, we assume every $b<a$ is accessible and $g(b):P(b)$ is defined, and from these define $g(a):P(a)$.

The omission of the second argument of $P$ is justified by the following lemma, whose proof is the only place where we use the more general form of the induction principle.

\begin{lem}
  Accessibility\index{accessibility} is a mere property.
\end{lem}
\begin{proof}
  We must show that for any $a:A$ and $s_1,s_2:\acc(a)$ we have $s_1=s_2$.
  We prove this by induction on $s_1$, with
  \[P_1(a,s_1) \defeq \prd{s_2:\acc(a)} (s_1=s_2). \]
  Thus, we must show that for any $a:A$ and ${h_1:\prd{b:A} (b<a) \to \acc(b)}$ and
  \[ k_1:{\prd{b:A}{l:b<a}{t:\acc(b)} h_1(b,l) = t},\]
  we have $\acc_<(a,h) = s_2$ for any $s_2:\acc(a)$.
  We regard this statement as $\prd{a:A}{s_2:\acc(a)} P_2(a,s_2)$, where
  \[P_2(a,s_2) \defeq
  \prd{h_1 : \cdots } %{h_1:\prd{b:A} (b<a) \to \acc(b)}
  {k_1 : \cdots} % \Parens{\prd{b:A}{l:b<a}{t:\acc(b)} h_1(b,l) = t} \to
  (\acc_<(a,h_1) = s_2);
  \]
  thus we may prove it by induction on $s_2$.
  Therefore, we assume $h_2 : \prd{b:A} (b<a) \to \acc(b)$, and $k_2$ with a monstrous but irrelevant type,
  % \begin{narrowmultline*}
  %   k_2:\prd{b:A}{l:b<a}
  %   \prd{h_1:\prd{b':A} (b'<b) \to \acc(b')}
  %   \narrowbreak
  %   \Parens{\prd{b':A}{l':b'<b}{t':\acc(b')} h_1(b',l') = t'} \to
  %   (\acc_<(b,h_1) = h_2(b,l)).
  % \end{narrowmultline*}
  and must show that for any $h_1$ and $k_1$ with types as above,
  we have $\acc_<(a,h_1) = \acc_<(a,h_2)$.
  By function extensionality, it suffices to show $h_1(b,l) = h_2(b,l)$ for all $b:A$ and $l:b<a$.
  This follows from $k_1$.
\end{proof}

\begin{defn}
  A binary relation $<$ on a set $A$ is \define{well-founded}
  \indexdef{relation!well-founded}%
  \indexdef{well-founded!relation}%
  if every element of $A$ is accessible.
\end{defn}

The point of well-foundedness is that for $P:A\to \type$, we can use the induction principle of $\acc$ to conclude $\prd{a:A} \acc(a) \to P(a)$, and then apply well-foundedness to conclude $\prd{a:A} P(a)$.
In other words, if from $\fall{b:A} (b<a) \to P(b)$ we can prove $P(a)$, then $\fall{a:A} P(a)$.
This is called \define{well-founded induction}\indexdef{well-founded!induction}.

\begin{lem}
  Well-foundedness is a mere property.
\end{lem}
\begin{proof}
  Well-foundedness of $<$ is the type $\prd{a:A} \acc(a)$, which is a mere proposition since each $\acc(a)$ is.
\end{proof}

\begin{eg}\label{thm:nat-wf}
  Perhaps the most familiar well-founded relation is the usual strict ordering on \nat.
  To show that this is well-founded, we must show that $n$ is accessible for each $n:\nat$.
  \index{strong!induction}%
  This is just the usual proof of ``strong induction'' from ordinary induction on \nat.

  Specifically, we prove by induction on $n:\nat$ that $k$ is accessible for all $k\le n$.
  The base case is just that $0$ is accessible, which is vacuously true since nothing is strictly less than $0$.
  For the inductive step, we assume that $k$ is accessible for all $k\le n$, which is to say for all $k<n+1$; hence by definition $n+1$ is also accessible.

  A different relation on \nat which is also well-founded is obtained by setting only $n < \suc(n)$ for all $n:\nat$.
  Well-foundedness of this relation is almost exactly the ordinary induction principle of \nat.
\end{eg}

\begin{eg}\label{thm:wtype-wf}
  Let $A:\set$ and $B : A \to \set$ be a family of sets.
  Recall from \cref{sec:w-types} that the $W$-type $\wtype{a:A} B(a)$ is inductively generated by the single constructor
  \begin{itemize}
  \item $\supp : \prd{a:A} (B(a) \to \wtype{x:A} B(x)) \to \wtype{x:A} B(x)$
  \end{itemize}
  We define the relation $<$ on $\wtype{x:A} B(x)$ by recursion on its second argument:
  \begin{itemize}
  \item For any $a:A$ and $f:B(a) \to \wtype{x:A} B(x)$, we define $w<\supp(a,f)$ to mean that there merely exists a $b:B(a)$ such that $w = f(b)$.
  \end{itemize}
  Now we prove that every $w:\wtype{x:A} B(x)$ is accessible for this relation, using the usual induction principle for $\wtype{x:A}B(x)$.
  This means we assume given $a:A$ and $f:B(a) \to \wtype{x:A} B(x)$, and also a lifting $f' : \prd{b:B(a)} \acc(f(b))$.
  But then by definition of $<$, we have $\acc(w)$ for all $w<\supp(a,f)$; hence $\supp(a,f)$ is accessible.
\end{eg}

Well-foundedness allows us to define functions by recursion and prove statements by induction, such as for instance the following.
Recall from \cref{subsec:prop-subsets} that $\power B$ denotes the \emph{power set}\index{power set} $\power B \defeq (B\to\prop)$.

\begin{lem}\label{thm:wfrec}
  Suppose $B$ is a set and we have a function
  \[ g : \power B \to B \]
  Then if $<$ is a well-founded relation on $A$, there is a function $f:A\to B$ such that for all $a:A$ we have
  \begin{equation*}
    f(a) = g\Big(\setof{ f(a') | a'<a }\Big).
  \end{equation*}
\end{lem}
\noindent
(We are using the notation for images of subsets from \cref{sec:image}.)
\begin{proof}
  We first define, for every $a:A$ and $s:\acc(a)$, an element $\bar f(a,s):B$.
  By induction, it suffices to assume that $s$ is a function assigning to each $a'<a$ a witness $s(a'):\acc(a')$, and that moreover for each such $a'$ we have an element $\bar f(a',s(a')):B$.
  In this case, we define
  \begin{equation*}
    \bar f(a,s) \defeq g\Big(\setof{ \bar f(a',s(a')) | a'<a }\Big).
  \end{equation*}

  Now since $<$ is well-founded, we have a function $w:\prd{a:A} \acc(a)$.
  Thus, we can define $f(a)\defeq \bar f (a,w(a))$.
\end{proof}

In classical\index{mathematics!classical} logic, well-foundedness has a more well-known reformulation.
In the following, we say that a subset $B: \power A$ is \define{nonempty}
\indexdef{nonempty subset}
if it is unequal to the empty subset $(\lam{x}\bot) : \power X$.
We leave it to the reader to verify that assuming excluded middle, this is equivalent to mere inhabitation, i.e.\ to the condition $\exis{x:A} x\in B$.

\begin{lem}\label{thm:wfmin}
  \index{excluded middle}%
  Assuming excluded middle, $<$ is well-founded if and only if every nonempty subset $B: \power A$ merely has a minimal element.
\end{lem}
\begin{proof}
  Suppose first $<$ is well-founded, and suppose $B\subseteq A$ is a subset with no minimal element.
  That is, for any $a:A$ with $a\in B$, there merely exists a $b:A$ with $b<a$ and $b\in B$.

  We claim that for any $a:A$ and $s:\acc(a)$, we have $a\notin B$.
  By induction, we may assume $s$ is a function assigning to each $a'<a$ a proof $s(a'):\acc(a')$, and that moreover for each such $a'$ we have $a'\notin B$.
  If $a\in B$, then by assumption, there would merely exist a $b<a$ with $b\in B$, which contradicts this assumption.
  Thus, $a\notin B$; this completes the induction.
  Since $<$ is well-founded, we have $a\notin B$ for all $a:A$, i.e. $B$ is empty.

  Now suppose each nonempty subset merely has a minimal element.
  Let $B = \setof{ a:A | \neg \acc(a) }$.
  Then if $B$ is nonempty, it merely has a minimal element.
  Thus there merely exists an $a:A$ with $a\in B$ such that for all $b<a$, we have $\acc(b)$.
  But then by definition (and induction on truncation), $a$ is merely accessible, and hence accessible, contradicting $a\in B$.
  Thus, $B$ is empty, so $<$ is well-founded.
\end{proof}

\begin{defn}
  A well-founded relation $<$ on a set $A$ is \define{extensional}
  \indexdef{relation!extensional}%
  \indexdef{extensional!relation}%
  if for any $a,b:A$, we have
  \[ \Parens{\fall{c:A} (c<a) \Leftrightarrow (c<b)} \to (a=b). \]
\end{defn}

Note that since $A$ is a set, extensionality is a mere proposition.
This notion of ``extensionality'' is unrelated to function extensionality, and also unrelated to the extensionality of identity types.
\index{axiom!of extensionality}%
Rather, it is a ``local'' counterpart of the axiom of extensionality in classical set theory.

\begin{thm}
  The type of extensional well-founded relations is a set.
\end{thm}
\begin{proof}
  By the univalence axiom, it suffices to show that if $(A,<)$ is extensional and well-founded and $f:(A,<) \cong (A,<)$, then $f=\idfunc[A]$.
  \index{automorphism!of extensional well-founded relations}%
  We prove by induction on $<$ that $f(a)=a$ for all $a:A$.
  The inductive hypothesis is that for all $a'<a$, we have $f(a')=a'$.

  Now since $A$ is extensional, to conclude $f(a)=a$ it is sufficient to show
  \[\fall{c:A}(c<f(a)) \Leftrightarrow (c<a).\]
  However, since $f$ is an automorphism, we have $(c<a) \Leftrightarrow (f(c)<f(a))$.
  But $c<a$ implies $f(c)=c$ by the inductive hypothesis, so $(c<a) \to (c<f(a))$.
  On the other hand, if $c<f(a)$, then $f^{-1}(c)<a$, and so $c = f(f^{-1}(c)) = f^{-1}(c)$ by the inductive hypothesis again; thus $c<a$.
  Therefore, we have $(c<a) \Leftrightarrow (c<f(a))$ for any $c:A$, so $f(a)=a$.
\end{proof}

\begin{defn}\label{def:simulation}
  If $(A,<)$ and $(B,<)$ are extensional and well-founded, a \define{simulation}
  \indexdef{simulation}%
  \indexsee{function!simulation}{simulation}%
  is a function $f:A\to B$ such that
  \begin{enumerate}
  \item if $a<a'$, then $f(a)<f(a')$, and\label{item:sim1}
  \item for all $a:A$ and $b:B$, if $b<f(a)$, then there merely exists an $a'<a$ with $f(a')=b$.\label{item:sim2}
  \end{enumerate}
\end{defn}

\begin{lem}
  Any simulation is injective.
\end{lem}
\begin{proof}
  We prove by double well-founded induction that for any $a,b:A$, if $f(a)=f(b)$ then $a=b$.
  The inductive hypothesis for $a:A$ says that for any $a'<a$, and any $b:B$, if $f(a')=f(b)$ then $a=b$.
  The inner inductive hypothesis for $b:A$ says that for any $b'<b$, if $f(a)=f(b')$ then $a=b'$.

  Suppose $f(a)=f(b)$; we must show $a=b$.
  By extensionality, it suffices to show that for any $c:A$ we have $(c<a)\Leftrightarrow (c<b)$.
  If $c<a$, then $f(c)<f(a)$ by \cref{def:simulation}\ref{item:sim1}.
  Hence $f(c)<f(b)$, so by \cref{def:simulation}\ref{item:sim2} there merely exists $c':A$ with $c'<b$ and $f(c)=f(c')$.
  By the inductive hypothesis for $a$, we have $c=c'$, hence $c<b$.
  The dual argument is symmetrical.
\end{proof}

In particular, this implies that in \cref{def:simulation}\ref{item:sim2} the word ``merely'' could be omitted without change of sense.

\begin{cor}
  If $f:A\to B$ is a simulation, then for all $a:A$ and $b:B$, if $b<f(a)$, there \emph{purely} exists an $a'<a$ with $f(a')=b$.
\end{cor}
\begin{proof}
  Since $f$ is injective, $\sm{a:A} (f(a)=b)$ is a mere proposition.
\end{proof}

We say that a subset $C :\power B$ is an \define{initial segment}
\indexdef{initial!segment}%
\indexsee{segment, initial}{initial segment}%
if $c\in C$ and $b<c$ imply $b\in C$.
The image of a simulation must be an initial segment, while the inclusion of any initial segment is a simulation.
Thus, by univalence, every simulation $A\to B$ is \emph{equal} to the inclusion of some initial segment of $B$.

\begin{thm}
  For a set $A$, let $P(A)$ be the type of extensional well-founded relations on $A$.
  If $\mathord{<_A} : P(A)$ and $\mathord{<_B} : P(B)$ and $f:A\to B$, let $H_{\mathord{<_A}\mathord{<_B}}(f)$ be the mere proposition that $f$ is a simulation.
  Then $(P,H)$ is a standard notion of structure over \uset in the sense of \cref{sec:sip}.
\end{thm}
\begin{proof}
  We leave it to the reader to verify that identities are simulations, and that composites of simulations are simulations.
  Thus, we have a notion of structure.
  For standardness, we must show that if $<$ and $\prec$ are two extensional well-founded relations on $A$, and $\idfunc[A]$ is a simulation in both directions, then $<$ and $\prec$ are equal.
  Since extensionality and well-foundedness are mere propositions, for this it suffices to have $\fall{a,b:A} (a<b) \Leftrightarrow (a\prec b)$.
  But this follows from \cref{def:simulation}\ref{item:sim1} for $\idfunc[A]$.
\end{proof}

\begin{cor}\label{thm:wfcat}
  There is a category whose objects are sets equipped with extensional well-founded relations, and whose morphisms are simulations.
\end{cor}

In fact, this category is a poset.

\begin{lem}
  For extensional and well-founded $(A,<)$ and $(B,<)$, there is at most one simulation $f:A\to B$.
\end{lem}
\begin{proof}
  Suppose $f,g:A\to B$ are simulations.
  Since being a simulation is a mere property, it suffices to show $\fall{a:A}(f(a)=g(a))$.
  By induction on $<$, we may suppose $f(a')=g(a')$ for all $a'<a$.
  And by extensionality of $B$, to have $f(a)=g(a)$ it suffices to have $\fall{b:B}(b<f(a)) \Leftrightarrow (b<g(a))$.

  But since $f$ is a simulation, if $b<f(a)$, then we have $a'<a$ with $f(a')=b$.
  By the inductive hypothesis, we have also $g(a')=b$, hence $b<g(a)$.
  The dual argument is symmetrical.
\end{proof}

Thus, if $A$ and $B$ are equipped with extensional and well-founded relations, we may write $A\le B$ to mean there exists a simulation $f:A\to B$.
\cref{thm:wfcat} implies that if $A\le B$ and $B\le A$, then $A=B$.

\begin{defn}
  An \define{ordinal}
  \indexdef{ordinal}%
  \indexsee{number!ordinal}{ordinal}%
  is a set $A$ with an extensional well-founded relation which is \emph{transitive}, i.e.\ satisfies $\fall{a,b,c:A}(a<b)\to (b<c) \to (a<c)$.
\end{defn}

\begin{eg}
  Of course, the usual strict order on \nat is transitive.
  It is easily seen to be extensional as well; thus it is an ordinal.
  As usual, we denote this ordinal by $\omega$.
\end{eg}

\symlabel{ord}
Let \ord denote the type of ordinals.
By the previous results, \ord is a set and has a natural partial order.
We now show that \ord also admits a well-founded relation.

\symlabel{initial-segment}
If $A$ is an ordinal and $a:A$, let $\ordsl A a \defeq \setof{ b:A | b<a}$ denote the initial segment.
\index{initial!segment}%
Note that if $\ordsl A a = \ordsl A b$ as ordinals, then that isomorphism must respect their inclusions into $A$ (since simulations form a poset), and hence they are equal as subsets of $A$.
Therefore, since $A$ is extensional, $a=b$.
Thus the function $a\mapsto \ordsl A a$ is an injection $A\to \ord$.

\begin{defn}
  For ordinals $A$ and $B$, a simulation $f:A\to B$ is said to be \define{bounded}
  \indexdef{simulation!bounded}%
  \indexdef{bounded!simulation}%
  if there exists $b:B$ such that $A = \ordsl B b$.
\end{defn}

The remarks above imply that such a $b$ is unique when it exists, so that boundedness is a mere property.

We write $A<B$ if there exists a bounded simulation from $A$ to $B$.
Since simulations are unique, $A<B$ is also a mere proposition.

\begin{thm}\label{thm:ordord}
  $(\ord,<)$ is an ordinal.
\end{thm}

\noindent
More precisely, this theorem says that the type $\ord_{\UU_i}$ of ordinals in one universe\index{universe level} is itself an ordinal in the next higher universe, i.e.\ $(\ord_{\UU_i},<):\ord_{\UU_{i+1}}$.

\begin{proof}
  Let $A$ be an ordinal; we first show that $\ordsl A a$ is accessible (in \ord) for all $a:A$.
  By well-founded induction on $A$, suppose $\ordsl A b$ is accessible for all $b<a$.
  By definition of accessibility, we must show that $B$ is accessible in \ord for all $B<\ordsl A a$.
  However, if $B<\ordsl A a$ then there is some $b<a$ such that $B = \ordsl{(\ordsl A a)}{b} = \ordsl A b$, which is accessible by the inductive hypothesis.
  Thus, $\ordsl A a$ is accessible for all $a:A$.

  Now to show that $A$ is accessible in \ord, by definition we must show $B$ is accessible for all $B<A$.
  But as before, $B<A$ means $B=\ordsl A a$ for some $a:A$, which is accessible as we just proved.
  Thus, \ord is well-founded.

  For extensionality, suppose $A$ and $B$ are ordinals such that
  \narrowequation{\prd{C:\ord} (C<A) \Leftrightarrow (C<B).}
  Then for every $a:A$, since $\ordsl A a<A$, we have $\ordsl A a<B$, hence there is $b:B$ with $\ordsl A a = \ordsl B b$.
  Define $f:A\to B$ to take each $a$ to the corresponding $b$; it is straightforward to verify that $f$ is an isomorphism.
  Thus $A\cong B$, hence $A=B$ by univalence.

  Finally, it is easy to see that $<$ is transitive.
\end{proof}

Treating \ord as an ordinal is often very convenient, but it has its pitfalls as well.
For instance, consider the following lemma, where we pay attention to how universes are used.

\begin{lem}\label{thm:ordsucc}
  Let \bbU be a universe.
  For any $A:\ord_\bbU$, there is a $B:\ord_\bbU$ such that $A<B$.
\end{lem}
\begin{proof}
  Let $B=A+\unit$, with the element $\ttt:\unit$ being greater than all elements of $A$.
  Then $B$ is an ordinal and it is easy to see that $A\cong \ordsl B \ttt$.
\end{proof}

The ordinal $B$ constructed in the proof of \cref{thm:ordsucc} is called the \define{successor}\indexdef{successor!of an ordinal} of $A$.

This lemma illustrates a potential pitfall of the ``typically ambiguous''\index{typical ambiguity} style of using \UU to denote an arbitrary, unspecified universe.
Consider the following alternative proof of it.

\begin{proof}[Another putative proof of \cref{thm:ordsucc}]
  Note that $C<A$ if and only if $C=\ordsl A a$ for some $a:A$.
  This gives an isomorphism $A \cong \ordsl \ord A$, so that $A<\ord$.
  Thus we may take $B\defeq\ord$.
\end{proof}

The second proof would be valid if we had stated \cref{thm:ordsucc} in a typically ambiguous style.
But the resulting lemma would be less useful, because the second proof would constrain the second ``\ord'' in the lemma statement to refer to a higher universe level than the first one.
The first proof allows both universes to be the same.

Similar remarks apply to the next lemma, which could be proved in a less useful way by observing that $A\le \ord$ for any $A:\ord$.

\begin{lem}\label{thm:ordunion}
  Let \bbU be a universe.
  For any $X:\type$ and $F:X\to \ord_\bbU$, there exists $B:\ord_\bbU$ such that $Fx\le B$ for all $x:X$.
\end{lem}
\begin{proof}
  Let $B$ be the set-quotient (see \cref{rmk:quotient-of-non-set}) of the equivalence relation $\eqr$ on $\sm{x:X} Fx$ defined as follows:
  \[ (x,y) \eqr (x',y')
  \;\defeq\;
  \Big(\ordsl{(Fx)}{y} \cong \ordsl{(Fx')}{y'}\Big).
  \]
  Define $(x,y)<(x',y')$ if $\ordsl{(Fx)}{y} < \ordsl{(Fx')}{y'}$.
  This clearly descends to the quotient, and can be seen to make $B$ into an ordinal.
  Moreover, for each $x:X$ the induced map $Fx\to B$ is a simulation.
\end{proof}



\section{Classical well-orderings}
\label{sec:wellorderings}

\index{denial|(}%
We now show the equivalence of our ordinals with the more familiar classical\index{mathematics!classical} well-orderings.

\begin{lem}
  \index{excluded middle}%
  Assuming excluded middle, every ordinal is trichotomous:
  \index{trichotomy of ordinals}%
  \index{ordinal!trichotomy of}%
  \[ \fall{a,b:A} (a<b) \vee (a=b) \vee (b<a). \]
\end{lem}
\begin{proof}
  By induction on $a$, we may assume that for every $a'<a$ and every $b':A$, we have $(a'<b') \vee (a'=b') \vee (b'<a')$.
  Now by induction on $b$, we may assume that for every $b'<b$, we have $(a<b') \vee (a=b') \vee (b'<a)$.

  By excluded middle, either there merely exists a $b'<b$ such that $a<b'$, or there merely exists a $b'<b$ such that $a=b'$, or for every $b'<b$ we have $b'<a$.
  In the first case, merely $a<b$ by transitivity, hence $a<b$ as it is a mere proposition.
  Similarly, in the second case, $a<b$ by transport.
  Thus, suppose $\fall{b':A}(b'<b)\to (b'<a)$.

  Now analogously, either there merely exists $a'<a$ such that $b<a'$, or there merely exists $a'<a$ such that $a'=b$, or for every $a'<a$ we have $a'<b$.
  In the first and second cases, $b<a$, so we may suppose $\fall{a':A}(a'<a)\to (a'<b)$.
  However, by extensionality, our two suppositions now imply $a=b$.
\end{proof}

\begin{lem}
  A well-founded relation contains no cycles, i.e.\
  \[ \fall{n:\mathbb{N}}{a:\mathbb{N}_n\to A} \neg\Big((a_0<a_1) \wedge \dots \wedge (a_{n-1}<a_n)\wedge (a_n<a_0)\Big). \]
\end{lem}
\begin{proof}
  We prove by induction on $a:A$ that there is no cycle containing $a$.
  Thus, suppose by induction that for all $a'<a$, there is no cycle containing $a'$.
  But in any cycle containing $a$, there is some element less than $a$ and contained in the same cycle.
\end{proof}

\indexdef{relation!irreflexive}%
\index{irreflexivity!of well-founded relation}%
In particular, a well-founded relation must be \define{irreflexive}, i.e.\ $\neg(a<a)$ for all $a$.

\begin{thm}\label{thm:wellorder}
  Assuming excluded middle, $(A,<)$ is an ordinal if and only if every nonempty subset $B\subseteq A$ has a least element.
\end{thm}
\begin{proof}
  If $A$ is an ordinal, then by \cref{thm:wfmin} every nonempty subset merely has a minimal element.
  But trichotomy implies that any minimal element is a least element.
  Moreover, least elements are unique when they exist, so merely having one is as good as having one.

  Conversely, if every nonempty subset has a least element, then by \cref{thm:wfmin}, $A$ is well-founded.
  We also have trichotomy, since for any $a,b$ the subset
  $ \setof{a,b} \defeq \setof{x:A | x=a \lor x=b} $
  merely has a least element, which must be either $a$ or $b$.
  This implies transitivity, since if $a<b$ and $b<c$, then either $a=c$ or $c<a$ would produce a cycle.
  Similarly, it implies extensionality, for if $\fall{c:A}(c<a)\Leftrightarrow (c<b)$, then $a<b$ implies (letting $c$ be $a$) that $a<a$, which is a cycle, and similarly if $b<a$; hence $a=b$.
\end{proof}

In classical\index{mathematics!classical} mathematics, the characterization of \cref{thm:wellorder} is taken as the definition of a \emph{well-ordering}, with the \emph{ordinals} being a canonical set of representatives of isomorphism classes for well-orderings.
In our context, the structure identity principle means that there is no need to look for such representatives: any well-ordering is as good as any other.

We now move on to consider consequences of the axiom of choice.
For any set $X$, let $\powerp X$ denote the type of merely inhabited subsets of $X$:
\symlabel{inhabited-powerset}
\[ \powerp X \defeq \setof{ Y : \power X | \exis{x:X} x\in Y}. \]
Assuming excluded middle, this is equivalently the type of \emph{nonempty}\index{nonempty subset} subsets of $X$, and we have $\power X \eqvsym (\powerp X) + \unit$.

\begin{thm}\label{thm:wop}
  \index{axiom!of choice}%
  \index{excluded middle}%
  Assuming excluded middle, the following are equivalent.
  \begin{enumerate}
  \item For every set $X$, there merely exists a function
    $ f: \powerp X \to X $
    such that $f(Y)\in Y$ for all $Y:\powerp X$.\label{item:wop1}
  \item Every set merely admits the structure of an ordinal.\label{item:wop2}
  \end{enumerate}
\end{thm}

\noindent
Of course,~\ref{item:wop1} is a standard classical\index{mathematics!classical} version of the axiom of choice; see \cref{ex:choice-function}.

\begin{proof}
  One direction is easy: suppose~\ref{item:wop2}.
  Since we aim to prove the mere proposition~\ref{item:wop1}, we may assume $A$ is an ordinal.
  But then we can define $f(B)$ to be the least element of $B$.

  Now suppose~\ref{item:wop1}.
  As before, since~\ref{item:wop2} is a mere proposition, we may assume given such an $f$.
  We extend $f$ to a function
  \[ \bar f:\power X \eqvsym (\powerp X) + \unit \longrightarrow X+\unit
  \]
  in the obvious way.
  Now for any ordinal $A$, we can define $g_A:A\to X+\unit$ by well-founded recursion:
  \[ g_A(a) \defeq
    \bar f\Big(X \setminus \setof{ g_A(b) | \strut (b<a) \wedge (g_A(b) \in X) }\Big)
  \]
  (regarding $X$ as a subset of $X+\unit$ in the obvious way).

  Let $A'\defeq \setof{a:A | g_A(a) \in X}$ be the preimage of $X\subseteq X+\unit$; then we claim the restriction $g_A':A' \to X$ is injective.
  For if $a,a':A$ with $a\neq a'$, then by trichotomy and without loss of generality, we may assume $a'<a$.
  Thus $g_A(a') \in \setof{ g_A(b) | b<a }$, so since $f(Y)\in Y$ for all $Y$ we have $g_A(a) \neq g_A(a')$.

  Moreover, $A'$ is an initial segment of $A$.
  For $g_A(a)$ lies in \unit if and only if $\setof{g_A(b)|b<a} = X$, and if this holds then it also holds for any $a'>a$.
  Thus, $A'$ is itself an ordinal.

  Finally, since \ord is an ordinal, we can take $A\defeq\ord$.
  Let $X'$ be the image of $g_\ord':\ord' \to X$; then the inverse of $g_\ord'$ yields an injection $H:X'\to \ord$.
  By \cref{thm:ordunion}, there is an ordinal $C$ such that $Hx\le C$ for all $x:X'$.
  Then by \cref{thm:ordsucc}, there is a further ordinal $D$ such that $C<D$, hence $Hx<D$ for all $x:X'$.
  Now we have
  \begin{align*}
    g_{\ord}(D) &= \bar f\Big( X \setminus \setof{ g_\ord(B) | \rule{0pt}{1em} B<D \wedge (g_\ord(B) \in X)} \Big)\\
    &=\bar f\Big( X \setminus \setof{ g_\ord(B) | \rule{0pt}{1em} g_\ord(B) \in X} \Big)
  \end{align*}
  since if $B:\ord$ and $(g_\ord(B) \in X)$, then $B = Hx$ for some $x:X'$, hence $B<D$.
  Now if
  \[\setof{ g_\ord(B) | \rule{0pt}{1em} g_\ord(B) \in X}\]
  is not all of $X$, then $g_\ord(D)$ would lie in $X$ but not in this subset, which would be a contradiction since $D$ is itself a potential value for $B$.
  So this set must be all of $X$, and hence $g_\ord'$ is surjective as well as injective.
  Thus, we can transport the ordinal structure on $\ord'$ to $X$.
\end{proof}

\begin{rmk}
  If we had given the wrong proof of \cref{thm:ordsucc} or \cref{thm:ordunion}, then the resulting proof of \cref{thm:wop} would be invalid: there would be no way to consistently assign universe levels\index{universe level}.
  As it is, we require propositional resizing (which follows from \LEM{}) to ensure that $X'$ lives in the same universe as $X$ (up to equivalence).
\end{rmk}

\begin{cor}
  Assuming the axiom of choice, the function $\ord\to\set$ (which forgets the order structure) is a surjection.
\end{cor}

Note that \ord is a set, while \set is a 1-type.
In general, there is no reason for a 1-type to admit any surjective function from a set.
Even the axiom of choice does not appear to imply that \emph{every} 1-type does so (although see \cref{ex:acnm-surjset}), but it readily implies that this is so for 1-types constructed out of \set, such as the types of objects of categories of structures as in \cref{sec:sip}.
The following corollary also applies to such categories.

\begin{cor}
  \index{weak equivalence!of precategories}%
  Assuming \choice{}, \uset admits a weak equivalence functor from a strict category.
\end{cor}
\begin{proof}
  Let $X_0\defeq \ord$, and for $A,B:X_0$ let $\hom_X(A,B) \defeq (A\to B)$.
  Then $X$ is a strict category, since \ord is a set, and the above surjection $X_0 \to \set$ extends to a weak equivalence functor $X\to \uset$.
\end{proof}

Now recall from \cref{sec:cardinals} that we have a further surjection $\cd{\blank}:\set\to\card$, and hence a composite surjection $\ord\to\card$ which sends each ordinal to its cardinality.

\begin{thm}
  Assuming \choice{}, the surjection $\ord\to\card$ has a section.
\end{thm}
\begin{proof}
  There is an easy and wrong proof of this: since \ord and \card are both sets, \choice{} implies that any surjection between them \emph{merely} has a section.
  However, we actually have a canonical \emph{specified} section: because \ord is an ordinal, every nonempty subset of it has a uniquely specified least element.
  Thus, we can map each cardinal to the least element in the corresponding fiber.
\end{proof}

It is traditional in set theory to identify cardinals with their image in \ord: the least ordinal having that cardinality.

It follows that \card also canonically admits the structure of an ordinal: in fact, one isomorphic to \ord.
Specifically, we define by well-founded recursion a function $\aleph:\ord\to\ord$, such that $\aleph(A)$ is the least ordinal having cardinality greater than $\aleph({\ordsl A a})$ for all $a:A$.
Then (assuming \choice{}) the image of $\aleph$ is exactly the image of \card.

\index{denial|)}%

\index{ordinal|)}%

\section{The cumulative hierarchy}
\label{sec:cumulative-hierarchy}

\index{bargaining|(}%
We can define a cumulative hierarchy $V$ of all sets in a given universe $\UU$ as a higher inductive type, in such a way that $V$ is again a set (in a larger universe $\UU'$), equipped with a binary ``membership'' relation $x\in y$ which satisfies the usual laws of set theory.

\begin{defn}\label{defn:V}
  The \define{cumulative hierarchy}
  \indexdef{cumulative!hierarchy, set-theoretic}%
  \indexdef{hierarchy!cumulative, set-theoretic}%
  $V$ relative to a type universe $\UU$ is the
  higher inductive type generated by the following constructors.
  %
  \begin{enumerate}
  \item For every $A : \UU$ and $f : A \to V$, there is an element $\vset(A, f) : V$.
  \item For all $A, B : \UU$, $f : A \to V$ and $g : B \to V$ such that
    %
    \begin{narrowmultline} \label{eq:V-path}
      \big(\fall{a:A} \exis{b:B} \id[V]{f(a)}{g(b)}\big) \land \narrowbreak
      \big(\fall{b:B} \exis{a:A} \id[V]{f(a)}{g(b)}\big)
    \end{narrowmultline}
    %
    there is a path $\id[V]{\vset(A,f)}{\vset(B,g)}$.
  \item The 0-truncation constructor: for all $x,y:V$ and $p,q:x=y$, we have $p=q$.
  \end{enumerate}
\end{defn}

In set-theoretic language, $\vset(A,f)$ can be understood as the set (in the sense of classical set theory) that is the image of $A$ under $f$, i.e.\ $\setof{ f(a) | a \in A }$.
However, we will avoid this notation, since it would clash with our notation for subtypes (but see~\eqref{eq:class-notation} and \cref{def:TypeOfElements} below).

The hierarchy $V$ is
bootstrapped from the empty map $\rec\emptyt(V) : \emptyt \to V$, which gives the empty set as $\emptyset = \vset(\emptyt,\rec\emptyt(V))$.
Then the singleton $\{\emptyset\}$ enters $V$ through $\unit \to V$, defined as $\ttt \mapsto \emptyset$, and so
on.
(The definition can also be adapted to include an arbitrary set of ``atoms'' or ``urelements'', by adding an additional point constructor.)
The type $V$ lives in the same universe as the base universe $\UU$.

The second constructor of $V$ has a form unlike any we have seen before: it involves not only paths in $V$ (which in \cref{sec:hittruncations} we claimed were slightly fishy) but truncations of sums of them.
It certainly does not fit the general scheme described in \cref{sec:naturality}, and thus it may not be obvious what its induction principle should be.
Fortunately, like our first definition of the 0-truncation in \cref{sec:hittruncations}, it can be re-expressed using auxiliary higher inductive types.
We leave it to the reader to work out the details (see \cref{ex:cumhierhit}).

\index{induction principle!for cumulative hierarchy}%
At the end of the day, the induction principle for $V$ (written in pattern matching language) says that given $P:V\to \set$, in order to construct $h:\prd{x:V} P(x)$, it suffices to give the following.
\begin{enumerate}
\item For any $f:A\to V$, construct $h(\vset(A,f))$, assuming as given $h(f(a))$ for all $a:A$.
\item Verify that if $f : A \to V$ and $g : B \to V$ satisfy~\eqref{eq:V-path}, then $\dpath{P}{q}{h(\vset(A,f))}{h(\vset(B,g))}$, where $q$ is the path arising from the second constructor of $V$ and~\eqref{eq:V-path}, assuming inductively that $h(f(a))$ and $h(g(b))$ are defined for all $a:A$ and $b:B$, and that the following condition holds:
\begin{eqnarray*}
    &       & \big(\fall{a:A} \exis{b:B} \exis{p:f(a)=g(b)} \dpath{P}{p}{h(f(a))}{h(g(b))}\big) \\
    & \land & \big(\fall{b:B} \exis{a:A} \exis{p:f(a)=g(b)} \dpath{P}{p}{h(f(a))}{h(g(b))}\big)
\end{eqnarray*}
\end{enumerate}
The second clause checks that the map being defined must respect the paths introduced in \eqref{eq:V-path}.
As usual when we state higher induction principles using pattern matching, it may seem tautologous, but is not.
The point is that ``$h(f(a))$'' is essentially a formal symbol which we cannot peek inside of, which $h(\vset(A,f))$ must be defined in terms of. Thus, in the second clause, we assume equality of these formal symbols when appropriate, and verify that the elements resulting from the construction of the first clause are also equal.
Of course, if $P$ is a family of mere propositions, then the second clause is automatic.

Observe that, by induction, for each $v:V$ there merely exist $A:\UU$ and $f:A\to V$ such that $v=\vset(A,f)$.
Thus, it is reasonable to try to define the \define{membership relation}
\indexdef{membership, for cumulative hierarchy}%
$x\in v$ on $V$ by setting:
%
% Note: "membership" rather than "elementhood", because "element" is taken.
%
\symlabel{V-membership}
\begin{equation*}
  (x \in \vset(A,f)) \defeq (\exis{a : A} x = f(a)).
\end{equation*}
%
To see that the definition is valid, we must use the recursion principle of $V$.  Thus, suppose we have a path $\vset(A, f) = \vset(B, g)$
constructed through~\eqref{eq:V-path}. If $x \in \vset(A,f)$ then there merely is $a : A$ such
that $x = f(a)$, but by~\eqref{eq:V-path} there merely is $b : B$ such that $f(a) = g(b)$, hence
$x = g(b)$ and $x \in \vset(B,g)$. The converse is symmetric.

The \define{subset relation}
\indexdef{subset!relation on the cumulative hierarchy}%
$x\subseteq y$ is defined on $V$ as usual by
%
\begin{equation*}
  (x \subseteq y) \defeq \fall{z : V} z \in x \Rightarrow z \in y.
\end{equation*}

A \define{class}
\indexdef{class}%
may be taken to be a mere predicate on~$V$. We can say that a class $C : V \to \prop$ is a
\define{$V$-set}
\indexdef{set!in the cumulative hierarchy}%
if there merely exists $v:V$ such that
%
\begin{equation*}
  \fall{x : V} C(x) \Leftrightarrow x \in v.
\end{equation*}
We may also use the conventional notation for classes, which matches our standard notation for subtypes:
\begin{equation}
  \setof{ x | C(x) } \defeq \lam{x}C(x).\label{eq:class-notation}
\end{equation}
%
A class $C: V\to \prop$ will be called \define{$\UU$-small}
\indexdef{class!small}%
\indexdef{small!class}%
if all of its values $C(x)$ lie in $\UU$, specifically $C: V\to \prop_{\UU}$.
Since $V$ lives in the same universe $\UU'$ as does the base universe $\UU$ from which it is built, the same is true for the identity types $v=_V w$ for any $v,w:V$. To obtain a well-behaved theory in the absence of propositional resizing,
\index{propositional!resizing}%
\index{resizing}%
therefore, it will be convenient to have a $\UU$-small ``resizing'' of the identity relation, which we can define by induction as follows.

\begin{defn}\label{def:bisimulation}
  Define the \define{bisimulation}
  \indexdef{bisimulation}%
  relation
  %
  \begin{equation*}
    \mathord\bisim : V \times V \longrightarrow \prop_{\UU}
  \end{equation*}
  %
  by double induction over $V$, where for $\vset(A,f)$ and $\vset(B,g)$ we let:
  \begin{narrowmultline*}
    \vset(A,f)  \bisim \vset(B,g) \defeq \narrowbreak
    \big(\fall{a:A}\exis{b:B} f(a)  \bisim g(b)\big) \land
    \big(\fall{b:B}\exis{a:A} f(a) \bisim g(b)\big).
  \end{narrowmultline*}
\end{defn}
%
To verify that the definition is correct, we just need to check that it respects paths $\vset(A, f) = \vset(B, g)$ constructed through~\eqref{eq:V-path}, but this is obvious, and that $\prop_{\UU}$ is a set, which it is.  Note that $u \bisim v$ is in $\propU$ by construction.

\begin{lem}\label{lem:BisimEqualsId}
For any $u,v:V$ we have $(u=_V v) = (u \bisim v)$.
\end{lem}

\begin{proof}
An easy induction shows that $\bisim$ is reflexive, so by transport we have $(u=_V v)\to (u \bisim v)$.
Thus, it remains to show that $(u \bisim v)\to (u=_V v)$.
By induction on $u$ and $v$, we may assume they are $\vset(A,f)$ and $\vset(B,g)$ respectively.
(We can ignore the path constructors of $V$, since $(u \bisim v)\to (u=_V v)$ is a mere proposition.)
Then by definition, $\vset(A,f)\bisim\vset(B,g)$ implies $(\fall{a:A}\exis{b:B}f(a)  \bisim g(b))$ and conversely.
But the inductive hypothesis then tells us that $(\fall{a:A}\exis{b:B}f(a) = g(b))$ and conversely.
So by the path con\-struc\-tor for $V$ we have $\vset(A,f) =_V \vset(B,g)$.
\end{proof}

One might think that we could omit the 0-truncation constructor of $V$ and \emph{prove} that $V$ is 0-truncated by applying \cref{thm:h-set-refrel-in-paths-sets} to the bisimulation.
However, in the proof of \cref{lem:BisimEqualsId} we used the fact that $V$ is 0-truncated, to conclude that $(u \bisim v)\to (u=_V v)$ is a mere proposition so that in the induction it suffices to assume $u$ and $v$ are $\vset(A,f)$ and $\vset(B,g)$.

Now we can use the resized identity relation to get the following useful principle.

\begin{lem}\label{lem:MonicSetPresent}
For every $u:V$ there is a given $A_u:\UU$ and monic $m_u: A_u \mono V$ such that $u = \vset(A_u, m_u)$.
\end{lem}

\begin{proof}
  Take any presentation $u = \vset(A,f)$ and factor $f:A\to V$ as a surjection followed by an injection:
  %
  \begin{equation*}
    f = m_u\circ e_u : A \epi A_u \mono V.
  \end{equation*}
  %
  Clearly $u = \vset(A_u, m_u)$ if only $A_u$ is still in $\UU$, which holds if the kernel of $e_u : A \epi A_u$ is in $\UU$.  But the kernel of $e_u : A \epi A_u$ is the pullback along $f : A\to V$ of the identity on $V$, which we just showed to be $\UU$-small, up to equivalence.  Now, this construction of the pair $(A_u, m_u)$ with $m_u :A_u \mono V$ and $u = \vset(A_u, m_u)$ from $u:V$ is unique up to equivalence over $V$, and hence up to identity by univalence.  Thus by the principle of unique choice \eqref{cor:UC} there is a map $c : V\to\sm{A:\UU}(A\to V)$ such that $c(u) = (A_u, m_u)$, with $m_u :A_u \mono V$ and $u = \vset(c(u))$, as claimed.
\end{proof}

\begin{defn}\label{def:TypeOfElements}
  For $u:V$, the just constructed monic presentation $m_u: A_u \mono V$ such that $u = \vset(A_u, m_u)$ may be called the \define{type of members}
  \indexdef{type!of members}%
  of $u$ and denoted $m_u : [u] \mono V$, or even $[u] \mono V$.  We can think of $[u]$ as the ``subclass of $V$ consisting of members of $u$''.
\end{defn}

\begin{thm}\label{thm:VisCST}
  \index{axiom!of set theory, for the cumulative hierarchy}%
  The following hold for $(V, {\in})$:
  %
  \begin{enumerate}
  \item \emph{extensionality:}
    %
    \begin{equation*}
      \fall{x, y : V} x \subseteq y \land y \subseteq x \Leftrightarrow x = y.
    \end{equation*}
    %
     \item \emph{empty set:} for all $x:V$, we have $\neg (x\in \emptyset)$.
    %
    \item \emph{pairing:} for all $u, v:V$, the class $\{u, v\} \defeq \setof{ x | x = u \vee x = v}$ is a $V$-set.
      %
    \item \emph{infinity:}\index{axiom!of infinity}  there is a $v:V$ with $\emptyset\in v$ and $x\in v$ implies $x\cup \{x\}\in v$.
    %
  \item \emph{union:} for all $v:V$, the class $\cup v\defeq \setof{ x | \exis{u:V} x \in u \in v}$ is a $V$-set.
    %
    \item \emph{function set:} for all $u, v:V$, the class $v^u \defeq \setof{ x | x : u\to v}$ is a $V$-set.%
      \footnote{Here $x:u\to v$ means that $x$ is an appropriate set of ordered pairs, according to the usual way of encoding functions in set theory.}
    %
   \item \emph{$\in$-induction:} if $C : V \to \prop$ is a class such that $C(a)$ holds whenever $C(x)$ for all $x\in a$, then $C(v)$ for all $v:V$.
   %
     \item \emph{replacement:}\index{axiom!of replacement} given any $r : V \to V$ and $x : V$, the class
       %
       \begin{equation*}
         \setof{ y | \exis{z : V} z \in x \land y = r(z)}
       \end{equation*}
       %
       is a $V$-set.
  %
   \item \emph{separation:}\index{axiom!of separation}  given any $a : V$ and $\UU$-small $C : V \to \propU$, the class
     %
     \begin{equation*}
       \setof{ x | x \in a \land C(x)}
     \end{equation*}
     %
     is a $V$-set.
  \end{enumerate}
\end{thm}


\begin{proof}[Sketch of proof]
  \mbox{}
  %
  \begin{enumerate}
  \item Extensionality: if $\vset(A,f) \subseteq \vset(B, g)$ then $f(a) \in \vset(B, g)$
    for every $a : A$, therefore for every $a : A$ there merely exists $b : B$ such that
    $f(a) = g(b)$. The assumption $\vset(B, g) \subseteq \vset(A, f)$ gives the other half
    of~\eqref{eq:V-path}, therefore $\vset(A,f) = \vset(B,g)$.

  \item Empty set: suppose $x\in \emptyset = \vset(\emptyt,\rec\emptyt(V))$.  Then $\exis{a:\emptyt}x=\, \rec\emptyt(V,a)$, which is absurd.

  \item Pairing: given $u$ and $v$, let $w=\vset(\bool,\rec\bool(V,u,v))$.
    \index{pair!unordered}

  \item Infinity: take $w = \vset(\nat,I)$, where $I: \nat \to V$ is given by the recursion $I(0) \defeq \emptyset$ and $I(n+1) \defeq I(n)\cup \{I(n)\}$.

  \item Union: Take any $v:V$ and any presentation $f :A\to V$ with $v=\vset(A,f)$.  Then let $\tilde{A} \defeq \sm{a:A}[fa]$, where $m_{fa} : [fa] \mono V$ is the type of members from \cref{def:TypeOfElements}.  $\tilde{A}$ is plainly $\UU$-small, and we have $\cup v \defeq \vset(\tilde{A}, \lam{x} m_{f(\proj1(x))}(\proj2(x)))$.

  \item Function set: given $u, v:V$, take the types of members $[u] \mono V$ and $[v] \mono V$, and the function type $[u]\to [v]$.  We want to define a map
  \[
 r: ([u]\to [v])\ \longrightarrow\ V
  \]
   with ``$r(f) = \setof{ \pairr{x, f(x)} | x : [u] }$'', but in order for this to make sense we must first define the ordered pair $\pairr{x, y}$, and then we take the map $r': x \mapsto \pairr{x, f(x)}$, and then we can put $r(f)\defeq \vset([u], r')$.  But the ordered pair can be defined in terms of unordered pairing as usual.

  \item $\in$-induction: let $C : V \to \prop$ be a class such that $C(a)$ holds whenever $C(x)$ for all $x\in a$, and take any $v=\vset(B,g)$.  To show that $C(v)$ by induction, assume that $C(g(b))$ for all $b:B$.  For every $x\in v$ there merely exists some $b:B$ with $x = g(b)$, and so $C(x)$.  Thus $C(v)$.

  \item Replacement: let $C$ denote the class in question.
    The statement ``$C$ is a $V$-set'' is a mere proposition, so we may
    proceed by induction as follows. Supposing $x$ is $\vset(A, f)$, we claim that $w
    \defeq \vset(A, r \circ f)$ is the set we are looking for.  If $C(y)$ then there merely exists
    $z : V$ and $a : A$ such that $z = f(a)$ and $y = r(z)$, therefore $y \in w$.
    Conversely, if $y \in w$ then there merely exists $a : A$ such that $y = r(f(a))$, so
    if we take $z \defeq f(a)$ we see that $C(y)$ holds.

  \item Let us say that a class $C: V\to\prop$ is \define{separable}
    \indexdef{class!separable}%
    \indexdef{separable class}%
    if for any $a:V$ the class
  %
  \symlabel{class-intersection}
  \begin{equation*}
    a \cap C \defeq\setof{x | x\in a \wedge C(x)}
  \end{equation*}
  %
  is a $V$-set.
We need to show that any $\UU$-small  $C: V \to \propU$ is separable. Indeed, given $a=\vset(A,f)$, let $A' = \sm{x:A}C(fx)$, and take $f' = f\circ i$, where $i : A' \to A$ is the obvious inclusion.  Then we can take $a' = \vset(A',f')$ and we have $x\in a\wedge C(x) \Leftrightarrow x\in a'$ as claimed.  We needed the assumption that $C$ lands in $\UU$ in order for $A' = \sm{x:A}C(fx)$ to be in $\UU$.\qedhere
\end{enumerate}
\end{proof}

It is also convenient to have a strictly syntactic criterion of separability, so that one can read off from the expression for a class that it produces a $V$-set.  One such familiar condition is being ``$\Delta_0$'', which means that the expression is built up from equality $x=_V y$ and membership $x\in y$, using only mere-propositional connectives $\neg$, $\land$, $\lor$, $\Rightarrow$ and quantifiers $\forall$, $\exists$ over particular sets, i.e.\ of the form $\exists(x\in a)$ and $\forall(y\in b)$ (these are called \define{bounded} quantifiers\index{bounded!quantifier}\index{quantifier!bounded}).\indexdef{separation!.Delta0@$\Delta_0$}%

\begin{cor}\label{cor:Delta0sep}
If the class $C: V \to \prop$ is $\Delta_0$ in the above sense, then it is separable.
\end{cor}
\index{axiom!of $\Delta_0$-separation}%

\begin{proof}
Recall that we have a $\UU$-small resizing $x \bisim y$ of identity $x = y$. Since $x\in y$ is defined in terms of $x=y$, we also have a $\UU$-small resizing of membership
%
\symlabel{resized-membership}
\begin{equation*}
  x\bin\vset(A,f) \defeq \exis{a:A} x \bisim f(a).
\end{equation*}
%
Now, let $\Phi$ be a $\Delta_0$ expression for $C$, so that as classes $\Phi = C$ (strictly speaking, we should distinguish expressions from their meanings, but we will blur the difference). Let $\widetilde{\Phi}$ be the result of replacing all occurrences of $=$ and $\in$ by their resized equivalents $\bisim$ and $\bin$.  Clearly then $\widetilde{\Phi}$ also expresses $C$, in the sense that for all $x:V$, $\widetilde{\Phi}(x) \Leftrightarrow C(x)$, and hence $\widetilde{\Phi}=C$ by univalence.  It now suffices to show that $\widetilde{\Phi}$ is $\UU$-small, for then it will be separable by the theorem.

We show that  $\widetilde{\Phi}$ is $\UU$-small by induction on the construction of the expression.  The base cases are $x \bisim y$ and $x\bin y$, which have already been resized into $\UU$.  It is also clear that $\UU$ is closed under the mere-propositional operations (and $(-1)$-truncation), so it just remains to check the bounded quantifiers $\exists(x\in a)$ and $\forall(y\in b)$.  By definition,
\begin{align*}
\exists(x\in a) P(x) &\defeq \Brck {\sm{x:V}(x\bin a \land P(x))},\\
\forall(y\in b) P(x) &\defeq  \prd{x:V}(x\bin a \to P(x)).
\end{align*}
Let us consider $\brck {\sm{x:V}(x\bin a \land P(x))}$.  Although the body $(x\bin a \land P(x))$ is $\UU$-small since $P(x)$ is so by the inductive hypothesis, the quantification over $V$ need not stay inside $\UU$.  However, in the present case we can replace this with a quantification over the type $[a]\mono V$ of members of $a$, and easily show that
\begin{equation*}
  \sm{x:V}(x\bin a \land P(x)) = \sm{x:[a]} P(x).
\end{equation*}
The right-hand side does remain in $\UU$, since both $[a]$ and $P(x)$ are in $\UU$.  The case of $\prd{x:V}(x\bin a \to P(x))$ is analogous, using $\prd{x:V}(x\bin a \to P(x)) = \prd{x:[a]}P(x)$.
\end{proof}

We have shown that in type theory with a universe $\UU$, the cumulative hierarchy $V$ is a model of a ``constructive set theory''
\index{constructive!set theory}%
with many of the standard axioms.
However, as far as we know, it lacks the \emph{strong collection}
\index{axiom!strong collection}%
\index{collection!strong}%
\index{strong!collection}%
and \emph{subset collection}
\index{axiom!subset collection}%
\index{collection!subset}%
\index{subset!collection}%
axioms which are included in \CZF{}~\cite{AczelCZF}.
In the usual interpretation of this set theory into type theory, these two axioms are consequences of the setoid-like definition of equality; while in other constructed models of set theory, strong collection may hold for other reasons.
We do not know whether either of these axioms holds in our model $(V,\in)$, but it seems unlikely.
Since $V$ is a higher inductive type \emph{inside} the system, rather than being an \emph{external} construction, it is not surprising that it differs in some ways from prior interpretations.

Finally, consider the result of adding the axiom of choice for sets to our type theory, in the form  $\choice{}$ from \cref{subsec:emacinsets} above.  This has the consequence that $\LEM{}$ then also holds, by \cref{thm:1surj_to_surj_to_pem}, and so $\set$ is a topos\index{topos} with subobject classifier $\bool$, by \cref{thm:settopos}.  In this case, we have $\prop = \bool:\UU$, and so \emph{all classes are separable}.
Thus we have shown:

\begin{lem}\label{lem:fullsep}
  In type theory with $\choice{}$, the law of \define{(full) separation}
  \indexdef{separation!full}%
  holds for $V$: given \emph{any} class $C : V \to \prop$ and $a : V$, the class $a \cap C$ is a $V$-set.
\end{lem}

\begin{thm}\label{thm:zfc}
In type theory with $\choice{}$ and a universe $\UU$, the cumulative hierarchy $V$ is a model of Zermelo--Fraenkel\index{set theory!Zermelo--Fraenkel} set theory with choice, ZFC.
\end{thm}

\begin{proof}
We have all the axioms listed in \cref{thm:VisCST}, plus full separation, so we just need to show that there are power sets\index{power set} $\power a:V$ for all $a:V$.  But since we have $\LEM{}$ these are simply function types $\power a = (a\to\bool)$.  Thus $V$ is a model of Zermelo--Fraenkel set theory ZF. We leave the verification of the set-theoretic axiom of choice from $\choice{}$ as an easy exercise.
\end{proof}

\index{bargaining|)}%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\sectionNotes

The basic properties one expects of the category of sets date back to the early days of elementary topos theory.
The \emph{Elementary theory of the category of sets} referred to in \cref{subsec:emacinsets} was introduced by Lawvere\index{Lawvere} in
\cite{lawvere:etcs-long}, as a category-theoretic axiomatization of set theory.
\index{Elementary Theory of the Category of Sets}%
The notion of $\Pi W$-pretopos, regarded as a predicative version of an elementary topos, was introduced in~\cite{MoerdijkPalmgren2002}; see also~\cite{palmgren:cetcs}.

The treatment of the category of sets in \cref{sec:piw-pretopos} roughly follows that in~\cite{RijkeSpitters}.
The fact that epimorphisms are surjective (\cref{epis-surj}) is well known in classical mathematics, but is not as trivial as it may seem to prove \emph{predicatively}.
\index{mathematics!predicative}%
The proof in~\cite{Mines/R/R:1988} uses the power set operation (which is impredicative), although it can also be seen as a predicative proof of the weaker statement that a map in a universe $\UU_i$ is surjective if it is an epimorphism in the next universe $\UU_{i+1}$.
A predicative proof for setoids was given by Wilander~\cite{Wilander2010}.
Our proof is similar to Wilander's, but avoids setoids by using pushouts and univalence.

The implication in \cref{thm:1surj_to_surj_to_pem} from $\choice{}$ to $\LEM{}$ is an adaptation to homotopy type
theory of a theorem from topos theory due to Diaconescu~\cite{Diaconescu}; it was posed as a problem already by Bishop~\cite[Problem~2]{Bishop1967}.

For the intuitionistic theory of ordinal numbers, see~\cite{taylor:ordinals,Taylor99} and also \cite{JoyalMoerdijk1995}.
Definitions of well-foundedness in type theory by an induction principle, including the inductive predicate of accessibility\index{accessibility}, were studied in~\cite{Huet80,Paulson86,Nordstrom88}, although the idea dates back to Gentzen's proof of the consistency\index{consistency!of arithmetic} of arithmetic~\cite{Gentzen36}.

The idea of algebraic set theory, which informs our development in \cref{sec:cumulative-hierarchy} of the cumulative hierarchy, is due to~\cite{JoyalMoerdijk1995}, but it derives from earlier work by~\cite{AczelCZF}.
\index{algebraic set theory}%
\index{set theory!algebraic}%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\sectionExercises

\begin{ex}\label{ex:utype-ct}
  Following the pattern of $\uset$, we would like to make a category $\utype$ of all types and maps between them (in a given universe $\UU$).  In order for this to be a category in the sense of \cref{sec:cats}, however, we must first declare $\hom(X,Y) \defeq \pizero{X\to Y}$, with composition defined by induction on truncation from ordinary composition $(Y\to Z) \to (X\to Y) \to (X\to Z)$.  This was defined as the \emph{homotopy precategory of types} in \cref{ct:hoprecat}.  It is still not a category, however, but only a precategory (its type of objects $\UU$ is not even a $0$-type).  It becomes a category by Rezk completion
  \index{completion!Rezk}%
  (see \cref{ct:hocat}), and its type of objects can be identified with $\trunc1\type$ by \cref{ct:ex:hocat}.  Show that the resulting category $\utype$, unlike $\uset$, is not a pretopos.
\end{ex}

\begin{ex}\label{ex:surjections-have-sections-impl-ac}
  Show that if every surjection has a section in the category $\uset$, then the axiom of choice holds.
\end{ex}

\begin{ex}\label{ex:well-pointed}
  Show that with $\LEM{}$, the category $\uset$ is well-pointed,
  \indexdef{category!well-pointed}%
  in the sense that the following statement holds: for any $f, g : A\to B$, if $f \neq g$ then there is a function $a : 1\to A$ such that $f(a) \neq g(a)$.
  Show that the slice category
  \index{category!slice}%
  $\uset/\bool$ consisting of functions $A\to \bool$ and commutative triangles does not have this property.
  (Hint: the terminal object in $\uset/\bool$ is the identity function $\bool \to \bool$, so in this category, there are objects $X$ that have no elements $1\to X$.)
\end{ex}

\begin{ex}\label{ex:add-ordinals}
  \index{addition!of ordinal numbers}%
  Prove that if $(A,<_A)$ and $(B,<_B)$ are well-founded, extensional, or ordinals, then so is $A+B$, with $<$ defined by
  \begin{align*}
    (a<a') &\defeq (a<_A a') & \text{for }& a,a':A\\
    (b<b') &\defeq (b<_B b') & \text{for }& b,b':B\\
    (a<b) &\defeq \unit      & \text{for }& (a:A),(b:B)\\
    (b<a) &\defeq \emptyt    & \text{for }& (a:A),(b:B).
  \end{align*}
\end{ex}
% \begin{proof}
%   We first prove by induction on $<_A$ that every element of $A$ is accessible in $A+B$.
%   This is easy since the only elements less than $a:A$ in $A+B$ are also in $A$.
%   We then prove by induction on $<_B$ that every element of $B$ is accessible in $A+B$.
%   This is easy since we have already proven that every element of $A$ is accessible.
% \end{proof}

\begin{ex}\label{ex:multiply-ordinals}
  \index{multiplication!of ordinal numbers}%
  Prove that if $(A,<_A)$ and $(B,<_B)$ are well-founded, extensional, or ordinals, then so is $A\times B$, with $<$ defined by
  \[ ((a,b) <(a',b')) \defeq (a<_A a') \vee ((a=a') \wedge (b<_B b')). \]
\end{ex}
% \begin{proof}
%   We prove by induction on $<_A$ that for every $a:A$, every element of the form $(a,b)$ is accessible in $A\times B$.
%   The inductive hypothesis is that for all $a'<_A a$, every pair $(a',b)$ is accessible.
%   Inside this induction, we prove by induction on $<_B$ that for every $b:B$, the element $(a,b)$ is accessible.
%   The nested inductive hypothesis is that for every $b'<_B b$, the element $(a,b')$ is accessible.
%   But now, if $(a',b')< (a,b)$, then either $a<_A a'$ in which case $(a',b')$ is accessible by the first inductive hypothesis, or $a=a'$ and $b'<_B b$, in which case $(a,b')$ is accessible by the second inductive hypothesis.
%   Thus, by definition of accessibility, $(a,b)$ is accessible.
%   This completes both inductions.
% \end{proof}

\begin{ex}\label{ex:algebraic-ordinals}
  Define the usual algebraic operations on ordinals, and prove that they satisfy the usual properties.
\end{ex}

\begin{ex}\label{ex:prop-ord}
  Note that $\bool$ is an ordinal, under the obvious relation $<$ such that $\bfalse<\btrue$ only.
  \begin{enumerate}
  \item Define a relation $<$ on $\prop$ which makes it into an ordinal.
  \item Show that $\id[\ord]\bool\prop$ if and only if \LEM{} holds.
  \end{enumerate}
\end{ex}

\begin{ex}\label{ex:ninf-ord}
  Recall that we denote \nat by $\omega$ when regarding it as an ordinal; thus we have also the ordinal $\omega+1$.
  On the other hand, let us define
  \[ \nat_\infty \defeq \setof{a:\nat\to\bool | \fall{n:\nat} (a_n \le a_{\suc(n)}) } \]
  where $\le$ denotes the obvious partial order on $\bool$, with $\bfalse\le\btrue$.
  \begin{enumerate}
  \item Define a relation $<$ on $\nat_\infty$ which makes it into an ordinal.
  \item Show that $\id[\ord]{\omega+1}{\nat_\infty}$ if and only if the limited principle of omniscience~\eqref{eq:lpo} holds.%
    \index{limited principle of omniscience}%
  \end{enumerate}
\end{ex}

\begin{ex}\label{ex:well-founded-extensional-simulation}
  Show that if $(A,<)$ is well-founded and extensional and $A:\UU$, then there is a simulation $A\to V$, where $(V,\in)$ is the cumulative hierarchy from \cref{sec:cumulative-hierarchy} built from the universe~\UU.
\end{ex}

\begin{ex}\label{ex:choice-function}
  Show that \cref{thm:wop}\ref{item:wop1} is equivalent to the axiom of choice~\eqref{eq:ac}.
\end{ex}

\begin{ex}\label{ex:cumhierhit}
  Given types $A$ and $B$, define a \define{bitotal relation}
  \indexsee{bitotal relation}{relation, bitotal}%
  \indexdef{relation!bitotal}%
  to be $R:A\to B\to \prop$ such that
  \[ \Big(\fall{a:A}\exis{b:B} R(a,b) \Big) \land \Big(\fall{b:B}\exis{a:A} R(a,b) \Big). \]
  For such $A,B,R$, let $A\sqcup^R B$ be the higher inductive type generated by
  \begin{itemize}
  \item $i:A\to A\sqcup^R B$
  \item $j:B\to A\sqcup^R B$
  \item For each $a:A$ and $b:B$ such that $R(a,b)$, a path $i(a)=j(b)$.
  \end{itemize}
  Show that the cumulative hierarchy $V$ can be defined by the following more straightforward list of constructors, and that the resulting induction principle is the one given in \cref{sec:cumulative-hierarchy}.
  \begin{itemize}
  \item For every $A : \UU$ and $f : A \to V$, there is an element $\vset(A, f) : V$.
  \item For any $A,B:\UU$ and bitotal relation
    \index{relation!bitotal}%
    $R:A\to B\to \prop$, and any map $h:A\sqcup^R B \to V$, there is a path $\id{\vset(A,h\circ i)}{\vset(B,h\circ j)}$.
  \item The 0-truncation constructor.
  \end{itemize}
\end{ex}

\begin{ex}\label{ex:strong-collection}
  In \CZF, the \define{axiom of strong collection}
  \indexdef{axiom!strong collection}%
  \indexdef{collection!strong}%
  \indexdef{strong!collection}%
  has the form:
   \begin{multline*}
   \Parens{\fall{x\in v}\exis{y} R(x,y)} \Rightarrow \\
   \exis{w}\big[\big(\fall{x\in v}\exis{y\in w}R(x,y)\big)\land \big(\fall{y\in w}\exis{x\in v}R(x,y) \big)\big]
   \end{multline*}
   Does it hold in the cumulative hierarchy $V$?  (We do not know the answer to this.)
\end{ex}

\begin{ex}\label{ex:choice-cumulative-hierarchy-choice}
Verify that, if we assume $\choice{}$, then the cumulative hierarchy $V$ satisfies the usual set-theoretic axiom of choice, which may be stated in the form:
  \[
   \fall{x:V} \Parens{(\fall{y\in x}\exis{z:V} z\in y) \Rightarrow  \exis{c\in(\cup x)^x}\fall{y\in x} c(y)\in y}
   \]
\end{ex}

\begin{ex}\label{ex:plump-ordinals}
  Assuming propositional resizing, show that there is a mere predicate $\mathsf{isPlump}:\ord\to\prop$ such that for any $A:\ord$ we have
  \begin{multline*}\label{eq:plump}
    \mathsf{isPlump}(A) = \Parens{\fall{B<A} \mathsf{isPlump}(B)} \wedge\narrowbreak
    \Parens{\fall{C,B:\ord} C\le B < A \wedge \mathsf{isPlump}(C) \Rightarrow C < A}.
  \end{multline*}
  Note that $\mathsf{isPlump}$ cannot be defined by a simple well-founded induction over \ord; you must use a different well-founded relation.
  We say that an ordinal $A$ is \define{plump}~\cite{taylor:ordinals,Taylor99} if $\mathsf{isPlump}(A)$.
  \index{plump!ordinal}\index{ordinal!plump}%
\end{ex}

\begin{ex}\label{ex:not-plump}
  Show that \LEM{} is equivalent to the statement ``all ordinals are plump''.
\end{ex}

\begin{ex}\label{ex:plump-successor}
  Define the \define{plump successor}\index{plump!successor}\indexdef{successor!plump} of an ordinal $A$ to be
  \[ t(A) \defeq \setof{ B:\ord | (B\le A) \wedge \mathsf{isPlump}(B) } \]
  \begin{enumerate}
  \item By definition, $t(A)$ belongs to the next higher universe.
    Show that assuming propositional resizing, it is equal to an ordinal in the same universe as $A$.
  \item Again assuming propositional resizing, show that if $A$ is plump (\cref{ex:plump-ordinals}) then so is $t(A)$.
  \end{enumerate}
\end{ex}

\begin{ex}\label{ex:ZF-algebras}
  A \define{ZF-algebra}~\cite{JoyalMoerdijk1995}
  \index{ZF-algebra}%
  relative to a universe $\UU_i$ is a poset (see \cref{ct:orders}) $V:\UU_{i+1}$, which has all suprema indexed by types in $\UU_i$, and is equipped with a ``successor'' function $s:V\to V$ (not necessarily respecting $\le$ in any way).
  \begin{enumerate}
  \item Show that the cumulative hierarchy $(V_{\UU_i},\subseteq,s)$ is the initial ZF-algebra, where $s(x)$ is the singleton $\setof{x}$.
  \item Show that $(\ord_{\UU_i},\le,s)$ is the initial ZF-algebra with the property that $x\le s(x)$ for all $x$, where $s(A)=A+\unit$ is the successor\index{successor!of an ordinal} from \cref{thm:ordsucc}.
  \item Assuming propositional resizing, show that $\Parens{\setof{A:\ord_{\UU_i} | \mathsf{isPlump}(A) },\le,t}$ is the initial ZF-algebra with the property that $(x\le y) \Rightarrow (t(x)\le t(y))$ for all $x,y$, where $t$ is the plump successor from \cref{ex:plump-successor}.
  \end{enumerate}
\end{ex}

\begin{ex}\label{ex:monos-are-split-monos-iff-LEM-holds}
  For a category $A$, a morphism $f: \hom_A(a,b)$ is said to be a \define{split monomorphism} if there exists a morphism $g: \hom_A(b,a)$ such that $\id{g \circ f}{1_a}$. (Such $g$ is called a \define{retraction} of $f$.)
  Prove that the following are logically equivalent.
  \begin{enumerate}
  \item $\LEM{}$.
  \item For every sets $A$ and $B$, if $A$ is inhabited then for every monomorphism $f: A \to B$ in $\uset$, $f$ is also a split monomorphism in $\uset$.
  \end{enumerate}
\end{ex}

\index{set|)}%

% Local Variables:
% TeX-master: "hott-online"
% End:

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE HoTT/theory-schema/upstream/book-578b85cc/symbols.tex | SHA256 17d0ca29a5a42f2d658afb432b97b019e09e6f324d83cfff725c7936db3da70c | LINES 1-282/282 =====
\phantomsection % black magic to get TOC to point to correct page
\markboth{}{\textsc{Index of symbols}}
\addcontentsline{toc}{part}{Index of symbols}
\chapter*{Index of symbols}

% Shorthand for \pageref, we have lots of these.
\newcommand{\pg}[1]{p.~\pageref{#1}}
% In the next macro whitespace matters, so be careful
\newcommand{\symbolindex}[2]{\hbox{\makebox[0.2\textwidth][s]{#1\hfill}\hspace*{2.5em}\parbox[t]{0.65\textwidth}{#2\hfill}}\\[1.5pt]}

% The entries in this table are sorted "alphabetically" whatever that means.

{\OPTindexfont % Set same font size as for the index

% MAKE SURE THERE ARE NO EMPTY LINES, OR ELSE WE GET A PARAGRAPH BREAK.
% ALSO, DO NOT INSERT ANY WHITESPACE AT THE BEGINNING OF ARGUMENTS OF \symbolindex
\noindent
%%%%%%%%%% Equalities %%%%%%%%%%
\symbolindex{$x \defeq a$	}{definition, \pg{defn:defeq}}
\symbolindex{$a \jdeq b$	}{judgmental equality, \pg{defn:judgmental-equality}}
\symbolindex{$a =_A b$	}{identity type, \pg{sec:identity-types}}
\symbolindex{$a = b$	}{identity type, \pg{sec:identity-types}}
\symbolindex{$x \defid b$	}{propositional equality by definition, \pg{rmk:defid}}
\symbolindex{$\idtypevar{A}(a,b)$	}{identity type, \pg{sec:identity-types}}
\symbolindex{$\dpath{P}{p}{a}{b}$	}{dependent path type, \pg{eq:dpath}}
\symbolindex{$a \neq b$	}{disequality, \pg{sec:disequality}}
%%%%%%%%%% Stuff that's hard to alphabetize %%%%%%%%%%
\symbolindex{$\refl{x}$	}{reflexivity path at $x$, \pg{sec:identity-types}}
\symbolindex{$\opp{p}$	}{path reversal, \pg{lem:opp}}
\symbolindex{$p\ct q$	}{path concatenation, \pg{lem:concat}}
\symbolindex{$p\leftwhisker r$	}{left whiskering, \pg{thm:EckmannHilton}}
\symbolindex{$r\rightwhisker q$	}{right whiskering, \pg{thm:EckmannHilton}}
\symbolindex{$r\hct s$	}{horizontal concatenation of 2-paths, \pg{thm:EckmannHilton}}
\symbolindex{$g\circ f$	}{composite of functions, \pg{ex:composition}}
\symbolindex{$g\circ f$	}{composite of morphisms in a precategory, \pg{ct:precategory}}
\symbolindex{$\inv{f}$	}{quasi-inverse of an equivalence, \pg{thm:equiv-eqrel}}
\symbolindex{$\inv{f}$	}{inverse of an isomorphism in a precategory, \pg{ct:inv}}
%%%%%%%%%% Numbers etc. %%%%%%%%%%
\symbolindex{$\emptyt$	}{empty type, \pg{sec:coproduct-types}}
\symbolindex{$\unit$	}{unit type, \pg{sec:finite-product-types}}
\symbolindex{$\ttt$	}{canonical inhabitant of $\unit$, \pg{sec:finite-product-types}}
\symbolindex{$\bool$	}{type of booleans, \pg{sec:type-booleans}}
\symbolindex{$\btrue$, $\bfalse$	}{constructors of $\bool$, \pg{sec:type-booleans}}
\symbolindex{$\izero$, $\ione$	}{point constructors of the interval $\interval$, \pg{sec:interval}}
%%%%%%%%%% A %%%%%%%%%%
\symbolindex{$\choice{}$	}{axiom of choice, \pg{eq:ac}}
\symbolindex{$\choice{\infty}$	}{``type-theoretic axiom of choice'', \pg{thm:ttac}}
\symbolindex{$\acc(a)$	}{accessibility predicate, \pg{defn:accessibility}}
\symbolindex{$P \land Q$	}{logical conjunction (``and''), \pg{defn:logical-notation}}
\symbolindex{$\apfunc{f}(p)$ or $\ap{f}{p}$	}{application of $f:A\to B$ to $p:\id[A]xy$, \pg{lem:map}}
\symbolindex{$\apd{f}{p}$	}{application of $f:\prd{a:A} B(a)$ to $p:\id[A]xy$, \pg{lem:mapdep}}
% This is not currently a distinctive notation that someone would look up
% $\aptwo{f}{p}$ & two-dimensional $\apfunc{}$, \pg{thm:ap2}
% \\
\symbolindex{$\apdtwo{f}{p}$	}{two-dimensional dependent $\apfunc{}$, \pg{thm:apd2}}
\symbolindex{$x\apart y$	}{apartness of real numbers, \pg{apart}}
%%%%%%%%%% B %%%%%%%%%%
\symbolindex{$\base$	}{basepoint of $\Sn^1$, \pg{sec:intro-hits}}
\symbolindex{$\base$            }{basepoint of $\Sn^2$, \pg{s2a} and \pg{s2b}}
\symbolindex{$\biinv(f)$        }{proposition that $f$ is bi-invertible, \pg{defn:biinv}}
\symbolindex{$x \bisim y$       }{bisimulation, \pg{def:bisimulation}}
\symbolindex{$\blank$           }{blank used for implicit $\lambda$-abstractions, \pg{blank}}
%%%%%%%%%% C %%%%%%%%%%
\symbolindex{$\CAP$             }{type of Cauchy approximations, \pg{cauchy-approximations}}
\symbolindex{$\card$            }{type of cardinal numbers, \pg{defn:card}}
\symbolindex{$\modal A$         }{reflector or modality applied to $A$, \pg{defn:reflective-subuniverse} and \pg{defn:modality}}
\symbolindex{$\cocone{X}{Y}$    }{type of cocones, \pg{defn:cocone}}
% Not used
%\symbolindex{
%  \cone{X}{Y}$
%}{
%  type of cones
%}
\symbolindex{$\code$            }{family of codes for paths, \pg{sec:compute-coprod}, \pg{S1-universal-cover}, \pg{sec:general-encode-decode}}
\symbolindex{$A \setminus B$    }{subset complement, \pg{complement}}
\symbolindex{$\cons(x,\ell)$    }{concatenation constructor for lists, \pg{lst} and \pg{lst-freemonoid}}
\symbolindex{$\contr_x$         }{path to the center of contraction, \pg{defn:contractible}}
\symbolindex{$\mathcal{F}\cover\pairr{J, \mathcal{G}}$          }{inductive cover, \pg{defn:inductive-cover}}
\symbolindex{$\dcut(L,U)$       }{the property of being a Dedekind cut, \pg{defn:dedekind-reals}}
\symbolindex{$\surr{L}{R}$      }{cut defining a surreal number, \pg{surreal-cut}}
%%%%%%%%%% D %%%%%%%%%%
\symbolindex{$\dgr{X}$          }{morphism reversal in a $\dagger$-category, \pg{sec:dagger-categories}}
\symbolindex{$\decode$          }{decoding function for paths, \pg{sec:compute-coprod}, \pg{S1-universal-cover}, \pg{sec:general-encode-decode}}
%%%%%%%%%% E %%%%%%%%%%
\symbolindex{$\encode$	}{encoding function for paths, \pg{sec:compute-coprod}, \pg{S1-universal-cover}, \pg{sec:general-encode-decode}}
\symbolindex{$\mreturn^\modal_A$ or $\mreturn_A$	}{the function $A\to\modal A$, \pg{defn:reflective-subuniverse} and \pg{defn:modality}}
\symbolindex{$A \epi B$	}{epimorphism or surjection}
\symbolindex{$\noeq(x,y)$	}{path constructor of the surreals, \pg{defn:surreals}}
\symbolindex{$\rceq(u,v)$	}{path constructor of the Cauchy reals, \pg{defn:cauchy-reals}}
\symbolindex{$a \eqr b$	}{an equivalence relation, \pg{equivalencerelation}}
\symbolindex{$\eqv{X}{Y}$	}{type of equivalences, \pg{eq:eqv}}
\symbolindex{$\texteqv{X}{Y}$	}{type of equivalences (same as $\eqv{X}{Y}$)}
\symbolindex{$\cteqv{A}{B}$	}{type of equivalences of categories, \pg{ct:equiv}}
\symbolindex{$P \Leftrightarrow Q$	}{logical equivalence, \pg{defn:logical-notation}}
\symbolindex{$\exis{x:A} B(x)$	}{logical notation for mere existential, \pg{defn:logical-notation}}
\symbolindex{$\extend f$	}{extension of $f:A\to B$ along $\eta_A$, \pg{extend}}
%%%%%%%%%% F %%%%%%%%%%
\symbolindex{$\bot$	}{logical falsity, \pg{defn:logical-notation}}
\symbolindex{$\hfib{f}{b}$	}{fiber of $f:A\to B$ at $b:B$, \pg{defn:homotopy-fiber}}
\symbolindex{$\Fin(n)$  }{standard finite type, \pg{fin}}
\symbolindex{$\fall{x:A} B(x)$	}{logical notation for dependent function type, \pg{defn:logical-notation}}
\symbolindex{$\funext$	}{function extensionality, \pg{axiom:funext}}
\symbolindex{$A\to B$	}{function type, \pg{sec:function-types}}
\symbolindex{$B^A$      }{functor precategory, \pg{ct:functor-precat}}
%%%%%%%%%% G %%%%%%%%%%
\symbolindex{$\glue$	}{path constructor of $A \sqcup^C B$, \pg{sec:colimits}}
%%%%%%%%%% H %%%%%%%%%%
\symbolindex{$\happly$	}{function making a path of functions into a homotopy, \pg{eq:happly}}
\symbolindex{$\hom_A(a,b)$	}{hom-set in a precategory, \pg{ct:precategory}}
\symbolindex{$f \htpy g$	}{homotopy between functions, \pg{defn:homotopy}}
%%%%%%%%%% I %%%%%%%%%%
\symbolindex{$\interval$	}{the interval type, \pg{sec:interval}}
\symbolindex{$\idfunc[A]$	}{the identity function of $A$, \pg{idfunc}}
\symbolindex{$1_a$	}{identity morphism in a precategory, \pg{ct:precategory}}
\symbolindex{$\idtoeqv$	}{function $(A=B)\to(\eqv A B)$ which univalence inverts, \pg{eq:uidtoeqv}}
\symbolindex{$\idtoiso$	}{function $(a=b) \to (a\cong b)$ in a precategory, \pg{ct:idtoiso}}
\symbolindex{$\im(f)$	}{image of map $f$, \pg{defn:modal-image}}
\symbolindex{$\im_n(f)$	}{$n$-image of map $f$, \pg{defn:modal-image}}
\symbolindex{$P \Rightarrow Q$	}{logical implication (``implies''), \pg{defn:logical-notation}}
\symbolindex{$a \in P$	}{membership in a subset or subtype, \pg{membership}}
\symbolindex{$x\in v$	}{membership in the cumulative hierarchy, \pg{V-membership}}
\symbolindex{$x\bin v$	}{resized membership, \pg{resized-membership}}
\symbolindex{$\ind{\emptyt}$	}{induction for ${\emptyt}$, \pg{defn:induction-emptyt},}
\symbolindex{$\ind{\unit}$	}{induction for ${\unit}$, \pg{defn:induction-unit},}
\symbolindex{$\ind{\bool}$	}{induction for ${\bool}$, \pg{defn:induction-bool},}
\symbolindex{$\ind{\nat}$	}{induction for ${\nat}$, \pg{defn:induction-nat}, and}
\symbolindex{$\indid{A}$	}{path induction for $=_A$, \pg{defn:induction-ML-id},}
\symbolindex{$\indidb{A}$	}{based path induction for $=_A$, \pg{defn:induction-PM-id},}
\symbolindex{$\ind{A \times B}$	}{induction for ${A \times B}$, \pg{defn:induction-times},}
\symbolindex{$\ind{\sm{x:A} B(x)}$	}{induction for ${\sm{x:A} B}$, \pg{defn:induction-sm},}
\symbolindex{$\ind{A + B}$	}{induction for ${A + B}$, \pg{defn:induction-plus},}
\symbolindex{$\ind{\wtype{x:A} B(x)}$	}{induction for ${\wtype{x:A} B}$, \pg{defn:induction-wtype}}
\symbolindex{$\ordsl{A}{a}$	}{initial segment of an ordinal, \pg{initial-segment}}
\symbolindex{$\inj(A,B)$	}{type of injections, \pg{inj}}
\symbolindex{$\inl$	}{first injection into a coproduct, \pg{sec:coproduct-types}}
\symbolindex{$\inr$	}{second injection into a coproduct, \pg{sec:coproduct-types}}
\symbolindex{$A \cap B$	}{intersection of subsets, \pg{intersection}, classes, \pg{class-intersection}, or intervals, \pg{interval-intersection}}
\symbolindex{$\iscontr(A)$	}{proposition that $A$ is contractible, \pg{defn:contractible}}
\symbolindex{$\isequiv(f)$	}{proposition that $f$ is an equivalence, \pg{basics-isequiv}, \pg{cha:equivalences}, and \pg{sec:concluding-remarks}}
\symbolindex{$\ishae(f)$	}{proposition that $f$ is a half-adjoint equivalence, \pg{defn:ishae}}
\symbolindex{$a\cong b$	}{type of isomorphisms in a (pre)category, \pg{ct:isomorphism}}
\symbolindex{$A\cong B$	}{type of isomorphisms between precategories, \pg{ct:isocat}}
\symbolindex{$A\cong B$	}{type of isomorphisms between sets, \pg{basics:iso}}
\symbolindex{$a\unitaryiso b$	}{type of unitary isomorphisms, \pg{ct:unitary}}
\symbolindex{$\isotoid$	}{inverse of $\idtoiso$ in a category, \pg{isotoid}}
\symbolindex{$\istype{n}(X)$	}{proposition that $X$ is an $n$-type, \pg{def:hlevel}}
\symbolindex{$\isprop(A)$	}{proposition that $A$ is a mere proposition, \pg{defn:isprop}}
\symbolindex{$\isset(A)$	}{proposition that $A$ is a set, \pg{defn:set}}
%%%%%%%%%% J %%%%%%%%%%
\symbolindex{$A*B$	}{join of $A$ and $B$, \pg{join}}
%%%%%%%%%% K %%%%%%%%%%
\symbolindex{$\ker(f)$	}{kernel of a map of pointed sets, \pg{kernel}}
%%%%%%%%%% L %%%%%%%%%%
\symbolindex{$\lam{x} b(x)$	}{$\lambda$-abstraction, \pg{eq:lambda-abstraction}}
\symbolindex{$\lcoh{f}{g}{\eta}$	}{type of left adjoint coherence data, \pg{defn:lcoh-rcoh}}
\symbolindex{$\LEM{}$	}{law of excluded middle, \pg{eq:lem}}
\symbolindex{$\LEM{\infty}$	}{inconsistent propositions-as-types \LEM{}, \pg{thm:not-lem} and \pg{lem-infty}}
\symbolindex{$x < y$	}{strict inequality on natural numbers, \pg{leq-nat}, ordinals, \pg{sec:ordinals}, Cauchy reals, \pg{lt-RC}, surreals, \pg{defn:surreals}, etc.}
\symbolindex{$x \le y$	}{non-strict inequality on natural numbers, \pg{leq-nat}, Cauchy reals, \pg{leq-RC}, surreals, \pg{defn:surreals}, etc.}
\symbolindex{$\preceq$, $\prec$	}{recursive versions of $\le$ and $<$ for surreals, \pg{defn:No-codes}}
\symbolindex{$\ble$, $\blt$, $\bble$, $\bblt$	}{orderings on codomain of $\NO$-recursion, \pg{NO-recursion}}
\symbolindex{$\rclim(x)$	}{limit of a Cauchy approximation, \pg{defn:cauchy-reals}}
\symbolindex{$\linv(f)$	}{type of left inverses to $f$, \pg{defn:linv-rinv}}
\symbolindex{$\lst{X}$	}{type of lists of elements of $X$, \pg{lst} and \pg{lst-freemonoid}}
\symbolindex{$\lloop$	}{path constructor of $\Sn^1$, \pg{sec:intro-hits}}
%%%%%%%%%% M %%%%%%%%%%
\symbolindex{$\Map_*(A,B)$	}{type of based maps, \pg{based-maps}}
\symbolindex{$x\mapsto b$	}{alternative notation for $\lambda$-abstraction, \pg{mapsto}}
\symbolindex{$\max(x,y)$	}{maximum in some ordering, e.g.\ \pg{ordered-field} and \pg{leq-RC}}
\symbolindex{$\merid(a)$	}{meridian of $\susp A$ at $a:A$, \pg{sec:suspension}}
\symbolindex{$\min(x,y)$	}{minimum in some ordering, e.g.\ \pg{ordered-field} and \pg{leq-RC}}
\symbolindex{$A \mono B$	}{monomorphism or embedding}
%%%%%%%%%% N %%%%%%%%%%
\symbolindex{$\N$	}{type of natural numbers, \pg{sec:inductive-types}}
\symbolindex{$\north$	}{north pole of $\susp A$, \pg{sec:suspension}}
\symbolindex{$\natw$, $\zerow$, $\sucw$	}{natural numbers encoded as a $W$-type, \pg{natw}}
\symbolindex{$\nalg$	}{type of $\nat$-algebras, \pg{defn:nalg}}
\symbolindex{$\nhom(C,D)$	}{type of $\nat$-homomorphisms, \pg{defn:nhom}}
\symbolindex{$\nil$	}{empty list, \pg{lst} and \pg{lst-freemonoid}}
\symbolindex{$\NO$	}{type of surreal numbers, \pg{defn:surreals}}
\symbolindex{$\neg P$	}{logical negation (``not''), \pg{defn:logical-notation}}
\symbolindex{$\typele{n}$, $\typeleU{n}$	}{universe of $n$-types, \pg{universe-of-ntypes}}
%%%%%%%%%% O %%%%%%%%%%
\symbolindex{$\Omega(A,a)$, $\Omega A$		}{loop space of a pointed type, \pg{def:loopspace}}
\symbolindex{$\Omega^k(A,a)$, $\Omega^k A$		}{iterated loop space, \pg{def:loopspace}}
\symbolindex{$A\op$	}{opposite precategory, \pg{ct:opposite-category}}
\symbolindex{$P \lor Q$	}{logical disjunction (``or''), \pg{defn:logical-notation}}
\symbolindex{$\ord$	}{type of ordinal numbers, \pg{ord}}
%%%%%%%%%% P %%%%%%%%%%
\symbolindex{$\pairr{a,b}$	}{(dependent) pair, \pg{sec:finite-product-types} and \pg{defn:dependent-pair}}
\symbolindex{$\pairpath$	}{constructor for $=_{A \times B}$, \pg{defn:pairpath}}
\symbolindex{$\pi_n(A)$	}{$n^{\mathrm{th}}$ homotopy group of $A$, \pg{thm:homotopy-groups} and \pg{def-of-homotopy-groups}}
\symbolindex{$\power A$	}{power set, \pg{powerset}}
\symbolindex{$\powerp A$	}{merely-inhabited power set, \pg{inhabited-powerset}}
\symbolindex{$\Zpred$	}{predecessor function $\Z\to\Z$, \pg{subsec:pi1s1-encode-decode}}
\symbolindex{$A\times B$	}{cartesian product type, \pg{sec:finite-product-types}}
\symbolindex{$\prd{x:A} B(x)$	}{dependent function type, \pg{sec:pi-types}}
\symbolindex{$\proj1(t)$	}{the first projection from a pair, \pg{defn:proj} and \pg{defn:dependent-proj1}}
\symbolindex{$\proj2(t)$	}{the second projection from a pair, \pg{defn:proj} and \pg{defn:dependent-proj1}}
\symbolindex{$\prop$, $\propU$	}{universe of mere propositions, \pg{propU}}
\symbolindex{$A \times_C B$	}{pullback of $A$ and $B$ over $C$, \pg{eq:defn-pullback}}
\symbolindex{$A \sqcup^C B$	}{pushout of $A$ and $B$ under $C$, \pg{sec:colimits}}
%%%%%%%%%% Q %%%%%%%%%%
\symbolindex{$\Q$	}{type of rational numbers, \pg{sec:field-rati-numb}}
\symbolindex{$\Qp$	}{type of positive rational numbers, \pg{positive-rationals}}
\symbolindex{$\qinv(f)$	}{type of quasi-inverses to $f$, \pg{qinv}}
\symbolindex{$A/R$	}{quotient of a set by an equivalence relation, \pg{sec:set-quotients}}
\symbolindex{$A\sslash R$	}{alternative definition of quotient, \pg{def:VVquotient}}
%%%%%%%%%% R %%%%%%%%%%
\symbolindex{$\R$	}{type of real numbers (either), \pg{sec:compactness-interval}}
\symbolindex{$\RC$	}{type of Cauchy real numbers, \pg{defn:cauchy-reals}}
\symbolindex{$\RD$	}{type of Dedekind real numbers, \pg{defn:dedekind-reals}}
\symbolindex{$\rcrat(q)$	}{rational number regarded as a Cauchy real, \pg{defn:cauchy-reals}}
\symbolindex{$\rcoh{f}{g}{\epsilon}$	}{type of right adjoint coherence data, \pg{defn:lcoh-rcoh}}
\symbolindex{$\rec{\emptyt}$	}{recursor for ${\emptyt}$, \pg{defn:recursor-emptyt}}
\symbolindex{$\rec{\unit}$	}{recursor for ${\unit}$, \pg{defn:recursor-unit}}
\symbolindex{$\rec{\bool}$	}{recursor for ${\bool}$, \pg{defn:recursor-bool}}
\symbolindex{$\rec{\nat}$	}{recursor for ${\nat}$, \pg{defn:recursor-nat}}
\symbolindex{$\rec{A \times B}$	}{recursor for ${A \times B}$, \pg{defn:recursor-times}}
\symbolindex{$\rec{\sm{x:A} B(x)}$	}{recursor for ${\sm{x:A} B}$, \pg{defn:recursor-sm}}
\symbolindex{$\rec{A + B}$	}{recursor for ${A + B}$, \pg{defn:recursor-plus}}
\symbolindex{$\rec{\wtype{x:A} B(x)}$	}{recursor for ${\wtype{x:A} B}$, \pg{defn:recursor-wtype}}
\symbolindex{$\rinv$	}{type of right inverses to $f$, \pg{defn:linv-rinv}}
%%%%%%%%%% S %%%%%%%%%%
\symbolindex{$\south$	}{south pole of $\susp A$, \pg{sec:suspension}}
\symbolindex{$\Sn^n$	}{$n$-dimensional sphere, \pg{sec:circle}}
\symbolindex{$\seg$	}{path constructor of the interval $\interval$, \pg{sec:interval}}
\symbolindex{$\set$, $\setU$	}{universe of sets, \pg{setU}}
\symbolindex{$\uset$	}{category of sets, \pg{ct:precatset}}
\symbolindex{$\vset(A,f)$	}{constructor of the cumulative hierarchy, \pg{defn:V}}
\symbolindex{$x\sim_\epsilon y$	}{relation of $\epsilon$-closeness for $\RC$, \pg{defn:cauchy-reals}}
\symbolindex{$x\approx_\epsilon y$	}{recursive version of $\sim_\epsilon$, \pg{defn:RC-approx}}
\symbolindex{$\bsim_\epsilon$ or $\bbsim_\epsilon$	}{closeness relations on codomain of $\RC$-recursion, \pg{RC-recursion}}
\symbolindex{$A\wedge B$	}{smash product of $A$ and $B$, \pg{smash}}
\symbolindex{$\setof{x : A | P(x)}$	}{subset type, \pg{defn:setof}}
\symbolindex{$\setof{ f(x) | P(x)}$	}{image of a subset, \pg{subset-image}}
\symbolindex{$B \subseteq C$	}{containment of subset types, \pg{subset}}
\symbolindex{$(q,r)\subseteq (s,t)$	}{inclusion of intervals, \pg{interval-subset}}
\symbolindex{$\suc$	}{successor function $\N\to\N$, \pg{sec:inductive-types}}
\symbolindex{$\Zsuc$	}{successor function $\Z\to\Z$, \pg{sec:pi1s1-initial-thoughts}}
\symbolindex{$A+B$	}{coproduct type, \pg{sec:coproduct-types}}
\symbolindex{$\sm{x:A} B(x)$	}{dependent pair type, \pg{sec:sigma-types}}
\symbolindex{$\supp(a, f)$	}{constructor for $W$-type, \pg{defn:supp}}
\symbolindex{$\surf$	}{2-path constructor of $\Sn^2$, \pg{s2a} and \pg{s2b}}
\symbolindex{$\susp A$	}{suspension of $A$, \pg{sec:suspension}}
%%%%%%%%%% T %%%%%%%%%%
\symbolindex{$\total{f}$	}{induced map on total spaces, \pg{defn:total-map}}
\symbolindex{$\trans{p}{u}$	}{transport of $u:P(x)$ along $p:x=y$, \pg{lem:transport}}
\symbolindex{$\transfib{P}{p}{u}$	}{transport of $u:P(x)$ along $p:x=y$, \pg{lem:transport}}
\symbolindex{$\transtwo{X}{Y}$	}{two-dimensional transport, \pg{thm:transport2}}
\symbolindex{$\transconst{X}{Y}{Z}$	}{transporting in a constant family, \pg{thm:trans-trivial}}
\symbolindex{$\trunc{n}{A}$	}{$n$-truncation of $A$, \pg{sec:truncations}}
\symbolindex{$\tproj[A]{n}{a}$, $\tproj{n}{a}$	}{image of $a:A$ in $\trunc n A$, \pg{sec:truncations}}
\symbolindex{$\brck{A}$	}{propositional truncation of $A$, \pg{subsec:prop-trunc} and \pg{sec:hittruncations}}
\symbolindex{$\bproj{a}$	}{image of $a:A$ in $\brck A$, \pg{subsec:prop-trunc} and \pg{sec:hittruncations}}
\symbolindex{$\top$	}{logical truth, \pg{defn:logical-notation}}
%%%%%%%%%% U %%%%%%%%%%
\symbolindex{$\nameless$	}{an unnamed object or variable}
\symbolindex{$A \cup B$	}{union of subsets, \pg{union}}
\symbolindex{$\uniq{A\times B}$ }{uniqueness principle for the product $A\times B$, \pg{uniquenessproduct}}
\symbolindex{$\uniq{\unit}$     }{uniqueness principle for $\unit$, \pg{uniquenessunit}}
\symbolindex{$\UU$	}{universe type, \pg{sec:universes}}
\symbolindex{$\modaltype$	}{universe of modal types, \pg{eq:modaltype}}
\symbolindex{$\pointed\type$	}{universe of pointed types, \pg{def:pointedtype}}
\symbolindex{$\ua$	}{inverse to $\idtoeqv$ from univalence, \pg{ua}}
%%%%%%%%%% V %%%%%%%%%%
\symbolindex{$V$	}{cumulative hierarchy, \pg{defn:V}}
%%%%%%%%%% W %%%%%%%%%%
\symbolindex{$\walg(A,B)$	}{type of $w$-algebras, \pg{walg}}
\symbolindex{$\whom_{A,B}(C,D)$	}{type of $\w$-homomorphisms, \pg{whom}}
\symbolindex{$\wtype{x:A} B(x)$	}{$W$-type (inductive type), \pg{sec:w-types}}
\symbolindex{$A\vee B$	}{wedge of $A$ and $B$, \pg{wedge}}
%%%%%%%%%% X %%%%%%%%%%
%%%%%%%%%% Y %%%%%%%%%%
\symbolindex{$\y$	}{Yoneda embedding, \pg{ct:yoneda}}
%%%%%%%%%% Z %%%%%%%%%%
\symbolindex{$\Z$	}{type of integers, \pg{defn-Z}}}

%%% Local Variables: 
%%% mode: latex
%%% TeX-master: "hott-online"
%%% End: 

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE HoTT/verification/VERIFICATION_REPORT.md | SHA256 d77dbf4cc399f4a9b720bb653fb16728355327432034041c220f5f6148570414 | LINES 1-521/521 =====
# HoTT–Z 验证与可复现性报告

状态：`CURRENT RECEIPT`
验证日期：2026-08-31；补充验证：2026-09-01
验证主机：macOS arm64；另用 Docker `linux/amd64` 对齐上游 Agda CI 二进制

## 1. 交接包静态完整性

| 检查 | 结果 | 边界 |
|---|---|---|
| `sha256sum -c metadata/SHA256SUMS` | 1,081/1,081 条通过 | 证明文件字节匹配清单，不证明内容正确 |
| `metadata/WORKSPACE_SNAPSHOT_PARITY.json` | 763 文件、14,694,045 bytes，source/snapshot exact match | 证明声明的快照 parity，不证明工作包验收 |
| WBS 注册表 | 45 个唯一 WP、依赖均存在、DAG | 只证明结构有效 |
| `latest_completion`/canonical/快照交叉阅读 | 已读根 00–06、AGENTS、索引、ledgers、WBS、理论、形式化、论文、review、文献与状态 | 审计结论见根报告 |

## 2. 交接包原有可执行检查的复核

在交接包副本上运行，避免污染其只读证据快照：

| 检查 | 当前复核结果 |
|---|---|
| 模型检查 | 30/30 通过 |
| Python 独立 kernel | 22/22 通过 |
| Node 交叉检查 | 7/7 通过 |
| Python/Node 比较 | 通过 |
| Lean `latest_completion/formal/secondary/TwoEvent.lean` | Lean 4.33.1，exit 0 |
| 活动主张 lint | **失败**：22 文件中 1 个误报 |

lint 的当前失败为：

```text
rule=internal_inconsistency_claim
file=papers/README.md
line=10
text=None of the manuscripts claims `HoTT ⊢ ⊥`.
exit=1
```

规则允许上下文含 `not/不是/不证明/does not`，却遗漏了 `None`。交接包保存的旧收据显示
`files_checked=17, passed=true`，当前脚本扫描 22 个文件并失败，因此旧收据是在最终快照增添文件前
产生的陈旧证据。它是 false positive，不表示论文真的宣称不一致；但它足以证明“最终回归全绿”
不成立。

此外，补充文档要求运行 `bash verification/run_all.sh`，而 1,081 文件中不存在该路径；发布包没有
单一真实入口。

## 3. 上游 no-section 定理核验

锁定对象：

- `UniMath/agda-unimath` commit `88cfce0ce195ae3b64a9e73e8ec744ae64b4006b`；
- GitHub/codeload 归档 SHA-256：
  `50ed8718a56820049eebf5ad86b619774ec0c23a9c5b3ca4a4447b3e70a785a6`；
- `src/univalent-combinatorics/2-element-types.lagda.md` SHA-256：
  `72f9ad29b6c24b84e1e06f10f701895783e7a56cfaedc1dc0d295dba3629c82e`；
- `agda-unimath.agda-lib` SHA-256：
  `d42bd31babacf7fced8aab84f499d9004a1cac5c3219dc7b360c56c23e9b6221`。

锁定源中确有：

```agda
no-section-type-2-Element-Type :
  {l : Level} → ¬ ((X : 2-Element-Type l) → type-2-Element-Type X)
```

这证明“二元素类型的规范族没有全局 section”。本地用 Agda 2.8.0 将本项目
`NoCanonicalPoint.agda` 放在上游项目配置下 type-check，exit 0；不是只查看网页或相信交接说明。

## 4. 发现并定位原 Agda 构建缺陷

交接包 `latest_completion/formal/build_agda_unimath.sh` 把下面这组库 flags 作为全局 CLI 参数传给
每一次 Agda 调用：

```text
--without-K --exact-split --no-import-sorts --auto-inline
--no-require-unique-meta-solutions -WnoWithoutKFlagPrimEraseEquality
--no-postfix-projections
```

用官方 Agda 2.8.0 macOS arm64 包运行，12/12 个目标均在 Agda 自带
`Agda.Primitive.Cubical.agda:50` 失败：`Set` 不在作用域，exit 42。为了排除平台差异，又使用上游 CI
同一 Linux 2.8.0 包（SHA-256
`824081b8dcbe431289a50ac6bd83e451f390c51c3884ac7a8c4a5c0df2632faf`）在 Docker
`linux/amd64` 中运行，结果相同。

原因不是 no-section 定理失败，而是调用层级错误：`--no-import-sorts` 作为全局 CLI option 也作用到
Agda 原语模块；上游自己的 CI 是进入 repo 后执行 `make check`，让 `.agda-lib` 的 flags 作为项目
配置应用。交接包的 9 个自包含 specs 还直接依赖隐式 `Set`，因此也不应使用该全局 option 集。

纠正调用方式后：

- 3 个原 `agda-unimath` wrappers 在锁定项目配置下全部 exit 0；
- 9 个自包含 specs 在默认 Agda 2.8.0 下全部 exit 0；
- 本项目收敛后的 `ZCore.agda` 与 `NoCanonicalPoint.agda` 在 macOS 官方 Agda 2.8.0 下 exit 0；
- 本项目 `TwoEvent.lean` 在 Lean 4.33.1 下 exit 0。

所以精确裁决是：**证明源可通过；交接包宣称的统一构建脚本不可通过。**

## 5. 当前项目可复现命令

```bash
AGDA=/path/to/agda-2.8.0 \
AGDA_UNIMATH_ROOT=/path/to/agda-unimath-88cfce0ce195ae3b64a9e73e8ec744ae64b4006b \
LEAN=/path/to/lean \
bash HoTT/formal/build.sh
```

2026-08-31 本机收据：

```text
Agda version 2.8.0-3d04bac
Checking ZCore ...
Checking hott-z.NoCanonicalPoint ...
Lean version 4.33.1 ...
exit=0
```

同一 `build.sh` 又在 Docker `debian:bookworm-slim --platform linux/amd64` 中使用上游官方 Linux
Agda 2.8.0 二进制重放，两个 Agda 模块 exit 0；容器未安装 Lean，因此正确报告 NOTICE 而不把
第二实现伪装成已运行。

`build.sh` 先核对两个关键上游文件的 SHA-256；不匹配时 exit 65，缺 Agda 或锁定库时 exit 77。
生成的 `.agdai` 是可重建缓存，已由 `.gitignore` 排除并在验收后移除，不属于证据源。

## 6. 机器证明的精确含义

| 文件/定理 | 机器证明到的内容 | 没有证明的内容 |
|---|---|---|
| `ZCore.fiber-truth-invariant` | exact decoder 存在时目标在表示纤维上常值 | 一般充分性、HoTT 不一致 |
| `ZCore.no-free-enrichment` | 被合并且目标不同的两世界必须被 enrichment 区分 | 富化非法、某种富化唯一 |
| provenance/direction 例 | 特定 Unit reduct 无法恢复二值标签 | 任意快照、任意范畴、任意时间理论 |
| fixed-point-free monodromy | 给定无固定点 transport 后不存在 section | 任意 HoTT 族自动满足前提 |
| upstream no-section | 无统一函数为每个无标签二元素类型选一个元素 | 已给顺序的二点集无最小元、完整时间序不可能 |
| Lean 二事件 | swap 无固定点；Unit reduct 无方向 decoder | 第二套 univalence/no-section 实现 |

## 7. 验证等级

- `V4-L`：本项目 Agda 两个模块和 Lean 有限模型已在当前主机实际编译。
- `V4-U`：锁定上游 no-section 定理来自正式库并在该版本项目配置下本地重放。
- `V3`：Python/Node 有限模型和交叉检查通过，只覆盖枚举实例。
- `V2`：纸面/文档证明仍需逐个检查假设与量词。
- `EXTERNAL_OPEN`：没有独立专家报告、外部干净环境收据或同行评审决定。

本报告不把低等级证据自动提升为高等级，也不把本机一次成功等同于长期 CI。

## 8. 2026-09-01 现实相对悖论交接静态验证

本轮验证的是用户原文保存、current owner、启动路由和认知检查资产，不验证同函数异时数学候选
已经机器化，也不替代真正 Fresh Session。

| 检查 | 结果 | 边界 |
|---|---|---|
| Better Best 临时 attachment 与项目原文 `cmp` | exit 0，字节完全一致 | 证明复制保真，不证明原文数学结论 |
| Better Best SHA-256 | `2b60b6f3bf63750f89b16e111a2b3c0e358f688e210cd4e219bb2fd20ac4ee37` | 与 `SOURCE_REGISTRY.md` 一致 |
| 本轮用户原文包 SHA-256 | `48ab13acd61ea67630a87a3b440328dcac14a3121ea4a02309ceaaf675044e48` | 含编辑性标题/元数据，正文为逐字用户消息 |
| 来源 registry bytes/lines/hash 对照 | 2/2 通过 | 只覆盖新增用户来源 |
| 新交接认知路径存在性 | 7/7 通过 | 文件存在不等于未来 AI 已理解 |
| 23 个受影响 Markdown 的本地链接 | 12 条，missing=0 | 外部网页可用性未在此静态检查 |
| Claim matrix ID | 30 行，C-01–C-30 连续且唯一 | 不证明每条数学主张正确；状态仍由证据边界限定 |
| 启动路由关键断言 | 6 文件、21 项、0 failure | 机械检查目标/原文/候选/禁区是否进入 owner |
| 旧 P0/current-lane 搜索 | 当前 owner/AGENTS/MEMORY 未把 no-canonical-earlier-event 作为 P0 | 历史对话/审计仍保留旧事实，不删除谱系 |
| `validate_governance_repo.sh` | PASS，layout complete | 证明治理骨架/路由结构，不证明理解质量 |
| `git diff --check` 与治理尾随空白扫描 | exit 0 | 当前大量文件仍 untracked/未版本闭合 |

`FRESH_SESSION_COGNITION_CHECK.md` 已建立，但尚未在全新 Session 实际运行。因此：

```text
HOTT-006 = IMPLEMENTED_PENDING_FRESH_SESSION_VERIFICATION
```

不得把本节静态 PASS 写成冷启动理解 PASS。当前工作树也尚未形成可恢复业务 commit，不能声称
跨 worktree/机器版本闭合。

## 9. 2026-09-01 aistudio HoTT 逐字讨论语料验证（历史运行）

验证对象：`hott-discussion-corpus/v1`；manager `HoTT/tools/hott_discussion_corpus.py` 1.1.0；源根为
`aistudio-docs/` 与 `HoTT/sources/aistudio-docs/`。本验证检查原文保存和可回源性，不审定片段中的
数学主张。

本节运行时 `CURRENT`：`178d020916e8ca44cf4a`；它已由 §10 的完整来源 reconciliation generation
替代。初始 `f969fab10e494de3c7ee` 曾对非问答源使用章节/窗口；
人工审查发现任意窗口仍可能截断连续论述，因此升级到 1.1.0 并保留 19 份非问答候选全文。旧
generation 未删除，但不再是当前证据入口。

### 9.1 构建与结构统计

```text
source_files=2087
source_bytes=1385090071
candidate_source_files=441
excerpt_count=2006
captured_source_lines=1142278
captured_verbatim_bytes=132079472
captured_candidate_byte_ratio=0.185118
full_migrated_source_excerpt_count=16
full_non_qa_source_excerpt_count=19
duplicate_content_groups=0
```

| 源结构 | 全部源 | 候选源 | excerpt |
|---|---:|---:|---:|
| `qa_dialogue` | 1,190 | 422 | 1,987 |
| `prompt_response` | 0 | 0 | 0 |
| `headed_prose` | 188 | 4 | 4 |
| `unheaded_prose` | 709 | 15 | 15 |
| **非问答合计** | **897** | **19** | **19** |

`prompt_response=0` 是本次源快照的观测结果，不表示 manager 只支持问答；实现仍有独立 Prompt
边界分支。非问答候选人工文件名复核为 19/19，包括 LIG 系列论文稿、日期文档、AIX+Z 长文、
`同构悖论_1.md`、`main_3.md`、`Notes_8.md` 和 `谷歌提示词.md` 等；这 19 份共 1,149,229 bytes、
16,506 行，全部一文件一全文保存。

### 9.2 独立 validator

快速验证：

```bash
python3 HoTT/tools/hott_discussion_corpus.py validate --fast
```

```text
status=PASS
generation_id=178d020916e8ca44cf4a
inventory_rows=2087
manifest_rows=2006
fast=true
```

随后从磁盘重新枚举、读取并哈希全部 1.385 GB 源，而不是复用 build 的内存对象：

```bash
python3 HoTT/tools/hott_discussion_corpus.py validate
```

```text
status=PASS
generation_id=178d020916e8ca44cf4a
inventory_rows=2087
manifest_rows=2006
fast=false
```

全量 PASS 覆盖：source inventory 精确一致；源 SHA；manifest schema/排序/唯一 ID；连续且不重叠的
行区间；逐字字节长度/SHA；excerpt SHA 与 BEGIN marker 后原文字节；无缺失/孤儿 excerpt；所有
v1 anchor 命中行至少落入一个片段；全部/候选/excerpt 的结构统计以及非问答数量可复算。

补充合同检查：Python `py_compile` 通过；四个人工最小 fixture 分别走通 `qa_turn`、`prompt_turn`、
`heading_section`、`context_window` 和 `full_non_qa_source`；使用 jsonschema 4.26.0 Draft 2020-12
对 2,006 条 manifest row 逐条验证，全部 PASS。这里 `prompt_turn` 的通过是实现分支测试；当前
真实源快照没有这种结构。另对 manifest 机械断言：19/19 非问答条目均满足 `line_start=1`、
`line_end=source_lines`、`verbatim_bytes=source_bytes` 和全文字节相等。

### 9.3 非问答人工回源抽样

| ID | 源与行区间 | 结构/模式 | bytes | 逐字 SHA-256 | 源切片一致 |
|---|---|---|---:|---|---|
| `HOTT-DISC-F3280A0885A6878B` | `aistudio-docs/2025-09-12.md:1-314` | `headed_prose / full_non_qa_source` | 13,513 | `9c0b52ad5d97b5a48dc492155f534b5529fa407cf1964897f5d36e0368bacc95` | 全文 true |
| `HOTT-DISC-05DA6B3D01F18AA2` | `aistudio-docs/LIG-9.md:1-344` | `unheaded_prose / full_non_qa_source` | 39,986 | `832e7f78a459693f9dc0e7e74f2c797156726ada9005292e98af146d1194a359` | 全文 true |
| `HOTT-DISC-59121560694E40CA` | `aistudio-docs/Notes_8.md:1-550` | `unheaded_prose / full_non_qa_source` | 22,417 | `ab0b0676eb9242b1ab84aac10e3416ab9c3f305d6460f90c9b1a6dd2b6ca471e` | 全文 true |

### 9.4 结论边界

验证支持“当前锚点命中的讨论已按记录结构逐字保存且可回源”，并直接证明实现没有把全部文档
误作问答。它不支持“所有语义上与 HoTT 有关的隐喻都已发现”，也不支持“收录主张正确、用户
采纳、原创或经外部审查”。所有 2,006 条仍为 `UNREVIEWED_RAW_CAPTURE`；未来审读只能增加
annotation/curated view，不能删除或改写 raw generation。

## 10. 2026-09-01 对照库来源补齐与 corpus 1.2 验证

覆盖 Feature：HOTT-007；来源裁定：R-009。

### 10.1 环境、对照口径与前置风险

- 对照根：`/Users/aurolafly/shuxuedashi-aistudio/ALL-Markdown`；Git HEAD
  `b025b7a6996f1673c0498c72e15b019fad571460`，工作树 dirty；2,000 余份原文未被该 Git 跟踪。
- 目标根：`/Volumes/D/ALL-Markdown`；Git HEAD `dc1e369a6a7493dd6671016c295e8f04f2231aa3`，
  当前 HoTT/治理工作仍未版本闭合。
- 对照原文平铺在根目录；目标原文分布在 `aistudio-docs/` 和已迁移 16 份的
  `HoTT/sources/aistudio-docs/`。比较使用文件 basename、Unicode NFC+casefold、bytes 和 SHA-256。
- 操作只增量复制目标不存在且内容真正缺失的文件；同名异 SHA 必须停止。对照源始终保留，故
  无破坏性源变更；本轮未删除/覆盖目标文件。

对照根现有 2,095 个普通文件；排除 `.DS_Store` 后，用户所指 2,094 的构成为：

| 类型 | 数量 |
|---|---:|
| 小写 `.md` | 2,088 |
| 大写 `.MD` | 1 |
| `.markdown` | 2 |
| CSV/TSV 归档报告 | 2 |
| `.gitignore` | 1 |

### 10.2 初始差集与复制收据

初始小写 Markdown 对比为：对照 2,088、目标 corpus inventory 2,087；精确名称差集三项、同名异
SHA 冲突 0。两项是内容已存在的 Unicode 等价别名：

| 对照精确名 | 当前精确名 | bytes | SHA-256 |
|---|---|---:|---|
| `20250920T115153Z__Unproven Geometric Gödel Paradox.md` | `20250920T115153Z__Unproven Geometric Gödel Paradox.md` | 46895 | `4daac4aee4e373f4cefe8056d54ea1ea6483bce5496ff4957d611ae44315c6ba` |
| `【✅】P≠NP的证明（100）.md` | `【✅】P≠NP的证明（100）.md` | 2889510 | `72f369073816da38f21ace9279e959b4cb3da397682e68440a45db0a5978a36a` |

唯一真正缺失并复制到目标的是：

```text
aistudio-docs/20250823T011706Z__尊湃案件法院方.md
bytes=73698
lines=757
sha256=297742a5af046439a85effeadb6124640b716e5bdff59ed28a10b521f9f4c0bc
```

复制前目标不存在；使用保留 mode/mtime 的增量复制后，源/目标 `cmp` exit 0，双方 SHA 相同。该
文件无 HoTT v1 anchor，当前 inventory 正确记录 `candidate=false`，没有生成 excerpt。

### 10.3 全文件 reconciliation

排除对照 `.DS_Store/.gitignore` 后，与目标两个归档根对账：

```text
source_data_files=2093
target_archive_union_files=2093
source_bytes=1385603988
target_bytes=1385603988
content_sha_multiset_equal=true
normalized_name_sha_multiset_equal=true
```

目标此前已经逐字拥有 `conversion-report.csv`、`md-dedup-report.tsv`、`README_1.markdown`、
`Google Stitch System Prompt Leaked (2025-05-24) - Analysis and Insights.markdown` 和 `NOTICE_1.MD`。
对照 `.gitignore` 的 8 条有效规则是当前根 `.gitignore` 16 条有效规则的子集；因此旧配置没有被
复制或覆盖，`.DS_Store` 也未迁入。

### 10.4 manager 1.2.0 与新 generation

旧 manager 只匹配小写 `*.md`，所以即使三份非标准后缀 Markdown 已在目标，它们也没有进入
source inventory。manager 1.2.0 将 discussion source universe 修正为后缀大小写不敏感的 `.md`
和 `.markdown`，明确排除 CSV/TSV 报告、仓库配置和系统缓存。

CURRENT：`743f0765775ff62344b7`。

```text
source_files=2091
source_bytes=1385175826
suffix .md (casefolded)=2089
suffix .markdown=2
qa_dialogue=1191
headed_prose=190
unheaded_prose=710
candidate_source_files=441
excerpt_count=2006
captured_verbatim_bytes=132079472
```

新增四份讨论文档均没有 HoTT v1 anchor，因此候选、锚点和 excerpt 数与上一代一致。大写 `.MD`
和两份 `.markdown` 已在 inventory；CSV/TSV 报告明确不在 inventory。

实际运行：

```text
python3 HoTT/tools/hott_discussion_corpus.py build --dry-run  -> exit 0
python3 HoTT/tools/hott_discussion_corpus.py build            -> exit 0
python3 HoTT/tools/hott_discussion_corpus.py validate --fast  -> PASS, inventory=2091, manifest=2006
python3 HoTT/tools/hott_discussion_corpus.py validate         -> PASS, inventory=2091, manifest=2006
```

补充合同核查：jsonschema 4.26.0 Draft 2020-12 对 2,006 条 manifest row 全部 PASS；manager
`SUPPORTED_MARKDOWN_SUFFIXES={.md,.markdown}` 与 2,089/2 的实际 suffix 分布一致；C-01–C-33、
R-001–R-009 连续唯一，治理布局和本地链接检查 PASS。

### 10.5 结论边界

已验证结论是：用户指定对照库中除 `.DS_Store` 外的 2,094 个逻辑项，在当前项目中已有职责正确的
对应——2,093 个归档数据文件逐字闭合，当前根 `.gitignore` 完整覆盖旧规则；其中 2,091 份 Markdown
讨论文档进入 corpus inventory。不能把 2,094、2,093 和 2,091 混写，也不能为追求表面计数相等把
报告、配置、缓存或 Unicode 字节重复别名当成新的讨论原文。

这仍不证明 HoTT 锚点语义完备、excerpt 数学正确或对照源具有 Git commit 级 provenance。当前
交付为本地已实现并验证、未版本闭合；新补原文被当前根 `.gitignore:2 /*` 判为 ignored/untracked，
所以其他 clone 尚不能从 Git 恢复它。本轮未 commit、force-add、push、删除旧 generation、修改
归档跟踪策略或修改对照库。

## 11. 2026-09-01 Russell 时间构造与用户数学哲学优先合同验证

本节验证 R-013 的本地文档化、最小状态机、来源身份、主张／Fresh 连续性和路由；不验证完整集合
formation semantics、一般 Halting Problem、HoTT 特定定理或 future AI 的实际行为。

### 11.1 来源与状态机

指定 Matrix 源当前仍为：

```text
bytes=297569
logical_lines=5683
sha256=24530b89725d4043a7a5292a403ab50d48feed5417351c348790150726ae9409
mtime=2026-09-01T11:37:19-0400
```

`matrix_book_paradox_extract.py validate`：PASS；generation `a18a4dcec701895cc959`，10 extracts、84
images、98 explicit hits、0 uncovered。源 3570–3807 与 MP-03/04 连续保存“假集合、逻辑丢失时间
轴、序列点、计算合法性先于真值、Russell 为计算问题”。

对 `rₙ₊₁=¬rₙ` 穷举两个布尔初值：

```text
start=0: 0 1 0 1 0 1 0 1
start=1: 1 0 1 0 1 0 1 0
boolean_fixed_points=0
```

该检查只证明当前一比特模型 period 2 且无布尔 fixed point；没有运行或验证完整 Russell set
constructor，也没有完成 computability reduction。

### 11.2 认知资产与机械检查

| 检查 | 结果 | 边界 |
|---|---|---|
| 用户原文七当前身份 | 7908 bytes、55 lines、SHA `93e117af…57f7` | 证明逐字保存，不证明外部技术真值 |
| R-013／HOTT-005/006／current owners | marker/route 存在 | documented/implemented locally，不是 formal theorem |
| Claim matrix ID | C-01–C-49 连续且各一次 | 状态受各行证据边界限制 |
| Fresh questions | Q1–Q16 连续；Q15 Russell、Q16 philosophy-first | checklist ready，未实际运行 |
| Closure sequence | 四份路径存在；第四份 current | 前身不删除／不覆盖 |
| stale current markers | current routes 未残留 C-01–C-42、Q1–Q14 或第三份 current 标记 | 历史闭包／历史日志仍可合法保存旧状态 |
| Matrix manager validate | PASS | 抽取与血缘，不证明主张正确 |
| governance layout/shards | PASS；indexes=0 | 结构检查，不证明理解质量 |
| trailing whitespace／`git diff --check` | 无错误输出 | 大量目标仍 untracked |

### 11.3 状态边界

```text
RUSSELL_MINIMAL_STAGE_MODEL = DOCUMENTED_AND_ENUMERATED
RUSSELL_PROOF_ASSISTANT = OPEN
GENERAL_HALTING_REDUCTION = OPEN
USER_MATH_PHILOSOPHY_FIRST_CONTRACT = DOCUMENTED
FRESH_SESSION_BEHAVIOR = NOT_YET_EXECUTED
GIT_VERSION_CLOSURE = OPEN
```

本节未改外部 Matrix 源、未启动 subagent、未 commit/push/publish，也未把用户哲学、源文件身份或
静态检查升级为独立数学／物理证明。

## 12. 2026-09-01 Z 铁律最终定性与 HoTT 认知惯性假说静态验证

本节验证 R-014、本轮第五份 Closure、current owner、Feature、claim matrix 和 Fresh 路由；不验证
项目外 Z 全称元定理、集合论历史因果、HoTT 假说、物理离散性或 future AI 实际行为。

### 12.1 核心标记与连续性

| 检查 | 结果 | 边界 |
|---|---|---|
| `Z_STRONG_PHILOSOPHICAL_LAW`／“理论抽象必然导致悖论” | current ruling/Feature/Z/core doubt/README/MEMORY/Closure 可达 | 用户项目真值，不是外部定理收据 |
| 朴素集合论时间否定 | 描述≠构造≠存在、formation time、`rₙ₊₁=¬rₙ` 均进入 current owners | 哲学定性＋最小模型，不是全部 set theory 历史证明 |
| 说谎者／Russell／Better Best 程序族 | 统一 illegal-program philosophy，runtime/Halting 分层存在 | 不证明同一 Halting reduction |
| HoTT 认知惯性／路径依赖 | 标为 `USER_CORE_HOTT_HYPOTHESIS / ACTIVE_RESEARCH / NOT ESTABLISHED` | 未冒充 theorem |
| Claim matrix | C-01–C-58 连续且各一次 | 行状态仍受证据边界限制 |
| Rulings | R-001–R-014 连续且各一次 | sequential user decisions |
| Fresh | Q1–Q18 连续；Q17 strong/technical，Q18 naive set/HoTT | checklist ready，未执行 |
| Closure sequence | 五份路径存在；第五份 current | predecessors retained |
| stale current markers | current routes 未残留 C-01–C-49、Q1–Q16 或 Russell Closure current 标记 | historical rows/logs may preserve old state |
| user source current identity | 10117 bytes、61 lines、SHA `5de32759…fb7e` | 原文七／八逐字保存 |
| Matrix manager validate | PASS；10 extracts、84 images、98 hits、0 uncovered | source integrity only |
| Russell state enumeration | two period-2 tracks；0 Boolean fixed points | one-bit model only |
| governance layout/shards | PASS；indexes=0 | structure, not comprehension |
| trailing whitespace／`git diff --check` | 无错误输出 | targets still largely untracked |

### 12.2 状态边界

```text
Z_STRONG_PHILOSOPHICAL_LAW = DOCUMENTED_CURRENT_PROJECT_PRINCIPLE
Z_TECHNICAL_NONFACTORIZATION_CORE = VERIFIED_WITH_DEFINITIONS
Z_EXTERNAL_UNIVERSAL_THEOREM = OPEN
NAIVE_SET_TEMPORAL_NEGATION = DOCUMENTED_USER_FINAL_JUDGMENT
HOTT_COGNITIVE_INERTIA_HYPOTHESIS = ACTIVE_RESEARCH_NOT_ESTABLISHED
FRESH_SESSION_Q17_Q18 = NOT_YET_EXECUTED
GIT_VERSION_CLOSURE = OPEN
```

本节未更改 Matrix 外部源、未实现 formal code、未启动 subagent、未 commit/push/publish；`PASS`
仅覆盖认知资产完整性、状态分层和机械可达性。

## 13. 2026-09-09 第五份闭包公开原文保全续完

本次继续完成 R-014 已授权的“完整保存上一回答并与用户消息有机结合”。复核发现此前第五份闭包
有完整论点整合，但缺上一公开回答的逐字全文。因此在同一文件 §17 增补两份原文附件及覆盖对应表，
并由 README/MEMORY 指向它们。没有另起第六份闭包。

### 13.1 完整性核验

| 核验对象 | 实际结果 | 证据边界 |
|---|---|---|
| 上一公开回答全文 | 619 行，6,422 字符，13,166 UTF-8 bytes | 从本任务可见公开 final 消息逐段转录，包含六个主要章节、五层说明、全部公式、表格和末尾链接 |
| 写入与回读 | 与本次提供给 apply_patch 的完整回答字符串一致 | 这是文件回读一致性；没有另行导出会话数据库作为独立逐字对照 |
| 用户消息全文 | 733 字符，2,117 UTF-8 bytes | 与已保存的用户来源“原文八”正文逐字相同 |
| 原文标记 | 两组 BEGIN/END 各唯一 | 整合正文、编辑注记与原文边界可机械区分 |
| 六节与五层说明 | 已保留完整原文并建立覆盖表 | 覆盖表用于回查，不替代原文 |
| 前四份闭包 | 四份 SHA 均与原冻结值一致 | 未覆写历史前身 |
| 用户来源文件 | SHA 仍为 `5de32759308ce5e3ea20a856bb19eff07b4b63341827bf093af3df67b8cffb7e` | 本次没有修改原文文件 |
| 当前入口 | README、MEMORY、Feature、HoTT README、Fresh 检查均指向第五份闭包 | 新增三个人工锚点可达 |
| 现有编号 | C-01–C-58、R-001–R-014、Q1–Q18 连续 | 未增加数学主张编号或提高研究完成状态 |
| 文本检查 | 代码围栏闭合；尾随空白无命中；`git diff --check` 无错误 | 对未跟踪闭包另做直接文本检查，不能只依赖 Git diff |

原文段落哈希采用 UTF-8、LF；不计 BEGIN/END 标记及其分隔换行：

```text
prior_assistant_sha256=d05afa67b169cc7bbdb6c1898ab7af58031c5966d9d0753c31dcce2bba5bae3b
user_message_sha256=8f9a9272896f1aad5dc4075f1a1739fe5a9b9b606258e1b22f5483196397e514
```

### 13.2 本次文件快照与完成范围

| 路径 | SHA-256（2026-09-09 核验） |
|---|---|
| `认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md` | `8779e99507cf737f2506323c9590e2237d6b0d680d52b449e24510b63c8a1e12` |
| `README.md` | `c84a1e7aec8a4267927141196314f931c93d75fa878d05ed68317752f17be38b` |
| `MEMORY.md` | `ff318e21bef1877a67e0136bccac16a1a578c7b0ae18abcc12433a2e6e4f6f31` |

第五闭包 §9 的旧 hash 表仍表示 2026-09-01 冻结时点；README/MEMORY 于本次更新后的 hash 由本表
记录，不把不同日期快照误报为并行冲突。

`PASS` 只覆盖公开文本保全、内容回读、覆盖对应和入口可达性。“理论抽象必然导致悖论”按用户
数学哲学完整保存；HoTT 是否存在所寻找的具体时间悖论仍须证明。原回答中的解释不因被收录而成为
数学定理。未运行新的 Agda/Lean 证明或 Fresh Session；现有暂存的 16 项来源迁移未被提交或改动。

===== END SOURCE CHUNK | EOF=true =====
