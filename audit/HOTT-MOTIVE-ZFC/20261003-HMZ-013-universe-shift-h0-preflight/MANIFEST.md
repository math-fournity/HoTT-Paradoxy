# HMZ-013：type-theory universe 与 Grothendieck universe 的 H0 传输预检

> **身份：** `SOURCE_PREFLIGHT / EXISTING_AUTHOR_SOURCE_NEW_H0_LOCUS / UNIVERSE_SHIFT_CONTROL / ADMISSION_REJECTED_WITH_SCOPE / NOT_A_FULL_DENOMINATOR_RUN`。

## 预检问题

Voevodsky 2013 把 Coq-style type-theory universes \(U_i\) 的 univalent model 放在“ZFC with \(\omega+2\) universes”中；每个 \([U_i]\) 的 simplices 被要求属于第 \(i\) 个 set-theoretic universe。Shulman 2008 则分析以 inaccessible \(\kappa\) 得到的 Grothendieck universe \(V_\kappa\)，以及在不同 universe 间改变“small”范围时，某个对象是否仍是同一个对象。

这是否给出用户所说 `H0→Z0→Q0` 的正向传输：HoTT universe-level sameness/completion 现象在 ZFC 的 universe shift 中有同一对象、同一过程、同一观察和同一 Done 的对应物？

## 冻结来源

| ID | 类 | 来源 | 已归档身份 | 本轮 locator 与作用 |
|---|---|---|---|---|
| `HMZ-S-012` | A/B | Vladimir Voevodsky, *Univalent Foundations and Set Theory*, 2013-05-08. | [HMZ-002 原件](../20261003-HMZ-002-voevodsky-set-theory/originals/HMZ-S-012-Voevodsky-2013-Univalent-Foundations-and-Set-Theory.pdf)，SHA-256 `bf2e5e71f00503d0d9297ceada068ee698bf0d1fcc2b14496d6b462927aecbeb`. | Slides 12–18 / derived lines 173–263：type universes、set-theoretic universe number、model consistency benchmark。 |
| `HMZ-S-010` | C/D/E | Michael Shulman, *Set Theory for Category Theory*, arXiv:0810.1279v2, 2008. | [HMZ-001 原件](../20261003-HMZ-001-primary-motives/originals/HMZ-S-010-Shulman-2008-Set-Theory-for-Category-Theory.pdf)，SHA-256 `3f1e2d9f9a7a026ab54cd982cfad8742c9c38e9696cb60b52e18dfaa90298012`. | PDF pp. 15–17, 21–22 / derived lines 740–814, 1045–1090：\(V_\kappa\)、inaccessibles、Grothendieck universe 与 universe-juggling consumer control。 |

`originals/README.md` 和 `derived/LOCATORS.md` 只指回上述 hash-pinned 原件；本预检没有复制或改写来源。

## 来源支持的对应与控制

```text
HoTT/model side:
  U_i is interpreted using fibers whose simplices lie in set-theoretic universe i.
  The model assumes ZFC with ω+2 universes, rather than bare ZFC.

ZFC/category-theory side:
  V_κ is a Grothendieck universe only when κ is inaccessible; ZFC does not
  prove an inaccessible exists. A universe change changes which sets/groups
  count as small.

actual consumer/control:
  Shulman's G/H example says a statement “there exists a small G such that
  φ(G,H) for all small H” may hold relative to each inaccessible, while there
  is no a priori reason that the same G persists or works for all groups.
```

## T0–T5 disposition

| Gate | Result |
|---|---|
| T0, ZFC one-level object | `PARTIAL_ONLY` — \(V_\kappa\) is a model/set under an inaccessible, not the bare-ZFC universe or a direct object-language counterpart of a HoTT universe. |
| T1, formation/interface | `SOURCE_PAYMENT` — inaccessible assumption, \(V_\kappa\), and redefinition of small/large are explicit. |
| T2, subject/process/observation/Done | `FAIL` — HoTT universe identity/completion and category-theory universe-relative quantification ask different tasks. |
| T3, unpaid completion | `FAIL` — sources make the stronger universe assumption and scope switch visible. |
| T4, P2/P3 reentry/admission | `NOT_SUPPLIED` — no same-object negative reentry or pending formation transition. |
| T5, controls | `PASS_AS_CONTROL` — Shulman explicitly warns that one cannot infer the same \(G\) after changing universes. |

```text
H0→Z0: NOT FORMED
Q0: UNFORMED
next disposition: ANTI_ANALOGY_CONTROL + SOURCE_PAYMENT
SUCCESSOR RUN: ADMISSION_REJECTED_WITH_SCOPE
```

The preflight does not say that universe shifts are uninteresting. It says the best source-level consumer found here already refuses the identity/same-Done inference that an H0 transport would require.
