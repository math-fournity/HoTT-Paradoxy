# CG001-C-401：Z0 D3 的 `hAll`/`hExs`/`hRoot` 支——**三条 blocker 接口**与语义路线否证

> **证明包**：`MP-CG001-Z0-W8-HALL-BLOCKER-001`。
> **目标包**：CG-007，单元 W8 第 2 层（依据 `.claude/goals/CG-007-formalization-completion/GOAL.md` 完成门 2：
> 「W8 内部化，**或者照实写明阻塞引理**」）。
> **理论变体**：Lean 4.34.0 + Foundation（`1fb01b72`），经典逻辑，
> 内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。
> **最后更新**：2026-10-13（本文件此前版本 §2/§2.5/§3 已全部过时，见 §6 的版本说明）。

## 0. 位置与身份

**身份**：**机器证明（有范围）+ 照实写明的阻塞**。按 GOAL.md 完成门 2 的允许，
本文件给出 `hAll`/`hExs`/`hRoot` 三支的**精确剩余**，并把它固定为**三条命名的 `def`**。

**不声称**：`ShCraigElim` 已完成。**三条 blocker 仍未被证**。

**⚠ 本线 2026-10-13 的实质贡献**：不是证出 blocker，而是
（a）把三支**收敛成可被下游直接 `exact` 的接口**；
（b）**否证**了本线自己提出的「语义路线」。
两件事都是负面/结构性结果，按 GOAL.md「分开报告」的要求，**不冒充为完成**。

## 1. 已机器验证的部分（全部 exit 0，公理只有三条）

### 1.1 ★ 三条 blocker 的**接口**（本线交付物）

`ShCraigElimSetupQ.lean`（399 行，**零未证标记**，exit 0）：

```lean
def AllBlockerQ : Prop :=
  ∀ {s p dd : V}, IsFormulaSet (L := ℒₒᵣ) s → ^∀ p ∈ (s : V) →
    fstIdx dd = insert (free ℒₒᵣ p) (setShift (L := ℒₒᵣ) s) →
    Derivation (V := V) (L := ℒₒᵣ) Sh.craig dd →
    Q (V := V) dd → Q (V := V) (allIntro s p dd)

def ExsBlockerQ : Prop :=
  ∀ {s p t dd : V}, IsFormulaSet (L := ℒₒᵣ) s → ^∃ p ∈ (s : V) →
    IsTerm ℒₒᵣ t →
    fstIdx dd = insert (substs1 ℒₒᵣ t p) s →
    Derivation (V := V) (L := ℒₒᵣ) Sh.craig dd →
    Q (V := V) dd → Q (V := V) (exsIntro s p t dd)

def RootBlockerQ : Prop :=
  ∀ {s p : V}, IsFormulaSet (L := ℒₒᵣ) s → p ∈ s → p ∈ Sh.craig.Δ₁Class →
    Q (V := V) (axm s p)
```

**`induction_setup_Q_of_blockers`** 把三条作为**参数**，**证明完整**——
`ShCraigElim` 因此**精确等价于「三条 blocker 同时成立」**，下游可直接填证明，不必读散文。

**验收台**：`probes/W8-blocker-acceptance-bench-20261013.lean`——
三个 `accept_*` 验收位 + 自检证据（真证明干净 / 占位带 `sorryAx`）。

### 1.2 ⚠ 两条 blocker 曾**过强**，已机器证伪并修复

原 `AllBlockerQ`/`ExsBlockerQ` **丢了 `Derivation Sh.craig dd`**（`hd.2`），
于是假设比原支更弱 ⟹ 义务过强。

**试金石（通用）**：取 `p = ⊤`——`free ⊤ = ⊤`、`substs1 t ⊤ = ⊤`，
`Q dd` 退化成「sequent 里有 `⊤`」，对**任意** `s` 无条件成立。
机器证明（`probes/W8-blockers-TOO-STRONG-20261013.lean`）：
blocker 蕴含 `∀ s, ^∀ ⊤ ∈ s → Derivable (translateSeq s)`——**显然为假**。
（`⊥` 不行：单边 LK 里 `⊥` 在右侧不使 sequent 可导。）

