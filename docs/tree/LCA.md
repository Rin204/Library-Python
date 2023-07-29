---
title: LCA
documentation_of: ././expansion/tree/LCA.py
---

# 概要
LCA です．

## 使い方

- \_\_init\_\_(n, root=0, edges=None) := 頂点数 n で初期化します．辺情報を与える場合は，$ edges[from] = [to1, to2, ...]$の形式で与えてください．
- add_edge(u, v) := u -> v の有向辺を追加します．
- read_edges(indexed=1) := n - 1 辺の情報を標準入力として受け取ります．
- build(root) := 根を root として構築します
- get_path(u, v) := 頂点 u-v 間のpath を返します．
- lca(u, v) := 頂点 u-v の LCA を求めます
- dist(u, v) := 頂点 u-v 間の距離を求めます
- jump(u, v, k) := 頂点 u から v の方向に k だけ移動した頂点を返します．ただし dist(u, v) < k の場合 -1 を返します．
