# CoreAdequacyTaskCard — C1B4：set.mm 的 M→S 与 theorem-dependency card

> **状态：** `LOCAL_LEAF_CLOSED / M_TO_S_SOURCE_AUDIT / NOT_A_CORE_VERDICT`。
>
> **父合同：** F-B / C0B4；冻结 `set.mm@160ebb…`、其 source comments、同一database verifier receipt和公开 Proof Explorer source pages。

## 1. 问题

```text
What exact foundation relation supports df-sum / df-rlim / geoihalfsum in the
fixed set.mm database, and which parts are ZF, ZFC, or database-level only?
```

## 2. 必须支付

- exact database identity和 `geoihalfsum` theorem identity；
- source-level dependency / axiom scope sufficient to call this an M→S edge;
- distinction between object-level convergence theorem and verifier acceptance;
- prohibited conclusion: exact P/Bridge or physical motion result.

## 3. 最强反证与停止

若该 theorem只从未冻结的extension、unverified mathbox或非ZFC object layer得来，降为`NOT_ADMISSIBLE_M_TO_S`。若其 M→S identity支付，建立C1B4结果并自动转C2B4；无论如何不停止 Goal。

**实际结论。** [C1B4 card](ZFC-META-SUBTHEORY-ADEQUACY-001-C1B4-SETMM-M-TO-S-AND-DEPENDENCY.md)以本轮full-database replay和`geoihalfsum` traceback确认：固定 theorem 的对象层依赖包含`ax-rep`、`ax-pow`、`ax-un`、`ax-inf2`等ZF-side labels，而显示的trace不列`ax-ac`；故它可作为 ZF（从而 ZFC-founded）M→S edge，而非proof-checker acceptance。下一C2B4仅审它与C2C dense `FormalDone`的数学保真，不能跳到physical P。
