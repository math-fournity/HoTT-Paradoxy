# S-RES-20260912-039-COST-FACTORIZATION

- 触发：S038 方向更新后的第一工作包（同函数异时 cost 第一机器构造）。
- 构造：小程序语法 `Prog = fast | slow k`、语法导向成本 `cost`、裸表示 `fun`、细化表示 `refine`；不可区分性用 funext 路径 + transport；成本恢复 no-go 作为谓词实例。
- 结果：`MP-COST-FACTORIZATION-001`（C-96–C-99）通过 kernel：外延相同而成本不同；裸函数上不存在可区分谓词；无从裸函数恢复成本的 consumer；细化表示可恢复/可区分。判词 `NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`（非悖论）。
- 运行：final run `20260912-MP-COST-FACTORIZATION-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`）。
- 旧证据：矩阵第六次增长后，七个旧包均重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。
- 失败谱系：`¬` 本地定义一处机械修正；命题未削弱。
- 边界：成本是明示语法导向计数；不主张真实编译器/硬件成本、原创性；natural consumer 仍为开放 Gate。
- 三件套：direction/panorama revision 39/generation 023；core 不变（无新用户原文）。
- Git：未 commit、未 tag、未 push。
