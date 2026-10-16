<!-- governance-shard:v2
logical_id: PREMISE-001
shard_id: 006
index: ../PREMISE-001.md
-->

# P3P4 判定与审计链 C-G（AI 执行）

> 角色 A 执行，依据修订片 009（角色重分工）。每条带 P3P4_AUDIT_TRAIL 全部必填字段。
> **全部条目 audit_status = AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT。**
> 本分片是**候选判定**，不是结论。判定不改变分母。
> 输入：003 分片的 P2。方法论声明见 005 分片（steelman 硬纪律 + 构造偏见对冲）。

---

## C 类（恒等与等价）

### PREMISE-C-01 · identity type 的命题性（isProp）

- **ai_verdict**：现实
- **verdict_reason**：isProp(Id) 假定任意两条路径间已有更高阶路径可判定，
  即"裁决的供给"随类型内建。但 isProp 是**类型的性质**，不是关于现实仲裁的主张。
  一个类型是命题，意味着它的元素间都相等——这是**形式定义**，
  其"裁决供给"是定义的推论，不是经验主张。
- **reality_steelman**（本条即判定理由）：isProp 是形式性质；
  现实中"两条证据是否等价要等新证据"，对应的是该类型**不是命题**——
  这是类型差异，不是 isProp 定义的缺陷。
- **falsifier**：给出一个类型，其形式上满足 isProp，但两条路径间实际无更高阶路径。
- **confidence**：中
- **corpus_self_audit**：中。命题性在语料中多以"唯一性引理"出现，
  我刻意避开"证明策略"读法；判定理由不依赖语料频率。
- **evidence_anchors**：003 分片 C-01；CORE_RULES.md（identity 规则）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-C-02 · 函数外延性（funext）

- **ai_verdict**：暂不判定
- **verdict_reason**：funext 把"对所有 x 有 f(x)=g(x) 则 f=g"当作同一性判据，
  抹掉调度次序、资源消耗、故障模式。这些被抹掉的差异在现实的工艺任务中
  **确实构成"不是同一条路线"**。但 funext 是**关于函数外延的**形式原则：
  它说同一性由逐点行为决定。被抹掉的内容是否属于"同一性"的一部分，
  本身就是本判定的争点——我不能用它来反驳它自己。
- **reality_steelman**：funext 定义了"函数这一对象的同一判据是外延行为"。
  调度/资源差异属于**实现**而非**函数**——两条算法不同但函数相同是常态。
  若任务关心调度，它的对象不是函数而是流程。
- **falsifier**：给出一个任务，其对象确为函数（外延对象），
  但结论错误可归因于 funext，而非归因于"对象选错了"。
- **confidence**：低
- **corpus_self_audit**：中。外延性在语料中几乎只以代数形态出现，
  我的工艺/履约域是构造的且未经确认。
- **evidence_anchors**：003 分片 C-02；CORE_RULES.md（funext）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-C-03 · univalence（公理形式）

- **ai_verdict**：暂不判定
- **verdict_reason**：公理形式把"等价即相等"当作无需维持的既成事实，
  省掉了"兑换的可用性需要被维持"。这个省略在现实兑换任务中**确实不可省**
  （汇率变动、规则修订使"能兑换"成为可失效状态）。
  但 univalence 是**关于类型同一性**的公理，不是关于现实兑换可执行性的主张。
- **reality_steelman**：univalence 断言的是"等价蕴含相等"这一**类型层方向**。
  现实兑换的有损/失效属于实现层，已在 008 §2 划为域外。
  公理不声称兑换在物理上总是可行。
- **falsifier**：给出一个任务，其对象确为类型间的等价，
  但结论错误可归因于 univalence 公理本身，而非归因于把物理兑换误当类型等价。
- **confidence**：低
- **corpus_self_audit**：中。univalence 常被作为"同构即同一"的动机性陈述讨论，
  容易被跳过；我刻意把判定理由放在"可用性需维持"，但这是**结构观察**，
  003 分片自身已标注"不是该前提非现实的判定"。
- **evidence_anchors**：003 分片 C-03（含自我限定）；CORE_RULES.md（univalence）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-C-04 · univalence（cubical 定理形式）

