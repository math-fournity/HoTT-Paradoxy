# C0 successor reselection 002：统一 M/S/Q/P/Adequacy 来源合同的候选发现

> **身份：** `CORE_ADEQUACY_TASK_CARD / ACTIVE_SUCCESSOR_SELECTION / NOT_A_MATHEMATICAL_RESULT`。
>
> **父方案：** [ZFC-META-SUBTHEORY-ADEQUACY-SOP](../dev-docs/ZFC元理论子理论充分性最终闭环SOP.md)。
>
> **前序：** [C1D bounded coupling audit](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C1D-FORMALIZATION-APPLICATION-COUPLING-DENOMINATOR.md)。

## 1. 唯一目标

从仍然 live 的 `F-A / F-B / F-C` 中选择一个**新**来源候选。候选只有同时给出或可由明确 source links 逐项支付以下所有字段时才可进入 C1–C5：

```text
M          : bare ZFC 或版本固定的 ZFC-founded foundation context
S          : version-fixed continuum/limit subtheory or theorem
Q          : runner/circle/physical-process target with C/I/O/OriginDone
FormalDone : S 的精确结果
P          : source actual promotion from FormalDone to a claimed solution
Bridge     : preservation payment or explicit task switch
Adequacy   : foundation/application responsibility source
```

## 2. 不可接受的候选

- 只给一个 ZF/ZFC proof assistant theorem；
- 只给一篇“极限解决芝诺”的教材叙述；
- 只给 foundation 的语言/representation 讨论；
- 只给 physical model 而没有 mathematical/foundational provenance；
- 只把 C1A–C1D/C5A–C5C 里已经拒绝的 source pieces换名字再组合。

## 3. 当前候选入口和最小判别动作

| 入口 | 最小判别动作 | 成功条件 | 失败时的正确登记 |
|---|---|---|---|
| `F-A` | 找到与 IEP/Norton不同、版本固定的 Standard-Solution authority，检查它是否明确保留 strict OriginDone。 | source 真的断言 same task，而非改写 Done。 | `EXPLICIT_TASK_SWITCH` 或 `P_NOT_STRICT`。 |
| `F-B` | 查 formalization publication/readme/companion source 是否以 exact ZF/ZFC theorem 消费 runner target，而不只 formalize analysis。 | 同一 formal theorem 被 P 明确调用。 | `FORMALIZATION_APPLICATION_COUPLING_UNPAID_WITH_SCOPE`。 |
| `F-C` | 查 set-theoretic foundation source 是否把 physical process completion纳入自身 required faithful-representation verification。 | direct `AdequacyRequiresBridge M S Q P` source payment。 | `FOUNDATION_APPLICATION_DUTY_UNPAID_WITH_SCOPE`。 |

## 4. 访问、证据与停止

- 可读 public primary/authoritative sources、fixed project source snapshots与正式 formalization documentation；不读取 credential、私有对话或未授权 worktree。
- 每一次 source action必须冻结 URL/version/hash、给出 source-to-field map和强反证；搜索结果页只能导航，不能单独支付字段。
- 发现 source gap只关闭这个候选入口；立即做 successor scan。没有 C6 source-to-spec fidelity与kernel run，不得称 bare ZFC research completed。

## 5. 首项操作

```text
C0R2-F-B-PUBLICATION-COUPLING-SEARCH

先从 Mizar / Isabelle-ZF formalization 的公开 documentation、论文与
引用网络中查找是否存在“Zeno / Achilles / Dichotomy / physical motion”
的 explicit consumer；同时反向检查当前 Standard-Solution sources是否
明确引用某个 formalization。只要任一方向没有 source identity，登记
bounded result并移交 F-A 或 F-C，而不是泛搜所有数学资料。
```
