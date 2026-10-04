# 证明收据捕获器对 linked worktree 根的识别修复

> **身份：** `IMPLEMENTATION_AND_VERIFICATION_REPAIR / PROOF_EVIDENCE_INFRASTRUCTURE / NOT_A_MATHEMATICAL_RESULT`。

## 发现

在当前 linked Git worktree 中，`.git` 是包含 `gitdir: ...` 的文件，而不是目录。`capture_lean_proof_run.py` 与 `capture_agda_proof_run.py` 原先只接受 `.git` 目录，因而在任何 proof assistant 启动之前退出 `PROJECT_GIT_ROOT_REQUIRED`。这会把一个合法隔离 worktree 误判为非项目根，阻止本轮 Q／P／A／B 的可复现收据被写入权威 run 根。

## 修复的精确合同

两只捕获器现在共同使用同一最小判据：

```text
git -C <project-root> rev-parse --show-toplevel
  必须成功，且解析后的绝对路径必须等于 <project-root>。
```

这同时接受 primary checkout 的 `.git/` 目录与 linked worktree 的 `.git` 指针文件；它仍拒绝：非 Git 目录、嵌套子目录、以及 Git 报出的 top level 与调用者指定 root 不同的目录。它不扩大 source、网络、权限或 proof assistant 访问范围。

Lean 捕获器还新增可选 `--toolchain`：当使用 `lean-proof-toolchain/v1` 时，它把 `lean.root/bin/lean` 的字节大小和 SHA-256 核对并写入 `source-manifest.json` 的 `external_dependencies`。这填补了 registry 要求的“实际 command 二进制已 pin”证据；没有 `--toolchain` 的旧调用保持兼容。

## 验证

| 检查 | 结果 |
|---|---|
| Python bytecode 编译 | `capture_lean_proof_run.py`、`capture_agda_proof_run.py` 均通过。 |
| linked-worktree 正控制 | 两只模块的 `require_project_git_root(Path.cwd())` 均接受当前 worktree。 |
| 非 Git 临时目录负控制 | 两只模块均以 `PROJECT_GIT_ROOT_REQUIRED` 拒绝。 |
| Lean 实际捕获 | `20261004-MP-ZFC-ACTUAL-Q-POLICY-002-03` 成功；source manifest 固定 `ActualQPolicy.lean`、toolchain JSON 与 Lean 4.34.1 二进制。 |
| Cubical Agda 实际捕获 | `20261004-MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001-01` 成功；证明了修复不只停留在 helper 单测。 |

项目静态 `verify_math_proof_delivery_governance.py` 当前仍因 pre-existing `.codex/AGENTS.md` 缺失 `math-proof-delivery-gate:v1` marker 而 fail closed。该状态与捕获器修复无关，本轮未修改项目治理标记，也不把该 static validator 的失败说成数学证明失败。

## 影响与边界

受影响的是 proof receipt 的环境根资格化。数学 source、C-359、C-360、来源解释、P/Q 判断、模型和 Git current truth 均未由此改变。将来其它 `capture_*_run.py` 若也采用错误的 `.git.is_dir()` 条件，应在各自实际 consumer 触发时按同一 `git rev-parse` 合同修复；本轮不进行无关批量改写。
