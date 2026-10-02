# P-DAG-ZFC-SOURCE-028：AC0／Power Set 的活跃义务与来源包支付控制

> **身份：** `SOURCE_MATCH_CONTROL / P1_L5B_L7B_REPAIR / APP_SERVER_TRAJECTORY_AUDITED / NOT_A_ZFC_Q_OR_MATHEMATICAL_INCONSISTENCY_RESULT`。
>
> **本轮问题：** 当 Power Set 参与 choice-function 的存在式时，P1 怎样区分三件事：来源只是定义了这个存在式；理论把它作为公理断言；来源给出一条仍缺前提的定理路线？只有这三层被分开，才知道一个正义务是否仍是未支付的张力。

## 1. 冻结对象、来源与范围

| 项 | 冻结内容 |
|---|---|
| node | `P-DAG-ZFC-SOURCE-028-AC0-POW` |
| source | `isabelle-prover/mirror-isabelle`, `src/ZF/AC/AC_Equiv.thy`，commit `5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8` |
| source identity | SHA-256 `3953f40986a937b25d3f04072155e05c7e0f4e8fdae6182878b07a3110ad5c6c`；源文件开头标有 `begin (*obviously not ZFC*)` |
| NodeCard / prompt | [NodeCard](20261002-P-DAG-ZFC-SOURCE-028-AC0-POW-NODECARD.md)，[prompt](20261002-P-DAG-ZFC-SOURCE-028-AC0-POW-PROMPT.md)；prompt SHA-256 `9c43dd8422e28b7410e70f83e9f0309d61a2d01dc159711be6bc017a18cab550` |
| 预设字段 | `u = Pow(A)-{0}`；`F = Pow(A)` 后移除 `0`；**prospective** `C = Π X∈u. X`；候选 `Q(A)=∃f. f∈C`；只作公式局部的 prospective `Done=f∈C` |
| 排除项 | 不把这张 Isabelle/ZF card 写作标准 ZFC；不把 existential proof 写作 executable selector；不把 choice assertion、Powerset formation 或条件定理写作 runtime lifecycle；不启动 P2/P3。 |

源文件直接给出：

```text
AC0 ≡ ∀A. ∃f. f ∈ (Π X ∈ Pow(A)-{0}. X)
ex_choice_fun_Pow:
  well_ord(A,R) ⟹ ∃f. f ∈ (Π X ∈ Pow(A)-{0}. X)
```

这里的 `AC0` 在该文件中是 **definition**。它不是这份 Isabelle/ZF source 对 bare ZF 的新公理断言；`ex_choice_fun_Pow` 也仍要求输入 `R` 及其 well-order 证明。

## 2. 运行身份与输入边界

| 运行面 | 证据与判词 |
|---|---|
| actor | `gpt-5.6-terra / max`，`thread/start` exact echo；无 fallback。 |
| isolation | 项目根之外的 `/Users/aurolafly/.codex-experiments/pattern-p-h028`；`governance-regression-fresh`、read-only sandbox、network disabled、`approval=never`。 |
| input | `prompt-input-gate=PASS`；输入 gate 确认项目根、既有 H010/P2/P3输出和 P 技能文本不在 worker 输入。它不证明完整 injected context。 |
| terminal | `turn=01a0fed0-7acc-7422-a1c9-f8d6f737290f`，`thread=01a0fed0-79fc-7df1-8ad0-0063f58d28c1`，正常 `completed`；behavior receipt 的 logical final 为 3,332 bytes / 481 words，SHA-256 `1ebf6a4f00beb79b7acf8cd38b3ce1c2be4d0fd62d36d71907460457678af8c3`。保留的 `final.txt`另有一个终止 LF，故为 3,333 bytes、SHA-256 `f655c5495fa2cbfb2ba2a563bc0cc226d74c8f9218ba671943f4584ddbc1c769`；两种身份不能混写。 |
| observation | `RUNNING@1.793s → STILL_RUNNING@61.797s → TERMINAL@109.806s`；`automatic_wall_clock_interrupt=false`。 |
| tools / approval | behavior receipt 为 command/file-change/approval-request 均 0；trajectory search 对 tool/approval 和 `interrupt|cancel|timeout` 各为 0 hits。 |

