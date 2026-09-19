# 交接阶段经验

1. “用户提问已提取”不等于“AI 回答、工具事件、代码和 Git 已审计”；必须分开建立 ledger。
2. LocalGPT 的父线程和 HoTT-2 子线程不能用一个文件的数量替代 38-turn lineage；同一用户内容的重复和补充要显式标识。
3. WebGPT 的 workspace 快照是历史来源；其 `STATE`、R、SESSION 和 Git 需要重新绑定到顶层 repo，不能直接当作当前状态。
4. Gemini 的 `inlineFile` 是代码载荷，不能因为旧报告的摘要而分类成空记录；Drive 文档正文缺失必须保留缺口。
5. `/Volumes/D/ALL-Markdown/aistudio-docs/` 被用户移走是有效边界；替代文件是否覆盖原目录是待证事实，不是文件名可以解决的语义问题。
6. 核心认知的编号/hash/定位可以机械验证；是否深化、纠偏或偏航仍需当前 AI 写逐编号公开评估。
7. 22,226 条来源行可以全部登记而不等于 22,226 条语义已经人工判定；register 的 locator/ID/规则依据必须与 `PENDING_DIRECT_SENTENCE_ADJUDICATION` 同时保留。
8. 理解章节的逐文件“合并”可以安全地先形成 canonical 选择和 rollback receipt；保留 nested 源比未经授权删除更重要，line diff 也不等于数学内容等价。
9. core 当前代必须由人工 curation + canonical manager 生成；任何用户新悖论/元数学原文进入新 generation，旧代由 tag/transition 保留，不能手工编辑生成物。
10. full EOF/hash、checkpoint、Git commit 和测试都不能认证模型理解；`model_context=NOT_CERTIFIED_BY_TOOL` 是必须保留的真实边界。
11. `role=user` 只证明消息由用户通道发送，不证明其中每段都是用户原创；Response annotations、转发信件、复合 briefing 必须逐项区分，不能把 AI 文字注入 core。
12. “core 必须全文加载”保护的是用户定义的当前逻辑文档，不保护旧生成器的错误边界；重建可缩小当前输入，但必须精确原文、逐消息 disposition、完整迁移和可回滚历史。
13. `evidence_status=REVIEW_REQUIRED` 不等于 `lifecycle_status=ACTIVE_WORK`。把二者混成一个 status 会让历史 Session/逐-KC表永久复活并形成自激压缩循环。
14. 失败要按责任点记录：错误 unittest 入口不是测试失败；旧 2115 行下限是坏 oracle；旧 payload 含 `---` 使“完全相等”预期错误。修命令/规格后复跑，不能改数据求绿。
15. 一个 compatibility runtime 副本若可直接路由到 canonical 实现，就不应长期维护第二份独立代码；路径兼容和真值唯一可以同时成立。
16. core 换代后必须让 direction→core 主题通过当前 manifest 集合校验；只更新主要结果行仍可能留下一个旧标签，负向 validator 应使这种残留 fail closed。
17. 已退出 current truth 的文档 rename 归档时，必须迁移当前 README/方向/STATE consumer 与 replacement；不可变 checkpoint 中的旧路径保留为当时证据。原始 pack 的 `archive/` 与叙事治理史的 `history/` 职责不同。
18. 分项测试已从 3 增至 4 时，suite PASS 与 projection revision PASS 仍可能遗漏 MEMORY 的旧计数；current narrative lint 应核 stable 测试锚点，但不能把自由文本检查扩张为数学语义裁判。
19. `different_pairs` 只能计数双方都存在且不同的同名对；单侧独有项应另计，并可用 `nonidentical_union_entries` 表示整个 union 中的非 identical 项，不能用一个含糊字段同时承担两种分母。
20. R 编号不是跨工作区全局身份：workspace 的 R041 是 ZCode 治理接入，用户后来导出的数学 R041 是 bind/race 研究；必须绑定路径、hash、基线、commit 和容器，不能仅凭编号合并。
21. 一份 Web 页面导出的 PROOF_NOTE 可以把 AI 自述升级为可审读纸笔来源，但不能替代其声称的源码、测试原始输出和 Git object；正文取得与执行谱系取得要分列。
22. 部分计算抽象应以操作闭包成对审查：bind 是尊重结果等价的正向控制，race/timeout 是读取完成先后的负向探针；正向 monad 构造和现实相对使用桥梁不是同一成果。
23. “HoTT 解决悖论”至少要拆成 formation 拒绝、概念区分、显式结构建模、一般界限继承和现实解释开放；把五类压成一个“解决了”会同时高估 HoTT 和抹去用户问题。
24. 在 `理解章节/` 新增 current C 系列文档会真实改变 merge inventory；必须同轮重建 manifest、更新全景计数并重跑 projection freshness，不能让旧 25/24 收据继续证明新增后的目录。
25. “战略上最重要”与“下一个最可执行”不是同一排序：W51×RP-B01×自指更接近最终理论目标，而 R041 partiality 操作闭包的证据链更成熟，适合先建立完整研究样板；必须显式区分，避免用成熟度覆盖目标价值或用目标价值掩盖证据缺口。
26. 后续候选应按资格保持性判别，并分成 `DEFENSE_WORKS`、`REPRESENTATION_BOUNDARY`、`NATURAL_USAGE_MISMATCH`、`INTERNAL_INCONSISTENCY`；商拒绝非同余 race、截断拒绝取见证或提取器拒绝经典项时，这是理论防御证据，不能绕过规则制造悖论。
27. “一个有限证明可检查/一个系统有归一化”与“所有命题可自动决定/理论能证明自身整体可靠”属于不同层次；若不先拆 V1–V5，会把正面元理论结果和哥德尔边界写成伪矛盾。
28. 理论经济必须相对于任务族定义：`J` 通过 `α` 分解才是抽象对该任务充分；非单射抽象并非对所有任务失败，但必有观察能击穿其全局无损声明。
29. 省略、商去、逻辑否定和理想化添加是四种不同理论操作；“理论中不存在 F”与“理论断言 ¬F”不能互换。用户的存在/不存在双视角应作为现实相对语义保留，而非无条件对象逻辑等价。
30. core generation 更新和 STATE checkpoint 存在双资源过渡：先生成新 core 会让旧 STATE 的动态 generation 校验失败。runtime 3.1 只在给出 manifest+transition、旧/新 generation 和零 remainder 的窄迁移声明时允许 checkpoint 建立基线；普通 Session 仍 fail closed。
31. `FactorsThrough(α,J)` 无条件推出 `FiberConstant(α,J)`，逆向却依赖像/商的消去泛性质、截面或选择；非单射也不保证对任意固定余域 Y 都有区分观察（subsingleton Y 是立即反例）。全局经济 no-go 必须显式量化 separating observation family，或允许 Y=R 与 J=id。
32. 最小反例中的乘积 `A×S` 需要实际给出 `a₀:A`；仅有 `s₀≠s₁:S` 在 A 为空时不能产生一对现实状态。有限任务族也不使函数相等或 factorization 自动可判定；可执行模型必须另给有限类型、可判定相等或具体枚举器。
33. 数学结论交付必须把自然语言命题、形式命题、proof source、匹配语义的 kernel run、原始输出和 claim index 绑定；代码存在、有限测试、外部论文、旧 aggregate receipt 或 `/tmp` 唯一文件都不能替代。无法闭合时正确结果是降格，而不是补强措辞。
34. `MP-ERCF-001` 机器证明了通用因子化 walking skeleton，并以 subsingleton、section、separating family 和 identity 观察提供正反控制；这使 E₀ 从 coverage-gap 候选降为可表达的通用基础。下一步必须引入真实 HoTT abstraction/consumer，不能以普通 Lean `Eq` 重命名为 HoTT 悖论。
35. proof run 的零字节 stdout/stderr 是需要原样留存并用 hash 认证的运行证据，但不是认知 loader 要求的非空正文；stable record 应通过 RUN.json/source manifest/verifier 路由它，避免 `EMPTY_REQUIRED_FILE` 在跨 Session 水合时误阻塞。
36. stable record 的 `depends_on` 表示会传播证据 stale/review 的验证依赖，不应拿来表示开放母题、研究动机或叙事归属；后者应保留为非传播的 research-parent 关系，否则已机器闭合的子证明会被父问题的 paper-only 状态误降级。
37. 原生 propositional truncation 证明显示理论经济与 ASK 防御可同时存在：向 mere proposition 的 consumer 合法，point-preserving Bool witness extraction 因 squash path 不可能。正确拒绝是 `DEFENSE_WORKS`，不能为了目标把它改名成悖论。
38. Cubical checker 的证据身份包含 library infective options 与 XDG cache generation；错误 source path、漏 library flags、混合 option cache 和缺 `--guardedness` 是四类不同失败。先按责任点修复再重跑，不能改命题求绿。
39. 不断增长的 claim matrix 不能以 whole-file hash 永久绑定每个旧 run。先冻结 proof/claim 精确行 hash；未来 append 时逐行保持，改写旧行仍 fail closed，才兼顾不可覆盖证据与可增长索引。
40. proof package 同轮更新 source/run/index 与人读入口时，必须对 stable record 的全部 `source_hashes` 做全量差异审计；只更新新增 proof/hash 仍会让旧 README hash 传播 stale，最终验收必须以 task hydration 的 `review_required=[]` 收口。
41. 十个机器包之后的距离评估把 `NATURAL_USAGE_MISMATCH` 的六要素收敛为 E1–E6：E1–E5 已在固定模型中成立，E6（真实、固定版本、可回查的 natural consumer）是唯一决定性缺环。没有 E6 时只能停在 `REPRESENTATION_BOUNDARY`；审计负结论必须写成“在本次固定的审计集合内未发现”，不得写成“系统中不存在”。
42. N1 的有界审计表明，E6 的缺失既可能来自“没有 consumer”，也可能来自“consumer 被显式围栏”：`SplitSupport`/`satAC` 是显式假设，`MagicTrick.recover` 受依赖余域与类型检查围栏，delay 商受 choice/QIIT 条件约束，效应组合的失败被写成不可分配定理，CATT 是 refinement 而非裸函数恢复。审计必须区分 documented boundary / explicit assumption / type-level fence / refinement interface，并把负结论限定在被审计版本与集合内。
43. 提取接口审计必须有真实运行证据：Agda postulate 在 MAlonzo 中被编译为 `error "postulate evaluated"`，Lean 4.33.1 对 `Prop → Bool` 大消去与 noncomputable 求值分别拒绝。类型层“可定义”与执行层“可交付”是两个独立验收面；接口的默认拒绝是 DEFENSE_WORKS，而不是悖论，也不是“理论已经解决问题”。
44. 原生升级旧的有限检查边界时，先固定 claim 映射与禁止外推，再处理实现警告：把索引归纳族改成构造子递归的函数定义（如 `_≤_`）可消除 `UnsupportedIndexedMatch` 而不改变命题；矩阵追加新 proof 后必须重放全部旧包并保持 row-stable，不能只验证新包。
45. 候选生成必须先用最小探针排除可证伪的机制：`ua` regularity 在 Cubical Agda 2.8.0/Cubical v0.9 中由 `probe-regular = refl` 直接排除，不能靠文献印象保留。N1–N3 表明核心库接口系统性防御；E6 更可能在派生开发对自身构造的承诺中，因此 N5 审计派生开发而不是继续重审核心库。
46. 派生开发的“可计算”自述要先看它的**类型**是否已经携带资格：ADK 的 `isPositive : ℝq → 𝟐⊥` 是 partial classifier，作者同时说明 total `ℝq → 𝟐` 不可定义，并把 propositional 与 definitional equality 分开；D2–D4 的 choice/分配律/resource-bounded 假设也都写在接口或正文里。审计的判定单位是“同一任务下是否隐藏假设”，不是文案里是否出现 compute/extract 字样。
47. 最小的 strict-vs-partial 机器边界不需要完整 partiality monad：`Q = A/R_A`（a~b）、`D≈ = Delay Bool/R_D`（now x ~ later (now x)）、代表层 `P0 a = now true`、`P0 b = later (now true)` 就足以证明「strict 扩展不存在、up-to-≈ partial classifier 存在、strict 消费者不能下降、代表层消费者仍可区分」。先做最小片段再决定是否升级到完整单子。
48. post-N6 距离综合确认：十二个机器包全部以 defense/boundary/positive structure 收口；核心库接口、提取后端与派生开发自述都在各自范围内执行资格分离。E6 若存在，更可能在应用层“自然使用链”或 SIP/表示消费者中；继续重审核心库只会重复已有防御。
49. 最小 SIP 边界可以用 `ΣPathP (ua notEquiv , toPathP (uaβ notEquiv true))` 手写，不需要完整 SIP 模块；关键是把“签名外观察量”写成需要额外表示数据（carrier 是 Bool）的值，而不是伪装成 `Str → Bool` 全函数。正控制则是把观察量加入签名，使识别不再成立。
50. 最小 Cauchy modulus 边界显示“按极限值取商”与“保留给定 modulus”是两个不同承诺：`ℕ → Bool` 序列加 `Σ N` 常量性数据就足以证明商层识别 `(constTrue,0)`/`(constTrue,1)` 而 modulus 不可统一恢复；把 modulus 纳入同一性关系即得正控制。外部 agda-unimath 把 convergence modulus 与 modulated Cauchy 序列写成显式结构、完备性定理 `opaque`，与该边界方向一致；引用外部接口时必须绑定抓取提交与 blob hash，且不得由接口形状推断某个具体使用已经出错。
61. 截断“不可恢复”可以族群化而不失围栏：把 C-70 的 Bool 实例升级为「任意集合值读出 + 任意分离见证」的一般形式（C-134–C-138），代价只是把 motive 换成路径类型、并用库定理 `isOfHLevelPath'` 说明「集合中路径类型是命题」。族群化的价值是把用户「理论经济保留存在、遗忘身份」的命题从单例观察变成带正控制（mere proposition 目标仍可消费）和适用域围栏（非集合高阶目标不外推）的机器边界；它仍是 `DEFENSE_WORKS`，不是悖论。工程侧教训：Cubical Agda 2.8 中 `isOfHLevelPath'` 必须按位置传参（`isOfHLevelPath' 1 Sset x y`），把类型写成 `{A = ...}` 会被当作额外隐式参数而失败；边界计算（`squash₁` 端点）也不能依赖 λ 的直接展开，用 `cong`/`sym`/`∙` 组合更稳。
60. 报告口径必须先各带单位再比较：2,369 是用户侧句级账本（句/引文片段，171 遍历单元），2,396 是理解章节行/句抽取账本（24 owner 的冻结行数），119 是三条对话录历史消息数，125 是含 6 条并行会话越界补充的归档记录数。机器复算显示冻结账本的 22/24 owner 至今逐条复现计数（2,268 行），增长集中在 C 系列新文档（2,128 行）与 README/C0 两处增量——说明“口径不一致”多数是单位/范围差而不是数据丢失；同时暴露冻结分母相对当前文档面（4,547 行）的真实覆盖率，任何“已全量覆盖”表述都必须写成相对冻结分母。
59. 快照账本漂移的“有界修复”不是重写历史，而是三件套：只读检查器（逐条比对当前行文本）、owner hash sidecar（未来编辑可对比发现）、显式引用政策（引用 claim 行先核 owner 当前内容）。实测 2,396 条中仅 29 条漂移且全部集中在两份被改写的“当前边界”文档（README/C0），说明漂移与“文档是否持续维护”强相关而不是普遍噪声。第三批抽样证明“低覆盖 owner 加深”与“关键词/等距”互补：新增 22 条 SUPPORTED 中大量是引文、路由元数据与已实现实践，PENDING 全为解释/计划/口径类——证据队列的剩余工作因此可以按“表述类型”而不是“未知事实”来排队。
58. 快照账本必须记录被引 owner 文档的 hash：claim-evidence-ledger 的 `claim_owner_document`+`claim_line` 在 owner 文档被更新后会行锚/文本漂移（实例：C0 的 generation-2 903-KC 文本 vs 当前 generation-3/4 正文）。在给出逐条裁决前先核 owner 文档当前内容；修复方向是给账本加 owner-doc hash 与行锚复核（或按变更集重抽取），而不是静默修正。同时，分层抽样（按 owner 类）比纯等距更能覆盖真实认知分布：第二批 50 条中 30 条直接 `SUPPORTED`、15 条 `PENDING` 集中于解释与问句片段，说明“待裁决”的主体是表述类型而不是未知事实。
57. “自证声明”类 consumer 的审计要按四条件逐源核对，并记录**围栏**而不是只记结论：Agda 文档列禁用特性（含 Girard–Hurken 悖论来源）、Cubical 文档记录传输值可能不计算、MetaRocq 提供认证工具而非自证、Rocq 官方的 verified reference checker 自带三层限定（OCaml 信任内核、验证相对规范、片段范围）、NBE-in-TT 需要 QIIT 元语言且只形式化大部分构造。真实系统普遍**文档化**自己的资格边界；把这种自限读成“已经自证”或“已经失败”都是越级。五层审计塔（核心库/提取接口/派生开发/编译后端/自证声明）齐全后，悖论候选的缺口只剩真实自然使用链（E6）。
56. 证据队列的“有界推进”要靠固定抽样规则而不是穷举：关键词层全选中位后等距封顶、剩余层等距补足，样本量取 40/2,396（1.67%），逐条给四值判词（SUPPORTED / SUPERSEDED_BY_MACHINE_RESULT / UNSUPPORTED / PENDING）。实测分布（13/7/0/20）说明：历史主张的主要缺口不是“被否证”，而是解释性表述与历史叙述尚未句级裁决；机器结果已经接管的那部分（cost、商下降、race、W51）可以安全地从 PENDING 池移出。抽取脚本必须确定性、可复跑，报告只支持样本范围结论。
55. 候选生成要有“必填门槛”和“归约表”：N11 要求每个候选写明 HoTT 特有规则参与的关键步骤、同一任务对照与可机器化判别，然后把 13 个候选逐一映射到已有机器结果/通用边界/元层观察，得到有界负结论而不是无限生成。关键区分：工具链行为（编译拒绝、stuck 项）不等于对象理论定理；模型选择（稠密连续统）不等于 HoTT 特有；只有“真实使用链把弱资格当交付”（E6）才允许升级。三条研究线（自证、继承、A 方向）在同一轮汇合到同一缺口时，应停止生成同型候选、转入证据队列收口。
54. 把方向性判断（如 W51“HoTT 对齐程序后继承程序界限”）命题化时，必须拆成可分别判定的强度：局部分离（有机器抽象核）、一般继承边界（通用 Turing/Gödel 型，不依赖目标理论特有规则）、以及特有使用失配（需要真实接口）。前两者成立不构成悖论候选；只有第三层（=E6/B01-TARGET）满足四条件（真实性、资格越级、无新增假设、可核查性）才允许升级。历史上的“双方都同意”或“纸笔推导”不能被追认为机器结果；源记录重读时同时给出 hash 与归档副本。
53. 前置任务的“同层可行性”应先用最弱载体检验：ERCF-3 的 P2/P3 语法层（对象语法、无捕获替换、Hilbert 证明谓词接口）在纯 Agda builtins（无 cubical 特征、无库导入）下即可通过 kernel，因此“需要 QIIT/2LTT”的压力只属于自应用层（把类型论自身内部化），不属于对象语法层。把“需要新层级”的判断推迟到它真正出现的那一层，可以避免用表示代价掩盖问题本身的层次结构。技术提示：定义用 if_then_else_ + rewrite 引理比多层嵌套 with 更稳；替换代数的完整定律应与可表示性一起留给同一后续任务。
52. ERCF-3 一类“理论为自身认证器开总完备证明”的要求，其最强读法可以在**编码层**就被对角核反驳：带 section 的精确自编码 `A → (A → Bool)` 不存在（Lawvere 不动点 + `not` 无不动点）。该论证与 HoTT 无关，因此不能当作 HoTT 特有悖论；有意义的机器化应停在“前置条件 + 探针”层，只有出现真实 natural consumer 或 HoTT 特有规则的不可替代使用才继续升级。评估必须显式区分强/弱/分层三种读法，否则会把“前提不可满足”误读成“理论失败”。
51. 交付层的资格分离可以先于运行时发生：Agda 2.8.0 的两个编译后端整体拒绝 `--cubical` 模块，`--erased-cubical` 只允许与计算无关的擦除使用（计算性 `transport` 与 cubical 库函数 `not` 都报 `DefinitionIsErased`），cubical 选项是 infective 的（普通模块导入即 `InfectiveImport`），因此“理论检查通过”与“可编译执行”是两层不同验收面。审计交付链必须区分 type check、编译接受、生成物检查与实际运行四种证据；无 GHC 时只能到“生成物检查”，不能声称已执行。
62. 不要为疑似错误目标继续调证明机制。N38 的常量目标有 `s=id` 纸笔反例候选，但该精确否定没有独立 claim/run/index，按 F-011 必须降为 paper-level；机器已闭合的是 C-142–C-148 的自识别相干/无统一选点命题。先分开“目标纠偏”和“已机器证明内容”。
63. 同一源被多个 run 钉住时，新 claim 应进入新模块与新 proof id：把 `TruncationNoRecovery.agda` 恢复为冻结字节、让 C-142+ 落在 `NoCanonicalPoint.agda`，可同时保住旧 run 的 source pinning 与行稳定（`-03` 仍 `ROW_STABLE_AFTER_INDEX_EVOLUTION`），避免共享 proof row 反复改行。同 proof id 的早期 run 会随源演进处于历史源态，这是可选接受态，但必须在 Session/审计中明写，不能默默忽略。
64. Session 完整性是结构事实，不是收尾文字：S067–S085 共 19 个 Session 缺 `CORE_COGNITION_AUDIT.md`（协议要求 36 KC 全量表）而 POST-CHECKPOINT 仍显示 PASS。每轮应实际运行 `build_core_cognition_audit.py --verify-only --session-id <ID>`；缺文件属于治理漂移，按 `A-KC-AUDIT-GAP-001` 有界登记并恢复，不追溯伪造语义回评。
65. 证据契约要按理论变体分支，而不是把 cubical 要求硬编码成全局要求：本轮为 agda-unimath（without-K）重放扩展 `verify_formal_proof_run.py`——cubical 变体仍要求 `--safe --cubical`，without-K 变体要求 `--without-K --exact-split`，其它变体 fail closed；分支必须按最具体的标记优先（一个 without-K 运行可以合法地自述『no cubical features』，单纯出现 cubical 字样不得触发 cubical 要求——该误报在本轮实际发生并已修正），并以既有 Cubical/Lean runs 回归兜底。外部树依赖标签同样应参数化，而不是每加一份外部库就改一次判定逻辑。
66. 外部库源码中的定理不因位于同一仓库就自动成为保存 run 的已重放结论。agda-unimath 固定源码含 `no-global-choice` 与正控制，但 C-05 run 不导入 `foundation.global-choice`；当前只能称 source-inspected。literate-aware 扫描必须排除 Markdown prose，得到 20 postulate / 9 primitive / 22 union，实际 run 闭包 7 个声明文件。
67. 外部归档的可信身份不能靠单一本地哈希：codeload commit tarball 不发布 SHA-256、也不支持 Range/续传（探针 200 而非 206），此时应按 `external-large-download` 降级为单连接 + `If-Match`（用探针得到的强 ETag）+ `gzip -t`/tar 结构校验，并明确披露『本机哈希只证明本地字节身份』；重放收据里同时固定 commit SHA、归档哈希、库文件哈希、确定性源码树哈希与 Agda 二进制哈希，才能在未来独立复核。

