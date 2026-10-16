# C-379–C-382：CCTTmini₀ 的 formula / certificate-predicate 接口

> **证明包：** `MP-CUBICAL-GODEL-FORMULA-PREDICATE-001`。

| Claim | Agda declaration | 精确范围 |
|---|---|---|
| C-379 | `closedAccepted` | `validCode (code closedC) ≡ true`。 |
| C-380 | `closedProvWitness` | closed certificate 的自然数 code 有明确 `ProvWitness`。 |
| C-381 | `quoteClosed` | `quoteCert closedC` 的 syntax 精确为 `provF (code closedC)`。 |
| C-382 | `quoteClosedHolds` | `provF` formula 的本单位 partial semantic clause 由同一 witness 支付。 |

`validCode`/`ProvWitness` 都是 meta-level constructs。它们不是对象算术内部的可表示谓词；`Formula`
也还没有 Nat coding、formula substitution 或 self-code fixed point。负控制要求 quoted formula 等于 `botF`，
kernel 必须拒绝。
