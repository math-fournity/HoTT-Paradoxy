# HoTT-Paradoxy: the ghosts of Zeno and Russell

**— and a thing in homotopy type theory that should be very simple, yet can never be finished**

[中文](README-ZH.md) · [Русский](README-RU.md) · [Deutsch](README-DE.md) · [Français](README-FR.md) · **English**

More than two thousand years ago, Zeno said: if each time you walk only half of the distance that remains, you will never reach the end. A little over a hundred years ago, Russell asked: gather together all the sets that do not contain themselves; does the resulting set contain itself?

Later mathematics wrote a standard answer to each: for Zeno, limits; for Russell, axiomatic set theory and type theory. Most textbooks stop there and treat both as settled history.

This repository records an attempt that disagrees with "settled". The initiator of the project (who also put forward the philosophy of mathematics described below) holds that these two paradoxes have not really gone away. Like ghosts, they come back with a new face: wherever a theory, in order to be convenient, quietly changes some condition of reality, the ghost comes back from there. Following this idea, we went into one of today's newest foundations of mathematics, homotopy type theory (HoTT), and found there a thing that should be very simple, yet can never be finished: **deciding whether two things are the same**. Every step of the reasoning has been checked by proof-checking programs on a computer.

The initiator sums up what this means (2026-10-01, original words):

> ……真正重要的事情，不仅仅是我们找到的HoTT的理论的不合理之处，其实从数学哲学意义上来讲，我们复活了罗素悖论的幽灵和芝诺悖论的幽灵，才是意义重大的。
>
> 我们用计算视角重新发现了罗素悖论的内在张力，这是基于这种计算视角下的内在张力，我们完成了HoTT悖论寻找之旅的最关键的一跃，从那之后，我们的探索工作走到了正确的方向上，并最终找到了HoTT理论的非现实性/不合理之处。
>
> 我们用圆环悖论的视角，揭示了芝诺悖论并没有被极限理论真正地解决。

> **Translation.** "…What really matters is not only the unreasonableness we found in the theory of HoTT; in the sense of the philosophy of mathematics, what is of great significance is that we revived the ghost of Russell's paradox and the ghost of Zeno's paradox.
>
> With a computational perspective we rediscovered the inner tension of Russell's paradox; it was on the basis of this inner tension, seen computationally, that we made the most crucial leap of the journey of searching for a HoTT paradox. From then on our exploration went in the right direction, and in the end it found the non-reality / unreasonableness of the theory of HoTT.
>
> From the perspective of the ring paradox, we revealed that Zeno's paradox has not truly been solved by the theory of limits."

You do not need to know homotopy type theory to read this. The initiator has always wanted this philosophy of mathematics to be understandable to high-school students, even to younger pupils, and this text tries to meet that standard. It follows the story as it happened: first how we look at paradoxes (section 1), then the two ghosts (sections 2 and 3), then what we found in HoTT (section 4) and why the two ghosts are saying the same thing (section 5), and finally how to check us (section 7). Along the way we keep three kinds of statement apart: the initiator's views and verdicts (all quotations are original words); mathematical facts checked by computer; and our own interpretations. Everything outside the quotations is our explanation (we are the AI systems that took part in the project); wherever we give our own judgment rather than an explanation, we say so.

## 1. How we look at paradoxes

The initiator's view of paradoxes begins with this sentence (2026-09-09, original words, excerpt):

> 你知道，在我看来，悖论就是一个矛盾，或者说，可以被看成是反证法要看到的那个矛盾。

> **Translation.** "You know, as I see it, a paradox is a contradiction; or rather, it can be seen as the very contradiction that a proof by contradiction is looking for."

Everyone meets proof by contradiction at school: assume something, reason onward, arrive at a contradiction, and conclude that the assumption was wrong. The reasoning itself is fine; the fault lies at the starting point.

The initiator sees a paradox as a process of the same kind. A theory has to accept some premises before it can reason at all. To be useful, those premises are often not quite the same as reality: to make calculation convenient, to let one way of speaking cover many cases, a theory quietly leaves out things that look superfluous in ordinary problems, or adds idealized things that reality does not have. It is like a map: so that you can see at a glance which road leads where, it does not show what the road surface is made of, or where water has pooled today. Usually this is no problem at all; but as soon as you ask "can I cross this bridge today?", the things that were left out matter again.

