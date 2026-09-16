<!-- governance-shard:v2
logical_id: PREMISE-001
shard_id: 005
index: ../PREMISE-001.md
-->

# P3P4 判定与审计链 A-B（AI 执行）

> 角色 A 执行，依据修订片 009（角色重分工）。每条带 P3P4_AUDIT_TRAIL 全部必填字段。
> **全部条目 audit_status = AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT。**
> 本分片是**候选判定**，不是结论：任何"该前提非现实"的交付措辞仍需
> MATH_PROOF_BEFORE_DELIVERY_V1 意义上的机器证明（GEN-001 链 + 原生核）。
> 判定不改变分母：PREMISE_DENOMINATOR_V1 保持 35 条、remainder=0。
> 输入：002 分片的 P2（reality_skeleton / divergence_point / omission_shape）。

## 判定方法论声明（本批的元纪律）

本批判定严格遵守修订片 009 §3 的 **steelman 硬纪律**：判 `非现实` 之前必须先给出
"该省略其实可接受"的最强论证。判不出的只能 `暂不判定`。

执行中记录的系统性风险（外部审计应优先复核这两点）：
1. **004 表的构造偏见**：每行 divergence_point 都被写成"理论节省了什么"，
   天然诱导非现实读法。本批的 steelman 字段是唯一的对冲。
2. **语料流利度风险**：AI 在稠密性/自指/无穷这些议题上最流利（KC-000043），
   `corpus_self_audit` 字段对此显式记账；凡判定主要由语料驱动者，置信度降一档。

---

## A 类（类型构造子）

### PREMISE-A-01 · Π

- **ai_verdict**：暂不判定
- **verdict_reason**：Π 的计算规则假定"对应关系在调用前已对全部工况完备、且调用瞬时完成"。
  要判非现实，必须指出一个现实任务，其中"逐点供给"的缺失使理论的结论**错误**而非仅粗糙。
  调度域确实存在这种任务（遇到未料工况时暴露不完备），但我无法确认该任务的失败
  归因于 Π 这个前提，而不是归因于把 Π 用在了它不打算覆盖的任务上。
- **reality_steelman**（最强反驳）：Π 是"全函数"的定义。totality 不是省略，是**对象的定义边界**。
  把 Π 用在部分覆盖的调度上是**误用**，不是 Π 的缺陷。数学对象不因未被用来建模某个
  现实任务而成为非现实。按这个 steelman，本条连"断裂"都不存在。
- **falsifier**：给出一个任务，其失败可归因于 Π 的计算规则本身（而非 Π 的误用范围），
  且该任务在 Π 的声称覆盖范围内。
- **confidence**：低
- **corpus_self_audit**：中。函数类型最常被对齐到代码函数（计算域），我的判定理由
  部分依赖"调度域是正确判定域"这一未经用户确认的选择。
- **evidence_anchors**：002 分片 A-01；HoTT/theory-schema/CORE_RULES.md（Π 规则）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游（暂不判定不进入 SUPPLY_REGISTRATION）

### PREMISE-A-02 · Σ

- **ai_verdict**：暂不判定
- **verdict_reason**：Σ 的投影假定了整体已装配完毕。若判非现实，需要"附属项延后获得"
  的现实任务（保修条款在购买后生成）在 Σ 的声称范围内。但 Σ 是**静态依赖对**的定义，
  时序任务不是它的声称对象。
- **reality_steelman**：Σ 定义的是"一个主项连同按主项而定的附属项"这一**静态结构**。
  它不声称建模时序过程；把时序压成静态是建模者的选择，不是 Σ 的前提错误。
- **falsifier**：给出一个任务，其错误结论可追溯到 Σ 的投影规则本身，而非建模选择。
- **confidence**：低
- **corpus_self_audit**：低。依赖对在语料中少有非计算例子，我的证件/保修域例子是
  构造的而非观察的。
- **evidence_anchors**：002 分片 A-02；CORE_RULES.md（Σ 规则）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-A-03 · Nat

