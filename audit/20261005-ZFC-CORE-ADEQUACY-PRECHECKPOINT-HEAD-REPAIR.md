# ZFC 核心充分性方案：pre-checkpoint HEAD 修复

> **身份：** `COGNITION_INTEGRITY_REPAIR / PRECHECKPOINT_BOOTSTRAP / NO_MATHEMATICAL_CLAIM`。

新方案从 `014c42fe` 创建时，`.codex/cognition/HEAD.json` revision 301 仍记录
`MEMORY/001 - 当前执行队列.md` 的旧 SHA-256：

```text
expected f5829ffaf8dfdc9fe575e34a54a4bce5ba1d3fbc5dfb2b4884d46ea4ffa4e7c9
actual   8e734cd5dced1adcc72c5794643f1d33bb24885b754f12c3378281db0f10c6d4
```

Git history显示，`014c42fe` 将 GODEL-Q/MM0 文字更新写入 `MEMORY/001`，但没有同事务刷新 cognition HEAD 的该条 tracked hash。因此 `cognition_runtime.py plan` 正确 fail-closed 为 `UNCOMMITTED_STATE`；这不是 ZFC、T、C0–C6 或任何数学命题的失败。

本文件授权的 bootstrap 只将 HEAD 的这一条 hash 同步到当前已提交文件字节，保持 revision、latest session 和其它 tracked entry 不变。其后必须立即通过新的正式 checkpoint 写入本轮 C0 plan、closure、Feature、MEMORY、STATE session 和 canonical transaction/result；bootstrap 自身不构成 checkpoint，也不产生数学结论。