**修复后**同一论证需要额外的 `Derivation Sh.craig (axm (insert ⊤ s) ⊤)`，
而它要求 `⊤ ∈ Sh.craig.Δ₁Class`，不再免费（`W8-blockers-FIX-BLOCKS-20261013`，exit 0）。

### 1.3 `hAll` 的归约——**缺的不是等式，是弱化**

`imp_wk`、`all_m_premise`、`hAll_mem`、`hAll_reduce` 四条（均 exit 0）。

**关键更正**：此前三轮把 `hAll` 卡点记成「需要
`iT 0 (free ℒₒᵣ p) = free ℒₛₑₜ (imp domZero (iT 1 p))` 这条等式」。
**那条等式确实为假，但 `hAll` 从来不需要它**——
`free_imp_domZero` 已把 `domZero` 层剥离到一次 ∨ 弱化里。

### 1.4 `hRoot` 的归约——**不需要 `Δ₁Class`**

`derivable_of_mem_of_provable` + `hRoot_core`（exit 0）：
`p ∈ s` 且 `iT 0 p` 内部可证 ⟹ `translateSeq s` 可导。
剩余义务降为 `p ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT 0 p)`。

**一步归约已证**（`W8-blocker-acceptance-bench` 的 `accept_root_via_reduction`）：
`RootBlocker` 与该命题之间只差这一条 `h`。

**依赖链已查清**（`Theory.craig T = {φ | ∃ σ s, Evalb ![s, ⌜σ⌝] ↑T.reWitness ∧ φ = padding σ s}`）：
`p ∈ Sh.craig.Δ₁Class` **天然**给出 `∃ σ s, Evalb … ↑Sh.reWitness ∧ …`——
`reWitness` 是**定义里就有的**（V 层现成件），不是 ℕ→V 搬运。
但**仍需 V 内的构造能力**（从「见证存在」到「V 内造出证明码」）——
即 002 线的「四墙精确交点 = 在 V 内证明 ω 归纳」。

### 1.5 基建（`TranslateShiftCompat.lean`，全部 exit 0）

`termSubstVec_congr'`、`termSubst_congr'`、`subst_congr_prefix'`（**语言多态**）、
`substs_qqAlls`、`qVec_two`、`substs_qqAlls_two`、`iVE_resultVec_two`、
`subst_qVec_domZero'`、`len_qVec`、`subst_qVec_shrink`。

### 1.6 四条语言无关性（**边界严格**）

`termBShift`/`termSubst` 在 `bvar`/`fvar` 上跨 `ℒₒᵣ`/`ℒₛₑₜ` 一致——
**但这仅覆盖这些构造子**。`^func` 上**不一致**（§3.4），**不能外推**。

## 2. 精确剩余（三条，均为**阻塞**）

| 支 | 义务 | 性质 |
|---|---|---|
| `hAll` | `AllBlockerQ` ← `AllKey` ← **桥 B**（§2.2：链已闭合） |
| `hExs` | `ExsBlockerQ` ← `ExsBridge2` **一条**（§2.1） |
| `hRoot` | `RootBlockerQ` ← `RootKey`（= D3 本身，§1.4） |

**三条的形状已统一**：各一条 `Provable` 层陈述，
三条归约定理（`allBlockerQ_of_key`/`exsBlockerQ_of_bridge2`/`rootBlockerQ_of_key`）
**全部 exit 0、公理三条、无 `sorryAx`**，均在生产包 `ShCraigElimSetupQ.lean` 内。

### 2.1 ★ `hExs` 的精确剩余：`ExsBridge2`（**唯一一条**）

