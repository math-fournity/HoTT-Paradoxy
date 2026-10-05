# CoreAdequacyTaskCard — C0R5：SOP总完成门与版本闭合审计

> **状态：** `TOTAL_GATES_1_TO_8_PASS_WITH_SCOPE / SELECTED_PROOF_VERSION_CLOSED / GOAL_COMPLETION_ELIGIBLE_WITH_SCOPE`。
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

八门现已通过。本卡不把这件事扩大为bare ZFC对象语言结论：它只关闭用户固定`OriginDone`、IEP ZFC-founded Standard Solution和本项目application adequacy criterion组成的冻结合同。随后可按既有授权提交并推送候选分支；若任何新证据满足C5D/C5E或H0的reopen条件，必须新开C-id而非改写本卡。

**最终审计结果。** [C0R5 total audit](ZFC-META-SUBTHEORY-ADEQUACY-001-C0R5-TOTAL-GATE-AUDIT.md)确认Gate 1–8已通过，其中Gate 7由`1f2145c0…`、`accde430…`以及C-369/C-370/C-371的`HEAD_BYTES_CHECKED`关闭。
