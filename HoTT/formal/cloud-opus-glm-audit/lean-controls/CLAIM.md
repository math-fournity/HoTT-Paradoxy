# Lean 对照的补充控制：路线的首尾是否真被检查、内核自己是否也这样判（2026-09-27）

> Cloud-Opus 审计会话（分支 `claude/charming-pasteur-mvzlio`）。用户要求对本会话后来的工作做一次声明层与证明层的自查，"尤其是 Lean 相关的证明，如果存在问题，立即进行必要的更新、完善"。本包就是这次自查的产物。
>
> - 工具链：Lean 4.34.0 Linux 发布资产，记录 `../LEAN_TOOLCHAIN_META.linux-x86_64.json`。它与本会话先前的记录 `../LEAN_TOOLCHAIN.linux-x86_64.json` 前缀相同、二进制相同，多钉住了 Lean 与 Std 两个库（`import Lean` 需要它们）。
> - 驱动：CG-001 的 `.claude/goals/CG-001-targeted-overview/tools/lean_check.py`，未改动。
> - 捕获：`Cloud-Opus审计并补完GLM/tools/capture_copus_lean_run.py`，命令见 `Cloud-Opus审计并补完GLM/tools/capture_lean_controls.sh`。

## 1. 查出的问题

Opus 的 C-65（`HoTT/formal/claude-cg001/wild-sst-lean/`）有一个负控制 `WrongRoute.lean`。它的注释写的是：

> "The step no longer fits between the previous endpoint and the target, so the kernel must reject it. This shows the route bookkeeping is checked, not merely parsed."

也就是说，它声称检验两件事：一步路线的**首尾**接不上时会被拒；拒绝它的是**内核**。

实际运行（Opus 的原收据 `20260926-CG001-WILD-SST-LEAN-NEG-01`，本会话的重放 `20260927-COPUS-REPLAY-CG001-WILD-SST-LEAN-NEG-01`，两份输出逐字节相同）报的却是另一件事：

```
WrongRoute.lean:20:63: error: Application type mismatch: The argument
  weaken_le i j p
has type
  LeF (weaken i) (weaken j)
but is expected to have type
  LeF (weaken j) (weaken i)
```

报出的错误落在这一步的**参数**上：给出的次序证明方向反了。（这一步其实首尾也接不上，但 Lean 报的是参数错，所以这次运行显示不出首尾有没有被比较。）报错的是细化器（elaborator），项没有走到内核。所以：

- 注释声称的"首尾记账被检查"，这个负控制没有显示出来；
- 注释说的"内核拒绝"，实际是细化器拒绝；
- C-65 自己的 `CLAIM.md` 对拒绝理由的描述是对的（"需要 `LeF (weaken j) (weaken i)`，所给的是 `LeF (weaken i) (weaken j)`"），错的只是 `.lean` 文件里的注释。

同类的用词问题在 C-72 的负控制 `WrongCastFlips.lean` 上也有：注释写 "expected KERNEL_REJECTED"，实际是细化器以 "Not a definitional equality" 拒绝。它的理由本身是对的（`cast p true` 化简为 `true`），只是阶段写错了。本会话 2026-09-27 为这两个负控制捕获的重放收据，状态字都是仓库通用的 `KERNEL_REJECTED`，阶段字段 `rejection_stage` 是准确的 `ELABORATION_ERROR_IN_TARGET`。

C-65 的主张本身（`coh2`）不受影响：它是被接受的定理，`leanchecker --fresh` 在全新内核里重查过。受影响的只是"负控制证明了什么"这一句。

## 2. 补上的控制

