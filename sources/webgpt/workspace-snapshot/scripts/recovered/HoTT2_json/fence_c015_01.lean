-- 假定 HoTT 的单价公理存在
axiom ua {A B : Type} (e : Equiv A B) : A = B

-- 声明一个取反的等价操作
def notEquiv : Equiv Bool Bool := ... -- (实现取反的等价证明)

-- 用 HoTT 的方式去计算取反：要求 true 沿着 ua 搭建的“空间桥梁”走过去
noncomputable def hott_calc : Bool :=
  cast (ua notEquiv) true

-- 理论可以在"命题相等"的层面上，逻辑证明它等于 false
theorem hott_is_false : hott_calc = false := by
  -- 证明可以通过公理改写来强行打通
  sorry 

-- 但是，机器底层执行计算：
#reduce hott_calc
