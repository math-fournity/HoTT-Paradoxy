# Bliudze--Furic 2014：standard-real Zeno 与 operational-time repair source snapshot

> **身份：** `PRIMARY_PUBLISHED_SOURCE_SNAPSHOT / C0R11_SHARED_SIMULATION_TASK_CANDIDATE / NOT_A_BARE_ZFC_VERDICT`。

## 原件

| field | value |
|---|---|
| authors | Simon Bliudze, Sébastien Furic |
| title | *An Operational Semantics for Hybrid Systems Involving Behavioral Abstraction* |
| publication | Proceedings of the 10th International Modelica Conference, 2014, pp. 693–706; DOI `10.3384/ECP14096693` |
| official PDF | `https://ep.liu.se/ecp/096/073/ecp14096073.pdf` |
| PDF | `Bliudze-Furic-2014-Operational-Semantics-Hybrid-Behavioral-Abstraction.pdf`; 14 pages; SHA-256 `f4553082176decad3b555d0e89367ea52d171609be10298b09c6d18893624750` |
| derived text | `Bliudze-Furic-2014-Operational-Semantics-Hybrid-Behavioral-Abstraction.txt`; `pdftotext` reading aid; SHA-256 `e8887f02301eebe6d53e689052b90d03a31ccdbecc79dd10b29998686a269298` |

## Original-page visual checks

| PDF / printed page | verified content |
|---|---|
| PDF p.2 / p.694 | static semantics, discrete execution steps, adaptive discretization and compositionality requirements; prior models may preserve neither causality nor Zeno-freeness. |
| PDF p.3 / p.695 | explicit Modelica bouncing-ball model, `t_i` / `v_i`, standard-real time assumption, and geometric decrease of bounce durations. |
| PDF p.4 / p.696 | total bounce-time convergence; the source says the Zeno effect prevents the model from moving beyond its convergence limit, and a simulator that does so is not executing the alleged semantics. |

## Scope boundary

The source gives a language/model-level task, not an empirical proof about an actual ball. Its non-standard repair is a semantic construction with explicit extra temporal structure; no claim in this source assigns a general adequacy duty to bare ZFC.
