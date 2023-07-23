---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: src/math/TwoSAT.py
    title: src/math/TwoSAT.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
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
  path: src/graph/SCC.py
  requiredBy:
  - src/math/TwoSAT.py
  timestamp: '2023-07-09 16:59:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: src/graph/SCC.py
layout: document
redirect_from:
- /library/src/graph/SCC.py
- /library/src/graph/SCC.py.html
title: src/graph/SCC.py
---
