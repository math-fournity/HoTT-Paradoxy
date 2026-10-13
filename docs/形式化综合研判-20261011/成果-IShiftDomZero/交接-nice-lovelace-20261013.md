# CG-009 nice-lovelace 会话交接（2026-10-13）

> 会话 `claude/nice-lovelace-ab1147`，工作树
> `/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/nice-lovelace-ab1147`。
> 本文件写给接手者：**不是成果清单**（成果在 git），而是**未写下的诊断、走过的弯路、别人可能重蹈的坑**。

## 0. 权威状态（截至本会话末）

- 核验脚本：`verify-openhb.sh`，**35 文件、clean 35/35 (FAIL 0, SORRY 0)**
  （判据 = exit code + `error:` + `sorry|sorryAx`，见 §4 教训）
- 本会话主产出：`ITSubstOpen6.lean`（**(★★) subst_iVE_open**）、
  `ITSubstOpen7.lean`（`subst_QvecV_cRel` + `VRel_rel`）
- 提交：`e4e1bc92`（★★）、`1e5a9843`（cRel）、`92b7beb9`（判据修复）、
  `9b52bb5a`（VRel_rel）、`4b9b9668`（src 强制入 git）

## 1. (★★) 的精确形状与它的两个"必须先知道"

**陈述**（`ITSubstOpen6.subst_iVE_open`）：
```
∀ m t, IsSemiterm ℒₒᵣ (m+1) t →
∀ Vw Ww, IsUTermVec ℒₛₑₜ (m+1) Vw → IsUTermVec ℒₛₑₜ ((m+1)+1) Ww →
(∀ k ≤ m, Vw.[k] = Ww.[k]) → Ww.[m+1] = ^&0 →
subst ℒₛₑₜ Vw (iVE m (termSubst ℒₒᵣ (QvecVOr m) t)) = subst ℒₛₑₜ Ww (iVE (m+1) t)
```

### 1.1 归纳原理必须是 `IsSemiterm.induction 𝚷`，不是 `sigma1_induction`

**这是本次最贵的坑（浪费约 1 小时）**。谓词含 `∀ Vw Ww, … → … → … = …`，
量词在前 ⟹ 是 **Π 形**。`IsSemiterm.sigma1_induction` 会以
`Tactic 'aesop' failed` 报错（`definability` 失败），错误信息完全不提示"极性错了"。

**判据**：若 `definability` 在项归纳的目标上失败，先想极性。
`IsSemiterm.induction 𝚷` 与 `sigma1_induction` 的参数列表**相同**，只换首参。

**另一个必知**：`definability` 对**命名 `def` + `unfold`** 有效，对**内联 lambda**
失败。写法必须是：
```lean
def QPred (m t : V) : Prop := ∀ Vw Ww, …
theorem … := by
  apply IsSemiterm.induction 𝚷 (n := m+1) (P := QPred (V := V) m)
  · unfold QPred; definability
```

### 1.2 func k=2 支的核心：归纳假设用在**变换后**的向量上

`ve2` 的体在 `qqAlls _ 2` 下，`subst` 下降两层。**关键**：不是对原 `(Vw, Ww)`
用 ih，而是对**变换后的** `(Vw₁, Ww₁)` 用：
```
Vw₁ = termSubstVec (m+1) (qVec² Vw) (^#i ∷ shiftVec 3 m)
Ww₁ = termSubstVec (m+2) (qVec² Ww) (^#i ∷ shiftVec 3 (m+1))
```
关系保持 = `ITSubstOpen4.VRel_transform`（上一会话已证）。
`subst_ve2_gen`（ITSubstOpen6）把它封装成一条引理。

**易错点**：我一开始把 ih 用在原向量上，Lean 报了一堆 type mismatch
（`result ℒₒᵣ iVE.construction … = termSubst …` 形状对不上）。**症状**：
目标里出现 `TermRec.Construction.result`。**处方**：改用变换向量。

## 2. rel 支的 VRel 实例（`ITSubstOpen7.VRel_rel`）

rel 支（`q = ^rel 2 R v`）需要 (★★) 在
```
Vw := ^#j ∷ shiftVec 2 m                              (长 m+1)
Ww := termSubstVec (m+2) (QvecV (m+2)) (^#j ∷ shiftVec 2 (m+1))
```
处的实例。**注意 Ww 的写法**：不是 `^#j ∷ shiftVec 2 (m+1)` 本身，而是它
**经 `QvecV (m+2)` 代入后**的向量（因为 RHS 的 `subst (QvecV m)` 会先被
`subst_qqAlls_two` 推到体内，向量变成 `qVec² (QvecV m) = QvecV (m+2)`）。
三条件的逐项核验已机器证（`VRel_rel`）。

