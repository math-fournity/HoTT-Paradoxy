# ZFC completion-observation 收束：新鲜机器证明闭包

> **身份：** `CONTRIBUTOR_CANDIDATE_NOT_CURRENT / FRESH_REPLAY_CLOSURE / NOT_A_ZFC_OBJECT_LANGUAGE_THEOREM`。

## 闭包目标

本报告只关闭这条收束诊断所依赖的**形式资产完整性**：当前工作树中的 Agda／Lean 源码、fresh run、负控制、source-manifest、冻结 Pattern-P 输入卡与 main source pin 是否一致。它不将这种完整性提升为“ZFC 已不一致”“P 已被共同体采用”或“原过程与模型过程已经同一”。

## 新鲜重放分母

| 组件 | fresh run | 结果 |
|---|---|---|
| 观察碰撞与 completion bridge 核 | `20261003-MP-ZFC-OBSERVATION-BOUNDARY-001-05` | Lean core `KERNEL_ACCEPTED_WITH_SCOPE`。 |
| 几何级数极限／有限阶段分离 | `20261003-MP-ZFC-GEOMETRIC-COMPLETION-001-05` | Mathlib Lean `KERNEL_ACCEPTED_WITH_DECLARED_AXIOMS_AND_SCOPE`。 |
| O1–O5/QProfile 条件政策 | `20261003-MP-ZFC-META-OBSERVATION-CONSISTENCY-001-04` | Lean core `KERNEL_ACCEPTED_WITH_SCOPE`。 |
| Q缺失／P采纳／A-B 的条件政策 | `20261004-MP-ZFC-COMMUNITY-OBSERVATION-POLICY-001-04` | Lean core `KERNEL_ACCEPTED_WITH_SCOPE`。 |
| IEP／截断／bare QuestioningDelay 来源状态 | `20261004-MP-ZFC-COMPLETION-SUBSTITUTION-PROFILE-001-04` | Lean core `KERNEL_ACCEPTED_WITH_SCOPE`。 |
| main HoTT `QuestioningDelay` | `20261004-CG001-QUESTIONING-DELAY-ZFC-CLOSURE-01` | Cubical Agda `KERNEL_ACCEPTED_WITH_SCOPE`。 |
| 其早停错误断言 | `20261004-CG001-QUESTIONING-DELAY-ZFC-CLOSURE-NEG-01` | Cubical Agda `KERNEL_REJECTED`，exit 42，`UnequalTerms`。 |
| main HoTT C-83 截断控制 | `20261004-CG001-TRUNCATION-QUESTIONING-ZFC-CLOSURE-01` | Cubical Agda `KERNEL_ACCEPTED_WITH_SCOPE`。 |
| 其“截断后仍沉默”错误断言 | `20261004-CG001-TRUNCATION-QUESTIONING-ZFC-CLOSURE-NEG-01` | Cubical Agda `KERNEL_REJECTED`，exit 42，`UnequalTerms`。 |

两组 Agda 主包均使用当前工作树、钉定 Agda 2.8.0 / cubical 0.9 release asset、`--safe --cubical --guardedness` 与多 include root。负控制表明该工具链没有仅仅接受文件：它实际拒绝了和主结论相反的指定 `refl` 断言。

## 机械闭包收据

运行：

```sh
python3 -B scripts/audit/verify_zfc_completion_observation_closure.py \
  --out audit/20261004-ZFC-COMPLETION-OBSERVATION-FORMAL-CLOSURE-RECEIPT-02.json
```

脚本逐一验证：

1. 每个 `RUN.json` 的 run id、proof id、状态和退出码；
2. stdout、stderr、environment、source-manifest 的字节数和 SHA-256；
3. source-manifest 中全部本地 source 文件的当前 hash；
4. main@`894e381` 的 README、社区稿 03 和 QuestioningDelay 两个 blob pin；
5. H100–H105 冻结 TaskCard/prompt 的 hash；
6. Lean core 包的 `#print axioms` 输出，及对 Mathlib 几何包保留其已声明经典依赖的边界。

PASS 只说明这套 contributor 闭包可重放、输入未漂移且同样的正负命题被保存。它不替代 canonical claim matrix 的集成工作。`...-RECEIPT.json`保留第一次通过验证的历史快照；`...-RECEIPT-02.json`绑定H106和profile `-04`后的当前闭包。

第一次验证曾正确发现 H100 的运行使用了格式化前的结尾字节、而 current TaskCard/prompt 已经被 Git whitespace 规范化。该失败收据作为历史保留；H106以当前字节重跑同一 source-match 问题，P 状态不变，新的 `...-03` Lean receipt绑定当前 TaskCard和capture script。于是本闭包不再以“语义相同”放过 source hash 漂移。
