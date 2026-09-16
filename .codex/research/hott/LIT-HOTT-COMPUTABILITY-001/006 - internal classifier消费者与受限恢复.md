<!-- governance-shard:v2
logical_id: LIT-HOTT-COMPUTABILITY-001
shard_id: 006
index: ../LIT-HOTT-COMPUTABILITY-001.md
-->

# internal classifier消费者与受限恢复

## LOPS：普通 internal classifier no-go 与 crisp 恢复

LOPS 2018 的真实消费者是 fibration universe classifier，用于内部构造 CCHM 类模型、univalent universe、HIT 与 directed/cubical type theory。官方 Cambridge source 13 files / 44,374 bytes 已在 clean Agda-flat 2.6.0.1-70899fb 整包重放（C-233–C-238）。

普通 `IntUniv.code` 可应用于依赖 local `i : I` 的 pointwise fibration，因而把 fiberwise fibrancy提升为 family fibrancy；对 `P i = (O ≡ i)` 得到 interval collapse。crisp Theorem 5.2 改为只接收 global/crisp base 和 fibration，在 tiny/right-adjoint 显式假设下仍构造 `U/El/code/Elcode/codeEl`。modal control 验证：crisp argument 通过，local argument 被拒为 `Variable x is declared top`。

## Boulier–Tabareau：degenerate replacement 加 transport

`InternalCubical-Coq emptyctx@28a2568` 的 20 文件 subtree 未发现 license，故以外部 archive/tree 固定。Coq 8.13.2 重放 C-239–C-243：

- 对任意 open family 假定 `RFib (repl ∘ P)` 会导出 `False`；assumptions 明列 `RFib_repl`；
- actual QIT `repl` 只证明 `Fib_repl : DFib repl`；
- `RFib → DFib`、`RFib → Trans`、`DFib + Trans → RFib`；
- replacement eliminator只接受 `RFib` motive；路径 J 另依赖 `extension_rule__emptyctx`。

论文的 model-structure/HIT 消费者因此不是无条件获得 regular family replacement，而是自由补 degenerate composition、再保留输入 family 的 transport。完整 `Model_structure.v` 在 Coq 8.13.2 的旧 implicit placeholder 失败；作者 history 目标为 8.10，本轮不冒充完整 replay。

## Swan–Uemura 与 Reedy 对照

Swan–Uemura 的 `LFR(A)` 被用于 suspension、propositional truncation与后续 HIT；它自由加入 homogeneous composition，再与 transport结合成 Kan composition。2LTT Reedy fibrant replacement只接受 pointwise fibrant diagrams，并明确拒绝 arbitrary outer diagrams。

## 当前判词与下一步

`NATURAL-CONSUMER-002` 已找到 natural consumer，但成功接口能完成真实的 global/qualified task；只有把输入域扩为 local/open family 时才坍缩。因此当前判词为：

```text
NATURAL_CONSUMER_FOUND
/ QUALIFICATION_SCOPE_WIDENING_CAUSES_COLLAPSE
/ RESTRICTED_INTERFACE_COMPLETES_REAL_TASK
/ DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT
/ NOT_A_BASIC_HOTT_BUG
```

下一工作单元转 `CE-MAP-001`，把 global→local、fiberwise→familywise、DFib+Trans、crisp rejection 归入统一 class，并寻找尚未被现有 defense 覆盖的 HoTT-specific cells。完整审计见 `audit/2LTT纤维替换自然消费者与crisp退化纤维性消融-20260915.md`。
