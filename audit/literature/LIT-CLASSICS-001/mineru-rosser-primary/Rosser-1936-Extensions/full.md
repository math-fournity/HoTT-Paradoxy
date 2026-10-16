Extensions of Some Theorems of Gödel and Church
Author(s): Barkley Rosser
Reviewed work(s):
Source: The Journal of Symbolic Logic, Vol. 1, No. 3 (Sep., 1936), pp. 87-91
Published by: Association for Symbolic Logic
Stable URL: http://www.jstor.org/stable/2269028
Accessed: 22/07/2012 05:26

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# EXTENSIONS OF SOME THEOREMS OF GÖDEL AND CHURCH

BARKLEY ROSSER $^{1}$

Introduction. We shall say that a logic is “simply consistent” if there is no formula A such that both A and $\sim A$ are provable. “ $\omega$ -consistent” will be used in the sense of Gödel. $^{2}$ “General recursive” and “primitive recursive” will be used in the sense of Kleene, $^{2}$ so that what Gödel calls “rekursiv” will be called “primitive recursive.” By an “Entscheidungsverfahren” will be meant a general recursive function $\phi(n)$ such that, if n is the Gödel number of a provable formula, $\phi(n)=0$ and, if n is not the Gödel number of a provable formula, $\phi(n)=1$ . In specifying that $\phi$ must be general recursive we are following Church $^{3}$ in identifying “general recursiveness” and “effective calculability.”

First, a modification is made in Gödel's proofs of his theorems, Satz VI (Gödel, p. 187—this is the theorem which states that $\omega$ -consistency implies the existence of undecidable propositions) and Satz XI (Gödel, p. 196—this is the theorem which states that simple consistency implies that the formula which states simple consistency is not provable). The modifications of the proofs make these theorems hold for a much more general class of logics. Then, by sacrificing some generality, it is proved that simple consistency implies the existence of undecidable propositions (a strengthening of Gödel's Satz VI and Kleene's Theorem XIII) and that simple consistency implies the non-existence of an Entscheidungsverfahren (a strengthening of the result in the last paragraph of Church). The class of logics for which these two results are proved is more general in some respects and less general in other respects than the class of logics for which Gödel's proof of Satz VI holds or the class of logics for which Kleene's proof of Theorem XIII holds.

## 1. Preliminary lemmas.

LEMMA I. Given a general recursive function $\phi(x, y_1, \cdots, y_n)$ and a number $k$ such that $(Ey_1, \cdots, y_n)[\phi(k, y_1, \cdots, y_n)=0]$ , there is a primitive recursive function $\gamma(m)$ such that $\gamma(0), \gamma(1), \gamma(2), \cdots$ is an enumeration (allowing repetitions) of the $x$ 's such that $(Ey_1, \cdots, y_n)[\phi(x, y_1, \cdots, y_n)=0]$ .

Proof.4 Let $\psi(y)$ and $R(x, y_1, \cdots, y_n, y)$ be chosen for $\phi(x, y_1, \cdots, y_n)$ as in the proof of IV of Kleene. Then put $\gamma(m) = \epsilon p[p \leq m + k \& \{R(1 Gl m, \cdots, [n+2]Gl m) \& \psi([n+2]Gl m) = 0 \& p = 1 Gl m\} \vee \{[R(1 Gl m, \cdots, [n+2]Gl m) \vee \psi([n+2]Gl m) \neq 0\} \& p = k\}\}$ . We note that the uniqueness clause of Definition 2b of Kleene allows one to add the clause “and $(\mathfrak{x}, y)[R(\mathfrak{x}, y) \to \psi(y) = \psi(\epsilon y[R(\mathfrak{x}, y)])]$ ” to IV of Kleene.

COROLLARY I. If a class can be enumerated (allowing repetitions) by a general recursive function, it can be enumerated (allowing repetitions) by a primitive recursive function.

