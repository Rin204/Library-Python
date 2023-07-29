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
    \            ids[i] = group_num - 1 - ids[i]\n\n        return group_num, ids\n\
    \n\nclass TwoSAT:\n    def __init__(self, n):\n        self.n = n\n        self.scc\
    \ = SCC(2 * n)\n        self._build = False\n\n    def add_clause(self, i, pos_i,\
    \ j, pos_j):\n        \"\"\"\n        a V b\n        pos_i = True -> a = i,\n\
    \        pos_i = False -> a = \xACi\n        \"\"\"\n        i0 = i\n        i1\
    \ = i + self.n\n        if not pos_i:\n            i0, i1 = i1, i0\n\n       \
    \ j0 = j\n        j1 = j + self.n\n        if not pos_j:\n            j0, j1 =\
    \ j1, j0\n\n        self.scc.add_edge(i1, j0)\n        self.scc.add_edge(j1, i0)\n\
    \n    def check(self):\n        _, self.ids = self.scc.build()\n\n        for\
    \ i in range(self.n):\n            if self.ids[i] == self.ids[i + self.n]:\n \
    \               return False\n        return True\n\n    def assign(self):\n \
    \       ret = [False] * self.n\n        for i in range(self.n):\n            if\
    \ self.ids[i] > self.ids[i + self.n]:\n                ret[i] = True\n\n     \
    \   return ret\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/math/TwoSAT.py
  requiredBy: []
  timestamp: '2023-07-09 16:59:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/math/TwoSAT.py
layout: document
title: 2SAT
---

# 概要
2SAT です．

## 使い方

- \_\_init\_\_(n) := 変数の個数を n で初期化します．
- add_clause(i, pos_i, j, pos_j) := $(x_i == pos_i) \cup (x_j == pos_j)$ の条件を追加します．
- check() := 2SAT が充足可能かを判定します．
- assign() := 充足可能である場合，有効な割り当ての１つを返します．充足不
可能な場合は未定義です．