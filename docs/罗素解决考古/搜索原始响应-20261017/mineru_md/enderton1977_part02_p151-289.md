the function H must be one-to-one. But the function j is in general not one-to-one, nor is $H(j)$ . It may help to think of H as a “super function” that assigns certain lower-level functions to other lower-level functions. The super function in this proof is one-to-one, but the lower-level functions are not necessarily one-to-one.

Examples 1. $2 + 2 = 4$ . Proving this amounts to finding disjoint sets $K$ and $L$ with $K \approx 2$ and $L \approx 2$ , and then checking that $K \cup L \approx 4$ . (This is not the same as the verification of $2 + 2 = 4$ in Chapter 4, because now we are using the addition operation for cardinal numbers. But Theorem 6J assures us that the answer is unchanged.)

2. For $m$ and $n$ in $\omega, m \cdot n = \operatorname{card} m \times n$ and $m^n = \operatorname{card} ^n m$ .

3. For any natural number $n$ ,

$$
n + \aleph_ {0} = \aleph_ {0} \quad \text { and } \quad n \cdot \aleph_ {0} = \aleph_ {0}
$$

(unless $n = 0$ ). Also

$$
\aleph_ {0} + \aleph_ {0} = \aleph_ {0} \quad \text { and } \quad \aleph_ {0} \cdot \aleph_ {0} = \aleph_ {0}.
$$

The last equation follows from an earlier example showing that $\omega \times \omega \approx \omega$ . To prove that $2 + \aleph_0 = \aleph_0$ , it suffices to show that $\{a, b\} \cup \omega \approx \omega$ (where $a$ and $b$ are not in $\omega$ ). The function

$$
f (a) = 0, \quad f (b) = 1, \quad f (n) = n ^ {+ +}
$$

establishes this. The other equations are left for you to check. Observe that cancellation laws fail for infinite cardinals, e.g., $2 + \aleph_0 = 3 + \aleph_0$ , but $2 \neq 3$ .

4. For any cardinal number $\kappa$ ,

$$
\kappa + 0 = \kappa , \quad \kappa \cdot 0 = 0, \quad \kappa \cdot 1 = \kappa .
$$

5. Recall that $\varnothing K = \{\varnothing\}$ for any set $K$ and that $^K\varnothing = \varnothing$ for nonempty $K$ . In terms of cardinal numbers, these facts become

$$
\begin{array}{l l} \kappa^ {0} = 1 & \text { for   any   } \kappa , \\ 0 ^ {\kappa} = 0 & \text { for   any   nonzero   } \kappa . \end{array}
$$

In particular, $0^0 = 1$ .

6. For any set A, the cardinality of its power set is $2^{card A}$ . This is because by the definition of exponentiation,

$$
2 ^ {\operatorname{card} A} = \operatorname{card} (^ {A} 2).
$$

And we have shown that $^{A}2 \approx P A$ , and hence

$$
2 ^ {\operatorname{card} A} = \operatorname{card} (^ {A} 2) = \operatorname{card} \mathscr {P} A.
$$

In particular, card $P\omega = 2^{N_{0}}$ . (The term “power set” is rooted in the fact that card PA equals 2 raised to the power card A.)

7. By Cantor's theorem and the preceding example, $\kappa \neq 2^{\kappa}$ for any $\kappa$ . In particular $\aleph_0 \neq 2^{\aleph_0}$ .

8. For any cardinal $\kappa$ ,

$$
\kappa + \kappa = 2 \cdot \kappa .
$$

You are invited to explain how this fact is obtained.

The following theorem lists some of the elementary facts of cardinal arithmetic. (Parts of the theorem will later be seen to be rather trivial.)

Theorem 6I For any cardinal numbers $\kappa, \lambda$ , and $\mu$ :

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1.  $\kappa + \lambda = \lambda + \kappa$  and  $\kappa \cdot \lambda = \lambda \cdot \kappa.$ 
2.  $\kappa + (\lambda + \mu) = (\kappa + \lambda) + \mu$  and  $\kappa \cdot (\lambda \cdot \mu) = (\kappa \cdot \lambda) \cdot \mu.$ 
3.  $\kappa \cdot (\lambda + \mu) = \kappa \cdot \lambda + \kappa \cdot \mu.$ 
4.  $\kappa^{\lambda+\mu} = \kappa^{\lambda} \cdot \kappa^{\mu}.$ 
5.  $(\kappa \cdot \lambda)^{\mu} = \kappa^{\mu} \cdot \lambda^{\mu}.$ 
6.  $(\kappa^{\lambda})^{\mu} = \kappa^{\lambda \cdot \mu}.$
</div>

Proof Take sets K, L, and M with card $K = \kappa$ , card $L = \lambda$ , and card $M = \mu$ ; for convenience choose them in such a way that any two are disjoint. Then each of the equations reduces to a corresponding statement about equinumerous sets. For example, $\kappa \cdot \lambda = card K \times L$ and $\lambda \cdot \kappa = card(L \times K)$ ; consequently showing that $\kappa \cdot \lambda = \lambda \cdot \kappa$ reduces to showing that $K \times L \approx L \times K$ . Listed in full, the statements to be verified are:

1. $K \cup L \approx L \cup K$ and $K \times L \approx L \times K$ .

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
2. $K \cup (L \cup M) \approx (K \cup L) \cup M$ and $K \times (L \times M) \approx (K \times L) \times M$.
3. $K \times (L \cup M) \approx (K \times L) \cup (K \times M)$.
4. $(^L \cup^M)K \approx {}^L K \times {}^M K$.
5. $^M(K \times L) \approx {}^M K \times {}^M L$.
6. $^M(^L K) \approx {}^{(L \times M)} K$.
</div>

Most of the verifications are left as exercises.

In the case of item 6 we want a one-to-one function $H$ from $^{M}(^{L}K)$ onto $(^{L\times M})K$ . For $f\in^{M}(^{L}K)$ , let $H(f)$ be the function whose value at $\langle l,m\rangle$ equals the value of the function $f(m)$ at $l$ .

To see that H is one-to-one, observe that if $f \neq g$ (both belonging to $M(LK)$ ), then for some m, the functions $f(m)$ and $g(m)$ differ. This in turn implies that for some $l, f(m)(l) \neq g(m)(l)$ . Hence

$$
H (f) (l, m) = f (m) (l) \neq g (m) (l) = H (g) (l, m)
$$

so that $H(f) \neq H(g)$ .

Finally, to see that ran $H$ is all of $^{(L \times M)}K$ , consider any function $j \in (^{L \times M})K$ . Then $j = H(f)$ , where (for $m \in M$ ) $f(m)$ is the function whose value at $l \in L$ is $j(l, m)$ .

The next theorem reassures us that for finite cardinals (i.e., for natural numbers), the present arithmetic operations agree with those of Chapter 4. In Chapter 4, exponentiation was defined only in passing; for completeness we include it here.

Theorem 6J Let m and n be finite cardinals. Then

$$
\begin{array}{c} m + n = m + _ {\omega} n, \\ m \cdot n = m \cdot_ {\omega} n, \\ m ^ {n} = m ^ {n}, \end{array}
$$

where on the right side we use the operations of Chapter 4 (defined by recursion) and on the left side we use the operations of cardinal arithmetic.

Proof We use induction on n. First we claim that for any cardinal numbers $\kappa$ and $\lambda$ the following identities are correct.

(a1) $\kappa + 0 = \kappa$ .

(a2) $\kappa + (\lambda + 1) = (\kappa + \lambda) + 1$ .

(m1) $\kappa \cdot 0 = 0.$

(m2) $\kappa \cdot (\lambda + 1) = \kappa \cdot \lambda + \kappa$ .

(e1) $\kappa^0 = 1$ .

(e2) $\kappa^{\lambda + 1} = \kappa^{\kappa} \cdot \kappa.$

In each case, the equation is either trivial or is an immediate consequence of Theorem 6I (or both).

The second piece of information we need is that for a finite cardinal n,

$$
n + 1 = n ^ {+}
$$

(with cardinal addition). This holds because $n$ and $\{n\}$ are disjoint sets of cardinality $n$ and 1, respectively, and hence

$$
n + 1 = \operatorname{card} (n \cup \{n \}) = \operatorname{card} n ^ {+} = n ^ {+}.
$$

It remains only to go through the motions of the induction. Consider any $m \in \omega$ and let

$$
T = \{n \in \omega | m + n = m + _ {\omega} n \}.
$$

Then $0 \in A$ since $n + 0 = n = n + _{\omega} 0$ , by (a1) and (A1), where (A1) is given in Theorem 4I. Suppose that $k \in T$ . Then

$$
\begin{array}{r l} m + k ^ {+} & = m + (k + 1) \\ & = (m + k) + 1 \quad \text { by   (a2) } \\ & = (m + _ {\omega} k) + 1 \quad \text { since } \quad k \in T \\ & = (m + _ {\omega} k) ^ {+} \\ & = m + _ {\omega} k ^ {+} \quad \text { by   (A2). } \end{array}
$$

Hence $k^{+} \in T$ , $T$ is inductive, and $T = \omega$ .

For multiplication and exponentiation the argument is identical.

Corollary 6K If A and B are finite, then $A \cup B$ , $A \times B$ , and $^{B}A$ are also finite.

Proof Let $m = \operatorname{card} A$ and $n = \operatorname{card} B$ . Then we calculate: $\operatorname{card}(A \times B) = \operatorname{card} A \cdot \operatorname{card} B = m \cdot n = m \cdot_{\omega} n \in \omega$ . A similar argument applies to $^B A$ and $m^n$ .

For union we must use disjoint sets:

$$
A \cup B = A \cup (B - A).
$$

$B - A$ is a subset of a finite set and hence (by Corollary 6G) is finite. Let $k = \operatorname{card}(B - A)$ . Then $\operatorname{card}(A \cup B) = m + k = m + _{\omega} k \in \omega$ .

The above corollary can also be proved without using arithmetic (Exercises 8 and 9).

## Exercises

10. Prove part 4 of Theorem 6I.

11. Prove part 5 of Theorem 6I.

12. The proof to Theorem 6I involves eight instances of showing two sets to be equinumerous. (The eight are listed in the proof of the theorem as statements numbered 1–6.) In which of these eight cases does equality actually hold?

13. Show that a finite union of finite sets is finite. That is, show that if $B$ is a finite set whose members are themselves finite sets, then $\bigcup B$ is finite.

14. Define a permutation of K to be any one-to-one function from K onto K. We can then define the factorial operation on cardinal numbers by the equation

$$
\kappa ! = \operatorname{card} \{f | f \text {   is   a   permutation   of   } K \},
$$

where K is any set of cardinality $\kappa$ . Show that $\kappa!$ is well defined, i.e., the value of $\kappa!$ is independent of just which set K is chosen.

## ORDERING CARDINAL NUMBERS

We can use the concept of equinumerosity to tell us when two sets A and B are of the same size. But when should we say that B is larger than A?

Definition A set $A$ is dominated by a set $B$ (written $A \preccurlyeq B$ ) iff there is a one-to-one function from $A$ into $B$ .

For example, any set dominates itself. If $A \subseteq B$ , then A is dominated by B, since the identity function on A maps A one-to-one into B. More generally we have: $A \preccurlyeq B$ iff A is equinumerous to some subset of B. This is just a restatement of the definition, since f is a function from A into B iff it is a function from A onto a subset of B (see Fig. 38).

![](images/4880a404363c1077b105db68e3c5d30369421e10afc08170c03e9a6b35eb0477.jpg)  
Fig. 38. F shows that $A \preccurlyeq B$ .

We define the ordering of cardinal numbers by utilizing the concept of dominance:

$$
\operatorname{card} A \leq \operatorname{card} B \quad \text { iff } \quad A \preccurlyeq B.
$$

As with the operations of cardinal arithmetic, it is necessary to check that the ordering relation is well defined. For suppose we start with two cardinal numbers, say $\kappa$ and $\lambda$ . In order to determine whether or not $\kappa \leq \lambda$ , our definition demands that we employ selected representatives K and L for which $\kappa = card K$ and $\lambda = card L$ . Then

$$
\kappa \leq \lambda \quad \text { iff } \quad K \preccurlyeq L.
$$

But the truth or falsity of “ $\kappa \leq \lambda$ ” must be independent of which selected representatives are chosen. Suppose also that $\kappa = card K'$ and $\lambda = card L'$ . To avoid embarrassment, we must be certain that

$$
K \preccurlyeq L \quad \text {   iff   } \quad K ^ {\prime} \preccurlyeq L.
$$

To prove this, note first that $K \approx K'$ and $L \approx L'$ (because card $K = \text{card } K'$ and card $L = \text{card } L'$ ). If $K \preccurlyeq L$ , then we have one-to-one maps (i) from $K'$ onto $K$ , (ii) from $K$ into $L$ , and (iii) from $L$ onto $L'$ . By composing the three functions, we can map $K'$ one-to-one into $L'$ , and hence $K' \preccurlyeq L'$ .

We further define

$$
\kappa <   \lambda \quad \text { iff } \quad \kappa \leq \lambda \quad \text { and } \quad \kappa \neq \lambda .
$$

Thus in terms of sets we have

$$
\operatorname{card} K <   \operatorname{card} L \quad \text { iff } \quad K \preccurlyeq L \quad \text { and } \quad K \not \cong L.
$$

Notice that this condition is stronger than just saying that K is equinumerous to a proper subset of L. After all, $\omega$ is equinumerous to a proper subset of itself, but we certainly do not want to have card $\omega < card \omega$ . The definition of “<” has the expected consequence that

$$
\kappa \leq \lambda \quad \text { iff } \quad \text { either } \quad \kappa <   \lambda \quad \text { or } \quad \kappa = \lambda .
$$

Examples 1. If $A \subseteq B$ , then card $A \leq$ card $B$ . Conversely, whenever $\kappa \leq \lambda$ , then there exist sets $K \subseteq L$ with card $K = \kappa$ and card $L = \lambda$ . To prove this, start with any sets $C$ and $L$ of cardinality $\kappa$ and $\lambda$ , respectively. Then $C \preccurlyeq L$ , so there is a one-to-one function $f$ from $C$ into $L$ . Let $K = \operatorname{ran} f$ ; then $C \approx K \subseteq L$ .

2. For any cardinal $\kappa$ , we have $0 \leq \kappa$ .

3. For any finite cardinal $n$ , we have $n < \aleph_0$ . (Why?) For any two finite cardinals $m$ and $n$ , we have

$$
m \in n \Rightarrow m \subseteq n \Rightarrow m \leq n.
$$

Furthermore the converse implications hold. For if $m \leq n$ , then $m \preccurlyeq n$ and there is a one-to-one function $f: m \to n$ . By the pigeonhole principle, it is impossible to have $n$ less than $m$ , so by trichotomy $m \in n$ . Thus our new ordering on finite cardinals agrees with the epsilon ordering of Chapter 4.

4. $\kappa < 2^{\kappa}$ for any cardinal $\kappa$ . For if $A$ is any set of cardinality $\kappa$ , then $\mathcal{P}A$ has cardinality $2^{\kappa}$ . Then $A \preccurlyeq \mathcal{P}A$ (map $x \in A$ to $\{x\} \in \mathcal{P}A$ ), but by Cantor's theorem (Theorem 6B) $A \not\cong \mathcal{P}A$ . Hence $\kappa \leq 2^{\kappa}$ but $\kappa \neq 2^{\kappa}$ , i.e., $\kappa < 2^{\kappa}$ . In particular, there is no largest cardinal number.

The first thing to prove about the ordering we have defined for cardinals is that it actually behaves like something we would be willing to call an ordering. After all, just using the symbol “≤” does not confer any special properties, but it does indicate the expectation that special properties will be forthcoming. For a start, we ask if the following are valid for all cardinals $\kappa$ , $\lambda$ , and $\mu$ :

1. $\kappa \leq \kappa$

2. $\kappa \leq \lambda \leq \mu \Rightarrow \kappa \leq \mu .$

3. $\kappa \leq \lambda \& \lambda \leq \kappa \Rightarrow \kappa = \lambda.$

4. Either $\kappa \leq \lambda$ or $\lambda \leq \kappa$ .

The first is obvious, since $A \preccurlyeq A$ holds for any set $A$ . The second item follows at once from the fact that

$$
A \preccurlyeq B \& B \preccurlyeq C \Rightarrow A \preccurlyeq C.
$$

(We prove this by taking the composition of two functions.) The third item is nontrivial. But the assertion is correct, and is called the Schröder-Bernstein theorem. We will also prove the fourth item, but that proof will require the axiom of choice.

First we will prove the Schröder–Bernstein theorem, which will be a basic tool in calculating the cardinalities of sets. Typically when we want to calculate card S for a given set S, we try to squeeze card S between upper and lower bounds. If possible, we try to get these bounds to coincide,

$$
\kappa \leq \operatorname{card} S \leq \kappa ,
$$

whereupon the Schröder–Bernstein theorem asserts that card $S = \kappa$ . We will see examples of this technique after proving the theorem.

Schröder–Bernstein Theorem (a) If $A \preccurlyeq B$ and $B \preccurlyeq A$ , then $A \approx B$ .

(b) For cardinal numbers $\kappa$ and $\lambda$ , if $\kappa \leq \lambda$ and $\lambda \leq \kappa$ , then $\kappa = \lambda$ .

Proof It is done with mirrors (see Fig. 39). We are given one-to-one functions $f \colon A \to B$ and $g \colon B \to A$ . Define $C_n$ by recursion, using the formulas

$$
C _ {0} = A - \operatorname{ran} g \quad \text { and } \quad C _ {n ^ {+}} = g [ f [ [ C _ {n} ] ].
$$

Thus $C_0$ is the troublesome part that keeps $g$ from being a one-to-one correspondence between $B$ and $A$ . We bounce it back and forth, obtaining $C_1, C_2, \ldots$ . The function showing that $A \approx B$ is the function $h: A \to B$ defined by

$$
h (x) = \left\{ \begin{array}{l l} f (x) & \text {   if   } x \in C _ {n} \text {   for   some   } n, \\ g ^ {- 1} (x) & \text {   otherwise.   } \end{array} \right.
$$

Note that in the second case $(x \in A$ but $x \notin C_n$ for any $n$ ) it follows that $x \notin C_0$ and hence $x \in \operatorname{ran} g$ . So $g^{-1}(x)$ makes sense in this case.

![](images/4bb974dc4c2036edb84a38a137df7fe406dc83a4e0b9f320dc4c77895ebe557a.jpg)  
Fig. 39. The Schröder–Bernstein theorem.

Does it work? We must verify that $h$ is one-to-one and has range $B$ . Define $D_n = f[C_n]$ , so that $C_{n^+} = g[D_n]$ . To show that $h$ is one-to-one, consider distinct $x$ and $x'$ in $A$ . Since both $f$ and $g^{-1}$ are one-to-one, the only possible problem arises when, say, $x \in C_m$ and $x' \notin \bigcup_{n \in \omega} C_n$ . In this case,

$$
h (x) = f (x) \in D _ {m},
$$

whereas

$$
h (x ^ {\prime}) = g ^ {- 1} (x ^ {\prime}) \notin D _ {m},
$$

lest $x' \in C_{m^+}$ . So $h(x) \neq h(x')$ .

Finally we must check that ran $h$ exhausts $B$ . Certainly each $D_n \subseteq \operatorname{ran} h$ , because $D_n = h[C_n]$ . Consider then a point $y$ in $B - \bigcup_{n \in \omega} D_n$ . Where is $g(y)$ ? Certainly $g(y) \notin C_0$ . Also $g(y) \notin C_{n^+}$ , because $C_{n^+} = g[D_n]$ , $y \notin D_n$ , and $g$ is one-to-one. So $g(y) \notin C_n$ for any $n$ . Therefore $h(g(y)) = g^{-1}(g(y)) = y$ . This shows that $y \in \operatorname{ran} h$ , thereby proving part (a).

Part (b) is a restatement of part (a) in terms of cardinal numbers.

The Schröder–Bernstein theorem is sometimes called the “Cantor–Bernstein theorem.” Cantor proved the theorem in his 1897 paper, but his proof utilized a principle that is equivalent to the axiom of choice. Ernst Schröder announced the theorem in an 1896 abstract. His proof, published in 1898, was imperfect, and he published a correction in 1911. The first fully satisfactory proof was given by Felix Bernstein and was published in an 1898 book by Borel.

Examples The usefulness of the Schröder–Bernstein theorem in calculating cardinalities is indicated by the following examples.

1. If $A \subseteq B \subseteq C$ and $A \approx C$ , then all three sets are equinumerous. To prove this, let $\kappa = \text{card } A = \text{card } C$ and let $\lambda = \text{card } B$ . Then by hypothesis $\kappa \leq \lambda \leq \kappa$ , so by the Schröder-Bernstein theorem $\kappa = \lambda$ .

2. The set $\mathbb{R}$ of real numbers is equinumerous to the closed unit interval [0, 1]. For we have

$$
(0, 1) \subseteq [ 0, 1 ] \subseteq \mathbb {R},
$$

and (as noted previously) $\mathbb{R} \approx (0, 1)$ . Thus by the preceding example, all three sets are equinumerous. (For a more direct construction of a one-to-one correspondence between $\mathbb{R}$ and $[0, 1]$ , we suggest trying Exercise 4.)

3. If $\kappa \leq \lambda \leq \mu$ , then, as we observed before, $\kappa \leq \mu$ . We can now give an improved version:

$$
\begin{array}{r l} \kappa \leq \lambda <   \mu & \Rightarrow \quad \kappa <   \mu , \\ \kappa <   \lambda \leq \mu & \Rightarrow \quad \kappa <   \mu . \end{array}
$$

For by the earlier observation we obtain $\kappa \leq \mu$ ; if equality held, then (as in the first example) all three cardinal numbers would coincide.

4. $\mathbb{R} \approx {}^{\omega}2$ , and hence $\mathbb{R} \approx \mathcal{P}\omega$ . Thus the set of real numbers is equinumerous to the power set of $\omega$ . To prove this it suffices, by the Schröder–Bernstein theorem, to show that $\mathbb{R} \preccurlyeq {}^{\omega}2$ and ${}^{\omega}2 \preccurlyeq \mathbb{R}$ .

To show that $\mathbb{R} \preccurlyeq^{\omega} 2$ , we construct a one-to-one function from the open unit interval $(0,1)$ into ${}^{\omega} 2$ . The existence of such a function, together with the fact that $\mathbb{R} \approx (0,1)$ , gives us

$$
\mathbb {R} \approx (0, 1) \preccurlyeq^ {\omega} 2.
$$

The function is defined by use of binary expansions of real numbers; map the real whose binary expansion is 0.1100010... to the function in $\omega 2$ whose successive values are 1, 1, 0, 0, 0, 1, 0, .... In general, for a real number $z$ in (0, 1), let $H(z)$ be the function $H(z): \omega \to 2$ whose value at $n$ equals the $(n + 1)$ st bit (binary digit) in the binary expansion of $z$ . Clearly $H$ is one-to-one. (But $H$ does not have all of $\omega 2$ for its range. Note that 0.1000... = 0.0111... = $\frac{1}{2}$ . For definiteness, always select the nonterminating binary expansion.)

To show that $^{\omega}2 \preccurlyeq \mathbb{R}$ we use decimal expansions. The function in $^{\omega}2$ whose successive values are 1, 1, 0, 0, 0, 1, 0, ... is mapped to the real number with decimal expansion 0.1100010.... This maps $^{\omega}2$ one-to-one into the closed interval $[0, \frac{1}{9}]$ .

5. By virtue of the above example,

$$
\text { card } \mathbb {R} = 2 ^ {\aleph_ {0}}.
$$

Consequently the plane $\mathbb{R} \times \mathbb{R}$ has cardinality

$$
2 ^ {\aleph_ {0}} \cdot 2 ^ {\aleph_ {0}} = 2 ^ {\aleph_ {0} + \aleph_ {0}} = 2 ^ {\aleph_ {0}}.
$$

Thus the line R is equinumerous to the plane $R \times R$ . This will not come as a surprise if you have heard of “space-filling” curves.

The next theorem shows that the operations of cardinal arithmetic have the expected order-preserving properties.

Theorem 6L Let $\kappa, \lambda,$ and $\mu$ be cardinal numbers.

(a) $\kappa \leq \lambda \Rightarrow \kappa +\mu \leq \lambda +\mu .$

(b) $\kappa \leq \lambda \Rightarrow \kappa \cdot \mu \leq \lambda \cdot \mu.$

(c) $\kappa \leq \lambda \Rightarrow \kappa^{\mu} \leq \lambda^{\mu}$ .

(d) $\kappa \leq \lambda \Rightarrow \mu^{\kappa} \leq \mu^{\lambda}$ ; if not both $\kappa$ and $\mu$ equal zero.

Proof Let $K, L$ , and $M$ be sets of cardinality $\kappa, \lambda$ , and $\mu$ , respectively. Then $^M K$ has cardinality $\kappa^\mu$ , etc. We assume that $\kappa \leq \lambda$ ; hence we may select $K$ and $L$ such that $K \subseteq L$ . And we may select $M$ so that $L_{\cap}M = \emptyset$ .

Parts (a), (b), and (c) are now immediate, since

$$
K \cup M \subseteq L \cup M, \quad K \times M \subseteq L \times M, \quad {} ^ {M} K \subseteq {} ^ {M} L.
$$

For part (d), first consider the case in which $\mu = 0$ . Then $\kappa \neq 0$ and $\mu^{\kappa} = 0 \leq \mu^{\lambda}$ . There remains the case in which $\mu \neq 0$ , i.e., $M \neq \emptyset$ . Take some fixed $a \in M$ . We need a one-to-one function $G$ from $^{K}M$ into $^{L}M$ . For any $f \in ^{K}M$ , define $G(f)$ to be the function with domain $L$ for which

$$
G (f) (x) = \left\{ \begin{array}{l l} f (x) & \text { if } \quad x \in K, \\ a & \text { if } \quad x \in L - K. \end{array} \right.
$$

In one line, $G(f) = f \cup ((L - K) \times \{a\})$ . Then $G: ^K M \to {}^LM$ and $G$ is clearly one-to-one.

Example We can calculate the product $\aleph_0 \cdot 2^{\aleph_0}$ by the method of upper and lower bounds:

$$
2 ^ {\aleph_ {0}} \leq \aleph_ {0} \cdot 2 ^ {\aleph_ {0}} \leq 2 ^ {\aleph_ {0}} \cdot 2 ^ {\aleph_ {0}} = 2 ^ {\aleph_ {0}},
$$

whence equality holds throughout.

We would like to show that $\aleph_0$ is the least infinite cardinal; that is, that $\aleph_0 \leq \kappa$ for any infinite cardinal $\kappa$ . This amounts (by the definition of $\leq$ ) to showing that $\omega \preccurlyeq A$ for any infinite $A$ . We might attempt to define a one-to-one function $g: \omega \to A$ by recursion:

$g(0) =$ some member of $A$

$$
g (n ^ {+}) = \text { some   member   of } A - g [ n ^ {+} ].
$$

Here $A - g[n^{+}]$ is nonempty, lest $A$ be finite. A minor difficulty here is that $g(n^{+})$ is being defined not from $g(n)$ but from $g[n^{+}] = \{g(0), g(1), \ldots, g(n)\}$ . This difficulty is easily circumvented, and will be circumvented in the proof of Theorem 6N. A major difficulty is the phrase “some member.” Unless we say which member, the above cannot possibly be construed as defining $g$ .

What is needed here is the axiom of choice, which will enable us to convert “some member” into a more acceptable phrase.

## Exercises

15. Show that there is no set $\mathcal{A}$ with the property that for every set there is some member of $\mathcal{A}$ that dominates it.

16. Show that for any set $S$ we have $S \preccurlyeq {}^s 2$ , but $S \not\cong {}^s 2$ . (This should be done directly, without use of $\mathcal{PS}$ or cardinal numbers. If $F: S \to {}^s 2$ , then define $g(x) = 1 - F(x)(x)$ .)

17. Give counterexamples to show that we cannot strengthen Theorem 6L by replacing “≤” by “<” throughout.

## AXIOM OF CHOICE

At several points in this book we have already encountered the need for a principle asserting the possibility of selecting members from nonempty sets. We can no longer postpone a systematic discussion of such a principle. There are numerous equivalent formulations of the axiom of choice. The following theorem lists six of them. Others will be found in the exercises.

Theorem 6M The following statements are equivalent.

(1) Axiom of choice, I. For any relation $R$ , there is a function $F \subseteq R$ with $\operatorname{dom} F = \operatorname{dom} R$ .

(2) Axiom of choice, II; multiplicative axiom. The Cartesian product of nonempty sets is always nonempty. That is, if $H$ is a function with domain $I$ and if $(\forall i \in I)H(i) \neq \emptyset$ , then there is a function $f$ with domain $I$ such that $(\forall i \in I)f(i) \in H(i)$ .

(3) Axiom of choice, III. For any set $A$ there is a function $F$ (a "choice function" for $A$ ) such that the domain of $F$ is the set of nonempty subsets of $A$ , and such that $F(B) \in B$ for every nonempty $B \subseteq A$ .

(4) Axiom of choice, IV. Let $\mathcal{A}$ be a set such that (a) each member of $\mathcal{A}$ is a nonempty set, and (b) any two distinct members of $\mathcal{A}$ are disjoint. Then there exists a set $C$ containing exactly one element from each member of $\mathcal{A}$ (i.e., for each $B \in \mathcal{A}$ the set $C \cap B$ is a singleton $\{x\}$ for some $x$ ).

(5) Cardinal comparability. For any sets $C$ and $D$ , either $C \preccurlyeq D$ or $D \preccurlyeq C$ . For any two cardinal numbers $\kappa$ and $\lambda$ , either $\kappa \leq \lambda$ or $\lambda \leq \kappa$ .

(6) Zorn's lemma. Let $\mathcal{A}$ be a set such that for every chain $\mathcal{B} \subseteq \mathcal{A}$ , we have $\bigcup \mathcal{B} \in \mathcal{A}$ . ( $\mathcal{B}$ is called a chain iff for any $C$ and $D$ in $\mathcal{B}$ , either $C \subseteq D$ or $D \subseteq C$ .) Then $\mathcal{A}$ contains an element $M$ (a "maximal" element) such that $M$ is not a subset of any other set in $\mathcal{A}$ .

Statements (1)-(4) are synoptic ways of saying that there exist uniform methods for selecting elements from sets. On the other hand, statements (5) and (6) appear to be rather different.

Proof in part First we will prove that (1)-(4) are equivalent.

(1)⇒(2) To prove (2), we assume that H is a function with domain I and that $H(i) \neq \varnothing$ for each $i \in I$ . In order to utilize (1), define the relation

$$
R = \{\langle i, x \rangle \mid i \in I \& x \in H (i) \}.
$$

Then (1) provides us with a function $F \subseteq R$ such that $\operatorname{dom} F = \operatorname{dom} R = I$ . Then since $\langle i, F(i) \rangle \in F \subseteq R$ , we must have $F(i) \in H(i)$ . Thus the conclusion of (2) holds.

(2) $\Rightarrow$ (4). Let $\mathcal{A}$ be a set meeting conditions (a) and (b) of (4). Let $H$ be the identity function on $\mathcal{A}$ ; then $(\forall B \in \mathcal{A}) H(B) \neq \emptyset$ . Hence by (2) there is a function $f$ with domain $\mathcal{A}$ such that $(\forall B \in \mathcal{A}) f(B) \in H(B) = B$ . Let $C = \operatorname{ran} f$ . Then for $B \in \mathcal{A}$ we have $B \cap C = \{f(B)\}$ . (Nothing else could belong to $B \cap C$ by condition (b).)

(4) $\Rightarrow (3)$ Given a set $A$ , define

$$
\mathcal {A} = \{\{B \} \times B \mid B \text {   is   a   nonempty   subset   of   } A \}.
$$

Then each member of $\mathcal{A}$ is nonempty, and any two distinct members are disjoint (if $\langle x, y \rangle \in (\{B\} \times B) \cap (\{B'\} \times B')$ , then $x = B = B'$ ). Let $C$ be a set (provided by (4)) whose intersection with each member of $\mathcal{A}$ is a singleton:

$$
C \cap (\{B \} \times B) = \{\langle B, x \rangle \},
$$

where $x \in B$ . It is a priori possible that $C$ contains extraneous elements not belonging to any member of $\mathcal{A}$ . So discard them by letting $F = C \cap (\bigcup_{\mathcal{A}} \mathcal{A})$ . We claim that $F$ is a choice function for $A$ . Any member of $F$ belongs to some $\{B\} \times B$ , and hence is of the form $\langle B, x \rangle$ for $x \in B$ . For any one nonempty set $B \subseteq A$ , there is a unique $x$ such that $\langle B, x \rangle \in F$ , because $F \cap (\{B\} \times B)$ is a singleton. This $x$ is of course $F(B)$ and it is a member of $B$ .

(3) $\Rightarrow$ (1) Consider any relation $R$ . Then (3) provides us with a choice function $G$ for ran $R$ ; thus $G(B) \in B$ for any nonempty subset $B$ of ran $R$ . Then define a function $F$ with $\operatorname{dom} F = \operatorname{dom} R$ by

$$
F (x) = G (\{y \mid x R y \}).
$$

Then $F(x) \in \{y \mid xRy\}$ , i.e., $\langle x, F(x) \rangle \in R$ . Hence $F \subseteq R$ .

It remains to include parts (5) and (6) of the theorem.

(6)⇒ (1) The strategy behind this application (and others) of Zorn's lemma is to form a collection A of pieces of the desired object, and then to show that a maximal piece serves the intended purpose. In the present case, we are given a relation R and we choose to define

$$
\mathscr {A} = \{f \subseteq R | f \text {   is   a   function } \}.
$$

Before we can appeal to Zorn's lemma, we must check that $\mathcal{A}$ is closed under unions of chains. So consider any chain $\mathcal{B} \subseteq \mathcal{A}$ . Since every member of $\mathcal{B}$ is a subset of $R$ , $\bigcup \mathcal{B}$ is a subset of $R$ . To see that $\bigcup \mathcal{B}$ is a function, we use the fact that $\mathcal{B}$ is a chain. If $\langle x, y \rangle$ and $\langle x, z \rangle$ belong to $\bigcup \mathcal{B}$ , then

$$
\langle x, y \rangle \in G \in \mathcal {B} \quad \text { and } \quad \langle x, z \rangle \in H \in \mathcal {B}
$$

for some functions $G$ and $H$ in $\mathcal{A}$ . Either $G \subseteq H$ or $H \subseteq G$ ; in either event both $\langle x, y \rangle$ and $\langle x, z \rangle$ belong to a single function, so $y = z$ . Hence $\bigcup \mathcal{B}$ is in $\mathcal{A}$ . Now we can appeal to (6), which provides us with a maximal function $F$ in $\mathcal{A}$ . We claim that $\operatorname{dom} F = \operatorname{dom} R$ . For otherwise take any $x \in \operatorname{dom} R - \operatorname{dom} F$ . Since $x \in \operatorname{dom} R$ , there is some $y$ with $xRy$ . Define

$$
F ^ {\prime} = F \cup \{\langle x, y \rangle \}.
$$

Then $F' \in \mathcal{A}$ , contradicting the maximality of $F$ . Hence $\operatorname{dom} F = \operatorname{dom} R$ . (6) $\Rightarrow$ (5) Let $C$ and $D$ be any sets; we will show that either $C \preccurlyeq D$ or $D \preccurlyeq C$ . In order to utilize (6), define

$$
\mathscr {A} = \{f | f \text {   is   a   one - to - one   function   } \& \operatorname{dom} f \subseteq C \& \operatorname{ran} f \subseteq D \}.
$$

Consider any chain $\mathcal{B} \subseteq \mathcal{A}$ . As in the preceding paragraph, $\bigcup \mathcal{B}$ is a function, and a similar argument shows that $\bigcup \mathcal{B}$ is one-to-one. Next consider $\langle x, y \rangle \in \bigcup \mathcal{B}$ ; then $\langle x, y \rangle \in f \in \mathcal{A}$ . Consequently $x \in C$ and $y \in D$ . Thus $\operatorname{dom} \bigcup \mathcal{B} \subseteq C$ and $\operatorname{ran} \bigcup \mathcal{B} \subseteq D$ . Hence $\bigcup \mathcal{B} \in \mathcal{A}$ and we can apply (6) to obtain a maximal $\hat{f} \in \mathcal{A}$ . We claim that either $\operatorname{dom} \hat{f} = C$ (in which case $C \preccurlyeq D$ ) or $\operatorname{ran} \hat{f} = D$ (in which case $D \preccurlyeq C$ since $\hat{f}^{-1}$ is then a one-to-one function from $D$ into $C$ ). Suppose to the contrary that neither condition holds, so that there exist elements $c \in C - \operatorname{dom} \hat{f}$ and $d \in D - \operatorname{ran} \hat{f}$ . Then

$$
f ^ {\prime} = \hat {f} \cup \{\langle c, d \rangle \}
$$

is in $\mathcal{A}$ , contradicting the maximality of $\hat{f}$ . (You will observe that the strategy underlying this application of Zorn's lemma is the same one as in the preceding paragraph.)

At this point we have proved that part of Theorem 6M shown in Fig. 40. The proof will be completed in Chapter 7.

Remarks Zorn's lemma first appeared in a 1922 paper by Kuratowski. Earlier maximality principles that were similar in spirit had been published by Felix Hausdorff. The importance of Zorn's lemma lies in the fact that it is well suited to many applications. in mathematics. For example, to prove in linear algebra that every vector space has a basis requires some form of choice, and Zorn's lemma is a convenient form to use here. (Take $\mathcal{A}$ to be the collection of all linearly independent sets; then a maximal element will be a basis.) Similarly in proving that there exist maximal proper ideals in a ring with identity or in proving that there exist maximal Abelian subgroups in a group, Zorn's lemma provides a suitable tool.

We can give a plausibility argument for Zorn's lemma as follows. A cannot be empty, because $\varnothing$ is a chain and so $\varnothing = \bigcup \varnothing \in A$ . Probably $\varnothing$ is not maximal, so we can choose a larger set. If that larger set is not maximal, we can choose a still larger one. After infinitely many steps, even if we have not found a maximal set we have at least formed a chain. So we can take its union and continue. The procedure can stop only when we finally reach a maximal set. So if only we are patient enough, we should reach such a set.

![](images/23e679e1d48c1aa408e38ffb2b5354a02de023ca8f3a972bf39217d9a8835901.jpg)  
Fig. 40. This much of Theorem 6M we prove now; the rest is postponed.

We now formally add the axiom of choice to our list of axioms. And we do it without a marginal stripe. This is because historically the axiom of choice has had a unique status. Initially some mathematicians objected to the axiom, because it asserts the existence of a set without specifying exactly what is in it. To this extent it is less “constructive” than the other axioms. Gradually the axiom has won acceptance (at least acceptance by most mathematicians willing to accept classical logic). But it retains a slightly tarnished image, from the days when it was not quite respectable. Consequently it has become wide-spread practice, each time the axiom of choice is used, to make explicit mention of the fact. (No such gesture is extended to the other axioms, which are used extensively and mentioned rarely.)

In Chapter 7 we will complete our axiomatization by adding the replacement axioms and the regularity axiom.

Without the axiom of choice, we can still prove that for a finite set I, if $H(i) \neq \varnothing$ for all $i \in I$ , then there is a function f with domain I such that $f(i) \in H(i)$ for all $i \in I$ (Exercise 19). But for an infinite set I, the axiom of choice is indispensable. (If we are making seven choices, we can explicitly mention each one; for $N_{0}$ choices this is no longer possible.)

In particular, if we are choosing one thing, then we do not need the axiom of choice. (We mention this because people sometimes overreact when first hearing of the axiom of choice.) For example, assume that $A \neq \varnothing$ . Then there exists some $y_{0}$ in A; we can use $y_{0}$ in further arguments (to show, e.g., that some singleton $\{y_{0}\}$ is a subset of A). This makes no use of the axiom of choice, even when phrased as “we can choose some fixed $y_{0}$ in A.”

For a second example, assume we are given a relation $R$ . For any particular $x$ in dom $R$ , there exists some $y_0$ for which $xRy_0$ . And we can conclude that for any $x$ in dom $R$ , there is a singleton $\{y_0\}$ included in $\{t \mid xRt\}$ . We have not yet used the axiom of choice. What does require the axiom of choice is saying that for any $x$ in dom $R$ there is some $y_x$ for which $xRy_x$ , and then putting all these $y_x$ 's together into a set, e.g.,

$$
\{y _ {x} \mid x \in \operatorname{dom} R \}.
$$

This in effect is making many choices, one for each x in dom R, which may be an infinite set. (A human being cannot perform infinitely many actions. But the axiom of choice asserts that, despite our practical limitations, there exists, in theory, a set produced by making infinitely many choices.)

Another situation in which the axiom of choice can be avoided is where we can specify exactly which object we want to choose. For example, we can show, without using the axiom of choice, that there is a choice function for $\omega$ . Namely, define $F: (\mathcal{P}\omega - \{\varnothing\}) \to \omega$ by

$$
F (A) = \text { the   least   member   of } A
$$

for $\varnothing \neq A \subseteq \omega$ . The crucial point here is that we can write down an expression defining the selected member of $A$ . If $\omega$ is replaced by $\mathbb{R}$ , for example, there is no longer the possibility of defining a way to select numbers from arbitrary nonempty subsets of $\mathbb{R}$ .

Since there is a choice function on $\omega$ , it follows that there is a choice function on any set equinumerous to $\omega$ . (Why?) And similarly any finite set has a choice function.

The following example is due to Russell. If we have $N_{0}$ pairs of shoes, then we can select one shoe from each pair without using the axiom of choice. We simply select the left shoe from each pair. But if we have $N_{0}$ pairs of socks, then we must use the axiom of choice if we are to select one sock from each pair. For there is no definable difference between the two socks in a pair.

Example Assume that $f$ is a function from $A$ onto $B$ . We claim that $B \preccurlyeq A$ . To verify this, recall that by Theorem 3J(b), the proof of which used choice, there is a right inverse $g: B \to A$ such that $f \circ g = I_B$ . And $g$ is one-to-one since it has a left inverse. The function $g$ shows that $B \preccurlyeq A$ .

Conversely assume that $B \preccurlyeq A$ and $B$ is nonempty. Then (since $B \preccurlyeq A$ ) there is a one-to-one function $g: B \to A$ . By Theorem 3J(a) there is a left inverse $f: A \to B$ such that $f \circ g = I_B$ . And $f$ maps $A$ onto $B$ since it has a right inverse.

Hence we can conclude: If B is nonempty, then $B \preccurlyeq A$ iff there is a function from A onto B. As a special case, we can conclude that a nonempty set B is dominated by $\omega$ iff there is a function from $\omega$ onto B. (This special case can be proved without the axiom of choice.)

We now utilize the axiom of choice to prove that $N_{0}$ is the least infinite cardinal number.

Theorem 6N (a) For any infinite set $A$ , we have $\omega \preccurlyeq A$ .

(b) $\aleph_0\leq \kappa$ for any infinite cardinal $\kappa$ .

Proof Part (b) is merely a restatement of part (a) in terms of cardinals; it suffices to prove (a). So consider an infinite set A. The idea is to select $N_{0}$ things from A: a first, then a second, then a third, .... Let F be a choice function for A (as provided by the axiom of choice, III). We must somehow employ F repeatedly; in fact $N_{0}$ times.

As a first try, we could attempt to define a function $g: \omega \to A$ by recursion. We know A is nonempty; fix some element $a \in A$ . Maybe we can take

$$
\begin{array}{l} g (0) = a, \\ g (n ^ {+}) = \text { the   chosen   member   of } A - \{g (0), \dots , g (n) \} \\ = F (A - g [ n ^ {+} ]). \end{array}
$$

No, we cannot. This would require a stronger recursion theorem than the one proved in Chapter 4. We are attempting to define $g(n^{+})$ not just from $g(n)$ , but from the entire list $g(0), g(1), \ldots, g(n)$ .

But our second try will succeed. We will define by recursion a function h from $\omega$ into the set of finite subsets of A. The guiding idea is to have, for example, $h(7) = \{g(0), \ldots, g(6)\}$ . Formally,

$$
\begin{array}{c} h (0) = \varnothing , \\ h (n ^ {+}) = h (n) \cup \{F (A - h (n)) \}. \end{array}
$$

Thus we start with $\varnothing$ , and successively add chosen new elements from $A$ . $A - h(n)$ is nonempty because $A$ is infinite and $h(n)$ is a finite subset. And $h(n^{+})$ is again a finite subset of $A$ .

Now we can go back and recover g. Define

$$
g (n) = F (A - h (n))
$$

so that $g(n)$ is the thing we added to the set $h(n)$ to make $h(n^{+})$ . Thus $g: \omega \to A$ ; we must check that $g$ is one-to-one.

Suppose then that $m \neq n$ . One number is less than the other; say $m \in n$ . Then $m^{+} \in n$ and so

$$
g (m) \in h (m ^ {+}) \subseteq h (n).
$$

But $g(n) \notin h(n)$ , since

$$
g (n) = F (A - h (n)) \in A - h (n).
$$

Hence $g(m) \neq g(n)$ .

We can now list some consequences of the foregoing theorem.

1. Any infinite subset of $\omega$ is equinumerous to $\omega$ . In this special case we can avoid using the axiom of choice, since we have a choice function for $\omega$ anyway.

2. We have by part (b) of the theorem that if $\kappa < \aleph_0$ , then $\kappa$ is finite. Since the converse is clear, we have

$$
\kappa <   \aleph_ {0} \quad \text { iff } \quad \kappa \text {   is   finite. }
$$

3. We get another proof that subsets of finite sets are finite (Corollary 6G). For if

$$
\operatorname{card} A \leq \operatorname{card} n <   \aleph_ {0},
$$

then by the Schröder–Bernstein theorem card $A < X_{0}$ , and hence A is finite.

Another consequence of the preceding theorem is the following characterization of the infinite sets (proposed by Dedekind in his 1888 book as a definition of “infinite”).

Corollary 6P A set is infinite iff it is equinumerous to a proper subset of itself.

Proof Half of this result is contained in Corollary 6D, where we showed that if a set was equinumerous to a proper subset of itself, then it was infinite. Conversely, consider an infinite set A. Then by the above theorem, there is a one-to-one function f from $\omega$ into A. Define a function g from A into A by

$$
g (f (n)) = f \left(n ^ {+}\right) \quad \text { for } \quad n \in \omega ,
$$

$$
g (x) = x \quad \text { for } \quad x \notin \operatorname{ran} f
$$

(see Fig. 41). Then $g$ is a one-to-one function from $A$ onto $A - \{f(0)\}$ .

![](images/e301cbfcabbaa4cc7b456de2dc2b055acb79319b6c26b8e1c0598eacd250b29b.jpg)  
Fig. 41. $f(0)$ is not in ran $g$ .

## Exercises

18. Prove that the following statement is equivalent to the axiom of choice: For any set A whose members are nonempty sets, there is a function f with domain A such that $f(X) \in X$ for all X in A.

19. Assume that H is a function with finite domain I and that $H(i)$ is nonempty for each $i \in I$ . Without using the axiom of choice, show that there is a function f with domain I such that $f(i) \in H(i)$ for each $i \in I$ . [Suggestion: Use induction on card I.]

20. Assume that A is a nonempty set and R is a relation such that $(\forall x \in A)(\exists y \in A)yRx$ . Show that there is a function $f: \omega \to A$ with $f(n^{+})Rf(n)$ for all n in $\omega$ .

21. (Teichmüller–Tukey lemma) Assume that A is a nonempty set such that for every set B,

$B \in \mathcal{A} \Leftrightarrow$ every finite subset of $B$ is a member of $\mathcal{A}$ .

Show that A has a maximal element, i.e., an element that is not a subset of any other element of A.

22. Show that the following statement is another equivalent version of the axiom of choice: For any set $A$ there is a function $F$ with $\operatorname{dom} F = \bigcup A$ and such that $x \in F(x) \in A$ for all $x \in \bigcup A$ .

23. Show that in the proof to Theorem 6N, we have $g[n] = h(n)$ .

24. How would you define the sum of infinitely many cardinal numbers? Infinite products?

25. Assume that $S$ is a function with domain $\omega$ such that $S(n) \subseteq S(n^{+})$ for each $n \in \omega$ . (Thus $S$ is an increasing sequence of sets.) Assume that $B$ is a subset of the union $\bigcup_{n \in \omega} S(n)$ such that for every infinite subset $B'$ of $B$ there is some $n$ for which $B' \cap S(n)$ is infinite. Show that $B$ is a subset of some $S(n)$ .

## COUNTABLE SETS

The definition below applies the word “countable” to those sets whose elements can, in a sense, be counted by means of the natural numbers. A “counting” of a set can be taken to be a one-to-one correspondence between the members of the set and the natural numbers (or the natural numbers less than some number n). This requires that the set be no larger than $\omega$ .

Definition A set $A$ is countable iff $A \preccurlyeq \omega$ , i.e., iff card $A \leq \aleph_0$ .

Since we have recently found that

$$
\kappa <   \aleph_ {0} \Leftrightarrow \kappa \text {   is   finite, }
$$

we can also formulate the definition as follows: A set $A$ is countable iff either $A$ is finite or $A$ has cardinality $\aleph_0$ .

For example, the set $\omega$ of natural numbers, the set Z of integers, and the set Q of rational numbers are all infinite countable sets. But the set R of real numbers is uncountable (Theorem 6B).

Any subset of a countable set is obviously countable. The union of two countable sets is countable, as is their Cartesian product. (The union has at most cardinality $\aleph_0 + \aleph_0$ , the product at most $\aleph_0 \cdot \aleph_0$ . But both of these numbers equal $\aleph_0$ .) On the other hand, $\mathcal{P}A$ is uncountable for any infinite set $A$ . (If $2^\kappa \leq \aleph_0$ , then $\kappa < \aleph_0$ .)

Recall (from the example preceding Theorem 6N) that a nonempty set B is countable iff there is a function from $\omega$ onto B. This fact is used in the proof of the next theorem.

Theorem 6Q A countable union of countable sets is countable. That is, if $\mathcal{A}$ is countable and if every member of $\mathcal{A}$ is a countable set, then $\bigcup \mathcal{A}$ is countable.

Proof We may suppose that $\varnothing \notin \mathcal{A}$ , for otherwise we could simply remove it without affecting $\bigcup \mathcal{A}$ . We may further suppose that $\mathcal{A} \neq \emptyset$ , since $\bigcup \emptyset$ is certainly countable. Thus $\mathcal{A}$ is a countable (but nonempty) from $\omega \times \omega$ onto $\bigcup \mathcal{A}$ . We already know of functions from $\omega$ onto $\omega \times \omega$ , and the composition will map $\omega$ onto $\bigcup \mathcal{A}$ , thereby showing that $\bigcup \mathcal{A}$ is countable.

Since $\mathcal{A}$ is countable but nonempty, there is a function $G$ from $\omega$ onto $\mathcal{A}$ . Informally, we may write

$$
\mathcal {A} = \{G (0), G (1), \dots \}.
$$

(Here G might not be one-to-one, so there may be repetitions in this enumeration.) We are given that each set $G(m)$ is countable and nonempty.

Hence for each m there is a function from $\omega$ onto $G(m)$ . We must use the axiom of choice to select such a function for each m.

Because the axiom of choice is a recent addition to our repertoire, we will describe its use here in some detail. Let $H \colon \omega \to {}^{\omega}(\bigcup \mathcal{A})$ be defined by

$H(m) = \{g \mid g \text{ is a function from } \omega \text{ onto } G(m)\}$ .

We know that $H(m)$ is nonempty for each $m$ . Hence there is a function $F$ with domain $\omega$ such that for each $m$ , $F(m)$ is a function from $\omega$ onto $G(m)$ .

To conclude the proof we have only to let $f(m, n) = F(m)(n)$ . Then $f$ is a function from $\omega \times \omega$ onto $\bigcup \mathcal{A}$ .

Example For any set A, define a sequence in A to be a function from some natural number into A. Let $\operatorname{Sq}(A)$ be the set of all sequences in A:

$$
\begin{array}{r l} \operatorname{Sq} (A) & = \left\{f \mid (\exists n \in \omega) f \text {   maps   } n \text {   into   } A \right\} \\ & = ^ {0} A \cup {} ^ {1} A \cup {} ^ {2} A \cup \dots . \end{array}
$$

The length of a sequence is simply its domain.

In order to verify that $\operatorname{Sq}(A)$ is a legal set, note that if $f: n \to A$ , then

$$
f \subseteq n \times A \subseteq \omega \times A,
$$

so that $f \in \mathcal{P}(\omega \times A)$ . Hence $\operatorname{Sq}(A) \subseteq \mathcal{P}(\omega \times A)$ .

We now list some observations that establish the existence of transcendental real numbers.

1. $\operatorname{Sq}(\omega)$ has cardinality $\aleph_0$ . This can be proved by using primarily the fact that $\omega \times \omega \approx \omega$ . Another very direct proof is the following. Consider any $f \in \operatorname{Sq}(\omega)$ ; say the length of $f$ is $n$ . Then define

$$
H (f) = 2 ^ {f (0) + 1} \cdot 3 ^ {f (1) + 1} \cdot \dots \cdot p _ {n - 1} ^ {f (n - 1) + 1},
$$

where $p_{i}$ is the $(i+1)$ st prime. (If the length of f is 0, then $H(f)=1$ .) Thus $H: \mathrm{Sq}(\omega) \to \omega$ and by the fundamental theorem of arithmetic (which states that prime factorizations are unique) H is one-to-one. Hence card $\mathrm{Sq}(\omega) \leq \aleph_{0}$ , and the opposite inequality is clear. (In Chapter 4 we did not actually develop the theory of prime numbers. But there are no difficulties in embedding any standard development of the subject into set theory.)

2. $\operatorname{Sq}(A)$ is countable for any countable set $A$ . By the countability of $A$ there is a one-to-one function $g$ from $A$ into $\omega$ . This function naturally induces a one-to-one map from $\operatorname{Sq}(A)$ into $\operatorname{Sq}(\omega)$ . Hence card $\operatorname{Sq}(A) \leq$ card $\operatorname{Sq}(\omega) = \aleph_0$ . (An alternative proof writes $\operatorname{Sq}(A) = \bigcup \{^n A \mid n \in \omega\}$ , a countable union of countable sets.)

We can think of this set A as an alphabet, and the elements of $\operatorname{Sq}(A)$ as being words on the alphabet A. In this terminology, the present example can be stated: On any countable alphabet, there are countably many words.

3. There are $\aleph_0$ algebraic numbers. (Recall that an algebraic number is a real number that is the root of some polynomial with integer coefficients. For this purpose we exclude from the polynomials the function that is identically equal to 0.) As a first step in counting the algebraic numbers, note that the set $\mathbb{Z}$ of integers has cardinality $\aleph_0 + \aleph_0 = \aleph_0$ . Next we calculate the cardinality of the set $P$ of polynomials with integer coefficients. We can assign to each polynomial (of degree $n$ ) its sequence (of length $n + 1$ ) of coefficients, e.g., $1 + 7x - 5x^2 + 3x^4$ is assigned the sequence of length 5 whose successive values are 1, 7, -5, 0, 3. This defines a one-to-one map from $P$ into $\operatorname{Sq}(\mathbb{Z})$ , a countable set. Hence $P$ is countable. Since each polynomial in $P$ has only finitely many roots, the set of algebraic numbers is a countable union of finite sets. Hence it is countable, by Theorem 6Q. Since the set of algebraic numbers is certainly infinite, it has cardinality $\aleph_0$ .

4. There are uncountably many transcendental numbers. (Recall that a transcendental number is defined to be a real number that is not algebraic.) Since the set of algebraic numbers is countable, the set of transcendental numbers cannot also be countable lest the set R be countable. (Soon we will be able to show that the set of transcendental numbers has cardinality $2^{N_{0}}$ .)

## Exercises

26. Prove the following generalization of Theorem 6Q: If every member of a set $\mathcal{A}$ has cardinality $\kappa$ or less, then

$$
\operatorname{card} \bigcup \mathscr {A} \leq (\operatorname{card} \mathscr {A}) \cdot \kappa .
$$

27. (a) Let $A$ be a collection of circular disks in the plane, no two of which intersect. Show that $A$ is countable.

(b) Let $B$ be a collection of circles in the plane, no two of which intersect. Need $B$ be countable?

(c) Let $C$ be a collection of figure eights in the plane, no two of which intersect. Need $C$ be countable?

28. Find a set A of open intervals in R such that every rational number belongs to one of those intervals, but $\bigcup A \neq R$ . [Suggestion: Limit the sum of the lengths of the intervals.]

29. Let A be a set of positive real numbers. Assume that there is a bound b such that the sum of any finite subset of A is less than b. Show that A is countable.

30. Assume that $A$ is a set with at least two elements. Show that $\operatorname{Sq}(A) \preccurlyeq {}^{\omega} A$ .

## ARITHMETIC OF INFINITE CARDINALS

We can use the axiom of choice to show that adding or multiplying two infinite cardinals is a more trivial matter than it first appeared to be.

Lemma 6R For any infinite cardinal $\kappa$ , we have $\kappa \cdot \kappa = \kappa$ .

Proof Let $B$ be a set of cardinality $\kappa$ . It would suffice to show that $B \times B \approx B$ , and we will almost do this. Define

$$
\mathscr {H} = \{f \mid f = \emptyset \text {   or   for   some   infinite   } A \subseteq B, f \text {   is   a   }
$$

one-to-one correspondence between $A \times A$ and $A\}$ .

Our strategy is to use Zorn's lemma to obtain a maximal function $f_{0}$ in H. Although $f_{0}$ might not quite show that $B \times B \approx B$ , it will come close enough. (The reason for including $\varnothing$ as a member of H is that our statement of Zorn's lemma requires that H contain the union of any chain, even the empty chain.)

Before applying Zorn's lemma to H, we must check for closure under unions of chains. Let C be a chain included in H. We may suppose that C contains some nonempty function, since otherwise $\bigcup C = \varnothing \in H$ . As we have seen before, $\bigcup C$ is again a one-to-one function. Define

$$
A = \bigcup \{\operatorname{ran} f \mid f \in \mathscr {C} \} = \operatorname{ran} \bigcup \mathscr {C}
$$

(compare Exercise 8 of Chapter 3). $A$ is infinite since $\mathcal{C}$ contains some nonempty function. We claim that $\bigcup \mathcal{C}$ is a one-to-one correspondence between $A \times A$ and $A$ . The only part of this claim not yet verified is that $\operatorname{dom} \bigcup \mathcal{C} = A \times A$ . First consider any $\langle a_1, a_2 \rangle \in A \times A$ . Then $a_1 \in \operatorname{ran} f_1$ and $a_2 \in \operatorname{ran} f_2$ for some $f_1$ and $f_2$ in $\mathcal{C}$ . Either $f_1 \subseteq f_2$ or $f_2 \subseteq f_1$ ; by symmetry we may suppose that $f_1 \subseteq f_2$ . Then

$$
\langle a _ {1}, a _ {2} \rangle \in \operatorname{ran} f _ {2} \times \operatorname{ran} f _ {2} = \operatorname{dom} f _ {2} \subseteq \bigcup \{\operatorname{dom} f | f \in \mathscr {C} \} = \operatorname{dom} \bigcup \mathscr {C}.
$$

Conversely any member of $\operatorname{dom} \bigcup \mathcal{C}$ belongs to $\operatorname{dom} f$ for some $f \in \mathcal{C}$ . But $\operatorname{dom} f = \operatorname{ran} f \times \operatorname{ran} f \subseteq A \times A$ . Thus $\operatorname{dom} \bigcup \mathcal{C} = A \times A$ . So $\bigcup \mathcal{C}$ is a one-to-one correspondence between $A \times A$ and $A$ ; hence $\bigcup \mathcal{C} \in \mathcal{H}$ .

Zorn's lemma now provides us with a maximal $f_0 \in \mathcal{H}$ . First, we must check that $f_0 \neq \emptyset$ . Since $B$ is infinite, it has a subset $A$ of cardinality $\aleph_0$ . Because $\aleph_0 \cdot \aleph_0 = \aleph_0$ , there is a one-to-one correspondence $g$ between $A \times A$ and $A$ . Thus $g \in \mathcal{H}$ ; since $g$ properly extends $\emptyset$ , it is impossible for $\emptyset$ to be maximal is $\mathcal{H}$ . Hence $f_0 \neq \emptyset$ . So by the definition of $\mathcal{H}$ , $f_0$ is a one-to-one correspondence between $A_0 \times A_0$ and $A_0$ , where $A_0$ is some infinite subset of $B$ .

Let $\lambda = \operatorname{card} A_0$ ; then $\lambda$ is infinite and $\lambda \cdot \lambda = \lambda$ . One might hope that by virtue of the maximality, $A_0$ would be all of $B$ . This may not be true, but we will show that $\lambda = \kappa$ and that $B - A_0$ has smaller cardinality.

In order to show that $\operatorname{card}(B-A_{0})<\lambda$ , suppose that to the contrary $\lambda\leq\operatorname{card}(B-A_{0})$ . Then $B-A_{0}$ has a subset D of cardinality $\lambda$ . We will show that this contradicts the maximality of $f_{0}$ by finding a proper extension of $f_{0}$ that is a one-to-one correspondence between the sets $(A_{0}\cup D)\times(A_{0}\cup D)$ and $A_{0}\cup D$ . We have

$$
\left(A _ {0} \cup D\right) \times \left(A _ {0} \cup D\right) = \left(A _ {0} \times A _ {0}\right) \cup \left(A _ {0} \times D\right) \cup \left(D \times A _ {0}\right) \cup (D \times D)
$$

![](images/7179611f393d4473217c5253db368d317e9b907ad0748b0fffc47bf5a419318d.jpg)  
Fig. 42. The set $B \times B$ (in Lemma 6R).

(see Fig. 42). Of the four sets on the right side of this equation, $A_0 \times A_0$ is already paired with $A_0$ by $f_0$ . The remainder

$$
\left(A _ {0} \times D\right) \cup \left(D \times A _ {0}\right) \cup (D \times D)
$$

(shaded in Fig. 42) clearly has cardinality

$$
\begin{array}{r l} \lambda \cdot \lambda + \lambda \cdot \lambda + \lambda \cdot \lambda & = \lambda + \lambda + \lambda \\ & = 3 \cdot \lambda \\ & \leq \lambda \cdot \lambda \\ & = \lambda . \end{array}
$$

Hence there is a one-to-one correspondence g between the shaded sets and D. Then $f_{0} \cup g \in H$ and properly extends $f_{0}$ , contradicting the maximality of $f_{0}$ . Hence our supposition that $\lambda \leq \text{card}(B - A_{0})$ is false. By cardinal comparability, $\text{card}(B - A_{0}) < \lambda$ .

Finally we have

$$
\begin{array}{l} \kappa = \operatorname{card} A _ {0} + \operatorname{card} (B - A _ {0}) \\ \leq \lambda + \lambda = 2 \cdot \lambda \leq \lambda \cdot \lambda = \lambda \leq \kappa , \end{array}
$$

whence $\lambda = \kappa$ . Hence $\kappa \cdot \kappa = \kappa$ .

Absorption Law of Cardinal Arithmetic Let $\kappa$ and $\lambda$ be cardinal numbers, the larger of which is infinite and the smaller of which is nonzero. Then

$$
\kappa + \lambda = \kappa \cdot \lambda = \max (\kappa , \lambda).
$$

Proof By the symmetry we may suppose that $\lambda \leq \kappa$ . Then

$$
\kappa \leq \kappa + \lambda \leq \kappa + \kappa = \kappa \cdot 2 \leq \kappa \cdot \kappa = \kappa
$$

and

$$
\kappa \leq \kappa \cdot \lambda \leq \kappa \cdot \kappa = \kappa .
$$

Hence equality holds throughout.

Example We do not have a well-defined subtraction operation for infinite cardinal numbers. If you start with $N_{0}$ things and take away $N_{0}$ things, then the number of remaining things can be anywhere from 0 to $N_{0}$ , depending on which items were removed. But if you start with $\kappa$ things (where $\kappa$ is infinite) and remove $\lambda$ things where $\lambda$ is strictly less than $\kappa$ , then exactly $\kappa$ things remain. To prove this, let $\mu$ be the cardinality of the remaining items. Then $\kappa = \lambda + \mu = \max(\lambda, \mu)$ , so that we must have $\mu = \kappa$ .

Example There are exactly $2^{N_{0}}$ transcendental numbers. This follows from the preceding example. If from the $2^{N_{0}}$ real numbers we remove the countable set of algebraic numbers, then $2^{N_{0}}$ numbers remain.

Example For any infinite cardinal $\kappa$ , we have $\kappa^{\kappa} = 2^{\kappa}$ . To prove this, observe that

$$
\kappa^ {\kappa} \leq (2 ^ {\kappa}) ^ {\kappa} = 2 ^ {\kappa \cdot \kappa} = 2 ^ {\kappa} \leq \kappa^ {\kappa},
$$

whence equality holds throughout.

We conclude this section with two counting problems:

1. How many functions from $\mathbb{R}$ into $\mathbb{R}$ are there?

2. How many of these are continuous?

The first question asks for the cardinality of the set $^{R}R$ . The cardinal number of this set is

$$
(2 ^ {\aleph_ {0}}) ^ {2 ^ {\aleph_ {0}}} = 2 ^ {\aleph_ {0} \cdot (2 ^ {\aleph_ {0}})} = 2 ^ {2 ^ {\aleph_ {0}}}.
$$

This last expression cannot be further simplified; it provides the answer to the first question. (As with finite numbers, $\kappa^{\lambda\mu}$ means $\kappa^{(\lambda\mu)}$ and not $(\kappa^{\lambda})^{\mu}$ .)

Now consider the second question; let $C(\mathbb{R})$ be the set of continuous functions in $^{\mathbb{R}}\mathbb{R}$ . It is easy to see that

$$
2 ^ {\aleph_ {0}} \leq \operatorname{card} C (\mathbb {R}) \leq 2 ^ {2 ^ {\aleph_ {0}}},
$$

but we need an exact answer. We claim that card $C(\mathbb{R}) = 2^{\aleph_0}$ . To prove this, we will consider the restriction of the continuous functions to the set $\mathbb{Q}$ of rational numbers (where $\mathbb{Q}$ is regarded as a subset of $\mathbb{R}$ ). If $f$ and $g$ are two distinct continuous functions, then $f - g$ is not identically zero. (Here $f - g$ is the result of subtracting $g$ from $f$ , not the relative complement.) Hence by continuity, there is an open interval throughout which $f - g$ is nonzero. In this interval lies some rational, so $f \upharpoonright \mathbb{Q} \neq g \upharpoonright \mathbb{Q}$ . Hence the map from $C(\mathbb{R})$ into $^{\mathbb{Q}}\mathbb{R}$ assigning to each continuous function $f$ its restriction $f \upharpoonright \mathbb{Q}$ is a one-to-one map. Thus $C(\mathbb{R}) \leq ^{\mathbb{Q}}\mathbb{R}$ and so

$$
\operatorname{card} C (\mathbb {R}) \leq \operatorname{card} ^ {\mathbb {Q}} \mathbb {R} = (2 ^ {\aleph_ {0}}) ^ {\aleph_ {0}} = 2 ^ {\aleph_ {0}}.
$$

## Exercises

31. In the proof of Lemma 6R we utilized a certain set H. How do we show from the axioms that such a set exists?

32. Let $\mathcal{F}A$ be the collection of all finite subsets of $A$ . Show that if $A$ is infinite, then $A \approx \mathcal{F}A$ .

33. Assume that $A$ is an infinite set. Prove that $A \approx \operatorname{Sq}(A)$ .

34. Assume that $2 \leq \kappa \leq \lambda$ and $\lambda$ is infinite. Show that $\kappa^{\lambda} = 2^{\lambda}$ .

35. Find a collection $\mathcal{A}$ of $2^{\aleph_0}$ sets of natural numbers such that any two distinct members of $\mathcal{A}$ have finite intersection. [Suggestion: Start with the collection of infinite sets of primes.]

36. Show that for an infinite cardinal $\kappa$ , we have $\kappa! = 2^{\kappa}$ , where $\kappa!$ is defined as in Exercise 14.

## CONTINUUM HYPOTHESIS

We have in this chapter given some examples of countable sets and uncountable sets. But every uncountable set examined thus far has had cardinality $2^{N_{0}}$ or more. This raises the question: Are there any sets with cardinality between $N_{0}$ and $2^{N_{0}}$ ? The “continuum hypothesis” is the assertion that the answer is negative, i.e., that there is no $\kappa$ with $N_{0} < \kappa < 2^{N_{0}}$ . Or equivalently, the continuum hypothesis can be stated: Every uncountable set of real numbers is equinumerous to the set of all real numbers.

Cantor conjectured that the continuum hypothesis was true. And David Hilbert later published a purported proof. But the proof was incorrect, and more recent work has cast doubt on the continuum hypothesis. In 1939 Gödel proved that on the basis of our axioms for set theory (which we here assume to be consistent) the continuum hypothesis could not be disproved. Then in 1963 Paul Cohen showed that the continuum hypothesis could not be proved from our axioms either.

But since the continuum hypothesis is neither provable nor refutable from our axioms, what can we say about its truth or falsity? We have some informal ideas about what sets are like, but our intuition might not assign a definite answer to the continuum hypothesis. Indeed, one might well question whether there is any meaningful sense in which one can say that the continuum hypothesis is either true or false for the “real” sets. Among those set-theorists nowadays who feel that there is such a meaningful sense, the majority seems to feel that the continuum hypothesis is false.

The “generalized continuum hypothesis” is the assertion that for every infinite cardinal $\kappa$ , there is no cardinal number between $\kappa$ and $2^{\kappa}$ . Gödel’s 1939 work shows that even the generalized continuum hypothesis cannot be disproved from our axioms. And of course Cohen’s result shows that it cannot be proved from our axioms (even in the special case $\kappa = N_{0}$ ).

There is the possibility of extending the list of axioms beyond those in this book. And the new axioms might conceivably allow us to prove or to refute the continuum hypothesis. But to be acceptable as an axiom, a statement must be in clear accord with our informal ideas of the concepts being axiomatized. It would not do, for example, simply to adopt the generalized continuum hypothesis as a new axiom. It remains to be seen whether any acceptable axioms will be found that settle satisfactorily the correctness or incorrectness of the continuum hypothesis.

The work of Gödel and Cohen also shows that the axiom of choice can neither be proved nor refuted from the other axioms (which we continue to assume are consistent). But unlike the continuum hypothesis, the axiom of choice conforms to our informal view of how sets should behave. For this reason, we have adopted it as an axiom.

Results such as those by Gödel and Cohen belong to the metamathematics of set theory. That is, they are results that speak of set theory itself, in contrast to theorems within set theory that speak of sets.

# ORDERINGS AND ORDINALS

In this chapter we will begin by discussing both linear orderings (mentioned briefly in Chapter 3) and, more generally, partial orderings. But we will soon focus our attention on a special case of the linear orderings, namely the so-called well orderings. The well orderings will lead us to the study of ordinal numbers and to the fulfillment of promises (e.g., the definition of cardinal numbers) that have been made.

## PARTIAL ORDERINGS

A partial ordering is a special sort of relation. Before making any definitions, it will be helpful to consider a few examples.

1. Let S be any fixed set, and let $\subset_{S}$ be the relation of strict inclusion on subsets of S:

$$
\subset_ {S} = \{\langle A, B \rangle \mid A \subseteq B \subseteq S \& A \neq B \}.
$$

Of course we write “ $A \subset_{S} B$ ” in place of the more awkward “ $\langle A, B \rangle \in \subset_{S}$ .”

2. Let $P$ be the set of positive integers. The strict divisibility relation on $P$ is

$$
\{\langle a, b \rangle \in P \times P \mid a \cdot q = b \text {   for   some   } q \neq 1 \}.
$$

For example, 5 divides 60 (here q = 12), but 2 does not divide 3, nor does 3 divide 2. No number in P strictly divides itself.

3. For the set R of real numbers, we have the usual ordering relation <. For any distinct real numbers x and y, either x < y or y < x.

Definition A partial ordering is a relation $R$ meeting the following two conditions:

(a) $R$ is a transitive relation: $xRy \& yRz \Rightarrow xRz$ .

(b) $R$ is irreflexive: It is never the case that $xRx$ .

In the foregoing examples, it is easy to see that $\subset_{s}$ , strict divisibility, and < are all partial ordering relations. The preferred symbols for partial ordering relations are < and similar symbols, e.g., $\prec$ , $\subset$ , and the like. If < is such a relation, then we can define:

$$
x \leq y \quad \text { iff } \quad \text { either } \quad x <   y \quad \text { or } \quad x = y.
$$

![](images/3365b979e8466bce761de3d5966cb7ccb99b92d95bb67e74ff1b327806ce9ac9.jpg)  
Fig. 43. The inclusion ordering on $\{0, 1, 2\}$ .

![](images/68e18dcca262a6291705eafe3806363a4a8d65474da14a1ab0cdd113a29602ef.jpg)  
Fig. 44. A finite part of an infinite picture.

It is easy to see that, for example,

$$
x \leq y <   z \Rightarrow x <   z.
$$

At the end of Chapter 3 we drew some pictures (Fig. 15) of orderings. For partial orderings the pictures show more variety. Again we represent the members of $A$ by dots, placing the dot for $x$ below the dot for $y$ whenever $x < y$ , and drawing lines to connect the dots. For example, Fig. 43 is a picture of the partial ordering $\subset_{S}$ on the set $S = \{0, 1, 2\}$ . There is no need to add a direct nonstop line from $\varnothing$ to $\{0, 1\}$ , because there are lines from $\varnothing$ to $\{0\}$ and from $\{0\}$ to $\{0, 1\}$ . Figure 44 is a picture of a small piece of the divisibility ordering on the positive integers; the full picture would have to be infinite.

The following theorem lists some easy consequences of our definitions.

Theorem 7A Assume that $<$ is a partial ordering. Then for any $x, y$ , and $z$ :

(a) At most one of the three alternatives,

$$
x <   y, \quad x = y, \quad y <   x,
$$

can hold.

$$
\text { (b) } \quad x \leq y \leq x \Rightarrow x = y.
$$

Proof In part (a), if we had both x < y and x = y, then we would have x < x, contradicting irreflexivity. And if both x < y and y < x, then by transitivity x < x, again contradicting irreflexivity.

In part (b) if $x \neq y$ then we would have $x < y < x$ , contradicting part (a).

We are particularly interested in cases where part (a) of this theorem can be strengthened to read “exactly one,” i.e., trichotomy holds.

Definition R is a linear ordering on A iff R is a binary relation on A that is a transitive relation and satisfies trichotomy on A, i.e., for any x and y in A exactly one of the three alternatives,

$$
x R y, \quad x = y, \quad y R x,
$$

holds.

Note that we have to specify the set A in this definition. We can also speak of a partial ordering on A, this being just a binary relation on A that is a partial ordering.

Examples The usual ordering relation on R is linear. Strict divisibility is a partial ordering, but is not a linear ordering on the positive integers. And inclusion $\subset_{S}$ is nonlinear if S has two or more members.

Notice that if R is a linear ordering on A, then R is also a partial ordering (since trichotomy implies irreflexivity—recall Theorem 3R).

Digression In the study of partial orderings, there is always the question whether to use strict orderings (<) or weak orderings (≤) as the basic concept. We have taken the “<” course, by demanding that a partial ordering be irreflexive. For the “≤” version, one demands that a partial ordering on A be reflexive on A. Yet a third course is to specify neither extreme, but to allow any pairs $\langle x, x \rangle$ to belong to the ordering or not, as they please. Each alternative has its own minor advantages and its own drawbacks. One feature of demanding reflexivity is that whenever ≤ is a partial ordering on A, then A = fld ≤. Consequently we can treat just the ordering ≤; the set A is then encoded inside this relation. For strict orderings this feature is lost; for example, ∅ is a partial ordering on any set. Often we will want to refer to a set A together with an ordering < on A.

Definition A structure is a pair $\langle A, R \rangle$ consisting of a set A and a binary relation R on A (i.e., $R \subseteq A \times A$ ).

In particular, we can speak of a partially (or linearly) ordered structure if R is a partial (or linear) ordering relation on A. (The terms poset and loset are sometimes used here.)

There is a certain amount of terminology for orderings that has proved sufficiently useful to have become standard. Let < be a partial ordering; let D be a set. An element m of D is said to be a minimal element of D iff there is no x in D with x < m (or equivalently, iff for all x in D, $x \neq m$ ). And m is a least (or smallest or minimum) element of D iff $m \leq x$ for all x in D. A least element is also minimal. For a linear ordering on a set that includes D the two concepts coincide, since

$$
x \not <   m \Rightarrow m \leq x
$$

for a linear ordering. But in the nonlinear case, minimality is weaker than leastness.

Example Consider the strict divisibility relation on the set P of positive integers. Then 1 is the least element of P. But let D be $\{a \in P \mid a \neq 1\}$ . Then every prime is a minimal element of D, and D has no least element.

A least element of a set (if one exists) is automatically unique. (If $m_{1}$ and $m_{2}$ are both least, then $m_{1} \leq m_{2}$ and $m_{2} \leq m_{1}$ , whence equality holds.) In this event, the least element is the only minimal element. But a set can have many minimal elements, as the above example shows. It is also possible for a set to have no minimal elements at all. (What is an example of such a set?)

Similarly an element m of D is a maximal element of D iff there is no x in D with m < x (or equivalently, iff for all x in D, $m \neq x$ ). And m is a greatest (or largest or maximum) element of D iff $x \leq m$ for all x in D. The remarks we have made concerning minimal and least elements carry over to maximal and greatest elements. That is, a greatest element is also maximal. For a linear ordering (on a set that includes D) the two concepts coincide. A set can have only one greatest element. But if a set has no greatest element, it can have many maximal elements (or it might have none).

If R is a partial ordering, then $R^{-1}$ is also a partial ordering (Exercise 2). And for a set D, the minimal elements of D with respect to $R^{-1}$ are exactly the maximal elements with respect to R. When it is necessary to specify the ordering, we can speak of “R-minimal” elements.

Suppose that $<$ is a partial ordering on $A$ and consider a subset $C$ of $A$ . An upper bound of $C$ is an element $b \in A$ such that $x \leq b$ for all $x \in C$ . Here $b$ may or may not belong to $C$ ; if it belongs to $C$ , then it is clearly the greatest element of $C$ . If $b$ is the least element of the set of all upper bounds for $C$ , then $b$ is the least upper bound (or supremum) of $C$ . Lower bound and greatest lower bound (or infimum) are defined analogously.

Example Consider a fixed set S and the partial ordering $\subset_{s}$ on PS. For A and B in PS, the set $\{A, B\}$ has a least upper bound (with respect to $\subset_{s}$ ), namely $A \cup B$ . Similarly $A \cap B$ is the greatest lower bound of $\{A, B\}$ . If $A \subseteq PS$ , then $\bigcup A$ is the least upper bound of A. And $\bigcap A$ (if $A \neq \varnothing$ ) is the greatest lower bound.

Example Next consider the set $\mathbb{Q}$ of rational numbers with its usual linear ordering relation $<$ . The set of positive rational numbers has no upper bounds at all. The set $\{x \in \mathbb{Q} \mid x^2 < 2\}$ has upper bounds in $\mathbb{Q}$ , but no least upper bound in $\mathbb{Q}$ .

Example In the set of positive integers ordered by divisibility, greatest lower bounds are called “greatest common divisors” (g.c.d.’s). And least upper bounds are called “least common multiples” (l.c.m.’s). In this ordering, any finite set has an l.c.m., but infinite sets have no upper bounds. Any nonempty set of positive integers has a g.c.d.

## Exercises

1. Assume that $<_{A}$ and $<_{B}$ are partial orderings on $A$ and $B$ , respectively, and that $f$ is a function from $A$ into $B$ satisfying

$$
x <   _ {A} y \Rightarrow f (x) <   _ {B} f (y)
$$

for all $x$ and $y$ in $A$ .

(a) Can we conclude that $f$ is one-to-one?

(b) Can we conclude that

$$
x <   _ {A} y \Leftrightarrow f (x) <   _ {B} f (y)?
$$

2. Assume that $R$ is a partial ordering. Show that $R^{-1}$ is also a partial ordering.

3. Assume that $S$ is a finite set having $n$ elements. Show that a linear ordering on $S$ contains $\frac{1}{2} n(n - 1)$ pairs.

## WELL ORDERINGS

Definition A well ordering $^{1}$ on A is a linear ordering on A with the further property that every nonempty subset of A has a least element.

For example, we proved in Chapter 4 that the usual ordering on $\omega$ is a well ordering. But the usual ordering on the set Z of integers is not a well ordering; Z has no least element.

Well orderings are significant because they can be used to index constructions that proceed “from the bottom up,” where at every stage in the construction (except the last) there is a unique next step. This idea is made precise in the transfinite recursion theorem, which we will encounter presently.

We can very informally describe what well orderings are like; later we will give exact statements and proofs. Assume that $<$ is a well ordering on $A$ . Then the set $A$ itself, if nonempty, has a least element $t_0$ . And then what is left, $A - \{t_0\}$ , has (if it is nonempty) a least element $t_1$ . Next consider $A - \{t_0, t_1\}$ , and so forth. We obtain

$$
t _ {0} <   t _ {1} <   t _ {2} <   \dots .
$$

There may be still more in $A - \{t_0, t_1, \ldots\}$ , in which case there is a least element $t_\omega$ . And this might continue:

$$
t _ {0} <   t _ {1} <   \dots <   t _ {\omega} <   t _ {\omega + 1} <   \dots <   t _ {\omega \cdot 2} <   t _ {\omega \cdot 2 + 1} <   \dots .
$$

Eventually we use up all the elements of A, and things grind to a halt.

We can use the axiom of choice to obtain another way of characterizing the well orderings.

Theorem 7B Let $<$ be a linear ordering on $A$ . Then it is a well ordering iff there does not exist any function $f: \omega \to A$ with $f(n^{+}) < f(n)$ for every $n \in \omega$ .

A function $f: \omega \to A$ for which $f(n^{+}) < f(n)$ (for all $n \in \omega$ ) is sometimes called a descending chain, but this terminology should not be confused with other uses we make of the word “chain.” The theorem asserts that, for a linear ordering <, it is a well ordering iff there are no descending chains.

Proof If there is a descending chain f, then ran f is a nonempty subset of A. And clearly ran f has no least element; for each element $f(n)$ there is a smaller element $f(n^{+})$ . Hence the existence of a descending chain implies that < is not a well ordering.

Conversely, assume that $<$ is not a well ordering on $A$ , so that some nonempty $B \subseteq A$ lacks a least element. Then $(\forall x \in B)(\exists y \in B)y < x$ . By Exercise 20 of Chapter 6, there is a descending chain $f: \omega \to B$ with $f(n^{+}) < f(n)$ for each $n$ in $\omega$ .

If $<$ is some sort of ordering on $A$ (at least a partial ordering) and $t \in A$ , then the set

$$
\operatorname{seg} t = \{x | x <   t \}
$$

is called the initial segment up to t. (A less ambiguous notation would be $\sec_{<}t$ , but in practice the simpler notation suffices.) For example, $\omega$ was ordered by $\in$ , and consequently we had for $n \in \omega$ ,

$$
\operatorname{seg} n = \{x \mid x \in n \} = n.
$$

Transfinite Induction Principle Assume that $<$ is a well ordering on $A$ . Assume that $B$ is a subset of $A$ with the special property that for every $t$ in $A$ ,

$$
\operatorname{seg} t \subseteq B \Rightarrow t \in B.
$$

Then $B$ coincides with $A$ .

Before proving this, let us define a subset B of A to be a <-inductive subset of A iff it has this special property, i.e., for every t in A,

$$
\operatorname{seg} t \subseteq B \Rightarrow t \in B.
$$

This condition, in words, states that t's membership in B is guaranteed once it is known that all things less than t are already in B. The transfinite induction principle can be restated: If < is a well ordering on A, then any <-inductive subset of A must actually coincide with A.

Proof If B is a proper subset of A, then A - B has a least element m. By the leastness, $y \in B$ for any y < m. But this is to say that $\operatorname{seg} m \subseteq B$ , so by assumption $m \in B$ after all.

The above proof is so short that we might take a second glance at the situation. First take the least element $t_{0}$ of A. Then seg $t_{0} = \varnothing$ , and so automatically seg $t_{0} \subseteq B$ . The assumption on B then tells us that $t_{0} \in B$ . Next we proceed to the least element $t_{1}$ of $A - \{t_{0}\}$ . Then seg $t_{1} = \{t_{0}\} \subseteq B$ , so we obtain $t_{1} \in B$ . And so forth and so forth. But to make the “and so forth” part secure, we have the foregoing actual proof of the principle.

The transfinite induction principle is a generalization of the strong induction principle for $\omega$ , encountered at the end of Chapter 4. The following theorem is somewhat of a converse to transfinite induction. It asserts that the only linear orderings for which the transfinite induction principle is valid are the well orderings. Although we make no later use of this theorem, it is of interest in showing why one might choose to study well orderings.

Theorem 7C Assume that $<$ is a linear ordering on $A$ . Further assume that the only $<$ -inductive subset of $A$ is $A$ itself. That is, assume that for any $B \subseteq A$ satisfying the condition

$$
(\forall t \in A) (\operatorname{seg} t \subseteq B \Rightarrow t \in B),\tag{☆}
$$

we have B = A. Then < is a well ordering on A.

Proof Let C be any subset of A; we will show that either C has a least element or C is empty. We decide (for reasons that may seem mysterious at the moment) to consider the set B of “strict lower bounds” of C:

$$
B = \{t \in A \mid t <   x \text {   for   every   } x \in C \}.
$$

Note that $B \cap C = \emptyset$ , lest we have $t < t$ . We ask ourselves whether condition $(\star)$ holds for $B$ .

Case I Condition (☆) fails. Then there exists some $t \in A$ with seg $t \subseteq B$ but $t \notin B$ . We claim that t is a least element of C. Since $t \notin B$ , there is some $x \in C$ with $x \leq t$ . But x cannot belong to seg t, which is disjoint from C. Thus x = t and $t \in C$ . And t is least in C, since anything smaller than t is in seg t and hence not in C.

Case II Condition (☆) holds. Then by the hypothesis of the theorem, A = B. Consequently in this case C is empty.

Next we turn to the important business of defining a function on a well-ordered structure by transfinite recursion. Assume that $<$ is a well ordering on $A$ . Conceivably we might possess some rule for defining a function value $F(t)$ at $t \in A$ , where the rule requires knowing first all values $F(x)$ for $x < t$ . Then we can start with the least element $t_0$ of $A$ , apply our rule to find $F(t_0)$ , go on the next element, and so forth. That phrase “and so forth” has to cover a great deal of ground. But, because $<$ is a well ordering, after defining $F$ on any proper subset $B$ of $A$ , we always have a unique next element (the least element of $A - B$ ) to which we can apply our rule so as to continue.

Now let us try to make these ideas more concrete. The “rule” of the preceding paragraph might be provided by a function G. Then $F(t)$ for $t \in A$ is to be found by applying G to the values $F(x)$ for x < t:

$$
F (t) = G (F \upharpoonright \operatorname{seg} t).
$$

We will say that $F$ is “ $G$ -constructed” if the above equation holds for every $t \in \operatorname{dom} F$ . For the right side of this equation to succeed, the domain of $G$ must contain all functions of the form $F \upharpoonright \operatorname{seg} t$ . This leads us to define, for a set $B$ , the set $^{<A}B$ of all functions from initial segments of $<$ into $B$ :

$$
{ } ^ { <   A } B = \{ f \mid \text {   for   some   } t \in A , f \text {   is   a   function   from   } \operatorname{seg} t \text {   into   } B \} .
$$

To check that there is indeed such a set, observe that if $f\colon \operatorname{seg} t \to B$ , then $f \subseteq A \times B$ . Hence $^{<A}B$ is obtainable by applying a subset axiom to $\mathcal{P}(A \times B)$ .

Transfinite Recursion Theorem, Preliminary Form Assume that $<$ is a well ordering on $A$ , and that $G: ^{<}A B \to B$ . Then there is a unique function $F: A \to B$ such that for any $t \in A$ ,

$$
F (t) = G (F \upharpoonright \operatorname{seg} t).
$$

Example In the case of the well-ordered set $\omega$ , we have for each $n$ in $\omega$ the equation $\operatorname{seg} n = \{x \mid x \in n\} = n$ . Hence the above theorem asserts the existence of a unique $F: \omega \to B$ satisfying for every $n$ in $\omega$

$$
F (n) = G (F \upharpoonright n).
$$

In particular, we have

$$
\begin{array}{l} F (0) = G (F \upharpoonright 0) = G (\varnothing), \\ F (1) = G (F \upharpoonright 1) = G (\{\langle 0, F (0) \rangle \}), \\ F (2) = G (F \upharpoonright 2) = G (\{\langle 0, F (0) \rangle , \langle 1, F (1) \rangle \}). \end{array}
$$

This can be compared with the recursion theorem of Chapter 4. There is the difference that in Chapter 4 the value of $F(n)$ was constructed by using only the one immediately preceding value of the function. But now in constructing $F(n)$ we can use all of the previous values, which are given to us by $F \upharpoonright n$ . (This alteration is not made solely for reasons of generosity. It is forced on us by the fact that in an arbitrary well ordering, there may not always be an “immediately preceding” element.)

Before proving the transfinite recursion theorem, we want to state it in a stronger form. In our informal comments we spoke of a “rule” for forming $F(t)$ from the restriction $F \upharpoonright$ seg t. We want to be broad-minded and to allow the case in which the rule is not given by a function. We have in mind such rules as

$$
F (t) = \{F (x) \mid x <   t \} = \operatorname{ran} (F \upharpoonright \operatorname{seg} t).
$$

There is no function G such that $G(a) = \text{ran } a$ for every set a; such a function would have to have everything in its domain, but its domain is merely a set. To be sure, for any fixed set B there is indeed a function G with $G(a) = \text{ran } a$ for every $a \in B$ . But our desire is to avoid having to produce in advance the set B.

In terms of proper classes, we can formulate the improved version of transfinite recursion as follows. Let $<$ be a well ordering on $A$ and let $G$ be a “function-class,” i.e., a class of ordered pairs that satisfies the definition of a function except for not being a set. Further suppose that the domain of $G$ includes $^{<A}V$ , where $^{<A}V$ is the class

$\{f \mid \text{for some } t \text{ in } A, f \text{ is a function with dom } f = \text{seg } t\}$ .

Then there exists a unique function $F$ with domain $A$ that is "G-constructed" in the sense that

$$
F (t) = \mathbf {G} (F \upharpoonright \operatorname{seg} t)
$$

for all $t \in A$ . (Here $F$ is a set.)

Because we are working in Zermelo–Fraenkel set theory, we must reword the above formulation of transfinite recursion so as to avoid reference to the class G. Instead we allow ourselves only a formula $\gamma(x, y)$ that defines G:

$$
\mathbf {G} = \{\langle x, y \rangle \mid \gamma (x, y) \}.
$$

Applying this rewording (the standard rewording for these predicaments), we obtain the statement below.

Transfinite Recursion Theorem Schema For any formula $\gamma(x, y)$ the following is a theorem:

Assume that $<$ is a well ordering on a set $A$ . Assume that for any $f$ there is a unique $y$ such that $\gamma(f, y)$ . Then there exists a unique function $F$ with domain $A$ such that

$$
\gamma (F \upharpoonright \operatorname{seg} t, F (t))
$$

for all $t$ in $A$ .

This is a theorem schema; that is, it is an infinite package of theorems, one for each formula $\gamma(x, y)$ . (The formula $\gamma(x, y)$ is allowed to mention other fixed sets in addition to x and y.) We will say that F is $\gamma$ -constructed if the condition $\gamma(F \upharpoonright \text{seg } t, F(t))$ holds for every t in dom F.

Example We obtain one instance of transfinite recursion by taking $\gamma(x, y)$ to be: y = ran x. Now it is automatically true that for any f there is a unique y such that y = ran f. So we are left with the theorem:

Assume that $<$ is a well ordering on $A$ . Then there exists a unique function with domain $A$ such that

$$
F (t) = \operatorname{ran} (F \upharpoonright \sec t)
$$

for all $t$ in $A$ .

This is the instance of transfinite recursion we will need in order to make ordinal numbers.

Example The preliminary form of transfinite recursion is obtained by choosing the formula $\gamma(x, y)$ :

$$
\begin{array}{r c l} \gamma (x, y) & \Leftrightarrow & \text { either } \\ & & \text { or } \end{array}
$$

(i)

(ii)

$$
\begin{array}{l} x \in {} ^ {<   A} B \text {   and   } y = G (x) \\ x \notin {} ^ {<   A} B \text {   and   } y = \varnothing . \end{array}
$$

Then for any $f$ there is a unique $y$ such that $\gamma(f, y)$ . We can conclude from the transfinite recursion theorem that there is a unique function $F$ with domain $A$ that is $\gamma$ -constructed: For $t \in A$ , either (i) ( $F \upharpoonright \operatorname{seg} t$ ) $\in {}^<{}^A B$ and $F(t) = G(F \upharpoonright \text{seg } t)$ or (ii) $(F \upharpoonright \text{seg } t) \notin {}^{<A} B$ and $F(t) = \emptyset$ . Since $G: {}^{<A} B \to B$ , we can see (by transfinite induction) that we have alternative (i) for every $t$ in $A$ . Thus $F$ is $G$ -constructed.

One momentary drawback to the above statement of transfinite recursion is that we are unable to prove it with the axioms now at our disposal. Actually this drawback is shared by a number of other statements that are intuitively true under our informal ideas about sets. For example, we are unable to prove that

$$
\emptyset \cup \mathcal {P} \emptyset \cup \mathcal {P P} \emptyset \cup \mathcal {P P P} \emptyset \cup \dots
$$

is a set. In fact we cannot prove the existence of any inductive set other than $\omega$ . These deficiencies will be eliminated in the next section by the replacement axioms.

## Exercises

4. Let $<$ be the usual ordering on the set $P$ of positive integers. For $n$ in $P$ , let $f(n)$ be the number of distinct prime factors of $n$ . Define the binary relation $R$ on $P$ by

$$
m R n \Leftrightarrow \text { either } f (m) <   f (n) \quad \text { or } [ f (m) = f (n) \& m <   n ].
$$

Show that $R$ is a well ordering on $P$ . Does $\langle P, R \rangle$ resemble any of the pictures in Fig. 45 (p. 185)?

5. Assume that $<$ is a well ordering on $A$ , and that $f: A \to A$ satisfies the condition

$$
x <   y \Rightarrow f (x) <   f (y)
$$

for all $x$ and $y$ in $A$ . Show that $x \leq f(x)$ for all $x$ in $A$ . [Suggestion: Consider $f(f(x))$ .]

6. Assume that S is a subset of the real numbers that is well ordered (under the usual ordering on reals). Show that S is countable. [Suggestion: For each x in S, choose a rational number between x and the next member of S, if any.]

7. Let C be some fixed set. Apply transfinite recursion to $\omega$ (with its usual well ordering), using for $\gamma(x, y)$ the formula

$$
y = C \cup \bigcup \bigcup \operatorname{ran} x.
$$

Let $F$ be the $\gamma$ -constructed function on $\omega$ .

(a) Calculate $F(0), F(1)$ , and $F(2)$ . Make a good guess as to what $F(n)$ is.

(b) Show that if $a \in F(n)$ , then $a \subseteq F(n^{+})$ .

(c) Let $\overline{C} = \bigcup \operatorname{ran} F$ . Show that $\overline{C}$ is a transitive set and that $C \subseteq \overline{C}$ .

(The set $\bar{C}$ is called the transitive closure of $C$ , denoted TC $C$ .)

## REPLACEMENT AXIOMS

If H is a function and A is a set, then $H[A]$ is a set, simply because it is included in ran H. (Lemma 3D guarantees that ran H is a set.) But now consider a “function-class” H, i.e., a class of ordered pairs that satisfies the definition of being a function, except that it may not be a set. Is it still true that $H[A]$ is a set? With the axioms stated thus far, we are unable to prove that it is. (The unprovability of this can actually be proved; we will return to this point in Chapter 9.) But certainly $H[A]$ cannot be too big to be a set, for it is no larger than the set A. So if we adopt the principle that what distinguishes the sets from the proper classes is the property of being limited in size, then it is eminently reasonable to adopt an axiom that, in a way, asserts that $H[A]$ is a set. Now the axiom in Zermelo-Fraenkel set theory cannot legally refer to a class H; it must instead involve a formula $\varphi$ that defines H. (You will recall that there was a similar situation in the case of the subset axioms.) For each formula that might define a function-class, we get an axiom.

Replacement Axioms For any formula $\varphi(x, y)$ not containing the letter $B$ , the following is an axiom:

$$
\begin{array}{r l} \forall A [ (\forall x \in A)   \forall y _ {1}   \forall y _ {2} (\varphi (x, y _ {1})   \&   \varphi (x, y _ {2}) & \Rightarrow \quad y _ {1} = y _ {2}) \\ \Rightarrow \exists B   \forall y (y \in B \Leftrightarrow (\exists x \in A)   \varphi (x, y)) ]. \end{array}
$$

Here the formula $\varphi(x,y)$ is permitted to name sets other than x and y; we could have emphasized this fact by writing $\varphi(x,y,t_{1},\ldots,t_{k})$ and inserting the phrase “ $\forall t_{1}\cdots\forall t_{k}$ ” at the beginning of the axiom. But $\varphi(x,y)$ must not mention the set B whose existence is being asserted by the axiom.

To translate the replacement axioms into words, define the class

$$
\mathsf {H} = \{\langle x, y \rangle \mid x \in A \& \varphi (x, y) \}.
$$

Then the hypothesis of the axiom,

$$
(\forall x \in A) \forall y _ {1} \forall y _ {2} (\varphi (x, y _ {1}) \& \varphi (x, y _ {2}) \Rightarrow y _ {1} = y _ {2}),
$$

asserts that H is a function-class. And the second line,

$$
\exists B \forall y (y \in B \Leftrightarrow (\exists x \in A) \varphi (x, y)),
$$

asserts that if we let

$$
B = \{y \mid (\exists x \in A)   \varphi (x, y) \} = \mathsf {H} [ [ A ] ],
$$

then $B$ is a set. (It then follows that $\mathsf{H}$ , being included in $A \times B$ , is also a set.)

An alternative way of translating replacement into words is as follows. Read $\varphi(x, y)$ as “x nominates y.” Then the hypothesis of the axiom says, “Each member of A nominates at most one object.” And the conclusion says, “The collection of all nominees is a set.”

The name “replacement” reflects the idea of replacing each x in the set A by its nominee (if any) to obtain the set B.

Example If A is a set, then $\{Pa \mid a \in A\}$ is also a set, by Exercise 10 of Chapter 2. But we now have an easy proof of this fact. Take $\varphi(x, y)$ to be $y = P x$ . That is, let each x nominate its own power set. Then replacement tells us that the collection of all power sets of members of A forms a set.

Example Let S be any set. Then replacement tells us that

$$
\{\text { card } x \mid x \in S \}
$$

is a set. We take the formula $\varphi(x, y)$ to be $y = \text{card } x$ .

Proof of the Transfinite Recursion Theorem The proof is similar, in its general outline, to the proof of the recursion theorem on $\omega$ . Again we construct the desired function F as the union of many approximating functions. For t in A, say that a function v is $\gamma$ -constructed up to t iff dom $v = \{x \mid x \leq t\}$ and for any x in dom v,

$$
\gamma (v \upharpoonright \operatorname{seg} x, v (x)).
$$

1. First we claim that if $t_1 \leq t_2$ , $v_1$ is $\gamma$ -constructed up to $t_1$ and $v_2$ is $\gamma$ -constructed up to $t_2$ , then $v_1(x) = v_2(x)$ for all $x \leq t_1$ . Should this fail, there is a least $x \leq t_1$ with $v_1(x) \neq v_2(x)$ . By the leastness of $x$ , we have $v_1 \upharpoonright \operatorname{seg} x = v_2 \upharpoonright \operatorname{seg} x$ . Also we have

$$
\gamma (v _ {1} \upharpoonright \operatorname{seg} x, v _ {1} (x)) \quad \text { and } \quad \gamma (v _ {2} \upharpoonright \operatorname{seg} x, v _ {2} (x)),
$$

whence by our assumption on $\gamma$ we conclude that $v_{1}(x) = v_{2}(x)$ after all. This establishes the claim.

In particular, by taking $t_{1}=t_{2}$ we see that for any $t\in A$ there is at most one function v that is $\gamma$ -constructed up to t. We next want to form the set K of all functions v that are, for some t in A, $\gamma$ -constructed up to t:

$$
\mathscr {K} = \{v \mid (\exists t \in A) v \text {   is   a   function   } \gamma \text {-constructed   up   to   } t \}.
$$

$\mathcal{K}$ is provided by a replacement axiom. Take for $\varphi(t, v)$ the formula

v is a function that is $\gamma$ -constructed up to t.

We have shown that

$$
t \in A \& \varphi (t, v _ {1}) \& \varphi (t, v _ {2}) \Rightarrow v _ {1} = v _ {2}.
$$

Hence by replacement there is a set $\mathcal{K}$ such that for any $v$ ,

$$
\begin{array}{r c l} v \in \mathcal {K} & \Leftrightarrow & (\exists t \in A)   \varphi (t, v) \\ & \Leftrightarrow & (\exists t \in A)   v \text {   is   } \gamma \text {-constructed   up   to   } t. \end{array}
$$

Now let $F$ be $\bigcup\mathcal{K}$ , the union of all the $v$ 's. Thus

$$
\langle x, y \rangle \in F \Leftrightarrow v (x) = y \text {   for   some   } v \text {   in   } \mathscr {K}.
$$

First observe that $F$ is a function. For suppose that $\langle x, y_1 \rangle$ and $\langle x, y_2 \rangle$ belong to $F$ . By $(\star)$ there exist $v_1, t_1, v_2$ , and $t_2$ such that $v_i(x) = y_i$ and $v_i$ is $\gamma$ -constructed up to $t_i$ for $i = 1, 2$ . Either $x \leq t_1 \leq t_2$ or $x \leq t_2 \leq t_1$ , and in either event we have by our earlier claim $y_1 = v_1(x) = v_2(x) = y_2$ .

2. Next we claim that for any $x \in dom F$ , $\gamma(F \upharpoonright \text{seg } x, F(x))$ . For if $x \in dom F$ , there exists v in K with $x \in dom v$ . Then we have

$$
\begin{array}{l l} \gamma (v \upharpoonright \text {seg} x, v (x)) & \text {since} v \in \mathcal {K}, \\ v \upharpoonright \text {seg} x = F \upharpoonright \text {seg} x & \text {by} (\star) \text {and part 1}, \\ v (x) = F (x) & \text {by} (\star), \end{array}
$$

from which we conclude that $\gamma(F \upharpoonright \operatorname{seg} x, F(x))$ .

3. We now claim that $\operatorname{dom} F = A$ . If this fails, then there is a least $t \in A - \operatorname{dom} F$ . Then $\operatorname{seg} t \subseteq \operatorname{dom} F$ ; in fact $\operatorname{seg} t = \operatorname{dom} F$ . Take the unique $y$ such that $\gamma(F, y)$ and let

$$
v = F \cup \{\langle t, y \rangle \}.
$$

We want to show that v is $\gamma$ -constructed up to t. Clearly v is a function and dom $v = \{x \mid x \leq t\}$ . For any x < t we have $v \upharpoonright \operatorname{seg} x = F \upharpoonright \operatorname{seg} x$ and $v(x) = F(x)$ , and so by part 2 we conclude that $\gamma(v \upharpoonright \operatorname{seg} x, v(x))$ . For the case x = t we have $v \upharpoonright \operatorname{seg} t = F$ and $v(t) = y$ , and so by our choice of y we obtain $\gamma(v) \upharpoonright \operatorname{seg} t, v(t)$ . Hence v is $\gamma$ -constructed up to t. But this implies that $t \in \operatorname{dom} F$ after all.

4. Finally we claim that $F$ is unique. For suppose that $F_{1}$ and $F_{2}$ both satisfy the conclusion of the theorem. We can apply transfinite induction; let $B$ be the set on which $F_{1}$ and $F_{2}$ agree:

$$
B = \{t \in A \mid F _ {1} (t) = F _ {2} (t) \}.
$$

It suffices to show that for any $t \in A$ ,

$$
\operatorname{seg} t \subseteq B \Rightarrow t \in B.
$$

But this is easy. If $\operatorname{seg} t \subseteq B$ , then we have $F_{1} \upharpoonright \operatorname{seg} t = F_{2} \upharpoonright \operatorname{seg} t$ . Also we have

$$
\gamma (F _ {1} \upharpoonright \operatorname{seg} t, F _ {1} (t)) \quad \text { and } \quad \gamma (F _ {2} \upharpoonright \operatorname{seg} t, F _ {2} (t)),
$$

whence by our assumption on $\gamma$ we conclude that $F_{1}(t) = F_{2}(t)$ . Hence $t \in B$ and we are done.

## Exercises

8. Show that the subset axioms are provable from the other axioms.

9. Show that the pairing axiom is provable from the other axioms.

## EPSILON-IMAGES $^{2}$

Our first application of transfinite recursion will be to the construction of the ordinal numbers. Assume that $<$ is a well ordering on $A$ and take for $\gamma(x, y)$ the formula: $y = \operatorname{ran} x$ . The transfinite recursion theorem then presents us with a unique function $E$ with domain $A$ such that for any $t \in A$ :

$$
\begin{array}{r l} E (t) & = \operatorname{ran} (E \upharpoonright \operatorname{seg} t) \\ & = E [   [ \operatorname{seg} t ]   ] \\ & = \{E (x) \mid x <   t \}. \end{array}
$$

Let $\alpha = \operatorname{ran} E$ ; we will call $\alpha$ the $\in$ -image of the well-ordered structure $\langle A, < \rangle$ . (Later $\alpha$ will also be called an ordinal number, but we want to postpone introducing that terminology.)

Example To get some idea of what the $\in$ -image might look like, take the three-element set $A = \{r, s, t\}$ , where $r < s < t$ . Then we calculate

$$
\begin{array}{l} E (r) = \{E (x) \mid x <   r \} = \varnothing , \\ E (s) = \{E (x) \mid x <   s \} = \{E (r) \} = \{\varnothing \}, \\ E (t) = \{E (x) \mid x <   t \} = \{E (r), E (s) \} = \{\varnothing , \{\varnothing \} \}. \end{array}
$$

Thus $E(r) = 0$ , $E(s) = 1$ , $E(t) = 2$ , and the $\in$ -image $\alpha$ of $\langle A, < \rangle$ is 3. You are invited to contemplate whether natural numbers will always appear in $\alpha$ like this.

In the above example, $\alpha$ was a set equinumerous with A. Moreover, while < was a well ordering on A, the membership relation

$$
\epsilon_ {\alpha} = \{\langle x, y \rangle \in \alpha \times \alpha | x \in y \}
$$

provided a well ordering on $\alpha$ . We will show that this always happens, whence the name “ $\in$ -image.”

Theorem 7D Let $<$ be a well ordering on $A$ and let $E$ and $\alpha$ be as described as above.

(a) $E(t) \notin E(t)$ for any $t \in A$ .

(b) $E$ maps $A$ one-to-one onto $\alpha$ .

(c) For any $s$ and $t$ in $A$ ,

$$
s <   t \quad \text { iff } \quad E (s) \in E (t).
$$

(d) $\alpha$ is a transitive set.

Proof We prove that $E(t) \notin E(t)$ by the “least counterexample” method. That is, let S be the set of counterexamples:

$$
S = \{t \in A \mid E (t) \in E (t) \}.
$$

We hope that $S$ is empty. But if not, then there is a least $\hat{t} \in S$ . Since $E(\hat{t}) \in E(\hat{t})$ , there is (by the definition of $E(\hat{t})$ ) some $s < \hat{t}$ with $E(\hat{t}) = E(s)$ . But then $E(s) \in E(s)$ , contradicting the leastness of $\hat{t}$ . Hence $S = \emptyset$ , which proves part (a).

For part (b), it is obvious that $E$ maps $A$ onto $\alpha$ ; we must prove that $E$ is one-to-one. If $s$ and $t$ are distinct members of $A$ , then one is smaller than the other; assume $s < t$ . Then $E(s) \in E(t)$ , but, by part (a), $E(t) \notin E(t)$ . Hence $E(s) \neq E(t)$ .

In part (c) we have

$$
s <   t \Rightarrow E (s) \in E (t)
$$

by definition. Conversely if $E(s) \in E(t)$ , then (by the definition of $E(t)$ ) there is some x < t with $E(s) = E(x)$ . Since E is one-to-one, we must have s = x and hence s < t.

Finally for part (d) it is easy to see that $\alpha$ is a transitive set. If $u \in E(t) \in \alpha$ , then there is some $x < t$ with $u = E(x)$ ; consequently $u \in \alpha$ .

Define the binary relation on $\alpha$ :

$$
\epsilon_ {\alpha} = \{\langle x, y \rangle \in \alpha \times \alpha | x \in y \}.
$$

Under the assumptions of the preceding theorem, $\epsilon_{\alpha}$ is a well ordering on $\alpha$ . We will postpone verifying this fact until we can do so in a more general setting (see Corollary 7H). Since $\alpha$ is a transitive set, we can characterize $\epsilon_{\alpha}$ by the condition

$$
x \in_ {\alpha} y \Leftrightarrow x \in y \in \alpha .
$$

## Exercises

10. For any set $S$ , we can define the relation $\epsilon_{s}$ by the equation:

$$
\epsilon_ {s} = \{\langle x, y \rangle \in S \times S \mid x \in y \}
$$

(a) Show that for any natural number $n$ , the $\epsilon$ -image of $\langle n, \epsilon_n \rangle$ is $n$ .

(b) Find the $\epsilon$ -image of $\langle \omega, \epsilon_{\omega} \rangle$ .

11. (a) Although the set $\mathbb{Z}$ of integers is not well ordered by its normal ordering, show that the ordering

$$
0, 1, 2, \dots , - 1, - 2, - 3, \dots
$$

is a well ordering on $\mathbb{Z}$ .

(b) Suppose that we define the usual function $E$ on $\mathbb{Z}$ , using the well ordering of part (a). Calculate $E(3), E(-1)$ , and $E(-2)$ . Describe ran $E$ .

## ISOMORPHISMS

Theorem 7D told us that a well-ordered structure $\langle A, <\rangle$ looks a great deal like its $\in$ -image $\langle \alpha, \epsilon_{\alpha} \rangle$ . We had a one-to-one correspondence $E$ between $A$ and $\alpha$ with the order-preserving property:

$$
s <   t \quad \text { iff } \quad E (s) \in E (t)
$$

for s and t in A. In formalizing this concept of “looking alike,” we need not restrict attention to well orderings. Instead we might as well formulate our definition in broader terms.

Definition Consider structures $\langle A, R \rangle$ and $\langle B, S \rangle$ . An isomorphism from $\langle A, R \rangle$ onto $\langle B, S \rangle$ is a one-to-one function $f$ from $A$ onto $B$ such that

$$
x R y \quad \text { iff } \quad f (x) S f (y)
$$

for $x$ and $y$ in $A$ . If such an isomorphism exists, then we say that $\langle A, R \rangle$ is isomorphic to $\langle B, S \rangle$ , written: $\langle A, R \rangle \cong \langle B, S \rangle$ .

Example Let $<$ be a well ordering on $A$ and let $\alpha$ be the $\in$ -image of $\langle A, <\rangle$ . Then Theorem 7D states that $\langle A, <\rangle$ is isomorphic to $\langle \alpha, \epsilon_{\alpha} \rangle$ , and that $E$ is an isomorphism.

Example Isomorphic structures really do look alike. We can draw pictures (at least in the simple cases) as in Figs. 43 and 44. Figure 45 consists of pictures of four well-ordered structures. Figure 45a shows a well ordering on $\{r, s, t\}$ , and Fig. 45b shows a well ordering on $\{x, y, z\}$ . The two structures are isomorphic, and the two pictures are obviously very much alike. Figures 45c and 45d provide pictures of infinite structures. Figure 45c

<3, 1>

![](images/03b89fb3878619a2182f6f9c48cb634335c2de02df8b20592e2deac4a04d8323.jpg)  
Fig. 45. Four well orderings, of which two are isomorphic.

shows the usual ordering on $\omega$ . Figure 45d is a picture of $\omega \times \omega$ with the “lexicographic” (dictionary) ordering

$$
\langle m, n \rangle <   _ {\mathrm{L}} \langle p, q \rangle \quad \text { iff } \quad m \in p \quad \text { or } \quad (m = p \& n \in q).
$$

Although $\omega$ is equinumerous to $\omega \times \omega$ , the pictures do not look alike. For example, in Fig. 45c the set seg n is always finite, whereas in Fig. 45d the set $\text{seg}\langle m, n\rangle$ is infinite for $m \neq 0$ . And the two structures are not isomorphic.

Actually we have used the word “isomorphic” before, e.g., in Theorem 4H. Both there and here we are using special cases of the general concept of isomorphism of structures. In Theorem 4H we had “structures” $\langle N, S, e \rangle$ consisting of a set N together with a function $S: N \to N$ and an element $e \in N$ . Now we have structures $\langle A, R \rangle$ , where R is a binary relation on A. We will have no need here for greater generality, but you are nonetheless invited to devise general concepts of structure and isomorphism.

We have the easy theorem stating that isomorphism is an “equivalence concept.” That is, it obeys laws of reflexivity, symmetry, and transitivity.

Theorem 7E Let $\langle A, R\rangle$ , $\langle B, S\rangle$ , and $\langle C, T\rangle$ be any structures. Then

$$
\langle A, R \rangle \cong \langle A, R \rangle ,
$$

$$
\langle A, R \rangle \cong \langle B, S \rangle \Rightarrow \langle B, S \rangle \cong \langle A, R \rangle ,
$$

$$
\langle A, R \rangle \cong \langle B, S \rangle \cong \langle C, T \rangle \Rightarrow \langle A, R \rangle \cong \langle C, T \rangle .
$$

Proof For the first of these we can use the identity function on A; it is an isomorphism of $\langle A, R \rangle$ onto itself. To prove the second we take the inverse of the given isomorphism; to prove the third we take the composition of the two given isomorphisms.

If two structures are isomorphic, then for any statement that is true of one, there is a corresponding statement that is true of the other. This is because the structures look exactly alike. But to nail down this general principle in precise terms, we would have to say formally what we meant by “true statement” and “corresponding statement.” This would lead us away from set theory into logic. Instead we will just list (in Theorem 7G) some particular instances of the general principle.

Lemma 7F Assume that $f$ is a one-to-one function from $A$ into $B$ , and that $<_{B}$ is a partial ordering on $B$ . Define the binary relation $<_{A}$ on $A$ by

$$
x <   _ {A} y \quad \text { iff } \quad f (x) <   _ {B} f (y)
$$

for $x$ and $y$ in $A$ .

(a) The relation $<_{A}$ is a partial ordering on $A$ .

(b) If $<_{B}$ is a linear ordering on $B$ , then $<_{A}$ is a linear ordering on $A$ .

(c) If $<_{B}$ is a well ordering on $B$ , then $<_{A}$ is a well ordering on $A$ .

Proof The proof is straightforward and is left, for the most part, to the exercises. We will give details here for only the following part: If $<_{B}$ is a well ordering on $B$ , then any nonempty subset $S$ of $A$ has a least (with respect to $<_{A}$ ) element. First note that $f[S]$ is a nonempty subset of $B$ . Hence it has a least element, which must be $f(m)$ for some unique $m \in S$ . We claim that $m$ is least in $S$ . Let $x$ be any other member of $S$ . Then $f(x) \in f[S]$ , and by the leastness of $f(m)$ we have $f(m) \leq_{B} f(x)$ . In fact, $f(m) <_{B} f(x)$ since $f$ is one-to-one. Hence $m <_{A} x$ , which shows that $m$ is indeed least in $S$ .

Theorem 7G Assume that structures $\langle A, <_{A}\rangle$ and $\langle B, <_{B}\rangle$ are isomorphic. If one is a partially (or linearly or well) ordered structure, so also is the other.

Proof Suppose that one is a partially ordered structure; by symmetry we may suppose that it is $\langle B, <_{B} \rangle$ . We are given an isomorphism $f$ of $\langle A, <_{A} \rangle$ onto $\langle B, <_{B} \rangle$ . Thus

$$
x <   _ {A} y \quad \text { iff } \quad f (x) <   _ {B} f (y)
$$

for $x$ and $y$ in $A$ . Hence we can apply the above lemma.

Theorem 7D told us that well orderings were isomorphic to their $\epsilon$ -images. In light of the above theorem, we can now conclude that the $\epsilon$ -images are well ordered by epsilon.

Corollary 7H Assume that $<$ is a well ordering on $A$ and let $\alpha$ be the $\in$ -image of $\langle A, <\rangle$ . Then $\alpha$ is a transitive set and $\epsilon_{\alpha}$ is a well ordering on $\alpha$ .

## Exercises

12. Complete the proof of Lemma 7F.

13. Assume that two well-ordered structures are isomorphic. Show that there can be only one isomorphism from the first onto the second.

14. Assume that $\langle A, <\rangle$ is a partially ordered structure. Define the function F on A by the equation

$$
F (a) = \{x \in A \mid x \leq a \},
$$

and let $S = \operatorname{ran} F$ . Show that $F$ is an isomorphism from $\langle A, < \rangle$ onto $\langle S, \subset_S \rangle$ .

## ORDINAL NUMBERS

It will be extremely useful in our discussion of well orderings if we can assign a “number” to each well-ordered structure that measures its “length.” Two well-ordered structures should receive the same number iff they look alike, i.e., iff they are isomorphic. The situation is much like that in Chapter 6, where we assigned cardinal numbers to sets so as to measure their size. Two sets received the same cardinal number iff they were equinumerous. The key to the present situation lies in the following theorem.

Theorem 7I Two well-ordered structures are isomorphic iff they have the same $\in$ -image. That is, if $<_{1}$ and $<_{2}$ are well orderings on $A_{1}$ and $A_{2}$ , respectively, then $\langle A_{1}, <_{1} \rangle \cong \langle A_{2}, <_{2} \rangle$ iff the $\in$ -image of $\langle A_{1}, <_{1} \rangle$ is the same as the $\in$ -image of $\langle A_{2}, <_{2} \rangle$ .

Proof In one direction, this follows at once from the fact that well-ordered structures are isomorphic to their $\in$ -images. That is, if $\langle A_1, <_1 \rangle$ and $\langle A_2, <_2 \rangle$ have the same $\in$ -image $\alpha$ , then

$$
\langle A _ {1}, <   _ {1} \rangle \cong \langle \alpha , \epsilon_ {\alpha} \rangle \cong \langle A _ {2}, <   _ {2} \rangle .
$$

For the other direction, assume that $f$ is an isomorphism from $\langle A_1, <_1 \rangle$ onto $\langle A_2, <_2 \rangle$ . Let $E_1: A_1 \to \alpha_1$ and $E_2: A_2 \to \alpha_2$ be the usual isomorphisms of the well orderings onto their $\in$ -images:

$$
E _ {1} (s) = \left\{E _ {1} (x) \mid x <   _ {1} s \right\} \quad \text { and } \quad E _ {2} (t) = \left\{E _ {2} (y) \mid y <   _ {2} t \right\}.
$$

Then we can use transfinite induction to show that $E_1(s) = E_2(f(s))$ for all $s \in A_1$ . For let $B$ be the set on which this equation holds:

$$
B = \{s \in A _ {1} \mid E _ {1} (s) = E _ {2} (f (s)) \}.
$$

Suppose that $\operatorname{seg} s \subseteq B$ . Then we calculate

$$
\begin{array}{l l} E _ {1} (s) = \{E _ {1} (x) \mid x <   _ {1} s \} & \text { by   definition } \\ = \{E _ {2} (f (x)) \mid x <   _ {1} s \} & \text { since   seg   } s \subseteq B \\ = \{E _ {2} (y) \mid y <   _ {2} f (s) \} & \text {(see below)} \\ = E _ {2} (f (s)). \end{array}
$$

The third line on this calculation requires some thought. Clearly

$$
\{E _ {2} (f (x)) \mid x <   _ {1} s \} \subseteq \{E _ {2} (y) \mid y <   _ {2} f (s) \}
$$

because we can take $y = f(x)$ . Conversely, the other inclusion holds because $f$ maps onto $A_2$ and therefore any $y$ less than $f(s)$ must equal $f(x)$ for some (unique) $x$ less than $s$ .

Thus if $\operatorname{seg} s \subseteq B$ , then $E_1(s) = E_2(f(s))$ and so $s \in B$ . By the transfinite induction principle, $B = A_1$ , i.e.,

$$
E _ {1} (s) = E _ {2} (f (s))
$$

for all $s \in A_1$ . Consequently,

$$
\begin{array}{l l} \alpha_ {1} = \left\{E _ {1} (s) \mid s \in A _ {1} \right\} \\ = \left\{E _ {2} (f (s)) \mid s \in A _ {1} \right\} \\ = \left\{E _ {2} (t) \mid t \in A _ {2} \right\} & \text { since } f \text { maps   onto } A _ {2} \\ = \alpha_ {2}. \end{array}
$$

Thus the $\in$ -images coincide.

The solution to our problem of how to assign “numbers” to well orderings is provided by the foregoing theorem. We just use $\epsilon$ -images.

Definition Let $<$ be a well ordering on $A$ . The ordinal number of $\langle A, < \rangle$ is its $\in$ -image. An ordinal number is a set that is the ordinal number of some well-ordered structure.

(More generally, we could seek to define an “order type” ot $\langle A, R \rangle$ whenever R was a partial ordering on A. The order type should measure the “shape” of R, in the sense that

$$
\operatorname{ot} \langle A, R \rangle = \operatorname{ot} \langle B, S \rangle \quad \text { iff } \quad \langle A, R \rangle \cong \langle B, S \rangle .
$$

This can be done; see Exercise 32. But the methods that are required are quite unlike the methods used for ordinal numbers.)

We can generate examples of ordinal numbers by calculating $\epsilon$ -images. The example preceding Theorem 7D shows that 3 is an ordinal number. And study of Fig. 45c will show that $\omega$ is an ordinal number. More examples will appear presently. First we need some additional information about well orderings.

If $<$ is any ordering on $A$ and $C$ is a subset of $A$ , then the elements of $C$ are, of course, still ordered by $<$ . Now it is not strictly true that $<$ is an ordering on $C$ , because (if $C \neq A$ ) $<$ is not a binary relation on $C$ . But $< \cap (C \times C)$ is an ordering on $C$ . This notation is excessively cumbersome for the simplicity of the ideas involved. And so we define

$$
\langle C, <   ^ {\circ} \rangle = \langle C, <   \cap (C \times C) \rangle .
$$

The symbol $^{\circ}$ reminds us that the relation $<$ can be cut down to fit the set $C$ . In particular, if $C = \text{seg } c$ , then we have the ordered structure $\langle \text{seg } c, <^{\circ} \rangle$ .

Theorem 7J Assume that $<$ is a partial ordering on $A$ , and that $C \subseteq A$ . Then $<^{\circ}$ is a partial ordering on $C$ . This continues to hold with "partial" replaced by "linear" or "well."

Proof This is an immediate consequence of Lemma 7F, wherein we take $f$ to be the identity function on $C$ .

The following theorem is a sort of trichotomy law for well-ordered structures.

Theorem 7K For any two well-ordered structures, either they are isomorphic or one is isomorphic to a segment of the other. More precisely, let $<_{A}$ and $<_{B}$ be well orderings on $A$ and $B$ . Then one of the following

alternatives holds:

$$
\begin{array}{l l} \langle A, <   _ {A} \rangle \cong \langle B, <   _ {B} \rangle , \\ \langle A, <   _ {A} \rangle \cong \langle \operatorname{seg} b, <   _ {B} ^ {\circ} \rangle & \text { for   some } \quad b \in B, \\ \langle \operatorname{seg} a, <   _ {A} ^ {\circ} \rangle \cong \langle B, <   _ {B} \rangle & \text { for   some } \quad a \in A. \end{array}
$$

Proof The idea is to start pairing elements of A with elements of B in the natural way: We pair the least elements of the two sets, then the next smallest, and so forth. Eventually we run out of elements on one side or the other. If the two sets run out simultaneously, then $\langle A, <_{A}\rangle \cong \langle B, <_{B}\rangle$ . Otherwise one set runs out first; in this case it is isomorphic to a segment of the other.

The pairing is obtained by transfinite recursion. Let e be some extraneous object belonging neither to A nor to B. By transfinite recursion there is a unique function $F: A \to B \cup \{e\}$ such that for each $t \in A$ ,

$$
F (t) = \left\{ \begin{array}{l l} \text { the   least   element   of } B - F [ \text { seg } t ] & \quad \text { if   any }, \\ e & \quad \text { if } B - F [ \text { seg } t ] \text { is   empty }. \end{array} \right.
$$

Case I $e \in \operatorname{ran} F$ . Let $a$ be the least element of $A$ for which $F(a) = e$ . We claim that $F \upharpoonright \operatorname{seg} a$ is an isomorphism from $\langle \operatorname{seg} a, <_{A}^{\circ} \rangle$ onto $\langle B, <_{B} \rangle$ . Let $F^{\circ} = F \upharpoonright \operatorname{seg} a$ .

Clearly $F^{\circ}$ : $\operatorname{seg} a \to B$ , and its range is all of $B$ since $B - F[\operatorname{seg} a] = \emptyset$ . We have

$$
\begin{array}{r c l} x \leq_ {A} y <   _ {A} a & \Rightarrow & F [   [ \text { seg } x ]   ] \subseteq F [   [ \text { seg } y ]   ] \\ & \Rightarrow & B - F [   [ \text { seg } y ]   ] \subseteq B - F [   [ \text { seg } x ]   ] \\ & \Rightarrow & F (x) \leq_ {B} F (y). \end{array}
$$

Furthermore if $x < _A y < _A a$ then $F(x) \neq F(y)$ , because $F(x) \in F[\text{seg } y]$ but by construction $F(y) \notin F[\text{seg } y]$ . Therefore $F^\circ$ is one-to-one, and in fact

$$
x <   _ {A} y <   _ {A} a \Rightarrow F (x) <   _ {B} F (y).
$$

Consequently, $F^{\circ}$ preserves order, since

$$
\begin{array}{r c l} F (x) <   _ {B} F (y) & \Rightarrow & F (y) \not \leq_ {B} F (x) \\ & \Rightarrow & y \not \leq_ {A} x \\ & \Rightarrow & x <   _ {A} y. \end{array}
$$

Thus $F^{\circ}$ is an isomorphism as claimed.

Case II ran $F = B$ . Then $F: A \to B$ , and just as in Case I (but without the $a$ ) $F$ is one-to-one and preserves order. Thus $F$ is an isomorphism from $\langle A, <_{A} \rangle$ onto $\langle B, <_{B} \rangle$ .

Case III Otherwise ran $F$ is a proper subset of $B$ . Let $b$ be the least element of $B - \operatorname{ran} F$ . We claim that $\operatorname{ran} F = \operatorname{seg} b$ . By the leastness of $b$ , we have $\operatorname{seg} b \subseteq \operatorname{ran} F$ . Conversely, we cannot have $b < _B F(x)$ for any $x$ , because $F(x)$ is least in $B - F[\operatorname{seg} x]$ , a set to which $b$ belongs. Hence ran $F = \operatorname{seg} b$ .

As in Cases I and II, $F$ is one-to-one and preserves order. Hence $F$ is an isomorphism from $\langle A, <_{A} \rangle$ onto $\langle \text{seg } b, <_{B}^{\circ} \rangle$ .

We now return to the study of ordinal numbers. The next theorem will show that any ordinal number is its own $\in$ -image. To extract the maximum of information from the proof, the following definition will help.

Definition A set $A$ is well ordered by epsilon iff the relation

$$
\in_ {A} = \{\langle x, y \rangle \in A \times A | x \in y \}
$$

is a well ordering on $A$ .

We have shown that any ordinal number is a transitive set that is well ordered by epsilon (Corollary 7H). The converse is also true; the ordinal numbers are exactly the transitive sets that are well ordered by epsilon:

Theorem 7L Let $\alpha$ be any transitive set that is well ordered by epsilon. Then $\alpha$ is an ordinal number; in fact $\alpha$ is the $\epsilon$ -image of $\langle \alpha, \epsilon_{\alpha} \rangle$ .

Proof Let E be the usual function from $\alpha$ onto its $\in$ -image. We can use transfinite induction to show that E is just the identity function on $\alpha$ . Note that for $t \in \alpha$ ,

$$
x \in t \quad \Leftrightarrow \quad x \in_ {\alpha} t
$$

because $\alpha$ is a transitive set. As a consequence we have $\operatorname{seg} t = t$ .

If the equation $E(x) = x$ holds for all $x$ in $\sec t$ , then

$$
\begin{array}{r l} E (t) & = \left\{E (x) \mid x \in_ {\alpha} t \right\} \\ & = \left\{x \mid x \in_ {\alpha} t \right\} \\ & = \operatorname{seg} t \\ & = t. \end{array}
$$

Hence by transfinite induction, $E$ is the identity function on $\alpha$ , so the $\epsilon$ -image of $\langle \alpha, \in_{\alpha} \rangle$ is just $\alpha$ itself.

The class of all ordinal numbers is (as we will prove shortly) too large to be a set. But except for not being a set, it has many of the properties of the ordinal numbers themselves. The next theorem shows that the class of all ordinal numbers is a transitive class well ordered by epsilon.

Theorem 7M The following are valid for any ordinal numbers $\alpha$ , $\beta$ , and $\gamma$ .

(a) (transitive class) Any member of $\alpha$ is itself an ordinal number.

(b) (transitivity) $\alpha \in \beta \in \gamma \Rightarrow \alpha \in \gamma$ .

(c) (irreflexivity) $\alpha \notin \alpha$ .

(d) (trichotomy) Exactly one of the alternatives,

$$
\alpha \in \beta , \quad \alpha = \beta , \quad \beta \in \alpha ,
$$

holds.

(e) Any nonempty set $S$ of ordinal numbers has a least element $\mu$ (i.e., $\mu \in \alpha$ for every $\alpha \in S$ ).

Proof For part (a), consider any $x$ in $\alpha$ . Now $\alpha$ is the $\in$ -image of some well-ordered structure $\langle A, <\rangle$ . So $x = E(t)$ where $E$ is the usual isomorphism and $t$ is some member of $A$ . We will prove that $x$ is an ordinal by showing that it is the $\in$ -image of $\langle \text{seg } t, <^{\circ}\rangle$ . By Theorem 7J the restriction $<^{\circ}$ is a well ordering on $\text{seg } t$ . The $\in$ -image of $\langle \text{seg } t, <^{\circ}\rangle$ is easily seen to be $E[\text{seg } t]$ , but this is just $E(t)$ , which is $x$ . Hence $x$ is an ordinal.

Part (b) is true because the ordinal $\gamma$ is a transitive set.

Part (c) follows from Theorem 7D(a). If $\alpha \in \alpha$ , then $\alpha = E(t)$ for some $t$ (in the notation used above in proving part (a)). But then $E(t) \in E(t)$ , which contradicts Theorem 7D(a).

In trichotomy, the “at most one” part follows from transitivity and irreflexivity (as in Theorem 7A). The “at least one” half is a consequence of Theorem 7K, which tells us that either $\langle\alpha,\in_{\alpha}\rangle$ and $\langle\beta,\in_{\beta}\rangle$ are isomorphic, or else one is isomorphic to a segment of the other.

Case I $\langle \alpha, \epsilon_{\alpha} \rangle \cong \langle \beta, \epsilon_{\beta} \rangle$ . Then both have the same $\epsilon$ -image, by Theorem 7I. But ordinals are their own $\epsilon$ -images by Theorem 7L, so $\alpha = \beta$ .

Case II By symmetry we may suppose that $\langle \alpha, \epsilon_{\alpha} \rangle$ is isomorphic to $\langle \text{seg } \delta, \epsilon_{\beta}^{\circ} \rangle$ , where $\delta \in \beta$ . But then $\delta$ is an ordinal, $\text{seg } \delta = \delta$ , and $\epsilon_{\beta}^{\circ} = \epsilon_{\delta}$ . Thus we have

$$
\langle \alpha , \in_ {\alpha} \rangle \cong \langle \delta , \in_ {\delta} \rangle .
$$

Now by Case I, $\alpha = \delta$ . Hence $\alpha \in \beta$ .

For part (e), first consider some arbitrary $\beta \in S$ . If $\beta \cap S = \emptyset$ , then we claim that $\beta$ is least in $S$ . This is because

$$
\alpha \in S \Rightarrow \alpha \notin \beta \Rightarrow \beta \subseteq \alpha
$$

by trichotomy. There remains the possibility that $\beta \cap S \neq \emptyset$ . Then we have here a nonempty subset of $\beta$ . Hence $\beta \cap S$ has a least (with respect to $\epsilon_{\beta}$ )

member $\mu$ . We claim that $\mu$ is least in $S$ . To verify this, consider any $\alpha \in S$ :

$$
\alpha \notin \beta \Rightarrow \beta \in \alpha \Rightarrow \beta \subseteq \alpha \Rightarrow \mu \in \alpha ,
$$

$$
\alpha \in \beta \Rightarrow \alpha \in \beta \cap S \Rightarrow \mu \in \alpha .
$$

Either way, $\mu \in \alpha$ .

Corollary 7N (a) Any transitive set of ordinal numbers is itself an ordinal number.

(b) 0 is an ordinal number.

(c) If $\alpha$ is any ordinal number, then $\alpha^{+}$ is also an ordinal number.

(d) If $A$ is any set of ordinal numbers, then $\bigcup A$ is also an ordinal number.

Proof (a) We can conclude from the preceding theorem that any set of ordinals is well ordered by epsilon. If, in addition, the set is a transitive set, then it is an ordinal number by Theorem 7L.

(b) $\varnothing$ is a transitive set of ordinals. (It is the $\in$ -image of the well-ordered structure $\langle\varnothing,\varnothing\rangle$ .)

(c) Recall that $\alpha^{+} = \alpha \cup \{\alpha\}$ . The members of $\alpha^{+}$ are all ordinals (by Theorem 7M(a)). And $\alpha^{+}$ is a transitive set by Theorem 4E (compare Exercise 2 of Chapter 4).

(d) We can also apply part (a) to prove part (d). Any member of $\bigcup A$ is a member of some ordinal, and so is itself an ordinal. To show that $\bigcup A$ is a transitive set, we calculate

$$
\begin{array}{r c l l} \delta \in \bigcup A & \Rightarrow & \delta \in \alpha \in A & \text { for   some } \alpha \\ & \Rightarrow & \delta \subseteq \alpha \in A & \text { since } \alpha \text { is   transitive } \\ & \Rightarrow & \delta \subseteq \bigcup A. \end{array}
$$

Thus by part (a), $\bigcup A$ is an ordinal.

In fact more is true here. If $A$ is any set of ordinals, then $\bigcup A$ is an ordinal that is the least upper bound of $A$ . To verify this, first note that the epsilon ordering on the class of all ordinals is also defined by $\subset$ . That is, for ordinals $\alpha$ and $\beta$ we have:

$$
\begin{array}{r c l l} \alpha \in \beta & \Rightarrow & \alpha \subset \beta & \text { since } \beta \text { is   a   transitive   set   and } \alpha \neq \beta \\ & \Rightarrow & \beta \notin \alpha & \text { lest } \beta \in \beta \\ & \Rightarrow & \alpha \in \beta & \text { by   trichotomy. } \end{array}
$$

Thus $\alpha\in\beta$ iff $\alpha\subset\beta$ . Since $\bigcup A$ is the least upper bound for A in the inclusion ordering, it is the least upper bound for the epsilon ordering.

In the same vein, we can assert that $\alpha^{+}$ is the least ordinal larger than $\alpha$ . Clearly $\alpha \in \alpha^{+}$ , so $\alpha^{+}$ is larger than $\alpha$ . Suppose $\alpha \in \beta$ for some ordinal $\beta$ . Then $\alpha \subseteq \beta$ as well, and hence $\alpha^{+} \subseteq \beta$ . As noted above, this yields the fact that $\alpha^{+} \subseteq \beta$ . This shows that $\alpha^{+}$ is the least ordinal larger than $\alpha$ .

Observe also that any ordinal is just the set of all smaller ordinals. That is:

$$
\begin{array}{l} \alpha = \{x \mid x \in \alpha \} \\ = \{x \mid x \text {   is   an   ordinal   } \& x \in \alpha \}. \end{array}
$$

Since our ordering relation is $\in$ , this can be read as, “ $\alpha$ equals the set of ordinals less than $\alpha$ .”

At long last we can get a better picture of what the ordinals are like. The least ordinal is 0. Next come $0^{+}, 0^{++}, \ldots$ , i.e., the natural numbers. The least ordinal greater than these is the least upper bound of the set of natural numbers. This is just $\bigcup \omega$ , which equals $\omega$ . (Or more directly: $\omega$ is an ordinal and the ordinals less than $\omega$ are exactly its members.) Then come $\omega^{+}, \omega^{++}, \ldots$ . All of these are countable ordinals (i.e., ordinals that are countable sets). The least uncountable ordinal $\Omega$ is the set of all smaller ordinals, i.e., is the set of all countable ordinals. But here we are on thin ice, because we have not shown that there are any uncountable ordinals. That defect will be corrected in the next section.

Burali-Forti Theorem There is no set to which every ordinal number belongs.

Proof Theorem 7M told us that the class of all ordinals was a transitive class well ordered by epsilon. If it were a set, then by Theorem 7L it would be an ordinal itself. But then it would be a member of itself, and no ordinal has that property.

This theorem is also called the “Burali-Forti paradox.” Like the later paradox of Russell, it showed the inconsistency of Cantor’s casual use of the abstraction principle, which permitted speaking of “the set of all ordinals.” The theorem was published in 1897 by Burali-Forti, and was the first of the set-theoretic paradoxes to be published.

## Exercises

15. (a) Assume that $<$ is a well ordering on $A$ and that $t \in A$ . Show that $\langle A, < \rangle$ is never isomorphic to $\langle \text{seg } t, <^{\circ} \rangle$ .

(b) Show that in Theorem 7K, at most one of the three alternatives holds.

16. Assume that $\alpha$ and $\beta$ are ordinal numbers with $\alpha \in \beta$ . Show that $\alpha^{+} \in \beta^{+}$ . Conclude that whenever $\alpha \neq \beta$ , then $\alpha^{+} \neq \beta^{+}$ .

17. Assume that $\langle A, < \rangle$ is a well-ordered structure with ordinal number $\alpha$ and that $B \subseteq A$ . Let $\beta$ be the ordinal number of the well-ordered structure $\langle B, <^{\circ} \rangle$ and show that $\beta \in \alpha$ .

18. Assume that $S$ is a set of ordinal numbers. Show that either (i) $S$ has no greatest element, $\bigcup S \notin S$ , and $\bigcup S$ is not the successor of another ordinal; or (ii) $\bigcup S \in S$ and $\bigcup S$ is the greatest element of $S$ .

19. Assume that $A$ is a finite set and that $<$ and $\prec$ are linear orderings on $A$ . Show that $\langle A, < \rangle$ and $\langle A, \prec \rangle$ are isomorphic.

20. Show that if $R$ and $R^{-1}$ are both well orderings on the same set $S$ , then $S$ is finite.

21. Prove the following version of Zorn's lemma. Assume that $<$ is a partial ordering on $A$ . Assume that whenever $C$ is a subset of $A$ for which $<^{\circ}$ is a linear ordering on $C$ , then $C$ has an upper bound in $A$ . Then there exists a maximal element of $A$ .

## DEBTS PAID

In this section we will pay off the debts incurred in Chapter 6. We will define cardinal numbers as promised, and we will complete the proof of Theorem 6M.

The first theorem assures an adequate supply of ordinal numbers. Recall that B is dominated by $A (B \preccurlyeq A)$ iff B is equinumerous to a subset of A.

Hartogs' Theorem For any set $A$ , there is an ordinal not dominated by $A$ .

Proof There is a systematic way to construct the least such ordinal $\alpha$ . Any ordinal that is dominated by A is smaller than (i.e., is a member of) $\alpha$ . And conversely, any ordinal smaller than (i.e., a member of) $\alpha$ should be dominated by A, if $\alpha$ is to be least. Hence we decide to try defining

$$
\alpha = \{\beta \mid \beta \text {   is   an   ordinal   } \& \beta \preccurlyeq A \}.
$$

The essential part of the proof is showing that $\alpha$ is a set. After all, the theorem is equivalent to the assertion that $\alpha$ is not the class of all ordinals.

We begin by defining

$$
W = \{\langle B, <   \rangle \mid B \subseteq A \& <   \text { is   a   well   ordering   on } B \}.
$$

We claim that any member of $\alpha$ is obtainable as the $\epsilon$ -image of something in $W$ . (Thus $\alpha$ is, in a sense, no larger than $W$ .) Consider any ordinal $\beta$ in $\alpha$ . Then some function $f$ maps $\beta$ one-to-one onto a subset $B$ of $A$ . There is a well ordering $<$ on $B$ such that $f$ is an isomorphism from $\langle \beta, \epsilon_{\beta} \rangle$ onto $\langle B, < \rangle$ , namely

$$
<   = \{\langle f (x), f (y) \rangle | x \in y \in \beta \}.
$$

Thus $\langle B, <\rangle \in W$ and the $\epsilon$ -image of $\langle B, <\rangle$ is the same as the $\epsilon$ -image of $\langle \beta, \epsilon_{\beta} \rangle$ , which is just $\beta$ . Thus $\beta$ is indeed the $\epsilon$ -image of a member of $W$ .

$W$ is a set, because if $\langle B, < \rangle \in W$ , then

$$
\langle B, <   \rangle \in \mathscr {P} A \times \mathscr {P} (A \times A).
$$

We can then use a replacement axiom to construct the set E of $\in$ -images of members of W. The preceding paragraph shows that $\alpha \subseteq E$ . (In fact it is not hard to see that $\alpha = E$ .)

Since $\alpha$ is a set, we can conclude from the Burali-Forti theorem that some ordinals do not belong to $\alpha$ . This proves the theorem, but we will continue and show that $\alpha$ itself is the least such ordinal. Clearly $\alpha$ is a set of ordinals, and since

$$
\gamma \in \beta \in \alpha \Rightarrow \gamma \subseteq \beta \preccurlyeq A \Rightarrow \gamma \in \alpha ,
$$

$\alpha$ is transitive. Hence $\alpha$ is an ordinal. We could not have $\alpha \preccurlyeq A$ , lest $\alpha$ belong to itself. And $\alpha$ is the least such ordinal, since $\beta \in \alpha \Rightarrow \beta \preccurlyeq A$ by construction.

Hartogs' theorem does not require the axiom of choice. But the following theorem does.

Well-Ordering Theorem For any set A, there is a well ordering on A.

This theorem is often stated more informally: Any set can be well ordered. As we will observe presently, the well-ordering theorem is equivalent to the axiom of choice. We can prove the well-ordering theorem from Zorn's lemma (Exercise 22). But in order to complete the proof of Theorem 6M, we will instead use the axiom of choice, III.

Proof Let G be a choice function for A, and let $\alpha$ be an ordinal not dominated by A (furnished by Hartogs' theorem). Our strategy is to order A by first choosing a least element, then a next-to-least, and so forth. For the “and so forth” part, we use $\alpha$ as a base; $\alpha$ is large enough that we will exhaust A before coming to the end of $\alpha$ .

Let $e$ be an extraneous object not belonging to $A$ . We can use transfinite recursion to obtain a function $F: \alpha \to A \cup \{e\}$ such that for any $\gamma \in \alpha$ ,

$$
F (\gamma) = \left\{ \begin{array}{l l} G (A - F [   [ \gamma ]   ]) & \quad \text { if } \quad A - F [   [ \gamma ]   ] \neq \varnothing , \\ e & \quad \text { if } \quad A - F [   [ \gamma ]   ] = \varnothing . \end{array} \right.
$$

In other words, $F(\gamma)$ is the chosen member of $A - F[\![\gamma]\!]$ , until $A$ is exhausted. Suppose $\gamma \in \beta \in \alpha$ . If neither $F(\gamma)$ nor $F(\beta)$ equals $e$ , then $F(\gamma) \neq F(\beta)$ , since $F(\gamma) \in F[\![\beta]\!]$ but $F(\beta) \notin F[\![\beta]\!]$ . That is, $F$ is one-to-one until $e$ appears. It follows that $e \in \operatorname{ran} F$ , lest $F$ be a one-to-one function from $\alpha$ into $A$ , contradicting the fact that $A$ does not dominate $\alpha$ .

Let $\delta$ be the least element of $\alpha$ for which $F(\delta) = e$ . Then $F[\delta] = A$ . And by the preceding paragraph, $F \upharpoonright \delta$ is a one-to-one map from $\delta$ onto $A$ . This produces a well ordering on $A$ , namely

$$
<   = \{\langle F (\beta), F (\gamma) \rangle | \beta \in \gamma \in \delta \}.
$$

Then $F \upharpoonright \delta$ is an isomorphism from $\langle \delta, \epsilon_{\delta} \rangle$ onto $\langle A, < \rangle$ .

Example The well-ordering theorem claims that there exists a well ordering W on the set R of real numbers. Now the usual ordering on R is definitely not a well ordering, so W is some unusual ordering. What is it? We have a theorem asserting the existence of W, but its proof (which used choice) gives no clues as to just what W is like. It is entirely possible that there is no formula of the language of set theory that will explicitly define a well ordering on R.

The following variant of the well-ordering theorem follows easily from it.

Numeration Theorem Any set is equinumerous to some ordinal number.

Proof Consider any set A; by the preceding theorem there is a well ordering < on A. Then A is equinumerous to the $\epsilon$ -image $\alpha$ of $\langle A, <\rangle$ .

The name “numeration theorem” reflects the possibility of “counting” the members of A by using the ordinal numbers in $\alpha$ , where a “counting” is a one-to-one correspondence.

The numeration theorem produces a satisfactory definition of cardinal number.

Definition For any set $A$ , define the cardinal number of $A$ (card $A$ ) to be the least ordinal equinumerous to $A$ .

The following theorem makes good our promise of Chapter 6.

Theorem 7P (a) For any sets $A$ and $B$ ,

$$
\operatorname{card} A = \operatorname{card} B \quad \text { iff } \quad A \approx B.
$$

(b) For a finite set $A$ , card $A$ is the unique natural number equinumerous to $A$ .

Proof First, note that by our definition, $A \approx card A$ for any set A. Hence if card A = card B, then we have

$$
A \approx \operatorname{card} A = \operatorname{card} B \approx B.
$$

Conversely if $A \approx B$ , then $A$ and $B$ are equinumerous to exactly the same ordinals. Hence the least such ordinal is the same in both cases.

Part (b) follows from the fact that the natural numbers are also ordinal numbers. If A is finite, then (by definition) $A \approx n$ for a unique natural number n. A is not equinumerous to any smaller ordinal, since the smaller ordinals are just the natural numbers in n. Hence card A = n.

Proof of Theorem 6M, concluded Figure 46 shows how Fig. 40 is to be extended. Here “WO” is the well-ordering theorem, which we proved from (3). It remains to establish $(5) \Rightarrow \text{WO}$ and $\text{WO} \Rightarrow (6)$ .

Proof of $(5) \Rightarrow WO$ Given any set $A$ , we obtain from Hartogs' theorem an ordinal $\alpha$ not dominated by $A$ . By (5), we have $A \preccurlyeq \alpha$ ; i.e., there is a

![](images/2352e5f8bac5d9944e0168f48e67f6e637e06b7428e1040535f5034c8c8d56de.jpg)  
Fig. 46. The proof of Theorem 6M.

one-to-one function $f$ from $A$ into $\alpha$ . This induces a well ordering of $A$ ; define

$$
s <   t \quad \Leftrightarrow \quad f (s) \in f (t)
$$

for $s$ and $t$ in $A$ . Then $<$ is a well ordering of $A$ (by Lemma 7F).

Proof of $WO \Rightarrow (6)$ Consider any A that is closed under unions of chains. By WO there exists a well ordering < of A. We want to make a very large chain $C \subseteq A$ such that $\bigcup C$ is a maximal element. The idea is to go through the members of A in order, adding to C any member of A that includes each set previously placed in C. This construction uses transfinite recursion. That is, the transfinite recursion theorem gives us a function $F: A \to 2$ such that for any $A \in A$ ,

$$
F (A) = \left\{ \begin{array}{l l} 1 & \text {   if   } A \text {   includes   every   set   } B <   A \text {   for   which   } F (B) = 1, \\ 0 & \text {   otherwise.   } \end{array} \right.
$$

Then let $\mathcal{C} = \{A\in \mathcal{A}\mid F(A) = 1\}$ . Thus $F$ is the characteristic function of $\mathcal{C}$ , and for $A\in \mathcal{A}$ ,

$A\in \mathcal{C}\Leftrightarrow A$ includes every $B <   A$ for which $B\in \mathcal{C}$

We claim that $\bigcup \mathcal{C}$ is a maximal element of $\mathcal{A}$ .

First of all, $\mathcal{C}$ is a chain. For if $A$ and $B$ are in $\mathcal{C}$ , then

$$
A \leq B \Rightarrow A \subseteq B \quad \text { and } \quad B \leq A \Rightarrow B \subseteq A.
$$

Since $\mathcal{C}$ is a chain, $\bigcup \mathcal{C} \in \mathcal{A}$ . To prove maximality, suppose that $\bigcup \mathcal{C} \subseteq D \in \mathcal{A}$ . Then $D \in \mathcal{C}$ , since $D$ includes every member of $\mathcal{C}$ . Hence $D \subseteq \bigcup \mathcal{C}$ , and so $D = \bigcup \mathcal{C}$ . Thus $\bigcup \mathcal{C}$ is not a proper subset of any member of $\mathcal{A}$ .

There are several easy consequences of our definition of cardinal numbers. Say that an ordinal number is an initial ordinal iff it is not equinumerous to any smaller ordinal number. Then any initial ordinal is its own cardinal number. Conversely any cardinal number must, by the definition, be an initial ordinal. Thus the cardinal numbers and the initial ordinals are exactly the same things.

Next consider any cardinal number, say $\kappa = card S$ . Then $\kappa \approx S$ (and $\kappa$ is the least ordinal with this property). Also card $\kappa = \kappa$ , since $\kappa$ is an initial ordinal. That is, $\kappa$ is itself a set of cardinality $\kappa$ .

The cardinal numbers, like any other ordinal numbers, are well ordered by the epsilon relation as described in Theorem 7M. It is now easy to verify that this ordering agrees with the ordering of cardinal numbers defined in Chapter 6. For any cardinals $\kappa$ and $\lambda$ ,

$$
\begin{array}{r c l} \kappa \in \lambda & \Rightarrow & \kappa \subset \lambda \\ & \Rightarrow & \kappa \preccurlyeq \lambda   \&   \kappa \neq \lambda \\ & \Rightarrow & \kappa \leq \lambda   \&   \kappa \neq \lambda \\ & \Rightarrow & \kappa <   \lambda . \end{array}
$$

Conversely,

$$
\begin{array}{r c l} \kappa \notin \lambda & \Rightarrow & \lambda \in \kappa \\ & \Rightarrow & \lambda \leq \kappa \\ & \Rightarrow & \kappa \not <   \lambda . \end{array} \quad \text { by   the   above }
$$

In particular, any nonempty set of cardinal numbers has a smallest element. And the word “smallest” is used unambiguously here, since the epsilon ordering and the cardinality ordering agree. The smallest cardinal after $N_{0}$ is of course denoted as $N_{1}$ . We can also characterize $N_{1}$ as the least uncountable ordinal. Next in order of magnitude comes $N_{2}$ . And this continues. In Chapter 8, we define $N_{\alpha}$ for every ordinal $\alpha$ .

## Exercises

22. Prove the well-ordering theorem from the version of Zorn's lemma given in Exercise 21.

23. Assume that $A$ is a set and define (as in Hartogs' theorem) $\alpha$ to be the set of ordinals dominated by $A$ . Show that (i) $\alpha$ is a cardinal number, (ii) card $A < \alpha$ , and (iii) $\alpha$ is the least cardinal greater than card $A$ .

24. Show that for any ordinal number $\alpha$ , there is a cardinal number $\kappa$ that is (as an ordinal) larger than $\alpha$ .

25. (Transfinite induction schema) Let $\varphi(x)$ be a formula and show that the following holds:

Assume that for any ordinal $\alpha$ , we have $(\forall x \in \alpha)\varphi(x) \Rightarrow \varphi(\alpha)$ . Then $\varphi(\alpha)$ for any ordinal $\alpha$ .

## RANK

In this final section of the chapter we want to return to the informal view of sets mentioned in Chapter 1—and especially to Fig. 3. The description that was somewhat vague at the start of this book can now be made quite precise.

We want to define for every ordinal number $\alpha$ the set $V_{\alpha}$ . $V_{0}$ is to be empty, and, in general, $V_{\alpha}$ is to contain those sets whose members are all in some $V_{\beta}$ for $\beta$ less than $\alpha$ . Thus we want

$$
\begin{array}{r c l} a \in V _ {\alpha} & \Leftrightarrow & a \subseteq V _ {\beta} \qquad \text { for   some } \beta \in \alpha \\ & \Leftrightarrow & a \in \mathcal {P} V _ {\beta} \qquad \text { for   some } \beta \in \alpha , \end{array}
$$

or equivalently,

$$
V _ {\alpha} = \bigcup \{\mathscr {P} V _ {\beta} \mid \beta \in \alpha \}.
$$

Theorem 7U will show that in particular cases, this equation can be simplified. If $\alpha = \delta^{+}$ , the equation will become

$$
V _ {\delta^ {+}} = \mathscr {P} V _ {\delta},
$$

whereas if $\alpha$ is not the successor of another ordinal, then the equation will become

$$
\begin{array}{c} V _ {\alpha} = \bigcup \{V _ {\beta} \mid \beta \in \alpha \} \\ = \bigcup_ {\beta \in \alpha} V _ {\beta}. \end{array}
$$

Thus $V_{3} = \mathcal{P}\mathcal{P}\mathcal{P}\emptyset$ and $V_{\omega} = V_{0} \cup V_{1} \cup V_{2} \cup \dots$ .

But we are getting ahead of ourselves. We have yet to show how to define $V_{\alpha}$ . The equation

$$
V _ {\alpha} = \bigcup \{\mathscr {P} V _ {\beta} \mid \beta \in \alpha \}
$$

defines $V_{\alpha}$ in terms of $V_{\beta}$ for $\beta$ less than $\alpha$ . So we need to define $V_{\alpha}$ by transfinite recursion. The class of all ordinals is well ordered, so transfinite recursion over this class should give us a function-class F such that

$$
\mathsf {F} (\alpha) = \bigcup \{\mathscr {P} \mathsf {F} (\beta) \mid \beta \in \alpha \}
$$

for each ordinal $\alpha$ . But there is an obvious hitch here. We cannot work directly with classes that are not sets. Instead we will sneak up gradually on F.

Lemma 7Q For any ordinal number $\delta$ there is a function $F_{\delta}$ with domain $\delta$ such that

$$
F _ {\delta} (\alpha) = \bigcup \{\mathscr {P} F _ {\delta} (\beta) \mid \beta \in \alpha \}
$$

for every $\alpha \in \delta$ .

Proof We apply transfinite recursion. On $\delta$ we have the well ordering $\epsilon_{\delta}$ . Take for $\gamma(x, y)$ the formula

$$
y = \bigcup \{\mathscr {P} z \mid z \in \operatorname{ran} x \}.
$$

We can show that $\{\mathcal{P}z \mid z \in \operatorname{ran} x\}$ is a set by showing that it is included in $\mathcal{PP} \cup (\operatorname{ran} x)$ . But an easier proof uses a replacement axiom: Let $\varphi(z, w)$ be the formula $w = \mathcal{P}z$ . Then because $\operatorname{ran} x$ is a set, $\{\mathcal{P}z \mid z \in \operatorname{ran} x\}$ is also a set.

Obviously for any $f$ there is a unique $y$ such that $\gamma(f, y)$ , namely $y = \bigcup \{\mathcal{P}z \mid z \in \operatorname{ran} f\}$ . Transfinite recursion then gives us a function $F_{\delta}$ such that

(☆)

$$
F _ {\delta} (\alpha) = \bigcup \{\mathscr {P} z \mid z \in \operatorname{ran} (F _ {\delta} \upharpoonright \sec \alpha) \}
$$

for every $\alpha \in \delta$ . Now then,

$$
\begin{array}{r l} \operatorname{seg} \alpha & = \left\{t \mid t \in_ {\delta} \alpha \right\} \\ & = \left\{t \mid t \in \alpha \right\} \\ & = \alpha . \end{array}
$$

Thus

$$
\begin{array}{r c l} z \in \operatorname{ran} (F _ {\delta} \upharpoonright \operatorname{seg} \alpha) & \Leftrightarrow & z \in \operatorname{ran} (F _ {\delta} \upharpoonright \alpha) \\ & \Leftrightarrow & z = F _ {\delta} (\beta) \qquad \text { for   some } \beta \in \alpha . \end{array}
$$

So (☆) becomes

$$
\begin{array}{r l} F _ {\delta} (\alpha) & = \bigcup \{\mathcal {P} z \mid z = F _ {\delta} (\beta) \text {   for   some   } \beta \in \alpha \} \\ & = \bigcup \{\mathcal {P} F _ {\delta} (\beta) \mid \beta \in \alpha \} \end{array}
$$

as desired.

Now consider any two ordinals $\delta$ and $\varepsilon$ . The smaller of the two is $\delta \cap \varepsilon$ . (Why?) We have two functions $F_{\delta}$ and $F_{\varepsilon}$ from the preceding lemma. These functions agree on $\delta \cap \varepsilon$ :

Lemma 7R Let $\delta$ and $\varepsilon$ be ordinal numbers; let $F_{\delta}$ and $F_{\varepsilon}$ be functions from Lemma 7Q. Then

$$
F _ {\delta} (\alpha) = F _ {\varepsilon} (\alpha)
$$

for all $\alpha \in \delta \cap \varepsilon$ .

Proof By the symmetry, we suppose that $\delta \in \varepsilon$ . Hence $\delta \subseteq \varepsilon$ and $\delta \cap \varepsilon = \delta$ . We will establish the equation $F_{\delta}(\alpha) = F_{\varepsilon}(\alpha)$ by using transfinite induction in $\langle \delta, \epsilon_{\delta} \rangle$ . Define

$$
B = \{\alpha \in \delta | F _ {\delta} (\alpha) = F _ {\varepsilon} (\alpha) \}.
$$

In order to show that $B = \delta$ , it suffices to show that $B$ is “ $\in_{\delta}$ -inductive,” i.e., that

$$
\operatorname{seg} \alpha \subseteq B \Rightarrow \alpha \in B
$$

for each $\alpha \in \delta$ .

We calculate:

$$
\begin{array}{r c l} \text {seg} \alpha \subseteq B & \Rightarrow & F _ {\delta} (\beta) = F _ {\varepsilon} (\beta) \quad \text {for} \quad \beta \in \alpha \\ & \Rightarrow & \bigcup \{\mathscr {P} F _ {\delta} (\beta) \mid \beta \in \alpha \} = \bigcup \{\mathscr {P} F _ {\varepsilon} (\beta) \mid \beta \in \alpha \} \\ & \Rightarrow & F _ {\delta} (\alpha) = F _ {\varepsilon} (\alpha) \\ & \Rightarrow & \alpha \in B \end{array}
$$

for $\alpha \in \delta$ . And so we are done.

In particular (by taking $\delta = \varepsilon$ ) we see that the function $F_{\delta}$ from Lemma 7Q is unique. We can now unambiguously define $V_{\alpha}$ .

Definition Let $\alpha$ be an ordinal number. Define $V_{\alpha}$ to be the set $F_{\delta}(\alpha)$ , where $\delta$ is any ordinal greater than $\alpha$ (e.g., $\delta = \alpha^{+}$ ).

Theorem 7S For any ordinal number $\alpha$ ,

$$
V _ {\alpha} = \bigcup \{\mathscr {P} V _ {\beta} \mid \beta \in \alpha \}.
$$

Proof Let $\delta = \alpha^{+}$ . Then $V_{\alpha} = F_{\delta}(\alpha)$ and $V_{\beta} = F_{\delta}(\beta)$ for $\beta \in \alpha$ . Hence the desired equation reduces to Lemma 7Q.

Lemma 7T For any ordinal number $\alpha$ , $V_{\alpha}$ is a transitive set.

Proof We would like to prove this by transfinite induction over the class of all ordinals. This can be done by utilizing Exercise 25. But we can also avoid that exercise by proving for each ordinal $\delta$ that $V_{\alpha}$ is a transitive set whenever $\alpha \in \delta$ . This requires only transfinite induction over $\langle \delta, \epsilon_{\delta} \rangle$ .

Let $B$ be the set on which the conclusion holds:

$$
B = \{\alpha \in \delta \mid V _ {\alpha} \text {   is   a   transitive   set } \}.
$$

We want to show that $B = \delta$ ; this will follow from the transfinite induction theorem if we show that $B$ is “ $\in_{\delta}$ -inductive,” i.e., that

$$
\alpha \subseteq B \Rightarrow \alpha \in B
$$

for all $\alpha \in \delta$ . (Recall that $\operatorname{seg} \alpha = \alpha$ .)

Suppose then that $\alpha \subseteq B$ . Then for any $\beta \in \alpha$ , $V_{\beta}$ is a transitive set, as is $\mathcal{P}V_{\beta}$ (by Exercise 3 of Chapter 4). It follows that $V_{\alpha}$ is a transitive set, because

$$
\begin{array}{r c l} x \in V _ {\alpha} & \Rightarrow & x \in \mathcal {P} V _ {\beta} \\ & \Rightarrow & x \subseteq \mathcal {P} V _ {\beta} \\ & \Rightarrow & x \subseteq V _ {\alpha}. \end{array} \quad \text { for   some } \beta \in \alpha \quad \text { for   some } \beta \in \alpha
$$

Thus $\alpha \in B$ , and we are done.

There are three sorts of ordinal number. First, there is 0, called zero. Second, there are the ordinals of the form $\alpha^{+}$ for a smaller ordinal $\alpha$ . These are called the successor ordinals. Third, there are all the others, called limit ordinals. For example, the least limit ordinal is $\omega$ .

If $\lambda$ is a limit ordinal and $\beta\in\lambda$ , then $\beta^{+}\in\lambda$ . This is because $\beta^{+}$ , being the least ordinal larger than $\beta$ , must satisfy $\beta^{+}\in\lambda$ . And $\beta^{+}\neq\lambda$ since $\lambda$ is a limit ordinal.

The following theorem describes $V_{\alpha}$ for each of the three sorts of ordinal number.

Theorem 7U (a) For ordinals $\beta \in \alpha$ we have $V_{\beta} \subseteq V_{\alpha}$ .

(b) $V_{0} = \varnothing.$

(c) $V_{\alpha^{+}} = \mathcal{P}V_{\alpha}$ for any ordinal number $\alpha$ .

(d) $V_{\lambda} = \bigcup_{\beta \in \lambda} V_{\beta}$ for any limit ordinal $\lambda$ .

Proof For part (a), first observe that $V_{\beta} \in \mathcal{P}V_{\beta} \subseteq V_{\alpha}$ , so that $V_{\beta} \in V_{\alpha}$ . Since $V_{\alpha}$ is a transitive set, we also have $V_{\beta} \subseteq V_{\alpha}$ .

Part (b) is clear.

For part (c), we first obtain from part (a)

$$
\beta \in \alpha \Rightarrow V _ {\beta} \subseteq V _ {\alpha} \Rightarrow \mathcal {P} V _ {\beta} \subseteq \mathcal {P} V _ {\alpha}.
$$

Now $V_{\alpha^{+}} = \bigcup \{\mathcal{P}V_{\beta} \mid \beta \in \alpha\}$ and this union is equal to the largest set, $\mathcal{P}V_{\alpha}$ . Finally for part (d) we have one inclusion:

$$
\begin{array}{r c l l} x \in V _ {\lambda} & \Rightarrow & x \in \mathscr {P} V _ {\beta} & \text {   for   some   } \beta \in \lambda \\ & \Rightarrow & x \in V _ {\beta^ {+}} & \text {   by   part   (c)   } \\ & \Rightarrow & x \in \bigcup_ {\beta \in \lambda} V _ {\beta} & \text {   since   } \beta^ {+} \in \lambda . \end{array}
$$

The other inclusion is similar:

$$
\begin{array}{r c l} x \in \bigcup_ {\beta \in \lambda} V _ {\beta} & \Rightarrow & x \in V _ {\beta} \subseteq V _ {\beta^ {+}} = \mathscr {P} V _ {\beta} \quad \text { for   some } \beta \in \lambda \\ & \Rightarrow & x \in V _ {\lambda}. \end{array}
$$

Thus equality holds.

We will say that a set A is grounded iff $A \subseteq V_{\alpha}$ for some ordinal number $\alpha$ . In this event, we define the rank of A (rank A) to be the least such ordinal $\alpha$ . Thus for a grounded set A:

$$
A \subseteq V _ {\text { rank } A} \quad \text { and } \quad A \in V _ {(\text { rank } A) ^ {+}}.
$$

The number rank A indicates how many times the power set operation must be used to obtain all the members of A. For example, every ordinal $\alpha$ is grounded and rank $\alpha = \alpha$ (Exercise 26).

There is one methodological objection that can be raised concerning the definition of rank. We want rank A to be the least member of $\{\alpha \mid A \subseteq V_{\alpha}\}$ . But (for a grounded set A) this is not a set of ordinals, but a proper class of ordinals. Nonetheless, it has a least member. Being nonempty, it has some member $\beta$ . Either $\beta$ is its least member, or

$$
\{\alpha \in \beta \mid A \subseteq V _ {\alpha} \}
$$

is a nonempty set of ordinals. In the latter case, we can apply Theorem 7M(e) to obtain a least element.

Theorem 7V (a) If $a \in A$ and $A$ is grounded, then $a$ is grounded and rank $a \in \operatorname{rank} A$ .

(b) If every member of $A$ is grounded, then $A$ is also grounded and

$$
\operatorname{rank} A = \bigcup \left\{\left(\operatorname{rank} a\right) ^ {+} \mid a \in A \right\}.
$$

Proof For the first part, assume that A is grounded and that $a \in A$ . Then

$$
\begin{array}{r c l} A \subseteq V _ {\text {rank} A} & \Rightarrow & a \in V _ {\text {rank} A} \\ & \Rightarrow & a \in \mathcal {P} V _ {\beta} \\ & \Rightarrow & a \subseteq V _ {\beta} \\ & \Rightarrow & \text {rank} a \in \text {rank} A. \end{array} \qquad \text {for some} \beta \in \text {rank} A
$$

For part (b), assume that every member of $A$ is grounded. Define

$$
\alpha = \bigcup \left\{\left(\operatorname{rank} a\right) ^ {+} \mid a \in A \right\}.
$$

To show that $\alpha$ is a set, we use a replacement axiom first to conclude that $\{(\text{rank } a)^+ \mid a \in A\}$ is a set. Then by the union axiom, $\alpha$ is a set.

By Corollary 7N(d), $\alpha$ is an ordinal. First we claim that $A \subseteq V_{\alpha}$ . (This will show that $A$ is grounded and that rank $A \in \alpha$ .) We calculate

$$
\begin{array}{r c l} a \in A & \Rightarrow & a \subseteq V _ {\text { rank   } a} \\ & \Rightarrow & a \in V _ {(\text { rank   } a) ^ {+}} \\ & \Rightarrow & a \in V _ {\alpha} \quad \text { by   Theorem   7U(a) }, \end{array}
$$

since (rank $a)^{+} \in \alpha$ for each $a \in A$ . Thus $A \subseteq V_{\alpha}$ .

To show that $\alpha \in \operatorname{rank} A$ , we use part (a).

$$
\begin{array}{r c l} a \in A & \Rightarrow & \operatorname{rank} a \in \operatorname{rank} A \\ & \Rightarrow & (\operatorname{rank} a) ^ {+} \underline {{\in}} \operatorname{rank} A. \end{array}
$$

Hence rank A is an upper bound for the ordinals (rank $a)^{+}$ , and so is at least as large as their least upper bound $\alpha$ .

Part (b) of the foregoing theorem can be translated into words as: The rank of a set is the least ordinal that is strictly greater than the ranks of all members of the set.

Theorem 7W The following two statements are equivalent.

(a) Every set is grounded.

(b) (Regularity) Every nonempty set $A$ has a member $m$ with $m \cap A = \varnothing$ .

Proof First assume that every set is grounded, and let A be a nonempty set. The idea is to take $m \in A$ having the least possible rank $\mu$ . Thus from

$$
\{\operatorname{rank} a \mid a \in A \},
$$

we take the least member $\mu$ , and then we select $m \in A$ having rank $m = \mu$ . If $x \in m$ , then by Theorem 7V(a), rank $x \in \mu$ . We cannot have $x \in A$ , due to the leastness of $\mu$ . Hence $m \cap A = \emptyset$ as desired.

For the converse, assume that (b) holds. Suppose that, contrary to our expectations, some set c is not grounded. Then some set (e.g., $\{c\}$ ) has a nongrounded member. And hence some transitive set B has a nongrounded member; we can take B to be the transitive closure of $\{c\}$ (see Exercise 7).

Let $A = \{x \in B \mid x \text{ is not grounded}\}$ . Since $A$ is nonempty, by (b) there is some $m \in A$ with $m \cap A = \varnothing$ . We claim that every member of $m$ is grounded. If $x \in m$ , then $x \in B$ since $B$ is transitive. But $x \notin A$ because $m \cap A = \varnothing$ , so $x$ must be grounded.

Since every member of $m$ is grounded, we can conclude from Theorem 7V(b) that $m$ is also grounded. This contradicts the fact that $m \in A$ .

Near the bottom of p. 8, we stated as “a fundamental principle” that every set is grounded. So on an informal level at least, we must accept both parts of the above theorem as true.

But neither part is provable from the axioms adopted up to now. To correct this defect, we will now adopt the regularity axiom. For this axiom we could use either (a) or (b) from the above theorem. We select (b) because it has a more elementary formulation.

Regularity Axiom Every nonempty set $A$ has a member $m$ with $m \cap A = \varnothing$ .

The regularity axiom is also known as the foundation axiom or the Fundierungsaxiom. The idea first appeared in a 1917 paper by Mirimanoff; the axiom was listed explicitly in von Neumann's 1925 paper.

The concept of rank, as well as the concept of regularity, appeared in Mirimanoff's 1917 paper. The idea of rank is a descendant of Russell's concept of type.

The following theorem lists some basic consequences of regularity.

Theorem 7X (a) No set is a member of itself.

(b) There do not exist any sets $a$ and $b$ with $a \in b$ and $b \in a$ .

(c) There is no function $f$ with domain $\omega$ such that

$$
\dots \in f (2) \in f (1) \in f (0).
$$

Proof For part (c), suppose to the contrary that $f(n^{+}) \in f(n)$ for each $n \in \omega$ . Let A = ran f. Any member m of A must equal $f(n)$ for some n. Then $f(n^{+}) \in m \cap A$ , so that $m \cap A$ is always nonempty. This contradicts regularity.

Parts (a) and (b) can be proved either by similar arguments or as consequences of part (c). We leave the details as an exercise.

Since every set is grounded, the sets are arranged in an orderly hierarchy according their rank. This is the situation that Fig. 3 attempts to illustrate. Thus the universe of all sets is, in a sense, determined by two factors:

1. the extent of the class of all ordinals, and

2. the variety of subsets that are assigned to a set by the power set operation.

## Exercises

26. Show that every ordinal number $\alpha$ is grounded, and that rank $\alpha = \alpha$ .

27. Show that the set $\mathbb{R}$ of real numbers, as constructed in Chapter 5, has rank $\omega^{+ + + + + }$

28. Show that

$$
V _ {\alpha} = \{X \mid \operatorname{rank} X \in \alpha \}.
$$

29. Prove parts (a) and (b) of Theorem 7X.

30. Show that for any sets

$$
\operatorname{rank} \{a, b \} = \max (\operatorname{rank} a, \operatorname{rank} b) ^ {+},
$$

$$
\operatorname{rank} \mathscr {P} a = (\operatorname{rank} a) ^ {+},
$$

$$
\operatorname{rank} \bigcup a \in \operatorname{rank} a.
$$

31. Define kard A to be the collection of all sets B such that (i) A is equinumerous to B, and (ii) nothing of rank less than rank B is equinumerous to B.

(a) Show that kard $A$ is a set.

(b) Show that kard $A$ is nonempty.

(c) Show that for any sets $A$ and $B$ ,

$$
\operatorname{kard} A = \operatorname{kard} B \quad \text { iff } \quad A \approx B.
$$

32. Let $\langle A, R \rangle$ be a structure. Define the isomorphism type it $\langle A, R \rangle$ of this structure to be the set of all structures $\langle B, S \rangle$ such that (i) $\langle A, R \rangle$ is isomorphic to $\langle B, S \rangle$ , and (ii) nothing of rank less than rank $\langle B, S \rangle$ is isomorphic to $\langle B, S \rangle$ .

(a) Show that it $\langle A, R \rangle$ is a set (and not a proper class).

(b) Show that it $\langle A, R \rangle$ is nonempty.

(c) Show that

$$
\operatorname{it} \langle A, R \rangle = \operatorname{it} \langle B, S \rangle \quad \text { iff } \quad \langle A, R \rangle \cong \langle B, S \rangle .
$$

33. Assume that $D$ is a transitive set. Let $B$ be a set with the property that for any $a$ in $D$ ,

$$
a \subseteq B \Rightarrow a \in B.
$$

Show that $D \subseteq B$ .

34. Assume that

$$
\{x, \{x, y \} \} = \{u, \{u, v \} \}
$$

and show that $x = u$ and $y = v$ .

35. Show that if $a^{+} = b^{+}$ , then $a = b$ .

36. Show that the rank of any set S is the same as the rank of its transitive closure TC S (as defined in Exercise 7).

37. Show that a set $\alpha$ is an ordinal number iff it is a transitive set with the property that for any distinct x and y in $\alpha$ , either $x \in y$ or $y \in x$ .

38. Show that whenever $\lambda$ is a limit ordinal, then $\lambda = \bigcup \lambda$ .

39. Prove that a set is an ordinal number iff it is a transitive set of transitive sets.

# ORDINALS AND ORDER TYPES

This chapter ends with a discussion of the arithmetic of ordinal numbers. That topic is preceded by material that is useful for ordinal arithmetic, and that also has independent interest.

The logical dependencies among the sections of this chapter are as follows. The section on alephs depends on the preceding section on transfinite recursion. The section on ordinal operations can be independent of the others, but it refers to the section on alephs for examples. The section on isomorphism types is independent of the earlier sections, and in turn forms the basis for the following section on the arithmetic of order types.

The section on ordinal arithmetic refers to the preceding section for addition and multiplication, and to transfinite recursion for exponentiation. But it is indicated how all of the operations can be based on transfinite recursion, thereby avoiding order types. In either event, the section on ordinal operations is utilized here.

## TRANSFINITE RECURSION AGAIN

In Chapter 7 we defined a set $V_{\alpha}$ for each ordinal $\alpha$ . That definition proceeded in a somewhat roundabout manner, defining first a function

$F_{\delta}$ for each $\delta$ , and then proving that $F_{\delta}(\alpha)$ was actually independent of $\delta$ (as long as $\delta$ was greater than $\alpha$ ). We could then define $V_{\alpha}$ to be $F_{\delta}(\alpha)$ for any large $\delta$ .

It is interesting to note that the goal of the construction was not a function but a definition. We could not hope to have a function F with $\mathbf{F}(\alpha)=V_{\alpha}$ for every $\alpha$ , because the domain of F would have to be the proper class of all ordinals.

We now want a general transfinite recursion theorem that will yield directly the definition of $V_{\alpha}$ , and will be applicable to other cases as well. In terms of proper classes, we can state this theorem as follows:

Let G be a function-class whose domain is the class V of all sets. Then we claim that there is a function-class F whose domain is the class of all ordinals and such that

$$
\mathsf {F} (\alpha) = \mathsf {G} (\mathsf {F} \upharpoonright \alpha)
$$

for every $\alpha$ .

Now we must apply the standard rewording. In place of G we have a formula $\gamma(x, y)$ that defines G. The assumption that G is a function-class with domain V is reworded to state that for any x there is a unique y such that $\gamma(x, y)$ holds. In place of F we also have a formula $\varphi(x, y)$ defining F. For every ordinal $\alpha$ there must be a unique y such that $\varphi(\alpha, y)$ holds. The equation

$$
\mathbf {F} (\alpha) = \mathbf {G} (\mathbf {F} \upharpoonright \alpha)
$$

is reworded to state that whenever $f$ is a function with domain $\alpha$ such that $\varphi(\beta, f(\beta))$ holds for all $\beta \in \alpha$ (i.e., whenever $f = F \upharpoonright \alpha$ ) then the unique $y$ such that $\varphi(\alpha, y)$ equals the unique $y$ such that $\gamma(f, y)$ .

Transfinite Recursion Schema on the Ordinals Let $\gamma(x, y)$ be any formula. Then we can construct another formula $\varphi(u, v)$ such that the following is a theorem.

Assume that for every f there is a unique set y such that $\gamma(f, y)$ . Then for every ordinal number $\alpha$ there is a unique y such that $\varphi(\alpha, y)$ . Furthermore whenever f is a function whose domain is an ordinal number $\alpha$ and such that $\varphi(\beta, f(\beta))$ for all $\beta$ less than $\alpha$ , we then have

$$
\varphi (\alpha , y) \quad \text { iff } \quad \gamma (f, y)
$$

for every $y$ .

We will give the proof presently. The significance of the theorem is that it justifies making a certain definition. We select some available symbol, say “t,” and define the term

$$
t _ {\alpha} = \text { the   unique } y \text { such   that } \varphi (\alpha , y)
$$

for every ordinal $\alpha$ . The operation of going from $\alpha$ to $t_{\alpha}$ is $\gamma$ -constructed in the following sense. Whenever f is the restriction of the operation to some ordinal $\alpha$ (i.e., dom $f = \alpha$ and $f(\beta) = t_{\beta}$ for each $\beta$ less than $\alpha$ ), then we can conclude from the above theorem that $\gamma(f, t_{\alpha})$ . We might abbreviate this by writing

$$
\gamma (t \upharpoonright \alpha , t _ {\alpha}).
$$

Example We will apply the foregoing theorem to construct $V_{\alpha}$ . For $\gamma$ use the formula we used before (in Lemma 7Q), so that $\gamma(f, y)$ is

$$
y = \bigcup \{\mathscr {P} z \mid z \in \operatorname{ran} f \}.
$$

Now plug this into the theorem and the subsequent discussion, but select the symbol “V” instead of “t.” We get a set $V_{\alpha}$ for each $\alpha$ , but we must use the fact that the operation is $\gamma$ -constructed to be sure that we have the right $V_{\alpha}$ . So consider any fixed $\alpha$ and let f. be the restriction of the operation to $\alpha$ :

$$
f (\beta) = V _ {\beta}
$$

for $\beta$ less than $\alpha$ . Then we can conclude that $\gamma(f, V_{\alpha})$ , which when expanded becomes

$$
\begin{array}{r l} V _ {\alpha} & = \bigcup \{\mathcal {P} z \mid z \in \operatorname{ran} f \} \\ & = \bigcup \{\mathcal {P} V _ {\beta} \mid \beta \in \alpha \}. \end{array}
$$

Comparing this equation with Theorem 7S, we see (by transfinite induction) that we have the same $V_{\alpha}$ as in Chapter 7.

Proof of the theorem The formula $\varphi (\alpha ,y)$ is the following:

There exists an ordinal $\delta$ greater than $\alpha$ and there exists a $\gamma$ -constructed function $F_{\delta}$ with domain $\delta$ such that $F_{\delta}(\alpha)=y$ .

As in Chapter 7, $F_{\delta}$ is said to be $\gamma$ -constructed iff $\gamma(F_{\delta} \upharpoonright \beta, F_{\delta}(\beta))$ for every $\beta \in \delta$ .

First we will show that these $F_{\delta}$ functions always exist. We are given that for every $f$ there is a unique $y$ such that $\gamma(f, y)$ . Hence for any ordinal $\delta$ we can apply transfinite recursion (from Chapter 7) to the well-ordered structure $\langle \delta, \in_{\delta} \rangle$ . By doing so, we obtain the unique $\gamma$ -constructed function $F_{\delta}$ with domain $\delta$ . Now suppose we are given some ordinal $\alpha$ and we want to find some $y$ such that $\varphi(\alpha, y)$ . We choose $\delta$ to be any larger ordinal (such as $\alpha^{+}$ ) and take $y = F_{\delta}(\alpha)$ . Then clearly $\varphi(\alpha, y)$ holds.

Next we will prove a uniqueness result. Namely, we claim that if $F_{\delta}$ and $F_{\varepsilon}$ are $\gamma$ -constructed functions with domains $\delta$ and $\varepsilon$ , respectively, then $F_{\delta}(\alpha) = F_{\varepsilon}(\alpha)$ for all $\alpha$ in $\delta \cap \varepsilon$ . (This corresponds to Lemma 7R in the special case of $V_{\alpha}$ .) The claim is proved by transfinite induction. For the inductive step, suppose that $F_{\delta}(\beta) = F_{\varepsilon}(\beta)$ for all $\beta \in \alpha$ . Then $F_{\delta} \upharpoonright \alpha = F_{\varepsilon} \upharpoonright \alpha$ . Since both $\gamma(F_{\delta} \upharpoonright \alpha, F_{\delta}(\alpha))$ and $\gamma(F_{\varepsilon} \upharpoonright \alpha, F_{\varepsilon}(\alpha))$ , we can conclude that $F_{\delta}(\alpha) = F_{\varepsilon}(\alpha)$ .

It now follows that for any ordinal $\alpha$ there is a unique y such that $\varphi(\alpha, y)$ , and we know what this unique y is. Finally assume that f is a function whose domain is $\alpha$ and that $\varphi(\beta, f(\beta))$ holds for all $\beta \in \alpha$ . We must show that

$$
\varphi (\alpha , y) \Leftrightarrow \gamma (f, y)
$$

for each y. But what is f? It must be the function $F_{\alpha}$ , by the above. The only y for which $\gamma(F_{\alpha}, y)$ is $F_{\delta}(\alpha)$ , where $\delta$ is some larger ordinal. And it is also the only y for which $\varphi(\alpha, y)$ .

In the next section we will see further examples of the use of transfinite recursion on the ordinals.

## ALEPHS

Suppose that we have defined some class A of ordinals. Now A might or might not be a set. If A is bounded, i.e., if there is an ordinal $\beta$ such that $\alpha \in \beta$ for each $\alpha$ in A, then $A \subseteq \beta^{+}$ and consequently A is a set. On the other hand, if A is unbounded, then $\bigcup A$ is the class of all ordinals. (This holds because any $\beta$ , failing to bound A, is less than some $\alpha$ in A. Thus $\beta \in \alpha \in A$ and $\beta \in \bigcup A$ .) By the Burali-Forti theorem, A cannot be a set. Thus we can conclude that A is a set iff it is bounded.

Now focus attention on the case where we have defined an unbounded (and hence proper) class of ordinals. As an example we will take the class of infinite cardinal numbers, but later we can apply our work to other classes. The class of infinite cardinal numbers is unbounded. (One way to prove this fact is to observe that for any ordinal $\beta$ we obtain from Hartogs' theorem the least ordinal $\alpha$ not dominated by $\beta$ . Then $\alpha$ is an initial ordinal and is larger than $\beta$ . An alternative proof uses $2^{card\beta}$ .)

The class of infinite cardinal numbers, like any class of ordinals, inherits the well ordering by epsilon on the class of all ordinals, given by Theorem 7M. We want to enumerate its members in ascending order. There is a least infinite cardinal, which we have always called $\aleph_0$ . Then there is a next one (the least infinite cardinal greater than $\aleph_0$ ), which we call $\aleph_1$ . And so forth.

We will now expand that “and so forth.” Suppose we have worked our way up to $\alpha$ , i.e., we have defined $N_{\beta}$ for all $\beta$ less than $\alpha$ and we are ready to try defining $N_{\alpha}$ . (In the preceding paragraph $\alpha = 2$ .) Naturally we define

$\aleph_{\alpha} =$ the least infinite cardinal different from $\aleph_{\beta}$ for every $\beta$ less than $\alpha$ .

Such a cardinal must exist, because $\{\aleph_{\beta} \mid \beta \in \alpha\}$ is merely a set, whereas the class of infinite cardinals is unbounded.

Now that we know how to construct $N_{\alpha}$ from the smaller alephs, we can apply transfinite recursion on the ordinals. Choose for $\gamma(f, y)$ the formula

$y$ is the least infinite cardinal not in $\operatorname{ran} f$ .

Then for any set f, there is a unique y such that $\gamma(f, y)$ , again because ran f is merely a set whereas the class of infinite cardinals is unbounded. Then transfinite recursion lets us pick a symbol (we pick “ $\aleph$ ”) and define $\aleph_{\alpha}$ for each $\alpha$ in a way that is $\gamma$ -constructed. That is, if f is the function with domain $\alpha$ defined by

$$
f (\beta) = \aleph_ {\beta} \quad \text {   for   } \quad \beta \in \alpha ,
$$

then $\gamma(f, \aleph_{\alpha})$ . And $\gamma(f, \aleph_{\alpha})$ , when written out, becomes

$\aleph_{\alpha}$ is the least infinite cardinal not in ran f,

which by the definition of $f$ becomes

$\aleph_{\alpha}$ is the least infinite cardinal different from $\aleph_{\beta}$ for every $\beta$ less than $\alpha$ .

The following theorem verifies that this construction enumerates the infinite cardinals in ascending order.

Theorem 8A (a) If $\alpha \in \beta$ , then $\aleph_{\alpha} < \aleph_{\beta}$ .

(b) Every infinite cardinal is of the form $\aleph_{\alpha}$ for some $\alpha$ .

Proof (a) This is a consequence of the fact that $\aleph_{\alpha}$ is the least cardinal meeting certain conditions that become more stringent as $\alpha$ increases. Both $\aleph_{\alpha}$ and $\aleph_{\beta}$ meet the condition of being different from $\aleph_{\gamma}$ for all $\gamma$ less than $\alpha$ . Since $\aleph_{\alpha}$ was the least such candidate (and $\aleph_{\beta} \neq \aleph_{\alpha}$ ), we have $\aleph_{\alpha} < \aleph_{\beta}$ .

(b) We use transfinite induction on the class of infinite cardinal numbers (a subclass of the ordinals). Suppose, as the inductive hypothesis, that $\kappa$ is an infinite cardinal for which all smaller infinite cardinals are in the range of the aleph operation. Consider the corresponding set $\{\beta \mid \aleph_{\beta} < \kappa\}$ of ordinals. This is a set (and not a proper class), being no larger than $\kappa$ . And it is a transitive set by part (a). So it is itself an ordinal; call it $\alpha$ . By construction, $\aleph_{\alpha}$ is the least infinite cardinal different from $\aleph_{\beta}$ whenever $\aleph_{\beta} < \kappa$ . By the inductive hypothesis, this is the least infinite cardinal different from all those less than $\kappa$ , which is just $\kappa$ itself.

The construction up to here is applicable to any unbounded class A of ordinals that we might have defined. We take for $\gamma(f, y)$ the formula

$y$ is the least member of $\mathbf{A}$ not in ran $f$ .

Transfinite recursion then lets us define $t_{\alpha}$ for every $\alpha$ in such a way that

$t_{\alpha}$ is the least member of $\mathbf{A}$ different from $t_{\beta}$ for every $\beta$ less than $\alpha$ .

The analogue of Theorem 8A holds (and with the same proof), showing that we have constructed an enumeration of A in ascending order.

Now that we have a legal definition of $\aleph_{\alpha}$ , we can try to see what that definition can give us. There are three possibilities for $\alpha$ : zero, a successor ordinal, or a limit ordinal. We already know about $\aleph_0$ , so consider the case where $\alpha$ is a successor ordinal, say $\alpha = \beta^{+}$ . By the construction and Theorem 8A, $\aleph_{\beta^{+}}$ is the least infinite cardinal greater than $\aleph_{\gamma}$ for every $\gamma$ less than $\beta^{+}$ . We can simplify this since the largest candidate for $\aleph_{\gamma}$ is $\aleph_{\beta}$ . Thus

$$
\aleph_ {\beta^ {+}} = \text { the   least   cardinal   greater   than } \aleph_ {\beta}.
$$

By Exercise 23 of Chapter 7, the least cardinal greater than $\aleph_{\beta}$ , as a set, is the set of all ordinals dominated by the set $\aleph_{\beta}$ .

Now consider the case of limit ordinal $\lambda$ . As before, $\aleph_{\lambda}$ is the least infinite cardinal greater than $\aleph_{\beta}$ for every $\beta$ less than $\lambda$ . We claim that in fact

$$
\aleph_ {\lambda} = \bigcup_ {\beta \in \lambda} \aleph_ {\beta}.
$$

From Chapter 7 we know that $\bigcup_{\beta \in \lambda} \aleph_{\beta}$ is the least ordinal greater than $\aleph_{\beta}$ for every $\beta$ in $\lambda$ . The following lemma shows that it is actually a cardinal number.

Lemma 8B The union of any set of cardinal numbers is itself a cardinal number.

Proof Let A be any set of cardinals. Then $\bigcup A$ is an ordinal by Corollary 7N(d). We must show that it is an initial ordinal. So assume that $\alpha \in \bigcup A$ ; we must show that $\alpha \not\cong \bigcup A$ . We know that $\alpha \in \kappa \in A$ for some cardinal number $\kappa$ . Thus $\alpha \subseteq \kappa \subseteq \bigcup A$ , so that if $\alpha \approx \bigcup A$ , then $\alpha \approx \kappa$ . But it is impossible to have $\alpha \approx \kappa$ , since $\kappa$ is an initial ordinal. Hence $\alpha \not\cong \bigcup A$ .

As another application of transfinite recursion on the ordinals, we can define the beth numbers $\beth_{\alpha}$ . (The letter $\beth$ , called $beth$ , is the second letter of the Hebrew alphabet.) The following three equations describe the term $\beth_{\alpha}$ that we want to define:

$$
\begin{array}{c} \beth_ {0} = \aleph_ {0}, \\ \beth_ {\alpha^ {+}} = 2 ^ {\beth_ {\alpha}}, \\ \beth_ {\lambda} = \bigcup_ {\alpha \in \lambda} \beth_ {\alpha}, \end{array}
$$

where $\lambda$ is a limit ordinal. The transfinite recursion machinery lets us convert these three equations into a legal definition.

To operate the machinery, let $\gamma(f, y)$ be the formula:

Either (i) $f$ is a function with domain 0 and $y = \aleph_0$ , or (ii) $f$ is a function whose domain is a successor ordinal $\alpha^{+}$ and $y = 2^{f(\alpha)}$ ,

or (iii) $f$ is a function whose domain is a limit ordinal $\lambda$ , and $y = \bigcup (\operatorname{ran} f)$ ,

or (iv) none of the above and $y = \emptyset$ .

Then transfinite recursion gives us a formula $\varphi$ with the usual properties. We select the symbol $\square$ and define

$$
\beth_ {\alpha} = \text { the   unique } y \text { such   that } \varphi (\alpha , y).
$$

Then the machinery tells us that “ $\gamma(\beth \upharpoonright \alpha, \beth_{\alpha})$ .” Writing out this condition with $\alpha = 0$ produces the equation

$$
\beth_ {0} = \aleph_ {0}.
$$

Similarly, by using a successor ordinal and then a limit ordinal we get the other two equations

$$
\begin{array}{c} \beth_ {\alpha^ {+}} = 2 ^ {\beth_ {\alpha}}, \\ \beth_ {\lambda} = \bigcup_ {\alpha \in \lambda} \beth_ {\alpha}. \end{array}
$$

The continuum hypothesis (mentioned in Chapter 6) can now be stated by the equation $\aleph_1 = \beth_1$ , and the generalized continuum hypothesis is the assertion that $\aleph_{\alpha} = \beth_{\alpha}$ for every $\alpha$ . (We are merely stating these hypotheses as objects for consideration; we are not claiming that they are true.)

## Exercises

1. Show how to define a term $t_{\alpha}$ (for each ordinal $\alpha$ ) so that $t_0 = 5$ , $t_{\alpha^+} = (t_\alpha)^+$ , and $t_\lambda = \bigcup_{\alpha \in \lambda} t_\alpha$ for a limit ordinal $\lambda$ .

2. In the preceding exercise, show that if $\alpha \in \omega$ , then $t_{\alpha} = 5 + \alpha$ . Show that if $\omega \in \alpha$ , then $t_{\alpha} = \alpha$ .

## ORDINAL OPERATIONS

There are several operations on the class of ordinal numbers that are of interest to us. A few of these operations have already been defined: the successor operation assigning to each ordinal $\beta$ its successor $\beta^{+}$ , and the aleph and beth operations assigning to $\beta$ the numbers $\aleph_{\beta}$ and $\beth_{\beta}$ . More examples will be encountered when we study ordinal arithmetic.

These operations do not correspond to functions (which are sets of ordered pairs), because the class of all ordinals fails to be a set. Instead for each ordinal $\beta$ we define an ordinal $t_{\beta}$ as the unique ordinal meeting certain specified conditions. We will say that the operation is monotone iff the condition

$$
\alpha \in \beta \Rightarrow t _ {\alpha} \in t _ {\beta}
$$

always holds. We will say that the operation is continuous iff the equation

$$
t _ {\lambda} = \bigcup_ {\beta \in \lambda} t _ {\beta}
$$

holds for every limit ordinal $\lambda$ . Finally we will say that the operation is normal iff it is both monotone and continuous.

Example If $\alpha \in \beta$ , then $\alpha^{+} \in \beta^{+}$ (by Exercise 16 of Chapter 7). Thus the successor operation on the ordinals is monotone. But it lacks continuity, because $\omega^{+} \neq \bigcup_{n \in \omega} n^{+} = \omega$ .

Example The aleph operation is normal by Theorem 8A (for monotonicity) and Lemma 8B with the accompanying discussion (for continuity). More generally, whenever the $t_{\alpha}$ 's enumerate an unbounded class A of ordinals in ascending order, then monotonicity holds (by the analogue of Theorem 8A). Pursuing the analogy, we can assert that continuity holds if A is closed in the sense that the union of any nonempty set of members of A is itself a member of A. Conversely whenever we have defined some normal ordinal operation $t_{\alpha}$ , then its range-class

$$
\{t _ {\alpha} | \alpha \text {   is   an   ordinal   number } \}
$$

is a closed unbounded class of ordinal numbers (Exercise 6).

Recall (from the discussion following Corollary 7N) that whenever S is a set of ordinal numbers, then $\bigcup S$ is an ordinal that is the least upper bound of S. It is therefore natural to define the supremum of S (sup S) to be simply $\bigcup S$ , with the understanding that we will use this notation only when S is a set of ordinal numbers. For example,

$$
\omega = \sup \{0, 2, 4, \dots \}.
$$

The condition for an operation taking $\beta$ to $t_{\beta}$ to be continuous can be stated

$$
t _ {\lambda} = \sup \{t _ {\beta} \mid \beta \in \lambda \}
$$

for limit ordinals $\lambda$ .

The following result shows that for a continuous operation, the condition for monotonicity can be replaced by a more “local” version.

Theorem Schema 8C Assume that we have defined a continuous operation assigning an ordinal $t_{\beta}$ to each ordinal number $\beta$ . Then the operation is monotone provided that $t_{\gamma} \in t_{\gamma^{+}}$ for every ordinal $\gamma$ .

Proof We consider a fixed ordinal $\alpha$ and prove by transfinite induction on $\beta$ that

$$
\alpha \in \beta \Rightarrow t _ {\alpha} \in t _ {\beta}.
$$

Case I $\beta$ is zero. Then the above condition is vacuously true, since $\alpha \notin \beta$ .

Case II $\beta$ is a successor ordinal $\gamma^{+}$ . Then

$$
\begin{array}{r c l} \alpha \in \beta & \Rightarrow & a \underline {{\in}} \gamma \\ & \Rightarrow & t _ {\alpha} \underline {{\in}} t _ {\gamma} \\ & \Rightarrow & t _ {\alpha} \in t _ {\gamma^ {+}} \\ & \Rightarrow & t _ {\alpha} \in t _ {\beta}. \end{array} \quad \text { by   the   inductive   hypothesis } \quad \text { since } \quad t _ {\gamma} \in t _ {\gamma^ {+}}
$$

Case III $\beta$ is a limit ordinal. Then

$$
\begin{array}{r c l} \alpha \in \beta & \Rightarrow & \alpha \in \alpha^ {+} \in \beta \\ & \Rightarrow & t _ {\alpha} \in t _ {\alpha^ {+}} \underline {{\in}} t _ {\beta} \end{array}
$$

by continuity. Hence $t_{\alpha} \in t_{\beta}$ .

Example The beth operation (assigning $\beth_{\beta}$ to $\beta$ ) is normal. The continuity is obvious from its definition. And since $\beth_{\gamma}$ is always less than $2^{\beth_{\gamma}}$ , we have (by the above theorem) monotonicity.

The next results will have useful consequences for the arithmetic of ordinal numbers.

Theorem Schema 8D Assume that we have defined a normal operation assigning an ordinal $t_{\alpha}$ to each ordinal $\alpha$ . Then for any given ordinal $\beta$ that is at least as large as $t_{0}$ , there exists a greatest ordinal $\gamma$ such that $t_{\gamma} \in \beta$ .

We know that any nonempty set of ordinals has a least member, but the above theorem asserts that the set $\{\gamma \mid t_{\gamma} \in \beta\}$ has a greatest member.

Proof Consider the set $\{\alpha \mid t_{\alpha} \in \beta\}$ . This is a set of ordinals and it is (by monotonicity) a transitive set. So it is itself an ordinal. It is not 0, because $t_0 \in \beta$ . Could it be a limit ordinal $\lambda$ ? If so, then

$$
t _ {\lambda} = \sup \{t _ {\alpha} \mid \alpha \in \lambda \} \subseteq \beta ,
$$

whence $\lambda \in \lambda$ . This is impossible, so our set must in fact be a successor ordinal $\gamma^{+}$ . Thus $\gamma$ is the largest member of the set, and so is the largest ordinal for which $t_{\gamma} \in \beta$ .

Theorem Schema 8E Assume that we have defined a normal operation assigning $t_{\alpha}$ to each ordinal number $\alpha$ . Let S be a nonempty set of ordinal numbers. Then

$$
t _ {\sup S} = \sup \{t _ {\alpha} \mid \alpha \in S \}.
$$

Proof We get the “≥” half by monotonicity:

$$
\begin{array}{r c l} \alpha \in S & \Rightarrow & \alpha \underline {{\in}} \sup S \\ & \Rightarrow & t _ {\alpha} \underline {{\in}} t _ {\sup S}, \end{array}
$$

whence $\sup\{t_{\alpha} \mid \alpha \in S\} \subseteq t_{\sup S}$ .

For the other inequality, there are two cases. If $S$ has a largest member $\delta$ , then $\sup S = \delta$ and so $t_{\sup S} = t_{\delta} \in \sup \{t_{\alpha} | \alpha \in S\}$ .

If $S$ has no largest member, then $\sup S$ must be a limit ordinal (since $S \neq \emptyset$ ). So by continuity,

$$
t _ {\sup S} = \sup \{t _ {\beta} | \beta \in \sup S \}.
$$

If $\beta \in \sup S$ , then $\beta \in \gamma \in S$ for some $\gamma$ . Consequently $t_{\beta} \in t_{\gamma}$ , and so

$$
t _ {\beta} \in \sup \{t _ {\alpha} | \alpha \in S \}.
$$

Since $\beta$ was an arbitrary member of sup $S$ ,

$$
\sup \{t _ {\beta} \mid \beta \in \sup S \} \subseteq \sup \{t _ {\alpha} \mid \alpha \in S \}
$$

as desired.

For a monotone operation, we always have $\beta \in t_{\beta}$ , by Exercise 5. Is it possible to have $\beta = t_{\beta}$ ? Yes; the identity operation (assigning $\beta$ to $\beta$ ) is normal. But even for normal operations with rapid growth (such as the beth operation), there are “fixed points” $\beta$ with $\beta = t_{\beta}$ . The following theorem, although not essential to our later work, shows that in fact such fixed points form a proper class.

Veblen Fixed-Point Theorem Schema (1907) Assume that we have defined a normal operation assigning $t_{\alpha}$ to each ordinal number $\alpha$ . Then the operation has arbitrarily large fixed points, i.e., for every ordinal number $\beta$ we can find an ordinal number $\gamma$ with $t_{\gamma} = \gamma$ and $\beta \in \gamma$ .

Proof From the monotonicity we have $\beta \in t_{\beta}$ . If $\beta = t_{\beta}$ , we are done—just take $\gamma = \beta$ . So we may assume that $\beta \in t_{\beta}$ . Then by monotonicity

$$
\beta \in t _ {\beta} \in t _ {t _ {\beta}} \in \dots .
$$

We claim that the supremum of these ordinals is the desired fixed point.

More formally, we define by recursion a function $f$ from $\omega$ into the ordinals such that

$$
f (0) = \beta \quad \text { and } \quad f (n ^ {+}) = t _ {f (n)}.
$$

Thus $f(1) = t_{\beta}$ , $f(2) = t_{t_{\beta}}$ , and so forth. We will write $t_{\beta}^{n}$ for $f(n)$ . As mentioned above, by monotonicity $t_{\beta}^{n} \in t_{\beta}^{n+}$ , so that

$$
\beta \in t _ {\beta} \in t _ {\beta} ^ {2} \in \dots .
$$

Define $\lambda = \sup \operatorname{ran} f = \sup \{t_{\beta}^{n} \mid n \in \omega\}$ . We claim that $t_{\lambda} = \lambda$ .

Clearly $\lambda$ has no largest element, and hence is a limit ordinal. Let $S = \operatorname{ran} f = \{t_{\beta}^{n} \mid n \in \omega\}$ , so that $\lambda = \sup S$ . By Theorem 8E,

$$
\begin{array}{r l} & t _ {\lambda} = \sup \{t _ {\alpha} | \alpha \in S \} \\ & \quad = \sup \{t _ {\beta} ^ {n +} | n \in \omega \} \\ & \quad = \lambda . \end{array}
$$

Thus we have a fixed point.

This proof actually gives us the least fixed point that is at least as large as $\beta$ (by Exercise 7). For example, consider the aleph operation with $\beta = 0$ . Then

$$
0 \in \aleph_ {0} \in \aleph_ {\aleph_ {0}} \in \dots
$$

and the supremum of these numbers is the least fixed point.

Since the class of fixed points of the operation t is an unbounded class of ordinals, we can define the derived operation $t'$ enumerating the fixed points in ascending order. The definition of $t'$ is produced by the transfinite recursion machinery; the crucial equation is

$t_{\alpha}^{\prime} =$ the least fixed point of $t$ different from $t_{\beta}^{\prime}$ for every $\beta \in \alpha$ .

It turns out (Exercise 8) that $t'$ is again a normal operation.

## Exercises

3. Assume that we have defined a monotone operation assigning $t_{\alpha}$ to each ordinal $\alpha$ . Show that

$$
\beta \in \gamma \quad \Leftrightarrow \quad t _ {\beta} \in t _ {\gamma}
$$

and

$$
t _ {\beta} = t _ {\gamma} \Rightarrow \beta = \gamma
$$

for any ordinals $\beta$ and $\gamma$ .

4. Assume that we have defined a normal operation assigning $t_{\alpha}$ to each $\alpha$ . Show that whenever $\lambda$ is a limit ordinal, then $t_{\lambda}$ is also a limit ordinal.

5. Assume that we have defined a monotone operation assigning $t_{\alpha}$ to each $\alpha$ . Show that $\beta \in t_{\beta}$ for every ordinal number $\beta$ .

6. Assume that we have defined a normal operation assigning $t_{\alpha}$ to each $\alpha$ . Show that the range-class

$$
\{t _ {\alpha} \mid \alpha \text {   is   an   ordinal   number } \}
$$

is a closed unbounded class of ordinal numbers.

7. Show that the proof of Veblen's fixed-point theorem produces the least fixed point that is at least as large as $\beta$ .

8. Assume that we have defined a normal operation assigning $t_{\alpha}$ to each $\alpha$ . Let $t'$ be the derived operation, enumerating the fixed points of t in order. Show that $t'$ is again a normal operation.

## ISOMORPHISM TYPES

We have ordinal numbers to measure the length of well orderings. If you know the ordinal number of a well-ordered structure, then you know everything there is to know about that structure, “to within isomorphism.” This is an informal way of saying that two well-ordered structures receive the same ordinal iff they are isomorphic (Theorem 7I).

Our next undertaking will be to extend these ideas to handle structures that are not well ordered. Although our intent is to apply the extended ideas to linearly ordered structures, the initial definitions will be quite general.

Consider then a structure $\langle A, R\rangle$ . The “shape” of this structure is to be measured to within isomorphism by it $\langle A, R\rangle$ , the isomorphism type of $\langle A, R\rangle$ . This is to be defined in such a way that two structures receive the same isomorphism type iff they are isomorphic:

$$
\operatorname{it} \langle A, R \rangle = \operatorname{it} \langle B, S \rangle \quad \text { iff } \quad \langle A, R \rangle \cong \langle B, S \rangle .
$$

As a first guess, we could argue as follows: Isomorphism is an equivalence concept, so why not take it $\langle A, R \rangle$ to be the equivalence class of $\langle A, R \rangle$ ? Then as in Lemma 3N, two structures should have the same equivalence class iff they are isomorphic.

In one way, this first guess is a very bad idea. The “equivalence classes” here will fail to be sets. If A is nonempty, then no set contains every structure that is isomorphic to $\langle A, R\rangle$ ; this is Exercise 9.

With but one modification, this first guess will serve our needs perfectly. Do not take all structures isomorphic to $\langle A, R\rangle$ , just those of least possible rank $\alpha$ . Then these structures will be in $V_{\alpha^{+}}$ , and so it $\langle A, R\rangle$ will be a set. We now will write this down officially.

Definition Let R be a binary relation on A. The isomorphism type it $\langle A, R \rangle$ of the structure $\langle A, R \rangle$ is the set of all structures $\langle B, S \rangle$ such that

(i) $\langle A, R \rangle \cong \langle B, S \rangle$ , and

(ii) no structure of rank less than rank $\langle B, S \rangle$ is isomorphic to $\langle B, S \rangle$ .

It will help to bring in (but only for very temporary use) some terminology. Call a structure pioneering iff there is no structure of smaller rank isomorphic to it. If two pioneering structures are isomorphic, then clearly they have the same rank.

We claim that any structure $\langle A, R \rangle$ is isomorphic to some (not necessarily unique) pioneering structure. The class

## $\{\alpha \mid \alpha$ is the rank of a structure isomorphic to $\langle A, R \rangle\}$

is nonempty (rank $\langle A, R \rangle$ is in it). So it has a least element $\alpha_{0}$ , which we can call the pioneer ordinal for $\langle A, R \rangle$ . Some structure of rank $\alpha_{0}$ is isomorphic to $\langle A, R \rangle$ , and it is pioneering by the leastness of $\alpha_{0}$ .

The definition of it $\langle A, R \rangle$ can now be phrased: It is the set of all pioneering structures that are isomorphic to $\langle A, R \rangle$ . This set has been seen to be nonempty.

Note that it $\langle A, R \rangle$ is indeed a set, being a subset of $V_{\alpha^{+}}$ , where $\alpha$ is the pioneer ordinal for $\langle A, R \rangle$ .

Theorem 8F Structures $\langle A, R \rangle$ and $\langle B, S \rangle$ have the same isomorphism type iff they are isomorphic:

$$
\operatorname{it} \langle A, R \rangle = \operatorname{it} \langle B, S \rangle \quad \text { iff } \quad \langle A, R \rangle \cong \langle B, S \rangle .
$$

Proof First assume that it $\langle A, R \rangle = it \langle B, S \rangle$ . Let $\langle C, T \rangle$ be any structure in this common isomorphism type. Then

$$
\langle A, R \rangle \cong \langle C, T \rangle \cong \langle B, S \rangle .
$$

For the converse, assume that $\langle A, R \rangle \cong \langle B, S \rangle$ . Then the same structures are isomorphic to each of these two; in particular, the same pioneering structures are isomorphic to each. Hence it $\langle A, R \rangle = \text{it} \langle B, S \rangle$ .

Digression Concerning Cardinal Numbers The crucial property of cardinal numbers,

$$
\operatorname{card} A = \operatorname{card} B \quad \text { iff } \quad A \approx B,
$$

looks a lot like Theorem 8F, simplified by omission of the binary relations. This indicates the possibility of an alternative definition of cardinal numbers.

Specifically, define kard A to be the set of all sets B equinumerous to A and having the least possible rank. Then (as in Theorem 8F),

$$
\operatorname{kard} A = \operatorname{kard} B \quad \text { iff } \quad A \approx B.
$$

In comparing card A with kard A, we see that the definition of card A uses the axiom of choice (but not regularity). The definition of kard A relies on regularity but does not require the axiom of choice. (This is a point in favor of kard.) For a finite nonempty set A, kard A fails to be a natural number. (This is a point in favor of card.)

## Exercises

9. Assume that $\langle A, R \rangle$ is a structure with $A \neq \emptyset$ . Show that no set contains every structure isomorphic to $\langle A, R \rangle$ .

10. (a) Show that kard $n = \{n\}$ for $n = 0, 1,$ and 2.

(b) Calculate kard 3.

## ARITHMETIC OF ORDER TYPES

We now focus attention solely on the order types.

Definition An order type is the isomorphism type of some linearly ordered structure.

We will use Greek letters $\rho, \sigma, \ldots$ for order types. Any member of an order type $\rho$ is said to be a linearly ordered structure of type $\rho$ .

First we want to define addition of order types. The basic idea is that $\rho + \sigma$ should be the order type “first $\rho$ and then $\sigma$ .” For the real definition of $\rho + \sigma$ , first select $\langle A, R \rangle$ of type $\rho$ and $\langle B, S \rangle$ of type $\sigma$ with $A \cap B = \varnothing$ . (This is possible, by Exercise 11.) Then define the relation $R \oplus S$ by

$$
R \oplus S = R \cup S \cup (A \times B).
$$

(We reject the cumbersome $R_{A} \oplus_{B} S$ notation.) Finally we define $\rho + \sigma$ by

$$
\rho + \sigma = \mathrm{it} \langle A \cup B, R \oplus S \rangle .
$$

The idea is that we want to order $A \cup B$ in such a way that any member of A is less than any member of B. But within A and B, we order according to R and S.

The next lemma verifies that $\rho + \sigma$ is a well-defined order type.

Lemma 8G Assume that $\langle A, R \rangle$ and $\langle B, S \rangle$ are linearly ordered structures with $A$ and $B$ disjoint.

(a) $R \oplus S$ is a linear ordering on $A \cup B$ .

(b) If $\langle A, R \rangle \cong \langle A', R' \rangle$ , $\langle B, S \rangle \cong \langle B', S' \rangle$ , and $A' \cap B' = \emptyset$ , then

$$
\langle A \cup B, R \oplus S \rangle \cong \langle A ^ {\prime} \cup B ^ {\prime}, R ^ {\prime} \oplus S ^ {\prime} \rangle .
$$

Proof (a) First of all, $R \oplus S$ is irreflexive because a pair of the form $\langle x, x \rangle$ cannot belong to R or S, nor can it belong to $A \times B$ since A and B are disjoint.

To check that $R \oplus S$ is transitive, suppose that $\langle x, y \rangle$ and $\langle y, z \rangle$ belong to $R \oplus S$ . If both of these pairs come from R (or from S), then of course xRz (or xSz). Otherwise one of the pairs comes from $A \times B$ . We may suppose that $\langle x, y \rangle \in A \times B$ ; the other case is similar. Then $x \in A$ and the pair $\langle y, z \rangle$ comes from S (because $y \in B$ ). Hence $z \in B$ and $\langle x, z \rangle \in A \times B$ .

Finally, it is easy to see that $R \oplus S$ is connected on $A \cup B$ . Consider any x and y in $A \cup B$ . There are three cases: both in A, both in B, or mixed. But all three are trivial.

Part (b) is sufficiently straightforward so that nothing more need be said.

The role of this lemma is to assure us that when we define

$$
\rho + \sigma = \mathrm{it} \langle A \cup B, R \oplus S \rangle ,
$$

the end result will be independent of just which structures of type $\rho$ and $\sigma$ are utilized.

Example For each ordinal $\alpha$ , we have the order type it $\langle\alpha, \in_{\alpha}\rangle$ . Distinct ordinals yield distinct order types, since

$$
\begin{array}{r c l} \mathrm{it} \langle \alpha , \in_ {\alpha} \rangle = \mathrm{it} \langle \beta , \in_ {\beta} \rangle & \Rightarrow & \langle \alpha , \in_ {\alpha} \rangle \cong \langle \beta , \in_ {\beta} \rangle \\ & \Rightarrow & \alpha = \beta \end{array}
$$

for ordinals, by Theorems 7I and 7L. The order type it $\langle\alpha,\in_{\alpha}\rangle$ will be denoted as $\bar{\alpha}$ . In particular, we have the order types $\overline{1},\overline{3}$ , and $\bar{\omega}$ (which are it $\langle1,\in_{1}\rangle$ and so forth). And $\overline{1}+\overline{3}=\overline{4}$ . (Please explain why.) Also $\overline{1}+\bar{\omega}=\bar{\omega}$ , whereas $\bar{\omega}+\overline{1}=\omega^{+}$ .

Example It is traditional to use $\eta$ and $\lambda$ to denote the order type of the rationals and reals, respectively (in their usual ordering):

$$
\eta = \mathrm{it} \langle \mathbb {Q}, <   _ {Q} \rangle \quad \text { and } \quad \lambda = \mathrm{it} \langle \mathbb {R}, <   _ {R} \rangle .
$$

Then $\bar{1} + \eta$ is an order type with a least element but no greatest element. (Or more pedantically, the ordered structures of type $\bar{1} + \eta$ have least elements but not greatest elements.) But $\eta + \bar{1}$ has a greatest element but no least element; hence $\bar{1} + \eta \neq \eta + \bar{1}$ . Also $\lambda + \lambda \neq \lambda$ , because in type $\lambda + \lambda$ there is a bounded nonempty set without a least upper bound. On the other hand $\eta + \eta = \eta$ . This is not obvious, but see Exercise 19.

Any order type $\rho$ can be run backwards to yield an order type $\rho^{*}$ . More specifically, we can select a linearly ordered structure $\langle A, R \rangle$ of type $\rho$ . Then we define

$$
\rho^ {*} = \mathrm{it} \langle A, R ^ {- 1} \rangle .
$$

It is routine to check that $\rho^{*}$ is a well-defined order type (compare Exercise 43 of Chapter 3). For any finite ordinal $\alpha$ , we have $\bar{\alpha}^{*} = \bar{\alpha}$ by Exercise 19 of Chapter 7. But $\bar{\omega}^{*} \neq \bar{\omega}$ ; in fact $\bar{\omega}^{*}$ is the order type of the negative integers, which are not well ordered. It is easy to see that $\eta^{*} = \eta$ and $\lambda^{*} = \lambda$ .

Example The sum $\bar{\omega}^{*} + \bar{\omega}$ is the order type of the set Z of integers. But $\bar{\omega} + \bar{\omega}^{*}$ is different; it has both a least element and a greatest element, and infinitely many points between the two.

Now consider the multiplication of order types. The product $\rho\cdot\sigma$ can be described informally as “ $\rho,\sigma$ times.” More formally, we select structures $\langle A,R\rangle$ and $\langle B,S\rangle$ of types $\rho$ and $\sigma$ , respectively. Then define $R*S$ to be “Hebrew lexicographic order” on $A\times B$ :

$$
\langle a _ {1}, b _ {1} \rangle (R * S) \langle a _ {2}, b _ {2} \rangle \quad \text { iff } \quad \text { either   } b _ {1} S b _ {2} \quad \text { or   } (b _ {1} = b _ {2} \text {   and   } a _ {1} R a _ {2}).
$$

This orders the pairs in $A \times B$ according to their second coordinates, and then by their first coordinates when the second coordinates coincide. We can now define the product

$$
\rho \cdot \sigma = \mathrm{it} \langle A \times B, R * S \rangle .
$$

The next lemma verifies that $\rho\cdot\sigma$ is a well-defined order type. This lemma does for multiplication what Lemma 8G does for addition.

Lemma 8H Assume that $\langle A, R \rangle$ and $\langle B, S \rangle$ are linearly ordered structures.

(a) $R * S$ is a linear ordering on $A \times B$ .

(b) If $\langle A, R \rangle \cong \langle A', R' \rangle$ and $\langle B, S \rangle \cong \langle B', S' \rangle$ , then

$$
\langle A \times B, R * S \rangle \cong \langle A ^ {\prime} \times B ^ {\prime}, R ^ {\prime} * S ^ {\prime} \rangle .
$$

Proof (a) It is easy to see from the definition of $R * S$ that it is irreflexive (because both R and S are) and is connected on $A \times B$ . It remains to verify that it is a transitive relation. So assume that

$$
\langle a _ {1}, b _ {1} \rangle (R * S) \langle a _ {2}, b _ {2} \rangle \quad \text { and } \quad \langle a _ {2}, b _ {2} \rangle (R * S) \langle a _ {3}, b _ {3} \rangle .
$$

This assumption breaks down into four cases, as illustrated in Fig. 47. But in each case, we have $\langle a_1, b_1 \rangle (R * S) \langle a_3, b_3 \rangle$ .

Part (b) is again sufficiently straightforward that nothing more need be said.

$$
\langle a _ {1}, b _ {1} \rangle (R * S) \langle a _ {2}, b _ {2} \rangle \left\{ \begin{array}{c c c} & \langle a _ {2}, b _ {2} \rangle (R * S) \langle a _ {3}, b _ {3} \rangle \\ & b _ {2} S b _ {3} & b _ {2} = b _ {3} \& a _ {2} R a _ {3} \\ \hline b _ {1} S b _ {2} & b _ {1} S b _ {3} & b _ {1} S b _ {3} \\ \hline b _ {1} = b _ {2} & b _ {1} S b _ {3} & b _ {1} = b _ {3} \& a _ {1} R a _ {3} \\ \& & & \\ a _ {1} R a _ {2} & & \end{array} \right.
$$

Fig. 47. Transitivity of $R * S$ .

Examples The product $\bar{\omega}\cdot\bar{2}$ is “ $\bar{\omega},\bar{2}$ times.” The set $\omega\times2$ under Hebrew lexicographic ordering is:

$$
\langle 0, 0 \rangle \quad \langle 1, 0 \rangle , \quad \langle 2, 0 \rangle , \dots , \langle 0, 1 \rangle , \quad \langle 1, 1 \rangle , \quad \langle 2, 1 \rangle , \dots .
$$

On the other hand $\bar{2}\cdot\bar{\omega}$ is “ $\bar{2}$ , $\bar{\omega}$ times.” The set $2\times\omega$ under Hebrew lexicographic order is:

$$
\langle 0, 0 \rangle \quad \langle 1, 0 \rangle , \quad \langle 0, 1 \rangle , \quad \langle 1, 1 \rangle , \quad \langle 0, 2 \rangle , \langle 1, 2 \rangle , \dots .
$$

This ordering, unlike the other, is isomorphic to the natural numbers, i.e., $\bar{2} \cdot \bar{\omega} = \bar{\omega}$ . In particular, $\bar{2} \cdot \bar{\omega} \neq \bar{\omega} \cdot \bar{2}$ .

The next theorem gives some of the general laws that addition and multiplication obey. We have already seen that neither operation obeys the commutative law in general; for example,

$$
\bar {1} + \bar {\omega} \neq \bar {\omega} + \bar {1} \quad \text { and } \quad \bar {2} \cdot \bar {\omega} \neq \bar {\omega} \cdot \bar {2}.
$$

Furthermore the right distributive law fails; for example,

$$
(\bar {\omega} + \bar {1}) \cdot \bar {2} \neq \bar {\omega} \cdot \bar {2} + \bar {1} \cdot \bar {2}
$$

(Exercise 15).

Theorem 8I The following identities hold for any order types.

(a) Associative laws

$$
\begin{array}{c} (\rho + \sigma) + \tau = \rho + (\sigma + \tau), \\ (\rho \cdot \sigma) \cdot \tau = \rho \cdot (\sigma \cdot \tau). \end{array}
$$

(b) Left distributive law

$$
\rho \cdot (\sigma + \tau) = (\rho \cdot \sigma) + (\rho \cdot \tau).
$$

## (c) Identity elements

$$
\rho + \bar {0} = \bar {0} + \rho = \rho ,
$$

$$
\rho \cdot \overline {{{1}}} = \overline {{{1}}} \cdot \rho = \rho ,
$$

$$
\rho \cdot \bar {0} = \bar {0} \cdot \rho = \bar {0}.
$$

Proof Both $(\rho + \sigma) + \tau$ and $\rho + (\sigma + \tau)$ produce the “first $\rho$ then $\sigma$ and then $\tau$ ” ordering. Let $\langle A, R \rangle$ , $\langle B, S \rangle$ , and $\langle C, T \rangle$ be of type $\rho$ , $\sigma$ , and $\tau$ , respectively, with A, B, and C disjoint. Then both $(R \oplus S) \oplus T$ and $R \oplus (S \oplus T)$ are easily shown to be

$$
R \cup S \cup T \cup A \times B \cup A \times C \cup B \times C.
$$

Both $(\rho \cdot \sigma) \cdot \tau$ and $\rho \cdot (\sigma \cdot \tau)$ produce Hebrew lexicographic order on $A \times B \times C$ . $(R * S) * T$ is an ordering on $(A \times B) \times C$ , and $R * (S * T)$ is an ordering on $A \times (B \times C)$ , but we can establish an isomorphism. In detail, the condition for $\langle a_{1}, b_{1}, c_{1} \rangle$ to be less than $\langle a_{2}, b_{2}, c_{2} \rangle$ under $(R * S) * T$ is, when expanded,

$$
c _ {1} T c _ {2} \quad \text { or } \quad (c _ {1} = c _ {2} \& b _ {1} S b _ {2}) \quad \text { or } \quad (c _ {1} = c _ {2} \& b _ {1} = b _ {2} \& a _ {1} R a _ {2}).
$$

The condition for $\langle a_1, \langle b_1, c_1 \rangle \rangle$ to be less than $\langle a_2, \langle b_2, c_2 \rangle \rangle$ under $R * (S * T)$ is, when expanded, exactly the same.

In the left distributive law, both $R * (S \oplus T)$ and $(R * S) \oplus (R * T)$ are orderings on the set $(A \times B) \cup (A \times C)$ . And in both cases the condition for $\langle a_{1}, x \rangle$ to be less than $\langle a_{2}, y \rangle$ turns out to be

$$
x S y \quad \text { or } \quad x T y \quad \text { or } \quad (x \in B \& y \in C) \quad \text { or } \quad (x = y \& a _ {1} R a _ {2}).
$$

Part (c) is straightforward.

## Exercises

11. Show that for any order types $\rho$ and $\sigma$ there exist structures $\langle A, R \rangle$ and $\langle B, S \rangle$ of types $\rho$ and $\sigma$ , respectively, such that $A \cap B = \emptyset$ .

12. Prove that for any linearly ordered structures,

$$
\mathrm{it} \langle A, R \rangle + \mathrm{it} \langle B, S \rangle = \mathrm{it} \langle (\{0 \} \times A) \cup (\{1 \} \times B), <   _ {\mathrm{L}} \rangle ,
$$

where $<_{\mathrm{L}}$ is lexicographic ordering.

13. Supply proofs for part (b) of Lemma 8G and part (b) of Lemma 8H.

14. Assume that $\rho \cdot \sigma = \bar{0}$ . Show that either $\rho = \bar{0}$ or $\sigma = \bar{0}$ .

15. Show that $(\bar{\omega} + \bar{1}) \cdot \bar{2}$ is not the same as $(\bar{\omega} \cdot \bar{2}) + (\bar{1} \cdot \bar{2})$ .

16. Supply a proof for part (c) of Theorem 8I.

17. A partial ordering $R$ is said to be dense iff whenever $xRz$ , then $xRy$ and $yRz$ for some $y$ . For example, the usual ordering $<_{Q}$ on the set $\mathbb{Q}$ of rational numbers is dense. Assume that $\langle A, R \rangle$ is a linearly ordered structure with $A$ countable and $R$ dense. Show that $\langle A, R \rangle$ is isomorphic to $\langle B, <_{Q}^{\circ} \rangle$ for some subset $B$ of $\mathbb{Q}$ . [Suggestion: Suppose that $A = \{a_0, a_1, \ldots\}$ . Define $f(a_i)$ by recursion on $i$ .]

18. Assume that $\langle A, R\rangle$ and $\langle B, S\rangle$ are both linearly ordered structures with dense orderings. Assume that A and B are countable and nonempty. Assume that neither ordering has a first or last element. Show that $\langle A, R\rangle \cong \langle B, S\rangle$ . [Suppose that $A = \{a_{0}, a_{1}, \ldots\}$ and $B = \{b_{0}, b_{1}, \ldots\}$ . At stage 2n be sure that $a_{n}$ is paired with some suitable $b_{j}$ and at stage $2n + 1$ be sure that $b_{n}$ is paired with some suitable $a_{i}$ .]

19. Use the preceding exercise to show that $\eta + \eta = \eta \cdot \eta = \eta$ .

## ORDINAL ARITHMETIC

There are two available methods for defining addition and multiplication on the ordinals. One method uses transfinite recursion on the ordinals, extending the definitions by recursion used for the finite ordinals in Chapter 4. The second method uses our more recent work with order types, and defines $\alpha + \beta$ to be the ordinal $\gamma$ such that $\bar{\alpha} + \bar{\beta} = \bar{\gamma}$ (under addition of order types).

Since both methods have their advantages, we will show that they produce exactly the same operations. We will then be able to draw on either method as the occasion demands.

We will say that an order type $\rho$ is well ordered iff the structures of type $\rho$ are well ordered.

Theorem 8J The sum and the product of well-ordered types is again well ordered.

Proof Assume that $\langle A, R \rangle$ and $\langle B, S \rangle$ are well-ordered structures with $A$ and $B$ disjoint. What is to be proved is that $\langle A \cup B, R \oplus S \rangle$ and $\langle A \times B, R * S \rangle$ are well-ordered structures. If $C$ is a nonempty subset of $A \cup B$ , then either $C \cap A \neq \emptyset$ (in which case its $R$ -least element is $(R \oplus S)$ -least in $C$ ) or else $C \subseteq B$ (in which case its $S$ -least element is $(R \oplus S)$ -least. Similarly if $D$ is a nonempty subset of $A \times B$ , we first take the $S$ -least $b_0$ in ran $D$ . Let $a_0$ be the $R$ -least member of $\{a \mid \langle a, b_0 \rangle \in D\}$ . Then $\langle a_0, b_0 \rangle$ is the $(R * S)$ -least element of $D$ .

The above theorem lets us transfer addition and multiplication from well-ordered types directly to the ordinals. For ordinals $\alpha$ and $\beta$ , we have the wellordered types $\bar{\alpha} + \bar{\beta}$ and $\bar{\alpha} \cdot \bar{\beta}$ . The ordinals of these types are defined to be $\alpha + \beta$ and $\alpha \cdot \beta$ .

Definition Let $\alpha$ and $\beta$ be ordinal numbers. Define the sum $\alpha + \beta$ to be the unique ordinal $\gamma$ such that $\bar{\alpha} + \bar{\beta} = \bar{\gamma}$ . Define the product $\alpha \cdot \beta$ to be the unique ordinal $\delta$ such that $\bar{\alpha} \cdot \bar{\beta} = \bar{\delta}$ .

To be more specific, observe that $\bar{\alpha} +\bar{\beta}$ is the order type of

$$
(\{0 \} \times \alpha) \cup (\{1 \} \times \beta)
$$

in lexicographic order $<_{L}$ (compare Exercise 12). Consequently $\alpha + \beta$ is the ordinal number of the structure

$$
\langle (\{0 \} \times \alpha) \cup (\{1 \} \times \beta), <   _ {L} \rangle .
$$

This is the ordinal number that measures the “first $\alpha$ and then $\beta$ ” ordering. Similarly $\bar{\alpha} \cdot \bar{\beta}$ is the order type of $\alpha \times \beta$ with Hebrew lexicographic order $<_{H}$ . Consequently $\alpha \cdot \beta$ is the ordinal number of the structure $\langle\alpha \times \beta, <_{H}\rangle$ . This is the ordinal number that measures the “ $\alpha$ , $\beta$ times” ordering.

We use the same symbols + and $\cdot$ for both order type arithmetic and ordinal arithmetic, but we will try always to be clear about which is intended.

Example To calculate the sum $1 + \omega$ , we shift to the order types $\bar{1} + \bar{\omega}$ . From a previous example $\bar{1} + \bar{\omega} = \bar{\omega}$ , so going back to ordinals we have $1 + \omega = \omega$ . Similarly from the known equations $\bar{\omega} + \bar{1} = \overline{\omega^{+}}$ and $\bar{2} \cdot \bar{\omega} = \bar{\omega}$ , we obtain the corresponding equations for ordinals: $\omega + 1 = \omega^{+}$ and $2 \cdot \omega = \omega$ .

Example We claim that $\alpha + 1 = \alpha^{+}$ for any ordinal $\alpha$ . The sum $\bar{\alpha} + \bar{1}$ is the order type of $\alpha \cup \{s\}$ (where $s \notin \alpha$ ) under the ordering that makes s the largest element. This is the same as the order type of $\alpha \cup \{\alpha\}$ under the epsilon ordering, which is just $\overline{\alpha^{+}}$ . So we have $\bar{\alpha} + \bar{1} = \overline{\alpha^{+}}$ , whereupon $\alpha + 1 = \alpha^{+}$ .

Note that the definition of ordinal addition and multiplication yields the equations

$$
\bar {\alpha} + \bar {\beta} = \overline {{{{\alpha + \beta}}}} \quad \text { and } \quad \bar {\alpha} \cdot \bar {\beta} = \overline {{{{\alpha \cdot \beta}}}}.
$$

To verify an equation, e.g., $\omega \cdot 2 = \omega + \omega$ , we can use the following strategy. If suffices to show that the order types $\overline{\omega \cdot 2}$ and $\overline{\omega + \omega}$ are the same, since the assignment of order types to ordinals is one-to-one. By the above equations, this reduces to verifying that $\bar{\omega} \cdot \bar{2} = \bar{\omega} + \bar{\omega}$ . And this can be done by selecting representative structures for each side of the equation and showing them to be isomorphic. In recent notation, the fact that

$$
\langle \omega \times 2, <   _ {\mathrm{H}} \rangle \cong \langle (\{0 \} \times \omega) \cup (\{1 \} \times \omega), <   _ {\mathrm{L}} \rangle
$$

does the job. (Alternatively, we can appeal to the next theorem to obtain $\omega \cdot 2 = \omega + \omega$ .)

The laws previously established for all order types must in particular be valid for ordinals:

Theorem 8K For any ordinal numbers:

$$
\begin{array}{r} (\alpha + \beta) + \gamma = \alpha + (\beta + \gamma), \\ (\alpha \cdot \beta) \cdot \gamma = \alpha \cdot (\beta \cdot \gamma), \\ \alpha \cdot (\beta + \gamma) = (\alpha \cdot \beta) + (\alpha \cdot \gamma), \\ \alpha + 0 = 0 + \alpha = \alpha , \\ \alpha \cdot 1 = 1 \cdot \alpha = \alpha , \\ \alpha \cdot 0 = 0 \cdot \alpha = 0. \end{array}
$$

Proof We know from Theorem 8I that addition of order types is associative, so

$$
(\bar {\alpha} + \bar {\beta}) + \bar {\gamma} = \bar {\alpha} + (\bar {\beta} + \bar {\gamma}).
$$

Hence the ordinals $(\alpha + \beta) + \gamma$ and $\alpha + (\beta + \gamma)$ have the same order type, and thus are equal. The same argument is applicable to the other parts of the theorem.

Our work with order types also provides us with counterexamples to the commutative laws and the right distributive laws:

$$
\begin{array}{c} 1 + \omega \neq \omega + 1, \\ 2 \cdot \omega \neq \omega \cdot 2, \\ (\omega + 1) \cdot 2 \neq (\omega \cdot 2) + (1 \cdot 2). \end{array}
$$

The next theorem gives the equations that characterize addition and multiplication by recursion. Recall that for a set S of ordinals, its supremum sup S is just $\bigcup S$ .

Theorem 8L For any ordinal numbers $\alpha$ and $\beta$ and any limit ordinal $\lambda$ the following equations hold.

(A1)

$$
\alpha + 0 = \alpha ,\tag{A2}
$$

$$
\alpha + \beta^ {+} = (\alpha + \beta) ^ {+},\tag{A3}
$$

$$
\alpha + \lambda = \sup \{\alpha + \beta \mid \beta \in \lambda \},\tag{M1}
$$

$$
\alpha \cdot 0 = 0,\tag{M2}
$$

$$
\alpha \cdot \beta^ {+} = \alpha \cdot \beta + \alpha ,\tag{M3}
$$

$$
\alpha \cdot \lambda = \sup \{\alpha \cdot \beta \mid \beta \in \lambda \}.
$$

Proof (A1) and (M1) are contained in the previous theorem. To prove (A2), recall that $\beta^{+} = \beta + 1$ . Hence

$$
\begin{array}{r l} \alpha + \beta^ {+} & = \alpha + (\beta + 1) \\ & = (\alpha + \beta) + 1 \\ & = (\alpha + \beta) ^ {+}. \end{array}
$$

Similarly for (M2) we have

$$
\begin{array}{r l} \alpha \cdot \beta^ {+} & = \alpha \cdot (\beta + 1) \\ & = (\alpha \cdot \beta) + (\alpha \cdot 1) \\ & = (\alpha \cdot \beta) + \alpha . \end{array}
$$

It remains to prove (A3) and (M3). For that proof we need a lemma on chains of well orderings. Say that a structure $\langle B, <_{B} \rangle$ is an end extension of a structure $\langle A, <_{A} \rangle$ iff $A \subseteq B$ , $<_{A} \subseteq <_{B}$ , and every element of $B - A$ is larger than anything in $A$ :

$$
a \in A \& b \in B - A \Rightarrow a <   _ {B} b.
$$

Lemma 8M Assume that C is a set of well-ordered structures. Further assume that if $\langle A, <_{A}\rangle$ and $\langle B, <_{B}\rangle$ are structures in C, then one is an end extension of the other. Let $\langle W, <_{W}\rangle$ be the union of all these structures in the sense that

$$
\begin{array}{l} W = \bigcup \{A \mid \langle A, <   _ {A} \rangle \in \mathscr {C} \text {   for   some   } <   _ {A} \}, \\ <   _ {W} = \bigcup \{<   _ {A} \mid \langle A, <   _ {A} \rangle \in \mathscr {C} \text {   for   some   } A \}. \end{array}
$$

Then $\langle W, <_{w}\rangle$ is a well-ordered structure whose ordinal number is the supremum of the ordinals of the members of C.

Proof of the Lemma For each structure $\langle A, <_{A} \rangle$ in $\mathcal{C}$ , we have the usual isomorphism $E_{A}$ onto its ordinal number, ordered by epsilon. If $\langle B, <_{B} \rangle$ is an end extension of $\langle A, <_{B} \rangle$ , then $E_{B}$ is an extension of $E_{A}$ , i.e., $E_{A} = E_{B} \upharpoonright A$ . (This is easy to see, but formally we verify $E_{A}(a) = E_{B}(a)$ by induction on $a$ in $A$ .) Thus the set of all possible $E_{A}$ 's

$$
\left\{E _ {A} \mid \langle A, <   _ {A} \rangle \in \mathscr {C} \text {   for   some   } <   _ {A} \right\}
$$

is a chain of one-to-one functions. So its union (call it E) is a one-to-one function. The domain of E is the union of all possible A's; that is, dom E = W. The range of E is the union (supremum) of the ordinals of the structures in C; call this ordinal $\theta$ . Thus E maps W one-to-one onto $\theta$ .

Furthermore it preserves order:

$$
\begin{array}{l l l l} x <   _ {W} y & \Leftrightarrow & x <   _ {A} y & \text {   for   some   } A \text {   in   } \mathscr {C} \\ & \Leftrightarrow & E _ {A} (x) \in E _ {A} (y) & \text {   for   some   } A \text {   in   } \mathscr {C} \\ & \Leftrightarrow & E (x) \in E (y). \end{array}
$$

Thus $E$ is an isomorphism of $\langle W, <_{W} \rangle$ onto $\langle \theta, \in_{\theta} \rangle$ . Hence $\langle W, <_{W} \rangle$ is well ordered, and its ordinal is $\theta$ .

Now return to the proof of Theorem 8L. Since $\lambda$ is a limit ordinal, we have $\lambda = \bigcup \lambda$ . The sum $\alpha + \lambda$ is the ordinal number of the following set (under lexicographic order):

$$
\begin{array}{r l} (\{0 \} \times \alpha) \cup (\{1 \} \times \lambda) & = (\{0 \} \times \alpha) \cup (\{1 \} \times \bigcup \{\beta \mid \beta \in \lambda \}) \\ & = (\{0 \} \times \alpha) \cup \bigcup \{\{1 \} \times \beta \mid \beta \in \lambda \} \\ & = \bigcup \{(\{0 \} \times \alpha) \cup (\{1 \} \times \beta) \mid \beta \in \lambda \} \\ & = \bigcup \{A _ {\beta} \mid \beta \in \lambda \}, \end{array}
$$

where $A_{\beta} = (\{0\} \times \alpha) \cup (\{1\} \times \beta)$ . The ordinal of $A_{\beta}$ (under lexicographic order) is $\alpha + \beta$ . The ordinal of $\bigcup \{A_{\beta} \mid \beta \in \lambda\}$ is provided by the lemma. Once we verify that the lemma is applicable, it will tell us that the ordinal of $\bigcup \{A_{\beta} \mid \beta \in \lambda\}$ is $\sup \{\alpha + \beta \mid \beta \in \lambda\}$ , which is what we need for (A3).

For any $\beta$ and $\gamma$ in $\lambda$ , either $\beta \in \gamma$ or $\gamma \in \beta$ . If it is the former, then $A_{\gamma}$ (under lexicographic order) is clearly an end extension of $A_{\beta}$ . Thus the lemma is applicable.

The proof of (M3) is similar. The product $\alpha \cdot \lambda$ is the ordinal number of $\alpha \times \lambda$ under $<_{\mathbf{H}}$ , Hebrew lexicographic order:

$$
\begin{array}{c} \alpha \times \lambda = \alpha \times \bigcup \{\beta \mid \beta \in \lambda \} \\ = \bigcup \{\alpha \times \beta \mid \beta \in \lambda \} \end{array}
$$

and the ordinal of $\alpha \times \beta$ is $\alpha \cdot \beta$ . Again the lemma is applicable, because whenever $\beta \in \gamma$ , then $\alpha \times \gamma$ is an end extension of $\alpha \times \beta$ (under $<_{\mathbf{H}}$ ). The lemma tells us that the ordinal of $\bigcup \{\alpha \times \beta \mid \beta \in \lambda\}$ is $\sup \{\alpha \cdot \beta \mid \beta \in \lambda\}$ , which completes the proof of (M3).

For finite ordinals (the natural numbers) we have now defined addition and multiplication three times: first in Chapter 4 (by recursion), then in Chapter 6 (as finite cardinals), and now again (by use of order types). All three agree on the natural numbers; Theorem 8L shows that the recent definition is in agreement with Chapter 4.

Theorem 8L also indicates how addition and multiplication could have been (equivalently) defined by transfinite recursion on the ordinals. The six equations in the theorem describe how, for fixed $\alpha$ , to form $\alpha + \beta$ from earlier values $\alpha + \gamma$ for $\gamma$ less than $\beta$ .

We will give the details of this approach of exponentiation, but they are easily modified to cover addition and multiplication. Consider then, a fixed nonzero ordinal $\alpha$ . We propose to define $\alpha^{\beta}$ in such a way as to satisfy the following three equations:

(E1)

$$
\alpha^ {0} = 1,\tag{E2}
$$

$$
\alpha^ {\beta^ {+}} = \alpha^ {\beta} \cdot \alpha ,\tag{E3}
$$

$$
\alpha^ {\lambda} = \sup \{\alpha^ {\beta} \mid \beta \in \lambda \}
$$

for a limit ordinal $\lambda$ .

Now we activate the transfinite recursion machinery. The procedure is similar to that used for the beth operation. Let $\gamma(f, y)$ be the formula:

Either (i) $f$ is a function with domain 0 and $y = 1$ , or (ii) $f$ is a function whose domain is a successor ordinal $\beta^{+}$ and $y = f(\beta) \cdot \alpha$ ,

or (iii) $f$ is a function whose domain is a limit ordinal $\lambda$ and $y = \bigcup \operatorname{ran} f$ ,

or (iv) none of the above and $y = \emptyset$ .

Then transfinite recursion replies with a formula $\varphi$ that will define the exponentiation operation. We select the symbol “ $_{\alpha}E$ ” and define

$$
_ {\alpha} E _ {\beta} = \text { the   unique } y \text { such   that } \varphi (\beta , y)
$$

for every ordinal $\beta$ . Then we are assured that “ $\gamma_{(\alpha}E \upharpoonright \beta, _{\alpha}E_{\beta)}$ ”. For $\beta = 0$ , this fact becomes

$$
_ {\alpha} E _ {0} = 1.
$$

For a successor ordinal $\beta^{+}$ in place of $\beta$ it becomes

$$
{ } _ { \alpha } E _ { \beta ^ { + } } = { } _ { \alpha } E _ { \beta } \cdot \alpha
$$

and for a limit ordinal $\lambda$ in place of $\beta$ it becomes

$$
{ } _ { \alpha } E _ { \lambda } = \operatorname * { s u p } \{ _ { \alpha } E _ { \gamma } \mid \gamma \in \lambda \} .
$$

These three displayed equations are (E1)-(E3), except for notational differences. We henceforth dispense with any special symbol for exponentiation, and instead use the traditional placement of letters:

$$
\alpha^ {\beta} = _ {\alpha} E _ {\beta}.
$$

There is a special problem in defining $0^{\beta}$ . If we were to follow blindly (E1)–(E3), we would have $0^{\omega}=1$ . This is undesirable, which is our reason for having specified in the foregoing that $\alpha$ is a fixed nonzero ordinal. We can simply define $0^{\beta}$ directly: $0^{0}=1$ and $0^{\beta}=0$ for $\beta\neq0$ .

Example We have $2^{\omega} = \sup\{2^{n} \mid n \in \omega\} = \omega$ . Thus ordinal exponentiation is very different from cardinal exponentiation, since $2^{\kappa} \neq \kappa$ for cardinals. Ordinal addition and multiplication are also very different from cardinal addition and multiplication. Please do not confuse them. Theorem 6J tells us that the operations agree on finite numbers; that theorem does not extend to infinite numbers.

We can now apply our remarks on ordinal operations to derive information concerning ordinal arithmetic. Consider a fixed ordinal number $\alpha$ . Then the operation of $\alpha$ -addition is the operation assigning to each ordinal $\beta$ the sum $\alpha + \beta$ . (In our earlier notation, $t_{\beta} = \alpha + \beta$ , where $\alpha$ is fixed.) Similarly, the operation of $\alpha$ -multiplication assigns to $\beta$ the product $\alpha \cdot \beta$ , and $\alpha$ -exponentiation assigns to $\beta$ the power $\alpha^{\beta}$ .

Theorem 8N (a) For any ordinal number $\alpha$ , the operation of $\alpha$ -addition is normal.

(b) If $1 \in \alpha$ , then the operation of $\alpha$ -multiplication is normal.

(c) If $2 \in \alpha$ , then the operation of $\alpha$ -exponentiation is normal.

Proof Continuity is immediate from (A3) and (M3) of Theorem 8L and from (E3). For monotonicity, we use Theorem 8C, which tells us that it suffices to show that:

$$
\begin{array}{c c} \alpha + \beta \in \alpha + \beta^ {+}, \\ \alpha \cdot \beta \in \alpha \cdot \beta^ {+} & \text {if} 1 \subseteq \alpha , \\ \alpha^ {\beta} \in \alpha^ {\beta^ {+}} & \text {if} 2 \subseteq \alpha . \end{array}
$$

The first of these is immediate from (A2) of Theorem 8L:

$$
\alpha + \beta \in (\alpha + \beta) ^ {+} = \alpha + \beta^ {+},
$$

whence $\alpha$ -addition is normal.

For multiplication we have

$$
1 \in \alpha \Rightarrow 0 \in \alpha
$$

and so by the monotonicity of $(\alpha \cdot \beta)$ -addition,

$$
\alpha \cdot \beta \in \alpha \cdot \beta + \alpha .
$$

This together with (M2) gives $\alpha \cdot \beta \in \alpha \cdot \beta^{+}$ .

Exponentiation is similar;

$$
2 \in \alpha \Rightarrow 1 \in \alpha ,
$$

whence by the monotonicity of $\alpha^{\beta}$ -multiplication and (E3)

$$
\alpha^ {\beta} \in \alpha^ {\beta} \cdot \alpha = \alpha^ {\beta +}.
$$

This completes the proof.

Example Assume that $\lambda$ is a limit ordinal. By Exercise 4, $t_{\lambda}$ (for a normal operation) is also a limit ordinal. So by the preceding theorem, $\alpha + \lambda$ is a limit ordinal for any ordinal $\alpha$ . If $1 \in \alpha$ , then both $\alpha \cdot \lambda$ and $\lambda \cdot \alpha$ are limit ordinals. (In the second case we use the fact that $\lambda \cdot \beta^{+} = \lambda \cdot \beta + \lambda$ .) Similarly if $2 \in \alpha$ , then both $\alpha^{\lambda}$ and $\lambda^{\alpha}$ are limit ordinals.

Corollary 8P (a) The following order-preserving laws hold.

$$
\beta \in \gamma \Leftrightarrow \alpha + \beta \in \alpha + \gamma .
$$

If $1 \in \alpha$ , then

$$
\beta \in \gamma \Leftrightarrow \alpha \cdot \beta \in \alpha \cdot \gamma .
$$

If $2 \in \alpha$ , then

$$
\beta \in \gamma \Leftrightarrow \alpha^ {\beta} \in \alpha^ {\gamma}.
$$

(b) The following left cancellation laws hold:

$$
\alpha + \beta = \alpha + \gamma \Rightarrow \beta = \gamma .
$$

If $1 \in \alpha$ , then

$$
\alpha \cdot \beta = \alpha \cdot \gamma \Rightarrow \beta = \gamma .
$$

If $2 \in \alpha$ , then

$$
\alpha^ {\beta} = \alpha^ {\gamma} \Rightarrow \beta = \gamma .
$$

Proof These are consequences of monotonicity. Any monotone operation assigning $t_{\beta}$ to $\beta$ has the properties

$$
\begin{array}{r c l} \beta \in \gamma & \Leftrightarrow & t _ {\beta} \in t _ {\gamma}, \\ t _ {\beta} = t _ {\gamma} & \Rightarrow & \beta = \gamma , \end{array}
$$

by Exercise 3.

Part (b) of this theorem gives only left cancellation laws. Right cancellation laws fail in general. For example,

$$
\begin{array}{c} {2 + \omega = 3 + \omega = \omega ,} \\ {2 \cdot \omega = 3 \cdot \omega = \omega ,} \\ {2 ^ {\omega} = 3 ^ {\omega} = \omega ,} \end{array}
$$

but we cannot cancel the $\omega$ 's to get $2 = 3$ . There is a weakened version of part (a) that holds:

Theorem 8Q The following weak order-preserving laws hold for any ordinal numbers:

(a) $\beta \in \gamma \Rightarrow \beta + \alpha \in \gamma + \alpha.$

(b) $\beta \in \gamma \Rightarrow \beta \cdot \alpha \in \gamma \cdot \alpha.$

(c) $\beta \in \gamma \Rightarrow \beta^{\alpha} \in \gamma^{\alpha}$ .

Proof Each part can be proved by transfinite induction on $\alpha$ . But parts (a) and (b) also can be proved using concepts from order types. Assume that $\beta \in \gamma$ ; then also $\beta \subseteq \gamma$ . Thus

$$
(\{0 \} \times \beta) \cup (\{1 \} \times \alpha) \subseteq (\{0 \} \times \gamma) \cup (\{1 \} \times \alpha)
$$

and $\beta \times \alpha \subseteq \gamma \times \alpha$ . Furthermore in each case the relevant ordering (lexicographic and Hebrew lexicographic, respectively) on the subset is the restriction of the ordering on the larger set. Hence when we take the ordinal numbers of the sets, we get $\beta + \alpha \in \gamma + \alpha$ and $\beta \cdot \alpha \in \gamma \cdot \alpha$ (compare Exercise 17 of Chapter 7).

We will prove (c) by transfinite induction on $\alpha$ . So suppose that $\beta \in \gamma$ and that $\beta^{\delta} \subseteq \gamma^{\delta}$ whenever $\delta \in \alpha$ ; we must show that $\beta^{\alpha} \in \gamma^{\alpha}$ . If $\alpha = 0$ , then $\beta^{\alpha} = \gamma^{\alpha} = 1$ . Next take the case where $\alpha$ is a successor ordinal $\delta^{+}$ . Then

$$
\begin{array}{l l} \beta^ {\alpha} = \beta^ {\delta} \cdot \beta \\ \quad \subseteq \gamma^ {\delta} \cdot \beta & \text { since } \quad \beta^ {\delta} \in \gamma^ {\delta} \\ \quad \subseteq \gamma^ {\delta} \cdot \gamma & \text { by   Corollary   8P } \\ = \gamma^ {\alpha}. \end{array}
$$

Finally take the case where $\alpha$ is a limit ordinal. We may suppose that neither $\beta$ nor $\gamma$ is 0, since those cases are clear. Since $\beta^{\delta} \in \gamma^{\delta}$ for $\delta$ in $\alpha$ , we have

$$
\beta^ {\alpha} = \sup \left\{\beta^ {\delta} \mid \delta \in \alpha \right\} \in \sup \left\{\gamma^ {\delta} \mid \delta \in \alpha \right\} = \gamma^ {\alpha},
$$

whence $\beta^{\alpha} \in \gamma^{\alpha}$ .

It is not possible to replace “ $\underline{\in}$ ” by “ $\in$ ” in the above theorem, since

$$
\begin{array}{c} 2 + \omega \notin 3 + \omega , \\ 2 \cdot \omega \notin 3 \cdot \omega , \\ 2 ^ {\omega} \notin 3 ^ {\omega}, \end{array}
$$

despite the fact that $2 \in 3$ .

Subtraction Theorem If $\alpha \in \beta$ (for ordinal numbers $\alpha$ and $\beta$ ), then there exists a unique ordinal number $\delta$ (their “difference”) such that $\alpha + \delta = \beta$ .

Proof The uniqueness of $\delta$ is immediate from the left cancellation law (Corollary 8P). We will indicate two proofs of existence.

Since $\alpha$ -addition is a normal operation and $\beta$ is at least as large as $\alpha + 0$ , we know from Theorem 8D that there is a largest $\delta$ for which $\alpha + \delta \in \beta$ . But equality must hold, for if $\alpha + \delta \in \beta$ , then

$$
\alpha + \delta^ {+} = (\alpha + \delta) ^ {+} \in \beta
$$

contradicting the maximality of $\delta$ .

The other proof starts from the fact that $\beta - \alpha$ (i.e., $\{x \in \beta \mid x \notin \alpha\}$ ) is well ordered by epsilon. Let $\delta$ be its ordinal. Then $\alpha + \delta$ is the ordinal of $(\{0\} \times \alpha) \cup (\{1\} \times (\beta - \alpha))$ under lexicographic order, which is isomorphic to $\beta$ under the epsilon ordering.

For example, if $\alpha = 3$ and $\beta = \omega$ , then the “difference” is $\omega$ , since $3 + \omega = \omega$ . If $\alpha \in \beta$ , we cannot in general find a $\delta$ for which $\delta + \alpha = \beta$ ; for example, there is no $\delta$ for which $\delta + 3 = \omega$ . (Why?)

Division Theorem Let $\alpha$ and $\delta$ be ordinal numbers with $\delta$ (the divisor) nonzero. Then there is a unique pair of ordinal numbers $\beta$ and $\gamma$ (the quotient and the remainder) such that

$$
\alpha = \delta \cdot \beta + \gamma \quad \text { and } \quad \gamma \in \delta .
$$

Proof First we will prove existence. Since $\delta$ -multiplication is a normal operation, there is a largest $\beta$ for which $\delta \cdot \beta \in \alpha$ . Then by the subtraction theorem there is some $\gamma$ for which $\delta \cdot \beta + \gamma = \alpha$ . We must show that $\gamma \in \delta$ . If to the contrary $\delta \in \gamma$ , then

$$
\delta \cdot \beta^ {+} = \delta \cdot \beta + \delta \in \delta \cdot \beta + \gamma = \alpha ,
$$

contradicting the maximality of $\beta$ .

Having established existence, we now turn to uniqueness. Assume that

$$
\alpha = \delta \cdot \beta_ {1} + \gamma_ {1} = \delta \cdot \beta_ {2} + \gamma_ {2},
$$

where $\gamma_{1}$ and $\gamma_{2}$ are less than $\delta$ . To show that $\beta_{1} = \beta_{2}$ , it suffices to eliminate the alternatives. Suppose, contrary to our hopes, that $\beta_{1} \in \beta_{2}$ . Then $\beta_{1}^{+} \in \beta_{2}$ and so $\delta \cdot (\beta_{1}^{+}) \in \delta \cdot \beta_{2}$ . Since $\gamma_{1} \in \delta$ , we have

$$
\alpha = \delta \cdot \beta_ {1} + \gamma_ {1} \in \delta \cdot \beta_ {1} + \delta = \delta \cdot (\beta_ {1} ^ {+}) \subseteq \delta \cdot \beta_ {2} \subseteq \delta \cdot \beta_ {2} + \gamma_ {2} = \alpha .
$$

But this is impossible, so $\beta_{1} \notin \beta_{2}$ . By symmetry, $\beta_{2} \notin \beta_{1}$ . Hence $\beta_{1} = \beta_{2}$ ; call it simply $\beta$ . We now have

$$
\alpha = \delta \cdot \beta + \gamma_ {1} = \delta \cdot \beta + \gamma_ {2},
$$

whence by left cancellation (Corollary 8P), $\gamma_{1} = \gamma_{2}$ .

Digression Ordinal addition and multiplication are often introduced by transfinite recursion instead of by order types. In that case, the foregoing theorems can be used to establish the connection with order types, without need of Theorem 8L or Lemma 8M. The statements to be proved are those that we took in our development as definitions: The order type of an ordinal sum (or product) is the sum (or product) of the order types. That is, the equations

$$
\overline {{{{\alpha + \beta}}}} = \bar {\alpha} + \bar {\beta} \quad \text { and } \quad \overline {{{{\alpha \cdot \beta}}}} = \bar {\alpha} \cdot \bar {\beta}
$$

are, in this alternative development, to be proved. For addition, it suffices to give an isomorphism from $(\{0\} \times \alpha) \cup (\{1\} \times \beta)$ with lexicographic ordering onto $\alpha + \beta$ with epsilon ordering. The isomorphism f is defined by the equations

$$
\begin{array}{l l} f (\langle 0, \gamma \rangle) = \gamma & \text { for } \quad \gamma \text { in } \alpha , \\ f (\langle 1, \delta \rangle) = \alpha + \delta & \text { for } \quad \delta \text { in } \beta . \end{array}
$$

Then it can be verified that ran $f = \alpha + \beta$ and that f preserves order. For multiplication, the isomorphism g from $\alpha \times \beta$ with Hebrew lexicographic order onto $\alpha \cdot \beta$ with epsilon ordering is defined by the equation

$$
g (\langle \gamma , \delta \rangle) = \alpha \cdot \delta + \gamma
$$

for $\gamma$ in $\alpha$ and $\delta$ in $\beta$ . Again it can be verified that ran $g = \alpha \cdot \beta$ and that g preserves order.

Logarithm Theorem Assume that $\alpha$ and $\beta$ are ordinal numbers with $\alpha \neq 0$ and $\beta$ (the base) greater than 1. Then there are unique ordinal numbers $\gamma$ , $\delta$ , and $\rho$ (the logarithm, the coefficient, and the remainder) such that

$$
\alpha = \beta^ {\gamma} \cdot \delta + \rho \& 0 \neq \delta \in \beta \& \rho \in \beta^ {\gamma}.
$$

Proof Since $\beta$ -exponentiation is a normal operation, there is (by Theorem 8D) a largest $\gamma$ such that $\beta^{\gamma} \in \alpha$ . Apply the division theorem to $\alpha \div \beta^{\gamma}$ to obtain $\delta$ and $\rho$ such that

$$
\alpha = \beta^ {\gamma} \cdot \delta + \rho \quad \text { and } \quad \rho \in \beta^ {\gamma}.
$$

Note that $\delta\neq0$ since $\rho\in\beta^{\gamma}\in\alpha$ . We must show that $\delta\in\beta$ . If to the contrary $\beta\in\delta$ , then $\beta^{\gamma^{+}}=\beta^{\gamma}\cdot\beta\in\beta^{\gamma}\cdot\delta\in\beta^{\gamma}\cdot\delta+\rho=\alpha$ , contradicting the maximality of $\gamma$ . Thus we have the existence of $\gamma,\delta,$ and $\rho$ meeting the prescribed conditions.

To show uniqueness, consider any representation $\alpha = \beta^{\gamma} \cdot \delta + \rho$ for which $0 \neq \delta \in \beta$ and $\rho \in \beta$ . We first claim that $\gamma$ must be exactly the one we used in the preceding paragraph. We have

$$
\begin{array}{l l} \beta^ {\gamma} \in \alpha = \beta^ {\gamma} \cdot \delta + \rho & \text { since } 1 \in \delta \\ \in \beta^ {\gamma} \cdot \delta + \beta^ {\gamma} & \text { since } \rho \in \beta^ {\gamma} \\ = \beta^ {\gamma} \cdot \delta^ {+} \\ \in \beta^ {\gamma} \cdot \beta & \text { since } \delta \in \beta \\ = \beta^ {\gamma^ {+}}. \end{array}
$$

Thus $\beta^{\gamma} \in \alpha \in \beta^{\gamma^{+}}$ . This double inequality uniquely determines $\gamma$ ; it must be the largest ordinal for which $\beta^{\gamma} \in \alpha$ . Once $\gamma$ is fixed, the division theorem tells us that $\delta$ and $\rho$ are unique.

Observe that in the logarithm theorem, we always have $\rho\in\beta^{\gamma}\in\alpha$ . An interesting special case is where the base $\beta$ is $\omega$ . Then given any nonzero ordinal $\alpha$ , we can write

$$
\alpha = \omega^ {\gamma_ {1}} \cdot n _ {1} + \rho_ {1},
$$

where $n_1$ is a nonzero natural number and $\rho_1 \in \omega^{\gamma_1} \in \alpha$ . If $\rho_1$ is nonzero, then we can repeat:

$$
\rho_ {1} = \omega^ {\gamma_ {2}} \cdot n _ {2} + \rho_ {2},
$$

where $n_{2}$ is a nonzero natural number and $\rho_{2}\in\omega^{\gamma_{2}}\subseteq\rho_{1}\in\omega^{\gamma_{1}}$ . Hence both $\rho_{2}\in\rho_{1}$ and $\gamma_{2}\in\gamma_{1}$ . Continuing in this way, we construct progressively smaller ordinals $\rho_{1},\rho_{2},\ldots$ . This descending chain cannot be infinite, so $\rho_{k}=0$ for some (finite!) k. We then have $\alpha$ represented as an “ $\omega$ -polynomial”

$$
\alpha = \omega^ {\gamma_ {1}} \cdot n _ {1} + \dots + \omega^ {\gamma_ {k}} \cdot n _ {k},
$$

where $n_{1}, \ldots, n_{k}$ are nonzero natural numbers and $\gamma_{k} \in \gamma_{k-1} \in \cdots \in \gamma_{1}$ . This polynomial representation is called the Cantor normal form of $\alpha$ . You are asked in Exercise 26 to show that it is unique.

Theorem 8R For any ordinal numbers,

$$
\alpha^ {\beta + \gamma} = \alpha^ {\beta} \cdot \alpha^ {\gamma}.
$$

Proof We use transfinite induction on $\gamma$ . In the limit ordinal case we will use the normality of $\alpha$ -exponentiation. But normality is true only for $\alpha$ greater than 1. So a separate proof is needed for the cases $\alpha = 0$ and $\alpha = 1$ . We leave this separate proof, which does not require induction, to you (Exercise 27). Henceforth we assume that $\alpha$ is at least 2.

Suppose, as the inductive hypothesis, that $\alpha^{\beta+\delta}=\alpha^{\beta}\cdot\alpha^{\delta}$ for all $\delta$ less than $\gamma$ ; we must prove that $\alpha^{\beta+\gamma}=\alpha^{\beta}\cdot\alpha^{\gamma}$ .

Case I $\gamma = 0$ . Then on the left side we have $\alpha^{\beta + 0} = \alpha^{\beta}$ . On the right side we have $\alpha^{\beta} \cdot \alpha^{0} = \alpha^{\beta} \cdot 1 = \alpha^{\beta}$ , so this case is done.

Case II $\gamma = \delta^{+}$ for some $\delta$ . Then

$$
\begin{array}{r l} \alpha^ {\beta + \gamma} = \alpha^ {\beta + \delta +} & \\ = \alpha^ {(\beta + \delta) +} & \text {by (A2)} \\ = \alpha^ {\beta + \delta} \cdot \alpha & \text {by (E2)} \\ = \alpha^ {\beta} \cdot \alpha^ {\delta} \cdot \alpha & \text {by the inductive hypothesis} \\ = \alpha^ {\beta} \cdot \alpha^ {\delta +} & \text {by (E2)} \\ = \alpha^ {\beta} \cdot \alpha^ {\gamma}. & \end{array}
$$

(The associative law was also used here.)

Case III $\gamma$ is a limit ordinal. Then

$$
\begin{array}{r l} \alpha^ {\beta + \gamma} = \alpha^ {\sup \{\beta + \delta \mid \delta \in \gamma \}} & \text { by   (A3) } \\ = \sup \{\alpha^ {\beta + \delta} \mid \delta \in \gamma \} & \text { by   Theorem   8E } \\ = \sup \{\alpha^ {\beta} \cdot \alpha^ {\delta} \mid \delta \in \gamma \} & \end{array}
$$

by the inductive hypothesis. On the other side,

$$
\begin{array}{r l} \alpha^ {\beta} \cdot \alpha^ {\gamma} & = \alpha^ {\beta} \cdot \sup \{\alpha^ {\delta} \mid \delta \in \gamma \} \\ & = \sup \{\alpha^ {\beta} \cdot \alpha^ {\delta} \mid \delta \in \gamma \} \end{array}
$$

by Theorem 8E again, this time applied to $\alpha^{\beta}$ -multiplication. Thus the two sides agree.

Theorem 8S For any ordinal numbers,

$$
(\alpha^ {\beta}) ^ {\gamma} = \alpha^ {\beta \cdot \gamma}.
$$

Proof We again use transfinite induction on $\gamma$ . And again we leave to you the case $\alpha = 0$ or $\alpha = 1$ (Exercise 27). Henceforth we assume that $\alpha$ is at least 2.

Suppose, as the inductive hypothesis, that $(\alpha^{\beta})^{\delta} = \alpha^{\beta \cdot \delta}$ for all $\delta$ less than $\gamma$ ; we must prove that $(\alpha^{\beta})^{\gamma} = \alpha^{\beta \cdot \gamma}$ .

Case I $\gamma = 0$ . Obviously both sides are equal to 1.

Case II $\gamma = \delta^{+}$ . Then we calculate

$$
\begin{array}{r l} (\alpha^ {\beta}) ^ {\gamma} & = (\alpha^ {\beta}) ^ {\delta^ {+}} \\ & = (\alpha^ {\beta}) ^ {\delta} \cdot \alpha^ {\beta} \\ & = \alpha^ {\beta \cdot \delta} \cdot \alpha^ {\beta} \quad \text { by   the   inductive   hypothesis } \\ & = \alpha^ {\beta \cdot \delta + \beta} \quad \text { by   the   previous   theorem } \\ & = \alpha^ {\beta \cdot \delta^ {+}} \\ & = \alpha^ {\beta \cdot \gamma} \end{array}
$$

as desired.

Case III $\gamma$ is a limit ordinal. Then

$$
\begin{array}{r l} \alpha^ {\beta \cdot \gamma} = \alpha^ {\sup \{\beta \cdot \delta \mid \delta \in \gamma \}} \\ = \sup \{\alpha^ {\beta \cdot \delta} \mid \delta \in \gamma \} & \text { by   Theorem   8E } \\ = \sup \{(\alpha^ {\beta}) ^ {\delta} \mid \delta \in \gamma \} & \text { by   the   inductive   hypothesis } \\ = (\alpha^ {\beta}) ^ {\gamma} \end{array}
$$

as desired.

Example As with finite numbers, $\alpha^{\beta\gamma}$ always means $\alpha^{(\beta\gamma)}$ . The other grouping, $(\alpha^{\beta})^{\gamma}$ , equals $\alpha^{\beta\cdot\gamma}$ by Theorem 8S. Now suppose that we start with $\omega$ and apply exponentiation over and over again. Let

$$
\varepsilon_ {0} = \sup \{\omega , \omega^ {\omega}, \omega^ {\omega^ {\omega}}, \dots \}.
$$

Then by Theorem 8E

$$
\omega^ {\varepsilon_ {0}} = \sup \{\omega^ {\omega}, \omega^ {\omega \omega}, \dots \} = \varepsilon_ {0}.
$$

The equation $\varepsilon_{0} = \omega^{\varepsilon_{0}}$ gives the Cantor normal form representation for $\varepsilon_{0}$ . More generally, the epsilon numbers are the ordinals $\varepsilon$ for which $\varepsilon = \omega^{\varepsilon}$ . The smallest epsilon number is $\varepsilon_{0}$ . It is a countable ordinal, being the countable union of countable sets. By the Veblen fixed-point theorem, the class of epsilon numbers is unbounded.

## Exercises

20. Show that every ordinal number is expressible in the form $\lambda + n$ where $n \in \omega$ and $\lambda$ is either zero or a limit ordinal. Show further that the representation in this form is unique.

21. In Exercise 4 of Chapter 7, find the ordinal number of $\langle P, R \rangle$ .

22. Prove parts (a) and (b) of Theorem 8Q by transfinite induction on $\alpha$ .

23. (a) Show that $\omega + \omega^2 = \omega^2$ .

(b) Show that whenever $\omega^2 \in \beta$ , then $\omega + \beta = \beta$ .

24. Assume that $\omega \in \alpha$ and $\alpha^2 \subseteq \beta$ . Show that $\alpha + \beta = \beta$ . (This generalizes the preceding exercise.)

25. Consider any fixed ordinals $\alpha$ and $\theta$ . Show that

$$
\alpha + \theta = \alpha \cup \{\alpha + \delta \mid \delta \in \theta \}.
$$

26. Prove that the representation of an ordinal number in Cantor normal form is unique.

27. Supply proofs for Theorem 8R and Theorem 8S when $\alpha$ is 0 or 1.

28. Show that for any given ordinal number, there is a larger epsilon number.

29. Show that the class of epsilon numbers is closed, i.e., if S is a non-empty set of epsilon numbers, then sup S is an epsilon number.

# SPECIAL TOPICS

In this final chapter, we present three topics that stand somewhat apart from our previous topics, yet are too interesting to omit from the book. The three sections are essentially independent.

## WELL-FOUNDED RELATIONS

Some of the important properties of well orderings (such as transfinite induction and recursion) depend more on the “well” than on the “ordering.” In this section, we extend those properties to a larger class of relations.

Recall that for a partial ordering R and a set, D, an element m of D was said to be a minimal element if there was no x in D with xRm. This terminology can actually be applied to any set R:

Definition An element $m$ of a set $D$ is said to be an $R$ -minimal element of $D$ iff there is no $x$ in $D$ for which $xRm$ .

Definition A relation $R$ is said to be well founded iff every nonempty set $D$ contains an $R$ -minimal element.

If the set D in this definition is not a subset of fld R, then it is certain to contain an R-minimal element (namely any m in D - fld R). Thus the only sets D that matter here are the subsets of fld R.

Examples The finite relation

$$
R = \{\langle 1, 2 \rangle , \langle 2, 6 \rangle , \langle 3, 6 \rangle \}
$$

is well founded. Its field is $\{1, 2, 3, 6\}$ , and all fifteen nonempty subsets of the field have R-minimal elements. The empty relation is also well founded, but for uninteresting reasons.

Example Consider any set S and the membership relation

$$
\epsilon_ {s} = \{\langle x, y \rangle \in S \times S \mid x \in y \}
$$

on S. Then we can show from the regularity axiom that $\in_{s}$ is well founded. For consider any nonempty set D. By regularity there some m in D with $m \cap D = \varnothing$ , i.e., there is no x in D with $x \in m$ . So certainly there is no x in D with $x \in_{s} m$ . Hence m is $\in_{s}$ -minimal in D. In fact the regularity axiom can be summarized by the statement: The membership relation is well founded.

The following theorem extends Theorem 7B, which asserted that a linear ordering was a well ordering iff it had no descending chains.

Theorem 9A A relation R is well founded iff there is no function f with domain $\omega$ such that $f(n^{+})Rf(n)$ for each n.

Proof The proof is exactly the same as for Theorem 7B. If $R$ is not well founded, then there exists a nonempty set $A$ without an $R$ -minimal element, i.e., $(\forall x \in A)(\exists y \in A)yRx$ . So we can apply Exercise 20 of Chapter 6 to obtain a descending chain.

If R is a binary relation on A (i.e., $R \subseteq A \times A$ ) that is well founded, then we can say that R is a well-founded relation on A or that $\langle A, R \rangle$ is a well-founded structure.

Transfinite Induction Principle Assume that R is a well-founded relation on A. Assume that B is a subset of A with the special property that for every t in A,

$$
\{x \in A \mid x R t \} \subseteq B \Rightarrow t \in B.
$$

Then $B$ coincides with $A$ .

This theorem is the direct analogue of the transfinite induction principle for well-ordered relations (in Chapter 7). It asserts that any R-inductive subset of A must actually be A itself. In fact the earlier theorem is a special case of the above theorem, wherein R linearly orders A.

Proof The proof is the same as before. If $B$ is a proper subset of $A$ , then $A - B$ has an $R$ -minimal element $m$ . By the minimality, $\{x \in A \mid xRm\} \subseteq B$ . But then by the special property of $B$ (the property of being $R$ -inductive), $m \in B$ after all.

Next we want to describe how any relation R (well founded or not) can be extended to $R^{t}$ , the smallest transitive relation extending R.

Theorem 9B Let $R$ be a relation. Then there exists a unique relation $R^{\mathrm{t}}$ such that:

(a) $R^{\mathrm{t}}$ is a transitive relation and $R\subseteq R^{\mathrm{t}}$

(b) If $Q$ is any transitive relation that includes $R$ , then $R^{\mathfrak{t}} \subseteq Q$ .

Proof There are two equivalent ways to obtain $R^{t}$ . The brute force method is to define $R^{*}$ “from above” by

$$
R ^ {*} = \bigcap \{Q \mid R \subseteq Q \subseteq \operatorname{fld} R \times \operatorname{fld} R \& Q \text {   is   a   transitive   relation } \}.
$$

The collection of all such $Q$ 's is nonempty, since fld $R \times$ fld $R$ is a member. Hence it is permissible to take the intersection.

Then $R \subseteq R^{*}$ (because $R \subseteq Q$ for each of those $Q$ 's). $R^{*}$ is a transitive relation (recall Exercise 34 of Chapter 3). And $R^{*}$ is as small as possible, being the intersection of all candidates. Hence we may take $R^{t} = R^{*}$ . Uniqueness is immediate; by (b) any two contenders must be subsets of each other.

Although the theorem is now proved, we will ignore that fact and give the construction of $R^{t}$ “from below.” Define $R_{n}$ by recursion for n in $\omega$ by the equations

$$
R _ {0} = R \quad \text { and } \quad R _ {n + 1} = R _ {n} \circ R
$$

and then define $R_{*} = \bigcup_{n\in \omega}R_{n}$ . For example, we can describe $R_{n}$ for small $n$ as follows:

$$
R _ {0} = R = \{\langle x, y \rangle | x R y \},
$$

$$
R _ {1} = R \circ R = \{\langle x, y \rangle | x R t R y \text {   for   some   } t \},
$$

$$
R _ {2} = R \circ R \circ R = \{\langle x, y \rangle | x R t _ {1} R t _ {2} R y \text {   for   some   } t _ {1} \text {   and   } t _ {2} \}.
$$

In general,

$$
R _ {n} = \{\langle x, y \rangle | x R t _ {1} R \dots R t _ {n} R y \text {   for   some   } t _ {1}, \dots , t _ {n} \}
$$

and

$$
R _ {*} = \{\langle x, y \rangle \mid x R _ {n} y \text {   for   some   } n \}.
$$

Clearly $R \subseteq R_{*}$ . To show that $R_{*}$ is a transitive relation, suppose that $xR_{*}yR_{*}z$ . Then $xR_{m}yR_{n}z$ for some $m$ and $n$ . We claim that $xR_{m+n+1}z$ .

This is clear from the above characterization of $R_{n}$ ; the “three dots” technique can, as usual, be replaced by an induction on n. Hence $xR_{*}z$ .

To see that $R_{*}$ also satisfies the minimality clause (b), consider any transitive relation $Q$ that includes $R$ . To show that $R_{*} \subseteq Q$ , it suffices to show that $R_{n} \subseteq Q$ for each $n$ . We do this by induction on $n$ . It holds for $n = 0$ by assumption. If $R_{k} \subseteq Q$ and $xR_{k + 1}z$ , then we have $xR_{k}yRz$ for some $y$ , whence $xQyQz$ and (by transitivity) $xQz$ . So $R_{k + 1} \subseteq Q$ and the induction is complete.

We are now entitled to conclude that $R^{\mathfrak{t}} = R^{*} = R_{*}$ .

Example Assume that S is a transitive set. Define the binary relation

$$
\epsilon_ {S} = \{\langle x, y \rangle \in S \times S | x \in y \}
$$

on S. Then for x and y in S,

$$
\begin{array}{r l} {x \in_ {S} ^ {t} y} & {\Leftrightarrow x \in_ {S} \dots \in_ {S} y} \\ & {\Leftrightarrow x \in \dots \in y,} \end{array}
$$

where the intermediate points are automatically in S (by transitivity). Hence we have

$$
x \in_ {S} ^ {\mathfrak {t}} y \Leftrightarrow x \in \mathrm{TC} y.
$$

Recall from Exercise 7 of Chapter 7 that TC y, the transitive closure of y, is the smallest transitive set that includes y. Its members are roughly the members of members of $\cdots$ of members of y. A little more precisely,

$$
\mathrm{TC} y = y \cup \bigcup y \cup \bigcup \bigcup y \cup \dots .
$$

Theorem 9C If R is a well-founded relation, then its transitive extension $R^{t}$ is also well founded.

Proof We will give a proof that uses the axiom of choice. Exercise 1 requests an alternative proof that does not require choice.

Suppose that, contrary to our expectations, $R^{\mathfrak{t}}$ is not well founded. Then by Theorem 9A there is a descending chain $f$ . That is, $f$ is a function with domain $\omega$ and $f(n^{+})R^{\mathfrak{f}}(n)$ for each $n$ .

The idea is to fill in this descending chain to get a descending chain for R, and thereby to contradict the assumption that R is well founded. Since $f(n^{+})R^{\prime}f(n)$ , we know that

$$
f (n ^ {+}) R x _ {1} R \dots R x _ {k} R f (n)
$$

for some $x_{1}, \ldots, x_{k}$ . By interpolating these intermediate points between $f(n^{+})$ and $f(n)$ (and doing this for each n), we get a descending chain g such that $g(m^{+})Rg(m)$ for each m.

Corollary 9D If $R$ is a well-founded relation on $A$ , then $R^{\mathrm{t}}$ is a partial ordering on $A$ .

Proof Certainly $R^{t} \subseteq A \times A$ and $R^{t}$ is a transitive relation. So we need show only that $R^{t}$ is irreflexive. But any well-founded relation is irreflexive; we cannot have $xR^{t}x$ lest $\{x\}$ fail to have a $R^{t}$ -minimal element.

Because of this corollary, transitive well-founded relations are sometimes called partial well orderings.

Transfinite Recursion Theorem Schema For any formula $\gamma(x, y, z)$ the following is a theorem:

Assume that R is a well-founded relation on a set A. Assume that for any f and t there is a unique z such that $\gamma(f, t, z)$ . Then there exists a unique function F with domain A such that

$$
\gamma (F \upharpoonright \{x \in A \mid x R t \}, t, F (t))
$$

for all t in A.

Here $\gamma$ defines a function-class G, and the equation

$$
F (t) = \mathsf {G} (F \upharpoonright \{x \in A \mid x R t \}, t)
$$

holds for all t in A. A comparison of the above theorem schema with its predecessor in Chapter 7 will show that we have added an additional variable to $\gamma$ (and to G). This is because knowing what $F \upharpoonright \{x \in A \mid xRt\}$ is does not tell us what t is. The proof of the above theorem schema is much like the proofs of recursion theorems given in Chapters 4 and 7.

Proof As before, we form $F$ by taking the union of many approximating functions. For any $x$ in $A$ , define $\operatorname{seg} x$ to be $\{t \mid tRx\}$ . For the purposes of this proof, call a function $v$ acceptable iff $\operatorname{dom} v \subseteq A$ and whenever $x \in \operatorname{dom} v$ , then $\operatorname{seg} x \subseteq \operatorname{dom} v$ and $\gamma(v \upharpoonright \operatorname{seg} x, x, v(x))$ .

1. First we claim that any two acceptable functions $v_{1}$ and $v_{2}$ agree at all points (if any) belonging to both domains. Should this fail, there is an $R$ -minimal element $x$ of $\operatorname{dom} v_{1} \cap \operatorname{dom} v_{2}$ for which $v_{1}(x) \neq v_{2}(x)$ . By the minimality, $v_{1} \upharpoonright \operatorname{seg} x = v_{2} \upharpoonright \operatorname{seg} x$ . But then acceptability together with our assumption on $\gamma$ tells us that $v_{1}(x) = v_{2}(x)$ after all.

We can now use a replacement axiom to form the set $\mathcal{K}$ of all acceptable functions. Take $\varphi(u, v)$ to be the formula: $u \subseteq A \& v$ is an acceptable function with domain $u$ . It follows from the preceding paragraph that

$$
\varphi (u, v _ {1}) \& \varphi (u, v _ {2}) \Rightarrow v _ {1} = v _ {2}.
$$

Hence by replacement there is a set K such that

$$
v \in \mathcal {K} \Leftrightarrow (\exists u \in \mathscr {P} A) \varphi (u, v).
$$

Letting $\mathcal{K}$ be the set of all acceptable functions, we can explicitly define $F$ to be the set $\bigcup \mathcal{K}$ . Thus

$$
\langle x, y \rangle \in F \Leftrightarrow v (x) = y \text {   for   some   acceptable   } v.
$$

Observe that $F$ is a function, because any two acceptable functions agree wherever both are defined.

2. Next we claim that the function $F$ is acceptable. Consider any $x$ in $\operatorname{dom} F$ . Then there exists some acceptable $v$ with $x \in \operatorname{dom} v$ . Hence $x \in A$ and $\sec x \subseteq \operatorname{dom} v \subseteq \operatorname{dom} F$ . We must check that $\gamma(F \upharpoonright \sec x, x, F(x))$ holds. We have

$$
\begin{array}{l l} \gamma (v \upharpoonright \text {seg} x, x, v (x)) & \quad \text {by acceptability}, \\ v \upharpoonright \text {seg} x = F \upharpoonright \text {seg} x & \quad \text {by (\star) and (1)}, \\ v (x) = F (x) & \quad \text {by (\star)}, \end{array}
$$

from which we can conclude that $\gamma(F \upharpoonright \operatorname{seg} x, x, F(x))$ .

3. We now claim that dom $F$ is all of $A$ . If this fails, then there is an $R$ -minimal element $t$ of $A - \operatorname{dom} F$ . By minimality, $\operatorname{seg} t \subseteq \operatorname{dom} F$ . Take the unique $y$ such that $\gamma(F \upharpoonright \operatorname{seg} t, t, y)$ and let $\hat{v} = F \cup \{\langle t, y \rangle\}$ . We must verify that $\hat{v}$ is acceptable. Clearly $\hat{v}$ is a function and $\operatorname{dom} \hat{v} \subseteq A$ . Consider any $x$ in $\operatorname{dom} \hat{v}$ . One possibility is that $x \in \operatorname{dom} F$ . Then $\operatorname{seg} x \subseteq \operatorname{dom} F \subseteq \operatorname{dom} \hat{v}$ and from the equations

$$
\hat {v} \upharpoonright \operatorname{seg} x = F \upharpoonright \operatorname{seg} x \quad \text { and } \quad \hat {v} (x) = F (x)
$$

we conclude that $\gamma (\hat{v}\upharpoonright \operatorname {seg}x,x,\hat{v} (x))$ . The other possibility is that $x = t$ . Then $\operatorname {seg}t\subseteq \operatorname {dom}F\subseteq \operatorname {dom}\hat{v}$ and from the equations

$$
\hat {v} \upharpoonright \operatorname{seg} t = F \upharpoonright \operatorname{seg} t \quad \text { and } \quad \hat {v} (t) = y
$$

we conclude that $\gamma (\hat{v}\upharpoonright \operatorname {seg}t,t,\hat{v} (t))$ . Hence $\hat{v}$ is acceptable, and so $t\in \operatorname {dom}F$ after all. Consequently, $\operatorname {dom}F = A$ .

4. $F$ is unique, by an inductive argument like those used before.

We now proceed to show how transfinite recursion can be applied to the membership relation to produce the rank of a set (and thereby generate all of the ordinal numbers). Recall that in Chapter 7 we applied transfinite recursion to a well-ordered structure $\langle A, <\rangle$ to obtain a function E with domain A such that

$$
E (a) = \{E (x) | x \in a \}
$$

for each $a \in A$ . It then turned out that ran $E$ was (by definition) the ordinal number of $\langle A, < \rangle$ .

Now we intend to perform the analogous construction using, in place of a well ordering, the membership relation on some set. After all, the regularity axiom assures us that the membership relation is always well founded. So we can apply transfinite recursion. What will we get? The answer is that if we do it right, we will get the rank of the set!

To be more specific, let $S$ be the set $\langle 1,0\rangle$ , or

$$
\{\{\{\emptyset \} \}, \{\emptyset , \{\emptyset \} \} \}
$$

to use its full name. We can illustrate the formation of this set by Fig. 48. The sets appearing below S in this figure are the sets in TC S, the transitive closure of S.

![](images/47c5a9067e70d73ef0650887bcb89fcca2a80ac3e72fecfb7649dae22ccf5e5e.jpg)  
Fig. 48. The membership relation on TC{<1, 0>}

Let M be the membership relation on TC S:

$$
M = \{\langle x, y \rangle \mid x \in y \in \mathrm{TC} S \}.
$$

The pairs in this relation are illustrated by straight lines in Fig. 48. The relation M is sure to be well founded; in the present example it is also finite. We have seen that $M^{t}$ is a well-founded partial ordering on TC S; in fact it is the partial ordering corresponding to Fig. 48. Since $M^{t}$ is well founded, we can apply transfinite recursion to obtain the unique function E on TC S for which

$$
E (a) = \{E (x) \mid x M ^ {t} a \}
$$

for every $a$ in TC S. (In the transfinite recursion theorem schema, take $\gamma(f, t, z)$ to be the formula $z = \operatorname{ran} f$ . Then

$$
\begin{array}{r l} E (a) & = \operatorname{ran} (E \upharpoonright \{x \in \mathrm{TC} S \mid x M ^ {\iota} a \}) \\ & = E [ [ \{x \mid x M ^ {\iota} a \} ] ] \\ & = \{E (x) \mid x M ^ {\iota} a \} \end{array}
$$

as predicted.) The values of $E$ are shown by the bracketed numerals in Figure 48. Observe that ran $E = E[\mathrm{TC}S] = 3$ , which is indeed rank $S$ . And furthermore $E(a) = \text{rank } a$ for every $a$ in TC $S$ .

Was it just a lucky coincidence that for $S = \langle 1, 0 \rangle$ we reproduced the rank function? (Would we have gone through the example if it were?) The following theorem says that the outcome is inevitable.

Theorem 9E Let $S$ be any set and let

$$
M = \{\langle x, y \rangle \mid x \in y \in \mathrm{TC} S \}.
$$

Let $E$ be the unique function with domain TC $S$ such that

$$
E (a) = \{E (x) | x M ^ {t} a \}
$$

for each $a$ in TC S. Then ran $E = \operatorname{rank} S$ . Furthermore $E(a) = \operatorname{rank} a$ for each $a$ in TC S.

Proof This theorem is a consequence of Theorem 7V, which characterized rank a as the least ordinal strictly greater than rank x for every x in a. The heart of the proof consists of showing that

(☆)

$$
\operatorname{rank} a = \{\operatorname{rank} x \mid x M ^ {t} a \}
$$

for all $a$ in TC S.

To prove the “ $\supseteq$ ” half of $(\star)$ , we use Theorem 7V(a):

$$
\begin{array}{r c l} x M ^ {t} a & \Rightarrow & x \in \dots \in a \\ & \Rightarrow & \operatorname{rank} x \in \dots \in \operatorname{rank} a \\ & \Rightarrow & \operatorname{rank} x \in \operatorname{rank} a. \end{array}
$$

The “ $\subseteq$ ” half of $(\star)$ is proved by transfinite induction on $a$ over the well-founded structure $\langle \mathrm{TC} S, M^t\rangle$ . Suppose then that $(\star)$ holds of $b$ whenever $bM^t a$ and that $\alpha \in \operatorname{rank} a$ . We must show that $\alpha = \operatorname{rank} x$ for some $x$ with $xM^t a$ . By Theorem 7V(b), $\alpha \in (\operatorname{rank} b)^+$ for some $b \in a$ , so $\alpha \in \operatorname{rank} b$ . If $\alpha = \operatorname{rank} b$ , we are done, so suppose not. By the inductive hypothesis

$$
\alpha \in \operatorname{rank} b \subseteq \{\operatorname{rank} x \mid x M ^ {t} b \}
$$

so that we have

$$
\alpha = \operatorname{rank} x \& x M ^ {t} b \& b \in a
$$

for some $x$ . Since $xM^{\mathfrak{t}}a$ , the proof of $(\star)$ is complete.

From $(\star)$ and the equation $E(a) = \{E(x) \mid xM^{\prime}a\}$ we can conclude (from the uniqueness clause in recursion) that $E(a) = \operatorname{rank} a$ for all $a$ in TC $S$ .

By applying $(\star)$ to a set containing S (in place of S itself) we obtain

$$
\operatorname{rank} S = \{\operatorname{rank} a \mid a \in \dots \in S \} = \operatorname{ran} E
$$

as claimed.

Theorem 9E gives one of the (many) possible ways of introducing ordinal numbers. It produces the rank operation directly (without reference to ordinals). Thus one could then define an ordinal number to be something that is the rank of some set. It then follows, for example, that rank $\alpha = \alpha$ for any ordinal $\alpha$ . And all this can be carried through without any mention of well-ordered structures! One can then proceed to develop the usual properties of ordinal numbers (e.g., those in Theorem 7M) by using the rank operation. The end result of such an approach would be equivalent to the more traditional approach followed in Chapter 7.

## Exercises

1. Prove Theorem 9C without using the axiom of choice.

2. Give an intrinsic characterization of these relations $R$ with the property that $R^{\mathrm{t}}$ is a partial ordering.

3. (König) Assume that $R$ is a well-founded relation such that $\{x \mid xRy\}$ is finite for each $y$ . Prove that $\{x \mid xR^t y\}$ is finite for each $y$ .

4. Show that for any set S,

$$
\mathrm{TC} S = S \cup \bigcup \{\mathrm{TC} x \mid x \in S \}.
$$

## NATURAL MODELS

$$
\begin{array}{c} \text {)} \\ \text {of} \end{array}
$$

In this section we want to consider the question of whether there can be a set M that is in a certain sense a miniature model of the class V of all sets. Consider a formula $\sigma$ of the language of set theory; for example $\sigma$ might be one of our axioms. (Recall from Chapter 2 the ways of constructing formulas.) We can convert $\sigma$ to a new formula $\sigma^{M}$ by replacing expressions $\forall x$ and $\exists x$ by $\forall x \in M$ and $\exists x \in M$ . Then the proposition (true or false) that $\sigma$ asserts of V is asserted by $\sigma^{M}$ of just M.

Example Let $\sigma$ be the pairing axiom,

$$
\forall u \forall v \exists B \forall x [ x \in B \Leftrightarrow x = u \text { or } x = v ].
$$

Then $\sigma^M$ is

$$
(\forall u \in M) (\forall v \in M) (\exists B \in M) (\forall x \in M) [ x \in B \Leftrightarrow x = u \text {   or   } x = v ].
$$

In something closer to English, this says that you can take any u and v inside the set M, and be assured of the existence of a set B inside the set M whose members belonging to the set M are exactly u and v. If somebody has the delusion that M is the class of all sets, then $\sigma^{M}$ asserts what he believes the pairing axiom to assert.

The formula $\sigma^{M}$ is called the relativization of $\sigma$ to M. We say that $\sigma$ is true in M (or that M is a model of $\sigma$ ) iff $\sigma^{M}$ is true. Now it is conceivable that there might be some set M that was a model for all of our axioms. It is also conceivable that no such M exists. In this section we will be particularly concerned with the question of whether $V_{\alpha}$ , for some lucky $\alpha$ , might be a model of all of our axioms.

Logical Notes (1) What we here call a model might also be called an “∈-model.” There is a more general concept of a model $\langle M, E \rangle$ involving not only reinterpretation of $\forall$ and $\exists$ (to refer to M), but also a reinterpretation of $\in$ (by means of E). We will not delve into this more general concept; we only caution you that it exists. (2) There is a fascinating theorem of mathematical logic, called “Gödel’s second incompleteness theorem.” It implies, among other things, that if our axioms are consistent (as we sincerely believe them to be), then we can never use them to prove the existence of a model of the axioms. Such a model may exist (as a set), but a proof (from our axioms) that it is there does not exist. So do not expect such a proof in this section!

We will now go through the axioms one by one, checking to see whether its relativization is true in $V_{\alpha}$ for suitable $\alpha$ .

1. Extensionality. We claim that the relativization of extensionality to any transitive set (and $V_{\alpha}$ is always a transitive set) is true. That is, consider any transitive set M and any sets A and B in M. Our claim is that if

$$
(\forall x \in M) (x \in A \Leftrightarrow x \in B),\tag{☆}
$$

then $A = B$ . Well, if $x \in A$ , then $x \in A \in M$ , and by the transitivity of $M$ we have $x \in M$ . Hence we can apply $(\star)$ to conclude that $x \in B$ . Thus $A \subseteq B$ , and similarly $B \subseteq A$ . So $A = B$ .

2. Empty set. We claim that the relativization of the empty set axiom to $V_{\alpha}$ is true provided that $\alpha \neq 0$ . We must show that (for $\alpha \neq 0$ ),

$$
(\exists B \in V _ {\alpha}) (\forall x \in V _ {\alpha}) x \notin B.
$$

What should we take for $B$ ? The empty set, of course. Since $1 \in \alpha$ , we have $\varnothing \in V_1 \subseteq V_\alpha$ , so the empty set is in $V_\alpha$ . And certainly nothing in $V_\alpha$ (or elsewhere) belongs to the empty set.

3. Pairing. We claim that the relativization of the pairing axiom to $V_{\lambda}$ is true for any limit ordinal $\lambda$ . To prove this, consider any $u$ and $v$ in $V_{\lambda}$ . Since $V_{\lambda} = \bigcup_{\alpha \in \lambda} V_{\alpha}$ , we have $u \in V_{\alpha}$ and $v \in V_{\beta}$ for some $\alpha$ and $\beta$ less than $\lambda$ . Either $\alpha \in \beta$ or $\beta \in \alpha$ ; by the symmetry we may suppose that $\alpha \in \beta$ . Then $\{u, v\} \subseteq V_{\beta}$ and

$$
\{u, v \} \in V _ {\beta^ {+}} \subseteq V _ {\lambda}.
$$

Thus in $V_{\lambda}$ there is a set $B$ (namely $\{u, v\}$ ) such that

$$
(\forall x \in V _ {\lambda}) (x \in B \Leftrightarrow x = u \text {   or   } x = v).
$$

And this is what we want.

4. Union. The union axiom is true in $V_{\alpha}$ for any $\alpha$ . For suppose that $A \in V_{\alpha}$ . Then $A \subseteq V_{\beta}$ for some $\beta$ less than $\alpha$ . Since $V_{\beta}$ is a transitive set,

$$
\begin{array}{r c l} x \in \bigcup A & \Rightarrow & x \in b \in A \quad \text {   for   some   } b \\ & \Rightarrow & x \in V _ {\beta}. \end{array}
$$

So $\bigcup A \subseteq V_{\beta}$ , whence $\bigcup A \in V_{\alpha}$ . Thus we have a set $B$ in $V_{\alpha}$ (namely, $\bigcup A$ ) such that for any $x$ in $V_{\alpha}$ (or elsewhere),

$$
\begin{array}{r c l} x \in B & \Leftrightarrow & (\exists b) (x \in b \in A) \\ & \Leftrightarrow & (\exists b \in V _ {\alpha}) (x \in b \in A) \end{array}
$$

since $V_{\alpha}$ is transitive.

5. Power set. As with the pairing axiom, the power set axiom is true in $V_{\lambda}$ whenever $\lambda$ is a limit ordinal. To prove this, consider any set a in $V_{\lambda}$ . Then rank $a < \lambda$ , so that

$$
\operatorname{rank} \mathcal {P} a = (\operatorname{rank} a) ^ {+} <   \lambda
$$

and $\mathcal{P}a\in V_{\lambda}$ . Thus we have a set $B$ in $V_{\lambda}$ (namely $\mathcal{P}a$ ) such that for any $x$ in $V_{\lambda}$ ,

$$
\begin{array}{r c l} x \in B & \Leftrightarrow & x \subseteq a \\ & \Leftrightarrow & \forall t (t \in x \Rightarrow t \in a) \\ & \Leftrightarrow & (\forall t \in V _ {\lambda}) (t \in x \Rightarrow t \in a) \end{array}
$$

since $V_{\lambda}$ is transitive.

6. Subset. All subset axioms are true in $V_{\alpha}$ for any $\alpha$ . For consider any set c in $V_{\alpha}$ and any formula $\varphi$ not containing B. We seek a set B in $V_{\alpha}$ such that for any x in $V_{\alpha}$ ,

$$
x \in B \Leftrightarrow x \in c \& \varphi^ {V _ {\alpha}}.
$$

This tells us exactly what to take for $B$ , namely $\{x \in c \mid \varphi^{V_{\alpha}}\}$ . Since $B \subseteq c \in V_{\alpha}$ , we have $B \in V_{\alpha}$ .

7. Infinity: The infinity axiom is true in $V_{\alpha}$ for any $\alpha$ greater than $\omega$ . We have $\omega \subseteq V_{\omega}$ , whence $\omega \in V_{\alpha}$ for any larger $\alpha$ . As with the other axioms, this implies that the infinity axiom is true in $V_{\alpha}$ .

8. Choice. The axiom of choice (version I) is true in $V_{\alpha}$ for any $\alpha$ . If $R$ is a relation in $V_{\alpha}$ , then any subset of $R$ is in $V_{\alpha}$ . In particular, the subfunction $F$ of $R$ provided by the axiom of choice (version I) is in $V_{\alpha}$ . (For some other versions of the axiom of choice, we need to assume that $\alpha$ is a limit ordinal. Although Theorem 6M proves that the several versions are equivalent, the proof to 6M uses some of the above-listed axioms. And those axioms may fail in $V_{\alpha}$ if $\alpha$ is not a limit ordinal.)

9. The regularity axiom is true in $V_{\alpha}$ for any $\alpha$ . Consider any nonempty set A in $V_{\alpha}$ . Let m be a member of A having least possible rank. Then $m \in V_{\alpha}$ and $m \cap A = \varnothing$ . (Note that we do not need to use the regularity axiom in this proof, in contrast to the situation with all other axioms.)

We have now verified the following result.

Theorem 9F If $\lambda$ is any limit ordinal greater than $\omega$ , then $V_{\lambda}$ is a model of all of our axioms except the replacement axioms.

Our axioms (including replacement) are called the Zermelo–Fraenkel axioms, whereas the Zermelo axioms are obtained by omitting replacement. (Recall the historical notes of Chapter 1.) The above theorem asserts that $V_{\lambda}$ is a model of the Zermelo axioms whenever $\lambda$ is a limit ordinal greater than $\omega$ .

The smallest limit ordinal greater than $\omega$ is $\omega \cdot 2$ . Informally, we can describe the ordinal $\omega \cdot 2$ by the equation

$$
\omega \cdot 2 = \{0, 1, 2, \dots , \omega , \omega^ {+}, \omega^ {+ +}, \dots \}
$$

listing the smaller ordinals. It is the ordinal of the set Z of integers under the peculiar ordering

$$
0 <   1 <   2 <   \dots <   - 1 <   - 2 <   - 3 <   \dots .
$$

$V_{\omega}$ contains the sets of finite rank. Any set in $V_{\omega}$ is finite, its members are all finite, and so forth. We can informally describe $V_{\omega\cdot2}$ as

$$
V _ {\omega \cdot 2} = V _ {\omega} \cup \mathcal {P} V _ {\omega} \cup \mathcal {P P} V _ {\omega} \dots .
$$

In $V_{\omega \cdot 2}$ all the sets needed in elementary mathematics can be found. The real numbers are all there, as are all functions from reals to reals (compare Exercise 27 of Chapter 7). This reflects the fact that we needed only the Zermelo axioms to construct the reals. What sets are not in $V_{\omega \cdot 2}$ ? Well, the only ordinals in $V_{\omega \cdot 2}$ are those less than $\omega \cdot 2$ , by Exercise 26 of Chapter 7. Since $\omega \cdot 2$ is obviously a countable ordinal, $V_{\omega \cdot 2}$ contains only ordinals that are countable, and not even all of those.

Lemma 9G There is a well-ordered structure in $V_{\omega \cdot 2}$ whose ordinal number is not in $V_{\omega \cdot 2}$ .

Proof Start with an uncountable set $S$ in $V_{\omega \cdot 2}$ , such as $\mathbb{R}$ or $\mathcal{P}\omega$ . By the well-ordering theorem, there exists some well ordering $<$ on $S$ . Now $< \subseteq S \times S \subseteq \mathcal{PPS}$ by Lemma 3B, so $<$ is also in $V_{\omega \cdot 2}$ . (The rank of $<$ is only two steps above the rank of $S$ .) Hence by going up two more steps, we have $\langle S, < \rangle$ in $V_{\omega \cdot 2}$ . But the ordinal number of $\langle S, < \rangle$ , being uncountable, cannot be in $V_{\omega \cdot 2}$ .

Corollary 9H Not all of the replacement axioms are true in $V_{\omega \cdot 2}$ .

Sketch of Proof Let $\sigma$ be the formula of set theory: "For any well-ordered structure $\langle S, <\rangle$ there exists an ordinal $\alpha$ such that $\langle S, <\rangle$ is isomorphic to $\langle \alpha, \epsilon_{\alpha} \rangle$ ." Then $\sigma$ can be proved from the Zermelo-Fraenkel axioms—we proved it back in Chapter 7 (see Theorem 7D). But we claim that $\sigma$ is not true in $V_{\omega \cdot 2}$ . This claim follows from Lemma 9G, together with some argument to the effect that if it appears from inside $V_{\omega \cdot 2}$ that $\alpha$ is the ordinal number of $\langle S, <\rangle$ , then it really is.

But if $V_{\omega \cdot 2}$ were a model for the Zermelo-Fraenkel axioms, it would have to be a model for any theorem that follows from those axioms. (This was the meaning of "theorem" back in Chapter 1.) So $V_{\omega \cdot 2}$ cannot be a model of the Zermelo-Fraenkel axioms. Since it is a model of the Zermelo axioms, it must be replacement axioms that fail in $V_{\omega \cdot 2}$ .

Corollary 9I Not all of the replacement axioms are theorems of the Zermelo axioms.

Proof Any theorem of the Zermelo axioms must be true in any model of those axioms, such as $V_{\omega\cdot2}$ . But by the preceding result, not all replacement axioms are true in $V_{\omega\cdot2}$ .

The standard abbreviation for the Zermelo–Fraenkel axioms is “ZF” (or “ZFC” if we want to emphasize that the axiom of choice is included). The above corollary shows that there is a sense in which ZF is strictly stronger than the Zermelo axioms. It is our only excursion into the metamathematics of set theory.

Definition A cardinal number $\kappa$ is said to be inaccessible iff it meets the following three conditions.

(a) $\kappa$ is greater than $\aleph_0$ .

(b) For any cardinal $\lambda$ less than $\kappa$ , we have $2^{\lambda} < \kappa$ . (Here cardinal exponentiation is used.)

(c) It is not possible to represent $\kappa$ as the supremum of fewer than $\kappa$ smaller ordinals. That is, if S is a set of ordinals less than $\kappa$ and if card $S < \kappa$ , then the ordinal sup S is less than $\kappa$ .

Cardinals meeting clause (c) are called regular; we will have more to say about such cardinals in the section on cofinality.

Examples Conditions (b) and (c) are true when $\kappa = \aleph_0$ (by Corollary 6K and Exercise 13 of Chapter 6). But of course condition (a) fails. Conditions (a) and (c) hold when $\kappa = \aleph_1$ (since a countable union of countable ordinals is countable). But condition (b) fails for $\aleph_1$ . Conditions (a) and (b) hold when $\kappa = \beth_\omega$ , but condition (c) fails since $\beth_\omega = \bigcup_{n \in \omega} \beth_n$ . What is an example of a cardinal meeting all three conditions? Are there any inaccessible cardinals at all? We will return to these questions after the next theorem.

First we need the following lemma, which relates the beth numbers to the $V_{\alpha}$ sets.

Lemma 9J For any ordinal number $\alpha$ ,

$$
\operatorname{card} V _ {\omega + \alpha} = \beth_ {\alpha}.
$$

Proof We use transfinite induction on $\alpha$ .

Case I $\alpha = 0$ . We must show that card $V_{\omega} = \aleph_0$ . But this is clear, since $V_{\omega}$ is the union of $\aleph_0$ finite sets of increasing size.

Case II $\alpha$ is a successor ordinal $\beta^{+}$ . Then

$$
V _ {\omega + \beta^ {+}} = V _ {(\omega + \beta) ^ {+}} = \mathcal {P} V _ {\omega + \beta}
$$

and its cardinality is

$$
2 ^ {\operatorname{card} V _ {\omega + \beta}} = 2 ^ {\beth_ {\beta}} = \beth_ {\beta^ {+}}
$$

by the inductive hypothesis.

Case III $\alpha$ is a limit ordinal. Then $\omega + \alpha$ is also a limit ordinal and so $\omega + \alpha = \sup\{\omega + \delta \mid \delta \in \alpha\}$ . Consequently (Exercise 9), $V_{\omega + \alpha} = \bigcup\{V_{\omega + \delta} \mid \delta \in \alpha\}$ . Since card $V_{\omega + \delta} = \beth_{\delta}$ , the cardinality of the union is at least $\beth_{\alpha}$ . On the other hand, it is at most (card $\alpha) \cdot \beth_{\alpha}$ . Since card $\alpha \in \alpha \in \beth_{\alpha}$ (by the monotonicity of the beth operation), this product is just $\beth_{\alpha}$ .

Lemma 9K Assume that $\kappa$ is inaccessible.

(a) If $\alpha$ is an ordinal less than $\kappa$ , then $\beth_{\alpha}$ is less than $\kappa$ .

(b) If $A \in V_{\kappa}$ , then card $A < \kappa$ .

Proof We prove part (a) by transfinite induction on $\alpha$ . So suppose that the condition holds for all ordinals less than $\alpha$ , where $\alpha$ is less than $\kappa$ .

Case I $\alpha = 0$ . Then $\beth_0 = \aleph_0 < \kappa$ since $\kappa$ is uncountable.

Case II $\alpha = \beta^{+}$ for some $\beta$ . Then $\beth_{\beta} < \kappa$ by the inductive hypothesis, and $\beth_{\alpha} = 2^{\beth_{\beta}} < \kappa$ by inaccessibility.

Case III $\alpha$ is a limit ordinal. Then by the inductive hypothesis, $\beth_{\gamma} < \kappa$ for all $\gamma \in \alpha$ . Then $\beth_{\alpha} = \sup \{\beth_{\gamma} | \gamma \in \alpha\} < \kappa$ , since $\kappa$ is not the supremum of fewer than $\kappa$ (and card $\alpha < \kappa$ ) smaller ordinals.

This proves part (a). For part (b), suppose that $A \in V_{\kappa}$ . Then $A \subseteq V_{\alpha}$ for some $\alpha$ less than $\kappa$ . Hence we have

$$
\operatorname{card} A \leq \operatorname{card} V _ {\alpha} \leq \beth_ {\alpha} <   \kappa
$$

by the preceding lemma and part (a).

Theorem 9L If $\kappa$ is an inaccessible cardinal number, then all of the ZF axioms (including the replacement axioms) are true in $V_{\kappa}$ .

Proof All of the Zermelo axioms are true in $V_{\kappa}$ by Theorem 9F, since $\kappa$ is an uncountable limit ordinal. The only axioms left to worry about are the replacement axioms.

Consider a set $A$ in $V_{\kappa}$ and any formula $\varphi(x, y)$ such that

$$
(\forall x \in A) \forall y _ {1} \forall y _ {2} [ \varphi (x, y _ {1}) \& \varphi (x, y _ {2}) \Rightarrow y _ {1} = y _ {2} ]
$$

is true in $V_{\kappa}$ . Define the function $F$ by

$$
F = \{\langle x, y \rangle \in A \times V _ {\kappa} | \varphi (x, y) \text {   is   true   in   } V _ {\kappa} \}.
$$

Notice that F is a function, by what we have said about $\varphi$ . The domain of F is some subset of A. Let B = ran F; thus for any y in $V_{\kappa}$

$$
y \in B \Leftrightarrow (\exists x \in A) \varphi (x, y) \text {   is   true   in   } V _ {\kappa}.
$$

What we must prove is that $B \in V_{\kappa}$ , because then it will follow that

$$
\exists B \forall y [ y \in B \Leftrightarrow (\exists x \in A) \varphi (x, y) ]
$$

is true in $V_{\kappa}$ .

To show that $B \in V_{\kappa}$ , consider the set

$$
S = \{\operatorname{rank} F (x) \mid x \in \operatorname{dom} F \}.
$$

The ordinals in S are all less than $\kappa$ (because $F(x) \in V_{\kappa}$ ), and card $S \leq card dom F \leq card A < \kappa$ by part (b) of the above lemma. So by the inaccessibility, the ordinal

$$
\alpha = \sup S = \sup \{\operatorname{rank} F (x) \mid x \in \operatorname{dom} F \}
$$

is less than $\kappa$ . But any member $F(x)$ of $B$ has rank no more than $\alpha$ , so $F(x) \in V_{\alpha^{+}}$ . Hence $B \subseteq V_{\alpha^{+}}$ and so rank $B \in \alpha^{+} \in \kappa$ . Thus $B \in V_{\kappa}$ , as desired.

Now back to the question: Are there any inaccessible cardinals at all? If so, then by the above theorem, there are models of the ZF axioms. Because we cannot hope to prove the existence of such a model (due to Gödel's second incompleteness theorem, mentioned earlier in this section), it follows that we cannot hope to prove from our axioms that inaccessible cardinals exist.

On the other hand, we intuitively want the cardinal and ordinal numbers to go on forever. To deny the existence of inaccessible numbers would appear to impose an unnatural ceiling on “forever.” With these thoughts in mind, Alfred Tarski in 1938 proposed for consideration as an additional set-theoretic axiom the statement:

For any cardinal number there is a larger inaccessible cardinal number.

This is an example of a “large cardinal axiom.” Despite the fact that it literally concerns huge sets, one can prove from it new facts about natural numbers! The interest in various large cardinal axioms and their consequences motivates an important part of current research in set theory.

## Exercises

5. Show that a set S belongs to $V_{\omega}$ iff TC S is finite. (Thus S belongs to $V_{\omega}$ iff S is finite and all the members of ... of members of S are finite. Because of this fact, $V_{\omega}$ is often called HF, the collection of hereditarily finite sets.)

6. Are the replacement axioms true in $V_{\omega}$ ? Which axioms are not true in $V_{\omega}$ ?

7. Let $\mathcal{F}$ be the collection of finite subsets of $\omega$ . Let $g$ be a one-to-one correspondence between $\omega$ and $\mathcal{F}$ with the property that whenever $m \in g(n)$ , then $m$ is less than $n$ . (For example, we can use $g(n) = \{m \in \omega \mid \text{the coefficient of } 2^m \text{ in the binary representation of } n \text{ is } 1\}$ .) Define the binary relation $E$ on $\omega$ by

$$
m E n \Leftrightarrow m \in g (n).
$$

Show that $\langle \omega, E \rangle$ is isomorphic to $\langle V_{\omega}, \in^{\circ} \rangle$ .

8. The proof to Lemma 9G used the axiom of choice (in the form of the well-ordering theorem). Give a proof that does not use the axiom of choice.

9. Assume that $\lambda$ is a limit ordinal. Show that

$$
V _ {\alpha + \lambda} = \bigcup \{V _ {\alpha + \delta} | \delta \in \lambda \}.
$$

10. Define the set

$$
S = \omega \cup \mathcal {P} \omega \cup \mathcal {P P} \omega \cup \dots .
$$

Prove that $S$ is a model of the Zermelo axioms.

11. Assume that $\kappa$ is inaccessible. Show that $\beth_{\kappa} = \kappa$ and card $V_{\kappa} = \kappa$ .

## COFINALITY

Any limit ordinal is the supremum of the set of all smaller ordinals; this merely says that $\lambda = \bigcup \lambda$ for any limit ordinal $\lambda$ . But we do not need to take all smaller ordinals. We can find a proper subset S of $\lambda$ such that $\lambda$ is the supremum $\bigcup S$ of S. How small can we take S to be? That will depend on what $\lambda$ is.

Definition The cofinality of a limit ordinal $\lambda$ , denoted cf $\lambda$ , is the smallest cardinal $\kappa$ such that $\lambda$ is the supremum of $\kappa$ smaller ordinals. The cofinality of nonlimit ordinals is defined by setting cf 0 = 0 and cf $\alpha^{+} = 1$ .

Thus to find the cofinality of $\lambda$ , we seek a set S of smaller ordinals (i.e., $S \subseteq \lambda$ ) for which $\lambda = \sup S$ . Such a set S is said to be cofinal in $\lambda$ . There will be many sets that are cofinal in $\lambda$ ; for example, $\lambda$ itself is such a set. There will not exist any smallest (with respect to inclusion) set S cofinal in $\lambda$ . But there will be a smallest possible cardinality for S, and this smallest cardinality is by definition cf $\lambda$ .

Example Obviously cf $\lambda \leq$ card $\lambda$ , since $\lambda$ is cofinal in itself. Sometimes equality holds; for example, cf $\omega = \aleph_0$ . (We could not have cf $\omega < \aleph_0$ , since a finite union of natural numbers would be finite.) On the other hand, sometimes cf $\lambda \neq$ card $\lambda$ . For example, Theorem 9N will show that $\aleph_{\omega}$ (as a limit ordinal) has cofinality $\aleph_0$ , being the supremum of $\{\aleph_0, \aleph_1, \aleph_2, \ldots\}$ .

Definition A cardinal $\kappa$ is said to be regular iff cf $\kappa = \kappa$ , and is said to be singular if cf $\kappa < \kappa$ .

The above example shows that $N_{0}$ is regular whereas $N_{\omega}$ is singular. Recall that an inaccessible cardinal is required to be regular.

Note on Style The definition of cofinality has an awkward three-part format. Can we not give a simple definition covering zero, the successor ordinals, and the limit ordinals in one sweep? Yes, we can do so by using the idea of the “strict supremum.” The cofinality of any ordinal $\alpha$ is the least cardinal number $\kappa$ such that there exists a subset S of $\alpha$ having cardinality $\kappa$ and $\alpha$ is the least ordinal strictly greater than every member of S. (Exercise 12 asks you to verify that this is correct.)

Theorem 9M $\aleph_{\alpha +1}$ is a regular cardinal number for every $\alpha$ .

Proof Assume that $\aleph_{\alpha + 1} = \sup S$ , where $S$ is a set of ordinals, each of which is less than $\aleph_{\alpha + 1}$ . Then each member of $S$ has cardinality at most $\aleph_{\alpha}$ . Therefore (compare Exercise 26 of Chapter 6) we have $\aleph_{\alpha + 1} = \operatorname{card} \bigcup S \leq (\operatorname{card} S) \cdot \aleph_{\alpha}$ . But this implies that card $S \geq \aleph_{\alpha + 1}$ .

Since $\aleph_0$ is also a regular cardinal, there remain only the cardinals $\aleph_{\lambda}$ where $\lambda$ is a limit ordinal.

Theorem 9N For any limit ordinal $\lambda$ , cf $\aleph_{\lambda} = \operatorname{cf} \lambda$ .

Proof First of all, we claim that $cf N_{\lambda} \leq cf \lambda$ . We know that $\lambda$ is the supremum of some set $S \subseteq \lambda$ with card $S = cf \lambda$ . It suffices to show that $N_{\lambda} = \sup\{\aleph_{\alpha} | \alpha \in S\}$ . But this is Theorem 8E, applied to the aleph operation. Second, we claim that $cf \lambda \leq cf N_{\lambda}$ . Suppose that $N_{\lambda}$ is the supremum of some set A of smaller ordinals. Let

$B = \{\gamma \in \lambda \mid \aleph_{\gamma}$ is the cardinality of some ordinal in $A\}$ .

Then card $B \leq$ card $A$ . To complete the proof it suffices to show that $\sup B = \lambda$ . Any $\alpha$ in $A$ has cardinality at most $\aleph_{\sup B}$ , so $\alpha \in \aleph_{(\sup B) + 1}$ . Hence $\aleph_{\lambda} = \sup A \leq \aleph_{(\sup B) + 1}$ and so $\lambda \in (\sup B) + 1$ . Since $\lambda$ is a limit ordinal, $\lambda \in \sup B$ , whence equality holds.

For example, cf $N_{\omega} = cf \omega = N_{0}$ . And cf $N_{\Omega} = cf \Omega = N_{1}$ (where $\Omega$ is the first uncountable ordinal). In particular, both $N_{\omega}$ and $N_{\Omega}$ are singular. For any limit ordinal $\lambda$ ,

$$
\operatorname{cf} \aleph_ {\lambda} = \operatorname{cf} \lambda \in \lambda \in \aleph_ {\lambda}.
$$

If $N_{\lambda}$ is regular, then equality holds throughout. But does this ever happen? If it happens, $\lambda$ is said to be weakly inaccessible. We cannot prove (from our axioms, if they are consistent) that any weakly inaccessible cardinals exist. If any inaccessible cardinals exist, then they are also weakly inaccessible (Exercise 15).

There is another way of characterizing cofinality that uses increasing sequences of ordinals instead of sets of ordinals. For an ordinal number $\alpha$ , define an $\alpha$ -sequence to be simply a function with domain $\alpha$ . For example, an ordinary infinite sequence is an $\omega$ -sequence, and a finite sequence is an n-sequence for some natural number n. For an $\alpha$ -sequence f, it is customary to write $f_{\xi}$ in place of the Eulerian $f(\xi)$ . An $\alpha$ -sequence $f$ into the ordinals is called increasing iff it preserves order:

$$
\xi \in \eta \Rightarrow f _ {\xi} \in f _ {\eta}.
$$

An increasing $\alpha$ -sequence of ordinals is said to converge to $\beta$ iff $\beta = \sup \operatorname{ran} f$ , i.e.,

$$
\beta = \sup \{f _ {\xi} | \xi \in \alpha \}.
$$

From a nonincreasing sequence we can extract an increasing subsequence (possibly with a smaller domain):

Lemma 9P Assume that f is an $\alpha$ -sequence (not necessarily increasing) into the ordinal numbers. There is an increasing $\beta$ -sequence g into the ordinal numbers for some $\beta \in \alpha$ with sup ran f = sup ran g.

Proof We will construct g so that it is a subsequence of f. That is, we will have $g_{\xi} = f_{h_{z}}$ for a certain increasing sequence h.

First define the sequence $h$ by transfinite recursion over $\langle \alpha, \in_{\alpha} \rangle$ . Suppose that $h_{\delta}$ is known for every $\delta \in \xi$ . Then define

$$
h _ {\xi} = \text { the   least } \gamma \text { such   that } f _ {h _ {\delta}} \in f _ {\gamma} \text { for   all } \delta \in \xi ,
$$

if any such $\gamma$ exists; if no such $\gamma$ exists, then the sequence halts. Let $\beta = \operatorname{dom} h$ , and define

$$
g _ {\xi} = f _ {h _ {\xi}} \quad \text {   for   } \quad \xi \in \beta .
$$

Then by construction,

$$
\delta \in \xi \Rightarrow f _ {h _ {\delta}} \in f _ {h _ {\xi}} \Rightarrow g _ {\delta} \in g _ {\xi},
$$

so g is increasing. Also h is increasing, because h is one-to-one and $h_{\xi}$ is the least ordinal meeting certain conditions that become more stringent as $\xi$ increases.

We have ran $g \subseteq \operatorname{ran} f$ , so certainly sup ran $g \in \sup \operatorname{ran} f$ . On the other hand we have

$$
f _ {\delta} \in f _ {h _ {\xi}} = g _ {\xi} \quad \text {   for   all   } \quad \delta \in h _ {\xi}
$$

by the leastness of $h_{\xi}$ . In particular, $\xi \in h_{\xi}$ , so $f_{\xi} \in g_{\xi}$ . Hence if $\beta = \alpha$ , then clearly sup ran $f \in \sup r$ and $g$ . But if $\beta$ is less than $\alpha$ , it is only because there exists no $\gamma$ for which $f_{\gamma}$ exceeds every $g_{\delta}$ for $\delta \in \beta$ . Again we conclude that sup ran $f \in \sup r$ and $g$ .

This lemma is used in the proof of the following theorem.

Theorem 9Q Assume that $\lambda$ is a limit ordinal. Then there is an increasing (cf $\lambda$ )-sequence into $\lambda$ that converges to $\lambda$ .

Proof By definition of cofinality, $\lambda$ is the supremum of cf $\lambda$ smaller ordinals. That is, there is a function f from cf $\lambda$ into $\lambda$ such that $\lambda = \sup \operatorname{ran} f$ . Apply the lemma to obtain an increasing $\beta$ -sequence converging to $\lambda$ for some $\beta \in cf \lambda$ . But it is impossible that $\beta \in cf \lambda$ , lest we have $\lambda$ represented as the supremum of card $\beta$ smaller ordinals, contradicting the leastness of cf $\lambda$ .

Corollary 9R For a limit ordinal $\lambda$ , we can characterize cf $\lambda$ as the least ordinal $\alpha$ such that some increasing $\alpha$ -sequence into $\lambda$ converges to $\lambda$ .

We know that cf $\lambda \leq \lambda$ . What about cf cf $\lambda$ ? Or cf cf cf $\lambda$ ? These are all equal to cf $\lambda$ , by the next theorem.

Theorem 9S For any ordinal $\lambda$ , cf $\lambda$ is a regular cardinal.

Proof We must show that cf cf $\lambda = cf \lambda$ . We may assume that $\lambda$ is a limit ordinal, since 0 and 1 are regular. By the preceding theorem, there is an increasing (cf $\lambda$ )-sequence f that converges to $\lambda$ .

Suppose that cf $\lambda$ is the supremum of some set S of smaller ordinals; we must show that cf $\lambda \leq card S$ . (This will prove that cf $\lambda \leq cf$ $\lambda$ and will be done.) To do this, consider the set

$$
f [ [ S ] ] = \{f _ {\alpha} | \alpha \in S \}.
$$

This is a subset of $\lambda$ having the same cardinality as $S$ . It suffices to show that $f[[S]]$ is cofinal in $\lambda$ , since this implies that

$$
\operatorname{cf} \lambda \leq \operatorname{card} f [ [ S ] ] = \operatorname{card} S.
$$

Consider then any $\alpha \in \lambda$ . Since $f$ converges to $\lambda$ , we have $\alpha \in f(\beta) \in \lambda$ for some $\beta \in \operatorname{cf} \lambda$ . Since $\operatorname{cf} \lambda = \sup S$ , we have $\beta \in \gamma \in S$ for some $\gamma$ . Hence

$$
\alpha \in f (\beta) \in f (\gamma) \in f [ [ S ] ].
$$

So $f[[S]]$ is indeed cofinal in $\lambda$ .

Now we want to study the particular case where $\lambda$ is an infinite cardinal number. In this case, we can give an “all cardinal” characterization of cf $\lambda$ that makes no direct mention of ordinal numbers.

Theorem 9T Assume that $\lambda$ is an infinite cardinal. Then cf $\lambda$ is the least cardinal number $\kappa$ such that $\lambda$ can be decomposed into the union of $\kappa$ sets, each having cardinality less than $\lambda$ .

Proof We know that $\lambda$ is the union of cf $\lambda$ smaller ordinals, and any smaller ordinal $\alpha$ satisfies

$$
\operatorname{card} \alpha \in \alpha \in \lambda = \operatorname{card} \lambda .
$$

Hence $\lambda$ can be represented as the union of cf $\lambda$ sets of cardinality less than $\lambda$ . It remains to show that we cannot make do with fewer than cf $\lambda$ such sets.

So consider an arbitrary decomposition $\lambda = \bigcup \mathcal{A}$ where each member of $\mathcal{A}$ has cardinality less than $\lambda$ . Let $\kappa = \operatorname{card} \mathcal{A}$ ; we seek to prove that $\operatorname{cf} \lambda \leq \kappa$ . We can express $\mathcal{A}$ as the range of a $\kappa$ -sequence of sets:

$$
\mathscr {A} = \left\{A _ {\xi} \mid \xi \in \kappa \right\}.
$$

Thus $\lambda = \bigcup \{A_{\xi} | \xi \in \kappa\}$ and card $A_{\xi} < \lambda$ .

Define the cardinal $\mu = \sup \{\text{card } A_{\xi} \mid \xi \in \kappa\}$ . Then each card $A_{\xi} \leq \mu$ and so $\lambda = \text{card } \bigcup \{A_{\xi} \mid \xi \in \kappa\} \leq \mu \cdot \kappa$ (compare Exercise 26 of Chapter 6).

Case I $\lambda \leq \kappa$ . Then cf $\lambda \leq \lambda \leq \kappa$ , so we are done.

Case II $\kappa < \lambda$ . Then since $\lambda \leq \mu \cdot \kappa$ , we can conclude that $\lambda = \mu$ . Thus we have $\lambda = \sup \{\text{card } A_{\xi} | \xi \in \kappa\}$ , so $\lambda$ is the supremum of $\kappa$ smaller ordinals. Hence cf $\lambda \leq \kappa$ .

Cantor's theorem tells us that $2^{\kappa}$ is always greater than $\kappa$ . The following theorem tells us that even cf $2^{\kappa}$ is greater than $\kappa$ .

König's Theorem Assume that $\kappa$ is an infinite cardinal number. Then $\kappa < \operatorname{cf} 2^{\kappa}$ .

Proof Suppose to the contrary that cf $2^{\kappa} \leq \kappa$ . Then $2^{\kappa}$ , and consequently any set of size $2^{\kappa}$ , is representable as the union of $\kappa$ sets each of size less than $2^{\kappa}$ . The particular set to consider is $^{\kappa}S$ , where S is some set of size $2^{\kappa}$ . (Thus card $^{\kappa}S = (2^{\kappa})^{\kappa} = 2^{\kappa}$ .)

We have, then, a representation of the form

$$
{ } ^ { \kappa } S = \bigcup \{ A _ { \xi } | \xi \in \kappa \} ,
$$

where card $A_{\xi} < 2^{\kappa}$ . For any one $\xi$ in $\kappa$ ,

$$
\{g (\xi) \mid g \in A _ {\xi} \} \subseteq S.
$$

Furthermore we have proper inclusion, because $\operatorname{card}\{g(\xi) | g \in A_{\xi}\} \leq \operatorname{card} A_{\xi} < 2^{\kappa}$ , whereas $\operatorname{card} S = 2^{\kappa}$ . So we can choose some point

$$
s _ {\xi} \in S - \{g (\xi) \mid g \in A _ {\xi} \}.
$$

This construction yields a $\kappa$ -sequence $s$ , i.e., $s \in {}^{\kappa} S$ . But $s \notin A_{\xi}$ for any $\xi \in \kappa$ , by the construction.

Corollary 9U $2^{\aleph_0}\neq \aleph_\omega$

Proof By König's theorem, cf $2^{\aleph_0}$ is uncountable. But cf $\aleph_{\omega} = \aleph_0$ .

## Exercises

12. For any set S of ordinals, define the strict supremum of S, ssup S, to be the least ordinal strictly greater than every member of S. Show that the cofinality of any ordinal $\alpha$ (zero, successor, or limit) is the least cardinal $\kappa$ such that $\alpha$ is the strict supremum of $\kappa$ smaller ordinals.

13. Show that cf $\beth_{\lambda} = \operatorname{cf}\lambda$ for any limit ordinal $\lambda$ .

14. Assume that $R$ is a well-founded relation, $\kappa$ is a regular infinite cardinal, and $\operatorname{card}\{x \mid xRy\} < \kappa$ for each $y$ . Prove that $\operatorname{card}\{x \mid xR^t y\} < \kappa$ for each $y$ .

15. Prove that any inaccessible cardinal is also weakly inaccessible.

16. Assume that $\lambda$ is weakly inaccessible, i.e., it is a limit ordinal for which $N_{\lambda}$ is regular. Further assume that the generalized continuum hypothesis holds. Show that $\lambda$ is an inaccessible cardinal.

17. (König) Assume that for each $i$ in a set $I$ we are given sets $A_{i}$ and $B_{i}$ with card $A_{i} < \text{card } B_{i}$ . Show that card $\bigcup_{i \in I} A_{i} < \text{card } \mathsf{X}_{i \in I} B_{i}$ . [Suggestion: If $f$ maps $\bigcup_{i \in I} A_{i}$ onto $\mathsf{X}_{i \in I} B_{i}$ , then select a point $b_{i}$ in $B_{i}$ not in the projection of $f[[A_{i}]]$ .]

18. Consider the operation assigning to each ordinal number $\alpha$ its cofinality of $\alpha$ . Is this operation monotone? Continuous? Normal? (Give proofs or counterexamples.)

19. Assume that $\kappa$ is a regular cardinal and that $S$ is a subset of $V_{\kappa}$ with card $S < \kappa$ . Show that $S \in V_{\kappa}$ .

20. Consider a normal operation assigning $t_{\alpha}$ to each ordinal number $\alpha$ , and assume that $\lambda$ is a limit ordinal. Show that $\operatorname{cf} t_{\lambda} = \operatorname{cf} \lambda$ .

# NOTATION, LOGIC, AND PROOFS

In Chapters 1 and 2 we described how formulas of the language of set theory could be built up from component parts. We start with the indivisible “atomic” formulas, such as ‘x ∈ S’ and ‘x = y’. Once we know what objects are named by the letters ‘x’, ‘y’, and ‘S’, we can consider the truth or falsity of such formulas. $^{1}$

Given any formulas $\varphi$ and $\psi$ , we can combine them in various ways to obtain new ones. For example, $(\varphi \& \psi)$ will be a new formula. The intended meaning of the ampersand can be captured by giving a truth table (Table 1). And similarly we can specify by this table that 'or' is to mean "one or the other or both." A simpler case is ' $\neg$ '; the truth value of $(\neg \varphi)$ is determined by the last column of Table 1.

TABLE 1

<table><tr><td> $\varphi$ </td><td> $\psi$ </td><td> $(\varphi \& \psi)$ </td><td> $(\varphi \text{ or } \psi)$ </td><td> $(\neg \varphi)$ </td></tr><tr><td> $T$ </td><td> $T$ </td><td> $T$ </td><td> $T$ </td><td> $F$ </td></tr><tr><td> $T$ </td><td> $F$ </td><td> $F$ </td><td> $T$ </td><td> $F$ </td></tr><tr><td> $F$ </td><td> $T$ </td><td> $F$ </td><td> $T$ </td><td> $T$ </td></tr><tr><td> $F$ </td><td> $F$ </td><td> $F$ </td><td> $F$ </td><td> $T$ </td></tr></table>

Example We can show that the truth value, $T$ or $F$ , of $\lceil (\neg (\varphi \& \psi)) \rceil$ is always the same as the truth value of $\lceil ((\neg \varphi) \text{ or } (\neg \psi)) \rceil$ by making a table (Table 2) illustrating every possibility.

TABLE 2

<table><tr><td> $\varphi$ </td><td> $\psi$ </td><td> $(\neg(\varphi \& \psi))$ </td><td> $((\neg\varphi) \text{ or } (\neg\psi))$ </td></tr><tr><td> $T$ </td><td> $T$ </td><td> $F$ </td><td> $F$ </td></tr><tr><td> $T$ </td><td> $F$ </td><td> $T$ </td><td> $T$ </td></tr><tr><td> $F$ </td><td> $T$ </td><td> $T$ </td><td> $T$ </td></tr><tr><td> $F$ </td><td> $F$ </td><td> $T$ </td><td> $T$ </td></tr></table>

Example The truth value of $\left( \varphi \& (\psi \text{ or } \theta) \right)'$ is always the same as the truth value of $\left( \left( \varphi \& \psi \right) \text{ or } (\varphi \& \theta) \right)'$ . The table for this must have eight lines to cover all possibilities. You are invited to contemplate the relationship of this example to Fig. 5 in Chapter 2.

The formula $\left( \varphi \Rightarrow \psi \right)'$ is to be read as "if $\varphi$ , then $\psi$ ." The exact meaning is determined by Table 3. Note in particular that the formula is "vacuously" true whenever $\varphi$ is false. The formula is sometimes read as " $\varphi$ implies $\psi$ ." This usage of the word "implies" is a conventional part of mathematical jargon, but it is not exactly the way the rest of the world used the word.

TABLE 3

<table><tr><td> $\varphi$ </td><td> $\psi$ </td><td> $(\varphi \Rightarrow \psi)$ </td><td> $(\varphi \Leftrightarrow \psi)$ </td></tr><tr><td> $T$ </td><td> $T$ </td><td> $T$ </td><td> $T$ </td></tr><tr><td> $T$ </td><td> $F$ </td><td> $F$ </td><td> $F$ </td></tr><tr><td> $F$ </td><td> $T$ </td><td> $T$ </td><td> $F$ </td></tr><tr><td> $F$ </td><td> $F$ </td><td> $T$ </td><td> $T$ </td></tr></table>

Example The truth value of $\left( \varphi \Rightarrow \psi \right)'$ is always the same as the truth value of its contrapositive $\left( (\neg \psi) \Rightarrow (\neg \varphi) \right)'$ . (You should check this.) Sometimes when it is desired to prove a formula of the form $\left( \varphi \Rightarrow \psi \right)'$ , it is actually more convenient to prove $\left( (\neg \psi) \Rightarrow (\neg \varphi) \right)'$ . And this suffices to establish the truth of $\left( \varphi \Rightarrow \psi \right)'$ .

Example If $\theta$ is true, then the truth value of $r((\neg \varphi) \Rightarrow (\neg \theta))'$ is the same as the truth value of $\varphi$ . Sometimes to prove $\varphi$ , we proceed in an indirect way: We show that $r(\neg \varphi)$ would lead to a result contradicting what is already known to be true, i.e., we use a "proof by contradiction."

Example The truth value of $\left( \neg (\varphi \Rightarrow \psi) \right)'$ is the same as the truth value of $\left( \varphi \& (\neg \psi) \right)'$ . This is reflected in the fact that to give a counterexample to show that $\left( \varphi \Rightarrow \psi \right)'$ is false, we give an example in which $\varphi$ is true and $\psi$ is false.

To construct any interesting formulas, we must use (in addition to features already mentioned) the phrases “for all x” and “for some x.” These phrases can be symbolized by ‘∀x’ and ‘∃x’, respectively. If φ is a formula (in which ‘x’ occurs but ‘∀x’ and ‘∃x’ do not), then the condition for ‘∀x φ’ to be true is that φ should be true no matter what ‘x’ names (in the universe of all sets). And the condition for ‘∃x φ’ to be true is that there is at least one thing (in the universe of all sets) such that φ is true when ‘x’ names that thing. These criteria do not reduce to simple tables. There is no mechanical procedure that can be substituted for clear thinking.

Example The truth value of $\lceil (\neg \forall x \varphi) \rceil$ is the same as the truth value of $\lceil \exists x(\neg \varphi) \rceil$ . To deny that $\varphi$ is true of everything is to assert that there is at least one thing of which $\varphi$ is false, and of which $\lceil (\neg \varphi) \rceil$ is consequently true. Similarly the truth value of $\lceil (\neg \exists x \varphi) \rceil$ is the same as the truth value of $\lceil \forall x(\neg \varphi) \rceil$ .

Example Suppose that $\exists x \forall y \varphi$ is true. Then, reading from left to right, we can say that there is some set x for which $\forall y \varphi$ is true. That is, there is at least one set that, when we bestow the name 'x' upon it, we then find that no matter what set 'y' names, $\varphi$ is true. This guarantees that the weaker statement $\forall y \exists x \varphi$ is true. This weaker statement demands only that for any set (upon which we momentarily bestow the name 'y') there exists some set (which we call 'x') such that $\varphi$ is true. The difference here is that the choice of x may depend on y, whereas $\exists x \forall y \varphi$ demands that there be an x fixed in advance that is successful with every y. For example, it is true of the real numbers that for every number y there is some number x (e.g., $x = y + 1$ ) with y < x. But the stronger statement, that there is some number x such that for every number y we have y < x, is false. Or to give a different sort of example, it may well be true that every boy has some girl whom he admires, and yet there is no one girl so lucky as to be admired by every boy.

Next we want to give an example of a proof. Actually, the book is full of proofs. But what we want to do now is to illustrate how one constructs a proof, without knowing in advance how to do it. After one knows how the proof goes, it can be written out in the conventional form followed by contemporary mathematics books. But before one knows how the proof goes, it is a matter of looking at the assumptions and the conclusions and trying to gain insight into the connection between them. Suppose, for example, one wants to prove the assertion:

$$
a \in B \Rightarrow \mathscr {P} a \in \mathscr {P P} \bigcup B.
$$

We will present the process of constructing the proof as a discussion among three mental states: Prover, Referee, and Commentator.

P: We assume that $a \in B$ .

C: We might as well, because the assertion to be proved is vacuously true if $a \notin B$ .

R: It is to be proved that $Pa \in PP \cup B$ .

C: Always keep separate the facts you have available and the facts that you want to establish.

P: I have $a \in B$ , but it is not obvious how to utilize that fact.

R: Look at the goal. It suffices to show that $\mathcal{P}a\subseteq\mathcal{P}\bigcup B$ , by the definition of $\mathcal{P}$ .

P: Well, in that case I will assume that $c \in \mathcal{P}a$ .

R: Then the goal is to show that $c \in P \cup B$ .

C: The point is to consider an arbitrary member (call it $c$ ) of $\mathcal{P}a$ , and show that it belongs to $\mathcal{P} \bigcup B$ . Then we can conclude that $\mathcal{P}a \subseteq \mathcal{P} \bigcup B$ .

P: $c \subseteq a.$

R: The goal is to get $c \subseteq \bigcup B$

C: This pair of sentences is a recasting of their previous pair, using definitions.

P: Since I am expected to prove that $c \subseteq \bigcup B$ , I will consider any $x \in c$ .

R: The goal now is to get $x \in \bigcup B$ .

P: Looking back, I see that

$$
x \in c \subseteq a \in B.
$$

R: But you want $x \in \bigcup B$ .

P: $x \in a \in B$ , so I have $x \in \bigcup B$ .

C: The job is done. The information Prover has is the same as the information Referee wants.

Now that the mental discussion is over, the proof can be written out in the conventional style. Here it is:

Proof Assume that $a \in B$ . To show that $\mathcal{P}a \in \mathcal{PP} \bigcup B$ , it suffices to show that $\mathcal{P}a \subseteq \mathcal{P} \bigcup B$ . So consider any $c \in \mathcal{P}a$ . Then we have

$$
\begin{array}{r c l} x \in c & \Rightarrow & x \in c \subseteq a \in B \\ & \Rightarrow & x \in a \in B \\ & \Rightarrow & x \in \bigcup B. \end{array}
$$

Thus $c \subseteq \bigcup B$ and $c \in \mathcal{P} \bigcup B$ . Since $c$ was arbitrary in $\mathcal{P}a$ , we have shown that $\mathcal{P}a \subseteq \mathcal{P} \bigcup B$ , as desired.

We conclude this appendix with some comments on a task mentioned in Chapter 2. In that chapter there is a fairly restrictive definition of what a formula is. In particular, to obtain a legal formula, it is necessary to get rid of the defined symbols, such as ‘∅’, ‘∪’, ‘P’, etc. We will indicate a mechanical procedure for carrying out this elimination process.

Suppose then, we have a statement ‘\_Pt \_’ in which ‘P’ occurs. We can rewrite it first as

$$
\forall a (a = \mathscr {P} t \Rightarrow \_ a \_)
$$

and then rewrite 'a = P t' as

$$
\forall x (x \in a \Leftrightarrow x \in \mathscr {P} t).
$$

This reduces the problem to eliminating ‘P’ from statements of the form ‘x ∈ Pt’. And this is easy; ‘x ∈ Pt’ can be replaced by ‘x ⊆ t’ or by ‘∀y(y ∈ x ⇒ y ∈ t)’.

This process is similar for other symbols. For the union symbol, we reduce the problem to eliminating ‘∪’ from ‘x ∈ ∪t’. And the definition of ‘∪’ tells us how to do this; we replace ‘x ∈ ∪t’ by ‘∃y(x ∈ y ∈ t)’.

The image contains no text. The visible element is a stylistic or background line, which must be ignored according to the rules.

# SELECTED REFERENCES FOR FURTHER STUDY

Georg Cantor. Contributions to the Founding of the Theory of Transfinite Numbers, translated by P. Jourdain. Dover, New York, 1955.
This is a translation of two papers that Cantor originally published in 1895 and 1897. The papers treat cardinal and ordinal numbers and their arithmetic. Jourdain's introduction, first published in 1915, discusses Cantor's work in historical perspective.

Paul J. Cohen. Set Theory and the Continuum Hypothesis. Benjamin, New York, 1966.
This gives a highly condensed account of the main results in the metamathematics of set theory.

Frank R. Drake. Set Theory, An Introduction to Large Cardinals. North-Holland Publ., Amsterdam, 1974.
This book treats the implications that large cardinals have for the metamathematics of set theory, along with other related topics.

Abraham A. Fraenkel, Yehoshua Bar-Hillel, and Azriel Levy. Foundations of Set Theory, 2nd rev. ed. North-Holland Publ., Amsterdam, 1973. This book considers the philosophical background for set theory

and the foundations of mathematics. Different approaches to set theory are developed and compared. Among the topics discussed are the limitations of axiomatizations, the role of classes in set theory, and the history of the axiom of choice.

Thomas J. Jech. The Axiom of Choice. North-Holland Publ., Amsterdam, 1973.

Centered on the topic of its title, this book contains much material on the metamathematics of set theory.

K. Kuratowski and A. Mostowski. Set Theory. PWN—Polish Scientific Publ., Warsaw, and North-Holland Publ., Amsterdam, 1968.

In addition to the standard topics of set theory, this book has considerable material on the applications of set theory, particularly to topology. The footnotes provide a guide to the history of set-theoretic ideas.

Wacław Sierpiński. Cardinal and Ordinal Numbers, 2nd ed. PWN—Polish Scientific Publ., Warsaw, 1965.

This is a classic book on cardinal and ordinal arithmetic, the axiom of choice, and related topics. The approach is nonaxiomatic.

Jean van Heijenoort (editor). From Frege to Gödel, A Source Book in Mathematical Logic, 1879–1931. Harvard Univ. Press, Cambridge, Massachusetts, 1967.

This is a collection of forty-six fundamental papers in logic and set theory, translated into English and supplied with commentaries. There is an 1899 letter from Cantor to Dedekind and the 1902 correspondence between Russell and Frege. Zermelo's 1908 paper giving the first axiomatization of set theory is included, as are papers by Fraenkel, Skolem, and von Neumann.

# LIST OF AXIOMS

Extensionality axiom

$$
\forall A \forall B [ \forall x (x \in A \Leftrightarrow x \in B) \Rightarrow A = B ]
$$

Empty set axiom

$$
\exists B \forall x x \notin B
$$

Pairing axiom

$$
\forall u \forall v \exists B \forall x (x \in B \Leftrightarrow x = u \text { or } x = v)
$$

Union axiom

$$
\forall A \exists B \forall x [ x \in B \Leftrightarrow (\exists b \in A) x \in b ]
$$

Power set axiom

$$
\forall a \exists B \forall x (x \in B \Leftrightarrow x \subseteq a)
$$

Subset axioms For each formula $\varphi$ not containing $B$ , the following is an axiom:

$$
\forall t _ {1} \dots \forall t _ {k} \forall c \exists B \forall x (x \in B \Leftrightarrow x \in c \& \varphi)
$$

Infinity axiom

$$
\exists A [ \emptyset \in A \& (\forall a \in A) a ^ {+} \in A ]
$$

Choice axiom

$(\forall$ relation $R)(\exists$ function $F)(F \subseteq R \& \operatorname{dom} F = \operatorname{dom} R)$

Replacement axioms For any formula $\varphi(x, y)$ not containing the letter B, the following is an axiom:

$$
\begin{array}{r c l} \forall t _ {1} \dots \forall t _ {k} \forall A [ (\forall x \in A) \forall y _ {1} \forall y _ {2} (\varphi (x, y _ {1}) \& \varphi (x, y _ {2}) & \Rightarrow & y _ {1} = y _ {2}) \\ \Rightarrow & \exists B   \forall y (y \in B \Leftrightarrow (\exists x \in A) \varphi (x, y)) ] \end{array}
$$

Regularity axiom

$$
(\forall A \neq \emptyset) (\exists m \in A) m \cap A = \emptyset
$$

## INDEX

## A

Abelian group, 95, 122
Absolute value, 109, 118
Absorption law, 164
Abstraction, 4–6, 20–21, 30, 37
Addition, see Arithmetic
Additive inverse, 95, 104, 117
Aleph, 137, 212
Algebra of sets, 27–31
Algebraic numbers, 161
Antinomies, see Paradoxes
Archimedean, 120
Arithmetic
of cardinal numbers, 138–143, 149, 164
of integers, 92–100
of natural numbers, 79–82, 85
of order types, 222–226
of ordinal numbers, 227–239
of rational numbers, 103–110
of real numbers, 114–119
Associative laws, 28, see also Arithmetic
Atomic formula, 263

Atoms, 7–9, 13
Aussonderung axioms 15, 21, see also Subset axioms
Axiom of choice, see Choice axiom
Axiomatic method, 10–11, 66, 125
Axioms of set theory, 15, 166, 271–272, see also individual axioms

## B

Bar-Hillel, Yehoshua, 269  
Bernays, Paul, 15  
Bernstein, Felix, 148  
Bernstein's theorem, 147  
Berry, G., 6  
Berry paradox, 5  
Beth, 214, 254  
Binary operation, 79  
Binary relation, 42  
Borel, Émile, 148  
Bound, 114, 171  
Bounded, 114, 212

Burali-Forti, Cesare, 15, 194
Burali-Forti theorem, 194
Burrill, Claude, 112

## C

Cancellation laws
for cardinal numbers, 141
for integers, 100
for natural numbers, 86
for ordinal numbers, 234
for rational numbers, 110
for real numbers, 118

Canonical map, 58
Cantor, Georg, 14–15, 112, 148, 166. 194, 269–270

Cantor-Bernstein theorem, 148
Cantor normal form, 238
Cantor's theorem, 132, 261
Cardinal comparability, 151
Cardinal numbers, 136–137, 197. 199, 221
arithmetic of, 138–143, 149, 164
ordering of, 145

Cardinality, 137
Cartesian product, 37
infinite, 54

Cauchy sequence, 112
Chain, 151
descending, 173

Characteristic function, 131
Choice axiom, 11. 49. 55. 151–155. 198
Choice function, 151
Class, 6. 10. 15. 20
Closed, 68, 70, 107. 216

Closure, 78
transitive, 178. 244

Cofinal, 257
Cofinality, 257. 260
Cohen, Paul, 166. 269
Commutative diagram, 59
Commutative laws, 28. see also Arithmetic
Commutative ring, 122
Comparability, 151
Compatible, 60
Complement, 27. see also Relative complement
Complete ordered field, 119. 123
Composition, 44. 47
Comprehension. see Abstraction
Connected, 63

Constructed, 175–177, 180, 211
Constructive method, 66, 125
Constructivity, 154
Continuous, 216
Continuous functions, 165
Continuum hypothesis, 165, 215 generalized, 166, 215
Contradiction, proof by, 265
Contrapositive, 265
Converge, 259
Coordinate, 37, 54
Coordinate plane, 40
Corners, 263
Correspondence, 129
Countable, 159
Counterexample, 87, 265
Counting, 136, 197
Cut, 112–113

## D

De Morgan's laws, 28, 31, 264  
Dedekind, Richard. 14, 70, 157, 270  
Dedekind cut. 112–113  
Defined terms. 23, 267  
Denominator, 102  
Dense. 111, 227  
Derived operation, 219  
Descartes. René. 37  
Descending chain, 173  
Difference, 50, 91, see also Relative complement  
Disjoint. 3, 57  
Distributive laws. 28, 30, see also Arithmetic  
Divisibility. 40, 167  
Division. 107  
Division theorem. 236  
Domain. 40  
Dominate, 145  
Drake. Frank. 269

## E

Element. 1
Embedding. 100, 110, 119
Empty set. 2, 18
Empty set axiom. 18
End extension. 230
Enderton. Herbert. 12

Index

Epsilon, 16  
Epsilon-image, 182  
Epsilon numbers, 240  
Epsilon ordering, 191  
Equality, 2  
Equinumerous, 129  
Equivalence class, 57  
Equivalence concept, 132, 186  
Equivalence relation, 56  
Euler, Léonard, 43  
Even, 83  
Exhaustive, 57  
Exponentiation, see Arithmetic  
Extension, 125  
Extensional, 125  
Extensionality, 2, 12, 13, 17, 52

## F

Factorial, 144, 165
Field
    algebraic, 107, 122
    ordered, 109, 119, 123
    of set, 40
Finite, 133, 157
    cardinal, 137
Fixed point, 54, 218
Formula, 22–23, 263–265
    atomic, 263
Foundation axiom, see Regularity axiom
Foundations of mathematics, 10–12, 15,
    123–127, 250
Fourier series, 14
Fraction, 102
Fraenkel, Abraham, 15, 269, 270, see also
    Zermelo–Fraenkel set theory
Frege, Gottlob, 6, 15, 124–125, 270
Function, 42–43
    multiple-valued, 44
Function-class, 176, 179
Fundierungsaxiom, see Regularity axiom

## G

Galileo Galilei, 131
Gleason, Andrew, 119
Gödel, Kurt, 15, 166
Gödel–Bernays set theory. 15

Gödel's second incompleteness theorem, 250, 256  
Graph, 39, 42  
Greatest, 171  
Greatest common divisor, 172  
Greatest lower bound, 171  
Grounded, 204  
Group, 122, 154  
Abelian, 95, 122

## H

Hamilton, Norman, 113
Hartogs' theorem, 195
Hausdorff, Felix, 153
Hebrew lexicographic order, 224
Hereditarily finite, 256
Hilbert, David, 166
Historical notes, 6, 11, 14–16, 36, 43n, 67, 70, 111, 112, 124, 131, 148, 153, 154, 166, 194, 206, 256
Honesty, 124

## I

Identity element, 94–95, 97, 104, 106, 116, 119, 226, 229
Identity function, 40, 47
Identity principle, 2
Iff, 2
Image, 44, 50.
Imply, 264
Inaccessible, 254–256
weakly, 258
Inclusion, 3
proper, 85, 167
Increasing, 259, see also Monotone
Index set, 51, 54
Induction, 69
strong, 87
transfinite, 174, 200, 242
Inductive, 68, 174
Infimum, 171
Infinite 15, 133, 157
cardinal, 137
Infinity axiom, 68
Initial ordinal, 199
Initial segment, 173
Injection, 43

Integers, 75, 92, 121
arithmetic of, 92–100
ordering of, 98
Integral domain, 97, 122
Intensional, 125
Intersection, 3, 21, 24–25
indexed, 51
Interval, 44, 130
Into, 43
Inverse, 44, 46, see also Additive inverse,
Multiplicative inverse
left, 48
right, 48
Inverse image, 45, 51
Irreflexive, 63
Isomorphic, 77, 184
Isomorphic embedding, 100, 110, 119
Isomorphism, 184, 186
Isomorphism type, 207, 221

## J

Jech, Thomas, 270
Jourdain, Philip, 269

## K

König, Dénes, 249
König, Julius, 262
König's theorem, 261
Kronecker, Leopold, 14
Kuratowski, Kazimierz, 36, 153, 270

## L

Landin, Joseph, 113  
Language of set theory, see Formula  
Large cardinal axiom, 256  
Largest, 171  
Least, 87, 171  
Least common multiple, 172  
Least upper bound, 114, 171, see also Supremum  
Length, 160  
Less than, 83  
Levy, Azriel, 269  
Lexicographic ordering, 64, 185  
Hebrew, 224

Limit ordinal, 203  
Linear algebra, 58, 153  
Linear ordering, 62, 170  
Logarithm theorem, 237  
Logic, 12, 186, 263–267  
Logical consequence, 12  
Logicism, 15  
Loset, 170  
Lower bound, 171

## M

Map, 43
Mathematics, 126
Maximal, 151, 171
Maximum, 171
Measurement, 136, 187, 220
Member, 1, 11
Mendelson, Elliott, 119
Metamathematics, 16, 166, 253
Minimal, 170, 241
Minimum, 171
Mirimanoff, Dmitry, 15, 206
Model, 250
Monotone, 216, see also Increasing
Monotonicity, 30
Mostowski, Andrzej, 270
Multiplication, see Arithmetic
Multiplicative axiom, 151
Multiplicative inverse, 102, 107, 119

## N

n-ary relation, 42
n-tuples, 41
Naive set theory, 11
Natural map, 58
Natural numbers, 21, 66, 68
arithmetic of, 79–82, 85
ordering of, 83
Neumann, John von, see von Neumann,
John
Normal, 216
Notation, 13, see also Formula
Number, concept of, 123–127
Numbers, see Cardinal numbers, Integers,
Natural numbers, Ordinal numbers,
Rational numbers, Real numbers
Numeration theorem, 197
Numerology, 5

## 0

Odd, 83
One-to-one, 43
One-to-one correspondence, 129
Onto, 43
Operation
    binary, 79
    on ordinals, 215–216
Order-preservation in arithmetic
    for cardinal numbers, 149
    for integers, 99
    for natural numbers, 85
    for ordinal numbers, 234
    for rational numbers, 109
    for real numbers, 118–119
Order type, 189, 222, see also Isomorphism type
    arithmetic of, 222–226
Ordered field, 109, 119, 123
Ordered n-tuples, 41–42
Ordered pair, 35–36
Ordering
    of cardinal numbers, 145
    of integers, 98
    of natural numbers, 83
    of ordinal numbers, 192
    of rational numbers, 108
    of real numbers, 113
Orderings, 39–40
    lexicographic, 64, 185, 224
    linear, 62, 170
    partial, 168
    total, 62
    well, 172
Ordinal numbers, 8, 15, 182, 189, 191–194, 249
    arithmetic of, 227–239
    initial, 199
    limit, 203
    ordering of, 192
    successor, 203

## P

Pair set, 2, 19
ordered, 35–36
Pairing axiom, 18
Paradoxes, 5, 6, 11, 15, 21, 194
Partial ordering, 168

Partial well ordering, 245
Partition, 55, 57
Peano, Giuseppe, 16, 70
Peano induction postulate, 71
Peano system, 70, 76–77
Peano's postulates, 70
Perfect number, 5
Permutation, 144
Pigeonhole principle, 134
Pioneer, 221
Poset, 170
Positive, 99, 109
Power set, 4, 19, 141
Power set axiom, 18
Pre, 52
Primitive notions, 11
Proof, 12, 266
Proper class, 6, 15
Proper subset, 85, 134
Pure sets, 9
Pythagoreans, 111

## Q

Quadruples, 42
Quantifiers, 265
Quotient, 58
Quotient field, 107

## R

Range, 40
Rank, 9, 204, 206, 247–248
Rational numbers, 102, 121
    arithmetic of, 103–110
    ordering of, 108
Real numbers, 113, 121
    arithmetic of, 114–119
    ordering of, 113
Recursion, 73
    transfinite, 175, 177, 210, 245
Reflexive, 56
Regular, 254, 257
Regularity, 8, 205–206
Regularity axiom, 15, 84, 206
Relation, 40
    binary, 42
    equivalence, 56
    n-ary, 42
    ordering, 62

Relative complement, 21, 27  
Relativization, 250  
Replacement axioms, 15, 179, 253  
Restriction, 44, 189  
Richard, Jules, 6  
Ring, 122, 154  
Russell, Bertrand, 6, 15, 155, 206, 270  
Russell's paradox, 6, 11, 15, 21

## S

Schema, 33, 177  
Schröder, Ernst, 148  
Schröder-Bernstein theorem, 147  
Segment, 173  
Sequence, 52, 54, 160, 258  
Set, 1, 6–8, 11  
Sierpinski, Wacław, 270  
Single-rooted, 43  
Single-valued, 42  
Singleton, 19  
Singular, 257  
Size, 128  
Skolem, Thoralf. 15, 270  
Smallest, 171  
Space-filling curves, 149  
Strong induction, 87  
Structure, 170, 186  
Subsequence, 259  
Subset, 3  
proper, 85, 134  
Subset axioms, 21  
Subtraction, see Arithmetic  
Subtraction theorem, 235  
Successor, 68  
Successor ordinal, 203  
Supremum, 171, 193, 216  
strict, 258, 262  
Symmetric, 56  
Symmetric difference. 32

## T

Tarski, Alfred. 256  
Teichmüller–Tukey lemma. 158  
Ternary, 42  
Theorem. 12  
Thread, 54  
Total ordering, 62

Transcendental numbers, 161, 164
Transfinite induction, 174, 242
schema, 200
Transfinite numbers, 14, see also Cardinal numbers, Ordinal numbers
Transfinite recursion, 175, 177
on ordinals, 210
on well-founded relations, 245
Transitive closure, 178, 244
Transitive extension, 244
Transitive relation, 56, 243
Transitive set, 71–73
Trichotomy, 62–63, 99, see also Ordering Triples, 41
True, 250
Truth table, 29, 264
Truth value, 264
Tuples, 41, 54
Type, see Order type
Types (Russell), 206

## U

Unary, 42  
Undefined notions, see Primitive notions  
Union, 3, 19, 23  
indexed, 51  
Union axiom, 18, 24  
Universal set, 10, 22  
Upper bound, 114, 171  
Use and mention, 263

## v

Vacuous truth, 3, 264
Value. 43
van Heijenoort, Jean, 270
Veblen theorem, 218
Vector. 58, 153
Venn diagram, 29
von Neumann, John, 15, 67, 206, 270
von Neumann–Bernays set theory. 10, 15

## w

Well defined. 18, 59–60. 92. 98
Well founded. 241–242

Well ordering, 172
by epsilon, 191
of natural numbers, 86
partial, 245

Well-ordering theorem, 196

Wiener, Norbert, 36

Word, 160

Woset, 172

Z

Zermelo, Ernst, 6, 15, 67, 270

Zermelo-Fraenkel set theory, 10, 15, 252

Zermelo set theory, 252

Zero, 203

Zero divisor, 97, 107

ZF, see Zermelo-Fraenkel set theory

Zorn's lemma, 151, 153–154, 195