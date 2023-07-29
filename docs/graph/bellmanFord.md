---
title: bellmanFord
documentation_of: ././expansion/graph/bellmanFord.py
---

# 概要
ベルマンフォードです．

$edges = [(from1, to1, cost1), (from2, to2, cost2), ...)]$の形式で辺情報を与えてください

## 使い方
inf は十分に大きい値を適当に設定してください
```
dist = bellmanFord(n, edges, s, inf=1 << 60)
```
負閉路がある場合は None を返します．
