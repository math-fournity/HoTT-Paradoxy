<!-- governance-shard:v2
logical_id: T_PRECISION_DIAGONAL_PLAN
shard_id: 002
index: ../理论精度与哥德尔式自反方案.md
-->

# T-OBS相对观察精度形式规格

> **状态：** C-367_MACHINE_PROVED_WITH_SCOPE / ABSTRACT_INTERFACE_ONLY。
>
> **功能：** 将“维度缺失／观察力不完备／理论精度低”从哲学直觉转成任务相对的可判定证明义务。

## 1. 基本对象

固定：

~~~text
W               原过程、原世界或任务状态域
L               被观察的低精度理论／接口
H               比 L 精细的描述或理论接口
πL : W → OL     L 实际保留的观察投影
πH : W → OH     H 实际保留的观察投影
r : OH → OL     忘却映射，πL = r ∘ πH
D : W → Prop    任务判词，例如 OriginDone、合法形成或可用资格
~~~

这里的“维度”不限定为几何坐标。它可以是时序、阶段、来源、操作历史、资源、证明证书、completion bridge 或任何在任务判词中起决定作用、却未被 πL 保留的量。

H 相对 L 更精细，不表示 H 在所有数学任务上更强；它只表示在这个固定 W 和 D 上，H 保留了 L 忘却的差异。

## 2. 候选核心定理 T-OBS-1

待证明的抽象命题是：

~~~text
若存在 x y : W，
  πL(x) = πL(y)
  且 D(x) ≠ D(y)，
则不存在 δL : OL → Prop，使
  ∀ w : W, D(w) ↔ δL(πL(w)).
~~~

这是一条因子化失败／信息不可判定命题。它的数学内容比“L 没有某个维度”更精确：

> L 的指定接口无法仅凭其实际输出全域决定 D。

它不推出：

- L 的对象语言不一致；
- L 不能编码 x、y 或 D；
- 所有 L 的接口都不够精细；
- H 已经是现实的最终描述；
- D 已经被证明是研究发起人原任务的唯一完成谓词。

## 3. 与现有 C-364 的关系

BareZFCPrecision.lean 已验证一个有限 completion-contract control：同一 standardResolutionView 对两个 worlds 给出相同 resolved，而 OriginDone 不同；因此该 fixed view 不决定 OriginDone，也不支付 universal bridge。它是 T-OBS-1 的**校准实例**，不是 T-OBS-1 的全域证明，也不是 bare ZFC 的精度定理。

正控制同样重要：rich completion view 和携带 contract bit 的 process code 可以决定 OriginDone。它表明结论是“该观察接口不够”，不是“过程信息不可表示”。

## 4. T-OBS 的机器化合同

未来首个 proof package 必须固定：

| 字段 | 要求 |
|---|---|
| W | 不能用未说明的自然语言世界替代 |
| OL/OH | 精确 type、set、category 或 syntax domain |
| πL/πH/r | 真正的函数或结构保持映射 |
| D | 精确谓词及来源或任务合同 |
| 碰撞 witnesses | πL(x)=πL(y) 与 D(x)≠D(y) 各有证明或来源认证 |
| 正控制 | 增加保留字段后 D 可恢复，或反例被阻断 |
| 禁止外推 | 不由 abstract theorem 归因任何具体理论 |

若使用 Lean，仅证明普通函数／命题版本，应标作 ABSTRACT_OBSERVATION_BOUNDARY_MACHINE_PROVED_WITH_SCOPE。若声称 HoTT、Cubical 或 ZFC-specific 内容，则必须使用保真 target calculus 或已证明的翻译。

## 5. 失败、停止与重开

- 找不到 D 的稳定任务合同：USER_OR_SOURCE_TASK_CONTRACT_REQUIRED；
- 找不到同投影异判词的 witness：NO_PRECISION_GAP_WITHIN_FIXED_INTERFACE_SCOPE；
- rich interface 已使 D 可恢复：记录为 INTERFACE_PRECISION_DEFENSE_WITH_SCOPE；
- 一般定理成立但 T-ZFC source interface 未支付：只完成抽象层，不进入 ZFC 归因；
- 出现新真实接口、任务合同或反例时，重开对应 fixed scope。

## 6. T-OBS-001 已完成的首个抽象单元

T0 选择了一般函数／命题接口而不是任一具体理论：World、View、project、observe 及碰撞 witness。MP-T-PRECISION-TOBS-001 / C-367 以 Lean 4.34.1 core 机器证明第 2 节的 collision-to-no-decoder 命题，并给出 TinyWorld 的粗观察负控制和 identity/rich observation 正控制。

来源层由 T0 source denominator 固定：HoTT Book §6.10 的 quotient universal property 与 Lean core Quotient.lift 说明了 factorization 必须 respect 被压平的关系；它们不被写成 Lean 公理，也不把 C-367 提升为 bare ZFC、HoTT 或现实结论。运行、负控制、claim matrix 与 selected registry evidence 均已按 C-367 的精确范围留存。
