# aistudio HoTT 逐字讨论语料

资产类型：`MACHINE_MANAGED_DERIVED`

Schema：`hott-discussion-corpus/v1`

唯一 manager：`../../tools/hott_discussion_corpus.py`（当前 `1.2.0`）

原始权威：

1. `/Volumes/D/ALL-Markdown/aistudio-docs/` 中后缀大小写不敏感的 `.md` 和 `.markdown`；
2. `/Volumes/D/ALL-Markdown/HoTT/sources/aistudio-docs/` 中相同类型文件（含已迁移的 16 份 HoTT
   主线全文）。

`conversion-report.csv`、`md-dedup-report.tsv` 是归档生成/去重报告，项目根 `.gitignore` 是仓库配置，
`.DS_Store` 是操作系统缓存；它们不是 AI 讨论文档，因此不进入 discussion corpus inventory，但原始
文件按各自职责保留。不能把“对照目录全部文件数”与“讨论文档 source_files”混为同一指标。

本目录不是摘要库，也不是数学真理库。它是一个高召回、逐字、可回源的派生视图：把散落在
2,000 余份归档文档中的 HoTT 讨论按各自真实结构复制到统一位置，同时保留源路径、源 SHA-256、
行区间、命中锚点和逐字片段哈希。归档并不全是“问—答”对话；manager 明确区分
`qa_dialogue`、`prompt_response`、`headed_prose` 和 `unheaded_prose`，禁止把非问答材料强行套进
问答模型。

## 1. 为什么存在

此前“文件主对象是否是 HoTT”的规则适合把 16 份核心全文迁入专题目录，但会遗漏其他长文档中
嵌入的 HoTT 问答、专题段落、连续论述和无标题正文。人工摘要又会受当前 AI 的问题意识和偏见
影响。因此本语料采用：

```text
原始文件不动
→ 高召回机械命中
→ 问答按完整 turn/unit；非问答候选全文；混合文档 turn 外锚点才回退 section/window
→ 保存连续原文字节
→ 分类只加标签，不删除 raw capture
```

未来 AI 可以直接阅读原始讨论，而不必相信摘要。

## 2. 当前结构

```text
aistudio-discussions/
├── README.md
├── schema.json
├── CURRENT                         # 当前 immutable generation ID
└── generations/<generation-id>/
    ├── STATS.json
    ├── source_inventory.jsonl      # 全部源文件身份、SHA、重复组、候选状态
    ├── manifest.jsonl              # 每个逐字 excerpt 的血缘与行区间
    ├── INDEX.md                    # 人类可读派生索引
    └── excerpts/
        └── HOTT-DISC-*.md          # header + 连续逐字原文 + footer
```

Generation 由 schema、manager、配置和全部源路径/哈希确定；相同输入重复 build 得到同一 ID。旧
generation 不在 build 中删除，`CURRENT` 原子更新，因此中断或新扫描不会覆盖旧证据。

## 3. 抽取单位

优先级：

1. 已迁移的 16 份 HoTT 主线文档：全文作为 verbatim block；
2. 非问答候选（`headed_prose`、`unheaded_prose`）：候选文件全文作为 verbatim block，消除任意
   章节/窗口边界对连续论述的截断；
3. 有 `# N. 问/思考/答` 的对话：命中 turn 加前后各一个完整问答；
4. `Prompt/Response` 导出：命中 prompt unit 加相邻 unit；
5. 混合文档中落在 turn 之外的锚点：按一级/二级 section，仍无 heading 时使用前后 40 行窗口。

重叠范围确定性合并。Validator 逐个检查所有 anchor 命中行至少被一个 excerpt 覆盖。
`STATS.json` 分别报告全部源文件、候选源文件和 excerpt 的结构分布，以及非问答候选/摘录数量；
这三组数字是防止未来实现退化成“只扫问答”的验收证据。

## 4. 高召回锚点

v1 包含：

- `HoTT`、`homotopy type theory`、`同伦类型论`；
- `univalence`、`univalent foundations`、单价/泛等公理；
- identity type、path induction、等价即相等、相等即路径、类型即空间、同伦同一性；
- higher inductive type、∞-groupoid；
- cubical、guarded、two-level、directed type theory。

时间、历史、资源、自指、极限、悖论、计算和 universe 只作为 context tags；它们不会单独让普通
文档进入 HoTT 语料。锚点版本是可修订工程配置，不冒充“所有语义上相关内容”的完备定义。

## 5. 命令

从 repo 根执行：

```bash
# 只读扫描，输出预计 generation/statistics
python3 HoTT/tools/hott_discussion_corpus.py scan

# 完整计算但不写
python3 HoTT/tools/hott_discussion_corpus.py build --dry-run

# 建立 immutable generation 并更新 CURRENT
python3 HoTT/tools/hott_discussion_corpus.py build

# 全量核对源 inventory、SHA、逐字行片段、excerpt、anchor coverage 和 orphan
python3 HoTT/tools/hott_discussion_corpus.py validate

# 快速核对 manifest/excerpt/source slice，不重扫全部 inventory
python3 HoTT/tools/hott_discussion_corpus.py validate --fast

# 当前统计
python3 HoTT/tools/hott_discussion_corpus.py stats

# 查询；不会修改 manifest
python3 HoTT/tools/hott_discussion_corpus.py query --topic time_process --limit 20
python3 HoTT/tools/hott_discussion_corpus.py query --structure unheaded_prose --limit 20
python3 HoTT/tools/hott_discussion_corpus.py query --source '普罗米西斯' --anchor univalence
python3 HoTT/tools/hott_discussion_corpus.py query --id HOTT-DISC-...
```

## 6. 证据与编辑纪律

- `excerpts/`、manifest、inventory、INDEX、STATS 禁止手改；修改源或 manager 后重建 generation。
- excerpt 收录只证明关键词命中和原文曾这样讨论，不证明数学正确、用户认可或原创。
- `UNREVIEWED_RAW_CAPTURE` 不能被标题、AI 自称专家或旧 `✅/Final` 提升。
- 将来语义审计只能新增 review annotation/curated view，不能删除或改写 raw capture。
- 精确主张仍回到源全文、当前 owner、形式证明、一手文献和外部审查。
- 源文件被移动但字节不变时，inventory 保留全部实例路径并按 SHA 去重内容。

## 7. 失败、恢复与删除边界

- build 采用排他 lock、临时目录和同文件系统 rename；失败不更新 `CURRENT`。
- 相同 generation 已存在时 build 幂等，只更新 `CURRENT`。
- source inventory 漂移时 validate 失败并要求重建，不静默沿用旧结果。
- 本系统不删除 `aistudio-docs`、已迁移源或旧 generation。
- 若未来需要回收 derived generation，必须先证明它不是唯一引用证据，并取得用户明确删除授权。

## 8. 当前盲区

- 只通过隐喻讨论 HoTT、且不出现任何 v1 锚点的段落可能漏掉；不能声称语义全覆盖。
- 自动边界不能理解所有混合对话结构；非问答候选已全文保留，问答/Prompt 仍保留完整源路径和
  行号供回查。
- 相邻 turn 会有大量非 HoTT 上下文，这是为了防止摘录偏见，不是噪声清理失败。
- 近重复而非字节重复的 AI 分支仍分别保留；未来可建立非破坏性相似度视图，但不能自动合并原文。
