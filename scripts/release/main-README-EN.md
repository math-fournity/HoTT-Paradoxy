# ZFC Failure

```
我们假设存在一个ZFC的缺失了的理论观察力Q，即其对时间维度的观察存在一种不完备，这种不完备导致：
A：在芝诺悖论上，Q的存在，导致允许数学幻觉P的成立——因为Q是缺失性的，所以无从拒绝P，进而使得在ZFC中被允许判定：极限理论解决了芝诺悖论和圆环悖论。
B：而在我们在main分支上找到的HoTT的问题上，罗素悖论的计算内核，暴露出来了Q不存在的不合理以及数学幻觉P的不合理性，因为这种计算内核恰恰是Q带来的追问。
那么ZFC在Q上的缺失，及这种缺失允许产生出的数学幻觉P，就在ZFC中表现出了矛盾。
换句话说，允许“极限理论解决了芝诺悖论”是数学界需要的，但这同时要求：
1、数学幻觉P的成立。
2、ZFC缺失Q。
而数学幻觉P成立，在芝诺悖论上带来了数学家想要的结果：芝诺悖论被解决。
而在我们发现的HoTT的问题上，他们却得到了自己不想要的结果——我们所定义的那种`不合理`。
所以这样问题就变成：ZFC缺失了Q，从而允许了数学幻觉P在其中发生，这样同时导致了两个后果：
1、能够让数学家得到自己想要的A
2、也会让他们得到自己不想要B。
再换句话说：设ZFC-1=ZFC+A，则ZFC-1=ZFC+P，而ZFC-1导致B。
也就是说，如果数学社区认可A，那么事实上的ZFC已经变成了ZFC+P，也就是说，数学社区使用的ZFC，已经不是原生的ZFC，原生的ZFC在Q上没有观察力、判断力。
而如果数学社区在Q上选择了P，等价于数学社区实际使用的不是ZFC，而是ZFC-1。
而ZFC-1中的P之所以是所谓的“数学幻觉”，本质上是反现实的，是不可计算的，是我们在`核心认知.md`中所说的：理论为了经济性和工具性便利，作出的否定现实的理论中的前提假设。
我们同时在`核心认知.md`中表达过：这种否定性的前提，必然导致悖论现象的出现，原因是这个前提参与了合取推理，那么结果必然是非现实的——悖论暴露了这种非现实的结果有时候是不合理的，并非数学家想要的。也就是说，虽然A是数学家想要的，但是B就不是了。
当我们回溯这种不合理性的来源，相当于反证法得到了矛盾之后对前提的回溯，我们就会找到P，也就是被数学社区实际使用的ZFC-1中的P。
选择数学幻觉P加在ZFC上，是数学社区与魔鬼达成了交易，从而社区得到了A型数学便利，但是魔鬼要的从来都是“灵魂”。
数学的灵魂——数学真理性。
```

**Translation.**

