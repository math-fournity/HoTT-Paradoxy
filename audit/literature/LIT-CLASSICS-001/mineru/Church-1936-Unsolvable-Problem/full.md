An Unsolvable Problem of Elementary Number Theory
Author(s): Alonzo Church
Source: American Journal of Mathematics, Vol. 58, No. 2 (Apr., 1936), pp. 345-363
Published by: The Johns Hopkins University Press
Stable URL: https://www.jstor.org/stable/2371045
Accessed: 18-08-2025 15:44 UTC

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at https://about.jstor.org/terms

The Johns Hopkins University Press is collaborating with JSTOR to digitize, preserve and extend access to American Journal of Mathematics

# AN UNSOLVABLE PROBLEM OF ELEMENTARY NUMBER THEORY. $^{1}$

By Alonzo Church.

1. Introduction. There is a class of problems of elementary number theory which can be stated in the form that it is required to find an effectively calculable function $f$ of $n$ positive integers, such that $f(x_1, x_2, \cdots, x_n) = 2^2$ is a necessary and sufficient condition for the truth of a certain proposition of elementary number theory involving $x_1, x_2, \cdots, x_n$ as free variables.

An example of such a problem is the problem to find a means of determining of any given positive integer n whether or not there exist positive integers x, y, z, such that $x^{n} + y^{n} = z^{n}$ . For this may be interpreted, required to find an effectively calculable function f, such that $f(n)$ is equal to 2 if and only if there exist positive integers x, y, z, such that $x^{n} + y^{n} = z^{n}$ . Clearly the condition that the function f be effectively calculable is an essential part of the problem, since without it the problem becomes trivial.

Another example of a problem of this class is, for instance, the problem of topology, to find a complete set of effectively calculable invariants of closed three-dimensional simplicial manifolds under homeomorphisms. This problem can be interpreted as a problem of elementary number theory in view of the fact that topological complexes are representable by matrices of incidence. In fact, as is well known, the property of a set of incidence matrices that it represent a closed three-dimensional manifold, and the property of two sets of incidence matrices that they represent homeomorphic complexes, can both be described in purely number-theoretic terms. If we enumerate, in a straightforward way, the sets of incidence matrices which represent closed three-dimensional manifolds, it will then be immediately provable that the problem under consideration (to find a complete set of effectively calculable invariants of closed three-dimensional manifolds) is equivalent to the problem, to find an effectively calculable function f of positive integers, such that $f(m,n)$ is equal to 2 if and only if the m-th set of incidence matrices and the n-th set of incidence matrices in the enumeration represent homeomorphic complexes.

Other examples will readily occur to the reader.

The purpose of the present paper is to propose a definition of effective calculability $^{3}$ which is thought to correspond satisfactorily to the somewhat vague intuitive notion in terms of which problems of this class are often stated, and to show, by means of an example, that not every problem of this class is solvable.

2. Conversion and $\lambda$ -definability. We select a particular list of symbols, consisting of the symbols $\{,\},(\,),\lambda,[,]$ , and an enumerably infinite set of symbols a, b, c, $\cdots$ to be called variables. And we define the word formula to mean any finite sequence of symbols out of this list. The terms well-formed formula, free variable, and bound variable are then defined by induction as follows. A variable x standing alone is a well-formed formula and the occurrence of x in it is an occurrence of x as a free variable in it; if the formulas F and X are well-formed, $\{\mathbf{F}\}(\mathbf{X})$ is well-formed, and an occurrence of x as a free (bound) variable in F or X is an occurrence of x as a free (bound) variable in $\{\mathbf{F}\}(\mathbf{X})$ ; if the formula M is well-formed and contains an occurrence of x as a free variable in M, then $\lambda x[M]$ is well-formed, any occurrence of x in $\lambda x[M]$ is an occurrence of x as a bound variable in $\lambda x[M]$ , and an occurrence of a variable y, other than x, as a free (bound) variable in M is an occurrence of y as a free (bound) variable in $\lambda x[M]$ .

We shall use heavy type letters to stand for variable or undetermined formulas. And we adopt the convention that, unless otherwise stated, each heavy type letter shall represent a well-formed formula and each set of symbols standing apart which contains a heavy type letter shall represent a well-formed formula.

When writing particular well-formed formulas, we adopt the following abbreviations. A formula $\{\boldsymbol{F}\}(\boldsymbol{X})$ may be abbreviated as $\boldsymbol{F}(\boldsymbol{X})$ in any case where F is or is represented by a single symbol. A formula $\{\{\boldsymbol{F}\}(\boldsymbol{X})\}(\boldsymbol{Y})$ may be abbreviated as $\{\boldsymbol{F}\}(\boldsymbol{X},\boldsymbol{Y})$ , or, if F is or is represented by a single symbol, as $\boldsymbol{F}(\boldsymbol{X},\boldsymbol{Y})$ . And $\{\{\{\boldsymbol{F}\}(\boldsymbol{X})\}(\boldsymbol{Y})\}(\boldsymbol{Z})$ may be abbreviated as $\{\boldsymbol{F}\}(\boldsymbol{X},\boldsymbol{Y},\boldsymbol{Z})$ , or as $\boldsymbol{F}(\boldsymbol{X},\boldsymbol{Y},\boldsymbol{Z})$ , and so on. A formula $\lambda x_{1}[\lambda x_{2}[\cdots\lambda x_{n}[\boldsymbol{M}]\cdots]]$ may be abbreviated as $\lambda x_{1}x_{2}\cdots\dot{x}_{n}\cdot M$ or as $\lambda x_{1}x_{2}\cdots\dot{x}_{n}M$ .

