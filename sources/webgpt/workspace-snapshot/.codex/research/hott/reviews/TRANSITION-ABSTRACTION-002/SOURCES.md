# R038 来源与推导分界

## 当前原始基线
- 用户本轮原消息：继续。
- 恢复包：HoTT_transition_abstraction_rev37_with_git.zip；真实SHA、Git及所有基线文件见artifacts/r038/RESTORE.json。
- R036全文：.codex/research/hott/reviews/TRANSITION-ABSTRACTION-001/PROOF_NOTE.md。本轮继承其存在关系像与有限反例，不改旧结论。
- 当前三问v6、第五闭包§22、AGENTS/业务Skill v1.3.4：已有能力、共有界限、具体新增失真分开。没有新的Gemini来信或用户哲学原话。

## 本地固定的HoTT Book
commit 578b85cc8d586b1677ec4335148adeb443057d24。
- HoTT/theory-schema/upstream/book-578b85cc/hits.tex L1210–1234：商映射满射，商递归要求关系保持，目标为集合。
- HoTT/theory-schema/upstream/book-578b85cc/logic.tex L801–838：命题截断目标为命题时的消去及唯一选择方法。
- 本轮用这些规则推导后继谓词下降和Acc迁移；不是原书逐字陈述了本轮的全部定理。

## 本轮一手在线核查（2026-09-11）
1. https://cj-xu.github.io/agda/constructive-ordinals-in-hott/Cubical.Induction.WellFounded.html
   作者项目托管的Cubical源文件渲染。网页实际显示--cubical --safe、Acc、isPropAcc及其递归定义；仅来源阅读，未在本机编译，也没有锁定其仓库commit。关系方向与本轮R相反，明确用R^op对应。
2. https://agda.github.io/cubical/Cubical.HITs.PropositionalTruncation.Properties.html
   官方库页面，rec要求目标isProp。本轮页面阅读，不认证所有版本与扩展。
3. https://raw.githubusercontent.com/HoTT/book/578b85cc8d586b1677ec4335148adeb443057d24/hits.tex
   读取成功，固定版本与本地对应。

失败与未采用：官方WellFounded.html及raw master WellFounded.agda访问出现cache miss；没有报告成下载成功。还读到作者的HoTT_Markov页面，页面含额外“arith : forall A,A”草稿公理，因此不将该整个文件作为可靠机器证明，亦不依赖它取得本轮结论。

上述网页未通过容器下载存成仓库源码。本文件保存准确出处、阅读范围与关键接口；本地fixed Book保留原字节。不要将本说明当作下载原件或内核日志。

## 本轮新推导
PROOF_NOTE §2为后继关系下降/当前态提升/有限相容路径的构造等价；§3为在函数外延性下借isPropAcc进行截断消去的良基证明迁移；§5–6为无限分支倒计时及相容逆极限反例。均提供纸笔证明，不认领原创性。有限程序的测试不覆盖一般宇宙与无限定理。
