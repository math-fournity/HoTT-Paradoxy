# CLASSES OF RECURSIVELY ENUMERABLE SETS AND THEIR DECISION PROBLEMS $^{(1)}$

BY

H. G. RICE

1. Introduction. In this paper we consider classes whose elements are recursively enumerable sets of non-negative integers. No discussion of recursively enumerable sets can avoid the use of such classes, so that it seems desirable to know some of their properties. We give our attention here to the properties of complete recursive enumerability and complete recursiveness (which may be intuitively interpreted as decidability). Perhaps our most interesting result (and the one which gives this paper its name) is the fact that no nontrivial class is completely recursive.

We assume familiarity with a paper of Kleene [5](2), and with ideas which are well summarized in the first sections of a paper of Post [7].

## I. FUNDAMENTAL DEFINITIONS

2. Partial recursive functions. We shall characterize recursively enumerable (r.e.) sets of non-negative integers by the partial recursive functions of Kleene. The set characterized (or, as we shall say more frequently, enumerated) by a partial recursive function of one variable will be taken as the range of values of the function. A function undefined for all arguments (and thus producing no values) will be considered to produce an enumeration of the empty set o.

Kleene has shown [5, pp. 50–58] that a Gödel enumeration of the partial recursive functions is possible, so that we may designate any partial recursive function of one variable as $\phi_n(x)$ , where $n$ is a Gödel number of the function. Actually, it requires only a minor adjustment of Kleene's constructions to insure that, not only does every function have at least one number, but that every non-negative integer $n$ is the number of some function. We shall assume this to be the situation, and shall make one other minor adjustment: $\phi_0(x)$ is the identity function.

Kleene further showed the existence of a recursive predicate $T(x, y, z)$ and a primitive recursive function $U(x)$ such that

$$
\phi_ {n} (x) = \Phi (n, x) = U (\mu y T (n, x, y))
$$

so that every partial recursive function of one variable can be written as $\Phi(n, x)$ for some $n$ .

This numbering enables us to characterize a class $A$ of sets by the set of all $n$ 's such that $\Phi(n, x)$ enumerates a set of $A$ , which leads to the definitions in the following section.

## 3. Definitions $^{(3)}$ .

DEFINITION. A class $A$ is recursively enumerable if there exists a partial recursive function $\Phi(r, x)$ with the following property: a set $\alpha \in A$ if and only if there is a number $a$ such that $\Phi(\Phi(r, a), x)$ enumerates $\alpha$ . The set $\beta$ enumerated by $\Phi(r, x)$ is called a recursive enumeration of $A$ .

DEFINITION. A class $A$ is completely recursively enumerable (c.r.e.) if there exists a partial recursive function $\Phi(r, x)$ with the following property: a partial recursive function $\Phi(a, x)$ enumerates a set $\alpha$ of $A$ if and only if there exists a number $b$ such that $\Phi(r, b) = a$ . The set of all $n$ 's such that $\Phi(n, x)$ enumerates a set of $A$ we shall denote by $\theta_A$ . $A$ is c.r.e. if and only if $\theta_A$ is r.e. From the fact that there are infinitely many partial recursive functions enumerating each r.e. set, it follows that $\theta_A$ is always either infinite or empty (in case $A$ is the empty class).

Lemma A is immediately evident from the definition, and Lemma B from Lemma A.

LEMMA A. $\theta_{A}$ is a complete (not necessarily recursive) enumeration of some class A if and only if it has the following property: if $\Phi(m, x)$ and $\Phi(n, x)$ enumerate the same set, then either both m and n are in $\theta_{A}$ , or neither is.

LEMMA B. If two sets $\theta_{A}$ and $\theta_{B}$ are complete enumerations of the classes A and B, then their union and intersection ( $\theta_{A} + \theta_{B}$ and $\theta_{A}\theta_{B}$ ) are complete enumerations of the classes $A + B$ and AB. This holds also for infinite unions and intersections.

DEFINITION. A class $A$ is completely recursive (c.r.) if $\theta_{A}$ is a recursive set. If we denote the class of all r.e. sets by $F$ , then the complement of $\theta_{A}$ is $\theta_{F-A}$ . So when $A$ is c.r., both $A$ and $F-A$ are c.r.e.

