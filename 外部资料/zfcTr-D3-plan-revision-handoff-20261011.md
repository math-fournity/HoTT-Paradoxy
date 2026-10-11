# 对 `zfcTr-D3-plan.md` 的独立修订说明（2026-10-11，本机实编译核验）

> 本说明独立于交接文档 `形式化追踪/09-Codex接手-现状核验与下一步-20261011.md`，
> 直接附在计划 `zfcTr-D3-plan.md` 旁边。结论来自本机 Lean 4.34.0 实编译与 Foundation 源码/GitHub 逐项核对，
> 不是对话摘要。

## 一、计划本身对不对？

**方向对，命题精确，但它不是主线的最小路径；不要照它从头做。**

- 计划 §3 的 `Bridge′` 与 §5 的“经翻译的 Δ₀/Σ₁ 完全性”，数学上**等价于**仓库归约链的最终目标
  （`Provable 𝗭𝗙𝗖 ⌜translate σ⌝` 来自真 Σ₁ 句 σ）。但它绕开、重复了仓库已有的
  `ShCraigElim → bwd → keyE` 机器，自行重证一套翻译版 Σ₁ 完全性（要移植 Foundation `D3.lean` 的 ~1080 行）。
  这是一条**更大的、不与现有收据对接**的路线。
- 仓库的**最小路径**（已大部分具备）是：`iT_neg` 差两量词支 → 补 `iT_setShift`/`iT_substs1`
  → 填 10 支归纳成无 `sorry` 的 `ShCraigElim` → `Z0Blocked.sorry` 改为 `exact bwd_of_shcraig_elim`
  → `Z0Full.zfc_z0_full_of_D3_internalize` 直接给最终定理。无需新路线。
- 计划里“`Sh` 这样的界不存在，否则不可判定”“CraigTrick 不需要 D3 级界”等元层判断**正确**，与第三位 AI 反馈一致。

## 二、对计划中几处具体判断的更正

1. **§7.3 环境描述偏乐观**：计划称“本机 `~/workspace/toolchain-cache/` 已备好 90% 环境”。实际本机工具链在
   `/Volumes/D/HoTT-toolchain-cache/`（Foundation 源 `foundation-src` 314 个 .lean、olean 构建
   `foundation-build-1fb01b72-v4.34.0`），并非 `~/workspace`。路径不为真。
2. **§5.1 L3 量词方向**：计划把有界 `∀x<t` 的归纳写成“在 IΣ₁ 内对 `u ≤ b` 做 Σ₁ 归纳”。这一步在仓库路线里
   **不需要**——仓库走的是 `Sh.craig` 的推导归纳（`induction1`），不是算术 Σ₁ 完全性的内部归纳。
3. **§4 对 `of_provability` 的否定成立**：它确实是语义的（经完备性定理），不产生非标准 V 里的证明编码，
   因此搬不进 `𝗜𝚺₁`。这与仓库 `Z0Blocked`/`Z0Bridge` 的 docstring 一致。

## 三、第三位 AI 的“缺 20 模块”是误判（本机实测）

- 本机 Foundation 源 `/Volumes/D/HoTT-toolchain-cache/foundation-src/` 含 **314 个** `.lean`（commit `1fb01b72`）。
- 它点名的 `D3.lean`、`Syntax/CraigTrick.lean`、`Syntax/Proof/Typed.lean`、`Syntax/Formula/Functions.lean`、
  `Syntax/Formula/Basic.lean`、`Syntax/Proof/Basic.lean` **全部存在**。
- GitHub `raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72de.../<路径>` 逐一 `curl` 实测：
  除一个**路径拼写错**（`R0/Basic.lean` 应为 `SetTheory/R0/Basic.lean`，且本包不用 R0）外，全部 HTTP 200。
- 误判来源：该 AI 所处沙箱无 Lean/Mathlib/Foundation、zip 只含 4 个模块，故只能手推、交不出编译骨架。
  **无需补发“缺失模块”**；要给外部 AI，直接指本地路径或 GitHub raw。

## 四、当前真实缺口（一句话）

主线只差 `ShCraigElim`（把 V 中 `Sh.craig` 推导编码翻译成 `𝗭𝗙𝗖` 推导编码）。
其中 `iT_neg` 的 `all`/`exs` 两量词支尚未编译通过（机械错误，可修），其余 9 支归纳仍待填。
详见 `形式化追踪/09-Codex接手-现状核验与下一步-20261011.md`。