68. `POST-CHECKPOINT.json` 是 AI 派生摘要，不能证明 checkpoint 已应用；唯一证据是 canonical runtime 生成的 transaction、before/after 与 `result.json.status=CHECKPOINT_COMMITTED`。历史缺收据必须登记，不能追溯补造。
69. `depends_on` 不是时间线。只有会传播 stale 的验证依赖才递归水合；批次先后、报告概括、研究归属和相似现象必须用 `research_parent`/`related_records`，否则 query-first 原件会被重新拉成数十 MB 启动正文。
70. task plan 的 `review_required=[]` 只说明已选 record 没有当前 stale 标记，不证明计划可装配。必须同时检查总 bytes/lines、document count、largest documents、query-first promotion，并实际完成 snapshot coverage。

71. Proof run 的 frozen index row 与当前 Git closure 是正交维度：原位把 `LOCAL_UNCOMMITTED` 改成 `VERSION_CLOSED` 会破坏历史 row manifest。正确做法是保持旧行逐字不变，在矩阵末尾追加 exact commit registry，并由 current STATE/投影引用；Git closure 不重证数学。

72. Release commit/tag 之后必须重新检查 current STATE 是否还写 `PENDING_GIT_COMMIT`。Checkpoint 记录的是写入时状态，不能自动感知后续 Git；最终可用状态应由一个新的、真实 receipt 对齐，而不是篡改旧 transaction。