- **ai_verdict**：暂不判定
- **verdict_reason**：定理形式把存在性升级为可计算构造，计算规则假定兑换沿区间
  连续完成、comp 立即给出结果。作为**计算规则**，它在符号层确实是即时的。
  "连续执行是耗时的运动过程"这一现实性质，在符号层不适用。
- **reality_steelman**：comp 的即时性是计算规则的定义；
  物理运动的耗时属于实现层。符号层的"连续"是形式参数的代数，
  不是时间中的运动。
- **falsifier**：给出一个实例，其中 comp 作为符号计算规则产生错误结论
  （而非物理执行耗时导致的错误）。
- **confidence**：低
- **corpus_self_audit**：中。cubical univalence 在语料中只在形式规则层面讨论，
  我引入"连续执行作为运动"是刻意避开计算域，但该域选择未经确认。
- **evidence_anchors**：003 分片 C-04；EXTENSIONS_AND_METATHEORY.md（cubical）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

---

## D 类（cubical 机器）

### PREMISE-D-01 · 区间 I 与端点、连接

- **ai_verdict**：非现实
- **verdict_reason**：区间被当作**给定的、稠密可分的连续体**：任意两位置间"总还有位置"
  是内建事实。**判定非现实的关键任务**：任何"转动/连续运动的分辨率受测量与控制条件
  约束"的现实任务（伺服定位、刻度可读性、量仪精度）。在这些任务下，
  被节省的条件——"可分性受观察条件约束"——**确实不可省**：
  理论把稠密性当作给定结构，而现实的可分性是**被设备允许时才有的性质**。
  这不是精度问题：给定的稠密结构无法表达"在条件 c 下不可分"，
  因为可分性被烘进了区间本身。本条 omission_shape=continuity 是**依前提本性选定**的
  （区间的定义内容就是稠密连续体），非默认归类。
- **reality_steelman**（最强反驳）：区间是**理想化的数学对象**，正如实数轴。
  所有连续数学都做这个理想化，且在宏观任务中给出**正确**结论。
  量子尺度的不连续性意味着该任务不是区间建模的对象，而是某个离散/非交换几何的对象。
  **这个 steelman 强**：理想化本身不构成非现实。
  我仍判非现实的理由：本条的特殊性在于**可分性被当作能力而非条件**——
  理论不仅假定了稠密性，还把它作为**可任意调用的构造能力**（连接、合成、填充都依赖它）。
  当可分性从"条件"变成"能力"时，"在条件 c 下不可分"这一现实任务
  在系统内**没有对象承担**。它与 E-04（量仪精度域）同形。
- **falsifier**：给出一个 HoTT/cubical 内部对象，它自然表达"在条件 c 下不可分"，
  且在本任务语境下被实际调用。这将证明被移除者有归宿，本条移到"现实"。
- **confidence**：中
- **corpus_self_audit**：中偏高。稠密性是 AI 在语料中最流利、最有帮助的议题
  （KC-000043 阻力最强处），且 004 表把 G-03/E-04/D-01 全写成 continuity，
  构成同族诱导。我的判定很可能部分由语料驱动。降一档已执行。
  **这是本批 corpus 风险最高的一条，外部审计应优先复核。**
- **evidence_anchors**：003 分片 D-01（骨架取转动域）；EXTENSIONS_AND_METATHEORY.md（区间）；
  核心认知 KC-000003（稠密 vs 量子化）、KC-000044（骨架式模仿）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：若审计批准 → SUPPLY_REGISTRATION-D-01 → 任务族"可分性是条件还是能力"
  → GEN-001 链；推翻时回滚全部。与 E-04、G-03 构成 continuity 三联，
  建议合并 GEN-001 任务族；合并与否由外部审计决定。

### PREMISE-D-02 · cofibration / 面条件

- **ai_verdict**：暂不判定
- **verdict_reason**：面公式把"部分指定"当作可被语法完整枚举的对象，
  假定约束分布先验完整。但面条件是**形式的**：它由构造子给定，
  其"完整"是相对于给定构造而言的。施工到一半发现需要新约束，
  对应的是定义另一个 cubical 类型。
