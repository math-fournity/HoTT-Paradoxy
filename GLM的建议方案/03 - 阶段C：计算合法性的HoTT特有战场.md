# 03 - 阶段 C：计算合法性的 HoTT 特有战场（与 A/B 并行）

> 对齐声明：本阶段服务 `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`（ACTIVE_USER_DIRECTION）
> 与 KC-000010/011/012/013/024/027/036。**不是放弃 Gödel/计算合法性主线，而是把它
> 闭合到终局判词并交付，把火力从 generic 区移到 HoTT 特有区**（自审计 G3）。

## 1. 战场转移的论证

R0–R2 已闭合、R3 已机器重放（C-244–C-249）。按 `R3-R4-GODEL-RETURN-001` §6 自设的
消融设计，R4 的可预测终局是 `GENERIC_GODEL_BOUNDARY_WITH_HOTT_INSTANCE`——不完备性
机制经 Q 解释转移，不依赖同伦结构。这一预测**不改变该线的用户价值**：KC-000027 的
框架正是"HoTT 对齐程序后，程序的问题就是它的问题"——继承性本身就是用户要的呈现
方式。因此本阶段对 R4 的处置是：

1. 完成十二义务矩阵中可机械闭合的部分（H-SYNTAX/H-NAT/H-ID-PATH/H-CONVERSION/
   H-EFFECTIVITY，用 `akaposi/cohtt` 形式语法切片 + 一个具名 community calculus）；
2. 把终局判词**按继承框架写成交付物**（"exact HoTT calculus 在显式一致性/有效性前提
   下承袭程序侧不完备性；消融显示机制 generic"），而不是当作"又一条 NO_HIT"入库了事；
3. 严格遵守 KC-000036 的元/对象分层（宿主 Coq/Agda 的定理 ≠ 对象理论 HoTT 的定理；
   `方向追踪/003` DIR-L-SELF-REFLECTION 行已保留此纪律）；
4. **不重复堆叠**第三份同型 Gödel 编码（ERCF-3 T3 链 C-157–C-183 与 R2 ProgramCode
   C-191–C-198 已在库；新编码仅在 RL 任务需要时按阶段 B 的消费者驱动产生）。

继续深挖与否（例如 Rosser 强度、独立句的 HoTT 侧精化）由所有者裁定，默认排队不推进。

## 2. C-U1：stuck-transport 机器演示（Book HoTT 典范性失败的展览件）

命题形状（Agda，postulate 版，进 F-011）：

```agda
postulate
  UA : {A B : Set} → (A ≃ B) → (A ≡ B)     -- Book HoTT 式公理 univalence

stuck : Bool
stuck = transport (λ _ → Bool) (UA notEquiv) true
```

要点：`stuck` 是 **Bool 的闭项**，但不规范到 `true`/`false`（`J` 只在 `refl` 上计算，
公理路径卡死）——Book HoTT"断言了它不能求值的相等"的直接展览（方向 B 的纯形态：
把公理资格当计算能力）。机器证据分三层：

1. postulate 版：闭项停在非规范形（求值不产数字——用 `C-c C-n` 观察留档 + 正式 run）；
2. cubical 对照：同一命题在 Cubical Agda 中**确实计算**（C-100 已证 ua 路径按 `not`
   计算）——即防御存在，支付是区间/cofibration 结构；
3. 交付层：S052/N10 已实测 cubical 内容无编译交付路径（`--cubical` 全拒、
   `--erased-cubical` 仅擦除）——支付的尽头是"可求值但不可交付"。

三层合起来是计算合法性视角下最完整的方向 B 证据链，全部有已验证锚点，只差第 1 层的
一个新 run。预算：1 session。

## 3. C-U2：交付路径审计扩展（S052 的定向加深）

以 N10 五层审计塔为基础，只补两个有判别力的缺口：

1. `--erased-cubical` 擦除语义的形式化命题：擦除后交付的到底是什么（一个"形状检查
   通过但不携带计算内容"的产物）——把 N10 的实测升级为一个可机器检查的命题；
2. Lean 侧对应物：`noncomputable`/商大消去在交付链上的语义（N2 已有实测，补命题化）。

预算：2 sessions。产出喂阶段 A 第 8 章。

## 4. C-U3：支付-债务目录（P3 原则的落地）

把 `DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT` 类结果重编为统一表（每行必有 C-claim/run 锚点）：

| 构造 | 被删/被换维度 | 防御 | 支付 π | π 典范性 |
|---|---|---|---|---|
| 2LTT 严格化（C-227–C-232） | 内层路径结构 | replacement+UIP 边界 | 外层 UIP | 理论强制 |
| LOPS internal classifier（C-233–C-238） | global/local 资格 | ordinary no-go | crisp/global 假设 | 模态限制 |
| ITT regular replacement（C-239–C-243） | 路径消去强度 | regular→False | DFib+Trans / emptyctx 限制 | 分层限制 |
| Book univalence（C-100 对照 + C-U1） | 相等的可求值性 | cubical 计算 | 区间+cofibration | 实现税 |
| cubical 交付（S052/N10） | 可执行性 | 擦除交付 | 放弃计算内容 | 无典范（擦除不可逆） |
| 截断（C-67–C-70、C-134–C-141） | 见证/选择 | 命题消费者限定 | 分离见证数据 | 无典范（C-142–C-148） |
| SIP（C-124–C-128） | 签名外结构 | 结构表示 | 细化签名 | 表示依赖 |
| Cauchy（C-129–C-133） | 模数/时间 | 纳入同一性 | 模数数据 | 任务依赖 |

目录语义（对齐 KC-000018/000029）：支付不是缺陷清单，是**理论经济学的资产负债表**——
每一行都是"工具性收益 ↔ 被转移责任"的机器化记账；π 无典范的行是 Z 铁律技术核的
直接证据（恢复通道存在但没有理论内定的那一条）。预算：1 session（纯重组+引用核对）。
目标 ≥10 行，喂阶段 A 第 7 章。

## 5. 成功判据

1. C-U1 run 入 `HoTT/verification/runs/`，矩阵新增行措辞含"Book/cubical 对照、非
   Book HoTT 独有缺陷"的 scope；
2. C-U2 两命题通过或如实登记 NOT_RUN 边界；
3. C-U3 目录 ≥10 行、每行锚点可回溯、经 01 号 A-U4 交叉核对；
4. R4 矩阵终局判词落库并按继承框架写入 A 报告第 9 章（对照与边界）。

## 6. 本阶段不做的事

- 不重放/重建任何已有 R2/R3/ERCF-3 编码；
- 不把 generic 结果写成 HoTT 特有（goal.md §1 禁令继续有效）；
- 不因 C-U1 的"卡死"宣称 Book HoTT 不一致或不可用——它是典范性现象，防御（cubical）
  存在且已付费，目录如实记两行。
