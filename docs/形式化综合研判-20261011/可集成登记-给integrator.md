# 可集成登记（CG-009 产出，2026-10-11）

> 本文件是**给 integrator / 下一会话的增量补丁草稿**。按根 CLAUDE.md 第一节，本会话不直接改共享文件（`HoTT/CLAIM_EVIDENCE_MATRIX.md`、`形式化追踪/` 等），只把应登记的增量写在这里。行格式与现行共享文件一致（裸 claim id、单行追加、不删行）。

## A. 形式化追踪 · 99-更新日志（追加行）

```
2026-10-11 | 跨工位 | CG-009 综合审查：38 个 worktree 全量初筛；bd4295b5 的 Z0CraigBridge 条件归约层（反向桥三档，含 ⊥ 处版本）独立编译超时、未过核，登记为候选；ef7e5239 的 CG-008 Phase 0 锚点与条件收尾独立编译 exit 0；HoTT-machine-overview 的 Cubical 哥德尔基础设施线（9 条收据）尚未登记入矩阵 | 未提交（本 worktree）
```

## B. 形式化追踪 · 01-有哥德尔路线 README（"下一步"节增量）

- **2026-10-11 CG-009 独立核验**：`dev-bd4295b5` 工位的 `Z0CraigBridge.lean` 给出三档条件归约：`hbl3_of_reverse_on_image`（只在 `zfcTr` 像上的反向桥 ⇒ HBL3）、`hbl3_of_pointwise_equivalence`（逐点等价 ⇒ 前者，更强）、`zfc_z0_full_of_reverse_at_bottom`（只在 ⊥ 处反向桥 ⇒ 最终 Z0）。整文件三次编译均超时（240 s / 580 s / 580 s），与该作者自记的"`cl_prover` 12M 心跳超时"一致；**但其最轻定理 `hbl3_of_reverse_on_image` 经本会话隔离探针（逐字证明体、无 `cl_prover`）编译 exit 0，公理仅三条标准公理**——超时确认来自 `cl_prover` 重的兄弟定理。负控制 `WithoutCraigBridge.lean` exit 1（内核拒绝 Craig-HBL3 冒充 zfcTr-HBL3），按预期工作。
- **CG-008 锚点核验**：`dev-ef7e5239` 的 `ZFCSetSigma1.lean`（Phase 0 锚点）与 `Z0Final.lean`（条件收尾）在本会话独立编译 **exit 0**，公理均仅三条标准公理。CG-008（Lévy-Σ₁ 完全性）作为与 ShCraigElim 并列的候选路线成立；两条路线是否同一缺口仍待机器证据。

## C. CLAIM_EVIDENCE_MATRIX 建议行（未写入，待 integrator 决定编号）

Cubical 哥德尔基础设施线（来源 `/Volumes/D/HoTT-machine-overview`，分支 `feat/machine-overview-m1`，2026-09-14 运行）。**2026-10-11 本会话已用 pinned Agda 2.8.0 + cubical v0.9 对 10 个源文件逐字副本独立重放，10/10 exit 0**（证据 `.cg009-cubical/RUN.json`）——登记时判词可写"canonical 本机重放通过（CG-009，2026-10-11）"：

