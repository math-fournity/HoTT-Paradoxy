# CG001-C-391：Z0 D3 攻坚第 2 层的地基——公式保持性（`iVE`/`iTR`/`iT`）

> **证明包**：`MP-CG001-Z0-W8-LAYER2-ISEMIFORMULA-IT-001`。
> **目标包**：CG-007，单元 W8 第 2 层（依据 `.claude/goals/CG-007-formalization-completion/W8-下一单元-V内部语法解释定理-规格.md` §9.3–§10.1 与 `W8-第二层进展-公式保持性地基.md`）。
> **理论变体**：同 `godel-q-zfc-z0-full`：Lean 4.34.0 + Mathlib（`5ed29652`）+ Foundation（`1fb01b72`），经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。

## 0. 位置与身份

**身份**：机器证明（有范围）。这是 ← 方向（V 内部的语法解释定理）第 2 层「10 个 case 组装」的**公共地基**。
`Derivation.*` 的每个构造子都要求 `IsFormulaSet`，所以「翻译把公式码送到公式码」必须先有。
本文件给出这一整块地基，并**不**做 10 个 case 的组装。

它承接的是 §38 之后的第二层拆解（9 条已证引理：`isSemiformula_cRel`、`_cDomN`、`_cFunc_*`、
`isSemitermVec_shiftVec(_V)`、`_single_bvar`、`isSemiformula_conjunct`、`shiftVec_definable(')`），
把当时清单里剩下的 #1–#5 全部证完。

## 1. 精确命题（类型逐字见 `GodelQ/ZFC/SeqTranslateFormula.lean`）

| 名字 | 命题 |
|---|---|
| `iVE_bvar` | `iVE n (^#z) = eqAtom (^#(z + 1))` |
| `iVE_fvar` | `iVE n (^&x) = eqAtom (^&x)` |
| `iVE_func` | `iVE n (^func k f v) = (if k = 0 then ve0 k f else ve2 n k f (iVE.construction.resultVec ℒₒᵣ ![n] k v))`（对 `IsFunc k f`、`IsUTermVec k v`） |
| `isSemiformula_iVE` | `IsSemiterm ℒₒᵣ n t → IsSemiformula ℒₛₑₜ (n + 1) (iVE n t)` |
| `isSemiformula_domZero` | `IsSemiformula ℒₛₑₜ (n + 1) domZero` |
| `isSemiformula_iTR` | `IsRel k R → IsSemitermVec ℒₒᵣ k n v → IsSemiformula ℒₛₑₜ n (iTR n k R v)` |
| **`isSemiformula_iT`** | `IsSemiformula ℒₒᵣ n p → IsSemiformula ℒₛₑₜ n (iT n p)` |

以上全部在 `{V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]` 的**任意**模型 V 中成立。

## 2. 证明

### 2.1 `iVE` 的三条计算规则

`iVE.construction` 的 fixpoint 语义给出三条化简；`iVE` 本身是 `construction.result`，
`result_bvar`/`result_fvar`/`result_func'`（`Term/Basic.lean:562/565/630`）把它们抠出来。**此前无人做过**。

### 2.2 `isSemiformula_iVE`：项侧没有带层数的 TermRec 归纳

正确工具是 `IsSemiterm.sigma1_induction`（`Term/Basic.lean:936`），层数 `n` 固定。
三支 `bvar`/`fvar`/`func`；`func` 支再按 `k = 0` 分 `ve0`（层 1 常数公式，`isSemiformula_mono` 提升到 `n+1`）
与 `ve2`（层 `n+1`）。`ve2` 体内 `conjunct 3 n i _` 出现在 `qqAlls … 2` 的体内，层数 `n+3`，
两条 `isSemiformula_conjunct` 的边界义务 `i < 3 + n` 由 `lt_add_self_add_one` + `ring` 支付
（`omega` 在 V 上不工作）。

`definability` 义务需要 `iVE` 的**层级实例**（照 `shiftVec` 的先例）：
`instance iVE_definable' (Γ m) : Γᴬ_[m + 1]-Function₂[V] iVE`。

### 2.3 `isSemiformula_domZero` / `isSemiformula_iTR`

`domZero = subst ?[^#0] cDomN`，用 `IsSemiformula.subst` + `isSemitermVec_single_bvar`。

