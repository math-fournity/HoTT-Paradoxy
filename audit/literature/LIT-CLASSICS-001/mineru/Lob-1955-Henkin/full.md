Solution of a Problem of Leon Henkin
Author(s): M. H. Lob
Source: The Journal of Symbolic Logic, Vol. 20, No. 2 (Jun., 1955), pp. 115-118
Published by: Association for Symbolic Logic
Stable URL: http://www.jstor.org/stable/2266895
Accessed: 28/03/2013 09:44

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# SOLUTION OF A PROBLEM OF LEON HENKIN $^{1}$

## M. H. LÖB

PROBLEM. If $\Sigma$ is any standard formal system adequate for recursive number theory, a formula (having a certain integer $q$ as its Gödel number) can be constructed which expresses the proposition that the formula with Gödel number $q$ is provable in $\Sigma$ . Is this formula provable or independent in $\Sigma$ ? [2].

One approach to this problem is discussed by Kreisel in [4]. However, he still leaves open the question whether the formula $(Ex)\mathfrak{B}(x,\mathfrak{a})$ , with Gödel-number a, is provable or not. Here $\mathfrak{B}(x,y)$ is the number-theoretic predicate which expresses the proposition that x is the number of a formal proof of the formula with Gödel-number y.

In this note we present a solution of the previous problem with respect to the system $Z_{\mu}$ [3] pp. 289–294, and, more generally, with respect to any system whose set of theorems is closed under the rules of inference of the first order predicate calculus, and satisfies the subsequent five conditions, and in which the function $\tilde{s}(k,l)$ used below is definable.

The notation and terminology is in the main that of [3] pp. 306–326, viz. if $\mathfrak{A}$ is a formula of $Z_{\mu}$ containing no free variables, whose Gödel number is $a$ , then $\tilde{\mathfrak{B}}(\{\mathfrak{A}\})$ stands for $(Ex)\mathfrak{B}(x,a)$ (read: the formula with Gödel number $a$ is provable in $Z_{\mu}$ ); if $\mathfrak{A}$ is a formula of $Z_{\mu}$ containing a free variable, $y$ say, $\tilde{\mathfrak{B}}(\{\mathfrak{A}\})$ stands for $(Ex)\mathfrak{B}(x,g(y))$ , where $g(y)$ is a recursive function such that for an arbitrary numeral $n$ the value of $g(n)$ is the Gödel number of the formula obtained from $\mathfrak{A}$ by substituting $n$ for $y$ in $\mathfrak{A}$ throughout. We shall, however, depart trivially from [3] in writing $\tilde{\mathfrak{B}}(n)$ , where $n$ is an arbitrary numeral, for $(Ex)\mathfrak{B}(x,n)$ .

In [3] (loc. cit.) the following four conditions are shown to be satisfied by the predicate $\mathfrak{B}(m,n)$ of $Z_{\mu}$ .

I. For any formulae S and T, the formula

$$
\mathfrak {B} (\{\mathfrak {S} \rightarrow \mathfrak {T} \}) \rightarrow [ \mathfrak {B} (\{\mathfrak {S} \}) \rightarrow \mathfrak {B} (\{\mathfrak {T} \}) ]
$$

is a theorem.

II. If the formula $\mathfrak{T}$ is derivable from the formula $\mathfrak{S}$ , then the formula

$$
\mathfrak {B} (\{\mathfrak {S} \}) \rightarrow \mathfrak {B} (\{\mathfrak {T} \})
$$

is a theorem.

III. If $f(x)$ is a recursive term, then the formula

$$
f (x) = 0 \rightarrow \mathfrak {B} (\{f (x) = 0 \})
$$

is a theorem.

IV. If the formula $\mathfrak{A}$ is provable, so is the formula $\mathfrak{B}(\{\mathfrak{A}\})$ .

In addition, we require the following condition.

V. For any formula $\mathfrak{A}$ , the formula

$$
\mathfrak {B} (\{\mathfrak {A} \}) \rightarrow \mathfrak {B} (\{\mathfrak {B} (\{\mathfrak {A} \}) \})
$$

is a theorem.

Proof of V. From the axiom-schema

$$
A (y) \rightarrow (E x) A (x)
$$

and II we see that

$$
\mathfrak {B} (\{A (y) \}) \rightarrow \mathfrak {B} (\{(E x) A (x) \}),
$$

and hence by the predicate calculus

$$
(E x) \widetilde {\mathfrak {B}} (\{A (x) \}) \rightarrow \widetilde {\mathfrak {B}} (\{(E x) A (x) \}),
$$

are formal theorems.

Replacing $A(x)$ by $f(x)=0$ , where $f(x)$ is a recursive term, we obtain the theorem

$$
(E x) \mathfrak {B} (\{f (x) = 0 \}) \rightarrow \mathfrak {B} (\{(E x) (f (x) = 0) \}).\tag{a}
$$

From III we prove by the predicate calculus the formula

$$
(E x) (f (x) = 0) \rightarrow (E x) \widetilde {\mathfrak {B}} (\{f (x) = 0 \}),
$$

and thence, in conjunction with (a), obtain the theorem

$$
(E x) (f (x) = 0) \rightarrow \mathfrak {B} (\{(E x) (f (x) = 0) \}).\tag{b}
$$

