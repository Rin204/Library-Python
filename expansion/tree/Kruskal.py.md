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
  code: "class UnionFind:\n    def __init__(self, n):\n        self.n = n\n      \
    \  self.par = [-1] * n\n        self.group_ = n\n\n    def find(self, x):\n  \
    \      if self.par[x] < 0:\n            return x\n        lst = []\n        while\
    \ self.par[x] >= 0:\n            lst.append(x)\n            x = self.par[x]\n\
    \        for y in lst:\n            self.par[y] = x\n        return x\n\n    def\
    \ unite(self, x, y):\n        x = self.find(x)\n        y = self.find(y)\n   \
    \     if x == y:\n            return False\n\n        if self.par[x] > self.par[y]:\n\
    \            x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n        self.group_ -= 1\n        return True\n\n    def size(self, x):\n\
    \        return -self.par[self.find(x)]\n\n    def same(self, x, y):\n       \
    \ return self.find(x) == self.find(y)\n\n    @property\n    def group(self):\n\
    \        return self.group_\n\n\ndef Kruskal(n, edges, is_sorted=False):\n   \
    \ if n == 1:\n        return 0\n    if not is_sorted:\n        edges.sort(key=lambda\
    \ x: x[2])\n    UF = UnionFind(n)\n    res = 0\n    for u, v, cost in edges:\n\
    \        if UF.unite(u, v):\n            res += cost\n            if UF.group\
    \ == 1:\n                return res\n    return -1\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/tree/Kruskal.py
  requiredBy: []
  timestamp: '2023-06-18 16:34:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/tree/Kruskal.py
layout: document
redirect_from:
- /library/expansion/tree/Kruskal.py
- /library/expansion/tree/Kruskal.py.html
title: expansion/tree/Kruskal.py
---