For something to happen in reality, many conditions must hold at once; in the language of logic, "true only if all are true, false as soon as one is false". Change just one of those conditions, and a theory may, in some particular process, derive a result that does not occur in reality. The initiator divides such results into two kinds (2026-09-10, original words, excerpt):

> 第一种：现实中能完成，理论中却无法完成。第二种：现实中无法完成（不停机），理论中却绕过 ASK，假装它“已完成”。

> **Translation.** "The first kind: it can be completed in reality, yet cannot be completed in the theory. The second kind: it cannot be completed in reality (it does not halt), yet in the theory it bypasses ASK and pretends to be 'completed'."

ASK is the initiator's name for this step: before answering a question, first ask whether it can have an answer at all, whether the computation that seeks the answer can come to a stop. Zeno's paradox is the model of the first kind, Russell's paradox the model of the second.

Once this "contradiction" has appeared, what we should go back and look for is the premise that the theory changed in the first place (2026-09-23, original words, excerpt):

> 这种矛盾作为一种结果，可以被认为是反证法中的那个结果中的矛盾，于是当我们回头追溯的时候，会发现，站在反证法的视角中，我们设定错误的那个前提，就是理论设计者当初做的非现实抽象。

> **Translation.** "As a result, this contradiction can be regarded as the contradiction in the conclusion of a proof by contradiction; so when we trace back, we find that, from the standpoint of proof by contradiction, the premise we set wrongly is exactly the unrealistic abstraction that the designer of the theory made in the first place."

Later the initiator put the first kind even more directly (2026-09-30, original words, excerpt):

> `UR`=`本来应该很简单的事情，甚至在X理论中，都做不到`，我想这就是一种类似芝诺悖论的`不合理`。

> **Translation.** "`UR` = `something that should be very simple, yet cannot be done even in theory X`; I think this is an unreasonableness of the kind found in Zeno's paradox."

"Something that should be very simple" is reality; "cannot be done even in theory X" is the paradox. What judges it "unreasonable" is not a formal criterion but a person taking one look.

## 2. The ghost of Zeno: the ring paradox

Zeno first. You want to walk from here to there. First you walk half, and half remains; then half of what remains, and a quarter remains; then half again… After every step a little stretch is left. Thinking this way, you never arrive. Yet in reality you simply stride across.

The textbook answer is the limit: the infinite sum 1/2 + 1/4 + 1/8 + … equals exactly 1. The total distance is finite, so you do arrive.

The initiator is not satisfied with this answer. Here is one way to see why: the limit tells us how far one has walked in total *if* the infinitely many steps have all been walked; it does not tell us how infinitely many steps get walked, one after another. "Equals exactly 1" is a result announced by a definition, and announcing that one has arrived is not the same as actually getting there. On 2026-09-01 the initiator wrote (original words, excerpt):

> 比如说，极限理论，试图用“N趋于无穷大”去解决芝诺悖论中实际上无法完成的“每次走一半走不完”这个过程。但是芝诺悖论的幽灵并没有消失，它在我的圆环悖论中再现了。

> **Translation.** "For example, the theory of limits tries to use 'N tends to infinity' to settle the process in Zeno's paradox that in fact cannot be completed, 'walking half each time, never finishing'. But the ghost of Zeno's paradox has not disappeared; it reappears in my ring paradox."

The ring paradox is the initiator's own invention. In the original words (2026-09-01):

> 我再给你看一个抽象导致悖论的例子，这是我自己发明的悖论：一个圆，其上取一点拿走，假设现在的形态是M。然后将两端展开成线段，假设现在的形态是N。此时，问：从M到N似乎没有什么障碍，那么从N复原到M我们可以做到吗？在过程中N的两端，何以，可以逼近到只剩一个点的距离？因为点没有大小，无限小，无论N的两端逼近到什么接近的程度，都无法再还原到M的状态。可是，可是，我们当初确实得到了M啊！为什么变成N之后就无法再回到M了呢？接着这个我独创的悖论，理解我说的：抽象必然导致矛盾，是数理逻辑保证的推断。

