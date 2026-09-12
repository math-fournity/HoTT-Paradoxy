# 形式化核心

本目录只机器检查审计报告中明确、窄化后的数学命题；不把解释性标题当成形式定理。

## 文件

- `self-contained/ZCore.agda`：表示因子化的必要条件、无免费富化、来源/方向有限反例、语境欠定和两个条件性固定点引理。
- `agda-unimath/hott-z/NoCanonicalPoint.agda`：对锁定 `agda-unimath` 定理的薄包装；名称刻意写成“无规范点”，不冒充完整时间序定理。
- `lean/TwoEvent.lean`：二元素交换与方向丢失的独立有限模型。
- `build.sh`：校验关键上游文件哈希后运行 Agda，并在 Lean 可用时运行第二实现。

## 锁定环境

- Agda：2.8.0。
- `agda-unimath` commit：`88cfce0ce195ae3b64a9e73e8ec744ae64b4006b`。
- 上游归档 SHA-256：`50ed8718a56820049eebf5ad86b619774ec0c23a9c5b3ca4a4447b3e70a785a6`。
- `2-element-types.lagda.md` SHA-256：`72f9ad29b6c24b84e1e06f10f701895783e7a56cfaedc1dc0d295dba3629c82e`。
- `agda-unimath.agda-lib` SHA-256：`d42bd31babacf7fced8aab84f499d9004a1cac5c3219dc7b360c56c23e9b6221`。

## 运行

```bash
AGDA=/path/to/agda \
AGDA_UNIMATH_ROOT=/path/to/agda-unimath-at-pinned-commit \
bash HoTT/formal/build.sh
```

不得把成功编译解释成以下命题：`HoTT ⊢ ⊥`、HoTT 无法编码时间、所有 HoTT 箭头均可逆，或
HoTT 作为数学基础已被推翻。机器证书的精确边界见 `../CLAIM_EVIDENCE_MATRIX.md`。
