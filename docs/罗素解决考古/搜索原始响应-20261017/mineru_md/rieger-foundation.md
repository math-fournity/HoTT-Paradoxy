Rieger, A. Paradox, ZF, and the axiom of foundation. In Clark, P. and Hallett, M. and DeVidi, D. (Eds) Vintage Enthusiasms: Essays in Honour of J. L. Bell. (2008).

http://eprints.gla.ac.uk/3810/

Deposited on: 8 November 2007

# Paradox, ZF, and the Axiom of Foundation<sup>∗</sup>

Adam Rieger

It is a great pleasure to contribute to this Festschrift for John Bell. No-one has done more than he has to demonstrate the fruitfulness of the interplay between technical mathematics and philosophical issues, and he is an inspiration to all of us who work somewhere in the borderland between mathematics and philosophy.

I also owe him a great personal debt. I arrived at the LSE dejected and disillusioned by my experiences of the Mathematical Tripos at Cambridge, but it is impossible to be downhearted for long in the company of John. His enthusiasm, humour and warmth were the perfect antidote to the stufiness and inhumanity of Cambridge and helped hugely to rebuild my interest and self-confidence. John’s energy levels must be seen to be believed, and an evening with him is an unforgettable experience. It generally starts about 4 p.m. and ends around 5 in the morning, when the last of his companions (never John, who always gives the impression that he could go on talking indefinitely) finally succumbs to sleep.

At John’s suggestion, I wrote my M.Sc. dissertation at the L.S.E. on truth, which led on eventually to an Oxford D.Phil. which concerned both the semantic and set-theoretical paradoxes. It is the concept of set—example par excellence of one that straddles philosophy and mathematics—that is the subject of this essay.

## 1

At the beginning of the twentieth century there was a crisis in the foundations of mathematics. The crisis centred around the concept of set, which suddenly achieved prominence in two diferent ways. Firstly Cantor’s theory of the transfinite showed that sets were of great intrinsic mathematical interest. And secondly through the work of Frege and Russell it emerged that sets were central to the philosophical project—logicism—of reducing mathematics to logic.

The discovery by Russell and others that, if handled carelessly, sets give rise to contradictions, threatened not only the logicist programme, but also mathematics itself; for large parts of mathematics, in particular analysis, make essential use of the completed infinite, and the paradoxes seemed to show that this was a risky practice.

A hundred years later there is no longer a foundational crisis. Why is this? By 1930, mathematicians had found a way of coping with the paradoxes. A system of axiomatic set theory, Zermelo-Fraenkel set theory (ZF for short) had been developed, which allowed mathematicians to do all they wanted to do with sets, whilst maintaining consistency. ZF is not the only axiomatic set theory, but at the present time it has a completely dominant position amongst such theories. For the purposes of university mathematics courses, for example, set theory just is ZF.

Does ZF really deserve its elevated position? Below I examine three sorts of argument which can be adduced in support of ZF:

1. Argument from the paradoxes

2. Argument from the iterative conception

3. Argument from pragmatic mathematical considerations

and conclude that none of them are convincing.

## 2

There is a widespread view that one needs some kind of hierarchy, and hence ZF or something like it, to avoid the paradoxes.<sup>1</sup> Let us go back to basics to examine the merits of this claim.

According to the naive conception of set, any arbitrary collection forms a set.<sup>2</sup> This entails the truth of the naive comprehension schema

$$
\exists x \forall y (y \in x \leftrightarrow \phi (y)).
$$

But this schema is in fact logically false: for as Russell noticed [1902], on letting $\phi$ be $y \not \in y$ we obtain a contradiction.

Now whilst this shows that there is a fatal defect with the naive conception, it does not yield an illuminating explanation of what exactly is wrong with it, an explanation that might be of some use in the reform of the concept of set which must inevitably follow.

Such an explanation is, however, available.

Suppose a is a set, and consider the set

$$
b = \{x \in a: x \not \in x \}.
$$

It is easy to see that $b \not \in a .$ . So we have a recipe which, for any set $^ { a , }$ gives us a set which is not a member of $a .$ . The set $b$ “diagonalizes $\mathrm { o u t } ^ { \dag }$ of $a .$

If a already has all sets as members, trouble arrives in the shape of the Russell paradox. And naively, there must be such a set $^ { a , }$ for example the set of everything whatever. (Just take $\phi ( y )$ to be $y = y$ in the naive schema above.) On this way of looking at it, contradiction arises because, under the naive conception, we have both extensibility (the ability to extend any given set by finding something that is not one of its members) and universality (the existence of a set which contains everything). Clearly these cannot co-exist consistently.

Essentially the same diagnosis can be given for the other standard settheoretic paradoxes. In the so-called Cantor paradox, extensibility arises from the power set operation—since the power set $P ( a )$ of a is always strictly larger than a, there must be elements of $P ( a )$ which are not in a. So again the existence of a universal set leads to contradiction.

