# 当前工作记忆

> Owner：顶层 `AGENTS.md`、Feature/rulings 与 `.codex/cognition/PROTOCOL.md`。本文件只记录当前状态/队列，不复制三件套或历史长文。

## 当前执行队列（2026-09-12）

1. 用户新增项目级硬约束 F-011：当前 AI 的所有数学结论在交付前必须有匹配语义的机器证明；源码、实际 kernel run 和 claim/proof/run 索引必须留在 repo，`/tmp` 不能是唯一证据位置。
2. 当前数学主方向仍是 HoTT 自反真理验证/理论经济；下一最小研究结果 ERCF-1/2 只有在 `HoTT/formal/`、`HoTT/verification/runs/` 和 claim matrix 形成完整 proof package 后，才可作为数学结论交付。
3. C4 保持 `PAPER_ONLY`，新规则不追认或伪造历史证明；未来重用其命题时必须逐项形式化和重放。
4. C3 的资格保持性、W51×RP-B01、自指与 R041 partiality 对照继续在全局视野；同样受 F-011 约束。
5. 历史交接开放项仍为 2,396 条 claim、aistudio coverage、历史数学主张和 response→artifact/code/Git 因果；新门禁不批量重写历史状态。
6. 治理独立验证仍开放：fresh Session/真实压缩后模型是否实际遵循 proof Gate；static tests 不能替代行为验收。

## 当前已验证状态

- `核心认知.md` 为 generation-4/36 KC，SHA-256 `7548bd1716915319932a3e5b7ba4df8fc13c8f4812df6e3f7a933f70b354877b`；4 个登记来源、89 条消息、24 条纳入消息。generation-3 的 27/27 单元全部 `PRESERVED_EXACT`，新增 `KC-000028`–`KC-000036`。
- C4 经量词纠偏后共 733 行，SHA-256 `8a5a88d9f11569c6bde145ce1944eadf063bb24784732a41c56bf95f8cc15f7a`；它将验证任务分五层，提出 ERCF、任务相对 factorization、存在/不存在四分法、E₀/E₁ 与 Gödel/元层边界；状态仍为 `PAPER_ONLY`。纤维常值只无条件给出必要性，逆向需 quotient/image 泛性质、截面或选择；全局 no-go 需 separating observation family。
- 当前最强数学判断：某些 cubical HoTT 风格系统的有限判断可归一化/判定；足够强有效理论不能同时拥有同层内部、总停机、健全、完备的全局真理自验证。二者不矛盾。
- 理解章节 merge manifest 当前为 top-level 29、nested 24、union 29、same-name 24、identical 15、different 9、top-only 5、nonidentical 14、unresolved nontrivial 0。
- project-local governance 3.1 是未提交 candidate；最近已封存 tag 仍为 `governance-v3.0.0`。本轮未获 commit/tag/push 授权。
- S023 只完成 post-verification/EOF 格式收尾：core 7/7、runtime 28/28、reader 17/17、three-way 4/4、36-KC audit、merge/register/history/fresh/projection 均通过；不改变 C4 数学状态。
- S024 修正 C4 的 factorization 逆向与观察余域量词；ERCF 方向不变，数学状态不升级。
- S025 补齐 E₀ 的 `a₀:A`/`s₀≠s₁` 见证，并明确有限任务族不自动推出 factorization 可判定。
- F-011 proof-delivery Gate 已在根/`.codex` AGENTS、PROTOCOL、双 Skills、稳定规范、formal/run/index owner 中实现；4/4 正负向 static tests PASS。它只证明治理结构，不证明未来模型行为或任何数学命题。

## 当前证据上限

- 本轮 core/curation/transition、C4、方向/全景和治理机制可机器检查；C4 本身尚无 proof-assistant 证明或具体发散运行轨迹。
- 没有证明 HoTT 内部不一致、所有验证都会死循环、物理时空离散、Russell 标准悖论等价于无时序程序，或存在一个一致而 HoTT 完全无法保真解释的最小理论。
- 2LTT/QIIT/QIIRT/内部模型资料支持“自我元理论困难且常需分层/表示变化”，不自动证明 HoTT coverage failure。
- fresh Python 输入保真可验证；模型对三件套的实际理解仍不由工具认证。
- 数学结论若没有 repo 内匹配语义的 proof source、kernel run 和 claim index，只能保持 `QUESTION/CONJECTURE/HEURISTIC/PAPER_ONLY/COUNTEREXAMPLE_CANDIDATE/SOURCE_REPORTED_NOT_REPLAYED`。

## 恢复入口

按根 AGENTS 全文加载 core→direction→panorama。任何数学结论交付先执行 F-011，并读 `docs/quality/数学结论机器证明与证据留存规范.md`。当前问题先 query `A-HOTT-SELF-VALIDATION-ECONOMY-001` 并读 C4；进入机器证明时再读 C3、Theory Schema 和选定 proof assistant 接口。不要直接跳到 ERCF-3：先完成 ERCF-1/2 的正反对照。
