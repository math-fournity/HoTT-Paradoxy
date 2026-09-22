# P36：圆去点来源的静态定义、强细化与 provenance 边界审计

**任务：** `P36-P1-PROVENANCE-ORIGIN-COVERAGE-001`

**状态：** `PARTIAL_REUSE / STATIC_FIXED_POINT_PUNCTURE_DEFINED / ACTUAL_MRICH_IS_STRONG_REFINEMENT / HISTORICAL_PROVENANCE_NOT_FORMALIZED / P37_WEAK_PUNCTURE_FIDELITY_REQUALIFICATION_SELECTED / NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM`

## 1. P36 要回答的精确问题

P36 从 `G0 → P1 → P34 → P35 → P36` 只检查原圆环 `X` 的来源边：当前形式化中的
`mRich` 是否真的是“一个指定点被从实际圆上拿掉后的 M”，并且是否保存了这种来源作为操作或历史。

本波次固定四层，避免把它们混为一句“圆去点”：

| 层 | 需要的对象 | 当前问题 |
|---|---|---|
| 圆与指定点 | `RealCircle` 与 `east` | 是否有实际圆和固定被去掉点？ |
| 弱静态去点 | `PuncturedRealCircle = Σ p:RealCircle. p ≠ east` | 是否真的定义了“除 east 外的圆点”这一 carrier？ |
| 强去点细化 | `StrongPuncture = Σ p:RealCircle. Strong p` | `mRich` 用的是不是原弱 carrier，还是一个额外条件的细化？ |
| 来源历史/事件 | 某个明示 `circle + point → source` 的操作、时间/轨迹或 provenance witness | 当前 `Input.source` 是被产生/证明的，还是被直接供应的？ |

P36 不把静态子类型定义误称为一个实际物理删除事件，也不把缺少 provenance event 写成 HoTT 缺陷。

## 2. 本地资产侦察与公开检索判断

**公开检索：** `NOT_SEARCHED_WITH_REASON`。本波次只问固定本地 source 是否含指定 definitions、refinement 和 provenance 字段；外部论文不能改变这些实际 declarations。P6 已比较过相邻的 marked/stratified/cospan/directed 数学对象，P36 不以换术语重复该分母。

**本地资产逐项判词：**

| 资产 | 发现 | 分类 |
|---|---|---|
| `NativeRealCircleQualification.agda` | `RealCircle` 是实际 Dedekind 实平面圆子类型；`east` 被明确构造；`PuncturedRealCircle` 是 `p ≠ east` 的子类型。 | `EXACT_STATIC_PUNCTURE_BASE` |
| `PunctureApartness.agda` | `StrongPuncture = Σ RealCircle Strong`，并有 `forgetStrong : StrongPuncture → PuncturedRealCircle`。 | `EXACT_STRONG_REFINEMENT_AND_FORGETFUL_MAP` |
| `NativeStereographic.agda` | 从弱去点回到强去点需要 `Lift`；现有 `weakCircleEquivStrong` 与 `weakCircleEquivReal` 显式以该前提为参数。 | `EXACT_CONDITIONAL_REFINEMENT_BOUNDARY` |
| `NativeRichCurve.agda` | `mRich = StrongPuncture , mData`；因此实际 P34/P35 source 不是裸 `PuncturedRealCircle`。 | `ACTUAL_SOURCE_REQUALIFICATION_REQUIRED` |
| `NativeSourceContract.agda` | 文件明确说 source data 是 supplied，且没有 physical provenance oracle；`actualInput.source = mRich`。 | `HISTORICAL_PROVENANCE_NOT_FORMALIZED` |
| C-283–C-290 及其保存 run | 已机器化弱/强逻辑界、强域参数化、条件弱域等价及与开区间的条件桥。 | `REUSABLE_FORMAL_EVIDENCE_WITH_SCOPE` |

## 3. 对原 M 的准确裁决

### 3.1 已被定义的静态“去点”

在固定 `east=(1,0)` 下，`puncturedSubtype p = ¬(p=east)` 和
`PuncturedRealCircle` 的确把“实际 RealCircle 上除指定 east 外的点”定义成一个子类型。
因此，若用户所说的“圆上拿掉一点”只要求一个**静态的指定点排除 carrier**，当前来源有直接数学对应。

### 3.2 当前 `mRich` 不是该弱去点 carrier 本身

`mRich` 的 underlying carrier 是 `StrongPuncture`，不是 `PuncturedRealCircle`。
`Strong p` 是 `apart(xCoord p,1)`；它可推出 `p≠east`，但反向的 point-preserving refinement
需要 `Lift`。现有代码保留了这一条件而没有悄悄把弱排除变成强 apartness：