| 文件 | proof id | 预期 | 检验什么 |
|---|---|---|---|
| `WrongRouteEndpoint.lean` | `MP-COPUS-LEAN-C65-ENDPOINT-NEG-001` | 拒绝（细化器） | 路线 A 的第三步单独证明、单独被接受（`stepThreeWrongFace`，`#print axioms` 可见），它是正确的改写套在错误的外层面映射下（`S.d m i` 而不是 `S.d m k`）。把它接在前两步后面，就只剩首尾接不上这一个错。 |
| `KernelRoute.lean` | `MP-COPUS-LEAN-C65-KERNEL-001` | 接受 | 路线 A 的三步分别证明（`stepOne`、`stepTwo`、`stepThree`）；`addRoute` 用 `mkAppN` 把 `Eq.trans stepOne (Eq.trans stepTwo stepThree)` 拼成原始项，**每个端点都显式写出**，再用 `Lean.addDecl` 直接交给内核。`mkAppN` 什么都不检查，`addDecl` 不经过细化器：接不接得上只由内核判。第二步终点是 `weaken (fsuc j)`，第三步起点是 `fsuc (weaken j)`，内核要展开 `weaken` 才能把它们接上。 |
| `KernelRouteEndpoint.lean` | `MP-COPUS-LEAN-C65-KERNEL-NEG-001` | 拒绝（内核） | 同一个 `addRoute`，只把第三步换成 `stepThreeWrong`（单独被接受，错在外层面映射）。 |
| `KernelCast.lean` | `MP-COPUS-LEAN-C72-KERNEL-001` | 接受 | `addCastDecl` 陈述 `∀ p : Bool = Bool, cast p true = r`，证明项给 `fun p => Eq.refl r`，直接交给内核。要接受它，内核必须自己算出 `cast p true`，再与 `r` 比较。这里 `r = true`。 |
| `KernelCastFlips.lean` | `MP-COPUS-LEAN-C72-KERNEL-NEG-001` | 拒绝（内核） | 同一个 `addCastDecl`，`r = false`。 |

## 3. 命题全文

- **COPUS-LEAN-C01**（`KernelRoute.lean`，命名空间 `CopusLeanControls`）：
  - `stepOne`、`stepTwo`、`stepThree` 三条定理，参数表与 `routeA` 相同（`S m i j k p q x`），陈述分别是路线 A 三步各自的等式；
  - `kernelRouteA`：由 `addRoute` 交给内核的定理，陈述就是 `routeA` 的陈述（取自 `getConstInfo ``routeA`），证明项是上面那条显式首尾的链；
  - `kernelRouteA_states_routeA : @kernelRouteA = @routeA := rfl`（两者陈述相同；证明无关使它们定义性相等）；
  - `#print axioms`：`kernelRouteA`、`kernelRouteA_states_routeA` 都不依赖任何公理。
- **COPUS-LEAN-C02**（`KernelCast.lean`）：
  - `kernelCastIsId : ∀ (p : Bool = Bool), cast p true = true`，证明项 `fun p => Eq.refl true`，由 `addCastDecl` 交给内核；
  - `kernelCastIsId_states_castIsId : @kernelCastIsId = fun p => CG001.UniverseSetLean.castIsId p true := rfl`；
  - `#print axioms`：两者都不依赖任何公理。

## 4. 这件事说明什么（解释，非机器证明）

- 【解释】C-65 的两条路线在 Lean 里确实被逐步检查：一步的首尾接不上，细化器会拒（`WrongRouteEndpoint`）；绕过细化器、把项直接交给内核，内核也会在同一个接口处拒（`KernelRouteEndpoint`，报错以 `(kernel)` 开头），而同一个拼装器配上正确的第三步，内核接受（`KernelRoute`）。所以"`coh2` 用 `rfl` 成立"不是因为 Lean 不看路线，而是因为两条都被检查过的路线是同一个命题的两个证明，Lean 的相等证明无关。
- 【解释】C-72 的 cast 判断，内核自己也这样判：要它接受 `cast p true = true`，它接受；要它接受 `cast p true = false`，它拒（`declaration type mismatch`）。

## 5. 禁止外推

- 本包全部是 UIP 类型论（Lean 4）中的事，不陈述任何关于 HoTT 路径的事。
- 负控制只证明"这些具体的错误项被拒"，不证明 Lean 内核一般可靠。
- `kernelRouteA` 与 `routeA` 是同一命题的两个证明，本包不给 C-65 增加新数学。

## 6. 对原包的处理

- Opus 的 `WrongRoute.lean`、`WrongCastFlips.lean` 和它们的收据都不改动：它们的哈希被各自的收据钉住。
- 在原包目录各加一份只增不改的说明：`HoTT/formal/claude-cg001/wild-sst-lean/REVISIONS.md`、`HoTT/formal/claude-cg001/universe-set-lean/REVISIONS.md`，写明注释与实际行为的差别，并指向本包。
- 本会话先前的工具链记录 `../LEAN_TOOLCHAIN.linux-x86_64.json` 里有一句 "used only to replay the set-level contrast CG001-C-72" 已经过时（同一工具链后来也重放了 C-65）。该文件被 4 份收据钉住，不改；更正写在新记录的 `relation_to_base_record` 字段和这里。

## 7. 运行

见 `Cloud-Opus审计并补完GLM/证据索引.md` §4.5 与 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 末节"自查轮追加"。
