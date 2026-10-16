# 核心演算：判断、构造、相等与计算

类型：HUMAN_EDITED；Theory Schema v0.1 的核心规则说明。基线为 [HoTT Book 固定源码](upstream/README.md)，主要采用附录 A.2 与 A.3；A.1 的差异单列。规则是中文规范化转述，不是上游逐字原文；若发生歧义回到锁定源码，不反向改写来源。

本文件中所有 `Γ ⊢` 都是推导判断，`a =_A b` 是类型，`p : a =_A b` 才是这个类型的项。宇宙下标 i、j 属于呈现的元语言索引；省略处须能补出合法层级。依赖绑定均避免变量捕获。

## C01 · 语法与判断形状

**依据**：[formal.tex](upstream/book-578b85cc/formal.tex)，Preliminaries、A.1、A.2。

A.1 的项语法为变量、λ 抽象、应用、原始常量与已定义常量：

```text
t ::= x | λx.t | t(t′) | c | f
```

A.2 用带类型与绑定位置的构造器、消去器表达同样的基本意图，不把 A.1 的无类型 convertibility 与 A.2 的 typed equality 混为一个定义。

A.2 有三类基本判断：

```text
Γ ctx                 上下文合法
Γ ⊢ a : A             项 a 在 Γ 中具有类型 A
Γ ⊢ a ≡ b : A         项 a、b 在 A 中判断相等
```

“Γ ⊢ A type”在某些类型论教材中是独立判断；这里通过“Γ ⊢ A : Uᵢ”表达类型资格。上下文合法、项具有类型、项判断相等都不是理论内部的一般布尔判定函数。

派生式是一棵规则树。写出一个字符串不等于已经给出其类型推导；写出一个类型也不等于已经给出它的项。

**非承诺**：没有由任意自然语言描述自动产生合法项的规则；没有把“无法找到证明”当成“存在反证”的规则。

## C02 · 上下文、变量、绑定与依赖

**依据**：A.2 Contexts、Structural rules，源码 503 行起。

```text
────────────
· ctx

Γ ⊢ A : Uᵢ     x fresh
─────────────────────
Γ,x:A ctx
```

变量规则：若上下文合法，其中列出的 `xᵢ:Aᵢ` 可作为假设使用。对依赖上下文
`x₁:A₁,…,xₙ:Aₙ`，Aᵢ 只能依赖此前的变量。

这是实际存在的**依赖顺序**。它不自动表示物理时间，也不保证某个假设已经在现实中被生产出来。假设可用性、证明过程中的先决关系、运行时值的可用时刻必须分别检查。

**重要反例**：不能以“HoTT 不使用 clock 下标”为由断言“HoTT 的规则不区分先后”或“未声明变量可以随便引用”。

## C03 · 结构规则、替换与转换

**依据**：A.2 Structural rules；替换与弱化在该呈现中是 admissible rules，不是额外任意公理。

```text
Γ ⊢ a:A     Γ,x:A,Δ ⊢ b:B
─────────────────────────
Γ,Δ[a/x] ⊢ b[a/x] : B[a/x]

Γ ⊢ A:Uᵢ    Γ,Δ ⊢ b:B
───────────────────────
Γ,x:A,Δ ⊢ b:B            x fresh
```

还有作用于判断相等的替换/弱化版本：替换相等项、替换环境中的项，都要同时替换后续依赖类型。判断相等具有自反、对称、传递以及所有类型/项构造器的合同性。

转换规则：

```text
Γ ⊢ a:A     Γ ⊢ A ≡ B : Uᵢ
───────────────────────────
Γ ⊢ a:B
```

已有 `a ≡ b:A` 也可沿类型的判断相等改写为 `a ≡ b:B`。这不同于沿 `p:A=_U B` 作显式 transport。

本核心并非线性资源系统；变量可以重复出现或不使用。但这不表示物理资源能够无成本复制，也不允许任意重排有依赖的上下文。

**排版观察**：锁定 formal.tex 第 610 行的 Π-intro-eq 结论出现 A′，局部前提未声明它。本文依据该段明确表述的“构造器保持判断相等”使用同一 A，不把疑似排版问题当作新增自由规则。原文件保持不变，未向上游提交修改。

## C04 · 宇宙与类型资格

**依据**：A.1 Type universes；A.2 Type universes；第 1 章 §1.3。

```text
Γ ctx
───────────────
Γ ⊢ Uᵢ : Uᵢ₊₁

Γ ⊢ A : Uᵢ
────────────────
Γ ⊢ A : Uᵢ₊₁
```

