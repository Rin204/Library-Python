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
  code: "class SCC:\n    def __init__(self, n, edges=None):\n        self.n = n\n\
    \        if edges is None:\n            self.edges = []\n        else:\n     \
    \       self.edges = edges\n\n    def add_edge(self, u, v):\n        self.edges.append((u,\
    \ v))\n\n    def read_edges(self, m, indexed=1):\n        for _ in range(m):\n\
    \            u, v = map(int, input().split())\n            u -= indexed\n    \
    \        v -= indexed\n            self.add_edge(u, v)\n\n    def build(self):\n\
    \        start = [0] * (self.n + 1)\n        elist = [0] * len(self.edges)\n \
    \       for u, _ in self.edges:\n            start[u + 1] += 1\n        for i\
    \ in range(1, self.n + 1):\n            start[i] += start[i - 1]\n\n        counter\
    \ = start[:]\n        for u, v in self.edges:\n            elist[counter[u]] =\
    \ v\n            counter[u] += 1\n\n        now_ord = 0\n        group_num = 0\n\
    \        visited = []\n        low = [0] * self.n\n        ord = [-1] * self.n\n\
    \        ids = [0] * self.n\n        bpos = [-1] * self.n\n\n        def dfs(v):\n\
    \            nonlocal now_ord, group_num\n\n            visited.append(v)\n  \
    \          stack = [~v, v]\n            while stack:\n                pos = stack.pop()\n\
    \                if pos >= 0:\n                    if ord[pos] == -1:\n      \
    \                  low[pos] = ord[pos] = now_ord\n                        now_ord\
    \ += 1\n                        visited.append(pos)\n                        for\
    \ i in range(start[pos], start[pos + 1]):\n                            to = elist[i]\n\
    \                            if ord[to] == -1:\n                             \
    \   stack.append(~to)\n                                stack.append(to)\n    \
    \                            bpos[to] = pos\n                            else:\n\
    \                                low[pos] = min(low[pos], ord[to])\n         \
    \       else:\n                    pos = ~pos\n                    if low[pos]\
    \ == ord[pos]:\n                        while 1:\n                           \
    \ u = visited.pop()\n                            ord[u] = self.n\n           \
    \                 ids[u] = group_num\n                            if u == pos:\n\
    \                                break\n                        group_num += 1\n\
    \                    if bpos[pos] != -1:\n                        low[bpos[pos]]\
    \ = min(low[bpos[pos]], low[pos])\n\n        for i in range(self.n):\n       \
    \     if ord[i] == -1:\n                dfs(i)\n\n        for i in range(self.n):\n\
    \            ids[i] = group_num - 1 - ids[i]\n\n        return group_num, ids\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/graph/SCC.py
  requiredBy: []
  timestamp: '2023-07-09 16:59:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/graph/SCC.py
layout: document
title: SCC
---

# 概要
強連結成分分解をします．

## 使い方

- \_\_init\_\_(n, edges=None) := 頂点数 n でグラフを初期化します．edges を与える場合は，$edges = [(from_1, to_1), (from_2, to_2), \ldots]$ の形式で与えてください
- add_edge(u, v) := u -> v の有向辺を追加します．
- read_edges(m, indexed=1) := m 辺の情報を標準入力として受け取ります．
- build() := 構築します．強連結成分の個数と，各頂点がどの連結成分に属するかを返します．連結成分の番号はトポロジカル順序です．
