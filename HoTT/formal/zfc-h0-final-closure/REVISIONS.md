# M1-A 修订记录

## 2026-10-04：trace 的点态来源更正

最初草稿把 `universeQuestioningNeverAnswers` 用作 `funExt` 的点态输入。Cubical Agda 拒绝该项：前者的类型是 `¬ Questioning.Halts`，不是逐 fuel 的 `runFor … ≡ nothing`。

修正为导入同一 fixed H0 包已经给出的

```text
universeQuestioningRunsNothing :
  (judge : Judge (Type ℓ-zero)) (n : ℕ) →
  runFor n (question (Type ℓ-zero) judge) ≡ nothing
```

此修正没有弱化命题；它把 trace projection 的证明直接接到 C-78 的正确 pointwise theorem。主运行和负控制均在修正后重新捕获。

## 2026-10-04：canonical 运行收据升级

最初的 `-001-01` 和 `-NEG-001-01` 已完整编译并保留，但它们的 source manifest 使用了旧的 external-dependency 字段，不能通过当前通用 `verify_formal_proof_run.py`。不改写历史收据；修复 capture schema 后重放为 `-001-02` 和 `-NEG-001-02`，其中 binary 与 cubical extracted tree 都按通用 verifier 的字段完整登记。随后，索引前更正了 `CLAIM.md` 的 canonical run locator；为使 manifest 与所有当前 proof inputs（含总SOP）相符，最终 canonical recapture 使用 `-001-05` 和 `-NEG-001-05`。`-03`作为同一 source identity 的已验证 replay、`-04`作为总SOP更新前的主运行留存。
