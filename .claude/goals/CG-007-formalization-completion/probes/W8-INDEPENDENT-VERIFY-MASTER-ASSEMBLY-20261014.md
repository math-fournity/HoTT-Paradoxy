# 独立核验：Master 的 `MasterAssemblyProbe`（第二条眼睛）

> 核验人：9276-W8-D3。日期：2026-10-14。
> 对象：`MasterAssemblyProbe.lean`（来自
> `claude/infallible-mestorf-ce08c0` 分支，
> `.cg009-verification/master-assembly-poc-20261014/`）。
> 判据：exit code + `#print axioms`。

## 方法（刻意比原方法更严）

原方法借 9276 的 devbuild olean 缓存作种子（`SEED`）。
**本核验把 `SEED` 置空**，从零编译全链——这同时满足
Master 要求的「skipped=0」。

路径常量改成本 checkout 的绝对路径；其余 driver 逻辑不动。

## 结果

```
=== done: compiled=74 skipped=0 failed=0 in 223s ===
```

**74 文件从零编译，74/74 OK，0 跳过，0 失败。**

## Master 要求的三点核验

### 核验点 1：`allBlockerQ_uncond` 的公理表 ✅

```
'GodelQ.MasterAssemblyProbe.bridgeB'           depends on axioms: [propext, Classical.choice, Quot.sound]
'GodelQ.MasterAssemblyProbe.allKey_uncond'     depends on axioms: [propext, Classical.choice, Quot.sound]
'GodelQ.MasterAssemblyProbe.allBlockerQ_uncond' depends on axioms: [propext, Classical.choice, Quot.sound]
```

三条**全部干净**，**无 `sorryAx`**。

### 核验点 2：`ITSubstOpen4` 的 `len_qVec` 修改（5 处 `Bootstrapping.` 前缀）✅

**语义未变——已用 `rfl` 机器证明**：

```lean
example (w : V) (hw : IsUTermVec ℒₛₑₜ (len w) w) :
    Bootstrapping.len_qVec hw = GodelQ.TranslateShiftCompat.len_qVec hw := rfl
```

**exit 0**。即两个 `len_qVec`（Foundation 版与包内 `TranslateShiftCompat:1073` 版）
**陈述完全相同**（`len (qVec ℒₛₑₜ w) = len w + 1`）。
⟹ 加 `Bootstrapping.` 前缀是**纯命名歧义消解**，无语义改动。

（对照：包内版在 `TranslateShiftCompat.lean:1073`，同一陈述。）

### 核验点 3：driver 的 `skipped=0` ✅

见上：`compiled=74 skipped=0 failed=0`。

## 关于 olean 命名（Master 提醒的坑）

driver 用的是**嵌套模块路径**：
`--o=$OUT/GodelQ/ZFC/X.olean` + `-R $ASM`。
⟹ **不会**吃旧缓存，无扁平命名陷阱。**本核验未遇到 stale-olean 假象。**

## 结论

**`MasterAssemblyProbe.allBlockerQ_uncond` 独立核验通过。**
舰队第一条无条件 blocker（hAll 支）确认成立。

装配链（复核其每一环在本核验中都被编译通过）：
```
ITSubstOpen9.iT_subst_open  →  bridgeB  →  allKey_of_bridge  →  AllKey  →  allBlockerQ_of_key  →  AllBlockerQ
```

## 附：本核验用到的文件

* `driver_indep.py`：把 `ASM` 改成本 checkout 路径、`SEED` 置空、
  `LEAN_PATH` 去掉 `SEED`。其余不动。
* `CHECKS.lean`：核验点 2 的 `rfl` 对照。