基线采用累积宇宙，且类型属于某个宇宙。不能将 `Uᵢ:Uᵢ₊₁` 改写成 `Uᵢ:Uᵢ`；不能因宇宙名称被省略就取消大小条件。升到更大宇宙的可用性不等于不同宇宙已经等价。

A.2 的若干形成/消去规则使用同一个宇宙指标；需要多个指标时，先用累积性在共同较大宇宙中解释，不能不加说明地把另一个 proof assistant 的 universe-polymorphism 规则当成书中逐字规则。

**非承诺**：没有任意 resizing，也没有所有类型组成的同层类型。Propositional resizing 是另行标记的可选假设，见 D04。

## C05 · Π：依赖函数类型

**依据**：A.2 Dependent function types，646 行起。

```text
Formation:
Γ ⊢ A:Uᵢ    Γ,x:A ⊢ B:Uᵢ
──────────────────────────
Γ ⊢ Π(x:A).B : Uᵢ

Introduction:
Γ,x:A ⊢ b:B
─────────────────────
Γ ⊢ λx.b : Π(x:A).B

Elimination:
Γ ⊢ f:Π(x:A).B    Γ ⊢ a:A
──────────────────────────
Γ ⊢ f(a):B[a/x]

Computation (β):
(λx.b)(a) ≡ b[a/x] : B[a/x]

Uniqueness (η, A.2):
f ≡ λx.f(x) : Π(x:A).B
```

非依赖情形定义 `A→B := Π(x:A).B`。β/η 是判断相等；函数外延性是另外一项内部 identity 原则，不是把这两个规则改名。

**呈现差异**：A.1 明确不加入这里的 judgmental η，A.2 加入。谈归约和正规化时必须标明采用哪一呈现。

**时间切口**：函数项具有计算行为，但其 identity 不自动记录代码、执行轨迹和运行成本。具体丢失何物需要指定 Program→Function 语义，而非由 Π 类型名称决定。

## C06 · Σ：依赖对类型

**依据**：A.2 Dependent pair types，713 行起；§2.7。

```text
Formation:
A:Uᵢ, x:A ⊢ B:Uᵢ    ⇒    Σ(x:A).B : Uᵢ

Introduction:
a:A, b:B(a)           ⇒    (a,b):Σ(x:A).B

Elimination:
C:(Σ(x:A).B)→Uⱼ
d:Π(x:A).Π(y:B(x)).C(x,y)
⇒ indΣ(C,d):Π(p:Σ(x:A).B).C(p)

Computation:
indΣ(C,d,(a,b)) ≡ d(a,b)
```

这里使用函数式记法转述消去器；严格 A.2 绑定写法及宇宙条件见来源。投影 `pr₁(p):A`、`pr₂(p):B(pr₁(p))` 可由消去器定义。非依赖情形为积 A×B。

Σ 的 judgmental η **未在此基线假定**；`(pr₁ p,pr₂ p)=p` 的命题性唯一性可以证明。

**现实切口**：Σ 正是把来源、成本或证明附在对象上的直接方法。忘掉第二分量可能损失信息；“用了 HoTT”本身不要求把第二分量忘掉。

## C07 · 余积 A+B

**依据**：A.2 Coproduct types，766 行起。

- 形成：A、B 为同一可容纳宇宙的类型，则 A+B 为类型。
- 引入：`inl(a):A+B` 与 `inr(b):A+B`。
- 消去：给 C:(A+B)→U，分别给出左分支 `Πa.C(inl a)` 和右分支 `Πb.C(inr b)`。
- 计算：在 inl 上归约到左分支，在 inr 上归约到右分支。
- 不额外假定通用 judgmental η。

**非承诺**：A+B 携带选择了哪一侧的数据；逻辑中的截断析取 `∥A+B∥` 不是同一个类型。

## C08 · 空类型 0、单位类型 1、布尔类型 2

**依据**：A.2 Empty / Unit；§1.5、§1.8。

| 类型 | 形成 | 引入 | 消去 | 计算 / 唯一性 |
|---|---|---|---|---|
| 0 | 0:Uᵢ | 无 | 从 a:0 可得 C(a) | 无构造子计算规则 |
| 1 | 1:Uᵢ | ★:1 | 给 c:C(★)，得 Πx:1.C(x) | ind₁(C,c,★)≡c；不假定 judgmental η |
| 2 | 可作为有限类型呈现，也可编码为 1+1 | 两个构造值 | 两分支消去 | 两个 β 方程；编码选择要注明 |

