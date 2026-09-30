# 09 致 Opus 的差量报告与 patch 提案（验收项 D6）

> 编号约定：本文的 C-63、C-67、C-71、C-72、C-75、C-76 指 Opus CG-001 目标内索引的 `CG001-C-NN`（`.claude/goals/CG-001-targeted-overview/证据索引.md`），不是 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 其它节里同号的 claim。

> 2026-09-27；Cloud-Opus 审计会话 → 本仓库 Opus 线（`.claude/`）。按委托工作单 §6，`.claude/` 对本会话只读：以下是**提案**，由用户转交 Opus 走其 REVISIONS／修订流程；本会话没有写 `.claude/` 的任何文件（包括总索引，见文末 D 节）。

> **【2026-09-30 更新：提案已落地】**用户 2026-09-27 授权“入核和登记……立即完成所有剩余的你可以完成的工作”，上面“`.claude/` 对本会话只读、提案由用户转交”的做法因此不再适用。落地情况（全部只加不改，原文保留；`git diff` 逐文件核过只有插入）：
>
> | 提案 | 落地位置 |
> |---|---|
> | P1 | `.claude/思考与发现/CN-039 - …md` §7 第 2 条之下的修订块；§10 第 3 条之下的完成注记 |
> | P2 | CN-039 §7 第 1 条之下的修订块；§7“我的判断”之后的修订块（该块同时吸收 P5 的精确表述） |
> | P3 | `HoTT/formal/claude-cg001/self-interpretation/REVISIONS.md` 新增一节 |
> | P4 | `.claude/goals/CG-001-targeted-overview/证据索引.md` §15 补注（C-63）与 §19 补注（C-75、C-76） |
> | P5 | **点名不成立**：核对后，“发动机/燃料”一类比喻不在 CN-039 里（`.claude/` 下没有这个词），只出现在 GLM 一侧的文件和 GLM-Auditor 的问答里。上面 P5 那句“CN-039 与 GLM 文件都曾……”对 CN-039 的部分是我写错了。精确表述仍被吸收进 CN-039 的“我的判断”修订块，但不是作为对 CN-039 的更正 |
> | P6 | `.claude/总索引/` 的 002、003、004、005 已更新（含 Opus 线遗漏的 CN-039、C-75、C-76、`universe-questioning` 包的补登） |
> | P7 | CN-039 §5 第 3 条之下的修订块；证据索引 §19 补注；`HoTT/formal/claude-cg001/universe-questioning/REVISIONS.md`（新建，因为 `CLAIM.md` 已被运行收据的哈希钉住，不能改） |
> | P8 | 告知性质，无需改动 |
>
> 另：`.claude/goals/CG-001-targeted-overview/relay.md` 文首加了一条 2026-09-30 加注，说明 R1、R2、R3 各自的现状；其中 R3 第 6 条（让非 Claude 的 AI 也能看见总索引）已在根 README 的分片 001 里加了一行指针。

## A. 与 Opus 证据直接相关的新事实

| # | 新事实 | 身份 | 证据 |
|---|---|---|---|
| A1 | **KS 定理 5.9/5.10 的一般 n 已在本仓库机器重放**：`KS-Theorem-5-9 : (n : ℕ) → ¬ isOfHLevel (2 + n) (Type (lvl n))`、`workOrderForm`、`KS-Theorem-5-10-U≤/-Loop`、通用归纳步 `step` | 【数学事实】 | `HoTT/formal/cloud-opus-glm-audit/ks-universe-tower/`；运行 `20260927-COPUS-KS-UNIVERSE-TOWER-01` |
| A2 | C-63 `typeIsNotASet` 名称级闭包无 HIT（101 名）；C-71 `hSetNotSet`（KS 基例）无 HIT（149 名） | 【数学事实】 | `20260927-COPUS-HITSCAN-CERT-OPUS-01`（COPUS-R1-C04）、`-OPUS-02`（COPUS-R1-C06） |
| A3 | C-75 包的 `localGlobal` 名称级闭包无 HIT（201 名）；`universeHasNoLevel` 依赖 `EM₁、EM₁-raw、S¹、Susp、HubAndSpoke` | 【数学事实】 | `-HITSCAN-CERT-OPUS-01`（COPUS-R6-C01）、`-HITSCAN-NEG-02` |
| A4 | `localGlobal` 的**带点**版本 `localGlobal∙`（KS Lemma 5.2 的 pointed 形式）与 KS Lemma 5.1 的一般形式 `ΩΣtrunc` 已写成，可供复用 | 【数学事实】 | `KSUniverseTower.agda` |
| A5 | GLM-R1-C01：一个只含真实 ι 等式、同构于 Bool 的玩具 HIT 语法（未截断）是集合 | 【数学事实】（GLM 证明，本会话复现） | `20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-02` |

