# P2-KTHEORY-SIP-001：Structure Identity Principle 与 `R_min` 的规则级桥审计

> 状态：`NO_K_THEORY_WITHIN_SIP_DENOMINATOR / SOURCE_AND_REUSE_AUDIT / NO_NEW_MATHEMATICAL_CLAIM`。
> 分支：P2，规则/定理级 `K_theory`。
> 固定分母：HoTT Book §9.8；本地版本冻结为 `sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc/categories.tex`，commit `578b85cc8d586b1677ec4335148adeb443057d24`，特别第 1205–1289 行。
> 问题：该分母是否把 P1 的裸 H/U 当作足以完成 `Done_s`，而不是要求明确保存/保持结构？

## 1. 启动凭据与资产侦察

P1 已固定当前强任务为 `Input + CurveData + Denotes/Satisfies + O + D`。因此本 wave 不是重问“univalence 是否存在”，而是审计一个新、版本冻结的结构同一性分母是否存在下列实际桥：

```text
bare carrier relation H/U  ──K_theory──>  Done_s
```

按 `goal-3.md` §2.2，先做本地资产侦察。结果如下。

| 资产 | 与当前 P2 的关系 | 覆盖判定 | 可复用部分与不可替代的缺口 |
|---|---|---|---|
| `HoTT/formal/sip-representation/SIPRepresentation.agda`，`MP-SIP-REPRESENTATION-001` / `C-124`–`C-128` | 原生 Cubical 中的最小 `ua`/点结构观察边界 | `PARTIAL_REUSE` | 它机器证明：粗签名的结构可被识别、签名外 Bool 观察不能由 `Str → Bool` 统一恢复、细化签名可保观察。它不是当前 `mRich/nRich`、没有 `Input`/`Operation`/`Done_s` 的完整 P1 实例，也不实现 Book §9.8 的一般 `(P,H)` 定理。 |
| `S-RES-20260912-050-SIP-REPRESENTATION` 与 `audit/sip-representation机器证明实施证据-20260912.md` | 对上述 kernel run 的来源、范围和正控制审计 | `PARTIAL_REUSE` | 可复用其 `SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL` 结论及明确非目标；不能把旧点结构当作当前圆环任务的机器证明。 |
| WebGPT `S-ANS-20260910-008-RELATIONAL-SIP` | Book §9.8 的结构同构必须有正、逆两方向 `H` 的纸笔审查；含带时刻关系的模型 | `HISTORICAL_UNVERIFIED` | 它精确指出关系结构同构包含 `H_{αβ}(f)` 与 `H_{βα}(f⁻¹)`，但该 session 自己标明 `REVIEW_REQUIRED`、没有 Agda/Lean kernel run，且其时刻任务不等于本 wave 的圆环 `R_min`。 |
| `MS-TASK-L4-SIP-OBSERVATION-001` | 旧 SIP 机器结论的自动化校准 | `EXACT_COVERAGE`，但仅覆盖旧 Bool 案例 | 它已经把旧案例标为 `POST_FREEZE_KNOWN_CALIBRATION_NOT_BLIND`，并写明没有 natural consumer claim；不能作为当前 P2 或 P3 的新命中。 |

这个资产检查改变了 P2 的执行方式：不重跑 `C-124`–`C-128`，不重复有限关系枚举，也不另造一个同义 `ua` 反例。P2 只做 P1 新合同到 Book §9.8 的字段映射及其规则级判词。

## 2. Book §9.8 实际承诺

Book 把 `(P,H)` 定义为某个 precategory `X` 上的结构：`P : X₀ → U` 是结构族，`H_{αβ}(f)` 是**结构同态**的命题，并要求 identity 与 composition。只有当同一底层对象上的预序成为偏序时，才是 standard notion of structure。结构范畴的对象是 `Σ(x:X₀).P x`。

Book 的 Theorem 9.8.2 是：若 `X` 是 category 且 `(P,H)` standard，则结构的 precategory `Str_(P,H)(X)` 是 category。它在证明中明确分析结构同构：除了底层 `f : x ≅ y`，还同时需要

```text
H_{αβ}(f)  and  H_{βα}(f⁻¹).
```

因此该 theorem 的前提不是“任意 bare equivalence 已经是结构同构”，结论也不是“任意 carrier path/forgetful image 已经完成某个外部过程”。它把可替换性限定为明确结构的双向保持。

## 3. P1 `R_min` 的逐字段映射

| P1 字段 | 能否进入 `(P,H)` 的已知位置 | Book §9.8 是否自动提供它 | 对 `H/U → Done_s` 的含义 |
|---|---|---|---|
| `source : RichCurve`、`CurveData`、闭图 | 可被**选择**为 `P x` 的字段 | 否；先要定义相应 `P` 和其载体范畴 | 若作为结构写入，`H` 必须说明它怎样随 morphism 双向保持；若未写入，SIP 不会凭空恢复它 |
| `targetCarrier`、`encoding : Bare source ≃ targetCarrier` | 底层对象与候选等价/同构资料 | 否；bare equivalence 不是 Book 定义里的结构同构证明 | 单有 encoding 没有 `H` 与逆 `H`，不能满足结构同构的要求 |
| `Observation`、`Denotes` | 可被建模为结构字段、关系或性质 | 否 | 要求同一闭图/指称，就必须将相应观察数据/保持条件放进 `P` 或 `H`；Book 不把它从 carrier 恢复 |
| 操作合同 `O` | 可在适当定义中作为结构、morphism 类或额外关系 | 否；P1 已有 `CurveRun` 与 `AmbientStep/Success` 的不同合同 | Book 没有把“存在指定 run”与“在另一操作模型完成”自动等同 |
| `Done_w` 与 `Done_s = Done_w × Denotes` | 依赖 input/output 的完成性质；可作为额外规格的一部分 | 否；Theorem 9.8.2 谈结构范畴是 category，不谈运行完成 | `Done_s` 不是 carrier identity 的默认释义；需要另行定义并验证其 preservation |

