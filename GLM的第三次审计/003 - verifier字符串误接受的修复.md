<!-- governance-shard:v2
logical_id: GLM-HOTT-THIRD-COUNTER-AUDIT
shard_id: 003
index: ../GLM的第三次审计.md
-->

# verifier字符串误接受的修复

## 1. 根因

v3 的 `strip_agda_comments` 处理注释与 pragma，但**不识别 Agda 字符串字面量**
（`"…"`）与字符字面量（`'…'`）：字符串中出现的 `{-# OPTIONS --safe … #-}`
文本被原样保留，随后被 OPTIONS 正则提取，误计入 safe 资格。三审 holdout
（`StringLiteral.agda`）由本报告 002 片独立复现成立。

## 2. 修复（最小方向，采纳三审 005 §4 建议）

两层修复，均落到 `scripts/audit/verify_formal_proof_run.py`：

1. **文本剥离器补字面量处理**：在注释/pragma 状态机之外增加字符串与字符字面量
   状态（含转义 `\` 处理）：进入 `"` 后直至未转义的 `"` 才回到普通扫描；字符
   字面量同理（`'\''` 转义）。字面量内部一切文本（含假 pragma 形状）**不进入**
   pragma 提取输入。
2. **最终资格依据移交 Agda 实际执行**：对 theory_variant = cubical 的 run，
   校验器在重放时**实际追加 `--safe` 选项**执行一次 compile 检查——若源码含
   普通 postulate，Agda 将正确报 `SafeFlagPostulate` 拒绝。文本提取结果降级
   为「配置解释与冲突发现」，不再独自承担 safe 资格的最终依据（三审 005 §4
   的最小可靠方向）。新 run 合同（argv 含显式 `--safe`）作为独立证据单位登记，
   不改历史 argv。

## 3. 回归（六控制 + 一实收）

| 控制 | 期望 | 修复后 |
|---|---|---|
| SafePositive | PASS | 待实测 |
| UnsafeNegative | 拒 | 待实测 |
| CommentPragma | 拒 | 待实测 |
| LineComment | 拒 | 待实测 |
| Nested | 拒 | 待实测 |
| **StringLiteral（三审 holdout）** | **拒** | 待实测 |
| 实收 REAL-LAYER-03 | PASS | 待实测 |

（实测在修复提交后执行并如实回填。）

## 4. 边界

- 本修复不做完整 Agda 词法认证；字符串/字符/注释之外的结构（如 literate
  Agda 标记）超出当前输入范围，明确拒绝其支持。
- 修复不撤销任何既有收据的数学有效性；Astra 已如实指出 Agda 的 safe 机制
  本身工作正常，问题仅在项目校验器。
- 002 片 §4 的诚实边界升级为实现保证：凡文本扫描器不支持的输入，由第 2 层
  （Agda 实际执行）兜底。