For let $\phi(m)$ be general recursive and $\phi(0), \phi(1), \phi(2), \cdots$ be an enumeration of some class, then that class is just the class of all $x$ 's such that $(Ey)\phi(y)=x$ . But $[\phi(y)=x] \sim [(\phi(y) \div x) + (x \div \phi(y)) = 0]$ .

Although general recursive enumerability without repetitions is more general than primitive recursive enumerability without repetitions, the two concepts are equivalent when repetitions are allowed. For this reason “recursively enumerable” shall henceforth be understood as allowing repetitions and referring indifferently to enumeration by general or primitive recursive functions.

COROLLARY II. A general recursive class which is not null is recursively enumerable.

Put $n = 0$ in Lemma I.

The converse of this corollary is not true. For (cf. Footnote 16 and Theorem XV of Kleene) $(Ey)T_{1}(x,x,y)$ is a non-recursive class which is recursively enumerable. Also the class of well-formed formulas with normal forms (see Church) is not general recursive (Church, Theorem XVIII) and yet it can be enumerated, without repetitions, by a primitive recursive function. In this connection, Kleene has pointed out that if $\gamma(m)$ is primitive recursive and the class $(Em)[\gamma(m)=x]$ is not general recursive, then a primitive recursive function $\xi(m)$ can be defined such that the class $(Em)[\xi(m)=x]$ is not general recursive and $(m,n)[\xi(m)=\xi(n)\to m=n]$ . This is done by putting $\xi(m)=\epsilon z[z\leq2\gamma(m)+2m+1$ & $\{(n)[n<m\to\gamma(n)\neq\gamma(m)]\&z=2\gamma(m)\}\vee\{(En)[n<m\&\gamma(n)=\gamma(m)]\&z=2m+1\}\}$ .

DEFINITION. A set of rules of procedure for a logic is said to be general recursive if there is a general recursive function $\phi(n, x, y)$ such that “ $z$ is an immediate consequence of $x$ and $y$ ” is equivalent to “ $(En)[\phi(n, x, y) = z]$ ”.

LEMMA II. Let $C_1(x), \cdots, C_r(x)$ be recursively enumerable classes of numbers and $\phi_1(n, x, y), \cdots, \phi_s(n, x, y)$ be the determining functions of general recursive sets of rules of procedure. If $C(x)$ is the least class such that $(x)[C_i(x) \to C(x)]$ ( $i = 1, \cdots, r$ ) and $(n, x, y)[C(x) \& C(y) \to C(\phi_i(n, x, y))]$ ( $i = 1, \cdots, s$ ), then $C(x)$ is recursively enumerable.

Proof. Let $\theta_{i}(n)$ be the functions which enumerate $C_{i}(x)$ ( $i=1,\cdots,r$ ). Then put $\phi_{s+i}(n,x,y)=\theta_{i}(n)$ ( $i=1,\cdots,r$ ). Then it is easy enough to define recursively

$\phi (n,x,y)$ so that $\phi (n,x,y) = \phi_{\mathrm{Rem}(n,r + s) + 1}\left(\left[\frac{n}{r + s}\right],x,y\right)$ (cf. 21 in Kleene).

Then the class $C(x)$ is clearly the same as the least class $K(x)$ such that $K(\theta_1(0))$ and $(n, x, y)[K(x) \& K(y) \to K(\phi(n, x, y))]$ and by Theorem I, Kleene, this class is recursively enumerable.

2. Proofs of the theorems. P shall denote the system given in Gödel, pp. 176–178. The theorems shall be proved for P but the method of proqf will be general enough to apply to many other systems.

THEOREM I. If $P_{\kappa}$ is got by adding various axioms and rules of procedure to $P$ , and if the provable formulas of $P_{\kappa}$ are recursively enumerable:

A. If $P_{\kappa}$ is $\omega$ -consistent, then there is a primitive recursive class formula, $r$ , such that neither $v$ Gen $r$ nor $\text{Neg}(v \text{ Gen } r)$ is a provable formula in $P_{\kappa}$ (where $v$ is the free variable of $r$ ).