```
We assume that there is an observational power Q of theory that ZFC lacks, that is, its observation of the time dimension has a kind of incompleteness, and this incompleteness leads to:
A: On Zeno's paradox, the existence of Q leads to allowing the mathematical illusion P to hold — because Q is missing, there is no way to reject P, and this in turn allows the judgment, within ZFC, that the theory of limits has solved Zeno's paradox and the ring paradox.
B: And on the problem of HoTT that we found on the main branch, the computational kernel of Russell's paradox has exposed the unreasonableness of Q's absence and the unreasonableness of the mathematical illusion P, because this computational kernel is exactly the questioning that Q brings.
Then ZFC's lack of Q, and the mathematical illusion P that this lack allows to arise, show up in ZFC as a contradiction.
In other words, allowing "the theory of limits has solved Zeno's paradox" is something the mathematical world needs, but at the same time it requires:
1. that the mathematical illusion P holds;
2. that ZFC lacks Q.
And P holding brings, on Zeno's paradox, the result mathematicians want: Zeno's paradox is solved.
But on the problem of HoTT that we found, they get a result they do not want — the kind of `unreasonableness` that we have defined.
So the question becomes: ZFC lacks Q, which allows the mathematical illusion P to happen in it, and this leads at the same time to two consequences:
1. it lets mathematicians get the A they want;
2. it also makes them get the B they do not want.
To put it another way once more: let ZFC-1 = ZFC + A; then ZFC-1 = ZFC + P, and ZFC-1 leads to B.
That is, if the mathematical community accepts A, then the de facto ZFC has already become ZFC + P; the ZFC the mathematical community uses is no longer native ZFC, and native ZFC has no power of observation or judgment on Q.
And if the mathematical community has chosen P on Q, this amounts to the community actually using not ZFC but ZFC-1.
And the reason why P in ZFC-1 is a so-called "mathematical illusion" is that it is, in essence, anti-real and non-computable; it is what we said in `核心认知.md` (the core cognition): a premise in a theory that denies reality, made for the convenience of economy and of use as a tool.
We also said in `核心认知.md`: such a denying premise necessarily leads to the appearance of paradoxes, because this premise takes part in conjunctive reasoning, so the result is necessarily non-real — paradoxes expose that such non-real results are sometimes unreasonable, not what mathematicians want. That is, although A is what mathematicians want, B is not.
When we trace this unreasonableness back to its source, which amounts to tracing back to the premises after a proof by contradiction has reached its contradiction, we find P, that is, the P in the ZFC-1 that the mathematical community actually uses.
Choosing to add the mathematical illusion P to ZFC is a bargain the mathematical community has struck with the devil, by which the community obtained A-type mathematical convenience; but what the devil always wants is the "soul".
The soul of mathematics — mathematical truth.
```

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

You do not need to know homotopy type theory, or set theory, to read this. The initiator has always wanted this philosophy of mathematics to be understandable to high-school students, even to younger pupils, and this text tries to meet that standard. It follows the story as it happened: first how we look at paradoxes (section 1), then the two ghosts (sections 2 and 3), then what we found in HoTT (section 4) and why the two ghosts are saying the same thing (section 5). Section 6 returns to the passage at the top of the page, the "ZFC Failure" that the initiator personally placed there on 2026-10-04: this research finally converged on it, and the problem lies in ZFC, the set theory mathematicians actually use, and in a choice called A. Finally, how to check us (section 8). Along the way we keep three kinds of statement apart: the initiator's views and verdicts (all quotations are original words); mathematical facts checked by computer; and our own interpretations. Everything outside the quotations is our explanation (we are the AI systems that took part in the project); wherever we give our own judgment rather than an explanation, we say so.

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

Which condition of reality was changed? The initiator later split the problem in Zeno's paradox into two (2026-10-15, original words, excerpt):

> 在芝诺悖论中，首先存在一个问题：不可计算，也就是无限的过程的结果，被当作已经完成的结果参与计算。这肯定是有问题的。
> 其次，还有一个问题，就是现实到底是怎样的？……我们可以只观察到量子化时空这一层，这一程是量子化的、不连续的，足以支撑我们的后续思考。
> “现实中很容易完成”这句话，或者说，运动在现实中可以完成，因为量子化层面，在我们要观察的运动的物体来说，时空可以堪称是不再可分的不连续状态，所以，现实是“跳着”完成的。换句话说，现实的时空，在我们所观察的运动的物体来说，不满足芝诺悖论需要的持续不断地1/2切分这个要求。

> **Translation.** "In Zeno's paradox there is, first, one problem: non-computability, that is, the result of an infinite process is treated as an already completed result and used in computation. That is certainly a problem.
> Second, there is another problem: what is reality actually like? … We can observe only the layer of quantized space-time; this stretch is quantized and discontinuous, and that is enough to support our further thinking.
> The sentence 'in reality it is easily completed' — or, motion can be completed in reality — holds because at the quantized level, for the moving objects we want to observe, space-time can be regarded as a discontinuous state that can no longer be divided; so reality completes 'by jumps'. In other words, the space-time of reality, for the moving objects we observe, does not meet the requirement that Zeno's paradox needs: halving by 1/2, continuously and without end."

