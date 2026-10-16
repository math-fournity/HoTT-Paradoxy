# 实数分离原则的原典定位

本文件记录来源对照，不把原典陈述冒充本项目已机器证明的额外定理。访问日2026-09-20。

主要依据为[HoTT Book固定版本reals.tex](https://raw.githubusercontent.com/HoTT/book/578b85cc/reals.tex)，本地已固定副本`HoTT/theory-schema/upstream/book-578b85cc/reals.tex`。本地337–352行区分非相等与apartness，并陈述可逆性与apartness的关系；3205–3220行练习`ex:reals-apart-neq-MP`要求从全实数对的非相等→apartness推出二进制Markov原则，同时将逆方向作为问题提出。这里只登记原典内容；未声称本轮已经形式化该Markov蕴含或其逆方向。

固定agda-unimath的`src/logic/markovs-principle.lagda.md`把Markov's-Principle定义为is-markovian ℕ；`src/logic/markovian-types.lagda.md`用bool值谓词、否定处处为真和mere存在假值表达它。与书中双否定存在真值的写法需要显式翻译，名称一致不代替证明。

本轮RealNonzeroApartness在固定Dedekind ℝ₀上量化；从零点形式到全点对形式也应明确写出差运算归约。不能因某些构造分析文献采用Cauchy实数或不同选择前提，就直接宣布本模型原则与标准二进制Markov原则等价。

检索另定位到作者讲义[Introduction to constructive mathematics](https://www.speicherleck.de/iblech/stuff/algar-lecture-notes.pdf)及出版方的[Axioms for constructive fields](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/axioms-for-constructive-fields/3BA07D95AAD3C2B3F2B151C6B9A30B20)。本轮未完成其全文/前提对账，不用其摘要作为数学前提；后续按精确需要再消费。
