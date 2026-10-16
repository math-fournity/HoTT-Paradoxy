# P-DAG-HOTT-DISCOVERY-010：延迟询问过程候选的来源核验

> **身份：** `MASTER_PRIMARY_SOURCE_READ / PROCESS_SHAPE_MATCH / FULL_HOTT_REPLAY_NOT_PASSED`。

## 1. 核验问题

H010 的盲态输出选择 `Delay(ℕ)`／`now/later`和“会不会出现 `now k`”作为过程位置。本核验只问它是否与
既有 `QuestioningDelay` 的实际过程具有同一对象、接口和完成标准；再区分 source 中的宇宙特例是否由模型盲态
重现。它不是一次新机器证明，也不把已有项目命题重新交付为新的数学结论。

| Source | Identity |
|---|---|
| process source | `HoTT/formal/claude-cg001/questioning-delay/QuestioningDelay.agda`，SHA-256 `c7b5ddf389bb1501a6f420651c229f4dee84c78f6901ab4080c2faea242f69db` |
| explanatory/source map | `HoTT/formal/claude-cg001/questioning-delay/CLAIM.md`，SHA-256 `76b59863f07582b0e5417f54ef49c4dc5048b9d67a9cfee429df985cdc4a8e57` |
| latest tracked source commit | `5f73a7f` (`evidence: the questioning process Q as a Delay program with a judge; on the universe it is never`) |

## 2. 字段逐项对照

| H010 盲态字段 | 原典 source | 结论 |
|---|---|---|
| `C` 与阶段式 `J(k)` | lines 94–99: `Judge C = (k : ℕ) → Dec (isOfHLevel (suc k) C)` | `MATCHED` |
| `Delay(ℕ)` 与一问一步 | lines 101–110: `askFrom : ℕ → Delay ℕ`、`answer k (yes _) = now k`、`answer k (no _) = later (askFrom (suc k))`、`Q = askFrom 1` | `MATCHED` |
| completion = 出现并交出阶段 | lines 115–147 and CLAIM lines 28–37: `just k`来自 yes；否时进入下一问；过程从1开始 | `MATCHED` |
| `Q?`: 是否最终出现 `now k` | lines 163–188 define `Halts`与`HasLevel`并给出二者对应；CLAIM lines 47–50同样说明 | `MATCHED_AS_PROCESS_QUESTION` |
| specialisation to the universe | lines 275–295: `judgeU`每层为 no；`universeQuestioningIsNever`、`RunsNothing`、`NeverAnswers` | `SOURCE_ONLY_SPECIALISATION` |

因此，H010 不是仅仅在语词上碰到 “Delay”。它的第三位置与既有过程的对象、形成、`now/later`分支、起始阶段和
完成条件一一对应。这个匹配来自 blind output 与后续源对照的组合；source 内容不是 worker 的可见输入。

## 3. 直接支付、宇宙特例与重放状态

盲态 packet 中，`Delay`接口没有给出 `J`的实际分支，所以 D-L6 关于第三位置的“非直接支付”在 packet-visible
范围内成立。source tracer 后来发现的不是一个把它抹掉的普通构造规则，而是实际过程的进一步结果：

- 对任意 `C`，source 把停止等价于“某个有限 h-level 已落定”；
- 对 `Type ℓ-zero`，source 用 `universeHasNoLevel`构造所有阶段的 no，并给出 `question ... ≡ never`和
  `¬ Halts`；
- source 还明确区分另一个一步回答“是否有某层”的程序；该程序的 no 不是原询问过程的完成。

这说明 source 有一个**负的过程结果**，而不是盲态 worker 已经输出的 `now k`。它支持
`SOURCE_PROCESS_MATCH / SOURCE_NEGATIVE_PROCESS_RESULT_REPORTED`；不应被归类为 H008 那种“标准 theorem 直接支付并
淘汰候选”的同一控制。

同时，完整的同题重放仍只得到部分成功：H010 没有盲态选择 `C = Type ℓ-zero`，没有写出 `never`，没有给出
`universeHasNoLevel`，也没有显示 P2/P3、真实 consumer、UR或现实任务。因此当前状态是：

```text
P1 blind process-shape replay: PARTIAL_PASS
source process correspondence: MATCHED
universe specialisation / negative result: SOURCE_REPORTED_AFTER_BLIND_RUN
P2 / P3 / same-real-task / UR: NOT_YET_MAPPED
full HoTT replay release: NOT_PASSED
```

## 4. 下一张 DAG 卡的约束

下游 P2/P3 节点可以使用固定 source card，但不得再称为盲态。它们必须分别回答：

1. P2：`isOfHLevel`的层级判断、`Judge`、`Dec`、`Delay`和`now/later`如何形成可类型化的
   formation/reentry/guard 映射；是否存在真正 feedback，而不是普通递归定义；
2. P3：`yes`证明、`now k`完成、`no`证明、`later`和下一问之间的资格／算符依赖是否确为 source 中的
   构造状态，而不是把静态存在任意读成时间语义；
3. Master：同一过程的“现实任务、输入、观测量、完成标准”是否能从现有 source card建立，不能由
   `Q ≡ never`或 H010 的语言形状自动填补。

在这些节点完成并审计前，本核验不改变项目关于 HoTT 一致性、现实对应或 ZFC的任何结论。
