---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: src/graph/SCC.py
    title: src/graph/SCC.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/math/TwoSAT.test.py
    title: src/$tests/math/TwoSAT.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from src.graph.SCC import SCC\n\n\nclass TwoSAT:\n    def __init__(self,\
    \ n):\n        self.n = n\n        self.scc = SCC(2 * n)\n        self._build\
    \ = False\n\n    def add_clause(self, i, pos_i, j, pos_j):\n        \"\"\"\n \
    \       a V b\n        pos_i = True -> a = i,\n        pos_i = False -> a = \xAC\
    i\n        \"\"\"\n        i0 = i\n        i1 = i + self.n\n        if not pos_i:\n\
    \            i0, i1 = i1, i0\n\n        j0 = j\n        j1 = j + self.n\n    \
    \    if not pos_j:\n            j0, j1 = j1, j0\n\n        self.scc.add_edge(i1,\
    \ j0)\n        self.scc.add_edge(j1, i0)\n\n    def check(self):\n        _, self.ids\
    \ = self.scc.build()\n\n        for i in range(self.n):\n            if self.ids[i]\
    \ == self.ids[i + self.n]:\n                return False\n        return True\n\
    \n    def assign(self):\n        ret = [False] * self.n\n        for i in range(self.n):\n\
    \            if self.ids[i] > self.ids[i + self.n]:\n                ret[i] =\
    \ True\n\n        return ret\n"
  dependsOn:
  - src/graph/SCC.py
  isVerificationFile: false
  path: src/math/TwoSAT.py
  requiredBy: []
  timestamp: '2023-07-09 16:59:13+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/math/TwoSAT.test.py
documentation_of: src/math/TwoSAT.py
layout: document
redirect_from:
- /library/src/math/TwoSAT.py
- /library/src/math/TwoSAT.py.html
title: src/math/TwoSAT.py
---