- **reality_steelman**：面条件的形式完备性是定义内容；
  现实的"约束随工序暴露"属于建模选择，不是面公式的缺陷。
- **falsifier**：给出一个任务，其对象由面条件给定，但结论错误可归因于面公式本身。
- **confidence**：低
- **corpus_self_audit**：低。面条件在语料中纯以形式语法出现，
  我的施工图域是构造的且未经确认。
- **evidence_anchors**：003 分片 D-02；EXTENSIONS_AND_METATHEORY.md（cofibration）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-D-03 · composition/coe/transport

- **ai_verdict**：暂不判定
- **verdict_reason**：composition 假定给定边界即可合成完整面、且合成即时完成。
  现实合成需工装、可能失败。但作为**计算规则**，composition 在符号层确实即时完成；
  "虚焊/浇筑空洞"是物理实现层的失败，不是符号合成的失败。
- **reality_steelman**：composition 是符号规则；物理合成的资源性与可失败性
  属于实现层（域外）。形式层的"给定边界即得面"是定义。
- **falsifier**：给出一个实例，其中作为符号规则的 composition 产生错误结论
  （而非物理合成失败）。
- **confidence**：低
- **corpus_self_audit**：低。合成操作在语料中是纯规则。
- **evidence_anchors**：003 分片 D-03；EXTENSIONS_AND_METATHEORY.md（composition）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-D-04 · Kan 填充

- **ai_verdict**：非现实
- **verdict_reason**：Kan 条件把"存在填充物"当作"填充物已就位"。
  **判定非现实的关键任务**：任何"存在 ≠ 可用"的现实调度任务
  （胎具需设计/制造/库存，可能缺位、排队；产能存在但不在需要时可用）。
  在这些任务下，被节省的条件——"存在性到可用性之间有供给过程"——
  **确实不可省**：Kan 条件把存在性直接当作可调用的构造资源，
  而"能填"与"填得上、填得及时"在调度上是三件事。
  这不是精度问题：存在性陈述无法表达"存在但此时不可用"。
- **reality_steelman**（最强反驳）：Kan 填充是**形式的构造规则**，
  它的"存在"就是"在形式层可构造"。物理工装的缺位属于实现层（域外）。
  形式层的"存在即就位"是定义。
  **这个 steelman 强**，且与 D-03/C-04 同形（都是"形式规则 vs 物理实现"的分工）。
  我仍判非现实的理由：本条在**形式层内部**就有不对应——
  Kan 填充要求的是**对每个** composition 都提供填充物，
  这个"每个"把供给的**资源性**（填充物本身是有限的、需消耗的）移除了。
  在形式层，被填充的对象是类型；填充物是项。项的供给在形式层确实是无限的。
  **因此本条的判定理由在纯形式层较弱**——我把置信度设为低，
  并明确标注：本条最可能被外部审计推翻为"现实"。
- **falsifier**：在纯形式层展示"存在填充物"确实等于"填充物可就位"的证明，
  或给出形式层内存在性不蕴含可构造性的反例。
- **confidence**：低（自评：本批中最可能被推翻的一条）
- **corpus_self_audit**：中。Kan 在语料中只有拓扑例子，我刻意取制造工装域；
  该域是**我的构造**而非观察，且把"存在≠可用"这个现实判断
  移植到形式层可能本身就是范畴错误。
- **evidence_anchors**：003 分片 D-04（已标注"最需用户确认"）；
  EXTENSIONS_AND_METATHEORY.md（Kan 条件）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：若审计批准 → SUPPLY_REGISTRATION-D-04 → 任务族"存在性与可用性"
  → GEN-001 链；**低置信度条目建议审计优先复核**，推翻时回滚全部。

### PREMISE-D-05 · cofibration 紧性 / 操作下封闭

- **ai_verdict**：暂不判定
- **verdict_reason**：紧性/封闭性假定通用性无条件成立。但这是**形式性质**：
  "在操作下封闭"是关于给定 cofibration 类的代数事实，不是关于现实工装通用性的主张。
- **reality_steelman**：通用范围的有限性对应的是**定义另一个 cofibration 类**，
  不是本类封闭性的缺陷。