```text
forgetStrong : StrongPuncture → PuncturedRealCircle
weakCircleEquivStrong : Lift → PuncturedRealCircle ≃ StrongPuncture
```

所以此前的 `mRich`/`OpenRealInterval` 对照是一个**强去点版本**的 P1 实例。它不能未经说明地被当作
“任意 ordinary circle-minus-point M” 的无条件形式化。这个结论是规格忠实性的修正，不是矛盾。

### 3.3 未被定义的是历史删除事件

`NativeSourceContract` 的 `Input` 有 `source`、`targetCarrier` 和 `encoding`，并在注释中明说
“Supplied source data … no physical provenance oracle”。`actualInput.source = mRich` 使来源对象被固定，
但不提供一个从完整圆和指定点执行删除的时间性 operation、发生证书或可反演历史。

因此 P36 的精确判词是：

```text
PARTIAL_REUSE
  / 静态固定点去除已定义
  / 实际 mRich 使用更强的 apartness refinement
  / 来源历史或物理删除 event 尚未形式化
```

它既不能支撑“传统同胚已经被推翻”，也不能支撑“HoTT 允许把 M/N 混同”。它说明：若研究要继续以用户的
来源敏感 `R_min` 为主张，必须把普通弱去点、强技术性细化和历史 provenance 三件事明确分开。

## 4. P37：弱去点任务忠实性复资格化

P37 不先建立新的 provenance wrapper。它将固定原 M 的**弱**输入为
`PuncturedRealCircle`，然后把以下现有资产逐项映射到同一合同：

| 字段 | P37 检查 |
|---|---|
| Input | `RealCircle`、`east`、`PuncturedRealCircle` 的弱排除定义 |
| Refinement | `StrongPuncture` 与 `forgetStrong` 的方向，以及 `Lift` 的精确角色 |
| Operation | 到 `OpenRealInterval` 的实际 equivalence/path 是否只在强域无条件成立，弱域是否显式带 `Lift` |
| Observation | 指定点、闭图、端点以及普通弱点是否被保留或仅被忘却 |
| Done | 原 M 若要求普通去点，不得由强域结论替代；若需要 strong witness，必须把它写成输入条件 |
| 正控制 | C-283–C-290、`weakCircleEquivStrong`、`weakCircleUnitHomeomorphism` 的显式条件 |
| 最强反解释 | 若原用户的 M 已明确选择 strong apartness，则该 requalification 不产生 mismatch；否则它揭示的是 input refinement，仍非 HoTT defect |

P37 只决定现有 formalization 与原 M 的任务关系，不能用“弱域无无条件 equivalence”代替原始现实判词、实际 K 或理论错误。

## 5. 波次反思

1. **新增事实：** 当前 source 模型确有 fixed-point puncture 的静态定义；`mRich` 却是 `StrongPuncture` 细化，来源事件未记载。
2. **改变的判词：** P34/P35 只能被表述为强去点 P1 控制；任何把它们直接称为原普通 M 的说法需要降级并经过 P37。
3. **合同是否漂移：** 用户原 X 没变；发现的是当前 formal model 对 M 的额外输入条件。该条件必须显式保留。
4. **正控制与反解释：** `forgetStrong` 和 `Lift`-条件等价表明系统没有静默混同；静态 point exclusion 是正控制，历史 provenance 缺失是范围边界。
5. **重复检查：** C-283–C-290 已覆盖逻辑/参数化层，所以 P36 不重跑内核或复造它们。
6. **分支资格：** P1 的弱/强任务忠实性获得 P37 资格；P2 仍关闭，P3无新 K，P4无触发。
7. **停止理由：** P36 已完成定义和合同覆盖判断；再扩展同一关键词不会减少新的根义务。

### 波次坐标

- **最终目标连接：** P1 `R_min` 的来源与输入忠实性；它直接保护原 `X` 不被强域细化悄悄替换。
- **实际价值：** 给出可核查的 `SPEC_REFINEMENT` 风险，而不是把一个有利的强域正例误作原任务完成或 HoTT 失配。
- **裁决：** `CLOSE_WITH_SCOPE / SWITCH_BRANCH_TO_P37_WEAK_PUNCTURE_FIDELITY_REQUALIFICATION`。

## 6. 禁止外推

- 这不是普通拓扑学、HoTT 或 univalence 的反例。
- 这不是 `StrongPuncture` 与 `PuncturedRealCircle` 不等价的无条件定理；现有关系的精确条件是 `Lift`。
- 这不证明物理删除过程不可表达；只说明当前 source contract 没有提供这种事件/provenance。
- 这不建立 `K_theory`、`K_app`、`K_engine` 或现实非现实性悖论。