| 建议行（裸 id） | 包 | 运行 | 判词建议 |
|---|---|---|---|
| MP-CGI-PROOF-CHECKER-001 | `HoTT/formal/cubical-godel-infrastructure/MiniProofChecker.agda` | 20260914-CUBICAL-GODEL-PROOF-CHECKER-001 | KERNEL_ACCEPTED_WITH_SCOPE（已过核，未登记） |
| MP-CGI-PROOF-SERIALIZATION-001 | 同包 `ProofSerialization.agda` | 20260914-CUBICAL-GODEL-PROOF-SERIALIZATION-001 | 同上 |
| MP-CGI-FORMULA-BITCODE-001 | 同包 `FormulaBitCode.agda` | 20260914-CUBICAL-GODEL-FORMULA-BITCODE-001 | 同上 |
| MP-CGI-PROOF-BITCODE-001 | 同包 `ProofBitCode.agda` | 20260914-CUBICAL-GODEL-PROOF-BITCODE-001 | 同上 |
| MP-CGI-NAT-PROOF-CODE-001 | 同包 `NatProofCode.agda` | 20260914-CUBICAL-GODEL-NAT-PROOF-CODE-001 | 同上 |
| MP-CGI-PROOF-SEARCH-CLASSIFIER-001 | 同包 `ProofSearchClassifier.agda` | 20260914-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001 | 同上 |
| MP-CSI-*（5 条） | `HoTT/formal/cubical-synthetic-incompleteness/SyntheticIncompleteness.agda` | 20260914-CUBICAL-SYNTHETIC-INCOMPLETENESS-001 | 同上 |
| MP-CMH-*（3 条） | `HoTT/formal/cubical-machine-halting/MachineHalting.agda` | 20260914-CUBICAL-MACHINE-HALTING-001 | 同上 |
| MP-CCC-*（5 条） | `HoTT/formal/cubical-candidate-coverage/CandidateCoverage.agda` | 20260914-CUBICAL-CANDIDATE-COVERAGE-001 | 同上 |

**注意**：这批包的 `RUN.json` 自报 `git_status: LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`、`index_status: INDEXED_IN_CLAIM_EVIDENCE_MATRIX`（指向其所在 worktree 的矩阵副本）。是否正式纳入 canonical 矩阵、以及编号（D0x 前缀还是 CG001 前缀），由 integrator 与编号账本决定。本会话只做"未登记"事实报告与来源核对（收据文件与 CLAIM.md 逐字节读取）。

## D. 对 `形式化追踪/README.md` 总览的增量建议

- "分支上的形式包"行：八方向覆盖闭合的陈述保持不变；**补充一句**：另有一批 2026-09-14 的 Cubical 哥德尔基础设施包（机器总览工位）未在覆盖清单内，属"第九条线"性质的补充来源，待编号后登记。
- "有哥德尔路线"行：在 Z0 行末补"（2026-10-11：CG-009 独立核验 CG-008 锚点 exit 0、bd4295b5 条件桥编译超时未过核）"。

## F. 建议登记：CG-009 自研成果 Z0LocalGate（单句完成门）

来源：本会话（Claude，CG-009），文件 `docs/形式化综合研判-20261011/成果-Z0LocalGate/Z0LocalGate.lean`（**最终 sha256 `24ea1cb1…`**，本会话 pinned Lean 4.34.0 + Foundation `1fb01b72` 实测 exit 0；**14 条 `#print axioms` 全部仅三条标准公理**；含正对照 `gateG_standard`（门在 ℕ 成立）；负控制 `Z0LocalGateNegative.lean` 内核拒绝、exit 1 预期）。

建议 claim 行（编号待 integrator 定，如 `CG001-C-391` 起的下一个空号）：

| 建议行（裸 id） | 文件 | 内容 | 判词建议 |
|---|---|---|---|
| CG001-C-<next> | `Z0LocalGate.lean`（拟入 `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/`） | 单句完成门：最终 Z0 的完整形式只需 Gödel 句 G 处的一条单句前提（`gateG : 𝗜𝚺₁ ⊢ □Craig(zfcTr G) 🡒 zfcTr(zfcTr G)`，等价于单句消去 elim@G；另附 ⊥ 门与 `keyE@image` 规范形状对接） | 条件定理（前提仍是假设）——**不得读成 D3 已证**；证明已过核，前提未支付 |

**注意**：该成果为**条件归约**，与 `Z0Full.zfc_z0_full_of_D3_internalize` 同性质但门更弱（全称→单句）。登记时应写明"完成门收缩"，不要写成"Z0 已证"。是否并入 `dev`、用哪个编号，由 integrator 决定。

## E. 边界

- 本登记的所有"exit 0/exit 1/超时"均为本会话 pinned 环境（Lean 4.34.0 + Foundation `1fb01b72` + Mathlib `5ed29652`，1893 依赖摘要核对）实测；不是 canonical 收据。
- 涉及他人未提交文件的引用均为只读；未复制进本 worktree 的源码保持原位（核验副本在 `.cg009-verification/src/`）。
- 是否吸收、编号、提交，均待研究发起人与 integrator 决定。
