# `MP-BARE-ZFC-Q-PRECISION-001`

这是 F-049 的第一个可复核形式包。它不试图让 Lean 伪装成 ZFC 的完整对象语言实现，也不以“ZFC 没有时间 primitive”推出不可表达性。

| 文件 | 职责 |
|---|---|
| `BareZFCPrecision.lean` | 固定 source-contract control 的 M2 non-factorization、无免费 bridge 与两个富接口正控制。 |
| `WrongBareZFCPrecision.lean` | 故意把 coarse resolved view 当作 OriginDone decoder；应被 Lean 拒绝。 |
| `CLAIM.md` | C-364 的自然语言命题、来源绑定与禁止外推。 |
| `LEAN_CORE_TOOLCHAIN.json` | 固定 Lean core checker。 |
| `capture_bare_zfc_precision.py` | 产生可重放的主运行收据。 |
| capture_bare_zfc_precision_negative.py | 保存粗接口伪 decoder 被 Lean 拒绝的负控制收据。 |

## 与 bare ZFC 的关系

SEP 的基础语言事实和 IEP/Norton 的应用／完成合同事实进入来源卡，而不是作为 Lean 公理。该 kernel 只证明：给定明确的两个 completion-contract world 与其固定 projection，投影不能决定 `OriginDone`；带额外 contract 信息的接口能。

因此，本包是“**对一个实际 ZFC-supported standard-solution application interface 的精度控制**”。它把 bare-ZFC 理论精度假说收紧为一个可进一步来源化的问题，而没有把 source-facing application view 冒充 bare ZFC 本身。
