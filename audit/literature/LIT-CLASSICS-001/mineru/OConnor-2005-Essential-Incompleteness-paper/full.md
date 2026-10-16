# Essential Incompleteness of Arithmetic Verified by Coq

Russell O’Connor

<sup>1</sup> Institute for Computing and Information Science

Faculty of Science

Radboud University Nijmegen

<sup>2</sup> The Group in Logic and the Methodology of Science

University of California, Berkeley

r.oconnor@cs.ru.nl <sup>⋆</sup> <sup>⋆</sup> <sup>⋆</sup>

Abstract. A constructive proof of the G¨odel-Rosser incompleteness theorem [9] has been completed using the Coq proof assistant. Some theory of classical first-order logic over an arbitrary language is formalized. A development of primitive recursive functions is given, and all primitive recursive functions are proved to be representable in a weak axiom system. Formulas and proofs are encoded as natural numbers, and functions operating on these codes are proved to be primitive recursive. The weak axiom system is proved to be essentially incomplete. In particular, Peano arithmetic is proved to be consistent in Coq’s type theory and therefore is incomplete.

## 0 License

This work is hereby released into the Public Domain. To view a copy of the public domain dedication, visit http://creativecommons.org/licenses/publicdomain/ or send a letter to Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.

## 1 Introduction

The G¨odel-Rosser incompleteness theorem for arithmetic states that any complete first-order theory of a nice axiom system, using only the symbols +, ×, 0, S, and < is inconsistent. A nice axiom system must contain the nine specific axioms of a system called NN. These nine axioms serve to define the previous symbols. A nice axiom system must also be expressible in itself. This last restriction prevents the incompleteness theorem from applying to axioms systems such as the true first order statements about N.

A computer verified proof of G¨odel’s incompleteness theorem is not new. In 1986 Shankar created a proof of the incompleteness of Z2, hereditarily finite set theory, in the Boyer-Moore theorem prover [11]. My work is the first computer verified proof of the essential incompleteness of arithmetic. Harrison recently completed a proof in HOL Light [6] of the essential incompleteness of $\Sigma _ { 1 } \cdot$ complete theories, but has not shown that any particular theory is $\Sigma _ { 1 } .$ -complete. His work will be included in the next release of HOL Light.

My proof was developed and checked in Coq 7.3.1 using Proof General under XEmacs. It is part of the user contributions to Coq and can be checked in Coq 8.0 [14]. Examples of source code in this document use the new Coq 8.0 notation.

Coq is an implementation of the calculus of (co)inductive constructions. This dependent type theory has intensional equality and is constructive, so my proof is constructive. Actually the proof depends on the Ensembles library which declares an axiom of extensionality for Ensembles, but this axiom is never used.

This document points out some of the more interesting problems I encountered when formalizing the incompleteness theorem. My proof mostly follows the presentation of incompleteness given in An Introduction to Mathematical Logic [10]. I referred to the supplementary text for the book Logic for Mathematics and Computer Science [1] to construct G¨odel’s β-function. I also use part of Caprotti and Oostdijk’s contribution of Pocklington’s criterion [2] to prove the Chinese remainder theorem.

This document is organized as follows. First I discuss the dificulties I had when formalizing classical first-order logic over an arbitrary language. This is followed by the definition of a language LNN and an axiom system called NN. Next I give the statement of the essential incompleteness of NN. Then I briefly discuss coding formulas and proofs as natural numbers. Next I discuss primitive recursive functions and the problems I encountered when trying to prove that substitution can be computed by a primitive recursive function. Finally I briefly discuss the fixed-point theorem, Rosser’s incompleteness theorem, and the incompleteness of PA. At the end I give some remarks about how to extend my work in order to formalize G¨odel’s second incompleteness theorem.

## 1.1 Coq Notation

For those not familiar with Coq syntax, here is a short list of notation

$-  , / \backslash , \backslash / ,$ and \~ are the logical connectives ⇒, ∧, ∨, and ¬.

$- \texttt { A } \to \texttt { B } , \texttt { A } * \texttt { B }$ , and $\texttt { A + B }$ form function types, Cartesian product types, and disjoint union types.

\*, +, and S are the arithmetic operations of multiplication, addition, and successor.

inl and inr are the left and right injection functions of types $\texttt { A } \to \texttt { A } + \texttt { B }$ and $\texttt { B } \to \texttt { A } + \texttt { B }$

– ::, and ++ are the list operations cons, and append.

– is an omitted parameter that Coq can infer itself.

For more details see the Coq 8.0 reference manual [14].

## 2 First-Order Classical Logic

I began by developing the theory of first order classical logic inside Coq. In essence Coq’s logic is a formal metalogic to reason about this internal logic.

## 2.1 Definition of Language

I immediately took advantage of Coq’s dependent type system by defining Language to be a dependent record of types for symbols and an arity function from symbols to N. The Coq code is:

```txt
Record Language : Type := language
{Relations : Set;
Functions : Set;
arity : Relations + Functions -> nat}.
```

In retrospect it would have been slightly more convenient to use two arity functions instead of using the disjoint union type.

This approach difers from Harrison’s definition of first order terms and formulas in HOL Light [5] because HOL Light does not have dependent types. Dependent types allow the type system to enforce that all terms and formulas of a given language are well formed.

## 2.2 Definition of Term

For any given language, a Term is either a variable indexed by a natural number or a function symbol plus a list of n terms where n is the arity of the function symbol. My first attempt at writing this in Coq failed.

```verilog
Variable L : Language.
(* Invalid definition *)
Inductive Term0 : Set :=
| var0 : nat -> Term0
| apply0 : forall (f : Functions L) (l : List Term0),
(arity L (inr _ f)) = (length l) -> Term0.
```

