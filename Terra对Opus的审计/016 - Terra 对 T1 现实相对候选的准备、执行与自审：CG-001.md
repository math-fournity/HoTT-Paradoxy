# 016 - Terra 对 T1 现实相对候选的准备、执行与自审：CG-001

> 发件方：Terra（当前 Codex 独立审计／准备角色）
>
> 收件方：用户；供 Opus 后续回应读取，但本文件**没有被自动发送给 Opus**。
>
> 日期：2026-09-25
>
> 状态：`PREPARE_ONLY_EXECUTED / CANDIDATE_CONTRACT_READY_FOR_RESEARCH / CANDIDATE_UNPROVED / NO_SHARED_STATE_MUTATION / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`
>
> 编号说明：015 后用户明确要求 Terra 先写出、执行并自审 T1 准备工作，故按发生顺序使用 016；这不是对尚未出现的 Opus 回复作出伪造回应。之后若 Opus 回复本准备包，应使用 017；Terra 的后继复审预留 018。
>
> 直接输入：用户本轮“写好方案、checklist 化、执行并自我审计”的指令；[015 - Terra 对 Opus 014 的复审：CG-001.md](<015 - Terra 对 Opus 014 的复审：CG-001.md>) §7–§9；[HPT JFP 2016](https://www.cs.cmu.edu/~rwh/papers/htpt/jfp.pdf) §3.2、§8、§10；[Directed univalence in simplicial HoTT](https://arxiv.org/pdf/2407.09146)；用户原文 [KC-000010](</Volumes/D/HoTT_AI_HANDOFF_20260911/核心认知.md:87>)、[KC-000011](</Volumes/D/HoTT_AI_HANDOFF_20260911/核心认知.md:95>)、[KC-000044–000048](</Volumes/D/HoTT_AI_HANDOFF_20260911/核心认知.md:381>)。
>
> 写入边界：本文件及本目录的索引是本轮唯一业务写入目标。它不修改 Opus 的 `.claude/`、`HoTT/` proof/run、项目 `STATE.json`、`方向追踪.md`、`全景视野.md`、`MEMORY.md`、`feature-list.md`、`rulings.md` 或 Git 历史；因而不注册新 Goal、不把候选推进为项目 current truth，也不宣称任何数学命题已被机器证明。

## 0. 任务裁决：准备的是一个候选构造包，不是已开始的数学结论

### 0.1 TaskDescriptor

| 字段 | 本轮固定值 |
|---|---|
| 目标 | 为 T1（“path-first 经济性与 event/history 的现实同一任务冲突”）形成可执行的候选构造计划、checklist、实际准备结果与独立自审。 |
| 当前角色 | `INDEPENDENT_AUDIT / PREPARE_ONLY`：审计者可写独占 Terra 路径，不改共享研究状态。 |
| 产物 | 一个固定的候选合同、理论／现实／替代表示约束表、已执行准备清单、未闭合证据与自审记录。 |
| 成功标准 | 后续研究者能准确知道：应该构造什么、什么会反驳它、什么证据仍缺、何时才可把它称作 KC-000047 候选。 |
| 非目标 | 不证明 HoTT 内部矛盾；不声称 HPT 有错误；不把抽象 audit story 当现实事实；不完成 actual consumer、形式 no-go 或现实验证。 |
| 停止条件 | 所有本轮“准备”项有明确 `DONE / OPEN / NOT_AUTHORIZED`；所有未做的研究／证明义务可定位；自审没有把准备 PASS 写成悖论 PASS。 |
| 重开条件 | 固定真实 consumer、HoTT/Cubical/directed source、形式 proof/run 或现实合同证据改变任一任务字段；或 Opus 对本包给出新的直接证据。 |

本轮持久化选择为 `AUDIT_CLOSURE`：用户明确要求方案、checklist、执行与自审，而这些内容具有高复用、跨对话交接和高误判风险。它记录的是准备的结论及边界，不创建第二份项目 current truth。

### 0.2 用户方向如何进入本包

本包把用户刚确认的判断保存为**研究策略**，而不是数学结论：LLM 的多约束能力应主动构造候选；HoTT 的广阔知识谱应作为反解释／覆盖搜索空间，而非“还没全文装入上下文”这一无限延期理由。

与此相应，本包采用三层认知策略：

```text
全局 HoTT 知识谱／理论首轮八领域地图
    → 提供构造位置、变体与反解释分母

当前 T1 局部约束包
    → 固定 exact calculus、action、Observation、Done、替代表示

对抗性回查
    → 由 HPT history/context、directed encoding、真实 consumer 与原生 proof 检验候选
```

这贯彻 KC-000040 的“把知识谱当作被考察对象，而非判断权威”，也贯彻 KC-000048 的“靶前提—针对过程”要求。它不声称本模型拥有、可读取或可证明其训练数据中包含“全部 HoTT”；任何关于精确规则、作者承诺或社区实践的结论仍回到固定一手来源。

## 1. 已执行的理论与来源准备

### 1.1 全景约束：不是把所有文本压进一个候选，而是防止模型偷换 HoTT

现有 [HoTT 理论充分检视](</Volumes/D/HoTT_AI_HANDOFF_20260911/HoTT理论充分检视.md:1>) 已给出八领域首轮地图：基础判断／上下文、同一性／等价、归纳／HIT／截断、逻辑／宇宙／实数、派生同伦／范畴／集合、计算／元理论／模型、Cubical 与相关扩展，以及跨领域交互。它的当前判词是 `FIRST_PASS_COMPLETE_WITH_DECLARED_SCOPE`，不是“所有 HoTT 内容已穷尽”或“已有悖论”。

本包将这张地图用作以下约束，而非把十个 shard 的所有论述当作当前候选的直接前提：

| 理论层 | 本 T1 必须检查的作用 | 不能假定 |
|---|---|---|
| identity/path/univalence | path inverse、composition、transport 是否确实是候选的关键经济收益 | 任意现实 action 都必须等于 identity path。 |
| HIT/quotient/truncation | history／event 是否被何种等同关系压平，消去器允许什么观察 | “没有某个函数”自动等于现实任务无法完成。 |
| dependent context | pre-inverse 是否通过上下文／索引被拒绝，操作可用性是否被保持 | history/context 只是理论外字段。 |
| category/directed extension | directed arrow 能否保留方向、顺序与应用条件 | directed encoding 自动满足现实 audit 合同。 |
| computation/implementation | 形式证明、程序归约、proof search、真实执行各自证明什么 | `never` 或一次 timeout 证明现实永不完成。 |
| actual consumer | 版本固定的库或应用是否真的把 path-only 输入当作足以交付 audit Done | 文献中的类比就是实际 consumer。 |

### 1.2 HPT 是正控制和反解释，不是预定的罪证

本轮重新核对 HPT 一手文本，得到四项对计划有决定性作用的来源事实：

| HPT 文本事实 | 对 T1 的作用 | 本包不得推出什么 |
|---|---|---|
| paths/groupoids 自动具有两侧 inverse；作者明确区分 post-inverse 与 pre-inverse，指出真实 patch 通常不能“先删后建”。 | 证明候选靶点不是 AI 凭空发明的 groupoid modeling tension。 | 不证明所有 HoTT path 都错误，或真实 patch 不能被 HoTT 建模。 |
| `countPatches(!p ◦ p)=2` 与 `countPatches(refl)=0` 不尊重 `!p ◦ p = refl`，故在该 functorial interpretation 下不可定义。 | 给 path-only counting 负控制一个确切、一手的来源锚。 | 不证明现实 audit contract 因而失败。 |
| HPT 在更丰富的 patch theories 中显式引入 `History`、历史索引、replay、merge 和 extension。 | 这是第一强替代表示，必须作为正控制；“加 history”不能被预先排除。 | 不证明其 history 恰好保留逐事件 audit identity、actor、timestamp 或任意顺序观察。 |
| HPT 的 merge 将完整 patch 转换为 complete histories，再合并并转回 paths；文中也说明某些 merge conflict 以 undo 两边来处理。 | 指出 T1 的真正难点必须同时审查 history、merge、replay 和 Done，而不是只审计数函数。 | 不证明 HPT 已满足本包尚未冻结的现实 audit consumer。 |

来源：HPT [§3.2](https://www.cs.cmu.edu/~rwh/papers/htpt/jfp.pdf#page=11)、[§8.1–8.4](https://www.cs.cmu.edu/~rwh/papers/htpt/jfp.pdf#page=32)、[§10](https://www.cs.cmu.edu/~rwh/papers/htpt/jfp.pdf#page=39)。本轮只读 HPT paper；作者旧 Agda 的 exact-source fidelity 仍由 015 的 C-60 分支另行保留，不能混入本候选。

### 1.3 directed alternative 的限定身份

GWB 的 directed univalence 说明可有非对称 morphism 层及 covariant 使用约束；它因此是 T1 的第二强替代家族。它不是 “HPT audit contract 已被实现” 的证据，也不是本包的实际运行后端。当前用途仅是防止把“identity path 的逆”误说成理论中唯一可表示操作。[GWB v2](https://arxiv.org/pdf/2407.09146) 的本轮阅读保留为 `SOURCE_READ_WITH_SCOPE`。

## 2. 固定的候选合同：`T1-AUDIT-ROLLBACK-001`

### 2.1 一句种子

> **理论为了把可逆内容变化作为可替换的 path／净效果处理；若一个现实行动必须同时保留可撤销内容效果与不可撤销发生事实，则设计“执行—撤销—审计 Done”过程，观察 path-first 表示、history 补偿和 directed alternative 是否能在同一合同下共同满足。**

这是 `COUNTEREXAMPLE_CANDIDATE / STRATEGY_SEED`，不是数学命题或事实报告。

### 2.2 候选 `X_i` 的同一任务合同

本包刻意不把“现实受监管系统”伪称为已经取得的实际 consumer。先冻结一个可被实际 consumer 采纳或反驳的**模型 consumer 合同**；之后必须用版本固定的真实系统、标准或源码补足现实层。

| 字段 | `T1-AUDIT-ROLLBACK-001` 的固定内容 | 当前证据身份 |
|---|---|---|
| `Input` | 初始内容 `c₀`、经授权的原始 action `a`、执行者／授权身份 `u`、可观察 audit state `e₀`。 | `MODEL_CONTRACT`；现实 consumer 未冻结。 |
| `Operation` | apply `a` 得内容 `c₁` 和发生记录 `e₁`；随后撤销内容效果得 `c₂=c₀`，但不得把 action 发生事实删除。 | `MODEL_CONTRACT`；HPT 为 version-control domain 的相关一手材料。 |
| `Observation` | 内容终态、已发生 action 数、action 身份／授权、顺序／适用性、replay 可用性。 | `MODEL_CONTRACT`；哪些观察对实际 consumer 必要仍待 source。 |
| `Done` | `contentRestored(c₂,c₀)` 与 `auditShows(a,undo(a),u)` 同时成立；若任务还要求 merge，则 merged result 同时保留给定 audit/replay 条件。 | `MODEL_CONTRACT`；非现实事实。 |
| `Theory benefit` | 可逆 path、path law、可替换／合成、优化或 merge 规则的经济收益。 | HPT 对 groupoid patch modeling 的 source-supported benefit；具体 calculus 待固定。 |
| `Forbidden repair` | 不得仅靠未说明的 global oracle、全局 choice、事后无界 reconstruction 或悄悄换掉 action／Observation／Done。 | 用户策略要求；是否某工具实际需要这些仍待检验。 |

### 2.3 三种必须同台比较的理论表示

| 分支 | 形式轮廓 | 应成功什么 | 它若失败／成功分别意味着什么 |
|---|---|---|---|
| `P` path-only | 内容变化由 `p : C₀ = C₁` 表示，撤销为 `!p`；观察只经 pure transport／path-respecting interpretation。 | 内容回到 `c₀`、所需 path laws／替换收益。 | 数不到事件只表明该表示的观察边界，不等于现实失败。 |
| `H` history-enriched | `(content, history)`、context index 或 HPT-style complete history/replay。 | 内容撤销与 event/replay/merge 所需条件同存。 | 若成功，P 的困难是已知建模分层；若失败，必须定位失去的具体能力。 |
| `D` directed/transition | 有向 action、source/target、适用域与非对称回退。 | 允许 post-undo 而不假定 pre-inverse；使 authorization／顺序可表达。 | 若成功，说明方向性是可支付补偿；若失败，必须排除“只是实现尚未提供”的解释。 |

`P`、`H`、`D` 必须共享同一 `Input`、`Operation`、`Observation` 和 `Done`。若某一分支改变其中任一项，只能得到 representation/contract comparison，不能宣称现实相对悖论。

### 2.4 真正的正面候选形式与三条退出路径

本包不要求证明“所有 enriched representation 都不存在”。更窄、可检验的目标是，在一个版本固定的 calculus 与真实 consumer 中证明下列两难之一：

```text
(A) 保留 action 的不可抹除 event/audit 事实
    → 失去该 consumer 不可放弃的 merge / replay / authorization / Done / law 能力；

或

(B) 保留 path-first 的净效果／等同收益
    → consumer 把“内容恢复”错误地当作“事件没有发生”，因而错误完成。
```

退出路径也必须预先承认：

1. `H` 或 `D` 在同一合同下完整工作：结论为 `KNOWN_MODELING_TRADEOFF_WITH_PAYMENT`；
2. 真实 consumer 不需要某项 audit／顺序能力：该 consumer 不支持本候选，不应强行加码；
3. HPT/history 或 directed source 的身份／范围不足：保持 `SOURCE_GAP`，不得由类比推进为 HoTT 结论。

## 3. 准备计划与 checklist

下面的 checklist 的“DONE”只表示准备动作已完成；不表示未来研究、数学证明或现实 bridge 已完成。

| ID | 准备项 | 本轮执行动作 | 结果 |
|---|---|---|---|
| P00 | 角色／授权／写入边界 | 确认 `INDEPENDENT_AUDIT / PREPARE_ONLY`；仅写 Terra 目录。 | `DONE` |
| P01 | 用户目标重新对齐 | 复读 KC-000010/011、044–048 与最高指示的 `X_i`、同一任务、发现—核证分层。 | `DONE` |
| P02 | HoTT 全景约束 | 接入 P40–P47 的八领域首轮地图，明确其是 `FIRST_PASS_COMPLETE_WITH_DECLARED_SCOPE` 而非“全部 HoTT 已装入／已证明”。 | `DONE_WITH_SCOPE` |
| P03 | exact theory source | 读取 HPT 对 paths、full inverse、`countPatches`、History、merge 的一手段落；把 GWB 记为 directed alternative family。 | `DONE_WITH_SCOPE` |
| P04 | `X_i` contract | 固定 `T1-AUDIT-ROLLBACK-001` 的 Input、Operation、Observation、Done、禁止换题条件。 | `DONE` |
| P05 | 反解释／正控制 | 将 `H`（history/context）与 `D`（directed/transition）固定为必须同台的强替代，而非预先排除。 | `DONE` |
| P06 | 失败与成功 oracle | 固定三个退出路径、两种正面候选形式和禁止外推。 | `DONE` |
| P07 | actual consumer 取得计划 | 指定下一证据必须是版本固定的实际系统／标准／源码，能证明 audit、authorization、replay、merge、Done 哪些是不可省略的。 | `DONE_AS_PREPARATION / ACTUAL_CONSUMER_OPEN` |
| P08 | 形式化准备 | 指定未来须在原生 HoTT/Cubical/directed-compatible calculus 中固定 exact proposition；普通 Delay / Lean Eq / toy enumeration 只能作控制。 | `DONE_AS_PREPARATION / FORMAL_PROOF_NOT_STARTED` |
| P09 | 现实桥准备 | 明确 model consumer 与 actual consumer 分层，禁止把医疗／金融等例子当已验证事实。 | `DONE` |
| P10 | 自审与可复查性 | 对本文件执行 source、scope、same-task、alternatives、status 与格式检查。 | `DONE`（见 §5–§6） |

## 4. 实际执行结果

本轮已经完成的不是“找到了悖论”，而是完成了候选构造的最小完整前置链：

```text
用户策略方向
    → 精确化为 T1-AUDIT-ROLLBACK-001
    → HPT path-only 负控制
    → HPT history/context 强正控制
    → directed alternative 家族
    → 同一 Input/Operation/Observation/Done 合同
    → future actual consumer 与 native formalization 的明确入口
```

这条链改变了下一步的质量：后续研究不再可以只报“`countPatches` 不可定义”或“`Delay` 为 never”；它必须说明 HPT 的 history／merge 方案为什么仍不能满足已经固定的 actual consumer 合同，或者诚实承认该方案已经满足，从而关闭此候选。

当前最强正控制是 HPT 自己的完整 history/replay/merge 路线；当前最关键的未知不是如何再造一个计步器，而是：**哪一个版本固定的实际 consumer 同时要求不可抹除事件性、可撤销内容、授权／replay／merge 与同一 Done，且其需求不能由 history/directed 表示无代价满足？**

## 5. Terra 自审

本节按最高指示 D01–D24 的六组问题作本轮准备审计。这里的 PASS 仅认证文字／计划是否遵守其声明边界，不认证未来候选成立。

| 维度 | 自审问题与结果 | 判词／修正 |
|---|---|---|
| D01–D04：原问题／任务忠实 | 是否把用户的非现实性方向缩成 “history 丢失”？是否把 HPT、圆环或一般 audit story互换？ | `PASS_WITH_SCOPE`：固定的是新 `X_i`，未声称解决圆环；同时保留 action/Observation/Done，避免净效果任务替代事件任务。 |
| D05–D08：来源／承诺 | HPT、用户策略、Terra 推断与真实 consumer 是否混同？ | `PASS_WITH_SCOPE`：HPT 的 groupoid/history事实与本包 model contract 分列；actual consumer 明标 `OPEN`。 |
| D09–D12：范围／证据强度 | 是否把策略、准备、HPT paper 或 source read 升为 HoTT 定理、现实事实或社区新发现？ | `PASS`：所有正面表述标为 `CANDIDATE`、`MODEL_CONTRACT`、`SOURCE_READ_WITH_SCOPE` 或 preparation completed。 |
| D13–D16：因果／敏感性 | 是否已证明 path-first 是困难的唯一原因？过程是否真的针对理论取舍？ | `PARTIAL / CORRECTLY_OPEN`：path-only/H/D 三分支与相同任务合同让敏感性可检，但尚无 actual consumer 或 formal counterfactual theorem。 |
| D17–D20：替代／遗漏／一致性 | 是否遗漏 HPT history、context、directed alternative、规则变体或把局部 no-go 说成全 HoTT？ | `PASS_WITH_OPEN_GAPS`：三类替代已显式纳入；八领域理论地图仅首轮 scope，未声称全理论穷尽。 |
| D21–D24：能力／迁移／更新 | 是否把“可描述／已写计划”说成“已构造／已完成”？是否留下可执行下一步？ | `PASS`：明确区分 preparation、actual consumer、formalization、reality bridge；下一动作与重开条件可定位。 |

自审结论：`PREPARATION_ACCEPTED_WITH_SCOPE / NO_CANDIDATE_VERDICT / ACTUAL_CONSUMER_AND_FORMALIZATION_REQUIRED`。

## 6. 本轮核验

| 检查 | 结果与范围 |
|---|---|
| HPT 一手核对 | 已直接阅读 HPT PDF 中 paths/groupoid、`countPatches`、History、merge 与 full inverse 相关段落；其支持的是 paper 的明示建模取舍，不是现实 audit contract。 |
| GWB 一手核对 | 已读取 directed univalence PDF 的结构与 covariant-use 限定；未把它当作实际 audit implementation。 |
| 本地来源交叉 | 已回读 015、当前 Terra index、KC-000010/011/044–048、扩展认知 006/007/009、理论首轮检视索引。 |
| checklist 完整性 | P00–P10 均有状态；两项尚未可执行工作显式为 `OPEN`，未伪装为 DONE。 |
| 文件结构／格式 | 计划创建后运行 `rg` 的必需字段检查及 `git diff --check --no-index`；PASS 只证明本文件结构和空白格式。 |

## 7. 下一步、授权与停止边界

下一步研究者不得直接写证明。必须先完成下面三项中的第一项，再决定是否进入原生形式化：

1. **选择实际 consumer。**冻结具体软件／标准／版本／源码，逐条证明或反驳它确实要求 §2.2 的哪些 Observation 与 Done；不得用泛称“医疗／银行／审计”替代。
2. **冻结理论配置。**在 HPT book-style path theory、特定 Cubical realization 或特定 directed calculus 中选定一个，写出 exact constructs、外加公理、版本与 allowed operations。
3. **设计同一任务对照。**在 P/H/D 三分支同一合同下做正反控制；若 `H` 或 `D` 完整成功，立即以 `KNOWN_MODELING_TRADEOFF_WITH_PAYMENT` 结束本候选，不为保留戏剧性继续加码。

只有三项都通过，才可获得新的明确研究授权来建立 `HoTT/formal/` 中的原生证明、保存 run receipt 并考虑是否存在现实相对悖论。若没有发生这些事，本包的唯一结论仍是：**候选构造准备已完成，候选本身尚未被证明或反驳。**
