---
title: CentroidDecomposition
documentation_of: ././expansion/tree/CentroidDecomposition.py
---

# 概要
重心分解 です．

## 使い方

- \_\_init\_\_(n, edges=None) := 頂点数 n で初期化します．辺情報を与える場合は，$ edges[from] = [to1, to2, ...]$の形式で与えてください．
- add_edge(u, v) := u -> v の有向辺を追加します．
- read_edges(indexed=1) := n - 1 辺の情報を標準入力として受け取ります．
- build(root) := 根を root として構築します
- cent_ind_dist(u) := 頂点 u + 重心分解木における u の各先祖の [頂点番号, u からの距離] を返します．



- self.par := 重心分解木における各頂点の親です．
- self.centroids[i] := 重心分解木における深さがiの頂点の一覧です
