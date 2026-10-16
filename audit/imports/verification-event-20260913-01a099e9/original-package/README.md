# 实例结果：过去尚未验证，可以在后来被正确核查

本文件回答“你认为你可以做出实例来吗？”这一次实际构造的结果。

**我做出了原生 Cubical Agda 可以检查的具体实例。但是，它没有成为用户所要求的 HoTT 自身非现实性实例。相反，这个最小构造显示：保留时标时核查可以完成；把过去换成现在才会出现冲突，而这种转换被类型检查拒绝。**

这使上一份《验证事件与时标自反》中的最短候选获得了实际判别，不再只是纸面设想。结果不支持把本例升格成 HoTT BUG，也不证明所有相关候选都不可能。

## 一条完整的小链

固定一个简单的真命题 P。为排除原子命题计算本身的困难，源码把 P 取为 Unit。这个选择只让我们专注于证据的登记状态，不用未知数学事实制造困难。

模型有三个快照、两个事件和有限的命题代码：

| 快照 | 已登记的证据 | 下一事件 |
|---|---|---|
| initial | 无 | issueP：取得 P 的证据 |
| afterP | P 的证据 | recordHistory：记录对初始状态的核查 |
| afterHistory | P，以及“P成立且初始时尚未验证P”的证据 | 本次实验结束 |

登记关系 Registered 由源码中的三个构造子精确限定。K(s,c) 定义为这个关系的命题截断，表示在指定快照存在该命题的登记；它不是“在宇宙某处有一个证明”，也不是关于所有数学命题的知识算子。

关键的两种陈述是：

    Historical = P × ¬K(initial, P)
    Current(s) = P × ¬K(s, P)

Historical 固定谈论初始状态；Current(s) 随被考察的状态改变。模型明确允许后来登记并核查 Historical。全部登记都具有符合各自命题解释的证明，这一点在 knowledgeSound 中逐构造子证明，再经原生截断消去得到；没有把“HoTT自身全局健全”作为公理加入。

这是一个有限、受控的事件/登记模型，不是任意证明代码的检查器，不是自动发现证明的算法，也不是现实观察者的完整模型。

## 实际证明了什么

对应的精确源码符号和运行证据见 [命题—证据矩阵](HoTT/CLAIM_EVIDENCE_MATRIX.md)。所有数学判断均限制在上述定义内。

1. **后来能够正确核查过去。**historicalKnownLater 和 historicalVerifiedLater 给出明确证据；没有被“过去尚未知”阻塞。
2. **“当前尚未验证”在快照变化后有不同状态。**initialCurrentWitness 给出初始证据；currentFalseAfterP 和 currentFalseAfterHistory 排除两个后续快照的对应陈述。decideCurrent 是这个有限模型的带证明判定器，初始为 yes，后续为 no。
3. **不能把过去命题直接转成后来仍未验证的命题。**noHistoricalToCurrent 排除 Historical → Current(afterP)；noStageIndependentTruthPath 排除这两个相关命题类型的原生 Path 相等。
4. **完全擦除阶段不能保持当前判断。**把 Stage 做高阶归纳命题截断后，noTruthFaithfulStageErasure 证明不存在能在所有阶段与 Current(s) 双向对应的谓词族。源码保留阶段的 stageAwareFamily 则提供正控制。
5. **一个条件化的 Moore/Fitch 逻辑核可以核查。**noKnownMoore 在明示的事实性与合取消去封闭参数下给出否定结果。它没有证明全部可知性悖论，没有引入可知性原则，也没有证明 HoTT 自己具备该全域知识接口。

第4项确实使用了原生 Cubical Path、类型运输与高阶归纳截断，不是用普通 Lean Eq 或 Python 模拟器代替。没有调用 univalence；不主张这个机制为 HoTT 独有或本次原创。

## 负向校准：让错误真的交给内核

我另外写入了一个故意错误的转换：

```agda
bad : Historical → Current afterP
bad q = q
```

Agda实际拒绝，原始报文指出：

```text
error: [UnequalTerms]
afterP != initial of type Stage
when checking that the expression q has type Current afterP
```

这里不是主证明没有写完；主证明已经证明该转换不存在。BadCast.agda 是用来确认错误转换确实会被拒绝的受控输入，不能作为通过的证明文件引用。[拒绝收据](HoTT/verification/runs/negative-001/RUN.json) · [原始输出](HoTT/verification/runs/negative-001/stdout.txt)

## 对上一候选的裁决

如果“实例”指在 HoTT 风格原生系统中可以完整形式化的时序现象，这次已经完成一个：某个初始成立的“当前未知”陈述，在证据登记后不再成立，而关于那个过去状态的陈述仍可核查。

