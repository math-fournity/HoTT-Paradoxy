# S-GOV-20260913-MACHINE-OVERVIEW-M1

- 目标：在用户指定的**新 git worktree** 上实现 repo 外方案《HoTT 非现实性悖论机器统观完整方案》的自动化统观系统（方案 M0/M1），并贯通一条真实的「固定来源 → 自动生成候选 → 缩减 → 原生 HoTT 核验 → 现实对应审查 → 保存/恢复」链路。
- 工作位置：worktree `/Volumes/D/HoTT-machine-overview`，分支 `feat/machine-overview-m1`（base `fc79094`，local-only，未 push、未 tag）。
- 交付：
  - `machine-overview/`：协调器（`inspect-profile` / `create-case` / `search` / `verify` / `review-correspondence` / `explain` / `list` / `get` / `query` / `validate` / `selftest`）、profile/task/grammar、pinned Agda support 模块、cases/runs/reviews/reports/generated-index。
  - L1 校准链路实跑：profile 全部 pin PASS；文法内**完整枚举** 4,788 次 pair-context 检查、916 个分离、缩减为 50 个见证，分三族（deadline 14 / value 28 / completion-divergence 8）；`calibration_match=PRESENT`（R041/C-73–C-74）；顺序置换集合相同；删除 deadline 操作后该族消失。
  - 三族各取最小见证做原生 Cubical Agda 核验：`verify` exit 0、`controls` exit 0、负控制按预期非零、重放 stdout/stderr 字节一致；两次模板缺陷导致的失败运行（`...-COMPLETION-001`、`...-VALUE-001`）逐字节保留。
  - 另测：候选以 `postulate` 冒充目标时在产生任何副作用前被拒（`CANDIDATE_FORBIDDEN_DECLARATION:external_file:postulate`，exit 2，无 run 目录残留）；目标哈希篡改走 `TARGET_CHANGED` fail closed（单元测试）。
- 诚实边界：三族核验对象是**已有 C-73–C-75 机制的校准实例**，不是新数学 claim；探索收据只留在 `machine-overview/runs/`，未触碰 `HoTT/formal`、`HoTT/verification/runs`、`HoTT/CLAIM_EVIDENCE_MATRIX.md`。现实桥梁 `UNRESOLVED`；L3（稠密性/运动结构）与 B 方向未建任务。
- 已知集成缺口：`scripts/audit/capture_agda_proof_run.py` 要求 `(root/".git").is_dir()`，普通 worktree 的 `.git` 文件会被拒（`PROJECT_GIT_ROOT_REQUIRED`）；因此本轮用 coordinator 自己的 `machine-overview-kernel-run` 收据，F-011 canonical 捕获与矩阵落库属于 M5。
- 治理 verifier（worktree 内实测）：`verify_governance_shards`、`verify_three_way_cognition`、`verify_ledger_retrodiction`、`verify_proof_version_closure` 四项 PASS；`verify_understanding_merge`、`verify_fresh_three_way` 仅在缺失被 `.gitignore` 排除的嵌套资产时 FAIL（`AI对话录/理解章节`、`sources/local-gpt/ALL-Markdown-root/HoTT_is_GONE_COMPLETE.md`），属既有 worktree 移植性缺口。
- 未执行：M2–M5；主线 canonical checkpoint（`cognition_runtime.py checkpoint --apply`）；push/tag；对 `方向追踪.md`/`全景视野.md` 的主线写回。
