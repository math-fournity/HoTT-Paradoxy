# MP-T-PRECISION-TOBS-001

这是 T-PRECISION-DIAGONAL-SOP 的第一个 T-OBS proof package。

| 文件 | 职责 |
|---|---|
| ObservationPrecision.lean | 一般 collision-to-no-decoder 定理、有限 coarse control 与 rich-interface 正控制 |
| WrongObservationPrecision.lean | 伪造 coarse decoder 的 expected-negative control |
| CLAIM.md | C-367 的精确命题、来源分层和禁止外推 |
| LEAN_CORE_TOOLCHAIN.json | 固定 Lean core checker |
| capture_tobs.py | 捕获正向 kernel run |
| capture_tobs_negative.py | 捕获预期拒绝的负控制 |

本包不导入 Mathlib，也不实际构造 quotient。原因是本包的精确命题只需要普通函数、命题、存在和等价；HoTT Book 与 Lean quotient source 只提供“factorization must respect collapsed distinctions”的外部数学背景。

因此，该包所能证明的是一个任务相对 observation interface 的函数论边界。它不能被叙述成 bare ZFC、HoTT、现实时间、哥德尔不完备性或“理论抽象必然导致悖论”的证明。
