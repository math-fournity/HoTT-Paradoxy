import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## 反向引理的 `definability` 障碍：换表述（2026-10-13）

原表述 `P n q := ∃ k φ, n = ↑k ∧ q = ⌜φ⌝` 的 `definability` 过不去，
因为 `⌜φ⌝` 里的 `φ : Semiproposition` **不是 V 层对象**。

**关键认识**：其实不需要 `Semiproposition`！
`IsSemiformula.case_iff` 已经给出「码由构造子拼成」的**纯 V 层**刻画，
而每个构造子（`^rel`/`^⋏`/`^∀` …）都是 V 层函数，**可定义**。

故正确表述应是**纯 V 层**的：「存在一个由构造子拼成的码」——
但那就是 `IsSemiformula` 自身，循环了。

**本探针核验：`definability` 对哪种表述可行。** -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeRevQuoteDef

-- 表述 1（纯 V 层，无 Semiproposition）：`P n q := IsSemiformula L n q`
-- 这当然是 Σ₁ 可定义的（Foundation 已证），但循环——结论就是前提
#check @IsSemiformula.defined

-- 表述 2：用 `encode` 的像（若 Foundation 给了 V 层的 encode 刻画）
#check @Semiformula.quote_eq_encode
#check @Semiformula.coe_quote_eq_quote

-- 表述 3：`∃ φ : Semiproposition, q = ⌜φ⌝` —— 直接测试 definability
-- ⚠ 量词的宿主类型是 `Semiproposition ℒₛₑₜ 0`，**不是 V**，
--    故 `definability` 无法把它变成 V 层的有界量词 —— 这就是障碍所在。
-- ⚠ 下面这个 example **刻意失败**，它就是本探针的发现
-- example : 𝚺ᴬ₁-Relation (fun (q : V) ↦ ∃ φ : Semiproposition ℒₛₑₜ 0, q = (⌜φ⌝ : V)) := by
--   definability

-- ★ 结论（本探针的发现）：
-- `definability` 对 `∃ φ : Semiproposition …` **失败**，
-- 因为量词的宿主类型不是 V，无法变成 V 层的有界量词。
--
-- **但出路在于**：`IsSemiformula` 本身**已经是** Σ₁ 可定义的
-- （`IsSemiformula.defined`，Δ₁ 级），故**不需要**这条谓词——
-- 反向引理的归纳谓词应当写成**纯 V 层**的形式，例如
--   P n q := IsSemiformula ℒₛₑₜ n q ∧ ∃ ...（V 层成分）
-- 而那正是循环。
--
-- ⇒ **反向引理不能靠 sigma1_structural_induction 证**。
-- 真正的出路是**对码本身做 V 层递归**，或用 ℕ 层版 + 转移。
-- 这是本探针的诚实结论，不再往下推。

end ProbeRevQuoteDef