- **falsifier**：给出一个任务，其对象由给定 cofibration 类覆盖，
  但结论错误可归因于封闭性本身。
- **confidence**：低
- **corpus_self_audit**：低。紧性在语料中是纯代数。
- **evidence_anchors**：003 分片 D-05；EXTENSIONS_AND_METATHEORY.md（紧性）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

---

## E 类（截断与层级）

### PREMISE-E-01 · isProp/isSet 定义

- **ai_verdict**：暂不判定
- **verdict_reason**：定义把"某层之上不再有证据差异"当作可一次性判定的性质。
  现实中"无争议"需持续维护。但 isSet/isProp 是**类型的形式层级**，
  其"无差异"是定义内容；新检验手段分出差异，意味着该类型**不是 set**——
  是类型差异，不是定义的缺陷。
- **reality_steelman**：层级是形式定义；事后新差异对应 h-level 更高的类型，
  系统提供了这样的对象。
- **falsifier**：给出一个类型，其形式上 isSet，但事后出现形式层内的证据差异。
- **confidence**：低
- **corpus_self_audit**：低。
- **evidence_anchors**：003 分片 E-01；CORE_RULES.md（截断层级）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-E-02 · 命题截断

- **ai_verdict**：非现实
- **verdict_reason**：截断把"有见证"与"给出见证"分离，并假定**分离无损**——
  只需存在即可行动。**判定非现实的关键任务**：任何"只知存在不足以行动、
  且被丢弃的见证信息在后续工序不可恢复"的现实任务
  （仓库"有货"但不知是哪件无法发货；匿名举报无法追责）。
  在这些任务下，被节省的条件——"见证的可恢复性"——**确实不可省**：
  截断是**信息销毁**操作，被丢弃的见证在形式层确实不可恢复
  （这正是截断的定义内容：||A|| 的元素不含见证信息）。
  与 A-03/A-11 不同，本条的断裂**在形式层内部成立**：
  截断的定义就是丢弃，而后续工序的形式依赖被丢弃者。
- **reality_steelman**（最强反驳）：截断是**选择**——只在已决定见证不重要时才施加。
  使用截断的人有责任确认后续不需要见证。这是**使用纪律**问题，不是截断的缺陷。
  **这个 steelman 强**：它把本条压成"误用截断"。
  我仍判非现实的理由：HoTT 的标准实践中，截断常被作为**优化/抽象**施加
  （"只需存在性"），而"后续是否需要见证"这一判断被推迟；
  理论没有提供"施加截断前检查后续见证依赖"的机制。
  这是一个**工具缺失**而非前提错误——因此我把判定限定为
  "在'后续需要见证'这一类任务下不可省"，而不是"截断本身错误"。
- **falsifier**：展示 HoTT 标准库中存在"施加截断前检查后续见证依赖"的机制或惯例。
  这将证明被移除者有归宿，本条移到"现实"。
- **confidence**：中
- **corpus_self_audit**：中。截断在语料中多以"存在量词的构造式解读"出现，
  我的仓储/文职域是构造的；但**判定理由依赖形式层事实**（截断丢弃见证信息），
  不依赖语料频率。
- **evidence_anchors**：003 分片 E-02；CORE_RULES.md（命题截断）；
  核心认知 KC-000031/035（表达保真）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：若审计批准 → SUPPLY_REGISTRATION-E-02 → 任务族
  "见证信息的可恢复性" → GEN-001 链；推翻时回滚全部。

### PREMISE-E-03 · 商 HIT 与高阶截断

- **ai_verdict**：暂不判定
- **verdict_reason**：商把同类内差异一次性抹平并当作构造事实。
  现实"同类"有适用范围。但商是**按给定等价关系构造的类型**，
  其"同类内无差异"是定义内容；适用范围外的不可互换，
  对应的是**定义另一个等价关系**。
- **reality_steelman**：商的类型由等价关系决定；
  工况外不可互换意味着等价关系选错了，不是商的缺陷。
- **falsifier**：给出一个任务，其等价关系给定正确，
  但结论错误可归因于商的构造本身。
