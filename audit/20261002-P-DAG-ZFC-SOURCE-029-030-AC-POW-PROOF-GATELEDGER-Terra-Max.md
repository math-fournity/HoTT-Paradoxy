# P-DAG-ZFC-SOURCE-029/030：AC／Power Set proof-layer 支付控制与 Gate Ledger 回归

> **身份：** `P1_GATELEDGER_REGRESSION / PROOF_SYSTEM_PAYMENT_CONTROL / APP_SERVER_TRAJECTORY_AUDITED / NOT_A_ZFC_Q_OR_MATHEMATICAL_INCONSISTENCY_RESULT`。
>
> **问题：** P1 现在能区分“当前公式／义务是什么”与“同一来源包是否已经支付它”吗？若能，它能否把这两个判断稳定地写在各自正确的 `L5b` 与 `L7b` 字段，而不把 proof-system 的存在定理误报成对象层或运行时交付？

## 1. 共同冻结来源与卡片边界

两次节点都只消费同一份一手 source：`isabelle-prover/mirror-isabelle` 的
`src/ZF/AC.thy`，commit `5c8b47c933c27ebe9be9a7756ab74a28cc0b50f8`，SHA-256
`8f02e7ec0a2396972a1693572bc046d9906cc430b67b45a072eb1ffbd1e2e126`。

source 的关键事实是：它导入 Isabelle/ZF 后以 `axiomatization` 明确加入 `AC`，再在同一 proof system 中证明
`AC_Pi`、`AC_func`、`AC_func0` 与 `AC_func_Pow`。末项给出

```text
∃ f ∈ (Pow(C)-{0}) -> C.
  ∀ x ∈ Pow(C)-{0}. f`x ∈ x