This definition, after Post, is equivalent to the following: A is c.r. when there exists a general recursive function $\Phi(s, x)$ such that if $\Phi(n, x)$ is a partial recursive function enumerating a set of A, then $\Phi(s, n) = 1$ , and if $\Phi(n, x)$ is a partial recursive function enumerating a set of F - A, $\Phi(s, n) = 0$ .

We shall refer to this as the strong definition of complete recursiveness. The weak definition is as follows: there exists a partial recursive function $\Phi(r, x)$ such that if $\Phi(n, x)$ is a general recursive function enumerating a set of A, then $\Phi(r,n)=1$ , and if $\Phi(n,x)$ is a general recursive function enumerating a set of F-A, $\Phi(r,n)=0$ . Clearly, if a class is c.r. by the strong definition, it is c.r. by the weak.

Two trivial classes are immediately c.r. by the strong definition. F is completely recursively enumerated by the identity function, and the empty class F-F by any function enumerating the empty set. Hereafter we consider only proper subclasses of F.

## II. COMPLETE RECURSIVE ENUMERABILITY

## 4. Existence of c.r.e. classes.

THEOREM 1. The class of all sets containing a given number $k$ (we denote this class by $L(k)$ ) is c.r.e.

Proof. $\theta_{L(k)}$ is the range of the partial recursive function

$$
K (x) \cdot (1 \div | \Phi (K (x), L (x)) - k |)
$$

where $K(x)$ and $L(x)$ are the Cantor diagonal functions:

$$
\begin{array}{c c c c c c c c c} x & 0 & 1 & 2 & 3 & 4 & 5 & 6 \\ K (x) & 0 & 0 & 1 & 0 & 1 & 2 & 0 & \text { etc. } \\ L (x) & 0 & 1 & 0 & 2 & 1 & 0 & 3 \end{array}
$$

(The reader will recall from I, 2 the assumption that $\Phi(0, x)$ is the identity function.)

We now give a method for constructing c.r.e. classes which seems to be very general. We suppose given a recursively enumerable sequence (the key array) of finite sets (the key sets), each set given by a finite sequence of numbers.

