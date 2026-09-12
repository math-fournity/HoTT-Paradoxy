# 理解章节目录 v3（目录级认知闭包与当前审计层）

> **当前审计层（2026-09-12）**：先读 [`C0-当前整合审计与证据边界-20260912.md`](C0-当前整合审计与证据边界-20260912.md)、顶层 [`核心认知.md`](../核心认知.md) 和 [`audit/`](../audit/README.md)。C0 是本次三 AI 整合后的当前分母/证据边界 owner；下面 A/B 章节和旧“读态终态”保留为历史 transform，遇到冲突不能用旧表覆盖 C0、manifest、ledger 或底层实物。

> 架构：A 系列（用户认知章，逐轮应答式）+ B 系列（AI 工作编年史）+ C0 当前审计层 + 机器 ledger。旧 v2 的 171/119 等数字属于当时不同分母的历史记录；当前指定 primary 提取为 88 条，Codex supplemental 为 37 条，core 为 903 个 KC 单元，LocalGPT parent/main 为 220 条 visible assistant，WebGPT 为 55 Response，Gemini 为 24 ordinary text。具体分母与证据等级见 C0。
> v3 变更：顶层综合 repo 已建立；新增 `核心认知.md`、source manifest、逐消息/逐回答/逐工具/逐产物/逐 claim ledger、LocalGPT canonical trajectory 证据和本地 `.codex` 治理。旧 `verify_ai_coverage.py` 仍保留为历史验证器，不替代新账本。
> 版本链：v1=1d12edb（结构与账本）→ v2=1ccb299（B系列+锚点）→ 9ee73e2（Gemini 24 chunk 全文精读）→ 46bf864（网页GPT前21节）→ f815e65（网页GPT 55/55 全部完成）→ 7e77168（Codex 13 关键轮精读）。
> 读态总账（读遍账本.md）：用户侧 119 条 F=100%；网页 GPT 55/55 节回复 F=100%；Gemini 24 实质 chunk F=100%；Codex 13 哲学锻造关键轮 F + 其余 ~200 条 M（实质内容由 F 级闭包文档承载，重读边际价值低，已登记重开路径）。

## A 系列（用户认知——逐轮应答式积累）
| 文件 | 主题 | 处理的主要轮次 |
|---|---|---|
| A0-总目标.md | 我们在找什么（四次定形+审美标准） | C-T15/T22/T23/T24/T25、W8/W13/W22、G2/G3/G12§一二、G9 |
| A1-Z铁律.md | 抽象=否定/前提改变结论改变/X≠Y/**合取命题**/否定分层/哲学身份/朴素集合论判词 | C-T8/T12/T23/T24/T25/T28/T29/T32/T33、G6/G8 |
| A2-参照悖论谱.md | 芝诺/罗素/Better Best/圆环/shenchensh与Matrix/说谎者（按用户读法逐个展开） | C-T8/T9/T13/T15/T24/T26/T27、W18/W22、G7/G13 |
| A3-ASK计算合法性.md | 诞生/命名/完整定义/四变体/中途失效/时序成本论 | C-T11、W26/W27/W28、G3/G11/G12§三/G13 |
| A4-时间维度.md | 研究对象时间≠工作维度时间/程序参照系/四层区分 | C-T6/T7、W26、G13（用户部分）、三问校准 |
| A5-HoTT怀疑演进.md | 核心怀疑→三分律校准→逻辑+几何+程序/自指不可越过 | C-T4/T5/T14、W19/W44/W45/W51、G20/G21 |
| A6-Gemini论辩.md | 七封信的技术史与证据纪律 | W33–W45（转发轮）、G13–G19、G22、W36–W43 |
| A7-认识纪律.md | Thinking in my math philosophy/双阶段协议 | C-T10/T27、G7、G12§八 |
| A8-材料与保全.md | 原文至上/语料较真/外部AI审读/Schema定位 | C-T1/T3/T18/T19/T20/T21/T37、W2/W5/W6/W33/W34、G1、G12§七 |
| A9-工作治理.md | 落盘/闭包/Skill/MEMORY/代码保全/口径/交接 | C-T2/T5/T7/T16/T17/T22/T36/T38、W1/W3/W4/W9–W16/W31/W32/W42/W55/W56、G12§十 |
| A10-怎么找.md | 方法指令全集（先验匹配/成对证据/承诺归属/恢复对照/真运行/反停滞） | W8/W17/W20–W25/W29/W30/W46–W50/W52–W54、G4/G5/G10/G12§六九 |
| A11-开放问题与悬空接头.md | W51×RP-B01 未连接、自指线、A方向未动、38口径教训——给未来AI的接手清单 | W51、G20/G21、R0xx记录、本轮对话 |

