# ADR-003：以不可变逐字派生语料保存 aistudio 中的 HoTT 讨论

状态：`ACCEPTED`

日期：2026-09-01

来源裁定：R-008

## 1. 问题

`aistudio-docs/` 是约 1.3 GB 的历史归档。此前按“文件主对象”迁入 `HoTT/` 的 16 份全文适合
建立专题来源，但不能覆盖其他长文件里嵌入的 HoTT 讨论。只写摘要会让当前整理者决定什么值得
保存；把所有关键词命中文件整体移动，又会破坏原归档职责并把大量非 HoTT 主线内容误认成专题
全文。归档格式也不统一：既有 `# N. 问/思考/答`，也有专题文章、章节、笔记和无标题正文。

## 2. 决策

建立 `HoTT/sources/aistudio-discussions/` 这一 `MACHINE_MANAGED_DERIVED` 语料：

1. `aistudio-docs/` 与 `HoTT/sources/aistudio-docs/` 的原始 Markdown 继续是权威原文；build 不移动、
   改写或删除它们；Markdown universe 包含后缀大小写不敏感的 `.md` 和 `.markdown`，不把 CSV/TSV
   生成报告、仓库 `.gitignore` 或 `.DS_Store` 冒充讨论文档；
2. 以明确的 HoTT/同伦类型论、univalence、identity type、higher inductive type、∞-groupoid 和
   相关变体词作为高召回入口；时间、历史、资源、自指、极限和悖论仅作上下文标签；
3. 源结构先分类为 `qa_dialogue`、`prompt_response`、`headed_prose`、`unheaded_prose`；问答和
   Prompt 分别按完整 turn/unit 复制；两类非问答候选全文复制，避免用任意章节或窗口截断连续论述；
4. 已迁移的 16 份核心源也全文保留；问答体的匹配范围重叠时确定性合并，并默认保留命中问答
   前后各一个完整 turn；混合问答文档中 turn 外锚点才退回 Markdown section/±40 行窗口；
5. 每个 excerpt 记录源路径、全部字节重复实例、源 SHA-256、行区间、结构、提取方式、锚点、标签、
   逐字 SHA 与 excerpt SHA；收录状态固定为 `UNREVIEWED_RAW_CAPTURE`；
6. 输入快照决定不可变 generation；临时目录构建成功后才原子更新 `CURRENT`。旧 generation 默认
   保留，删除需要新的明确授权和可恢复性证明；
7. `manifest.jsonl`、`source_inventory.jsonl`、`STATS.json`、`INDEX.md` 和 `excerpts/` 只由
   `HoTT/tools/hott_discussion_corpus.py` 管理；人工不直接改写；
8. validator 必须复算源 inventory、结构分布、SHA、连续源字节、行范围、ID、孤儿文件和锚点覆盖，
   并单独核对非问答源/候选/摘录数量。

精确 schema、命令、恢复和盲区的唯一操作合同为
`HoTT/sources/aistudio-discussions/README.md` 与同目录 `schema.json`。

## 3. 被拒绝的方案

- **只保存摘要**：不能满足原文回顾要求，且摘要选择本身带有研究偏见。
- **只处理问答标题**：会漏掉论文、专题长文、原则文档、日期笔记和无标题正文；与 R-008 冲突。
- **把所有命中文件整体移入 `HoTT/`**：混淆“正文提及”与“文件主对象”，破坏来源归档边界。
- **覆盖式单目录输出**：中断时可能留下半成品，也无法复现旧快照。
- **语义分类时删除误报**：当前审读者会成为不可逆过滤器；因此 raw 层只追加标签，curated 层
  另建派生视图。

## 4. 后果与边界

优点是未来 AI 可通过 manifest 直接找到原始讨论，不必相信摘要，也无需每次重扫 1.3 GB；源字节
和行号可独立核验；当前 19 份非问答候选合计仅约 1.15 MB，全文保留消除了非问答边界偏见。代价
是高召回语料含无关相邻/全文上下文并占用派生存储；个别连续问答块很大。

v1 不是语义完备抽取：完全不出现锚点的隐喻性 HoTT 讨论仍可能漏检；锚点误报也会保留。语料
只能证明来源曾包含这些文字，不证明数学正确、用户认可、原创或外部审查完成。

## 5. 重审条件

以下任一情况出现时重审 schema/manager 并建立新 generation，而不是手改旧产物：发现新的稳定
归档结构；锚点存在有证据的系统性漏检；相邻 turn 导致不可接受的可用性问题；需要增加人工审读
annotation、近重复视图或检索索引。任何重审都必须保持原始源和已有 raw generation 可恢复。