The type (arity L (inr f))=(length l) fails to meet Coq’s positivity requirement for inductive types. Expanding the definition of length reveals a hidden occurrence of Term0 which is passed as an implicit argument to length. It is this occurrence that violates the positivity requirement.

My second attempt met the positivity requirement, but it had other dificulties. A common way to create a polymorphic lists of length n is:

```txt
Inductive Vector (A : Set) : nat -> Set :=
| Vnil : Vector A 0
| Vcons : forall (a : A) (n : nat),
Vector A n -> Vector A (S n).
```

Using this I could have defined Term like:

```txt
Inductive Term1 : Set :=
| var1 : nat -> Term1
| apply1 : forall f : Functions L,
(Vector Term1 (arity L (inr _ f))) -> Term1.
```

My dificulty with this definition was that the induction principle generated by Coq is too weak to work with.

Instead I created two mutually inductive types: Term and Terms.

```txt
Variable L : Language.
```

```verilog
Inductive Term : Set :=
| var : nat -> Term
| apply : forall f : Functions L,
Terms (arity L (inr _ f)) -> Term
with Terms : nat -> Set :=
| Tnil : Terms 0
| Tcons : forall n : nat,
Term -> Terms n -> Terms (S n).
```

Again the automatically generated induction principle is too weak, so I used the Scheme command to generate suitable mutual-inductive principles.

The disadvantage of this approach is that useful lemmas about Vectors must be reproved for Terms. Some of these lemmas are quite tricky to prove because of the dependent type. For example, proving forall x : Terms 0, Tnil = x is not easy.

Recently, Marche has shown me that the Term1 definition would be adequate. One can explicitly make a suficient induction principle by using nested Fixpoint functions [7].

## 2.3 Definition of Formula

The definition of Formula was straightforward.

```txt
Inductive Formula : Set :=
| equal : Term -> Term -> Formula
| atomic : forall r : Relations L, Terms (arity L (inl _ r)) -> Formula
| impH : Formula -> Formula -> Formula
| notH : Formula -> Formula
| forallH : nat -> Formula -> Formula.
```

I defined the other logical connectives in terms of impH, notH, and forallH.

The H at the end of the logic connectives (such as impH) stands for “Hilbert” and is used to distinguish them from Coq’s connectives.

For example, the formula $\lnot \forall x _ { 0 } . \forall x _ { 1 } . x _ { 0 } = x .$ <sub>1</sub> would be represented by:

$$
\text { notH   (forallH   0   (forallH   1   (equal   (var   0)   (var   1)))) }
$$

It would be nice to use higher order abstract syntax to handle bound variables by giving forallH the type (Term -> Formula) -> Formula. I would represent the above example as:

