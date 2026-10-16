class Term: pass

class Bool(Term):
    def __init__(self, val): self.val = val
    def __repr__(self): return "true" if self.val else "false"

class Not(Term):
    def __repr__(self): return "not"

class App(Term):
    def __init__(self, f, arg): self.f = f; self.arg = arg
    def __repr__(self): return f"{self.f}({self.arg})"

class UA(Term):
    def __init__(self, equiv): self.equiv = equiv
    def __repr__(self): return f"ua({self.equiv})"

class Transport(Term):
    def __init__(self, path, val): self.path = path; self.val = val
    def __repr__(self): return f"transport({self.path}, {self.val})"

class Trunc(Term):
    def __init__(self, val): self.val = val
    def __repr__(self): return f"|{self.val}|"

class Unquot(Term):
    def __init__(self, trunc_val): self.trunc_val = trunc_val
    def __repr__(self): return f"unquot({self.trunc_val})"

class OracleProof(Term):
    def __repr__(self): return "Oracle_Proof_From_Logic"

def reduce_eval(term):
    """模拟底层形式化系统（如Lean/Coq）的判断归约（Judgmental Reduction）过程"""
    if isinstance(term, App):
        f_red = reduce_eval(term.f)
        arg_red = reduce_eval(term.arg)
        if isinstance(f_red, Not) and isinstance(arg_red, Bool):
            return Bool(not arg_red.val)
        return App(f_red, arg_red)
        
    elif isinstance(term, Transport):
        path_red = reduce_eval(term.path)
        val_red = reduce_eval(term.val)
        # 悖论2的核心：书本版HoTT中，ua（单价公理）是公理，没有对应的执行规则！
        # 即使逻辑上它等同于执行 not，但在机器底层，求值器无法让它“走”过去，卡死了。
        return Transport(path_red, val_red)
        
    elif isinstance(term, Unquot):
        trunc_red = reduce_eval(term.trunc_val)
        # 如果是真正构造出来的截断值，可以提取
        if isinstance(trunc_red, Trunc):
            return reduce_eval(trunc_red.val)
        # 悖论1的核心：如果是通过纯逻辑（Oracle/排中律）得到的截断证明，底层没有见证人！
        return Unquot(trunc_red)
        
    return term

print("=== 机器求值器运行结果 ===")
# 正常的时间计算
normal_calc = App(Not(), Bool(True))
print(f"正常计算 (ASK 合法): {normal_calc}  --->  {reduce_eval(normal_calc)}")

# 悖论2：单价公理异化时间的卡死
hott_ua_calc = Transport(UA(Not()), Bool(True))
print(f"HoTT单价公理计算 : {hott_ua_calc}  --->  {reduce_eval(hott_ua_calc)}")

# 悖论1：命题截断掩盖不停机的卡死
hott_trunc_calc = Unquot(OracleProof())
print(f"HoTT命题截断提取 : {hott_trunc_calc}  --->  {reduce_eval(hott_trunc_calc)}")