B. If $P_{\kappa}$ is simply consistent, then the formal proposition which says that $P_{\kappa}$ is simply consistent is not provable in $P_{\kappa}$ .

Proof. Let $\phi(m)$ be a primitive recursive function which enumerates the provable formulas of $P_{\kappa}$ . On pp. 188, 189, 196 and 197 of Gödel replace $x B_{\kappa}y$ by $\phi(x)=y$ and $\operatorname{Bew}_{\kappa}(y)$ by $(Ex)[\phi(x)=y]$ . Then the proof of Satz VI becomes a proof of A and the proof of Satz XI becomes a proof of B.

By this proof we gain in generality over Gödel's proofs in the following way. Gödel used the hypothesis that the class of axioms was a primitive recursive class and that the rules of procedure were primitive recursive. In view of Lemma II it is sufficient that the class of axioms be recursively enumerable (and by Lemma I, Corollary II, this is even less restrictive than requiring that the class of axioms be general recursive) and that the rules of procedure be general recursive.

THEOREM II. If $P_{\kappa}$ is got by adding various axioms and rules of procedure to $P$ , and if the provable formulas of $P_{\kappa}$ are recursively enumerable, and if $P_{\kappa}$ is simply consistent, then there is a primitive recursive class formula, $r$ , such that neither $v$ Gen $r$ nor $\text{Neg}(v \text{ Gen } r)$ is a provable formula in $P_{\kappa}$ (where $v$ is the free variable of $r$ ).

Proof. Let $\phi(m)$ be a primitive recursive function which enumerates the provable formulas and assume that $P_{\kappa}$ is simply consistent. Put $x B_{\kappa}y$ for $\phi(x)=y$ , $\operatorname{Bew}_{\kappa}(y)$ for $(Ex)[x B_{\kappa}y]$ , $x Pr_{\kappa}y$ for $x B_{\kappa}y \& (\overline{Ez})[z \leq x \& z B_{\kappa} \operatorname{Neg}(y)]$ and $\operatorname{Prov}_{\kappa}(y)$ for $(Ex)[x Pr_{\kappa}y]$ . Then $\operatorname{Bew}_{\kappa}(y) \sim \operatorname{Prov}_{\kappa}(y)$ . However this equivalence is not provable formally since it requires the hypothesis of simple consistency, which we know by Thm. I to be formally unprovable. Hence the formalization of $\operatorname{Prov}_{\kappa}(y)$ may, and does, have properties not possessed by the formalization of $\operatorname{Bew}_{\kappa}(y)$ . Such a property is the following (which will be proved shortly). If $b$ is the number of the formalization of $\operatorname{Prov}_{\kappa}(a)$ , then $\operatorname{Prov}_{\kappa}(a) \to \operatorname{Prov}_{\kappa}(b)$ and $\text{Prov}_k(\text{Neg}(a)) \to \text{Prov}_k(\text{Neg}(b))$ . By use of this property one can proceed as on p. 188 of Gödel, but with $x Pr_k y$ in place of Gödel's $x B_k y$ and $\text{Prov}_k(y)$ in place of Gödel's $\text{Bew}_k(y)$ , to find an undecidable proposition of the form $v$ Gen $r$ .

We now prove the aforementioned property of “Prov $_{x}$ ”. $x$ $B_{x}y$ and $(Ez)[z \leq x \& z \, B_{x} \, \text{Neg}(y)]$ are both primitive recursive relations. Hence by Satz V of Gödel, there are formulas $r$ and $s$ , both with the free variables $u$ and $v$ such that:

$$
x B _ {x} y \rightarrow \operatorname{Bew} _ {x} \left[ S b \left(\begin{array}{c c}u&v\\r&Z (x)\end{array}Z (y)\right)\right],\tag{1}
$$

