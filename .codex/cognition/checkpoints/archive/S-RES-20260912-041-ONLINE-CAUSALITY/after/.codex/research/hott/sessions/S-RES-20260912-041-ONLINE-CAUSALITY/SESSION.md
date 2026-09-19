# S-RES-20260912-041-ONLINE-CAUSALITY

- 触发：S040 方向更新后的第一工作包（在线因果资格第一机器构造）。
- 构造：`Stream := ℕ → Bool`；前缀为嵌套对（`Prefix zero = Bool`，`Prefix (suc n) = Bool × Prefix n`）；在线策略 `(n) → Prefix n → Bool`；完整流函数 `Stream → Bool`。
- 结果：`MP-ONLINE-CAUSALITY-001`（C-106–C-109）通过 kernel：时刻 0 无前视；读第一个输入（时刻 0）与读第二个输入（时刻 1 起）两个正例；完整知识 ≠ 在线资格。判词 `ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS`（非悖论）。
- 运行：final run `20260912-MP-ONLINE-CAUSALITY-001-01`（`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`），零警告。
- 旧证据：矩阵第八次增长后，九个旧包均重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。
- 失败谱系：初版 Fin 索引前缀触发 `UnsupportedIndexedMatch` 警告；改为嵌套对前缀后零警告通过，命题未削弱。
- 边界：不主张物理时间、HoTT 独有或 guarded/clocked 完整翻译；正控制说明并非所有在线任务不可行。
- 三件套：direction/panorama revision 41/generation 025；core 不变（无新用户原文）。
- Git：未 commit、未 tag、未 push。