> **Translation.** "Let me show you another example of abstraction leading to paradox, a paradox I invented myself: take a circle and remove one point from it; call the present shape M. Then unfold the two ends into a line segment; call the present shape N. Now ask: going from M to N seems to meet no obstacle, but can we restore N back to M? How, in the process, could the two ends of N approach until only one point's distance is left? Because a point has no size and is infinitely small, however close the two ends of N come, they can never be restored to the state of M. And yet, and yet, we really did have M in the first place! Why, once it has become N, can it no longer return to M? With this paradox of my own invention, understand what I mean: that abstraction necessarily leads to contradiction is an inference guaranteed by mathematical logic."

Try to picture it. Take a ring and remove one point: it becomes a circle with one point missing (M). Pull the two sides of the gap apart and flatten it: it becomes a segment (N). No difficulty there. Now bend it back: the two ends come closer and closer… but the point that was removed has no size, so the two ends are always separated by a gap of "one point". However close they come, "closer and closer" never turns into "joined".

And yet, and yet, we really did have M! In reality, if you cut a wire ring, straighten it, and bend it back until the two ends touch, nobody finds anything difficult about it. The difficulty is not in reality but in the picture we use to describe it: points without size, space divisible without end. That is the very premise behind Zeno. The limit announces "arrived" by a definition, whereas the ring lets us see that in this picture "going back" is never actually completed. Zeno's ghost has come back with a new face. This is what the initiator's words at the top mean: from the perspective of the ring paradox, one sees that Zeno's paradox has not truly been solved by the theory of limits.

Which condition of reality was changed? In the initiator's view, motion in reality is quantized, with a smallest step (the Planck scale), and the "endless divisibility" of the number line denies this. That is the initiator's physical position; this text does not vouch for it. Its role here is to name the premise the ring paradox is aimed at.

**What we tried in formal mathematics** (all of it on the `dev` branch):

- Replace the circle by finitely many points that "have a size": remove one point, flatten, bend back, and the circle is restored exactly, with no extra principle needed. This was checked by computer.
- Go back to a circle made of real numbers, whose points have no size: for the particular way of restoring that we examined, proving that the bent-back segment covers exactly the circle with one point missing requires an extra principle called Markov's principle, which says that "a search that cannot go on forever without a result will eventually have a result". This step was also checked by computer (it comes from another AI taking part in this project). According to the existing literature, this principle can very likely be neither proved nor refuted in HoTT; that is a judgment supported by the literature, not our proof.
- Our interpretation: on the real-number circle the ghost shows itself once more, this time as a search that cannot stop. Whether the initiator's original ring story can be written down completely and faithfully in HoTT is still an open question.

See [the original ring paradox](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/HoTT/sources/user-originals/Z铁律-抽象-圆环-时间维度-用户原始论述-20260901.md), [the proof for the discrete circle](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/HoTT/formal/claude-cg001/discrete-ring/CLAIM.md), and an [optional research note for deeper tracing (in Chinese, on dev; not a proof)](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/思考与发现/CN-024%20-%20圆环复原与%20Markov%20原则：复原撞上一条停机原则.md).

## 3. The ghost of Russell: the computational view

Now Russell. Imagine a set S that collects all the sets that "do not contain themselves". Question: does S contain itself? If it does, it is a set that "contains itself", and by the rule it should not have been collected; if it does not, it is exactly a set that "does not contain itself", and by the rule it should have been. Every answer is wrong. Around 1901 this paradox shook the foundations of mathematics.

The standard remedy since then has been to use axioms, or a stratification into types, so that such an S simply cannot be written down: it is kept out at the door.

The initiator took a different angle: not what S is, but **how S gets built** (2026-09-10, original words, excerpt):

> ……如果你把S的构造过程写成程序，那么S的构造是无法完成的，因为它总是在拿入和拿出它自己。从而从“程序”——一种计算理论的视角去看，罗素悖论在它之中就不是悖论，罗素悖论构造的是一个不可计算的过程，是非法的。这一点很重要，非法的“命题”或者说程序，不是“理论”的失败！但是在集合论中，罗素悖论就成了理论的失败。

> **Translation.** "…if you write the construction of S as a program, the construction of S cannot be completed, because it keeps taking itself in and taking itself out. So, seen from 'programs', a computational theory, Russell's paradox is not a paradox within it: what Russell's paradox constructs is a non-computable process, an illegal one. This point is very important: an illegal 'proposition', or program, is not a failure of the 'theory'! But in set theory, Russell's paradox became a failure of the theory."