**旧形状 `ExsBridge`（`∀ T'` 量化）为假**：取 `T' = ^&0`，需要 `⊢ ∀x (x ∈ ω)`——
而带自由变量的 `Provable φ` 在 LK 里等价于 `⊢ ∀x φ`。反例 `p = #0 = #0`、`t = ^&0`。
**故「归约到 `ExsBridge`」是空洞的（前提不可满足），不是进展。**

**正确形状**（`W8-ExsBridge2-corrected-20261013.lean`）：

```
ExsBridge2 : ∀ {p t}, IsUFormula ℒₒᵣ p → IsTerm ℒₒᵣ t →
    Provable 𝗭𝗙𝗖 (imp ℒₛₑₜ (iT 0 (substs1 ℒₒᵣ t p)) (^∃ (domZero ⋏ iT 1 p)))
```

即「`p[t] → ∃x∈ω p(x)`」——**语义为真**（t 的值就是见证），且与 sequent 里的 ∃ 公式**同形**。

**归约已完整**（`exsBlockerQ_of_bridge2`，exit 0、公理干净）：
桥给 `¬A ⋎ ∃` → `split_or` 拆成 `{¬A, ∃}` → `wk` 得 `Derivable (insert (¬A) S)`
（**`∃ ∈ S` 是关键**）→ `cut A`。

### 2.2 ★ `hAll` 的链**已闭合**：桥 B ⟹ `AllKey` ⟹ `AllBlockerQ`（2026-10-14）

`allKey_of_bridge`（生产包，exit 0、公理三条）：层 1 的桥 `B` 推出 `AllKey`。

```
iT 0 (free ℒₒᵣ p) = subst ?[^&0] (iT 1 (shift ℒₒᵣ p))    -- 桥 B(q := shift ℒₒᵣ p)
                  = subst ?[^&0] (shift ℒₛₑₜ (iT 1 p))    -- iT_shift（已证）
                  = free ℒₛₑₜ (iT 1 p)                    -- free 的定义
```
再 `imp A A` 永真收尾。`AllKey` 只要**蕴含**，故等式一成立即可得。

**桥 `B` 正是 003 线的 `iT_substs1'`**（层 1 版）：
`subst ?[^&0] (iT 1 q) = iT 0 (subst ?[^&0] q)`。

⟹ **桥 B → AllKey → AllBlockerQ → ShCraigElim**：`hAll` 的链闭合，桥一通即得。

**⚠ 更正一处旧记录**（本文件 v4 及更早）：曾把 `hAll` 剩余记成
`iT 0 (free p) = free (iT 1 p)` 并说「该等式已机器证伪」。
**准确说法**：不带桥的**朴素版本**被证伪（`domZero` 计数不同）；
**带桥的版本恰恰成立**（即 `allKey_of_bridge` 里的 `heq`）。
旧措辞会让下游误以为这条路已死——**本版改回来**。

## 3. 为什么 `hAll` 难——三条**机器确认的**结构性障碍

### 3.1 向量长度的三种含义混淆

`subst` 的向量长度由**公式层数**定；`termSubstVec` 按**关系元数**走；
`iT` 的 `all` 支又把层数**推一格**。三者不同步 ⟹ 越界补零。
（`W8-subst-arity-zerofill-PROVED-20261013`：
`subst ?[^&0] (^rel 2 cEqN ?[^#1,^#0]) = ^rel 2 cEqN ?[0, ^&0]`。）

### 3.2 归纳谓词的偏移

`semiformula_result_induction` 的 `q` 被固定成 `result … param p`，
而目标要 `iT (param+1) p`。候选 1 的谓词**已被 Lean 接受**，
`verum`/`falsum`/`and`/`or` 四支已证。

**`IsSemiformula.induction` / `Semiformula.induction` 不存在**——
`Formula/Basic.lean:466–528` 是**整块注释掉的**（`#check` 报 unknown constant）。
可用的是 `sigma1_structural_induction`（`:1484`）与 `pi1_structural_induction`（`:1516`）。

### 3.3 `iT` 与 `subst` 在 `∀` 上**错开一格**

