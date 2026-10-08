# CN-060 · 复算暂停之后的诊断与 hook 安装位置

> **身份**：【证明】（只读核对与稀疏检出试验，有范围：试验在会话临时目录，未改主仓库）+【判断】+【建议】。
> **会话**：43345aa3，2026-10-07（本地时间；账本与 manifest 的时间为 UTC，即 2026-10-08）。
> **相关**：CN-058（独立性边界）、CN-059（压缩后自动恢复）、`dev-docs/GUI导出全量复算重读审计SOP.md`。

## 1. 事实：暂停时的状态（只读）

- 第一次运行停在阶段 A。`STATUS.md`（2026-10-08T00:40:33Z 生成）：已提交 40/636 块，义务行 8,000/126,503；下一块 B-dev-01-0041；账本 91 条，prev 链完整。
- 账本事件：RS 4 次（约 2 小时 15 分内的 4 次 CL-BR2）；压缩后、CL-BR2 完成之前写草稿 4 次（B-dev-01-0016、0024、0031、0037，执行者自己发现并作废）；REREAD_PREMATURE 4 次（reread.py 先写入 PASS，后被覆盖）；SOP_CONFLICT 2 次；ENV_EXPOSURE 2 次；EXEMPTION_ADDED 1 次（`^/tmp/pattern-p-forge-`，理由已写入文件）；ID_GAP_UNRECORDED 1 次（A2-0135 未登记）。
- seal-log 只有 STAGE_START，没有 ACCESS 或 SEAL_BREACH 记录。
- 最后一次写入是 2026-10-08T00:40:33Z（本地 20:40）；2026-10-07 21:12 复查时没有新写入，即执行会话已停止。
- ACTIVE 标记不存在；没有安装任何 hook 或规则。

## 2. 三个阻断问题

1. **CL-BR2 的代价随笔记增长。** 每次压缩后，CL-BR2 必须整读：`notes2/dev-01.md` 478,370 B、`classes2/dev-01.tsv` 55,574 B、`assets2.md` 131,249 B、`ledger2.jsonl` 90,550 B，合计约 756 KB（按 SOP 005 的估算，约 30 万 token）。近期 notes 每块约 14 KB（23:31Z 时为 243,589 B，现为 478,370 B，中间约 17 块）。外推：dev-01 完成时约 1.1 MB；636 块全部完成约 9 MB。SOP 没有对 notes2 的分片或上限（005 §2(g) 的 300 KB 分支只适用于 assets2）。
2. **方法 B 的禁令放大了阅读量。** 目标把 git 限定为 status、ls-files、rev-parse、hash-object、cat-file；SOP 002 §3.4 要求的 `git diff --no-index` 不在其中。结果 SHARED 为空，126,503 行全部成为义务行。执行者自己的估算：SOP 设计下的独有义务约 27,724 行，实际约为其 4.6 倍（ALIGN_INFO，2026-10-07T22:25:14Z）。
3. **门禁只靠纪律。** `reread.py` 接受调用者声明的 `--status PASS`，不核实第二遍整读是否真的发生；`commit_block.py` 的预检不检查本窗口是否已有 CL-BR2 收据（代码与检索均未见此检查）。结果是 4 次提前 PASS 与 4 次压缩后先写草稿，都由执行者自己发现。

## 3. 分片不会使已提交块的收据失效

`commit_block.py` 第 338–349 行：`notes_sha256 = sha256(sec_text)`，`sec_text` 是块的 notes 节；`classes_sha256` 与 `assets_sha256` 同样由本块的行计算（`cls_text`、`a_text`）。三个哈希都不是整个文件的哈希。因此 notes 按块边界分片后，只要块的节文本与行不变，已提交块的收据仍可核对。这支持 v2 的分片方案，不必作废 40 块；分片后仍由执行者在 CL-R2 中重新核对，审计者抽查。

## 4. hook 的实际状态（已核实，2026-10-07）

- 主目录：`.claude/settings.json`、`.claude/settings.local.json`、`.claude/hooks/`、`.claude/rules/gui-reaudit.md`、`audit/GUI-ASSET-REAUDIT/ACTIVE` 全部不存在。
- 现有 worktree（`.claude/worktrees/git-worktree-path-5657c0`）：同样全部不存在。
- 我写过的只有文档与模板，位于 `.claude/压缩后恢复机制/`（未跟踪、未提交）。模板不在 `settings.json`、`hooks/`、`rules/` 里，不会被 Claude Code 加载，因此对本会话的工作模式没有影响。
- 结论：没有需要拆除的已安装内容。若要删除模板或方案，删除不可逆，需要明确确认。

## 5. 现有 worktree 能不能找到要审计的文件