这张表的关键不是断言 `R_min` 不可形式化为标准结构，而是记录尚未完成的建模义务：P1 没有声称已构造一个 `X,(P,H)` 使所有 `O,D` 都是 standard structure。即使未来做出了这种模型，Book 的双向 `H` 条件也会要求对进入签名的字段作保持；它不会给裸 H/U 一张通向 `Done_s` 的免费桥。

## 4. 原生正控制如何约束解释

旧 `SIPRepresentation.agda` 是这个分母的最强本地正控制，而非攻击证据：`s=(Bool,true)` 与 `t=(Bool,false)` 在粗点结构 `Str=Σ(X:Type₀).X` 中由 `ua` 给出路径；由 path，任意 `f : Str → Bool` 在两点同值，因此不存在一个 identity-respecting `f` 恢复两端指定的不同 Bool 值。把观察值加进 `Str'` 后，投影可恢复值且 `s'` 与 `t'` 不再相等。

它说明两件事：

1. 结构外的观察若对任务必要，理论不会自动把它保留；这正是 P1 需要把 `Denotes`、O 和 D 显式写出的原因。
2. 一旦把观察纳入结构，`ua`/SIP 不会继续把不相容的富化结构识别；这是防止“bare equality 冒充强完成”的正控制。

旧原生结果不能升级为当前圆环任务的证明，也不能被反过来叙述为 HoTT 的自相矛盾。它给 P2 的作用是排除一种理论桥候选。

## 5. 本 wave 的学术与社区检查

本 wave 的有界公开来源检查集中于“SIP 的精确承诺和适用前提”，因为它们会改变 P2 是否独立、是否已知以及何时停止。

| 来源 | 结果分类 | 当前相关性 |
|---|---|---|
| [HoTT Book §9.8](https://homotopytypetheory.org/wp-content/uploads/2013/03/hott-online-611-ga1a258c.pdf) | `KNOWN_PRIMARY_FRAMEWORK` | 明确给出 `(P,H)`、standard 条件、`Σx.Px`、结构同构的双向 H 和 Theorem 9.8.2；直接否定“bare equivalence 自动就是结构完成”的读法 |
| [Ahrens–North–Shulman–Tsementzis, *The Univalence Principle* (2021)](https://arxiv.org/abs/2102.06275) | `KNOWN_HIGHER_FRAMEWORK` | 将可表述结构的等价不变性推广到更广类型的结构；它讨论的是**定义在 UF 中的结构**，不是外部来源/操作/完成标准自动成为结构 |
| [Ahrens–North–Shulman–Tsementzis, *A Higher Structure Identity Principle* (2020)](https://arxiv.org/abs/2004.06572) | `KNOWN_DEFENSE_OR_BOUNDARY` | 说明高阶版本还要求相应的 local univalence / indiscernibility 条件；没有给出从 bare carrier 到 P1 `Done_s` 的桥 |
| 当前 P1 的 `R_min` | `NO_RESULT_WITHIN_DECLARED_DENOMINATOR` | 没有发现来源把 `Input + CurveData + Denotes/Satisfies + O + D` 这个精确合同作为 Book §9.8 的现成实例，也没有发现其声称 H/U 自动满足强完成 |

这些来源表明 SIP 不是尚未被社区看见的漏洞；它是为了规定“哪些结构可被等同”而发展出的明确框架。它们既不解决用户的完整现实解释，也没有找到 P3 所要求的实际 `K_app`。

## 6. P2 判词、波次定位与后继

**判词：`NO_K_THEORY_WITHIN_SIP_DENOMINATOR / SIP_EXPLICIT_STRUCTURE_PRESERVATION`.**

- **最终目标连接**：P2 检验最终见证链的规则级桥边。结果消除了一个重要误读：SIP/UA 不把裸载体等价或 forgetful image 直接许诺为 P1 的强完成。
- **全局坐标**：这是 P1 之后、P3 之前的首个规则级分母。它使用 P1 固定的同一任务合同和既有 SIP 资产，但没有重放旧 proof。
- **实际价值**：把当前工作从“再做一次 SIP 示例”转为可复用的防御结论，并把 P3 的要求收窄为一个**真实、版本冻结的消费者**，它必须实际忽略 P1 所需字段并声称完成相同 `Done_s`。
- **为何不延续 SIP**：本地 kernel proof、Book 原文、历史关系审查和公开文献都在同一方向：SIP 的条件是结构保持。继续在此分母增加 toy examples、关键词或重新编译，不会改变 `K_theory` 判词。
- **后继裁决**：`CLOSE_WITH_SCOPE`；`SWITCH_BRANCH` 到 P3。下一 P3 单元先做资产侦察并冻结一个真实库/论文实现/应用的版本和调用链；不能把 SIP 的显式结构保护本身误称为那个消费者。

本报告没有新数学定理、没有新的 kernel run，也没有 HoTT 缺陷结论。