In some of the paradoxes the extensibility and universality are relativised to particular sub-collections of the universe. For example, the Burali-Forti paradox hinges on the tension between (i) the principle that, for any initial segment of ordinals, we can, by considering the ordinal number of the segment itself, find an ordinal not in that segment, and (ii) the principle that there is a well-ordered set of $a l l$ ordinals. The slightly less well-known Mirimanof paradox concerns the set W of all well-founded sets.<sup>3</sup> Since all the members of $W$ are well-founded, so is W, but then it should be a member of itself, and so, after all, not well-founded. Here extensibility is obtained by considering, for any set a of well-founded sets, the set $b = a \cup \{ a \}$ ; this is another set of well-founded sets (since a itself must be well-founded), yet it has a member (namely a itself) which is not a member of a (else we have $a \in a .$ , so a is not well-founded).<sup>4</sup>

A consequence of this diagnosis is that there is a neat and rather natural way to solve the paradoxes: ban universality by not allowing very large collections (e.g. the universe and the collection of all ordinals) to be sets. Remarkably, this solution was hit upon by the originator of set theory, Georg Cantor, before the “paradox industry” had even got under way. In a letter he wrote to Dedekind [1899] we find the following passage:

. . . it is necessary, as I discovered, to distinguish two kinds of multiplicity. . . For a multiplicity can be such that the assumption that all of its elements “are together” leads to a contradiction, so that it is impossible to conceive of the multiplicity as a unity, as “one finished thing”. Such multiplicities I call absolutely infinite or inconsistent multiplicities . . . If on the other hand the totality of the elements of a multiplicity can be thought of without contradiction as “being together”. . . I call it a consistent multiplicity or set.<sup>5</sup>

Cantor has discovered what in modern parlance is called the set/class distinction, usually attributed to von Neumann [1925]. The key idea is that some infinite collections are all right, and they form the sets; others are just too big, and are either abolished altogether, or allowed in as some other kind of entity (proper classes).<sup>6</sup> The idea is, in the light of our diagnosis, thoroughly motivated and not at all ad hoc.

And, indeed, this is exactly what happens with ZF. This is sometimes expressed, somewhat misleadingly, by saying that ZF incorporates the doctrine of limitation of size—misleading because this phrase suggests that there is some cardinal magnitude below which collections are safe but above which they are paradoxical, whereas the point is not that sets must be below some particular size but that they must not be as big as the universe.

Nothing we have said so far, however, requires sets to be arranged in a hierarchy. But the ZF axioms embody such a requirement. In particular, the axiom of foundation states that every (non-empty) set x has a member y which is minimal, in the sense that no member of x belongs to y.<sup>7</sup> Another way of putting this, equivalent in the presence of the axiom of choice, is that there is no infinite descending membership chain $x \ni x _ { 1 } \ni x _ { 2 } \ni . ~ . . .$ So there cannot be, for example, a set which is a member of itself, or a member of a member of itself.

A suspicion therefore arises that ZF restricts the notion of set more than is necessary to avoid the paradoxes, and therefore ofends against the following methodological principle: when forced by paradox to reform a naive concept, preserve as much of it as possible. The naive concept of set does not obey the axiom of foundation: it allows such self-membered sets as the set of absolutely everything, and the set of all things discussed in this paper. ZF rules out both of these, but the principle of restricting universality seems to deny sethood only to the first.<sup>8</sup> Can there be a consistent theory which allows the second?

Indeed there can. One sort of theory with this property is discussed by Aczel [1988]. Briefly, the idea is to take the axioms of ZF except foundation, and add to them some version of an anti-foundation axiom. This is best understood in terms of membership graphs. There is a natural sense in which (directed) graphs can be regarded as pictures of sets: for example, Figure 1 is a picture of the von Neumann ordinal 2 = {∅, {∅}}.

Only well-founded graphs (graphs without infinite paths) can be pictures of sets in the ZF universe; to obtain the richer non-well-founded universes we allow any graph to be a picture of a set. Thus Figure 2 is the picture of a set $a = \{ a , \emptyset \}$

By constructing a graph model from a model of ZF, Aczel proves that these systems are consistent if ZF is.<sup>9</sup>

Summary: it can be rigorously proved that ZF restricts the notion of set more than the paradoxes demand.

Figure 1: An exact picture of 2  
![](images/293bd06a97e3953582ffb0035ad5b05b38f78a217badccb82af514d3b9bc469c.jpg)

Figure 2: A non-well-founded graph  
![](images/b1c61fa7fa05374d23ab83c0bdcc7535c1239c634f74d1cb7e7a2129a9e997c6.jpg)

How did the idea take hold that a hierarchy is necessary to solve the paradoxes? To answer this it will be necessary to take a short historical detour.

In December 1905 Russell read a remarkable paper to the London Mathematical Society, later published as Russell [1906c]. In it he states clearly that the lesson of the paradoxes is that naive comprehension must be rejected:

