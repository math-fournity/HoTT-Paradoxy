import GodelQ.ZFC.ShCraigElimSetup
/-!
裁决探针 6（**不是收据**）：回答 004-Step 的问题——`Theory.Δ₁ T` 有没有"用 `T.RE` 构造"的通用路径。

读 Foundation `Bootstrapping/Syntax/Theory.lean` 的 `class Δ₁`（:16）：
  ch : 𝚫ᴬ₁.Semisentence 1
  mem_iff : ∀ φ, ℕ ⊧/![⌜φ⌝] ch.val ↔ ∃ σ ∈ T, φ = σ
  isDelta1 : ch.ProvablyProperOn 𝗜𝚺₁

Foundation 给出的**所有** `Δ₁` 实例构造子（grep 全库）：
  - `Theory.Δ₁.ofFinite`（Set.Finite）
  - `Theory.Δ₁.singleton`
  - `Theory.Δ₁.add` / `insert`
  - `Theory.Δ₁.ofEq`
  - `InductionScheme.delta1_of`（**这是唯一的通用模板**，要求调用方给出 Δ₁ 谓词 + 与 C 的对应）
  - `T.craig` 的实例（CraigTrick.lean:311）
  - 𝗣𝗔⁻、Con、Incon、InductionScheme univ/hierarchy/prenex

**没有 `Theory.Δ₁_of_RE`。** `RE`（`REPred (· ∈ T)`，即 Σ1 可枚举）与 `Δ₁`（须同时有 Σ1 和 Π1 表示）
不同：`Δ₁` 要求特征式是 𝚫 层。

本探针核三件事：
  (1) `Sh.RE` 合成（`Sh_RE`）——已合成，**`Sh.RE` 不是未证前提**；
  (2) `Theory.Δ₁ Sh` 不合成；
  (3) `Sh` 的定义（`Z0Shadow.lean:35`）中的 `⌜translate σ⌝` 引用 `iT`，而 `iT` 是
      **本包定义的内部翻译**，不是 Foundation 的原生构造子——`Sh` 的成员谓词
      因此**不是 Foundation 意义上的原生 Δ1/RE 谓词**，而是"`iT` 图 + 𝗭𝗙𝗖 可证性"的复合。
      这就是 `Sh.RE` 虽能合成、`Theory.Δ₁ Sh` 却不能的原因吗？本探针只记录现象，不断言原因。
-/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

namespace GodelQ.ProbeD1Sh

-- (1) Sh.RE 合成
#synth (Sh.RE)

-- Sh.RE 来自哪里
#check @Sh_RE_of_translate_computable
#check @zfc_z0

-- (2) Theory.Δ₁ Sh 不合成（单独放一个文件报错，这里只记录）

-- Sh 的定义
#print Sh

end GodelQ.ProbeD1Sh
