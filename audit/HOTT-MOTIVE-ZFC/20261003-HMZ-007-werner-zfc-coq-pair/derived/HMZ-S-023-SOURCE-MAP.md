# HMZ-S-023：Rocq/ZF archive source map

> **派生身份：** 本文件是 source locator，不是源码副本或新的证明版本。原始字节只保存在 `../originals/HMZ-S-023-rocq-archive-zfc-ede7126560844.tar.gz`；完整成员表在同目录 `HMZ-S-023-rocq-archive-zfc-tree.txt`。

## 冻结身份

```text
remote: https://github.com/rocq-archive/zfc
frozen commit: ede7126560844c381c2b021003a8dbcb0668ecad
archive SHA-256: 9181e163607d1e58ecc7f2c2e06b4f952268623461a43e519a42a2c6903522ac
member count: 17
```

## 已审源码 locator

| tar member | 精确作用 | 本 run 使用的范围 |
|---|---|---|
| `README` | historical contribution identity；`Ens`/`IN`/`EQ`；ZFC axioms as theorems；non-computational Choice for replacement and set AC。 | Description block。 |
| `zfc.v` | core `Ens := sup A (A -> Ens)`、`EQ`、`IN` 的 legacy implementation。 | lines 27–74。 |
| `Axioms.v` | bounded comprehension `Comp` 与 `Power`，后续 Power laws。 | lines 160–166、428–510。 |
| `Replacement.v` | `collection`、`choice`、collection→replacement与 classical replacement theorem。 | lines 21–93。 |
| `Russell.v` | `Russell : forall E : Ens, (forall E' : Ens, IN E' E) -> False`。 | lines 19–55。 |
| `Hierarchy.v` | small-set injection、`Power'`、`Big_closed_for_power`。 | lines 77–136。 |
| `Omega.v` | Power-based hierarchy expression `Vee`。 | lines 175–178。 |

## 验证方法

```sh
tar -tzf originals/HMZ-S-023-rocq-archive-zfc-ede7126560844.tar.gz
shasum -a 256 originals/HMZ-S-023-rocq-archive-zfc-ede7126560844.tar.gz
```

将解出的 member 与 `HMZ-S-023-rocq-archive-zfc-tree.txt` 比较，才可重建本 run 所读的 source snapshot。这个 map 不声称历史 Coq 6.3 环境仍可运行。