$$
\begin{array}{c c c c c} a _ {0} ^ {0} & a _ {1} ^ {0} & a _ {2} ^ {0} \cdot \cdot \cdot & a _ {n (0)} ^ {0} \\ a _ {0} ^ {1} & a _ {1} ^ {1} & a _ {2} ^ {1} \cdot \cdot \cdot & a _ {n (1)} ^ {1} \\ a _ {0} ^ {j} & a _ {1} ^ {j} & a _ {2} ^ {j} \cdot \cdot \cdot & a _ {n (j)} ^ {j} \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ a _ {0} ^ {j} & a _ {1} ^ {j} & a _ {2} ^ {j} \cdot \cdot \cdot & a _ {n (j)} ^ {j} \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot & \cdot & \cdot \\ a _ {0} ^ {0} = 0, a _ {1} ^ {0} = 0, a _ {2} ^ {0} = 0, a _ {3} ^ {0} = 0, a _ {4} ^ {0} = 0, a _ {5} ^ {0} = 0, a _ {6} ^ {0} = 0, a _ {7} ^ {0} = 0, a _ {8} ^ {0} = 0, a _ {9} ^ {0} = 0, a _ {1 0} ^ {0} = 0, a _ {1 1} ^ {0} = 0, a _ {1 2} ^ {0} = 0, a _ {1 3} ^ {0} = 0, a _ {1 4} ^ {0} = 0, a _ {1 5} ^ {0} = 0, a _ {1 6} ^ {0} = 0, a _ {1 7} ^ {0} = 0, a _ {1 8} ^ {0} = 0, a _ {1 9} ^ {0} = 0, a _ {2 0} ^ {0} = 0, a _ {2 1} ^ {0} = 0, a _ {2 2} ^ {0} = 0, a _ {2 3} ^ {0} = 0, a _ {2 4} ^ {0} = 0, a _ {2 5} ^ {0} = 0, a _ {2 6} ^ {0} = 0, a _ {2 7} ^ {0} = 0, a _ {2 8} ^ {0} = 0, a _ {2 9} ^ {0} = 0, a _ {3 0} ^ {0} = 0, a _ {3 1} ^ {0} = 0, a _ {3 2} ^ {0} = 0, a _ {3 3} ^ {0} = 0, a _ {3 4} ^ {0} = 0, a _ {3 5} ^ {0} = 0, a _ {3 6} ^ {0} = 0, a _ {3 7} ^ {0} = 0, a _ {3 8} ^ {0} = 0, a _ {3 9} ^ {0} = 0, a _ {4 0} ^ {0} = 0, a _ {\mathrm{foot}} ^ {\mathrm{foot}}. \\ a _ {\mathrm{foot}} ^ {\mathrm{foot}} = b (\mathrm{foot}) - b (\mathrm{foot}) + b (\mathrm{foot}) - b (\mathrm{foot}) + b (\mathrm{foot}) - b (\mathrm{foot}) + b (\mathrm{foot}) - b (\mathrm{foot}) + b (\mathrm{foot}) - b (\mathrm{foot}) + b (\mathrm{foot}) + b (\mathrm{foot}) + b (\mathrm{foot}) + b (\mathrm{foot}) + b (\mathrm{foot}) + b (\mathrm{foot}) + b (\mathrm{foot}) + b (\mathrm{foot}) + b (\mathrm{foot}) + b (\mathrm{foot}) + b (\mathrm{foot}) + b (\mathrm{foot}) + b (\mathrm{foot}) + b (\mathrm{foot}) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b) + b (b). \\ c o m p o r e s t i n g e d i s t i o n e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s. \\ c o m p o r e s t i n g e d i s t i o n e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m f o r e d i s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m f o r e d i s t i m e r s t i m e r s t i m e r s t i m e r s t i m f o r e d i s t i m f o r e d i s t i m f o r e d i s t i m f o r e d i s t i m f o r e d i s t i m f o r e d i s t i m f o r e d i s t i m f o r e d i s t i m f o r e d i s t i m f o r e d i s t i m f o r e d j u l l y n o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w | | | \\ c o m p o r e s t i n g e d i s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i n g. \\ c o m p o r e s t i n g e d i s t i m e r s t i m e r s t i m e r s t i m e r s t i m e r s t i n g. \\ c o m p o r e s t i n g e d j u l l y n o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w h o w | | | \\ c o m p o r e s t i n g e d j u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y. \\ c o m p o r e s t i n g e d j u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y. \\ c o m p o r e s t i n g e d j u l l y n u l l y n u l l y n u l l x y n x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x. \\ c o m p o r e s t i n g e d j u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y n u l l y. \\ c o m p o r e s t i n g e d j u l l y n u l l y n u l l Y N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X IN X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I NX I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X I N X | | | | \\ c o m p q / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / | | | | \\ c o m p q / / | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| c o m p q / / | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| c o m p q / / | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| c o m p q / / | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| c o m p q / / | | | | | | | | | | | | | | | | | | |
| c o m p q / / ] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b] [a,b]
$$

THEOREM 2. To every key array corresponds constructively a c.r.e. class; i.e., given the key array, we can construct a complete enumeration of the corresponding class.

Intuitively, we set all the partial recursive functions generating their values, and as soon as we see that the set enumerated by a function $\Phi(n, x)$ includes one of the key sets, we put n into $\theta_{A}$ . This must happen, if it is going to happen at all, in a finite length of time. A is then the class of all sets which include at least one of the key sets, and we have a constructive procedure for generating $\theta_{A}$ . (A simple formal proof of the recursive enumerability of $\theta_{A}$ will follow Theorem 3.)

