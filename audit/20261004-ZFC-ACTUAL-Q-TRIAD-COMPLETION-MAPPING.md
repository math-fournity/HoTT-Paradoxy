# 圆环、Zeno 与 HoTT：完成模式三方映射及政策范围缺口

> **身份：** `ACTUAL_Q_CARD / COMPLETION_PATTERN_MAPPING / SOURCE_SCOPE_UNOBSERVED / NOT_A_TASK_EQUIVALENCE_THEOREM`。

## 1. 三个现场的逐字段映射

| 字段 | 用户圆环 | Zeno／supertask 来源 | 固定 Cubical Agda HoTT Q |
|---|---|---|---|
| `T` | 连续统、去点／展开／复原与其现实解释。 | ZFC-supported real analysis、连续运动或 supertask 的解释。 | Cubical Agda + guarded `QuestioningDelay` + set truncation。 |
| `I` | 已有的圆 M，经去点和展开成为 N。 | 0 到 1 的 runner／Achilles 路线；无限中间 action 描述。 | 原 `Type ℓ-zero` Q 与其 set truncation `TU`。 |
| `Op` | 反向复原中 N 两端的逼近与预期接回。 | 连续运动、按半程经过位置，或无限 action 的完成语义。 | 原 Q 的逐层询问；集合截断后的粗观察。 |
| `O` | 两端距离、是否已成为此前 M、是否出现新点／新对象。 | partial sums、连续时间位置、是否有 final action、是否做完所有 actions。 | `runFor 0` 的 `just 1`／`nothing` 与原 Q 的有限 `Halts`。 |
| `Done_formal` | 存在圆同胚、紧化对象、极限对象或闭参数 endpoint。 | 数列极限为 1、连续模型到达目标、或 `Done_revised`。 | `runFor 0 (question TU judgeTU) ≡ just 1`。 |
| `OriginDone` | 此前的 M 经指定反向过程复原，不能由新造对象、静态同胚或事后黏合替代。 | 依来源而异：`Done_strict` 含 final action；`Done_revised` 指做完所有 action。 | 原 `Questioning.Halts (Type ℓ-zero) judgeU`。 |
| 已知反控制 | 闭连续参数 endpoint 可以出现，但这本身未支付来源／历史复原。 | SEP/Norton 明示 strict 与 revised Done 非同一；C-361 明示极限不推出有限阶段 endpoint。 | C-360 明示粗 completion 不反射原 Q 的有限 completion。 |

## 2. 能成立的模式层结论

三者具有同一个**完成模式候选**：

```text
一个理论/模型/粗观察给出 Done_formal；
原任务仍保留一个较强的 Done_origin；
需要问两种 Done 是否被同一来源、同一政策、同一任务桥支付。
```

这个结论只说明它们可进入同一 `P` 的研究语言。它不表示三个状态空间相同，也不表示一份来源已把三者归为同一个任务。

## 3. 为什么暂不要求三方 `TaskEquiv`

圆环几何、Zeno 运动和 HoTT 的类型程序没有理由天然拥有可逆状态空间同构。把 `TaskEquiv` 作为唯一门会把跨领域实际研究预先排除。

新的 C-359 采用两级标准：

```text
严格控制：TaskEquiv
  = 保持 State/input/step/observe/formalDone/originDone 的完整等价；

实际政策门：PolicyScopeWitness
  = 某个来源归属的理由，说明 P 为什么能在两侧共同适用。
```

`TaskEquiv` 仍然是防止滥用类比的强控制。`PolicyScopeWitness` 则是实际来源工作应支付的内容，不能由“都谈完成”自动补齐。

## 4. 当前未支付项

| 义务 | 当前状态 | 何种证据可支付或推翻 |
|---|---|---|
| 圆环 `OriginDone` 的完整过程规格 | `USER_DONE_ADJUDICATION_REQUIRED` | 用户原案或版本固定过程定义给出 State/Op/O/Done；不能由程序员补一个最后步骤。 |
| Zeno→圆环政策范围 | `SOURCE_UNOBSERVED` | 一手来源明确把其连续统 completion policy 施用于原 M/N 复原，或明确排除。 |
| Zeno→HoTT 政策范围 | `SOURCE_UNOBSERVED` | 基础验收或哲学来源把固定 HoTT completion contract 纳入同一 adequacy policy。 |
| Agda B→Lean B | `EXTERNAL_FORMAL_RESULT_WITH_RECEIPT` | 保真跨 kernel 解释表或独立证明，不是文件名相同。 |
| 强 P 的实际采用 | `SOURCE_TASK_CONTRACT_SPLIT` | 来源将 `Done_formal` 当 `OriginDone` 却不改写任务，或相反明确改写／支付 bridge。 |

## 5. 当前终态

```text
COMPLETION_PATTERN_SHARED_WITH_SCOPE
POLICY_SCOPE_NOT_ESTABLISHED
ACTUAL_Q_POLICY_CONFLICT_WITH_SOURCE_BOUNDARY = NOT_REACHED
```

这比“它们都是同一个 Q”更强也更可检验：它说明了可共享的模式在哪里，也说明了不能由模式相似偷渡到 ZFC 判词的那一跳究竟缺什么。
