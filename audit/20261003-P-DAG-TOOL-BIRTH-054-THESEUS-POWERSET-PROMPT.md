# P-DAG-TOOL-BIRTH-054：脱敏替换历史／快照身份 blind prompt

```text
You are a blind P-DISCOVERY mapper. Do not use tools, files, web, project history,
prior answers, or delegation. Give only a public D0–D5 DiscoveryTrace (at most 350
English words), never hidden reasoning.

Pattern profile: A finite artifact has components from a universe U. Its current state
is represented only by the subset of components currently present. A process can replace
one component at a time. One trace starts with an artifact and gradually replaces every
component; another trace later assembles an artifact from the removed original components.
At some endpoints, two traces can have the same current component subset while carrying
different histories. The representation treats states with the same current components
as equal and does not retain the trace. A downstream task asks whether an endpoint is
the same continuing artifact as the initial one, and says that replacement history may
matter to a correct answer. No source theorem, actual theory, implementation, consumer
contract, or real-world result is supplied.

Identify at most one concrete pattern clue. Do not treat subset equality itself as the
answer. In D3, attempt containment in all three existing tool roles: P1 object/formation/
same-task, P2 representation/bridge/reentry/polarity, P3 stages/admission/completion.
For each, say what is preserved or lost. Then give exactly one provisional verdict:
OLD_TOOL_FIELD_GAP, DERIVED_TOOL_CANDIDATE, UNCONTAINED_PATTERN_CANDIDATE, or
NOT_ENOUGH_EVIDENCE. A new numbered tool is never an output of this run.

D0 scope/exclusions.
D1 pattern object, process, observation, Done, and a nearby control where history is kept.
D2 exactly one final line beginning literally with MODEL_RECALL_SITE_CANDIDATE,
   or exactly one of these whole lines:
   NO_MODEL_RECALL_CANDIDATE / DIRECT_PAYMENT_ONLY
   NO_MODEL_RECALL_CANDIDATE / FORMATION_ORIGIN_NOT_SUPPLIED
D3 candidate plus P1/P2/P3 containment attempts, one minimal distortion witness, and
   the provisional Tool-BirthCard verdict. If none, explain why.
D4 source validation, actual theory, theorem, new tool, UR, and reality status remain UNKNOWN.
D5 a source fact or control that would falsify the terminal line.

Do not claim a theory defect, theorem, actual consumer, Q location, or UR.
```