0 是合法类型，不因没有闭项就成为“非法类型”。空类型的形成、一个闭项的存在、某段自然语言是否可形式化，是三种判断。这一点对“假集合/伪命题”类比尤其重要。

## C09 · 自然数、递归与归纳

**依据**：A.2 Natural number type，860 行起；§1.9–1.10。

```text
N:Uᵢ
zero:N
suc:N→N

C:N→U
c₀:C(zero)
cₛ:Π(n:N).C(n)→C(suc n)
──────────────────────────
indN(C,c₀,cₛ):Π(n:N).C(n)

indN(C,c₀,cₛ,zero) ≡ c₀
indN(C,c₀,cₛ,suc n) ≡ cₛ(n,indN(C,c₀,cₛ,n))
```

这是合法结构递归；不是任意自调用/循环算子。依赖归纳比只指定函数输入输出更有约束。一个定义使用递归，不代表它违反用户要求的因果准入。

**时间切口**：上述后继展开可计步，但核心规则没有同时规定墙钟耗时或自动保存所有步骤轨迹。需在固定操作语义中额外建模 Cost/Trace。

## C10 · W 类型与一般归纳定义

**依据**：A.1 W-types，410 行起；第 5 章 §5.3、§5.6。

```text
A:U, B:A→U
W := W(a:A).B(a)

sup : Π(a:A).(B(a)→W)→W

C:W→U
d:Π(a:A).Π(u:B(a)→W).
    (Π(b:B(a)).C(u(b)))→C(sup(a,u))
──────────────────────────────────
indW(C,d):Π(w:W).C(w)

indW(C,d,sup(a,u))
 ≡ d(a,u,λb.indW(C,d,u(b)))
```

A 是结点标签，B(a) 是分支索引。无限分支的树与实际已执行无限多个步骤不可混称。

A.2 没有单列 W 的整张规则表；本条采用 A.1/§5.3，不伪称来自 A.2。一般归纳定义要求严格正性；第 5 章同时讨论 indexed、mutual 等推广，不把任意递归类型方程全纳入核心。

**拒绝例**：貌似构造器 `g:(C→N)→C` 不能凭语法外观就获得普通归纳类型的消去规则。§5.6 给出为什么这类任意形成方案有问题；它展示的是 HoTT 对形成合法性的重视，而不是 HoTT 实际允许这些坏规则。

## C11 · Identity：同一类型内的路径

**依据**：A.2 Identity types，907 行起；§1.12。

```text
Formation:
A:U, a:A, b:A    ⇒    Id_A(a,b):U

Introduction:
refl_a : Id_A(a,a)

Elimination (J / unbased path induction):
C:Π(x y:A).Id_A(x,y)→U
d:Π(z:A).C(z,z,refl_z)
⇒ J(C,d):Π(x y:A).Π(p:Id_A(x,y)).C(x,y,p)

Computation:
J(C,d,a,a,refl_a) ≡ d(a)
```

另有 based path induction 呈现，与通常 path induction 的关系须按书中论证处理；不能把“归纳时只需检查 refl”读成“任何路径都判断等于 refl”。

**未加入**：一般 equality reflection（p:a=b 就让 a≡b）、全类型 UIP/K、全类型 proof irrelevance。

**禁区**：a:A、b:B 且没有共同类型/运输数据时，不可直接写 Id_A(a,b)。

## C12 · 由 identity 导出的路径代数与 transport

**依据**：第 2 章 §2.1–2.3。

```text
p:a=b                 ⇒ p⁻¹:b=a
p:a=b, q:b=c          ⇒ p·q:a=c
f:A→B, p:a=b          ⇒ ap_f(p):f(a)=f(b)
P:A→U, p:a=b          ⇒ transport_P(p):P(a)→P(b)
```

transport 在 refl 上判断归约为恒等。依赖函数的作用记 apd，其结果是依赖路径；需要包含 transport 的纤维端点。

路径单位律、结合律、逆律及更高 coherence 构成高阶结构；不能一律标成 judgmental equality。普通函数 A→B 不因 identity 有逆就全部可逆。

**对时间研究的意义**：相等路径的可逆性不是物理动作可逆性。若将事件映到 identity，需要单独审计该解释是否抹去不可逆条件。

## C13 · 同伦、等价与正确的 isEquiv

**依据**：§2.4；第 4 章 §4.1–4.5。

