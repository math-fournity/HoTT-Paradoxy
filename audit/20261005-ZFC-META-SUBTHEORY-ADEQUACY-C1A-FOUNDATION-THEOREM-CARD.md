# C1A：标准连续统 application 的基础—子理论—定理身份卡

> **身份：** `CORE_ADEQUACY_TASK_CARD / C1_PARTIAL / SOURCE_TO_SPEC_PRECONDITION / NOT_A_MATHEMATICAL_RESULT`。
>
> **父方案：** [ZFC-META-SUBTHEORY-ADEQUACY-SOP](../dev-docs/ZFC元理论子理论充分性最终闭环SOP.md)，C1。
>
> **候选族：** `F-A`（标准连续统 application）与 `F-B`（ZFC-founded formalization）的交叉核对。
>
> **本轮来源快照：** [source manifest](../sources/external/zfc-meta-subtheory-c1a-20261005/README.md)。

## 1. 这张卡要判别的狭窄问题

此前 IEP／Norton 卡已经支付了一个 application-level 事实：标准解法把 ZFC-with-Choice、标准实分析、有限时间到达和“间接解决芝诺”放在一起；Norton 也明说过严格的完成条件被换成 revised completion。C1A 不重复讨论这个 task switch。

本卡只问：是否已经有一个**版本固定的基础 (M) 到子理论 (S) 的关系**，以及一个可识别的 (S) 内的实际极限 theorem，能让后续 C2–C5 不必用“标准实分析”这个泛称偷换对象。

## 2. 冻结的两条链

### A. IEP 的 bare-ZFC-facing application chain

