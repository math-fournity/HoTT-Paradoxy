# godel-q-zfc-z0-sigma1：工作计划（012-Opus，2026-10-14）

> **完成状态（2026-10-14 晚）**：§2b 的主路线全部做完并取得收据。
> - 收据：`20261014-CG001-GODEL-Q-ZFC-Z0-SIGMA1-01`，PASS_WITH_SCOPE，精确重放；负控制 `-NEG-BALL-01`，按预期被拒绝。
> - 命题：CG001-C-413–C-417，见 `CLAIM.md`。
> - 结果：`zfc_z0_unconditional : 𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ`，不带未证前提。
> - 文件：`TransTyped`、`TransTerm`、`TransBall`、`TransSigma1`、`Z0D3`。§2b 原计划的 `SetIntFacts.lean` 没有单独建，标准句分散在各文件里。
> - 下面保留施工时的原文。

> 本包在独立 worktree `/Volumes/D/HoTT-worktrees/012-opus-w8`（分支 `claude/012-opus-w8`，取自 dev `c491326e`）。
> 现状：复制了依赖链（23 个模块，与 `godel-q-zfc-z0-translate` 逐字节相同，已核对）与 `dev` 的 `Z0Full.lean`，生成了固定记录（导入闭包 1,893 个模块，聚合 `02b0e80f…5161`）。依赖链加 `Z0Full.lean` 在本 worktree 编译通过（24 个模块全部 exit 0，`Z0Full` 的 8 条公理报告全为三条标准公理）。另有 `OpenTranslate.lean`（带自由变量的翻译正确性，C-410；与 `../godel-q-zfc-z0-freevar/` 中的同名文件逐字节相同，收据在那里），留作 D3 的部件。
> 编译：`devbuild_ns.py`（`.claude/goals/CG-007-formalization-completion/tools/`），依赖链清单在本会话 scratchpad 的 `s1_chain.txt`。多参数命令用 bash（zsh 不分词）。

## 1. 反例（✅ 已机器证明：`../godel-q-zfc-z0-freevar/`，CG001-C-410–C-412，2026-10-14）

舰队钉住的 `ExsBridge2`：
`IsUFormula p → IsTerm t → Provable 𝗭𝗙𝗖 (imp (iT 0 (substs1 t p)) (^∃ (domZero ^⋏ iT 1 p)))`。

【证明，C-411】它在 V = ℕ 中为假，反例是 t = `^&0`，p = ⌜x < 0⌝：
- 左边：翻译 `∀y₀y₁((y₀∈ω ∧ y₀=x) ∧ (y₁∈ω ∧ y₁=∅) ∧ ⊤ → y₀∈y₁)`；x 取 ω 时前件不可满足，所以为真。
- 右边：∃y∈ω (y ∈ ∅) 为假。
- 所以这个蕴含在 Universe 中、x = ω 时为假，𝗭𝗙𝗖 证明不了它。

同一个现象也说明，舰队的归纳不变量 `Derivation Sh.craig d → Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))` 在 ℕ 中为假【证明，C-412】：两步纯逻辑推导 `dCounter`（结论 `{∃x (x<0), ¬(&0<0)}`，∃ 引入以 &0 为见证）就让它失败。原因是翻译时自由变量没有加“∈ ω”的前提。（早先这里写的是 sequent `{¬(&0<0)}`；它要用理论公理才可导，机器证明改用了不需要公理的 `dCounter`。）

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

## 2b. 主路线的施工设计（2026-10-14 定稿，按此施工）

**目标**：对每个 V ⊧ 𝗜𝚺₁ 与每个 Σ1 算术句 σ（`ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1`），`V ⊧ σ → 𝗭𝗙𝗖.internalize V ⊢ ⌜σᵗ⌝`。取 σ := `zfcTr τ`（`zfcTr_sigma1`），由 `models_zfcTr_iff` 即得 `zfc_z0_full_of_D3_internalize` 的前提，于是 `𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ` 不带前提。

