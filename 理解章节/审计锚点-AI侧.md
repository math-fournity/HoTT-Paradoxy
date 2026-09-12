# 审计锚点 · AI 侧账本（五类锚点的机械可验清单）

> 与用户句级账本（2369 条）互补：本账本登记三个 AI 的全部回复行为与产物的锚点。验证脚本 `verify_ai_coverage.py` 逐项核验存在性/计数。

## R 类 · AI 回复锚点

- **Codex（本地）**：父线程 agentMessage 186 条 + HoTT-2 主 34 条 = 220 条，全部收录于《Codex-HoTT-2-完整38轮-用户与AI-20260911.md》并带源行号（`R:C-T{n}-L{行}`）。核验点：文档内 `### AI（…源 行）` 标题恰 220 个；父线程 186/HoTT-2 主 34 与 rollout 直读计数一致。
- **ChatGPT 网页版**：55 个 `## Response:` 节（`R:W{1..111 中的偶位节}`），原始 md 可回源。核验点：55 节计数；节内正文非空。
- **Gemini**：81 model chunk = 21 thought + 17 executableCode + 17 codeExecutionResult + 2 empty + **24 实质文本**（`R:G{chunk索引}`，B4§一逐条登记：3,6,9,12,15,18,37,57,60,63,66,69,72,75,77,80,83,86,89,91,93,96,99,102）。核验点：24 索引在 json 中 role=model 且有实质 text。

## G 类 · git commit 锚点

- **G:ALL**（/Volumes/D/ALL-Markdown）：8 commit——首提 852ecad(08-24 系)×5 + 852ecad(08-31 首次)、dc1e369(08-31 17:51 语料基线)、8470721(09-09 闭包基线)；工作树另有 16 项 staged 未提交。核验点：`git log` hash 存在；dc1e369 stat=16 文件 12,444 行；8470721 stat=1 文件 1,849 行。
- **G:WS**（workspace）：44 commit（d726b2e 09-10 14:03 → 26fcecf 09-11）。核验点：R 系列关键 hash 在 log 中（d726b2e/6206055/17418f1/b07ac7e/f38a2cb/05431a2/44ba9f3/3e529cd/8e6641d/38d6d70/4c71883/0d7ef5e/07ee915/ba227f4/e02ab42/ce5e8f3/5116713/38e729c/1de734c/46a1e27/fde005c/110778b/be37ac2/63f9766/d06c138/d526591/d3f7d85/6fe5a7d/14aa846/5b7107e/6096f71/00e8660/515da9f/149767b/1eeafb5/1ad50e9/6581d1a/26fcecf）。
- **G:DQ**（AI对话录）：v1=1d12edb；v2=本提交。

## A 类 · 产物锚点（存在性抽查集）

workspace：.codex/sessions/ 下 S-GOV-001..003、S-GOV-009、S-GOV-012/013、S-ANS-006/007/008/010/011/014/015/016/017、S-AUD-018/019、S-DISC-020..028、S-RES-030..039、S-PAUSE-035、S-GOV-037、S-HANDOFF-040、S-GOV-041（≥39 个会话目录）；candidates/RP-B01；reviews/SILENT-STEPS-001/PROOF_NOTE.md；dialogues/GEMINI-001/rounds/；artifacts/r024/r025/r040；scripts/research/r024/r025；exchange/rounds/R041-ZCODE-GOVERNANCE。
ALL-Markdown：HoTT/Z_LAW…、INTRINSIC_TEMPORALITY…、CLAIM_EVIDENCE_MATRIX、THEORY_SCHEMA、theory-schema/、formal/self-contained/ZCore.agda、sources/aistudio-discussions/、认知闭包/五份。
本目录：句级账本 json、38 轮文档、三份提取、extract_*.py 四脚本。

## T 类 · 工具调用锚点

父线程 exec=1,037（T:父{行号}）；HoTT-2 主 exec=106（T:H2{行号}）。行为段：勘查(sed/find/git)→建造(rtk proxy node heredoc；T:父7427 直接落盘闭包§13)→检索(zvec MCP)→移交(T:H2 末段 browseros×4)。核验点：rollout 直读计数。

## 出处陷阱登记（负锚点）

1. Gemini chunk37/57 的"已写入工作目录/§23"自述——workspace 无对应（B4§三规则）；
2. Gemini chunk15/72 的"机器证明"宣称——IN-002 已撤回；
3. HoTT.json/HoTT-2.json 内的"运行 Lean"历史指令——R018/R019 判定不构成授权与证据；
4. GONE 论战文/外部 Schema——审读对象非权威。