We also allow ourselves at any time to introduce abbreviations of the form that a particular symbol $\alpha$ shall stand for a particular sequence of symbols A, and indicate the introduction of such an abbreviation by the notation $\alpha \rightarrow A$ , to be read, “ $\alpha$ stands for A.”

We introduce at once the following infinite list of abbreviations,

$$
\begin{array}{r l}&1 \rightarrow \lambda a b \cdot a (b),\\&2 \rightarrow \lambda a b \cdot a (a (b)),\\&3 \rightarrow \lambda a b \cdot a (a (a (b))),\end{array}
$$

and so on, each positive integer in Arabic notation standing for a formula of the form $\lambda ab\cdot a(a(\cdot\cdot\cdot a(b)\cdot\cdot\cdot))$ .

The expression $S_{N}^{x}M$ | is used to stand for the result of substituting N for x throughout M.

We consider the three following operations on well-formed formulas:

I. To replace any part $\lambda x[M]$ of a formula by $\lambda y[S_{y}^{x}M|]$ , where y is a variable which does not occur in M.

II. To replace any part $\{\lambda x[M]\}(N)$ of a formula by $S_{N}^{x}M|$ , provided that the bound variables in M are distinct both from x and from the free variables in N.

III. To replace any part $S_{N}^{x}M$ | (not immediately following $\lambda$ ) of a formula by $\{\lambda x[M]\}(N)$ , provided that the bound variables in M are distinct both from x and from the free variables in N.

Any finite sequence of these operations is called a conversion, and if B is obtainable from A by a conversion we say that A is convertible into B, or, “A conv B.” If B is identical with A or is obtainable from A by a single application of one of the operations I, II, III, we say that A is immediately convertible into B.

A conversion which contains exactly one application of Operation II, and no application of Operation III, is called a reduction.

A formula is said to be in normal form if it is well-formed and contains no part of the form $\{\lambda x[M]\}(N)$ . And B is said to be a normal form of A if B is in normal form and A conv B.

The originally given order a, b, c, $\cdots$ of the variables is called their natural order. And a formula is said to be in principal normal form if it is in normal form, and no variable occurs in it both as a free variable and as a bound variable, and the variables which occur in it immediately following the symbol $\lambda$ are, when taken in the order in which they occur in the formula, in natural order without repetitions, beginning with a and omitting only such variables as occur in the formula as free variables. $^{4}$ The formula B is said to be the principal normal form of A if B is in principal normal form and A conv B.

Of the three following theorems, proof of the first is immediate, and the second and third have been proved by the present author and J. B. Rosser: $^{5}$

THEOREM I. If a formula is in normal form, no reduction of it is possible.

THEOREM II. If a formula has a normal form, this normal form is unique to within applications of Operation I, and any sequence of reductions of the formula must (if continued) terminate in the normal form.

THEOREM III. If a formula has a normal form, every well-formed part of it has a normal form.

We shall call a function of positive integers if the range of each independent variable is the class of positive integers and the range of the dependent variable is contained in the class of positive integers. And when it is desired to indicate the number of independent variables we shall speak of a function of one positive integer, a function of two positive integers, and so on. Thus if F is a function of n positive integers, and $a_{1}, a_{2}, \cdots, a_{n}$ are positive integers, then $F(a_{1}, a_{2}, \cdots, a_{n})$ must be a positive integer.

A function F of one positive integer is said to be $\lambda$ -definable if it is possible to find a formula F such that, if $F(m) = r$ and m and r are the formulas for which the positive integers m and r (written in Arabic notation) stand according to our abbreviations introduced above, then $\{F\}(m)$ conv r.

Similarly, a function F of two positive integers is said to be $\lambda$ -definable if it is possible to find a formula F such that, whenever $F(m,n)=r$ , the formula $\{F\}(m,n)$ is convertible into r (m,n,r being positive integers and m,n,r the corresponding formulas). And so on for functions of three or more positive integers. $^{6}$

It is clear that, in the case of any $\lambda$ -definable function of positive integers, the process of reduction of formulas to normal form provides an algorithm for the effective calculation of particular values of the function.

3. The Gödel representation of a formula. Adapting to the formal notation just described a device which is due to Gödel, $^{7}$ we associate with every formula a positive integer to represent it, as follows. To each of the symbols {, (, [ we let correspond the number 11, to each of the symbols }, ), ] the number 13, to the symbol $\lambda$ the number 1, and to the variables $a, b, c, \cdots$ the prime numbers 17, 19, 23, $\cdots$ respectively. And with a formula which is composed of the n symbols $\tau_{1}, \tau_{2}, \cdots, \tau_{n}$ in order we associate the number $2^{t_{1}}3^{t_{2}} \cdots p_{n}^{t_{n}}$ , where $t_{i}$ is the number corresponding to the symbol $\tau_{i}$ , and where $p_{n}$ stands for the n-th prime number.

This number $2^{t_{1}}3^{t_{2}}\cdots p_{n}^{t_{n}}$ will be called the Gödel representation of the formula $\tau_{1}\tau_{2}\cdots\tau_{n}$ .