```text
f ~ g := Π(x:A).f(x)=g(x)
A ≃ B := Σ(f:A→B).isEquiv(f)
fib_f(b) := Σ(a:A).f(a)=b
isContr(X) := Σ(c:X).Π(x:X).c=x
```

`Π(b:B).isContr(fib_f(b))` 是等价的一个正确刻画；**书在 §4.5 最终选择 ishae（half-adjoint equivalence）作为 isEquiv 的定义**，不是直接以 qinv 数据替代。

Half-adjoint 数据可写为 f 的逆 g、η:g∘f~id、ε:f∘g~id，及适当三角 coherence；按 book 的方向约定为 `ap_f(η_x)=ε_(f x)`。Bi-invertible 与 contractible-fiber 刻画和它等价。

qinv 足以用来证明等价，但“给逆函数及双侧同伦的数据类型”一般不是 mere proposition；不能在单价公理中不加检查替换掉 isEquiv。

## C14 · 函数外延性

**依据**：§2.9；§4.9；A.3 Function extensionality and univalence。

由 J 可定义：

```text
happly : (f=g) → Π(x:A).f(x)=g(x)
```

函数外延性断言 happly 是等价，因而得到逆方向 funext。依赖函数也适用。其逆同伦提供的是命题性计算/唯一性关系，不是无条件新的 β 归约。

A.3 可把它列为公理常量；§4.9 又从单价性导出它。因此“列出”和“逻辑独立地需要”不同；依赖图允许它是冗余公理。

**研究连接**：同函数异时使用本条把点态相等提升为函数 identity；后续 Runtime/Cost 是否可以从这个 identity 下的对象恢复，仍是另外的断言。

## C15 · 单价性

**依据**：§2.10；A.3；宇宙范围必须明确。

由 J 和 transport 定义：

```text
idtoequiv_(A,B) : (A =_U B) → (A ≃ B)
```

单价性断言这个函数是等价，得到逆 ua：

```text
ua : (A ≃ B) → (A =_U B)
```

基线中 transport 沿 ua(e) 与 e 的作用之间有**命题性**计算关系；没有自动把所有这类式子变成判断相等。所选书式呈现把相应公理加为常量，不增加 cubical 求值规则。

**承诺范围**：等价类型可以在宇宙 identity 意义下识别；携带结构时还要保存那份结构。它不把任意现实同名对象、社会角色、历史身份或不同程序代码自动判同。

## C16 · 高阶归纳类型与圆

**依据**：A.3 The circle；第 6 章，尤其 §6.2、§6.13。

圆的基本数据：

```text
S¹:U
base:S¹
loop:base=base
```

给 `C:S¹→U`、`b:C(base)`，并给依赖路径
`ℓ:transport_C(loop,b)=b`，得到 `indS¹(C,b,ℓ):Π(x:S¹).C(x)`。

- 点计算：`indS¹(C,b,ℓ,base)≡b`；
- 路径计算：相应 apd 在 loop 上等于 ℓ，是命题性路径，不是这里的 judgmental 归约。

**一般 HIT 的状态**：源码 §6.13 给出严格正性、构造子按依赖排序、端点表达式自然性等准则，但明确没有提供一份完整精确的通用语法。Schema 必须记录这个边界，不能自己发明一个“所有 HIT 的万能形成规则”。

书中的 interval HIT 也不是 cubical 类型论的原始维度对象，更不是物理时间轴。

## C17 · 定义、精化、检查与证明搜索

**依据**：A.2 Definitions；A.1 已定义常量；§1.10。

- 定义名、隐式参数和典型歧义需要展开/精化到规则能检查的形式；
- 精化（elaboration）不等于类型核心本身；
- 检查给定候选项，不等于搜索任意问题的证明；
- 书中结构递归不能替代任意求值器的终止保证；
- 公理常量是有类型的假设，不是被归约计算出来的见证。

因此“证明检查器接受”还必须追问：接受了哪个项、哪些公理、什么 universe 设定、什么编译/内核选项。Schema 不把特定 Agda/Lean 行为自动等同于 book 核心。

## C18 · 元理论：结论与适用系统一起记录

**依据**：A.4 Basic metatheory，1064 行起。

