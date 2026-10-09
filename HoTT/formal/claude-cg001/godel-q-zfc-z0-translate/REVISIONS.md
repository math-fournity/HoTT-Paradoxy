# 修订与补注

> `CLAIM.md` 已进入收据的源清单哈希，不改；更正与补注写在这里。

## 补注 1（2026-10-09，本机会话 d58e0c0d；不是更正）

C-120 中的一致性句 `Sh.craig.consistent` 来自 Foundation 的 Craig 版第二定理。读 Foundation `1fb01b72` 的源码（`Bootstrapping/Syntax/CraigTrick.lean`）核对到：`Sh.craig` 的公理集由 `reCh := codeOfREPred (encode '' Sh)` 定义，那是用选择公理挑出的某个 Σ1 公式。它在 ℕ 中正确定义 Sh，在非标准模型里怎样表现，由这次选择决定。

所以 C-120 说的是：对**这一个**（由选择给出的）Sh 的一致性句，𝗭𝗙𝗖 证明不了它的翻译。第二定理对 Sh 的任何 Σ1 定义都成立，结论本身不受影响；但这句话在 𝗜𝚺₁ 内部与 Con(𝗭𝗙𝗖) 的关系无从推理。

因此 W8 若要接到 Con(𝗭𝗙𝗖)，应改用显式的可证性谓词 `Provable 𝗭𝗙𝗖 (iT 0 x)`，而不是在 `Sh.craig.consistent` 与 Con(𝗭𝗙𝗖) 之间搭桥。见 CN-072 §4。
