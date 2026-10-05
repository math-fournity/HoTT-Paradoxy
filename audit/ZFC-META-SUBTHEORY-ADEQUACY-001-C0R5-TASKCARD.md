# CoreAdequacyTaskCard — C0R5：SOP总完成门与版本闭合审计

> **状态：** `GATES_1_TO_6_AND_8_PASS_WITH_SCOPE / GATE_7_GIT_VERSION_CLOSURE_PENDING`。
>
> **父合同：** SOP 004、C6D及所有C0–C6 source/run artifacts。

## 1. 问题

```text
Have all eight total-completion gates actually been satisfied, including
candidate-family exhaustion, actual source-to-spec contract, controls,
H0 exclusion, successor scans, and a clean committed version closure?
```

## 2. 禁止捷径

- C6D source/Lean consequence不能自行支付Git version closure；
- candidate count为零不能替代actual contract；
- `CORE_ADEQUACY_FAILURE_WITH_SCOPE`不能被写成bare ZFC object-language theorem；
- worktree dirty、untrackedreceipt或未更新owner时，Gate 7失败且Goal继续。

## 3. 停止与后继

只有八门通过后才可以commit/push、标记Goal完成。若任何门失败，写明确未通过字段和下一C-id；不得因为已产生核心候选结论而提前停止。

**当前审计结果。** [C0R5 total audit](ZFC-META-SUBTHEORY-ADEQUACY-001-C0R5-TOTAL-GATE-AUDIT.md)确认Gate 1–6与8已通过；Gate 7仅待精确commit、C-370/C-371版本闭合、clean branch和owner回读。此时仍不得标Goal完成。