73. 长治理文档分片必须先有“逻辑文档”加载语义再迁移正文：只把 canonical 路径换成索引、而加载器不展开分片，会让未来 Session 静默丢掉正文。正确顺序是 runtime/合同/校验入口先行（CP-1），文档迁移后行（CP-2）。300 行只是软目标，不能当拆分依据。

74. 分片索引里的 shard 路径是**相对索引所在目录**解析的（规范与 validator 都如此）。工具与加载器必须归一化为仓库相对路径；只按仓库根解析时，根目录文档（README/MEMORY）会通过、子目录文档（理解章节/C*）会静默失败。首次迁移就撞上了这个坑：错误产物已移出仓库，受影响文件从 boundary tag 精确还原后重做。

75. 大表分片必须保留**表头**（否则 Markdown 渲染失效），因此对账规则要从“整文拼接逐字节相同”升级为“每行恰好消费一次 + 唯一允许的额外行 = 表头行 × (行分片数 − 1)”；投影的身份字段（marker 块、`source_state_revision`/`projection_generation`/`semantic_status`）必须留在索引，因为 runtime 与 freshness 校验直读该物理路径。只按“文件级 hash”迁移会破坏这两点。

76. 分片把“读到索引”变成了“以为读到全文”的捷径，所以索引需要**首屏可见 banner**（而不是只在规范里写规则），并且 banner 必须被机械检查（`verify_governance_shards.py` → `MISSING_READER_BANNER`/`INCOMPLETE_READER_BANNER` 直接 FAIL）。另一条经验：`理解章节/C1`–`C4` 的索引文件被 merge manifest 逐文件 pin，任何索引文本改动（哪怕只加一行 banner）都必须重建 manifest 并在同一 checkpoint 重签 14 条 record。