**归纳**：照 Foundation `D3.lean` 的 `bold_sigma_one_complete`，用 `Bounding.Hierarchy.arithmetic_sigma₁_induction'`（情形：⊤、⊥、=、≠、<、≮、⋏、⋎、有界 ∀、∃）。
- 集合语言没有函数符号，数不能用项命名。参数 w : Fin n → V 改用**自由变量加假设**：把 σ 的约束变量 #i 换成自由变量 &i，上下文 Γ(w) = [N_{w_0}(&0), …, N_{w_{n−1}}(&(n−1))]（FiniteContext），断言 `Γ(w) ⊢[Z] ⌜σᵗ⌝.subst (&·)`。进量词时 Γ(a ∷ w) = N_a(&0) ∷ Γ(w).map shift，与 Foundation 的 `free`/`generalize!` 约定一致。
- N_a := `numF a`：Rayo 式数字公式（`NumeralCode.lean` 的 `numCode` 的有型版本），N_0(z) = ∀u(u ∉ z)，N_{a+1}(z) = ∃y(N_a(y) ∧ Succ(z, y))。

**内部引理（Z := 𝗭𝗙𝗖.internalize V；* = 在 V 中归纳）**
1. `numF` 合式（IsSemiformula 1）*，无自由变量*。
2. N 的引入与消去（展开定义，不归纳）；N 对等号的相合（分 a = 0 与 a = c + 1，不归纳）。
3. 存在* `Z ⊢ ∃x N_a(x)`；属于 ω* `Z ⊢ ∀x(N_a(x) → x ∈ ω)`；唯一* `Z ⊢ ∀x y(N_a(x) → N_a(y) → x = y)`。
4. 加法* `Z ⊢ ∀x y z(N_a(x) → N_b(y) → Add(z,x,y) → N_{a+b}(z))`（对 b 归纳）；乘法*（对 b 归纳，用加法）。
5. 小于*：a < b 时 `N_a(x) → N_b(y) → x ∈ y`（对 b − a − 1 归纳）；不小于、不等：由小于、唯一与 ω 上 ∈ 的标准事实。
6. 有界 ∀ 的合并*：若对每个 i < b 有 `Z ⊢ ∀x(N_i(x) → Φ(x))`，则 `Z ⊢ ∀x z(N_b(z) → x ∈ z → Φ(x))`（对 c ≤ b 归纳）。
7. 项引理（对标准项作元层归纳）：存在 `Γ(w) ⊢ ∃z(z ∈ ω ∧ VE_t(z; &·))`，刻画 `Γ(w) ⊢ ∀z(VE_t(z; &·) → N_{t(w)}(z))`。
- 一切“一致的”事实（关于 ω、Succ、Add、Mul、等号相合、定义域）都是标准 𝗭𝗙𝗖 句：用 `SetTheory.complete` 在模型里证（`OmegaArith`、`ArithInterp` 的语义引理），再用 `internal_provable_of_outer_provable` 搬进 V，用 `TProof.specialize` 在自由变量处实例化。只有含 N_a 的部分需要 V 中归纳（归纳谓词“Z ⊢ 码(a)”是 Σ1 的）。

**文件**：`IntLogic.lean`（内部逻辑小工具：∃ 消去、空量词）→ `SetIntFacts.lean`（有型的 ∈、=、ω、Succ、Add、Mul 与标准句）→ `SetNum.lean`（1–3）→ `SetNumArith.lean`（4–6）→ `TransTyped.lean`（翻译的有型引号）→ `TransTerm.lean`（7）→ `TransSigma1.lean`（归纳）→ `Z0D3.lean`（D3 与完整 Z0）。

**为什么不走证明翻译**：见 `../godel-q-zfc-z0-freevar/`（C-410–C-412）：舰队的不变量在 ℕ 中就假；改成带自由变量 ω 前提的不变量也要对非标准公式做内部归纳。本路线只对标准公式作元层归纳，非标准的只有数字。

## 3. 待研究发起人决定

- 反例机器证明之后，要不要通知舰队 Master，让舰队停下 ExsBridge2 与 RootKey？
- main 发布的时机。
