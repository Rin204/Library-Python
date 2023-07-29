---
title: Hungarian
documentation_of: ././expansion/geometry/Hungarian.py
---

# 概要
割り当て問題を解きます．

$N \times M, (N \le M)$ の行列 $A$ があるときに。
$\sum_{i = 0}^{N - 1} A_{i, p_i}$ を最小化する $p_i$ (重複なし) を構成します。

## 使い方
inf は十分に大きい値を適当に設定してください
```
cost, assignment = Hungarian(A, inf=1 << 60):
```