77. 吸收外部 AI 工作时：原件必须按字节保全并**独立复现**其只读核验脚本；外部 run 的 schema 与项目 capture 不同，只能分别登记，不能改名/补字段冒充；历史 packege 的冻结 registry（如 17 包 PROOF_VERSION_CLOSURE）不改写，新包走追加式 `later_packages` + 'tracked/INDEXED/exit 0' 机械检查。候选文档的'值得研究'与被检验后的'未构成目标'必须分开写。

78. `HoTT/CLAIM_EVIDENCE_MATRIX.md` 必须**保持冻结前缀 + 末尾追加**：`verify_proof_version_closure.py` 要求当前矩阵以 d3dfb0e 快照为前缀，中间插入新行会直接 `CURRENT_MATRIX_NOT_APPEND_ONLY_SUCCESSOR` BLOCK。新 proof package 的包行与 claim 行一律追加到文末（可另起追加节 + 自己的表头）；只要行文本不变，旧 run 的 `index-row-manifest` 仍为 `ROW_STABLE_AFTER_INDEX_EVOLUTION`。

79. 把一份 AI 撰写的长文提升为常驻输入时，必须在加载层同时声明**角色**：`LOAD_SET.full_set_roles` + 文档内 `essay-role:v1` 让“AI 阐释层”和“用户原文权威”在上下文里可区分；否则常驻加载本身会重演 rulings §9/§12 要防的‘AI 展开被当成用户原意’。另外：MUTABLE 集合新增成员后 HEAD 会 `HEAD_TRACKING_INCOMPLETE`，必须先用 canonical `initialize_cognition_head.py` 重新引导（它现在直接从 `runtime.MUTABLE` 取集合，避免漏项）。