## 3. V 层算术的三个坑（本会话实测，全部真实踩过）

1. **`k'+1+1` 不是 definitionally `k'+2`**（V 是任意模型，`2` 是字面量）。
   凡目标里出现 `m+2`/`m+3`/`m+4` 的地方，要么统一写成 `(m+1)+1` 形式，
   要么用 `show … = … by ring` 显式转换。`ring` 能证等式但**不会**在
   `rw`/`exact` 里自动归一化。
2. **`rw` 的 pattern 匹配对 `if` 表达式不友好**：`nth_cons_shiftVec2` 的结论含
   `if k = 0 then … else …`，`rw [if_pos rfl]` 常报 "Did not find an occurrence"。
   **处方**：改用 `simp [termSubst_bvar, …]`，或先 `rcases zero_or_succ k` 再 `simp`。
3. **`lt_succ_iff_le.mp` 的输入必须是 `x < y+1` 形状**：若手里是 `x < y`，
   先 `lt_iff_succ_le.mp`（得 `x+1 ≤ y`）或 `add_lt_add_right`。

## 4. 核验判据的教训（Master 抓到的，我认）

**旧判据 `grep -q '^src.*error'` 是瞎的**：错误行路径前缀是
`.cg009-verification/round31/src/…`（以点开头），不以 `src` 开头，
**对任何错误都匹配不到** ⟹ 打印 "OK"。所以此前的 "34/34 clean" 是假通过。

**新判据**（已修）：
```bash
rc=$?
if [ "$rc" -ne 0 ] || grep -q 'error:' "$log"; then …FAIL…
elif grep -qE 'sorry|sorryAx' "$log"; then …SORRY…
```
**原则**：判据不得依赖"日志文本里出现什么"；唯一可靠 = **exit code +
`#print axioms` 不含 sorryAx**。修完后立刻暴露 `ITSubstOpen2` 带 1 个 sorry
（未完成的 `composite_eq`），已整块移除（下游零引用）。

## 5. 我走过但没写下的弯路（省下接手者的时间）

1. **曾尝试对 (★★) 用 `IsSemiterm.sigma1_induction`** —— 见 §1.1。
2. **曾把 ih 用在原向量上** —— 见 §1.2。
3. **`congr 1` 链在深嵌套目标上会走偏**：`congr 1; congr 1` 在
   `neg (a ⋏ (b ⋏ ⊤)) ⋎ C` 形状上会把目标切成错误的子目标。**处方**：用
   显式 `congrArg₂ (fun a b => …)` 树（`subst_ve2_gen` 的收尾就是这么写的）。
4. **`IsUTermVec.isSemitermVec` 给的层数是 `listMax (termBVVec …)`**，不是
   调用方想要的层。若下游需要特定层，用 `LayerMono.IsSemitermVec.mono`。
5. **`ite_eq_left`/`ite_eq_right` 是 `if_pos`/`if_neg` 的新名**（deprecation
   警告可忽略，但新代码建议用新名）。

## 6. 与舰队其他线的接口（版本注意）

- **m=0 实例 = 003 的 `iT_substs1`**：我不重复证（按 Master 派工）。
- **Craig 公理的 V 层展开**（004-Step 更正）：是
  `Theory.IsCraigAxiom (V:=V) Sh p = (∃ s p' : V, p = p' ^⋏ qqVerums s ∧ …)`
  **不是**定义层的 `padding`/ℕ。**同名不同层**，照旧版写会卡类型。
- **Master 的 round31 快照**在其树 `132b808e4`（不在我树的历史里）；
  我的 src 也已强制入 git（`4b9b9668`），两树各自自包含。

## 7. 下一步（若继续本线）

`iT_subst_open`（公式层，∀m）的组装：
- **rel 支**：零件全齐（`subst_QvecV_cRel`、`VRel_rel`、(★★)）。
  剩：把 `iTR m 2 R (termSubstVec 2 (QvecVOr m) v)` 与
  `subst (QvecV m) (iTR (m+1) 2 R v)` 各自用 `subst_qqAlls_two` 推入两层，
  体内用 (★★) 的 rel 实例逐分量对齐。
- **all/exs 支**：用 `SubstDomZero.subst_QvecV_domZero`（已证）。
- **and/or/neg/verum/falsum**：`substs_and`/`substs_or`/`substs_neg` 直接组合。
- **注意**：Master 已把一般律（∀m 含 0）派给 001-Step 主攻（m=0 的 all/exs
  会递归到 m=1）。接手前先与 Master 确认是否仍需要本线做。
