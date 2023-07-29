---
title: lowLink
documentation_of: ././expansion/graph/lowLink.py
---

# 概要
グラフの橋と関節点を見つけます．

$ edges[from] = [to1, to2, ...]$の形式で辺情報を与えてください

## 使い方
```
isartic, bridge = lowLink(edges)
```
isartic は各頂点が関節点かどうかを表す bool 列です．