80. 用户以 Session Name 指代另一个 AI 的会话时，repo 必须能解析该别名：把「名称 ↔ thread_id ↔ rollout 原件 ↔ 已吸收产物」写成一行可查记录，否则未来 AI 只能靠猜。另外，审计「有没有读到 EOF」不能只看 canonical 编号-Read 合同是否匹配——先看被审 Agent 实际用的是哪种读取工具，再用保存了该现场的 commit 做逐字节/逐行对账；否则会把合同不匹配误报成内容缺失（本轮实测：`coverage` 报 L2 FAIL，而运行期源快照对账为完整）。

81. 理论经济账本应先于具体候选，帮助显式写出收入、悬置/加入因子、补偿与复活条件；支付装置的可用/昂贵/不存在只是描述坐标，不是候选准入或搜索穷尽 Gate。现有包的归类一致性不能证明账本完备。

82. 商/截断消去器把同余或目标层级义务写进类型，能拒绝一类直接资格越级；但真实截断消费者确实存在。后续必须分别检查消费者真实性、条件是否合法、是否把弱资格提升为更强交付，不能把 E6 预设成只会出现在文档措辞里。

83. 粗域接口检索可先用词汇 triage 建立有界队列，再人工实读；两批低精度样本只支持收益/成本暂停，不能证明剩余命中都是假阳性。队列保持可复算和开放，真实消费者不自动等于 E6。

