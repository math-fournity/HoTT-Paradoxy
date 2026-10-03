# HMZ-007：消费者、支付与反解释控制

| 控制 | 来源事实 | 阻止的误报 |
|---|---|---|
| `HMZ-C-011` 配对归因控制 | WoLLIC 的“multiple attempts”没有点名 Werner。 | 不把年代接近／主题相同写成 Voevodsky 明确批评 Werner。 |
| `HMZ-C-012` Choice payment | README、Werner §4.5、`Replacement.v` 将 Choice/TTDA 与 Replacement、set AC 的证明显式连接。 | 不把 `∀A∃B` 或一个 Prop-level existential 自动称为可交付 set／function。 |
| `HMZ-C-013` Power construction control | `Power` 以既有 `Ens`、`sup` 和 `A -> Prop` 定义；相应性质在 model 中证明。 | 不把 Power Set 的名字或“全部谓词”写成未形成对象的自身使用。 |
| `HMZ-C-014` Russell guard | `Russell.v` 的结论以 universal-container hypothesis 为前提。 | 不把一个反证 universal set 的证明改写为“系统已无条件接受罗素集合”。 |
| `HMZ-C-015` host boundary | WoLLIC slide 8 自报 Coq universe-management 与 patch 的限制；archive 是 2022 port，未重跑 Coq 6.3。 | 不把 source code 存在、旧 README 的 build instruction 或 proof-assistant host 行为当作 ZFC 理论层结论。 |

这些控制说明的只是：此分母中的实际编码公开了 formation、choice、guard 或 host 条件。它们不证明所有 ZFC使用都已支付，也不关闭 Power Set 的独立 P-FORGE 站位。