$$
\begin{array}{l} \text { notH(forallH(fun x:Term => } \\ \quad (\text  forallH(fun y:Term =>(equal x y)))) \end{array}
$$

This technique would require addition work to disallow “exotic terms” that are created by passing a function into forallH that does a case analysis on the term and returning entirely diferent formulas in diferent cases. Despeyroux et al. [3] address this problem by creating a complicated predicate that only valid formulas satisfy.

Another choice would have been to use de Bruijn indexes to eliminate named variables. However dealing with free and bound variables with de Bruijn indexes can be dificult.

Using named variables allowed me to closely follow Hodel’s work [10]. Also, in order to help persuade people that the statement of the incompleteness theorem is correct, it is helpful to make the underlying definitions as familiar as possible.

Renaming bound variables turned out to be a constant source of work during development because variable names and terms were almost always abstract. In principle the variable names could conflict, so it was constantly necessary to consider this case and deal with it by renaming a bound variable to a fresh one. Perhaps it would have been better to use de Bruijn indexes and a deduction system that only deduced closed formulas.

## 2.4 Definition of substituteFormula

I defined the function substituteFormula to substitute a term for all occurrences of a free variable inside a given formula. While the definition of substituteTerm is simple structural recursion, substitution for formulas is complicated by quantifiers. Suppose we want to substitute the term s for $\mathbf { \Delta } _ { \mathbf { \mathcal { X } } _ { i } }$ in the formula $\forall x _ { j } . . \varphi$ and $i \neq j$ . Suppose $\mathbf { \Delta } _ { \mathbf { \mathcal { X } } _ { j } }$ is a free variable of s. If we na¨ıvely perform the substitution then the occurrences of $\mathbf { \Delta } _ { \mathbf { \mathcal { X } } _ { \mathcal { I } } }$ in s get captured by the quantifier. One common solution to this problem is to disallow substitution for a term s when s is not substitutable for $x _ { i }$ in $\varphi .$ . The solution I take is to rename the bound variable in this case.

$( \forall x _ { j } . \varphi ) [ { \pmb x } _ { i } / s ] \stackrel { \mathrm { d e f } } { = } \forall { \pmb x } _ { k } . ( \varphi [ { \pmb x } _ { j } / { \pmb x } _ { k } ] ) [ { \pmb x } _ { i } / s ]$ where k 6= i and $\scriptstyle { \mathbf {  { x } } } _ { k }$ is not free in ϕ or s

Unfortunately this definition is not structurally recursive. The second substitution operates on the result of the first substitution, which is not structurally smaller than the original formula.

Coq will not accept this recursive definition as is; it is necessary to prove the recursion will terminate. I proved that substitution preserves the depth of a formula, and that each recursive call operates on a formula of smaller depth.

One of McBride’s mantras says, “If my recursion is not structural, I am using the wrong structure” [8, p. 241]. In this case, my recursion is not structural because I am using the wrong recursion. Stoughton shows that it is easier to define substitution that substitutes all variables simultaneously because the recursion is structural [13]. If I had made this definition first, I could have defined substitution of one variable in terms of it and many of my dificulties would have disappeared.

## 2.5 Definition of Prf

I defined the inductive type (Prf Gamma phi) to be the type of proofs of phi, from the list of assumptions Gamma.

```txt
Inductive Prf : Formulas -> Formula -> Set :=
| AXM : forall A : Formula, Prf (A :: nil) A
| MP : forall (Axm1 Axm2 : Formulas) (A B : Formula),
    Prf Axm1 (impH A B) -> Prf Axm2 A ->
    Prf (Axm1 ++ Axm2) B
| GEN : forall (Axm : Formulas) (A : Formula) (v : nat),
    ~ In v (freeVarListFormula L Axm) -> Prf Axm A ->
    Prf Axm (forallH v A)
| IMP1 : forall A B : Formula, Prf nil (impH A (impH B A))
| IMP2 : forall A B C : Formula,
    Prf nil (impH (impH A (impH B C))
    (impH (impH A B) (impH A C)))
| CP : forall A B : Formula,
    Prf nil (impH (impH (notH A) (notH B)) (impH B A))
| FA1 : forall (A : Formula) (v : nat) (t : Term),
    Prf nil (impH (forallH v A) (substituteFormula L A v t))
| FA2 : forall (A : Formula) (v : nat),
    ~ In v (freeVarFormula L A) -> Prf nil (impH A (forallH v A))
| FA3 : forall (A B : Formula) (v : nat),
    Prf nil
    (impH (forallH v (impH A B))
    (impH (forallH v A) (forallH v B)))
| EQ1 : Prf nil (equal (var 0) (var 0))
| EQ2 : Prf nil (impH (equal (var 0) (var 1))
    (equal (var 1) (var 0)))
| EQ3 : Prf nil
    (impH (equal (var 0) (var 1))
    (impH (equal (var 1) (var 2)) (equal (var 0) (var 2))))
| EQ4 : forall R : Relations L, Prf nil (AxmEq4 R)
```

AxmEq4 and AxmEq5 are recursive functions that generate the equality axioms for relations and functions. AxmEq4 R generates

$$
\boldsymbol {x} _ {0} = \boldsymbol {x} _ {1} \Rightarrow \dots \Rightarrow \boldsymbol {x} _ {2 n - 2} = \boldsymbol {x} _ {2 n - 1} \Rightarrow (R (\boldsymbol {x} _ {0}, \dots , \boldsymbol {x} _ {2 n - 2}) \Leftrightarrow R (\boldsymbol {x} _ {1}, \dots , \boldsymbol {x} _ {2 n - 1}))
$$

and AxmEq5 f generates

$$
\boldsymbol {x} _ {0} = \boldsymbol {x} _ {1} \Rightarrow \dots \Rightarrow \boldsymbol {x} _ {2 n - 2} = \boldsymbol {x} _ {2 n - 1} \Rightarrow f (\boldsymbol {x} _ {0}, \dots , \boldsymbol {x} _ {2 n - 2}) = f (\boldsymbol {x} _ {1}, \dots , \boldsymbol {x} _ {2 n - 1})
$$

I found that replacing ellipses from informal proofs with recursive functions was one of the most dificult tasks. The informal proof does not contain information on what inductive hypothesis should be used when reasoning about these recursive definitions. Figuring out the correct inductive hypotheses was not easy.

## 2.6 Definition of SysPrf

There are some problems with the definition of Prf given. It requires the list of axioms to be in the correct order for the proof. For example, if we have Prf Gamma1 (impH phi psi) and Prf Gamma2 phi then we can conclude only Prf Gamma1++Gamma2 psi. We cannot conclude Prf Gamma2++Gamma1 psi or any other permutation of psi. If an axiom is used more than once, it must appear in the list more than once. If an axiom is never used, it must not appear. Also, the number of axioms must be finite because they form a list.

To solve this problem, I defined a System to be Ensemble Formula, and (SysPrf T phi) to be the proposition that the system T proves phi.

```txt
Definition System := Ensemble Formula.
Definition mem := Ensembles.In.

Definition SysPrf (T : System) (f : Formula) :=
    exists Axm : Formulas,
    (exists prf : Prf Axm f,
    (forall g : Formula, In g Axm -> mem _ T g)).
```

Ensemble A represents subsets of A by the functions A -> Prop. a : A is consid ered to be a member of T : Ensemble A if and only if the type T a is inhabited. I also defined mem to be Ensembles.In so that it does not conflict with List.In.

## 2.7 The Deduction Theorem

The deduction theorem states that if $T \cup \{ \varphi \} \vdash \psi$ then $T \vdash \varphi \Rightarrow \psi .$

There is a choice of whether the side condition for the ∀-generalization rule, \~ In v (freeVarListFormula L Axm), should be required or not. If this side condition is removed then the deduction theorem requires a side condition on it. Usually all the formulas in an axiom system are closed, so the side condition on the ∀-generalization is easy to show. So I decided to keep the side condition on the ∀-generalization rule.

At one point the proof of the deduction theorem requires proving that if ${ \cal { T } } \cup \{ \varphi \} \vdash \psi$ because $\psi \in { \cal { T } } \cup \{ \varphi \}$ , then ${ \cal { T } } \vdash \varphi \Rightarrow \psi$ . There are two cases to consider. If $\psi = \varphi$ then the result easily follows from the reflexivity $\mathrm { o f } \Rightarrow$ Otherwise $\psi \in { \cal T } .$ , and therefore $T \vdash \psi$ . The result then follows. In order to constructively make this choice it is necessary to decide whether $\psi = \varphi$ or not. This requires Formula to be a decidable type, and that requires the language L to be decidable. Since L could be anything, I needed to add hypotheses that the function and relation symbols are decidable types.

$$
\begin{array}{l} \text {forall x y : Functions L, \{x = y\} + \{x <   >y} \\ \text {forall x y : Relations L, \{x = y\} + \{x <   >y}. \end{array}
$$

I used the deduction theorem without restriction and ended up using the hypotheses in many lemmas. I expect that many of these lemmas could be proved without assuming the decidability of the language. It is hard to imagine a useful language that is not decidable, so I do not feel too bad about using these hypotheses in unnecessary places.

## 2.8 Languages and Theories of Number Theory

I created two languages. The first language, LNT, is the language of number theory and just has the function symbols Plus, Times, Succ, and Zero with appropriate arities. The second language, LNN, is the language of NN and has the same function symbols as LNT plus one relation symbol for less than, LT.

I define two axiom systems: NN and PA. NN and PA share six axioms.

1. $\forall x _ { 0 } . . . . S x _ { 0 } = \mathbf { 0 }$

2. $\forall x _ { 0 } . \forall x _ { 1 } . ( S x _ { 0 } = S x _ { 1 } \Rightarrow x _ { 0 } = x _ { 1 } )$

3. $\forall \pmb { x } _ { 0 } . \pmb { x } _ { 0 } + \pmb { 0 } = \pmb { x } _ { 0 }$

4. $\forall x _ { 0 } . \forall x _ { 1 } . x _ { 0 } + S x _ { 1 } = S ( x _ { 0 } + x _ { 1 } )$

5. $\forall \pmb { x } _ { 0 } . \pmb { x } _ { 0 } \times \pmb { 0 } = \mathbf { 0 }$

$$
\forall \boldsymbol {x} _ {0}. \forall \boldsymbol {x} _ {1}. \boldsymbol {x} _ {0} \times \boldsymbol {S x} _ {1} = (\boldsymbol {x} _ {0} \times \boldsymbol {x} _ {1}) + \boldsymbol {x} _ {0}
$$

NN has three additional axioms about less than.

1. $\forall x _ { 0 } . . . . x _ { 0 } < \mathbf { 0 }$

$$
\forall \boldsymbol {x} _ {0}. \forall \boldsymbol {x} _ {1}. (\boldsymbol {x} _ {0} <   \boldsymbol {S x} _ {1} \Rightarrow (\boldsymbol {x} _ {0} = \boldsymbol {x} _ {1} \lor \boldsymbol {x} _ {0} <   \boldsymbol {x} _ {1}))
$$

3. $\forall x _ { 0 } . \forall x _ { 1 } . ( x _ { 0 } < x _ { 1 } \lor x _ { 0 } = x _ { 1 } \lor x _ { 1 } < x _ { 0 } )$

PA has an infinite number of induction axioms that follow one schema.

$$
1. \text {(schema)} \forall \boldsymbol {x} _ {i _ {1}} \dots \forall \boldsymbol {x} _ {i _ {n}}. \varphi [ \boldsymbol {x} _ {j} / \boldsymbol {0} ] \Rightarrow \forall \boldsymbol {x} _ {j}. (\varphi \Rightarrow \varphi [ \boldsymbol {x} _ {j} / S \boldsymbol {x} _ {j} ]) \Rightarrow \forall \boldsymbol {x} _ {j}. \varphi
$$

The $\pmb { x } _ { i _ { 1 } } , \ldots , \pmb { x } _ { i _ { n } }$ are the free variables of $\forall x _ { j } . . \varphi$ . The quantifiers ensure that all the axioms of PA are closed.

Because NN is in a diferent language than PA, a proof in NN is not a proof in PA. In order to reuse the work done in NN, I created a function called LNN2LNT formula to convert formulas in LNN into formulas in LNT by replacing occurrences of $t _ { 0 } ~ < ~ t _ { 1 }$ with $( \exists { \pmb x } _ { 2 } . { \pmb x } _ { 0 } + ( { \pmb S } { \pmb x } _ { 2 } ) = { \pmb x } _ { 1 } ) [ { \pmb x } _ { 0 } / t _ { 0 } , { \pmb x } _ { 1 } / t _ { 1 } ] .$ $\varphi [ { \pmb x } _ { 0 } / t _ { 0 } , { \pmb x } _ { 1 } / t _ { 1 } ]$ is the simultaneous substitution of $t _ { 0 }$ for $\scriptstyle { \mathbf { { \mathit { x } } } } _ { 0 }$ and $t _ { 1 }$ for $\scriptstyle { \mathbf { \mathscr { x } } } _ { 1 }$ . Then I proved that if $\mathrm { N N } \vdash \varphi$ then PA ⊢ LNN2LNT formul $\mathsf { a } ( \varphi )$

I also created the function natToTerm : nat -> Term to return the closed term representing a given natural number. In this document I will refer to this function as $\Gamma . 7$ , so $ { \boldsymbol { \Gamma } } 0 ^ { \top } = \mathbf { 0 } ,  { \boldsymbol { \Gamma } } 1 ^ { \top } =  { \boldsymbol { S } } \mathbf { 0 }$ , etc.

## 3 Coding

To prove the incompleteness theorem, it is necessary for the inner logic to reason about proofs and formulas, but the inner logic can only reason about natural numbers. It is therefore necessary to code proofs and formulas as natural numbers.

G¨odel’s original approach was to code a formula as a list of numbers and then code that list using properties from the prime decomposition theorem[4]. I avoided needing theorems about prime decomposition by using the Cantor pairing function instead. The Cantor pairing function, cPair, is a commonly used bijection between $\mathbb { N } \times \mathbb { N }$ and N.

$$
\operatorname{cPair} (a, b) \stackrel {{\text { def }}} {{=}} a + \sum_ {i = 1} ^ {a + b} i
$$

All my inductive structures were easy to recursively encode. I gave each constructor a unique number and paired that number with the encoding of all its parameters. For example, I defined codeFormula as:

```verilog
Fixpoint codeFormula (f : Formula) : nat :=
match f with
| fol.equal t1 t2 => cPair 0 (cPair (codeTerm t1) (codeTerm t2))
| fol.impH f1 f2 =>
    cPair 1 (cPair (codeFormula f1) (codeFormula f2))
| fol.notH f1 => cPair 2 (codeFormula f1)
| fol.forallH n f1 => cPair 3 (cPair n (codeFormula f1))
| fol.atomic R ts => cPair (4+(codeR R)) (codeTerms _ ts)
end.

where codeR is a coding of the relation symbols for the language.
I will use 「φ」 for 「codeFormula φ」 and 「t」 for 「codeTerm t」.
```

## 4 The Statement of Incompleteness

The incompleteness theorem states the essential incompleteness of NN, meaning that for every axiom system T such that

$$
- \mathrm{NN} \subseteq T
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$T$ can represent its own axioms $T$ is a decidable set
</div>

then there exists a sentence ϕ such that if T ⊢ ϕ or T ⊢ ¬ϕ then T is inconsistent. The theorem is only about proofs in LNN, the language of NN. This statement does not show the incompleteness of theories that extend the language.

In Coq the theorem is stated as as:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Theorem Incompleteness
: forall T : System,
Included Formula NN T -&gt;
RepresentsInSelf T -&gt;
DecidableSet Formula T -&gt;
exists f : Formula,
Sentence f /$SysPrf T f \/ SysPrf T (notH f) -&gt; Inconsistent LNN T$.
</div>

A System is Inconsistent if it proves all formulas.

```txt
Definition Inconsistent (T : System) := forall f : Formula, SysPrf T f.
```

A Sentence is a Formula without any free variables.

```prolog
Definition Sentence (f : Formula) :=
    forall v : nat, ~ In v (freeVarFormula LNN f).
```

A DecidableSet is an Ensemble such that every item either belongs to the Ensemble or does not belong to the Ensemble. This hypothesis is trivially true in classical logic, but in constructive logic I needed it to prove the strong constructive existential quantifier in the statement of incompleteness.

```txt
Definition DecidableSet (A : Type)(s : Ensemble A) := forall x : A, mem A s x \/ ~ mem A s x.
```

The RepresentsInSelf hypothesis restricts what the System T can be. The statement of essential incompleteness normally requires T be a recursive set. Instead I use the weaker hypothesis that the set T is expressible in the system T.

Given a system T extending NN and another system U along with a formula ϕ with at most one free variable ${ \mathbf { } } x _ { i } .$ , we say ϕ expresses the axiom system U in T if the following hold for all formulas $\psi$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1. if $\psi \in U$ then $T\vdash \varphi_U[\pmb {x}_i / \ulcorner \psi \urcorner ]$   
2. if $\psi \notin U$ then $T\vdash \neg \varphi_U[\pmb {x}_i / \ulcorner \psi \urcorner ]$
</div>

U is expressible in T if there exists a formula $\varphi _ { U }$ such that $\varphi _ { U }$ expresses the axiom system U in T.

In Coq I write the statement T is expressible in $T$ as

```txt
Definition RepresentsInSelf (T : System) :=
exists rep : Formula, exists v : nat,
(forall x : nat, In x (freeVarFormula LNN rep) -> x = v) /\
(forall f : Formula,
    mem Formula T f ->
    SysPrf T (substituteFormula LNN rep v
    (natToTerm (codeFormula f)))) /\
(forall f : Formula,
    ~ mem Formula T f ->
    SysPrf T (notH (substituteFormula LNN rep v
    (natToTerm (codeFormula f)))).
```

This is weaker than requiring that T be a recursive set because any recursive set of axioms T is expressible in NN. Since T is an extension of NN, any recursive set of axioms T is expressible in T .

By using this weaker hypothesis I avoid defining what a recursive set is. Also, in this form the theorem could be used to prove that any complete and consistent theory of arithmetic cannot define its own axioms. In particular, this could be used to prove Tarski’s theorem that the truth predicate is not definable.

## 5 Primitive Recursive Functions

A common approach to proving the incompleteness theorem is to prove that every primitive recursive function is representable. Informally an n-ary function f is representable in NN if there exists a formula ϕ such that

1. the free variables of ϕ are among x<sub>0</sub>, . . . , x<sub>n</sub>.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
2. for all  $a_{1},\ldots,a_{n}:N$ ,
NN  $\vdash (\varphi \Rightarrow \boldsymbol{x}_{0} = \lceil f(a_{1},\ldots,a_{n}) \rceil)[\boldsymbol{x}_{1}/\lceil a_{1} \rceil, \ldots, \boldsymbol{x}_{n}/\lceil a_{n} \rceil]$
</div>

I defined the type PrimRec n as:

```verilog
Inductive PrimRec : nat -> Set :=
| succFunc : PrimRec 1
| zeroFunc : PrimRec 0
| projFunc : forall n m : nat, m < n -> PrimRec n
| composeFunc :
    forall (n m : nat) (g : PrimRecs n m) (h : PrimRec m),
    PrimRec n
| primRecFunc :
    forall (n : nat) (g : PrimRec n) (h : PrimRec (S (S n))), 
    PrimRec (S n)
with PrimRecs : nat -> nat -> Set :=
| PRnil : forall n : nat, PrimRecs n 0
| PRcons : forall n m : nat,
    PrimRec n -> PrimRecs n m -> PrimRecs n (S m).
```

PrimRec n is the expression of an n-ary primitive recursive function, but it is not itself a function. I defined evalPrimRec : forall n : nat, PrimRec n -> naryFunc n to convert the expression into a function. Rather than working directly with primitive recursive expressions, I worked with particular Coq functions and proved they were extensionally equivalent to the evaluation of primitive recursive expressions.

I proved that every primitive recursive function is representable in NN. This required using G¨odel’s $\beta \mathrm { . }$ function along with the Chinese remainder theorem. The $\beta \mathrm { . }$ -function is a function that codes array indexing. A finite list of numbers $a _ { 0 } , \ldots , a _ { n }$ is coded as a pair of numbers $( x , y )$ and $\beta ( x , y , i ) = a _ { i }$ . The $\beta \mathrm { . }$ -function is special because it is defined in terms of plus and times and is non-recursive. The Chinese remainder theorem is used to prove that the $\beta \mathrm { . }$ -function works.

I took care to make the formulas representing the primitive recursive functions clearly $\Sigma _ { 1 }$ by ensuring that only the unbounded quantifiers are existential; however, I did not prove that the formulas are $\Sigma _ { 1 }$ because it is not needed for the first incompleteness theorem. Such a proof could be used for the second incompleteness theorem [12].

## 5.1 codeSubFormula is Primitive Recursive

I proved that substitution is primitive recursive. Since substitution is defined in terms of Formula and Term, it itself cannot be primitive recursive. Instead I proved that the corresponding function operating on codes is primitive recursive. This function is called codeSubFormula and I proved it is correct in the following sense.

$$
\text { codeSubFormula } (^ {\lceil} \varphi^ {\lceil}, i, ^ {\lceil} s ^ {\lceil}) = ^ {\lceil} \varphi [ \boldsymbol {x} _ {i} / s ] ^ {\lceil}
$$

Next I proved that it is primitive recursive. This proof is very dificult. The problem is again with the need to rebind bound variables. Normally one would attempt to create this primitive recursive function by using course-of-values recursion. Course-of-values recursion requires all recursive calls have a smaller code than the original call. Renaming a bound variable requires two recursive calls. Recall the definition of substitution in this case:

$( \forall x _ { j } . \varphi ) [ { \pmb x } _ { i } / s ] \stackrel { \mathrm { d e f } } { = } \forall { \pmb x } _ { k } . ( \varphi [ { \pmb x } _ { j } / { \pmb x } _ { k } ] ) [ { \pmb x } _ { i } / s ]$ where k $\neq$ i and $\scriptstyle { \mathbf {  { x } } } _ { k }$ is not free in $\varphi$ or s

If one is lucky one might be able to make the inner recursive call. But there is no reason to suspect the input to the second recursive call, $\varphi [ \pmb { x } _ { j } / \pmb { x } _ { k } ]$ , is going to have a smaller code than the original input, $\forall x _ { j } . . \varphi$

If I had used the alternative definition of substitution, where all variables are substituted simultaneously, there would still be problems. The input would include a list of variable and term pairs. In this case a new pair would be added to the list when making the recursive call, so the input to the recursive call could still have a larger code than the input to the original call.

It seems that using course-of-values recursion is dificult or impossible. Instead I introduce the notion of the trace of the computation of substitution. Think of the trace of computation as a finite tree where the nodes contain the input and output of each recursive call. The subtrees of a node are the traces of the computation of the recursive calls. This tree can be coded as a number. I proved that there is a primitive recursive function that can check to see if a number represents a trace of the computation of substitution.

The key to solving this problem is to create a primitive recursive function that computes a bound on how large the code of the trace of computation can be for a given input. With this I created another primitive recursive function that searches for the trace of computation up to this bound. Once the trace is found—I proved that it must be found—the function extracts the result from the trace and returns it.

## 5.2 checkPrf is Primitive Recursive

Given a code for a formula and a code for a proof, the function checkPrf returns 0 if the proof does not prove the formula, otherwise it returns one plus the code of the list of axioms used in the proof. I proved this function is primitive recursive, as well as proving that it is correct in the sense that for every proof $p$ of $\varphi$ from a list of axioms $T _ { \mathbf { \delta } }$ , checkPrf $( ^ { \Gamma } \varphi ^ {                , \Gamma } p ^ { \intercal } ) = 1 + { } ^ { \Gamma } \Gamma ^ { \intercal } ;$ and for all $n , m : \mathbb { N }$ if checkPrf $( n , m ) \neq 0$ then there exists $\varphi , T$ , and some proof $p$ of $\varphi$ from $\varGamma$ such that $\ulcorner \varphi ^ { \daleth } = n$ and $^ { \Gamma } p ^ { 7 } = m$

For any axiom system $U$ expressible in T, I created the formulas codeSysPrf and codeSysPf. code $\mathrm { ; y s P r f } [ { \pmb x } _ { 0 } / \Gamma n ^ { \top } , { \pmb x } _ { 1 } / \Gamma m ^ { \top } ]$ is provable in $T$ if m is the code of a proof in $U$ of a formula coded by n. codeS $\mathtt { y s P f } [ \pmb { x } _ { 0 } / \Gamma _ { n } \rceil ]$ is provable in $T$ if there exists a proof in $U$ of a formula coded by n.

codeSysPrf and codeSysPf are not derived from a primitive recursive functions because I wanted to prove the incompleteness of axiom systems that may not have a primitive recursive characteristic function.

## 6 Fixed Point Theorem and Rosser’s Incompleteness Theorem

The fixed point theorem states that for every formula $\varphi$ there is some formula $\psi$ such that

$$
\mathrm{NN} \vdash \psi \Leftrightarrow \varphi [ \boldsymbol {x} _ {i} / \ulcorner \psi \urcorner ]
$$

and that the free variables of $\psi$ are that of $\varphi$ less $\mathbf { \Delta } _ { \mathbf { \mathcal { X } } _ { i } }$ .

The fixed point theorem allows one to create “self-referential sentences”. I used this to create Rosser’s sentence which states that for every code of a proof of itself, there is a smaller code of a proof of its negation. The proof of Rosser’s incompleteness theorem requires doing a bounded search for a proof, and this requires knowing what is and what is not a proof in the system. For this reason, I require the decidability of the axiom system. Without a decision procedure for the axiom system, I cannot constructively do the search.

## 6.1 Incompleteness of PA

To demonstrate the incompleteness theorem I used it to prove the incompleteness of PA. I created a primitive recursive predicate for the codes of the axioms of PA. Coq is suficiently powerful to prove the consistency of PA by proving that the natural numbers model PA.

One subtle point is that Coq’s logic is constructive while the internal logic is classical. One cannot interpret a formula of the internal logic directly in Coq and expect it to be provable if it is provable in the internal logic. Instead I use a double negation translation of the formulas. The translated formula will always hold if it holds in the internal logic.

The consistency of PA along with the expressibility of its axioms and the translations of proofs from NN to PA allowed me to apply Rosser’s incompleteness theorem and prove the incompleteness of PA—there exists a sentence ϕ such that neither $\mathrm { P A } \vdash \varphi$ nor $\mathrm { P A } \vdash \lnot \varphi$

```txt
Theorem PAIncomplete : 
    exists f : Formula,
    (forall v : nat, ~ In v (freeVarFormula LNT f)) /\
    ~ (SysPrf PA f \/ SysPrf PA (notH f)).
```

## 7 Remarks

## 7.1 Extracting the Sentence

Because my proof is constructive, it is possible, in principle, to compute this sentence that makes PA incomplete. This was not done for two reasons. The first reason is that the existential statement lives in Coq’s Prop universe, and Coq’s only extracts from its Set universe. This was an error on my part. I should have used Coq’s Set existential quantifier; this problem would be fairly easy to fix. The second reason is that the sentence contains a closed term of the code of most of itself. I believe this code is a very large number and it is written in unary notation. This would likely make the sentence far to large to be actually printed.

## 7.2 Robinson’s System Q

The proof of essential incompleteness is usually carried out for Robinson’s system Q. Instead I followed Hodel’s development [10] and used NN. Q is PA with the induction schema replaced with $\forall \mathbf { x } _ { 0 }$ .∃x<sub>1</sub>. $( \pmb { x } _ { 0 } = \mathbf { 0 } \lor \pmb { x } _ { 0 } = \pmb { S } \pmb { x } _ { 1 } )$ . All of NN axioms are $\varPi _ { 1 }$ whereas Q has the above $\varPi _ { 2 }$ axiom. Both axiom systems are finite.

Neither system is strictly weaker than the other, so it would not be possible to use the essential incompleteness of one to get the essential incompleteness of the other; however both NN and Q are suficiently powerful to prove a small number of needed lemmas, and afterward only these lemmas are used. If one abstracts my proof at these lemmas, it would then be easy to prove the essential incompleteness of both Q and NN.

## 7.3 Comparisons with Shankar’s 1986 Proof

It is worth noting the diferences between this formalization of the incompleteness theorem and Shankar’s 1986 proof in the Boyer-Moore theorem prover. The most notable diference is the proof systems. In Coq the user is expected to input the proof, in the form of a proof script, and Coq will check the correctness of the proof. In the Boyer-Moore theorem prover the user states a series of lemmas and the system generates the proofs. However, using the Boyer-Moore proof system requires feeding it a “well-chosen sequence of lemmas” [11, p. xii], so it would seem the information being fed into the two systems is similar.

There are some notable semantic diferences between Shankar’s statement of incompleteness and mine. His theorem only states that finite extensions of Z2, hereditarily finite set theory, are incomplete, whereas my theorem states that even infinite extensions of NN are incomplete as long as they are selfrepresentable. Also Shankar’s internal logic allows axioms to define new relation or function symbols as long as they come with the required proofs of admissibility. Such extensions are conservative over $\mathrm { Z 2 } .$ but no computer verified proof of this fact is given. My internal logic does not allow new symbols. Finally, I prove the essential incompleteness of NN, which is in the language of arithmetic. Without any set structures the proof is somewhat more dificult because it requires using G¨odel’s $\beta \mathrm { . }$ -function.

One of Shankar’s goals when creating his proof was to use a proof system without modifications. Unfortunately he was not able to meet that goal; he ended up making some improvements to the Boyer-Moore theorem prover. My proof was developed in Coq without any modifications.

## 7.4 G¨odel’s Second Incompleteness Theorem

The second incompleteness theorem states that if $T$ is a recursive system extending PA—actually a weaker system could be used here—and $T \vdash \mathrm { C o n } _ { T }$ then T is inconsistent. Con<sub>T</sub> is some reasonable formula stating the consistency of $T ,$ such as $\lnot \mathrm { P r } _ { T } ( \Gamma \mathbf { 0 } = S \mathbf { 0 } ^ { \lnot \setminus j } )$ ), where Pr<sub>T</sub> is the provability predicate codeSysPf for $T .$

If I had created a formal proof in PA, I would have $\vdash _ { \mathrm { P A } }$ “G¨odel’s first incompleteness theorem”. This could then be mechanically transformed to create another formal proof in PA that ⊢<sub>PA</sub> (PA ⊢ “G¨odel’s first incompleteness theorem”). The reader can verify that the second incompleteness theorem follows from this. Unfortunately I have only shown that ⊢ ${ \bf \bar { \Delta } } _ { C o q }$ “G¨odel’s first incompleteness theorem”, so the above argument cannot be used to create a proof of the second incompleteness theorem.

Still, this work can be used as a basis for formalizing the second incompleteness theorem. The approach would be to formalize the Hilbert-Bernays-L¨ob derivability conditions:

1. if $\mathrm { P A } \vdash \varphi$ then $\mathrm { P A } \vdash \mathrm { P r } _ { \mathrm { P A } } ( ^ { \Gamma } \varphi ^ { \daleth } )$

$$
\begin{array}{l} 2. \text { PA } \vdash \text { Pr } _ {\text { PA }} (\ulcorner \varphi \urcorner) \Rightarrow \text { Pr } _ {\text { PA }} (\ulcorner \text { Pr } _ {\text { PA }} (\ulcorner \varphi \urcorner) \urcorner) \\ 3. \text { PA } \vdash \text { Pr } _ {\text { PA }} (\ulcorner \varphi \Rightarrow \psi \urcorner) \Rightarrow \text { Pr } _ {\text { PA }} (\ulcorner \varphi \urcorner) \Rightarrow \text { Pr } _ {\text { PA }} (\ulcorner \psi \urcorner) \end{array}
$$

The second condition is the most dificult to prove. It is usually proved by first proving that for every $\Sigma _ { 1 }$ sentence $\varphi , \mathrm { P A } \vdash \varphi \Rightarrow \mathrm { P r } _ { \mathrm { P A } } ( ^ { \Gamma } \varphi ^ { \rceil } )$ . Because I made sure that all primitive recursive functions are representable by a $\Sigma _ { 1 }$ formula, it would be easy to go from this theorem to the second Hilbert-Bernays-L¨ob condition.

## 8 Statistics

My proof, excluding standard libraries and the library for Pocklington’s criterion [2], consists of 46 source files, 7 036 lines of specifications, 37 906 lines of proof, and 1 267 747 total characters. The size of the gzipped tarball $\left( \mathtt { g } \mathtt { z } \mathtt { i } \mathtt { p } \ - \mathtt { 9 } \right)$ of all the source files is 146 008 bytes, which is an estimate of the information content of my proof.

## 9 Acknowledgements

I would like to thank NSERC for providing funding for this research. I thank Robert Schneck for introducing me to Coq, and helping me out at the beginning. I would like to thank Nikita Borisov for letting me use his computer when the proof became to large for my poor laptop. I would also like to thank my Berkeley advisor, Leo Harrington, for his advice on improving upon Hodel’s proof. And last, but not least, thanks to the Coq team, because without Coq there would be no proof.

## References

1. Stanley N. Burris. Logic for mathematics and computer science: Supplementary text. http://www.math.uwaterloo.ca/\~snburris/htdocs/LOGIC/stext.html, 1997.

2. Olga Caprotti and Martijn Oostdijk. Formal and eficient primality proofs by use of computer algebra oracles. J. Symb. Comput., 32(1/2):55–70, 2001.

3. Jo¨elle Despeyroux and Andr´e Hirschowitz. Higher-order abstract syntax with induction in coq. In LPAR ’94: Proceedings of the 5th International Conference on Logic Programming and Automated Reasoning, pages 159–173, London, UK, 1994. Springer-Verlag.

4. K. G¨odel. Ueber Formal Unentscheidbare s¨atze der Principia Mathematica und Verwandter Systeme I. Monatshefte f¨ur Mathematik und Physik, 38:173–198, 1931. english translation: On Formally Undecidable Propositions of Principia Mathemat ica and Related Systems I, Oliver & Boyd, London, 1962.

5. John Harrison. Formalizing basic first order model theory. In Jim Grundy and Malcolm Newey, editors, Theorem Proving in Higher Order Logics: 11th International Conference, TPHOLs’98, volume 1497 of Lecture Notes in Computer Science, pages 153–170, Canberra, Australia, 1998. Springer-Verlag.

6. John Harrison. The HOL-Light manual, 2000.

7. Claude Marche. Fwd: Question about fixpoint. Coq club mailing list correspondence, http://pauillac.inria.fr/pipermail/coq-club/2005/001641.html, [cited 2005-02-07], February 2005.

8. Conor McBride. Dependently Typed Functional Programs and their Proofs. PhD thesis, University of Edinburgh, 1999. Available from http://www.lfcs.informatics.ed.ac.uk/reports/00/ECS-LFCS-00-419/.

9. Russell O’Connor. The G¨odel-Rosser 1st incompleteness theorem. http://r6.ca/Goedel20050512.tar.gz, March 2005.

10. Richard E. Hodel. An Introduction to Mathematical Logic. PWS Pub. Co., 1995.

11. N. Shankar. Metamathematics, Machines, and G¨odel’s Proof. Cambridge Tracts in Theoretical Computer Science. Cambridge University Press, Cambridge, UK, 1994.

12. J. R. Shoenfield. Mathematical Logic. Addison-Wesley, 1967.

14. The Coq Development Team. The Coq Proof Assistant Reference Manual – Version V8.0, April 2004. http://coq.inria.fr.

13. Allen Stoughton. Substitution revisited. 59(3):317–325, August 1988.