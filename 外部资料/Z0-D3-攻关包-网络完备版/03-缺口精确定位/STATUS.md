# 缺口精确定位 / 真实进度（2026-10-11 复核）

> 警告：前一个交接摘要把进度乐观化了。本文件记录 `dev` 工作树实物核对后的**真实**状态。

## 一句话目标

把 `ShCraigElim`（对 `Sh.craig` 推导编码做归纳消去）写成无 `sorry` 的精确 Lean 定理。一旦成立，
归约链立即给出 Z0 完整形式（见 02-目标命题/GOAL.md）。

## 真实进度（不是"9 支已填"）

| 组件 | 真实状态 | 证据 |
|---|---|---|
| `ShCraigElimNegLaw.iT_neg` | ✅ 0 sorry，已编译 | `07-项目模块/GodelQ/ZFC/ShCraigElimNegLaw.lean` 全文无 sorry |
| `ShCraigElimBranches.hWk` / `hVerumIntro` | ✅ 已填（但用的是 `Q=Derivable` 版谓词） | `ShCraigElimBranches.lean` |
| `ShCraigElimSetup.induction_setup` | ❌ **10 个 `sorry` 骨架**，一个支都没填 | `ShCraigElimSetup.lean` 全文 10 个 `sorry` |
| `ShCraigElimBranches.lean` 文档 | ⚠️ 陈旧：仍写"一般 `neg` 相容律尚不存在" | 文档未回改（neg 律其实已证） |

**结论**：neg 律已证但**没接进归纳**；归纳 10 支仍是空骨架。你的工作是从这里开始填支。

## 归纳不变量与两个谓词（架构提醒）

- `ShCraigElimSetup` 用 `P d := Provable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`（单层公式，Σ1 谓词已证）。
- `ShCraigElimBranches` 的 `hWk`/`hVerumIntro` 用 `Q d := Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`（sequent）。
- 建议：把 `induction_setup` 的归纳谓词统一成 `Q`（`Derivable`，sequent 层，与 LK 10 条规则同层），
  支全填完后用 `internal_provable_iff_internal_derivable`（单公式情形）把结论化到 `Provable`，喂给 `ShCraigElim`。

## 10 个规则支现状

| 支 | 需要的关键零件 | 现状 |
|---|---|---|
| axL | `iT_neg`（已证） | 待填 |
| verumIntro | `iT_verum`（已证） | ✅ 已填骨架外（hVerumIntro） |
| andIntro | `iT_and` + 归纳假设 | 待填 |
| orIntro | `iT_or` + 归纳假设 | 待填 |
| allIntro | `iT` 与 `setShift` 相容 | 待填 |
| exsIntro | `iT` 与 `substs1` 相容 | 待填 |
| wkRule | `Derivable.wk` + `translateSeq_mono` | ✅ 已填（hWk） |
| shiftRule | `iT` 与 `setShift` 相容 | 待填 |
| cutRule | `iT_neg` + `iT_and` | 待填 |
| axm | `Sh.craig` 公理形状（`ρ.padding k`）翻译落到 `𝗭𝗙𝗖` 公理 | 待填（唯一用 `𝗭𝗙𝗖` 公理处） |

真正的核心难点是 `iT_setShift` / `iT_substs1`（照已证的 `iT_neg` 模板写）。

## 为什么不能走 Foundation 的 of_provability

`Foundation/.../LK/Interpretation.lean:443` 的 `of_provability` 用完备性定理**语义地**给出
`U ⊢ σ → T ⊢ π.translate σ`，它不产生 V 内部的证明编码，因此搬不进 𝗜𝚺₁。你必须走"归纳 `Sh.craig`
的推导编码"这条路（即本包）。
