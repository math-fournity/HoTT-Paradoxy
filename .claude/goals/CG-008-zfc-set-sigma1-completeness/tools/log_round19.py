#!/usr/bin/env python3
"""Append round-19 entries to the master-index shards 003, 005 (goal-local bookkeeping).

Writes only the two shards it owns for this work unit; the shallow payload is
plain text so no quoting hazards.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

E005 = """
### 2026-10-13（CG-008 P3 第十九轮，worktree `dev-ef7e5239`）· round 19 收据化 + 两条收窄合成为**正交**，不是叠加

- **Maker 结果**：`CG008AxStepSplit.lean` 把 `AxStep` 按 Foundation 自己的
  `InductionOnPrenexHierarchy.mem_Δ₁Class_iff`（`Definability.lean:229`）劈成两半，
  **有限半边已证成**（`mem_ofList_ch` / `mem_ofFinite_ch` / `mem_PAMinus_is_standard` /
  `axStep_finite_proved`）；`CG008InductionBody.lean` 把归纳半边的体 `K` 固定为
  `IsPrenexHierarchy 𝚺 1` 公式的码，并付清**标准码**支（`axStep_standard_code`），
  从而把缺口精确到**非标准码**（`axStep_induction_reduces`）。
  `CG008FleetGap.lean` 定下舰队共享形状 C（`MinimalGap`）；`CG008MinimalGapSuffices.lean`
  机器核对 **C 单独对 `hD3G` 是充分的**（回答 002-Step 的质疑）。
- **本轮新增**（`CG008TargetShape.lean`，提交 `b1a19fbb`）：
  - `godel_is_standard`：`gödel`（`Basic.lean:188`）是**元层定义**，故 `⌜𝐆⌝` 是标准码——
    002-Step 的单实例收窄**没有**绕开非标准码那道墙；
  - `z0_of_finalTarget`：`FinalTarget`（= `𝐆` 上那一条 D3 实例）⟹ 完整形式 Z0，经
    单实例定理，**不需整族 `MinimalGap`**；
  - `finalTarget_of_minimalGap`：`MinimalGap ⟹ FinalTarget`，**单向**。
  - **结论：两条收窄正交**——B（002-Step）减少的是「需要多少条 D3」，
    A（本线）减少的是「证一条 D3 需要什么」。合起来不是「靶子 = `𝐆` 的非标准码」
    （`𝐆` 没有非标准码），而是「只需证 `𝐆` 上这一条，而证它时只剩非标准公理码那一支」。
- **收据**：run `2026-10-13-CG001-CG008-AXSTEP-SPLIT-01`，proof_id
  `MP-CG001-GODEL-Q-ZFC-Z0-CG008-014`，claims `CG001-C-143` / `CG001-C-144`；
  97 源（闭包由导入图算出，末个 = `CG008TargetShape.lean`）、553 外部件 pin 校验通过、
  stderr 0 B、exit 0；verifier `verify_cg001_run.py --rerun` **PASS_WITH_SCOPE**，
  `replay = EXACT_EXIT_STDOUT_STDERR_MATCH`，全部定理公理只有 propext、Classical.choice、Quot.sound。
  **工具坑（修好了）**：`make_z0_pins.py` 返回的是 dict（`modules` 是计数、
  `locally_built_files` 单独一项），而 manifest 的 `external_dependencies` 必须是
  `{label,local_path,bytes,sha256}` 行组成的 **list**；capture 脚本原先直接把 dict 塞进去，
  校验器在 `EXTERNAL_DEPENDENCY_ROW_INVALID` 处拒绝。改法照 `capture_z0_run.py:84-100`：
  pinned Lean 文件（label `lean-<rel>`）+ `locally_built_files` 里逐个 `.olean*`
  （label `foundation-build-<path>`）。pins 工具仍跑一次，只作一致性闸门（比 `aggregate_sha256`）。
- **边界（照实）**：`hD3G`、`MinimalGap`（= C）、`AxStep_induction`、`FinalTarget`、单实例
  **均未证**；`Z0Blocked.lean:65` 的未证标记仍在；**完整形式 Z0 未证成，不交付**。