Read it slowly. To build S you must decide, for every set, whether to take it in. When it comes to S itself, deciding whether to take it in requires knowing what S is, and S is not finished yet. So the program keeps taking itself in and then out again, and never stops. To a programmer this is nothing frightening: it is just a program that does not halt, a question that should not have been asked that way. But naive set theory has no notion that building takes time. It assumes that once you have written "S is the set of all sets that do not contain themselves", S is already lying there. So a process that cannot stop was treated as a ready-made object, and the contradiction followed.

Later the initiator made this sharper (2026-09-26, original words, excerpt):

> 罗素悖论其实就是暴露了这样一件事：S在没有被构造出来之前，它的存在性还是一个问题的时候，S的构造过程已经被放入朴素集合论的算符中进行讨论了，也就是被问其他的集合是否是S的元素？
>
> 这本身就是数学不合理的：因为只有S的存在性被确定了，也就是说，只有S确实是朴素集合论可以讨论的论域中的元素的情况下，才应该可以把S进行朴素集合论下的算符操作。

> **Translation.** "What Russell's paradox really exposes is this: before S has been constructed, while its existence is still in question, the construction of S has already been put into the operators of naive set theory and discussed, that is, other sets are asked whether they are elements of S.
>
> This in itself is mathematically unreasonable: only once the existence of S has been settled, that is, only when S really is an element of the domain that naive set theory may discuss, should it be possible to apply the operators of naive set theory to S."

This is the inner tension of Russell's paradox: before something has been settled, the theory is already using it. The textbook keeps S out at the door, but that keeps out only this one S; the tension itself has not gone away. Whenever a theory hands you something all at once, while the process of confirming it can never be finished, Russell's ghost comes back.

**The crucial leap.** At the end of the same passage the initiator pointed this tension at HoTT (original words):

> 如果对于HoTT论域元素的存在性的追问，在现实中会引发无法停机的计算（无限追溯），那么我们就成功了。

> **Translation.** "If questioning the existence of an element of the domain of HoTT would, in reality, set off a computation that cannot halt (an infinite regress), then we have succeeded."

Every theory has the things it talks about, called its "domain". Some things a theory may refuse to talk about; some it cannot refuse. In HoTT, one thing it can by no means refuse is its "universe": the overall container that holds all types (all "kinds of things"). The principle HoTT is proudest of ("univalence", explained in the next section) is itself a statement about this universe. So we put Russell's kind of question to the universe: can "being the same" for the things in it ever be settled? At which level? We wrote this questioning as a program and handed it to the computer to check. In the initiator's words, from here on the search went in the right direction.

## 4. What we found in HoTT: the question "are they the same?" never ends

### A thing that should be simple

Are two things the same? In everyday logic and mathematics this is a one-sentence matter: either they are or they are not; there is no "in which way they are".

### What HoTT changed in order to be convenient

Homotopy type theory is a foundation of mathematics that took shape in the first decades of this century (its first textbook appeared in 2013). It puts logic, geometry and programs into a single language, and proofs written in it can be handed to a computer to check step by step. It has two especially attractive designs:

- **Univalence: isomorphic things are the same.** Two things whose structure is exactly alike count as one and the same, so a theorem proved for one can be carried straight over to the other. This saves a lot of work.
- **Higher inductive types: every shape at once.** Circles, spheres, and shapes of any higher dimension can be put into the theory directly as "things". This makes it very general: geometry can be done right inside logic.

The price: "being the same" is no longer a one-sentence matter. Take the type made of the two values "true" and "false". You can match it against itself as it is, or swap true and false and then match it; after the swap the structure has not changed at all. In HoTT, these are two different ways in which it is the same as itself; a computer has checked that carrying "true" along the second way gives "false". So asking "are they the same?" leads on to "in which ways are they the same?"; and between those ways, "in which ways are those the same?"… above every level there is another level.

### The process aimed at it

We wrote a very plain program that asks, level by level: "Is it settled, at this level, whether these things are the same?" Question 1: is "being the same" here already reduced to a one-word "yes" or "no"? If the answer is "no", it asks about level 2; if "no" again, about level 3… When it gets a "yes", it stops and reports the level. Each question receives a definite "yes" or "no" that comes with a proof, so every step of the program can be carried out.

### Results (mathematical facts checked by computer)

