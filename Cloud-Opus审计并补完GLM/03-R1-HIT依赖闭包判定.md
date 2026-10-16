# 03 R1："HIT-free"的机器判定（含 R6 的桥引理）

> 编号约定：本文的 C-63、C-67、C-71、C-72、C-75、C-76 指 Opus CG-001 目标内索引的 `CG001-C-NN`（`.claude/goals/CG-001-targeted-overview/证据索引.md`），不是 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 其它节里同号的 claim。

> 委托工作单 §3 R1："被调用引理的依赖闭包未机器排查……逐引理追 import 闭包；判定成立则把判定过程落盘为收据级证据，不成立则降格标签"。

## 1. 结论先行

【数学事实】（HITScan 证书，运行 `20260927-COPUS-HITSCAN-CERT-GLM-01 / -OPUS-01 / -KS-01`）：

| 被判定的定理 | 名称级闭包规模 | 闭包中的 HIT | 闭包中的数据类型 | 公理/公设叶子 |
|---|---|---|---|---|
| GLM-R3-C01 `¬universeIsGroupoid` | 251 | **无** | I、ℕ、⊥、Bool | 1=1、IsOne、inS、Sub、Level、PathP |
| GLM-R2-C01 `universeLoopSpaceAtSetIsSet` | 189 | **无** | （同类） | 同上 |
| GLM-R2-C02 `noLevel2AscentAtSets` | 190 | **无** | （同类） | 同上 |
| C-63 `typeIsNotASet`（Opus） | 101 | **无** | I、Bool、⊥ | 同上 |
| C-71 `hSetNotSet`（Opus；= KS 基例） | 149 | **无** | （同类） | 同上（运行 `-HITSCAN-CERT-OPUS-02`，COPUS-R1-C06） |
| C-75 包的 `localGlobal`（Opus，R6 的桥） | 201 | **无** | （同类） | 同上 |
| 一般 n：`KS-Theorem-5-9` / `workOrderForm` / `KS-Theorem-5-10-U≤` / `-Loop` | 363 / 364 / 363 / 364 | **无** | I、Bool、⊥、ℕ | 同上 |

负控制（扫描器有牙齿，运行 `-HITSCAN-NEG-01/02/03`，均被拒且点名 HIT）：

| 目标 | 扫描器报告的 HIT |
|---|---|
| GLM-R1-C01 `realisticIotaSyntaxIsASet` | `RealisticIotaSyntax.Tm` |
| C-75 `universeHasNoLevel` | `HubAndSpoke`（截断）、`Susp`、`S¹`、`EM₁`、`EM₁-raw` |
| 一行 `∥ Bool ∥₁` 用例 | `∥_∥₁` |

所以 R1 的判定是：**GLM 的"HIT-free"断言成立**（R3-C01、R2-C01/C02），并由人工断言升级为收据级机器证据；C-63 的"本来就无 HIT"（GLM 查重时的判断）同样成立；C-75 与 C-76 的高层部分确实依赖 HIT（与 Opus 的自述一致）。

## 2. 为什么必须在"名称级"判定

【数学事实】cubical 0.9 中，`Cubical.Data.Sigma.Base` 直接导入 `Cubical.HITs.PropositionalTruncation.Base`（为定义 `∃`）；`Cubical.Homotopy.Loopspace` 直接导入 `Cubical.HITs.SetTruncation` 与 `Cubical.HITs.Truncation`。因此：
- GLM-R3-C01 的运行（`--ignore-interfaces`）检查了 74 个库模块，其中 4 个 `PropositionalTruncation*`；
- 一般 n 的运行检查了 157 个库模块，其中 35 个 `Cubical.HITs.*`。

"导入闭包无 HIT"对任何用到 Σ/等价的证明都不可能成立。GLM 的原边界声明（groupoid REVISIONS L13："HIT-free 指证明的导入与构造不使用任何 HIT 类型；……传递接口图包含 `Cubical.HITs.*` 模块……未进入本证明的任何构造"）方向正确，但"未进入任何构造"当时只是断言。

## 3. 判定工具 HITScan（`HoTT/formal/cloud-opus-glm-audit/hitscan/HITScan.agda`）

