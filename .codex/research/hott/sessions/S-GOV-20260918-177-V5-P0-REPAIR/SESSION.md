# S-GOV-20260918-177-V5-P0-REPAIR

身份：治理框架 v5 迁移的 **P0 修复单元**（用户 2026-09-18 晚指令"全部执行完成"授权
011 清单 P0–P3；本会话 = ZCode，host=zcode-desktop）。本单元执行 v5 检查清单 P0-1～P0-5。

## 本单元做了什么

1. **P0-1 漂移处置（本节）**：S170–S176 七轮会话以直接 git commit 绕过 checkpoint
   事务（RESUME.md 提交 `4065616` 等），导致 `HEAD.json` 停在 revision 169、
   `plan` 被 `UNCOMMITTED_STATE` fail-closed。处置遵循合同"历史缺收据只登记、
   禁止追溯伪造"：新增治理记录 `G-V5-RECEIPT-GAP-S170-S176`（CHECKPOINT_RECEIPT_MISSING
   登记，非伪造事务）；STATE revision 169→170；latest_session 指向本修复会话；
   `HEAD.json.tracked` 对全部 32 个被跟踪文件按当前工作区重算。备份：
   `.codex/cognition/backups-v5/{STATE,HEAD}.pre-v5-p0.json`。
2. **P0-2 根 AGENTS 指针化**：generation-4/36、curation-v4 字面量改为纯动态指针
   （"不得内嵌具体代数/分母数字"入文）。
3. **P0-3 过期代数清扫**：README/001、本地治理 SOP 两处、扩展认知 marker
   baseline → generation-7。
4. **P0-4 修订片索引补 030 行**：banner 29→30、last_shard→030（修复 validator
   orphan FAIL）。
5. **P0-5 精确提交**：三份报告目录 + 本方案目录 + dev-notes 0032–0047 + 上述修复。

## 本单元不是什么

- 不是数学研究单元：零数学主张，registers_new_claim:false，不进 CLAIM_EVIDENCE_MATRIX。
- 不是伪造收据：S170–176 的缺口以 `CHECKPOINT_RECEIPT_MISSING` 登记永久保留；
  本修复本身是 out-of-band 登记（沿 revision 160→161 修复先例），其真实性由
  RUNS.json 的 plan/validator 实际输出与 git 历史背书。
- 不改变四件套、核心认知、任何证明/运行证据。

## 验证（详见 RUNS.json）

`plan --profile governance` 恢复可运行（UNCOMMITTED_STATE 解除）；
`verify_governance_shards.py` FAIL 3→2（030 orphan 已修，余 2 为已登记 checkpoint
after/ 已知缺口）；治理正文过期代数 grep 清零。
