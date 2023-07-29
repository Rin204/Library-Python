---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LCA:\n    def __init__(self, n, root=0, edges=None):\n        self.n\
    \ = n\n        self.root = root\n        self.logn = (self.n - 1).bit_length()\n\
    \        if edges is None:\n            self.edges = [[] for _ in range(n)]\n\
    \        else:\n            self.edges = edges\n            # \u30B3\u30D4\u30FC\
    \u3057\u3066\u306A\u3044\u306E\u3067\u6CE8\u610F\n\n        self.depth = [-1]\
    \ * n\n        self.par = [[-1] * n for _ in range(self.logn)]\n\n    def build(self):\n\
    \        self.depth[self.root] = 0\n        stack = [self.root]\n        while\
    \ stack:\n            pos = stack.pop()\n            for npos in self.edges[pos]:\n\
    \                if self.depth[npos] == -1:\n                    self.depth[npos]\
    \ = self.depth[pos] + 1\n                    stack.append(npos)\n            \
    \        self.par[0][npos] = pos\n\n        for i in range(1, self.logn):\n  \
    \          for j in range(self.n):\n                if self.par[i - 1][j] != -1:\n\
    \                    self.par[i][j] = self.par[i - 1][self.par[i - 1][j]]\n\n\
    \    def add_edge(self, u, v):\n        self.edges[u].append(v)\n        self.edges[v].append(u)\n\
    \n    def read_edges(self, indexed=1):\n        for _ in range(self.n - 1):\n\
    \            u, v = map(int, input().split())\n            u -= indexed\n    \
    \        v -= indexed\n            self.add_edge(u, v)\n\n    def lca(self, u,\
    \ v):\n        if self.depth[u] > self.depth[v]:\n            u, v = v, u\n\n\
    \        d = self.depth[v] - self.depth[u]\n        i = 0\n        while d > 0:\n\
    \            if d & 1:\n                v = self.par[i][v]\n            i += 1\n\
    \            d >>= 1\n\n        if u == v:\n            return u\n\n        d\
    \ = self.depth[u]\n        logn = (d - 1).bit_length()\n        for i in range(logn\
    \ - 1, -1, -1):\n            pu = self.par[i][u]\n            pv = self.par[i][v]\n\
    \            if pu != pv:\n                u = pu\n                v = pv\n\n\
    \        return self.par[0][u]\n\n    def dist(self, u, v):\n        return self.depth[u]\
    \ + self.depth[v] - 2 * self.depth[self.lca(u, v)]\n\n    def jump(self, u, v,\
    \ k):\n        if k == 0:\n            return u\n\n        p = self.lca(u, v)\n\
    \        du = self.depth[u] - self.depth[p]\n        dv = self.depth[v] - self.depth[p]\n\
    \        if du + dv < k:\n            return -1\n        if k <= du:\n       \
    \     d = k\n        else:\n            u = v\n            d = du + dv - k\n\n\
    \        i = 0\n        while d > 0:\n            if d & 1:\n                u\
    \ = self.par[i][u]\n            i += 1\n            d >>= 1\n\n        return\
    \ u\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/tree/LCA.py
  requiredBy: []
  timestamp: '2023-07-07 22:56:19+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/tree/LCA.py
layout: document
title: LCA
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