Two distinct formulas may sometimes have the same Gödel representation, because the numbers 11 and 13 each correspond to three different symbols, but it is readily proved that no two distinct well-formed formulas can have the same Gödel representation. It is clear, moreover, that there is an effective method by which, given any formula, its Gödel representation can be calculated; and likewise that there is an effective method by which, given any positive integer, it is possible to determine whether it is the Gödel representation of a well-formed formula and, if it is, to obtain that formula.

In this connection the Gödel representation plays a rôle similar to that of the matrix of incidence in combinatorial topology (cf. §1 above). For there is, in the theory of well-formed formulas, an important class of problems, each of which is equivalent to a problem of elementary number theory obtainable by means of the Gödel representation. $^{8}$

4. Recursive functions. We define a class of expressions, which we shall call elementary expressions, and which involve, besides parentheses and commas, the symbols 1, S, an infinite set of numerical variables x, y, z, $\cdots$ , and, for each positive integer n, an infinite set $f_{n}$ , $g_{n}$ , $h_{n}$ , $\cdots$ of functional variables with subscript n. This definition is by induction as follows. The symbol 1 or any numerical variable, standing alone, is an elementary expression. If A is an elementary expression, then $S(A)$ is an elementary expression. If $A_{1}, A_{2}, \cdots, A_{n}$ are elementary expressions and $f_{n}$ is any functional variable with subscript n, then $f_{n}(A_{1}, A_{2}, \cdots, A_{n})$ is an elementary expression.

The particular elementary expressions 1, $S(1)$ , $S(S(1))$ , $\cdots$ are called numerals. And the positive integers 1, 2, 3, $\cdots$ are said to correspond to the numerals 1, $S(1)$ , $S(S(1))$ , $\cdots$ .

An expression of the form A = B, where A and B are elementary expressions, is called an elementary equation.

The derived equations of a set E of elementary equations are defined by induction as follows. The equations of E themselves are derived equations. If A = B is a derived equation containing a numerical variable x, then the result of substituting a particular numeral for all the occurrences of x in A = B is a derived equation. If A = B is a derived equation containing an elementary expression C (as part of either A or B), and if either C = D or D = C is a derived equation, then the result of substituting D for a particular occurrence of C in A = B is a derived equation.

Suppose that no derived equation of a certain finite set E of elementary equations has the form k=l where k and l are different numerals, that the functional variables which occur in E are $f_{n_{1}}^{1}, f_{n_{2}}^{2}, \cdots, f_{n_{r}}^{r}$ with subscripts $n_{1}, n_{2}, \cdots, n_{r}$ respectively, and that, for every value of i from 1 to r inclusive, and for every set of numerals $k_{1}^{i}, k_{2}^{i}, \cdots, k_{n_{i}}^{i}$ , there exists a unique numeral $k^{i}$ such that $f_{n_{i}}^{i}(k_{1}^{i}, k_{2}^{i}, \cdots, k_{n_{i}}^{i}) = k^{i}$ is a derived equation of E. And let $F^{1}, F^{2}, \cdots, F^{r}$ be the functions of positive integers defined by the condition that, in all cases, $F^{i}(m_{1}^{i}, m_{2}^{i}, \cdots, m_{n_{i}}^{i})$ shall be equal to $m^{i}$ , where $m_{1}^{i}, m_{2}^{i}, \cdots, m_{n_{i}}^{i}$ , and $m^{i}$ are the positive integers which correspond to the numerals $k_{1}^{i}, k_{2}^{i}, \cdots, k_{n_{i}}^{i}$ , and $k^{i}$ respectively. Then the set of equations E is said to define, or to be a set of recursion equations for, any one of the functions $F^{i}$ , and the functional variable $f_{n_{i}}^{i}$ is said to denote the function $F^{i}$ .

A function of positive integers for which a set of recursion equations can be given is said to be recursive. $^{9}$

It is clear that for any recursive function of positive integers there exists an algorithm using which any required particular value of the function can be effectively calculated. For the derived equations of the set of recursion equations E are effectively enumerable, and the algorithm for the calculation of particular values of a function $F^{i}$ , denoted by a functional variable $f_{n_{i}}^{i}$ , consists in carrying out the enumeration of the derived equations of E until the required particular equation of the form $f_{n_{i}}^{i}(k_{1}^{i}, k_{2}^{i}, \cdots, k_{n_{i}}^{i}) = k^{i}$ is found. $^{10}$

We call an infinite sequence of positive integers recursive if the function $F$ such that $F(n)$ is the $n$ -th term of the sequence is recursive.

We call a propositional function of positive integers recursive if the function whose value is 2 or 1, according to whether the propositional function is true or false, is recursive. By a recursive property of positive integers we shall mean a recursive propositional function of one positive integer, and by a recursive relation between positive integers we shall mean a recursive propositional function of two or more positive integers.

A function F, for which the range of the dependent variable is contained in the class of positive integers and the range of the independent variable, or of each independent variable, is a subset (not necessarily the whole) of the class of positive integers, will be called potentially recursive, if it is possible to find a recursive function $F'$ of positive integers (for which the range of the independent variable, or of each independent variable, is the whole of the class of positive integers), such that the value of $F'$ agrees with the value of F in all cases where the latter is defined.

By an operation on well-formed formulas we shall mean a function for which the range of the dependent variable is contained in the class of well-formed formulas and the range of the independent variable, or of each independent variable, is the whole class of well-formed formulas. And we call such an operation recursive if the corresponding function obtained by replacing all formulas by their Gödel representations is potentially recursive.

