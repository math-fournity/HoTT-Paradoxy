<!-- governance-shard:v2
logical_id: GLM-HOTT-SECOND-COUNTER-AUDIT
shard_id: 002
index: ../GLM的第二次审计.md
-->

# A09 残留的完整修复：verifier v3

## 1. 缺陷复现（Astra 二审 003 片受控反例）

verifier v2 的正则 `\{-#\s*OPTIONS([^#]*?)#-\}` 不区分有效 pragma 与注释中的
同形文本。CommentPragma.agda：

```agda
{-# OPTIONS --cubical #-}
{-
{-# OPTIONS --safe --cubical #-}
-}
module CommentPragma where
postulate witness : Set
```

块注释内的假 `--safe` 被计入 token 集 → 误授予 safe 资格。本作者以 verifier
实际正则复跑该文本确认（token 集含 `--safe`）——**Astra 反例完全成立**。
v2 的修复语义（「OPTIONS pragma 实际解析」）是过强表述，本作者在第一次报告
中的该句措辞随之修正。

## 2. v3 设计：注释剥离 → pragma 提取 → token 匹配

`verify_formal_proof_run.py` 新增 `strip_agda_comments`（Agda 词法的最小正确
子集，满足本检查需要）：

1. **块注释**：深度计数嵌套 `{- … -}`（Agda 块注释可嵌套）；深度>0 时内部
   一切为注释文本（含嵌套 `{-#` 形状）；
2. **pragma**：`{-#` 开头的段整体**保真拷贝**至 `#-}`（其内的 `--flag` 不进
   入注释分支——这是 v3 开发中踩到并修正的自嵌坑：`{-#` 以 `{-` 开头，若先
   判块注释会把 pragma 本身吃掉，导致全部 safe 收据 FAIL）；
3. **行注释**：深度 0 且非 pragma 位置遇 `--` 跳至行尾；
4. 剥离后文本上跑原正则提取 OPTIONS 内容，token 精确匹配（`--safe` 须为
   独立 token）。

## 3. 回归结果（五控制 + 三真实收据）

| 控制 | 期望 | 实测 |
|---|---|---|
| SafePositive（真 safe pragma + 数据声明） | safe 资格 ✓ | ✓（token: --safe --cubical） |
| UnsafeNegative（无 safe + postulate） | 拒 | ✓（仅 --cubical） |
| **CommentPragma（二审反例）** | **拒** | ✓（假 pragma 被剥离，仅 --cubical） |
| LineComment（行注释内假 pragma） | 拒 | ✓ |
| Nested（嵌套块注释内假 pragma） | 拒 | ✓ |
| TA-01（真实公设控制收据） | FAIL（正确分类） | ✓ FAIL |
| REAL-LAYER-03 / M3-UNC-01（真实 safe 收据） | PASS | ✓ PASS |

## 4. 边界（如实登记，采纳二审 003 §5 最小合同的 1/4）

- 本实现是**本检查所需的最小词法正确子集**，不是完整 Agda 词法（字符串/字符
  字面量中的 `--`、`{-` 未特殊处理——OPTIONS pragma 区内不含字面量，本检查
  只消费 pragma 区）；回归 PASS 只关闭五控制覆盖范围；
- 二审最小合同其余三项（正式 safe 证明让 Agda 在规定选项下实际检查的新运行
  合同、公设控制的独立分类 schema、执行配置/依赖闭包的实际核对）**未做**，
  与 R2/R3/可移植包一并列 005 片；
- 首版 v3 开发中自嵌 bug（pragma 被块注释分支吞掉 → 全部 FAIL）被本作者自己
  的回归测试当场捕获并修正——这正是五控制回归的价值。
