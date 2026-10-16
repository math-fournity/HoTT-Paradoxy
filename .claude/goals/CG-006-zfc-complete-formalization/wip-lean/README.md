# CG-006 WIP Lean 源（未收据化，不是交付证据）

2026-10-07 会话 d58e0c0d 在临时目录过核（exit 0，只依赖 propext / Classical.choice / Quot.sound，无 sorry）的文件副本：

| 文件 | 阶段 | 内容 |
|---|---|---|
| `GodelQ/FoundationArith.lean` | S1 | `EffectiveTheory` 落到 Foundation 的任意 Δ1、⪰𝗥₀、Σ1 可靠算术理论 T；哥德尔 I 过程形式（含独立性）、魔鬼交易、与 `incomplete_of_halting_problem` 交叉核对 |
| `GodelQ/ZFC/OmegaArith.lean` | S3a | 任意 `V ⊧ 𝗭` 的 ω 上用 `NaturalNumberRec` 定义加乘；标准数字上算得正确；对 ω 封闭 |
| `GodelQ/ZFC/ArithInterp.lean` | S3b | `arithTrln : DirectTranslation 𝗭𝗙𝗖 ℒₒᵣ`（定义域 ω，`<` ↦ `∈`） |
| `GodelQ/ZFC/R0Model.lean` | S3c | `models_R0 : (N M)↓[ℒₒᵣ] ⊧* 𝗥₀`；`arithInterp : 𝗭𝗙𝗖 ⊳ 𝗥₀` |

构建：`build.sh.txt`（原 scratch 脚本）。LEAN_PATH = 输出目录 : Foundation 构建树 `/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0` : Astra 包；CG-005 模块（`GodelQ/ProcessObservation` 等）取自 `HoTT/formal/claude-cg001/godel-q/`。Lean v4.34.0 固定路径，禁网 sandbox。
正式交付前须迁入 `HoTT/formal/` 包、做 pins 与运行收据并逐字节重放（F-011）。
