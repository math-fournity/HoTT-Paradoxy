# GUI 问答树 v3 · 启动提示词

> 身份：2026-10-08，会话 43345aa3（Claude Code，Haiku 5.5）编写。与对话中的代码块逐字相同。
> 修订：2026-10-08，会话 d58e0c0d 按研究发起人要求把规范改为按需读取：四个代码块中“CLAUDE.md 已导入规范”一句改为“调用 gui-qa-tree Skill 并用 Read 读规范与闭包，压缩后重读”。其余文字未改；因此本文件与当初对话中的代码块不再逐字相同。
> 使用方法：在仓库根目录 `/Volumes/D/HoTT_AI_HANDOFF_20260911` 启动新会话，把对应代码块作为 goal 的正文。每个会话只做一件事（一个分组、一组分支卡、综合或审计）。标注与分支卡可以并行；综合在分支卡全部通过之后；审计的盲审可以与标注同时开始，比较须在标注完成之后。

## 1. 标注会话（分组 G1–G8，八个会话并行）

```text
【GUI 问答树 v3 · 标注会话】本会话的分组：G1
（开新会话时，把上一行的 G1 改成 G2、G3、…、G8 之一；一个会话只做一组。）

在仓库根目录 /Volumes/D/HoTT_AI_HANDOFF_20260911 中工作。开工前先调用 gui-qa-tree Skill，并用 Read 读完本任务全部规范（SOP 索引与 001–006、闭包 GUI-QA-TREE-001）；压缩或恢复后先重读它们（根 CLAUDE.md 第二节）。

任务：完成本组每个单元的逐轮标注，并通过机器校验。
- 单元与轮号范围见 dev-docs/GUI导出问答树SOP/003 - 阅读与标注规则（v3）.md §6。
- 分部单元（dev-08）：标注文件名按表写，例如 G1 写 annotations/dev-08.a.jsonl；校验时单元名仍是 dev-08，并用 --docs 限定范围。
- 不可见尾部单元（G8 中的 unexported-*）：每轮 outcome 写明“未在任何 GUI 导出中”（SOP 002 §4）。

逐轮要求：
- 按 SOP 003 §1 读完每轮的完整文档，从本组最大轮号倒着读到最小轮号。
- 按 SOP 003 §2 写一行 JSON；引文逐字复制；refs 逐字出现在该轮文档中。
- 每读完 10 轮，追加写入对应的标注文件（追加，不覆盖）。不得跳过任何一轮；无内容的写 NO_CONTENT。
- 身份：reader 填 annot-G1（即 annot- 加上你的分组号）；model 填你本会话所用模型的 ID。两者不得为空，model 不得为 GLM-5.3 家族。

完成判据（全部满足才算完成）：
1. 本组每个单元的校验退出码为 0，例如：
   python3 -I -B audit/GUI-SYNTH-REDO/tools/check_annotations.py --stage annotations --unit <单元> [--docs <范围>]
2. 对应报告 audit/GUI-SYNTH-REDO/reports/annotations--<单元>.json 的 status 为 PASS。
3. 最后的回复列出：每个单元的校验结果、写入的文件、遇到的问题。未通过时写出缺口与原因，不得声称完成。

禁止：
- 调用 Agent 工具（子代理）；commit、push；
- 修改 qa/、cards/、synthesis/、audits/ 下的任何文件；修改其他分组的标注文件；替其他分组写标注；
- 读取 audit/GUI-ASSET-REAUDIT*、第一战役的产物、其他 worktree 的文件、git-worktree对话录/*-gui.md（SOP 006 §2）；
- 删除任何文件。
```

## 2. 分支卡会话（分组 K1–K3，三个会话）

```text
【GUI 问答树 v3 · 分支卡会话】本会话的分组：K1
（分组：K1 = dev-08；K2 = archive-01a0fb08、archive-01a0fb73、dev-01、dev-02、dev-03；K3 = dev-04、dev-06、dev-07、dev-09。开新会话时改成对应的 K 号。）

在仓库根目录中工作。开工前先调用 gui-qa-tree Skill，用 Read 读完 SOP（索引与 001–006）与闭包 GUI-QA-TREE-001，重点是 SOP 005 §1 与 §5；压缩或恢复后先重读（根 CLAUDE.md 第二节）。

前提：本组每个分支的标注校验（--stage annotations --unit <单元>，不带 --docs）都必须已经 PASS，它们的分叉父分支也必须 PASS。未满足则停止，报告缺口，不写卡。

任务：为本组每个分支写 audit/GUI-SYNTH-REDO/cards/<分支>.md，章节与规则严格按 SOP 005 §1：
- 五个章节顺序固定；每条以 "- " 开头，并含 [分支#NNNN] 引用；
- `## 终点` 引用本分支末轮；`## 分叉节点` 引用分叉轮（根分支写“根分支，无分叉”并附第一轮引用）；
- 依据以标注为主（status、intent、outcome），需要核对时打开该轮文档（audit/GUI-SYNTH-REDO/qa/<分支>/NNNN.md）；分叉关系读 qa/<分支>/_branch.json；
- 不替综合会话写 synthesis/；只描述 AI 在这些轮做了什么、结果如何，不作数学判断。

