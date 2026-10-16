# 可用引理与关键 API 引用（本机已实测）

## 本项目已证、可直接 `rw` / `apply` 的零件

| 名称 | 位置 | 形状 / 用途 |
|---|---|---|
| `iT_neg` | `07-.../ShCraigElimNegLaw.lean` | 一般（V 内任意公式码）`iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)`，9 支全填，0 sorry。**写 `iT_setShift`/`iT_substs1` 的模板** |
| `iT_and` / `iT_or` | `07-.../InternalTranslate.lean` | `iT 0 (p ⋏ q) = iT 0 p ⋏ iT 0 q`（同形 `iT_or`）；注意只对公式，V 内任意码可用 |
| `iT_verum` / `iT_falsum` | `InternalTranslate.lean` | `iT 0 ⊤ = ⊤` 等 |
| `iT_quote` | `InternalTranslate.lean:611` | **只对引号化公式** `iT 0 ⌜φ⌝ = ⌜arithTrln.translate φ⌝`；归纳支拿到的是 V 内任意码，不能直接用 |
| `isSemiformula_iT` | `07-.../SeqTranslateFormula.lean` | 主定理：`IsSemiformula ℒₛₑₜ 0 (iT 0 x)` |
| `translateSeq_mono` | `SeqTranslate.lean` | `translateSeq` 保包含 |
| `Derivable.wk` / `verum` / `and_m` / `or_m` / `axL` / `cut` | `Foundation/.../Bootstrapping/Syntax/Proof/Basic.lean`（`:798` 附近 and_m） | LK 规则，sequent 层 |
| `internal_provable_iff_internal_derivable` | Foundation（单公式情形） | 把 `Derivable` 结论化到 `Provable` 喂给 `ShCraigElim` |
| `IsUFormula.neg_neg` / `neg_and` / `and` / `imp` / `subst` / `rel` / `qqAlls` | `Foundation/.../Formula/Functions.lean` | 结构引理，neg 律模板里已大量使用 |
| `IsSemiterm.bvar` / `IsSemitermVec.cons_iff` / `isSemitermVec_shiftVec` | Foundation | 项侧引理 |

## 关键 Foundation 文件（已在 06/ 清单里，附本地行号）

- `FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:642` — `Derivation.induction1`（10 支）
- `FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:798` — `Derivable.and_m`
- `FirstOrder/Arithmetic/Bootstrapping/Syntax/CraigTrick.lean` — `Sh.craig` 公理形状（`ρ.padding k`）
- `FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean` — Foundation 对 `Sh.craig` 的 D3（`inferInstance`）
- `FirstOrder/LK/Interpretation.lean:443` — `of_provability`（语义，不可内化，故不能走这条路）
- `FirstOrder/Arithmetic/Bootstrapping/Syntax/Formula/Functions.lean` — `IsUFormula.*` 结构引理

## 工具链 pin（不得修改 Foundation/Mathlib 源码）

- Lean 4.34.0（commit `293d5d0c` 的工具链），Mathlib `5ed29652`，Foundation `1fb01b72`。
- 新引理只能写成包内新文件，按包内既有顺序加入编译驱动；带 `sorry` 的文件不进收据源。