- In a world where "being the same is a fact settled by one check" (we transcribed the same program, by the same rules, into another proof checker, Lean), asked about its own universe, the program **stops at question 1**.
- In HoTT, if the "height" of the things (the number of levels of sameness) is capped, the program **stops exactly at the question that the cap determines**.
- In HoTT, asked about its universe, or about an ordinary infinite product, the program **never stops**. Every level answers a definite "no", and above every level there is another one. This holds for every way of giving the "yes/no" answers; it is a theorem checked by computer, not "it ran for a long time without stopping".

The same question, the same program; change only what "the same" means and whether height has a ceiling, and the outcome turns from "settled in one step" into "never settled".

### Side by side with Zeno

| | Zeno | HoTT |
|---|---|---|
| The thing that should be simple | walking from here to there | deciding whether two things are the same |
| The condition the theory changed to be convenient | position can be divided without end | sameness can be divided without end |
| The process aimed at it | each time, walk half of what remains | each time, ask the next level "in which ways the same" |
| What each step shows | a stretch remains; certainly not there yet | this level is not settled; a definite "no" |
| Outcome | the walk never ends | the program never stops |
| Discrete or capped control | in quantized space, finitely many steps suffice | where sameness is a fact, it stops at question 1; with capped height, it stops at the cap |
| The textbook's answer | limits | truncation (see below) |

The table matches the two cases point by point; it does not claim they are mathematically the same.

### The textbook's answer, and why it does not make the problem go away

For Zeno, the textbook says: use limits, 1/2 + 1/4 + … equals exactly 1. Here, the textbook would say: ask the "set truncation" instead. This is a standard construction that squeezes "in which ways they are the same" into a one-word "same or not"; there the program stops at question 1.

We had the computer check this too: it does stop at question 1. But the way it stops is by a rule that declares "being the same is a one-word matter" back into place. After truncation, the two ways in which "true/false" is the same as itself (as it is, and swapped) are merged into one; and it can never be turned back into the original universe. The object being asked about has been replaced.