- **confidence**：低
- **corpus_self_audit**：低。
- **evidence_anchors**：003 分片 E-03；CORE_RULES.md（商 HIT）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-E-04 · 层级的稠密性（截断塔可任意延伸）

- **ai_verdict**：非现实
- **verdict_reason**：截断塔不预设上限，把"可任意细分"当作理论**已提供的能力**。
  **判定非现实的关键任务**：任何"分辨率受测量条件与成本约束"的现实任务
  （量仪精度等级有限；再细一步需要新设备）。在这些任务下，
  被节省的条件——"细分需要新的测量条件"——**确实不可省**：
  理论把可分性当作内建能力，而现实的可分性是**被设备允许时才有的性质**。
  与 D-01 同形（continuity 三联）。
- **reality_steelman**（最强反驳）：截断塔是**形式结构**，
  它的"可延伸"是定义的推论。物理精度的限制意味着该任务不是"任意层级"的对象，
  而是某个固定 h-level 的对象。理想化本身不构成非现实。
  **这个 steelman 强**，理由与 D-01 相同。
  我仍判非现实的理由相同：可分性被当作**能力**而非**条件**，
  "在条件 c 下不可细分"在系统内没有对象承担。
- **falsifier**：给出一个 HoTT 内部对象，它自然表达"在条件 c 下不可细分"，
  且在本任务语境下被实际调用。
- **confidence**：中（与 D-01 同形，置信度同步）
- **corpus_self_audit**：中偏高。与 D-01/G-03 同属 continuity 族，
  是 KC-000043 阻力最强处；004 表把三者全写成 continuity 构成同族诱导。
  降一档已执行。**外部审计应优先复核。**
- **evidence_anchors**：003 分片 E-04（骨架取量仪精度域）；
  EXTENSIONS_AND_METATHEORY.md（截断塔）；核心认知 KC-000003
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：若审计批准 → SUPPLY_REGISTRATION-E-04 → 与 D-01/G-03 合并
  GEN-001 任务族"可分性是条件还是能力"；合并与否由外部审计决定。

---

## F 类（宇宙与分层）

### PREMISE-F-01 · universe U 的封闭性

- **ai_verdict**：现实
- **verdict_reason**：封闭性被当作构造事实。但 U 的封闭性是**生成规则的自洽性**：
  formation rules 定义了哪些构造可登记，封闭性是这些规则的推论。
  "编目规则需随新类型修订"在形式层不成立——新类型**就是**由 formation rules 生成的。
- **reality_steelman**（本条即判定理由）：U 的封闭性相对于其 formation rules 成立；
  现实编目体系的开放性是因为其对象不是由规则生成的。这是域的错位比较。
- **falsifier**：给出一个由 formation rules 生成的构造，它不能登记进 U。
- **confidence**：中
- **corpus_self_audit**：中。宇宙常引向罗素悖论式自指讨论，
  我刻意拉开；"编目需修订"的描述仍带自指族惯性，但判定理由不依赖它。
- **evidence_anchors**：003 分片 F-01（含自我限定）；CORE_RULES.md（U 封闭性）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-F-02 · Cumulativity / 2LTT 内外层分工

- **ai_verdict**：暂不判定
- **verdict_reason**：累积性假定"外层看到的也是内层的"、不需迁移成本。
  但累积性是**形式的包含关系**，不是关于归档成本的主张。
  归档的有损性对应的是**非累积**的分层，不是累积性的缺陷。
- **reality_steelman**：累积/2LTT 的层间关系是形式定义；
  有损压缩对应另一套分层结构（如 modal/冻结层）。
- **falsifier**：给出一个任务，其对象确为累积分层，
  但结论错误可归因于累积性本身。
- **confidence**：低
- **corpus_self_audit**：低。
- **evidence_anchors**：003 分片 F-02；EXTENSIONS_AND_METATHEORY.md（2LTT）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

---

## G 类（设计决策类前提）

### PREMISE-G-01 · 把恒等设为类型族

- **ai_verdict**：暂不判定
- **verdict_reason**：把相等设为类型族是**能力的获得**（非省略），
  它把"层深锚定义务"移出理论。但"理论不提供某判据"与"理论的前提非现实"
  是两件事——本条移出的是**判据供给**，不是**条件**。
