# HMZ-019：classical realizability 的 ZF program correspondence 预检

> **身份：** `SOURCE_PREFLIGHT / P5_MODEL_SEMANTIC_COUNTERCONTROL / FULL_RUN_ADMISSION / NOT_A_BARE_ZFC_PROGRAM_CLAIM`。

## 预检问题

Krivine 的 classical realizability 是否提供一个真实的 ZF-level proof–program correspondence，从而改变 HMZ-018 对 P5 的处置？若提供，其 terms/realizers 是否就是普通 ZFC 存在证明交付给普通 ZFC consumer 的对象，还是一个具有 realizability algebra、`ZFε`、ground model和非二值 truth values的专门模型语义？

## 冻结来源

| ID | 类 | 来源 | 原件／哈希 | 实读范围 |
|---|---|---|---|---|
| `HMZ-S-032` | C/D/E | Jean-Louis Krivine, *Realizability algebras II: new models of ZF + DC*, 2010, updated 2013. | `originals/HMZ-S-032-Krivine-2013-Realizability-Algebras-II.pdf`; SHA-256 `3b64e06d838b99461d7b0c76f4bf8ddd04498958844aef832b29ff90cb5cc3d7`. | pp. 1–2, 4–8, 10–12. |

Public source: <https://www.irif.fr/~krivine/articles/R_ZF.pdf>. It is a classical-realizability/model source, not a statement that every ordinary ZFC proof environment automatically extracts a conventional program.

## Source facts

```text
proof-program claim:
  classical realizability extends proof-program correspondence to mathematical
  proofs with excluded middle, axioms of ZF, dependent choice, etc.
payment/context:
  standard realizability algebra, combinatory terms/stacks/processes, call/cc,
  ZFε, ground model M of ZFC, and realizability model N.
truth/model boundary:
  N has the same individuals as M but is not a usual model; truth values are
  subsets of stacks rather than 0/1.
axiom realization:
  ZFε axioms are realized by proof-like c-terms; ZF follows via conservative
  extension/translation in the stated framework.
```

## Preflight disposition

```text
ZF-related proof/program semantic contract: SOURCE-REPORTED
bare-ZFC proof-to-standard-program contract: NOT ESTABLISHED
same theory / same consumer / same Done with user-P: NOT ESTABLISHED
P5 preemptive use of unpaid u: NOT SUPPLIED
new source alters P5 source map: YES
SUCCESSOR RUN: FULL_RUN_ADMISSION
```

[HMZ-020](../20261003-HMZ-020-classical-realizability-p5-comparison/MANIFEST.md) has now completed that comparison. It confirms a strong ZF-related program-semantic control while leaving `P5_PREEMPTIVE_USE_NOT_ESTABLISHED`; model realization, proof term, executable program and ordinary mathematical-object delivery remain distinct.
