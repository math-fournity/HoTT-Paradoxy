# S-GOV-20260913-125-ROUND2-AUDIT-REPAIR-TAKEOVER

- 用户目标：接手被第二轮审计的 AI 工作线；以 `audit/imports/audit-absorption-round2-20260913/独立审计吸收-第二轮审计-20260913.md` 为整改基线。
- 接管基线：`0dd4596f38343562334e499bca6eed1ab065066b`；接管前 tracked tree clean，两个既有未跟踪 dev-notes 原样保留；未发现仍操作该根的进程。
- R2-1/R2-2：CURRENT 方向、全景、STATE、MEMORY、FRONTIER、LESSONS、RESUME 与 formal/run 入口原位收敛；历史 session/run/matrix rows 不改写。
- R2-3：proof closure v2 交叉核验 registry/RUN/source/row/matrix、claim 完整集合、唯一 ID 与 command/source/tool。
- R2-4：六条历史依赖例外绑定精确 run 与哈希；同 proof 新 run 不继承。
- R2-5：replay 先登记关系再 mark/freeze；primary 矩阵行不覆盖。
- 验证：`python3 -B -m unittest scripts.audit.test_proof_evidence_links` = 9/9 PASS；canonical verifier 在 checkpoint 后复跑。
- 数学边界：无新 claim；C-184–C-187 不重证、不扩大；ERCF-3 保持 `GATED`。
- Git：本轮不 push、不打 tag；是否本地提交由接管收尾的精确 Git 状态决定。