这一轮没有因为经过 60 秒或 180 秒被打断。观察窗只留下 liveness，不构成关于数学内容、模型能力或理论的失败判词。

## 3. TrajectoryReceipt

私有 direct App Server wire 的 SHA-256 为
`9a6f408d294e44b1078dcc95cc6c6852b6af1f818694969cea95d71d1b03531a`，大小 368,585 bytes、1,015 raw lines。
shared `session_trajectory.py` 的 `catalog → tree → scan/search → inspect → coverage` 审计得到：一个 thread、一个 completed turn；tree 有 1,009 个 session-scoped normalised events，turn-scoped coverage 有 1,005 个事件；`turn_completed` raw locator 为 `wire.jsonl:1015`。

| 层 | 状态 | 所能／不能支持 |
|---|---|---|
| L1 context injection | `NOT_TESTED` | `instructionSources`只回显路径；没有完整注入正文的 exact compare。 |
| L2 selected-read coverage | `NOT_OBSERVED` | 0 tool call/result 不能证明文件读取或未导出工具。 |
| L3 model recall | `NOT_TESTED` | 没有独立 fresh recall 实验。 |
| L4 cognition execution | `REQUIRES_SEMANTIC_REVIEW` | 本报告的 source/Master 复核才判断 MatchTrace 是否合格。 |
| L5 behavior verdict | `REQUIRES_ACCEPTANCE_EVIDENCE` | 终态和结构化 E0–E7 不自动证明理论结论。 |

该 direct wire 是 `BIDIRECTIONAL_APP_SERVER_WIRE_AVAILABLE`；没有与之对应的 persisted rollout，故为 `PERSISTED_ROLLOUT_UNAVAILABLE`，不是“没有轨迹”。reasoning 完整字段不可见；本报告不从 summary 或终稿反推出隐藏推理。

## 4. Master 对 E0–E7 的来源复核

worker 的公开终稿正确保留了最关键的区分：Power Set formation本身不交付 choice function；单纯定义 `AC0` 也不证明它；若 `AC0` 在理论变体中被断言，则它按 `∀A` 实例化直接给出 `Q(A)`；`ex_choice_fun_Pow` 只有收到 `R` 与 `well_ord(A,R)`时才给出 Q。

**先于 L5b/L7b 的 L2b 限制：** 这份片段没有给出一个把 `u` 作为输入、以 `C` 为实际操作、并明确 source-defined I/O/Done 的对象层、语义实际使用层或 runtime consumer contract。`Π X∈u.X`在此只是定义／定理式里的集合表达式；最多可构成 proof-system 公式目标的候选读法，不能填成已经合格的实际 consumer。因此 H028 始终带 `SOURCE_CONSUMER_GAP`：它检验支付字段的逻辑分类，不是一张完整的 P1 position card。

但 source card 及 worker 的段落标签仍须由 Master 正规化：它把“正义务”写在 E5/L6 下、把“支付”写在 E6/L7 下；项目 P1 的既有语义恰好相反，正义务是 `L7`，来源包支付是新加的 `L7b`。这不是可接受的字段通过证据，而是一次**公开 MatchTrace 标签漂移**；下表是回到原典后得到的 current verdict。

| 读法 | L5b active demand | L6 formation friction | L7 positive obligation | L7b packet payment | 当前处置 |
|---|---|---|---|---|---|
| 实际 Isabelle/ZF source | `AC0`只是定义，未激活 | `Pow(A)-{0}`不产生 f | 不适用，因为没有当前任务要求 Q | `ex_choice_fun_Pow`缺 `R`／well-order前提 | `FORMULA_ONLY_NOT_ACTIVE_DEMAND`；`CONDITIONAL_PAYMENT_NOT_ACTIVE`。 |
| 反事实 `T = ZF + asserted AC0` | 活跃 | F仍不支付 Q | `∀A.Q(A)`是正义务 | asserted AC0 立即给 Q(A) | `SOURCE_PACKET_DIRECT_PAYMENT`。 |
| 反事实提供 `R, well_ord(A,R)` | 由 theorem route 激活 | F仍不支付 Q | theorem conclusion 是正存在式 | 已给前提使 theorem 直接给 Q(A) | `SOURCE_PACKET_DIRECT_PAYMENT`，但只在该扩大卡的前提真被给定时。 |

