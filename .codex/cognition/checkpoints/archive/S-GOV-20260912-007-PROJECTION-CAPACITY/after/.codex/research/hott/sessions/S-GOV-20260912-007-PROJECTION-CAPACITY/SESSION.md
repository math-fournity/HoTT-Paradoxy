# 投影动态依赖容量修复 Session

- session_id: `S-GOV-20260912-007-PROJECTION-CAPACITY`
- scope: 修复成果投影把四个原始 ledger 作为每轮 `full_sources` 的上下文容量问题，并重新验证三件套
- authorization: 用户已授权本地治理框架升级；不修改外部 WebGPT/LocalGPT repo、不恢复已移走目录、不开展数学研究
- mathematical_status: `UNCHANGED_FROM_R039`
- cognition_status: `BOUNDED_PROJECTION_DEPENDENCY_REPAIR_WITH_FULL_KC_AUDIT`

## 发现

revision 6 的 runtime plan 因 `I-OUTCOME-PANORAMA-20260912` 全文依赖四个原始 ledger，规模上升到约 22.6MB。原始事件是重要证据，但不是每个新 Session 都需要无差别全文载入；强制加载它们会破坏“任务相对最小充分闭包”，并可能令三件套自身无法真正进入上下文。

## 修复

将成果 projection 的动态 `full_sources` 收敛为 `方向追踪.md`、source manifest、WebGPT STATE、LocalGPT claim matrix 以及 audit 的 summary/coverage/verification 文件。四个原始 ledger 仍保留在 `audit/`，由全景条目和 result owner 按需回源；没有删除或覆盖任何原始事件。

## 三方判定

- `core_change`: `NO`；generation-1 和 core SHA 未变。
- `direction_change`: `NO_SEMANTIC_CHANGE`；仅同步 projection revision。
- `panorama_change`: `YES`；更新其动态依赖边界，结果内容不冒充原始 ledger。
- `update_decision`: `UPDATE_PANORAMA_DEPENDENCY_SCOPE; KEEP_CORE_AND_DIRECTION_SEMANTICS`
- `cross_conflicts`: WebGPT README revision40 vs STATE/MEMORY revision41；WebGPT Skill manifest 1.3.3 vs actual 1.3.4；LocalGPT live dirty vs snapshot。
- `unresolved`: full semantic mapping、understanding merge、fresh/compaction 行为、core generation-2。

## 结果边界

本 Session 证明的是动态依赖范围被收敛并有理由保留按需原始证据；不证明模型理解、全量语义闭合或任何新数学结果。