What is demonstrated by the contradictions we have considered is broadly this: ‘A propositional function of one variable does not always determine a class.’ (Russell [1906c] pp. 144–5)

And he gives essentially the diagnosis above:

. . . there are what we may call self-reproductive processes and classes. That is, there are some properties such that, given any class of terms<sup>10</sup> all having such a property, we can always define a new term also having the property in question. Hence we can never collect all the terms having the said property into a whole; because, whenever we hope we have them all, the collection which we have immediately proceeds to generate a new term also having the said property. (Russell [1906c] p. 144)

This insight would seem to lead naturally to the conclusion outlined above, that a solution to the paradoxes may be obtained by ensuring that there is no universal class, no class of all ordinals, etc. However, Russell does not simply draw this inference; rather he considers three diferent responses, all of which would indirectly ban the ofending classes: the “zigzag” theory, the “limitation of size” theory, and the “no-classes” theory, tentatively suggesting that the last of these ofers the most promising route for a solution.<sup>11</sup>

Less than a year later, Russell had changed his mind about the paradoxes. In a paper published in September 1906, he wrote this:

I recognise, however, that the clue to the paradoxes is to be found in the vicious-circle suggestion. (Russell [1906b] p. 198)

The “vicious-circle suggestion” is . . . that whatever in any way concerns all o[r]<sup>12</sup> any or some (undetermined) of the members of a class must not itself be one of the members of a class.<sup>13</sup> (Russell [1906b] p. 198)

A new concept, circularity, has now entered the discussion. Russell believes that all the paradoxes result from the (allegedly) circular practice of allowing totalities containing members which, in some appropriate sense to be discussed below, “concern” that very totality.

It might perhaps seem at first sight that this is just another way of stating the original diagnosis. For is not this circularity the key feature of the “selfreproductive” classes identified in the earlier paper? But in fact the diference is dramatic. According to the previous diagnosis, there cannot be a class of all ordinals or all things (for this would lead to the contradictory consequence that there is a new ordinal (thing) which both must and must not be in the class). But in the later paper, Russell advocates the very much stronger principle that there can be no class whatever, large or small, which has members concerning that very class. This inevitably imposes a hierarchical structure on the universe of classes. At this point an alien constructivism was imported into classical mathematics, vestiges of which are still visible today. For the vicious circle principle is inextricably linked with a constructivist view of the metaphysics of mathematics.<sup>14</sup>

## 5

What had happened to Russell in the few months between the two papers? He had been reading Poincar´e. The second paper was, in fact, written in reply to Poincar´e [1905-6]. In that work Poincar´e blames the paradoxes on circularity. His treatment is sketchy, and he discusses only Richard’s paradox<sup>15</sup> in any detail, claiming that “the same explanation serves for the other antinomies, as may be easily verified” (p. 190). Thus applied to classes,

. . . the definitions that must be regarded as non-predicative are those which contain a vicious circle.<sup>16</sup> (p. 190)

Though he does not explicitly formulate the VCP, it is clear from a later passage in the paper that he has the same conception of it as Russell:

. . . if the definition of a notion N depends on all the objects A, it may be tainted with the vicious circle, if among the objects A there is one that cannot be defined without bringing in the notion N itself. (p. 194)

Now Poincar´e’s views on the VCP arise completely naturally from his wider views on the philosophy of mathematics, in particular, his view on mathematical existence. He is explicit in his constructivism. In a paper written in 1912, he declares that a mathematical object “exists only when it is conceived by the mind” (Poincar´e [1963] p. 72). He considers a “genus” (set) G with a member X, and writes of the members of G

. . . they will exist only after they have been constructed; that is, after they have been defined; X exists only by virtue of its definition,<sup>17</sup> which has meaning only if all the members of G are known beforehand, and X in particular.

This conception of existence of course provides a motivation for the VCP. If mathematical objects are brought into existence by their definitions, then it seems that no totality can possibly contain members defined in terms of that very totality. However, Russell adopted Poincar´e’s views on impredicativity without accepting the constructivist outlook. By doing so he landed the classical mathematical community in a philosophical confusion from which it has yet to emerge.<sup>18</sup>

Armed with his diagnosis of the paradoxes and aided by Whitehead, Russell embarked on reworking mathematics whilst obeying the VCP: the result was the ramified type theory of Principia Mathematica [1910–3]. This is not the place for a detailed discussion of that work, but for present purposes it is enough to note that the system obtained is a (rather complex) hierarchy of propositional functions; the position of a function in the hierarchy depends not only on (i) its arguments but also on (ii) the ranges of any quantifications in its definition (this latter refinement making the hierarchy “ramified”), both (i) and (ii) being required to be lower down in the hierarchy.

