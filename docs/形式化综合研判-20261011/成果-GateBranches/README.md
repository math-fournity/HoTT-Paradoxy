# 成果：GateBranches（gateG 的完整十支 + 条件组装）

> 2026-10-11，CG-009。文件 `GateBranches.lean`，sha256 `ea59e285…`。
> 本会话 pinned Lean 4.34.0 + Foundation `1fb01b72` 编译 **exit 0**；
> 全部 12 条声明（10 支 + 2 谓词 + 2 组装）`#print axioms` 均仅 `[propext, Classical.choice, Quot.sound]`。

## 这是什么

`gateG-证明义务清单.md` 的 O2 义务（10 条推导规则）**全部十支** + 两条组装定理，
写成**完全独立于 canonical 失败文件**的自足文件。

### 十支（4 无条件 + 6 条件）

| 定理 | 性质 | 条件（若有） |
|---|---|---|
| `hAnd`、`hOr`、`hWk`、`hVerumIntro` | **无条件** | — |
| `hAxL`、`hCut` | 条件 | 一般码 `iT_neg` |
| `hShift` | 条件 | `translateSeq`/`setShift` 交换 |
| `hAll`、`hExs` | 条件 | 量词规则翻译保持 |
| `hAxm` | 条件 | **O3 证书桥**：`∀p ∈ Sh.craig.Δ₁Class, Provable ZFC (iT 0 p)` |

### 组装（两条，均过核）

| 定理 | 内容 |
|---|---|
| `shCraigElim_of_obligations` | **五条义务 ⇒ 条件版 ShCraigElim**（对 V 内任意 Sh.craig 推导，经 `Derivation.induction1` 十支全接；`Q` 的 Σ1 谓词实例在文件内给出 `q_defined`） |
| `elim_at_godel_of_obligations` | **五条义务 ⇒ 单句消去 elim@G**（结论句固定为 `⌜zfcTr G⌝`，推导 d 仍任意） |

## 意义

- 这把"gateG 还差什么"从散文变成了**五条精确的 Lean 义务**：
  ```
  iT_neg : ∀ n p, IsSemiformula ℒₒᵣ n p → iT n (neg p) = neg (iT n p)
  tshift : translateSeq (setShift s) = setShift (translateSeq s)
  hall   : 全称规则翻译保持
  hexs   : 存在规则翻译保持（iVE 输出是公式不是项——最难的一条）
  axmBridge : ∀p ∈ Sh.craig.Δ₁Class, Provable ZFC (iT 0 p)   -- O3 证书桥
  ```
- **五条全部是独立可攻的小命题**，且前四条与全称 `ShCraigElim` 的缺口完全同源——
  在单句门上解决一次，全称版直接复用。
- 与 `Z0LocalGate.lean` 串联即得：**五条义务 ⇒ 最终 Z0 完整形式**
  （`elim_at_godel_of_obligations` ⇒ `local_D3_of_elim_at_godel` ⇒ `zfc_z0_full_of_local_D3`）。

## 五条义务的攻打优先级（本会话判断）

1. **`iT_neg`**（最接近）：canonical 活跃战线正在攻；本会话已给病灶定位
   （`exs` 支的 `exsChanges` 对齐 + `or` 支心跳，见增量扫描日志第 6–9 轮）。
2. **`tshift`**：可能比预想易——`setShift` 与 `translateSeq` 都经 `sigma₁_replacement` 构造，
   或可经 `mem_ext` + 成员级论证直接得（未试）。
3. **`hall`**：需要 `free`/`setShift` 与 `iT` 的相容 + `Derivable.all_m`；中等。
4. **`axmBridge`**（O3）：最难——`reCh` 的选择代码只在 ℕ 有规格；
   候选：显式带证书的 Craig 公理化、或对 G 的 Craig 公理做更窄的表示引理。
5. **`hexs`**：结构上最难（`iVE` 输出是值关系公式，项代入跨层）。

## 边界

- 全部为**条件**定理：五条义务是假设，不是已证。**不得读成 ShCraigElim/Z0 已完成**。
- 文件可整体复制进正式包（新文件、不改既有）；依赖 `Z0Full`、`SeqTranslate`、
  `SeqTranslateFormula`、`InternalTranslate`（均已过核）。
- 组装定理的证明已过核；结论的条件性全部来自五条前提。
