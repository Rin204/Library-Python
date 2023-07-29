---
title: SCC
documentation_of: ././expansion/graph/SCC.py
---

# 概要
強連結成分分解をします．

## 使い方

- \_\_init\_\_(n, edges=None) := 頂点数 n でグラフを初期化します．edges を与える場合は，$edges = [(from_1, to_1), (from_2, to_2), \ldots]$ の形式で与えてください
- add_edge(u, v) := u -> v の有向辺を追加します．
- read_edges(m, indexed=1) := m 辺の情報を標準入力として受け取ります．
- build() := 構築します．強連結成分の個数と，各頂点がどの連結成分に属するかを返します．連結成分の番号はトポロジカル順序です．