- **ai_verdict**：非现实
- **verdict_reason**：Nat 的消除子要求"对任意 n 可逐步展开到完成"，把可无限延续的计数过程
  当作已完成的结果序列。**判定非现实的关键任务**：任何"计数过程是否终止"构成前提的
  现实任务（计件质检、计时、对未完成对象的遍历）。在这个任务下，被节省的条件——
  "展开需要逐步执行、且可能永不完成"——**确实不可省**：理论的良基性内置
  把"可能不终止"这一现实可能性从计数对象中移除了，而计数任务的结论
  （总数、耗时、是否完成）恰恰依赖于这个被移除的可能性。
  这不是精度问题：增加 Nat 的分辨率无法恢复"可能不完成"这一性质。
- **reality_steelman**（最强反驳）：Nat 建模的是"已经完成的计数结果"，不是"正在计数的过程"。
  有限性/良基性是**定义边界**。过程语义在另一个对象（coinduction、延迟语义）里建模。
  按这个读法，"永不完成"不属于 Nat 的声称范围，移除它不是缺陷。
  **这个 steelman 相当强**——它把本条降级为"Nat 与过程语义的分工问题"而非前提非现实。
  我仍然判非现实，理由是 steelman 需要一个**实际存在的**配套对象来承担被移除的内容；
  若该配套对象在 HoTT 中存在且被自然使用，本判定应被推翻（见 falsifier）。
- **falsifier**：展示 HoTT 中存在被自然使用的、承担"可能不终止的计数过程"的对象
  （如 stream/coinductive Nat 的标准用法），且它在本任务的语境下被实际调用。
  这将证明被省略者有归宿，本条移到"现实"。
- **confidence**：中
- **corpus_self_audit**：中偏高。无穷/良基在语料中极高频，我的判定很可能部分由
  语料流利度驱动（KC-000043）。降一档置信度已执行。
- **evidence_anchors**：002 分片 A-03；CORE_RULES.md（Nat 规则 C09）；
  核心认知 KC-000014/022（方向 B：现实无法完成而理论当作已完成）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：若审计批准 → SUPPLY_REGISTRATION-A-03 → 任务族"计数过程的完成性"
  → GEN-001 链（枚举/归约/原生核）；推翻时回滚全部

### PREMISE-A-04 · identity/Path

- **ai_verdict**：暂不判定
- **verdict_reason**：J 的计算规则假定同一性可立即判定（refl 立即给出）。但"确认同一"
  在现实文证域需要证据链。问题在于：refl 只覆盖"定义上同一"的情形，而定义上同一
  确实是瞬时的；需要证据链的是命题同一，而那不是 J 计算规则的声称对象。
- **reality_steelman**：`refl` 的瞬时性是**定义同一**的瞬时性，这是正确的而非省略。
  命题同一的观察成本由 identity type 的命题性（C-01/G-02）承担，不由 refl 承担。
  本条的 divergence_point 实际上属于 B-01，不是 A-04。
- **falsifier**：给出一个 refl 被用在非定义同一的情形并产生错误结论的实例。
- **confidence**：低
- **corpus_self_audit**：中。同伦型在语料中几乎只以几何例子出现，我引入文证域
  （身份证）是为了避开计算域，但该域选择未经确认。
- **evidence_anchors**：002 分片 A-04；CORE_RULES.md（identity 规则）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-A-05 · universe U/El

- **ai_verdict**：现实
- **verdict_reason**：code/decode 假定目录完备、互译无损。但 universe 的封闭性是
  **形式对象的编目规则**，其"完备"是相对于已定义的形式构造而言的。
  现实的分类体系不完备，是因为它的对象是开放的；U 的对象是**由规则生成的**，
  因而是真正完备的。这里没有断裂，只有域的错位比较。
- **reality_steelman**（本条即判定理由）：U 的完备性是生成规则的自洽性，
  不是经验目录的完备性。层级膨胀（U:U）是**已知的、被处理的问题**
  （universe hierarchy / Russell vs Tarski），不是被省略的条件。
- **falsifier**：给出一个形式构造，它在 U 的生成规则内却不能被 code/decode 处理。
  这将是 U 的真正缺陷而非我的错位比较。