84. 吸收外部评审时，先做**逐项独立核验**再决定判词：本轮 5 主条 + 5 细节全部成立，但核验本身产生了新事实——`labeledChoice` 是“预先保留”而非“恢复”、`canon` 丢弃等待时间、`GuardErasure` 是等价刻画不是判定器、集合商消去到集合只需尊重关系 + 集合余域。方法层的第二课：**不要把待检验的猜想变成准入 Gate**；判别坐标只能描述候选的处境，不能决定它是否有资格被研究；“补偿操作”必须逐例写成可检查的三类动作（恢复/预先保留/新增），否则“表示更细”会掩盖换了任务。

85. 文档“原位重写”会连带改动三类哈希：文档自身的 record pin、依赖它做机械检查的脚本契约、以及记录该文档哈希的派生 manifest（后者会级联重绑所有 pin 了 manifest 的 record）。重写后必须**先跑全部 verifier**再提交，本轮就是靠 verifier 才发现 v2 误删了 univalence 行、且校验脚本仍在用 v1 的行标签。修正走一个新的 corrective checkpoint（同类 S099→S098），不篡改已应用的事务。

86. 词汇级扫描的两批 40 条样本说明命名造成严重噪音，继续调词表的边际收益低；它不构成“精度极限”定理。未读队列中至少两条是真实截断消费者，因此停止必须写成成本决定并保留重开与逐条语义检查。

