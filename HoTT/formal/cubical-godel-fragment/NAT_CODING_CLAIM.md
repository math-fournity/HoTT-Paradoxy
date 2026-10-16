# C-375–C-378：CCTTmini₀ 的 Nat coding / decoding

> **证明包：** `MP-CUBICAL-GODEL-NAT-CODING-001`。
>
> **输入语言：** GZ-008 的项目定义 `RawCert`；不是上游 cctt/redtt 的完整 source language。

| Claim | Agda declaration | 范围 |
|---|---|---|
| C-375 | `unbits-code` | 任意有限 `List Bool` 经 `codeBits` 后，在已知 bit length 下可恢复。 |
| C-376 | `parse-run` | prefix grammar 的 finite-fuel parser 在 `bits c ++ rest` 上恢复 `c` 与原 rest。 |
| C-377 | `decode-code` | `decode (code c) ≡ c`：total `Nat → RawCert` decoder 对每个编码像 roundtrip。 |
| C-378 | `code-injective` | `code c ≡ code d → c ≡ d`。 |

`WrongCCTTminiNat.agda` 声称 `decode (code positiveC) ≡ zeroC`，必须被 kernel 拒绝。

## 严格边界

该编码使用 self-delimiting bit grammar、total fallback decoder 和 finite fuel；Malformed natural
codes 也得到某个 `RawCert`，但只证明编码像上的 roundtrip。`CCTTminiNat.agda` 在 Cubical Agda 中
保留一个 `UnsupportedIndexedMatch` warning：辅助 `≤-trans` 在 transport 下不计算。主 declarations
仍由 kernel 接受；本包不主张该辅助证明的 transport-computational behavior。

本包仍不包含：formula language、proof predicate `Provable`、arithmetized representability、quotation into
an object arithmetic theory、diagonal fixed point、independence theorem、full cubical conversion/univalence/HIT、
fixed H0 transport 或任何 bare ZFC conclusion。