## B 系列（AI 工作编年史——三份对话录的历史 transform）
| 文件 | 内容 |
|---|---|
| B0-工作史总览.md | 三时代编年总线：用户轮↔AI行为↔落盘↔git↔R轮 主对照表+跨时代不变量/断裂点 |
| B1-本地GPT工作史.md | E001-E018 ↔ 1,143 次工具调用 ↔ 3 commit；建造了什么/怎么建造/未竟与移交 |
| B2-网页GPT工作史-I.md | W1-W34 ↔ R004-R019：治理建造、九方向 S-ANS 轮、revision-ZIP 机制、双 JSON 审计 |
| B3-网页GPT工作史-II.md | W35-W56 ↔ R020-R040：论辩九轮落盘映射、R029-R039 深化、暂停对齐、R040 交接 |
| B4-Gemini工作史.md | 24 条实质 chunk 逐段登记、三段弧线、沙箱出处陷阱、两问回答 |
| B5-成果总账.md | 按证据等级（E1-E5）的全部成果+负结果库+防冒领清单 |

## C 系列（当前整合审计与可回源边界）

| 文件 | 内容 |
|---|---|
| C0-当前整合审计与证据边界-20260912.md | 当前唯一整合纠偏层：三份 primary、Codex supplemental、AI response/tool/work-product/claim 分母，历史旧口径的纠偏，aistudio-docs 缺口和下一接管顺序 |

当前机器审计资产位于顶层 `audit/`，不再把“用户句级账本、聚合锚点、旧 PASS”单独当作全部 AI 行为证据。C0 只负责当前判定和路由，逐条原文/事件仍需回源 ledger 和来源文件。

## 审计基建
- 用户句级账本（上级目录 sentence_ledger_annotated.json，2369 条 0 缺锚，171 遍历单元）；
- 审计锚点-AI侧.md（R/G/A/T 四类+负锚点）；verify_ai_coverage.py（**29 项全 PASS**——批次 9 扩展后含产物内容核验与 r024 代码行号锚点项）；
- 三个 git 仓库：ALL-Markdown（8）、workspace（44，HEAD=26fcecf R041）、AI对话录（批次 1–9 共 13 commit）。

## 版本链（全量精读工作方案批次 1–9，2026-09-11 完成）

批次 1（7113aa8）RP-B01+论辩实物 → 批次 2（876adc9）代码 305 测试重执行 → 批次 3（0178b9c）artifacts 四计数 → 批次 4（9b14759）44 SESSION+19 份数学正文 → 批次 5（a83f9e1）Codex 38 轮 AI 回复 100% F → 批次 6（bdd2dc4）五闭包+owner 全读+A1–A4 零差异 → 批次 7（7be5805）ALL-Markdown 其余+HOTT_Z 台账+archive 处置表+R006–R015 收据核验关闭 → 批次 8（45d78fa）git/Gemini/onboarding/exec 边角清零 → 批次 9（本 commit）B5 终稿+verify 扩展+README 版本链。读遍账本终态见其"批次 1–8 汇总"表。

## 使用指南
新 AI 接手顺序：B5（有什么）→ A0（找什么）→ A11（接什么）→ B0（总线）→ 按需深入 A/B 各章；任何主张沿锚点回源。
