# -*- coding: utf-8 -*-
from pathlib import Path

chain = """GodelQ/ProcessObservation.lean
GodelQ/EffectiveTheory.lean
GodelQ/GodelZenoRunner.lean
GodelQ/FoundationArith.lean
GodelQ/ZFC/SetLanguage.lean
GodelQ/ZFC/SchemaDelta1.lean
GodelQ/ZFC/ReplacementDelta1.lean
GodelQ/ZFC/ZFCDelta1.lean
GodelQ/ZFC/NumeralCode.lean
GodelQ/ZFC/NeverRE.lean
GodelQ/ZFC/OmegaArith.lean
GodelQ/ZFC/NumeralSemantics.lean
GodelQ/ZFC/ArithInterp.lean
GodelQ/ZFC/R0Model.lean
GodelQ/ZFC/Effective.lean
GodelQ/ZFC/Soundness.lean
GodelQ/ZFC/OmegaLaws.lean
GodelQ/ZFC/PAModel.lean
GodelQ/ZFC/Z0Shadow.lean
GodelQ/ZFC/Z0PA.lean
GodelQ/ZFC/ShRE.lean
GodelQ/ZFC/InternalTranslate.lean
GodelQ/ZFC/TranslateRE.lean
GodelQ/ZFC/Z0Full.lean
GodelQ/ZFC/Z0Blocked.lean
"""
p = Path("/Volumes/D/HoTT_AI_HANDOFF_20260911/外部资料/Z0-D3-攻关包/收据/BUILD.md")
t = p.read_text(encoding="utf-8")
t += "\n---\n\n## 24 个模块的编译次序（最后一个是要改的）\n\n```\n" + chain + "```\n"
p.write_text(t, encoding="utf-8")
print("chain appended")
