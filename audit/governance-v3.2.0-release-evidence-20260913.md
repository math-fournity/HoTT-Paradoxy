# governance-v3.2.0 发布与版本闭合证据

状态：`RELEASE_CONTRACT_FOR_LOCAL_ANNOTATED_TAG`。日期：2026-09-13。用户授权：`rulings.md` §16。该 release 只在本地创建，不 push、不发布。

## 1. 版本边界

| 边界 | Commit / ref | 含义 |
|---|---|---|
| 上一已发布治理版 | `governance-v3.0.0` → `636e4e5…` | generation-3 旧边界；不含后续全部研究/治理工作 |
| 接手原貌保全 | `35cace735a58…` | S089 时 1,915 路径完整现场；保留错误 POST 与旧证据措辞供审计，不作为修复版本 |
| proof asset / repair commit | `d3dfb0e1869f5f05527f23ef4cb05dc95352eb10` | 17 个 current proof package、全部 run/index、S090/S091 治理修复可恢复 |
| 本 release ref | `governance-v3.2.0` | 必须指向包含 S092 version-closure checkpoint、本 registry 与本报告的最终 HEAD |

版本级别采用 MINOR：generation-4/三件套/F-011 的 3.2 candidate 已在 baseline 中形成，本轮兼容地补齐 checkpoint/session evidence、record relation、hydration diagnostics、external replay 证据分层和 Git closure；不改变核心三件套职责、STATE v2 主体或用户数学目标。

## 2. 数学资产的 Git 维度

机器 registry：`HoTT/verification/PROOF_VERSION_CLOSURE.json`。

- `d3dfb0e…` 中本矩阵 SHA-256 为 `e598228b…7a18`，58,897 bytes / 210 行；
- 当前矩阵只在该字节前缀之后追加 Git closure 登记，不改 frozen proof/claim rows；
- 17 个 package 覆盖 C-59–C-148 共 90 个 current-project machine-proved claims；C-05 是 1 个 fixed external-library replay；
- 当前项目 proof 状态可标 `MACHINE_PROVED_VERSION_CLOSED`；C-05 可标 `MACHINE_REPLAYED_EXTERNAL_LIBRARY_VERSION_CLOSED_WITH_SCOPE`；
- Git closure 不重证数学、不扩大命题、不认证原创性，也不把 source-inspected `no-global-choice` 变成重放结果。

上表 frozen rows 保留运行建立时的 `LOCAL_UNCOMMITTED` 文本，是为了保持 `index-row-manifest` 可验证。当前 Git 维度只由追加 registry 与 STATE current records 表达。

## 3. S092 闭合合同

S092 Session：`S-GOV-20260913-092-GOVERNANCE-V3-2-VERSION-CLOSURE`。

该 checkpoint 必须：

1. 原子写入 SESSION/RUNS/36-KC audit 与全部 current owners；
2. 把 19 个 current A-record（18 个项目 proof 记录身份，含同一 truncation package 的扩展 records；1 个 external replay）加 exact `version_closure`；
3. current projections 使用 version-closed 状态，历史 Session/RUN.json 不改；
4. 刷新 matrix/Feature/README/registry 等 source hashes；
5. 产生 canonical `transaction.json` 与 `result.json=CHECKPOINT_COMMITTED`；
6. 通过 `scripts/audit/verify_proof_version_closure.py`，创建 tag 后再以 `--require-tag` 复验。

如果 S092 或 tag 失败，本报告不能单独把 release 变为成功；应保留失败并停止 version-closed 声明。

## 4. C01–C10 最终影响组

| ID | 最终处置 |
|---|---|
| C01 | UPDATE：ruling §16；F-003/F-005/F-008/F-009/F-010/F-011/F-012 当前状态与验收 |
| C02 | UPDATE_PROJECT_ONLY：水合/事务 detailed contract；共享 `/Users/aurolafly/codex` NO_CHANGE（产品专属语义，且共享工作树有无关 dirty） |
| C03 | UPDATE_PROJECT_ONLY：治理 Skill 3.2、业务 Skill 1.8、PROTOCOL 2.3、runtime 3.2；共享 workflows/runtime Skills NO_CHANGE |
| C04 | UPDATE：根/`.codex` AGENTS、启动/压缩恢复、checkpoint receipt 与 relation routing |
| C05 | UPDATE：README/docs/MEMORY/Feature/三件套投影/STATE/FRONTIER/LESSONS/RESUME；历史 replacement 保留 |
| C06 | UPDATE：runtime 32/32、scan 2/2、S090 verifier、proof version verifier、S090–S092 canonical receipts、五个真实 task plans |
| C07 | NO_CHANGE：Codex config、Rules/Hooks/plugins、permission/secret 边界没有改变 |
| C08 | NO_CHANGE：OpenCode/其它 host adapters、WebGPT 历史快照、外部 repo 和共享方法库未修改 |
| C09 | UPDATE：baseline、repair、S092 release commit、annotated `governance-v3.2.0`、rollback refs；不 push |
| C10 | UPDATE：S086–S089 receipt gap、S067–S085 KC gap、N38/S088 降级、并行工作树残留与所有 remaining unknowns 保留 |

Remainder = 0。

## 5. 验证矩阵

发布前/后必须通过：

- 8 个项目认知/ledger/projection verifier；
- runtime 32/32、full closure 17/17、core 7/7、three-way 4/4、proof-governance 4/4、scan 2/2；
- S090 verifier（四历史 gap、五 task plans、0 query-first promotion、source pins 0 mismatch）；
- 17 个 proof run 的 source/index 检查；N40/N42 还在本轮实际 `--rerun` 后保持 exact stdout/stderr；
- `verify_proof_version_closure.py`，tag 后 `--require-tag`；
- authored/staged diff `git diff --check`；
- tag 指向最终 HEAD；无活动 writer/transaction；无 push。

任何 PASS 只覆盖其断言。Fresh Python input fidelity 不认证模型理解；Git 资产闭合不认证数学；proof kernel run 不认证现实桥梁。

## 6. 并行工作与提交边界

本轮检测到另一会话新增 `从抽象到悖论——HoTT研究的核心问题意识与思想展开.md`、两个独立 Session 目录，并修改 README/dev-notes。它们被保留在工作树，但不属于本治理 release 的实现提交；README 只暂存本轮 hunks。最终 tag 可以在存在这些未提交并行资产的 checkout 上创建，但必须报告 dirty 残留，不能称整个工作树 clean。

## 7. 研究状态不被 release 夸大

Release 后第一数学主线仍是固定下游应用/派生开发的真实 E6 consumer；T3 联合递归为第二线；batch 13 和无差别基础库扫描降优先级。仍未得到 E6、现实桥梁、自馈不可停机实例、`NATURAL_USAGE_MISMATCH` 或 HoTT 悖论。