```

冻结 TaskCard 的层严格是 **proof system**：

```text
T      = Isabelle/ZF proof system + source's explicitly axiomatized AC
u/F    = Pow(C)-{0} / Pow plus removal of 0
C      = AC_func_Pow 的 formal derivation
I/O    = C + AC proof environment / accepted proof of the displayed existential
Done   = theorem acceptance at proof-system layer
Q      = AC_func_Pow existential conclusion
```

这不是标准 ZFC object-level consumer，不是 bare ZF 证明，也没有 source 交付 named executable `f`、runtime lifecycle 或现实任务。

## 2. H029：内容链正确，Gate 标签仍漂移

H029的 [NodeCard](20261002-P-DAG-ZFC-SOURCE-029-AC-POW-PROOF-NODECARD.md) 与
[prompt](20261002-P-DAG-ZFC-SOURCE-029-AC-POW-PROOF-PROMPT.md) 已在运行前以 commit `ea058df5` 封存。
Terra/Max source-match自然终态，public E0–E7 明确给出：

```text
AC (axiomatized) → AC_Pi → AC_func → AC_func0 → AC_func_Pow = Q
```

它正确保持 proof-system layer，也明确拒绝把结果写成 ZFC、bare-ZF、runtime 或 executable selector。但它把
active/positive/payment 的结论错放到 `L5b/L6/L7/L7b` 标签中，例如以 formation说明 L5b、以“没有 executable f”说明 L7b。

| 观察 | Master 判词 |
|---|---|
| source rules和最短支付链 | 与冻结 source 相容 |
| layer | `QUALIFYING_PROOF_SYSTEM_CARD`，不可跨层 |
| Gate 的字段归属 | `MATCHTRACE_GATE_LABEL_DRIFT` |
| P2/P3 | 不启动 |
| ZFC Q | 未定位 |

这不是模型隐藏推理的判断。它是公开文字与冻结 P1 字段定义的逐项不一致，故属于 `IDEA_SPEC_INCOMPLETE`：旧 MatchTrace 要求“解释支付”，但没有强制每个 gate 的答案语法。

## 3. H030：固定 Gate Ledger 的回归

为避免只在事后由 Master 重排文字，P1新增 `T4d`，MatchTrace E5新增严格五行 `Gate Ledger`，P-DAG source-match
提示也强制这五个标签。修订与 [H030 NodeCard](20261002-P-DAG-ZFC-SOURCE-030-AC-POW-PROOF-GATELEDGER-NODECARD.md)
及 [prompt](20261002-P-DAG-ZFC-SOURCE-030-AC-POW-PROOF-GATELEDGER-PROMPT.md) 在 commit `209d5d47` 封存。

H030 对完全相同 source 得到下列公开 ledger；source facts 与每项门的语义一致：

| Gate | H030 公开理由 | Master verdict |
|---|---|---|
| L2c | `T` 与 Done 都是 Isabelle/ZF proof-system theorem acceptance | `QUALIFYING_PROOF_SYSTEM_CARD`；不得升级为对象／runtime层 |
| L5b | `AC_func_Pow` 是 source 内已证明的 theorem，Q 不再是当前未完成需求 | `COMPLETED_THEOREM_NOT_UNPAID_DEMAND` |
| L6 | `Pow(C)-{0}`只形成 domain，不产生 choice function | `F_NOT_PAYMENT` |
| L7 | 若当前任务是完成该 formal derivation，proof acceptance要求Q；但 source proof已完成 | `HISTORICAL_PROOF_OBLIGATION_ONLY`，不能留下当下未付 Q |
| L7b | `AC → AC_Pi → AC_func → AC_func0 → AC_func_Pow` 在可见 packet 内直接推出Q | `SOURCE_PACKET_DIRECT_PAYMENT` |

所以H030的最强判词是：

```text
GATE_LEDGER_REGRESSION_PASS_WITH_SCOPE
QUALIFYING_PROOF_SYSTEM_CARD
COMPLETED_THEOREM_NOT_UNPAID_DEMAND
SOURCE_PACKET_DIRECT_PAYMENT
P2/P3_NOT_LAUNCHED
NOT_ZFC_Q_LOCATED
```

它只证明这个冻结 Prompt、模型、source 和字段格式下，公开自我说明已能把门分别放对；不能证明未来所有理论、prompt或模型都稳定如此。`SOURCE_PACKET_DIRECT_PAYMENT`还只关闭 P1 的未支付义务路径：它不把 proof acceptance升级为现实／计算完成，也不关闭 B 向；B 向仍需要 P3 的实际构造状态与同一任务证据。

## 4. 运行与轨迹证据

| 项 | H029 | H030 |
|---|---|---|
| model / effort | `gpt-5.6-terra / max` | `gpt-5.6-terra / max` |
| profile | `source-match`, `governance-regression-fresh`, read-only, network disabled, `approval=never` | 相同 |
| prompt input gate | PASS，source/profile present且项目/旧答案标记不在输入 | PASS，input SHA `82c297336dcf91fa91f4a23d8bac30f30a492fff077f1a4f48e5a35f95716bf9` |
| terminal | 30.905 s，final logical SHA `ca999230836ba079c9684d906d3436ba9742223d39404e6964ef030309ca6499` | 113.942 s，final logical SHA `5d5728c7c9a678efd770e022cc8f51efd8a00279dbe1faf0e420b75265435394` |
| liveness | `RUNNING → TERMINAL`，无自动interrupt | `RUNNING → STILL_RUNNING@65.404s → TERMINAL`，无自动interrupt |
| tool/file/approval | 0 / 0 / 0 | 0 / 0 / 0 |
| private wire | 822 raw lines，SHA `ab4104489f52d147b5d57e30eb6bb3832ee8ade1ca7c8d61559018d3fb2db20d` | 662 raw lines，SHA `5613cac4a190705f12e98abc684e6c8fa5a65e20387fc037d39d784a2f7c4652` |
| terminal locator | `wire.jsonl:822` | `wire.jsonl:662` |

对两张 direct App Server wire，shared `session_trajectory.py` 均运行了
`catalog → tree → coverage → tool/approval search → terminal inspect`。H029是一个 completed turn / 816 session events / 812 turn events；H030是一个 completed turn / 656 session events / 652 turn events。二者均无 tool/approval/cancel/interrupt search hit。

两者的 L1=`NOT_TESTED`、L2=`NOT_OBSERVED`、L3=`NOT_TESTED`、L4=`REQUIRES_SEMANTIC_REVIEW`、L5=`REQUIRES_ACCEPTANCE_EVIDENCE`。private bidirectional wire 可用而 persisted rollout 未提供，故状态为 `BIDIRECTIONAL_APP_SERVER_WIRE_AVAILABLE / PERSISTED_ROLLOUT_UNAVAILABLE`。没有从 reasoning summary 或终稿推断任何不可见 reasoning。

## 5. SelfAuditCard 与下一触发

```text
original requirement: P写清后应当能引导AI定位位置，并能公开说明为什么是那里；三把刀要在同一ZFC Q上会合，
                      不能以代理自述或来源公式替代同一任务。
H029 actual: 内容链正确，但公开字段标签漂移。
classification: IDEA_SPEC_INCOMPLETE, not original-idea challenge and not runner failure.
repair: T4d + fixed five-line Gate Ledger + exact prompt contract.
H030 actual: 同source回归在固定字段上通过；proof-system card的Q已被AC链支付。
classification: ALIGNED_REGRESSION_WITH_SCOPE.
P1/P2/P3 ownership: P1获得说明语法；P2/P3不填该source card。
falsifier: 新版本/新source上若gate ledger仍错置，或只有提示答案才能通过，需重开该合同；若一个同层实际consumer
            给出活跃、正向且未支付Q，则它可进入P2/P3，H029/H030不得阻止。
```

下一节点不能把这个 proof-layer control 当作 Power Set 的实际消费者。它必须在一个版本固定的 ZFC 或数学实际使用来源中同时给出 `u/F/C/I/O/Done`，再检查 Q 是否越过 L5b、L6、L7 与 L7b。
