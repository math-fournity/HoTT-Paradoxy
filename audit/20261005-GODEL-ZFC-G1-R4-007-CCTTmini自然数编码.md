# GZ-009：CCTTmini₀ 的自然数编码、decoder 与 injectivity

> **身份：** `ROUTE_UNIT_RECORD / GODEL-ZFC-CONVERGENCE-SOP / G1-R4`。
>
> **状态：** `LOCAL_CLOSED_WITH_SCOPE / GZ-010_SUCCESSOR_REQUIRED`。

## 1. Parent gap

GZ-008 已有有限 `RawCert`、structural checker 和 `Deriv` witness，但没有把证书带入自然数域。
Gödel式 quotation、substitution 和 diagonalization 都要求能够谈论具体 code；因此这一单位只解决
**同一有限 fragment 的 Nat coding**，不增加新的 cubical language constructs。

## 2. 冻结构造

`CCTTminiNat.agda` 实现：

```text
RawCert
  → bits : List Bool                  -- self-delimiting prefix grammar
  → codeBits : List Bool → Nat
  → code : RawCert → Nat

Nat
  → unbits / finite-fuel run
  → decode : Nat → RawCert            -- malformed-code fallback included
```

parser 的 fuel 是显式 `Nat`，按 fuel 结构递归；`codeBits` 的 size bound 让一个有效 code 自己供给
解析其 image 所需的 fuel。主 obligations 是 bit-list roundtrip、streaming parser roundtrip、image
roundtrip `decode (code c) ≡ c` 与 injectivity。

## 3. 实际 kernel 结果

主 run [MP-CUBICAL-GODEL-NAT-CODING-001](../HoTT/verification/runs/20261005-MP-CUBICAL-GODEL-NAT-CODING-001-01/RUN.json)
在 pinned Cubical Agda 2.8.0-3d04bac 上 exit 0。C-375--C-378 分别固定：

1. `unbits-code`；
2. `parse-run`；
3. `decode-code`；
4. `code-injective`。

negative source `WrongCCTTminiNat.agda` 要求 `decode (code positiveC) ≡ zeroC`，在
`reflC (sucC (varC zero)) != zeroC` 处以 exit 42 被拒绝。

### 保留的 compiler warning

Agda 对 `≤-trans` 给出 `UnsupportedIndexedMatch`：该辅助函数依赖 `suc` constructor 的 injectivity，
在 arbitrary cubical transport 上不会按预期计算。这个 warning 没有使 C-375--C-378 的 declarations
被拒绝；但它限制了本单位的语言：这里只主张 fixed RawCert coding propositions 的 kernel acceptance，
不主张 `≤-trans` 的 transport-computational behavior。warning 原文完整保留在主／负 run stdout。

## 4. 局部判词

```text
CCTTMINI_NAT_CODING_DECODING_MACHINE_PROVED_WITH_SCOPE
TOTAL_FALLBACK_DECODER_AND_IMAGE_ROUNDTRIP_MACHINE_PROVED
WARNING_PRESERVED_TRANSPORT_COMPUTATION_NOT_CLAIMED
```

这使 GZ-008 的 certificate object 具备可自指研究所必需的 **Nat code domain**，但还没有一个
object-language formula predicate `Provable(code)`；因此不是 Gödel fixed point，更不是 HoTT 或 bare ZFC
的结论。

## 5. Required successor

`GZ-010 / R4-CCTTMINI-FORMULA-PREDICATE-001`：在不修改 CCTTmini₀ certificate coding 的前提下，
定义一个有限 formula language 和 `Provable`/proof-certificate relation；要求把 `RawCert` code 作为
可引用对象带入公式语法，区分 meta-level checker 与 object-level predicate。随后才可冻结 representability
与 diagonal fixed-point 的精确前提。

`GZ-010` 不得通过把 Foundation 的 `Provable` 名称、ERCF-3 的 formula grammar 或 redtt host checker
直接挪入 CCTTmini₀ 来跳过 source correspondence；任何复用必须写出 translator 和范围。
