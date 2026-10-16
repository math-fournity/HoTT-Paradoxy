# 攻坚路线：8 个待填支逐支拆解

所有支的归纳不变量见 `03-缺口精确定位/STATUS.md`。目标形状由 `simp only [Q, fstIdx_*]` 化简为
`Derivable 𝗭𝗙𝗖 (translateSeq s)`。下列写法本机已实测类型对得上（除核心难点 E/F/G/H）。

## 支 A/B：andIntro / orIntro（最易，优先）
- `iT_and`：`iT 0 (p ⋏ q) = iT 0 p ⋏ iT 0 q`（同形 `iT_or`）。
- 配 `Derivable.and_m` / `or_m`（`Foundation/.../Arithmetic/Bootstrapping/Syntax/Proof/Basic.lean:798`）。
- 卡点只是 `fstIdx dp` 的归约，由 `DerivationOf` 的 `.1` 在真实支里提供：`have hdp := ...; rw [hdp.1]`。

## 支 C/D：axL / cutRule（易，用已证 iT_neg）
- `axL`：`translateSeq s` 含 `iT 0 p` 与 `iT 0 (neg p)`；用 `iT_neg`（一般版本，非引号化 `iT_quote_neg`）
  把后者化成 `neg (iT 0 p)`，得到互补对，由 `Derivable.axL` 得可证。
- `cutRule`：同法 `rw [iT_neg]` 化 `iT 0 (neg p)`，配 `iT_and` 与 `Derivable.cut`。

## 支 E/F/G：shiftRule / allIntro / exsIntro（核心难点）
- 需要 `iT_setShift`：`iT (n+1) (setShift p) = setShift ℒₛₑₜ (iT n p)`。
- 需要 `iT_substs1`：`iT (n+1) (substs1 p t) = substs1 ℒₛₑₜ (iT n p) (translateTerm t)`。
- **模板**：`07-项目模块/GodelQ/ZFC/ShCraigElimNegLaw.lean` 的 `iT_neg`——它用
  `UformulaRec1.Construction.semiformula_result_induction`（与 `isSemiformula_iT` 同原理）沿公式结构
  归纳，同样的 9 支形状，把 `neg` 换成 `setShift`/`substs1` 即可。
- 需要的 Foundation 支持引理：`setShift`/`substs1` 的逐构造子展开、`IsUFormula.setShift_and` 等
  （仿 `IsUFormula.neg_and`），在 Foundation 源码里按 05-API.md 的引用表定位。

## 支 H：axm（中难，唯一用 𝗭𝗙𝗖 公理）
- `Sh.craig` 公理形状来自 Foundation 的 Craig 填充（形如 `ρ.padding k`），定义在
  `Foundation/.../Arithmetic/Bootstrapping/Syntax/CraigTrick.lean`。
- 翻译后需落到 `𝗭𝗙𝗖` 公理；其余 9 支只靠逻辑规则 + `iT` 相容律。
- 建议先证 E/F/G 的支持引理再处理此支；参考 `zfcTr-D3-plan.md` §5.1 与 Claude W8 规格 §3。

## 组装（收尾）
8 支无 sorry 后，在 `induction_setup` 里把 `sorry` 换成各支引理，得到无 sorry 的 `induction_setup`；
新增无 sorry 的 `ShCraigElim`（见 02-GOAL.md），`Z0Blocked.lean` 的 `sorry` 改为引用它。

## 难度排序
1. 支 A/B（直接填）2. 支 C/D（iT_neg 已证）3. 支 E/F/G（照 iT_neg 写 setShift/substs1）4. 支 H（axm）