但用户真正要求的是 HoTT 的某种合法理论化自身产生现实相对的非现实性。**这次没有达到这个目标。**我们看到的是：一旦准确表达被谈论的状态，理论能够保留需要的区别；试图完全抹去区别再保持原判断时，所需的函数/类型路径没有得到许可。

因此，我不能用这个实例宣布“HoTT里出现了矛盾”。也不能把“换了命题而被拒绝”叙述成“现实可做，HoTT却做不了”。本例中的现实对应任务——后来核查固定过去——在模型中已经有正向构造。

这一结果只处置了当前明确定义的最小模型。它没有证明 HoTT 的所有时间/时序处理都充分，也没有处理芝诺的运动、时空非连续性与理论稠密性问题。它同样没有完成任何新的 Gödel 不完备性实例。

下一次如果仍沿此族研究，必须拿出新的、具体的理论化步骤或任务关系；仅改命题名称、增加快照或把语法调试再拆成多个小单元，不足以重新赋予本候选更强的资格。

## 工具、证明与失败留存

工具：Agda 2.8.0-3d04bac；用户源码使用 --safe --cubical；交付命令使用 --ignore-interfaces 和 --no-libraries。源码依赖仅为该工具自带的原语模块与本文件定义的高阶归纳截断，无外部 Cubical 库依赖。

Agda可执行文件只读复用本机已固定版本，SHA-256 为 ac285c193c30ed0f5e1073a2623ae312c7165a4d344940b5c504ce6a2fe1741e。原语运行数据与所需内建接口缓存已复制到本独立目录，构建缓存与临时目录也在这里；未写共享工具链目录或当前repo。

| Run | 结果 | 解释 |
|---|---|---|
| attempt-001 | exit 154 | 隔离运行数据的启动内部错误，尚不能评估候选 |
| smoke-001 / smoke-002 | exit 154 | 单元素类型也报同样错误，排除把它直接归因于候选 |
| smoke-003 | exit 0 | 私有复制本机现有内建接口缓存后可运行 |
| attempt-002 | exit 42 | 用户源码的否定算子宇宙层级不够；旧源码和输出保留 |
| attempt-003 | exit 0 | 将 Not 正确写为层级多态后，完整主模块通过 |
| negative-001 | exit 42，符合预期 | 错误时标转换被 UnequalTerms 拒绝 |
| negative-002 | exit 42，符合精确报文预期 | 捕获器收紧为核对错误码、文件行号与具体时标差异后重跑；不再将任意失败视为负向校准成功 |
| positive-final-001 | exit 0 | 独立重跑，stdout/stderr 与 attempt-003 精确一致 |

启动问题的观察边界是“复制现有内建接口缓存后恢复”。本轮没有调查出可外推的 Agda 根因，也没有把工具启动异常当成数学悖论。第一次缓存复制曾因目标已有生成文件而停止，随后先保存已有缓存到 build/pre-cache-replacement 再复制；相关失败运行未删除。

每个交付run包含 RUN.json、stdout.txt、stderr.txt、environment.txt、source-manifest.json；最终run还包含源码快照、捕获脚本、内建接口输入哈希和命题索引快照。依赖源码与运行时数据的哈希已逐个回查。

**证明状态：FORMAL_CHECKED_WITH_SCOPE / EXTERNAL_ISOLATED_PACKAGE。**源码与结果都持久保存在 D 盘，不在 /tmp；根据用户并发边界没有导入共享 repo 的 formal/run/index，也未提交 Git，故为 LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED。不能把这个独立包称为共享项目的已合并结果。

## 查看与重跑

- [主证明源码](HoTT/formal/VerificationEvent.agda)
- [精确命题索引](HoTT/CLAIM_EVIDENCE_MATRIX.md)
- [最终运行收据](HoTT/verification/runs/positive-final-001/RUN.json)
- [最终原始输出](HoTT/verification/runs/positive-final-001/stdout.txt)
- [错误转换源码](HoTT/formal/BadCast.agda)
- [运行捕获器](run_proof.py)

在本目录运行下列命令，必须使用未出现过的run名称；旧run不会被覆盖：

```sh
python3 run_proof.py my-replay-001
python3 run_proof.py my-negative-001 --negative
```

捕获器的退出码会区分测试预期；负向测试时 Agda 的原始42退出码保存在RUN.json中，不被改成内核成功。

## 用户问题与工作边界

> 你认为你可以做出实例来吗？

本次沿用先前明确的 repo 外隔离要求，实际进行了构造、原生检查、错误输入校准和重跑。当前共享repo和共享对话归档均未修改。继承本对话中已加载的用户原始问题意识；本包不声明新的完整三件套冷启动认证。