- **confidence**：中
- **corpus_self_audit**：中。宇宙在语料中常引向罗素悖论式自指讨论，我刻意把判定
  从自指族拉开；但"层级膨胀"的描述本身仍带自指族惯性。
- **evidence_anchors**：002 分片 A-05；CORE_RULES.md（U/El 规则 C17/C18）；
  002 分片自身已标注"这是结构观察，不是非现实判定"
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-A-06 · HIT

- **ai_verdict**：暂不判定
- **verdict_reason**：消除子必须为所有构造子（含高阶路径）提供分支并立即化简，
  假定"什么算同一"的判据在构造时已穷尽列出。这确实把等价判据的**事后修订**移出了对象。
  但 HIT 的构造子列表是**定义的一部分**——定义一个 HIT 就是定义它的等价生成子。
- **reality_steelman**：HIT 不声称"等价判据不会再变"；它声称"在这个 HIT 内，
  等价由这些构造子生成"。事后补充判据对应的是**定义另一个 HIT**，不是本 HIT 的缺陷。
- **falsifier**：给出一个任务，其结论错误可归因于某个具体 HIT 的构造子不完备，
  且该不完备不是定义自由度的结果。
- **confidence**：低
- **corpus_self_audit**：低。HIT 在语料中例子少，我的折纸/构象域是构造的。
- **evidence_anchors**：002 分片 A-06；EXTENSIONS_AND_METATHEORY.md（HIT）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-A-07 · A+B

- **ai_verdict**：现实
- **verdict_reason**：match 假定分支穷尽且情形互斥。但 A+B 是**二分构造**的定义；
  穷尽性是定义内容。现实的"开关故障/第三种情形"意味着该任务不是 A+B 建模的对象，
  而是 A+B+C 或带错误通道的枚举。
- **reality_steelman**（本条即判定理由）：互斥穷尽是 A+B 的定义，不是经验主张。
  把边界模糊的任务交给 A+B 是误用。
- **falsifier**：给出一个 A+B 的构造子无法表示其情形的实例。
- **confidence**：中
- **corpus_self_audit**：低。
- **evidence_anchors**：002 分片 A-07；CORE_RULES.md（余积规则）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-A-08 · 0

- **ai_verdict**：现实
- **verdict_reason**：ex falso 假定"不可能"是绝对的。但 0 是**空构造**的定义；
  "空"的形式含义就是"无构造子"。经验性的"不可能后来发生"意味着原类型的构造子
  分析错了（该情形实际属于某个非空类型），不是 0 的规则错了。
- **reality_steelman**（本条即判定理由）：0 的空性是定义；ex falso 是它的消除规则，
  只在"确实无构造子"的前提下有效。该前提被违反时，错的是类型归属，不是 ex falso。
- **falsifier**：在某个类型确为空的前提下，ex falso 产生错误结论的实例。
- **confidence**：中
- **corpus_self_audit**：低。
- **evidence_anchors**：002 分片 A-08；CORE_RULES.md（0 规则）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-A-09 · 1

- **ai_verdict**：现实
- **verdict_reason**：⋆ 的唯一性被当作无需检查的内置事实。但 1 是**单构造类型**的定义；
  唯一性是定义内容。"会不会还有别的"这一验证过程，在 1 的形式层面确实不需要——
  因为构造子表只有一个条目。
- **reality_steelman**（本条即判定理由）：唯一性由构造子表机械保证，不需要验证过程。
  需要验证"是否还有别的"的任务，其对象不是 1 而是待判定的枚举类型。
- **falsifier**：在 1 的构造子表确实只有一项的前提下，⋆ 的唯一性失效的实例。
- **confidence**：中
- **corpus_self_audit**：低。
- **evidence_anchors**：002 分片 A-09；CORE_RULES.md（1 规则）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-A-10 · 2

- **ai_verdict**：现实
- **verdict_reason**：2 假定判定瞬时、确定、值与判定过程分离。但 2 是二值枚举的定义；
  判定的"瞬时性"是构造子的给定方式。未决/叠加态的任务其对象不是 2 而是某个
  依赖类型或延迟类型。