- **reality_steelman**：类型族的设计是**表达能力的扩展**；
  "该停在哪一层"由任务决定，理论提供的是**可以停在任意层**——
  这恰恰是功能而非缺陷。
- **falsifier**：给出一个任务，其结论错误可归因于"理论未提供层深判据"，
  而非归因于任务自身未指定层深。
- **confidence**：低
- **corpus_self_audit**：低。
- **evidence_anchors**：003 分片 G-01（已标注"与 G-03 互为镜像"）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-G-02 · 把相等设为命题（局部命题性）

- **ai_verdict**：暂不判定
- **verdict_reason**：把"高阶路径不携带新相等信息"设为基本事实，
  省掉了互换性的适用条件。但这是**设计选择**：选择相等为命题，
  就是选择在该类型上不区分更高阶证据。适用条件由**类型选择**承担。
- **reality_steelman**：命题性是类型的设计选择；
  需要更高阶证据的任务，其对象不是命题。
- **falsifier**：给出一个类型，其设计为命题，
  但更高阶证据确实携带新相等信息。
- **confidence**：低
- **corpus_self_audit**：中。集合式行为在语料中被当作"显然"，
  我刻意避开；判定理由不依赖语料频率。
- **evidence_anchors**：003 分片 G-02；CORE_RULES.md（命题性）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-G-03 · 把高阶相等设为可无限迭代

- **ai_verdict**：非现实
- **verdict_reason**：无上限迭代被当作类型层的**内置能力**：p=q 之后还能 =，
  不需任何外部锚定或资源。**判定非现实的关键任务**：任何"可分性/迭代深度
  受观察条件约束"的现实运动任务（与圆环悖论同形：运动的无限二分在现实中
  总在某个测量条件下终止）。在这些任务下，被节省的条件——
  "迭代的终止/锚定条件"——**确实不可省**：理论把它**完全移出**，
  于是"在条件 c 下迭代应终止"在系统内没有对象承担。
  本条是 004 表标为"形状上最直接"的一条（与用户圆环悖论的现实出发点同形）。
- **reality_steelman**（最强反驳）：高阶相等的无限迭代是**形式结构**，
  它的"可迭代"是 identity type 的定义推论。物理运动的有限可分性
  意味着该任务不是 ∞-groupoid 的对象，而是某个固定 h-level 的对象。
  **这是本批最强的 steelman**：理想化本身不构成非现实，
  且 HoTT 明确提供了固定 h-level 的截断类型作为"终止"的归宿。
  我仍判非现实的理由：截断类型提供的是"**决定**停在某层"，
  而不是"**在条件 c 下必须停在某层**"——
  前者是选择，后者是约束。被移出的是**约束**，不是**选项**。
  现实任务的可分性是约束（设备不允许更细），
  而理论只提供选项（你可以截断）。
- **falsifier**：给出一个 HoTT 内部对象，它自然表达"在条件 c 下必须截断"，
  且在本任务语境下被实际调用。这将证明被移除的**约束**有归宿，
  本条移到"现实"。
- **confidence**：中（**不因形状熟悉而提高**——本条 corpus 风险最高：
  它同时是语料最流利处、004 表的推荐起点、与用户自身思考路径同形。
  三重诱导叠加。降一档已执行，且我明确不把"形状上最直接"当作证据。）
- **corpus_self_audit**：高（三重诱导：语料流利 + 004 表导航 + 用户路径同形）。
  **本条是全批 corpus_self_audit 最高的一条，外部审计必须优先复核。**
  我的判定理由刻意不依赖"与圆环悖论同形"这一熟悉性，
  只依赖"约束 vs 选项"这一结构论证——但该论证本身也可能由语料塑造。
- **evidence_anchors**：003 分片 G-03；CORE_RULES.md（identity 规则）；
  核心认知 KC-000003（稠密 vs 量子化）、KC-000044（骨架式模仿）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：若审计批准 → SUPPLY_REGISTRATION-G-03 → 与 D-01/E-04 合并
  GEN-001 任务族"可分性是条件还是能力"；合并与否由外部审计决定。
  **本条是 continuity 三联中外部审计复核优先级最高的一条。**