87. 对一个已经给出 `isSet B`、`f : A → B` 与关系 `R` 的具体 recursor 问题，“对识别不敏感”可以被精确写成所需同余证明；但规格可形式化或口头不敏感不会自动构造这些输入。S108 的空集结论因此撤回，具体 `UnlabeledTwoElement` 样本继续保留。

88. 门 A（形式化规格）与门 B（同层自我担保）是两条可操作路线，不是穷尽结论。时间/运动结构、量词与完成顺序、B 方向独立行及新规则组合持续有研究资格；停止重复同型枚举不等于证明没有其它候选。

89. T3 的“共享判定”教训：`--safe` 作为**文件 pragma** 会传染给未声明 `--safe` 的历史脉冲模块并触发 `CoInfectiveImport`，而**命令行 `--safe`** 不会——canonical run 必须与既存脉冲命令一致，失败尝试保留为 `-01`。另一条经验：**试图证明恒等式本身就是查错手段**——公式层证明失败时发现历史脉冲 `CodeStoreFixF` 的 `all` 影子分支把 `codeF φ` 写成了 `codeF (all m φ)`（双重编码）；正确做法是新模块给出修正函数并以新 claim 登记，历史文件与会话证据逐字节不改。

90. 新增 proof package 后必须**同时刷新两级索引**：`HoTT/formal/README.md`（包清单）与 `HoTT/verification/runs/README.md`（run 索引）。本轮发现两者分别滞后一个和五个登记周期——包本身、矩阵、closure registry 都对，但未来 AI 从索引出发找不到它们。索引文件被 record 钉住时，刷新后要在同一 checkpoint 里做 revalidation 重绑，而不是回避更新。

91. 登记义务前先查**命名是否兑现了承诺**：`DiagonalCore.⌜-injective` 只做“沿码相等的替换同余”，不是单射性；而 `ObjectSyntax` 明文把 decodability/injectivity 列为未形式化义务。把这条义务的下界机器化（`codeT (var 2) ≡ codeT (num 0)` 而两项不同 ⇒ 无单射解码器）比继续在错误编码上做 P 表示性更省时间：**当前编码不可解码，必须先修编码**。命名误用只登记、不改历史文件。

92. 说“要修编码”之前，先把修复写成**可检查的规格**：`(c : Tm → A) (dec : A → Tm) → (∀ t → dec (c t) ≡ t) → c 单射`。这条通用引理把“修复”与“单射性”绑在一起（C-164），于是“当前编码没有解码器”（C-165）就等于“当前编码不能作为修复”，而结构化树编码的往返（C-163）给出正控制。剩下的是明确的算术半：Nat 值编码需要标签不相交或列表/配对编码加算术引理——按义务边界分批，而不是一句“需要修编码”就换题。

