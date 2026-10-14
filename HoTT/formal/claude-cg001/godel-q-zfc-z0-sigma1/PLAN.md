# godel-q-zfc-z0-sigma1：工作计划（012-Opus，2026-10-14，未开工的部分）

> 本包在独立 worktree `/Volumes/D/HoTT-worktrees/012-opus-w8`（分支 `claude/012-opus-w8`，取自 dev `c491326e`）。
> 现状：只复制了依赖链（23 个模块，与 `godel-q-zfc-z0-translate` 逐字节相同，已核对）并生成固定记录（导入闭包 1,893 个模块，聚合 `02b0e80f…5161`）。`Z0Full.lean` 尚未复制进来。
> 编译：`devbuild_ns.py`（`.claude/goals/CG-007-formalization-completion/tools/`），依赖链清单在本会话 scratchpad 的 `s1_chain.txt`。多参数命令用 bash（zsh 不分词）。

## 1. 反例（待机器证明）

舰队钉住的 `ExsBridge2`：
`IsUFormula p → IsTerm t → Provable 𝗭𝗙𝗖 (imp (iT 0 (substs1 t p)) (^∃ (domZero ^⋏ iT 1 p)))`。

【判断，尚未机器证明】它在 V = ℕ 中为假，反例是 t = `^&0`，p = ⌜x < 0⌝：
- 左边：翻译 `∀y₀y₁((y₀∈ω ∧ y₀=x) ∧ (y₁∈ω ∧ y₁=∅) ∧ ⊤ → y₀∈y₁)`；x 取 ω 时前件不可满足，所以为真。
- 右边：∃y∈ω (y ∈ ∅) 为假。
- 所以这个蕴含在 Universe 中、x = ω 时为假，𝗭𝗙𝗖 证明不了它。

同一个例子也说明，舰队的主定理 `Derivation Sh.craig d → Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))` 在 ℕ 中为假：对 sequent {¬(&0 < 0)} 不成立。原因是翻译时自由变量没有加“∈ ω”的前提。

所需工具（已核对存在）：
- `Provable.sound2`（Proof/Coding.lean:413）：开公式的可证性在 ℕ 中给出 LK2 推导；
- `LK2.Derivation.toProofData` 与 `LK.Derivation.sound f`：给出任意自由变量赋值下的可靠性；
- 命题层的引号引理：`typed_quote_substs`、`typed_quote_fvar`、`free_quote` 等。

要写的：
- `iT_quote` 的命题版：带自由变量的 `iVE`、`iT` 与 `translate` 的编码一致。照 `InternalTranslate.lean` 的证明做，多一个 fvar 情形；
- Universe 中的求值。

## 2. 新架构（待写）

- 完整 Z0 已归结为 `zfc_z0_full_of_D3_internalize`（dev 的 `Z0Full.lean`）。
- 再进一步归结为“经翻译的形式化 Σ1 完全性”：
  `∀ V ⊧ 𝗜𝚺₁, ∀ σ (Σ1 句), V ⊧ σ → Provable 𝗭𝗙𝗖 ⌜σᵗ⌝`。
  由此立得 D3，因为 `zfcTr τ` 是 Σ1 句（`zfcTr_sigma1`）。
- 证法：仿 Foundation 的 `D3.lean` 中 `bold_sigma_one_complete`。
  - 对标准 Σ1 公式做**元层**归纳；
  - 非标准的只有参数，用数字公式 `Num_a`（C-96 的 `numCode`）表示；
  - 需要的内部引理：`Num_a` 的存在、唯一、属于 ω；加、乘、< 在 `Num` 上的计算（对 a、b 做内部归纳）；有界 ∀ 的合并（对界做内部归纳）。
  - 所需的 𝗭𝗙𝗖 定理都是 PA 定理的翻译（C-109 `zfc_proves_PA_theorems`），或是关于 ω 与 succ 的混合句（用完备性加 OmegaArith 的语义引理证明）。
- 不走舰队的“证明翻译”路线，理由有两条：
  - 那条路的 exsIntro 支需要对**非标准公式**做内部归纳，以证明翻译与项代换可证相容，这最难；
  - 它的 hRoot 支在 Sh.craig 上做不了（Sh.craig 的公理集由选择公理挑出的 Σ1 公式定义）。
- 备选：𝗣𝗔⁻ 路线。Foundation 的 Σ1 完全性对 𝗣𝗔⁻ 成立（𝗣𝗔⁻ 有限，可用 `Theory.Δ₁.ofFinite`），再接“𝗣𝗔⁻ 证明的内部翻译”。若要走这条路，正确的归纳不变量是 `Derivable 𝗭𝗙𝗖 (H(d) ∪ translateSeq (fstIdx d))`，其中 `H(d) = {¬(&i ∈ ω) : i < d}`；根部再逐个消去这些前提（对 &0 做 allIntro，再与 𝗭𝗙𝗖 ⊢ ∃x x∈ω 做 cut）。

## 3. 待研究发起人决定

- 反例机器证明之后，要不要通知舰队 Master，让舰队停下 ExsBridge2 与 RootKey？
- main 发布的时机。
