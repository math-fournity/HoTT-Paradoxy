# 构建一个极其严格的极简 HoTT 核心引擎 (Minimal HoTT Kernel)

class Term: pass

# --- 1. 语法树定义 (AST) ---
class BoolType(Term): 
    def __str__(self): return "Bool"

class TrueVal(Term): 
    def __str__(self): return "true"

class FalseVal(Term): 
    def __str__(self): return "false"

class NotFunc(Term):
    def __str__(self): return "not"

class App(Term):
    def __init__(self, func, arg): self.func = func; self.arg = arg
    def __str__(self): return f"{self.func}({self.arg})"

class PathType(Term):
    def __init__(self, A, B): self.A = A; self.B = B
    def __str__(self): return f"({self.A} = {self.B})"

class Refl(Term):
    def __init__(self, A): self.A = A
    def __str__(self): return f"refl_{self.A}"

class UnivalenceAxiom(Term):
    # 单价公理：将等价关系（这里是不仅可逆而且等价的not）异化为静态的相等路径
    def __init__(self, equiv_func): self.equiv_func = equiv_func
    def __str__(self): return f"ua({self.equiv_func})"

class Transport(Term):
    # 路径运输：沿着某条路径，把项从A转运到B
    def __init__(self, path, term): self.path = path; self.term = term
    def __str__(self): return f"transport({self.path}, {self.term})"

# --- 2. 静态类型检查器 (Type Checker - 代表 HoTT 的静态逻辑) ---
def type_check(term):
    if isinstance(term, TrueVal) or isinstance(term, FalseVal):
        return BoolType()
    elif isinstance(term, NotFunc):
        return "Bool -> Bool"
    elif isinstance(term, App):
        func_type = type_check(term.func)
        arg_type = type_check(term.arg)
        if func_type == "Bool -> Bool" and isinstance(arg_type, BoolType):
            return BoolType()
        raise Exception("Type Error in App")
    elif isinstance(term, UnivalenceAxiom):
        # 单价公理神谕：只要传入的是合法的等价(如not)，直接返回类型相等的Path
        # 这里绕过了"它怎么运算"，直接发放逻辑通行证
        if isinstance(term.equiv_func, NotFunc):
            return PathType(BoolType(), BoolType())
        raise Exception("Type Error in UA")
    elif isinstance(term, Transport):
        path_type = type_check(term.path)
        term_type = type_check(term.term)
        # 如果路径是 A = B，且项的类型是 A，则运输后的类型是 B
        if isinstance(path_type, PathType) and isinstance(term_type, type(path_type.A)):
            return path_type.B
        raise Exception("Type Error in Transport")
    else:
        raise Exception(f"Unknown term: {term}")

# --- 3. 操作语义求值器 (Evaluator - 代表现实的时间与时序执行) ---
def evaluate(term):
    if isinstance(term, App):
        func_eval = evaluate(term.func)
        arg_eval = evaluate(term.arg)
        # 真实的计算动作：遇到 not(true) 就变成 false
        if isinstance(func_eval, NotFunc):
            if isinstance(arg_eval, TrueVal): return FalseVal()
            if isinstance(arg_eval, FalseVal): return TrueVal()
        return App(func_eval, arg_eval)
        
    elif isinstance(term, Transport):
        path_eval = evaluate(term.path)
        term_eval = evaluate(term.term)
        
        # 如果路径是平凡的 refl，不需要异化，直接返回原值
        if isinstance(path_eval, Refl):
            return term_eval
            
        # 【致死打击点】：如果是 ua 公理生成的路径，求值器根本不知道怎么走！
        # 因为 ua 是一条静态的拓扑空间公理，它没有赋予底层时序执行的 step 规则。
        # 此时，计算彻底卡死（Stuck）
        return Transport(path_eval, term_eval)
        
    return term

# --- 4. 运行证明剧本 ---
print("==================================================")
print("【机器证明报告】HoTT 中“时间被异化”引发的不可计算悖论")
print("==================================================\n")

# 场景A：现实中遵循时序的计算
print(">>> 场景 A：现实中的时序计算 (不使用单价性异化)")
real_calc = App(NotFunc(), TrueVal())
print(f"1. 表达式: {real_calc}")
print(f"2. ASK预审 (Type Check): 它的类型是 {type_check(real_calc)}")
print(f"3. 现实时序执行 (Evaluate): 计算得出结果为 {evaluate(real_calc)}")
print("结论：现实计算完美结束，瞬间停机。\n")

# 场景B：Think in HoTT 产生的非现实性悖论
print(">>> 场景 B：Think in HoTT 产生的“时空异化”悖论")
# 构造：用单价公理把 not 动作异化为空间路径，然后强迫 true 沿着路径移动
hott_path = UnivalenceAxiom(NotFunc())
hott_calc = Transport(hott_path, TrueVal())

print(f"1. 表达式: {hott_calc}")
print("2. HoTT 的静态逻辑审查 (Type Check):")
try:
    calc_type = type_check(hott_calc)
    print(f"   [通过] HoTT类型系统确认：它是一个完美合法的 {calc_type}！")
    print("   (理论傲慢地宣布：它是一个布尔值，逻辑上它就是存在的，绕过了ASK！)")
except Exception as e:
    print(f"   [失败] {e}")

print("3. 时序引擎强制执行 (Evaluate):")
final_result = evaluate(hott_calc)
print(f"   [结果] 机器输出: {final_result}")

if isinstance(final_result, Transport):
    print("\n【反证法矛盾 / 悖论爆发】")
    print("理论层面 (Type Check) 说：它是一个布尔值 (Bool)。")
    print("现实层面 (Evaluate) 说：它既不是 true，也不是 false，计算引擎被死死卡住 (Stuck)！")
    print("一个本该瞬间停机的问题，在 HoTT 理论推演下，变成了永远无法给出答案的非现实怪物。")
print("==================================================")
