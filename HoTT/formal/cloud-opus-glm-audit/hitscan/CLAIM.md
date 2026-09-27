# HITScan：名称级依赖闭包的 HIT 机器判定（审计项 R1、R6）

> 编号约定：本文的 C-63、C-67、C-71、C-72、C-75、C-76 指 Opus CG-001 目标内索引的 `CG001-C-NN`（`.claude/goals/CG-001-targeted-overview/证据索引.md`），不是 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 其它节里同号的 claim。

> 2026-09-27；Cloud-Opus 审计会话。工作单 §3 R1："HIT-free 是人工断言……逐引理追 import 闭包；判定成立则把判定过程落盘为收据级证据"。
> - 工具：`HITScan.agda`（Agda 反射宏；无公设，`--safe --cubical`）。
> - proof ids：`MP-COPUS-HITSCAN-001`（`CertGLM.agda`）、`-002`（`CertOpus.agda`）、`-003`（`CertKS.agda`）、`-004`（`CertC71.agda`）；负控制 `MP-COPUS-HITSCAN-NEG-001`（`NegCertIota.agda`）、`-NEG-002`（`NegCertC75.agda`）、`-NEG-003`（`NegCertPT.agda`）。

## 1. 为什么不能只看导入清单

cubical 0.9 的 `Cubical.Data.Sigma.Base` 直接导入 `Cubical.HITs.PropositionalTruncation.Base`；`Cubical.Homotopy.Loopspace` 直接导入 `SetTruncation` 与 `Truncation`。因此任何用到 Σ/等价/环路空间的证明，其**导入闭包**必含 HIT 模块（GLM-R3-C01 的运行里就检查了 4 个 PT 模块；一般 n 的运行检查了 35 个 HIT 模块）。"是否用到 HIT"只能在**被使用的名字**层面判定。

## 2. 判定方法（`HITScan.agda` 文件头为准）

从目标名出发，用反射读每个名字的类型与定义（子句望远镜、模式、定义体），收集出现的全部名字并递归直至闭包；对闭包中每个数据类型，把其全部构造子的类型归一化，若某构造子的陪域是路径类型（`PathP` 或 BUILTIN PATH `_≡_`），该数据类型记为 HIT。宏 `hitsOf`/`sizeOf`/`axiomsOf` 可写进类型，由类型检查器核对等式。

**边界（明示）**：① 闭包是 Agda 反射所揭示的；抽象/不透明定义或公设会作为叶子出现在 `axiomsOf` 中——本次所有目标的叶子只有 cubical 内建的 `1=1, IsOne, inS, Sub, Level, PathP` 六项；② 为避开 Agda 2.8.0 在 `withReconstructed` 下的内部错误（`__IMPOSSIBLE__`，ReconstructParameters.hs:137），不重建被省略的构造子/投影参数；因此唯一理论上漏看的情形是"HIT 类型只出现在被省略的构造子参数里、却不出现在任何被遍历的类型或项中"——这种出现可以换成任何类型而不影响证明（它不涉及 HIT 的构造子、消去子或任何提及 HIT 的常量类型）。

## 3. 命题

| claim | 形式命题（逐字） | 读法 |
|---|---|---|
| COPUS-R1-C01 | `glm-r3-c01-noHIT : Path (List Name) (hitsOf ¬universeIsGroupoid) []`；`glm-r3-c01-size : Path Nat (sizeOf ¬universeIsGroupoid) 251` | GLM-R3-C01 的名称级闭包（251 名）无 HIT |
| COPUS-R1-C02 | 同式，`universeLoopSpaceAtSetIsSet`，189 | GLM-R2-C01 无 HIT |
| COPUS-R1-C03 | 同式，`noLevel2AscentAtSets`，190 | GLM-R2-C02 无 HIT |
| COPUS-R1-C04 | 同式，`typeIsNotASet`（C-63），101 | C-63 无 HIT |
| COPUS-R1-C06 | 同式，`hSetNotSet`（C-71，= KS 基例），149 | C-71 无 HIT |
| COPUS-R6-C01 | 同式，`localGlobal`（C-75 包），201 | local-global 桥无 HIT（其**文件**导入 EM，但桥不用） |
| COPUS-R1-C05 | 同式，`KS-Theorem-5-9` 363、`workOrderForm` 364、`KS-Theorem-5-10-U≤` 363、`KS-Theorem-5-10-Loop` 364 | 一般 n 重放无 HIT |

负控制（须被拒且点名 HIT）：`realisticIotaSyntaxIsASet` → `[Tm]`；`universeHasNoLevel`（C-75）→ `[HubAndSpoke, Susp, S¹, EM₁, EM₁-raw]`；一行 ∥_∥₁ 用例 → `[∥_∥₁]`。

## 4. 禁止外推

- 证书说的是"证明项与所涉常量的类型不涉及任何 HIT"，不是"证明可在没有 HIT 的某个元理论中进行"的元定理；后者还需要对 cubical Agda 的片段做元理论论证。
- 证书不覆盖 cubical 的原语本身（Glue、hcomp、transp 等是原语，不是 HIT；单价性经 Glue 实现）。
- 名称级闭包规模（251 等）依赖 cubical 0.9 的库内部结构，换库版本会变。
