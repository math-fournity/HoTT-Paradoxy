# ELEMENTS OF SET THEORY

Herbert B. Enderton

DEPARTMENT OF MATHEMATICS
UNIVERSITY OF CALIFORNIA, LOS ANGELES
LOS ANGELES, CALIFORNIA

![](images/14eb3de39ef6733b29191e51ac8766363161f009b6f779a186c42db848a40e71.jpg)

ACADEMIC PRESS New York San Francisco London
A Subsidiary of Harcourt Brace Jovanovich, Publishers

COPYRIGHT © 1977, BY ACADEMIC PRESS, INC.
ALL RIGHTS RESERVED.
NO PART OF THIS PUBLICATION MAY BE REPRODUCED OR TRANSMITTED IN ANY FORM OR BY ANY MEANS, ELECTRONIC OR MECHANICAL, INCLUDING PHOTOCOPY, RECORDING, OR ANY INFORMATION STORAGE AND RETRIEVAL SYSTEM, WITHOUT PERMISSION IN WRITING FROM THE PUBLISHER.

ACADEMIC PRESS, INC.
111 Fifth Avenue, New York, New York 10003

United Kingdom Edition published by
ACADEMIC PRESS, INC. (LONDON) LTD.
24/28 Oval Road, London NW1

Library of Congress Cataloging in Publication Data

Enderton, Herbert B
Elements of set theory.

Bibliography: p.
Includes index.
1. Set theory. I.
QA248.E5 511'.3
ISBN 0-12-238440-7

AMS (MOS) 1970 Subject Classifications: 04-01, 04A05, 04A10

PRINTED IN THE UNITED STATES OF AMERICA

To my teachers with gratitude
To my students with hope

Preface xi
List of Symbols xiii
Chapter 1 INTRODUCTION 1
Baby Set Theory 1
Sets—An Informal View 7
Classes 10
Axiomatic Method 10
Notation 13
Historical Notes 14
Chapter 2 AXIOMS AND OPERATIONS 17
Axioms 17
Arbitrary Unions and Intersections 23
Algebra of Sets 27
Epilogue 33
Review Exercises 33

Chapter 3 RELATIONS AND FUNCTIONS 35
Ordered Pairs 35
Relations 39
n-Ary Relations 41
Functions 42
Infinite Cartesian Products 54
Equivalence Relations 55
Ordering Relations 62
Review Exercises 64

Chapter 4 NATURAL NUMBERS 66
Inductive Sets 67
Peano's Postulates 70
Recursion on ω 73
Arithmetic 79
Ordering on ω 83
Review Exercises 88

Chapter 5 CONSTRUCTION OF THE REAL NUMBERS 90
Integers 90
Rational Numbers 101
Real Numbers 111
Summaries 121
Two 123

Chapter 6 CARDINAL NUMBERS AND THE AXIOM OF CHOICE 128
Equinumerosity 128
Finite Sets 133
Cardinal Arithmetic 138
Ordering Cardinal Numbers 145
Axiom of Choice 151
Countable Sets 159
Arithmetic of Infinite Cardinals 162
Continuum Hypothesis 165

Chapter 7 ORDERINGS AND ORDINALS 167
Partial Orderings 167
Well Orderings 172
Replacement Axioms 179
Epsilon-Images 182
Isomorphisms 184
Ordinal Numbers 187
Debts Paid 195
Rank 200

Contents ix
Chapter 8 ORDINALS AND ORDER TYPES 209
Transfinite Recursion Again 209
Alephs 212
Ordinal Operations 215
Isomorphism Types 220
Arithmetic of Order Types 222
Ordinal Arithmetic 227
Chapter 9 SPECIAL TOPICS 241
Well-Founded Relations 241
Natural Models 249
Cofinality 257
Appendix NOTATION, LOGIC, AND PROOFS 263
Selected References for Further Study 269
List of Axioms 271
Index 273

This is an introductory undergraduate textbook in set theory. In mathematics these days, essentially everything is a set. Some knowledge of set theory is a necessary part of the background everyone needs for further study of mathematics. It is also possible to study set theory for its own interest—it is a subject with intriguing results about simple objects. This book starts with material that nobody can do without. There is no end to what can be learned of set theory, but here is a beginning.

The author of a book always has a preferred manner for using the book: A reader should simply study it from beginning to end. But in practice, the users of a book have their own goals. I have tried to build into the present book enough flexibility to accommodate a variety of goals.

The axiomatic material in the text is marked by a stripe in the margin. The purpose of the stripe is to allow a user to deemphasize the axiomatic material, or even to omit it entirely.

A course in axiomatic set theory might reasonably cover the first six or seven chapters, omitting Chapter 5. This is the amount of set theory that everyone with an interest in matters mathematical should know. Those with a special interest in set theory itself are encouraged to continue to the end of the book (and beyond). A very different sort of course might emphasize the set-theoretic construction of the number systems. This course might cover the first five chapters, devoting only as much attention to the axiomatic material as desired. The book presupposes no specific background. It does give real proofs. The first difficult proof is not met until part way through Chapter 4.

The hierarchical view of sets, constructed by transfinite iteration of the power set operation, is adopted from the start. The axiom of regularity is not added until it can be proved to be equivalent to the assertion that every set has a rank.

The exercises are placed at the end of each (or nearly each) section. In addition, Chapters 2, 3, and 4 have “Review Exercises” at the ends of the chapters. These are comparatively straightforward exercises for the reader wishing additional review of the material. There are, in all, close to 300 exercises.

There is a brief appendix dealing with some topics from logic, such as truth tables and quantifiers. This appendix also contains an example of how one might discover a proof.

At the end of this text there is an annotated list of books recommended for further study. In fact it includes diverse books for several further studies in a variety of directions. Those wishing to track down the source of particular results or historical points are referred to the books on the list that provide specific citations.

There are two stylistic matters that require mention. The end of a proof is marked by a reversed turnstile (-). This device is due to C. C. Chang and H. J. Keisler. In definitions, I generally pass up the traditionally correct “if” in favor of the logically correct “iff” (meaning “if and only if”).

Two preliminary editions of the text have been used in my courses at UCLA. I would be pleased to receive comments and corrections from further users of the book.

# LIST OF SYMBOLS

The number indicates the page on which the symbol first occurs in the text or the page on which it is defined.

<table><tr><td>Symbol</td><td>Page</td><td>Symbol</td><td>Page</td><td>Symbol</td><td>Page</td></tr><tr><td> $\in$ </td><td>1</td><td>or</td><td>13</td><td> $\bigcap_{X \in \mathcal{A}}$ </td><td>32</td></tr><tr><td> $\notin$ </td><td>1</td><td> $\Rightarrow$ </td><td>13</td><td> $\langle x, y \rangle$ </td><td>35</td></tr><tr><td> $\{, \}$ </td><td>1</td><td> $\Leftrightarrow$ </td><td>13</td><td> $A \times B$ </td><td>37</td></tr><tr><td>=</td><td>2</td><td>ZF</td><td>15</td><td> $xRy$ </td><td>40</td></tr><tr><td>iff</td><td>2</td><td>VNB</td><td>15</td><td> $I_S$ </td><td>40</td></tr><tr><td> $\emptyset$ </td><td>2</td><td>GB</td><td>15</td><td>dom</td><td>40</td></tr><tr><td> $\cup$ </td><td>3</td><td> $\{x \in c \mid \_\}$ </td><td>21</td><td>ran</td><td>40</td></tr><tr><td> $\cap$ </td><td>3</td><td> $A - B$ </td><td>21</td><td>fld</td><td>40</td></tr><tr><td> $\subseteq$ </td><td>3</td><td> $\omega$ </td><td>21</td><td> $\langle x, y, z \rangle$ </td><td>41</td></tr><tr><td> $\mathcal{P}$ </td><td>4</td><td> $\vdash$ </td><td>22</td><td> $\langle x \rangle$ </td><td>42</td></tr><tr><td> $\{x \mid \_\}$ </td><td>4</td><td> $\bigcup$ </td><td>23</td><td> $F(x)$ </td><td>43</td></tr><tr><td> $V_a$ </td><td>7</td><td> $\bigcap$ </td><td>25</td><td> $F: A \to B$ </td><td>43</td></tr><tr><td> $\forall$ </td><td>13</td><td> $A \setminus B$ </td><td>27</td><td> $F^{-1}$ </td><td>44</td></tr><tr><td> $\exists$ </td><td>13</td><td> $\mathbb{R}$ </td><td>27</td><td> $F \circ G$ </td><td>44</td></tr><tr><td> $\neg$ </td><td>13</td><td> $-A$ </td><td>28</td><td> $F \upharpoonright A$ </td><td>44</td></tr><tr><td>&amp; $[x, y]$ </td><td>1344</td><td> $\bigcup_{X \in \mathcal{A}}$  $<_{z}$ </td><td>3298</td><td> $F[[A]]$ E</td><td>44182</td></tr><tr><td> $\bigcup_{i \in I}$ </td><td>51</td><td> $\mathbb{Q}$ </td><td>102</td><td> $\cong$ </td><td>184</td></tr><tr><td> $\bigcap_{i \in I}$ </td><td>51</td><td> $0_{Q}$ </td><td>102</td><td> $<_{L}$ </td><td>185</td></tr><tr><td> $F_{i}$ </td><td>51</td><td> $1_{Q}$ </td><td>102</td><td> $<^{\circ}$ </td><td>189</td></tr><tr><td> $^{A}B$ </td><td>52</td><td> $+_{Q}$ </td><td>103</td><td> $\Omega$ </td><td>194</td></tr><tr><td> $X_{i \in I}$ </td><td>54</td><td> $\dot{Q}$ </td><td>105</td><td> $\aleph_{1}$ </td><td>199</td></tr><tr><td> $[x]_{R}$ </td><td>57</td><td> $r^{-1}$ </td><td>107</td><td> $V_{\alpha}$ </td><td>200</td></tr><tr><td> $[x]$ </td><td>57</td><td> $s \div r$ </td><td>107</td><td>rank S</td><td>204</td></tr><tr><td>A/R</td><td>58</td><td> $<_{Q}$ </td><td>108</td><td> $\aleph_{\alpha}$ </td><td>212</td></tr><tr><td>0</td><td>67</td><td> $|r|$ </td><td>109</td><td> $\beth_{\alpha}$ </td><td>214</td></tr><tr><td>1</td><td>67</td><td> $\mathbb{R}$ </td><td>113</td><td>sup S</td><td>216</td></tr><tr><td>2</td><td>67</td><td> $<_{R}$ </td><td>113</td><td>it  $\langle A, R \rangle$ </td><td>220</td></tr><tr><td>3</td><td>67</td><td> $+_{R}$ </td><td>114</td><td>kard S</td><td>222</td></tr><tr><td> $a^{+}$ </td><td>68</td><td> $0_{R}$ </td><td>115</td><td> $\oplus$ </td><td>222</td></tr><tr><td> $\omega$ </td><td>69</td><td> $-x$ </td><td>117</td><td> $\rho + \sigma$ </td><td>222</td></tr><tr><td> $\sigma$ </td><td>71</td><td> $|x|$ </td><td>118</td><td> $\bar{\alpha}$ </td><td>223</td></tr><tr><td> $\mathbb{Z}$ </td><td>75</td><td> $\dot{R}$ </td><td>118</td><td> $\eta$ </td><td>223</td></tr><tr><td> $m + n$ </td><td>79</td><td> $1_{R}$ </td><td>119</td><td> $\rho^{*}$ </td><td>224</td></tr><tr><td>A1</td><td>79</td><td> $\approx$ </td><td>129</td><td> $R * S$ </td><td>224</td></tr><tr><td>A2</td><td>79</td><td> $(x, y)$ </td><td>130</td><td> $\rho \cdot \sigma$ </td><td>224</td></tr><tr><td> $m \cdot n$ </td><td>80</td><td>card S</td><td>136</td><td> $\alpha + \beta$ </td><td>228</td></tr><tr><td>M1</td><td>80</td><td> $\aleph_{0}$ </td><td>137</td><td> $\alpha \cdot \beta$ </td><td>228</td></tr><tr><td>M2</td><td>80</td><td> $\kappa + \lambda$ </td><td>139</td><td> $<_{H}$ </td><td>228</td></tr><tr><td> $m^{n}$ </td><td>80</td><td> $\kappa \cdot \lambda$ </td><td>139</td><td>A3</td><td>229</td></tr><tr><td>E1</td><td>80</td><td> $\kappa^{\lambda}$ </td><td>139</td><td>M3</td><td>229</td></tr><tr><td>E2</td><td>80</td><td> $\kappa!$ </td><td>144</td><td> $\alpha^{\beta}$ </td><td>232</td></tr><tr><td> $\Xi$ </td><td>83</td><td> $\preccurlyeq$ </td><td>145</td><td>E3</td><td>232</td></tr><tr><td> $\epsilon_{S}$ </td><td>83</td><td> $\kappa \leq \lambda$ </td><td>145</td><td> $\varepsilon_{0}$ </td><td>240</td></tr><tr><td> $\subset$ </td><td>85</td><td> $\kappa < \lambda$ </td><td>146</td><td> $R^{t}$ </td><td>243</td></tr><tr><td> $\mathbb{Z}$ </td><td>91</td><td> $\text{Sq}(A)$ </td><td>160</td><td> $\sigma^{M}$ </td><td>249</td></tr><tr><td> $+_{z}$ </td><td>92</td><td> $\subset_{S}$ </td><td>167</td><td>ZFC</td><td>253</td></tr><tr><td> $0_{z}$ </td><td>92</td><td> $\leq$ </td><td>168</td><td>HF</td><td>256</td></tr><tr><td> $-a$ </td><td>95</td><td>seg</td><td>173</td><td>cf  $\lambda$ </td><td>257</td></tr><tr><td> $\dot{z}$ </td><td>95</td><td> $<^{A}B$ </td><td>175</td><td>ssup S</td><td>262</td></tr><tr><td> $1_{z}$ </td><td>97</td><td>TC S</td><td>178</td><td> $^{1}\varphi^{1}$ </td><td>263</td></tr></table>

# INTRODUCTION

## BABY SET THEORY

We shall begin with an informal discussion of some basic concepts of set theory. In these days of the “new math,” much of this material will be already familiar to you. Indeed, the practice of beginning each mathematics course with a discussion of set theory has become widespread, extending even to the elementary schools. But we want to review here elementary-school set theory (and do it in our notation). Along the way we shall be able to point out some matters that will become important later. We shall not, in these early sections, be particularly concerned with rigor. The more serious work will start in Chapter 2.

A set is a collection of things (called its members or elements), the collection being regarded as a single object. We write “ $t \in A$ ” to say that t is a member of A, and we write “ $t \notin A$ ” to say that t is not a member of A.

For example, there is the set whose members are exactly the prime numbers less than 10. This set has four elements, the numbers 2, 3, 5, and 7. We can name the set conveniently by listing the members within braces (curly brackets):

Call this set $A$ . And let $B$ be the set of all solutions to the polynomial equation

$$
x ^ {4} - 1 7 x ^ {3} + 1 0 1 x ^ {2} - 2 4 7 x + 2 1 0 = 0.
$$

Now it turns out (as the industrious reader can verify) that the set B has exactly the same four members, 2, 3, 5, and 7. For this reason A and B are the same set, i.e., A = B. It matters not that A and B were defined in different ways. Because they have exactly the same elements, they are equal; that is, they are one and the same set. We can formulate the general principle:

Principle of Extensionality If two sets have exactly the same members, then they are equal.

Here and elsewhere, we can state things more concisely and less ambiguously by utilizing a modest amount of symbolic notation. Also we abbreviate the phrase “if and only if” as “iff.” Thus we have the restatement:

Principle of Extensionality If $A$ and $B$ are sets such that for every object $t$ ,

$$
t \in A \quad \text { iff } \quad t \in B,
$$

then A = B.

For example, the set of primes less than 10 is the same as the set of solutions to the equation $x^{4}-17x^{3}+101x^{2}-247x+210=0$ . And the set $\{2\}$ whose only member is the number 2 is the same as the set of even primes.

Incidentally, we write “A = B” to mean that A and B are the same object. That is, the expression “A” on the left of the equality symbol names the same object as does the expression “B” on the right. If A = B, then automatically (i.e., by logic) anything that is true of the object A is also true of the object B (it being the same object). For example, if A = B, then it is automatically true that for any object t, $t \in A$ iff $t \in B$ . (This is the converse to the principle of extensionality.) As usual, we write “A ≠ B” to mean that it is not true that A = B.

A small set would be a set $\{0\}$ having only one member, the number 0. An even smaller set is the empty set $\varnothing$ . The set $\varnothing$ has no members at all. Furthermore it is the only set with no members, since extensionality tells us that any two such sets must coincide. It might be thought at first that the empty set would be a rather useless or even frivolous set to mention, but, in fact, from the empty set by various set-theoretic operations a surprising array of sets will be constructed.

For any objects $x$ and $y$ , we can form the pair set $\{x, y\}$ having just the members $x$ and $y$ . Observe that $\{x, y\} = \{y, x\}$ , as both sets have exactly the same members. As a special case we have (when $x = y$ ) the set $\{x, x\} = \{x\}$ .

For example, we can form the set $\{\varnothing\}$ whose only member is $\varnothing$ . Note that $\{\varnothing\} \neq \varnothing$ , because $\varnothing \in \{\varnothing\}$ but $\varnothing \notin \varnothing$ . The fact that $\{\varnothing\} \neq \varnothing$ is reflected in the fact that a man with an empty container is better off than a man with nothing—at least he has the container. Also we can form $\{\{\varnothing\}\}, \{\{\{\varnothing\}\}\}$ , and so forth, all of which are distinct (Exercise 2).

Similarly for any objects $x, y$ , and $z$ we can form the set $\{x, y, z\}$ . More generally, we have the set $\{x_1, \ldots, x_n\}$ whose members are exactly the objects $x_1, \ldots, x_n$ . For example,

$$
\{\varnothing , \{\varnothing \}, \{\{\varnothing \} \} \}
$$

is a three-element set.

![](images/7241bd75104ec8b5ef9b49eefe7fe477e8c232d00e653a68d79887ea4c94f87a.jpg)  
(a)

![](images/eea9ed276c26651e8f1814aac3b55750a150bc470942b4f1e4214f68b388afd5.jpg)  
(b)  
Fig. 1. The shaded areas represent (a) $A \cup B$ and (b) $A \cap B$ .

Two other familiar operations on sets are union and intersection. The union of sets A and B is the set $A \cup B$ of all things that are members of A or B (or both). Similarly the intersection of A and B is the set $A \cap B$ of all things that are members of both A and B. For example,

$$
\{x, y \} \cup \{z \} = \{x, y, z \}
$$

and

$$
\{2, 3, 5, 7 \} \cap \{1, 2, 3, 4 \} = \{2, 3 \}.
$$

Figure 1 gives the usual pictures illustrating these operations. Sets A and B are said to be disjoint when they have no common members, i.e., when $A \cap B = \varnothing$ .

A set A is said to be a subset of a set B (written $A \subseteq B$ ) iff all the members of A are also members of B. Note that any set is a subset of itself. At the other extreme, $\varnothing$ is a subset of every set. This fact (that $\varnothing \subseteq A$ for any A) is “vacuously true,” since the task of verifying, for every member of $\varnothing$ , that it also belongs to A, requires doing nothing at all.

If $A \subseteq B$ , then we also say that $A$ is included in $B$ or that $B$ includes $A$ . The inclusion relation $(\subseteq)$ is not to be confused with the membership relation (∈). If we want to know whether $A \in B$ , we look at the set A as a single object, and we check to see if this single object is among the members of B. By contrast, if we want to know whether $A \subseteq B$ , then we must open up the set A, examine its various members, and check whether its various members can be found among the members of B.

Examples 1. $\varnothing \subseteq \varnothing$ , but $\varnothing \notin \varnothing$ .

2. $\{\varnothing\} \in \{\{\varnothing\}\}$ but $\{\varnothing\} \not\subseteq \{\{\varnothing\}\}$ . $\{\varnothing\}$ is not a subset of $\{\{\varnothing\}\}$ because there is a member of $\{\varnothing\}$ , namely $\varnothing$ , that is not a member of $\{\{\varnothing\}\}$ .

3. Let Us be the set of all people in the United States, and let Un be the set of all countries belonging to the United Nations. Then

$$
\text {   John   Jones   } \in U s \in U n.
$$

But John Jones $\notin$ Un (since he is not even a country), and hence $Us \not\subseteq Un$ .

Any set A will have one or more subsets. (In fact, if A has n elements, then A has $2^{n}$ subsets. But this is a matter we will take up much later.) We can gather all of the subsets of A into one collection. We then have the set of all subsets of A, called the power $^{1}$ set PA of A. For example,

$$
\begin{array}{c} \mathcal {P} \emptyset = \{\emptyset \}, \\ \mathcal {P} \{\emptyset \} = \{\emptyset , \{\emptyset \} \}, \\ \mathcal {P} \{0, 1 \} = \{\emptyset , \{0 \}, \{1 \}, \{0, 1 \} \}. \end{array}
$$

A very flexible way of naming a set is the method of abstraction. In this method we specify a set by giving the condition—the entrance requirement—that an object must satisfy in order to belong to the set. In this way we obtain the set of all objects x such that x meets the entrance requirement. The notation used for the set of all objects x such that the condition \_x\_ holds is

$$
\{x \mid \_ x \_ \}.
$$

For example:

1. PA is the set of all objects x such that x is a subset of A. Here “x is a subset of A” is the entrance requirement that x must satisfy in order to belong to PA. We can write

$$
\begin{array}{r l} \mathcal {P} A & = \{x \mid x \text {   is   a   subset   of   } A \} \\ & = \{x \mid x \subseteq A \}. \end{array}
$$

2. $A \cap B$ is the set of all objects $y$ such that $y \in A$ and $y \in B$ . We can write

$$
A \cap B = \{y \mid y \in A \text {   and   } y \in B \}.
$$

It is unimportant whether we use “x” or “y” or another letter as the symbol (which is used as a pronoun) here.

3. The set $\{z \mid z \neq z\}$ equals $\varnothing$ , because the entrance requirement “ $z \neq z$ ” is not satisfied by any object z.

4. The set $\{n \mid n$ is an even prime number $\}$ is the same as the set $\{2\}$ .

There are, however, some dangers inherent in the abstraction method. For certain bizarre choices of the entrance requirement, it may happen that there is no set containing exactly those objects meeting the entrance requirement. There are two ways in which disaster can strike.

One of the potential disasters is illustrated by

$\{x \mid x \text{ is a positive integer definable in one line of type}\}.$

The tricky word here is “definable.” Some numbers are easy to define in one line. For example, the following lines each serve to define a positive integer:

12,317,

the millionth prime number,

the least number of the form $2^{2^n} + 1$ that is not prime,

the 23rd perfect $^{2}$ number.

Observe that there are only finitely many possible lines of type (because there are only finitely many symbols available to the printer, and there is a limit to how many symbols will fit on a line). Consequently

$\{x \mid x$ is a positive integer definable in one line of type\}

is only a finite set of integers. Consider the least positive integer not in this set; that is, consider

the least positive integer not definable in one line of type.

The preceding line defines a positive integer in one line, but that number is, by its construction, not definable in one line! So we are in trouble, and the trouble can be blamed on the entrance requirement of the set, i.e., on the phrase “is a positive integer definable in one line of type.” While it may have appeared originally to be a meaningful entrance requirement, it now appears to be gravely defective. (This example was given by G. G. Berry in 1906. A related example was published in 1905 by Jules Richard.)

There is a second disaster that can result from an overly free-swinging use of the abstraction method. It is exemplified by

$$
\{x \mid x \notin x \},
$$

this is, by the set of all objects that are not members of themselves. Call this set A, and ask “is A a member of itself?” If $A \notin A$ , then A meets the entrance requirement for A, whereupon $A \in A$ . But on the other hand, if $A \in A$ , then A fails to meet the entrance requirement and so $A \notin A$ . Thus both “ $A \in A$ ” and “ $A \notin A$ ” are untenable. Again, we are in trouble. The phrase “is not a member of itself” appears to be an illegal entrance requirement for the abstraction method. (This example is known as Russell’s paradox. It was communicated by Bertrand Russell in 1902 to Gottlob Frege, and was published in 1903. The example was independently discovered by Ernst Zermelo.)

These two sorts of disaster will be blocked in precise ways in our axiomatic treatment, and less formally in our nonaxiomatic treatment. The first sort of disaster (the Berry example) will be avoided by adherence to entrance requirements that can be stated in a totally unambiguous form, to be specified in the next chapter. The second sort of disaster will be avoided by the distinction between sets and classes. Any collection of sets will be a class. Some collections of sets (such as the collections $\varnothing$ and $\{\varnothing\}$ ) will be sets. But some collections of sets (such as the collection of all sets not members of themselves) will be too large to allow as sets. These oversize collections will be called proper classes. The distinction will be discussed further presently.

In practice, avoidance of disaster will not really be an oppressive or onerous task. We will merely avoid ambiguity and avoid sweepingly vast sets. A prudent person would not want to do otherwise.

## Exercises

1. Which of the following become true when “∈” is inserted in place of the blank? Which become true when “⊆” is inserted?

(a) $\{\varnothing\} - \{\varnothing, \{\varnothing\}\}$ .

(b) $\{\varnothing\} - \{\varnothing, \{\{\varnothing\}\}\}$ .

(c) $\{\{\varnothing\}\}-\{\varnothing,\{\varnothing\}\}$ .

(d) {{∅}} — {∅, {{∅}}}

(e) $\{\{\varnothing\}\}-\{\varnothing,\{\varnothing,\{\varnothing\}\}\}$ .

2. Show that no two of the three sets $\varnothing, \{\varnothing\}$ , and $\{\{\varnothing\}\}$ are equal to each other.

3. Show that if $B \subseteq C$ , then $\mathcal{P}B \subseteq \mathcal{P}C$ .

4. Assume that $x$ and $y$ are members of a set $B$ . Show that $\{\{x\}, \{x, y\}\} \in \mathcal{P}\mathcal{P}B$ .

## SETS—AN INFORMAL VIEW

We are about to present a somewhat vague description of how sets are obtained. (The description will be repeated much later in precise form.) None of our later work will actually depend on this informal description, but we hope it will illuminate the motivation behind some of the things we will do.

![](images/ef14981dde2a3245f23fdc9ffc453a6b99949842fadfaadb77bb930bd6da7e17.jpg)  
Fig. 2. $V_{0}$ is the set $A$ of atoms.

First we gather together all those things that are not themselves sets but that we want to have as members of sets. Call such things atoms. For example, if we want to be able to speak of the set of all two-headed coins, then we must include all such coins in our collection of atoms. Let A be the set of all atoms; it is the first set in our description.

We now proceed to build up a hierarchy

$$
V _ {0} \subseteq V _ {1} \subseteq V _ {2} \subseteq \dots
$$

of sets. At the bottom level (in a vertical arrangement as in Fig. 2) we take $V_{0} = A$ , the set of atoms. The next level will also contain all sets of atoms:

$$
V _ {1} = V _ {0} \cup \mathscr {P} V _ {0} = A \cup \mathscr {P} A.
$$

The third level contains everything that is in a lower level, plus all sets of things from lower levels:

$$
V _ {2} = V _ {1} \cup \mathscr {P} V _ {1}.
$$

And in general

$$
V _ {n + 1} = V _ {n} \cup \mathscr {P} V _ {n}.
$$

Thus we obtain successively $V_0, V_1, V_2, \ldots$ . But even this infinite hierarchy does not include enough sets. For example, $\varnothing \in V_1, \{\varnothing\} \in V_2, \{\{\varnothing\}\} \in V_3$ , etc., but we do not yet have the infinite set

$$
\{\varnothing , \{\varnothing \}, \{\{\varnothing \} \}, \dots \}.
$$

To remedy this lack, we take the infinite union

$$
V _ {\omega} = V _ {0} \cup V _ {1} \cup \dots ,
$$

and then let $V_{\omega + 1} = V_{\omega} \cup \mathcal{P}V_{\omega}$ , and we continue. In general for any $\alpha$ ,

$$
V _ {\alpha + 1} = V _ {\alpha} \cup \mathscr {P} V _ {\alpha},
$$

and this goes on “forever.” Whenever you might think that the construction is finished, you instead take the union of all the levels obtained so far, take the power set of that union, and continue.

A better explanation of the “forever” idea must be delayed until we discuss (in Chapter 7) the “numbers” being used as subscripts in the preceding paragraphs. These are the so-called “ordinal numbers.” The ordinal numbers begin with 0, 1, 2, …; then there is the infinite number $\omega$ , then $\omega + 1$ , $\omega + 2$ , …; and this goes on “forever.”

A fundamental principle is the following: Every set appears somewhere in this hierarchy. That is, for every set $a$ there is some $\alpha$ with $a \in V_{\alpha + 1}$ . That is what the sets are; they are the members of the levels of our hierarchy.

Examples Suppose that $a$ and $b$ are sets. Say that $a \in V_{\alpha + 1}$ and $b \in V_{\beta + 1}$ and suppose that $V_{\beta + 1}$ is "higher" in the hierarchy than $V_{\alpha + 1}$ . Then both $a$ and $b$ are in $V_{\beta + 1}$ , since each level includes all lower levels. Consequently in $V_{\beta + 2}$ we have the pair set $\{a, b\}$ . On the other hand at no point do we obtain a set of all sets, i.e., a set having all sets as members. There simply is no such set.

There is one way in which we can simplify our picture. We were very indefinite about just what was in the set A of atoms. The fact of the matter is that the atoms serve no mathematically necessary purpose, so we banish them; we take $A = \varnothing$ . In so doing, we lose the ability to form sets of flowers or sets of people. But this is no cause for concern; we do not need set theory to talk about people and we do not need people in our set theory. But we definitely do want to have sets of numbers, e.g., $\{2, 3 + i\pi\}$ . Numbers do not appear at first glance to be sets. But as we shall discover (in Chapters 4 and 5), we can find sets that serve perfectly well as numbers.

Our theory then will ignore all objects that are not sets (as interesting and real as such objects may be). Instead we will concentrate just on “pure” sets that can be constructed without the use of such external objects. In

![](images/a1986616bf4a727db6295576fe61efd00b09530395cd04e39aedf1c9b5053bfb.jpg)  
Fig. 3. The ordinals are the backbone of the universe.

particular, any member of one of our sets will itself be a set, and each of its members, if any, will be a set, and so forth. (This does not produce an infinite regress, because we stop when we reach ∅.)

Now that we have banished atoms, the picture becomes narrower (Fig. 3). The construction is also simplified. We have defined $V_{\alpha + 1}$ to be $V_{\alpha} \cup \mathcal{PV}_{\alpha}$ . Now it turns out that this is the same as $A \cup \mathcal{PV}_{\alpha}$ (see Exercise 6). With $A = \emptyset$ , we have simply $V_{\alpha + 1} = \mathcal{PV}_{\alpha}$ .

## Exercises

5. Define the rank of a set $c$ to be the least $\alpha$ such that $c \subseteq V_{\alpha}$ . Compute the rank of $\{\{\varnothing\}\}$ . Compute the rank of $\{\varnothing, \{\varnothing\}, \{\varnothing, \{\varnothing\}\}\}$ .

6. We have stated that $V_{\alpha + 1} = A \cup \mathcal{P}V_{\alpha}$ . Prove this at least for $\alpha < 3$ .

7. List all the members of $V_{3}$ . List all the members of $V_{4}$ . (It is to be assumed here that there are no atoms.)

## CLASSES

There is no “set of all sets,” i.e., there is no set having all sets as members. This is in accordance with our informal image of the hierarchical way sets are constructed. Later, the nonexistence of a set of all sets will become a theorem (Theorem 2A), provable from the axioms.

Nonetheless, there is some mild inconvenience that results if we forbid ourselves even to speak of the collection of all sets. The collection cannot be a set, but what status can we give it? Basically there are two alternatives:

The Zermelo-Fraenkel alternative The collection of all sets need have no ontological status at all, and we need never speak of it. When tempted to speak of it, we can seek a rephrasing that avoids it.

The von Neumann–Bernays alternative The collection of all sets can be called a class. Similarly any other collection of sets can be called a class. In particular, any set is a class, but some classes are too large to be sets. Informally, a class A is a set if it is included in some level $V_{\alpha}$ of our hierarchy (and then is a member of $V_{\alpha+1}$ ). Otherwise it is not a set, and can never be a member of a set.

For advanced works in set theory, the Zermelo–Fraenkel alternative seems to be the better of the two. It profits from the simplicity of having to deal with only one sort of object (sets) instead of two (classes and sets). And the circumlocutions it requires (in order to avoid reference to classes that are not sets) are things to which set-theorists learn early to adapt.

For introductory works in set theory (such as this book), the choice between the two alternatives is less clear. The prohibition against mentioning any class that fails to be a set seems unnatural and possibly unfair. Desiring to have our cake and eat it too, we will proceed as follows. We officially adopt the Zermelo-Fraenkel alternative. Consequently the axioms and theorems shall make no mention of any class that is not a set. But in the expository comments, we will not hesitate to mention, say, the class of all sets if it appears helpful to do so. To avoid confusion, we will reserve upper-case sans serif letters (A, B, ...) for classes that are not guaranteed to be sets.

## AXIOMATIC METHOD

In this book we are going to state the axioms of set theory, and we are going to show that our theorems are consequences of those axioms. The great advantage of the axiomatic method is that it makes totally explicit just what our initial assumptions are.

It is sometimes said that “mathematics can be embedded in set theory.” This means that mathematical objects (such as numbers and differentiable functions) can be defined to be certain sets. And the theorems of mathematics (such as the fundamental theorem of calculus) then can be viewed as statements about sets. Furthermore, these theorems will be provable from our axioms. Hence our axioms provide a sufficient collection of assumptions for the development of the whole of mathematics—a remarkable fact. (In Chapter 5 we will consider further the procedure for embedding mathematics in set theory.)

The axiomatic method has been useful in other subjects as well as in set theory. Consider plane geometry, for example. It is quite possible to talk about lines and triangles without using axioms. But the advantages of axiomatizing geometry were seen very early in the history of the subject.

The nonaxiomatic approach to set theory is often referred to as “naive set theory,” a terminology that does not hide its bias. Historically, set theory originated in nonaxiomatic form. But the paradoxes of naive set theory (the most famous being Russell’s paradox) forced the development of axiomatic set theory, by showing that certain assumptions, apparently plausible, were inconsistent and hence totally untenable. It then became mandatory to give explicit assumptions that could be examined by skeptics for possible inconsistency. Even without the foundational crises posed by the paradoxes of naive set theory, the axiomatic approach would have been developed to cope with later controversy over the truth or falsity of certain principles, such as the axiom of choice (Chapter 6). Of course our selection of axioms will be guided by the desire to reflect as accurately as possible our informal (preaxiomatic) ideas regarding sets and classes.

It is nonetheless quite possible to study set theory from the nonaxiomatic viewpoint. We have therefore arranged the material in the book in a “two-tier” fashion. The passages dealing with axioms will henceforth be marked by a stripe in the left margin. The reader who omits such passages and reads only the unstriped material will thereby find a nonaxiomatic development of set theory. Perhaps he will at some later time wish to look at the axiomatic underpinnings. On the other hand, the reader who omits nothing will find an axiomatic development. Notice that most of the striped passages appear early in the book, primarily in the first three chapters. Later in the book the nonaxiomatic and the axiomatic approaches largely converge.

Our axiom system begins with two primitive notions, the concepts of "set" and "member." In terms of these concepts we will define others, but the primitive notions remain undefined. Instead we adopt a list of axioms concerning the primitive notions. (The axioms can be thought of as divulging partial information regarding the meaning of the primitive notions.)

Having adopted a list of axioms, we will then proceed to derive sentences that are logical consequences (or theorems) of the axioms. Here a sentence $\sigma$ is said to be a logical consequence of the axioms if any assignment of meaning to the undefined notions of set and member making the axioms true also makes $\sigma$ true.

We have earlier sketched, in an informal and sometimes vague way, what “set” and “member” are intended to mean. But for a sentence to be a logical consequence of the axioms, it must be true whatever “set” and “member” mean, provided only that the axioms are true. The sentences that appear, on the basis of our informal viewpoint, as if they ought to be true, must still be shown to be logical consequences of the axioms before being accepted as theorems. In return for adopting this restriction, we escape any drawbacks of the informality and vagueness of the nonaxiomatic viewpoint.

(There is an interesting point here concerning the foundations of mathematics. If $\sigma$ is a logical consequence of a list of axioms, is there then a finitely long proof of $\sigma$ from the axioms? The answer is affirmative, under a very reasonable definition of “proof.” This is an important result in mathematical logic. The topic is treated, among other places, in our book A Mathematical Introduction to Logic, Academic Press, 1972.)

For example, the first of our axioms is the axiom of extensionality, which is almost as follows: Whenever A and B are sets such that exactly the same things are members of one as are members of the other, then A = B. Imagine for the moment that this were our only axiom. We can then consider some of the logical consequences of this one axiom.

For a start, take the sentence: “There cannot be two different sets, each of which has no members.” This sentence is a logical consequence of extensionality, for we claim that any assignment of meaning to “set” and “member” making extensionality true also makes the above sentence true. To prove this, we argue as follows. Let A and B be any sets, each of which has no members. Then exactly the same things belong to A as to B, since none belong to either. Hence by extensionality, A = B. (The validity of this argument, while independent of the meaning of “set” or “member,” does depend on the meaning of the logical terms such as “each,” “no,” “equal,” etc.)

On the other hand, consider a simple sentence such as $\sigma$ : “There are two sets, one of which is a member of the other.” This sentence is not a logical consequence of extensionality. To see this, let the word “set” mean “a number equal to 2,” and let “member of” mean “unequal to.” Under this interpretation, extensionality is true but $\sigma$ is false. Of course we will soon add other axioms of which $\sigma$ will be a logical consequence.

## NOTATION

To denote sets we will use a variety of letters, both lowercase $(a, b, \ldots)$ , uppercase $(A, B, \ldots)$ , and even script letters and Greek letters. Where feasible, we will attempt to have the larger and fancier letters denote sets higher in our hierarchy of levels than those denoted by smaller and plainer letters. In addition, letters can be embellished with subscripts, primes, and the like. This assures us of an inexhaustible supply of symbols for sets. In other words, when it comes to naming sets, anything goes.

It will often be advantageous to exploit the symbolic notation of mathematical logic. This symbolic language, when used in judicious amounts to replace the English language, has the advantages of both conciseness (so that expressions are shorter) and preciseness (so that expressions are less ambiguous).

The following symbolic expressions will be used to abbreviate the corresponding English expressions:

$\forall x$ for every set $x$

∃x there exists a set x such that

not

& and

or or (in the sense “one or the other or both”)

$\Rightarrow$ implies ("\_\_\_\_ $\Rightarrow$ \_\_\_\_ " abbreviates "if \_\_, then \_\_")

$\Leftrightarrow$ if and only if, also abbreviated "iff"

You have probably seen these abbreviations before; they are discussed in more detail in the Appendix.

We also have available the symbols $\in$ and $= (\text{and } \notin \text{ and } \neq, \text{ although we could economize by eliminating, e.g., } "a \notin B" \text{ in favor of } "\neg a \in B").$ With all these symbols, variables $(a, b, \ldots)$ , and parentheses we could avoid the English language altogether in the statement of axioms and theorems. We will not actually do so, or at least not all at once. But the fact that we have this splendid formal language available is more than a theoretical curiosity. When we come to stating certain axioms, the formal language will be a necessity.

Notice that we read $\forall x$ as “for all sets x,” rather than “for all things x.” This is due to our decision to eliminate atoms from our theory. A result of this elimination is that everything we consider is a set; e.g., every member of a set will itself be a set.

Example The principle of extensionality can be written as

$\forall A \forall B[(A \text{ and } B \text{ have exactly the same members}) \Rightarrow A = B]$ .

Then “A and B have exactly the same members” can be written as

$$
\forall x (x \in A \Leftrightarrow x \in B)
$$

so that extensionality becomes

$$
\forall A \forall B [ \forall x (x \in A \Leftrightarrow x \in B) \Rightarrow A = B ].
$$

Example “There is a set to which nothing belongs” can be written

$$
\exists B \forall x x \notin B.
$$

These two examples constitute our first two axioms. It is not really necessary for us to state the axioms in symbolic form. But we will seize the opportunity to show how it can be done, on the grounds that the more such examples you see, the more natural the notation will become to you.

## HISTORICAL NOTES

The concept of a set is very basic and natural, and has been used in mathematical writings since ancient times. But the theory of abstract sets, as objects to be studied for their own interest, was originated largely by Georg Cantor (1845–1918). Cantor was a German mathematician, and his papers on set theory appeared primarily during the period from 1874 to 1897.

Cantor was led to the study of set theory in a very indirect way. He was studying trigonometric series (Fourier series), e.g., series of the form

$$
a _ {1} \sin x + a _ {2} \sin 2 x + a _ {3} \sin 3 x + \dots .
$$

Such series had been studied throughout the nineteenth century as solutions to differential equations representing physical problems. Cantor's work on Fourier series led him to consider more and more general sets of real numbers. In 1871 he realized that a certain operation on sets of real numbers (the operation of forming the set of limit points) could be iterated more than a finite number of times; starting with a set $P_0$ one could form $P_0, P_1, P_2, \ldots, P_\omega, P_{\omega+1}, \ldots, P_{\omega+\omega}, \ldots$ . In December of 1873 Cantor proved that the set of all real numbers could not be put into one-to-one correspondence with the integers (Theorem 6B); this result was published in 1874. In 1879 and subsequent years, he published a series of papers setting forth the general concepts of abstract sets and "transfinite numbers."

Cantor's work was well received by some of the prominent mathematicians of his day, such as Richard Dedekind. But his willingness to regard infinite sets as objects to be treated in much the same way as finite sets was bitterly attacked by others, particularly Kronecker. There was no objection to a “potential infinity” in the form of an unending process, but an “actual infinity” in the form of a completed infinite set was harder to accept.

About the turn of the century, attempts were made to present the principles of set theory as being principles of logic—as self-evident truths of deductive thought. The foremost work in this direction was done by Gottlob Frege. Frege was a German mathematician by training, who contributed to both mathematics and philosophy. In 1893 and 1903 he published a two-volume work in which he indicated how mathematics could be developed from principles that he regarded as being principles of logic. But just as the second volume was about to appear, Bertrand Russell informed Frege of a contradiction derivable from the principles (Russell's paradox).

Russell's paradox had a tremendous impact on the ideas of that time regarding the foundations of mathematics. It was not, to be sure, the first paradox to be noted in set theory. Cantor himself had observed that some collections, such as the collection of all sets, had to be regarded as “inconsistent totalities,” in contrast to the more tractable “consistent totalities,” such as the set of numbers. In this he foreshadowed the distinction between proper classes and sets, which was introduced by John von Neumann in 1925. Also in 1897, Cesare Burali-Forti had observed a paradoxical predicament in Cantor's theory of transfinite ordinal numbers. But the simplicity and the directness of Russell's paradox seemed to destroy utterly the attempt to base mathematics on the sort of set theory that Frege had proposed.

The first axiomatization of set theory was published by Ernst Zermelo in 1908. His axioms were essentially the ones we state in Chapters 2 and 4. (His Aussonderung axioms were later made more precise by Thoralf Skolem and others.) It was observed by several people that for a satisfactory theory of ordinal numbers, Zermelo's axioms required strengthening. The axiom of replacement (Chapter 7) was proposed by Abraham Fraenkel (in 1922) and others, giving rise to the list of axioms now known as the "Zermelo-Fraenkel" (ZF) axioms. The axiom of regularity or foundation (Chapter 7) was at least implicit in a 1917 paper by Dmitry Mirimanoff and was explicitly included by von Neumann in 1925.

An axiomatization admitting proper classes as legitimate objects was formulated by von Neumann in the 1925 paper just mentioned. Some of his ideas were utilized by Paul Bernays in the development of a more satisfactory axiomatization, which appeared in a series of papers published in 1937 and later years. A modification of Bernays's axioms was used by Kurt Gödel in a 1940 monograph. This approach is now known as “von Neumann–Bernays” (VNB) or “Gödel–Bernays” (GB) set theory.

The use of the symbol $\in$ (a stylized form of the Greek epsilon) to denote membership was initiated by the Italian mathematician Giuseppe Peano in 1889. It abbreviates the Greek word $\dot{\varepsilon}\sigma\tau\dot{i}$ , which means “is.” The underlying rationale is illustrated by the fact that if B is the set of all blue objects, then we write “ $x \in B$ ” in order to assert that x is blue.

Present-day research in set theory falls for the most part into two branches. One branch involves investigating the consequences of new and stronger axioms. The other branch involves the “metamathematics” of set theory, which is the study not of sets but of the workings of set theory itself: its proofs, its theorems, and its nontheorems.

# AXIOMS AND OPERATIONS

In this chapter we begin by introducing the first six of our ten axioms. Initially the axiomatization might appear to be like cumbersome machinery to accomplish simple tasks. But we trust that it will eventually prove itself to be powerful machinery for difficult tasks. Of course the axioms are not chosen at random, but must ultimately reflect our informal ideas about what sets are.

In addition to the introduction of basic concepts, this chapter provides practice in using the symbolic notation introduced in Chapter 1. Finally the chapter turns to the standard results on the algebra of sets.

## AXIOMS

The first of our axioms is the principle of extensionality.

Extensionality Axiom If two sets have exactly the same members, then they are equal:

$$
\forall A \forall B [ \forall x (x \in A \Leftrightarrow x \in B) \Rightarrow A = B ].
$$

The above symbolic rendering of extensionality is the one we developed previously. We will supply similar symbolizations for the other axioms. The more practice the better!

Next we need some axioms assuring the existence of some basic sets that were encountered informally in the preceding chapter.

Empty Set Axiom There is a set having no members:

$$
\exists B \forall x x \notin B.
$$

Pairing Axiom For any sets u and v, there is a set having as members just u and v:

$$
\forall u \forall v \exists B \forall x (x \in B \Leftrightarrow x = u \text { or } x = v).
$$

Union Axiom, Preliminary Form For any sets a and b, there is a set whose members are those sets belonging either to a or to b (or both):

$$
\forall a \forall b \exists B \forall x (x \in B \Leftrightarrow x \in a \text { or } x \in b).
$$

Power Set Axiom For any set a, there is a set whose members are exactly the subsets of a:

$$
\forall a \exists B \forall x (x \in B \Leftrightarrow x \subseteq a).
$$

Here we can, if we wish, rewrite “ $x \subseteq a$ ” in terms of the definition of $\subseteq$ :

$$
\forall t (t \in x \Rightarrow t \in a).
$$

Later we will expand this list to include

subset axioms, replacement axioms, infinity axiom, regularity axiom, choice axiom.

Also the union axiom will be restated in a stronger form. (Not all of these axioms are really necessary; some will be found to be redundant.)

The set existence axioms can now be used to justify the definition of symbols used informally in Chapter 1. First of all, we want to define the symbol “∅.”

Definition $\varnothing$ is the set having no members.

This definition bestows the name “∅” on a certain set. But when we write down such a definition there are two things of which we must be sure: We must know that there exists a set having no members, and we must know that there cannot be more than one set having no members. The empty set axiom provides the first fact, and extensionality provides the second. Without both facts the symbol “∅” would not be well defined.

Severe logical difficulties arise from introducing symbols when either there is no object for the symbol to name, or (even worse) the symbol names ambiguously more than one object.

The other set existence axioms justify the definition of the following symbols.

Definition (i) For any sets $u$ and $v$ , the pair set $\{u, v\}$ is the set whose only members are $u$ and $v$ .

(ii) For any sets $a$ and $b$ , the union $a \cup b$ is the set whose members are those sets belonging either to $a$ or to $b$ (or both).

(iii) For any set $a$ , the power set $\mathcal{P}a$ is the set whose members are exactly the subsets of $a$ .

As with the empty set, our set existence axioms assure us that the sets being named exist, and extensionality assures us that the sets being named are unique.

We can use pairing and union together to form other finite sets. First of all, given any x we have the singleton $\{x\}$ , which is defined to be $\{x, x\}$ . And given any $x_{1}, x_{2}$ , and $x_{3}$ we can define

$$
\left\{x _ {1}, x _ {2}, x _ {3} \right\} = \left\{x _ {1}, x _ {2} \right\} \cup \left\{x _ {3} \right\}.
$$

Similarly we can define $\{x_{1}, x_{2}, x_{3}, x_{4}\}$ , and so forth.

Having defined the union operation, we should accompany it by the intersection operation. But to justify the definition of intersection we need new axioms, to which we now turn. In the next few paragraphs we shall use our informal view of sets to motivate the formulation of these axioms.

Observe that our set existence axioms contain expressions like “there is a set B whose members are those sets x satisfying the condition \_\_,” where the blank is filled by some condition specifying which sets we want. In symbols this becomes

$$
\exists B \forall x (x \in B \Leftrightarrow \_).
$$

If the axiom mentions some other sets $t_{1}, \ldots, t_{k}$ , then the full version becomes

$$
\forall t _ {1} \dots \forall t _ {k} \exists B \forall x (x \in B \Leftrightarrow \_)
$$

with the blank filled by some expression involving $t_{1}, \ldots, t_{k}$ , and x. The empty set axiom is not quite in this form, but it can be rewritten as

$$
\exists B \forall x (x \in B \Leftrightarrow x \neq x),
$$

which is in the above form (with k = 0). The set B whose existence is asserted by such an axiom is (by extensionality) uniquely determined by $t_{1}, \ldots, t_{k}$ , so we can give it a name (in which the symbols $t_{1}, \ldots, t_{k}$ appear). This is just what we have done.

Now let us try to be more general and consider any sentence $\sigma$ of the form

$$
\forall t _ {1} \dots \forall t _ {k} \exists B \forall x (x \in B \Leftrightarrow \_),
$$

where the blank is filled by some expression involving at most $t_{1}, \ldots, t_{k}$ , and x. If this sentence is true, then the set B could be named by use of the abstraction notation of Chapter 1:

$$
B = \{x \mid \_ \}.
$$

The sets recently defined can be named by use of the abstraction notation:

$$
\begin{array}{c} \emptyset = \{x \mid x \neq x \}, \\ \{u, v \} = \{x \mid x = u \text {or} x = v \}, \\ a \cup b = \{x \mid x \in a \text {or} x \in b \}, \\ \mathcal {P} a = \{x \mid x \subseteq a \}. \end{array}
$$

One might be tempted to think that any sentence $\sigma$ of the form

$$
\forall t _ {1} \dots \forall t _ {k} \exists B \forall x (x \in B \Leftrightarrow \_)
$$

should be adopted as true. But this is wrong; some sentences of this form are false in our informal view of sets (Chapter 1). For example,

$$
\exists B \forall x (x \in B \Leftrightarrow x = x)
$$

is false, since it asserts the existence of a set B to which every set belongs. The most that can be said is that there is a class A (but not necessarily a set) whose members are those sets x such that \_.

$$
\mathbf {A} = \{x \mid \_ \}.
$$

In order for the class A to be a set it must be included in some level $V_{\alpha}$ of the hierarchy. In fact it is enough for A to be included in any set c, for then

$$
\mathsf {A} \subseteq c \subseteq V _ {\alpha}
$$

for some $\alpha$ , and from this it follows that $\mathbf{A} \in V_{\alpha + 1}$ .

All this is to motivate the adoption of the subset axioms. These axioms say, very roughly, that any class A included in some set c must in fact be a set. But the axioms can refer (in the Zermelo–Fraenkel alternative) only to sets. So instead of direct reference to the class A, we refer instead to the expression — that defined A.

Subset Axioms For each formula $\_\_\_$ not containing $B$ , the following is an axiom:

$$
\forall t _ {1} \dots \forall t _ {k} \forall c \exists B \forall x (x \in B \Leftrightarrow x \in c \& \_).
$$

In English, the axiom asserts (for any $t_{1}, \ldots, t_{k}$ and c) the existence of a set B whose members are exactly those sets x in c such that \_\_\_\_. It then follows automatically that B is a subset of c (whence the name “subset axiom”). The set B is uniquely determined (by $t_{1}, \ldots, t_{k}$ and c), and can be named by use of a variation on the abstraction notation:

$$
B = \{x \in c \mid \_ \}.
$$

Example One of the subset axioms is:

$$
\forall a \forall c \exists B \forall x (x \in B \Leftrightarrow x \in c \& x \in a).
$$

This axiom asserts the existence of the set we define to be the intersection $c \cap a$ of $c$ and $a$ .

We are not tied to one particular choice of letters. For example, we will also allow as a subset axiom:

$$
\forall A \forall B \exists S \forall t [ t \in S \Leftrightarrow t \in A \& t \notin B ].
$$

This set S is the relative complement of B in A, denoted A - B.

Note on Terminology The subset axioms are often known by the name Zermelo gave them, Aussonderung axioms. The word Aussonderung is German, and is formed from sonderen (to separate) and aus (out).

Example In Chapter 4 we shall construct the set $\omega$ of natural numbers:

$$
\omega = \{0, 1, 2, \dots \}.
$$

We will then be able to use the subset axioms to form the set of even numbers and the set of primes:

$$
\{x \in \omega \mid x \text {   is   even } \} \quad \text { and } \quad \{y \in \omega \mid y \text {   is   prime } \}.
$$

(But to do this we must be able to express “x is even” by means of a legal formula; we will return to this point shortly.)

Example Let s be some set. Then there is a set Q whose members are the one-element subsets of s:

$$
Q = \{a \in \mathscr {P} s \mid a \text {   is   a   one - element   subset   of   } s \}.
$$

We can now use the argument of Russell's paradox to show that the class $\mathsf{V}$ of all sets is not itself a set.

Theorem 2A There is no set to which every set belongs.

Proof Let A be a set; we will construct a set not belonging to A. Let

$$
B = \{x \in A \mid x \notin x \}.
$$

We claim that $B \notin A$ . We have, by the construction of B,

$$
B \in B \Leftrightarrow B \in A \& B \notin B.
$$

If $B \in A$ , then this reduces to

$$
B \in B \Leftrightarrow B \notin B,
$$

which is impossible, since one side must be true and the other false. Hence $B \notin A$ .

One might ask whether a set can ever be a member of itself. We will argue much later (in Chapter 7) that it cannot. And consequently in the preceding proof, the set B is actually the same as the set A.

At this point we need to say just what a formula is. After all, it would be most unfortunate to have as one of the subset axioms

$\exists B \forall x (x \in B \Leftrightarrow x \in \omega \& x$ is an integer definable in one line of type).

We are saved from this disaster by our logical symbols. By insisting that the formula be expressible in the formal language these symbols give us, we can eliminate “x is an integer definable in one line of type” from the list of possible formulas. (Moral: Those symbols are your friends!)

The simplest formulas are expressions such as

$$
a \in B \quad \text { and } \quad a = b
$$

(and similarly with other letters). More complicated formulas can then be built up from these by use of the expressions

$$
\forall x, \exists x, \neg , \ & , \text { or }, \Rightarrow , \Leftrightarrow ,
$$

together with enough parentheses to avoid ambiguity. That is, from formulas $\varphi$ and $\psi$ we can construct longer formulas $\forall x\varphi$ , $\exists x\varphi$ (and similarly $\forall y\varphi$ , etc.), $(\neg \varphi)$ , $(\varphi \& \psi)$ , $(\varphi$ or $\psi)$ , $(\varphi \Rightarrow \psi)$ , and $(\varphi \Leftrightarrow \psi)$ . We define a formula to be a string of symbols constructed from the simplest formulas by use of the above-listed methods. For example,

$$
\exists x (x \in A \& \forall t (t \in x. \Rightarrow (\neg t \in A)))
$$

is a formula. In practice, however, we are likely to abbreviate it by something a little more readable, such as

$$
(\exists x \in A) (\forall t \in x) t \notin A.
$$

An ungrammatical string of symbols such as )) $\Rightarrow A$ is not a formula, nor is

x is an integer definable in one line of type.

Example Let s be some set. In a previous example we formed the set of one-element subsets of s:

$$
\{a \in \mathcal {P} s \mid a \text {   is   a   one - element   subset   of   } s \}.
$$

Now “a is a one-element subset of s” is not itself a formula, but it can be rewritten as a formula. As a first step, it can be expressed as

$a \subseteq s \& a \neq \emptyset \& \text{ any two members of } a \text{ coincide.}$

This in turn becomes the formula

$$
((\forall x (x \in a \Rightarrow x \in s) \& \exists y y \in a) \& \forall u \forall v ((u \in a \& v \in a) \Rightarrow u = v)).
$$

In applications of subset axioms we generally will not write out the formula itself. And this example shows why; “a is a one-element subset of s” is much easier to read than the legal formula. But in every case it will be possible (for a person with unbounded patience) to eliminate the English words and the defined symbols (such as $\varnothing$ , $\cup$ , and so forth) in order to arrive at a legal formula. The procedure for eliminating defined symbols is discussed further in the Appendix.

## ARBITRARY UNIONS AND INTERSECTIONS

The union operation previously described allows us to form the union $a \cup b$ of two sets. By repeating the operation, we can form the union of three sets or the union of forty sets. But suppose we want the union of infinitely many sets; suppose we have an infinite collection of sets

$$
A = \{b _ {0}, b _ {1}, b _ {2}, \dots \}
$$

and we want to take the union of all the $b_{i}$ 's. For this we need a more general union operation:

$$
\begin{array}{r l} \bigcup A & = \bigcup_ {i} b _ {i} \\ & = \{x \mid x \text {   belongs   to   some   member   } b _ {i} \text {   of   } A \}. \end{array}
$$

This leads us to make the following definition. For any set $A$ , the union $\bigcup A$ of $A$ is the set defined by

$$
\begin{array}{r l} \bigcup A & = \{x \mid x \text {   belongs   to   some   member   of   } A \} \\ & = \{x \mid (\exists b \in A) x \in b \}. \end{array}
$$

Thus $\bigcup A$ is a melting pot into which all members of A are dumped. For example, suppose Un is (as on p. 4) the set of countries belonging to the United Nations. Then $\bigcup Un$ is the set of all people that are citizens of some country belonging to the United Nations. A smaller example (and one that avoids sets of people) is

$$
\bigcup \{\{2, 4, 6 \}, \{6, 1 6, 2 6 \}, \{0 \} \}.
$$

You should evaluate this expression to make certain that you understand the union operation. If you do it correctly, you will end up with a set of six numbers.

We need an improved version of the union axiom in order to know that a set exists containing the members of the members of A.

Union Axiom For any set A, there exists a set B whose elements are exactly the members of the members of A:

$$
\forall x [ x \in B \Leftrightarrow (\exists b \in A) x \in b ].
$$

We can state the definition of $\bigcup A$ in the following form:

$$
x \in \bigcup A \Leftrightarrow (\exists b \in A) x \in b.
$$

For example,

$$
\begin{array}{r l} \bigcup \{a, b \} & = \{x \mid x \text { belongs   to   some   member   of } \{a, b \} \} \\ & = \{x \mid x \text { belongs   to } a \text { or   to } b \} \\ & = a \cup b. \end{array}
$$

This example shows that our preliminary form of the union axiom can be discarded in favor of the new form. That is, the set $a \cup b$ produced by the preliminary form can also be obtained from pairing and the revised form of the union axiom.

Similarly we have

$$
\bigcup \{a, b, c, d \} = a \cup b \cup c \cup d \quad \text { and } \quad \bigcup \{a \} = a.
$$

An extreme case is $\bigcup \varnothing = \varnothing$ .

We also want a corresponding generalization of the intersection operation. Suppose we want to take the intersection of infinitely many sets $b_{0}, b_{1}, \ldots$ . Then where

$$
A = \left\{b _ {0}, b _ {1}, \dots \right\}
$$

the desired intersection can be informally characterized as

$$
\begin{array}{l} \bigcap A = \bigcap_ {i} b _ {i} \\ \qquad = \{x \mid x \text {   belongs   to   every   } b _ {i} \text {   in   } A \}. \end{array}
$$

In general, we define for every nonempty set $A$ , the intersection $\bigcap A$ of $A$ by the condition

$$
x \in \bigcap A \Leftrightarrow x \text {   belongs   to   every   member   of   } A.
$$

In contrast to the union operation, no special axiom is needed to justify the intersection operation. Instead we have the following theorem.

Theorem 2B For any nonempty set $A$ , there exists a unique set $B$ such that for any $x$ ,

$$
x \in B \Leftrightarrow x \text {   belongs   to   every   member   of   } A.
$$

This theorem permits defining $\bigcap A$ to be that unique set $B$ .

Proof We are given that A is nonempty; let c be some fixed member of A. Then by a subset axiom there is a set B such that for any x,

$$
\begin{array}{r c l} x \in B & \Leftrightarrow & x \in c \& x \text { belongs   to   every   other   member   of } A \\ & \Leftrightarrow & x \text { belongs   to   every   member   of } A. \end{array}
$$

Uniqueness, as always, follows from extensionality.

Examples

$$
\bigcap \{\{1, 2, 8 \}, \{2, 8 \}, \{4, 8 \} \} = \{8 \},
$$

$$
\bigcup \{\{1, 2, 8 \}, \{2, 8 \}, \{4, 8 \} \} = \{1, 2, 4, 8 \}.
$$

Examples

$$
\begin{array}{c} \bigcap \{a \} = a, \\ \bigcap \{a, b \} = a \cap b, \\ \bigcap \{a, b, c \} = a \cap b \cap c. \end{array}
$$

In these last examples, as A becomes larger, $\bigcap A$ gets smaller. More precisely: Whenever $A \subseteq B$ , then $\bigcap B \subseteq \bigcap A$ . There is one troublesome extreme case. What happens if $A = \varnothing$ ? For any x at all, it is vacuously true that x belongs to every member of $\varnothing$ . (There can be no member of $\varnothing$ to which x fails to belong.) Thus it looks as if $\bigcap \varnothing$ should be the class V of all sets. By Theorem 2A, there is no set C such that for all x,

$$
x \in C \Leftrightarrow x \text {   belongs   to   every   member   of   } \varnothing
$$

since the right side is true of every x. This presents a mild notational problem: How do we define $\bigcap\varnothing$ ? The situation is analogous to division by zero in arithmetic. How does one define $a \div 0$ ? One option is to leave $\bigcap\varnothing$ undefined, since there is no very satisfactory way of defining it. This option works perfectly well, but some logicians dislike it. It leaves $\bigcap\varnothing$ as an untidy loose end, which they may later trip over. The other option is to select some arbitrary scapegoat (the set $\varnothing$ is always used for this) and define $\bigcap\varnothing$ to equal that object. Either way, whenever one forms $\bigcap A$ one must beware the possibility that perhaps $A = \varnothing$ . Since it makes no difference which of the two options one follows, we will not bother to make a choice between them at all.

Example If $b \in A$ , then $b \subseteq \bigcup A$ .

Example If $\{\{x\}, \{x, y\}\} \in A$ , then $\{x, y\} \in \bigcup A$ , $x \in \bigcup \bigcup A$ , and $y \in \bigcup \bigcup A$ .

Example $\bigcap \{\{a\}, \{a, b\}\} = \{a\} \cap \{a, b\} = \{a\}$ . Hence

$$
\bigcup \bigcap \{\{a \}, \{a, b \} \} = \bigcup \{a \} = a.
$$

On the other hand,

$$
\bigcap \bigcup \{\{a \}, \{a, b \} \} = \bigcap \{a, b \} = a \cap b.
$$

## Exercises

See also the Review Exercises at the end of this chapter.

1. Assume that $A$ is the set of integers divisible by 4. Similarly assume that $B$ and $C$ are the sets of integers divisible by 9 and 10, respectively. What is in $A \cap B \cap C$ ?

2. Give an example of sets $A$ and $B$ for which $\bigcup A = \bigcup B$ but $A \neq B$ .

3. Show that every member of a set $A$ is a subset of $\bigcup A$ . (This was stated as an example in this section.)

4. Show that if $A \subseteq B$ , then $\bigcup A \subseteq \bigcup B$ .

5. Assume that every member of $\mathcal{A}$ is a subset of $B$ . Show that $\bigcup \mathcal{A} \subseteq B$ .

6. (a) Show that for any set $A, \bigcup \mathcal{P}A = A$ .

(b) Show that $A \subseteq \mathcal{P} \bigcup A$ . Under what conditions does equality hold?

7. (a) Show that for any sets $A$ and $B$ ,

$$
\mathcal {P} A \cap \mathcal {P} B = \mathcal {P} (A \cap B).
$$

(b) Show that $\mathcal{P}A\cup \mathcal{P}B\subseteq \mathcal{P}(A\cup B)$ . Under what conditions does equality hold?

8. Show that there is no set to which every singleton (that is, every set of the form $\{x\}$ ) belongs. [Suggestion: Show that from such a set, we could construct a set to which every set belonged.]

9. Give an example of sets a and B for which $a \in B$ but $Pa \notin PB$ .

10. Show that if $a \in B$ , then $\mathcal{P}a \in \mathcal{PP} \cup B$ . [Suggestion: If you need help, look in the Appendix.]

## ALGEBRA OF SETS

Two basic operations on sets are the operations of union and intersection:

$$
A \cup B = \{x \mid x \in A \text {   or   } x \in B \},
$$

$$
A \cap B = \{x \mid x \in A \& x \in B \}.
$$

Also we have for any sets A and B the relative complement A - B of B in A:

$$
A - B = \{x \in A \mid x \notin B \}.
$$

The usual diagram for $A - B$ is shown in Fig. 4. In some books the minus sign is needed for other uses, and the relative complement is then denoted $A \setminus B$ .

![](images/af07565e1182f2144fe4542855ac9923b2277067b7ab2b06ea9f00fffc2f4451.jpg)  
Fig. 4. The shaded area represents A - B.

The union axiom was used to give us $A \cup B$ . But $A \cap B$ and A - B were both obtained from subset axioms.

We cannot form (as a set) the “absolute complement” of B, i.e., $\{x \mid x \notin B\}$ . This class fails to be a set, for its union with B would be the class of all sets. In any event, the absolute complement is unlikely to be an interesting object of study.

For example, suppose one is studying sets of real numbers. Let $\mathbb{R}$ be the set of all real numbers, and suppose that $B \subseteq \mathbb{R}$ . Then the relative complement $\mathbb{R} - B$ consists of these real numbers not in $B$ . On the other hand, the absolute complement of $B$ would be a huge class containing all manner of irrelevant things; it would contain any set that was not a real number.

Example Let A be the set of all left-handed people, let B be the set of all blond people, and let C be the set of all male people. (We choose to suppress in this example, as in others, the fact that we officially banned people from our sets.) Then $A \cup (B - C)$ is the set of all people who either are left-handed or are blond nonmales (or both). On the other hand $(A \cup B) - C$ is the set of all nonmales who are either left-handed or blond. These two sets are different; Joe (who is a left-handed male) belongs to the

first set but not the second. The set

$$
(A - C) \cup (B - C)
$$

is the same as one of the two sets mentioned above. Which one?

The study of the operations of union $(\cup)$ , intersection $(\cap)$ , and relative complementation $(-)$ , together with the inclusion relation $(\subseteq)$ , goes by the name of the algebra of sets. In some ways, the algebra of sets obeys laws reminiscent of the algebra of real numbers (with +, $\cdot$ , -, and $\leq$ ), but there are significant differences.

The following identities, which hold for any sets, are some of the elementary facts of the algebra of sets.

Commutative laws

$$
A \cup B = B \cup A \quad \text { and } \quad A \cap B = B \cap A.
$$

Associative laws

$$
\begin{array}{l} A \cup (B \cup C) = (A \cup B) \cup C, \\ A \cap (B \cap C) = (A \cap B) \cap C. \end{array}
$$

Distributive laws

$$
\begin{array}{l} A \cap (B \cup C) = (A \cap B) \cup (A \cap C), \\ A \cup (B \cap C) = (A \cup B) \cap (A \cup C). \end{array}
$$

De Morgan's laws

$$
\begin{array}{l} C - (A \cup B) = (C - A) \cap (C - B), \\ C - (A \cap B) = (C - A) \cup (C - B). \end{array}
$$

Identities involving ∅

$$
\begin{array}{c} A \cup \varnothing = A \qquad \text { and } \qquad A \cap \varnothing = \varnothing , \\ A \cap (C - A) = \varnothing . \end{array}
$$

Often one considers sets, all of which are subsets of some large set or "space" S. A common example is the study of subsets of the space R of real numbers. Assume then that A and B are subsets of S. Then we can abbreviate S - A as simply -A, the set S being understood as fixed. In this abbreviation, De Morgan's laws become

$$
\begin{array}{l} - (A \cup B) = - A \cap - B, \\ - (A \cap B) = - A \cup - B. \end{array}
$$

Further, we have (still under the assumption that $A \subseteq S$ )

$$
\begin{array}{c c c} A \cup S = S & \text { and } & A \cap S = A, \\ A \cup - A = S & \text { and } & A \cap - A = \varnothing . \end{array}
$$

Now we should say something about how one proves all these facts. Let us take as a sample the distributive law:

$$
A \cap (B \cup C) = (A \cap B) \cup (A \cap C).
$$

One way to check this is to draw the picture (Fig. 5). After shading

![](images/80547eba8809a4dd96503d156d28aa1e4174260abda2975d3b48ddd63662c1fa.jpg)  
Fig. 5. Diagram for three sets.

the region representing $A \cap (B \cup C)$ and the region representing $(A \cap B) \cup (A \cap C)$ , one discovers that these regions are the same.

Is the foregoing proof, which relies on a picture, really trustworthy? Let us run through it again without the picture. To prove the desired equation, it suffices (by extensionality) to consider an arbitrary x, and to show that x belongs to $A \cap (B \cup C)$ iff it belongs to $(A \cap B) \cup (A \cap C)$ . So consider this arbitrary x. We do not know for sure whether $x \in A$ or not, whether $x \in B$ or not, etc., but we can list all eight possibilities:

$$
\begin{array}{l l l} x \in A & x \in B & x \in C \\ x \in A & x \in B & x \notin C \\ x \in A & x \notin B & x \in C \\ x \in A & x \notin B & x \notin C \\ x \notin A & x \in B & x \in C \\ x \notin A & x \in B & x \notin C \\ x \notin A & x \notin B & x \in C \\ x \notin A & x \notin B & x \notin C. \end{array}
$$

(These cases correspond to the eight regions of Fig. 5.) We can then verify that in each of the eight cases,

$$
x \in A \cap (B \cup C) \quad \text { iff } \quad x \in (A \cap B) \cup (A \cap C).
$$

For example, in the fifth case we find that

$$
x \notin A \cap (B \cup C) \quad \text { and } \quad x \notin (A \cap B) \cup (A \cap C).
$$

(What region of Fig. 5 does this case represent?) When verification for the seven other cases has been made, the proof of the equation is complete.

This method of proof is applicable to all the equations listed thus far; in fact it works for any equation or inclusion of this sort. If the equation involves n letters, then there will be $2^{n}$ cases. In the distributive law we had three letters and eight cases. But less mechanical methods of proof will be needed for some of the facts listed below.

For the inclusion relation, we have the following monotonicity properties:

$$
\begin{array}{r c l} A \subseteq B & \Rightarrow & A \cup C \subseteq B \cup C, \\ A \subseteq B & \Rightarrow & A \cap C \subseteq B \cap C, \\ A \subseteq B & \Rightarrow & \bigcup A \subseteq \bigcup B, \end{array}
$$

and the “antimonotone” results:

$$
\begin{array}{r c l} A \subseteq B & \Rightarrow & C - B \subseteq C - A, \\ \emptyset \neq A \subseteq B & \Rightarrow & \bigcap B \subseteq \bigcap A. \end{array}
$$

In each case, the proof is straightforward. For example, in the last case, we assume that every member of A is also a member of B. Hence if $x \in \bigcap B$ , i.e., if x belongs to every member of B, then a fortiori x belongs to every member of the smaller collection A. And consequently $x \in \bigcap A$ .

Next we list some more identities involving arbitrary unions and intersections.

Distributive laws

$$
\begin{array}{l} A \cup \bigcap \mathcal {B} = \bigcap \{A \cup X   |   X \in \mathcal {B} \} \quad \text { for } \quad \mathcal {B} \neq \emptyset , \\ A \cap \bigcup \mathcal {B} = \bigcup \{A \cap X   |   X \in \mathcal {B} \}. \end{array}
$$

The notation used on the right side is an extension of the abstraction notation. The set $\{A \cup X \mid X \in B\}$ (read “the set of all $A \cup X$ such that $X \in B$ ”) is the unique set D whose members are exactly the sets of the form $A \cup X$ for some X in B; i.e.,

$$
t \in \mathscr {D} \Leftrightarrow t = A \cup X \text {   for   some   } X \text {   in   } \mathscr {B}.
$$

The existence of such a set D can be proved by observing that $A \cup X \subseteq A \cup \bigcup B$ . Hence the set D we seek is a subset of $\mathcal{P}(A \cup \bigcup \mathcal{B})$ . A subset axiom produces

$$
\{t \in \mathcal {P} (A \cup \bigcup \mathcal {B}) \mid t = A \cup X \text {   for   some   } X \text {   in   } \mathcal {B} \},
$$

and this is exactly the set D.

For another example of this notation, suppose that sets A and C are under consideration. Then

$$
\{C - X \mid X \in \mathscr {A} \}
$$

is the set of relative complements of members of A, i.e., for any t,

$$
t \in \{C - X \mid X \in \mathscr {A} \} \Leftrightarrow t = C - X \quad \text { for   some } X \text { in } \mathscr {A}.
$$

Similarly, $\{\mathcal{P}X\mid X\in \mathcal{A}\}$ is the set for which

$$
t \in \{\mathcal {P} X \mid X \in \mathcal {A} \} \Leftrightarrow t = \mathcal {P} X \quad \text { for   some } X \text { in } \mathcal {A}.
$$

It is not entirely obvious that any such set can be proved to exist, but see Exercise 10.

De Morgan's laws (for $\mathcal{A} \neq \emptyset$ )

$$
\begin{array}{l} C - \bigcup \mathcal {A} = \bigcap \{C - X \mid X \in \mathcal {A} \}, \\ C - \bigcap \mathcal {A} = \bigcup \{C - X \mid X \in \mathcal {A} \}. \end{array}
$$

If $\bigcup \mathcal{A} \subseteq S$ , then these laws can be written as

$$
\begin{array}{r l} & {- \bigcup \mathcal {A} = \bigcap \{- X | X \in \mathcal {A} \},} \\ & {- \bigcap \mathcal {A} = \bigcup \{- X | X \in \mathcal {A} \},} \end{array}
$$

where it is understood that -X is S - X.

To prove, for example, that for nonempty A the equation

$$
C - \bigcup \mathscr {A} = \bigcap \{C - X \mid X \in \mathscr {A} \}
$$

holds, we can argue as follows:

$$
\begin{array}{r c l} t \in C - \bigcup \mathcal {A} & \Rightarrow & t \in C \qquad \text { but   } t \text {   belongs   to   no   member   of   } \mathcal {A} \\ & \Rightarrow & t \in C - X \qquad \text { for   every   } X \text {   in   } \mathcal {A} \\ & \Rightarrow & t \in \bigcap \{C - X \mid X \in \mathcal {A} \}. \end{array}
$$

Furthermore every step reverses, so that “ $\Rightarrow$ ” can become “ $\Leftrightarrow$ .” (A question for the alert reader: Where do we use the fact that $\mathcal{A} \neq \emptyset$ ?)

A Final Remark on Notation There is another style of writing some of the unions and intersections with which we have been working. We can write, for example,

$$
\bigcap_ {X \in \mathcal {B}} (A \cup X) \quad \text { for } \quad \bigcap \{A \cup X \mid X \in \mathcal {B} \}
$$

and

$$
\bigcup_ {X \in \mathcal {A}} (C - X) \quad \text {   for   } \quad \bigcup \{C - X \mid X \in \mathcal {A} \}.
$$

But for the most part we will stick to our original notation.

## Exercises

11. Show that for any sets $A$ and $B$ ,

$$
A = (A \cap B) \cup (A - B) \quad \text { and } \quad A \cup (B - A) = A \cup B.
$$

12. Verify the following identity (one of De Morgan's laws):

$$
C - (A \cap B) = (C - A) \cup (C - B).
$$

13. Show that if $A \subseteq B$ , then $C - B \subseteq C - A$ .

14. Show by example that for some sets $A, B$ , and $C$ , the set $A - (B - C)$ is different from $(A - B) - C$ .

15. Define the symmetric difference $A + B$ of sets $A$ and $B$ to be the set $(A - B) \cup (B - A)$ .

(a) Show that $A \cap (B + C) = (A \cap B) + (A \cap C)$ .

(b) Show that $A + (B + C) = (A + B) + C$ .

16. Simplify:

$$
[ (A \cup B \cup C) \cap (A \cup B) ] - [ (A \cup (B - C)) \cap A ].
$$

17. Show that the following four conditions are equivalent.

(a) $A \subseteq B,$ (b) A - B = ∅,

(c) $A \cup B = B,$ (d) $A \cap B = A.$

18. Assume that $A$ and $B$ are subsets of $S$ . List all of the different sets that can be made from these three by use of the binary operations $\cup, \cap,$ and $-$ .

19. Is $\mathcal{P}(A - B)$ always equal to $\mathcal{P}A - \mathcal{P}B$ ? Is it ever equal to $\mathcal{P}A - \mathcal{P}B$ ?

20. Let $A, B$ , and $C$ be sets such that $A \cup B = A \cup C$ and $A \cap B = A \cap C$ . Show that $B = C$ .

21. Show that $\bigcup (A\cup B) = \bigcup A\cup \bigcup B.$

22. Show that if $A$ and $B$ are nonempty sets, then $\bigcap (A \cup B) = \bigcap A \cap \bigcap B$ .

23. Show that if $\mathcal{B}$ is nonempty, then $A \cup \bigcap \mathcal{B} = \bigcap \{A \cup X \mid X \in \mathcal{B}\}$ .

24. (a) Show that if $\mathcal{A}$ is nonempty, then $\mathcal{P} \bigcap \mathcal{A} = \bigcap \{\mathcal{P}X \mid X \in \mathcal{A}\}$ .

(b) Show that

$$
\bigcup \{\mathcal {P} X \mid X \in \mathcal {A} \} \subseteq \mathcal {P} \bigcup \mathcal {A}.
$$

Under what conditions does equality hold?

25. Is $A \cup \bigcup \mathcal{B}$ always the same as $\bigcup \{A \cup X | X \in \mathcal{B}\}$ ? If not, then under what conditions does equality hold?

## EPILOGUE

This chapter was entitled “Axioms and Operations.” Some of the operations featured in the chapter are union, intersection, the power set axiom, and relative complementation. You should certainly know what all of these operations are and be able to work with them. You should also be able to prove various properties of the operations.

Also in this chapter we introduced six of our ten axioms. Or more accurately, we introduced five axioms and one axiom schema. (An axiom schema is an infinite bundle of axioms, such as the subset axioms.) From these axioms we can justify the definitions of the operations mentioned above. And the proofs of properties of the operations are, ultimately, proofs from our list of axioms.

## Review Exercises

26. Consider the following sets: $A = \{3, 4\}$ , $B = \{4, 3\} \cup \emptyset$ , $C = \{4, 3\} \cup \{\emptyset\}$ , $D = \{x \mid x^2 - 7x + 12 = 0\}$ , $E = \{\emptyset, 3, 4\}$ , $F = \{4, 4, 3\}$ , $G = \{4, \emptyset, \emptyset, 3\}$ . For each pair of sets (e.g., $A$ and $E$ ) specify whether or not the sets are equal.

27. Give an example of sets $A$ and $B$ for which $A \cap B$ is nonempty and

$$
\bigcap A \cap \bigcap B \neq \bigcap (A \cap B).
$$

28. Simplify:

$$
\bigcup \{\{3, 4 \}, \{\{3 \}, \{4 \} \}, \{3, \{4 \} \}, \{\{3 \}, 4 \} \}.
$$

29. Simplify:

(a) $\bigcap \{\mathcal{P}\mathcal{P}\mathcal{P}\emptyset, \mathcal{P}\mathcal{P}\emptyset, \mathcal{P}\emptyset, \emptyset\}$ .

(b) $\bigcap \{\mathcal{PP}\{\varnothing\};\mathcal{PP}\{\varnothing\},\mathcal{P}\{\varnothing\}\} .$

30. Let $A$ be the set $\{\{\emptyset\}, \{\{\emptyset\}\}\}$ . Evaluate the following:

(a) $\mathcal{P}A,$ (b) $\bigcup A,$ (c) $\mathcal{P}\bigcup A,$ (d) $\bigcup \mathcal{P}A.$

31. Let $B$ be the set $\{\{1, 2\}, \{2, 3\}, \{1, 3\}, \{\varnothing\}\}$ . Evaluate the following sets.
(a) $\bigcup B$ , (b) $\bigcap B$ , (c) $\bigcap \bigcup B$ , (d) $\bigcup \bigcap B$ .

32. Let $S$ be the set $\{\{a\}, \{a, b\}\}$ . Evaluate and simplify:
(a) $\bigcup \bigcup S$ , (b) $\bigcap \bigcap S$ , (c) $\bigcap \bigcup S \cup (\bigcup \bigcup S - \bigcup \bigcap S)$ .

33. With $S$ as in the preceding exercise, evaluate $\bigcup (\bigcup S - \bigcap S)$ when $a \neq b$ and when $a = b$ .

$$
\{\varnothing , \{\varnothing \} \} \in \mathscr {P P P S}
$$

35. Assume that $\mathcal{P}A = \mathcal{P}B$ . Prove that $A = B$ .

36. Verify that for all sets the following are correct.

(a) $A - (A \cap B) = A - B$ .

(b) $A - (A - B) = A \cap B.$

37. Show that for all sets the following equations hold.

(a) $(A\cup B) - C = (A - C)\cup (B - C).$

(b) $A - (B - C) = (A - B) \cup (A \cap C)$ .

(c) $(A - B) - C = A - (B \cup C).$

38. Prove that for all sets the following are valid.

(a) $A \subseteq C \& B \subseteq C \Leftrightarrow A \cup B \subseteq C.$

(b) $C \subseteq A \& C \subseteq B \Leftrightarrow C \subseteq A \cap B.$

# RELATIONS AND FUNCTIONS

In this chapter we introduce some concepts that are important throughout mathematics. The correct formulation (and understanding) of the definitions will be a major goal. The theorems initially will be those needed to justify the definitions, and those verifying some properties of the defined objects.

## ORDERED PAIRS

The pair set $\{1,2\}$ can be thought of as an unordered pair, since $\{1,2\}=\{2,1\}$ . We will need another object $\langle1,2\rangle$ that will encode more information: that 1 is the first component and 2 is the second. In particular, we will demand that $\langle1,2\rangle\neq\langle2,1\rangle$ .

More generally, we want to define a set $\langle x, y \rangle$ that uniquely encodes both what x and y are, and also what order they are in. In other words, if an ordered pair can be represented in two ways

$$
\langle x, y \rangle = \langle u, v \rangle ,
$$

then the representations are identical in the sense that $x = u$ and $y = v$ . And in fact any way of defining $\langle x, y \rangle$ that satisfies this property of unique decomposition will suffice. It will be instructive to consider first some examples of definitions lacking this property.

Example 1 If we define $\langle x, y \rangle_1 = \{x, y\}$ , then (as noted above), $\langle 1, 2 \rangle_1 = \langle 2, 1 \rangle_1$ .

Example 2 Let $\langle x, y \rangle_2 = \{x, \{y\}\}$ . Again the desired property fails, since $\langle \{\varnothing\}, \{\varnothing\} \rangle_2 = \langle \{\{\varnothing\}\}, \varnothing \rangle_2$ , both sides being equal to $\{\{\varnothing\}, \{\{\varnothing\}\}\}$ .

The first successful definition was given by Norbert Wiener in 1914, who proposed to let

$$
\langle x, y \rangle_ {3} = \{\{\{x \}, \emptyset \}, \{\{y \} \} \}.
$$

A simpler definition was given by Kazimierz Kuratowski in 1921, and is the definition in general use today:

Definition $\langle x, y \rangle$ is defined to be $\{\{x\}, \{x, y\}\}$ .

We must prove that this definition succeeds in capturing the desired property: The ordered pair $\langle x, y \rangle$ uniquely determines both what x and y are, and the order upon them.

Theorem 3A $\langle u, v \rangle = \langle x, y \rangle$ iff $u = x$ and $v = y$ .

Proof One direction is trivial; if $u = x$ and $v = y$ , then $\langle u, v \rangle$ is the same thing as $\langle x, y \rangle$ .

To prove the interesting direction, assume that $\langle u, v \rangle = \langle x, y \rangle$ , i.e.,

$$
\{\{u \}, \{u, v \} \} = \{\{x \}, \{x, y \} \}.
$$

Then we have

$$
\{u \} \in \{\{x \}, \{x, y \} \} \quad \text { and } \quad \{u, v \} \in \{\{x \}, \{x, y \} \}.
$$

From the first of these, we know that either

$$
\text {(a)} \quad \{u \} = \{x \} \quad \text {or} \quad \text {(b)} \quad \{u \} = \{x, y \},
$$

and from the second we know that either

$$
\text {(c)} \quad \{u, v \} = \{x \} \quad \text {or} \quad \text {(d)} \quad \{u, v \} = \{x, y \}.
$$

First suppose (b) holds; then $u = x = y$ . Then (c) and (d) are equivalent, and tell us that $u = v = x = y$ . In this case the conclusion of the theorem holds. Similarly if (c) holds, we have the same situation.

There remains the case in which (a) and (d) hold. From (a) we have u = x. From (d) we get either u = y or v = y. In the first case (b) holds; that case has already been considered. In the second case we have v = y, as desired.

The preceding theorem lets us unambiguously define the first coordinate of $\langle x, y \rangle$ to be x, and the second coordinate to be y.

Example Let R be the set of all real numbers. The pair $\langle x, y \rangle$ can be visualized as a point in the plane (Fig. 6), where coordinate axes have been established. This representation of points in the plane is attributed to Descartes.

Now suppose that we have two sets A and B, and we form ordered pairs $\langle x, y \rangle$ with $x \in A$ and $y \in B$ . The collection of all such pairs is called the Cartesian product $A \times B$ of A and B:

$$
A \times B = \{\langle x, y \rangle \mid x \in A \& y \in B \}.
$$

![](images/7c7e35d5db4cba127ec9c2bd115079c3d3db1f528ba9b1ba77c2ef2ede2edb42.jpg)  
Fig. 6. The pair $\langle x, y \rangle$ as a point in the plane.

We must verify that this collection is actually a set before the definition is legal. When we use the abstraction notation $\{t \mid \_ t \_\}$ for a set, we must verify that there does indeed exist a set D such that

$$
t \in D \Leftrightarrow \_ t \_
$$

for every t. For example, just as strings of symbols, the expressions

$$
\{x \mid x = x \} \quad \text { and } \quad \{x \mid x \neq x \}
$$

look similar. But by Theorem 2A the first does not name a set, whereas (by the empty set axiom) the second does.

The strategy we follow in order to show that $A \times B$ is a set (and not a proper class) runs as follows. If we can find a large set that already contains all of the pairs $\langle x, y \rangle$ we want, then we can use a subset axiom to cut things down to $A \times B$ . A suitable large set to start with is provided by the next lemma.

Lemma 3B If $x \in C$ and $y \in C$ , then $\langle x, y \rangle \in \mathcal{P}\mathcal{P}C$ .

Proof As the following calculation demonstrates, the fact that the braces in “ $\{\{x\},\{x,y\}\}$ ” are nested to a depth of 2 is responsible for the two applications of the power set operation:

$$
\begin{array}{c c c} x \in C & \text { and } & y \in C, \\ \{x \} \subseteq C & \text { and } & \{x,   y \} \subseteq C, \\ \{x \} \in {\mathcal P} C & \text { and } & \{x,   y \} \in {\mathcal P} C, \\ \{\{x \},   \{x,   y \} \} \subseteq {\mathcal P} C, \\ \{\{x \},   \{x,   y \} \} \in {\mathcal P} {\mathcal P} C. \end{array}
$$

Corollary 3C For any sets A and B, there is a set whose members are exactly the pairs $\langle x, y \rangle$ with $x \in A$ and $y \in B$ .

Proof From a subset axiom we can construct

$$
\{w \in \mathscr {P P} (A \cup B) \mid w = \langle x, y \rangle \text {   for   some   } x \text {   in   } A \text {   and   some   } y \text {   in   } B \}.
$$

Clearly this set contains only pairs of the desired sort; by the preceding lemma it contains them all.

This corollary justifies our earlier definition of the Cartesian product $A \times B$ .

As you have probably observed, our decision to use the Kuratowski definition

$$
\langle x, y \rangle = \{\{x \}, \{x, y \} \}
$$

is somewhat arbitrary. There are other definitions that would serve as well. The essential fact is that satisfactory ways exist of defining ordered pairs in terms of other concepts of set theory.

## Exercises

See also the Review Exercises at the end of this chapter.

1. Suppose that we attempted to generalize the Kuratowski definitions of ordered pairs to ordered triples by defining

$$
\langle x, y, z \rangle^ {*} = \{\{x \}, \{x, y \}, \{x, y, z \} \}.
$$

Show that this definition is unsuccessful by giving examples of objects $u, v, w, x, y, z$ with $\langle x, y, z \rangle^* = \langle u, v, w \rangle^*$ but with either $y \neq v$ or $z \neq w$ (or both).

2. $\forall a)$ Show that $A \times (B \cup C) = (A \times B) \cup (A \times C)$ .

(b) Show that if $A \times B = A \times C$ and $A \neq \emptyset$ , then $B = C$ .

3. Show that $A \times \bigcup \mathcal{B} = \bigcup \{A \times X \mid X \in \mathcal{B}\}$ .

4. Show that there is no set to which every ordered pair belongs.

5. (a) Assume that $A$ and $B$ are given sets, and show that there exists a set $C$ such that for any $y$ ,

$$
y \in C \Leftrightarrow y = \{x \} \times B \text {   for   some   } x \text {   in   } A.
$$

In other words, show that $\{\{x\} \times B | x \in A\}$ is a set.

(b) With $A, B$ , and $C$ as above, show that $A \times B = \bigcup C$ .

## RELATIONS

Before attempting to say what, in general, a relation is, it would be prudent to contemplate a few examples.

The ordering relation $<$ on the set $\{2, 3, 5\}$ , is one example. We might

![](images/ecc560f7f6f3930a76150c7b0dba028f023a364459ad2ac8c0b67367f63cf82c.jpg)  
Fig. 7. The ordering relation $<$ on $\{2, 3, 5\}$ .

say that $<$ relates each number to each of the larger numbers. Thus $3 < 5$ , so $<$ relates 3 to 5. Pictorially we can represent this by drawing an arrow from 3 to 5. Altogether we get three arrows in this way (Fig. 7).

What set adequately encodes this ordering relation? In place of the arrows, we take the ordered pairs $\langle2,3\rangle$ , $\langle2,5\rangle$ , and $\langle3,5\rangle$ . The set of these pairs

$$
R = \{\langle 2, 3 \rangle , \langle 2, 5 \rangle , \langle 3, 5 \rangle \}
$$

completely captures the information in Fig. 7. At one time it was fashionable to refer to the set R as the graph of the relation, a terminology that seems particularly appropriate if we think of R as a subset of the coordinate plane. But nowadays an even simpler viewpoint has become dominant: R is the ordering relation on $\{2, 3, 5\}$ . It consists of the pairs tying each number to the larger numbers; a relation is this collection of “ties.”

A homier example might be the relation of marriage. (We ignore for the moment the fact that we banished people from our set theory.) This relation is the aggregate total of individual ties between each married person and his or her spouse. Or to say it more mathematically, the relation is

$$
\{\langle x, y \rangle \mid x \text {   is   married   to   } y \}.
$$

You have probably guessed that for us a relation will be a set of ordered pairs. And there will be no further restrictions; any set of ordered pairs is some relation, even if a peculiar one.

Definition A relation is a set of ordered pairs.

For a relation $R$ , we sometimes write $xRy$ in place of $\langle x, y \rangle \in R$ . For example, in the case of the ordering relation $<$ on the set $\mathbb{R}$ of real numbers

$$
<   = \{\langle x, y \rangle \in \mathbb {R} \times \mathbb {R} | x \text {   is   less   than   } y \},
$$

the notation “x < y” is preferred to “ $\langle x, y \rangle \in <$ .”

Examples Let $\omega$ be the set $\{0, 1, 2, \ldots\}$ , which is introduced more formally in the next chapter. Then the divisibility relation is

$$
\{\langle m, n \rangle \in \omega \times \omega | (\exists p \in \omega) m \cdot p = n \}.
$$

The identity relation on $\omega$ is

$$
I _ {\omega} = \{\langle n, n \rangle | n \in \omega \}.
$$

And any subset of $\omega \times \omega$ (of which there are a great many) is some sort of relation.

Of course some relations are much more interesting than others. In the coming pages we shall look at functions, equivalence relations, and ordering relations. At this point we make some very general definitions.

Definition We define the domain of $R$ (dom $R$ ), the range of $R$ (ran $R$ ), and the field of $R$ (fld $R$ ) by

$$
\begin{array}{r c l} x \in \operatorname{dom} R & \Leftrightarrow & \exists y   \langle x, y \rangle \in R, \\ x \in \operatorname{ran} R & \Leftrightarrow & \exists t   \langle t, x \rangle \in R, \\ \operatorname{fld} R & = & \operatorname{dom} R \cup \operatorname{ran} R. \end{array}
$$

For example, let R be the set of all real numbers (a set we construct officially in Chapter 5) and suppose that $R \subseteq R \times R$ . Then R is a subset of the coordinate plane (Fig. 8). The projection of R onto the horizontal axis is dom R, and the projection onto the vertical axis is ran R.

To justify the foregoing definition, we must be sure that for any given R, there exists a set containing all first coordinates and second coordinates of pairs of R. The problem here is analogous to the recent problem of justifying the definition of $A \times B$ , which was accomplished by Corollary 3C. The crucial fact needed now is that there exists a large set already containing all of the elements we seek. This fact is provided by the following lemma, which is related to Lemma 3B. (Lemma 3D was stated as an example in the preceding chapter.)

Lemma 3D If $\langle x, y \rangle \in A$ , then $x$ and $y$ belong to $\bigcup \bigcup A$ .

Proof We assume that $\{\{x\}, \{x, y\}\} \in A$ . Consequently, $\{x, y\} \in \bigcup A$ since it belongs to a member of $A$ . And from this we conclude that $x \in \bigcup \bigcup A$ and $y \in \bigcup \bigcup A$ .

This lemma indicates how we can use subset axioms to construct the domain and range of R:

$$
\operatorname{dom} R = \{x \in \bigcup \bigcup R \mid \exists y \langle x, y \rangle \in R \},
$$

$$
\operatorname{ran} R = \{x \in \bigcup \bigcup R \mid \exists t \langle t, x \rangle \in R \}.
$$

![](images/f44564dc8f9cb0aec9abd708d15fbe3477c199749c89a9f05de79e15ff6d0d6b.jpg)  
Fig. 8. A relation as a subset of the plane.

## Exercises

6. Show that a set $A$ is a relation iff $A \subseteq \operatorname{dom} A \times \operatorname{ran} A$ .

7. Show that if $R$ is a relation, then $\operatorname{fld} R = \bigcup \bigcup R$ .

8. Show that for any set A:

$$
\operatorname{dom} \bigcup \mathcal {A} = \bigcup \{\operatorname{dom} R \mid R \in \mathcal {A} \},
$$

$$
\operatorname{ran} \bigcup \mathcal {A} = \bigcup \{\operatorname{ran} R \mid R \in \mathcal {A} \}.
$$

9. Discuss the result of replacing the union operation by the intersection operation in the preceding problem.

## n-ARY RELATIONS

We can extend the ideas behind ordered pairs to the case of ordered triples and, more generally, to ordered n-tuples. For triples we define

$$
\langle x, y, z \rangle = \langle \langle x, y \rangle , z \rangle .
$$

Similarly we can form ordered quadruples:

$$
\begin{array}{r l} \langle x _ {1}, x _ {2}, x _ {3}, x _ {4} \rangle & = \langle \langle x _ {1}, x _ {2}, x _ {3} \rangle , x _ {4} \rangle \\ & = \langle \langle \langle x _ {1}, x _ {2} \rangle , x _ {3} \rangle , x _ {4} \rangle . \end{array}
$$

Clearly we could continue in this way to define ordered quintuples or ordered n-tuples for any particular n. It is convenient for reasons of uniformity to define also the 1-tuple $\langle x\rangle = x$ .

We define an n-ary relation on A to be a set of ordered n-tuples with all components in A. Thus a binary (2-ary) relation on A is just a subset of $A \times A$ . And a ternary (3-ary) relation on A is a subset of $(A \times A) \times A$ . There is, however, a terminological quirk here. If n > 1, then any n-ary relation on A is actually a relation. But a unary (1-ary) relation on A is just a subset of A; thus it may not be a relation at all.

## Exercise

10. Show that an ordered 4-tuple is also an ordered m-tuple for every positive integer m less than 4.

## FUNCTIONS

Calculus books often describe a function as a rule that assigns to each object in a certain set (its domain) a unique object in a possibly different set (its range). A typical example is the squaring function, which assigns to each real number x its square $x^{2}$ . The action of this function on a particular number can be described by writing

$$
3 \mapsto 9, - 2 \mapsto 4, 1 \mapsto 1, \frac {1}{2} \mapsto \frac {1}{4}, \text { etc. }
$$

Each individual action can be represented by an ordered pair:

$$
\langle 3, 9 \rangle , \quad \langle - 2, 4 \rangle , \quad \langle 1, 1 \rangle , \quad \langle \frac {1}{2}, \frac {1}{4} \rangle , \quad \text { etc. }
$$

The set of all these pairs (one for each real number) adequately represents the squaring function. The set of pairs has at times been called the graph of the function; it is a subset of the coordinate plane $R \times R$ . But the simplest procedure is to take this set of ordered pairs to be the function.

Thus a function is a set of ordered pairs (i.e., a relation). But it has a special property: It is “single-valued,” i.e., for each x in its domain there is a unique y such that $x \mapsto y$ . We build these ideas into the following definition.

Definition A function is a relation $F$ such that for each $x$ in dom $F$ there is only one $y$ such that $xFy$ .

For a function F and a point x in dom F, the unique y such that xFy is called the value of F at x and is denoted $F(x)$ . Thus $\langle x, F(x) \rangle \in F$ . The “ $F(x)$ ” notation was introduced by Euler in the 1700s. We hereby resolve to use this notation only when F is a function and $x \in dom F$ . There are, however, some artificial ways of defining $F(x)$ that are meaningful for any F and x. For example, the set

$$
\bigcup \{y \mid \langle x, y \rangle \in F \}
$$

is equal to $F(x)$ whenever $F$ is a function and $x \in \operatorname{dom} F$ .

Functions are basic objects appearing in all parts of mathematics. $^{1}$ As a result, there is a good deal of terminology used in connection with functions. Unfortunately, no terminology has become uniformly standardized. We collect below some of this terminology.

We say that F is a function from A into B or that F maps A into B (written $F: A \rightarrow B$ ) iff F is a function, dom F = A, and ran $F \subseteq B$ . Note the unequal treatment of A and B here; we demand only that ran $F \subseteq B$ . If, in addition, ran F = B, then F is a function from A onto B. (Thus any function F maps its domain onto its range. And it maps its domain into any set B that includes ran F. The applicability of the word “onto” depends both on F and on the set B, not just on F. The word “onto” must never be used as an adjective.)

A function $F$ is one-to-one iff for each $y \in \operatorname{ran} F$ there is only one $x$ such that $xFy$ . For example, the function defined by

$$
f (x) = x ^ {3} \quad \text {   for   each   real   number   } x
$$

is one-to-one, whereas the squaring function is not, since $(-3)^{2}=3^{2}$ . One-to-one functions are sometimes called injections.

It will occasionally be useful to apply the concept of “one-to-one” to relations that are not functions. Since the phrase “one-to-one” seems inappropriate in such cases, we will use the phrase “single-rooted,” in analogy to “single-valued.”

Definition A set $R$ is single-rooted iff for each $y \in \operatorname{ran} R$ there is only one $x$ such that $xRy$ .

Thus for a function, it is single-rooted iff it is one-to-one.

It is entirely possible to have the domain of a function F consist of ordered pairs or n-tuples. For example, addition is a function + : R × R → R. Thus the domain of addition consists of pairs of numbers, and the addition function itself consists of triples of numbers. In place of $+(\langle x, y \rangle)$ we write either $+(x, y)$ or $x + y$ .

The following operations are most commonly applied to functions, sometimes are applied to relations, but can actually be defined for arbitrary sets A, F, and G.

Definition (a) The inverse of $F$ is the set

$$
F ^ {- 1} = \{\langle u, v \rangle | v F u \}.
$$

(b) The composition of $F$ and $G$ is the set

$$
F \circ G = \{\langle u, v \rangle | \exists t (u G t \& t F v) \}.
$$

(c) The restriction of $F$ to $A$ is the set

$$
F \upharpoonright A = \{\langle u, v \rangle | u F v \& u \in A \}.
$$

(d) The image of $A$ under $F$ is the set

$$
\begin{array}{r l} F [   [ A ]   ] & = \operatorname{ran} (F \upharpoonright A) \\ & = \{v \mid (\exists u \in A) u F v \}. \end{array}
$$

$F[\mathbb{A}]$ can be characterized more simply when $F$ is a function and $A \subseteq \operatorname{dom} F$ ; in this case

$$
F [   [ A ]   ] = \{F (u) \mid u \in A \}.
$$

In each case we can easily apply a subset axiom to establish the existence of the desired set. Specifically, $F^{-1} \subseteq \operatorname{ran} F \times \operatorname{dom} F$ , $F \circ G \subseteq \operatorname{dom} G \times \operatorname{ran} F$ , $F \upharpoonright A \subseteq F$ , and $F[[A]] \subseteq \operatorname{ran} F$ . (A more detailed justification of the definition of $F^{-1}$ would go as follows: By a subset axiom there is a set $B$ such that for any $x$ ,

$$
x \in B \Leftrightarrow x \in \operatorname{ran} F \times \operatorname{dom} F \& \exists u \exists v (x = \langle u, v \rangle \& v F u).
$$

It then follows that

$$
x \in B \Leftrightarrow \exists u \exists v (x = \langle u, v \rangle \& v F u).
$$

This unique set $B$ we denote as $F^{-1}$ .)

Example Let $F: \mathbb{R} \to \mathbb{R}$ be defined by the equation $F(x) = x^2$ . Let $A$ be the set $\{x \in R | -1 \leq x \leq 2\}$ , i.e., the closed interval $[-1, 2]$ . Then $F[[A]] = [0, 4]$ ; see Fig. 9. And $F^{-1}[A] = [-\sqrt{2}, \sqrt{2}]$ . Notice that although $F$ here is a function, $F^{-1}$ is not a function, because both $\langle 9, 3 \rangle$ and $\langle 9, -3 \rangle$ are in $F^{-1}$ . The so-called "multiple-valued functions" are relations, not functions. People write " $F^{-1}(9) = \pm 3$ ," but it would be preferable to write: $F^{-1}[[\{9\}]] = \{-3, 3\}$ .

![](images/375102c4cac50a948648574fc54a4ccf1c78dc785882bf943d56ec2eabf36713.jpg)  
Fig. 9. $F[\mathbb{A}]$ is the image of the set $A$ under $F$ .

Example In mathematical analysis it is often necessary to consider the “inverse image” of a set A under a function F, i.e., the set $F^{-1}[A]$ . For a function F,

$$
F ^ {- 1} [   [ A ]   ] = \{x \in \operatorname{dom} F \mid F (x) \in A \}
$$

(Exercise 24). In general, $F^{-1}$ will not be a function.

Example Let g be the sine function of trigonometry. Then $g^{-1}$ is not a function. (Why not?) But the restriction of g to the closed interval $[-\pi/2, \pi/2]$ is one-to-one, and its inverse

$$
(g \upharpoonright [ - \pi / 2, \pi / 2 ]) ^ {- 1}
$$

is the arc sine function.

Example Assume that we have the set of all people (!) in mind, and we define P to be the relation of parenthood, i.e.,

$$
P = \{\langle x, y \rangle \mid x \text {   is   a   parent   of   } y \}.
$$

Then

$$
P ^ {- 1} = \{\langle x, y \rangle \mid x \text {   is   a   son   or   daughter   of   } y \}
$$

and

$$
P \circ P = \{\langle x, y \rangle \mid x \text {   is   a   grandparent   of   } y \}.
$$

If $A$ is the set of people born in Poland, then

$(P \circ P)[[A]] = \{t \mid \text{a grandparent of } t \text{ was born in Poland}\}$ .

To further complicate matters, let S be the relation that holds between siblings:

$$
S = \{\langle x, y \rangle \mid x \text {   is   a   brother   or   sister   of   } y \}
$$

Then $S^{-1} = S$ . To find out what $P \circ S$ is, we can calculate:

$$
\begin{array}{r c l} \langle x, y \rangle \in P \circ S & \Leftrightarrow & x S t   \&   t P y \quad \text { for some }   t \\ & \Leftrightarrow & x \text { is a sibling of a parent of } y \\ & \Leftrightarrow & x \text { is an aunt or uncle of } y. \end{array}
$$

None of the relations in this example are functions.

Example Let

$$
F = \{\langle \emptyset , a \rangle , \langle \{\emptyset \}, b \rangle \}.
$$

Observe that $F$ is a function. We have

$$
F ^ {- 1} = \{\langle a, \emptyset \rangle , \langle b, \{\emptyset \} \rangle \}.
$$

$F^{-1}$ is a function iff $a \neq b$ . The restriction of $F$ to $\varnothing$ is $\varnothing$ , but

$$
F \upharpoonright \{\emptyset \} = \{\langle \emptyset , a \rangle \}.
$$

Consequently, $F[\{\emptyset\}] = \{a\}$ , in contrast to the fact that $F(\{\emptyset\}) = b$ .

The following facts about inverses are not difficult to show; the proofs of some of them are left as exercises.

Theorem 3E For a set $F$ , $\operatorname{dom} F^{-1} = \operatorname{ran} F$ and $\operatorname{ran} F^{-1} = \operatorname{dom} F$ . For a relation $F$ , $(F^{-1})^{-1} = F$ .

Theorem 3F For a set $F, F^{-1}$ is a function iff $F$ is single-rooted. A relation $F$ is a function iff $F^{-1}$ is single-rooted.

Theorem 3G Assume that $F$ is a one-to-one function. If $x \in \operatorname{dom} F$ , then $F^{-1}(F(x)) = x$ . If $y \in \operatorname{ran} F$ , then $F(F^{-1}(y)) = y$ .

Proof Suppose that $x \in \operatorname{dom} F$ ; then $\langle x, F(x) \rangle \in F$ and $\langle F(x), x \rangle \in F^{-1}$ . Thus $F(x) \in \operatorname{dom} F^{-1}$ . $F^{-1}$ is a function by Theorem 3F, so $x = F^{-1}(F(x))$ .

If $y \in \operatorname{ran} F$ , then by applying the first part of the theorem to $F^{-1}$ we obtain the equation $(F^{-1})^{-1}(F^{-1}(y)) = y$ . But $(F^{-1})^{-1} = F$ .

In place of Theorem 3G, we could have defined $F^{-1}$ (for a one-to-one function F) to be that function whose value at $F(x)$ is x (and whose domain is ran F). But this would be too restrictive; $F^{-1}$ can be a useful relation even when it is not a function. Hence we prefer a definition of $F^{-1}$ that is applicable to any set.

Theorem 3H Assume that $F$ and $G$ are functions. Then $F \circ G$ is a function, its domain is

$$
\{x \in \operatorname{dom} G \mid G (x) \in \operatorname{dom} F \},
$$

and for $x$ in its domain, $(F \circ G)(x) = F(G(x))$ .

Proof To see that $F \circ G$ is a function, assume that $x(F \circ G)y$ and $x(F \circ G)y'$ . Then for some $t$ and $t'$ ,

$$
x G t \& t F y \quad \text { and } \quad x G t ^ {\prime} \& t ^ {\prime} F y ^ {\prime}.
$$

Since $G$ is a function, $t = t'$ . Since $F$ is a function, $y = y'$ . Hence $F \circ G$ is a function.

Now suppose that $x \in \operatorname{dom} G$ and $G(x) \in \operatorname{dom} F$ . We must show that $x \in \operatorname{dom}(F \circ G)$ and that $(F \circ G)(x) = F(G(x))$ . We have $\langle x, G(x) \rangle \in G$ and $\langle G(x), F(G(x)) \rangle \in F$ . Hence $\langle x, F(G(x)) \rangle \in F \circ G$ , and this yields the desired facts.

Conversely, if $x \in \operatorname{dom} F \circ G$ , then we know that for some $y$ and $t$ , $xGt$ and $tFy$ . Hence $x \in \operatorname{dom} G$ and $t = G(x) \in \operatorname{dom} F$ .

Again we could have defined $F \circ G$ (for functions F and G) as the function with the properties stated in the above theorem. But we prefer to use a definition applicable to nonfunctions as well. For example, in Exercise 32, we will want $R \circ R$ for an arbitrary relation R.

Example Assume that $G$ is some one-to-one function. Then by Theorem 3H, $G^{-1} \circ G$ is a function, its domain is

$$
\{x \in \operatorname{dom} G \mid G (x) \in \operatorname{dom} G ^ {- 1} \} = \operatorname{dom} G,
$$

and for $x$ in its domain,

$$
\begin{array}{r l} (G ^ {- 1} \circ G) (x) & = G ^ {- 1} (G (x)) \\ & = x \quad \text { by   Theorem   3G. } \end{array}
$$

Thus $G^{-1} \circ G$ is $I_{\mathrm{dom}G}$ , the identity function on dom $G$ , by Exercise 11. Similarly one can show that $G \circ G^{-1}$ is $I_{\mathrm{ran}G}$ (Exercise 25).

Theorem 3I For any sets $F$ and $G$ ,

$$
(F \circ G) ^ {- 1} = G ^ {- 1} \circ F ^ {- 1}.
$$

Proof Both $(F\circ G)^{-1}$ and $G^{-1}\circ F^{-1}$ are relations. We calculate:

$$
\begin{array}{r c l} \langle x, y \rangle \in (F \circ G) ^ {- 1} & \Leftrightarrow & \langle y, x \rangle \in F \circ G \\ & \Leftrightarrow & y G t \& t F x \quad \text { for   some } t \\ & \Leftrightarrow & x F ^ {- 1} t \& t G ^ {- 1} y \quad \text { for   some } t \\ & \Leftrightarrow & \langle x, y \rangle \in G ^ {- 1} \circ F ^ {- 1}. \end{array}
$$

In a less abstract form, Theorem 3I expresses common knowledge. In getting dressed, one first puts on socks and then shoes. But in the inverse process of getting undressed, one first removes shoes and then socks.

Theorem 3J Assume that $F: A \to B$ , and that $A$ is nonempty.

(a) There exists a function $G \colon B \to A$ (a "left inverse") such that $G \circ F$ is the identity function $I_A$ on $A$ iff $F$ is one-to-one.

(b) There exists a function $H: B \to A$ (a "right inverse") such that $F \circ H$ is the identity function $I_B$ on $B$ iff $F$ maps $A$ onto $B$ .

Proof (a) First assume that there is a function $G$ for which $G \circ F = I_A$ . If $F(x) = F(y)$ , then by applying $G$ to both sides of the equation we have

$$
x = G (F (x)) = G (F (y)) = y,
$$

and hence $F$ is one-to-one.

For the converse, assume that $F$ is one-to-one. Then $F^{-1}$ is a function from ran $F$ onto $A$ (by Theorems 3E and 3F). The idea is to extend $F^{-1}$ to a function $G$ defined on all of $B$ . By assumption $A$ is nonempty, so we can fix some $a$ in $A$ . Then we define $G$ so that it assigns $a$ to every point in $B - \operatorname{ran} F$ :

$$
G (x) = \left\{ \begin{array}{l l} F ^ {- 1} (x) & \text { if } \quad x \in \operatorname{ran} F \\ a & \text { if } \quad x \in B - \operatorname{ran} F. \end{array} \right.
$$

In one line,

$$
G = F ^ {- 1} \cup (B - \operatorname{ran} F) \times \{a \}
$$

(see Fig. 10a). This choice for $G$ does what we want: $G$ is a function mapping $B$ into $A$ , $\operatorname{dom}(G \circ F) = A$ , and $G(F(x)) = F^{-1}(F(x)) = x$ for each $x$ in $A$ . Hence $G \circ F = I_A$ .

(b) Next assume that there is a function $H$ for which $F \circ H = I_B$ . Then for any $y$ in $B$ we have $y = F(H(y))$ , so that $y \in \operatorname{ran} F$ . Thus ran $F$ is all of $B$ .

The converse poses a difficulty. We cannot take $H = F^{-1}$ , because in general F will not be one-to-one and so $F^{-1}$ will not be a function. Assume that F maps A onto B, so that ran F = B. The idea is that for each $y \in B$ we must choose some x for which $F(x) = y$ and then let $H(y)$ be the chosen x. Since $y \in \operatorname{ran} F$ we know that such x's exist, so there is no problem (see Fig. 10b).

Or is there? For any one y we know there exists an appropriate x. But that is not by itself enough to let us form a function H. We have in general no way of defining any one particular choice of x. What is needed here is the axiom of choice.

![](images/e7dee8e86b8185495aa92c26166b071b5c751ad76c5ea1a7d4651ce62cb7f5ac.jpg)  
(a)

![](images/e39f8ff8c97326da4b1bc0b8134d10b353ebedb44af7fdd5c30b364fb68e4d88.jpg)  
(b)  
Fig. 10. The proof of Theorem 3J. In part (a), make $G(x) = a$ for $x \in B - \operatorname{ran} F$ . In part (b), $H(y)$ is the chosen $x$ for which $F(x) = y$ .

Axiom of Choice (first form) For any relation $R$ there is a function $H \subseteq R$ with $\operatorname{dom} H = \operatorname{dom} R$ .

With this axiom we can now proceed with the proof of Theorem 3J(b); take $H$ to be a function with $H \subseteq F^{-1}$ and $\operatorname{dom} H = \operatorname{dom} F^{-1} = B$ . Then $H$ does what we want: Given any $y$ in $B$ , we have $\langle y, H(y) \rangle \in F^{-1}$ ; hence $\langle H(y), y \rangle \in F$ , and so $F(H(y)) = y$ .

In Chapter 6 we will give a systematic discussion of the axiom of choice. It is the only axiom that we discuss without using the marginal stripe.

Theorem 3K The following hold for any sets. (F need not be a function.)

(a) The image of a union is the union of the images:

$$
F [   [ A \cup B ]   ] = F [   [ A ]   ] \cup F [   [ B ]   ] \quad \text { and } \quad F [   [ \bigcup \mathcal {A} ]   ] = \bigcup \{F [   [ A ]   ] \mid A \in \mathcal {A} \}.
$$

(b) The image of an intersection is included in the intersection of the images:

$$
F [ [ A \cap B ] ] \subseteq F [ [ A ] ] \cap F [ [ B ] ] \quad \text { and } \quad F [ [ \bigcap \mathscr {A} ] ] \subseteq \bigcap \{F [ [ A ] ] \mid A \in \mathscr {A} \}
$$

for nonempty $\mathcal{A}$ . Equality holds if $F$ is single-rooted.

(c) The image of a difference includes the difference of the images:

$$
F [ [ A ] ] - F [ [ B ] ] \subseteq F [ [ A - B ] ].
$$

Equality holds if F is single-rooted.

Example Let $F: \mathbb{R} \to \mathbb{R}$ be defined by $F(x) = x^2$ . Let $A$ and $B$ be the closed intervals $[-2, 0]$ and $[1, 2]$ :

$$
A = \{x | - 2 \leq x \leq 0 \} \quad \text { and } \quad B = \{x | 1 \leq x \leq 2 \}.
$$

Then $F[\mathbb{A}] = [0, 4]$ and $F[\mathbb{B}] = [1, 4]$ . This example shows that equality does not always hold in parts (b) and (c) of Theorem 3K, for $F[\mathbb{A} \cap B] = F[\emptyset] = \emptyset$ , whereas $F[\mathbb{A}] \cap F[\mathbb{B}] = [1, 4]$ . And $F[\mathbb{A}] - F[\mathbb{B}] = [0, 1)$ , whereas $F[\mathbb{A} - B] = F[\mathbb{A}] = [0, 4]$ .

Proof To prove Theorem 3K we calculate

$$
\begin{array}{r c l} y \in F [   [ A \cup B ]   ] & \Leftrightarrow & (\exists x \in A \cup B) x F y \\ & \Leftrightarrow & (\exists x \in A) x F y \text { or } (\exists x \in B) x F y \\ & \Leftrightarrow & y \in F [   [ A ]   ] \text { or } y \in F [   [ B ]   ]. \end{array}
$$

This proves the first half of (a). For intersections we have the corresponding calculation, except that the middle step

$$
(\exists x \in A \cap B) x F y \Rightarrow (\exists x \in A) x F y \& (\exists x \in B) x F y
$$

is not always reversible. It is possible that both $x_{1} \in A$ with $x_{1}Fy$ and $x_{2} \in B$ with $x_{2}Fy$ , and yet there might be no $x$ in $A \cap B$ with $xFy$ . But if $F$ is single-rooted, then $x_{1} = x_{2}$ and so it is in $A \cap B$ . Thus we obtain the first half of (b).

The second halves of (a) and (b) generalize the first halves. The proofs follow the same outlines as the first halves, but we leave the details to Exercise 26.

For part (c) we also calculate:

$$
\begin{array}{r c l} y \in F [   [ A ]   ] - F [   [ B ]   ] & \Leftrightarrow & (\exists x \in A) x F y \& \lnot (\exists t \in B) t F y \\ & \Rightarrow & (\exists x \in A - B) x F y \\ & \Leftrightarrow & y \in F [   [ A - B ]   ]. \end{array}
$$

Again if $F$ is single-rooted, then there is only one $x$ such that $xFy$ . In this case the middle step can be reversed.

Since the inverse of a function is always single-rooted, we have as an immediate consequence of Theorem 3K that unions, intersections, and relative complements are always preserved under inverse images.

Corollary 3L For any function G and sets A, B, and A:

$$
\begin{array}{l} G ^ {- 1} [   [ \bigcup \mathcal {A} ]   ] = \bigcup \{G ^ {- 1} [   [ A ]   ] \mid A \in \mathcal {A} \}, \\ G ^ {- 1} [   [ \bigcap \mathcal {A} ]   ] = \bigcap \{G ^ {- 1} [   [ A ]   ] \mid A \in \mathcal {A} \} \qquad \text { for } \quad \mathcal {A} \neq \emptyset , \\ G ^ {- 1} [   [ A - B ]   ] = G ^ {- 1} [   [ A ]   ] - G ^ {- 1} [   [ B ]. \end{array}
$$

We conclude our discussion of functions with some definitions that may be useful later. Our intent is to build a large working vocabulary of set-theoretic notations.

An infinite union is often “indexed,” as when we write $\bigcup_{i\in I}A_{i}$ . We can give a formal definition to such a union as follows. Let I be a set, called the index set. Let F be a function whose domain includes I. Then we define

$$
\begin{array}{l} \bigcup_ {i \in I} F (i) = \bigcup \{F (i) \mid i \in I \} \\ \qquad = \{x \mid x \in F (i) \text {   for   some   } i \text {   in   } I \}. \end{array}
$$

For example, if $I = \{0, 1, 2, 3\}$ , then

$$
\begin{array}{c} \bigcup_ {i \in I} F (i) = \bigcup \{F (0), F (1), F (2), F (3) \} \\ = F (0) \cup F (1) \cup F (2) \cup F (3). \end{array}
$$

Similar remarks apply to intersections (provided that I is nonempty):

$$
\begin{array}{l} \bigcap_ {i \in I} F (i) = \bigcap \{F (i) \mid i \in I \} \\ \qquad \qquad \qquad = \{x \mid x \in F (i) \text {   for   every   } i \text {   in   } I \}. \end{array}
$$

If we use the alternative notation

$$
F _ {i} = F (i),
$$

then we can rewrite the above equations as

$$
\begin{array}{r l} \bigcup_ {i \in I} F _ {i} & = \bigcup \{F _ {i} \mid i \in I \} \\ & = \{x \mid x \in F _ {i} \text {   for   some   } i \text {   in   } I \} \end{array}
$$

and

$$
\begin{array}{r l} \bigcap_ {i \in I} F _ {i} & = \bigcap \{F _ {i} \mid i \in I \} \\ & = \{x \mid x \in F _ {i} \text {   for   every   } i \text {   in   } I \}. \end{array}
$$

For sets A and B we can form the collection of functions F from A into B. Call the set of all such functions $^{4}B$ :

$$
^ {A} B = \{F \mid F \text {   is   a   function   from   } A \text {   into   } B \}.
$$

If $F: A \to B$ , then $F \subseteq A \times B$ , and so $F \in \mathcal{P}(A \times B)$ . Consequently we can apply a subset axiom to $\mathcal{P}(A \times B)$ to construct the set of all functions from $A$ into $B$ .

The notation $^{A}B$ is read “B-pre-A.” Some authors write $B^{A}$ instead; this notation is derived from the fact that if A and B are finite sets and the number of elements in A and B is a and b, respectively, then $^{A}B$ has $b^{a}$ members. (To see this, note that for each of the a elements of A, we can choose among b points in B into which it could be mapped. The number of ways of making all a such choices is $b \cdot b \cdot \cdots \cdot b$ , a times.) We will return to this point in Chapter 6.

Example Let $\omega = \{0, 1, 2, \ldots\}$ . Then ${}^{\omega}\{0, 1\}$ is the set of all possible functions $f: \omega \to \{0, 1\}$ . Such an $f$ can be thought of as an infinite sequence $f(0), f(1), f(2), \ldots$ of 0's and 1's.

Example For a nonempty set $A$ , we have ${}^4\varnothing = \varnothing$ . This is because no function could have a nonempty domain and an empty range. On the other hand, ${}^{\varnothing}A = \{\varnothing\}$ for any set $A$ , because $\varnothing: \varnothing \to A$ , but $\varnothing$ is the only function with empty domain. As a special case, we have ${}^{\varnothing}\varnothing = \{\varnothing\}$ .

## Exercises

11. Prove the following version (for functions) of the extensionality principle: Assume that $F$ and $G$ are functions, $\operatorname{dom} F = \operatorname{dom} G$ , and $F(x) = G(x)$ for all $x$ in the common domain. Then $F = G$ .

12. Assume that $f$ and $g$ are functions and show that

$$
f \subseteq g \Leftrightarrow \operatorname{dom} f \subseteq \operatorname{dom} g \& (\forall x \in \operatorname{dom} f) f (x) = g (x).
$$

13. Assume that $f$ and $g$ are functions with $f \subseteq g$ and $\operatorname{dom} g \subseteq \operatorname{dom} f$ . Show that $f = g$ .

14. Assume that $f$ and $g$ are functions.

(a) Show that $f \cap g$ is a function.

(b) Show that $f \cup g$ is a function iff $f(x) = g(x)$ for every $x$ in $(\operatorname{dom} f) \cap (\operatorname{dom} g)$ .

15. Let $\mathcal{A}$ be a set of functions such that for any $f$ and $g$ in $\mathcal{A}$ , either $f \subseteq g$ or $g \subseteq f$ . Show that $\bigcup \mathcal{A}$ is a function.

16. Show that there is no set to which every function belongs.

17. Show that the composition of two single-rooted sets is again single-rooted. Conclude that the composition of two one-to-one functions is again one-to-one.

18. Let $R$ be the set

$$
\{\langle 0, 1 \rangle , \langle 0, 2 \rangle , \langle 0, 3 \rangle , \langle 1, 2 \rangle , \langle 1, 3 \rangle , \langle 2, 3 \rangle \}.
$$

Evaluate the following: $R \circ R, R \upharpoonright \{1\}, R^{-1} \upharpoonright \{1\}, R[\{1\}], \text{and } R^{-1}[\{1\}]$ .

19. Let

$$
A = \{\langle \emptyset , \{\emptyset , \{\emptyset \} \} \rangle , \langle \{\emptyset \}, \emptyset \rangle \}.
$$

Evaluate each of the following: $A(\emptyset), A[\emptyset], A[\{\emptyset\}], A[\{\emptyset, \{\emptyset\}\}], A^{-1}, A \circ A, A \upharpoonright \emptyset, A \upharpoonright \{\emptyset\}, A \upharpoonright \{\emptyset, \{\emptyset\}\}, \bigcup \bigcup A$ .

20. Show that $F \upharpoonright A = F \cap (A \times \operatorname{ran} F)$ .

21. Show that $(R\circ S)\circ T = R\circ (S\circ T)$ for any sets $R,S$ , and $T$

22. Show that the following are correct for any sets.

(a) $A \subseteq B \Rightarrow F[[A]] \subseteq F[[B]]$ .

(b) $(F\circ G)[[A]] = F[G[A]]]$ .

(c) $Q \upharpoonright (A \cup B) = (Q \upharpoonright A) \cup (Q \upharpoonright B).$

23. Let $I_A$ be the identity function on the set $A$ . Show that for any sets $B$ and $C$ ,

$$
B \circ I _ {A} = B \upharpoonright A \quad \text { and } \quad I _ {A} [   [ C ]   ] = A \cap C.
$$

24. Show that for a function $F, F^{-1}[A] = \{x \in \operatorname{dom} F \mid F(x) \in A\}$ .

25. (a) Assume that $G$ is a one-to-one function. Show that $G \circ G^{-1}$ is $I_{\operatorname{ran} G}$ , the identity function on $\operatorname{ran} G$ .

(b) Show that the result of part (a) holds for any function $G$ , not necessarily one-to-one.

26. Prove the second halves of parts (a) and (b) of Theorem 3K.

27. Show that $\operatorname{dom}(F \circ G) = G^{-1}[\operatorname{dom} F]$ for any sets $F$ and $G$ . ( $F$ and $G$ need not be functions.)

28. Assume that $f$ is a one-to-one function from $A$ into $B$ , and that $G$ is the function with $\operatorname{dom} G = \mathcal{P}A$ defined by the equation $G(X) = f[[X]]$ . Show that $G$ maps $\mathcal{P}A$ one-to-one into $\mathcal{P}B$ .

29. Assume that $f: A \to B$ and define a function $G: B \to \mathcal{P}A$ by

$$
G (b) = \{x \in A | f (x) = b \}.
$$

Show that if $f$ maps $A$ onto $B$ , then $G$ is one-to-one. Does the converse hold? 30. Assume that $F: \mathcal{P}A \to \mathcal{P}A$ and that $F$ has the monotonicity property:

$$
X \subseteq Y \subseteq A \Rightarrow F (X) \subseteq F (Y).
$$

Define

$$
B = \bigcap \{X \subseteq A \mid F (X) \subseteq X \} \quad \text { and } \quad C = \bigcup \{X \subseteq A \mid X \subseteq F (X) \}.
$$

(a) Show that $F(B) = B$ and $F(C) = C$ .

(b) Show that if $F(X) = X$ , then $B \subseteq X \subseteq C$ .

## INFINITE CARTESIAN PRODUCTS $^{2}$

We can form something like the Cartesian product of infinitely many sets, provided that the sets are suitably indexed. More specifically, let I be a set (which we will refer to as the index set) and let H be a function whose domain includes I. Then for each i in I we have the set $H(i)$ ; we want the product of the $H(i)$ 's for all $i \in I$ . We define:

$\bigotimes_{i \in I} H(i) = \{f | f \text{ is a function with domain } I \text{ and } (\forall i \in I) f(i) \in H(i)\}$ .

Thus the members of $\mathsf{X}_{i\in I}H(i)$ are " $I$ -tuples" (i.e., functions with domain $I$ ) for which the "ith coordinate" (i.e., the value at $i$ ) is in $H(i)$ .

The members of $\mathsf{X}_{i\in I}H(i)$ are all functions from $I$ into $\bigcup_{i\in I}H(i)$ and hence are members of $^I (\bigcup_{i\in I}H(i))$ . Thus the set $\mathsf{X}_{i\in I}H(i)$ can be formed by applying a subset axiom to $^I (\bigcup_{i\in I}H(i))$ .

Example If for every $i \in I$ we have $H(i) = A$ for some one fixed $A$ , then $\bigcup_{i \in I} H(i) = ^I A$ .

Example Assume that the index set is the set $\omega = \{0, 1, 2, \ldots\}$ . Then $\mathsf{X}_{i \in \omega} H(i)$ consists of “ $\omega$ -sequences” (i.e., functions with domain $\omega$ ) that have for their $i$ th term some member of $H(i)$ . If we picture the sets $H(i)$ as shown in Fig. 11, then a typical member of $\mathsf{X}_{i \in \omega} H(i)$ is a “thread” that selects a point from each set.

$^{2}$ This section may be omitted if certain obvious adjustments are made in Theorem 6M.

If any one $H(i)$ is empty, then clearly the product $\mathsf{X}_{i\in I}H(i)$ is empty. Conversely, suppose that $H(i)\neq \emptyset$ for every $i$ in $I$ . Does it follow that $\mathsf{X}_{i\in I}H(i)\neq \emptyset$ ? To obtain a member $f$ of the product, we need to select some member from each $H(i)$ , and put $f(i)$ equal to that selected member. This requires the axiom of choice, and in fact this is one of the many equivalent ways of stating the axiom.

Axiom of Choice (second form) For any set I and any function H with domain I, if $H(i) \neq \varnothing$ for all i in I, then $\bigcup_{i \in I} H(i) \neq \varnothing$ .

![](images/c072a8c0b6126edeec8b8ec1cc2383aa9e48eae116126e28c4f63bf0a65e02ed.jpg)  
Fig. 11. The thread is a member of the Cartesian product.

## Exercise

31. Show that from the first form of the axiom of choice we can prove the second form, and conversely.

## EQUIVALENCE RELATIONS

Consider a set A (Fig. 12a). We might want to partition A into little boxes (Fig. 12b). For example, take $A = \omega$ ; we can partition $\omega$ into six parts:

$$
\begin{array}{c} \{0, 6, 1 2, \ldots \}, \\ \{1, 7, 1 3, \ldots \}, \\ \vdots \\ \{5, 1 1, 1 7, \ldots \}. \end{array}
$$

By “partition” we mean that every element of A is in exactly one little box, and that each box is a nonempty subset of A.

Now we need some mental agility. We want to think of each little box as being a single object, instead of thinking of it as a plurality of objects. (Actually we have been doing this sort of thing throughout the book, whenever we think of a set as a single object. It is really no harder than thinking of a brick house as a single object and not as a multitude of bricks.) This changes the picture (Fig. 12c); each box is now, in our mind, a single point. The set B of boxes is very different from the set A. In our example, B has only six members whereas A is infinite. (When we get around to defining “six” and “infinite” officially, we must certainly do it in a way that makes the preceding sentence true.)

The process of transforming a situation like Fig. 12a into Fig. 12c is common in abstract algebra and elsewhere in mathematics. And in Chapter 5 the process will be applied several times in the construction of the real numbers.

Suppose we now define a binary relation $R$ on $A$ as follows: For $x$ and $y$ in $A$ ,

$xRy \Leftrightarrow x$ and $y$ are in the same little box.

![](images/cca11fad03450797d7c3cf101d04e820426d0b1226f73e4dc96d6c12bb107f2a.jpg)  
(a)

![](images/e4206d105f5fc6f398254a421caeb7ac3cc4fe9b7a19e3116eec396d03fefcdd.jpg)  
(b)

![](images/77637ae444c9b1cf7d0fa8d1e7dfa57d54d74ccc7b330eb4266994b4dc8d5f4a.jpg)  
(c)  
Fig. 12. Partitioning a set into six little boxes.

Then we can easily see that $R$ has the following three properties.

1. $R$ is reflexive on $A$ , by which we mean that $xRx$ for all $x \in A$ .

2. $R$ is symmetric, by which we mean that whenever $xRy$ , then also $yRx$ .

3. R is transitive, by which we mean that whenever xRy and yRz, then also xRz.

Definition R is an equivalence relation on A iff R is a binary relation on A that is reflexive on A, symmetric, and transitive.

Theorem 3M If R is a symmetric and transitive relation, then R is an equivalence relation on fld R.

Proof Any relation $R$ is a binary relation on its field, since

$$
R \subseteq \operatorname{dom} R \times \operatorname{ran} R \subseteq \operatorname{fld} R \times \operatorname{fld} R.
$$

What we must show is that R is reflexive on fld R. We have

$$
\begin{array}{r c l l} x \in \operatorname{dom} R & \Rightarrow & x R y & \text { for   some } y \\ & \Rightarrow & x R y \& y R x & \text { by   symmetry } \\ & \Rightarrow & x R x & \text { by   transitivity }, \end{array}
$$

and a similar calculation applies to points in ran R.

This theorem deserves a precautionary note: If R is a symmetric and transitive relation on A, it does not follow that R is an equivalence relation on A. R is reflexive on fld R, but fld R may be a small subset of A.

We have shown how a partition of a set A induces an equivalence relation. (A more formal version of this is in Exercise 37.) Next we want to reverse the process, and show that from any equivalence relation R on A, we get a partition of A.

Definition The set $[x]_R$ is defined by

$$
[ x ] _ {R} = \{t \mid x R t \}.
$$

If R is an equivalence relation and $x \in fld$ R, then $[x]_{R}$ is called the equivalence class of x (modulo R). If the relation R is fixed by the context, we may write just [x].

The status of $[x]_R$ as a set is guaranteed by a subset axiom, since $[x]_R \subseteq \operatorname{ran} R$ . Furthermore we can construct a set of equivalence classes such as $\{[x]_R \mid x \in A\}$ , since this set is included in $\mathcal{P}(\operatorname{ran} R)$ .

Lemma 3N Assume that $R$ is an equivalence relation on $A$ and that $x$ and $y$ belong to $A$ . Then

$$
[ x ] _ {R} = [ y ] _ {R} \quad \text { iff } \quad x R y.
$$

Proof $(\Rightarrow)$ Assume that $[x]_R = [y]_R$ . We know that $y \in [y]_R$ (because $yRy$ ), consequently $y \in [x]_R$ (because $[x]_R = [y]_R$ ). By the definition of $[x]_R$ , this means that $xRy$ .

$(\Leftarrow)$ Next assume that $xRy$ . Then

$$
\begin{array}{r c l} t \in [ y ] _ {R} & \Rightarrow & y R t \\ & \Rightarrow & x R t \quad \text { because } x R y \text { and } R \text { is   transitive } \\ & \Rightarrow & t \in [ x ] _ {R}. \end{array}
$$

Thus $[y]_R \subseteq [x]_R$ . Since $R$ is symmetric, we also have $yRx$ and we can reverse $x$ and $y$ in the above argument to obtain $[x]_R \subseteq [y]_R$ .

Definition A partition $\Pi$ of a set A is a set of nonempty subsets of A that is disjoint and exhaustive, i.e.,

(a) no two different sets in $\Pi$ have any common elements, and

(b) each element of $A$ is in some set in $\Pi$ .

Theorem 3P Assume that $R$ is an equivalence relation on $A$ . Then the set $\{[x]_R \mid x \in A\}$ of all equivalence classes is a partition of $A$ .

Proof Each equivalence class $[x]_R$ is nonempty (because $x \in [x]_R$ ) and is a subset of $A$ (because $R$ is a binary relation on $A$ ). The main thing that we must prove is that the collection of equivalence classes is disjoint, i.e., part (a) of the above definition is satisfied. So suppose that $[x]_{R}$ and $[y]_{R}$ have a common element t. Thus

$$
x R t \quad \text { and } \quad y R t.
$$

But then $xRy$ and by Lemma 3N, $[x]_R = [y]_R$ .

If $R$ is an equivalence relation on $A$ , then we can define the quotient set

$$
A / R = \left\{\left[ x \right] _ {R} \mid x \in A \right\}
$$

whose members are the equivalence classes. (The expression A/R is read “A modulo R.”) We also have the natural map (or canonical map) $\varphi: A \to A/R$ defined by

$$
\varphi (x) = [ x ] _ {R}
$$

for $x\in A$

Example Let $\omega = \{0, 1, 2, \ldots\}$ ; define the binary relation $\sim$ on $\omega$ by

$$
m \sim n \Leftrightarrow m - n \text {   is   divisible   by   } 6.
$$

Then $\sim$ is an equivalence relation on $\omega$ (as you should verify). The quotient set $\omega / \sim$ has six members:

$$
[ 0 ], \quad [ 1 ], \quad [ 2 ], \quad [ 3 ], \quad [ 4 ], \quad [ 5 ],
$$

corresponding to the six possible remainders after division by 6.

Example The relation of congruence of triangles in the plane is an equivalence relation.

Example Textbooks on linear algebra often define vectors in the plane as follows. Let A be the set of all directed line segments in the plane. Two such line segments are considered to be equivalent iff they have the same length and direction. A vector is then defined to be an equivalence class of directed line segments. But to avoid the necessity of dealing explicitly with equivalence relations, books use phrases like “equivalent vectors are regarded as equal even though they are located in different positions,” or “we write PQ = RS to say that PQ and RS have the same length and direction even though they are not identical sets of points,” or simply “we identify two line segments having the same length and direction.”

Example Let $F: A \to B$ and for points in $A$ define

$$
x \sim y \quad \text { iff } \quad F (x) = F (y).
$$

The relation $\sim$ is an equivalence relation on $A$ . There is a unique one-to-one function $\hat{F}: A / \sim \to B$ such that $F = \hat{F} \circ \varphi$ (where $\varphi$ is the natural map as shown in Fig. 13). The value of $\hat{F}$ at a particular equivalence class is the common value of $F$ at the members of the equivalence class.

![](images/b5ec633465885a24d4c9e09b01f3d36fc98881742b4607bee3a12251fa7decf1.jpg)  
Fig. 13. F factors into the natural map followed by a one-to-one function.

The last problem we want to examine in this section is the problem of defining functions on a quotient set. Specifically, assume that R is an equivalence relation on A and that $F: A \rightarrow A$ . We ask whether or not there exists a corresponding function $\hat{F}: A/R \rightarrow A/R$ such that for all $x \in A$ ,

$$
\hat {F} ([ x ] _ {R}) = [ F (x) ] _ {R}
$$

(see Fig. 14). Here we are attempting to define the value of $\hat{F}$ at an equivalence class by selecting a particular member $x$ from the class and then forming $[F(x)]_R$ . But suppose $x_1$ and $x_2$ are in the same equivalence class. Then $\hat{F}$ is not well defined unless $F(x_1)$ and $F(x_2)$ are in the same equivalence class.

![](images/a3049c1d051189f719a08fa4c826f9bf9008843192ceb3f555a7953bd9eb70c6.jpg)  
Fig. 14. This diagram is said to be commutative if $\hat{F} \circ \varphi = \varphi \circ F$ .

Example Consider $\omega / \sim$ where $m \sim n$ iff $m - n$ is divisible by 6. Three functions from $\omega$ into $\omega$ are defined by

$$
F _ {1} (n) = 2 n, \quad F _ {2} (n) = n ^ {2}, \quad F _ {3} (n) = 2 ^ {n}.
$$

In each case we can ask whether there is $\hat{F}_{i}\colon\omega/\sim\to\omega/\sim$ such that for every n in $\omega$ :

$$
\hat {F} _ {1} ([ n ]) = [ 2 n ], \quad \hat {F} _ {2} ([ n ]) = [ n ^ {2} ], \quad \hat {F} _ {3} ([ n ]) = [ 2 ^ {n} ].
$$

It is easy to see that if $m \sim n$ , then $2m \sim 2n$ . Because of this fact $\hat{F}_{1}$ is well defined; that is, there exists a function $\hat{F}_{1}$ satisfying the equation $\hat{F}_{1}([n]) = [2n]$ . No matter what representative m of the equivalence class [n] we look at, we always obtain the same equivalence class [2m]. (For further details, see the proof of Theorem 3Q below.) Similarly if $m \sim n$ , then $m^{2} \sim n^{2}$ , for recall that $m^{2} - n^{2} = (m + n)(m - n)$ . Consequently $\hat{F}_{2}$ is also well defined. On the other hand, $\hat{F}_{3}$ is not well defined. For example, $0 \sim 6$ but $2^{0} = 1 \not\sim 64 = 2^{6}$ . Thus although [0] = [6], we have $[2^{0}] \neq [2^{6}]$ . Hence there cannot possibly exist any function $\hat{F}_{3}$ such that the equation $\hat{F}_{3}([n]) = [2^{n}]$ holds for both n = 0 and n = 6.

In order to formulate a general theorem here, let us say that $F$ is compatible with $R$ iff for all $x$ and $y$ in $A$ ,

$$
x R y \Rightarrow F (x) R F (y).
$$

Theorem 3Q Assume that R is an equivalence relation on A and that $F: A \rightarrow A$ . If F is compatible with R, then there exists a unique $\hat{F}: A/R \rightarrow A/R$ such that

$$
\hat {F} ([ x ] _ {R}) = [ F (x) ] _ {R} \quad \text {   for   all   } x \text {   in   } A.\tag{☆}
$$

If $F$ is not compatible with $R$ , then no such $\hat{F}$ exists. Analogous results apply to functions from $A \times A$ into $A$ .

Proof First assume that $F$ is not compatible; we will show that there can be no $\hat{F}$ satisfying $(\star)$ . The incompatibility tells us that for certain $x$ and $y$ in $A$ we have $xRy$ (and hence $[x] = [y]$ ) but not $F(x)RF(y)$ (and hence $[F(x)] \neq [F(y)]$ ). For $(\star)$ to hold we would need both

$$
\hat {F} ([ x ]) = [ F (x) ] \quad \text { and } \quad \hat {F} ([ y ]) = [ F (y) ].
$$

But this is impossible, since the left sides coincide and the right sides differ.

Now for the converse, assume that $F$ is compatible with $R$ . Since $(\star)$ demands that the pair $\langle [x], [F(x)] \rangle \in \hat{F}$ , we will try defining $\hat{F}$ to be the set of all such ordered pairs:

$$
\hat {F} = \{\langle [ x ], [ F (x) ] \rangle \mid x \in A \}.
$$

The crucial matter is whether this relation $\hat{F}$ is a function. So consider pairs $\langle [x], [F(x)] \rangle$ and $\langle [y], [F(y)] \rangle$ in $\hat{F}$ . The calculation

$$
\begin{array}{r l r l} {[ x ] = [ y ]} & {\Rightarrow} & {x R y} & {\quad \text { by   Lemma   3N }} \\ & {\Rightarrow} & {F (x) R F (y)} & {\quad \text { by   compatibility }} \\ & {\Rightarrow} & {[ F (x) ] = [ F (y) ]} & {\quad \text { by   Lemma   3N }} \end{array}
$$

shows that $\hat{F}$ is indeed a function. The remaining things to check are easier. Clearly $\operatorname{dom} \hat{F} = A / R$ and $\operatorname{ran} \hat{F} \subseteq A / R$ , hence $\hat{F}: A / R \to A / R$ . Finally (☆) holds because $\langle [x], [F(x)] \rangle \in \hat{F}$ .

We leave it to you to explain why $\hat{F}$ is unique, and to formulate the “analogous results” for a binary operation (Exercise 42).

## Exercises

32. (a) Show that $R$ is symmetric iff $R^{-1} \subseteq R$ .

(b) Show that $R$ is transitive iff $R \circ R \subseteq R$ .

33. Show that $R$ is a symmetric and transitive relation iff $R = R^{-1} \circ R$ .

34. Assume that A is a nonempty set, every member of which is a transitive relation.

(a) Is the set $\bigcap \mathcal{A}$ a transitive relation?

(b) Is $\bigcup \mathcal{A}$ a transitive relation?

35. Show that for any $R$ and $x$ , we have $[x]_R = R[[\{x\}]]$ .

36. Assume that $f \colon A \to B$ and that $R$ is an equivalence relation on $B$ . Define $Q$ to be the set

$$
\{\langle x, y \rangle \in A \times A | \langle f (x), f (y) \rangle \in R \}.
$$

Show that $Q$ is an equivalence relation on $A$ .

37. Assume that $\Pi$ is a partition of a set $A$ . Define the relation $R_{\Pi}$ as follows:

$$
x R _ {\Pi} y \Leftrightarrow (\exists B \in \Pi) (x \in B \& y \in B).
$$

Show that $R_{\Pi}$ is an equivalence relation on A. (This is a formalized version of the discussion at the beginning of this section.)

38. Theorem 3P shows that A/R is a partition of A whenever R is an equivalence relation on A. Show that if we start with the equivalence relation $R_{\Pi}$ of the preceding exercise, then the partition $A/R_{\Pi}$ is just $\Pi$ .

39. Assume that we start with an equivalence relation R on A and define $\Pi$ to be the partition A/R. Show that $R_{\Pi}$ , as defined in Exercise 37, is just R.

40. Define an equivalence relation R on the set P of positive integers by

mRn $\Leftrightarrow$ m and n have the same number of prime factors.

Is there a function $f: P / R \to P / R$ such that $f([n]_R) = [3n]_R$ for each $n$ ? 41. Let $\mathbb{R}$ be the set of real numbers and define the relation $Q$ on $\mathbb{R} \times \mathbb{R}$ by $\langle u, v \rangle Q\langle x, y \rangle$ iff $u + y = x + v$ .

(a) Show that $Q$ is an equivalence relation on $\mathbb{R} \times \mathbb{R}$ .

(b) Is there a function $G \colon (\mathbb{R} \times \mathbb{R}) / Q \to (\mathbb{R} \times \mathbb{R}) / Q$ satisfying the equation

$$
G ([ \langle x, y \rangle ] _ {Q}) = [ \langle x + 2 y, y + 2 x \rangle ] _ {Q}?
$$

42. State precisely the “analogous results” mentioned in Theorem 3Q. (This will require extending the concept of compatibility in a suitable way.)

## ORDERING RELATIONS

The first example of a relation we gave in this chapter was the ordering relation

$$
\{\langle 2, 3 \rangle , \langle 2, 5 \rangle , \langle 3, 5 \rangle \}
$$

on the set $\{2, 3, 5\}$ ; recall Fig. 7. Now we want to consider ordering relations on other sets. In the present section we will set forth the basic concepts, which will be useful in Chapter 5. A more thorough discussion of ordering relations can be found in Chapter 7.

Our first need is for a definition. What, in general, should it mean to say that R is an ordering relation on a set A? Well, for one thing R should tell us, given any distinct x and y in A, just which one is smaller. No x should be smaller than itself. And furthermore if x is less than y and y is less than z, then x should be less than z. The following definition captures these ideas.

Definition Let A be any set. A linear ordering on A (also called a total ordering on A) is a binary relation R on A (i.e., $R \subseteq A \times A$ ) meeting the following two conditions:

(a) $R$ is a transitive relation; i.e., whenever $xRy$ and $yRz$ , then $xRz$ .

(b) $R$ satisfies trichotomy on $A$ , by which we mean that for any $x$ and $y$ in $A$ exactly one of the three alternatives

$$
x R y, \quad x = y, \quad y R x
$$

holds.

To clarify the meaning of trichotomy, consider first the special case where x and y are the same member of A (with two names). Then trichotomy demands that exactly one of

$$
x R x, \qquad x = x, \qquad x R x
$$

holds. Since the middle alternative certainly holds, we can conclude that xRx never holds.

Next consider the case where x and y are two distinct members of A. Then the middle alternative x = y fails, so trichotomy demands that either xRy or yRx (but not both). Thus we have proved the following:

Theorem 3R Let R be a linear ordering on A.

(i) There is no $x$ for which $xRx$ .

(ii) For distinct $x$ and $y$ in $A$ , either $xRy$ or $yRx$ .

In fact for a transitive relation R on A, conditions (i) and (ii) are equivalent to trichotomy. A relation meeting condition (i) is called irreflexive; one meeting condition (ii) is said to be connected on A.

Note also that a linear ordering R can never lead us in circles, e.g., there cannot exist a circle such as

$$
x _ {1} R x _ {2}, \quad x _ {2} R x _ {3}, \quad x _ {3} R x _ {4}, \quad x _ {4} R x _ {5}, \quad x _ {5} R x _ {1}.
$$

This is because if we had such a circle, then by transitivity $x_{1}Rx_{1}$ , contradicting part (i) of the foregoing theorem.

Of course “R” is not our favorite symbol for a linear ordering; our favorite is “<.” For then we can write “x < y” to mean that the pair $\langle x, y \rangle$ is a member of the set <.

If $<$ is a linear ordering on $A$ and if $A$ is not too large, then we can draw a picture of the ordering. We represent the members of $A$ by dots, placing the dot for $x$ below the dot for $y$ whenever $x < y$ . Then we add vertical lines to connect the dots. The resulting picture has the points of $A$ stretched out along a line, in the correct order. (The adjective “linear” reflects the possibility of drawing this picture.)

Figure 15 contains three such pictures. Part (a) is the picture for the usual order on $\{2, 3, 5\}$ . Parts (b) and (c) portray the usual order on the natural numbers and on the integers, respectively. (Infinite pictures are more difficult to draw than finite pictures.)

In addition to the concept of linear ordering, there is the more general concept of a partial ordering. Partial orderings are discussed in the first section of Chapter 7. In fact you might want to read that section next, before going on to Chapter 4. At least look at Figs. 43 and 44 there, which contrast with Fig. 15.

![](images/1c081938591e6aaf112836abe0932fd54acb8a9fff5ee756ff03f354ef4c9dca.jpg)  
Fig. 15. Linear orderings look linear.

## Exercises

43. Assume that $R$ is a linear ordering on a set $A$ . Show that $R^{-1}$ is also a linear ordering on $A$ .

44. Assume that $<$ is a linear ordering on a set $A$ . Assume that $f: A \to A$ and that $f$ has the property that whenever $x < y$ , then $f(x) < f(y)$ . Show that $f$ is one-to-one and that whenever $f(x) < f(y)$ , then $x < y$ .

45. Assume that $<_{A}$ and $<_{B}$ are linear orderings on $A$ and $B$ , respectively. Define the binary relation $<_{L}$ on the Cartesian product $A \times B$ by:

$$
\langle a _ {1}, b _ {1} \rangle <   _ {\mathrm{L}} \langle a _ {2}, b _ {2} \rangle \quad \text { iff } \quad \text { either   } a _ {1} <   _ {A} a _ {2} \text {   or   } (a _ {1} = a _ {2} \& b _ {1} <   _ {B} b _ {2})
$$

Show that $<_{L}$ is a linear ordering on $A \times B$ . (The relation $<_{L}$ is called lexicographic ordering, being the ordering used in making dictionaries.)

## Review Exercises

46. Evaluate the following sets:

(a) $\bigcap \bigcap \langle x, y \rangle$ .

(b) $\bigcap \bigcap \bigcap \{\langle x, y \rangle\}^{-1}$ .

47. (a) Find all of the functions from $\{0, 1, 2\}$ into $\{3, 4\}$ .

(b) Find all of the functions from $\{0, 1, 2\}$ onto $\{3, 4, 5\}$ .

48. Let $T$ be the set $\{\varnothing, \{\varnothing\}\}$ .

(a) Find all of the ordered pairs, if any, in $\mathcal{PT}$ .

(b) Evaluate and simplify: $(\mathcal{PT})^{-1} \circ (\mathcal{PT} \upharpoonright \{\emptyset\})$

49. Find as many equivalence relations as you can on the set $\{0, 1, 2\}$ .

50. (a) Find a linear ordering on $\{0, 1, 2, 3\}$ that contains the ordered pairs $\langle 0, 3 \rangle$ and $\langle 2, 1 \rangle$ .

(b) Now find a different one meeting the same conditions.

51. Find as many linear orderings as possible on the set $\{0, 1, 2\}$ that contain the pair $\langle2, 0\rangle$ .

52. Suppose that $A \times B = C \times D$ . Under what conditions can we conclude that $A = C$ and $B = D$ ?

53. Show that for any sets $R$ and $S$ we have $(R \cup S)^{-1} = R^{-1} \cup S^{-1}$ , $(R \cap S)^{-1} = R^{-1} \cap S^{-1}$ , and $(R - S)^{-1} = R^{-1} - S^{-1}$ .

54. Prove that the following equations hold for any sets.

(a) $A \times (B \cap C) = (A \times B) \cap (A \times C)$ .

(b) $A \times (B \cup C) = (A \times B) \cup (A \times C)$ .

(c) $A \times (B - C) = (A \times B) - (A \times C).$

55. Answer "yes" or "no." Where the answer is negative, supply a counterexample.

(a) Is it always true that $(A\times A)\cup (B\times C) = (A\cup B)\times (A\cup C)?$

(b) Is it always true that $(A\times A)\cap (B\times C) = (A\cap B)\times (A\cap C)?$

56. Answer "yes" or "no." Where the answer is negative, supply a counterexample.

(a) Is $\operatorname{dom}(R \cup S)$ always the same as $\operatorname{dom} R \cup \operatorname{dom} S$ ?

(b) Is $\operatorname{dom}(R \cap S)$ always the same as $\operatorname{dom} R \cap \operatorname{dom} S$ ?

57. Answer “yes” or “no.” Where the answer is negative, supply a counterexample.

(a) Is $R \circ (S \cup T)$ always the same as $(R \circ S) \cup (R \circ T)$ ?

(b) Is $R \circ (S \cap T)$ always the same as $(R \circ S) \cap (R \circ T)$ ?

58. Give an example to show that $F[F^{-1}[S]]$ is not always the same as $S$ .

59. Show that for any sets $Q \upharpoonright (A \cap B) = (Q \upharpoonright A) \cap (Q \upharpoonright B)$ and $Q \upharpoonright (A - B) = (Q \upharpoonright A) - (Q \upharpoonright B)$ .

60. Prove that for any sets $(R \circ S) \upharpoonright A = R \circ (S \upharpoonright A)$ .

# NATURAL NUMBERS

There are, in general, two ways of introducing new objects for mathematical study: the axiomatic approach and the constructive approach. The axiomatic approach is the one we have used for sets. The concept of set is one of our primitive notions, and we have adopted a list of axioms dealing with the primitive notions.

Now consider the matter of introducing the natural numbers $^{1}$

## 0, 1, 2, ...

for further study. An axiomatic approach would consider “natural number” as a primitive notion and would adopt a list of axioms. Instead we will use the constructive approach for natural numbers. We will define natural numbers in terms of other available objects (sets, of course). In place of axioms for numbers we will be able to prove the necessary properties of numbers from known properties of sets.

$^{1}$ There is a curious point of terminology here. Is 0 a natural number? With surprising consistency, the present usage is for school books (through high-school level) to exclude 0 from the natural numbers, and for upper-division college-level books to include 0. Freshman and sophomore college books are in the transition zone. In this book we include 0 among the natural numbers.

Constructing the natural numbers in terms of sets is part of the process of “embedding mathematics in set theory.” The process will be continued in Chapter 5 to obtain more exotic numbers, such as $\sqrt{2}$ .

## INDUCTIVE SETS

First we need to define natural numbers as suitable sets. Now numbers do not at first glance appear to be sets. Not that it is an easy matter to say what numbers do appear to be. They are abstract concepts, which are slippery things to handle. (See, for example, the section on “Two” in Chapter 5.) Nevertheless, we can construct specific sets that will serve perfectly well as numbers. In fact this can be done in a variety of ways. In 1908, Zermelo proposed to use

$$
\varnothing , \{\varnothing \}, \{\{\varnothing \} \}, \dots
$$

as the natural numbers. Later von Neumann proposed an alternative, which has several advantages and has become standard. The guiding principle behind von Neumann's construction is to make each natural number be the set of all smaller natural numbers. Thus we define the first four natural numbers as follows:

$$
\begin{array}{l} 0 = \varnothing , \\ 1 = \{\varnothing \} = \{\varnothing \}, \\ 2 = \{0, 1 \} = \{\varnothing , \{\varnothing \} \}, \\ 3 = \{0, 1, 2 \} = \{\varnothing , \{\varnothing \}, \{\varnothing , \{\varnothing \} \} \}. \end{array}
$$

We could continue in this way to define 17 or any chosen natural number. Notice, for example, that the set 3 has three members. It has been selected from the class of all three-member sets to represent the size of the sets in that class.

This construction of the numbers as sets involves some extraneous properties that we did not originally expect. For example,

$$
0 \in 1 \in 2 \in 3 \in \dots
$$

and

$$
0 \subseteq 1 \subseteq 2 \subseteq 3 \subseteq \dots .
$$

But these properties can be regarded as accidental side effects of the definition. They do no harm, and actually will be convenient at times.

Although we have defined the first four natural numbers, we do not yet have a definition of what it means in general for something to be a natural number. That is, we have not defined the set of all natural numbers. Such a definition cannot rely on linguistic devices such as three dots or phrases like “and so forth.” First we define some preliminary concepts.

Definition For any set $a$ , its successor $a^{+}$ is defined by

$$
a ^ {+} = a \cup \{a \}.
$$

A set A is said to be inductive iff $\varnothing \in A$ and it is “closed under successor,” i.e.,

$$
(\forall a \in A) a ^ {+} \in A.
$$

In terms of the successor operation, the first few natural numbers can be characterized as

$$
0 = \varnothing , \quad 1 = \varnothing^ {+}, \quad 2 = \varnothing^ {+ +}, \quad 3 = \varnothing^ {+ + +}, \dots
$$

These are all distinct, e.g., $\varnothing^{+} \neq \varnothing^{++}$ (Exercise 1). And although we have not yet given a formal definition of “infinite,” we can see informally that any inductive set will be infinite.

We have as yet no axioms that provide for the existence of infinite sets. There are indeed infinitely many distinct sets whose existence we could establish. But there is no one set having infinitely many members that we can prove to exist. Consequently we cannot yet prove that any inductive set exists. We now correct that fault.

Infinity Axiom There exists an inductive set:

$$
(\exists A) [ \emptyset \in A \& (\forall a \in A) a ^ {+} \in A ].
$$

Armed with this axiom, we can now define the concept of natural number.

Definition A natural number is a set that belongs to every inductive set.

We next prove that the collection of all natural numbers constitutes a set.

Theorem 4A There is a set whose members are exactly the natural numbers.

Proof Let A be an inductive set; by the infinity axiom it is possible to find such a set. By a subset axiom there is a set w such that for any x,

$x \in w \Leftrightarrow x \in A \& x$ belongs to every other inductive set

$\Leftrightarrow x$ belongs to every inductive set.

(This proof is essentially the same as the proof of Theorem 2B.)

The set of all natural numbers is denoted by a lowercase Greek omega:

$$
\begin{array}{r c l} x \in \omega & \Leftrightarrow & x \text {   is   a   natural   number } \\ & \Leftrightarrow & x \text {   belongs   to   every   inductive   set. } \end{array}
$$

In terms of classes, we have

$$
\omega = \bigcap \{A \mid A \text {   is   inductive } \},
$$

but the class of all inductive sets is not a set.

Theorem 4B $\omega$ is inductive, and is a subset of every other inductive set.

Proof First of all, $\varnothing \in \omega$ because $\varnothing$ belongs to every inductive set. And second,

$$
\begin{array}{r c l} a \in \omega & \Rightarrow & a \text { belongs   to   every   inductive   set } \\ & \Rightarrow & a ^ {+} \text { belongs   to   every   inductive   set } \\ & \Rightarrow & a ^ {+} \in \omega . \end{array}
$$

Hence $\omega$ is inductive. And clearly $\omega$ is included in every other inductive set.

Since $\omega$ is inductive, we know that $0 (= \varnothing)$ is in $\omega$ . It then follows that $1 (= 0^{+})$ is in $\omega$ , as are $2 (= 1^{+})$ and $3 (= 2^{+})$ . Thus 0, 1, 2, and 3 are natural numbers. Unnecessary extraneous objects have been excluded from $\omega$ , since $\omega$ is the smallest inductive set. This fact can also be restated as follows.

Induction Principle for $\omega$ Any inductive subset of $\omega$ coincides with $\omega$ .

Suppose, for example, that we want to prove that for every natural number $n$ , the statement $_n$ holds. We form the set

$$
T = \{n \in \omega | - n - \}
$$

of natural numbers for which the desired conclusion is true. If we can show that $T$ is inductive, then the proof is complete. Such a proof is said to be a proof by induction. The next theorem gives a very simple example of this method.

Theorem 4C Every natural number except 0 is the successor of some natural number.

Proof Let $T = \{n \in \omega \mid \text{either } n = 0 \text{ or } (\exists p \in \omega) n = p^{+}\}$ . Then $0 \in T$ . And if $k \in T$ , then $k^{+} \in T$ . Hence by induction, $T = \omega$ .

## Exercise

See also the Review Exercises at the end of this chapter.

1. Show that $1 \neq 3$ , i.e., that $\varnothing^{+} \neq \varnothing^{+++}$ .

## PEANO'S POSTULATES $^{2}$

In 1889, Peano published a study giving an axiomatic approach to the natural numbers. He showed how the properties of natural numbers could be developed on the basis of a small number of axioms. Although he

![](images/465b708bbb455efb3fa386d46c7ddbd482e6f4359e40c063e0c8aecad11a32b8.jpg)  
(a)

![](images/fdef5ab2fa4b6a983fa73e48494aef9ee5e88e486e2138fbe2229ced32875a28.jpg)  
(b)

![](images/85872ec1b8518077dfd75bcbb9bf8da955764841354eff2f892331f3a7713f18.jpg)  
(c)  
Fig. 16. Any Peano system must behave like (c).

attributed the formulation of the axioms to Dedekind, the axioms are generally known as “Peano’s postulates.” We will first show that the set $\omega$ we have constructed satisfies Peano’s postulates, i.e., the “postulates” become provable when applied to $\omega$ . Later we will prove that anything satisfying Peano’s postulates is, in a certain specific sense, “just like” $\omega$ .

To formulate these results more accurately, we must define the concept of a Peano system. First of all, if $S$ is a function and $A$ is a subset of $\operatorname{dom} S$ , then $A$ is said to be closed under $S$ iff whenever $x \in A$ , then $S(x) \in A$ . (This can equivalently be expressed as $S[[A]] \subseteq A$ .) Define a Peano system to be a triple $\langle N, S, e \rangle$ consisting of a set $N$ , a function $S: N \to N$ , and a member $e \in N$ such that the following three conditions are met:

(i) $e \notin \operatorname{ran} S$ .

(ii) $S$ is one-to-one.

(iii) Any subset A of N that contains e and is closed under S equals N itself.

The condition “ $e \notin ran S$ ” rules out loops as in Fig. 16a—here the arrows indicate the action of S. And the requirement that S be one-to-one rules out the system of Fig. 16b. Consequently any Peano system must, in part, look like Fig. 16c. The last of the three conditions is the Peano induction postulate. Its function is to rule out any points other than the ones we expect. We expect the system to contain $e$ , $S(e)$ , $SS(e)$ , $SSS(e)$ , .... The Peano induction postulate replaces the three dots with a precise set-theoretic condition, stating that nothing smaller than $N$ itself can contain $e$ and be closed under $S$ .

First we want to show that $\omega$ (with the successor operation and 0) is a Peano system. In particular, this will show that some Peano system exists. Let $\sigma$ be the restriction of the successor operation to $\omega$ :

$$
\sigma = \{\langle n, n ^ {+} \rangle | n \in \omega \}.
$$

Theorem 4D $\langle\omega,\sigma,0\rangle$ is a Peano system.

Proof Since $\omega$ is inductive, we have $0 \in \omega$ and $\sigma: \omega \to \omega$ . The Peano induction postulate, as applied to $\langle \omega, \sigma, 0 \rangle$ , states that any subset $A$ of $\omega$ containing 0 and closed under $\sigma$ equals $\omega$ itself. This is just the induction principle for $\omega$ . Clearly $0 \notin \operatorname{ran} \sigma$ , since $n^{+} \neq \emptyset$ . It remains only to show that $\sigma$ is one-to-one. For that purpose (and others) we will use the concept of a transitive set.

Definition A set $A$ is said to be a transitive set iff every member of a member of $A$ is itself a member of $A$ :

$$
x \in a \in A \Rightarrow x \in A.
$$

This condition can also be stated in any of the following (equivalent) ways:

$$
\bigcup A \subseteq A,   a \in A \Rightarrow a \subseteq A,   A \subseteq \mathscr {P} A.
$$

At this point we have violated a basic rule—we have defined “transitive” to mean two different things. In Chapter 3 we said that A is transitive if whenever xAy and yAz, then xAz. And now we define A to be a transitive set if a very different condition is met. But both usages of the word are well established. And so we will learn to live with the ambiguity. In practice, the context will make clear which sense of “transitive” is wanted. Furthermore when the concept of Chapter 3 is meant, we will refer to A as a transitive relation (luckily A will be a relation), reserving the phrase “transitive set” for the concept defined above.

Example The set $\{\varnothing,\{\{\varnothing\}\}\}$ is not a transitive set. This is because

$$
\{\varnothing \} \in \{\{\varnothing \} \} \in \{\varnothing , \{\{\varnothing \} \} \},
$$

but $\{\varnothing\} \notin \{\varnothing, \{\{\varnothing\}\}\}$ . Also $\{0, 1, 5\}$ is not a transitive set, since $4 \in 5 \in \{0, 1, 5\}$ whereas $4 \notin \{0, 1, 5\}$ .

Theorem 4E For a transitive set $a$ ,

$$
\bigcup (a ^ {+}) = a.
$$

Proof We proceed to calculate $\bigcup a^{+}$ :

$$
\begin{array}{r l} \bigcup a ^ {+} & = \bigcup (a \cup \{a \}) \\ & = \bigcup a \cup \bigcup \{a \} \\ & = \bigcup a \cup a \\ & = a. \end{array} \quad \text { by   Exercise   21   of   Chapter   2 }
$$

The last step is justified by the fact that $\bigcup a \subseteq a$ for a transitive set $a$ .

Theorem 4F Every natural number is a transitive set.

Proof by induction We form the set of numbers for which the theorem is true; let $T = \{n \in \omega \mid n$ is a transitive set}. It suffices to show that T is inductive, for then $T = \omega$ .

Trivially $0 \in T$ . If $k \in T$ , then

$$
\begin{array}{r l} \bigcup (k ^ {+}) = k & \text { by   the   preceding   theorem } \\ \subseteq k ^ {+}, \end{array}
$$

whence $k^{+} \in T$ . Thus $T$ is inductive.

We can now complete the proof of Theorem 4D; it remained for us to show that the successor operation on $\omega$ is one-to-one. If $m^{+} = n^{+}$ for $m$ and $n$ in $\omega$ , then $\bigcup (m^{+}) = \bigcup (n^{+})$ . But since $m$ and $n$ are transitive sets, we have $\bigcup (m^{+}) = m$ and $\bigcup (n^{+}) = n$ by Theorem 4E. Hence $m = n$ .

Theorem 4G The set $\omega$ is a transitive set.

This theorem can be stated as: Every natural number is itself a set of natural numbers. We will later strengthen this to: Every natural number is the set of all smaller natural numbers.

Proof by induction We want to show that $(\forall n\in \omega)n\subseteq \omega$ . Form the set of $n$ 's for which this holds:

$$
T = \{n \in \omega \mid n \subseteq \omega \}.
$$

We must verify that $T$ is inductive. Clearly $0 \in T$ . If $k \in T$ , then we have

$$
k \subseteq \omega \quad \text { and } \quad \{k \} \subseteq \omega ,
$$

whereupon $k \cup \{k\} \subseteq \omega$ , thus showing that $k^{+} \in T$ . And so $T$ is inductive and therefore coincides with $\omega$ .

## Exercises

2. Show that if $a$ is a transitive set, then $a^+$ is also a transitive set.

3. (a) Show that if $a$ is a transitive set, then $\mathcal{P}a$ is also a transitive set. (b) Show that if $\mathcal{P}a$ is a transitive set, then $a$ is also a transitive set.

4. Show that if $a$ is a transitive set, then $\bigcup a$ is also a transitive set.

5. Assume that every member of $\mathcal{A}$ is a transitive set.

(a) Show that $\bigcup \mathcal{A}$ is a transitive set.

(b) Show that $\bigcap \mathcal{A}$ is a transitive set (assuming that $\mathcal{A}$ is nonempty).

6. Prove the converse to Theorem 4E: If $\bigcup (a^{+}) = a$ , then $a$ is a transitive set.

## RECURSION ON ω

Consider the following guessing game. Suppose I am thinking of a function $h: \omega \to A$ . Possibly I am reluctant to tell you directly what the values of this function are. Instead I reveal (i) what $h(0)$ is, and (ii) a function $F: A \to A$ such that $h(n^{+}) = F(h(n))$ for all $n \in \omega$ . This then gives away all the information; you can compute successively

$$
\begin{array}{l} h (0), \\ h (1) = F (h (0)), \\ h (2) = F (h (1)), \end{array}
$$

and so forth.

Now for a harder problem. Suppose we are given a set A, an element $a \in A$ , and a function $F: A \to A$ . How can we show that there exists a function $h: \omega \to A$ such that (i) $h(0) = a$ , and (ii) $h(n^{+}) = F(h(n))$ for each $n \in \omega$ . The preceding paragraph tells how to compute h if it exists. But we now want to prove that there exists a set h that is a function meeting the above conditions.

Recursion Theorem on $\omega$ Let $A$ be a set, $a \in A$ , and $F: A \to A$ . Then there exists a unique function $h: \omega \to A$ such that

$$
h (0) = a,
$$

and for every n in $\omega$ ,

$$
h (n ^ {+}) = F (h (n)).
$$

Proof $^{3}$ The idea is to let h be the union of many approximating functions. For the purposes of this proof, call a function v acceptable iff dom $v \subseteq \omega$ , ran $v \subseteq A$ , and the following conditions hold:

(i) If $0 \in \operatorname{dom} v$ , then $v(0) = a$ .

(ii) If $n^+ \in \operatorname{dom} v$ (where $n \in \omega$ ), then also $n \in \operatorname{dom} v$ and $v(n^+) = F(v(n))$ .

Let $\mathcal{K}$ be the collection of all acceptable functions, and let $h = \bigcup \mathcal{K}$ . Thus

$$
\begin{array}{l l} (\star) & \langle n, y \rangle \in h \quad \text { iff } \quad \langle n, y \rangle \text {   is   a   member   of   some   acceptable   } v \\ & \text { iff } \quad v (n) = y \text {   for   some   acceptable   } v. \end{array}
$$

We claim that this h meets the demands of the theorem. This claim can be broken down into four parts. The four parts involve showing that (1) h is a function, (2) h is acceptable, (3) dom h is all of $\omega$ , and (4) h is unique.

1. We first claim that h is a function. (Proving this will, in effect, amount to showing .that two acceptable functions always agree with each other whenever both are defined.) Let S be the set of natural numbers at which there is no more than one candidate for $h(n)$ :

$$
S = \{n \in \omega \mid \text {   for   at   most   one   } y, \langle n, y \rangle \in h \}.
$$

We must check that $S$ is inductive. If $\langle 0, y_1 \rangle \in h$ and $\langle 0, y_2 \rangle \in h$ , then by (☆) there exist acceptable $v_1$ and $v_2$ such that $v_1(0) = y_1$ and $v_2(0) = y_2$ . But by (i) it follows that $y_1 = a = y_2$ . Thus $0 \in S$ .

Next suppose that $k \in S$ ; we seek to show that $k^{+} \in S$ . Toward that end suppose that $\langle k^{+}, y_{1} \rangle \in h$ and $\langle k^{+}, y_{2} \rangle \in h$ . Again there must exist acceptable $v_{1}$ and $v_{2}$ such that $v_{1}(k^{+}) = y_{1}$ and $v_{2}(k^{+}) = y_{2}$ . By condition (ii) it follows that

$$
y _ {1} = v _ {1} (k ^ {+}) = F (v _ {1} (k)) \quad \text { and } \quad y _ {2} = v _ {2} (k ^ {+}) = F (v _ {2} (k)).
$$

But since $k \in S$ , we have $v_{1}(k) = v_{2}(k)$ . (This is because $\langle k, v_{1}(k) \rangle$ and $\langle k, v_{2}(k) \rangle$ are in $h$ .) Therefore

$$
y _ {1} = F (v _ {1} (k)) = F (v _ {2} (k)) = y _ {2}.
$$

This shows that $k^{+} \in S$ . Hence S is inductive and coincides with $\omega$ . Consequently h is a function.

2. Next we claim that $h$ itself is acceptable. We have just seen that $h$ is a function, and it is clear from $(\star)$ that $\operatorname{dom} h \subseteq \omega$ and $\operatorname{ran} h \subseteq A$ .

First examine (i). If $0 \in \operatorname{dom} h$ , then there must be some acceptable $v$ with $v(0) = h(0)$ . Since $v(0) = a$ , we have $h(0) = a$ .

Next examine (ii). Assume $n^{+} \in dom h$ . Again there must be some acceptable v with $v(n^{+}) = h(n^{+})$ . Since v is acceptable we have $n \in dom v$ (and $v(n) = h(n)$ ) and

$$
h (n ^ {+}) = v (n ^ {+}) = F (v (n)) = F (h (n)).
$$

Thus $h$ satisfies (ii) and so is acceptable.

3. We now claim that $dom h = \omega$ . It suffices to show that dom h is inductive. The function $\{\langle 0, a \rangle\}$ is acceptable and hence $0 \in dom h$ . Suppose that $k \in dom h$ ; we seek to show that $k^{+} \in dom h$ . If this fails, then look at

$$
v = h \cup \{\langle k ^ {+}, F (h (k)) \rangle \}.
$$

Then $v$ is a function, dom $v \subseteq \omega$ , and ran $v \subseteq A$ . We will show that $v$ is acceptable.

Condition (i) holds since $v(0) = h(0) = a$ . For condition (ii) there are two cases. If $n^{+} \in dom v$ where $n^{+} \neq k^{+}$ , then $n^{+} \in dom h$ and $v(n^{+}) = h(n^{+}) = F(h(n)) = F(v(n))$ . The other case occurs if $n^{+} = k^{+}$ . Since the successor operation is one-to-one, n = k. By assumption $k \in dom h$ . Thus

$$
v (k ^ {+}) = F (h (k)) = F (v (k))
$$

and (ii) holds. Hence $v$ is acceptable. But then $v \subseteq h$ , so that $k^{+} \in \operatorname{dom} h$ after all. So $\operatorname{dom} h$ is inductive and therefore coincides with $\omega$ .

4. Finally we claim that $h$ is unique. For let $h_1$ and $h_2$ both satisfy the conclusion of the theorem. Let $S$ be the set on which $h_1$ and $h_2$ agree:

$$
S = \{n \in \omega \mid h _ {1} (n) = h _ {2} (n) \}.
$$

Then $S$ is inductive; we leave the details of this to Exercise 7. Hence $S = \omega$ and $h_1 = h_2$ .

Examples Let Z be the set of all integers, positive, negative, and zero:

$$
\mathbb {Z} = \{\dots , - 1, 0, 1, 2, \dots \}.
$$

There is no function $h: \mathbb{Z} \to \mathbb{Z}$ such that for every $a \in \mathbb{Z}$ ,

$$
h (a + 1) = h (a) ^ {2} + 1.
$$

(For notice that $h(a) > h(a - 1) > h(a - 2) > \cdots > 0$ .) Recursion on $\omega$ relies on there being a starting point 0. Z has no analogous starting point.

For another example, let

$$
F (a) = \left\{ \begin{array}{l l} a + 1 & \quad \text { if } \quad a <   0, \\ a & \quad \text { if } \quad a \geq 0. \end{array} \right.
$$

Then there are infinitely many functions $h \colon \mathbb{Z} \to \mathbb{Z}$ such that $h(0) = 0$ and for every $a$ in $\mathbb{Z}$ , $h(a + 1) = F(h(a))$ . The graph of one such function is shown in Fig. 17.

Digression There is a classic erroneous proof of the recursion theorem that people have sometimes tried (even in print!) to give. The error is easier to analyze if we apply it not to $\omega$ but instead to an arbitrary Peano system $\langle N, S, e \rangle$ . Given any a in A and any function $F: A \to A$ , there is a unique function $h: N \to A$ such that $h(e) = a$ and $h(S(x)) = F(h(x))$ for each x in N. The erroneous proof of this statement runs as follows:

"We apply the Peano induction postulate to dom h. First of all, we are

![](images/7a3bc5ad7245c5edabc84a3541bee0fd64d76bfd2d985a2e248ffae8cdfa9c6f.jpg)  
Fig. 17. $h(a + 1)$ is $h(a) + 1$ when $h(a) < 0$ and is $h(a)$ when $h(a) \geq 0$ .

told that $h(e) = a$ , and so $h$ is defined at $e$ , i.e., $e \in \operatorname{dom} h$ . And whenever $x \in \operatorname{dom} h$ then immediately $h(S(x)) = F(h(x))$ , so $S(x) \in \operatorname{dom} h$ as well. Hence $\operatorname{dom} h$ is closed under $S$ . It follows (by induction) that $\operatorname{dom} h = N$ , i.e., $h$ is defined throughout $N$ .

What is wrong? Well, for one thing, the proof talks about the function h before any such function is known to exist. One might think that a little rewording would get around this objection. But no, a closer examination of the proof shows that it does not utilize conditions (i) and (ii) in the definition of Peano systems. The recursion theorem is in general false for systems not meeting those conditions, such as the systems of Fig. 16a or Fig. 16b. So any correct proof of recursion absolutely must make use of conditions (i) and (ii), as well as using induction. (Our proof of recursion on $\omega$ uses these conditions in part 3.)

Our first application of the recursion theorem will be to show that any Peano system is “just like” $\langle\omega,\sigma,0\rangle$ . There are other Peano systems; for example, let N be the set $\{1,2,4,8,\ldots\}$ of powers of 2, let $S(n)=2n$ , and let e=1. Then $\langle N,S,e\rangle$ is a Peano system. The following theorem expresses the structural similarity between this Peano system and $\langle\omega,\sigma,0\rangle$ .

Theorem 4H Let $\langle N, S, e \rangle$ be a Peano system. Then $\langle \omega, \sigma, 0 \rangle$ is isomorphic to $\langle N, S, e \rangle$ , i.e., there is a function h mapping $\omega$ one-to-one onto N in a way that preserves the successor operation

$$
h (\sigma (n)) = S (h (n))
$$

and the zero element

$$
h (0) = e.
$$

Remark The equation $h(\sigma(n)) = S(h(n))$ (together with $h(0) = e$ ) implies that $h(1) = S(e)$ , $h(2) = S(S(e))$ , $h(3) = S(S(S(e)))$ , etc. Thus the situation must be as shown in Fig. 18.

![](images/2504c05dcafeb420ccdba64221e5f7b234d1f05dacc5132de852ac7c15ca7fb8.jpg)  
Fig. 18. Isomorphism of Peano systems.

Proof By the recursion theorem there is a unique function $h: \omega \to N$ such that $h(0) = e$ and for all $n \in \omega$ , $h(n^{+}) = S(h(n))$ . It remains to show that $h$ is one-to-one and that ran $h = N$ .

To show that ran h = N we use the Peano induction postulate for $\langle N, S, e \rangle$ . Clearly $e \in \operatorname{ran} h$ . Also for any $x \in \operatorname{ran} h$ (say $x = h(n)$ ) we have $S(x) \in \operatorname{ran} h$ (since $S(x) = h(n^{+})$ ). Hence by the Peano induction postulate applied to ran h, we have ran h = N.

To show that h is one-to-one we use induction in $\omega$ . Let

$T = \{n\in \omega | \text{ for every } m \text{ in } \omega \text{ different from } n, h(m)\neq h(n)\} .$

First we claim that $0 \in T$ . Any $m \in \omega$ different from 0 must be of the form $p^{+}$ (by Theorem 4C). And $h(p^{+}) = S(h(p)) \neq e$ since $e \notin \operatorname{ran} S$ . Hence $h(0) = e \neq h(p^{+})$ , and consequently $0 \in T$ .

Now assume that $k \in T$ and consider $k^{+}$ . Suppose that $h(k^{+}) = h(m)$ . Then $m \neq 0$ by the preceding paragraph, so $m = p^{+}$ for some $p$ . Thus

$$
S (h (k)) = h (k ^ {+}) = h (p ^ {+}) = S (h (p)).
$$

Since $S$ is one-to-one, this leaves the equation $h(k) = h(p)$ . Since $k \in T$ , we have $k = p$ . Hence $k^{+} = p^{+} = m$ . This shows that $k^{+} \in T$ . So $T$ is inductive, and thus coincides with $\omega$ . Consequently $h$ is one-to-one.

Theorems 4D and 4H relate the constructive approach to the natural numbers and the axiomatic approach. Theorem 4D shows that Peano's postulates are true of the number system we have constructed. And Theorem 4H shows that the number system we have constructed is, "to within isomorphism," the only system satisfying Peano's postulates.

## Exercises

7. Complete part 4 of the proof of the recursion theorem on $\omega$ .

8. Let $f$ be a one-to-one function from $A$ into $A$ , and assume that $c \in A - \operatorname{ran} f$ . Define $h: \omega \to A$ by recursion:

$$
\begin{array}{c} h (0) = c, \\ h (n ^ {+}) = f (h (n)). \end{array}
$$

Show that h is one-to-one.

9. Let $f$ be a function from $B$ into $B$ , and assume that $A \subseteq B$ . We have two possible methods for constructing the "closure" $C$ of $A$ under $f$ . First define $C^*$ to be the intersection of the closed supersets of $A$ :

$$
C ^ {*} = \bigcap \{X \mid A \subseteq X \subseteq B \& f [ [ X ] ] \subseteq X \}.
$$

Alternatively, we could apply the recursion theorem to obtain the function h for which

$$
\begin{array}{c} h (0) = A, \\ h (n ^ {+}) = h (n) \cup f [ [ h (n) ] ]. \end{array}
$$

Clearly $h(0) \subseteq h(1) \subseteq \cdots$ ; define $C_{*}$ to be $\bigcup$ ran h; in other words

$$
C _ {*} = \bigcup_ {i \in \omega} h (i).
$$

Show that $C^* = C_*$ . [Suggestion: To show that $C^* \subseteq C_*$ , show that $f[C_*] \subseteq C_*$ . To show that $C_* \subseteq C^*$ , use induction to show that $h(n) \subseteq C^*$ .]

10. In Exercise 9, assume that $B$ is the set of real numbers, $f(x) = x^2$ , and $A$ is the closed interval $[\frac{1}{2}, 1]$ . What is the set called $C^*$ and $C_*$ ?

11. In Exercise 9, assume that $B$ is the set of real numbers, $f(x) = x - 1$ , and $A = \{0\}$ . What is the set called $C^*$ and $C_*$ ?

12. Formulate an analogue to Exercise 9 for a function $f: B \times B \to B$ .

## ARITHMETIC $^{4}$

We can apply the recursion theorem to define addition and multiplication on $\omega$ . (Another way of obtaining these operations will be discussed in Chapter 6.) For example, suppose we want a function $A_{5}: \omega \to \omega$ such that $A_{5}(n)$ is the result of adding 5 to n. Then $A_{5}$ must satisfy the conditions

$$
\begin{array}{c} A _ {5} (0) = 5, \\ A _ {5} (n ^ {+}) = A _ {5} (n) ^ {+} \end{array} \quad \text {   for   } n \text {   in   } \omega .
$$

The recursion theorem assures us that a unique such function exists.

In general, for each $m \in \omega$ there exists (by the recursion theorem) a unique function $A_{m} : \omega \to \omega$ for which

$$
\begin{array}{c} A _ {m} (0) = m, \\ A _ {m} (n ^ {+}) = A _ {m} (n) ^ {+} \qquad \text { for } n \text { in } \omega . \end{array}
$$

But we want one binary operation +, not all these little one-place functions.

Definition A binary operation on a set A is a function from $A \times A$ into A.

Definition Addition (+) is the binary operation on $\omega$ such that for any m and n in $\omega$ ,

$$
m + n = A _ {m} (n).
$$

Thus when written as a relation,

$$
+ = \{\langle \langle m, n \rangle , p \rangle | m \in \omega \& n \in \omega \& p = A _ {m} (n) \}.
$$

In conformity to everyday notation, we write $m + n$ instead of $+ (m, n)$ or $+ (\langle m, n \rangle)$ .

Theorem 4I For natural numbers m and n,

(A1)

$$
\begin{array}{c} {m + 0 = m,} \\ {m + n ^ {+} = (m + n) ^ {+}.} \end{array}\tag{A2}
$$

This theorem is an immediate consequence of the construction of $A_{m}$ . Observe that (A1) and (A2) serve to characterize the binary operation + in a recursive fashion. Our only reason for using the $A_{m}$ 's is that the recursion theorem applies directly to functions with domain $\omega$ , not domain $\omega \times \omega$ . We can now forget the $A_{m}$ 's, and use + and Theorem 4I instead.

We can now proceed to construct the multiplication operation in much the same way. We first apply the recursion theorem to obtain many functions $M_{m}:\omega\to\omega$ where $M_{m}(n)$ is the result of multiplying m by n. Specifically, for each $m \in \omega$ there exists (by the recursion theorem) a unique function $M_m: \omega \to \omega$ for which

$$
\begin{array}{c} {M _ {m} (0) = 0,} \\ {M _ {m} (n ^ {+}) = M _ {m} (n) + m.} \end{array}
$$

Definition Multiplication ( $\cdot$ ) is the binary operation on $\omega$ such that for any m and n in $\omega$ ,

$$
m \cdot n = M _ {m} (n).
$$

The theorem analogous to Theorem 4I is the following.

Theorem 4J For natural numbers m and n,

(M1)

$$
\begin{array}{c} m \cdot 0 = 0, \\ m \cdot n ^ {+} = m \cdot n + m. \end{array}\tag{M2}
$$

We can now discard the $M_{m}$ functions, and use $\cdot$ and Theorem 4J instead.

We could, in the same manner, define the exponentiation operation on $\omega$ . The equations that characterize exponentiation are

(E1)

$$
\begin{array}{c} m ^ {0} = 1, \\ m ^ {(n ^ {+})} = m ^ {n} \cdot m. \end{array}\tag{E2}
$$

Example $2 + 2 = 4$ (we would be alarmed if this failed), as the following calculation demonstrates:

$$
\begin{array}{r l} 2 + 0 = 2 & \text { by   (A1) }, \\ 2 + 1 = 2 + 0 ^ {+} & \\ = (2 + 0) ^ {+} & \text { by   (A2) } \\ = 2 ^ {+} & \\ = 3, & \end{array}
$$

$$
\begin{array}{r l} 2 + 2 & = 2 + 1 ^ {+} \\ & = (2 + 1) ^ {+} \quad \text { by   (A2) } \\ & = 3 ^ {+} \\ & = 4. \end{array}
$$

Having now given set-theoretic definitions of the operations of arithmetic, we next verify that some of the common laws of arithmetic are provable within set theory. This verification is additional evidence, albeit at an elementary level, that mathematics can be embedded in set theory.

Theorem 4K The following identities hold for all natural numbers.

(1) Associative law for addition

$$
m + (n + p) = (m + n) + p.
$$

(2) Commutative law for addition

$$
m + n = n + m.
$$

(3) Distributive law

$$
m \cdot (n + p) = m \cdot n + m \cdot p.
$$

(4) Associative law for multiplication

$$
m \cdot (n \cdot p) = (m \cdot n) \cdot p.
$$

(5) Commutative law for multiplication

$$
m \cdot n = n \cdot m.
$$

Proof Each part is proved by induction. This exemplifies a general fact: When a function has been constructed by use of the recursion theorem, then general properties of the function must usually be proved by induction.

(1) The proof uses induction on p. That is, consider fixed natural numbers m and n, and define $A = \{p \in \omega \mid m + (n + p) = (m + n) + p\}$ . We leave the verification that A is inductive for Exercise 15.

(2) It is necessary to prove two preliminary facts, each of which is proved by induction.

The first preliminary fact is that $0 + n = n$ for all $n \in \omega$ . Let $A = \{n \in \omega \mid 0 + n = n\}$ . Then $0 \in A$ by (A1). Suppose that $k \in A$ . Then

$$
\begin{array}{r l} 0 + k ^ {+} = (0 + k) ^ {+} & \text { by   (A2) } \\ = k ^ {+} & \text { since   } k \in A, \end{array}
$$

and hence $k^{+} \in A$ . So $A$ is inductive.

The second preliminary fact is that $m^{+} + n = (m + n)^{+}$ for m and n in $\omega$ . Consider any fixed $m \in \omega$ and let $B = \{n \in \omega \mid m^{+} + n = (m + n)^{+}\}$ . Again $0 \in B$ by (A1). Suppose that $k \in B$ . Then

$$
\begin{array}{r l} m ^ {+} + k ^ {+} = (m ^ {+} + k) ^ {+} & \text { by   (A2) } \\ = (m + k) ^ {+ +} & \text { since   } k \in B \\ = (m + k ^ {+}) ^ {+} & \text { by   (A2) }, \end{array}
$$

showing that $k^{+} \in B$ . Hence $B$ is inductive.

Finally we are ready to prove the commutative law. Consider any $n \in \omega$ and let $C = \{m \in \omega | m + n = n + m\}$ . By the first preliminary fact, $0 + n = n = n + 0$ , whence $0 \in C$ . Suppose that $k \in C$ . Then

$$
\begin{array}{r l} k ^ {+} + n = (k + n) ^ {+} & \text { by   second   fact } \\ = (n + k) ^ {+} & \text { since } k \in C \\ = n + k ^ {+} & \text { by } (\mathrm{A2}), \end{array}
$$

so that $k^{+} \in C$ . Hence $C$ is inductive.

(3) Consider fixed $m$ and $n$ in $\omega$ and let

$$
A = \{p \in \omega \mid m \cdot (n + p) = m \cdot n + m \cdot p \}.
$$

To check that $0 \in A$ , observe that

$$
\begin{array}{r l} m \cdot (n + 0) = m \cdot n & \text {by (A1)} \\ = m \cdot n + 0 & \text {by (A1)} \\ = m \cdot n + m \cdot 0 & \text {by (M1)}. \end{array}
$$

Now suppose that $k \in A$ . Then

$$
\begin{array}{l l} m \cdot (n + k ^ {+}) = m \cdot (n + k) ^ {+} & \text { by   (A2) } \\ = m \cdot (n + k) + m & \text { by   (M2) } \\ = (m \cdot n + m \cdot k) + m & \text { since   } k \in A \\ = m \cdot n + (m \cdot k + m) & \text { by   part   (1) } \\ = m \cdot n + m \cdot k ^ {+} & \text { by   (M2), } \end{array}
$$

which shows that $k^{+} \in A$ . Hence A is inductive.

The reader has no doubt observed that each inductive argument here is quite straightforward. And each is, for that matter, much like the next.

(4) Consider fixed $m$ and $n$ in $\omega$ and let

$$
A = \{p \in \omega \mid m \cdot (n \cdot p) = (m \cdot n) \cdot p \}.
$$

To check that $0 \in A$ we note that $m \cdot (n \cdot 0) = m \cdot 0 = 0$ by (M1), and $(m \cdot n) \cdot 0 = 0$ as well. Now suppose that $k \in A$ . Then

$$
\begin{array}{r l r} m \cdot (n \cdot k ^ {+}) = m \cdot (n \cdot k + n) & \text { by   (M2) } \\ = m \cdot (n \cdot k) + m \cdot n & \text { by   part   (3) } \\ = (m \cdot n) \cdot k + m \cdot n & \text { since   } k \in A \\ = (m \cdot n) \cdot k ^ {+} & \text { by   (M2), } \end{array}
$$

which shows that $k^{+} \in A$ . Hence $A$ is inductive.

(5) The proof here follows the outline of part (2). There are the analogous two preliminary facts to be proved: $0 \cdot n = 0$ and $m^{+} \cdot n = m \cdot n + n$ . The details of the three inductive arguments are left for Exercise 16.

## Exercises

13. Let $m$ and $n$ be natural numbers such that $m \cdot n = 0$ . Show that either $m = 0$ or $n = 0$ .

14. Call a natural number even if it has the form $2 \cdot m$ for some m. Call it odd if it has the form $(2 \cdot p) + 1$ for some p. Show that each natural number is either even or odd, but never both.

15. Complete the proof of part (1) of Theorem 4K.

16. Complete the proof of part (5) of Theorem 4K.

17. Prove that $m^{n + p} = m^n \cdot m^p$ .

## ORDERING ON ω

We have defined natural numbers in such a way that, for example, $4 \in 7$ . This may have appeared to be a spurious side effect of our definition, but we now want to turn it to our advantage. We have the following strikingly simple definition of order on $\omega$ : For natural numbers m and n, define m to be less than n iff $m \in n$ . We could introduce a special symbol “<” for this:

$$
m <   n \quad \text { iff } \quad m \in n.
$$

But the special symbol seems unnecessary; we can just use “∈”. But it will be necessary to keep in mind the dual role of this symbol, which denotes both membership and ordering. In place of an ≤ symbol, we define

$$
m \in n \quad \text { iff } \quad \text { either } \quad m \in n \quad \text { or } \quad m = n.
$$

Observe that

$$
p \in k ^ {+} \Leftrightarrow p \subseteq k,
$$

a fact we will use in later calculations.

We are now entitled to state the following fact: Any natural number is just the set of all smaller natural numbers. That is, for any n in $\omega$ ,

x is a member of n $\Leftrightarrow$ $x \in \omega \& x$ is less than n.

To verify this, note that we can restate it as

$$
x \in n \Leftrightarrow x \in \omega \& x \in n,
$$

which is true because $\omega$ is a transitive set, and thus $x \in n \in \omega \Rightarrow x \in \omega$ .

We should show that we do indeed have a linear ordering relation on $\omega$ , in the sense defined in Chapter 3. The relation in question is the set of ordered pairs $\epsilon_{\omega}$ defined by

$$
\epsilon_ {\omega} = \{\langle m, n \rangle \in \omega \times \omega | m \in n \}.
$$

We will prove that this is a linear ordering relation on $\omega$ , i.e., that it is a transitive relation that satisfies trichotomy on $\omega$ .

Because each natural number is a transitive set, we have for m, n, p in $\omega$ :

$$
m \in n \& n \in p \Rightarrow m \in p.
$$

That is, our ordering relation on $\omega$ is a transitive relation. It is somewhat harder to show from our definitions that of any two distinct natural numbers, one is larger than the other. For that result, we will need the following lemma.

Lemma 4L (a) For any natural numbers $m$ and $n$ ,

$$
m \in n \quad \mathrm{iff} \quad m ^ {+} \in n ^ {+}.
$$

(b) No natural number is a member of itself.

Proof (a) First assume that $m^{+} \in n^{+}$ . Then we have $m \in m^{+} \subseteq n$ . Hence (by the transitivity of $n$ ) we obtain $m \in n$ .

To prove the converse we use induction on n. That is, form

$$
T = \{n \in \omega | (\forall m \in n) m ^ {+} \in n ^ {+} \}.
$$

Then $0 \in T$ vacuously. Consider any $k \in T$ . In order to show that $k^{+} \in T$ , we must show that whenever $m \in k^{+}$ , then $m^{+} \in k^{++}$ . Given $m \in k^{+}$ , we have either m = k (in which case $m^{+} = k^{+} \in k^{++}$ ) or $m \in k$ . In the latter case (since $k \in T$ ), $m^{+} \in k^{+} \subseteq k^{++}$ . So in either case we get $m^{+} \in k^{++}$ and thus $k^{+} \in T$ . Hence T is inductive and coincides with $\omega$ .

Part (b) follows easily from (a). Let

$$
T = \{n \in \omega \mid n \notin n \}.
$$

Then $0 \in T$ since nothing is a member of 0. And by part (a), $k \notin k \Rightarrow k^{+} \notin k^{+}$ . Hence $T$ is inductive and coincides with $\omega$ .

(In Chapter 7 we will come to the regularity axiom, which implies among other things that no set is a member of itself. But for natural numbers we can get along without the regularity axiom.)

We next use the lemma to prove that for two distinct natural numbers, one is always a member of the other. (It is the smaller one that is a member of the larger one.)

Trichotomy Law for $\omega$ For any natural numbers $m$ and $n$ , exactly one of the three conditions

$$
m \in n, \qquad m = n, \qquad n \in m
$$

holds.

Proof First note that at most one can hold. If $m \in n$ and m = n, then $m \in m$ , in violation of Lemma 4L(b). Also if $m \in n \in m$ , then because m is a transitive set we again have $m \in m$ .

It remains to show that at least one holds. For that we use induction; let

$$
T = \{n \in \omega | (\forall m \in \omega) (m \in n \text {   or   } m = n \text {   or   } n \in m) \}.
$$

In order to show that $0 \in T$ , we want to show that $0 \in m$ for all m. This we do by induction on m. (An induction within an induction!) Clearly $0 \in 0$ , and if $0 \in k$ , then $0 \in k^{+}$ . Hence $0 \in T$ .

Now assume that $k \in T$ and consider $k^{+}$ . For any $m$ in $\omega$ we have (since $k \in T$ ) either $m \in k$ (in which case $m \in k^{+}$ ) or $k \in m$ . In the latter case $k^{+} \in m^{+}$ by Lemma 4L(a), and so $k^{+} \in m$ . Thus in every case, either $m \in k^{+}$ or $k^{+} = m$ or $k^{+} \in m$ . And so $k^{+} \in T$ , $T$ is inductive, and we are done.

A set $A$ is said to be a proper subset of $B$ ( $A \subset B$ ) iff it is a subset of $B$ that is unequal to $B$ .

$$
A \subset B \Leftrightarrow A \subseteq B \& A \neq B.
$$

Ordering on $\omega$ is given not only by the membership relation, but also by the proper subset relation:

Corollary 4M For any natural numbers m and n,

$$
m \in n \quad \mathrm{iff} \quad m \subset n
$$

and

$$
m \in n \quad \text { iff } \quad m \subseteq n.
$$

Proof Since $n$ is a transitive set,

$$
m \in n \Rightarrow m \subseteq n,
$$

and the inclusion is proper by Lemma 4L(b). Conversely assume that $m \subset n$ . Then $m \neq n$ , and $n \notin m$ lest $n \in n$ . So by trichotomy $m \in n$ and we are done.

The above proof uses trichotomy in a typical way: To show that $m \in n$ , it suffices to eliminate the other two alternatives.

The following theorem gives the order-preserving properties of addition and multiplication. The theorem will be used in Chapter 5 (but not elsewhere).

Theorem 4N For any natural numbers m, n, and p,

$$
m \in n \Leftrightarrow m + p \in n + p.
$$

If, in addition, $p \neq 0$ , then

$$
m \in n \Leftrightarrow m \cdot p \in n \cdot p.
$$

Proof First consider addition. For the “ $\Rightarrow$ ” half we use induction on $p$ . Consider fixed $m \in n \in \omega$ and let

$$
A = \{p \in \omega \mid m + p \in n + p \}.
$$

Clearly $0 \in A$ , and

$$
\begin{array}{r c l} k \in A & \Rightarrow & m + k \in n + k \\ & \Rightarrow & (m + k) ^ {+} \in (n + k) ^ {+} \qquad \text { by   Lemma   4L(a)} \\ & \Rightarrow & m + k ^ {+} \in n + k ^ {+} \qquad \text { by   (A2) } \\ & \Rightarrow & k ^ {+} \in A. \end{array}
$$

Hence $A$ is inductive and so $A = \omega$ .

For the “ $\Leftarrow$ ” half we use the trichotomy law and the “ $\Rightarrow$ ” half. If $m + p \in n + p$ , then we cannot have $m = n$ (lest $n + p \in n + p$ ) nor $n \in m$ (lest $n + p \in m + p \in n + p$ ). The only alternative is $m \in n$ .

For multiplication the procedure is similar. For the “ $\Rightarrow$ ” direction, consider fixed $m \in n \in \omega$ and let

$$
\boldsymbol {B} = \{q \in \omega \mid m \cdot q ^ {+} \in n \cdot q ^ {+} \}.
$$

(Recall that for a natural number $p \neq 0$ there is some $q \in \omega$ with $q^{+} = p$ .) It is easy to see that $0 \in B$ , since $m \cdot 0^{+} = m \cdot 0 + m = m$ . Suppose that $k \in B$ ; we need to show that $m \cdot k^{++} \in n \cdot k^{++}$ . Thus

$$
\begin{array}{c} m \cdot k ^ {+ +} = m \cdot k ^ {+} + m \\ \in n \cdot k ^ {+} + m \end{array}
$$

by applying the first part of the theorem to the fact that $m \cdot k^{+} \in n \cdot k^{+}$ . And by again applying the first part of the theorem (this time to the fact that $m \in n$ ),

$$
\begin{array}{c} n \cdot k ^ {+} + m \in n \cdot k ^ {+} + n \\ = n \cdot k ^ {+ +}. \end{array}
$$

Hence $k^{+} \in B$ , $B$ is inductive, and $B = \omega$ .

The “⇐” half then follows exactly as for addition.

Corollary 4P The following cancellation laws hold for m, n, and p in $\omega$ :

$$
m + p = n + p \Rightarrow m = n,
$$

$$
m \cdot p = n \cdot p \& p \neq 0 \Rightarrow m = n.
$$

Proof Apply trichotomy and the preceding theorem.

Well Ordering of $\omega$ Let $A$ be a nonempty subset of $\omega$ . Then there is some $m \in A$ such that $m \in n$ for all $n \in A$ .

Note Such an $m$ is said to be least in $A$ . Thus the theorem asserts that any nonempty subset of $\omega$ has a least element. The least element is always unique, for if $m_1$ and $m_2$ are both least in $A$ , then $m_1 \in m_2$ and $m_2 \in m_1$ . Consequently $m_1 = m_2$ .

Proof Assume that A is a subset of $\omega$ without a least element; we will show that $A = \varnothing$ . We could attempt to do this by showing that the complement $\omega - A$ was inductive. But in order to show that $k^{+} \in \omega - A$ , it is not enough to know merely that $k \in \omega - A$ , we must know that all numbers smaller than k are in $\omega - A$ as well. Given this additional information, we can argue that $k^{+} \in \omega - A$ lest it be a least element for A.

To write down what is approximately this argument, let

$B = \{m\in \omega | \text{ no number less than } m \text{ belongs to } A\}$ .

We claim that B is inductive. $0 \in B$ vacuously. Suppose that $k \in B$ . Then if n is less than $k^{+}$ , either n is less than k (in which case $n \notin A$ since $k \in B$ ) or n = k (in which case $n \notin A$ lest, by trichotomy, it be least in A). In either case, n is outside of A. Hence $k^{+} \in B$ and so B is inductive. It clearly follows that $A = \varnothing$ ; for example, $7 \notin A$ because $8 \in B$ .

Corollary 4Q There is no function $f: \omega \to \omega$ such that $f(n^{+}) \in f(n)$ for every natural number $n$ .

Proof The range of f would be a nonempty subset of $\omega$ without a least element, contradicting the well ordering of $\omega$ .

Our proof of the well ordering of $\omega$ suggests that it might be useful to have a second induction principle.

Strong Induction Principle for $\omega$ Let $A$ be a subset of $\omega$ , and assume that for every $n$ in $\omega$ ,

if every number less than n is in A, then $n \in A$ .

Then $A = \omega$ .

Proof Suppose, to the contrary, that $A \neq \omega$ . Then $\omega - A \neq \varnothing$ , and by the well ordering it has a least number m. Since m is least in $\omega - A$ , all numbers less than m are in A. But then by the hypothesis of the theorem $m \in A$ , contradicting the fact that $m \in \omega - A$ .

The well-ordering principle provides an alternative to proofs by induction. Suppose we want to show that for every natural number, a certain statement holds. Instead of forming the set of numbers for which the statement is true, consider the set of numbers for which it is false, i.e., the set C of counterexamples. To show that $C = \varnothing$ , it suffices to show that C cannot have a least element.

## Exercises

18. Simplify: $\in_{\omega}^{-1}[\{7, 8\}]$ .

19. Prove that if $m$ is a natural number and $d$ is a nonzero number, then there exist numbers $q$ and $r$ such that $m = (d \cdot q) + r$ and $r$ is less than $d$ .

20. Let $A$ be a nonempty subset of $\omega$ such that $\bigcup A = A$ . Show that $A = \omega$ .

21. Show that no natural number is a subset of any of its elements.

22. Show that for any natural numbers $m$ and $p$ we have $m \in m + p^{+}$ .

23. Assume that $m$ and $n$ are natural numbers with $m$ less than $n$ . Show that there is some $p$ in $\omega$ for which $m + p^{+} = n$ . (It follows from this and the preceding exercise that $m$ is less than $n$ iff $(\exists p \in \omega)m + p^{+} = n$ .)

24. Assume that $m + n = p + q$ . Show that

$$
m \in p \Leftrightarrow q \in n.
$$

25. Assume that $n \in m$ and $q \in p$ . Show that

$$
(m \cdot q) + (n \cdot p) \in (m \cdot p) + (n \cdot q).
$$

[Suggestion: Use Exercise 23.]

26. Assume that $n \in \omega$ and $f : n^{+} \to \omega$ . Show that ran f has a largest element.

27. Assume that $A$ is a set, $G$ is a function, and $f_1$ and $f_2$ map $\omega$ into $A$ . Further assume that for each $n$ in $\omega$ both $f_1 \upharpoonright n$ and $f_2 \upharpoonright n$ belong to dom $G$ and

$$
f _ {1} (n) = G \left(f _ {1} \upharpoonright n\right) \& f _ {2} (n) = G \left(f _ {2} \upharpoonright n\right).
$$

Show that $f_{1} = f_{2}$ .

28. Rewrite the proof of Theorem 4G using, in place of induction, the well ordering of $\omega$ .

## Review Exercises

29. Write an expression for the set 4 using only symbols $\varnothing$ , $\{, \}$ , and commas.

30. What is $\bigcup 4$ ? What is $\cap 4$ ?

31. What is $\bigcup \bigcup 7?$

32. (a) Let $A = \{1\}$ . Calculate $A^{+}$ and $\bigcup (A^{+})$ .

(b) What is $\bigcup (\{2\}^{+})?$

33. Which of the following sets are transitive? (For each set $S$ that is not transitive, specify a member of $\bigcup S$ not belonging to $S$ .)

(a) $\{0, 1, \{1\}\}$ .

(b) $\{1\}$ .

(c) $\langle0,1\rangle.$

34. Find suitable a, b, etc. making each of the following sets transitive.

(a) {{∅}}, a, b}.

(b) {{{{{∅}}}}}, c, d, e}.

35. Let $S$ be the set $\langle 1,0\rangle$ .

(a) Find a transitive set $T_{1}$ for which $S \subseteq T_{1}$ .

(b) Find a transitive set $T_2$ for which $S \in T_2$ .

36. There is a function $h \colon \omega \to \omega$ for which $h(0) = 3$ and $h(n^{+}) = 2 \cdot h(n)$ . What is $h(4)$ ?

37. We will say that a set S has n elements (where $n \in \omega$ ) iff there is a one-to-one function from n onto S. Assume that A has m elements and B has n elements.

(a) Show that if $A$ and $B$ are disjoint, then $A \cup B$ has $m + n$ elements.

(b) Show that $A \times B$ has $m \cdot n$ elements.

38. Assume that $h$ is the function from $\omega$ into $\omega$ for which $h(0) = 1$ and $h(n^{+}) = h(n) + 3$ . Give an explicit (not recursive) expression for $h(n)$ .

39. Assume that $h$ is the function from $\omega$ into $\omega$ for which $h(0) = 1$ and $h(n^{+}) = h(n) + (2 \cdot n) + 1$ . Give an explicit (not recursive) expression for $h(n)$ .

40. Assume that $h$ is the function from $\omega$ into $\omega$ defined by $h(n) = 5 \cdot n + 2$ . Express $h(n^{+})$ in terms of $h(n)$ as simply as possible.

CHAPTER 5

# CONSTRUCTION OF THE REAL NUMBERS $^{1}$

In Chapter 4 we gave a set-theoretic construction of the set $\omega$ of natural numbers. In the present chapter we will continue to show how mathematics can be embedded in set theory, by giving a set-theoretic construction of the real numbers. (The operative phrase is “can be,” not “is” or “must be.” We will return to this point in the section on “Two.”)

## INTEGERS

First we want to extend our set $\omega$ of natural numbers to a set Z of integers (both positive and negative). Here “extend” is to be loosely interpreted, since $\omega$ will not actually be a subset of Z. But Z will include an “isomorphic copy” of $\omega$ (Fig. 19).

A negative integer can be named by using two natural numbers and a subtraction symbol: 2 - 3, 5 - 10, etc. We need some sets to stand behind these names.

As a first guess, we could try taking the integer -1 to be the pair $\langle2,3\rangle$ of natural numbers used to name -1 in the preceding paragraph. And similarly we could try letting the integer -5 be the pair $\langle5,10\rangle$ of natural numbers. But this first guess fails, because -1 has a multiplicity of names: 2 - 3 = 0 - 1 but $\langle2,3\rangle \neq \langle0,1\rangle$ .

As a second guess, we can define an equivalence relation $\sim$ such that $\langle2,3\rangle\sim\langle0,1\rangle$ . (Imposing such an equivalence relation is sometimes described as “identifying” $\langle2,3\rangle$ and $\langle0,1\rangle$ .) Then we will have the one equivalence class

$$
[ \langle 2, 3 \rangle ] = [ \langle 0, 1 \rangle ],
$$

and we can take -1 to be this equivalence class. Then for the set Z of all integers, we can take the set of all equivalence classes:

$$
\mathbb {Z} = (\omega \times \omega) / \sim .
$$

This is in fact what we do. Call a pair of natural numbers a difference; then an integer will be an equivalence class of differences. Consider two differences $\langle m, n \rangle$ and $\langle p, q \rangle$ . When should we call them equivalent?

![](images/6c341ab7bb947c67159f937eac6f3f86743c3cc02d346f18ad6f38645b0ec59f.jpg)  
Fig. 19. There is a subset of Z that looks like $\omega$ .

Informally, they are equivalent iff m - n = p - q, but this equation has no official meaning for us yet. But the equation is equivalent to $m + q = p + n$ , and the latter equation is meaningful. Consequently we formulate the following definition.

Definition Define $\sim$ to be the relation on $\omega \times \omega$ for which

$$
\langle m, n \rangle \sim \langle p, q \rangle \quad \text {iff} \quad m + q = p + n.
$$

Thus $\sim$ is a set of ordered pairs whose domain and range are also sets of ordered pairs. In more explicit (but less readable) form, the above definition can be stated:

$$
\sim = \{\langle \langle m, n \rangle , \langle p, q \rangle \rangle | m + q = p + n \text {   and   all   are   in   } \omega \}.
$$

Theorem 5ZA The relation $\sim$ is an equivalence relation on $\omega \times \omega$ .

Proof We leave it to you to check that $\sim$ is reflexive on $\omega \times \omega$ and is symmetric. To show transitivity, suppose that $\langle m, n \rangle \sim \langle p, q \rangle$ and $\langle p, q \rangle \sim \langle r, s \rangle$ . Then (by the definition of $\sim$ )

$$
m + q + p + s = p + n + r + q.
$$

By use of the cancellation law (Corollary 4P), we obtain $m + s = r + n$ , and thus $\langle m, n \rangle \sim \langle r, s \rangle$ .

Definition The set Z of integers is the set $(\omega \times \omega)/\sim$ of all equivalence classes of differences.

For example, the integer $2_{z}$ is the equivalence class

$$
[ \langle 2, 0 \rangle ] = \{\langle 2, 0 \rangle , \langle 3, 1 \rangle , \langle 4, 2 \rangle , \dots \},
$$

and the integer $-3_{z}$ is the equivalence class

$$
[ \langle 0, 3 \rangle ] = \{\langle 0, 3 \rangle , \langle 1, 4 \rangle , \langle 2, 5 \rangle , \dots \}.
$$

These equivalence classes can be pictured as $45^{\circ}$ lines in the Cartesian product $\omega \times \omega$ (Fig. 20).

Next we want to endow Z with a suitable addition operation. Informally, we can add differences:

$$
(m - n) + (p - q) = (m + p) - (n + q).
$$

This indicates that the correct addition function $+_{z}$ for integers will satisfy the equation

$$
[ \langle m, n \rangle ] + _ {Z} [ \langle p, q \rangle ] = [ \langle m + p, n + q \rangle ].
$$

This equation will serve to define $+_{z}$ , once we have verified that it makes sense. The situation here is of the sort discussed in Theorem 3Q. We want to specify the value of the operation $+_{z}$ at a pair of equivalence classes by (1) selecting representatives $\langle m, n \rangle$ and $\langle p, q \rangle$ from the classes, (2)

![](images/781e688ce0fcf39c018e6685c624a6c4d7768d38373a20b699e68de43e7cff59.jpg)  
Fig. 20. An integer is a line in $\omega \times \omega$ .

![](images/0bc4804bab76b8b7c49f615044904ee0aa4b05119431eb3860128451618f3d2a.jpg)  
Fig. 21. Addition of lines is well defined.

operating on the representatives (by vector addition in this case), and then (3) forming the equivalence class of the result of the vector addition. For $+_{z}$ to be well defined, we must verify that choice of other representatives $\langle m', n' \rangle$ and $\langle p', q' \rangle$ from the given classes would yield the same equivalence class for the sum (Fig. 21).

Lemma 5ZB If $\langle m, n \rangle \sim \langle m', n' \rangle$ and $\langle p, q \rangle \sim \langle p', q' \rangle$ , then

$$
\langle m + p, n + q \rangle \sim \langle m ^ {\prime} + p ^ {\prime}, n ^ {\prime} + q ^ {\prime} \rangle .
$$

Proof We are given, by hypothesis, the two equations

$$
m + n ^ {\prime} = m ^ {\prime} + n \quad \text { and } \quad p + q ^ {\prime} = p ^ {\prime} + q.
$$

We want to obtain the equation

$$
m + p + n ^ {\prime} + q ^ {\prime} = m ^ {\prime} + p ^ {\prime} + n + q.
$$

But this results from just adding together the two given equations.

This lemma justifies the definition of $+_{z}$ . In the terminology of Theorem 3Q, it says that the function $F$ of vector addition

$$
F (\langle m, n \rangle , \langle p, q \rangle) = \langle m + p, n + q \rangle
$$

is compatible with $\sim$ . Hence there is a well-defined function $\hat{F}$ on the quotient set; $\hat{F}$ is just our operation $+_{z}$ . It satisfies the equation

$$
[ \langle m, n \rangle ] + _ {Z} [ \langle p, q \rangle ] = [ \langle m + p, n + q \rangle ].
$$

In other words, for integers $a$ and $b$ our addition formula is

$$
a + _ {z} b = [ \langle m + p, n + q \rangle ],
$$

where $\langle m, n \rangle$ is chosen from a and $\langle p, q \rangle$ is chosen from b. Theorem 3Q assures us that the equivalence class on the right is independent of how these choices are made.

Example We can calculate $2_{z} + _{z}(-3_{z})$ . Since $2_{z} = [\langle 2, 0 \rangle]$ and $-3_{z} = [\langle 0, 3 \rangle]$ , we have

$$
\begin{array}{r l} & 2 _ {\mathbf {z}} + _ {\mathbf {z}} (- 3 _ {\mathbf {z}}) = [ \langle 2, 0 \rangle ] + _ {\mathbf {z}} [ \langle 0, 3 \rangle ] \\ & \qquad = [ \langle 2 + 0, 0 + 3 \rangle ] \\ & \qquad = [ \langle 2, 3 \rangle ] \\ & \qquad = - 1 _ {\mathbf {z}}. \end{array}
$$

The familiar properties of addition, such as commutativity and associativity, now follow easily from the corresponding properties of addition of natural numbers.

Theorem 5ZC The operation $+_{z}$ is commutative and associative:

$$
\begin{array}{c} a + _ {z} b = b + _ {z} a, \\ (a + _ {z} b) + _ {z} c = a + _ {z} (b + _ {z} c). \end{array}
$$

Proof The integer $a$ must be of the form $[\langle m, n \rangle]$ for some natural numbers $m$ and $n$ ; similarly $b$ is $[\langle p, q \rangle]$ . Then:

$$
\begin{array}{r l} a + _ {z} b & = [ \langle m, n \rangle ] + _ {z} [ \langle p, q \rangle ] \\ & = [ \langle m + p, n + q \rangle ] \quad \text { by   definition   of } + _ {z} \\ & = [ \langle p + m, q + n \rangle ] \quad \text { by   commutativity   of } + \text { on } \omega \\ & = [ \langle p, q \rangle ] + _ {z} [ \langle m, n \rangle ] \\ & = b + _ {z} a. \end{array}
$$

The calculation for associativity is similar (Exercise 4).

Let $0_{z} = [\langle 0, 0 \rangle]$ . Then it is straightforward to verify that $a +_{z} 0_{z} = a$ for any integer $a$ , i.e., $0_{z}$ is an identity element for addition. And the new feature that $\mathbb{Z}$ has (and the feature for which the extension from $\omega$ to $\mathbb{Z}$ was made), is the existence of additive inverses.

Theorem 5ZD (a) $0_{z}$ is an identity element for $+_{z}$ :

$$
a + _ {z} 0 _ {z} = a
$$

for any $a$ in $\mathbb{Z}$ .

(b) Additive inverses exist: For any integer $a$ , there is an integer $b$ such that

$$
a + _ {z} b = 0 _ {z}.
$$

Proof (b) Given an integer $a$ , it must be of the form $[\langle m, n \rangle]$ . Take $b$ to be $[\langle n, m \rangle]$ . Then $a + _{z} b = [\langle m + n, n + m \rangle] = [\langle 0, 0 \rangle] = 0_{z}$ .

Theorems 5ZC and 5ZD together say that Z with the operation $+_{z}$ and the identity element $0_{z}$ is an Abelian group. The concept of an Abelian group is central to abstract algebra, but in this book the concept will receive only passing attention.

Inverses are unique. That is, if $a + _{z}b = 0_{z}$ and $a + _{z}b' = 0_{z}$ , then $b = b'$ . To prove this, observe that

$$
b = b + _ {z} (a + _ {z} b ^ {\prime}) = (b + _ {z} a) + _ {z} b ^ {\prime} = b ^ {\prime}.
$$

(This proof works in any Abelian group.) The inverse of $a$ is denoted as $-a$ . Then as the proof to Theorem 5ZD shows,

$$
- [ \langle m, n \rangle ] = [ \langle n, m \rangle ].
$$

Inverses provide us with a subtraction operation, which we define by the equation

$$
b - a = b + _ {z} (- a).
$$

We can also endow the set Z with a multiplication operation, which we obtain in much the same way as we obtained the addition operation. First we look at the informal calculation with differences

$$
(m - n) \cdot (p - q) = (m p + n q) - (m q + n p),
$$

which tells us that the desired operation $\cdot_{z}$ will satisfy the equation

$$
[ \langle m, n \rangle ] \cdot_ {Z} [ \langle p, q \rangle ] = [ \langle m p + n q, m q + n p \rangle ].
$$

(Here we write, as usual, mp in place of $m \cdot p$ .) Again we must verify that the above equation characterizes a well-defined operation on equivalence classes. That is, we must verify that the operation on differences

$$
G (\langle m, n \rangle , \langle p, q \rangle) = \langle m p + n q, m q + n p \rangle
$$

is compatible with $\sim$ . This verification is accomplished by the following lemma.

Lemma 5ZE If $\langle m, n \rangle \sim \langle m', n' \rangle$ and $\langle p, q \rangle \sim \langle p', q' \rangle$ , then

$$
\langle m p + n q, m q + n p \rangle \sim \langle m ^ {\prime} p ^ {\prime} + n ^ {\prime} q ^ {\prime}, m ^ {\prime} q ^ {\prime} + n ^ {\prime} p ^ {\prime} \rangle .
$$

Proof We are given the two equations

(1)

$$
m + n ^ {\prime} = m ^ {\prime} + n,\tag{2}
$$

$$
p + q ^ {\prime} = p ^ {\prime} + q,
$$

and we want to obtain the equation

$$
m p + n q + m ^ {\prime} q ^ {\prime} + n ^ {\prime} p ^ {\prime} = m ^ {\prime} p ^ {\prime} + n ^ {\prime} q ^ {\prime} + m q + n p.
$$

The idea is take multiples of (1) and (2) that contain the terms we need. First multiply Eq. (1) by p; this gives us an mp on the left and an np on the right. Second, multiply the reverse of Eq. (1) by q; this gives us an nq on the left and an mq on the right. Third, multiply Eq. (2) by $m'$ . Fourth, multiply the reverse of Eq. (2) by $n'$ . Now add the four equations we have obtained from (1) and (2). All the unwanted terms cancel, and we are left with the desired equation. It works.

As for addition, we can prove the basic properties of multiplication from the corresponding properties of multiplication of natural numbers.

Theorem 5ZF The multiplication operation $\cdot_{z}$ is commutative, associative, and distributive over $+_{z}$ :

$$
\begin{array}{c} {a \cdot_ {z} b = b \cdot_ {z} a} \\ {\left(a \cdot_ {z} b\right) \cdot_ {z} c = a \cdot_ {z} (b \cdot_ {z} c)} \\ {a \cdot_ {z} (b + _ {z} c) = (a \cdot_ {z} b) + _ {z} (a \cdot_ {z} c)} \end{array}
$$

Proof Say that $a = [\langle m, n \rangle]$ and $b = [\langle p, q \rangle]$ . For the commutative law, we have

$$
a \cdot_ {z} b = [ \langle m p + n q, m q + n p \rangle ],
$$

whereas

$$
b \cdot_ {z} a = [ \langle p m + q n, p n + q m \rangle ].
$$

The equality of these two follows at once from the commutativity of addition and multiplication in $\omega$ .

The other parts of the theorem are proved by the same method. Say that $c = [\langle r, s \rangle]$ . Then $(a \cdot_{\mathbf{z}} b) \cdot_{\mathbf{z}} c$ is

$$
[ \langle m p + n q) r + (m q + n p) s, (m p + n q) s + (m q + n p) r \rangle ],
$$

where $a\cdot_{z}(b\cdot_{z}c)$ is

$$
[ \langle m (p r + q s) + n (p s + q r), m (p s + q r) + n (p r + q s) \rangle ].
$$

The equality of these follows from laws of arithmetic in $\omega$ (Theorem 4K).

As for the distributive law, when we expand $a \cdot_{z}(b + _{z}c)$ , we obtain

$$
[ \langle m (p + r) + n (q + s), m (q + s) + n (p + r) \rangle ],
$$

whereas when we expand $a \cdot_{z} b +_{z} a \cdot_{z} c$ we obtain

$$
[ \langle m p + n q + m r + n s, m q + n p + m s + n r \rangle ].
$$

Again equality is clear from laws of arithmetic in $\omega$ .

The remaining properties of multiplication that we will need constitute the next theorem. Let $1_{z}$ be the integer $[\langle 1,0\rangle]$ .

Theorem 5ZG (a) The integer $1_{z}$ is a multiplicative identity element:

$$
a \cdot_ {z} 1 _ {z} = a
$$

for any integer $a$ .

(b) $0_{z} \neq 1_{z}$ .

(c) Whenever $a \cdot_{z} b = 0_{z}$ , then either $a = 0_{z}$ or $b = 0_{z}$ .

Part (c) is sometimes stated: There are no “zero divisors” in Z.

Proof Part (a) is a trivial calculation.

For part (b) it is necessary to check that $\langle 0,0\rangle \not\sim \langle 1,0\rangle$ . This reduces to checking that $0\neq 1$ in $\omega$ , which is true.

For part (c), assume that $a \neq 0_{z}$ and $b \neq 0_{z}$ ; it will suffice to prove that $a \cdot_{z} b \neq 0_{z}$ . We know that for some $m, n, p$ , and $q$ :

$$
a = [ \langle m, n \rangle ], \quad b = [ \langle p, q \rangle ],
$$

$$
a \cdot_ {z} b = [ \langle m p + n q, m q + n p \rangle ].
$$

Since $a \neq [\langle 0, 0 \rangle]$ , we have $m \neq n$ . So either $m \in n$ or $n \in m$ . Similarly, either $p \in q$ or $q \in p$ . This leads to a total of four cases, but in each case we have

$$
m p + n q \neq m q + n p
$$

by Exercise 25 of Chapter 4. Hence $a \cdot_{\mathbf{z}} b \neq [\langle 0, 0 \rangle]$ .

In algebraic terminology, we can say that $\mathbb{Z}$ together with $+_{\mathbf{z}}, \cdot_{\mathbf{z}}, 0_{\mathbf{z}}$ , and $1_{\mathbf{z}}$ forms an integral domain. This means that:

(i) $\mathbb{Z}$ with $+_{\mathbf{z}}$ and $0_{\mathbf{z}}$ forms as Abelian group (Theorems 5ZC and 5ZD).

(ii) Multiplication is commutative and associative, and is distributive over addition (Theorem 5ZF).

(iii) $1_{z}$ is a multiplicative identity (different from $0_{z}$ ), and no zero divisors exist (Theorem 5ZG).

There is a summary of these algebraic concepts near the end of this chapter. The value of the concepts stems from the large array of structures that satisfy the various conditions. In this book, however, we are concerned with only the most standard cases.

Example The calculation

$$
[ \langle 0, 1 \rangle ] \cdot_ {z} [ \langle m, n \rangle ] = [ \langle n, m \rangle ]
$$

shows that $-1_{z} \cdot_{z} a = -a$ .

Next we develop an ordering relation $<_{\mathbf{z}}$ on the integers. The informal calculation

$$
m - n <   p - q \quad \text { iff } \quad m + q <   p + n
$$

indicates that ordering $<_{z}$ on $\mathbb{Z}$ should be defined by

$$
[ \langle m, n \rangle ] <   _ {Z} [ \langle p, q \rangle ] \quad \text { iff } \quad m + q \in p + n.
$$

As usual, it is necessary to check that this condition yields a well-defined relation on the integers. That is, we want to define

$$
a <   _ {z} b \quad \text { iff } \quad m + q \in p + n,
$$

where m, n, p, and q are chosen so that $a = [\langle m, n \rangle]$ and $b = [\langle p, q \rangle]$ . But that choice can be made in infinitely many ways; we must verify that we have the same outcome each time. The following lemma does just this.

Lemma 5ZH If $\langle m, n \rangle \sim \langle m', n' \rangle$ and $\langle p, q \rangle \sim \langle p', q' \rangle$ , then

$$
m + q \in p + n \quad \text {iff} \quad m ^ {\prime} + q ^ {\prime} \in p ^ {\prime} + n ^ {\prime}.
$$

Proof The hypotheses give us the equations

$$
m + n ^ {\prime} = m ^ {\prime} + n \quad \text { and } \quad p + q ^ {\prime} = p ^ {\prime} + q.
$$

In order to utilize these equations in the inequality $m + q \in p + n$ , we add $n'$ and $q'$ to each side of this inequality:

$$
\begin{array}{r c l} m + q \in p + n & \Leftrightarrow & m + q + n ^ {\prime} + q ^ {\prime} \in p + n + n ^ {\prime} + q ^ {\prime} \\ & \Leftrightarrow & m ^ {\prime} + n + q + q ^ {\prime} \in p ^ {\prime} + q + n + n ^ {\prime} \\ & \Leftrightarrow & m ^ {\prime} + q ^ {\prime} \in p ^ {\prime} + n ^ {\prime}. \end{array}
$$

Here the first and third steps use Theorem 4N, while the middle step uses the given equations.

Theorem 5ZI The relation $<_{z}$ is a linear ordering relation on the set of integers.

Proof We must show that $<_{\mathbb{Z}}$ is a transitive relation that satisfies trichotomy on $\mathbb{Z}$ .

To prove transitivity, consider integers $a = [\langle m, n \rangle]$ , $b = [\langle p, q \rangle]$ , and $c = [\langle r, s \rangle]$ . Then

$$
\begin{array}{r c l} a <   _ {z} b \& b <   _ {z} c & \Rightarrow & m + q \in p + n \& p + s \in r + q \\ & \Rightarrow & m + q + s \in p + n + s \& p + s + n \in r + q + n \\ & \Rightarrow & m + q + s \in r + q + n \\ & \Rightarrow & m + s \in r + n \quad \text { by   Theorem   4N } \\ & \Rightarrow & a <   _ {z} c. \end{array}
$$

Proving trichotomy is easy. To say that exactly one of

$$
a <   _ {z} b, \quad a = b, \quad b <   _ {z} a
$$

holds is to say that exactly one of

$$
m + q \in p + n, \quad m + q = p + n, \quad p + n \in m + q
$$

holds. Thus the result follows from trichotomy in $\omega$ .

An integer $b$ is called positive iff $0_{z} <_{z} b$ . It is easy to check that

$$
b <   _ {z} 0 _ {z} \quad \text { iff } \quad 0 _ {z} <   _ {z} - b.
$$

Thus a consequence of trichotomy is the fact that for an integer $b$ , exactly one of the three alternatives

$$
b \text {   is   positive,   } \quad b \text {   is   zero,   } \quad - b \text {   is   positive }
$$

holds.

The next theorem shows that addition preserves order, as does multiplication by a positive integer. (The corresponding theorem for $\omega$ was Theorem 4N.)

Theorem 5ZJ The following are valid for any integers a, b, and c:

(a) $a < _{z}b \Leftrightarrow a + _{z}c < _{z}b + _{z}c.$

(b) If $0_{\mathbf{z}} <   _{\mathbf{z}}c$ , then

$$
a <   _ {z} b \Leftrightarrow a \cdot_ {z} c <   _ {z} b \cdot_ {z} c.
$$

Proof Assume that $a, b$ , and $c$ are $[\langle m, n \rangle]$ , $[\langle p, q \rangle]$ , and $[\langle r, s \rangle]$ , respectively. The result to be proved in part (a) then translates to the following statement about natural numbers:

$$
m + q \in p + n \Leftrightarrow m + r + q + s \in p + r + n + s.
$$

This is an immediate consequence of the fact that addition in $\omega$ preserves order (Theorem 4N).

Part (b) is similar in spirit. As in Theorem 4N, it suffices to prove one direction:

$$
0 _ {z} <   _ {z} c \& a <   _ {z} b \Rightarrow a \cdot_ {z} c <   _ {z} b \cdot_ {z} c.
$$

This translates to:

$$
s \in r \& m + q \in p + n \Rightarrow m r + n s + p s + q r \in p r + q s + m s + n r.
$$

This is not as bad as it looks. If we let $k = m + q$ and $l = p + n$ , then it becomes

$$
s \in r \& k \in l \Rightarrow k r + l s \in k s + l r.
$$

This is just Exercise 25 of Chapter 4.

Corollary 5ZK For any integers a, b, and c the cancellation laws hold:

$$
a + _ {z} c = b + _ {z} c \Rightarrow a = b,
$$

$$
a \cdot_ {z} c = b \cdot_ {z} c \& c \neq 0 _ {z} \Rightarrow a = b.
$$

Proof This follows from the preceding theorem in the same way that the cancellation laws in $\omega$ (Corollary 4P) followed from the order-preserving properties (Theorem 4N).

Although $\omega$ is not actually a subset of $\mathbb{Z}$ , nonetheless $\mathbb{Z}$ has a subset that is "just like" $\omega$ . To make this precise, define the function $E: \omega \to \mathbb{Z}$ by

$$
E (n) = [ \langle n, 0 \rangle ].
$$

For example, $E(0) = 0_{z}$ and $E(1) = 1_{z}$ .

The following theorem, in algebraic terminology, says that $E$ is an "isomorphic embedding" of the system $\langle \omega, +, \cdot, \in_{\omega} \rangle$ into the system $\langle \mathbb{Z}, +_{\mathbf{Z}}, \cdot_{\mathbf{Z}}, <_{\mathbf{Z}} \rangle$ . That is, $E$ is a one-to-one function that preserves addition, multiplication, and order.

Theorem 5ZL E maps $\omega$ one-to-one into Z, and satisfies the following properties for any natural numbers m and n:

(a) $E(m + n) = E(m) + _{z} E(n).$

(b) $E(mn) = E(m) \cdot_{Z} E(n).$

(c) $m \in n \text{ iff } E(m) <_{z} E(n).$

Proof To show that $E$ is one-to-one we calculate

$$
\begin{array}{r c l} E (m) = E (n) & \Rightarrow & [ \langle m, 0 \rangle ] = [ \langle n, 0 \rangle ] \\ & \Rightarrow & \langle m, 0 \rangle \sim \langle n, 0 \rangle \\ & \Rightarrow & m = n. \end{array}
$$

Parts (a), (b), and (c) are proved by routine calculations (Exercise 8).

Finally we can give a precise counterpart to our motivating guideline that the difference $\langle m, n \rangle$ should name m - n. For any m and n,

$$
[ \langle m, n \rangle ] = E (m) - E (m)
$$

as is verified by evaluating the right side of this equation (Exercise 9).

Henceforth we will streamline our notation by omitting the subscript “Z” on $+_{z}, \cdot_{z}, <_{z}, 0_{z}, 1_{z}$ , etc. Furthermore $a \cdot b$ will usually be written as just ab.

## Exercises

1. Is there a function $F: \mathbb{Z} \to \mathbb{Z}$ satisfying the equation

$$
F ([ \langle m, n \rangle ]) = [ \langle m + n, n \rangle ]?
$$

2. Is there a function $G: \mathbb{Z} \to \mathbb{Z}$ satisfying the equation

$$
G ([ \langle m, n \rangle ]) = [ \langle m, m \rangle ]?
$$

3. Is there a function $H: Z \to Z$ satisfying the equation

$$
H ([ \langle m, n \rangle ]) = [ \langle n, m \rangle ]?
$$

4. Prove that $+_{z}$ is associative. (This is part of Theorem 5ZC.)

5. Give a formula for subtraction of integers:

$$
[ \langle m, n \rangle ] - [ \langle p, q \rangle ] = ?
$$

6. Show that $a \cdot_{z} 0_{z} = 0_{z}$ for every integer a.

7. Show that

$$
a \cdot_ {z} (- b) = (- a) \cdot_ {z} b = - (a \cdot_ {z} b)
$$

for all integers $a$ and $b$ .

8. Prove parts (a), (b), and (c) of Theorem 5ZL.

9. Show that

$$
[ \langle m, n \rangle ] = E (m) - E (n)
$$

for all natural numbers m and n.

## RATIONAL NUMBERS

We can extend our set Z of integers to the set Q of rational numbers in much the same way as we extended $\omega$ to Z. In fact, the extension from Z to Q is to multiplication what the extension from $\omega$ to Z is to addition. In the integers we get additive inverses, i.e., solutions to the equation $a + x = 0$ .

In the rationals we will get multiplicative inverses, i.e., solutions to the equation $r \cdot_{\varrho} x = 1_{\varrho}$ (for nonzero $r$ ).

We can name a rational number by using two integers and a symbol for division:

$$
1 / 2, \quad - 3 / 4, \quad 6 / 1 2.
$$

But as before, each number has a multiplicity of names, e.g., 1/2 = 6/12. So the name “1/2” must be identified with the name “6/12.”

By a fraction we mean an ordered pair of integers, the second component of which (called the denominator) is nonzero. For example, $\langle1,2\rangle$ and $\langle6,12\rangle$ are fractions; we want a suitable equivalence relation $\sim$ for which $\langle1,2\rangle\sim\langle6,12\rangle$ . Since a/b=c/d iff $a\cdot d=c\cdot b$ , we choose to define $\sim$ as follows. Let $Z'$ be the set $Z-\{0\}$ of nonzero integers. Then $Z\times Z'$ is the set of all fractions.

Definition Define $\sim$ to be the binary relation on $\mathbb{Z} \times \mathbb{Z}'$ for which

$$
\langle a, b \rangle \sim \langle c, d \rangle \quad \text { iff } \quad a \cdot d = c \cdot b.
$$

The set $\mathbb{Q}$ of rational numbers is the set $(\mathbb{Z} \times \mathbb{Z}') / \sim$ of all equivalence classes of fractions.

We use the same symbol “\~” that has been used previously for other equivalence relations, but as we discuss only one equivalence relation at a time, no confusion should result.

For example, $\langle 1,2\rangle \sim \langle 6,12\rangle$ since $1\cdot 12 = 6\cdot 2$ . The equivalence class $[\langle 1,2\rangle ]$ is the rational number "one-half." The rationals zero and one are

$$
0 _ {Q} = [ \langle 0, 1 \rangle ] \quad \text { and } \quad 1 _ {Q} = [ \langle 1, 1 \rangle ].
$$

These are distinct, because $\langle 0,1\rangle \not\sim \langle 1,1\rangle$ . Of course we must check that $\sim$ is indeed an equivalence relation.

Theorem 5QA The relation $\sim$ is an equivalence relation on $\mathbb{Z} \times \mathbb{Z}'$ .

Proof You should verify that the relation is reflexive on $\mathbb{Z} \times \mathbb{Z}'$ and is symmetric. As for transitivity, suppose that

$$
\langle a, b \rangle \sim \langle c, d \rangle \quad \text { and } \quad \langle c, d \rangle \sim \langle e, f \rangle .
$$

Then

$$
a d = c b \quad \text { and } \quad c f = e d.
$$

Multiply the first equation by f and the second by b to get

$$
a d f = c b f \quad \text { and } \quad c f b = e d b.
$$

From this we conclude that $adf = edb$ and hence (by canceling the nonzero $d$ ) $af = eb$ . This tells us that $\langle a, b \rangle \sim \langle e, f \rangle$ .

We can picture the equivalence classes as nonhorizontal lines (in the “plane” $Z \times Z'$ ) through the origin (Fig. 22). The fraction $\langle1,2\rangle$ lies on the line with slope 2; in general, $[\langle a,b\rangle]$ is the line with slope b/a.

We arrive at addition and multiplication operations for $\mathbb{Q}$ by the same methods used for $\mathbb{Z}$ . For addition, the informal calculation

$$
\frac {a}{b} + \frac {c}{d} = \frac {a d + c b}{b d}
$$

indicates that $+_{o}$ should be defined by the equation

$$
[ \langle a, b \rangle ] + _ {Q} [ \langle c, d \rangle ] = [ \langle a d + c b, b d \rangle ].
$$

Note that $bd \neq 0$ since $b \neq 0$ and $d \neq 0$ . Hence $\langle ad + cb, bd \rangle$ is a fraction. As usual, we must check that there is a well-defined function $+_{Q}$ on equivalence classes that satisfies the above equation. The following lemma, together with Theorem 3Q, does just that.

$$
\begin{array}{c c} & 1 / 2 \\ & 3 \end{array}
$$

Fig. 22. Rational numbers are nonhorizontal lines.

Lemma 5QB If $\langle a, b \rangle \sim \langle a', b' \rangle$ and $\langle c, d \rangle \sim \langle c', d' \rangle$ , then

$$
\langle a d + c b, b d \rangle \sim \langle a ^ {\prime} d ^ {\prime} + c ^ {\prime} b ^ {\prime}, b ^ {\prime} d ^ {\prime} \rangle .
$$

Proof We are given the equations

$$
a b ^ {\prime} = a ^ {\prime} b \quad \text { and } \quad c d ^ {\prime} = c ^ {\prime} d.
$$

We want the equation

$$
(a d + c b) b ^ {\prime} d ^ {\prime} = (a ^ {\prime} d ^ {\prime} + c ^ {\prime} b ^ {\prime}) b d,
$$

which, when expanded (with the factors in alphabetic order), becomes

$$
\underline {{a b ^ {\prime} d d ^ {\prime}}} + b b ^ {\prime} \underline {{c d ^ {\prime}}} = \underline {{a ^ {\prime} b}} d d ^ {\prime} + b b ^ {\prime} \underline {{c ^ {\prime} d}}.
$$

This clearly is obtainable from the given equations.

Example Just to be on the safe side, we will check that $2 + 2 = 4$ in $\mathbb{Q}$ . Let $2_{Q} = [\langle 2,1\rangle ]$ and $4_{Q} = [\langle 4,1\rangle ]$ . Then

$$
\begin{array}{r l} 2 _ {Q} + _ {Q} 2 _ {Q} & = [ \langle 2, 1 \rangle ] + _ {Q} [ \langle 2, 1 \rangle ] \\ & = [ \langle 2 + 2, 1 \rangle ] \\ & = [ \langle 4, 1 \rangle ] = 4 _ {Q}, \end{array}
$$

where we use the fact that $2 + 2 = 4$ in Z.

The rationals with $+_{Q}$ and $0_{Q}$ also form an Abelian group:

Theorem 5QC (a) Addition $+_{o}$ is associative and commutative:

$$
(q + _ {Q} r) + _ {Q} s = q + _ {Q} (r + _ {Q} s),
$$

$$
r + _ {Q} s = s + _ {Q} r.
$$

(b) $0_{\pmb{q}}$ is an identity element for $+\mathbf{\Phi}_{\pmb{q}}$

$$
r + _ {Q} 0 _ {Q} = r
$$

for any $r$ in $\mathbb{Q}$ .

(c) Additive inverses exist: For any $r$ in $\mathbb{Q}$ there is an $s$ in $\mathbb{Q}$ such that $r + _Q s = 0_Q$ .

Proof First we verify commutativity. On the one hand,

$$
[ \langle a, b \rangle ] + _ {Q} [ \langle c, d \rangle ] = [ \langle a d + c b, b d \rangle ],
$$

'and on the other

$$
[ \langle c, d \rangle ] + _ {Q} [ \langle a, b \rangle ] = [ \langle c b + a d, d b \rangle ].
$$

But the right sides of these two equations are equal, by known commutative laws for arithmetic in $\mathbb{Z}$ .

The verification of associativity is similar. Consider three rational numbers $[\langle a, b\rangle]$ , $[\langle c, d\rangle]$ , and $[\langle e, f\rangle]$ . Then one grouping for the sum is

$$
\begin{array}{r l} ([ \langle a, b \rangle ] + _ {Q} [ \langle c, d \rangle ]) + _ {Q} [ \langle e, f \rangle ] & = [ \langle a d + c b, b d \rangle ] + _ {Q} [ \langle e, f \rangle ] \\ & = [ \langle (a d + c b) f + e (b d), (b d) f \rangle ] \\ & = [ \langle a d f + c b f + e b d, b d f \rangle ]. \end{array}
$$

The same expansion for the other grouping is

$$
\begin{array}{r l} [ \langle a, b \rangle ] + _ {Q} ([ \langle c, d \rangle ] + _ {Q} [ \langle e, f \rangle ]) & = [ \langle a, b \rangle ] + _ {Q} [ \langle c f + e d, d f \rangle ] \\ & = [ \langle a (d f) + (c f + e d) b, b (d f) \rangle ] \\ & = [ \langle a d f + c f b + e d b, b d f \rangle ], \end{array}
$$

which agrees with the first calculation.

Part (b) is a routine calculation. We know that $r = [\langle a, b \rangle]$ for some integers $a$ and $b$ . Then

$$
\begin{array}{r l} r + _ {Q} 0 _ {Q} & = [ \langle a, b \rangle ] + _ {Q} [ \langle 0, 1 \rangle ] \\ & = [ \langle a \cdot 1 + 0 \cdot b, b \cdot 1 \rangle ] \\ & = [ \langle a, b \rangle ] = r. \end{array}
$$

Finally for part (c) we select (with $r$ as above) $s = [\langle -a, b \rangle]$ . Then it is easy to calculate that

$$
\begin{array}{r l} r + _ {Q} s & = [ \langle a, b \rangle ] + _ {Q} [ \langle - a, b \rangle ] \\ & = [ \langle a b + (- a) b, b b \rangle ] \\ & = [ \langle 0, b b \rangle ] = 0 _ {Q}, \end{array}
$$

since $\langle 0, bb \rangle \sim \langle 0, 1 \rangle$ .

As in any Abelian group, the inverse of $r$ is unique; we denote it as $-r$ . The above proof shows that $-[\langle a, b \rangle] = [\langle -a, b \rangle]$ .

For rational numbers, multiplication is simpler than addition. The informal calculation

$$
{\frac {a}{b}} \cdot {\frac {c}{d}} = {\frac {a c}{b d}}
$$

indicates that $\cdot_{q}$ should be defined by the equation

$$
[ \langle a, b \rangle ] \cdot_ {Q} [ \langle c, d \rangle ] = [ \langle a c, b d \rangle ].
$$

(Notice the close analogy with $+_{z}$ .) This multiplication function is well defined, as the following lemma verifies.

Lemma 5QD If $\langle a, b \rangle \sim \langle a', b' \rangle$ and $\langle c, d \rangle \sim \langle c', d' \rangle$ , then

$$
\langle a c, b d \rangle \sim \langle a ^ {\prime} c ^ {\prime}, b ^ {\prime} d ^ {\prime} \rangle .
$$

Proof The proof is exactly as in Lemma 5ZB, but with addition replaced by multiplication.

Example Recall that $1_{Q} = [\langle 1, 1 \rangle]$ . We can now check that $1_{Q}$ is a multiplicative identity element, i.e., that $r \cdot_{Q} 1_{Q} = r$ . We know that $r = [\langle a, b \rangle]$ for some $a$ and $b$ . Thus

$$
\begin{array}{r l} r \cdot_ {\mathcal {Q}} 1 _ {\mathcal {Q}} & = [ \langle a, b \rangle ] \cdot_ {\mathcal {Q}} [ \langle 1, 1 \rangle ] \\ & = [ \langle a \cdot 1, b \cdot 1 \rangle ] \\ & = [ \langle a, b \rangle ] \\ & = r. \end{array}
$$

You should also verify that $r \cdot_{Q} 0_{Q} = 0_{Q}$ .

Theorem 5QE Multiplication of rationals is associative, commutative, and distributive over addition:

$$
\begin{array}{c} (p \cdot_ {Q} q) \cdot_ {Q} r = p \cdot_ {Q} (q \cdot_ {Q} r), \\ q \cdot_ {Q} r = r \cdot_ {Q} q, \\ p \cdot_ {Q} (q + _ {Q} r) = (p \cdot_ {Q} q) + _ {Q} (p \cdot_ {Q} r). \end{array}
$$

Proof The verification of associativity and commutativity is directly analogous to verification of the same properties for $+_{z}$ .

We will proceed to prove the distributive law. We know that we can write $p = [\langle a, b \rangle]$ , $q = [\langle c, d \rangle]$ , and $r = [\langle e, f \rangle]$ for some integers a, b, c, d, e, and f. Then

$$
\begin{array}{r l} p \cdot_ {Q} (r + _ {Q} s) = [ \langle a, b \rangle ] \cdot_ {Q} ([ \langle c, d \rangle ] + _ {Q} [ \langle e, f \rangle ]) \\ & = [ \langle a, b \rangle ] \cdot_ {Q} [ \langle c f + e d, d f \rangle ] \\ & = [ \langle a c f + a e d, b d f \rangle ]. \end{array}
$$

On the other side of the expected equation we have

$$
\begin{array}{r l} (p \cdot_ {Q} r) + _ {Q} (p \cdot_ {Q} s) & = ([ \langle a, b \rangle ] \cdot_ {Q} [ \langle c, d \rangle ]) + _ {Q} ([ \langle a, b \rangle ] \cdot_ {Q} [ \langle e, f \rangle ]) \\ & = [ \langle a c, b d \rangle ] + _ {Q} [ \langle a e, b f \rangle ] \\ & = [ \langle a c b f + a e b d, b d b f \rangle ]. \end{array}
$$

This agrees with the first calculation because $\langle i,j\rangle\sim\langle bi,bj\rangle$ .

The new property the rationals have (and that integers lack) is the existence of multiplicative inverses.

Theorem 5QF For every nonzero $r$ in $\mathbb{Q}$ there is a nonzero $q$ in $\mathbb{Q}$ such that $r \cdot_{\mathcal{Q}} q = 1_{\mathcal{Q}}$ .

Proof The given $r$ must be of the form $[\langle a, b \rangle]$ , where $a \neq 0$ , let $r = 0_{Q}$ . Let $q = [\langle b, a \rangle]$ . Then $q \neq 0_{Q}$ and $r \cdot_{Q} q = [\langle ab, ab \rangle] = 1_{Q}$ .

We can use the existence of multiplicative inverses to show that there are no zero divisors in $\mathbb{Q}$ :

Corollary 5QG If $r$ and $s$ are nonzero rational numbers, then $r \cdot_{\mathcal{Q}} s$ is also nonzero.

Proof The preceding theorem provides us with rationals $r'$ and $s'$ for which $r \cdot_{Q} r' = s \cdot_{Q} s' = 1_{Q}$ . Hence

$$
\left(r \cdot_ {Q} s\right) \cdot_ {Q} \left(r ^ {\prime} \cdot_ {Q} s ^ {\prime}\right) = 1 _ {Q}
$$

by using commutative and associative laws. But this implies that $r \cdot_{Q} s \neq 0_{Q}$ , because $0_{Q} \cdot_{Q}(r' \cdot_{Q} s') = 0_{Q} \neq 1_{Q}$ .

We can restate this corollary by saying that the set of nonzero rational numbers is closed under multiplication; i.e., the product of numbers in this set is again in this set.

As a result of the foregoing theorems, we can assert that the nonzero rationals with multiplication form an Abelian group. That is, multiplication gives us a binary operation on the nonzero rationals that is associative and commutative, we have an identity element $1_{Q}$ , and we have multiplicative inverses. As in any Abelian group, the inverse of r is unique; we denote it as $r^{-1}$ . The proof of Theorem 5QF shows that

$$
[ \langle a, b \rangle ] ^ {- 1} = [ \langle b, a \rangle ].
$$

Inverses provide us with a division operation. For a nonzero rational r we can define

$$
s \div r = s \cdot_ {Q} r ^ {- 1}.
$$

Then we have

$$
\begin{array}{c} \left[ \langle c, d \rangle \right] \div \left[ \langle a, b \rangle \right] = \left[ \langle c, d \rangle \right] \cdot_ {Q} \left[ \langle b, a \rangle \right] \\ = \left[ \langle c b, d a \rangle \right], \end{array}
$$

a version of the “invert and multiply” rule for division of fractions.

The algebraic concept exemplified by the rational numbers is the concept of a field. To say that $\langle Q, +_{Q}, \cdot_{Q}, 0_{Q}, 1_{Q} \rangle$ is a field means that it is an integral domain with the further property that multiplicative inverses exist. (Other examples of fields are provided by the real numbers and by the complex numbers.) The method we have used to extend from Z to Q can be applied to extend any integral domain to a field.

Next we want to define the ordering relation for the rational numbers. The informal calculation

$$
\frac {a}{b} <   \frac {c}{d} \quad \text { iff } \quad a d <   c b
$$

is correct if b and d are positive. There is no guarantee that denominators are always positive. But because

$$
[ \langle a, b \rangle ] = [ \langle - a, - b \rangle ],
$$

every rational number can be represented by some fraction with a positive denominator. (Recall that for nonzero $b$ , either $b$ or $-b$ is positive.) The above informal calculation then suggests that we define $<_Q$ so that

$$
[ \langle a, b \rangle ] <   _ {Q} [ \langle c, d \rangle ] \quad \text { iff } \quad a d <   c b
$$

whenever b and d are positive. As with $<_{z}$ , we must verify that this condition yields a well-defined relation. The following lemma accomplishes the verification.

Lemma 5QH Assume that $\langle a, b \rangle \sim \langle a', b' \rangle$ and $\langle c, d \rangle \sim \langle c', d' \rangle$ . Further assume that $b, b', d$ , and $d'$ are all positive. Then

$$
a d <   c b \quad \text { iff } \quad a ^ {\prime} d ^ {\prime} <   c ^ {\prime} b ^ {\prime}.
$$

Proof The proof is the same as the proof of Lemma 5ZH, but with multiplication of integers in place of addition of natural numbers.

This lemma guarantees that when we test to see whether or not $r <_{Q}s$ , it does not matter which fractions with positive denominators we choose from r and s.

Example To check that $0_{Q} <_{Q} 1_{Q}$ , we choose fractions $\langle 0, 1 \rangle \in 0_{Q}$ and $\langle 1, 1 \rangle \in 1_{Q}$ . Then since $0 \cdot 1 < 1 \cdot 1$ , we do indeed have $0_{Q} <_{Q} 1_{Q}$ . But we could also have chosen fractions $\langle 0, 4 \rangle \in 0_{Q}$ and $\langle 3, 3 \rangle \in 1_{Q}$ . Then since $0 \cdot 3 < 3 \cdot 4$ , we again find, in consistency with the first calculation, that $0_{Q} <_{Q} 1_{Q}$ .

Theorem 5QI The relation $<_{Q}$ is a linear ordering on $\mathbb{Q}$ .

Proof The proof is the same as the proof of Theorem 5ZI, with multiplication in place of addition. For example, to prove trichotomy, we consider rational numbers r and s. For suitable integers we can write

$$
r = [ \langle a, b \rangle ] \quad \text { and } \quad s = [ \langle c, d \rangle ],
$$

where b and d are positive. Then trichotomy for Z tells us that exactly one of

$$
a d <   c b, \quad a d = c b, \quad c b <   a d
$$

holds, whence exactly one of

$$
r <   _ {Q} s, \quad r = s, \quad s <   _ {Q} r
$$

holds.

One can check that $r <_{Q}0_{Q}$ iff $0_{Q} <_{Q} - r$ (Exercise 12). Call q positive iff $0_{Q} <_{Q} q$ . Then as a consequence of trichotomy, we have the fact for any rational number r, exactly one of the three alternatives

$r$ is positive, $r$ is zero, $-r$ is positive

holds. We can define the absolute value $|r|$ of $r$ by

$$
| r | = \left\{ \begin{array}{c l} - r & \text { if } - r \text { is   positive }, \\ r & \text { otherwise }. \end{array} \right.
$$

Then $0_{Q} \leq_{Q} |r|$ for every $r$ .

Next we prove that order is preserved by addition and by multiplication by a positive factor.

Theorem 5QJ Let r, s, and t be rational numbers.

(a) $r < _{Q}s$ iff $r + _{Q}t < _{Q}s + _{Q}t$ .

(b) If $t$ is positive, then

$$
r <   _ {Q} s \quad \text { iff } \quad r \cdot_ {Q} t <   _ {Q} s \cdot_ {Q} t.
$$

Proof Part (b) has the same proof as part (a) of Theorem 5ZJ, but with multiplication in place of addition. To prove part (a), we first write r, s, and t in the form

$$
r = [ \langle a, b \rangle ], \quad s = [ \langle c, d \rangle ], \quad t = [ \langle e, f \rangle ],
$$

where b, d, and f are positive. Since t is a positive rational, e is also a positive integer. Then

$$
\begin{array}{l l l} r + _ {Q} t <   _ {Q} s + _ {Q} t & \Leftrightarrow & [ \langle a f + e b, b f \rangle ] <   _ {Q} [ \langle c f + e d, d f \rangle ] \\ & \Leftrightarrow & (a f + e b) d f <   (c f + e d) b f \\ & \Leftrightarrow & a d f f + b d e f <   b c f f + b d e f \\ & \Leftrightarrow & a d <   b c \qquad \text {by Theorem 5ZJ} \\ & \Leftrightarrow & r <   _ {Q} s \end{array}
$$

as desired.

We have already said that the rational numbers form a field; the two preceding theorems state that $\langle \mathbb{Q}, +_Q, \cdot_Q, 0_Q, 1_Q, <_Q \rangle$ is an ordered field.

Theorem 5QK The following cancellation laws hold for any rational numbers.

(a) If $r + _o t = s + _o t$ , then $r = s$ .

(b) If $r \cdot_{Q} t = s \cdot_{Q} t$ and $t$ is nonzero, then $r = s$ .

Proof We can prove this as a corollary of the preceding theorem, following our past pattern. But there is now a simpler option open to us. In part (a) we add -t to both sides of the given equation, and in part (b) we multiply both sides of the given equation by $t^{-1}$ . (This proof works in any Abelian group.)

Finally, we want to show that, although Z is not a subset of Q, nevertheless Q has a subset that is “just like” Z. Define the embedding function $E: Z \rightarrow Q$ by

$$
E (a) = [ \langle a, 1 \rangle ].
$$

This functions gives us an isomorphic embedding in the sense that the following theorem holds.

Theorem 5QL E is a one-to-one function from Z into Q satisfying the following conditions:

(a) $E(a + b) = E(a) + _Q E(b)$ .

(b) $E(ab) = E(a) \cdot_{Q} E(b).$

(c) $E(0) = 0_{Q}$ and $E(1) = 1_{Q}$ .

(d) $a < b$ iff $E(a) < _Q E(b)$ .

Proof Each part of the theorem can be proved by direct calculation. First we check that E is one-to-one:

$$
\begin{array}{r c l} E (a) = E (b) & \Rightarrow & [ \langle a, 1 \rangle ] = [ \langle b, 1 \rangle ] \\ & \Rightarrow & \langle a, 1 \rangle \sim \langle b, 1 \rangle \\ & \Rightarrow & a = b. \end{array}
$$

Parts (a), (b), and (d) are proved by the following calculations:

$$
\begin{array}{r c l} E (a) + _ {Q} E (b) & = & [ \langle a, 1 \rangle ] + _ {Q} [ \langle b, 1 \rangle ] \\ & = & [ \langle a + b, 1 \rangle ] \\ & = & E (a + b), \end{array}
$$

$$
\begin{array}{r c l} E (a) \cdot_ {Q} E (b) & = & [ \langle a, 1 \rangle ] \cdot_ {Q} [ \langle b, 1 \rangle ] \\ & = & [ \langle a b, 1 \rangle ] \\ & = & E (a b), \end{array}
$$

$$
\begin{array}{r c l} E (a) <   _ {Q} E (b) & \Leftrightarrow & [ \langle a, 1 \rangle ] <   _ {Q} [ \langle b, 1 \rangle ] \\ & \Leftrightarrow & a \cdot 1 <   b \cdot 1 \\ & \Leftrightarrow & a <   b. \end{array}
$$

Finally part (c) is a restatement of the definitions of $0_{Q}$ and $1_{Q}$ .

We also obtain the following relation between fractions and division:

$$
[ \langle a, b \rangle ] = E (a) \div E (b).
$$

Since $b \neq 0$ , we have $E(b) \neq 0_{\sigma}$ , and so the indicated division is possible.

Henceforth we will simplify the notation by omitting the subscript “Q” on $+_{Q}, \cdot_{Q}, 0_{Q}$ , and so forth. Also the product $r \cdot s$ will usually be written as just rs.

## Exercises

10. Show that $r \cdot_{Q} 0_{Q} = 0_{Q}$ for every rational number $r$ .

11. Give a direct proof (not using Theorem 5QF) that if $r \cdot_{Q} s = 0_{Q}$ , then either $r = 0_{Q}$ or $s = 0_{Q}$ .

12. Show that

$$
r <   _ {Q} 0 _ {Q} \quad \text { iff } \quad 0 _ {Q} <   _ {Q} - r.
$$

13. Give a new proof of the cancellation law for $+_{z}$ (Corollary 5ZK(a)), using Theorem 5ZD instead of Theorem 5ZJ.

14. Show that the ordering of rationals is dense, i.e., between any two rationals there is a third one:

$$
p <   _ {Q} s \Rightarrow (\exists r) (p <   _ {Q} r <   _ {Q} s).
$$

## REAL NUMBERS

The last number system that we will consider involves the set R of all real numbers. The ancient Pythagoreans discovered, to their dismay, that there was a need to go beyond the rational numbers. They found that there simply was no rational number to measure the length of the hypotenuse of a right triangle whose other two sides had unit length.

In our previous extensions of number systems, we relied on the facts that an integer could be named by a pair of natural numbers, and a rational number could be named by a pair of integers. But we cannot hope to name real number by a pair of rationals, because, as we will prove in Chapter 6, there are too many real numbers and not enough pairs of rationals. Hence we must look at new techniques in searching for a way to name real numbers.

Actually there are several methods that can be used successfully to construct the real numbers. One approach is to utilize decimal expansions, so that a real number is determined by an integer and an infinite sequence of digits (a function from $\omega$ into 10). This approach may be found in Claude Burrill's book, Foundations of Real Numbers, McGraw-Hill, 1967.

A more common method of constructing a suitable set R is to utilize the fact that a real number can be named by giving a sequence of rationals (a function from $\omega$ into Q) converging to it. So one can take the set of all convergent sequences and then divide out by an equivalence relation (where two sequences are equivalent iff they converge to the same limit). But there is one hitch: The concepts of “convergent” and “equivalent” must be defined without reference to the real number to which the sequence is converging. This can be done by a technique named after Cauchy.

Define a Cauchy sequence to be a function $s: \omega \to \mathbb{Q}$ such that $|s_m - s_n|$ is arbitrarily small for all sufficiently large $m$ and $n$ ; i.e.,

$$
(\forall \text { positive } \varepsilon \text { in } \mathbb {Q}) (\exists k \in \omega) (\forall m > k) (\forall n > k) | s _ {m} - s _ {n} | <   \varepsilon .
$$

(Here we write $s_{n}$ in place of $s(n)$ , as usual for $\omega$ -sequences.) The concept of a Cauchy sequence is useful here because of the theorem of calculus asserting that a sequence is convergent iff it is a Cauchy sequence.

Let C be the set of all Cauchy sequences. For r and s in C, we define r and s to be equivalent $(r \sim s)$ iff $|r_{n} - s_{n}|$ is arbitrarily small for all sufficiently large n; i.e.,

$$
(\forall \text { positive } \varepsilon \text { in } \mathbb {Q}) (\exists k \in \omega) (\forall n > k) | r _ {n} - s _ {n} | <   \varepsilon .
$$

Then the quotient set $C / \sim$ is a suitable candidate for $\mathbb{R}$ . (This approach to constructing $\mathbb{R}$ is due to Cantor.)

An alternative construction of R uses so-called Dedekind cuts. This is the method we follow henceforth in this section. The Cauchy sequence construction and the Dedekind cut construction each have their own advantages. The Dedekind cut construction of R has an initial advantage of simplicity, in that it provides a simple definition of R and its ordering. But multiplication of Dedekind cuts is awkward, and verification of the properties of multiplication is a tedious business. The Cauchy sequence construction of R also has the advantage of generality, since it can be used with an arbitrary metric space in place of Q.

With these considerations in mind, we choose the following strategy. We will present the Dedekind cut construction, and will prove that least upper bounds exist in R. (This is the property that distinguishes R from the other ordered fields.) Although we will define addition and multiplication of real numbers, we will not give complete verification of the algebraic properties. The Cauchy sequence construction may be found, among other places, in Norman Hamilton and Joseph Landin's book, Set Theory and the Structure of Arithmetic, Allyn and Bacon, 1961.

The idea behind Dedekind cuts is that a real number x can be named by giving an infinite set of rationals, namely all the rationals less than x. We will in effect define x to be the set of all rationals smaller than x. To avoid circularity in the definition, we must be able to characterize the sets of rationals obtainable in this way. The following definition does the job.

Definition A Dedekind cut is a subset x of Q such that:

(a) $\varnothing \neq x \neq \mathbb{Q}$ .

(b) $x$ is "closed downward," i.e.,

$$
q \in x \& r <   \dot {q} \Rightarrow r \in x.
$$

(c) $x$ has no largest member.

We then define the set R of real numbers to be the set of all Dedekind cuts. Note that there is no equivalence relation here; a real (i.e., a real number) is a cut, not an equivalence class of cuts.

The ordering on $\mathbb{R}$ is particularly simple. For $x$ and $y$ in $\mathbb{R}$ , define

$$
x <   _ {R} y \quad \text { iff } \quad x \subset y.
$$

In other words, $<_{R}$ is the relation of being a proper subset:

$$
<   _ {R} = \{\langle x, y \rangle \in \mathbb {R} \times \mathbb {R} | x \subset y \}.
$$

Theorem 5RA The relation $<_{R}$ is a linear ordering on $\mathbb{R}$ .

Proof The relation is clearly transitive; we must show that it satisfies trichotomy on R. So consider any x and y in R. Obviously at most one of the alternatives,

$$
x \subset y, \quad x = y, \quad y \subset x,
$$

can hold, but we must prove that at least one holds. Suppose that the first two fail, i.e., that $x \not\subseteq y$ . We must prove that $y \subset x$ .

Since $x \not\subseteq y$ there is some rational $r$ in the relative complement $x - y$ (see Fig. 23). Consider any $q \in y$ . If $r \leq q$ , then since $y$ is closed downward, we would have $r \in y$ . But $r \notin y$ , so we must have q < r. Since x is closed downward, it follows that $q \in x$ . Since q was arbitrary (and $x \neq y$ ), we have $y \subset x$ .

![](images/3256aa9ac38841b4bd30ad936324cebe07803e7107ca4c66bb5634ffe623cd6f.jpg)  
Fig. 23. The proof of Theorem 5RA.

Now consider a set A of reals; a real number x is said to be an upper bound of A iff $y \leq_{R} x$ for every y in A. The number x itself might or might not belong to A. The set A is bounded (i.e., bounded above) iff there exists some upper bound of A. A least upper bound of A is an upper bound that is less than any other upper bound.

First consider an example not in R, but in Q. The set

$$
\{r \in \mathbb {Q} \mid r \cdot r <   2 \}
$$

of rationals whose square is less than 2 is a bounded set of rationals that has no least upper bound in Q. (We are stating this, not proving it, but it follows from the fact that $\sqrt{2}$ is irrational.) The following theorem shows that examples of this sort cannot be found in R.

Theorem 5RB Any bounded nonempty subset of R has a least upper bound in R.

Proof Let $A$ be the set of real numbers in question. We will show that the least upper bound is just $\bigcup A$ .

Simply by the definition of $\bigcup A$ , we have $x \subseteq \bigcup A$ for all $x \in A$ . Furthermore let $z$ be any upper bound for $A$ , so that $x \subseteq z$ for all $x \in A$ . It then follows that $\bigcup A \subseteq z$ ; compare Exercise 5 of Chapter 2. The argument so far is not tied to $\mathbb{R}$ ; we have only shown that $\bigcup A$ is the least upper bound of the set $A$ with respect to ordering by inclusion.

What remains to be shown is that $\bigcup A \in \mathbb{R}$ . Because $A$ is nonempty, it is easy to see that $\bigcup A \neq \varnothing$ . Also $\bigcup A \neq \mathbb{Q}$ because $\bigcup A \subseteq z$ where $z$ is an upper bound for $A$ . You can easily verify (Exercise 15) that $\bigcup A$ is closed downward and has no largest element.

The foregoing theorem is important in mathematical analysis. For example, it is needed in order to prove that a continuous function on a closed interval assumes a maximum. And this in turn is used to prove the mean value theorem of calculus.

The addition operation for $\mathbb{R}$ is easily defined from addition of rationals. For reals $x$ and $y$ , define:

$$
x + _ {R} y = \{q + r \mid q \in x \& r \in y \}.
$$

Lemma 5RC For real numbers $x$ and $y$ , the sum $x + _R y$ is also in $\mathbb{R}$ .

Proof Clearly $x + _R y$ is a nonempty subset of $\mathbb{Q}$ . To show that $x + _R y \neq \mathbb{Q}$ , choose some $q'$ in $\mathbb{Q} - x$ and $r'$ in $\mathbb{Q} - y$ . Then

$$
\begin{array}{r c l} q \in x \& r \in y & \Rightarrow & q <   q ^ {\prime} \& r <   r ^ {\prime} \\ & \Rightarrow & q + r <   q ^ {\prime} + r ^ {\prime} \end{array}
$$

so that any member $q + r$ of $x + _R y$ is strictly less than $q' + r'$ . Hence $q' + r' \notin x + _R y$ .

To show that $x + _R y$ is closed downward, consider any

$$
p <   q + r \in x + _ {R} y
$$

(where $q \in x$ and $r \in y$ ). Then adding $-q$ to both sides of the inequality, we have $p - q < r$ . Since $y$ is closed downward, we have $p - q \in y$ . Thus we can write $p$ as the sum

$$
p = q + (p - q)
$$

of $q$ from $x$ and $p - q$ from $y$ ; this is what we need to have $p \in x + _R y$ . (Note: Here “ $p - q$ ” refers to subtraction of rationals, $p + (-q)$ . Earlier in this proof “ $\mathbb{Q} - x$ ” referred to the relative complement of $x$ in $\mathbb{Q}$ . If this sort of thing happened often, we would use a different symbol “ $\mathbb{Q} \setminus x$ ” for complements. But in fact the opportunities for confusion will be rare.)

We leave it to you to verify that $x + _R y$ has no largest member (Exercise 16).

Theorem 5RD Addition of real numbers is associative and commutative:

$$
\begin{array}{r} (x + _ {R} y) + _ {R} z = x + _ {R} (y + _ {R} z), \\ x + _ {R} y = y + _ {R} x. \end{array}
$$

Proof Since addition of rationals is commutative, it is clear from the definition of $+_{R}$ that it is commutative as well. As for associativity, we have

$$
\begin{array}{r l} (x + _ {R} y) + _ {R} z & = \{s + r \mid s \in x + _ {R} y \& r \in z \} \\ & = \{(p + q) + r \mid p \in x \& q \in y \& r \in z \}, \end{array}
$$

and a similar calculation applies to the other grouping. Thus associativity of $+_{R}$ follows from associativity of addition of rationals.

The zero element of R is defined to be the set of negative rational numbers:

$$
0 _ {R} = \{r \in \mathbb {Q} \mid r <   0 \}.
$$

Theorem 5RE (a) $0_{R}$ is a real number.

(b) For any $x$ in $\mathbb{R}$ , we have $x + _R 0_R = x$ .

Proof (a) It is easy to see that $\varnothing \neq 0_R \neq \mathbb{Q}$ ; for example, $-1 \in 0_R$ and $1 \notin 0_R$ . And it is clear that $0_R$ is closed downward. The fact that $0_R$ has no largest member follows immediately from the density of the rationals (Exercise 14).

For part (b), we must prove that

$$
\{r + s \mid r \in x \& s <   0 \} = x.
$$

The “ $\subseteq$ ” inclusion holds because $x$ is closed downward. To prove the “ $\supseteq$ ” half, consider any $p$ in $x$ . Since $x$ has no largest member, there is some $r$ with $p < r \in x$ . Let $s = p - r$ . Then $s < 0$ and $p = r + s \in 0_R$ . Hence both inclusions hold.

![](images/e688b8ceac75d35e5c4cf955d102c8a84fbac983b7f016e049fd26df280a70ae.jpg)  
Fig. 24. Sometimes $-x$ is $\{r\in\mathbb{Q}\mid-r\notin x\}$ , but not always.

![](images/0ed5b659df21051712c974bc73232b0268e250aa21ab05b5f512ff50e9ee1dbf.jpg)  
(a)

![](images/2b121b16b2ad3b6cf61c3e8e3767771f6215a9b9537ec175962f64f841fd9d00.jpg)  
Fig. 25. In (a) $x$ is negative; in (b) $x$ is positive.

Before we can conclude that the real numbers form an Abelian group with $+_{R}$ and $0_{R}$ , we must prove that additive inverses exist. First we need to say just what set $-x$ should be (where $x \in \mathbb{R}$ ). We think of the real number $--x$ as the set of all smaller rational numbers. If we draw a picture as in Fig. 24, we might be tempted to think that $-x$ is the complement of $\{r \in \mathbb{Q} \mid -r \in x\}$ , or in other words, that $-x$ should be $\{r \in \mathbb{Q} \mid -r \notin x\}$ . This choice is not quite right, because it may have a largest element. Instead we define

$$
- x = \{r \in \mathbb {Q} | (\exists s > r) - s \notin x \}.
$$

In Fig. 25, -x is illustrated as a subset of the rational number line.

Theorem 5RF For every $x$ in $\mathbb{R}$ :

$$
\begin{array}{l l} \text {(a)} & - x \in \mathbb {R}, \\ \text {(b)} & x + _ {R} (- x) = 0 _ {R}. \end{array}
$$

Proof To prove that $-x$ is a real number, we first must show that $\varnothing \neq -x \neq \mathbb{Q}$ . There is some rational $t$ with $t \notin x$ ; let $r = -t - 1$ . Then $r \in -x$ because $r < -t$ and $-(t) \notin x$ . Hence $-x \neq \emptyset$ . To show that $-x \neq \mathbb{Q}$ , take any $p \in x$ . We claim that $-p \notin -x$ . This holds because if $s > -p$ , then $-s < p \in x$ , whence $-s \in x$ . Hence $-p \notin -x$ and so $-x \neq \mathbb{Q}$ . It is easier to show that $-x$ is closed downward. Suppose that $q < r \in -x$ . Then $(\exists s > r) - s \notin x$ . Consequently $(\exists s > q) - s \notin x$ , since the same $s$ can be used. Hence $q \in -x$ .

It remains to show that -x has no largest element. Consider then any element r in -x. We know that for some s > r we have $-s \notin x$ . Because the rationals are densely ordered (Exercise 14), there is some p with s > p > r. Then $p \in -x$ , and p is larger than r. This completes the proof that -x is a real number.

Now we turn to part (b). By definition

$$
x + _ {R} (- x) = \{q + r \mid q \in x \& (\exists s > r) - s \notin x \}.
$$

For any such member $q + r$ of this set, we have $r < s$ and $q < -s$ (lest $-s \leq q \in x$ ). Hence by the order-preserving property of addition,

$$
q + r <   (- s) + s = 0.
$$

This shows that $x + _R(-x) \subseteq 0_R$ .

To establish the other inclusion, consider any $p$ in $0_R$ . Then $p < 0$ , and so $-p$ is positive. By Exercise 19, there is some $q \in x$ for which $q + (-p \div 2) \notin x$ . Let $s = (p \div 2) - q$ , so that $-s \notin x$ . Then $p$ is the sum of $q$ (which is in $x$ ) and $p - q$ (which is less than $s$ , where $-s \notin x$ ). This makes $p$ a member of $x + _R(-x)$ . Thus we have both inclusions.

We have now shown that $\langle R, +_{R}, 0_{R} \rangle$ is an Abelian group. As in any Abelian group, the cancellation law holds:

Corollary 5RG For any real numbers,

$$
x + _ {R} z = y + _ {R} z \Rightarrow x = y.
$$

Proof Simply add -z to both sides of the given equation.

Next we prove that addition preserves order.

Theorem 5RH For any real numbers,

$$
x <   _ {R} y \Leftrightarrow x + _ {R} z <   _ {R} y + _ {R} z.
$$

Proof It is easy to prove that

$$
x \leq_ {R} y \Rightarrow x + _ {R} z \leq_ {R} y + _ {R} z,\tag{1}
$$

because this amounts to the statement that if $x \subseteq y$ , then

$$
\{q + s \mid q \in x \& s \in z \} \subseteq \{r + s \mid r \in y \& s \in z \},
$$

which is obvious. And by Corollary 5RG we have

$$
x \neq y \Rightarrow x + _ {R} z \neq y + _ {R} z,\tag{2}
$$

which together with (1) gives the “ $\Rightarrow$ ” half of the theorem. The “ $\Leftarrow$ ” half then follows by trichotomy (as in the proof to Theorem 4N).

We can define the absolute value $|x|$ of a real number x to be the larger of x and -x. Since our ordering is inclusion, the larger of the two is just their union. Thus our definition becomes

$$
| x | = x \cup - x.
$$

Then by Exercise 20, $|x|$ is always nonnegative, i.e., $0_R \leq_R |x|$ .

Consider now the definition of multiplication. For the product of x and y we cannot use $\{rs \mid r \in x \& s \in y\}$ (in analogy to the definition of $x +_{R}y$ ), because both x and y contain negative rationals of large magnitude. Instead we use the following variation on the above idea.

Definition (a) If $x$ and $y$ are nonnegative real numbers, then

$$
x \cdot_ {R} y = 0 _ {R} \cup \{r s \mid 0 \leq r \in x \& 0 \leq s \in y \}.
$$

(b) If $x$ and $y$ are both negative real numbers, then

$$
x \cdot_ {R} y = | x | \cdot_ {R} | y |.
$$

(c) If one of the real numbers $x$ and $y$ is negative and one is nonnegative, then

$$
x \cdot_ {R} y = - (| x | \cdot_ {R} | y |).
$$

The facts we want to know about multiplication are gathered into the following theorem. Let $1_{R}=\{r\in Q \mid r<1\}$ . Clearly $0_{R}<_{R}1_{R}$ . We will not give a proof for this theorem; a proof can be found in Appendix F of Number Systems and the Foundations of Analysis by Elliott Mendelson (Academic Press, 1973).

Theorem 5RI For any real numbers, the following hold:

(a) $x \cdot_{R} y$ is a real number.

(b) Multiplication is associative, commutative, and distributive over addition.

(c) $0_{R} \neq 1_{R}$ and $x \cdot_{R} 1_{R} = x$ .

(d) For nonzero $x$ there is a nonzero real number $y$ with $x \cdot_{R} y = 1_{R}$

(e) Multiplication by a positive number preserves order: If $0_{R} < _{R}z$ , then

$$
x <   _ {R} y \Leftrightarrow x \cdot_ {R} z <   _ {R} y \cdot_ {R} z.
$$

The foregoing theorems show that, like the rationals, the reals (with $+_{R}, \cdot_{R}, 0_{R}, 1_{R}$ , and $<_{R}$ ) form an ordered field. But unlike the rationals, the reals have the least-upper-bound property (Theorem 5RB). An ordered field is said to be complete iff it has the least-upper-bound property. It can be shown that the reals, in a sense, yield the only complete ordered field. That is, any other complete ordered field is “just like” (or more precisely, is isomorphic to) the ordered field of real numbers. For an exact statement of this theorem and for its proof, see any of the books we have referred to in this section, or p. 110 of Andrew Gleason’s book, Fundamentals of Abstract Analysis, Addison-Wesley, 1966.

The correct embedding function E from Q into R assigns to each rational number r the corresponding real number

$$
E (r) = \{q \in \mathbb {Q} \mid q <   r \},
$$

consisting of all smaller rationals.

Theorem 5RJ $E$ is a one-to-one function from $\mathbb{Q}$ into $\mathbb{R}$ satisfying the following conditions:

(a) $E(r + s) = E(r) + _R E(s).$

(b) $E(rs) = E(r) \cdot_{R} E(s).$

(c) $E(0) = 0_{R}$ and $E(1) = 1_{R}$ .

(d) $r < s$ iff $\bar{E}(r) < _R E(s)$ .

Proof First of all, we must show that $E(r)$ is a real number. Obviously $E(r)$ is a set of rationals, and it is closed downward. Furthermore $\varnothing \neq E(r) \neq Q$ because $r - 1 \in E(r)$ and $r \notin E(r)$ . $E(r)$ has no largest element, because if $q \in E(r)$ , then by Exercise 14 there is a larger element p with q < p < r. Hence $E(r)$ is indeed a real number.

To show that E is one-to-one, suppose that $r \neq s$ . Then one is less than the other; we may suppose that r < s. Then $r \in E(s)$ whereas $s \notin E(s)$ . Hence $E(r) \neq E(s)$ .

Next let us prove part (d), because it is easy. If $r < s$ , then clearly $E(r) \subseteq E(s)$ . The inclusion is proper since $E$ is one-to-one. Thus

$$
r <   s \Rightarrow E (r) \subset E (s).
$$

The converse follows from trichotomy. If $E(r) \subset E(s)$ , then we cannot have $r = s$ nor $s < r$ (lest $E(s) \subset E(r)$ ), so we must have $r < s$ .

For part (a), we have

$$
\begin{array}{r l} E (r) + _ {R} E (s) & = \{p + q \mid p \in E (r) \& q \in E (s) \} \\ & = \{p + q \mid p <   r \& q <   s \}. \end{array}
$$

We must show that this is the same as $E(r + s)$ , i.e., that

$$
\{p + q \mid p <   r \& q <   s \} = \{t \mid t <   r + s \}.
$$

The “⊆” inclusion holds because by Theorem 5QJ,

$$
p + q <   r + q <   r + s.
$$

To establish the “ $\supseteq$ ” inclusion, suppose that $t < r + s$ . Let $\varepsilon = (r + s - t) \div 2$ ; then $\varepsilon > 0$ . Define $p = r - \varepsilon$ and $q = s - \varepsilon$ . Then $p < r$ and $q < s$ and $p + q = t$ . Thus we can represent $t$ as a sum in the desired form. Hence both inclusions hold.

Finally, we omit the (awkward) proof of part (b), and part (c) is only a restatement of definitions.

## Exercises

15. In Theorem 5RB, show that $\bigcup A$ is closed downward and has no largest element.

16. In Lemma 5RC, show that $x + _R y$ has no largest element.

17. Assume that $a$ is a positive integer. Show that for any integer $b$ there is some $k$ in $\omega$ with

$$
b <   a \cdot E (k).
$$

18. Assume that p is a positive rational number. Show that for any rational number r there is some k in $\omega$ with

$$
r <   p \cdot E (E (k)).
$$

(Here k is in $\omega$ , $E(k)$ is the corresponding integer, and $E(E(k))$ is the corresponding rational.)

19. Assume that $p$ is a positive rational number. Show that for any real number $x$ there is some rational $q$ in $x$ such that

$$
p + q \notin x.
$$

20. Show that for any real number $x$ , we have $0_{R} \leq_{R} |x|$ .

21. Show that if $x < _R y$ , then there is a rational number $r$ with

$$
x <   _ {R} E (r) <   _ {R} y.
$$

22. Assume that $x \in R$ . How do we know that $|x| \in R$ ?

## SUMMARIES

In this chapter we have given one way of constructing the real numbers as particular sets. Along the way, some concepts from abstract algebra have naturally arisen. For convenient reference, we have collected in the present section certain definitions that have played a key role in this chapter.

Integers Let $m, n, p$ , and $q$ be natural numbers.

$$
[ \langle m, n \rangle ] \sim [ \langle p, q \rangle ] \Leftrightarrow m + q = p + n,
$$

$$
\begin{array}{r l} & {\left[ \langle m, n \rangle \right] + _ {Z} [ \langle p, q \rangle ] = [ \langle m + p, n + q \rangle ],} \\ & {\qquad - [ \langle m, n \rangle ] = [ \langle n, m \rangle ],} \end{array}
$$

$$
[ \langle m, n \rangle ] \cdot_ {Z} [ \langle p, q \rangle ] = [ \langle m p + n q, m p + n p \rangle ],
$$

$$
\begin{array}{c} \left[ \langle m, n \rangle \right] <   _ {Z} \left[ \langle p, q \rangle \right] \Leftrightarrow m + q \in p + n, \\ E (n) = [ \langle n, 0 \rangle ]. \end{array}
$$

Rational numbers Let $a, b, c$ , and $d$ be integers with $bd \neq 0$ .

$$
\langle a, b \rangle \sim \langle c, d \rangle \Leftrightarrow a d = c b,
$$

$$
[ \langle a, b \rangle ] + _ {Q} [ \langle c, d \rangle ] = [ \langle a d + c b, b d \rangle ],
$$

$$
- [ \langle a, b \rangle ] = [ \langle - a, b \rangle ],
$$

$$
[ \langle a, b \rangle ] \cdot_ {Q} [ \langle c, d \rangle ] = [ \langle a c, b d \rangle ],
$$

$[\langle a, b \rangle] < _Q [\langle c, d \rangle] \Leftrightarrow ad < cb,$ when $b$ and $d$ are positive,

$$
E (a) = [ \langle a, 1 \rangle ].
$$

Real numbers. A real number is a set $x$ such that $\varnothing \subset x \subset \mathbb{Q}$ , $x$ is closed downward, and $x$ has no largest member.

$$
\begin{array}{r l} & x <   _ {R} y \Leftrightarrow x \subset y, \\ & x + _ {R} y = \{q + r \mid q \in x \& r \in y \}, \\ & - x = \{r \in \mathbb {Q} \mid (\exists s > r) - s \notin x \}, \\ & | x | = x \cup - x, \\ & | x | \cdot_ {R} | y | = 0 _ {R} \cup \{r s \mid 0 \leq r \in | x | \& 0 \leq s \in | y | \}, \\ & E (r) = \{q \in \mathbb {Q} \mid q <   r \}. \end{array}
$$

Next we turn to the definitions from abstract algebra that are relevant to the number systems in this chapter.

An Abelian group (in additive notation) is a triple $^{2}$ $\langle A, +, 0\rangle$ consisting of a set A, a binary operation + on A, and an element (“zero”) of A, such that the following conditions are met:

1. + is associative and commutative.

2. 0 is an identity element, i.e., $x + 0 = x$ .

3. Inverses exist, i.e., $\forall x \exists y x + y = 0$ .

An Abelian group (in multiplicative notation) is a triple $\langle A, \cdot, 1\rangle$ consisting of a set A, a binary operation $\cdot$ on A, and an element 1 of A, such that the following conditions are met:

1. · is associative and commutative.

2. 1 is an identity element, i.e., $x \cdot 1 = x$ .

3. Inverses exist, i.e., $\forall x \exists y x \cdot y = 1$ .

This is, of course, the same as the preceding definition.

A group has the same definition, except that we do not require that the binary operation be commutative. All of the groups that we have considered have, in fact, been Abelian groups. But some of our results (e.g., the uniqueness of inverses) are correct in any group, Abelian or not.

A commutative ring with identity is a quintuple $\langle D, +, \cdot, 0, 1\rangle$ consisting of a set D, binary operations + and $\cdot$ on D, and distinguished elements 0 and 1 of D, such that the following conditions are met:

1. $\langle D, +, 0 \rangle$ is an Abelian group.

2. The operation $\cdot$ is associative and commutative, and is distributive over addition.

3. 1 is a multiplicative identity $(x \cdot 1 = x)$ and $0 \neq 1$ .

An integral domain is a commutative ring with identity with the additional property that there are no zero divisors:

4. If $x \neq 0$ and $y \neq 0$ , then also $x \cdot y \neq 0$ .

A field is a commutative ring with identity in which multiplicative inverses exist:

4'. If $x$ is a nonzero element of $D$ , then $x \cdot y = 1$ for some $y$ .

Any field is also an integral domain, because condition 4' implies condition 4 (see the proof to Corollary 5QG).

An ordered field is a sextuple $\langle D, +, \cdot, 0, 1, <\rangle$ such that the following conditions are met:

1. $\langle D, +, \cdot, 0, 1 \rangle$ is a field.

2. < is a linear ordering on $D$ .

3. Order is preserved by addition and by multiplication by a positive element:

$$
x <   y \Leftrightarrow x + z <   y + z.
$$

If $0 < z$ , then

$$
x <   y \Leftrightarrow x \cdot z <   y \cdot z.
$$

We can define ordered integral domain or even ordered commutative ring with identity by adjusting the first condition. A complete ordered field is an ordered field in which for every bounded nonempty subset of D there is a least upper bound.

The constructions in this chapter can be viewed as providing an existence proof for such fields. The conditions for a complete ordered field are not impossible to meet, for we have constructed a field meeting them.

## TWO

What is a two? What are numbers? These are awkward questions; yet when we discuss numbers one might naively expect us to know what it is we are talking about.

In the Real World, we do not encounter (directly) abstract objects such as numbers. Instead we find physical objects: a number of similar apples, a ruler, partially filled containers (Fig. 26).

![](images/47d0b879f193d9c1e603714995608968ed738b68d00e185b7bc076adbbd25748.jpg)  
Fig. 26. A picture of the Real World.

Somehow we manage to abstract from this physical environment the concept of numbers. Not in any precise sense, of course, but we feel inwardly that we know what numbers are, or at least some numbers like 2 and 3. And we have various mental images that we use when thinking about numbers (Fig. 27).

![](images/eadf596c9075c9295acd5b20002b8218d24e15ccc3705e6fd6b73fead99b4245.jpg)  
Fig. 27. Pictures of mental images.

Then at some point we acquire a mathematical education. This teaches us many formal manipulations of symbols (Fig. 28). It all seems fairly reasonable, but it can all be done without paying very much attention to what the symbols stand for. In fact computers can be programmed to carry out the manipulations without any understanding at all.

Since numbers are abstract objects (as contrasted with physical objects) it might be helpful to consider first other abstractions. Take honesty, for example. Honesty is a property possessed by those people whose utterances are true sentences, who do not fudge on their income tax, and so forth. By way of imitation, we can try characterizing two as the property that is true of exactly those sets that, for some distinct x and y, have as members x and y and nothing else. A slight variation on this proposal would be to eliminate sets and characterize two as the property that is true of exactly those properties that, for some distinct x and y, are true of x and y and nothing else. (This proposal is due to Frege.)

![](images/77a06bdca8d27dac5b7f4f20ccd8a2ed4de2b6ea91c0bf21a07333acf9f2f793.jpg)  
Fig. 28. Pictures of manipulated symbols.

If we define numbers in terms of properties, someone might ask us what a property is. And no matter how we define numbers, the procedure of defining one concept in terms of another cannot go on forever, producing an infinite regress of definitions. Eventually the procedure must be founded on a commonly agreed upon basis. Properties might form such a basis. For a mathematician, sets form a more workable basis.

Actually there is a close connection between properties and sets. Define the extension of a property to be the set of all objects of which that property is true. If a couple of properties have the same extension (i.e., if they are true of exactly the same objects), are they in fact one and the same property? Is the property of being a prime number less than 10 the same as the property of being a solution to

$$
x ^ {4} - 1 7 x ^ {3} + 1 0 1 x ^ {2} - 2 4 7 x + 2 1 0 = 0?
$$

If you answer “yes,” then one says that you are thinking of properties extensionally, whereas if you answer “no,” then you are thinking of properties intensionally. Both alternatives are legitimate, as long as the choice of alternatives is made clear. Either way, sets are the extensions of properties. (All sets are obtainable in this way; the set x is the extension of the property of belonging to x.)

We can recast Frege's proposal in terms of sets as follows: Two is the set having as members exactly those sets that, for some distinct $x$ and $y$ , have as members $x$ and $y$ and nothing else. But in Zermelo-Fraenkel set theory, there is no such set. (For the number one, you should check Exercise 8 of Chapter 2.) Our response to this predicament was to select artificially one particular set $\{\varnothing, \{\varnothing\}\}$ as a paradigm. Now $\{\varnothing, \{\varnothing\}\}$ is very different from the property that is true of exactly those sets that, for some distinct $x$ and $y$ , have as members $x$ and $y$ and nothing else, but it serves as an adequate substitute. Then rapidly one thing led to another, until we had the complete ordered field of real numbers. And as we have mentioned, one complete ordered field is very much like any other.

But let us back up a little. In mathematics there are two ways to introduce new objects:

(i) The new objects might be defined in terms of other already known objects.

(ii) The new objects can be introduced as primitive notions and axioms can be adopted to describe the notions. (This is not so much a way of answering foundational questions about the objects as it is a way of circumventing them.)

In constructing real numbers as certain sets we have selected the first path. The axiomatic approach would regard the definition of a complete ordered field as axioms concerning the real number system (as a primitive notion). On the other hand, for sets themselves we have followed (with stripes) the axiomatic method.

But what about the Real World and those mental images? And the manipulated symbols? We want not just any old concept of number, but a concept that accurately reflects our experiences with apples and rulers and containers, and accurately mirrors our mental images. This is not a precise criterion, since it demands that a precise mathematical concept be compared with informal and intuitive ideas. And consequently the question whether our concept is indeed accurate must be evaluated on informal grounds. Throughout this chapter our formulation of definitions has been motivated ultimately by our intuitive ideas. Is there any way we could have gone wrong?

Yes, we could have gone wrong. In seeking a number system applicable to problems dealing with physical objects and physical space, we might have been guided by erroneous ideas. There is always the possibility that lines in the Real World do not really resemble R. For example, over very short distances, space might be somehow quantized instead of being continuous. (Experimental evidence forced us to accept the fact that matter is quantized; experimental evidence has not yet forced us to accept similar ideas about space.) Or over very large distances, space might not be Euclidean (a possibility familiar to science-fiction buffs). In such events, mathematical theorems about R, while still true of R, would be less interesting, as they might be inapplicable to certain problems in the Real World.

Mathematical concepts are useful in solving problems from the Real World to the extent that the concepts accurately reflect the essential features of those problems. The process of solving a problem mathematically has three parts (Fig. 29). We begin with a Real World problem. Then we need to model the original problem by a mathematical problem. This typically requires simplifying or idealizing some aspects of the original problem. (For example, we might decide to ignore air resistance or friction.) The middle step in the process consists of finding a mathematical solution to the mathematical problem. The final step is to interpret the mathematical solution in terms of the original problem. The middle step in this process is called “pure mathematics,” and the entire process is called “applied mathematics.”

We have, for example, all been given problems such as: If Johnny has six pennies and steals eight more, how many does he have? We first convert this to the mathematical problem: $6 + 8 = ?$ Then by pure mathematics (addition, in this case) we obtain 14 as the solution. Finally, we decide that Johnny has fourteen pennies.

The mathematical modeling of a Real World problem is not always this straightforward. When we try to interpret our mathematical solution in terms of the original problem, we might discover that it just does not fit. If we start with six blobs of water and add eight more blobs, we may end up with only four or five rather large puddles. This outcome does not shake our faith in arithmetic at all. It does show that we need to revise the model and try again (perhaps by measuring volume instead of counting blobs). From the vast array of mathematical concepts we must select those (if any!) that accurately model the essential feature of the problem to be solved.

![](images/a1d4540d25ae215d8db4da97b6d28c88f810770b208b69d6d7e46972ae64d2ea.jpg)  
Fig. 29. Applied mathematics.

# CARDINAL NUMBERS AND THE AXIOM OF CHOICE

## EQUINUMEROSITY

We want to discuss the size of sets. Given two sets A and B, we want to consider such questions as:

(a) Do $A$ and $B$ have the same size?

(b) Does $A$ have more elements than $B$ ?

Now for finite sets, this is not very complicated. We can just count the elements in the two sets, and compare the resulting numbers. And if one of the sets is finite and the other is infinite, it seems conservative enough to say that the infinite set definitely has more elements than does the finite set.

But now consider the case of two infinite sets. Our first need is for a definition: What exactly should “A has the same size as B” mean when A and B are infinite? After we select a reasonable definition, we can then ask, for example, whether any two infinite sets have the same size. (We have not yet officially defined “finite” or “infinite,” but we will soon be in a position to define these terms in a precise way.)

An Analogy In order to find a solution to the above problem, we can first consider an analogous problem, but one on a very simple level.

![](images/8290e60b5f234bb0a586e7bfc8a02ee89110e3506333454aa1d8d49a860c7565.jpg)  
Fig. 30. Are there exactly as many houses as people?

Imagine that your mathematical education is just beginning—that you are on your way to nursery school. You are apprehensive about going, because you have heard that they have mathematics lessons and you cannot count past three. Sure enough, on the very first day they show you Fig. 30 and ask, “Are there exactly as many houses as people?” Your heart sinks. There are too many houses and too many people for you to count. This is just the predicament described earlier, where we had sets A and B that, being infinite, had too many elements to count.

But wait! All is not lost. You take your crayon and start pairing people with houses (Fig. 31). You soon discover that there are indeed exactly as many houses as people. And you did not have to count past three. You get a gold star and go home happy. We adopt the same solution.

![](images/ba03419f3974fa30eb6590e86ffbbba3f6d6bfc086d60104fb9876b53c0ed00c.jpg)  
Fig. 31. How to answer the question without counting.

Definition A set $A$ is equinumerous to a set $B$ (written $A \approx B$ ) iff there is a one-to-one function from $A$ onto $B$ .

A one-to-one function from A onto B is called a one-to-one correspondence between A and B. For example, in Fig. 30 the set of houses is equinumerous to the set of people. A one-to-one correspondence between the sets is exhibited in Fig. 31.

Example The set $\omega \times \omega$ is equinumerous to $\omega$ . There is a function $J$ mapping $\omega \times \omega$ one-to-one onto $\omega$ , shown in Fig. 32, where the value of

![](images/9539022116f954123855036d5ab0ced91c9eeaad261beba6938cc6035010b6d9.jpg)  
Fig. 32. $\omega \times \omega \approx \omega$ .

$J(m, n)$ is written at the point with coordinates $\langle m, n \rangle$ . In fact we can give a polynomial expression for $J$ :

$$
J (m, n) = \frac {1}{2} [ (m + n) ^ {2} + 3 m + n ],
$$

as you are asked to verify in Exercise 2.

Example The set of natural numbers is equinumerous to the set $\mathbb{Q}$ of rational numbers, i.e., $\omega \approx \mathbb{Q}$ . The method to be used here is like the one used in the preceding example. We arrange $\mathbb{Q}$ in an orderly pattern, then thread a path through the pattern, pairing natural numbers with the rationals as we go. The pattern is shown in Fig. 33. We define $f: \omega \to \mathbb{Q}$ , where $f(n)$ is the rational next to the bracketed numeral for $n$ in Fig. 33. To ensure that $f$ is one-to-one, we skip rationals met for the second (or third or later) time. Thus $f(4) = -1$ , and we skip $-2/2$ , $-3/3$ , and so forth.

![](images/f192f95b04cfc50b8cbf28706d1a01a03bf05b503dc1e6bf6b80e301c637981a.jpg)

$$
\text { Fig.   33. } \omega \approx \mathbb {Q}.
$$

Example The open unit interval

$$
(0, 1) = \{x \in \mathbb {R} \mid 0 <   x <   1 \}
$$

is equinumerous to the set $\mathbb{R}$ of all real numbers. A geometric construction of a one-to-one correspondence is shown in Fig. 34. Here $(0, 1)$ has been bent into a semicircle with center P. Each point in $(0, 1)$ is paired with its projection (from P) on the real line.

There is also an analytical proof that $(0, 1) \approx \mathbb{R}$ . Let $f(x) = \tan \pi(2x - 1)/2$ . Then $f$ maps $(0, 1)$ one-to-one (and continuously) onto $\mathbb{R}$ .

As the above example shows, it is quite possible for an infinite set, such as R, to be equinumerous to a proper subset of itself, such as $(0, 1)$ . (For finite sets this never happens, as we will prove shortly.) Galileo remarked in 1638 that $\omega$ was equinumerous to the set $\{0, 1, 4, 9, \ldots\}$ of squares of natural numbers, and found this to be a curious fact. The

![](images/63864caa71a712e2cf4b2159a9e79e144c45b77323d54609f5d06ef87c4ecd14.jpg)

squares are in some sense a small part of the natural numbers, e.g., the fraction of the natural numbers less than n that are squares converges to 0 as n tends to infinity. But when viewed simply as two abstract sets, the set of natural numbers and the set of squares have the same size. Similarly the set of even integers is equinumerous to the set of all integers. If we focus attention on the way in which even integers are placed among the others, then we are tempted to say that there are only half as many even integers as there are integers altogether. But if we instead view the two sets as two different abstract sets, then they have the same size.

Example For any set A, we have $PA \approx ^{A}2$ . To prove this, we define a one-to-one function H from PA onto $^{A}2$ as follows: For any subset B of A, $H(B)$ is the characteristic function of B, i.e., the function $f_{B}$ from A into 2 for which

$$
f _ {B} (x) = \left\{ \begin{array}{l l} 1 & \text { if } \quad x \in B, \\ 0 & \text { if } \quad x \in A - B. \end{array} \right.
$$

Then any function $g \in {}^A 2$ is in ran $H$ , since

$$
g = H (\{x \in A \mid g (x) = 1 \}).
$$

The following theorem shows that equinumerosity has the property of being reflexive (on the class of all sets), symmetric, and transitive. But it cannot be represented by an equivalence relation, because it concerns all sets. In von Neumann–Bernays set theory, one can form the class

$$
\mathbf {E} = \{\langle A, B \rangle | A \approx B \}.
$$

Then E is an “equivalence relation on V,” in the sense that it is a class of ordered pairs that is reflexive on V, symmetric, and transitive. But E is not a set, lest its field V be a set. In Zermelo–Fraenkel set theory, we have only the “equivalence concept” of equinumerosity.

Theorem 6A For any sets $A, B$ , and $C$ :

(a) $A \approx A.$

(b) If $A \approx B$ , then $B \approx A$ .

(c) If $A \approx B$ and $B \approx C$ , then $A \approx C$ .

Proof See Exercise 5.

In light of the examples presented up to now, you might well ask whether any two infinite sets are equinumerous. Such is not the case; some infinite sets are much larger than others.

Theorem 6B (Cantor 1873) (a) The set $\omega$ is not equinumerous to the set $\mathbb{R}$ of real numbers.

(b) No set is equinumerous to its power set.

Proof We will show that for any function $f: \omega \to R$ , there is a real number z not belonging to ran f. Imagine a list of the successive values of f, expressed as infinite decimals:

$$
\begin{array}{c} f (0) = 2 3 6. 0 0 1 \dots , \\ f (1) = - 7. 7 7 7 \dots , \\ f (2) = \quad 3. 1 4 1 5 \dots , \\ \vdots \end{array}
$$

(In Chapter 5 we did not go into the matter of decimal expansions, but you are surely familiar with them.) We will proceed to construct the real z. The integer part is 0, and the $(n+1)$ st decimal place of z is 7 unless the $(n+1)$ st decimal place of $f(n)$ is 7, in which case the $(n+1)$ st decimal place of z is 6. For example, in the case shown,

$$
z = 0. 7 6 7 \dots
$$

Then $z$ is a real number not in $\operatorname{ran} f$ , as it differs from $f(n)$ in the $(n + 1)$ st decimal place.

The proof of (b) is similar. Let $g: A \to \mathcal{P}A$ ; we will construct a subset $B$ of $A$ that is not in ran $g$ . Specifically, let

$$
B = \{x \in A \mid x \notin g (x) \}.
$$

Then $B \subseteq A$ , but for each $x \in A$ ,

$$
x \in B \Leftrightarrow x \notin g (x).
$$

Hence $B \neq g(x)$ .

The set R happens to be equinumerous to $P\omega$ , as we will soon be able to prove. A larger set is PR, and PPR is larger still.

Before continuing our consideration of infinite sets, we will study the other alternative: the sets that are “small” at least to the extent of being finite.

## Exercises

1. Show that the equation

$$
f (m, n) = 2 ^ {m} (2 n + 1) - 1
$$

defines a one-to-one correspondence between $\omega \times \omega$ and $\omega$ .

2. Show that in Fig. 32 we have:

$$
\begin{array}{r l} J (m, n) & = [ 1 + 2 + \dots + (m + n) ] + m \\ & = \frac {1}{2} [ (m + n) ^ {2} + 3 m + n ]. \end{array}
$$

3. Find a one-to-one correspondence between the open unit interval $(0, 1)$ and R that takes rationals to rationals and irrationals to irrationals.

4. Construct a one-to-one correspondence between the closed unit interval

$$
[ 0, 1 ] = \{x \in \mathbb {R} \mid 0 \leq x \leq 1 \}
$$

and the open unit interval (0, 1).

5. Prove Theorem 6A.

## FINITE SETS

Although we have long been using the words “finite” and “infinite” in an informal way, we have not yet given them precise definitions. Now is the time.

Definition A set is finite iff it is equinumerous to some natural number. Otherwise it is infinite.

Here we rely on the fact that in our construction of $\omega$ , each natural number is the set of all smaller natural numbers. For example, any natural number is itself a finite set.

We want to check that each finite set S is equinumerous to a unique number n. The number n can then be used as a count of the elements in S.

We first need the following theorem, which implies that if n objects are placed into fewer than n pigeonholes, then some pigeonhole receives more than one object. Recall that a set A is a proper subset of B iff $A \subseteq B$ and $A \neq B$ .

Pigeonhole Principle No natural number is equinumerous to a proper subset of itself.

Proof Assume that f is a one-to-one function from the set n into the set n. We will show that ran f is all of the set n (and not a proper subset of n). This suffices to prove the theorem.

![](images/c1561cd49664d508e1d16b0c82fb2ee057302fcea047fba2b47a927a0a4cc1da.jpg)  
Fig. 35. In $f$ we interchange two values to obtain $\hat{f}$ .

We use induction on n. Define:

$T = \{n\in \omega |$ any one-to-one function from $n$ into $n$ has range $n\}$ .

Then $0 \in T$ ; the only function from the set 0 into the set 0 is $\varnothing$ and its range is the set 0. Suppose that $k \in T$ and that $f$ is a one-to-one function from the set $k^{+}$ into the set $k^{+}$ . We must show that the range of $f$ is all of the set $k^{+}$ ; this will imply that $k^{+} \in T$ . Note that the restriction $f \upharpoonright k$ of $f$ to the set $k$ maps the set $k$ one-to-one into the set $k^{+}$ .

Case I Possibly the set k is closed under f. Then $f \upharpoonright k$ maps the set k into the set k. Then because $k \in T$ we may conclude that ran $(f \upharpoonright k)$ is all of the set k. Since f is one-to-one, the only possible value for $f(k)$ is the number k. Hence ran f is $k \cup \{k\}$ , which is the set $k^{+}$ .

Case II Otherwise $f(p) = k$ for some number p less than k. In this case we interchange two values of the function. Define $\hat{f}$ by

$$
\hat {f} (p) = f (k),
$$

$$
\hat {f} (k) = f (p) = k,
$$

$$
\hat {f} (x) = f (x) \quad \text {   for   other   } x \in k ^ {+}
$$

(see Fig. 35). Then $\hat{f}$ maps the set $k^{+}$ one-to-one into the set $k^{+}$ , and the set $k$ is closed under $\hat{f}$ . So by Case I, ran $\hat{f} = k^{+}$ . But ran $\hat{f} = \operatorname{ran} f$ . Thus in either case, ran $f = k^{+}$ . So $T$ is inductive and equals $\omega$ .

Corollary 6C No finite set is equinumerous to a proper subset of itself.

Proof This is the same as the pigeonhole principle, but for an arbitrary finite set A instead of a natural number. Since A is equinumerous to a natural number n, we can use the one-to-one correspondence g between A and n to “transfer” the pigeonhole principle to the set A.

Suppose that, contrary to our hopes, there is a one-to-one correspondence $f$ between $A$ and some proper subset of $A$ . Consider the composition $g \circ f \circ g^{-1}$ , illustrated in Fig. 36. This composition maps $n$ into $n$ , and it is one-to-one by Exercise 17 of Chapter 3. Furthermore its range $C$ is a proper subset of $n$ . (Consider any $a$ in $A - \operatorname{ran} f$ ; then $g(a) \in n - C$ .) Thus $n$ is equinumerous to $C$ , in contradiction to the pigeonhole principle.

The foregoing proof uses an argument that is useful elsewhere as well. We have sets A and n that are “alike” in that $A \approx n$ , but different in that they have different members. Think of the members of A as being red, the members of n as being blue. Then the function $g: A \to n$ paints red things blue, and the function $g^{-1}: n \to A$ paints blue things red. The composition $g \circ f \circ g^{-1}$ paints things red, applies f, and then restores the blue color.

![](images/ead8d6132aa17205aa4a605549e1d61bc306399b1537bfa7ee568bb535b60537.jpg)  
Fig. 36. What $f$ does to $A, g \circ f \circ g^{-1}$ does to $n$ .

Corollary 6D (a) Any set equinumerous to a proper subset of itself is infinite.

(b) The set $\omega$ is infinite.

Proof The preceding corollary proves part (a). Part (b) follows at once from part (a), since the function $\sigma$ whose value at each number $n$ is $n^{+}$ maps $\omega$ one-to-one onto $\omega - \{0\}$ .

Corollary 6E Any finite set is equinumerous to a unique natural number.

Proof Assume that $A \approx m$ and $A \approx n$ for natural numbers $m$ and $n$ . Then $m \approx n$ . By trichotomy and Corollary 4M, either $m = n$ or one is a proper subset of the other. But the latter alternative is impossible since $m \approx n$ . Hence $m = n$ .

For a finite set A, the unique $n \in \omega$ such that $A \approx n$ is called the cardinal number of A, abbreviated card A. For example, card n = n for $n \in \omega$ . And if a, b, c, and d are all distinct objects, then card $\{a, b, c, d\} = 4$ . This is because $\{a, b, c, d\} \approx 4$ ; selecting a one-to-one correspondence is the process called “counting.” Observe that for any finite sets A and B, we have $A \approx$ card A and

$$
\operatorname{card} A = \operatorname{card} B \quad \text { iff } \quad A \approx B.
$$

What about infinite sets? The number card A measures the size of a finite set A. We want “numbers” that similarly measure the size of infinite sets. Just what sets these “numbers” are is not too crucial, any more than it was crucial just what set the number 2 was. The essential demand is that we define card A for arbitrary A in such a way that

$$
\operatorname{card} A = \operatorname{card} B \quad \text { iff } \quad A \approx B.
$$

Now it turns out that there is no way of defining card A that is really simple. We therefore postpone until Chapter 7 the actual definition of the set card A. The information we need for the present chapter is embodied in the following promise.

Promise For any set A we will define a set card A in such a way that:

(a) For any sets $A$ and $B$ ,

$$
\operatorname{card} A = \operatorname{card} B \quad \text { iff } \quad A \approx B.
$$

(b) For a finite set $A$ , card $A$ is the natural number $n$ for which $A \approx n$ .

(In making good on this promise, we will use in Chapter 7 additional axioms, namely the replacement axioms and the axiom of choice. If you plan to omit Chapter 7, then regard card A as an additional primitive notion and the promise as an additional axiom.)

We define a cardinal number to be something that is card A for some set A. By part (b) of the promise, any natural number n is also a cardinal number, since n = card n. But card $\omega$ is not a natural number (card $\omega \neq n = card n$ , since $\omega$ is not equinumerous to n). Just what set card $\omega$ is will not be revealed until Chapter 7. Meanwhile we give it the name that Cantor gave it:

$$
\operatorname{card} \omega = \aleph_ {0}.
$$

The symbol $\aleph$ is aleph, the first letter of the Hebrew alphabet.

In general, for a cardinal number $\kappa$ , there will be a great many sets A of cardinality $\kappa$ , i.e., sets with card $A = \kappa$ . (The one exception to this occurs when $\kappa = 0$ .) In fact, for any nonzero cardinal $\kappa$ , the class

$$
\mathsf {K} _ {\kappa} = \{X \mid \text { card } X = \kappa \}
$$

of sets of cardinality $\kappa$ is too large to be a set (Exercise 6). But all of the sets of cardinality $\kappa$ look, from a great distance, very much alike—the elements of two such sets may differ but the number of elements is always $\kappa$ . In particular, if one set $X$ of cardinality $\kappa$ is finite, then all of them are; in this case $\kappa$ is a finite cardinal. And if not, then $\kappa$ is an infinite cardinal. Thus the finite cardinals are exactly the natural numbers. $\aleph_0$ is an infinite cardinal, as are card $\mathbb{R}$ , card $\mathcal{P}\omega$ , card $\mathcal{PP}\omega$ , etc.

Before leaving this section on finite sets, we will verify a fact that, on an informal level, appears inevitable: Any subset of a finite set is finite. (Later we will find another proof of this.)

Lemma 6F If $C$ is a proper subset of a natural number $n$ , then $C \approx m$ for some $m$ less than $n$ .

Proof We use induction. Let

$T = \{n\in \omega |$ any proper subset of $n$ is equinumerous to a member of $n\}$ .

Then $0 \in T$ vacuously, 0 having no proper subsets. Assume that $k \in T$ and consider a proper subset $C$ of $k^{+}$ .

$$
\text { Case   } I \quad C = k. \quad \text { Then   } C \approx k \in k ^ {+}.
$$

Case II $C$ is a proper subset of $k$ . Then since $k \in T$ , we have $C \approx m$ for $m \in k \in k^{+}$ .

Case III Otherwise $k \in C$ . Then $C = (C \cap k) \cup \{k\}$ and $C \cap k$ is a proper subset of k. Because $k \in T$ , there is $m \in k$ with $C \cap k \approx m$ . Say f is a one-to-one correspondence between $C \cap k$ and m; then $f \cup \{\langle k, m \rangle\}$ is a one-to-one correspondence between C and $m^{+}$ . Since $m \in k$ , we have $m^{+} \in k^{+}$ . Hence $C \approx m^{+} \in k^{+}$ and $k^{+} \in T$ .

Thus T is inductive and coincides with $\omega$ .

Corollary 6G Any subset of a finite set is finite.

Proof Consider $A \subseteq B$ and let $f$ be a one-to-one correspondence between $B$ and some $n$ in $\omega$ . Then $A \approx f[[A]] \subseteq n$ and by the lemma $f[[A]] \approx m$ for some $m \in n$ . Hence $A \approx m \in n \in \omega$ .

## Exercises

6. Let $\kappa$ be a nonzero cardinal number. Show that there does not exist a set to which every set of cardinality $\kappa$ belongs.

7. Assume that $A$ is finite and $f: A \to A$ . Show that $f$ is one-to-one iff $\operatorname{ran} f = A$ .

8. Prove that the union of two finite sets is finite (Corollary 6K), without any use of arithmetic.

9. Prove that the Cartesian product of two finite sets is finite (Corollary 6K), without any use of arithmetic.

## CARDINAL ARITHMETIC

The operations of addition, multiplication, and exponentiation are well known to be useful for finite cardinals. The operations can be useful for arbitrary cardinals as well. To extend the concept of addition from the finite to the infinite case, we need a characterization of addition that is correct in the finite case, and is meaningful (and plausible) in the infinite case. In Chapter 4 we obtained addition on $\omega$ by use of the recursion theorem. That approach is unsuitable here, so we seek another approach.

The answer to our search lies in the way addition is actually explained in the elementary schools. First-graders are not told about the recursion theorem. Instead, if they want to add 2 and 3, they select two sets K and L with card K = 2 and card L = 3. Sets of fingers are handy; sets of apples are preferred by textbooks. Then they look at card(K ∪ L). If they had the good sense to select K and L to be disjoint, then card(K ∪ L) = 5.

The same idea is embodied in the following definition of addition. In the same vein, we can include multiplication and exponentiation.

Definition Let $\kappa$ and $\lambda$ be any cardinal numbers.

(a) $\kappa + \lambda = \operatorname{card}(K \cup L)$ , where $K$ and $L$ are any disjoint sets of cardinality $\kappa$ and $\lambda$ , respectively.

(b) $\kappa \cdot \lambda = \operatorname{card}(K \times L)$ , where $K$ and $L$ are any sets of cardinality $\kappa$ and $\lambda$ , respectively.

(c) $\kappa^{\lambda} = \operatorname{card}^{L} K$ , where $K$ and $L$ are any sets of cardinality $\kappa$ and $\lambda$ , respectively.

In every case it is necessary to prove that the operation is well defined; that is, that the outcome is independent of the particular sets K and L selected to represent the cardinals. Also for the case of finite cardinals, we should check that the above definitions are not in open conflict with operations on $\omega$ defined in Chapter 4.

First consider addition. To add two cardinals $\kappa$ and $\lambda$ , the definition demands that we first select disjoint sets K and L with card $K = \kappa$ and card $L = \lambda$ . This is possible; if our first choices for K and L fail to be disjoint, we can switch to $K \times \{0\}$ and $L \times \{1\}$ . For then, since

$$
K \approx K \times \{0 \} \quad \text { and } \quad L \approx L \times \{1 \},
$$

we have $\operatorname{card}(K \times \{0\}) = \kappa$ and $\operatorname{card}(L \times \{1\}) = \lambda$ . And the sets $K \times \{0\}$ and $L \times \{1\}$ are disjoint.

Having selected disjoint representatives K and L for $\kappa$ and $\lambda$ , we form their union $K \cup L$ . Then by definition

$$
\kappa + \lambda = \operatorname{card} (K \cup L).
$$

We must verify that this sum is independent of the particular disjoint sets $K$ and $L$ selected. This verification is accomplished by part (a) of the following theorem. For suppose $K_{1}, L_{1}$ and $K_{2}, L_{2}$ are two selections of disjoint sets of cardinality $\kappa, \lambda$ . Since card $K_{1} = \text{card } K_{2} = \kappa$ , we have $K_{1} \approx K_{2}$ ; similarly $L_{1} \approx L_{2}$ . The following theorem then yields $K_{1} \cup L_{1} \approx K_{2} \cup L_{2}$ , whence

$$
\operatorname{card} \left(K _ {1} \cup L _ {1}\right) = \operatorname{card} \left(K _ {2} \cup L _ {2}\right).
$$

Thus we have an unambiguous sum $\kappa + \lambda$ . Parts (b) and (c) of the theorem perform the same service for multiplication and exponentiation.

Theorem 6H Assume that $K_{1} \approx K_{2}$ and $L_{1} \approx L_{2}$ .

(a) If $K_{1} \cap L_{1} = K_{2} \cap L_{2} = \emptyset$ , then $K_{1} \cup L_{1} \approx K_{2} \cup L_{2}$ .

(b) $K_{1} \times L_{1} \approx K_{2} \times L_{2}$ .

(c) $(L_1)\bar{K}_1\approx (L_2)\bar{K}_2$

Proof Since $K_{1} \approx K_{2}$ , there is a one-to-one function f from $K_{1}$ onto $K_{2}$ ; since $L_{1} \approx L_{2}$ , there is a one-to-one function g from $L_{1}$ onto $L_{2}$ . Then for (a), the function h, defined by

$$
h (x) = \left\{ \begin{array}{l l} f (x) & \text { if } \quad x \in K _ {1}, \\ g (x) & \text { if } \quad x \in L _ {1}, \end{array} \right.
$$

maps $K_{1} \cup L_{1}$ one-to-one onto $K_{2} \cup L_{2}$ . (We need $K_{1} \cap L_{1} = \emptyset$ to be sure $h$ is a function; we need $K_{2} \cap L_{2} = \emptyset$ to be sure it is one-to-one.)

For (b), the function $h$ , defined by

$$
h (\langle x, y \rangle) = \langle f (x), g (y) \rangle
$$

(for $x \in K_1$ and $y \in L_1$ ), maps $K_1 \times L_1$ one-to-one onto $K_2 \times L_2$ .

![](images/8f7fbc570e9ed19de2b5a9b1bb6bd708856e952f4c312072d0a9e7aa944dca92.jpg)  
Fig. 37. $H(j) = f \circ j \circ g^{-1}$ .

Finally for (c), the function $H$ , defined by

$$
H (j) = f \circ j \circ g ^ {- 1},
$$

maps $(L_1)K_1$ one-to-one onto $(L_2)K_2$ (see Fig. 37). For clearly $H(j)$ is a function from $L_2$ to $K_2$ . To see that $H$ is one-to-one, suppose that $j$ and $j'$ are different functions from $L_1$ into $K_1$ . Then $j(t) \neq j'(t)$ for some $t \in L_1$ . Then compute $H(j)$ and $H(j')$ at $g(t)$ :

$$
H (j) (g (t)) = f (j (t)) \neq f (j ^ {\prime} (t)) = H (j ^ {\prime}) (g (t))
$$

since $f$ is one-to-one. Hence the function $H(j)$ is different from the function $H(j')$ , i.e., $H$ is one-to-one. And to see that ran $H$ is all of $^{(L_2)}K_2$ , consider any function $d$ from $L_2$ into $K_2$ . Then $d = H(j)$ , where $j = f^{-1} \circ d \circ g$ .

Remark The proof of part (c) is our first proof dealing with cardinal exponentiation. Observe that it involves constructing a function H whose arguments and values are themselves functions. In such cases it is imperative to use a rationally chosen notation, e.g., an uppercase letter for H and lowercase letters for the arguments of H, as in the expression “ $H(j)$ .” Here