Similarly any function for which the range of the dependent variable is contained either in the class of positive integers or in the class of well-formed formulas, and for which the range of each independent variable is identical either with the class of positive integers or with the class of well-formed formulas (allowing the case that some of the ranges are identical with one class and some with the other), will be said to be recursive if the corresponding function obtained by replacing all formulas by their Gödel representations is potentially recursive. We call an infinite sequence of well-formed formulas recursive if the corresponding infinite sequence of Gödel representations is recursive. And we call a property of, or relation between, well-formed formulas recursive if the corresponding property of, or relation between, their Gödel representations is potentially recursive. A set of well-formed formulas is said to be recursively enumerable if there exists a recursive infinite sequence which consists entirely of formulas of the set and contains every formula of the set at least once. $^{11}$

In terms of the notion of recursiveness we may also define a proposition of elementary number theory, by induction as follows. If $\phi$ is a recursive propositional function of n positive integers (defined by giving a particular set of recursion equations for the corresponding function whose values are 2 and 1) and if $x_{1}, x_{2}, \cdots, x_{n}$ are variables which take on positive integers as values, then $\phi(x_{1}, x_{2}, \cdots, x_{n})$ is a proposition of elementary number theory. If P is a proposition of elementary number theory involving x as a free variable, then the result of substituting a particular positive integer for all occurrences of x as a free variable in P is a proposition of elementary number theory, and $(x)P$ and $(\exists x)P$ are propositions of elementary number theory, where $(x)$ and $(\exists x)$ are respectively the universal and existential quantifiers of x over the class of positive integers.

It is then readily seen that the negation of a proposition of elementary number theory or the logical product or the logical sum of two propositions of elementary number theory is equivalent, in a simple way, to another proposition of elementary number theory.

5. Recursiveness of the Kleene p-function. We prove two theorems which establish the recursiveness of certain functions which are definable in words by means of the phrase, “The least positive integer such that,” or, “The n-th positive integer such that.”

THEOREM IV. If F is a recursive function of two positive integers, and if for every positive integer x there exists a positive integer y such that $F(x,y) > 1$ , then the function $F^{*}$ , such that, for every positive integer x, $F^{*}(x)$ is equal to the least positive integer y for which $F(x,y) > 1$ , is recursive.

For a set of recursion equations for $F^{*}$ consists of the recursion equations for F together with the equations,

$$
i _ {2} (1, 2) = 2,
$$

$$
g _ {2} (x, 1) = i _ {2} \left(f _ {2} (x, 1), 2\right),
$$

$$
i _ {2} (S (x), 2) = 1,
$$

$$
g _ {2} (x, S (y)) = i _ {2} \left(f _ {2} (x, S (y)), g _ {2} (x, y)\right),
$$

$$
i _ {2} (x, 1) = ^ {\prime} 3,
$$

$$
h _ {2} (S (x), y) = x,
$$

$$
i _ {2} (x, S (S (y))) = 3,
$$

$$
h _ {2} (g _ {2} (x, y), x) = j _ {2} (g _ {2} (x, y), y),
$$

$$
j _ {2} (1, y) = y,
$$

$$
f _ {1} (x) = h _ {2} (1, x),
$$

$$
j _ {2} (S (x), y) = x,
$$

where the functional variables $f_{2}$ and $f_{1}$ denote the functions F and $F^{*}$ respectively, and 2 and 3 are abbreviations for $S(1)$ and $S(S(1))$ respectively. $^{12}$

THEOREM V. If F is a recursive function of one positive integer, and if there exist an infinite number of positive integers x for which $F(x) > 1$ , then the function $F^{0}$ , such that, for every positive integer n, $F^{0}(n)$ is equal to the n-th positive integer x (in order of increasing magnitude) for which $F(x) > 1$ , is recursive.

For a set of recursion equations for $F^{0}$ consists of the recursion equations for F together with the equations,

$$
\begin{array}{l} g _ {2} (1, y) = g _ {2} (f _ {1} (S (y)), S (y)), \\ g _ {2} (S (x), y) = y, \\ g _ {1} (1) = k, \\ g _ {1} (S (y)) = g _ {2} (1, g _ {1} (y)), \end{array}
$$

where the functional variables $g_{1}$ and $f_{1}$ denote the functions $F^{0}$ and F respectively, and where k is the numeral to which corresponds the least positive integer x for which $F(x) > 1.^{13}$

6. Recursiveness of certain functions of formulas. We list now a number of theorems which will be proved in detail in a forthcoming paper by S. C. Kleene $^{14}$ or follow immediately from considerations there given. We omit proofs here, except for brief indications in some instances.

Our statement of the theorems and our notation differ from Kleene's in that we employ the set of positive integers $(1,2,3,\cdots)$ in the rôle in which he employs the set of natural numbers $(0,1,2,\cdots)$ . This difference is, of course, unessential. We have selected what is, from some points of view, the less natural alternative, in order to preserve the convenience and naturalness of the identification of the formula $\lambda ab\cdot a(b)$ with 1 rather than with 0.

THEOREM VI. The property of a positive integer, that there exists a well-formed formula of which it is the Gödel representation is recursive.

THEOREM VII. The set of well-formed formulas is recursively enumerable.

This follows from Theorems V and VI.

