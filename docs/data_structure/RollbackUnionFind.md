---
title: RollbackUnionFind
documentation_of: ././expansion/data_structure/RollbackUnionFind.py
---

# 概要
UnionFind に Rollback 機能を付けたものです．

## 使い方
- \_\_init\_\_(n) := 長さ $N$ で初期化します．
- find(x) := x の代表元を返します．
- unite(x, y) := x の属する集合と y の属する集合を合併し，True を返します．もともと同じ集合に属した場合 False を返します．
- size(x) := x の属する集合の大きさを返します．
- same(x, y) := x と y が同じ集合に属するなら True を，そうでないなら False を返します．
- group := 現在の集合の個数を返します．
- undo() := 1 手状態を戻します
- get_state() := 現在の状態を返します．（unite を行った回数）
- rollback(state) := ↑で取得した状態に戻します 

