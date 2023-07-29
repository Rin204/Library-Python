---
title: maxflow
documentation_of: ././expansion/graph/maxflow.py
---

# 概要
最大流です．

Python のバージョン次第でコメントアウトしている `dataclass` が使えます．
`from` が Python の予約語なので，`from_` を用いています．

## 使い方
- \_\_init\_\_(n) := 頂点数 n でグラフを初期化します．
- add_edge(from_, to, cap) := u -> v の容量 cap の有向辺を追加します．
- get_edge(i) := i 番目に追加した辺の現在の状態を取得します．
- edges() := 現在の辺の状態を全て取得します．
- change_edge(i, new_cap, new_flow) := i 番目に追加した辺の状態を更新します
- flow(s, t, flow_limit=1 << 60) := s から t に最大で flow_limit の流量を流します．実際に流せた流量を返します．
- min_cut(s) := 頂点 s からたどり着けるかどうかを表した bool 配列を返します．