Moreover, whether or not n is placed in $\theta_{A}$ depends only on a property (inclusion) of the set enumerated by $\Phi(n, x)$ , and not on the order in which $\Phi(n, x)$ may produce its values. To the author's intuition, this procedure for constructing an enumeration of $\theta_{A}$ is as general as any procedure can be and still satisfy the two essential requirements: first, it is effectively constructive, and second, it gives a complete enumeration of a class of sets. On this basis (to be further supported by Theorem 7, Corollary A) we venture the conjecture that every c.r.e. class has a key array, or, in the language of Theorem 3, the c.r.e. classes are just the $\sum \prod L$ classes.

THEOREM 3. A is a c.r.e. class determined by a key array if and only if A can be written as a r.e. union of finite intersections of $L(k)'s$ .

Proof. Suppose a set $\alpha$ of $A$ includes the $j$ th key set $\{a_0^j, \cdots, a_{n(j)}^j\}$ . This is a necessary and sufficient condition that

$$
\alpha \in \prod_ {i = 0} ^ {i = n (j)} L (a _ {i} ^ {j}).
$$

$A$ can then be written as

$$
\sum_ {j} \prod_ {i = 0} ^ {i = n (j)} L \left(a _ {i} ^ {j}\right).
$$

The union, if infinite, is recursively enumerable.

Conversely, any class composed of $L(k)$ 's in finite intersections and r.e. unions determines a key array. For since the associative and distributive laws hold for these operations, any such class can be reduced to the form

$$
\sum_ {\mathbf {r . e .}} \prod_ {\text { finite }} L (k)
$$

and a key array constructed from the k's appearing in the operations.

This theorem suggests the name “ $\sum \prod L$ class” for any class determined by a key array.

Proof of Theorem 2. If $A$ is a $\sum \prod L$ class, then, by Lemma B, $\theta_A = \sum \prod \theta_{L(k)}$ . We need only note that finite intersections and r.e. unions of r.e. sets are again r.e.

We have excluded intersections of infinitely many $L(k)$ 's. This case is disposed of in a corollary to Theorem 4.

5. Existence of classes which are not c.r.e.

THEOREM 4. No class containing only infinite sets is c.r.e.

Proof. Let A be a class containing only infinite sets, and let $\Phi(r, x)$ be a general recursive function enumerating an infinite set $\alpha \subset \theta_{A}$ . Then each of the functions $\Phi(\Phi(r, n), x)$ enumerates an infinite set of $A$ . Using Kleene's representation of $\Phi(n, x)$ as

$$
U (\mu y T (n, x, y)),
$$

we define

$$
\begin{array}{c} u (0) = K (\mu y T (\Phi (r, 0), K (y), L (y))), \\ u (n + 1) = K (\mu y \big [ T (\Phi (r, n + 1), K (y), L (y)) \& K (y) > u (n) + 1 \big ]), \end{array}
$$

and

$$
\begin{array}{r l} v (n) = U (L (\mu y \big [ T (\Phi (r, 0), K (y), L (y)) \& \\ & \qquad \Phi (\Phi (r, 0), K (y)) \neq \Phi (\Phi (r, n), u (n)) ])). \end{array}
$$

Now the task of $u(n)$ is to find an argument for which $\Phi(\Phi(r, n), x)$ is defined and which is greater by at least 2 than the corresponding argument found for any m < n. Since each of the $\Phi(\Phi(r, n), x)$ produces infinitely many values, $u(n)$ is always defined and produces its values in strictly increasing order. $v(n)$ , on the other hand, finds a value produced by $\Phi(\Phi(r, 0), x)$ which is different from the value of $\Phi(\Phi(r, n), u(n))$ .

Finally, let us define $w(x)$ as the recursive characteristic function of the infinite complement of the recursive set enumerated by $u(x)$ . We are now ready to construct a function $\Phi(s, x)$ such that $s \in \theta_{A} - \alpha$ .

If $w(x) = 1$ , then $f(x) = \Phi(\Phi(r, 0), \sum_{z=0}^{z=x} w(z) \div 1)$ .

If $w(x) = 0$ , then there exists a unique $y$ such that $u(y) = x$ . Then $f(x) = v(y)$ .

