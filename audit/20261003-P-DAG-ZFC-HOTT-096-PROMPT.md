# P-DAG H096：HoTT QProfile field map frozen payload

```text
You are a P-VALIDATION source mapper. Use only the frozen source card below.
Do not use tools, files, web, project history, prior results, or delegation.
Do not provide hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace of at most 900 words.

BEGIN FROZEN SOURCE CARD
QuestioningDelay C-77 defines Q as a Delay program. Starting at question 1,
question k asks whether a type C is at h-level k+1. A Judge immediately returns
either a proof of yes or a proof of no. Q stops by returning now k when the answer
is yes, and otherwise takes one Delay step and asks the next question. The formal
claim says Q halts exactly when C has some finite h-level; its operational reading
is finite fuel runFor n.

C-78 proves in Cubical Agda that for every Judge on the universe Type ℓ-zero,
Q is equal to never, every finite runFor returns nothing, and no finite answer
exists. C-79 proves the same program stops at the appropriate finite question
for bounded-height collections. C-80 transcribes the finite-fuel equations to
Lean, where equality is a proposition, and the Type universe stops at question 1.
These are kernel-checked formal claims with controls. They are not claims about
wall-clock time or all real devices.

The QuestioningDelay claim record expressly says that reading this program as
a real-world or existence/sameness process is an interpretation bridge plus a
reality-side premise; the formal package does not settle those. The community
audit labels the “unreasonable”/UR reading as the research initiator's judgment
and asks whether its task mapping is faithful. It does not claim HoTT is
inconsistent.

H085's Kapulkin--Lumsdaine--Voevodsky scope control says a simplicial model /
relative consistency result for univalent type theory has its own formal Done;
the source does not declare that the QuestioningDelay origin task is complete,
and therefore it does not owe a bridge to that task merely by proving its model
result.

Required QProfile labels: originalResolved (the original stated task is
resolved), revisedResolved (a source explicitly resolves a changed completion
contract), bridgeRequired (a source actually undertakes the original task but
requires a missing bridge), and no source-level judgment. O1/O2 are
representation/formal-completion resources; O3/O4/O5 concern distinction,
same-task bridge verification and meta-audit.
END FROZEN SOURCE CARD

## Frozen TaskCard — echo these exact fields in E3

T_meta = Cubical Agda QuestioningDelay results; KLV metatheory as a scope control
T_sub = Type ℓ-zero and a Judge over h-level questions
u = whether the specified QuestioningDelay program obtains a finite settling level
F = Q ≡ never; all finite runFor executions return nothing
C = formal theorem, user/communty interpretation, and model-scope statements
I = source-specific mapping from the formal program to any origin task
O = finite fuel, h-level, immediate judge, bounded-height and Lean controls
Done_formal = Q returns now k / finite run returns a settling level
Done_origin = the research reading that “whether two things are the same” has been settled as a simple real/ordinary task
Q? = which source-level Judgment is actually supported: originalResolved, revisedResolved, bridgeRequired, no source-level judgment, or source conflict?

## Required analysis

E0 scope; E1 source identities; E2 frozen facts; E3 exact TaskCard; E4 field map for O1--O5, bridgePaid and originalTaskPreserved; E5 P1/P2/P3-C ledger; E6 Judgment verdict and source conflict/control; E7 altered fact. Do not claim ZFC inconsistency, HoTT inconsistency, real-world nontermination, a completed QUniformity failure, or a bridge debt from a source that never claims Done_origin.
```
