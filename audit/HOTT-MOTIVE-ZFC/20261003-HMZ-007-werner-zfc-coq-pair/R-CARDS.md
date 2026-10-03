# HMZ-007：R-Cards — WoLLIC 的机器基础动机

## HMZ-R-014 — ZFC-based proof-assistant formalization 的“不自然构造”

```text
source identity:
  HMZ-S-021, Voevodsky 2011 WoLLIC, slide 2.
claim class:
  CONTRASTIVE_CRITIQUE + CAPABILITY_GOAL + HISTORICAL_CONTEXT.
literal minimum:
  “Multiple attempts” to use ZFC as the basis of proof-assistant formalization
  “all led to very unnatural constructions.”
what the source does not say:
  no names of attempts; no source code; no definition of naturality; no ZFC
  inconsistency; no claim that every ZFC encoding has a P-shaped Q.
candidate Z pairing:
  Werner 1997 / rocq-archive-zfc is a source-grounded comparable implementation,
  but Voevodsky does not identify it.  Pairing status is NOT_ATTRIBUTED.
```

**反投影意义。** 这给出了一个可考察的任务：ZFC 作为 proof-assistant formalization 的基础是否需要不自然的
construction。但“自然／不自然”本身不是完成条件。要形成 Z-card，必须由具体实现固定 `Ens`、formation、proof
consumer、axiom payment 与实际 Done；否则它只是作者修辞。