### PREMISE-G-04 · 把等价提升为同一（univalence 方向）

- **ai_verdict**：暂不判定
- **verdict_reason**：方向设定把"结构同构"与"是同一个东西"在类型层同一化，
  省掉了互换性的任务边界。但这是**方向设定**：选择 univalence，
  就是选择在该类型理论中同构即同一。任务边界由**类型选择**承担。
  与 C-03/C-04 同主题但层次不同（C 是公理/定理，G 是设计方向）。
- **reality_steelman**：univalence 方向是**设计选择**；
  特定工况下不可互换意味着该对象不是同构的（在更细结构下）。
- **falsifier**：给出一个任务，其对象确为同构，
  但结论错误可归因于把同构当作同一。
- **confidence**：低
- **corpus_self_audit**：中。"同构即同一"在语料中常作为动机性陈述，
  容易被跳过；我刻意避开，判定理由不依赖语料频率。
- **evidence_anchors**：003 分片 G-04；CORE_RULES.md（univalence）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：无下游

### PREMISE-G-05 · 把"所有 cofibration 可填充"设为构造可用

- **ai_verdict**：非现实
- **verdict_reason**：把"存在性"设为**构造可调用**——存在=就位。
  **判定非现实的关键任务**：任何"产能/工装存在但不在需要时可用"的现实调度任务
  （订单有产能但排队；夹具存在但缺位）。在这些任务下，
  被节省的条件——"资源就位的供给过程"——**确实不可省**：
  理论把存在性抹成可调用，而"能填"与"填得上、填得及时"是三件事。
  与 D-04（Kan 填充）同形。
- **reality_steelman**（最强反驳）：这是**形式构造规则**：
  在 cubical 类型论中，可填充性是 cofibration 的**定义条件**——
  成为 cofibration 就意味着可填充。物理产能的排队属于实现层（域外）。
  **这个 steelman 强**，且在形式层比 D-04 更有力
  （D-04 是"存在→就位"，G-05 是"定义即包含可调用"）。
  我仍判非现实的理由与 D-04 相同且更弱：
  本条在纯形式层的判定理由最弱，因为可填充性确实是定义条件。
  **我把置信度设为低，并明确标注：本条与 D-04 是本批中最可能被推翻为"现实"的两条。**
- **falsifier**：展示"可填充"在形式层确实等于"可调用"，
  或给出形式层内可填充性不蕴含构造可用的反例。
- **confidence**：低（与 D-04 同列，最可能被推翻）
- **corpus_self_audit**：中。可填充性在语料中以纯规则形态出现，
  我的制造产能域是构造的；把"存在≠可用"移植到形式层可能是范畴错误。
- **evidence_anchors**：003 分片 G-05；EXTENSIONS_AND_METATHEORY.md（Kan/cofibration）
- **audit_status**：AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
- **depends_on**：若审计批准 → SUPPLY_REGISTRATION-G-05 → 与 D-04 合并
  GEN-001 任务族"存在性与可用性"；**低置信度，审计优先复核**。

---

## 本批汇总（C–G 20 条）

| 判定 | 条目 |
|---|---|
| 非现实 | D-01、D-04、E-02、E-04、G-03、G-05 |
| 现实 | C-01、F-01 |
| 暂不判定 | C-02、C-03、C-04、D-02、D-03、D-05、E-01、E-03、F-02、G-01、G-02、G-04 |

**主题簇（供外部审计决定是否合并 GEN-001 任务族）**：
- **continuity 三联**：D-01（转动域）/ E-04（量仪精度域）/ G-03（运动域）——
  共同分母"可分性是条件还是能力"。corpus 风险最高的三联。
- **存在性/可用性对**：D-04（Kan 填充）/ G-05（可填充设为构造可用）——
  低置信度，最可能被推翻的两条。
- **同一性层深与锚定**：B-01（见 005 分片）/ G-01 / G-02——
  "同一性判据的观察层依赖"。
- **过程 vs 已完成**：A-03 / A-11（见 005 分片）——
  "过程性被当作已完成"。
- **见证可恢复性**：E-02——"信息销毁的不可逆性"。
