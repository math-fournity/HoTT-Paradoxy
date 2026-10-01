# questioning-delay 包的修订记录

> 本包的 `CLAIM.md` 已经写入运行收据的哈希（`20260930-CG001-QUESTIONING-DELAY-*` 各运行的 `source-manifest.json` 都列了它），按规则不改；范围与措辞的修订写在这里。

## 2026-09-30：“另加一个极限情形”是非形式的说法

- `CLAIM.md` 在“这件事改变了什么”第 3 条说阶梯“现在是同一个程序的一族实例，另加一个极限情形”。这里的“极限”只是非形式的说法，意思是“成员高度没有上限的那一端”。
- 本包**没有**证明宇宙是 `Gathering n` 这一族目录的任何形式极限（极限或余极限）。形式事实只有两条：
  - C-79 (b)：h-层 1+n 的目录恰好在第 1+n 问停；
  - C-78 (a)：宇宙上的程序等于 `never`。
- 同日发现于两项自检（解释有没有加码），同时改了思考笔记 CN-046 的标题与第 2 节第 3 条。形式命题、源码与运行收据不变。

## 2026-09-30：Lean 一级说“同一个程序”要加限定

- `CLAIM.md` 在“这件事改变了什么”第 2 条说“同一个程序该停处都停”，所列里含“Lean 里的宇宙第 1 问停（C-80）”。
- 精确说法：在 Cubical Agda 内部（ℕ、Bool、`Gathering n`、宇宙），这是字面意义的同一个定义 `question`。Lean 一侧是按同一组燃料方程写成的有限燃料运行，是同一个过程的转写，不是跨系统的同一个对象。这与同文“禁止外推”第 6 条一致。
- 同日在更新根 README 时的两项自检中发现；根 README、CN-046 与 Claude 总索引 002 已改为精确说法。形式命题、源码与运行收据不变。

## 2026-09-30：macOS 跨平台重放（本机 Claude Code 会话 eadb3381；交接说明 W12）

- 本包原先只在 Linux 上捕获与重放（七个运行 `20260930-CG001-QUESTIONING-DELAY-*`）。在本机 macOS 上照同一 proof id、claim id、源码与 include 根重捕了全部七个，运行编号带 `-MACOS-`；Lean 的两个用固定工具链 `HoTT/formal/claude-cg001/pedometer-ablation-lean/LEAN_TOOLCHAIN.json`，不经 elan。
- 对照：七对运行退出码与状态相同；把两边的仓库根、cubical 库根、Lean 库根换成占位符以后，stdout 逐行相同；stderr 都是 0 字节。驱动与日志：`.claude/explore/20260930-阶段收尾/`。
- 七个新运行都经 `verify_cg001_run.py --rerun` 精确重放（两个 `PASS_WITH_SCOPE`，五个 `NEGATIVE_CONTROL_REJECTED_AS_EXPECTED`），登记在 CG-001 证据索引 §23。
- `CLAIM.md` 不改（它被运行收据的哈希钉住）；其中“运行只在 Linux 上重放”一句，自本条起不再成立。命题范围不变。
