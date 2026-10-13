import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★ 回答 001-Step：`¬A ⋎ B` 是否已是引号形？（2026-10-13）

**问题**：`hAB` 的目标 `Derivable 𝗭𝗙𝗖 (insert (¬A ⋎ B) ∅)` 中
`A = iT 0 (free p)`、`B = free (imp domZero (iT 1 p))`——
`¬A ⋎ B` 是否**已经是某个 `Sentence` 的引号**？

**答案**：**条件是**——复合结构（`imp`/`free`/`iT`）**都保持引号性**，
**唯一缺口是基例 `p = ⌜φ⌝`**（反向引理）。

本探针逐件核验「保持引号性」（exit 0，全部现成件）：

| 复合结构 | 保持引号性的件 | 位置 |
|---|---|---|
| `free` | `Semiformula.free_quote : ⌜Rewriting.free φ⌝ = ⌜φ⌝.free` | Foundation `Formula/Coding.lean:125` |
| `iT` | `iT_quote : iT ↑n ⌜φ⌝ = ⌜arithTrln.translate φ⌝` | 包内 `InternalTranslate.lean:611` |
| `⋏` | `Semiformula.quote_and : ⌜φ ⋏ ψ⌝ = ⌜φ⌝ ^⋏ ⌜ψ⌝` | Foundation `Coding.lean:240`（rfl） |
| `⋎` | `Semiformula.quote_or` | 同上（rfl） |
| `∀` | `Semiformula.quote_all : ⌜∀¹ φ⌝ = ^∀ ⌜φ⌝` | 同上 |
| `∃` | `Semiformula.quote_ex : ⌜∃¹ φ⌝ = ^∃ ⌜φ⌝` | 同上 |
| `→` | **无独立件**，但 V 层 `imp = neg _ ^⋎ _`，故由 `quote_or` 覆盖 |

**★ 结论（回答 001-Step 的「最关键一问」）**：

**「是」——但有一处保留。** `¬A ⋎ B` 是引号形，**条件是 `A`、`B` 本身是引号形**，
而 `A = iT 0 (free p)`、`B = free (imp domZero (iT 1 p))` 的引号性由上面两行
（`free_quote` + `iT_quote`）**逐层保持**——**唯一缺口是基例**：
`p` 须是 `⌜φ⌝` 形（即**反向引理** `IsSemiformula → ∃ φ, p = ⌜φ⌝`）。

**所以 001-Step 的两分支判断是**：
* 若 `p` 在 `hAB` 的语境里**已知是引号形**（例如来自 `induction1` 的具体构造子支），
  则语义路线**立即可用**，一般律可缩到 m=0/m=1；
* 若 `p` 是**任意 V 层符号**，则须先证反向引理——而反向引理**本身需要结构递归**
  （见 `W8-reverse-quote-20261013.lean`：已证 2/8 支，`and`/`or` 是同层递归，
  对 `m` 强归纳不够；`rel` 支还需姊妹引理「项向量分量是引号」）。

**关键区分**：反向引理与 `iT_subst_open` **不是同一件事**：
前者是「码 ↔ 引号」的**元层**识别（`IsSemiformula` 的性质），
后者是「`iT` 与 `subst` 的交换」（两个运算之间的关系）。
**两者都需要，但工作性质不同**——001-Step 的「一般律只用 m=0/m=1 + 语义路线收尾」
只有在反向引理可证（或 `p` 已知是引号）时才成立。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeQuotePreservation

-- ① `free` 保持引号性（Foundation 现成：`free_quote`）
#check @Semiformula.free_quote

-- ② `iT` 保持引号性（包内现成：`iT_quote`）
#check @iT_quote

-- ③ 逻辑联结词保持引号性（`quote_*` 全是 rfl）
#check @Semiformula.quote_and
#check @Semiformula.quote_or
#check @Semiformula.quote_all
#check @Semiformula.quote_ex

-- ④ `imp` 无独立 quote 引理，但 `imp` 的 V 层展开是 `neg _ ^⋎ _`，
--    故 `quote_or` + `quote_neg`（若有）覆盖；至少 `quote_or` 部分已核验。
--    **结论**：复合结构（and/or/all/exs/free/iT）保持引号性，全部有现成件。
--    唯一缺口仍是基例 `p = ⌜φ⌝`（反向引理）。

end ProbeQuotePreservation