# HMZ-009：预检覆盖与配对条件

## 本预检已读范围

| 事项 | 状态 | 证据 |
|---|---|---|
| HoTT Book source identity、three-file hash和上游 commit | `ARCHIVED_AND_HASHED` | `SOURCE-CATALOG.md`。 |
| Book 的 Power Set/resizing 段 | `READ` | `logic.tex:525–555`。 |
| Book 的 set-theoretic quotient / \(A\sslash R\) / universe 段 | `READ` | `hits.tex:1257–1297`、`setmath.tex:363–455`。 |
| Book 的 external/internal quotient control与内部 \(V\) control | `READ` | `setmath.tex:487–499,1755–1761`。 |
| 复用 ZF/ZFC Power Set、Separation formation sources | `READ_REUSED` | HMZ-001 的 `HMZ-S-007`、`HMZ-S-010`。 |
| 独立的 ZFC actual quotient consumer | `NOT_IN_DENOMINATOR` | 没有 source-defined `C/I/O/Done`。 |
| P2/P3 reentry/admission evidence | `NOT_SUPPLIED` | 以上来源均无该结构。 |

## 分母与 remainder

本次是单一 technical source 加两个既有 formation controls 的预检，不是 A–E 完整 run。它的范围是判断 Book 是否把 `R-HIGHER`／`R-SET-CONTROL` 接到 Power Set 的 quotient construction，而不是调查所有 quotient、所有 set theory 文献或所有 HoTT motivation。

```text
included source identities: 3 (1 new archival source, 2 reused controls)
unavailable: 0 within frozen scope
unread inside frozen Book locators: 0
actual-consumer remainder: 1 category, deliberately open
preflight outcome: PAIRING_SOURCE_REQUIRED
```

## 下一配对来源的最低门槛

新的来源只有同时满足以下项才可将本预检升级为完整 successor run：

1. 它以精确的 ZFC／ZF／NBG／具体 formalization 或明确数学实践层声明自己所处理论；
2. 固定同一 \(A,R\) quotient-like task，而不是只谈 class、HIT 或 Power Set；
3. 写出 consumer 的输入、operation、observation、Done；
4. 允许判断 Power Set / Separation / choice of representation / universe 与其它 payment 是否明示；
5. 至少提供 P1 的 actual-consumer entrance，或一个可审 P2/P3 formation-use/interleaving 线索。