$$
\overline {{{{x B _ {k} y}}}} \rightarrow \operatorname{Bew} _ {k} \left[ \operatorname{Neg} \left(S b \left(r\begin{array}{c c}u&v\\Z (x)&Z (y)\end{array}\right)\right)\right],\tag{2}
$$

$$
(E z) [ z \leq x \&z B _ {n} \operatorname{Neg} (y) ] \rightarrow \operatorname{Bew} _ {n} \left[ S b \left(s\begin{array}{c c}u&v\\Z (x)&Z (y)\end{array}\right)\right],\tag{3}
$$

$$
\overline {{(E z)}} [ z \leq x \&z B _ {\kappa} \operatorname{Neg} (y) ] \rightarrow \operatorname{Bew} _ {\kappa} \left[ \operatorname{Neg} \left(S b \left(s\begin{array}{c c}u&v\\Z (x)&Z (y)\end{array}\right)\right)\right].\tag{4}
$$

If $b$ is the number of the formalization of $\operatorname{Prov}_{\kappa}(a)$ , then clearly $\operatorname{Bew}_{\kappa}\left(b \operatorname{Aeq} u \operatorname{Ex}\left(Sb\left(r \begin{array}{c} v \\ Z(a) \end{array} \right) \text{Con} \operatorname{Neg}\left(Sb\left(s \begin{array}{c} v \\ Z(a) \end{array} \right)\right)\right)\right)$ . Hence $\operatorname{Prov}_{\kappa}(a) \to \operatorname{Prov}_{\kappa}(b)$ by (1), (4) and $\operatorname{Bew}_{\kappa}(y) \sim \operatorname{Prov}_{\kappa}(y)$ . Assume $x B_{\kappa} \operatorname{Neg}(a)$ . Then by induction within the system $P_{\kappa}$ and by use of (3), $\operatorname{Bew}_{\kappa}\left(Sb\left(s \begin{array}{cc} u & v \\ x N R(u) & Z(a) \end{array} \right)\right)$ (since this only requires the proof by induction of certain properties of the function $\chi$ given on p. 181 of Gödel). Also, by use of (2),

$$
\operatorname{Bew} _ {\kappa} \left(\operatorname{Neg} \left(S b \left(r \begin{array}{c c} u & v \\ Z (0) & Z (a) \end{array} \right)\right)\right),
$$

$$
\operatorname{Bew} _ {\kappa} \left(\operatorname{Neg} \left(S b \left(r \begin{array}{c c} u & v \\ Z (1) & Z (a) \end{array} \right)\right)\right),
$$

$$
\operatorname{Bew} _ {\kappa} \left(\operatorname{Neg} \left(S b \left(r \begin{array}{c c} u & v \\ Z (x) & Z (a) \end{array} \right)\right)\right),
$$

because $0B_{\kappa}a, 1B_{\kappa}a, \cdots, xB_{\kappa}a$ (since $\operatorname{Bew}_{\kappa}(\operatorname{Neg}(a))$ and $P_{\kappa}$ is simply consistent). But the formal analogue of $(z)[z=0 \vee z=1 \vee \cdots \vee z=x \vee(Ew)[z=x+w]]$ is provable in $P$ and hence in $P_{\kappa}$ , and so $\operatorname{Bew}_{\kappa}\left(u \operatorname{Gen}\left(\operatorname{Neg}\left(Sb\left(r \begin{array}{c}v \\ Z(a)\end{array}\right)\right) \operatorname{Dis} Sb\left(s \begin{array}{c}v \\ Z(a)\end{array}\right)\right)\right)$ . Hence $\operatorname{Prov}_{\kappa}(\operatorname{Neg}(a)) \to \operatorname{Prov}_{\kappa}(\operatorname{Neg}(b))$ .

telling whether or not a formula with no free variables is provable. Hence it is a corollary of Theorem III (stated below) that there is no Entscheidungsverfahren for $P_{\kappa}$ .