THEOREM VIII. The function of two variables, whose value, when taken of the well-formed formulas $\mathbf{F}$ and $\mathbf{X}$ , is the formula $\{\mathbf{F}\}(\mathbf{X})$ , is recursive.

THEOREM IX. The function, whose value for each of the positive integers $1, 2, 3, \cdots$ is the corresponding formula $1, 2, 3, \cdots$ , is recursive.

THEOREM X. A function, whose value for each of the formulas 1, 2, 3, $\cdots$ is the corresponding positive integer, and whose value for other well-formed formulas is a fixed positive integer, is recursive. Likewise the function, whose value for each of the formulas 1, 2, 3, $\cdots$ is the corresponding positive integer plus one, and whose value for other well-formed formulas is the positive integer 1, is recursive.

THEOREM XI. The relation of immediate convertibility, between well-formed formulas, is recursive.

THEOREM XII. It is possible to associate simultaneously with every well-formed formula an enumeration of the formulas obtainable from it by conversion, in such a way that the function of two variables, whose value, when taken of a well-formed formula A and a positive integer n, is the n-th formula in the enumeration of the formulas obtainable from A by conversion, is recursive.

THEOREM XIII. The property of a well-formed formula, that it is in principal normal form, is recursive.

THEOREM XIV. The set of well-formed formulas which are in principal normal form is recursively enumerable.

This follows from Theorems V, VII, XIII.

THEOREM XV. The set of well-formed formulas which have a normal form is recursively enumerable. $^{15}$

For by Theorems XII and XIV this set can be arranged in an infinite square array which is recursively defined (i.e. defined by a recursive function of two variables). And the familiar process by which this square array is reduced to a single infinite sequence is recursive (i.e. can be expressed by means of recursive functions).

THEOREM XVI. Every recursive function of positive integers is $\lambda$ -definable. $^{16}$

THEOREM XVII. Every $\lambda$ -definable function of positive integers is recursive. $^{17}$

For functions of one positive integer this follows from Theorems IX, VIII, XII, XIII, IV, X. For functions of more than one positive integer it follows by the same method, using a generalization of Theorem IV to functions of more than two positive integers.

7. The notion of effective calculability. We now define the notion, already discussed, of an effectively calculable function of positive integers by identifying it with the notion of a recursive function of positive integers $^{18}$ (or of a $\lambda$ -definable function of positive integers). This definition is thought to be justified by the considerations which follow, so far as positive justification can ever be obtained for the selection of a formal definition to correspond to an intuitive notion.

It has already been pointed out that, for every function of positive integers which is effectively calculable in the sense just defined, there exists an algorithm for the calculation of its values.

Conversely it is true, under the same definition of effective calculability, that every function, an algorithm for the calculation of the values of which exists, is effectively calculable. For example, in the case of a function F of one positive integer, an algorithm consists in a method by which, given any positive integer n, a sequence of expressions (in some notation) $E_{n1}, E_{n2}, \cdots, E_{nr_n}$ , can be obtained; where $E_{n1}$ is effectively calculable when n is given; where $E_{ni}$ is effectively calculable when n and the expressions $E_{nj}, j < i$ , are given; and where, when n and all the expressions $E_{ni}$ up to and including $E_{nr_n}$ are given, the fact that the algorithm has terminated becomes effectively known and the value of $F(n)$ is effectively calculable. Suppose that we set up a system of Gödel representations for the notation employed in the expressions $E_{ni}$ , and that we then further adopt the method of Gödel of representing a finite sequence of expressions $E_{n1}, E_{n2}, \cdots, E_{ni}$ by the single positive integer $2^{en_1}3^{en_2} \cdots p_i^{en_i}$ where $e_{n1}, e_{n2}, \cdots, e_{ni}$ are respectively the Gödel representations of $E_{n1}, E_{n2}, \cdots, E_{ni}$ (in particular representing a vacuous sequence of expressions by the positive integer 1). Then we may define a function G of two positive integers such that, if x represents the finite sequence $E_{n1}, E_{n2}, \cdots, E_{nk}$ , then $G(n, x)$ is equal to the Gödel representation of $E_{ni}$ , where $i = k + 1$ , or is equal to 10 if $k = r_n$ (that is if the algorithm has terminated with $E_{nk}$ ), and in any other case $G(n, x)$ is equal to 1. And we may define a function H of two positive integers, such that the value of $H(n, x)$ is the same as that of $G(n, x)$ , except in the case that $G(n, x) = 10$ , in which case $H(n, x) = F(n)$ . If the interpretation is allowed that the requirement of effective calculability which appears in our description of an algorithm means the effective calculability of the functions G and $H,^{19}$ and if we take the effective calculability of G and H to mean recursiveness ( $\lambda$ -definability), then the recursiveness ( $\lambda$ -definability) of F follows by a straightforward argument.

