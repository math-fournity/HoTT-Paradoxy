# R3→R4 Gödel 保真义务矩阵

状态：`R3_MACHINE_REPLAYED_R4_OBLIGATION_MATRIX_COMPLETE_WITH_SCOPE`  
source snapshot：`a00927f2239dfc227ce6ed9143c5210453153c5c89e8cf4aad7d03005146461a`  
R3 source：`MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001` / C-244–C-249  
R4 target slice：`MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001` / C-223–C-226

## 判词

R3 的一般 essential incompleteness 与 Robinson Q 条件独立句已在 Coq 8.15.2 中从 exact source archive 重放。它尚未成为 HoTT 不完备性定理。12 项 R4 义务中，`PRESENT_MACHINE_PROVED`=2、`ABSENT_BY_DEFINITION`=3、`OPEN`=7；R4 readiness=`NOT_READY`。

## 逐项矩阵

| 义务 | 状态 | 当前已有 | 要闭合的缺口 |
|---|---|---|---|
| `H-SYNTAX` | `PRESENT_MACHINE_PROVED` | Four-sort Con/Sub/Ty/Tm Cubical HIIT syntax with terminal context, context extension, U/El, Pi, lambda/app, beta/eta, truncation constructors and second-order coherence. | Nat, general object identity/Path, object univalence/HIT, and a single complete raw HoTT calculus. |
| `H-CONVERSION` | `OPEN` | The HIIT syntax carries judgmental/path equations and coherence constructors. | No total executable conversion or derivation checker for the exact quotient/HIIT object syntax has been constructed. |
| `H-NAT` | `ABSENT_BY_DEFINITION` | No Nat constructor occurs in the frozen TT syntax module denominator. | Nat formation, zero, successor, eliminator, computation rules, addition/multiplication and coding arithmetic. |
| `H-ID/PATH` | `ABSENT_BY_DEFINITION` | Cubical paths are used by the host to define the HIIT and prove coherence. | A general identity/Path type former and its formation/introduction/elimination/computation rules inside the object calculus. |
| `H-UNIVALENCE/HIT` | `ABSENT_BY_DEFINITION` | U/El and the syntax HIIT itself are present at the host/formalisation level. | Object-level univalence and named higher-inductive type rules in the exact calculus. |
| `H-PROOF-CODE` | `OPEN` | C-157-C-187 provide proof/formula coding for a separate small K/S/MP system. | Natural-number code, decoder, total checker and fair proof enumeration for derivations of the same HoTT calculus named by H-SYNTAX. |
| `H-SUBSTITUTION` | `PRESENT_MACHINE_PROVED` | The groupoid syntax has typed substitutions, composition, identity, action on types/terms, and second-order coherence. | An executable capture-avoiding formula substitution operation on a proof-coded arithmetic/HoTT language suitable for diagonalisation. |
| `H-ARITH-INTERP` | `OPEN` | R3 Coq source formalises Robinson Q and its standard first-order arithmetic infrastructure. | A machine-checked interpretation of Q or another sufficient arithmetic theory into the exact H-SYNTAX calculus. |
| `H-REPRESENTABILITY` | `OPEN` | C-246 assumes strong separation; the author R3 development proves it for its first-order arithmetic route. | Object-level strong representation of the HoTT proof predicate, coding and substitution functions in the target calculus. |
| `H-FIXPOINT` | `OPEN` | The R3 package contains the recursive-separation/diagonal mechanism for its source theory. | A fixed-point/diagonal lemma whose quotation and substitution operate on the exact target HoTT derivation syntax. |
| `H-INDEPENDENCE` | `OPEN` | C-246 and C-248 establish conditional independence in general formal systems and Robinson-Q extensions. | An independent sentence theorem with the target T instantiated to the exact HoTT calculus and every premise discharged or retained explicitly. |
| `H-EFFECTIVITY` | `OPEN` | The R3 source theory assumes/proves enumerability in its own first-order setting; finite host source files type-check. | Effective enumeration of the exact target rule/axiom schemas and proof relation, including the status of univalence, HIT, resizing, quotient or oracle rules. |

`H-SYNTAX` 与 `H-SUBSTITUTION` 的机器状态只覆盖当前 groupoid syntax 的结构层。宿主 Cubical Agda 的 Path 与 HIIT 能力不自动成为对象 calculus 的 `H-ID/PATH` 或 `H-UNIVALENCE/HIT`。C-157–C-187 的 proof code 属于另一小型系统，也不能直接填 `H-PROOF-CODE`。

## 下一最小切片

`R4-HOTT-NAT-EFFECTIVITY-001`：Choose or extend one exact target syntax with Nat and a finite derivation representation, then machine-check one end-to-end encoded derivation and a negative control.

禁止把 representability、universality、consistency 或 proof predicate 作为未证明 constructor/postulate 添加；那会把最主要的 Gödel 义务写进假设。

## 边界

本矩阵证明的是“当前证据在哪些义务上存在或缺失”的完整登记。它不证明缺口不可实现，不证明 exact HoTT R4，不证明 HoTT essentiality，也没有建立现实同任务桥梁。