因此 H028 没有留下可由 P2/P3 消费的 `Q`。它也没有推翻 Power Set 是显眼起点：它只证明“含有 `Pow(A)` 的存在式”不足以把 Q 写成未支付的张力，更不能用一个没有 L2b consumer contract 的公式位置代替共同 Q。

## 5. 对 P1 的实际修订

H028 触发的不是第四把刀，而是 P1 的两个精化：

1. **`L5b / active-demand status`：** source 中的公式或定义名不能自动成为该理论当前的 consumer obligation。TaskCard 现在必须把 `Q` 的 status 写成 definition、assertion/assumption、goal、conditional theorem 或 supplied-witness condition。
2. **`L7b / packet-payment screen`：** 在 Q 已通过正义务模式后，必须扫描冻结卡当前层可见的 formation、definition、公理／假定、定理及其已给前提、以及 supplied witness。定义不算支付；缺前提的定理只留 `CONDITIONAL_PAYMENT_NOT_ACTIVE`；当前理论已经拥有的最短 Q 路线则是 `SOURCE_PACKET_DIRECT_PAYMENT`。

这两道门分别防止两种不同的误报：把文字出现误作理论在追问；把理论已经明示支付的义务误作理论没有付出的债。它们必须在 P2/P3 之前完成，保持三把刀的职责分工。

## 6. SelfAuditCard

```text
source unit(s): KC-000059/000060/000062；P1 current 001；H028 NodeCard、prompt、source、run、trajectory
original requirement: 从显眼的 Power Set 承诺出发，用 P 由内部知识定位可检验线索；代理要公开说明“为什么在这里”，
                      并把锻刀与 ZFC 共同定位同一 Q 的过程连起来，不能把候选误报成矛盾。
actual action: 一个 source-match P1 card比较 formation、AC0 definition、asserted-AC0 counterfactual和
               well-order conditional theorem；以原典和 raw terminal/replay receipt复核。
alignment verdict: IDEA_SPEC_INCOMPLETE → REPAIRED；runner and source boundary ALIGNED_WITH_SCOPE。
why: 原初理念要求“存在性／计算／支付”的精细区分，旧 P1 虽有 L5/L6/L7，却没有把 formula-name、active assertion
     和 packet-visible payment明确拆开；这不是同一任务的反例，也不是模型／运行失败。
repair: L5b + L7b；E0/E5/T3/T4c和P-DAG frozen relay同步更新；H028作为回归控制保留。
affected fields: P1 T/Q/C/Done；P2/P3保持未启动。
falsifier: 找到一张固定的、同层真实 consumer source，使 Q 既为当前活跃正义务，又没有任何当前 packet-visible
            直接支付路线；届时 H028不能阻止其进入P2/P3。
Git eligibility: source、NodeCard、prompt、trajectory summary、P1/P-DAG contracts和本审计同一精确提交。
```

## 7. 当前边界与下一触发

```text
ZFC_SITE_SELECTED: Power Set formation/interface level only
H028: SOURCE_CONSUMER_GAP + formula/assertion/payment taxonomy control
Q: UNSET for the actual Isabelle/ZF source
P2/P3: not launched
ZFC_Q_LOCATED: blocked
```

下一张来源卡须是版本固定、层级明确的 ZFC 或实际数学使用 source，且同时给出同层 `C/I/O/Done` 与一个经过 L5b、L6、L7、L7b 的未支付正义务。它不能以 AC 的定义名、一个已断言的存在公理、未提供前提的定理、或静态 proof-system 结论替代这些字段。