Suppose that we are dealing with some particular system of symbolic logic, which contains a symbol, =, for equality of positive integers, a symbol { }() for the application of a function of one positive integer to its argument, and expressions 1, 2, 3, · · · to stand for the positive integers. The theorems of the system consist of a finite, or enumerably infinite, list of expressions, the formal axioms, together with all the expressions obtainable from them by a finite succession of applications of operations chosen out of a given finite, or enumerably infinite, list of operations, the rules of procedure. If the system is to serve at all the purposes for which a system of symbolic logic is usually intended, it is necessary that each rule of procedure be an effectively calculable operation, that the complete set of rules of procedure (if infinite) be effectively enumerable, that the complete set of formal axioms (if infinite) be effectively enumerable, and that the relation between a positive integer and the expression which stands for it be effectively determinable. Suppose that we interpret this to mean that, in terms of a system of Gödel representations for the expressions of the logic, each rule of procedure must be a recursive operation, $^{20}$ the complete set of rules of procedure must be recursively enumerable (in the sense that there exists a recursive function $\Phi$ such that $\Phi(n, x)$ is the representation of the result of applying the $n$ -th rule of procedure to the ordered finite set of formulas represented by $x$ ), the complete set of formal axioms must be recursively enumerable, and the relation between a positive integer and the expression which stands for it must be recursive. $^{21}$ And let us call a function $F$ of one positive integer $^{22}$ calculable within the logic if there exists an expression $f$ in the logic such that $\{f\}(\mu) = \nu$ is a theorem when and only when $F(m) = n$ is true, $\mu$ and $\nu$ being the expressions which stand for the positive integers $m$ and $n$ . Then, since the complete set of theorems of the logic is recursively enumerable, it follows by Theorem IV above that every function of one positive integer which is calculable within the logic is also effectively calculable (in the sense of our definition).

Thus it is shown that no more general definition of effective calculability than that proposed above can be obtained by either of two methods which naturally suggest themselves (1) by defining a function to be effectively calculable if there exists an algorithm for the calculation of its values (2) by defining a function $F$ (of one positive integer) to be effectively calculable if, for every positive integer $m$ , there exists a positive integer $n$ such that $F(m) = n$ is a provable theorem.

8. Invariants of conversion. The problem naturally suggests itself to find invariants of that transformation of formulas which we have called conversion. The only effectively calculable invariants at present known are the immediately obvious ones (e.g. the set of free variables contained in a formula). Others of importance very probably exist. But we shall prove (in Theorem XIX) that, under the definition of effective calculability proposed in §7, no complete set of effectively calculable invariants of conversion exists (cf. §1).

The results of Kleene (American Journal of Mathematics, 1935) make it clear that, if the problem of finding a complete set of effectively calculable invariants of conversion were solved, most of the familiar unsolved problems of elementary number theory would thereby also be solved. And from Theorem XVI above it follows further that to find a complete set of effectively calculable invariants of conversion would imply the solution of the Entscheidungsproblem for any system of symbolic logic whatever (subject to the very general restrictions of §7). In the light of this it is hardly surprising that the problem to find such a set of invariants should be unsolvable.

It is to be remembered, however, that, if we consider only the statement of the problem (and ignore things which can be proved about it by more or less lengthy arguments), it appears to be a problem of the same class as the problems of number theory and topology to which it was compared in § 1, having no striking characteristic by which it can be distinguished from them. The temptation is strong to reason by analogy that other important problems of this class may also be unsolvable.

LEMMA. The problem, to find a recursive function of two formulas A and B whose value is 2 or 1 according as A conv B or not, is equivalent to the problem, to find a recursive function of one formula C whose value is 2 or 1 according as C has a normal form or not. $^{23}$

For, by Theorem X, the formula a (the formula b), which stands for the positive integer which is the Gödel representation of the formula A (the formula B), can be expressed as a recursive function of the formula A (the formula B). Moreover, by Theorems VI and XII, there exists a recursive function F of two positive integers such that, if m is the Gödel representation of a well-formed formula M, then $F(m,n)$ is the Gödel representation of the n-th formula in an enumeration of the formulas obtainable from M by conversion. And, by Theorem XVI, F is $\lambda$ -definable, by a formula f. If we define,

$$
\begin{array}{l} Z _ {1} \to \mathcal {Q} (\lambda x \cdot x (I), I), \\ Z _ {2} \to \mathcal {Q} (\lambda x y \cdot S (x) - y, I), \end{array}
$$

where $\mathcal{Q}$ is the formula defined by Kleene (American Journal of Mathematics, vol. 57 (1935), p. 226), then $Z_{1}$ and $Z_{2}$ $\lambda$ -define the functions of one positive integer whose values, for a positive integer $n$ , are the $n$ -th terms respectively of the infinite sequences $1, 1, 2, 1, 2, 3, \cdots$ and $1, 2, 1, 3, 2, 1, \cdots$ . By Theorem VIII the formula,

$$
\{\lambda x y \cdot \mathfrak {p} (\lambda n \cdot \delta (\mathfrak {f} (x, Z _ {1} (n)), \mathfrak {f} (y, Z _ {2} (n))), 1) \} (\boldsymbol {a}, \boldsymbol {b}),
$$

where p and $\delta$ are defined as by Kleene (loc. cit., p. 173 and p. 231), is a recursive function of A and B, and this formula has a normal form if and only if A conv B.

Again, by Theorem X, the formula c, which stands for the positive integer which is the Gödel representation of the formula C, can be expressed as a recursive function of the formula C. By Theorems VI and XIII, there exists a recursive function G of one positive integer such that $G(m)=2$ if m is the Gödel representation of a formula in principal normal form, and $G(m)=1$ in any other case. And, by Theorem XVI, G is $\lambda$ -definable, by a formula g. By Theorem VIII the formula,

$$
\{\lambda x \cdot \mathfrak {p} (\lambda n \cdot \mathfrak {g} (\mathfrak {f} (x, n), 1, 1)) \} (\boldsymbol {c})
$$