`iTR n k R v = qqAlls (imp (conjunct 2 n 0 (iVE n v.[0]) ⋏ (conjunct 2 n 1 (iVE n v.[1]) ⋏ ⊤))
  (subst ?[^#0,^#1] (cRel R))) 2`。
算术语言只有等号与小于两个 2 元关系符号（`isRel_iff_LOR`），所以 `k = 2`；
体内层数 `n + 2`，两条 `conjunct 2 n i _` 用 2.2 的 `isSemiformula_iVE` 与 `cRel`。

### 2.4 主定理 `isSemiformula_iT`：护罩

`semiformula_result_induction`（`Formula/Basic.lean:1578`）把**输出层 `param`** 与**输入层 `n`**
独立量化，结论形如 `∀ {param n p}, IsSemiformula L n p → P param n p (c.result L param p)`。
而 `iT` 改层：`iTR param …` 要求 `v` 在层 `param`，`hRel` 只给层 `n`。`param ≠ n` 时证不出来。

归纳谓词取护罩：`P param n p q := param = n → IsSemiformula ℒₛₑₜ param q`。
结论实例化 `param := n` 即得目标；`hRel` 支由 `param = n` 把 `v` 的层搬过去；
`hall`/`hexs` 支的递归是 `P (param+1) (n+1) …`，护罩自动保持。
`result_all`/`result_exs`（`Formula/Basic.lean:1142/1147`）把外层量词的结果向量写出来，
用 `nth_adjoin_zero` 取第 0 项。（对照：Foundation 自己的 `semiformula_subst_induction`
不需要护罩，因为 `subst` 不改层。）

## 3. 负控制

`GodelQ/ZFC/WrongIVELayer.lean`：把 `iVE` 的 bvar 规则错写成"层数不加一"，
即断言 `iVE 0 ^#0 = eqAtom ^#0`。内核拒绝：`iVE_bvar` 给出 `eqAtom ^#(0+1)`，
目标 `eqAtom ^#(0+1) = eqAtom ^#0` 不可解。
运行 `20261011-CG001-Z0-W8-LAYER2-ISEMIFORMULA-IT-NEG-02`（判据运行；
`-NEG-01` 是驱动修正期，源清单漏文件，保留不淘汰）。

## 4. 还差什么（诚实边界）

**本包不证 `derivable_translateSeq`。** 第 2 层的 10 个 case 组装（`Derivation.induction1`）
仍未做。以下全部未证：

1. `iT` 与 `substs1`/`shift`/`free`/`setShift` 的相容（de Bruijn 结构改变，不是平凡交换）；
2. `axm` 支所需的 `codeOfREPred` 一般 V 表示引理；
3. `derivable_translateSeq`（10 个 case）；
4. `bridge` / `keyE` 的 ← / `zfcTr_D3_internalize`。

因此 Z0 完整形式仍以 `zfcTr_D3_internalize` 为显式前提；C-120 的影子形式不受影响。

## 5. 文件

- `GodelQ/ZFC/SeqTranslateFormula.lean`（本包扩展；原有的 9 引理 + 2 实例保留）；
- `GodelQ/ZFC/WrongIVELayer.lean`（负控制）。

## 6. 运行

- `HoTT/verification/runs/20261011-CG001-Z0-W8-LAYER2-ISEMIFORMULA-IT-01/`：
  25 个依赖模块 + `SeqTranslateFormula.lean`，exit 0，stderr 0 B，
  `#print axioms` 全为三条标准公理，`--rerun` `EXACT_EXIT_STDOUT_STDERR_MATCH`。
- `...-NEG-02/`：加 `WrongIVELayer.lean`，exit 1，内核在错误目标处拒绝，
  `--rerun --expect-rejected` `EXACT_EXIT_STDOUT_STDERR_MATCH`。
- 索引：CG-001 证据索引 §41。

## 7. 禁止外推

1. 不读成 D3 已证或部分证；不读成第 2 层已完成。
2. 不读成 `keyE` 任一方向已证。
3. 不推出 `𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)`；C-120 的影子形式仍是唯一无条件成立的结论。
4. `isSemiformula_iT` 是**元层**定理（对每个公式码与每个模型 V），不是 V 内部对"所有公式"的一句断言。
