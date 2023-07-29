---
title: dijkstra
documentation_of: ././expansion/graph/dijkstra.py
---

# 概要
ダイクストラ法です．

$edges[from] = [(to1, cost1), (to2, cost2), ...)]$の形式で辺情報を与えてください

## 使い方
inf は十分に大きい値を適当に設定してください
```
dist = dijkstra(edges, s=0, inf=1 << 60)
```
