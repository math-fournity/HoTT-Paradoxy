# `ZFC+Q_norm` 逻辑核：C-359／C-361／C-362／C-364 实际重放收据

> **身份：** `FORMAL_CONTROL_REPLAY_RECEIPT / NOT_A_NEW_CORE_THEOREM`。
>
> **消费者：** [normative process-audit extension admission](20261005-ZFC-META-SUBTHEORY-ADEQUACY-NORMATIVE-PROCESS-AUDIT-EXTENSION-ADMISSION.md)。

本收据记录本轮实际执行的 project verifier。它不替代各 proof package 的保存 `RUN.json`，也不把 source-bound controls升级为 bare-ZFC theorem。

| Claim | exact command target | 结果 | 精确范围 |
|---|---|---|---|
| C-359 | `20261004-MP-ZFC-ACTUAL-Q-POLICY-001-07` | `PASS_WITH_SCOPE`; kernel accepted; exact stdout/stderr replay | `QMissing ∧ SameFullQ ∧ P ∧ B → False` 的条件性 `ZFCOneUse` policy calculus。 |
| C-361 | `20261004-MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001-08` | `PASS_WITH_SCOPE`; kernel accepted; exact replay | geometric limit 与 finite Nat-stage endpoint区分；closed continuous-time endpoint正控制。 |
| C-362 | `20261004-MP-ZFC-ACTUAL-Q-SOURCE-CONTRACT-001-01` | `PASS_WITH_SCOPE`; kernel accepted; exact replay | source-certified revised completion没有 strict original bridge。 |
| C-364 | `20261004-MP-BARE-ZFC-Q-PRECISION-001-03` | `PASS_WITH_SCOPE`; kernel accepted; exact replay | fixed coarse resolution view不能决定 `OriginDone`；rich view / code为正控制。 |

执行命令均为：

```text
python3 -B scripts/audit/verify_formal_proof_run.py --run-dir <above-run-dir> --rerun
```

每个 verifier 同时报告：`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`、`ROW_STABLE_AFTER_INDEX_EVOLUTION`、`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。最后一项是当前工作树的事务身份说明，不改变对应 proof package 的已保存原始 run；它也不构成本轮新增 C6 package。

## 禁止外推

- C-359 仍需 actual `SameFullQ`、actual P 与 HoTT B mapping，不能推出 bare ZFC contradiction；
- C-361 不能推出连续运动无法到达；
- C-362 不能证明来源史或 ZFC 定理本身；
- C-364 不是 ZFC syntax/model formalization；
- 四项合在一起仅覆盖 `ZFC+Q_norm` 的逻辑控制核，不能替代 C6 actual source-to-spec admission。