Since, moreover, the formula $\mathfrak{B}(\{\mathfrak{A}\})$ (i.e. $(Ex)\mathfrak{B}(x,\mathfrak{a})$ , where $\mathfrak{a}$ is the Gödel number of $\mathfrak{A}$ ) is of the form $(Ex)(f(x)=0)$ , V follows.

THEOREM. $^{2}$ If S is any formula such that $\tilde{\mathfrak{B}}(\{\mathfrak{S}\}) \to \mathfrak{S}$ is a theorem, then S is a theorem.

COROLLARY. The particular formula $\mathfrak{S}$ of Henkin's problem, which is the same as $\tilde{\mathfrak{B}}(\{\mathfrak{S}\})$ , is a theorem.

Proof. Let $\mathfrak{S}$ be a formula such that $\tilde{\mathfrak{B}}(\{\mathfrak{S}\}) \to \mathfrak{S}$ is a theorem.

(i) Let $\mathfrak{s}(k,l)$ be the function such that, if $\mathfrak{f}$ is the Gödel number of an expression $\mathfrak{R}$ , the value of $\mathfrak{s}(\mathfrak{f},\mathfrak{l})$ is the Gödel number of the expression obtained from $\mathfrak{R}$ by replacing the variable $a$ throughout by $\mathfrak{l}$ .

By means of the function $\hat{s}(k,l)$ we can construct $^{3}$ a formula $\mathfrak{T}$ which has the form

$$
\mathfrak {B} (\{\mathfrak {T} \}) \to \mathfrak {S}.
$$

For consider the formula $\mathfrak{B}(\hat{s}(a, a)) \to \mathfrak{S}$ . Let its Gödel number be $f$ . Then the formula $\mathfrak{B}(\hat{s}(f, f)) \to \mathfrak{S}$ has the Gödel number $\hat{s}(f, f)$ . So if $\mathfrak{T}$ is the formula with Gödel number $\hat{s}(f, f)$ , then $\mathfrak{T}$ has the form $\mathfrak{B}(\{\mathfrak{T}\}) \to \mathfrak{S}$ .

(ii) If $\mathfrak{T}$ is a theorem, so is $\mathfrak{S}$ . For if $\mathfrak{T}$ is a theorem, so is $\tilde{\mathfrak{B}}(\{\mathfrak{T}\})$ according to IV, and then $\mathfrak{S}$ is obtained simply by modus ponens.

(iii) The argument of (ii) may be formalized to obtain a formal proof of the formula

$$
\mathfrak {B} (\{\mathfrak {T} \}) \rightarrow \mathfrak {B} (\{\mathfrak {S} \}).
$$

For let $\mathfrak{T}$ be the formula $\mathfrak{B}(\{\mathfrak{T}\})\to\mathfrak{S}$ of (i).

Now the formula

$$
\mathfrak {B} (\{\mathfrak {B} (\{\mathfrak {T} \}) \}) \&\mathfrak {B} (\{\mathfrak {B} (\{\mathfrak {T} \}) \rightarrow \mathfrak {S} \}) \rightarrow \mathfrak {B} (\{\mathfrak {S} \})\tag{c}
$$

is easily seen to be provable by an application of I. But by (i) the second conjunctive clause in the antecedent of (c) may be written in the form $\mathfrak{B}(\{\mathfrak{T}\})$ . Hence (c) reduces to the provable formula

$$
\mathfrak {B} (\{\mathfrak {B} (\{\mathfrak {T} \}) \}) \&\mathfrak {B} (\{\mathfrak {T} \}) \rightarrow \mathfrak {B} (\{\mathfrak {S} \}).\tag{d}
$$

From (d) we obtain the provability of

$$
\mathfrak {B} (\{\mathfrak {T} \}) \rightarrow \mathfrak {B} (\{\mathfrak {S} \}) \text { by } V.\tag{e}
$$

(iv) Now we make use of our hypothesis that $\mathfrak{B}(\{\mathfrak{S}\}) \to \mathfrak{S}$ is a theorem, combining it with (e) to obtain the information that

$$
\mathfrak {B} (\{\mathfrak {T} \}) \rightarrow \mathfrak {S}
$$

is a theorem, i.e. T is a theorem by (i).

(v) Since $\mathfrak{T}$ is provable (iv), we use (ii) to conclude that $\mathfrak{S}$ is a theorem. This completes the proof.

The method used in the previous proof leads to a new derivation of paradoxes in natural language. $^{4}$ For let A be any sentence, and let B be the sentence

$$
" \text {   If   this   sentence   is   true,   then   so   is   } A."
$$

Now we easily see that, if B is true, then so is A. That is, B is true. Hence, A is true. We have thus shown that every sentence is true.

It is worth noticing, perhaps, that this paradox is derived without using the word “not”. $^{4}$ It is therefore available as a test of inconsistency of formal systems which do not contain a symbol for negation.

## BIBLIOGRAPHY

[1] K. Gödel, Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I, Monatshefte für Mathematik und Physik, vol. 38 (1931), pp. 173–198.

[2] LEON HENKIN, A problem concerning provability, problem 3, this JOURNAL, vol. 17 (1952), p. 160.

[3] D. HILBERT and P. BERNAYS, Grundlagen der Mathematik, vol. 2, Berlin (Springer) 1939, xii + 498 pp.

[4] G. KREISEL, On a problem of Henkin's, Koninklijke Nederlandse Akademie van Wetenschappen, Proceedings, series A, vol. 56 (1953), pp. 405–406.

UNIVERSITY OF LEEDS, ENGLAND