- 分支 `claude/git-worktree-path-5657c0`，HEAD `f3127701`。它属于 2026-09-30 重建的 `main` 独立历史，与 `dev-glm-5.3`（f1060edb）没有共同祖先（`git merge-base` 为空）。
- 语料的 8 个文件、SOP、闭包、锚表全部不存在。**结论：这个 worktree 找不到要审计的文件，不能用于复算。**
- 它的好处：根目录没有 AGENTS.md；gitStatus 最近的提交标题是 main 线的发布标题，不含 GUI 字样。坏处：它带着 main 线的全部结论材料（五语 README、CLAIMS、证明包），对只做 GUI 导出复算的执行者是噪音，也可能成为锚定源。

## 6. 稀疏检出试验（临时目录，未改主仓库）

- 从 `dev-glm-5.3`（f1060edb）克隆到会话临时目录，只稀疏检出 `git-worktree对话录/`、SOP 索引与五片、闭包、锚表。
- 结果：8/8 个语料文件的 sha256 与字节数与 manifest2 完全一致（共 126,503 行，约 11.2 MB）；SOP 的五片名称正是 hook 模板 `ls` 会列出的名称；`audit/GUI-ASSET-RECOVERY/`、`AGENTS.md`、`.claude/`、`HoTT/` 均不存在。
- 这说明：可以为执行者建一个只含输入的工作树，第一战役的产物在物理上缺席，比规则更强。注意两点：git 历史仍可读，所以"不运行 git log、show"仍是纪律而不是技术限制；gitStatus 会显示 dev-glm-5.3 的最近提交标题（含 GUI 字样）。

## 7. 建议（待研究发起人裁定；登记于 `002` §2 第 29 条）

- **D-A 执行位置**：新建 `/Volumes/D/HoTT-GUI-reaudit-exec`（`git worktree add --detach … f1060edb`，然后稀疏检出）。放在仓库之外，避免向上查找时碰到主仓库的指令文件（CLAUDE.md 按文档会从上级目录加载）。推荐：是。
- **D-B hook 安装位置**：只装在 D-A（`.claude/settings.json`、`.claude/hooks/reaudit-after-compact.sh`、`.claude/rules/gui-reaudit.md`，均为未跟踪文件）；主目录与现有 worktree 不装。hook 以 `audit/GUI-ASSET-REAUDIT/ACTIVE` 为开关，ACTIVE 不存在时输出为空，所以在执行者创建 ACTIVE 之前不会有任何影响。推荐：是。
- **D-C 旧工作区**：在 v2 规范下续做（把主目录中未跟踪的 `audit/GUI-ASSET-REAUDIT/` 原样复制到 D-A，经 CL-R2 与收据核对，从第 41 块起），或重开。推荐：续做；若审计者抽查发现 40 块有问题，再重开。
- **D-D 规范 v2**：方法 B（允许 `git diff --no-index`，只比较两个语料文件，不读历史；或正式裁定全行义务）；notes 按块边界分片；reread 与草稿写入的工具门禁。推荐：三项都做，授权后我修订规范并记修订记录。
- **D-E 模板**：`.claude/压缩后恢复机制/模板/` 保留为安装来源；装完并核实后，再决定是否删除原件。

## 8. 本次没有做的事

- 没有新建 worktree，没有安装任何 hook，没有改动执行者的工作区，没有改 SOP 或闭包，没有提交。
- 稀疏检出试验留在会话临时目录，没有进入仓库。

## 9. 补注（2026-10-07，续五）：现成的 worktree `…4c282f`

- 位置：`.claude/worktrees/git-worktree-path-4c282f`，detached 于 f1060edb（与 dev-glm-5.3 的 HEAD 相同），工作区干净，完整检出（非稀疏）。
- 输入齐全：语料 8/8 与 manifest2 的 sha256 与字节数一致；SOP 索引与五片、认知闭包、协议锚表都在。
- 但它带着不该进执行者上下文的东西：第一战役产物 `audit/GUI-ASSET-RECOVERY/`（阶段 A 须封印）；根目录 `AGENTS.md`（没有 CLAUDE.md 时会被当作项目指令读取）；`.claude/rules/` 里的 `hott-claude.md` 与 `最高指示-Claude版.md`（没有 paths 字段，会话启动即加载，会把执行者拉进 Claude 线的治理）；`HoTT/` 与其它研究材料。
- 没有 hook、没有 ACTIVE、没有执行者工作区。
- 建议：把它作为 D-A，不新建 worktree。稀疏收缩为 17 个文件（语料 9、SOP 6、闭包 1、锚表 1）。收缩会移走上述工作区副本，git 历史保留，`git -C <wt> sparse-checkout disable` 可恢复。收缩前需要研究发起人确认；若该目录上有会话在运行，收缩后要重开会话。
- 仍存在的限制：gitStatus 会显示 f1060edb 的最近提交标题（含 GUI 字样）；这个 worktree 位于主仓库 `.claude/` 之下，尚未核实 Claude Code 是否会向上读取主目录的 AGENTS.md。若要避开，可用 `git worktree move` 把它挪出仓库。
