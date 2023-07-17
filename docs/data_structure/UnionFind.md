---
title: UnionFind
documentation_of: ././expansion/data_structure/UnionFind.py
---

# 概要
集合の合併 / どの集合に属しているかの判定を高速に行うものです．

## 使い方
- \_\_init\_\_(n) := 長さ $N$ で初期化します．
- find(x) := x の代表元を返します．
- unite(x, y) := x の属する集合と y の属する集合を合併し，True を返します．もともと同じ集合に属した場合 False を返します．
- size(x) := x の属する集合の大きさを返します．
- same(x, y) := x と y が同じ集合に属するなら True を，そうでないなら False を返します．
- group := 現在の集合の個数を返します．
 

