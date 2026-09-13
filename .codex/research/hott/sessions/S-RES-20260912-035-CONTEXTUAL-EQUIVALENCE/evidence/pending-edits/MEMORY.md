# 当前工作记忆

> Owner：顶层 `AGENTS.md`、Feature/rulings 与 `.codex/cognition/PROTOCOL.md`。本文件只记录当前状态/队列，不复制三件套或历史长文。

## 当前执行队列（2026-09-12）

1. `MP-CONTEXTUAL-EQUIV-001` 完成上下文等价层次：C-77–C-83 为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / REPRESENTATION_BOUNDARY`；`≡c` 精化结果等价且严格更细（时序/发散/值分离），结果等价严格粗于上下文等价；不是悖论。
2. 当前第一数学工作包转为一般商单子与更宽上下文语言：在 `Q(A)` 上用 canonical section 构造 `Q(A)×(A→Q(B))→Q(B)`（或给出精确选择/QIIT 边界），并评估更宽上下文族下的最粗等价。
3. C4 整体为 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_AND_NATIVE_TRUNCATION_DEFENSE_AND_PARTIALITY_BOUNDARY`；现实桥梁、natural consumer、自反/ERCF-3 和 HoTT 悖论仍未证明。
4. W51×RP-B01、自指、guard/在线因果和 R034 继续在全局视野；任何新数学结论仍逐 claim 执行 F-011。
5. 历史交接开放项仍为 2,396 条 claim、aistudio coverage、历史数学主张和 response→artifact/code/Git 因果；新门禁不批量重写历史状态。
6. 治理独立验证仍开放：fresh Session/真实压缩后模型是否实际遵循 proof Gate；static tests 不能替代行为验收。

## 当前已验证状态

- `核心认知.md` 为 generation-4/36 KC，SHA-256 `7548bd1716915319932a3e5b7ba4df8fc13c8f4812df6e3f7a933f70b354877b`；4 个登记来源、89 条消息、24 条纳入消息。generation-3 的 27/27 单元全部 `PRESERVED_EXACT`，新增 `KC-000028`–`KC-000036`。
- C4 当前共 773 行，SHA-256 `a1510b9335237bf5c94cbfc28ecc739921863419dc9ecd21a4902e1213e89fb1`；整体为 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_AND_NATIVE_TRUNCATION_DEFENSE`，明确区分两组机器子结果与现实/反射未决。
- 当前最强数学判断：某些 cubical HoTT 风格系统的有限判断可归一化/判定；足够强有效理论不能同时拥有同层内部、总停机、健全、完备的全局真理自验证。二者不矛盾。
- 理解章节 merge manifest 当前为 top-level 29、nested 24、union 29、same-name 24、identical 15、different 9、top-only 5、nonidentical 14、unresolved nontrivial 0。
- project-local governance 3.2 是未提交 candidate；最近已封存 tag 仍为 `governance-v3.0.0`。本轮未获 commit/tag/push 授权。
- S023 只完成 post-verification/EOF 格式收尾：core 7/7、runtime 28/28、reader 17/17、three-way 4/4、36-KC audit、merge/register/history/fresh/projection 均通过；不改变 C4 数学状态。
- S024 修正 C4 的 factorization 逆向与观察余域量词；ERCF 方向不变，数学状态不升级。
- S025 补齐 E₀ 的 `a₀:A`/`s₀≠s₁` 见证，并明确有限任务族不自动推出 factorization 可判定。
- F-011 proof-delivery Gate 已在根/`.codex` AGENTS、PROTOCOL、双 Skills、稳定规范、formal/run/index owner 中实现；4/4 正负向 static tests PASS。它只证明治理结构，不证明未来模型行为或任何数学命题。
- `MP-ERCF-001` 是 F-011 下首个真实数学 package：Lean 4.33.1 final run/index/hash/exact replay PASS；源码和运行原件均在 repo；未提交，且只证明一般 `Type` 值因子化。
- `MP-ERCF-TRUNC-001` 是首个原生 Cubical package：Agda 2.8.0/Cubical v0.9 final run、5 类外部依赖 hash、index row manifest 和 exact replay PASS；判词 `DEFENSE_WORKS`。
- `MP-RACE-TIMEOUT-001` 是第三个 F-011 package：原生 Cubical `SetQuotients`/`effective` 机器证明 `bind` 同余与商下降、`race`/`deadline` 非同余与商上无 race 选择子（C-71–C-76）；final run `20260912-MP-RACE-TIMEOUT-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `REPRESENTATION_BOUNDARY`。
- `MP-CONTEXTUAL-EQUIV-001` 是第四个 F-011 package：同一工具链机器证明上下文等价 `≡c` 精化结果等价且严格更细（C-77–C-83）；final run `20260912-MP-CONTEXTUAL-EQUIV-001-01`、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay PASS；判词 `REPRESENTATION_BOUNDARY`。
- S032 同步 F-011 record 的 formal/runs README hash；原生 proof task hydration 现在成功且 `review_required=[]`，数学状态不变。
- S033（接手会话）以新 Session 独立重放 `MP-ERCF-001`（`ROW_STABLE_AFTER_INDEX_EVOLUTION`）与 `MP-ERCF-TRUNC-001`（`EXACT_INDEX_SNAPSHOT_MATCH`），两者均 `KERNEL_ACCEPTED_WITH_SCOPE / EXACT_EXIT_STDOUT_STDERR_MATCH`；core 7/7、runtime 28/28、reader 17/17、three-way 4/4、F-011 4/4 与全部 verifier 复跑 PASS；上一 AI 状态声明在可机械复核范围内成立，数学与方向不变。
- S029 修复 `A-ERCF-FACTORIZATION-FORMAL-001` 的 task hydration：空 `stderr.txt` 仍原样保留并由 RUN.json/hash/verifier 认证，但不再被错误要求作为非空认知正文加载。
- S030 将 ERCF 的开放研究母题从 proof 的验证依赖改为 `research_parent`；A-ERCF task plan 现在可水合且不再把已闭合证明误列为 `review_required`。
- S026 checkpoint 已把门禁写入 direction v1.4、panorama v1.4 和 STATE stable record；S027 仅完成 current version/verification alignment。

