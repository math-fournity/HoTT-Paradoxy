import GodelQ.ZFC.Z0Full

namespace GodelQ.EnvProbe

/-- Confirms the pinned toolchain compiles the proven package end-to-end. -/
def envOk : True := by decide

end GodelQ.EnvProbe
