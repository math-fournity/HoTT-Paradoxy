# 本收据已被 `20260918-MP-DEDEKIND-OMEGA-GOLD-02` 取代

> 登记时间：2026-09-18（E1 重放审计期间）。本文件为指针，不改动本目录任何原始收据文件。

## 取代原因（两项，均为真过期）

1. **源码清单过期**：本收据的 `source-manifest.json` 捕获于 commit `615fbd2`
   （部分装配期：rounded→ 双向 + located）。此后 `CutGoldForm.agda` 扩展了
   `roundedL←` / `roundedU←` 双向见证方向，当前树的源码哈希与本收据不一致。
   **原始源码 pin 可由 `git show 615fbd2:HoTT/formal/dedekind-omega-missile/CutGoldForm.agda`
   等命令满足**（矩阵行已注明 commit）。
2. **RUN.json `non_goals` 滞后于源码**：本收据登记「`roundedL←` / `roundedU←` 未装配」，
   但当前 `CutGoldForm.agda`（行 353 / 581）已装配且过核——收据陈述滞后于源码事实。

## 判词关系

- 本收据判词 `GOLD_FORM_PARTIAL_ASSEMBLY_NOT_HOTT_CONTRADICTION` 作为**部分装配期历史**保留有效；
- 当前真值判词为 GOLD-02 的 `GOLD_FORM_FOUR_CONDITIONS_COMPLETE`（Book §11.2 四条件首次全部机器接受）；
- 两者共同的不变边界：**不声称 HoTT 不一致、不声称 ℝ 层命题、不声称 LEM/resizing 收费位置已机械化**。

## 后继收据

`HoTT/verification/runs/20260918-MP-DEDEKIND-OMEGA-GOLD-02/`（`--ignore-interfaces`
全量 clean 重放；`verify_formal_proof_run.py --rerun` 于 2026-09-18 达成
`EXACT_EXIT_STDOUT_STDERR_MATCH` / `EXACT_INDEX_SNAPSHOT_MATCH`）。