## B. patch 提案

### P1 — CN-039 §7 竞争归因 2 与 §10.3（状态更新）

- 现文：§7.2 "没有高阶归纳类型时，上升会沿宇宙层级走：Kraus–Sattler 证明 𝒰_n 不是 n-type，不用高阶归纳类型；本仓库未重放，只作来源。" §10.3 "不用高阶归纳类型的版本（可选）……"
- 提案（追加修订块，不改原文）：
  > 修订（2026-09-27，据 Cloud-Opus 审计 A1）：KS 定理 5.9 已在本仓库对一切 n 机器重放（COPUS-KS-C01，名称级闭包无 HIT）。§10.3 完成。

### P2 — CN-039 §7 竞争归因 1（P-S）的适用范围

- 现文：§7.1 "是大小问题：C-75 发生在同一个宇宙 `Type ℓ-zero` 内部，没有用到大小上升……不归 P-S。【证明】"
- 问题【判断】：对 C-75（带 HIT）的结论正确；但无 HIT 路线（A1）每一步都把 Loop_n 放进 U_{n+1}（`step : NT L k → NT (ℓ-suc L) (suc k)`），P-S 是该路线的必要成分；且按 KS §6，无 HIT 时单个宇宙的"无层"应当不可证，即无 HIT 时落不定的主语是**宇宙塔**。
- 提案（追加修订块）：
  > 修订（2026-09-27）：§7.1 的排除只对带 HIT 的 C-75 成立。无 HIT 路线（COPUS-KS-C01）中，P-S 是必要成分，且"永不停机"的主语由单个宇宙变为宇宙塔（每个 U_n 至少越过 n 层；单个 U_n 的"无层"按 KS §6 应当不可证）。据此 §7"我的判断"中"高阶归纳类型把它集中在一个宇宙里"宜改读为"高阶归纳类型是'单个论域元素永不停'的共同必要条件（来源级，KS §6）；无 HIT 时只有塔版"。

### P3 — C-67 (a) 的读法范围（self-interpretation REVISIONS）

- 现文（REVISIONS 第 3 条）："C-67 (a) 的读法不变：不截断时，语法本身不是集合，它自己的相干又成为义务。"
- 问题【判断】：C-67 (a) 的形式命题 `syntax∞IsNotASet` 依赖 `swap` 的非平凡解释（`ua flipEquiv ≠ refl`）；Opus 已在第 1 条承认 `swap` 不是真实类型论等式。A5 给出一个反向实例：只含真实 ι 等式的（退化）未截断语法是集合。所以"不截断时语法本身不是集合"作为一般读法没有被 C-67 (a) 支持；真实类型论完整语法（含替换、β、η）不截断时是否为集合仍开放。
- 提案（追加 REVISIONS 条目）：
  > 修订（2026-09-27，据 GLM-R1-C01 与 Cloud-Opus 审计）：(a) 的读法限定为"不截断、且语法含本意为非平凡认同的等式（如 swap）时，语法不是集合"。只含真实等式的退化片段（GLM-R1-C01，Tm ≃ Bool）不截断时是集合；真实类型论完整语法的情形开放。C-71 的执照拒绝（截断语法的消去子目标必须是集合）不受影响。

### P4 — 证据索引可引用的 HIT 证书（可选）

- `.claude/goals/CG-001-targeted-overview/证据索引.md` §15（C-63）与 §19（C-75/C-76）可各加一注：C-63 与 `localGlobal` 的无 HIT 已有名称级机器证书（A2、A3）；C-75 主定理与 C-76（k ≥ 2）依赖 HIT 由负证书确认。

### P5 — 关于"发动机/燃料"一类叙事（与 GLM 的 R8 同源）

- CN-039 与 GLM 文件都曾以"单价性是发动机、HIT 是燃料"叙事。【判断】机器证据支持的精确说法是："单价性负责把成员内部的相同提升到宇宙（两条路线共用这座桥）；单个宇宙的永不停还需要 HIT 提供无界高度的成员，宇宙塔的上升则由大小分层提供上一层宇宙。"建议 Opus 在后续笔记中采用此表述。

### P6 — 总索引登记（本会话未写，提案原文）

