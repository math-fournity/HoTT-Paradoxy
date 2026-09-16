# two-level-fibrant-replacement-uip

- proof ID：`MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001`
- claim IDs：`C-227`–`C-232`
- 主源码：`TwoLevelReplacementUIP.agda`
- 理论配置：Cubical Agda 2.8.0 + Cubical v0.9；`--safe --cubical --guardedness`
- 工具链 owner：`../partiality-race-timeout/TOOLCHAIN.json` 与 `../partiality-race-timeout/AGDA_LIBRARIES`
- 论文来源：`audit/literature/LIT-CLASSICS-001/mineru/Annenkov-Capriotti-Kraus-Sattler-2017-2LTT/full.md` §2.7，Theorem 2.20

形式命题、接口对应、控制和禁止外推见 `CLAIM-TWO-LEVEL-FIBRANT-REPLACEMENT-UIP.md`。本包以抽象内层 code 阻止宿主 Cubical Path 直接消去到任意外层类型；`R` 在证明中的作用因而是真实可见的。最终运行必须进入 `HoTT/verification/runs/` 并在 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 追加冻结行后，才可称本项目 `FORMAL_CHECKED_WITH_SCOPE`。
