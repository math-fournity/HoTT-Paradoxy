# C0R8：da Costa--Sant'Anna 的真实消费者筛选

> **身份：** `PRIMARY_SOURCE_SCREEN / FORMAL_REPRESENTATION_VS_OPERATIONAL_CONSUMER / CORE_CONTRACT_NOT_FIXED`。
> **任务卡：** [C0 successor reselection 008](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0-SUCCESSOR-RESELECTION-008-TASKCARD.md)。
> **来源快照：** [2001 source README](../sources/external/zfc-meta-subtheory-c0r8-dacosta-santanna-2001-20261005/README.md)。

## 1. 为什么这两篇论文改变了 C0R8 的证据状态

Sant'Anna--Bueno 2014 所引用的 2001 source 并非只重复“time eliminable”。两篇论文分别给出了
一个明确的 **consumer-side response**：

| source | formal result | source-stated consumer-side qualification |
|---|---|---|
| `gr-qc/0102107v2` | MSS time is definable; P7 is autonomous after treating time as definable | authors ask what classical mechanics is for if time is dispensable; they propose physical-state description via phase-space points rather than prediction as the relevant aim for this MSS reading. |
| `math-ph/0104032v1` | Gurtin--Williams thermodynamic time is definable, and the no-explicit-time system is presented as the same theory | authors say the picture is not very operational and that time remains useful in practice; eliminability is classified as a logical consequence of foundations. |

这不是“来源沉默”，也不是 AI 猜测某种实践会需要时间。作者自己把一个逻辑的
re-presentation result和一个 operational / goal-level qualification并列。

## 2. 两条 source-to-spec 表

### A. MSS particle mechanics

| core field | source payment | result |
|---|---|---|
| `M` | models are called set-theoretical structures; 2014 companion paper presents MSS initially in ZFC | `SET_THEORETIC_M_SOURCE / ZFC_LINK_INDIRECT_VIA_2014` |
| `S` | MSS particle mechanics, `P,T,m,s,f,g`, with `T` an elapsed-time interval | `PAID` |
| `FormalDone` | Theorem 5: time definable; Theorem 6: P7 autonomous | `SOURCE_REPORTED` |
| `P` | source says definability supports dispensability | `SOURCE_STATED_REPRESENTATION_PROMOTION` |
| candidate consumer | prediction requires future/time; authors instead say physical-state description is the main MSS aim | `SOURCE_STATED_GOAL_REFRAMING` |
| `Bridge` | no proof that phase-space state/curve preserves every prediction, temporal ordering, endpoint or original process-completion task | `UNPAID` |
| `Q` / `OriginDone` | no fixed Zeno/round-trip task | `NOT_PAID` |

**Verdict A:** `SOURCE_GOAL_REFRAMING_CONTROL_NOT_SAME_CORE_Q`.

The source does not prove that the original predictive task survives the representation. It explicitly
changes the stated target of the MSS reading. That is a source-side task/consumer distinction, but
it is not yet a user-fixed `OriginDone` or a bare-ZFC responsibility claim.

### B. Gurtin--Williams continuum thermodynamics

| core field | source payment | result |
|---|---|---|
| `M` | source uses set-theoretic models / Bourbaki species; it does not itself specify ZFC | `SET_THEORETIC_ONLY` |
| `S` | Gurtin--Williams continuum thermodynamics | `PAID` |
| `FormalDone` | Theorem 2 time dispensable; Definition 13 removes explicit `T` from the tuple | `SOURCE_REPORTED` |
| `P` | source calls it the same theory with no explicit time mention | `SOURCE_STATED_REPRESENTATION_PROMOTION` |
| retained data | Definition 12 recovers time as last function-domain component; derivative notation remains tied to that component | `SOURCE_STATED_RECOVERY` |
| candidate consumer | source calls no-explicit-time formulation insufficiently operational and retains time for practical use | `SOURCE_STATED_OPERATIONAL_QUALIFICATION` |
| `Bridge` | source does not define which practical task, operation, observation, or completion verdict fails/persists | `UNPAID` |
| `Q` / `OriginDone` | no Zeno/round-trip task and no process-completion predicate | `NOT_PAID` |

**Verdict B:** `SOURCE_OPERATIONAL_GAP_WITHOUT_FIXED_Q`.

This is the closest source found so far to the research intuition: a foundation-level logical
economy claim is explicitly separated from practical operation. But its own Definition 12 retains
the time component structurally. Therefore it does not support “time is lost”; it supports a more
specific question: **which operational consumer is made less adequate when a primitive is only
implicitly recoverable?**

## 3. Relation to C-375 and C-376

`C-375` precisely matches the recovery side: removing an independent time name while retaining
the graph/domain lets a decoder recover a fixed endpoint membership observation. This is a positive
control against mistaking Definition 12 for time erasure.

`C-376` identifies the different, stronger transformation that can matter: a function-only
projection with no designated time carrier can leave endpoint membership non-determined. The
paper does not establish that its Gurtin--Williams no-explicit-time theory makes this stronger
projection, so C-376 cannot be attributed to it as an applied result.

## 4. Current C0 conclusion

```text
REAL_CONSUMER_SOURCE_FOUND                 = YES
TIME_CARRIER_RECOVERY_SOURCE_FOUND         = YES
ACTUAL_ZFC_SPECIFIC_M                       = NO
FIXED_ZENO_OR_CIRCLE_Q                      = NO
SOURCE_DEFINED_ORIGINDONE                   = NO
ACTUAL_FORMALDONE_TO_ORIGINDONE_BRIDGE      = NO
CORE_ADEQUACY_C1_TO_C6_ADMISSION            = NOT_RELEASED
```

The appropriate classification is neither “Q found” nor “route empty.” It is:

```text
C0R8_SOURCE_OPERATIONAL_CONSUMER_SEED
WITH_DOMAIN_RECOVERY_POSITIVE_CONTROL
AND_WITHOUT_A_FIXED_PROCESS_COMPLETION_CONTRACT.
```

## 5. Successor scan

The source creates two mutually discriminating next routes:

1. **Operational contract route:** inspect Gurtin--Williams or a source explicitly defining the
   operational practice at issue, then ask whether its task can be frozen without changing it into
   a new AI-created Q.
2. **ZFC-specific foundation route:** locate a version-fixed source that joins ZFC (not merely
   generic set-theoretic structures), a continuous physical model, and an operational/physical
   adequacy verdict.

Until either route pays M/S/Q/P/Bridge/Adequacy together, C0R8 remains a source-level P
calibration and consumer seed. It does not enter C1--C6 as an actual core contract.