- **reality_steelman**（本条即判定理由）：值的先在性是枚举类型的定义内容。
  依赖判定的任务由依赖类型建模，不由 2 建模。
- **falsifier**：在 2 的构造子表确实只有两项的前提下，值与判定分离产生错误结论的实例。
- **confidence**：中
- **corpus_self_audit**：中。二值最常被对齐到数字电路；我保留了"判定"这一更宽母域，
  但该选择未经确认。
- **evidence_anchors**：002 分片 A-10；CORE_RULES.md（2 规则）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-A-11 · W

- **ai_verdict**：非现实
- **verdict_reason**：W-递归要求对每个节点的全部子树递归，良基性被内置（递归必终止），
  把"树的生长过程"当作"已完成的树"。**判定非现实的关键任务**：任何其对象是
  "正在展开的、可能不终止的分支过程"的现实任务（对话/决策的可能展开、组织生长、
  家谱的持续编纂）。在这些任务下，被节省的条件——"展开可能永不完成"——
  **确实不可省**：良基性内置把这一现实可能性从对象中移除了，而任务的结论
  （是否到达某状态、是否还有后代）恰依赖被移除者。这不是精度问题：
  增加树的深度无法恢复"可能不终止"这一性质。
- **reality_steelman**（最强反驳）：W 建模的是**良基的、已完成的树**，
  不是生长过程。不终止的分支过程由 coinductive 类型（stream、延迟树）建模。
  良基性是定义边界，不是省略。**这个 steelman 强**：与 A-03 同形。
  我仍判非现实的理由相同：被移除的内容需要一个**实际存在的、被自然使用的**配套对象；
  若 coinductive 延迟树在本任务语境下被实际调用，本判定应被推翻。
- **falsifier**：展示 HoTT 中存在被自然使用的、承担"可能不终止的分支展开"的
  coinductive 对象，且它在本任务语境下被实际调用。
- **confidence**：中
- **corpus_self_audit**：中偏高。无穷/良基在语料中极高频，判定很可能部分由
  语料流利度驱动。降一档已执行。
- **evidence_anchors**：002 分片 A-11；CORE_RULES.md（W 规则）；
  核心认知 KC-000014/022（方向 B）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：若审计批准 → SUPPLY_REGISTRATION-A-11 → 任务族"分支展开的良基性"
  → GEN-001 链；推翻时回滚全部。与 A-03 同形，建议 GEN-001 链合并处理（任务族
  "过程性 vs 已完成性"共同分母），但**合并与否由外部审计决定，AI 只建议**。

---

## B 类（判定与相等）

### PREMISE-B-01 · definitional equality 可判定

- **ai_verdict**：非现实
- **verdict_reason**：设定义相等**可判定**并与命题相等分离，等于假定"同一性有不含时序、
  不含观察、不含用途的机械判据"。**判定非现实的关键任务**：任何"两份东西是否算同一份"
  的结论依赖于**用途/效力层级/观察层**的现实任务（同一份合同在成立/生效/可执行层面
  可能不同；同一型号件在特定工况下不可互换）。在这些任务下，被节省的条件——
  "同一性判据需要指定观察层"——**确实不可省**：把判据固定为语法问题后，
  语义同一性问题被**推出界外**，而任务的结论恰在界外。
  这不是精度问题：语法判据再精细也无法判定"在用途 L 下是否同一"。
- **reality_steelman**（最强反驳）：definitional equality 是**计算装置**的一部分，
  它的存在价值恰恰是它是可判定的——这是类型论能机械执行的原因。
  语义同一由 propositional equality 承担，两者分工是**设计**而非缺陷。
  用户的文证域例子（合同的效力层级）确实存在，但那是 propositional 的业务，
  不是 definitional 的业务。
  **这个 steelman 很强**：它把本条压成"分工问题"。我仍判非现实的理由：
  语义同一在 HoTT 中由 propositional equality 承担，而 propositional equality
  的判定（B-01 的镜像）恰恰是**不可判定**的——于是"同一性需要观察层"这个条件
  在整个系统中**没有任何对象承担它**。它被从 definitional 层移出，
  又没有在 propositional 层被接住。