## 当前证据上限

- C4 的通用 factorization 子核和原生 truncation defense 分别有 Lean/Cubical Agda proof package；截断结果是理论防御，不是现实失配。C4 的 partiality natural consumer、自反与具体发散仍无机器证明/运行轨迹。
- 没有证明 HoTT 内部不一致、所有验证都会死循环、物理时空离散、Russell 标准悖论等价于无时序程序，或存在一个一致而 HoTT 完全无法保真解释的最小理论。
- 2LTT/QIIT/QIIRT/内部模型资料支持“自我元理论困难且常需分层/表示变化”，不自动证明 HoTT coverage failure。
- fresh Python 输入保真可验证；模型对三件套的实际理解仍不由工具认证。
- 数学结论若没有 repo 内匹配语义的 proof source、kernel run 和 claim index，只能保持 `QUESTION/CONJECTURE/HEURISTIC/PAPER_ONLY/COUNTEREXAMPLE_CANDIDATE/SOURCE_REPORTED_NOT_REPLAYED`。

## 恢复入口

按根 AGENTS 全文加载 core→direction→panorama。任何数学结论交付先执行 F-011，并读 `docs/quality/数学结论机器证明与证据留存规范.md`。当前问题先 query `A-HOTT-SELF-VALIDATION-ECONOMY-001`、`A-ERCF-FACTORIZATION-FORMAL-001`、`A-ERCF-TRUNCATION-DEFENSE-001`、`A-RACE-TIMEOUT-FORMAL-001`、`A-CONTEXTUAL-EQUIV-FORMAL-001`。truncation 与 partiality 三个原生 Gate 已分别闭合为防御与表示边界；下一步做一般商单子与更宽上下文语言评估，不直接跳 ERCF-3。