- 规则冲突【来源事实】：`.claude/rules/hott-claude.md` §4 要求 Claude 会话把工作登记进 `.claude/总索引`；委托工作单 §6 规定 `.claude/` 默认只读、改动走 patch 提案，用户本次也要求相关输出放进 `Cloud-Opus审计并补完GLM`。本会话以更具体、更晚的用户指令为准，没有写入，把登记内容放在这里。
- 提案：在 `.claude/总索引/005 - 工作日志.md` 末尾追加（该片是 `append_target`）：

  > ## 2026-09-27 · Cloud-Opus 云端会话（受委托审计并补完 GLM）
  >
  > - 性质：用户委托的独立审计 + 修正补完（`GLM-5.3-Flash/审计请求/20260927-委托工作单-审计修正补完交付最终卷宗.md`），不是 Claude 线目标包的续做。入口：`Cloud-Opus审计并补完GLM/README.md`。
  > - 与 Opus 线直接相关：KS 定理 5.9/5.10 一般 n 已机器重放（名称级无 HIT）；`CG001-C-63`、`CG001-C-71` 与 `localGlobal` 名称级闭包无 HIT；`CG001-C-75` 主定理依赖 HIT；C-67 (a) 读法建议限定。差量与提案见 `Cloud-Opus审计并补完GLM/09-致Opus差量报告与patch提案（D6）.md`。
  > - 002/003/004 是否吸收，由 Opus 线决定。

### P7 — CN-039 §5 第 3 条与 C-75 行"禁止外推"的一处量词（可选澄清；2026-09-27 终局轮追加）

- 原句【来源事实】：CN-039 §5 第 3 条"每个成员自己那一支的追问在有限层停"；CG-001 证据索引 C-75 行"每个成员自己那一支在有限层停，不宣称有无穷高的单个成员"。
- 问题【判断】：按上下文，"每个成员"指提供非平凡答案的那一族成员 `K n = EM ℤAbGroup (suc n)`，这样读是对的：库引理 `hLevelEM` 给出 `K n` 在第 3+n 层落定。但若读成"Type₀ 的每一个成员"，它既没有被证明，在标准模型中也不成立（例如 S² 没有有限的截断层级【来源转述】）。
- 提案：改为"证明用到的每个成员（`K n`）自己那一支在有限层停；Type₀ 的永不停是'没有统一的一层'，不依赖任何无穷高的单个成员（Type₀ 里是否另有无穷高的成员，本构造不用、不断言）"。终局判词 `14-罗素面终局判词.md` §3.4 已按此收窄（J-003）。
- 这不改变 C-75 的形式命题与证据状态。

### P8 — 终局判词对 CN-039 §8 与 §10 的影响（告知，不需改动）

- `14-罗素面终局判词.md` 在 CN-039 §8 的门一之外，按 M2 补上门二并说明门二怎样随门一而定；另把"永不停机"的主语钉为过程 Q（§3），并给出三级阶梯的邻近对照（UIP 第一步停、`hSet ℓ-zero` 第二步停、`Type ℓ-zero` 永不停）。
- 按 P2/P3 的字面，成功主张只能是强度 I，也就是 CN-039 原来的对象 Type₀（14 §9）。CN-039 §7 的判断因此不受影响。

## C. 不需要 Opus 改动的核对结果

- C-63、C-67、C-71、C-72、C-75、C-76 的形式命题本会话未发现断裂（C-63、`localGlobal` 另有 HIT 证书；C-75 的 HIT 依赖与其 CLAIM 自述一致）。
- CN-039 §5.3 "U 的永不停机是'没有统一的一层'，不是某一个成员无穷高"与本会话结论一致，且在无 HIT 路线下更显重要。

## D. 本会话对 `.claude/` 的写入

- ~~无。本文早先的计划是在 `.claude/总索引/005` 追加一行登记；考虑到委托工作单 §6 的只读边界，改为 P6 提案，由用户决定是否转交 Opus 执行。~~
- **【2026-09-30 更新】**有。用户授权后写了：`.claude/总索引/002`（原位更新）、`003`、`004`、`005`（追加）；`.claude/思考与发现/CN-039` 的修订块；`.claude/goals/CG-001-targeted-overview/证据索引.md` 的 §15、§19 补注；同目录 `relay.md` 文首的加注；`.claude/relay/20260924-attribution-correction/README.md` 文首的应用说明（此前已写）。`.claude/` 里其他文件没有动。另在 Opus 的证明包目录里写了 `HoTT/formal/claude-cg001/self-interpretation/REVISIONS.md`（追加一节）、`universe-questioning/REVISIONS.md`（新建）、`wild-sst-lean/REVISIONS.md` 与 `universe-set-lean/REVISIONS.md`（自查轮，此前已写）。