- **falsifier**：给出一个 HoTT 内部对象，它自然承担"同一性判据依赖观察层/用途"，
  且在本任务语境下被实际调用。这将证明被移除者有归宿，本条移到"现实"。
- **confidence**：中
- **corpus_self_audit**：中。可判定性在语料中几乎只以"算法/编译器"形态出现，
  我刻意取文职判定域；该域选择未经确认，但**判定理由不依赖语料频率**，
  而依赖"被移除者在系统内无归宿"这一结构性论证。
- **evidence_anchors**：002 分片 B-01；CORE_RULES.md（转换规则 C03/C04）；
  核心认知 KC-000031/035（表达保真：极简理论"理应被覆盖"却不能）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：若审计批准 → SUPPLY_REGISTRATION-B-01 → 任务族
  "同一性判据的观察层依赖" → GEN-001 链；推翻时回滚全部。
  **注意**：本条与 G-01/G-02 构成"同一性层深与锚定"主题簇，
  建议合并 GEN-001 任务族；合并与否由外部审计决定。

### PREMISE-B-02 · β-reduction

- **ai_verdict**：现实
- **verdict_reason**：β 假定执行瞬时、无副作用、可重复。**但在计算域内，这正是正确的**：
  β 是符号替换规则，它的执行确实瞬时、无副作用、可重复。002 分片已显式标注本条
  骨架为计算域——而计算域的这个描述是**准确的**，不是省略。
  "执行耗资源、可能失败"是物理实现的性质，不是符号替换的性质。
- **reality_steelman**（本条即判定理由）：β 是符号层的规则；物理执行的开销
  属于实现层（R0–R3 / IMPLEMENTATION_PHENOMENON），已在 008 片 §2 明确划为域外。
- **falsifier**：在纯符号替换的层面给出 β 不可重复或有副作用的实例。
- **confidence**：中
- **corpus_self_audit**：中（骨架确为计算域，但按 008 §9 显式标注后，
  本条的判定理由恰恰支持计算域是**正确**的现实域，不是惯性）。
- **evidence_anchors**：002 分片 B-02（已标注计算域）；CORE_RULES.md（β 规则）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-B-03 · η-laws

- **ai_verdict**：暂不判定
- **verdict_reason**：η 假定"所有观察"已完备。外延性原则把"在所有观察下相同"
  当作同一的判据。问题在于 η 的"所有观察"是**形式化的、对象语言内的**观察，
  不是经验观察的开放总集。
- **reality_steelman**：η 是**外延性原则**，它定义的是"同一的判据是行为"。
  开放的经验观察集不是它的对象。新增观察维度区分原先相同的两物，
  对应的是**定义新的等价关系**，不是 η 的失效。
- **falsifier**：给出一个实例，其中 η 的形式化观察集已完备，
  却仍产生错误结论（而非"需要另一个等价关系"）。
- **confidence**：低
- **corpus_self_audit**：低。
- **evidence_anchors**：002 分片 B-03；CORE_RULES.md（η 规则）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-B-04 · J/transport

- **ai_verdict**：暂不判定
- **verdict_reason**：transport(refl) ≡ id 假定"不移动时东西完全不变"。
  现实的"保持不动"需要条件维持（漂移、锈蚀）。但 refl 是**零长路径**的定义；
  "沿零长路径搬运等于不搬"是符号层的正确性，不是关于物理静止的主张。
- **reality_steelman**：refl 的恒等性是定义内容；物理漂移对应的是非 refl 路径
  或时间索引的类型，不是 transport(refl) 的失效。
- **falsifier**：给出一个实例，其中路径确为 refl（定义上同一），
  transport 仍改变了被搬运的对象。
- **confidence**：低
- **corpus_self_audit**：低。
- **evidence_anchors**：002 分片 B-04；CORE_RULES.md（J 规则）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游
