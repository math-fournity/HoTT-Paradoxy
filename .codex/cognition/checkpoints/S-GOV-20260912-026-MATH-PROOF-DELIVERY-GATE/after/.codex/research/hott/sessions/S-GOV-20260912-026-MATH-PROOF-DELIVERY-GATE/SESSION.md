# S-GOV-20260912-026-MATH-PROOF-DELIVERY-GATE

- 触发：用户要求把“所有当前 AI 数学结论交付前必须机器证明，证明代码和结果必须留在项目并索引，不得只放 `/tmp`”写入项目 AGENTS。
- 决策：F-011 为 accepted project requirement；core 不变，因为这是一般治理裁定而非新的悖论/元数学正文。
- 实现：根/`.codex` AGENTS、PROTOCOL 2.2、治理 Skill 3.2、业务 Skill 1.7、稳定 quality 规范、formal/run/index owner、README/docs/Feature/ruling。
- 验证：4/4 static 正负向测试和 verifier PASS；缺 Skill marker、`/tmp` authority、缺 stderr 合同均被拒绝。
- 边界：本轮没有数学结论，不生成伪 proof package；C4 仍 `PAPER_ONLY`；fresh model behavior、首个真实数学 package 和 Git version-close 均开放。
- Git：未 commit、未 tag、未 push。
