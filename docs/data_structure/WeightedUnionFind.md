---
title: WeightedUnionFind
documentation_of: ././expansion/data_structure/WeightedUnionFind.py
---

# 概要
UnionFind の各辺に重みを付けたものです．
各頂点に重みD[i]があるのを想定して差分を管理したりします

## 使い方
- \_\_init\_\_(n) := 長さ $N$ で初期化します．
- find(x) := x の代表元を返します．
- unite(x, y, d) := x の属する集合と y の属する集合を合併し，True を返します．もともと同じ集合に属した場合 False を返します．ここで，D[x] - D[y] = d となるように合併を行い，既に合併済みかつ長さ制約に矛盾がある場合は assert で落ちます
- size(x) := x の属する集合の大きさを返します．
- same(x, y) := x と y が同じ集合に属するなら True を，そうでないなら False を返します．
- group := 現在の集合の個数を返します．
- diff(x, y) := D[x] - D[y] を返します．x, y の属する集合が異なる場合は None を返します．