`σ = ^∀ X`（层 1）时两侧展开：第一分量由 `subst_qVec_domZero'` 对上（exit 0）；
第二分量 `iT 1 (subst (qVec ?[^&0]) X)` vs `subst (qVec ?[^&0]) (iT 2 X)`——**层数错开一格**。

### 3.4 ★ `termBShift`/`subst` **不跨语言**（源码级）

**决定性证据**（`Term/Basic.lean:321`，`TermRec.result` 的 graph）：

```
"y t. (!(isUTerm L).pi t → !(β.graph L) t y ⋯) ∧ (¬!(isUTerm L).sigma t → y = 0)"
```

`result L` **依赖 `IsUTerm L`**。故对 `ℒₒᵣ` 的函数符号码（如 `+`）：
`termBShift ℒₛₑₜ (^func 2 addIndex v)` 走 `y = 0` 支，`termBShift ℒₒᵣ` 正常计算。
**⟹ `qVec ℒₒᵣ w ≠ qVec ℒₛₑₜ w`（一般 `w`）**，`subst ℒₛₑₜ` 不能直接吃 `ℒₒᵣ` 的项向量。

**⚠ 测跨语言性质必须测 `^func`**——那正是 `IsUTerm L` 分叉的地方。
本线曾用两语言共有的构造子（`^#0`/`^&0`）上的成功推断「全部构造子」，**错**。

## 4. ★★ 语义路线的**否证**（本线提出，本线否证）

### 4.1 路线的动机与形状

`ExsBridge2` 的数学内核是**一阶逻辑重言式**，故本线 2026-10-13 提出：
不经语法桥（`iT_substs1`），改走**语义**——
用 `SetTheory.complete`（模型侧）把 `Provable 𝗭𝗙𝗖 φ` 化归为「在每个 𝗭𝗙𝗖 模型里成立」。

**动机（重要）**：提这条路的理由是**绕开语法等式桥**，不是认为语义更优雅。
**这个动机现在作废了**——绕开的代价是撞上一条假的枢纽。

### 4.2 否证（三条机器核验 + 一条结构性论证）

**枢纽**：整条路线压在一条反向引理上——

```
IsSemiformula L n p → ∃ F : Semiproposition L n, p = ⌜F⌝
```

Foundation 只有**正向**（`quote_isSemiformula`），反向不存在。

| 判定 | 结果 |
|---|---|
| 动机的 `definability`（`Semiproposition` 版） | **失败**（`aesop failed`） |
| 同上（`Sentence` 版，ξ = Empty） | **失败** |
| **命题真值** | **为假** |

**为假的三条源码事实**：

1. `IsSemiformula` 是 **Fixpoint**（`Formula/Basic.lean:284`）；
2. `limSeq` 的迭代指标是 **`V` 不是 `ℕ`**（`HFS/Fixpoint.lean:131`：
   `def limSeq (s : V) : V := c.prConstruction.result v s`）
   ⟹ 非标准模型里 `IsSemiformula` 含**非标准层高**的公式码；
3. `⌜F⌝`（`F` 是 Lean 对象）**永远是标准码**（有限多个构造子搭成）。

⟹ 取非标准模型中的非标准公式码 `p`：`IsSemiformula` 成立但**不存在** Lean `F` 使 `p = ⌜F⌝`。

**旁证（决定性）**：Foundation 的 `IsSemiformula.sound`（`Formula/Coding.lean:478`）
**载体是 `ℕ`**——`ℕ` 上没有非标准元，故 ℕ 层为真、V 层为假。
**这不是「搬不过来」，是真值不同**；也解释了「V 层没有 `Nat.strongRec`」不是缺工具。

**另有类型障碍**（即使想证也写不出）：归纳原理的动机是 `P : V → V → Prop`，
**第一分量 `n : V`**；而 `Semiproposition L k` 要 **`k : ℕ`**。
故「`p` 是某层 `n` 公式的引号」**在类型上就写不成 `P n p`**。

### 4.3 ⚠ 对「卡点不存在」的更正

