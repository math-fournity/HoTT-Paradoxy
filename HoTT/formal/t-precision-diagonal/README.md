# T-PRECISION T-DIAG 的条件性逻辑核

本目录只保存 `T-DIAG-001` 的 Lean-core logical kernel。它把“真正的自编码固定点”“接受接口”“原过程完成”和“completion bridge”作为明确字段，而不替任何现实过程、ZFC source 或 proof checker 自动填入这些字段。

主文件 `AcceptanceDiagonal.lean` 应通过 Lean kernel；`WrongAcceptanceDiagonal.lean` 必须被拒绝。命题和禁止外推以 `CLAIM.md` 为准。
