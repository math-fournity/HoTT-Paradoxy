# MP-CONTEXT-CHARACTERIZATION-001：上下文等价的完整刻画

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED`

本包收束 `MP-CONTEXTUAL-EQUIV-001` 的层次定理：在此之前只证明了 `≡c` 严格细于结果等价（`C-83`）。本包补上 trichotomy 与一般时间分离后，证明 **Bool 片段上 `≡c` 恰等于代表相等**——上下文族所能区分的最粗等价就是"同一个 `(n,a)` 或同为 `ω`"。

## 冻结命题

- `C-89`：`lt` 三分律：对任意 `n m`，`n ≡ m`，或 `lt n m ≡ true`，或 `lt m n ≡ true`。
- `C-90`：一般严格时间分离：`n ≢ m` 时 `¬ (ret n a ≡c ret m a)`（合并 `C-79` 的 0 步特例与 `C-82` 的单向情形）。
- `C-91`：完整刻画：`(p q : Delay Bool) → (p ≡c q) ⇔ (p ≡ q)`。

## 解释边界（判词）

判词是 `CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED`：

- 在本片段（R041 delay + 固定上下文族 + deadline 观察）上，被完整操作族尊重的最粗等价**就是代表相等**；不存在比代表相等更粗而又被上下文族尊重的可替换关系；
- 由于代表相等已是可能的最细等价，**任何进一步的上下文扩展都不可能区分更多**——"更宽上下文语言"问题在 Bool 片段上因此闭合（需要新值类型或新操作才有新问题）；
- 这既不是 HoTT 悖论，也不是 coverage failure：HoTT 的规则精确地保留了完成先后。

## 不证明（非目标）

- 只覆盖 Bool 值类型与固定 `Ctx`/deadline 观察；不做一般值类型（缺少两元素分离或类似 `fromSome` 工具）的推广；
- 不证明一般商（无可定义 section）上的同类结构；不证明现实并发失配或原创性。

## 证明身份

- proof ID：`MP-CONTEXT-CHARACTERIZATION-001`
- claim IDs：`C-89`–`C-91`
- final run：`20260912-MP-CONTEXT-CHARACTERIZATION-001-01`
- source：`ContextCharacterization.agda`（依赖同目录 `PartialityRaceTimeout.agda` 与 `ContextualEquivalence.agda`）
- toolchain：同目录 `TOOLCHAIN.json` + `AGDA_LIBRARIES`
- index：`../../CLAIM_EVIDENCE_MATRIX.md`

Agda 2.8.0/Cubical v0.9 在 `--safe --cubical --guardedness --ignore-interfaces` 下实际接受本文件。运行原件见 `../../verification/runs/20260912-MP-CONTEXT-CHARACTERIZATION-001-01/`。当前未获 Git commit/tag 授权，不能称 `MACHINE_PROVED_VERSION_CLOSED`。
