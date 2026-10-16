# universe-set-lean 包的修订记录

> 本包的 `.lean` 源文件与 `CLAIM.md` 已写入运行收据的哈希，按规则不改；更正写在这里。本文件由 Cloud-Opus 审计会话（分支 `claude/charming-pasteur-mvzlio`）按用户 2026-09-27 的自查要求新建，只增不改。

## 2026-09-27：负控制 `WrongCastFlips.lean` 的阶段用词

**注释的说法**："Negative control for CG001-C-72 (expected KERNEL_REJECTED)"。

**实际行为**（原收据 `HoTT/verification/runs/20260926-CG001-UNIVERSE-SET-LEAN-NEG-01`，Linux 重放 `HoTT/verification/runs/20260927-COPUS-REPLAY-CG001-UNIVERSE-SET-LEAN-NEG-01`，输出逐字节相同）：细化器在 `rfl` 处拒绝，"Not a definitional equality: the left-hand side cast p true is not definitionally equal to the right-hand side false"。拒绝的理由正确（`cast p true` 化简为 `true`），但拒绝发生在细化器，项没有走到内核。

**补上的内核级对照**（`HoTT/formal/cloud-opus-glm-audit/lean-controls/`，说明见其 `CLAIM.md`）：`KernelCast.lean` 把 `∀ p : Bool = Bool, cast p true = r` 与证明项 `fun p => Eq.refl r` 经 `Lean.addDecl` 直接交给内核。`r = true` 时内核接受，且所得定理就是 `castIsId` 在 `b = true` 处的实例（运行 `20260927-COPUS-LEAN-C72-KERNEL-01`，含 `leanchecker --fresh`）；`r = false` 时内核自己报 `(kernel) declaration type mismatch`（`KernelCastFlips.lean`，运行 `20260927-COPUS-LEAN-C72-KERNEL-NEG-01`）。
