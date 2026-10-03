# HMZ-013：universe shift 的消费者与反类比控制

## Candidate comparison

| Field | HoTT/model source | ZFC/category source | Same-task result |
|---|---|---|---|
| object | type universe \(U_i\) and its fibration semantics | Grothendieck universe \(V_\kappa\), small/large sets/groups | `NOT_IDENTIFIED` |
| formation | model constructed relative to a hierarchy of set-theoretic universes | choose inaccessible \(\kappa\); use \(V_\kappa\) as small universe | explicit assumptions / different layers |
| consumer | type-theory interpretation and consistency benchmark | category-theory theorem relative to “all small H” | no common consumer contract |
| observation | fibers / simplices / type-theoretic universe | rank/smallness / existence of G relative to \(\kappa\) | different observation spaces |
| Done | univalent model extends / consistency relative to a universe structure | theorem under a fixed universe convention | `NOT_SAME_DONE` |

## Source controls

1. **Assumption control.** The Voevodsky source uses ZFC with \(\omega+2\) universes. The Shulman source uses `ZFC+I`/inaccessibles. Neither source permits silently replacing this with bare ZFC.
2. **Scope control.** “Small” is relative to \(V_\kappa\); changing \(\kappa\) changes the consumer’s domain.
3. **Identity control.** Shulman explicitly says there is no a priori reason a particular witness \(G\) remains the same after universe change, or that it satisfies the property for all groups.
4. **P control.** No source treats an as-yet-unformed universe as a downstream operator input, and no same-object negative reentry/admission cycle appears.

The important result is therefore a **well-specified guard**: a source could only revive this route by supplying an actual consumer that ignores these explicit universe/scope payments while claiming a fixed same-object, same-Done deliverable.