where f is the formula f used in the preceding paragraph, is a recursive function of C, and this formula is convertible into the formula 1 if and only if C has a normal form.

Thus we have proved that a formula C can be found as a recursive function of formulas A and B, such that C has a normal form if and only if A conv B; and that a formula A can be found as a recursive function of a formula C, such that A conv 1 if and only if C has a normal form. From this the lemma follows.

THEOREM XVIII. There is no recursive function of a formula C, whose value is 2 or 1 according as C has a normal form or not.

That is, the property of a well-formed formula, that it has a normal form, is not recursive.

For assume the contrary.

Then there exists a recursive function H of one positive integer such that $H(m)=2$ if m is the Gödel representation of a formula which has a normal form, and $H(m)=1$ in any other case. And, by Theorem XVI, H is $\lambda$ -definable by a formula h.

By Theorem XV, there exists an enumeration of the well-formed formulas which have a normal form, and a recursive function A of one positive integer such that $A(n)$ is the Gödel representation of the n-th formula in this enumeration. And, by Theorem XVI, A is $\lambda$ -definable, by a formula a.

By Theorems VI and VIII, there exists a recursive function B of two positive integers such that, if m and n are Gödel representations of well-formed formulas M and N, then $B(m,n)$ is the Gödel representation of $\{M\}(N)$ . And, by Theorem XVI, B is $\lambda$ -definable, by a formula b.

By Theorems VI and X, there exists a recursive function C of one positive integer such that, if m is the Gödel representation of one of the formulas $1, 2, 3, \cdots$ , then $C(m)$ is the corresponding positive integer plus one, and in any other case $C(m) = 1$ . And, by Theorem XVI, C is $\lambda$ -definable, by a formula c.

By Theorem IX there exists a recursive function $Z^{-1}$ of one positive integer, whose value for each of the positive integers $1, 2, 3, \cdots$ is the Gödel representation of the corresponding formula $1, 2, 3, \cdots$ . And, by Theorem XVI, $Z^{-1}$ is $\lambda$ -definable, by a formula 3.

Let f and g be the formulas f and g used in the proof of the Lemma. By Kleene 15III Cor. (loc. cit., p. 220), a formula d can be found such that,

$\mathfrak{d}(1)$ conv $\lambda x\cdot x(1)$

$$
\mathfrak {d} (2) \text {   conv   } \lambda u \cdot \mathfrak {c} (\mathfrak {f} (u, \mathfrak {p} (\lambda m \cdot \mathfrak {g} (\mathfrak {f} (u, m)), 1))).
$$

We define,

$$
\mathfrak {e} \rightarrow \lambda n \cdot \mathfrak {d} (\mathfrak {h} (\mathfrak {b} (\mathfrak {a} (n), \mathfrak {z} (n))), \mathfrak {b} (\mathfrak {a} (n), \mathfrak {z} (n))).
$$

Then if n is one of the formulas 1, 2, 3, $\cdots$ , $\mathbf{c}(\mathbf{n})$ is convertible into one of the formulas 1, 2, 3, $\cdots$ in accordance with the following rules: (1) if $\mathbf{b}(\mathfrak{a}(\mathbf{n}),\mathfrak{z}(\mathbf{n}))$ conv a formula which stands for the Gödel representation of a formula which has no normal form, $\mathbf{e}(\mathbf{n})$ conv 1, (2) if $\mathbf{b}(\mathfrak{a}(\mathbf{n}),\mathfrak{z}(\mathbf{n}))$ conv a formula which stands for the Gödel representation of a formula which has a principal normal form which is not one of the formulas 1, 2, 3, $\cdots$ , $\mathbf{c}(\mathbf{n})$ conv 1, (3) if $\mathbf{b}(\mathfrak{a}(\mathbf{n}),\mathfrak{z}(\mathbf{n}))$ conv a formula which stands for the Gödel representation of a formula which has a principal normal form which is one of the formulas 1, 2, 3, $\cdots$ , $\mathbf{c}(\mathbf{n})$ conv the next following formula in the list 1, 2, 3, $\cdots$ .

By Theorem III, since $\mathfrak{e}(1)$ has a normal form, the formula $\mathfrak{e}$ has a normal form. Let $\mathfrak{G}$ be the formula which stands for the Gödel representation of $\mathfrak{e}$ . Then, if $n$ is any one of the formulas $1, 2, 3, \cdots$ , $\mathfrak{G}$ is not convertible into the formula $\mathfrak{a}(n)$ , because $\mathfrak{b}(\mathfrak{G}, \mathfrak{z}(n))$ is, by the definition of $\mathfrak{h}$ , convertible into the formula which stands for the Gödel representation of $\mathfrak{e}(n)$ , while $\mathfrak{b}(\mathfrak{a}(n), \mathfrak{z}(n))$ is, by the preceding paragraph, convertible into the formula stands for the Gödel representation of a formula definitely not convertible into $\mathfrak{e}(n)$ (Theorem II). But, by our definition of $\mathfrak{a}$ , it must be true of one of the formulas $n$ in the list $1, 2, 3, \cdots$ that $\mathfrak{a}(n)$ conv $\mathfrak{G}$ .

Thus, since our assumption to the contrary has led to a contradiction, the theorem must be true.