`W8-quote-is-code-20261013.lean` 曾写「**卡点不存在**」「组装障碍解除」——**过强**。
它实际只核了：

* ✅ **引号与构造子交换**（`rfl`）：`⌜φ ⋏ ψ⌝ = ⌜φ⌝ ^⋏ ⌜ψ⌝`、`⌜⊤⌝ = ^⊤`；
* ❌ **未核**：`IsSemiformula` 的每个元素**都是**引号的**满射性**。

前者是「引号是好的」，后者是「码都能倒回引号」——**两件事**。
要喂给 `tprovable_tquote_iff_provable_quote_sentence` 的**正是后者**。

### 4.4 本线试过并**否掉**的四个入口（都机器核过）

| 入口 | 状态 |
|---|---|
| `Provable.sound` | ❌ **硬接线宇宙 0**（`Provable.{0,0}`），任意 V 不可用 |
| `provable_iff_provable` | ❌ 载体 ℕ |
| `tprovable_tquote_iff_provable_quote_sentence` | ⚠ 多态 ✅ **但要求 `⌜σ⌝` 形** |
| `SetTheory.complete` | ⚠ 多态 ✅ **但要求类型化 `SetTheorySentence`** |

**两端都要求「V 层码 = 某个 Lean 对象的引号」**——这就是这条路**死**的原因，不是慢。

### 4.5 交叉印证

002-Flash 把 C 靶心窄到「**非标准码**」一条——与本节的**同一堵墙**：
非标准公式码既是 C 的障碍，也是语义路线枢纽的**反例来源**。

### 4.6 `ExsBridge2` **不受**此否证影响

`ExsBridge2` 的陈述是 `Provable (iT 0 (p[t]) → ^∃ (domZero ⋏ iT 1 p))`——
**不要求 `p` 是引号形**，故非标准码反例不适用。
**它的剩余是纯语法工作**（`W8-ExsBridge2-corrected` 的归约已完整）。

## 5. 未完成的部分（照实写）

* `AllBlockerQ`：未证（§3.4 的语言错配是真障碍）；
* `ExsBlockerQ`：未证，但**已归约到 `ExsBridge2` 一条**（§2.1）；
* `RootBlockerQ`：未证，**已归约到 D3**（§1.4）；
* `iT_substs1` 的 `rel`/`nrel`/`all`/`exs` 支：未证；
* 语义路线：**已否证**（§4），不再作为候选。

## 6. 收据位置

* 生产包：`GodelQ/ZFC/ShCraigElimSetupQ.lean`（399 行，零未证标记，exit 0）、
  `GodelQ/ZFC/TranslateShiftCompat.lean`（exit 0）；
* 验收台：`probes/W8-blocker-acceptance-bench-20261013.lean`；
* 否证探针：`probes/W8-hub-quote-motive-NOT-definable-20261013.lean`、
  `probes/W8-hub-quote-FALSE-nonstandard-20261013.lean`；
* 过强修复：`probes/W8-blockers-TOO-STRONG-20261013.lean`、`W8-blockers-FIX-BLOCKS-20261013.lean`；
* 探针总目录：`.claude/goals/CG-007-formalization-completion/probes/`（290+ 份）；
* 构建：`python3 -B .claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py <pkg> <module>`。

## 7. 版本说明（本文件自身的历史）

* **v1**（`hAll` 阻塞版）：§2 的 `iT_substs1` 形状（右端用 `w`）**不完整**，已被 §2.5 取代。
* **v2**（`qVec (iVE-像 w)` 版）：方向**正确**（源码级确认，§3.4），但当时把三支记为 `sorry`。
* **v3**（三条 blocker `def` 版）：三支改成**命名接口**，`induction_setup_Q_of_blockers` 证明完整。
* **v4**（本版）：补 §1.2 过强修复、§2.1 `ExsBridge2` 归约、§4 语义路线否证。
  **撤回 v1/v2/v3 中「等式路线」「语义路线可行」两处判断。**