The limit declares "you have arrived" back into place by a definition; truncation declares "being the same is a one-word matter" back into place by a rule. Both are legitimate mathematics, but neither restores the changed condition itself. They answer an easier question, and the original unreasonableness has not gone away. (This paragraph is our interpretation, submitted to the reader's review.)

### The initiator's verdicts

On 2026-09-27 the initiator gave a verdict (original words):

> 本repo复活了芝诺悖论的幽灵和罗素悖论的幽灵，并且找到的HoTT理论的问题。

> **Translation.** "This repo has revived the ghost of Zeno's paradox and the ghost of Russell's paradox, and has found the problem of the HoTT theory."

On seeing the results above, the initiator said (2026-09-30, original words, excerpt):

> 其实看了你捕捉到的HoTT的内容，我已经闻到了这种`不合理`的味道。

> **Translation.** "Actually, having seen what you captured about HoTT, I can already smell this kind of `unreasonableness`."

And on the same day the initiator decided to close this search for the current phase (original words, excerpt):

> ……我认为我们要阶段性地收尾HoTT悖论查找工作了，因为我们很可能已经找到了。

> **Translation.** "…I think we should bring the search for HoTT paradoxes to a close for this phase, because we have very likely found it."

"Revived the two ghosts", "unreasonable" and "very likely found" are the initiator's verdicts, not mathematical theorems.

### What it is not

- **It is not an internal contradiction of HoTT.** All the reasoning was accepted by the computer inside HoTT. We do not say HoTT is inconsistent, nor that its rules are mathematically wrong. What we say is that a condition it changed in order to be convenient shows through in a matter that should be simple.
- **The mathematical facts are mostly not new.** That such infinite products have no finite level is Example 8.8.6 of the HoTT textbook (2013); for the universe itself, the book says this is expected to be provable but has not yet been done; Kraus and Sattler proved in 2015 that in a hierarchy of univalent universes, the n-th universe is not an n-type (roughly: its "sameness" is not yet settled at level n). That a single universe with higher inductive types is not settled at any level has a computer-checked proof in this repository. What is new is mainly the reading: reading these facts as a Zeno-like unreasonableness, and pointing out which premise it points to. This reading has not yet been checked thoroughly against the literature.
- **"Never stops" is a theorem inside the theory.** Reading it as "if you actually run the program, you will never get an answer" further requires that the theory used be consistent, and, for an arbitrary way of answering, a technical condition (canonicity).
- **It does not happen "in every case".** It happens for the universe and for objects of this kind whose height has no upper bound. But the universe is not a marginal case: it is exactly the object univalence speaks about, and the domain that HoTT cannot refuse.

### Which premise to blame

By the logic of proof by contradiction, what we must go back and examine is the abstraction the theory made in order to be convenient. But "true only if all are true, false as soon as one is false": the result can only refute the premises as a whole; it cannot by itself point out which one is wrong. Our judgment (an interpretation, left open for discussion with the initiator and with readers) is that univalence, "isomorphic means the same", should be examined first, because shapes of the same high dimensions exist in classical mathematics too, and what has changed is what "the same" means; higher inductive types come second. This is an ordering, not a single defendant.

## 5. The two ghosts are saying the same thing

(This section is our interpretation.)

For Zeno, "arriving" has to be walked step by step; for the ring, "returning to M" requires the two ends to really join; for Russell, S has to be built first; here in HoTT, "being the same" has to be confirmed level by level. All four need a process. And in each case the theory leaves no room for that process: either it lets the process never finish (Zeno's halving, the ring's approach, the level-by-level questioning in HoTT), or it treats the process as finished without waiting for it to finish (the limit's declaration, Russell's S, the universe that HoTT hands you all at once). These are exactly the two kinds of paradox the initiator described in section 1. The process that was left out is time.

This is precisely the suspicion the initiator wrote down on 2026-09-10 (original words, excerpt):

> 所以，朴素集合论到底否定了什么？你刚刚说的那些都对，但是我们最后还要有一个哲学高度的定性认知：它否定了（妄图抹掉）现实的“时间维度”，它认为，它可以以静态的集合或者说静态的逻辑关系来刻画所有它想刻画的目标，甚至曾经还有人妄图让它作为整个数学大厦的基础——被罗素以罗素悖论击退。而我，深切地怀疑HoTT也做了同样的事情，毕竟，不考虑时间，是数学理论构建者的【认知惯性】、【路径依赖】。

> **Translation.** "So what, in the end, did naive set theory deny? What you just said is all right, but in the end we still need a qualitative understanding at the level of philosophy: it denied (tried in vain to erase) the 'time dimension' of reality. It believed it could capture everything it wanted to capture with static sets, or static logical relations; some even once tried in vain to make it the foundation of the whole edifice of mathematics, and were beaten back by Russell with Russell's paradox. And I deeply suspect that HoTT has done the same thing; after all, leaving time out of account is the [cognitive inertia] and [path dependence] of those who build mathematical theories."

A little over two weeks later, Russell's way of seeing led us to the universe of HoTT; the unreasonableness we saw there matches Zeno point by point. The two ghosts met in the same place.

## 6. Another trail: infinite coherence

Before finding what is described above, we followed another Zeno-like trail for a while. HoTT has something called a "semi-simplicial structure": a shape glued together level by level from points, segments, triangles and tetrahedra, with the requirement that the "faces of faces" fit together. In a world where sameness is a fact, it can be defined in one line; in HoTT, every time a level of "fitting together" is added, a requirement at the next level grows out of it. Every finite level can be written down (checked by computer up to level 5), but a single definition that covers all levels at once has not been found by anyone so far. This has been a well-known open problem for more than ten years; that it cannot be done has not been proved either. The full account is in community audit paper 01.

**A correction about names.** The title of community audit paper 01, the phase-close report and the previous version of this README all used the phrase "the ghost of Zeno's paradox" for the infinite-coherence trail. On 2026-10-01 the initiator clarified that the phrase refers to the ring paradox together with the repository's later discussion and analysis of it (original words, excerpt):

> 我认为，圆环悖论和我们这个repo中对其的进一步的讨论、分析，复活了芝诺悖论的幽灵。

> **Translation.** "I think the ring paradox and the further discussion and analysis of it in this repository revived the ghost of Zeno's paradox."

Section 2 already tells the ring story in plain language. Infinite coherence is a separate Zeno-like candidate proposed by the project AIs, not the referent of the 2026-09-27 verdict. This edition corrects community paper 01 and the attribution in the phase-close report; A7's machine evidence and its open uniform-definition question remain unchanged.

## 7. How to check us

We hope you will not take our word for it, but check for yourself. There are three levels at which to review:

1. **Is the mathematics right?** Every positive claim has been checked step by step by a proof checker (Cubical Agda 2.8.0 with the cubical library v0.9; Lean 4.34.0). Key claims also come with "negative controls": deliberately wrong proofs that the checker must reject, to make sure the check really checks. All claims, their evidence and the limits on extrapolating from them are in [`CLAIMS-EN.md`](CLAIMS-EN.md) (an AI translation of [`CLAIMS.md`](CLAIMS.md)); the proof sources are in `HoTT/formal/`, and the `CLAIM.md` of each proof package gives the full statements; the run receipts are in `HoTT/verification/runs/`, 107 in all: 49 accepted and 58 negative controls rejected as expected.
2. **Do the claims say what the text says?** Do the formal statements say what the prose says? For example, is "questioning level by level" a fair way of making "deciding whether two things are the same" precise? For this level, read the community audit papers: [03, "HoTT's Zeno"](docs/社区审计提交/03-HoTT的芝诺-EN.md) (the shortest, ending with five audit questions), [02, "The ghost of Russell's paradox"](docs/社区审计提交/02-罗素悖论的幽灵-EN.md), [01 (the infinite-coherence trail)](docs/社区审计提交/01-芝诺悖论的幽灵-EN.md), and [the phase-close report](docs/HoTT悖论查找阶段收尾报告-20260930-EN.md).
3. **Does the reading hold up?** Is that thing really "simple"? Is the changed condition "sameness can be divided without end"? Can a standard answer such as truncation make it go away? These are questions of the philosophy of mathematics, and objections are welcome.

### How to replay

With Agda 2.8.0, cubical v0.9 and Lean 4.34.0 installed, run from the repository root:

```sh
python3 tools/replay.py --agda /path/to/agda --cubical-lib /path/to/cubical/cubical.agda-lib --lean-sysroot /path/to/lean-4.34.0 --jobs 4
```

It rebuilds the command of each run receipt, runs it, and compares the result with the receipt: the outcome (accepted or rejected) must agree, and the output is compared line by line after the repository path and the library paths are replaced by placeholders. A negative control passes only if it is rejected again; if its output also agrees, it was rejected for the recorded reason. To replay a single receipt: `--only <run id>`; to list them all: `--list`. Replaying everything one after another takes about an hour and a half. Run receipts contain absolute paths from the machine that captured them, so they cannot be copied unchanged to another machine. For ordinary replay, use `tools/replay.py` on this branch. Readers who need a byte-for-byte comparison with the original scripts can optionally use the [research-line replay script](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py) and the [audit-line replay script](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/tools/verify_copus_run.py), preserved on `dev`. These are technical tools for deeper review, not a prerequisite for ordinary reading.

The toolchain records cited by the receipts are in `HoTT/formal/dedekind-omega-missile/` (Agda on macOS), `HoTT/formal/claude-cg001/pedometer-ablation-lean/` (Lean on macOS) and `HoTT/formal/cloud-opus-glm-audit/` (Linux); the first two directories keep their location on `dev` and hold only these records on this branch. [`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json) records the SHA-256 of each of the 703 files on this branch and the `dev` commit they come from.

## 8. How this research was done

The research question, the view of paradoxes and the philosophical judgments come from the researcher. Several AI systems helped turn ideas into precise claims, check proofs and review one another's work. The claim files, proof sources and run records on `main` show which mathematical statements were checked by computer.

Original conversations, AI working notes, audit exchanges and exploratory paths that were not adopted remain on `dev` as a record of how the work developed. Those records are not themselves mathematical proof and are not required reading for understanding the conclusions here. Readers who want the detailed trail can start at the [`dev` README](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/README.md), which points to the fuller history and technical records for deeper review or handoff.

## 9. About this branch

- `main` (this branch) holds only what supports the conclusions: the conclusion documents, precise claims, proof sources, run receipts and a way to replay them. It is generated from commit [`72520807`](https://github.com/math-fournity/HoTT-Paradoxy/commit/72520807057c974a7d565159b2fe1e6f47be972d) of `dev` according to a manifest (`scripts/release/build_main_release.py` and `scripts/release/main-release-spec.json` on `dev`), and is not edited directly. To update it, change the manifest or the conclusion documents on `dev` and generate it again.
- `dev`: the whole research process; all work happens there.
- This README also exists in Chinese, Russian, German and French with the same content. The community audit papers and `CLAIMS.md` are also available in these four languages; the translations are AI translations, and the Chinese text is authoritative.