But despite Whitehead and Russell’s eforts, their system has never been accepted as a foundation for mathematics. Instead, the system of axiomatic set theory developed in continental Europe, mostly by Zermelo, proved much easier to work with. Most of the axioms appear first in Zermelo’s paper [1908], which contains versions of: extensionality, empty set, pairs, separation, power set, union, choice and infinity, that is, all the axioms in the now-standard theory except for replacement and foundation. Interestingly Zermelo’s motivation at this point seems only partly to have been the paradoxes; primarily he was concerned to analyse exactly which principles concerning sets he had used in his proof that every set can be well-ordered (Zermelo [1904]). The central idea is to replace naive comprehension by separation: that is, we cannot in general form the set of absolutely all y such that $\phi ( y )$ , but only the set of all members of some set a such that $\phi ( y )$ . Paradox is avoided because there is no way to prove that the universe is a set; indeed the Russell paradox becomes a proof that it is not a set.<sup>19</sup>

The replacement axiom was added later by Fraenkel [1922] and Skolem [1922]. As for the axiom of foundation: the issue first seems to have been considered by Mirimanof ([1917a] and [1917b]), who distinguishes “ordinary” sets which do not have infinite descending membership chains from “extraordinary” ones which do. He does not assert, however, that there is anything wrong with the extraordinary sets. Von Neumann [1925] describes non-wellfounded sets as “superfluous” (p. 404) and gives an axiom (p. 412) which excludes some, but not all, of them. Three years later [1928] he formulates the axiom of foundation in the form ∀x $\cdot ( x \neq \varnothing \to \exists y \in x ( y \cap x = \varnothing ) )$ . However, it is not until the paper Zermelo [1930] that the axiom of foundation is explicitly adopted as a postulate. With this paper all the axioms of standard modern set theory are in place.

## 7

In comparing type theory with ZF, it is useful to try to get clearer about what the VCP is saying. Russell never provided a single clear statement of it. Here are two attempts:

I. No totality may contain members defined in terms of itself. (Russell [1908] p. 75)

II. Whatever involves all of a collection must not be one of the collection. (Russell [1908] p. 63)

Now it seems that Russell took these, and other, statements to be diferent formulations of the same principle.<sup>20</sup> However, G¨odel [1944] pointed out that it looks like there is more than one principle here, in particular one to do with definitions, the other to do with the notion of involving.<sup>21</sup> Let us call these VCP I and VCP II, and try to see more precisely what implications they have for sets.

VCP I seems closest to the constructivist spirit of Poincar´e. It rules out impredicative definitions: for example definitions of x which quantify over a collection of which x is a member.<sup>22</sup>

Since sets presumably “involve” their members, VCP II rules out sets which are members of themselves. It also seems reasonable that “involving” is transitive, so that a set also involves the members of its members, and so on. Hence a reasonable explication of “x involves y” in the case of sets is “y is a member of the transitive closure of x”,<sup>23</sup> in which case VCP II will be obeyed if sets satisfy the axiom of foundation.<sup>24</sup>

Now the system of Principia Mathematica obeys both VCP I and VCP II. Impredicative definitions are rigorously avoided, and the universe has a hierarchical structure. That ZF obeys VCP II is, as I have said, guaranteed by the axiom of foundation. But $\mathrm { Z F }$ violates VCP I. The axiom of separation allows us, for any set a, to define a new set b by admitting only those members of a satisfying some formula $\phi ( x )$ . But there is no restriction on the quantifiers that may occur in $\phi ( x )$ : they may range over the whole universe. Impredicative definitions are perfectly allowable in ZF.

## 8

As I recounted above, most of the axioms of ZF resulted from Zermelo’s attempt to defend his proof that every set could be well-ordered. This does not apply, however, to the axiom of foundation. I conjecture that it was inspired by type theory, but I do not know of anything explicit in the early literature which supports this. In any case, somewhat later a new way justifying the axioms developed. This is the second of the three ways I mentioned of arguing in favour of ZF.

The idea is as follows. We all have an intuitive grasp of the concept of natural number, that is, we grasp a structure which we refer to as “the natural numbers”. If someone wanted to justify the Peano axioms for number theory, they would appeal to the evident truth of the axioms in this intuitively understood structure. The claim is that something analogous can be done for set theory. There is an intuitive conception of set, the iterative conception, which gives rise to an intuitively understood model, the cumulative hierarchy. The axioms (or at least, a number of them)<sup>25</sup> are then justified by appealing to the fact that they are true in this model.

How does the model work? Start with the empty set.<sup>26</sup> Call this $V _ { 0 }$ $V _ { 1 }$ is the power set of $V _ { 0 }$ , and in general, we obtain the next level after $V _ { n }$ by taking the power set. $V _ { \omega }$ is just the union of all the $V _ { n }$ for finite $n _ { \mathrm { : } }$ , and $V _ { \omega + 1 }$ is the power set of $V _ { \omega }$ . Continue through the ordinals, forming power sets at each stage and taking unions at limit ordinals. The result is a hierarchy in which sets only have members from lower down the hierarchy. As Lavine [1994] points out, “the iterative conception gives the Axiom of Foundation center stage” (p. 144).