| 字段 | 冻结内容 | 直接来源 |
|---|---|---|
| `M_A` | IEP 说多数观点把带 Choice 的 Zermelo–Fraenkel set theory 当作实分析及其它数学分支的适当基础。 | `IEP-ZENO-20261005`，快照第 112–113 行；网页读取 [IEP lines 100–126](https://iep.utm.edu/zenos-paradoxes/)。 |
| `S_A` | 标准实分析：Dedekind cut、real continuum、limits 与 calculus。 | IEP 第 110–120 行。 |
| `Q_A` | Achilles／Dichotomy 中 runner 到达目标的任务。 | IEP 第 287–290 行。 |
| `FormalDone_A` | calculus 显示 runner 能在 finite time 到达目标；标准解法允许 actual infinity of paths。 | IEP 第 288–290 行。 |
| `P_A` | IEP 把标准实分析／calculus＋ZFC-with-Choice 称为对芝诺的间接／标准解答。 | IEP 第 112、125–128、289–290 行。 |

这条链支付了 `M_A → generic S_A` 与 `P_A` 的**应用叙述**。它没有指定一个版本固定的 real-analysis theorem 文件，因而尚未支付 `S theorem identity`。它同时明确把“完成 infinitely many tasks 是否合理”保留为争论，而不是给出 strict bridge（IEP 第 333–342 行；既有 Norton card 见 [A2](20261004-ZFC-ACTUAL-Q-A2-标准解法来源完成合同.md)）。

### B. Mizar FOTG 的形式化实分析 witness

| 字段 | 冻结内容 | 直接来源 |
|---|---|---|
| `M_B` | MML 的库基础是 first-order Tarski–Grothendieck set theory（FOTG），技术文献明确称其是 ZFC 的 non-conservative extension；该文还说明 Choice 在 FOTG 中可证明，而 MML 的适当 foundation 讨论全局 choice operator。 | Brown–Pąk, *A Tale of Two Set Theories*, PDF p. 2（快照）；[原报告](https://alioth.uwb.edu.pl/~pakkarol/articles/CBKP-CICMMKM2019TechReport.pdf)。MML 官方页也说所有库文本由 Mizar 验证为基础公理的 consequences。 |
| `S_B` | MML 中的 real sequences / real limits。 | `MML-numpoly1.miz`，frozen SHA 见 source manifest。 |
| `FormalDone_B` | `Th87`: `SumsReciTriang is convergent & lim SumsReciTriang = 2`。定义给出 `SumsReciTriang.n = 2 - 2/(n+1)`；随后 `Partial_Sums ReciTriangRS = SumsReciTriang`。 | `MML-numpoly1.miz:1991–2060`；公共 HTML/PDF 也显示第 83–89 项。 |
| checker 状态 | MML 官方页报告该类文本会经 Mizar 验证；本机未发现或资格化 Mizar checker，因此没有把该 theorem 重新运行。 | `SOURCE_REPORTED_FORMAL_THEOREM_UNREPLAYED`。 |

`M_B → S_B → FormalDone_B` 是版本冻结的**形式化数学 witness**。它不是 IEP 标准解法的 exact theorem：该序列的项和 IEP 的 Achilles／Dichotomy subpath model 不同，Mizar source 也没有芝诺的 P 语句。

## 3. 关键分裂，不能消掉

```text
IEP:       ZFC+Choice → standard real analysis → “standard solution” / finite-time arrival
Mizar:     FOTG(+system-level choice discussion) → checked real-sequence theorem

未支付：  IEP 的 S_A = Mizar 的 S_B
未支付：  IEP 的 FormalDone_A = Th87 的 FormalDone_B
未支付：  IEP 的 P_A 消费 Th87
未支付：  FormalDone_A/B → OriginDone 的 Bridge
```

因此，本卡拒绝两种错误捷径：

1. 把 Mizar 的 FOTG 直接写成 bare ZFC；
2. 把任何已检查的极限 theorem 直接写成 IEP 对 runner task 的解答 theorem。

## 4. CoreAdequacyTaskCard

| 字段 | 本 C1A 的值／状态 |
|---|---|
| `unit_id` | `C1A-FA-FOUNDATION-THEOREM-IDENTITY-001` |
| `M` | `M_A` 与 `M_B` 均被冻结；它们不是同一个 foundation variant。 |
| `S` | `S_A` 为 IEP 的 standard real analysis；`S_B` 为 Mizar real-sequence / limit library。 |
| `Q` | IEP Achilles／Dichotomy runner-to-goal contract；其 strict/revised split 已由 A2 source card 另行固定。 |
| `FormalDone` | A：finite-time arrival under Standard Solution；B：`Th87` convergence to 2。 |
| `P` | 只在 A 侧有 IEP 的 solution language；B 侧无 Zeno promotion。 |
| `Bridge` | `UNPAID / explicit task-switch control exists`。 |
| `Adequacy` | `NOT_YET_SOURCED`；不能把本项目的 bridge criterion伪装成 ZFC 的已知义务。 |
| `Control+` | IEP／Norton 明示 revised task contract；它显示 source 可以公开改写 Done。 |
| `Control−` | Mizar Th87 的确给出 concrete formal limit，但无 P/Q，因此它反控制“一个极限 theorem 自动是芝诺解决”。 |
| 最强 falsifier | 找到一个冻结来源链，逐项说明 exact ZFC (not merely FOTG) foundation、exact real-analysis theorem、该 theorem 在 IEP/Norton 的 P 中被消费，并实际支付 Bridge。 |
| 本 leaf 的允许结论 | `C1A_PARTIAL_FOUNDATION_AND_THEOREM_WITNESSES / FOUNDATION_VARIANT_AND_THEOREM_IDENTITY_UNPAID`。 |
| 禁止结论 | bare ZFC inadequate；ZFC cannot support analysis；Mizar proves Zeno; Th87 is the Zeno series；或任何 core verdict。 |

## 5. successor scan 与下一动作

`C1A` 的本地问题已经得到可审计的**部分答案**：我们现在有一个 ZFC+Choice 应用来源和一个 ZFC-extension 形式化极限定理来源，但尚无同一 chain。它不能结束 F-A、F-B 或总 Goal。

下一项最小行动定为：

```text
C1A-2 / C0B:
在版本固定的 Isabelle/ZF 或其它 exact-ZF formalization 中，寻找既有的
real / sequence / limit theorem，或者精确记录该 formalization只构造 reals而没有
theorem identity；随后检查它是否能与 IEP 的 P 形成非偷换的 source chain。
```

IsarMathLib 的公开 `Real_ZF` 页面已是一个候选入口：它明确自称为 Isabelle/ZF 中的 real-number construction，并说明 `RealNumbers` 是 slopes 的 quotient；但本卡还未找到它的 convergent-sequence theorem，也没有 IEP promotion。因此它是 `F-B` 的下一候选，不是已经进入 C2 的 contract。
