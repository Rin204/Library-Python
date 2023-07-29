---
title: Kruskal
documentation_of: ././expansion/tree/Kruskal.py
---

# 概要
最小全域木の重み総和を求めます．

$edges = [(from1, to1, cost1), (from2, to2, cost2), ...)]$の形式で辺情報を与えてください

## 使い方
```
cost = Kruskal(n, edges, is_sorted=False)
```
全体が連結でない場合は -1 を返します．