In order to present the essential ideas without any attempt at exact statement, the preceding proof may be outlined as follows. We are to deduce a contradiction from the assumption that it is effectively determinable of every well-formed formula whether or not it has a normal form. If this assumption holds, it is effectively determinable of every well-formed formula whether or not it is convertible into one of the formulas 1, 2, 3, · · · ; for, given a well-formed formula R, we can first determine whether or not it has a normal form, and if it has we can obtain the principal normal form by enumerating the formulas into which R is convertible (Theorem XII) and picking out the first formula in principal normal form which occurs in the enumeration, and we can then determine whether the principal normal form is one of the formulas 1, 2, 3, · · · . Let $A_{1}, A_{2}, A_{3}, \cdots$ be an effective enumeration of the well-formed formulas which have a normal form (Theorem XV). Let E be a function of one positive integer, defined by the rule that, where m and n are the formulas which stand for the positive integers m and n respectively, $E(n) = 1$ if $\{A_{n}\}(n)$ is not convertible into one of the formulas 1, 2, 3, · · · , and $E(n) = m + 1$ if $\{A_{n}\}(n)$ conv m and m is one of the formulas 1, 2, 3, · · · . The function E is effectively calculable and is therefore $\lambda$ -definable, by a formula e. The formula e has a normal form, since $\mathbf{e}(1)$ has a normal form. But e is not any one of the formulas $A_{1}, A_{2}, A_{3}, \cdots$ , because, for every n, $\mathbf{e}(\mathbf{n})$ is a formula which is not convertible into $\{\mathbf{A}_{n}\}(\mathbf{n})$ . And this contradicts the property of the enumeration $A_{1}, A_{2}, A_{3}, \cdots$ that it contains all well-formed formulas which have a normal form.

COROLLARY 1. The set of well-formed formulas which have no normal form is not recursively enumerable. $^{24}$

For, to outline the argument, the set of well-formed formulas which have a normal form is recursively enumerable, by Theorem XV. If the set of those which do not have a normal form were aslo recursively enumerable, it would be possible to tell effectively of any well-formed formula whether it had a normal form, by the process of searching through the two enumerations until it was found in one or the other. This, however, is contrary to Theorem XVIII.

This corollary gives us an example of an effectively enumerable set (the set of well-formed formulas) which is divided into two non-overlapping subsets of which one is effectively enumerable and the other not. Indeed, in view of the difficulty of attaching any reasonable meaning to the assertion that a set is enumerable but not effectively enumerable, it may even be permissible to go a step further and say that here is an example of an enumerable set which is divided into two non-overlapping subsets of which one is enumerable and the other non-enumerable. $^{25}$

COROLLARY 2. Let a function F of one positive integer be defined by the rule that $F(n)$ shall equal 2 or 1 according as n is or is not the Gödel representation of a formula which has a normal form. Then F (if its definition be admitted as valid at all) is an example of a non-recursive function of positive integers. $^{26}$

This follows at once from Theorem XVIII.

Consider the infinite sequence of positive integers, $F(1)$ , $F(2)$ , $F(3)$ , $\cdots$ . It is impossible to specify effectively a method by which, given any n, the n-th term of this sequence could be calculated. But it is also impossible ever to select a particular term of this sequence and prove about that term that its value cannot be calculated (because of the obvious theorem that if this sequence has terms whose values cannot be calculated then the value of each of those terms 1). Therefore it is natural to raise the question whether, in spite of the fact that there is no systematic method of effectively calculating the terms of this sequence, it might not be true of each term individually that there existed a method of calculating its value. To this question perhaps the best answer is that the question itself has no meaning, on the ground that the universal quantifier which it contains is intended to express a mere infinite succession of accidents rather than anything systematic.

There is in consequence some room for doubt whether the assertion that the function F exists can be given a reasonable meaning.

THEOREM XIX. There is no recursive function of two formulas A and B, whose value is 2 or 1 according as A conv B or not.

This follows at once from Theorem XVIII and the Lemma preceding it.

As a corollary of Theorem XIX, it follows that the Entscheidungsproblem is unsolvable in the case of any system of symbolic logic which is $\omega$ -consistent ( $\omega$ -widerspruchsfrei) in the sense of Gödel (loc. cit., p. 187) and is strong enough to allow certain comparatively simple methods of definition and proof. For in any such system the proposition will be expressible about two positive integers $a$ and $b$ that they are Gödel representations of formulas $A$ and $B$ such that $A$ is immediately convertible into $B$ . Hence, utilizing the fact that a conversion is a finite sequence of immediate conversions, the proposition $\Psi(a, b)$ will be expressible that $a$ and $b$ are Gödel representations of formulas $A$ and $B$ such that $A$ conv $B$ . Moreover if $A$ conv $B$ , and $a$ and $b$ are the Gödel representations of $A$ and $B$ respectively, the proposition $\Psi(a, b)$ will be provable in the system, by a proof which amounts to exhibiting, in terms of Gödel representations, a particular finite sequence of immediate conversions, leading from $A$ to $B$ ; and if $A$ is not convertible into $B$ , the $\omega$ -consistency of the system means that $\Psi(a, b)$ will not be provable. If the Entscheidungsproblem for the system were solved, there would be a means of determining effectively of every proposition $\Psi(a, b)$ whether it was provable, and hence a means of determining effectively of every pair of formulas $A$ and $B$ whether $A$ conv $B$ , contrary to Theorem XIX.

In particular, if the system of Principia Mathematica be $\omega$ -consistent, its Entscheidungsproblem is unsolvable.

PRINCETON UNIVERSITY,
PRINCETON, N. J.