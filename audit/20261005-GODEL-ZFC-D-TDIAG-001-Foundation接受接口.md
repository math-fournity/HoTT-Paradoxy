# D-001：Foundation 的实际证明接受接口与对角边界

> **身份：** `ACCEPTANCE_INTERFACE_CARD / GODEL-ZFC-CONVERGENCE-SOP / D-TDIAG`。
>
> **状态：** `LOCAL_CLOSED_WITH_SCOPE / A_M2M3_SUCCESSOR_REQUIRED`。
>
> **固定来源：** `FormalizedFormalLogic/Foundation@f3972f4204fc61e1b736ed843415894c83f35508`，
> `Foundation.FirstOrder.Incompleteness.First`。

## 1. Parent gap 与自己的构造

在连续四个 G1 fragment 单位之后，SOP 的非饥饿规则要求转到另一条 READY route。D-001 选择
已经由 C-369 current-replay 固定的一阶算术 source，因为它确实提供实际 proof acceptance 与
Gödel式 coding；但它不应被偷换成芝诺／H0 的 completion consumer。

冻结 interface card：

```text
Code_F(e)         算术 formula / semiformula 的可引用 code
Accept_F,T(e)     Provable T e / T ⊢ e
Diag_F            D → δ = codeOfREPred D → π = δ/[⌜δ⌝]
FormalDone_F(e)   “T 接受 e 有有限 derivation”的证明任务完成
OriginDone_F(e)   同一 proof task 中“有一份可验证有限 derivation”
Bridge_F          在这个 proof task 内是定义对齐；不跨运到过程完成
```

**反证设想：** 若只因 `Accept_F` 有 code/diag，就把它当作 `OriginDone` 的普遍 bridge，
那么 `Accept_F` 必须也能支付固定 H0、芝诺或圆环的 original process task。它没有这种 source contract；
这就是 `DifferentTask` control 的目标。

## 2. 一手 source 与 kernel evidence

C-369 的 package 实际 build 了 `Foundation.FirstOrder.Incompleteness.First`，并由
`Qualification.lean` 检查以下 exported declarations：

```text
FFL.FirstOrder.Arithmetic.incomplete
incomplete_of_RE
exists_true_but_unprovable_sentence_of_sigma1sound
exists_true_but_unprovable_sentence_of_RE_of_sigma1sound
```

`First.lean` 的 diagonal core 明示：

```text
D φ := IsSemiformula ℒₒᵣ 1 φ
       ∧ Provable T (neg ℒₒᵣ (subst ℒₒᵣ ?[numeral φ] φ))
δ := codeOfREPred D
π := δ/[⌜δ⌝]
```

随后它建立 `T ⊢ π ↔ T ⊢ ∼π` 并在显式 `T.Δ₁`、`𝗥₀ ⪯ T`、
`T.SoundOnHierarchy 𝚺 1` 前提下导出 `Entailment.Incomplete T`。主 run 和“去掉
Sigma₁ soundness”被拒绝的负控制由
[`MP-FOUNDATION-INCOMPLETENESS-R3-001`](../HoTT/formal/external-foundation-incompleteness/CLAIM-R3-FOUNDATION-INCOMPLETENESS.md)
和 C-369 拥有。

## 3. T-DIAG payment matrix

| 字段 | Foundation card 的状态 | 证据 / 边界 |
|---|---|---|
| `Code` | `PAID_WITH_SCOPE` | `codeOfREPred`、formula quotation、numeral substitution与 source theorem。 |
| `Verify/Accept` | `PAID_WITH_SCOPE` | `Provable T` 和 `T ⊢ e` 是 source theorem 的真实 proof-acceptance interface。 |
| `diag` | `PAID_WITH_SCOPE` | `D/δ/π` construction and equivalence are source-level theorem content. |
| `reflection` | `CONDITIONAL` | first incompleteness needs explicit soundness/strength assumptions；缺 soundness 的 project negative control被 Lean 拒绝。 |
| `OriginDone` | `PAID_ONLY_FOR_PROOF_TASK` | “finite derivation exists”与 `Provable` 可以在此 task contract 中对齐。 |
| `Bridge` | `BRIDGE_PAID_ONLY_FOR_PROOF_TASK` | 没有 source claim把 `Provable`转换为芝诺连续终点、圆环复原或 H0 finite halt。 |
| `SameFullQ` | `NOT_PAID` | Foundation arithmetic sentence/proof task 与 fixed H0 question/process contract不同。 |
| bare ZFC attribution | `NOT_PAID` | source is first-order arithmetic formalization, not a bare-ZFC-facing completion consumer. |

## 4. Controls

1. **BridgePaid 正控制：** 若把 `OriginDone_F` 明确固定成“存在该 formal theory 的可验证 finite proof”，
   `Accept_F` 的 bridge 是 task-preserving by definition。这说明本 card 不是“所有 interface 都漏 bridge”。
2. **DifferentTask 反控制：** fixed H0 的 `QuestioningDelay`、芝诺 strict completion与 Foundation
   sentence/proof 的输入、操作、观察、Done 都不相同；没有 translator 或 same-task source payment。
3. **Assumption control：** C-369 negative proof表明不能把 `T.SoundOnHierarchy 𝚺 1` 静默省去。
4. **Meta/object control：** Foundation source的 `Provable` 是其对象算术 theorem 的 predicate；GZ-008--011
   的 CCTTmini `ProvWitness` 只是项目 fragment 的 meta-level witness，二者不得同名即合并。

## 5. 局部判词

```text
ACTUAL_PROOF_ACCEPTANCE_AND_DIAGONAL_INTERFACE_SOURCE_PAID_WITH_SCOPE
BRIDGE_PAID_FOR_PROOF_TASK_ONLY
TASK_BRIDGE_UNPAID_FOR_H0_ZENO_CIRCLE
NO_BARE_ZFC_ATTRIBUTION
```

这条 card 完成了 D-TDIAG 的正控制：Gödel机制在一个真实、版本固定、机器重放的对象理论里确实拥有
`Code/Accept/diag`。它同时阻止最危险的过推：不能因为该 proof task bridge 正常，就把它说成 ZFC 已经有
时间／过程 completion 观察力，或说 H0 的问题已经被 Foundation 处理。

## 6. Required successor

下一自然路线是 `A-M2/M3 / CompletionAcceptanceCard-001`：选择实际来源中把 mathematical
completion 当作原过程完成或明确拒绝这种提升的 consumer，逐字段填
`Represent/FormalDone/OriginDone/Observe/Reject/BridgePaid/AdequacyLift`。该路线改变的是**真实完成
consumer**，不再重复 G1 proof-code 或 Foundation proof interface。

## 7. Reopen conditions

只有出现 Foundation/C-369 与 fixed H0 或 Zeno process 在同一任务中的 source-preserving translation，或
出现 Foundation source 自己将 `Provable`当作不同现实完成任务的充分接口时，才重开 D-001。否则它保持 proof-task
正控制身份。