With a little more trouble, such a definition of $f(x)$ may be given as will formally establish it as a partial recursive function, say $\Phi(s, x)$ . Now $s \in \theta_{A}$ , for $\Phi(s, x)$ enumerates the same set as does $\Phi(\Phi(r, 0), x)$ . On the other hand, $s \notin \alpha$ , for $\Phi(s, x)$ differs from every function $\Phi(\Phi(r, n), x)$ for at least the argument $x = u(n)$ .

Thus we see that no infinite r.e. set $\alpha$ can exhaust $\theta_{A}$ ; nor can any finite set, so that $\theta_{A}$ is not r.e.

COROLLARY A. No infinite intersection of $L(k)'s$ is c.r.e.

COROLLARY B. The set of all partial recursive functions enumerating a given infinite set $\alpha$ is not r.e.

For take the A of Theorem 4 as the unit class $I(\alpha)$ .

THEOREM 5. The unit class $I(o)$ of the empty set is not c.r.e.

Proof. We assume the contrary, and note that since $F - I(o) = \sum_{\text{all } k} L(k)$ is c.r.e. by Theorem 3, $\theta_{I(o)}$ is a recursive set, so there exists a recursive function $\Phi(t, x)$ such that $\Phi(t, n) = 1$ whenever $\Phi(n, x)$ enumerates the empty set (i.e., produces no values), and $\Phi(t, n) = 0$ otherwise.

Now consider an arbitrary partial recursive function $\Phi(m, x)$ .

$$
\Phi (m, x) = U (\mu y T (m, x, y))
$$

and there is a recursive function $r(m, x, y)$ which equals 1 when $T(m, x, y)$ holds, and 0 otherwise. We define

$$
f (y) = \mu z [ z + 1 = r (m, m, y) ].
$$

$f(y)$ is a partial recursive function, so there is an $r$ such that $f(y) = \Phi(r, y)$ . The Gödel enumeration of the partial recursive functions yields a recursive function $g(x)$ such that $r = g(m)$ .

Now whenever $\Phi(m, m)$ is undefined, $\Phi(r, y)$ enumerates $o$ , so that $\Phi(t, r) = 1$ , and if $\Phi(m, m)$ is defined, $\Phi(t, r) = 0$ .

Finally, there exists an integer $s$ such that

$$
\Phi (s, m) = \mu y [ y + 1 = \Phi (t, g (m)) ].
$$

$\Phi(s, m)$ is undefined whenever $\Phi(m, m)$ is defined, and is defined and equal to 0 whenever $\Phi(m, m)$ is undefined. A contradiction arises from the case of $\Phi(s, s)$ .

## III. COMPLETE RECURSIVENESS

6. The main theorem and the strong definition. We now give a theorem which shows that too many classes are not c.r.e. for any class to be c.r.

THEOREM 6. Let A be a class which contains a finite set $\{a_{0},\cdots,a_{k}\}$ , but omits a set $\alpha$ which includes $\{a_{0},\cdots,a_{k}\}$ . Then A is not c.r.e.

Proof. For any partial recursive function $\Phi(n, x)$ , we define

$$
f (n) = \mu z T (n, K (z), L (z)).
$$

$f(n)$ is undefined if $\Phi(n, x)$ enumerates $o$ , but assumes some value otherwise. Let $g(x)$ be defined by the equations

$$
\begin{array}{r l r} {g (0)} & & {= b _ {0},} \\ {g (1)} & & {= b _ {1},} \\ {\cdot \cdot \cdot} & & \end{array}
$$

$$
\begin{array}{l l} {g (k)} & {= b _ {k},} \\ {g (x + k + 1)} & {= 0} \end{array}
$$

and $h(x)$ by

$$
h (x) = 1 \div (1 \div (x \div k))
$$

where $a \div b = 0$ if $a < b$ , and $a - b$ otherwise. $h(x) = 0$ for $x \leq k$ , and 1 for $x > k$ . Finally, let $\Phi(t, x)$ be any partial recursive function. Now consider

$$
g (x) + 0 \cdot f (n \cdot h (x)) + \Phi (t \cdot h (x), x \div (k + 1)).
$$

When $b_0, \cdots, b_k$ and $t$ are chosen, this is a partial recursive function $\Phi(s, x)$ ,

