# wild-sst-lean 包的修订记录

> 本包的 `.lean` 源文件与 `CLAIM.md` 已写入运行收据的哈希，按规则不改；更正写在这里。本文件由 Cloud-Opus 审计会话（分支 `claude/charming-pasteur-mvzlio`）按用户 2026-09-27 的自查要求新建，只增不改。

## 2026-09-27：负控制 `WrongRoute.lean` 的注释与实际行为不符

**注释的说法**：路线 A 的最后一步把面映射次序颠倒后，"no longer fits between the previous endpoint and the target, so the kernel must reject it. This shows the route bookkeeping is checked, not merely parsed."

**实际行为**（原收据 `HoTT/verification/runs/20260926-CG001-WILD-SST-LEAN-NEG-01`，Linux 重放 `HoTT/verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-LEAN-NEG-01`，输出逐字节相同）：报错落在这一步的**参数**上，`weaken_le i j p` 证明的是 `LeF (weaken i) (weaken j)`，这一步要的是 `LeF (weaken j) (weaken i)`；报错的是细化器，项没有走到内核。

**所以**：
1. 这个负控制显示出"参数的类型被检查"，但显示不出"首尾被检查"，也不是内核拒绝。
2. 本包 `CLAIM.md` 的"负控制"一节对拒绝理由的描述是对的；错的只是 `WrongRoute.lean` 的注释。
3. 主定理 `coh2` 不受影响（被接受，`leanchecker --fresh` 在全新内核中重查过）。

**补上的控制**（`HoTT/formal/cloud-opus-glm-audit/lean-controls/`，说明见其 `CLAIM.md`）：
- `WrongRouteEndpoint.lean`：第三步单独证明、单独被接受，只错在外层面映射（`S.d m i` 代替 `S.d m k`）；接进路线后，细化器在第二步与第三步的接口处拒绝。运行 `20260927-COPUS-LEAN-C65-ENDPOINT-NEG-01`。
- `KernelRoute.lean` / `KernelRouteEndpoint.lean`：同一条路线用显式首尾拼成原始项，经 `Lean.addDecl` 直接交给内核。第三步正确时内核接受，且所得定理与 `routeA` 陈述相同（运行 `20260927-COPUS-LEAN-C65-KERNEL-01`，含 `leanchecker --fresh`）；第三步错在外层面映射时，内核自己报 `(kernel) application type mismatch`（运行 `20260927-COPUS-LEAN-C65-KERNEL-NEG-01`）。
