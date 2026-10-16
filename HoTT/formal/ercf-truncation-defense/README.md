# MP-ERCF-TRUNC-001：命题截断的原生防御边界

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / DEFENSE_WORKS`

本目录选择 Cubical Agda 的原生 Path 与 higher inductive type 语义，审查 propositional truncation 作为“理论信息经济”接口时允许和拒绝什么。

## 冻结命题

- `C-67`：squash HIT 可以消去到已给 `isProp` 证明的目标；这是受保护 consumer。
- `C-68`：二重命题截断可压平为单次截断，并在点构造上按 `refl` 计算。
- `C-69`：任意 `f : ∥ Bool ∥₁ → Bool` 都把两个 canonical Bool 点映到 path-equal 输出。
- `C-70`：不存在同时满足 `extract : ∥ Bool ∥₁ → Bool` 与逐点保持 `extract ∣ b ∣₁ ≡ b` 的 consumer。

## 解释边界

这组命题若通过，只说明 Cubical Agda 的 propositional truncation 确实遗忘 witness 差异，并用 path constructor/消去规则阻止无条件 point-preserving untruncation。它应被分类为 `DEFENSE_WORKS`：理论拒绝把 mere existence 提升为已经取得原 witness。

它不证明 HoTT 内部矛盾、现实任务失配、所有选择原则不成立、任意 `∥ A ∥₁ → A` 都不存在，也不证明 ERCF-3。常值函数说明后一个无条件说法是假的；真正被排除的是附带 point-preservation 合同的 extraction。

## 证明身份

- proof ID：`MP-ERCF-TRUNC-001`
- claim IDs：`C-67`–`C-70`
- final run：`20260912-MP-ERCF-TRUNC-001-01`
- source：`TruncationDefense.agda`
- toolchain：`TOOLCHAIN.json` + `AGDA_LIBRARIES`
- index：`../../CLAIM_EVIDENCE_MATRIX.md`

Agda 2.8.0/Cubical v0.9 已在 `--safe --cubical --ignore-interfaces` 下实际接受本文件；运行原件、外部依赖哈希与命令在 `../../verification/runs/20260912-MP-ERCF-TRUNC-001-01/`。工具链、官方 release digest、Cubical library tag/tree identity 和外置缓存位置见 `TOOLCHAIN.json`。当前未获 Git commit/tag 授权，因此不能称 `MACHINE_PROVED_VERSION_CLOSED`。
