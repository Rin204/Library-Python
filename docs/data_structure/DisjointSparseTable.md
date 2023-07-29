---
title: DisjointSparseTable
documentation_of: ././expansion/data_structure/DisjointSparseTable.py
---

# 概要
- $f(a, f(b, c)) = f(f(a, b), c)$

を満たす二項演算を処理します．

## 使い方
- \_\_init\_\_(A, ope) := 配列 A と条件を満たす演算 ope を与えて初期化します．
- prod(l, r) := 区間 [l, r) の演算結果を返します．
