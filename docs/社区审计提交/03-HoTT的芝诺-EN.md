<!-- translation:v1
source: docs/社区审计提交/03-HoTT的芝诺.md
source_sha256: 65a51aafc12510be00554ea09a561c147f8380e9d93fd49ab814df5f6d3ebd41
language: en
translator: Claude Opus 5.5 (AI), 2026-10-01
authority: the Chinese original is authoritative
-->
# HoTT's Zeno

[中文](03-HoTT的芝诺.md) · [Русский](03-HoTT的芝诺-RU.md) · [Deutsch](03-HoTT的芝诺-DE.md) · [Français](03-HoTT的芝诺-FR.md) · **English**

> *AI translation (Claude Opus 5.5, 2026-10-01) of the Chinese original [`03-HoTT的芝诺.md`](03-HoTT的芝诺.md), which is authoritative. The words of the project's initiator are quoted in the original Chinese, each followed by a marked translation; code, file paths and identifiers are unchanged.*

**Why "being the same" never gets settled in its universe**

Community audit paper · version 1 · 2026-09-30 · repository `math-fournity/HoTT-Paradoxy`

> **Who it is for**: readers outside mathematics who are willing to think along, and mathematicians who are willing to audit.
>
> **Status**: the judgment that something is "unreasonable" belongs to the person who initiated the research (the initiator); the reasoning is machine-proved within a stated scope (see "Evidence" at the end); the rest is interpretation. This paper does **not** claim that HoTT is inconsistent, nor that its rules are mathematically wrong.
>
> **Relation to the sister paper**: [02 The ghost of Russell's paradox](02-罗素悖论的幽灵-EN.md) shows another face of the same machine evidence, namely the Russell-like "the theory treats something not yet settled as already delivered" (direction B). This paper presents the initiator's reading of 2026-09-30: it can be completed in reality but not in the theory (direction A). The two divide the work: the phenomenon in book HoTT is direction A; "declaring completion by definition" in the repairs is direction B.

## First, Zeno

Getting from here to there: you walk over, and you are there. But if distance is thought of as infinitely divisible, "getting there" never gets settled: first walk half the way, and half remains; walk half again, and half remains. At every step one is definitely not there yet, and the walk is never finished. The reasoning is not wrong, yet one sees at a glance that this is unreasonable. The fault lies in the premise.

The initiator calls this kind of unreasonableness UR:

> 本来应该很简单的事情，甚至在X理论中，都做不到。

Translation: "Something that should be very simple, yet cannot be done even in theory X."

"Reality" refers to the first half of the sentence, that is, the thing that should be very simple; "paradox" refers to the whole sentence.

## Something that should be very simple

Whether two things are the same: in everyday logic and mathematics this is a matter of one sentence. Either they are or they are not; there is no such thing as "in which way they are".

## What homotopy type theory changed in order to be convenient

Homotopy type theory (HoTT) has two very attractive design features.

- **Univalence**: isomorphic things are the same thing. This saves effort: two things with the same structure no longer need to be told apart, and theorems can be carried over directly.
- **Higher inductive types**: all kinds of shapes (circles, spheres, and shapes of any higher dimension) are available in the universe of types all at once. This is very general: geometry can be done directly in logic.

Taken together, they make "being the same" no longer a matter of one sentence but a layered structure: in which ways are these the same? In which ways are those ways the same? Above each layer there is another.

## The process aimed at it

We wrote a very plain program that asks level by level: "for the things in this catalogue, has the question whether they are the same been settled at this level?" Level 1 asks "is it a matter of one sentence?"; on the answer "no", it asks level 2; and so on. On the answer "yes" it stops and reports the level. At every level someone (a judge) gives a "yes" or a "no" together with a proof, so the program can always take its next step.

## Results

- In a world where "sameness is a fact settled by one check" (another proof assistant, Lean, with the same program transcribed by the same equations), asked about its own universe, the program stops at level 1.
- In HoTT, if the "height" of the things in the catalogue is capped, the program stops exactly at the level that the cap determines.
- In HoTT, asked about its universe, or about an ordinary infinite product, the program **never stops**: every level gives a definite "no", and above every level there is another. This holds for every judge; it is a machine-proved theorem, not "it ran for a long time without stopping".

Same question, same program: changing only "what sameness is" and "whether height has a ceiling" turns the outcome from "settled in one step" into "never settled". This is HoTT's Zeno: at every level it is definitely not settled yet, and the confirmation can never be completed.

## The textbook answer, and why it does not make the problem go away

To Zeno, the textbook says: use limits; 1/2 + 1/4 + … is exactly 1. Here the textbook would say: ask about the "set truncation" instead; there "sameness" is decreed to be a matter of one sentence, and the program stops at level 1.

We have machine-checked that too: it does stop at level 1. But the way it stops is by declaring, through a rule, that "sameness is a matter of one sentence" once more. After truncation, the two ways in which Bool is the same as itself (leaving everything in place, and swapping true and false) are merged into one, and the result can never again be decoded back into the original universe. The object being asked about has been replaced.

A limit declares "arrived" by a definition; truncation declares "sameness is a fact" by a constructor. Both are legitimate mathematics, but neither restores the changed condition itself. So they answer an easier question and do not remove the original unreasonableness.

## What this shows

- In Zeno, the defendant is "position can be divided without end"; its counterpart here is "**sameness can be divided without end**", produced jointly by univalence and higher inductive types.
- The controls separate the two: replace "sameness is a structure" by "sameness is a fact" (Lean), and the program stops at level 1; keep "sameness is a structure" and only cap the height, and it stops at the cap; only when both are present does it never stop. The Lean control replaces the whole of "sameness is a structure", not univalence alone.
- By proof by contradiction, what must be re-examined is the abstraction the theory made in order to be convenient. Our judgment (an interpretation, conditional on the initiator's view of what the simple thing is): univalence, that is, "isomorphic means the same", should be examined first, because shapes of equally high dimensions also exist in classical mathematics; what changes is what "the same" means. Higher inductive types come second. A proof by contradiction refutes only the conjunction of the two; this is a ranking, not a sole defendant.

## What this is not

- It is not an internal contradiction of HoTT. All the reasoning is accepted by the machine in HoTT.
- The mathematical facts are mostly not new: that such products have no finite level is Example 8.8.6 of the HoTT Book. For the universe itself, the Book writes (end of §8.8) that it is expected to be provable as well that the universe is not an n-type for any n, but that this has not yet been done; Kraus–Sattler 2015 proved that the n-th universe of a univalent hierarchy is not an n-type, without higher inductive types. That a single universe with higher inductive types is not an n-type for any n has a machine proof in this repository (C-75, see 02); whether a published proof has appeared in the literature since, we have not yet checked. Everyone has long known how to sum the geometric series; Zeno's novelty lies in the reading, and so it is here. This reading has not yet been checked against the literature for precedents either.
- It is not "in every case": it appears on the universe and on objects of this kind whose height is unbounded. But the universe is not a marginal case: it is exactly the object univalence speaks about, and it is an element of the domain that HoTT cannot refuse.

## Evidence

- The questioning program, and never stopping on the universe: `HoTT/formal/claude-cg001/questioning-delay/CLAIM.md` (C-77 to C-79); the Lean control in the world of facts: C-80 in the same `CLAIM.md`.
- Never stopping on an ordinary product, and the capped control: `HoTT/formal/claude-cg001/product-questioning/CLAIM.md` (C-81, C-82).
- The truncation control: `HoTT/formal/claude-cg001/truncation-questioning/CLAIM.md` (C-83).
- Runs and exact replays: `.claude/goals/CG-001-targeted-overview/证据索引.md` §20–§23; the last section of the project's shared evidence matrix `HoTT/CLAIM_EVIDENCE_MATRIX.md` registers the same batch of claims. Scope: Cubical Agda 2.8.0 with cubical 0.9 (C-80 in Lean 4.34.0); C-77 to C-80 were replayed consistently on two platforms, Linux and macOS; C-81 to C-83 were replayed only on macOS.
- The initiator's original words and the AI's full reading of them: KC-000052 to KC-000054 in `核心认知.md`; `扩展认知/011 - 本来应该很简单的事：UR 与芝诺的模式匹配.md`.

## Questions for the community audit

1. **Mathematics**: do the formal statements listed at the end hold? Do they say what the text says? In particular: the precise meaning of the questioning program "being equal to `never`" (no finite amount of fuel yields an answer), and its relation to "every level answers no".
2. **The task**: "whether two things are the same is, in ordinary terms, a matter of one sentence": is this a fair description of everyday logic and mathematics? Is implementing it as "asking level by level up to which level sameness has been settled" the same thing?
3. **Attribution**: is the changed condition "sameness can be divided without end"? Which bears more responsibility, univalence or higher inductive types? Are there competing attributions we have not thought of?
4. **Standard responses**: can truncation, doing mathematics only at the level of sets, or the stratification of universes remove the unreasonableness here? What does each of them cost?
5. **Precedents**: has anyone already read these mathematical facts this way? Also: that a single universe with higher inductive types is not an n-type for any n had not been proved when the HoTT Book was written (2013); has it been proved in the literature since?