and the Gödel enumeration gives $s(n)$ as a recursive function of $n$ .

If $A$ is the class of the theorem, we now take $b_{i} = a_{i}$ and $t = t_{0}$ , where $\Phi(t_{0}, x)$ enumerates $\alpha$ . We define $\bar{\theta}_{A}$ as the set of all $n$ 's such that $s(n) \in \theta_{A}$ . If $\theta_{A}$ is r.e., so is $\bar{\theta}_{A}$ . For suppose $\Phi(r, x)$ enumerates $\theta_{A}$ . Then $\bar{\theta}_{A}$ is the range of the partial recursive function

$$
K (x) + \mu y [ y + 1 = 1 \div | \Phi (r, L (x)) - s (K (x)) | ].
$$

The crux of the proof lies in the fact that $\bar{\theta}_A = \theta_{I(o)}$ . Suppose $\Phi(n, x)$ enumerates $o$ . Then for $x \leq k$ , $h(x) = 0$ and

$$
\Phi (s (n), x) = g (x) + 0 \cdot f (0) + \Phi (0, 0).
$$

In this range $\Phi(s(n), x)$ is defined (recall again that $\Phi(0, x)$ was taken as the identity function in I, 2) and equal to $g(x)$ . So the set enumerated by $\Phi(s(n), x)$ includes $\{a_0, \cdots, a_k\}$ . However, for $x > k$ ,

$$
\Phi (s (n), x) = 0 + 0 \cdot f (n) + \Phi (t _ {0}, x \div (k + 1))
$$

and $\Phi(s(n), x)$ is not defined, since $f(n)$ is not. So $\Phi(s(n), x)$ enumerates just the set $\{a_0, \cdots, a_k\}$ , which is in $A$ . $s(n) \in \theta_A$ and $n \in \bar{\theta}_A$ .

On the other hand, suppose $\Phi(n, x)$ does not enumerate $o$ . Then, for $x > k$ , $f(n)$ is defined, so that

$$
\Phi (s (n), x) = 0 + 0 + \Phi (t _ {0}, x \div (k + 1)).
$$

For $x = k + y$ , $\Phi(s(n), x) = \Phi(t_0, y)$ . So $\Phi(s(n), x)$ enumerates $\alpha$ , which is not in $A$ . $s(n) \in \theta_A$ and $n \in \overline{\theta}_A$ .

We have, then, that if $\theta_{A}$ is r.e., $\overline{\theta}_{A}=\theta_{I(o)}$ is r.e., which by Theorem 5 is not the case. So $\theta_{A}$ is not r.e., and A is not c.r.e.

COROLLARY A. Every c.r.e. class includes a $\sum \prod L$ class.

For by Theorem 4, a c.r.e. class A contains a finite set $\{a_{0},\cdots,a_{k}\}$ . By Theorem 6, A contains all sets $\alpha$ which include $\{a_{0},\cdots,a_{k}\}$ . That is, A includes $\prod_{i=0}^{i=k}L(a_{i})$ . (In fact, it can be shown $^{(4)}$ ) that the finite sets of A can be recursively enumerated, so that A includes the $\sum\prod L$ class generated by its finite sets.)

COROLLARY B. There are no nontrivial c.r. classes by the strong definition.

For every nontrivial c.r.e. class A must contain the set $\epsilon$ of all nonnegative integers, and it is impossible for both A and F-A to contain the same set $\epsilon$ .

COROLLARY C. No nontrivial c.r.e. class A contains o.

For o is included in every set, so A would have to be F.

## COROLLARY D. No unit class is c.r.e.

We have already that if $\alpha$ is infinite, $I(\alpha)$ is not c.r.e. (Theorem 4, Corollary A), and if $\alpha$ is empty, $I(\alpha)$ is not c.r.e. (Theorem 5). The result if $\alpha$ is finite follows from Theorem 6.

If we identify properties with classes, and “effective” with “recursive,” we can give an intuitive interpretation of Corollary B. If P is any property possessed by some, but not all, r.e. sets, then there exists no effective general method for deciding, given a set $\alpha$ by means of a partial recursive function enumerating it, whether or not $\alpha$ has the property P. In stronger terms, there exists no effective general method for obtaining, from a partial recursive function, any information about the set of which the function is a characterization! Of course there will exist special methods for particular functions.