The cumulative hierarchy was hinted at by Mirimanof [1917a] and introduced explicitly by von Neumann [1929] for the purposes of a consistency proof, but the idea of using it as an intuitive model justifying the axioms only came later. It is suggested by G¨odel [1947] (pp. 474–5) but only becomes explicit around 1970, when a number of papers appeared roughly simultaneously. Shoenfield [1967] and [1977], Boolos [1971] and Wang [1974] are representative. Let us examine some of the passages in which they justify that part of their conception of set which gives rise to the axiom of foundation.<sup>27</sup> First Shoenfield:

Sets are formed in stages. For each stage S, there are certain stages which are before S. At each stage S, each collection consisting of sets formed at stages before S is formed into a set. . . . When we are forming a set z by choosing its members, we do not yet have the object z, and hence cannot use it as a member of z. The same reasoning shows that certain other sets cannot be members of z. For example, suppose that z ∈ y. Then we cannot form y until we have formed z. Hence y is not available as an object when z is formed, and therefore cannot be a member of z. (Shoenfield [1977] p. 323)

Boolos actually claims that the iterative conception of set has an intuitive plausibility independent of the paradoxes, and that one might have come to see it as superior to naive set theory (as embodied in the naive comprehension axiom) even if the paradoxes had never been discovered. That is (though this is not the way Boolos expresses it), there are really two versions of naive set theory, one captured by naive comprehension, the other by the iterative conception, and the latter has at least as great an intuitive appeal as the former:

ZF . . . is not only a consistent (apparently) but also an independently motivated theory of sets: there is, so to speak, a “thought behind $\mathrm { i t } ^ { \dag }$ about the nature of sets which might have been put forth even if, impossibly, naive set theory had been consistent. (Boolos [1971] p. 490)

Boolos observes that naive comprehension implies that there is a set of all sets, and that this set is then a member of itself. He continues

It is important to realise how odd the idea of something’s containing itself is. Of course a set can and must include itself (as a subset). But contain itself? Whatever tenuous hold on the concepts of set and member were given one by Cantor’s definitions of “set” and one’s ordinary understanding of “element”, “set”, “collection”, etc. is altogether lost if one is to suppose that some sets are members of themselves. The idea is paradoxical not in the sense that it is contradictory to suppose that some set is a member of itself, for, after all, “(∃x)(Sx & x ∈ x)”<sup>28</sup> is obviously consistent, but that if one understands “∈” as meaning “is a member of”, it is very, very peculiar to suppose it true. For when one is told that a set is a collection into a whole of definite elements of our thought, one thinks: Here are some things. Now we bind them up into a whole (footnote: We put a “lasso” around them, in a figure of Kripke’s.). Now we have a set. We don’t suppose that what we come up with after combining some elements into a whole could have been one of the very things we combined (not, at least, if we are combining two or more elements). (pp. 490–1)

## Wang says simply:

A set is a collection of previously given objects. (Wang [1974] p. 530)

What I want to emphasize here is the constant appeal, in these passages, to constructivist images and terminology. All three authors use temporal words: “before”, “yet”, “until”, “when”, “now”, “previously”. The question is, in what sense are we to take this? Clearly all agree that it is not to be taken literally: there is not actually a time $t _ { 0 }$ at which only the empty set exists, another (later) time by which the singleton of the empty set has been formed, and so on. The constructivist language is supposed only to be metaphorical. Boolos for example, having presented the intuitive idea in constructivist language, then back-pedals: “From the rough description it sounds as if sets were continually being created, which is not the case” (p. 491).

It is clear, then, that the conception of set advanced is not supposed to be literally constructivist, but apparently only constructivist “in principle”, under some liberal interpretation. The trouble is, I shall argue, that the sense has to be so liberal that it is no longer entitled to be called constructivist at all.

Wang admits (p. 531) that there is an element of “idealization” in supposing that we can “run through” an infinite number of objects in the way required in his description of the cumulative hierarchy. But all the authors are silent on what exactly this means. If the talk of “formation”, “collection” and so on are to have any force, there must surely be envisaged an agent who is doing the forming and collecting. What properties do we take this agent to have? Parsons ([1977] p. 507) raises some problems concerning this:

It is hard to see what the conception of an idealized mind is that would fit here: it would difer not only from finite minds but also from the divine mind as conceived in philosophical theology, for the latter is thought of either as in time, and therefore as doing things in an order with the same structure as that in which finite beings operate, or its eternity is interpreted as complete liberation from succession.