| 主张 | 锁定书中所指系统 | 此 Schema 的界限 |
|---|---|---|
| 保持类型 | A.1 的归约/转换系统 | 不是任意附加公理或新重写规则的总保证 |
| 合流 | 同一基础重写系统 | 合流不表示每条执行轨迹或成本相同 |
| 强正规化 | A.1 基础系统 | 不直接升级为任意 HoTT/HIT/扩展演算的新证明 |
| 正规形类型检查/证明检查 | 书中限定系统与表示 | 不等于自然语言翻译和无界证明搜索可判定 |
| 空类型无闭项、一致性 | 基础系统的正规化/正规形论证 | HoTT 扩展需相应语义或计算论证 |
| 自然数 canonicity | 基础系统 | 不自动适用于书式非计算公理常量 |

书在 A.4 明确说，上述论证不能原样用于扩展 HoTT，并讨论语义模型和开放计算问题。此处“开放”是书中呈现的历史语境，不是声称到 2026 年一切 cubical/HIT 结果仍未知；后续结果与具体系统见 [扩展图谱](EXTENSIONS_AND_METATHEORY.md)。

**尚未完成**：本项目没有重新证明这套基础元理论，也未对全部扩展做机器验收。Schema 建立来源与适用域，不用书中定理名称假装本地已复现。

## 跨呈现接口补充（v0.2）

以下是具体呈现的对照，不把不同系统合成一个虚构核心。官方依据为
[Agda Cubical 文档](https://agda.readthedocs.io/en/latest/language/cubical.html)
（2026-09-09 页面显示 2.9.0；这是日期化页面观察，非已固定的安装版本）；CCHM/CHM 的原始论文见扩展页。

| 接口 | 书式 A.2/A.3 | Cubical Agda 文档的相应接口 | 不可偷换 |
|---|---|---|---|
| 相等 | 原始 Id/refl/J | PathP；另有 cubical identity | PathP 不是普通函数类型的逐字别名 |
| J 计算 | J 在 refl 上 judgmental β | 官方从 Path 定义的 J 只给 path-level β | 不把该特定 Path-J 当成所有 cubical Id 都无 β |
| transport | 由 J 导出 | transp 配合 interval/face 条件 | transp 的侧条件不可省略 |
| composition | 由路径归纳构造路径合成 | hcomp/Kan 边界填充 | 不等同任意实际动作顺序 |
| interval | 可另定义 interval HIT | I:IUniv，带 De Morgan 运算；不支持通常 transp/hcomp | 不是默认的实数区间、物理时间或稠密数轴 |
| funext | A.3 假设，或从标准 UA 推出 | 可直接以路径抽象构造 | 同名定理不等于相同原始规则 |
| ua | 单价公理的逆方向，命题性计算 | 通过 Glue 与相应计算规则实现 | 不能把所有 ua/transport 式子无条件称 judgmental |
| HIT | 圆的点 judgmental、路径 propositional 计算 | 允许类的高阶构造可有 judgmental 计算 | 具体允许语法/边界须检查 |

最小的使用条目应包括：profile/版本、完整类型签名、宇宙、原始/定义/公理/派生状态、判断与
命题计算、此定义使用的依赖、此证明使用的假设、精确来源及运行证据（若有）。先保留在 Markdown，
不为元数据单独建立数据库。没有机器运行证据的字段写“未运行”。

### 等价表示不是全部两两同义

C13 的 half-adjoint、bi-invertible 与 contractible-fiber 刻画具有相应等价定理；qinv 数据能给出
isEquiv 的证据，但一般不能标成 qinv(f)≃isEquiv(f)。需要的关系是准确映射/条件定理，不是为了
统一接口而声明所有 variant 同义。直接定义依赖还会随 isEquiv 所选表示变化。

### 标准单价性与较弱同名原则

[Cavallo–Höfer 2026 v2](https://arxiv.org/abs/2605.00812v2) 将 categorical univalence 与标准
univalent universe 区分，并给出前者不蕴含函数外延性的模型。这里登记两条不同主张：

- 标准宇宙单价性 ⇒ universe 内的函数外延性（C14/C15、Book §4.9）；
- 较弱 categorical univalence 不一般 ⇒ 函数外延性（上述论文）。

这不是推翻 Book 定理，而是公理身份与强度需要精确化。本轮核查论文摘要/版本，未重建其模型。

## 核心闭合检查

本页覆盖 A.2 所列全部 11 个 subsection（其中 Contexts/Structural/Universes/Π/Σ/+/0/1/N/Id/Definitions），A.3 的两类 subsection，以及 A.1 的 W 与 η 差异，另定位 A.4 的边界。

全量原始规则仍在固定 formal.tex 中。这里的“核心覆盖”指每个规则家族有条目和来源，不声称逐条省略合同性规则均已重新形式化；上游的省略和未定一般 HIT 语法不会因我们列出表格而消失。