The second problem points to the "endless divisibility" of the number line, which mathematicians call density: between any two points there are always other points. The ring paradox is aimed at it too: only because points have no size and space can be divided without end does "closer and closer" never turn into "joined". The first problem is taken up in section 6: it is what the initiator later named A. "Reality completes by jumps" is the initiator's judgment about reality; this text does not vouch for it. What mathematics can prove is what happens in a world whose points have a size (see below).

**What we did in formal mathematics.** The initiator's ring paradox has been written as mathematics sentence by sentence and checked by computer, using the real numbers and the geometry that mathematicians use every day (the proof checker Lean with its standard mathematics library Mathlib). Going through the original words one sentence at a time:

- “从M到N似乎没有什么障碍” ("going from M to N seems to meet no obstacle"): the circle with one point missing (M) and a segment (N) can be turned into each other in one step, with no limit involved.
- “可是，可是，我们当初确实得到了M啊！” ("and yet, and yet, we really did have M in the first place!"): M is really there.
- “从N复原到M我们可以做到吗？” ("can we restore N back to M?"): bend the segment back step by step, each step covering half of what remains. The two ends come closer and closer and, in the sense of limits, "arrive"; but at every finite step the two ends have not yet met, and the shape at that step is not M; only at the moment "after all the steps" is the shape M. The far end, as it bends back, walks exactly Zeno's path.
- “因为点没有大小，无限小” ("because a point has no size and is infinitely small"): at every step the gap between the two ends still contains infinitely many points, and its length is greater than zero; "only one point's distance" is never reached at any finite step.
- Why it cannot go back: the removed point is crowded on all sides by other points. It is exactly at such places that "approaching" and "arriving" come apart.
- Control: replace the circle by finitely many points that "have a size": remove one point, flatten, bend back, and it closes in finitely many steps.

Our interpretation, which the initiator accepted on 2026-10-15 as the standard explanation: taking the circle apart is a transformation given directly, completed in one step; putting it back is a process of approach that always stays a little short; on a circle whose points have no size and which can be divided without end, the two come apart. The premise to blame is "endless divisibility".