To elaborate: if the agent is conceived of as working in ordinary time, there is just not enough of it to generate the whole hierarchy (at least if time consists of continuum-many instants). The agent needs to occupy a “super-time” with perhaps a class of instants isomorphic to the ordinals. On the other hand, we must not let the agent be too powerful; if he could move backwards and forwards in time at will then it is mysterious why the sets need to be constructed in order at all.

Even if the notion of the ideal agent could be satisfactorily clarified there remains the problem of the status of the ordinals. The cumulative hierarchy is obtained by iterating the power set operation up the entire collection of ordinals. If these are assumed as given from the start this seems a platonistic rather than constructive foundation for the whole enterprise. Wang (p. 532) suggests that the conception of what ordinals there are can develop as the hierarchy is generated. But only countably many ordinals can ever be defined, so it seems that some kind of platonistic conception is inevitable.

Worse than this, however, is the issue of impredicativity. A sine qua non of constructivism is that objects are conceived of as occurring in an order, such that at any point in the construction process, only those objects occurring earlier in the order are available. It seems therefore that no theory allowing impredicative definitions can rightly claim to be constructive: one simply cannot quantify over objects which, if the constructivism is taken seriously, do not exist (“at the time”). But the ZF axioms of which the hierarchy is an intuitive model involve impredicative quantifications. Most striking is the axiom of power set in tandem with the axiom of separation. From the power set axiom we know that for any set x the power set P(x) is also a set; the axiom of separation can then be used to pick out individual subsets by means of a formula φ. But this formula can contain quantifications over anywhere in the universe. To put it informally, what subsets there are of a particular set depends not only on what happens at the level of the set, and the next higher level, but also on what happens in the whole hierarchy—as Bell and Machover [1977] put it, “the size of a power set Pu of a given set u is proportional not only to the size of u but also to the ‘richness’ of the entire universe” (p. 509).<sup>29</sup> This seems incompatible with any constructive interpretation.

It is not that the authors are at all unaware of this; it is just that they are silent on the conflict between it and the constructivist heuristic which they give for the iterative conception of set. Wang for example (p. 532) says explicitly “we do not concern ourselves over how a set is defined, e.g. whether by an impredicative definition” and admits (p. 560) that “if we adopt a constructive approach, then we do have a problem in allowing unlimited quantifiers to define other sets”, but he seems to see no conflict between his own use of constructivist terminology and his advocacy of impredicativity.

The justification of ZF as constructivist in principle is an attempt to have the best of two incompatible worlds, and results in a hybrid position which is philosophically bankrupt and ought to satisfy nobody. A symptom of the philosophical confusion upon which ZF rests is the status of the axiom of choice. This is accepted by most mathematicians, but is not usually regarded as just another of the axioms of set theory—it has a more dubious status. It is customary to state carefully whether or not any theorem requires it, and to do without it if possible. It is almost as though people feel a little guilty in using it. Why is this? I suggest that the explanation is that the strongly non-constructive feel of the axiom conflicts with the (false) idea that the rest of ZF is constructive. But in fact the axiom of choice is fully in the spirit of the rest of set theory—the damage its absence does to the theory of cardinal arithmetic is one demonstration of this. If it were clearly realised that ZF is not constructive at all, the axiom of choice would cease to be regarded as a second-class citizen and take up its rightful position as just another of the axioms of set theory.

The conclusion of this section, then, is that ZF does not embody a philosophically coherent notion of set. There is a coherent constructivist position, which entails repudiating impredicative definitions, obeying VCP I, and ending up perhaps with something like ramified type theory. It seems, however, that such a position will not lead to a foundation for classical mathematics. (Whitehead and Russell famously had to postulate the axiom of reducibility to make possible the derivation of mathematics in their system, but this axiom is unmotivated in the light of the VCP. And alternative versions of constructivism, for example intuitionism, are more damaging yet to classical mathematics.) There is also a coherent anti-constructivist position, which rejects the metaphysics of constructivism and its resultant inability to justify classical mathematics. This position rejects the VCP in all its forms. But ZF is an uneasy compromise between these two: it pays lip-service to constructivism without really meaning it, and in doing so forfeits its claim to philosophical justification.

## 9

Suppose it is admitted that ZF cannot be given a coherent philosophical justification. It seems there is still a third and final argument a defender of it might use: we might call it the argument from mathematical pragmatics.

ZF has proved adequate as a foundation for mathematics, in the sense that all known mathematics can be carried out in ZF. It is convenient to work with: for example, the well-foundedness of the sets allows inductive definitions to be handled smoothly. So whether or not it can be thought of as the axiomatization of a coherent notion of set, it is reasonable—so the argument goes—for it to occupy the position it does as the dominant theory of sets.

One reply to this is that it is no longer clear that ignoring non-wellfounded sets gives a theory which is optimal for applications. In recent years uses have started to be found for non-well-founded theories—indeed the current revival of interest started with Aczel’s realization that the modelling work he was doing in computer science (on parallel processing) was much simpler if one abandoned foundation (Aczel [1988] Chapter 8). Rather than attempt to describe this application in detail, I will try to give the general