93. 算术标签层的精确结果必须按对象分开：C-166/C-168 约束 `double`/`odd`，C-167 证明 `codeAtom` 单射，而 C-184/C-185 证明 `codeAtom` 满射。修复后 `codeT'`/`codeF'` 像不含 1 由 C-186/C-187 支持；这说明全 `Nat` 解码规格需定义像外行为，并证明当前缺省分支可达，不强制所有实现采用同一语法结构。

94. 位级底座要按“数字算术 → 打包/抽取互逆 → 燃料界”一次做完整，别把界留成口号：本轮只做最低位/折半（`parity`/`half`/`twice`）就同时拿到了 C-170 的两侧引理，但**已知长度的往返**（C-171）仍不足以让解析器只凭码工作——真正让“燃料取自码本身”落地的是 C-172 的 `suc (LEN bs) ≤ codeBits bs`。两条经验：`double` 的单射/偶奇互斥这类引理用构造子冲突即可，不必引入模算术；而界证明的每一步（`≤-trans`、`n≤twice`、`suc≤pack`）都必须显式写出来，空缺处用 `Set` 占位符充数只会把义务藏起来。

95. 解析器的难点不在文法而在**递归形状**：`(t +t u)` 的自然解析是「先解析 t、再解析 u」，第二次调用必须用第一次调用**返回**的燃料，这在 Agda 里既不是结构递归也不被终止检查接受。解法是把待解析的右子做成显式框架栈（`Slot`/`Stack`/`close`），让每步只做一次 `run f rest …`：一次迭代恰好消费一位、消耗一个燃料单位，结构递归立即通过，而往返定理仍可写成**精确**形式（燃料 `BLEN t + k`，剩余恰为 `k`）。两条配套经验：把「多余燃料」下的 `unbits` 说成`unbits (i + j) c ≡ unbits i c ++ unbits j (halfs i c)`，再用 `n ≤ m → Σ k, m ≡ n + k`把 C-172 的界转成燃料形式，就完全避开了减法算术；以及 Agda 的 `rewrite` 在目标含同名子项时会同时改写不该动的位置（本轮 `junk` 内层被连带改写），改用 `subst'` 显式指定要改写的那个位置更稳。

96. 换一个数据类型重做同一构造时，最容易卡住的不是数学而是**定义的可归约性**。两条实测教训：（1）**模式参数放最前**：`run` 的第一个参数是 `Mode`（永远是构造子），若把位串放前面，`eqRight` 那一步的位串是卡住的 `bits u ++ rest`，Agda 就无法在不知道位串构造子的情况下选择子句——连「定义上相等」的等式也证不出来，把模式提到第一位即可。（2）**命题步骤要写成引理**：`tmFrom (bits t ++ rest) ≡ res t rest` 是命题而非定义上的等同，直接 `refl` 必然失败（`rewrite` 甚至找不到可改写位置，因为它不会自动展开目标里的 `run`）；把带 `tmFrom …` 的目标写成独立引理（`tmFrom-run`/`eq-node`/`eqRight-step`），再用 `SP.subst'` 显式搬运燃料与位串，才既可控又可读。另有两条小坑：`≤` 与 `+` 同默认 fixity，`n ≤ n + m` 会被解析成 `(n ≤ n) + m`，和式要加括号；登记义务时不要用 `Set` 占位符充数（`BitCoding` 已改用注释形式记录下一义务）。

97. 有了解码器之后，「码级替换与语法级替换一致」从工程变成**推论**：把码级替换定义为「解码—替换—编码」`substCode k n c = code' (subst k n (dec c))`，一致性就只是 `dec (code' t) ≡ t` 的一次改写（旧编码需要 C-157–C-159 的联合递归）。代价必须同时写清：这样的函数是**元层**的，「存在一个算得出来的函数」不等于「对象理论能表示它」——后者才是表示性义务。本轮据此把 T3 编码线自足部分收口，并把剩余义务明确归到门 B，避免用「看起来已完成」的推论冒充研究结论。

98. 半判定必须把三个层级写进接口与证明：每个有限 stage 的 approximant 总结束；`just` 是可核验的正见证并随 stage 保持；`nothing` 只表示当前界内尚未发现。再证明 `CodeHalts ↔ ∥Σ stage, isSome(semiHaltAt stage)=true∥`，才能同时得到 soundness/completeness 而不偷添总的负答案。某个显式 loop 的全阶段归纳证明仍只是一个程序的不变量，不能代替语言通用性与 halting-undecidability reduction。

99. 外部库写 `undecidable P` 时必须先展开定义再决定交付强度：本轮 Coq 定理实际是 `decidable P → enumerable(complement SBTM_HALT)`，不是纯构造内部 `¬decidable P`。正确跨框架做法是三段式：同核 source→target total reduction；第二 kernel 对同形 TaskSpec 独立证明；machine-readable correspondence 固定字段、量词和表示差异。有限 controls 只查分支交换，全称强度仍由各 kernel theorem 承担；跨 kernel 不能称 definitional equality。