This situation is not a result of admitting functions not always defined, for we now establish the same result for the weak definition.

## 7. The weak definition.

THEOREM 7. If a class A is c.r. by the weak definition, then $A - I(o)$ is c.r.e.

Proof. Under the hypothesis, there is a partial recursive function $\Phi(r, n)$ which is equal to 1 if $\Phi(n, x)$ is a general recursive function enumerating a set of A, and equal to 0 if $\Phi(n, x)$ is a general recursive function enumerating a set of F-A.

We must show that from an arbitrary partial recursive function $\Phi(n, x)$ enumerating a set $\alpha \neq o$ , we can construct a general recursive function $\Phi(m, x)$ , also enumerating $\alpha$ , in such a way that m is a recursive function of n.

We first define

$$
x _ {0} = K (\mu z T (n, K (z), L (z))).
$$

Since $\alpha \neq o$ , such a $z$ exists. Then

$\Phi (m,0) = \Phi (n,x_0);$

$\Phi(m, x) = \Phi(n, x_0)$ if $T(n, K(x), L(x))$ does not hold;

$$
\Phi (m, x) = \Phi (n, K (x)) \text {   if   } T (n, K (x), L (x)) \text {   holds. }
$$

$\Phi(m, x)$ is defined for all arguments, and a more formal definition in terms of the representing function $r(n, x, y)$ of $T(n, x, y)$ would establish that $\Phi(m, x)$ is recursive, and that the Gödel enumeration of the partial recursive functions would yield m as a recursive function of n. Say $f(n) = m$ .

To show that $A - I(o)$ is c.r.e., we note that $\theta_{A - I(o)}$ is the range of the partial recursive function

$$
g (n) + \mu y [ y + 1 = \Phi (r, f (g (n))) ]
$$

where $g(n)$ is a partial recursive function enumerating $\theta_{F - I(o)}$ .

COROLLARY. If A is c.r. by the weak definition, then $F-I(o)-A$ is c.r.e.

THEOREM 8. No nontrivial class is c.r. by the weak definition.

Proof. Suppose $A - I(o)$ is c.r.e. Then A contains $\epsilon$ , and so $F - I(o) - A$ does not contain $\epsilon$ . Thus $F - I(o) - A$ is not c.r.e., and by the corollary to Theorem 7, A is not c.r. by the weak definition.

We find, then, that the same unfortunate situation exists whether we agree to characterize sets by partial recursive functions, or whether we restrict characterization to the better-behaved general recursive functions. Nor does further restriction to the primitive recursive functions bring any improvement, for Rosser [8] has shown that from a given general recursive function we can effectively construct a primitive recursive function enumerating the same set. Arguments paralleling the proofs of Theorem 7 and 8 will then give the analogue of Theorem 8 for the primitive recursive functions.

## BIBLIOGRAPHY

1. Alonzo Church, An unsolvable problem of elementary number theory, Amer. J. Math. vol. 58 (1936) pp. 345–363.

2. Kurt Gödel, Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I, Monatshefte für Mathematik und Physik vol. 38 (1931) pp. 173–198.

3. S. C. Kleene, General recursive functions of natural numbers, Math. Ann. vol. 112 (1936) pp. 727–766.

4. ——, On notation for ordinal numbers, J. Symbolic Logic vol. 3 (1938) pp. 150–155.

5. ——, Recursive predicates and quantifiers, Trans. Amer. Math. Soc. vol. 53 (1943) pp. 41–73.

6. A. Mostowski, On definable sets of positive integers, Fund. Math. vol. 34 (1946) pp. 81-112.

7. E. L. Post, Recursively enumerable sets of positive integers and their decision problems, Bull. Amer. Math. Soc. vol. 50 (1944) pp. 284–316.

8. J. B. Rosser, Extensions of some theorems of Gödel and Church, J. Symbolic Logic vol. 1 (1936) pp. 87–91.