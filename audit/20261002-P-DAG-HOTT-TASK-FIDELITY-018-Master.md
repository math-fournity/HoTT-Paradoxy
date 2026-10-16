# H018：宇宙询问过程的任务忠实性与 UR 边界

> **身份：** `MASTER_SOURCE_AND_USER_INTENT_REVIEW / A_DIRECTION_SCOPE_JUDGMENT / NOT_A_NEW_MATHEMATICAL_RESULT`。

## 要判的不是“程序会不会停”

形式源码已说明：对具体 universe 的 `question`，任意有限运行不交出 `now`。H015 也在盲态重新定位了 subject、过程和 completion question。这里要判的不同问题是：这个形式过程是否忠实承接用户所说“本来应该很简单”的同一任务？

## 1. 三层不可混写

| 层 | 已有证据 | 本卡结论 |
|---|---|---|
| Formal process | `QuestioningDelay.agda`：`U`、`judgeU`、`Q`、`Halts`、`never`；保存的 Agda/Lean run由其 own evidence owner 管理。 | `FORMAL_PROCESS_EXACT_WITH_SCOPE`。 |
| Source task | CLAIM.md lines 26–37 明说过程问“目录 C 的相同在第 k+1 层落定了吗”，Done是返回 `now k`、交出落定层。 | `DECLARED_FORMAL_TASK_MATCHED`。 |
| User A-direction judgment | KC-000052–054 和扩展认知 011：用户把“确认两个东西是不是同一个、相同到哪层才了结”读作本来简单的事，并以 UR 判断这一线很可能找到目标。 | `USER_JUDGED_A_DIRECTION_WITH_SCOPE`。 |

这三者叠加支持：可以如实说“用户所认定的 A 向任务，与这份形式 h-level 询问过程已有明确、可逐项检查的对应”。它们不自动等于一个关于所有现实任务的数学定理。

## 2. 对应关系与未消除的差异

| 用户叙述 | 形式过程 | 对应强度 |
|---|---|---|
| “这份目录里的相同到哪一层了结” | `isOfHLevel (suc k) C` 与 `Judge C` | source 明示。 |
| “继续问下一层” | no branch → `later (askFrom (suc k))` | source 明示。 |
| “了结” | first `now k` / `Halts` | source 明示。 |
| “宇宙里没有有限了结” | `judgeU` + `universeQuestioningIsNever` / `NeverAnswers` | source 明示。 |
| “两个东西是不是同一个，本来是一句话的事” | h-level is a condition on all identity structure of `C` | 是用户/AI解释桥，不是源码从二元 equality 自动推出的等式。 |
| “现实中简单” | UR 的前半句 | 是研究发起人的判断，不由 type theory kernel 认证。 |

所以 A 向在本项目里不是缺口，也不该被说成 `UNKNOWN`：用户已作出有范围的研究判断。它的证据身份是 `USER_JUDGED_A_DIRECTION_WITH_SCOPE`，而不是 `MACHINE_PROVED_REALITY_CORRESPONDENCE`。B 向仍未建立：H017 说明这个 source 没有 admission/operator cycle；不能把内部 `never` 偷写成“未获资格的 U 已被算符使用”。

## 3. H015 replay release verdict

```text
deidentified P1 source/process/completion replay: PASS_WITH_SCOPE
same-U P2/P3 differential mapping: COMPLETE_WITH_NEGATIVE_CONTROLS
task fidelity: USER_JUDGED_A_DIRECTION_WITH_SCOPE
B-direction admission claim: NOT_ESTABLISHED
formal HoTT inconsistency: NOT_CLAIMED
```

这满足旧 HoTT calibration lock 的目的：P 已在无答案泄漏下重新定位既有 HoTT 的实际 **A 向过程位置**，并由同一 source card上的 P2/P3防止把它错读为逻辑 feedback 或准入环。它只允许下一阶段重新进入 **ZFC P-discovery/calibration**；仍不允许写 `ZFC_Q_LOCATED`、ZFC UR 或 ZFC mathematical claim。ZFC 的共同会合标准仍完全由 `模式P三把刀/009`拥有。

