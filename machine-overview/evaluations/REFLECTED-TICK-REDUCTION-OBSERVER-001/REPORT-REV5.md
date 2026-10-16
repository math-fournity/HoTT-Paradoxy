# Reflected tick / proof-termination evaluation：evolution-stable replay closure

> Current evaluation revision：`REFLECTED-TICK-REDUCTION-OBSERVER-005`  
> Current run：`20260914-REFLECTED-TICK-REDUCTION-OBSERVER-005`  
> Deterministic SHA-256：`69db8953ea10d57ca81bc0fca0eaca74d97c4063ed606cec94bead3f8667829b`  
> Current verdict：`HOST_SYNTAX_OBSERVATION_WITH_OBJECT_LEVEL_CONGRUENCE_FENCE / EXPLICIT_TERMINATION_ASSERTION_CAN_MAKE_PROOF_CHECKING_NOT_COMPLETE`  
> HoTT reality-relative status：`NOT_ESTABLISHED`  
> Gödel status：`GENERIC_SELF_REDUCTION_CALIBRATION_ONLY`

## 1. The evidence-lifecycle correction

Revision 4 successfully refreshed the live `HoTT/formal` denominator and reproduced all ten probes. It also showed that coupling every replay to the **current** whole formal tree would make any unrelated future theorem package invalidate the operational probe receipt again.

Revision 5 separates two evidence lifecycles:

1. the reflection/termination probes bind their exact compiler, guarded library, Cubical library and probe sources;
2. the project formal-tree statement binds a finite historical snapshot rather than claiming that the tree will never grow.

`FORMAL-TREE-SNAPSHOT-REV5.json` contains an exhaustive 99-file manifest with per-file bytes and SHA-256, aggregate tree identity, 50 Agda/literate-Agda sources scanned, the exact annotation regex and zero matches. The snapshot itself is a pinned source artifact in `SCOPE-REV5.json`, with three independently rechecked anchors. The live `HoTT/formal` directory is no longer a dynamic `trees[]` dependency.

This change does not weaken the historical claim. It fixes its quantifier:

```text
At the revision-5 snapshot, all 50 formal Agda sources contained zero
TERMINATING / NON_TERMINATING / NO_TERMINATION_CHECK declarations.
```

It no longer makes the unmaintainable claim that future formal sources must preserve the same aggregate tree hash for old probe bytes to remain reviewable.

## 2. Freeze and source qualification

| Item | Revision-5 result |
|---|---|
| freeze deterministic SHA | `49c190d004323da1d17bb666f0ee7808091a16a8054bf0d91989fd5c12bb0cd0` |
| decisions deterministic SHA | `3493a929407bd78ce32e2f57f64472d14b5c5eddf7061057aef2112e6fa27271` |
| source systems | 5 |
| pinned artifacts | 10 |
| anchors | 26/26 found |
| dynamic source trees | Cubical v0.9、guarded source、historical checker tests、historical checker examples |
| frozen project-formal snapshot | 99 files / 384,804 B / tree SHA `925765a8…1ad4`; 50 source files; 0 annotation matches |

The scope, expected result classes and future paths were frozen before the ten `Rev5*` probes, decisions, run and this report existed.

## 3. Native results and replay

| Classification | Probe IDs |
|---|---|
| `KERNEL_ACCEPTED` | P01, P03, P06, P09 |
| `EXPECTED_TYPE_REJECTION` | P02, P04, P05, P08 |
| `EXPECTED_OBSERVATION_LIMIT` | P07, P10 |

All first/replay pairs have the same exit code, stdout and stderr. A separate `verify --rerun` executes all ten commands again and reports `exact_recorded_output=true` for every probe.

The two historical refresh failures remain in revision 2/3 and are described in `REPORT-REV4.md`. They explain the immutable evaluator’s path/module contract and are not hidden by revision 5.

## 4. Mathematical scope

The operational conclusion is unchanged:

- reflection distinguishes particular syntax supplied at a call site;
- Path-respecting object functions cannot retain an incompatible Boolean distinction;
- ordinary termination checking and the certified fragment reject the direct unproductive definition or its override;
- explicitly asserting termination can expose an unbounded reduction when proof checking forces a different normal form;
- an opaque recursive definition gives finite rejection;
- guarded productive infinitude reaches the delay boundary and completes.

The Gödel work added elsewhere now contains actual natural-number proof codes, an exhaustive proof/refutation classifier and a conditional essential-incompleteness theorem. Those packages do not retrofit P07/P10 into Gödel instances: these two probes still depend on a manually asserted recursive equation, do not construct a represented independent sentence, and have no HoTT-specific natural consumer or reality bridge.

## 5. Verification status

```text
current run: REFLECTED_TICK_REDUCTION_TERMINATION_VALID
native rerun: 10/10 exact recorded output
focused tests: 8/8 PASS
historical revision 1: stale detected as designed
revision 2/3 failures: preserved
Git: LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED
```