- **做法**：Agda 反射宏。从目标名出发，读每个名字的类型与定义（函数子句的望远镜、模式、定义体；数据类型的构造子；记录的构造子与字段；构造子所属的数据类型），收集出现的所有名字，递归直到闭包（名字集合用哈希二叉树去重，燃料上限 10⁶）。对闭包里每个数据类型，把它全部构造子的类型归一化，若某个构造子的陪域是路径类型，就记为 HIT。
- **为什么这样判 HIT 是完整的**：cubical Agda 只能通过带路径构造子的 `data` 声明引入 HIT；路径构造子的类型陪域必是 `PathP` 或其别名。归一化会展开 `isSet`、`isProp`、`Path` 等别名，但 **`_≡_` 是 Agda 的 BUILTIN PATH，归一化后仍保持折叠**——扫描器的第一版只认 `PathP`，因此漏判了 `∥_∥₁`；这个缺陷正是由负控制 `NegCertPT` 当场暴露并修复的（现在 `PathP` 与 `_≡_` 两种头部都认）。
- **证书形式**：`hitsOf n : List Name` 与 `sizeOf n : Nat` 是可写进类型的宏，证书文件写成 `Path (List Name) (hitsOf ¬universeIsGroupoid) []`、`Path Nat (sizeOf ¬universeIsGroupoid) 251`，由类型检查器核对。加 `-v hitscan:10` 时，`reportClosure` 把整个闭包（每个名字及其种类）打印进运行的 stdout，收据里可逐名复核。

## 4. 边界（写明，不藏）

1. **反射所见即闭包**：抽象/不透明定义与公设在反射下是叶子，列入 `axiomsOf`。本次所有目标的叶子只有 cubical 内建的 6 个原语——没有被隐藏的库定义。
2. **未重建省略参数**：Agda 2.8.0 在 `withReconstructed` 下对某些库定义触发内部错误（`__IMPOSSIBLE__`，`ReconstructParameters.hs:137`），故不重建构造子/投影被省略的参数。理论上唯一可能漏看的情形，是某个 HIT 类型**只**出现在被省略的构造子参数里，而不出现在任何被遍历的类型或项中——这样的出现不涉及 HIT 的构造子、消去子或任何提及 HIT 的常量类型，可以换成任意类型而不影响证明。
3. **证书的含义**：它说的是"证明项与所涉常量的类型不涉及任何 HIT"，不是"证明可在某个无 HIT 的元理论中进行"的元定理。Glue、hcomp、transp 是 cubical 原语，不是 HIT；单价性经 Glue 实现（闭包里的 `primGlue`）。
4. 闭包规模依赖 cubical 0.9 的库内部结构。

## 5. R6：熄火读法的桥

- 【数学事实】C-75 包中的桥引理 `localGlobal : Ω^(2+n)(U, X) ≃ Π (x : X), Ω^(1+n)(X, x)` 的名称级闭包（201 名）**无 HIT**（COPUS-R6-C01）。它所在的**文件**导入 Eilenberg–MacLane 空间，那些 HIT 只被 C-75 的见证（`K n = EM ℤ (1+n)`）和 C-76 的高层部分使用。
- 因此"引擎在集合成员处熄火"这一读法的证据等级是：**形式部分（GLM-R2-C02）+ 桥（localGlobal）均为无 HIT 的机器事实；"引擎""熄火"这组词是解释层**。桥的陈述本就不提 HIT，证明也不用 HIT。
- 本会话的一般 n 证明使用的是 `localGlobal` 的**带点**版本 `localGlobal∙`（非平凡性要沿等价传递），同样无 HIT（COPUS-R1-C05 的闭包包含它）。

## 6. 标签处置

| 位置 | 原标签 | 处置 |
|---|---|---|
| groupoid REVISIONS L13、索引 §9、RUN.json scope | "HIT-free"（人工断言） | 保留"HIT-free"，改注"名称级闭包机器证书 COPUS-R1-C01（导入闭包含 PT 模块，未被使用）" |
| ascent-stall CLAIM、AscentStallAtSets.agda 注释 | "HIT-free imports only" | 同上改注 COPUS-R1-C02/C03；"imports only"措辞不准确（导入闭包含 PT），以名称级为准 |
| 索引 §9 查重段："C-63 导入仅 Prelude/Univalence/Bool/Nullary，本就无 HIT" | 人工判断 | 结论成立，改注 COPUS-R1-C04（导入闭包同样含 PT，未被使用） |
