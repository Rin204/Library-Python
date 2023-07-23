---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: src/tree/Kruskal.py
    title: src/tree/Kruskal.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/data_structure/UnionFind.test.py
    title: src/$tests/data_structure/UnionFind.test.py
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
    \        return self.group_\n"
  dependsOn: []
  isVerificationFile: false
  path: src/data_structure/UnionFind.py
  requiredBy:
  - src/tree/Kruskal.py
  timestamp: '2023-06-18 16:34:12+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/data_structure/UnionFind.test.py
documentation_of: src/data_structure/UnionFind.py
layout: document
redirect_from:
- /library/src/data_structure/UnionFind.py
- /library/src/data_structure/UnionFind.py.html
title: src/data_structure/UnionFind.py
---