"""

R143 = (
    "| `CG001-C-143` | **`AxStep` 劈成两半，有限半边已证——缺口全在非标准码**。"
    "① **劈法来自 Foundation 自己**：`InductionOnPrenexHierarchy.mem_Δ₁Class_iff`"
    "（`Definability.lean:229`）给出 `p ∈ 𝗜𝚺₁.Δ₁Class ↔ p ∈ 𝗣𝗔⁻.Δ₁Class ∨ "
    "InductionR (IsPrenexHierarchy 𝚺 1) p`。"
    "② **有限半边是定理**（`axStep_finite_proved`）：`𝗣𝗔⁻` 有限（`PeanoMinus.finite`），"
    "其 `Δ₁` 实例经 `Theory.Δ₁.ofFinite`，而 `ofFinite = ofList`（经 `ofEq`）；"
    "`mem_ofList_ch` 用列表归纳把 `ch` 求值成「`p` 等于表中某个 `⌜σ⌝`」——单例侧经 "
    "`singleton_toTDef_ch_val` + `Sentence.quote_eq_encode`（**后者是 `↑(encode σ)` 到 "
    "`⌜σ⌝` 的关键桥**），于是任意模型（含非标准）里「`p` 等于标准码」强制 `p` **就是**"
    "那个标准码（`mem_PAMinus_is_standard`）。"
    "③ **标准码支全部付清**（`axStep_standard_code`）：`p = ⌜σ⌝` 且 `p ∈ 𝗜𝚺₁.Δ₁Class` 时 "
    "`Δ₁Class.mem_iff` 给出 `σ ∈ 𝗜𝚺₁`，`axStep_standard` 收尾。"
    "④ **墙的精确位置**（`axStep_induction_reduces`）：`AxStep_induction` 等价于"
    "「每个归纳实例码要么是标准码要么可证」——实质内容全在非标准码上。"
    "⑤ **体受约束**（`induction_body_is_prenex`）：`K` 必须满足 `IsPrenexHierarchy 𝚺 1`；"
    "**标准体不缺桥**（`standard_body_bridges`）。"
    "⑥ **API 缺口查实**：Foundation 有 `DirectInterpretation`（`LK/Interpretation.lean:404`）"
    "但**没有**形式化的相对可解释性——在 FirstOrder 下 grep Interpretability 无命中；"
    "唯一的「解释保可证性」（`of_provability`）是**元层**的，而降进 V 内要 "
    "`T : ArithmeticTheory`（`provable_internalize`，`D3.lean:175`），`𝗭𝗙𝗖 : SetTheory` 不满足。"
    "⑦ **自我更正**：先前写「V 里没有集合，所以做不了」是**错误诊断**——`Provable 𝗭𝗙𝗖 (iT 0 p)` "
    "是**算术**命题（`Proof` 是 `𝚫ᴬ₁` 公式），不需要 V 有集合结构；正确的读法是"
    "「V 能不能**构造**出那个推导码」 | godel-q-zfc-z0-full |\n"
)

R144 = (
    "| `CG001-C-144` | **两条收窄**正交**，不是「靶子又小一圈」**。"
    "A（本线）= `AxStep_induction` 的墙全在非标准码；B（002-Step）= Z0 只需**一条** D3 实例"
    "（Gödel 句 `𝐆` 上）。**合成核对**（`godel_is_standard`）：`gödel`"
    "（`ProvabilityAbstraction/Basic.lean:188`）是**元层定义**，故 `⌜𝐆⌝` 是**标准**码——"
    "**B 要的那条实例的 `σ` 是标准的**，所以 **B 本身没有触到非标准码**。"
    "**因此两者正交**：B 减少的是「**需要多少条 D3**」，A 减少的是「**证一条 D3 需要什么**」。"
    "合起来是「只需证 `𝐆` 上这一条实例；而证它时只剩非标准公理码那一支」，**不是**"
    "「`𝐆` 的非标准码」（`𝐆` 没有非标准码）。**已机器化**（`CG008TargetShape.lean`，公理洁净）："
    "`z0_of_finalTarget`（`FinalTarget` ⟹ 完整 Z0，经单实例定理，**不需整族 `MinimalGap`**）；"
    "`finalTarget_of_minimalGap`（`MinimalGap ⟹ FinalTarget`，**单向**，反向不成立正是 B 的收窄内容）。"
    "**口径用途**：舰队文档把两条收窄写成「靶子 = `𝐆` 这一句的非标准码 D3 实例」会**过度收紧**"
    " | godel-q-zfc-z0-full |\n"
)


def main() -> None:
    p5 = ROOT / ".claude/总索引/005 - 工作日志.md"
    t5 = p5.read_text(encoding="utf-8")
    p5.write_text(t5 + E005, encoding="utf-8")

    p3 = ROOT / ".claude/总索引/003 - 工作单元与证据登记.md"
    t3 = p3.read_text(encoding="utf-8")
    p3.write_text(t3 + R143 + R144, encoding="utf-8")
    print("003 / 005 updated")


if __name__ == "__main__":
    main()
