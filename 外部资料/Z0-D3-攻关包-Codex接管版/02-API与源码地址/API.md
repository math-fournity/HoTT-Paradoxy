# 可用引理与 API（本机实测精确名字）

## 项目包内（GodelQ/ZFC/）

| 名字 | 文件 | 签名要点 |
|---|---|---|
| `iT` | InternalTranslate.lean:256 | `iT (n p : V) : V := iT.construction.result ℒₒᵣ n p` |
| `iT_rel` / `iT_nrel` | InternalTranslate.lean:538/ | `iT n (^rel k R v) = iTR n k R v` 等 |
| `iT_verum` / `iT_falsum` | InternalTranslate.lean: | `iT n ^⊤ = ^⊤` |
| `iT_and` | InternalTranslate.lean:552 | `iT n (p ^⋏ q) = iT n p ^⋏ iT n q`（需 IsUFormula ℒₒᵣ p q） |
| `iT_or` | InternalTranslate.lean:556 | `iT n (p ^⋎ q) = iT n p ^⋎ iT n q` |
| `iT_all` / `iT_exs` | InternalTranslate.lean: | 量词层 +1 |
| `iT_quote` | InternalTranslate.lean:611 | 仅引号化：`iT 0 ⌜φ⌝ = ⌜arithTrln.translate φ⌝`（C-119） |
| `translateSeq` | SeqTranslate.lean | `∀ y, y ∈ translateSeq s ↔ ∃ x ∈ s, y = iT 0 x` |
| `isSemiformula_iT` | SeqTranslateFormula.lean:348 | `IsSemiformula ℒₛₑₜ n (iT n p)`（C-391 主定理） |
| `models_zfcTr_iff` / `models_zfcTr_iff'` | Z0Full.lean / Z0UniBridge.lean | V ⊧ zfcTr σ ↔ Provable ZFC ⌜translate σ⌝ |
| `zfcTr_sigma1` | Z0Full.lean | zfcTr σ 是 Σ1 句 |
| `ShCraigElim` / `bwd_of_shcraig_elim` | Z0UniBridge.lean | 归约链（C-390） |

## Foundation（1fb01b72，路径相对 Foundation/）

| 名字 | 路径 | 作用 |
|---|---|---|
| `Derivation.induction1` | FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:642 | 10 支推导归纳 |
| `internal_provable_iff_internal_derivable` | 同上 :939/947 | Provable T φ ↔ Derivable T (insert φ ∅) |
| `Derivable.wk` / `verum` / `and_m` / `or_m` / `cut` / `by_axL` | FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:792+ | LK 规则（sequent 层） |
| `sigma_one_complete` | FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean 末 | 算术理论的 Σ1 完全性 |
| `provable_internalize` | 同上 | 只对 ArithmeticTheory |
| `internalize_provability`（D1） | FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D1.lean:27 | T ⊢ φ → Provable T ⌜φ⌝ |
| `modus_ponens_sentence`（D2） | DerivabilityCondition/D2.lean:30 | Provable 层 MP |
| `Theory.craig` | FirstOrder/Arithmetic/Bootstrapping/Syntax/CraigTrick.lean | 用 choice 挑出的 Σ1 一致句 |
| `UformulaRec1.Construction.semiformula_result_induction` | FirstOrder/Arithmetic/Bootstrapping/... | 对 UformulaRec1 构造做 formula 层归纳（iT_neg 用它） |
| `IsUFormula.neg_neg` / `neg_and` / `neg_or` / `neg_all` / `neg_ex` | FirstOrder/... | 否定对合与 De Morgan |