THEOREM III. If $P_{\kappa}$ is got by adding various axioms and rules of procedure to P, and if $P_{\kappa}$ is simply consistent, then there is no generally applicable effective process for determining whether or not a formula with no free variables is provable.

Proof. Assume that $P_{\kappa}$ is simply consistent and that there is a generally applicable effective process for determining whether or not a formula with no free variables is provable. Let us define $\phi(n)$ by the rule: $\phi(n)$ shall be 0 if $n$ is the number of a provable formula with no free variables, and 1 otherwise. Then $\phi(n)$ is effectively calculable and we shall follow Church in assuming that this necessitates that $\phi(n)$ be general recursive. Then the class of numbers of provable formulas with no free variables and the class of numbers which are not numbers of provable formulas with no free variables are both recursively enumerable. Also both are non-null. Let $\beta(m)$ and $\gamma(m)$ be primitive recursive functions which enumerate them respectively. Then there is a primitive recursive formula $\theta(m)$ such that $\theta(2n)=\beta(n)$ and $\theta(2n+1)=\gamma(n)$ . Then $\theta(m)$ enumerates all numbers in such a way that the numbers occurring in the even places are numbers of provable formulas with no free variables and the numbers occurring at the odd places are not numbers of provable formulas with no free variables. Now put $x B_{\kappa}y$ for $\theta(x)=y \& x/2$ , $\operatorname{Bew}_{\kappa}(y)$ for $(Ex)[x B_{\kappa}y]$ , $x Pr_{\kappa}y$ for $x B_{\kappa}y \& (\overline{Ez})[z \leq x \& \theta(z)=y \& \overline{z/2}]$ , and $\operatorname{Prov}_{\kappa}(y)$ for $(Ex)[x Pr_{\kappa}y]$ . Then $\operatorname{Bew}_{\kappa}(y) \sim \operatorname{Prov}_{\kappa}(y)$ . Now let $b$ be the number of the formalization of $\operatorname{Prov}_{\kappa}(a)$ . By a proof like that in the proof of Thm. II, it follows that $\operatorname{Prov}_{\kappa}(a) \to \operatorname{Prov}_{\kappa}(b)$ and $(Ez)[\theta(z)=a \& z/2] \to \operatorname{Prov}_{\kappa}(\operatorname{Neg}(b))$ . But if $\overline{\operatorname{Prov}_{\kappa}(a)}$ , then $(Em)[\gamma(m)=a]$ , and therefore $\theta(2(\epsilon m[\gamma(m)=a])+1)=a$ . Hence $\overline{\operatorname{Prov}_{\kappa}(a)} \to \operatorname{Prov}_{\kappa}(\operatorname{Neg}(b))$ . By use of this and $\operatorname{Prov}_{\kappa}(a) \to \operatorname{Prov}_{\kappa}(b)$ , one can derive a contradiction by proceeding as on p. 188 of Gödel, but with $x Pr_{\kappa}y$ and $\operatorname{Prov}_{\kappa}(y)$ in place of $x B_{\kappa}y$ and $\operatorname{Bew}_{\kappa}(y)$ respectively. With slight modifications, the proof above becomes a proof of:

With slight modifications the proof above becomes a proof of:

THEOREM IV. If $P_{\kappa}$ is got by adding various axioms and rules of procedure to P, and if $P_{\kappa}$ is simply consistent, then the class of numbers of provable formulas and the class of numbers of unprovable formulas are not both recursively enumerable.

From this theorem and Theorem III follow:

THEOREM V. If P is simply consistent, then:

A. The class of unprovable formulas is not recursively enumerable.

B. The class of undecidable formulas is not recursively enumerable.

C. The class of provable formulas is recursively enumerable but not general recursive.

D. The class of decidable formulas is recursively enumerable but not general recursive.

I wish to thank S. C. Kleene for reading an earlier draft of this paper and suggesting improvements.

HARVARD UNIVERSITY