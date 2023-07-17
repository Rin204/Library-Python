---
title: BIT
documentation_of: ././expansion/data_structure/BIT.py
---

# 概要
Binary Indexed Tree / Fenwick Tree です．1点加算区間和取得を高速に行います．

## 使い方
- \_\_init\_\_(n) := 長さ $N$ の配列 A を作成します．
- sum(r) := 区間 $[0, r)$ の総和を返します．
- sum(l, r) := 区間 $[l, r)$ の総和を返します．
- get(i) := A[i] の値を求めます．
- add(i, x) := A[i] に $x$ を加算します．
- lower_bound(x) := 区間 $[0, r)$ の総和が $x$ 以上となるような最小の $k$ を返します．