完成判据：本组每张卡的校验
  python3 -I -B audit/GUI-SYNTH-REDO/tools/check_annotations.py --stage cards --unit <分支>
退出码为 0，对应报告 reports/cards--<分支>.json 为 PASS。最后的回复列出每张卡的校验结果与未决事项。

禁止：调用 Agent 工具；commit、push；修改 qa/、annotations/、audits/；读取 SOP 006 §2 禁读的材料；删除任何文件。
```

## 3. 综合会话（一个会话，在全部分支卡通过之后开始）

```text
【GUI 问答树 v3 · 综合会话】

在仓库根目录中工作。开工前先调用 gui-qa-tree Skill，用 Read 读完 SOP（索引与 001–006）与闭包；压缩或恢复后先重读（根 CLAUDE.md 第二节）。重点是 SOP 005 §2–§5（综合与接手）与闭包 GUI-QA-TREE-001（特别是 §3 的 D8–D11 与 §6 的 U1）。

前提：所有标注校验（各单元，不带 --docs）与所有分支卡校验（各分支）都已 PASS。未满足则停止并报告。

任务：写 audit/GUI-SYNTH-REDO/synthesis/ 下五个文件：THREADS-MATRIX.md、CLAIMS.tsv、USER-STATEMENTS.md、CONTRADICTIONS.md、HANDOFF.md。格式与规则见 SOP 005 §2–§3。要点：
- 线程说了什么，不等于我们判断它对；综合不替线程背书。
- 每条论断都能回到具体轮 [分支#NNNN]；证据与断言分开，用 status 写明（SUPPORTED、ASSERTED_ONLY、CONTRADICTED、SUPERSEDED、OPEN）；未解决的写 OPEN，不补成结论。
- USER-STATEMENTS.md：用户原话用「」括起，逐字复制自所引轮的文档（可先从标注的 intent_quote 取，再打开原文核对），原话须在单行内，且同一行有 [分支#NNNN]。
- HANDOFF.md：五节标题分别含“先读、跳过、不能相信、待用户裁定、下一步”，下一步 1–5 条；待裁定事项逐条写清需要什么裁定，包括闭包 §6 的 U1，以及审计的分歧是否已裁决（审计未完成则写明未完成）。

完成判据：
1. python3 -I -B audit/GUI-SYNTH-REDO/tools/check_annotations.py --stage synthesis 退出码为 0；
2. python3 -I -B audit/GUI-SYNTH-REDO/tools/check_annotations.py --stage all（不带 --unit）之后，reports/annotations.json 与 reports/cards.json 为 PASS。
最后的回复列出两项校验结果、五个文件的要点与未决事项。

禁止：调用 Agent 工具；commit、push；修改 qa/、annotations/、cards/、audits/ 下的已有文件；删除任何文件。
身份：综合文件没有 reader、model 字段，不适用。
```

## 4. 独立审计会话（一个会话，reader 固定为 audit-1）

```text
【GUI 问答树 v3 · 独立审计会话】reader 固定为 audit-1

在仓库根目录中工作。开工前先调用 gui-qa-tree Skill，用 Read 读完 SOP（索引与 001–006）与闭包 GUI-QA-TREE-001，重点是 SOP 006 §1 与 §4 以及 SOP 003 §2（字段）；压缩或恢复后先重读（根 CLAUDE.md 第二节）。
你必须与所有标注会话不同。在你完成自己的全部审计行之前，不得打开 annotations/ 中的任何文件。

范围：audit/GUI-SYNTH-REDO/audits/<单元>.sample.json 中 docs 列出的全部轮，共 34 轮，分布在 18 个单元。清单只读，不得修改。

做法：
1. 对每个单元读取 audits/<单元>.sample.json，得到轮号；打开每轮的完整文档：
   - 分支单元：audit/GUI-SYNTH-REDO/qa/<单元>/NNNN.md
   - 尾部单元（unexported-XXXXXXXX）：audit/GUI-SYNTH-REDO/qa/_unexported/ 下名称以该 8 位前缀开头的文件夹中的 NNNN.md
2. 独立判断，对每个抽样轮写一行 JSON，追加到 audits/<单元>.auditor.jsonl（字段同 SOP 003 §2）。intent_quote、ai_quote 必须是该轮文档的逐字子串。reader 固定为 audit-1；model 填你本会话的模型 ID（不得为 GLM-5.3 家族）。
3. 全部审计行写完之后，才可以打开 annotations/ 中的标注，然后对每个单元运行：
   python3 -I -B audit/GUI-SYNTH-REDO/tools/check_annotations.py --stage audit --unit <单元>
   最后不带 --unit 运行一次，写出 reports/audit.json（总体一致率）。
4. 不做裁决：不一致的轮只在最后的回复里列出（单元、轮号、标注者的 status、你的 status、理由）。裁决由设计会话写入 audits/<单元>.decisions.md。

完成判据：34 轮都有审计行；每个单元都运行过 --stage audit（PASS 或 FAIL 都如实报告）；reports/audit.json 已写出。最后的回复给出总体一致率（分子、分母）与分歧清单。

禁止：调用 Agent 工具；commit、push；修改 qa/、annotations/、cards/、synthesis/ 与 audits/*.sample.json；读取 SOP 006 §2 禁读的材料；删除任何文件。
```
