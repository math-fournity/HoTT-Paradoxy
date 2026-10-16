# Reflected tick / proof-termination evaluation：formal-tree denominator refresh

> Evaluation revision：`REFLECTED-TICK-REDUCTION-OBSERVER-004`  
> Run：`20260914-REFLECTED-TICK-REDUCTION-OBSERVER-004`  
> Lifecycle：`SUPERSEDED_BY_REVISION_5_FOR_EVOLUTION_STABLE_REPLAY`; mathematical verdict unchanged  
> Deterministic SHA-256：`c1fcde82ba97d7c1a7cd79473911183c99bf9f3f0a2e9db7ee0398b3cfee8b2f`  
> Mathematical verdict：unchanged  
> HoTT reality-relative status：`NOT_ESTABLISHED`  
> Gödel status：`GENERIC_SELF_REDUCTION_CALIBRATION_ONLY`

## Why a new revision was required

Revision 1 froze the complete `HoTT/formal` tree because its source audit included the claim that no project formal source used `TERMINATING`, `NON_TERMINATING`, or `NO_TERMINATION_CHECK`. Subsequent authorized Gödel/nontermination research added new formal packages. Those additions did not alter any revision-1 probe or source dependency, but they changed the complete-tree denominator:

| Tree | Revision 1 | Revision 4 |
|---|---:|---:|
| `HoTT/formal` files | 83 | 99 |
| bytes | 293,434 | 384,804 |
| tree SHA-256 | `465f9094…715a` | `925765a8…1ad4` |
| termination-annotation matches | 0 | 0 |

The old verifier therefore correctly reports `REFLECTED_TICK_TREE_CHANGED:RT-T3-PROJECT-HOTT-FORMAL`. Treating that report as a stale-evidence signal preserves the original claim’s denominator instead of silently accepting unrelated tree evolution.

## Preserved failed refresh attempts

No frozen file or completed run was overwritten.

1. Revision 2 froze the current tree and completed its source decisions, but its probe directory was a sibling `probes-rev2/`. The immutable evaluator only mounts paths below `probes/`, so run `...-002` stopped before the first native probe. `SETUP-FAILURE.json` records zero native probes.
2. Revision 3 moved the files below `probes/rev3/`, but the copied Agda modules retained unqualified module names. Agda therefore rejected all 20 first/replay invocations at module-path resolution, before target checking. The per-probe raw outputs and a root `SETUP-FAILURE.json` are retained.
3. Revision 4 preregistered fresh top-level filenames and matching `Rev4...` module declarations. Only module identity changed; probe bodies remained the original bodies.

These two failures are evidence about evaluator path/module qualification. They are not mathematical counterexamples and are not counted as successful probes.

## Revision-4 result

`SCOPE-REV4.json` and `FREEZE-REV4.json` were created before the ten new probe files, decisions, run and this report. The scope retains the original fourteen research questions, two qualification gates, three-factor trigger cube and every expected result class.

`DECISIONS-REV4.json` finds all 23 source anchors and redoes the five-tree termination-annotation inventory. The current 99-file project formal tree still contributes zero matches.

All ten native probes match their preregistered classes:

| Class | Probes |
|---|---|
| kernel accepted | P01, P03, P06, P09 |
| expected type rejection | P02, P04, P05, P08 |
| expected observation limit | P07, P10 |

First/replay bytes are exact for every probe. An independent `verify --rerun` reproduces all ten exit/stdout/stderr triples exactly.

## Stable conclusion

The refreshed evidence preserves the original causal result:

- host reflection can distinguish call-site syntax without producing a uniform object-level discriminator that violates Path congruence;
- ordinary termination checking rejects the direct loop;
- the certified fragment rejects the termination override;
- a manually termination-asserted recursive definition can make proof checking continue when a distinct normal form is forced;
- keeping it opaque gives a finite type rejection;
- guarded productive infinitude completes at its delay boundary.

The current Gödel packages do not change this evaluation’s interpretation. They add actual proof codes, a proof/refutation classifier and a conditional synthetic incompleteness theorem elsewhere. P07/P10 still depend on a manual termination assertion and still do not instantiate object-language representability, strong separation, a Gödel sentence, a HoTT-specific cause, or a reality correspondence.

## Verification

```text
freeze rev4: 65640825fe3eced3101c5799137f3466d22c68e78a5e3bd2b481cda896f64834
decisions rev4: 4ca2669adbeade782e717e3b38e4aff141c23db8b9529458e451fecbbc093010
run rev4: c1fcde82ba97d7c1a7cd79473911183c99bf9f3f0a2e9db7ee0398b3cfee8b2f
focused tests: 7/7 PASS
native rerun: 10/10 exact recorded output
Git: LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED
```
