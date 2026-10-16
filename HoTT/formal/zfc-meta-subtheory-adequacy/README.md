# ZFC 元理论—子理论充分性：C6A 内核包

该目录保存 `MP-ZFC-META-SUBTHEORY-ADEQUACY-001` 的唯一 Lean 源码与来源范围说明。

它形式化的是一个来源认证的 application-adequacy contract：当一个数学模型的应用宣称原 physical target 已解决、而这个应用按固定 criterion 需要 bridge，却同时没有 bridge 和 explicit task switch 时，该**application case**被判为 `ApplicationAdequacyFailure`。

它不形式化 bare ZFC 的语法或模型，不证明 ZFC 矛盾，不证明任何物理运动结论，也不把 HoTT H0 并入定理；这些边界由 [CLAIM.md](CLAIM.md) 和相应 source cards 固定。

正运行收据位于 `HoTT/verification/runs/20261005-MP-ZFC-META-SUBTHEORY-ADEQUACY-001-04/`；负控制独立保存于同日期的 `NEG-001` run。
