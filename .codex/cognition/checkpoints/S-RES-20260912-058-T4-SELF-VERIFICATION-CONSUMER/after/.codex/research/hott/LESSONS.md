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
57. “自证声明”类 consumer 的审计要按四条件逐源核对，并记录**围栏**而不是只记结论：Agda 文档列禁用特性（含 Girard–Hurken 悖论来源）、Cubical 文档记录传输值可能不计算、MetaRocq 提供认证工具而非自证、Rocq 官方的 verified reference checker 自带三层限定（OCaml 信任内核、验证相对规范、片段范围）、NBE-in-TT 需要 QIIT 元语言且只形式化大部分构造。真实系统普遍**文档化**自己的资格边界；把这种自限读成“已经自证”或“已经失败”都是越级。五层审计塔（核心库/提取接口/派生开发/编译后端/自证声明）齐全后，悖论候选的缺口只剩真实自然使用链（E6）。
56. 证据队列的“有界推进”要靠固定抽样规则而不是穷举：关键词层全选中位后等距封顶、剩余层等距补足，样本量取 40/2,396（1.67%），逐条给四值判词（SUPPORTED / SUPERSEDED_BY_MACHINE_RESULT / UNSUPPORTED / PENDING）。实测分布（13/7/0/20）说明：历史主张的主要缺口不是“被否证”，而是解释性表述与历史叙述尚未句级裁决；机器结果已经接管的那部分（cost、商下降、race、W51）可以安全地从 PENDING 池移出。抽取脚本必须确定性、可复跑，报告只支持样本范围结论。
55. 候选生成要有“必填门槛”和“归约表”：N11 要求每个候选写明 HoTT 特有规则参与的关键步骤、同一任务对照与可机器化判别，然后把 13 个候选逐一映射到已有机器结果/通用边界/元层观察，得到有界负结论而不是无限生成。关键区分：工具链行为（编译拒绝、stuck 项）不等于对象理论定理；模型选择（稠密连续统）不等于 HoTT 特有；只有“真实使用链把弱资格当交付”（E6）才允许升级。三条研究线（自证、继承、A 方向）在同一轮汇合到同一缺口时，应停止生成同型候选、转入证据队列收口。
54. 把方向性判断（如 W51“HoTT 对齐程序后继承程序界限”）命题化时，必须拆成可分别判定的强度：局部分离（有机器抽象核）、一般继承边界（通用 Turing/Gödel 型，不依赖目标理论特有规则）、以及特有使用失配（需要真实接口）。前两者成立不构成悖论候选；只有第三层（=E6/B01-TARGET）满足四条件（真实性、资格越级、无新增假设、可核查性）才允许升级。历史上的“双方都同意”或“纸笔推导”不能被追认为机器结果；源记录重读时同时给出 hash 与归档副本。
53. 前置任务的“同层可行性”应先用最弱载体检验：ERCF-3 的 P2/P3 语法层（对象语法、无捕获替换、Hilbert 证明谓词接口）在纯 Agda builtins（无 cubical 特征、无库导入）下即可通过 kernel，因此“需要 QIIT/2LTT”的压力只属于自应用层（把类型论自身内部化），不属于对象语法层。把“需要新层级”的判断推迟到它真正出现的那一层，可以避免用表示代价掩盖问题本身的层次结构。技术提示：定义用 if_then_else_ + rewrite 引理比多层嵌套 with 更稳；替换代数的完整定律应与可表示性一起留给同一后续任务。
52. ERCF-3 一类“理论为自身认证器开总完备证明”的要求，其最强读法可以在**编码层**就被对角核反驳：带 section 的精确自编码 `A → (A → Bool)` 不存在（Lawvere 不动点 + `not` 无不动点）。该论证与 HoTT 无关，因此不能当作 HoTT 特有悖论；有意义的机器化应停在“前置条件 + 探针”层，只有出现真实 natural consumer 或 HoTT 特有规则的不可替代使用才继续升级。评估必须显式区分强/弱/分层三种读法，否则会把“前提不可满足”误读成“理论失败”。
51. 交付层的资格分离可以先于运行时发生：Agda 2.8.0 的两个编译后端整体拒绝 `--cubical` 模块，`--erased-cubical` 只允许与计算无关的擦除使用（计算性 `transport` 与 cubical 库函数 `not` 都报 `DefinitionIsErased`），cubical 选项是 infective 的（普通模块导入即 `InfectiveImport`），因此“理论检查通过”与“可编译执行”是两层不同验收面。审计交付链必须区分 type check、编译接受、生成物检查与实际运行四种证据；无 GHC 时只能到“生成物检查”，不能声称已执行。