flavour with some simpler examples.

It is very common in mathematical modelling to use (ordered) n-tuples $\langle x _ { 1 } , \ldots , x _ { n } \rangle$ . There is a standard way of handling n-tuples in set theory: for example for the pair $\langle a , b \rangle$ we use the set $\{ \{ a \} , \{ a , b \} \}$ . It can happen that we want an entire n-tuple to be equal to one of its elements, and this will be forbidden by the axiom of foundation.

Thus in Barwise and Etchemendy’s treatment of the liar [1987] (so far the best-known application of non-well-founded sets) the aim is to model a proposition which asserts its own falsehood. Propositions are modelled by pairs,<sup>30</sup> so what we need is a proposition p which satisfies $p = \langle \mathbf { F } , p \rangle$ (where F is an atom representing falsehood). This is possible only if we abandon foundation.

A similar example, this time from computer science: a stream is a sequence of data items, and can neatly be defined as an ordered pair where the first element is an item of data and the second element is a stream. Then an infinite sequence of zeroes is a stream s satisfying $s = \langle 0 , s \rangle$ . Once again the axiom of foundation prevents this from being modelled in a natural way. This example is from Barwise and Moss [1996], p. 34. The book explores applications in other areas, for example the theory of games and the model theory of modal logic.

It is true that a hard-line supporter of ZF cannot be forced to repudiate foundation. We can always carry out these modellings by choosing appropriate objects in the well-founded universe. But such an approach is analogous to a hard-line disbeliever in complex numbers insisting on them as mere pairs of reals. As more and more applications are discovered, it becomes clearer that there is no good reason for not accepting non-well-founded sets as genuine sets.

## 10

There is a second and deeper reply to the “pragmatic” argument for ZF. A theory of sets should, I think, be answerable to our informal concept of set as completely arbitrary collection, as well as to the needs of mathematicians. Thus, even if mathematicians can get by using only some special class of sets, it does not follow that we should rest content with a theory which says that these are all the sets there are. Only a non-well-founded theory can convincingly be shown to modify the naive conception as much as, but no more than, is required by the paradoxes; and only in adopting such a theory can we obtain a truly satisfactory solution.

## References

Peter Aczel. Non-well-founded Sets. CSLI, Stanford, 1988.

Jon Barwise and John Etchemendy. The Liar. Oxford University Press, 1987.

Jon Barwise and Laurence Moss. Vicious Circles. CSLI, 1996.

John Bell and Mosh´e Machover. A Course in Mathematical Logic. North-Holland, 1977.

Paul Benacerraf and Hilary Putnam, editors. Philosophy of mathematics: selected readings. Second edition. Cambridge University Press, 1983.

George Boolos. The iterative conception of set. Journal of Philosophy, 68: 215–232, 1971. Reprinted in Benacerraf and Putnam [1983].

Georg Cantor. Grundlagen einer allgemeinen Mannigfaltigkeitslehre. B.G.Teubner, 1883.

Georg Cantor. Letter to Dedekind, 1899. Translation in Heijenoort [1967] pp. 113–117.

Michael Dummett. Frege: Philosophy of Mathematics. Duckworth, 1991.

A. Fraenkel. Zu den Grundlagen der Cantor-Zermeloschen Mengenlehre. Mathematische Annalen, 86:230–237, 1922.

Gottlob Frege. Grundgesetze der Arithmetik, begrifsschriftlich abgeleitet, I. Pohle, 1893.

Kurt G¨odel. Russell’s mathematical logic. In Paul A. Schilpp, editor, The Philosophy of Bertrand Russell. Tudor, 1944. Reprinted in Benacerraf and Putnam [1983].

Kurt G¨odel. What is Cantor’s continuum problem? American Mathematical Monthly, 54:515–25, 1947. Reprinted with revisions in Benacerraf and Putnam [1983].

Warren Goldfarb. Russell’s reasons for ramification. In C. Wade Savage and C. Anthony Anderson, editors, Rereading Russell: Essays in Bertrand Russell’s Metaphysics and Epistemology, volume XII of Minnesota Studies in the Philosophy of Science, pages 24–40. University of Minnesota Press, 1989.

Patrick Grim. The Incomplete Universe. MIT Press, Cambridge, Massachusetts, 1991.

Michael Hallett. Cantorian Set Theory and Limitation of Size. Oxford University Press, 1984.

Michael Hallett. Putnam and the Skolem pardox. In Peter Clark and Bob Hale, editors, Reading Putnam, pages 66–97. University of Minnesota Press, 1994.

J. van Heijenoort, editor. From Frege to G¨odel: A Source Book in Mathematical Logic, 1879-1931, 1967. Harvard University Press.

Stephan K¨orner. The Philosophy of Mathematics. Dover, 1960.

Shaughan Lavine. Understanding the Infinite. Harvard University Press, 1994.

