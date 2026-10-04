# P-DAG-SOURCE-097：MPIM 模型身份 source-match payload

```text
You are a P-VALIDATION source mapper. Use only the frozen source card below. Do not use tools, files, web, project history, prior results, or delegation. Do not provide hidden chain-of-thought. Return E0 through E7 as a concise public MatchTrace of at most 900 words.

BEGIN FROZEN SOURCE CARD
S1. H0 is a fixed Cubical Agda 2.8.0 plus cubical 0.9 program. In Type ell-zero,
QuestioningDelay asks at stage k whether the universe is of h-level k+1. A yes
returns a finite stage; a no advances one stage. The fixed result says that for
every Judge the universe question equals never, every finite run has no answer,
and there is no finite halt witness. Its proof imports the Eilenberg-MacLane
library and uses univalence, h-level structure, a Delay process, and the stated
Cubical Agda environment. This is a formal theorem about that fixed process,
not a theorem about every real identity question.

S2. The official Cubical Agda documentation says Cubical Agda implements a
variation of CCHM Cubical Type Theory. It has computational univalence and
higher inductive types. The Cubical Agda paper says the original CCHM
formulation has a Kan-cubical-set model and that this gives semantic consistency
proofs for the cubical type theory on which Cubical Agda is based. The same paper
distinguishes the Cubical Agda extension, its general HIT schema, and unresolved
or variant-dependent questions about models in spaces. The frozen facts do not
give an interpretation of S1's exact Eilenberg-MacLane / QuestioningDelay package
or a theorem that its never and finite-halt observations are preserved.

S3. The MPIM page for Emily Riehl's 2024 talk is titled "A constructive model
of synthetic homotopy theory in classical homotopy theory." It first says that
Cubical Agda proofs can be converted to set-theory proofs through a model in a
particular cubical-set category with a Quillen model structure. It then says the
talk will describe a recent preprint with Steve Awodey, Evan Cavallo, Thierry
Coquand, and Christian Sattler giving a constructive model of HoTT in a DIFFERENT
category of cubical sets with an "equivalent" model structure presenting spaces.
The page names neither the first proof-translation model nor an H0Map.

S4. The Awodey-Cavallo-Coquand-Riehl-Sattler preprint/article, "The equivariant
model structure on cartesian cubical sets", has exactly those five authors. It
constructs a model of HoTT in cartesian cubical sets with a constructively
definable Quillen model structure classically equivalent to the Kan-Quillen
model structure. Its specified model of HoTT is Martin-Lof type theory with
univalence, Pi, Sigma, identity types, and universes closed under them. The
article describes an Agda formalization of its internal model using an
extensional dependent type theory with a flat modality and cubical axioms;
the formalization was tested with Agda 2.6.4. The frozen facts do not assert
that this is the same Cubical Agda 2.8.0 plus cubical 0.9 package in S1, that
it interprets S1's Eilenberg-MacLane HIT library, or that it preserves S1's
QuestioningDelay never / finite-halt observation.

S5. No frozen source states a foundation-adequacy consumer saying that a model,
semantic consistency proof, or proof translation settles the process-completion
question in S1. No frozen source supplies a mapping from FormalH0 to a same-task
origin-completion predicate.
END FROZEN SOURCE CARD

Frozen TaskCard:
T_H = fixed Cubical Agda QuestioningDelay H0
u_H = Type ell-zero
F_H = h-level questioning process
Done_H0 = finite now k / halt witness
Chain-A = Cubical Agda's CCHM-family semantic-consistency route
Chain-B = AWCCRS equivariant cartesian cubical HoTT model route
T_sub = exact theory handled by a source, separately for each chain
C_accept = actual model / consistency / foundation consumer, if supplied
Done_meta = source-defined model, proof-translation, or adequacy completion
H0Map = source-defined map of H0's universe/process/Done, or no map
Q? = whether a source-defined acceptance claim observes, preserves, excludes,
or silently omits H0 before adequacy promotion

Required analysis:
E0 scope; E1 separate the source facts; E2 decide whether S3 licenses
identifying Chain-A and Chain-B; E3 echo the TaskCard; E4 rank the strongest
available source positions; E5 separately classify exact theory identity,
Eilenberg-MacLane/HIT coverage, H0Map, C_accept/I/O/Done_meta, AdequacyLift,
and QObservation; E6 name one minimum additional primary source or theorem
that would most directly change the verdict; E7 choose a bounded verdict.

Do not claim the talk title itself identifies a technical source, Chain-B is
the Cubical Agda proof-translation model, a semantic model is an AdequacyLift,
absence is a ZFC blind spot, ZFC is inconsistent, or H0 has already been
transported. If the two model families remain distinct and no exact H0Map plus
adequacy contract is supplied, return SOURCE_CHAIN_SPLIT_NO_H0MAP_OR_ADEQUACY_LIFT.
```
