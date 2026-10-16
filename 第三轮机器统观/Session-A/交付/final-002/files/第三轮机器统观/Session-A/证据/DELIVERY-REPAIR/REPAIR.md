# 封存副本校验接口的真实失败与修正

本单元检验的是四个既有原生证明包怎样在固定交付副本中核查证据，未改变数学命题、源码、run或现实桥。结论ID为MO3-J-FINAL-13。

final-001的2,064文件字节seal/live/after校验均通过，manifest为8f49c74f9db9c2967a3e19ad11749c3d0ed748414f89516080619e2b0fb3d404，subject为b4fbad4e6532cebe96cfb2eb9b562938ba9bf240；原件不修改。seal-only提交499391e056324a1b9c3e0a4fb6932c0263ebf703保留全部字节与失败。

1. `verify_proof_version_closure --evidence-only --project-root <copy>`仍先访问历史Git基线及全registry dependency-gap allowlist；副本未复制不相关旧DiagonalLemma原件，触发LATER_DEPENDENCY_GAP_SOURCE_DRIFT。该工具源码440–535及load_gap_allowlist说明了原因。不能把evidence-only名称猜成完全独立于Git，也不为通过而修改旧原件/例外表或复制整个历史研究。
2. 尝试raw run verifier时，交付说明误把run-dir写成绝对路径，触发UNSAFE_PATH，保存diagnostic-002。源码main显式调用safe_relative。
3. 改成`--run-dir HoTT/verification/runs/<run>`后，四个主run在固定副本全部exit0，保存diagnostic-003。启用-B与PYTHONDONTWRITEBYTECODE，未执行kernel或写A输入。

修正：副本使用已实际通过的raw evidence命令；Git版本检查留在原repo及既有selected四包结果。原生重跑仍需B独占源码/库/XDG副本和路径映射，不直接执行原RUN绝对argv。实际命令与原始输出在交付/final-001-verification。新代次final-002收入该失败/修复证据、更新后的说明和当前方法/研究资产；旧代次不覆盖。

这是具体交付接口纠错，reflection=no-plan-change：没有改变Goal5验收、HoTT命题或给B减少工作；也不把copy evidence PASS冒充B独立语义审计。最终必须重新取得final-002的seal/live与四raw包副本接受，再完成host Goal。
