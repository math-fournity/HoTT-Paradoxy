# HMZ-010：预检覆盖、remainder 与重开条件

| 项目 | 状态 | 证据 |
|---|---|---|
| Source tag resolution | `FROZEN` | `Isabelle2021-1-RC5` = `6a65dad3761d436f234dbd752201fe70fffa0200`. |
| Exact source file and hash | `ARCHIVED_AND_HASHED` | `HMZ-S-027` in `originals/`. |
| quotient formation / I/E / unary / binary consumers | `READ` | source lines 10–231. |
| `RepFun` source meaning | `READ_REUSED` | HMZ-S-011 manual. |
| Book Power Set quotient comparison | `READ_REUSED` | HMZ-S-026 / HMZ-009. |
| Actual consumer at proof-formalization layer | `PRESENT` | `quotientE`, `UN_equiv_class`, `UN_equiv_class_type`, `UN_equiv_class2`, `UN_equiv_class_type2`. |
| Same Power Set-subset formation route | `ABSENT` | source uses `RepFun`, so pairing condition fails. |
| P2/P3 formation-use reentry | `NOT_SUPPLIED` | source has ordered formation, conditions and consumers. |

This is a focused pairing preflight, not a new full A–E denominator. It is complete only for the frozen code source plus its two declared reused controls.

## Reopen condition

Reopen only if a version-fixed source uses the **Power Set-subset** quotient route in the same \(A,R\) consumer task and supplies an independently checkable I/O/Done contract that is not already protected by explicit formation and congruence payment. An additional Isabelle quotient source using `RepFun`, or a generic quotation of the Power Set axiom, does not change this disposition.