Christopher Menzel. Cantor and the Burali-Forti paradox. Monist, 67:92– 107, 1984.

D. Mirimanof. Les antinomies de Russell et de Burali-Forti et le probl\`eme fondamental de la th´eorie des ensembles. L’Enseignement Math´ematique, 19:37–52, 1917a.

D. Mirimanof. Remarques sur la th´eorie des ensembles et les antinomies Cantoriennes (I). L’Enseignement Math´ematique, 19:208–217, 1917b.

John von Neumann. Eine Axiomatisierung der Mengenlehre. Journal f¨ur die reine und angewandte Mathematik, 154:219–240, 1925. Translation in Heijenoort [1967].

John von Neumann. Uber die Definition durch transfinite Induktion und<sup>¨</sup> verwandte Fragen der allgemeinen Mengenlehre. Mathematische Annalen, 99:373–391, 1928.

John von Neumann. Uber eine Widerspruchsfreiheitsfrage in der axioma-<sup>¨</sup> tischen Mengenlehre. Journal f¨ur die reine und angewandte Mathematik, 160:227–41, 1929.

Charles Parsons. What is the iterative collection of set? In Robert E. Butts and Jaakko Hintikka, editors, Proceedings of the 5th International Congress of Logic, Methodology and Philosophy of Science 1975, Part I: Logic, Foundations of Mathematics, and Computability Theory, pages 335– 367. D. Reidel, 1977. Reprinted in Benacerraf and Putnam [1983] and in Parsons [1983].

Charles Parsons. Mathematics in Philosophy: Selected Essays. Cornell University Press, 1983.

Jules Henri Poincar´e. Les math´ematiques et la logique. Revue de metaphysique et de morale, 1905-6. Translation in Poincar´e [1952].

Jules Henri Poincar´e. Science and Method. Dover, 1952.

Jules Henri Poincar´e. Mathematics and Science: Last Essays. Dover, 1963.

Graham Priest. The structure of the paradoxes of self-reference. Mind, 103: 25–34, 1994.

Jules Richard. Les principes de math´ematiques et le probl\`eme des ensembles. Revue g´en´erale des sciences pures et appliqu´es, 16:541, 1905. Translation in Heijenoort [1967].

Adam Rieger. Circularity and Universality. D.Phil. thesis, University of Oxford, 1996.

Adam Rieger. An argument for Finsler-Aczel set theory. Mind, 109(434): 241–53, 2000.

Bertrand Russell. Letter to Frege, 16th June, 1902. In Heijenoort [1967].

Bertrand Russell. Les paradoxes de la logique. Revue de M´etaphysique et de Morale, 14:627–650, 1906a.

Bertrand Russell. On insolubilia and their solution by symbolic logic. 1906b. Translation of Russell [1906a]; in Russell [1973].

Bertrand Russell. On some dificulties in the theory of transfinite numbers and order types. Proceedings of the London Mathematical Society, series 2, 4:29–53, 1906c. Reprinted in Russell [1973].

Bertrand Russell. Mathematical logic as based on the theory of types. American Journal ofMathematics, 30:222–262, 1908. Reprinted in Russell [1956].

Bertrand Russell. Logic and Knowledge, ed. Robert C. Marsh. Allen and Unwin, London, 1956.

Bertrand Russell. Essays in Analysis ed. Douglas Lackey. George Allen and Unwin, 1973.

J. R. Shoenfield. Mathematical Logic. Addison-Wesley, 1967.

J. R. Shoenfield. Axioms of set theory. In Jon Barwise, editor, Handbook of Mathematical Logic. North-Holland, 1977.

T. Skolem. Einige Bermekungen zur axiomatischen Begr¨undung der Mengenlehre, 1922. Matematikerkongressen i Helsingfors den 4–7 Juli, Den femte skandinaviska matematikerkongressen, Redog¨orelse. Translation in Heijenoort [1967].

Hao Wang. From Mathematics to Philosophy. Routledge and Kegan Paul, 1974. Pages 181–223 reprinted as The concept of set in Benacerraf and Putnam [1983].

Alfred North Whitehead and Bertrand Russell. Principia Mathematica, Volume 1. Cambridge University Press, 1910.

Alfred North Whitehead and Bertrand Russell. Principia Mathematica. Cambridge University Press, 1910–3.

Ernst Zermelo. Beweis, dass jede Menge wohlgeordnet werden kann. Mathematische Annalen, 59:514–516, 1904. Translation in Heijenoort [1967].

Ernst Zermelo. Untersuchen ¨uber die Grundlagen der Mengenlehre, I. Mathematische Annalen, 65:261–281, 1908.

Ernst Zermelo. Uber Grenzzahlen und Mengenbereiche: neue Untersuchen <sup>¨</sup> ¨uber die Grundlagen der Mengenlehre. Fundamenta Mathematicae, 16: 29–47, 1930.