# 九支（实为十支）归纳任务拆解与攻坚路线

`ShCraigElim` 用 `Derivation.induction1`（Foundation `.../Bootstrapping/Syntax/Proof/Basic.lean:642`）
对 Sh.craig 的推导做结构归纳。该原理的 10 个规则支是：
`axL`、`verumIntro`、`andIntro`、`orIntro`、`allIntro`、`exsIntro`、`wkRule`、`shiftRule`、
`cutRule`、`axm`。每个支的证明义务是把“当前推导的结论 sequent 翻译后 𝗭𝗙𝗖 可导”
（`Q d`，即 `Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`）从归纳假设推出来。

## 0. 前置：两条已填的支（模板）

- `hWk`：用 `Derivable.wk` + `translateSeq_mono` + `isFormulaSet_translateSeq`（已证在 ShCraigElimBranches.lean）。
- `hVerumIntro`：用 `Derivable.verum` + `iT_verum`（已证）。

## 1. neg 律（hAxL / hCut / hShift 三支配它）—— 必须先修，否则编译不过

`ShCraigElimNegLaw.lean` 想证一般（V 内任意公式码）的
`iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)`。当前文件用 `UformulaRec1.Construction.semiformula_result_induction`
展开，但 and/or/all/exs 支的 rewrite 模式错。修复要点（对照已证的 iT_and 的形状）：

`iT_and` 的真实定义（InternalTranslate.lean:552）是
`iT n (p ^⋏ q) = iT n p ^⋏ iT n q`，即改写的是 `iT (p⋏q)`。
而 neg 律的 `and` 支目标是 `iT param (neg (p⋏q)) = neg (iT param (p⋏q))`，
应先 `rw [neg_and]` 得到 `iT (neg p ⋎ neg q)`，再用 `iT_or`（改写 `iT (neg p ⋎ neg q)`）
得到 `neg (iT p) ⋎ neg (iT q)`，再用 `neg_or` 反向收成 `neg (iT p ^⋏ iT q)`，最后用归纳假设
`ihp : iT (neg p) = neg (iT p)`、`ihq` 代入。和 `ShCraigElimNegFilled.lean` 的 `neg_and_branch`
写法一致（那个文件本身编译通过，可作模板）。**不要再直接 `rw [iT_and, iT.construction.and]`**——
那样会在 `iT.construction.and` 上展开、和目标对不上。

`all`/`exs` 支：目标经 `neg_all`/`neg_ex` 展开后会出现 `imp ℒₛₑₜ domZero (iT (neg p))` 之类；
用 `iT_exs`/`iT_all`（它们改写 `iT (∃ p)`/`iT (∀ p)`，注意层数 +1 由 `domZero`/bound shift 处理），
再用 `IsUFormula.neg_neg` 抵消一次 neg，最后把归纳假设 `ih` 以 `congrArg` 形式代入。
`imp` 是 binder 里的连接词，rewrite 时要写成 `rw [neg_all .., iT_exs ..]` 后手动 `rw [imp]` 一次，
不要指望 simp 透过 binder 记号。`IsUFormula.imp` 是 iff，要用在 `have`/`rw` 时带 `.1`/`.2` 或 `constructor`。

修完 neg 律后，把它接成定理 `iT_neg`（当前文件已有这个名字，把 sorry 去掉即可），
供 hAxL/hCut/hShift 三支把 `iT (neg p)` 化成 `neg (iT p)`。

## 2. 纯语法支（应可直接填，照模板）

| 支 | 需要 | 写法 |
|---|---|---|
| hAnd | iT_and + Derivable.and_m | `iT (p⋏q) = iT p ⋏ iT q`，两子推导的 𝗭𝗙𝗖 推导用 and_m 合取 |
| hOr | iT_or + Derivable.or_m | 同上，or_m |
| hAxL | iT_neg（修后） | `p ∈ s ∧ ¬p ∈ s` => `Derivable 𝗭𝗙𝗖 (insert (iT p) ∅)` 由 `Derivable.by_axL` |
| hCut | iT_neg | 切去 `neg p`，用 Derivable.cut |

## 3. 需要新相容律的支（照 iT_neg 模板各写一个）

| 支 | 需要的相容律 | 说明 |
|---|---|---|
| hAll | iT 与 setShift 的相容 | `allIntro` 在 φ 上加一层量词，翻译后层数 +1，需 `iT (∀p) = ∀(iT p 经 setShift)` |
| hExs | iT 与 substs1 的相容 | `exsIntro` 用项代入，需 `iT (∃p[t]) = ∃(iT p 经 substs1)` |
| hShift | 同 hAll | `shiftRule` 平移自由变量，与 setShift 相关 |

这三个相容律的写法与 iT_neg 同形：用 `UformulaRec1.Construction.semiformula_result_induction`
（对 setShift / substs1 这两个 UformulaRec1 构造）证一般版本。Foundation 的 `setShift`/`substs1`
在 `Rewriting` 或 `Bootstrapping.Syntax` 里定义，先 `#print` 其 `construction` 字段确认可归纳。

## 4. axm 支（唯一用到 ZFC 公理）

`hAxm` 的结论 sequent 由 Sh.craig 的 Craig 公理给出（形状 `ρ.padding k`）。读
`Foundation/.../Bootstrapping/Syntax/CraigTrick.lean` 看 `Theory.craig` 如何把
一个 Σ1 定义挑成一致句；该支要证：`translateSeq` 把这个 Craig 公理翻译成 𝗭𝗙𝗖 的一条定理。
这正是 D3 跨到 ZFC 的实质一步，也是整条链里唯一真正“用”到 ZFC 公理的地方。

## 5. 组装

把 10 支接进 `ShCraigElimSetup.induction_setup`（替换 10 个 sorry），得到无 sorry 的
`ShCraigElim`。`Z0Blocked.lean` 的 sorry 改为 `exact bwd_of_shcraig_elim (fun σ => ...) σ h`。

## 6. 验收（F-011）

1. 精确命题落源码，无 sorry；
2. `#print axioms` 仅含 propext、Classical.choice、Quot.sound；
3. 正运行 + 至少一个负控制（内核应拒绝的变体）；
4. 正式 run receipt（capture_run.py）；
5. 更新 形式化追踪/ 与 CLAIM_EVIDENCE_MATRIX.md。
