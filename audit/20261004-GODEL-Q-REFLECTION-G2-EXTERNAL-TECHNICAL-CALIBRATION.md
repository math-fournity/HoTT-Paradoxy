# G2 技术校准：哥德尔化要求的不只是编码和“自指”名称

> **方案：** `GODEL-Q-REFLECTION-SOP`。
>
> **身份：** `EXTERNAL_TECHNICAL_CALIBRATION / SOURCE_REPORTED_NOT_LOCALLY_REPLAYED / NOT_A_TARGET_ZFC_THEOREM`。

> **判词：** `NUMERAL_BRIDGE_AND_INTERNAL_PROVABILITY_ADEQUACY_ARE_EXPLICIT_GODELIZATION_GATES`。

## 1. 为什么需要这张校准卡

Foundation 的 generic theorem、Metamath 的 proof acceptance、Flypitch 的 proof tree 都说明“有 syntax、proof 或 substitution”尚不足以得到本方案要的对象层哥德尔化。这里不再凭直觉补门，而是用两个独立的、已经公开的形式化来源校准缺口的名称。

## 2. 固定来源与范围

| ID | 来源 | 身份／版本锚点 | 这张卡实际使用的内容 |
|---|---|---|---|
| EGC-01 | Popescu 等，*Distilling the Requirements of Gödel’s Incompleteness Theorems with a Proof Assistant* | JAR 2021，DOI [10.1007/s10817-021-09599-8](https://doi.org/10.1007/s10817-021-09599-8)，2026-10-04 阅读 | 文章把 actual proofs 的表示、proof representability、内部 provability、substitution/instantiation 与 HBL 条件逐项拆开；它还明确区分对象层形式化与把一个内部公式解释为“真正可证明性”的额外 adequacy 问题。 |
| EGC-02 | AFP *An Abstract Formalization of Gödel’s Incompleteness* | [官方 proof document](https://www.isa-afp.org/browser_info/current/AFP/Goedel_Incompleteness/document.pdf)，页面显示 Isabelle `dc45b445012a`／AFP `f6f87675e7ff`，2026-10-04 阅读 | 目录将 proof representability、HBL 条件、formula encoding、computable-function encoding、term encoding、Jeroslow diagonalization 分成独立章节。 |
| EGC-03 | `coquand/agda-godel-tree` | `main@5475628ea4b648f956dce4baee7d0273ba257730`，README SHA-256 `75e774551b114a9e695a932fcf8d7486343241ec58fb5264b20c810a4e396f90`，2026-10-04 读取；[repository](https://github.com/coquand/agda-godel-tree) | README 明确说明 `num/cor` 的不对称、Theory 12 在 T 内部连接 term code 与 numeral/value 的必要性，以及 `thmT` 对 malformed code 的安全默认；这个源是 Basic Recursive Arithmetic，不是 ZFC。 |

这些都是**技术校准**。本轮没有下载、编译或重放 AFP / Agda development；它们不成为本项目的 machine proof，也不改变 G0 的 target source denominator。

## 3. 校准出的两个不可跳过字段

### 3.1 `NumeralBridge`

`Code` 不能只是一份 M 层数据类型或 host string。对于一个候选理论 T，必须固定：

```text
codeSyntax      : Syntax / Proof / Task → CodeDomain
numeralInT      : CodeDomain → Term_T
substituteCode  : 在 T 的 formula/term 中使用 numeralInT(codeSyntax(x)) 的规则
bridge theorem  : 上述编码、numeral 与 substitution 如何在 T 中对应
```

接受的证据必须是相称的 theorem 或 source-defined construction。只有“宿主能把 AST 序列化成整数”或“Lean 有 quotation”时，字段仍为 `OPEN`。

### 3.2 `InternalProvabilityAdequacy`

`Prov_T` 必须同时有两个不同层面的身份：

```text
externalProofRelation  -- 元层：什么是 T 的 proof
internalProvFormula    -- 对象层：T 中哪一个公式表达这件事
adequacy/payment       -- 二者在固定 code、numeral 和语义下为何相连
```

若最后一行未支付，最多只有一个外部 proof relation，不能把它说成“理论正在判断自身的可证明性”。同样，even an internal formula does not by itself say anything about `OriginDone`；后者仍由 GODEL-Q 的 `Bridge` 与 `RealityMap ρ` 单独负责。

## 4. 对本项目各来源的直接影响

| 当前来源 | `Code`／`Check` | `NumeralBridge` | `InternalProvabilityAdequacy` | 判定 |
|---|---|---|---|---|
| Metamath `set.mm` | 有外部 proof/database 与 verifier workflow | 未支付 | 未支付 | proof acceptance 正控制，不是对象层哥德尔化。 |
| Flypitch | 有 Lean M 层 proof tree、substitution | 未支付 | 未支付 | `reflect`/meta quotation 不可替代这两项。 |
| Foundation generic ArithmeticTheory | 对其 generic theorem source 已有 code/quote/substitution/provability 技术基线 | 仅在 generic arithmetic theorem 的既定假设下可用 | 未映射到 target ZFC interface | 不能直接实例化 Foundation ZFC `SetTheory`。 |
| IEP/Norton / C-366 | 过程 contract 或模型表示性 | 不适用 | 不适用 | 仍不能填 actual `Accept_T` 到 parent `OriginDone` 的桥。 |

## 5. 方案更新与禁止外推

本卡使 `GodelizationCard` 在原有 `Code` 与 `Diag` 之间新增显式 `NumeralBridge` 和 `InternalProvabilityAdequacy` gate。它提高的是**将来定理的命题忠实性**：避免一个看似自指的宿主程序、proof transport 或外部 checker被误当作 T 内哥德尔句。

它不证明：

- bare ZFC 有或没有这些桥；
- ZFC 已满足或不满足某个具体不完备性 theorem；
- 本项目的 `Accept_T`、`OriginDone`、`ρ`、Bridge 或 Q 已被固定；
- HoTT H0、芝诺或圆环已经进入一个哥德尔句；
- 外部 Agda / Isabelle 源已在本机重放。

因此 G1–G6 仍是 `NOT_RELEASED`。这个校准只规定：一旦出现目标 source，G2 不可用“有编码／有反射名字”绕过内部 numeral 和 provability payment。