(The previous version of this README described another way of writing it: restoring the circle needed an extra logical principle called Markov's principle. That version captured only part of the original story and has been superseded by the sentence-by-sentence version above.)

See [the original ring paradox]({{REPO}}/blob/dev/HoTT/sources/user-originals/Z铁律-抽象-圆环-时间维度-用户原始论述-20260901.md) and [the full statements of the sentence-by-sentence formalization](HoTT/formal/claude-cg001/circle-paradox/CLAIM.md).

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

By the logic of proof by contradiction, what we must go back and examine is the abstraction the theory made in order to be convenient. But "true only if all are true, false as soon as one is false": the result can only refute the premises as a whole; it cannot by itself point out which one is wrong. What can be done is to take the premises away one at a time and see whether the outcome changes.

The controls checked by computer hold for any "collection" (a catalogue in which each number points to a thing):

- with both "sameness is a structure" (univalence) and "every height handed over at once", the questioning never stops;
- cap only the height of the members, and the questioning stops at the cap;
- keep the members exactly as in the universe example, with every height present, and only turn the "sameness" of the catalogue's numbers into a one-sentence fact, and it stops at the first question.

So neither can be dropped. But this theorem is symmetric in the two; it does not say which of them departs from reality.

The initiator ruled on 2026-10-15: there is a single defendant, the "ready-made collection", that is, the universe hands you at once, as something already lying there, a whole that would take infinitely many levels to confirm; univalence is one of the causes and is kept. Section 6 will show that this is exactly what the initiator calls A. (The previous version of this README gave our own ordering here: univalence first, higher inductive types second. It has been corrected according to the ruling.)

## 5. The two ghosts are saying the same thing

(This section is our interpretation.)

For Zeno, "arriving" has to be walked step by step; for the ring, "returning to M" requires the two ends to really join; for Russell, S has to be built first; here in HoTT, "being the same" has to be confirmed level by level. All four need a process. And in each case the theory leaves no room for that process: either it lets the process never finish (Zeno's halving, the ring's approach, the level-by-level questioning in HoTT), or it treats the process as finished without waiting for it to finish (the limit's declaration, Russell's S, the universe that HoTT hands you all at once). These are exactly the two kinds of paradox the initiator described in section 1. The process that was left out is time.

This is precisely the suspicion the initiator wrote down on 2026-09-10 (original words, excerpt):

> 所以，朴素集合论到底否定了什么？你刚刚说的那些都对，但是我们最后还要有一个哲学高度的定性认知：它否定了（妄图抹掉）现实的“时间维度”，它认为，它可以以静态的集合或者说静态的逻辑关系来刻画所有它想刻画的目标，甚至曾经还有人妄图让它作为整个数学大厦的基础——被罗素以罗素悖论击退。而我，深切地怀疑HoTT也做了同样的事情，毕竟，不考虑时间，是数学理论构建者的【认知惯性】、【路径依赖】。

> **Translation.** "So what, in the end, did naive set theory deny? What you just said is all right, but in the end we still need a qualitative understanding at the level of philosophy: it denied (tried in vain to erase) the 'time dimension' of reality. It believed it could capture everything it wanted to capture with static sets, or static logical relations; some even once tried in vain to make it the foundation of the whole edifice of mathematics, and were beaten back by Russell with Russell's paradox. And I deeply suspect that HoTT has done the same thing; after all, leaving time out of account is the [cognitive inertia] and [path dependence] of those who build mathematical theories."

A little over two weeks later, Russell's way of seeing led us to the universe of HoTT; the unreasonableness we saw there matches Zeno point by point. The two ghosts met in the same place.

Then what took the place, inside the theory, of the time that was left out? Following this question, the initiator went back to the ground most mathematicians stand on today.

## 6. Back to the top of the page: the problem of ZFC-1

### A deeper question

After finding that thing in HoTT, the initiator turned to a deeper layer. The ground under the feet of most mathematicians today is a set theory called ZFC: written with about ten axioms about "sets", it lets almost all of mathematics be written as its theorems. The initiator asked (2026-10-03, original words, excerpt):

> 其实我觉得ZFC的问题我们已经找到了，就是圆环悖论的存在，就是ZFC的问题。你想，明明芝诺悖论没有解决，为什么极限理论可以声称已经在把它在ZFC中解决了呢？

> **Translation.** "Actually, I think we have already found the problem of ZFC: the existence of the ring paradox is the problem of ZFC. Think about it: Zeno's paradox has clearly not been solved, so why can the theory of limits claim to have solved it in ZFC?"

The next day the initiator wrote the passage "ZFC Failure" at the top of this page, and later made its letters clear one by one. One thing first: the initiator borrowed these letters at different times, to make the passage at hand clear, and the same letter can change its meaning over time. In the passage at the top, for instance, "A:" and "B:" are first the labels of two items, and A also names the result mathematicians want ("A-type mathematical convenience"); ten days later the initiator defined A as an act. Below we always follow the initiator's latest wording.

### A missing gate: Q

The initiator's definition of Q (2026-10-14, original words):

> ZFC缺的Q，是一种对数学理论M的观察力，这种观察力就是对某种存在于理论M中的表述L是否是“可计算的、可停机的”的判断。
>
> 一种表述是不可停机的，另外一种表述是可停机的，这两种表述在ZFC那里，在是否可停机这个观察角度上，不存在辨别力。
>
> 而是否可停机、可计算，恰恰是必须考察的 —— 它被哥德尔提出，被图灵重新表述，在算法设计中，更是一个算法合法的最根本的前提。

> **Translation.** "The Q that ZFC lacks is a power of observing a mathematical theory M; this power is the judgment of whether some statement L in the theory M is 'computable, able to halt'.
>
> One statement cannot halt, another can; in ZFC, from the angle of whether they can halt, there is no power to tell the two apart.
>
> And whether something can halt, whether it is computable, is exactly what must be examined — it was raised by Gödel, restated by Turing, and in the design of algorithms it is even the most fundamental precondition for an algorithm to be legitimate."

This is the ASK of section 1: before accepting that a result "is already there", first ask whether the process that produces it can stop.

The initiator places particular weight on that last sentence. In proof checkers of the kind that treat programs as proofs (Agda and Lean, used in this repository, are such checkers), this gate operates every day: a recursive definition is accepted only if it can be shown that its computation stops. The computer has checked that if this gate is removed, every proposition can be "proved" and logic collapses on the spot; with the gate in place, definitions have solutions.

### Two choices: A

The initiator went on (2026-10-14, original words):

> ZFC放弃了这种观察力，得到了A型数学便利，并同时异化为了ZFC-1=ZFC+A。放弃是一次选择，而A是第二次选择。A是什么？A就是一个无限的步骤才能到达，从而存在的结果，当作已经存在的结果，参与运算。

> **Translation.** "ZFC gave up this power of observation, obtained A-type mathematical convenience, and at the same time turned into ZFC-1 = ZFC + A. Giving it up is one choice, and A is the second choice. What is A? A is taking a result that can only be reached through an infinite number of steps, and exists on that account, as an already existing result, and letting it take part in computation."

Some of A's guises: reading the limit of 1/2 + 1/4 + 1/8 + … as "these infinitely many steps have already been walked"; holding that for every sequence that rises and has an upper bound, the endpoint is already lying there, ready-made; taking a whole that would take infinitely many levels to confirm as a ready-made thing handed over at once. The passage at the top says that the mathematical community “实际使用的不是ZFC，而是ZFC-1” ("actually uses not ZFC but ZFC-1"). Our reading: ZFC-1 is not another set of axioms but the way mathematicians use ZFC; A lives in words like "exists", "solved", "completed".

The computer has checked two things:

- **ZFC can see; it just sets no gate.** ZFC can say which questions are decidable and which are not, yet it never uses "can it stop?" as a threshold for accepting that something exists. There are always processes that never stop, for which ZFC can confirm at every moment "not stopped yet" but cannot prove "it never stops"; there are infinitely many such processes, and no patching ever finishes them.
- **The two choices are one principle.** At the simplest level, "the outcome of every infinite search is already settled" and "for a sequence that rises and has an upper bound, the endpoint exists ready-made" imply each other. Written with natural numbers, with rational numbers, or in the HoTT proof checker, it is the same, and none of it relies on the "either–or" law of excluded middle. We read the first sentence as giving up the gate and the second as choosing A.

### A gave mathematicians what they wanted: Zeno "solved"

ZFC itself proves Zeno's two sentences (checked by computer): in the sense of limits, it has arrived; no step really gets there. The number that is the limit (1) does not itself need A; it is given by a formula. What needs A is reading the first sentence as "these infinitely many steps have already been walked". The two problems of Zeno that the initiator distinguished (section 2) fall into place here: A declares the walk finished; "endless divisibility" makes it unfinishable.

### The same act gave, in HoTT, the B nobody wanted

What section 4 describes is the B at the top of the page. The initiator later restated it (2026-10-15, original words, excerpt):

> ZFC-1=ZFC+A，A是一个数学便利，对应了芝诺悖论被认为经由极限理论解决了。而我们在main分支上的HoTT上的工作，暴露了ZFC-1的不合理。

> **Translation.** "ZFC-1 = ZFC + A; A is a mathematical convenience, corresponding to Zeno's paradox being considered solved by the theory of limits. And our work on HoTT on the main branch exposed the unreasonableness of ZFC-1."

The same act, taking a whole that would take infinitely many levels to confirm as ready-made, grows in the universe of HoTT, together with univalence, into "whether things are the same can never be finished asking"; take away either one, and the questioning stops (section 4). "The same act on both sides" is a reading the initiator has accepted; formally they are two different principles, and the one in HoTT does not need the law of excluded middle used on the ZFC side.

### What A costs

The initiator said (2026-10-14, original words, excerpt):

> 也就是说，ZFC-1对现实的否定，与其说在于Q，不如说在于A。它是一套反现实的逻辑系统。
>
> 逻辑学，在起点上，就是对现实和对应的思维过程的抽象，ZFC-1这个反现实的逻辑，不仅仅在现实中是无法完成A的，而且在思维中，必然产生我们重新复活和新找到的悖论。

> **Translation.** "That is to say, ZFC-1's denial of reality lies not so much in Q as in A. It is an anti-real logical system.
>
> Logic, at its starting point, is an abstraction of reality and of the corresponding thought processes. ZFC-1, this anti-real logic, not only cannot accomplish A in reality, but also, in thought, necessarily produces the paradoxes that we have revived and newly found."

Missing Q only means not asking; A, however, is a positive assertion: a result that no process can deliver is already there.

**In reality it cannot be done.** The computer has checked two things:

- Classical logic says every search has a "settled outcome"; yet no program can deliver that outcome for every search. That not everything can be decided does not itself rely on excluded middle either: no program can recognize exactly the processes that "never stop".
- In a world whose points have a size, that is, in quantized time and space, every approach arrives within finitely many steps, and infinitely many steps cannot be squeezed into a finite time.

**In thought it produces paradoxes.** Zeno and the ring have been revived (section 2); the thing in HoTT has been newly found (section 4).

**The theory is caught by itself.** This part follows Gödel, to think the problem through more deeply. Late on 2026-10-14 the initiator said (original words):

> 我刚刚那份表述，是关于ZFC不判定“是否可以停机”这件事的，也是关于ZFC-1选择“将无法停机的过程的理想型目标作为数学的现实存在物进行运算”的。
> 而哥德尔不完备也是关于不可停机的讨论的。

> **Translation.** "The statement I just made is about ZFC not deciding 'whether something can halt', and also about ZFC-1 choosing 'to compute with the ideal target of a process that cannot halt as an object that really exists in mathematics'.
> And Gödel's incompleteness is also a discussion about not being able to halt."

The computer has checked three things on real ZFC (the formalization of ZFC comes from Lean's Foundation library):

- **The devil's bargain.** A theory that can be checked mechanically and can verify finite computations, once it swallows the rule "infinitely many steps have already been walked", proves of one and the same program both that it stops and that it never stops; to avoid contradicting itself it can only give up being mechanically checkable. The last two sentences of the passage at the top say that the devil wants the "soul", and that the soul of mathematics is mathematical truth.
- **The share the devil takes.** ZFC uses A everywhere, except on itself. Let ZFC search again and again for its own contradiction: at every moment it can confirm "not found yet", but it cannot prove "never found". This is Gödel's second incompleteness theorem, here checked by computer on real ZFC.
- **A runner who really reaches the end.** There is a runner who at each step covers half of what remains, whose position is less than the end at every moment, and who in the sense of limits really arrives; ZFC confirms at every moment that it is still running, yet cannot prove that it has arrived.

### Back to the premise

The passage at the top says (original words, excerpt): “当我们回溯这种不合理性的来源，相当于反证法得到了矛盾之后对前提的回溯，我们就会找到P” ("when we trace this unreasonableness back to its source, which amounts to tracing back to the premises after a proof by contradiction has reached its contradiction, we find P"). The initiator later explained what "contradiction" means here (2026-10-14, original words):

> 我说的“矛盾”，是不是“理论推出的结果与现实相矛盾”（反证法里的那个），而不是形式上推出 ⊥。

> **Translation.** "The 'contradiction' I speak of — is it not 'the result derived by the theory contradicts reality' (the one in a proof by contradiction), rather than formally deriving ⊥?"

The sentence has the form of a question; on 2026-10-15 the initiator explained that it is a confirmation. "⊥" is the logical symbol for "false". P and A are two names of one act: seen from the convenience it buys, it is A; seen from what it is (anti-real, non-computable), it is P. This is the equation in the passage at the top, “设ZFC-1=ZFC+A，则ZFC-1=ZFC+P” ("let ZFC-1 = ZFC + A; then ZFC-1 = ZFC + P").

The defendant is that act. On the HoTT side the initiator named the "ready-made collection" as the defendant (section 4); on Zeno's side, A declares the walk finished, and "endless divisibility" makes it unfinishable.

### What it is not

- We do not say that ZFC contradicts itself, and we do not derive "false" from ZFC.
- "Necessarily produces paradoxes" is the initiator's thesis, not a theorem. What the computer gives are instances: Zeno, the ring, the thing in HoTT.
- "The same act on both sides" is a reading the initiator has accepted; formally it is two principles.
- "Reality is quantized and completes by jumps" is the initiator's judgment about reality. Mathematics proves what happens when points have a size; it cannot prove that reality is like that.
- There are a few bridges of interpretation, and machine proof cannot prove the bridges themselves: "a process has completed" means "the computation has stopped"; the "time dimension" means running step by step; the "gate" means the termination requirement on recursive definitions.
- These mathematical facts are mostly known: the theorems of Gödel and Turing, the research in constructive mathematics on how such principles imply one another, the collapse of systems without a termination check. What is new is reading them sentence by sentence next to the initiator's words. This reading has not yet been checked thoroughly against the literature.

The sentence-by-sentence correspondence between the initiator's original words and the machine proofs is in [«The problem of ZFC-1: the original words sentence by sentence against machine proofs»](docs/ZFC-1的问题-原话逐句对照与机器证明-20261015.md) (in Chinese).

## 7. Another trail: infinite coherence

Before finding what is described above, we followed another Zeno-like trail for a while. HoTT has something called a "semi-simplicial structure": a shape glued together level by level from points, segments, triangles and tetrahedra, with the requirement that the "faces of faces" fit together. In a world where sameness is a fact, it can be defined in one line; in HoTT, every time a level of "fitting together" is added, a requirement at the next level grows out of it. Every finite level can be written down (checked by computer up to level 5), but a single definition that covers all levels at once has not been found by anyone so far. This has been a well-known open problem for more than ten years; that it cannot be done has not been proved either. The full account is in community audit paper 01.

**A correction about names.** The title of community audit paper 01, the phase-close report and the previous version of this README all used the phrase "the ghost of Zeno's paradox" for the infinite-coherence trail. On 2026-10-01 the initiator clarified that the phrase refers to the ring paradox together with the repository's later discussion and analysis of it (original words, excerpt):

> 我认为，圆环悖论和我们这个repo中对其的进一步的讨论、分析，复活了芝诺悖论的幽灵。

> **Translation.** "I think the ring paradox and the further discussion and analysis of it in this repository revived the ghost of Zeno's paradox."

Section 2 already tells the ring story in plain language. Infinite coherence is a separate Zeno-like candidate proposed by the project AIs, not the referent of the 2026-09-27 verdict. This edition corrects community paper 01 and the attribution in the phase-close report; A7's machine evidence and its open uniform-definition question remain unchanged.

## 8. How to check us

We hope you will not take our word for it, but check for yourself. There are three levels at which to review:

1. **Is the mathematics right?** Every positive claim has been checked step by step by a proof checker : Cubical Agda 2.8.0 with the cubical library v0.9; Lean 4.34.0, where many claims of sections 2 and 6 also use Lean's standard mathematics library Mathlib and the Foundation library, which writes ZFC down in Lean (both fixed at definite versions). Key claims also come with "negative controls": deliberately wrong proofs that the checker must reject, to make sure the check really checks. All claims, their evidence and the limits on extrapolating from them are in [`CLAIMS-EN.md`](CLAIMS-EN.md) (an AI translation of [`CLAIMS.md`](CLAIMS.md)); the proof sources are in `HoTT/formal/`, and the `CLAIM.md` of each proof package gives the full statements; the run receipts are in `HoTT/verification/runs/`, {{RUN_TOTAL}} in all: {{RUN_ACCEPTED}} accepted and {{RUN_REJECTED}} negative controls rejected as expected.
2. **Do the claims say what the text says?** Do the formal statements say what the prose says? For example, is "questioning level by level" a fair way of making "deciding whether two things are the same" precise? For this level, read the community audit papers: [03, "HoTT's Zeno"](docs/社区审计提交/03-HoTT的芝诺-EN.md) (the shortest, ending with five audit questions), [02, "The ghost of Russell's paradox"](docs/社区审计提交/02-罗素悖论的幽灵-EN.md), [01 (the infinite-coherence trail)](docs/社区审计提交/01-芝诺悖论的幽灵-EN.md), and [the phase-close report](docs/HoTT悖论查找阶段收尾报告-20260930-EN.md). For the ZFC-1 of section 6, read [«The problem of ZFC-1: the original words sentence by sentence against machine proofs»](docs/ZFC-1的问题-原话逐句对照与机器证明-20261015.md) (in Chinese): the initiator's original words, sentence by sentence, against the mathematics written for them and what the computer has proved, marking which sentences were never meant to be theorems.
3. **Does the reading hold up?** Is that thing really "simple"? Is the changed condition "sameness can be divided without end"? Can a standard answer such as truncation make it go away? Is A really the defendant? Should the gate "first ask whether it can stop" be placed at the level of "existence"? These are questions of the philosophy of mathematics, and objections are welcome.

### How to replay

Install Agda 2.8.0, cubical v0.9 and Lean 4.34.0, and prepare a built Foundation (commit `1fb01b72` of FormalizedFormalLogic/Foundation; run `lake exe cache get` and `lake build` there; it pins Lean 4.34.0 and Mathlib `5ed29652`); then run from the repository root:

```sh
python3 tools/replay.py --agda /path/to/agda --cubical-lib /path/to/cubical/cubical.agda-lib --lean-sysroot /path/to/lean-4.34.0 --foundation-root /path/to/Foundation --jobs 4
```

Without `--foundation-root`, the runs that use Mathlib or Foundation are reported as SKIPPED; the others are replayed as usual.

It rebuilds the command of each run receipt, runs it, and compares the result with the receipt: the outcome (accepted or rejected) must agree, and the output is compared line by line after the repository path and the library paths are replaced by placeholders. A negative control passes only if it is rejected again; if its output also agrees, it was rejected for the recorded reason. To replay a single receipt: `--only <run id>`; to list them all: `--list`. Replaying everything one after another takes about two and a half hours. Run receipts contain absolute paths from the machine that captured them, so they cannot be copied unchanged to another machine. For ordinary replay, use `tools/replay.py` on this branch. Readers who need a byte-for-byte comparison with the original scripts can optionally use the [research-line replay script]({{REPO}}/blob/dev/.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py) and the [audit-line replay script]({{REPO}}/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/tools/verify_copus_run.py), preserved on `dev`. These are technical tools for deeper review, not a prerequisite for ordinary reading.

The toolchain records cited by the receipts are in `HoTT/formal/dedekind-omega-missile/` (Agda on macOS), `HoTT/formal/claude-cg001/pedometer-ablation-lean/` (Lean on macOS) and `HoTT/formal/cloud-opus-glm-audit/` (Linux); the first two directories keep their location on `dev` and hold only these records on this branch. Packages that use Mathlib or Foundation also have, in their own directories, `LEAN_TOOLCHAIN.json` and `MATHLIB_CLOSURE.json`, which record the Lean files used at the time and the hash of every dependency module. [`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json) records the SHA-256 of each of the {{FILE_TOTAL}} files on this branch and the `dev` commit they come from.

## 9. How this research was done

The research question, the view of paradoxes and the philosophical judgments come from the researcher. Several AI systems helped turn ideas into precise claims, check proofs and review one another's work. The claim files, proof sources and run records on `main` show which mathematical statements were checked by computer.

Original conversations, AI working notes, audit exchanges and exploratory paths that were not adopted remain on `dev` as a record of how the work developed. Those records are not themselves mathematical proof and are not required reading for understanding the conclusions here. Readers who want the detailed trail can start at the [`dev` README]({{REPO}}/blob/dev/README.md), which points to the fuller history and technical records for deeper review or handoff.

## 10. About this branch

- `main` (this branch) holds only what supports the conclusions: the conclusion documents, precise claims, proof sources, run receipts and a way to replay them. It is generated from commit [`{{SOURCE_SHORT}}`]({{REPO}}/commit/{{SOURCE_COMMIT}}) of `dev` according to a manifest (`scripts/release/build_main_release.py` and `scripts/release/main-release-spec.json` on `dev`), and is not edited directly. To update it, change the manifest or the conclusion documents on `dev` and generate it again.
- `dev`: the whole research process; all work happens there.
- This README also exists in Chinese, Russian, German and French with the same content. The community audit papers and `CLAIMS.md` are also available in these four languages; the translations are AI translations, and the Chinese text is authoritative. «The problem of ZFC-1: the original words sentence by sentence against machine proofs» exists only in Chinese.
