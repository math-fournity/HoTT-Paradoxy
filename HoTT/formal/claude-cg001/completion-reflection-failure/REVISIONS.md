# C-358 修订与负控制谱系

## 2026-10-04：负控制的 scope failure

`20261003-CG001-ZFC-HOTT-COMPLETION-REFLECTION-NEG-01` 在
`WrongCompletionReflection.agda` 中报告 `NotInScope just`。这是测试文件漏导入
`Cubical.Data.Maybe.just`，尚未检查伪造的 original-halt witness，不能被解释为
`C-358` 的正确负控制。

后继文件只加入该构造子的最小导入，并使用新 run ID `...NEG-02`。预期且所需的
拒绝位置是 `runFor 0 (Questioning.Q Type judgeU) ≡ just 1`，即 `nothing != just 1`。
