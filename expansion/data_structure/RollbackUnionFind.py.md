---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
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
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class RollbackUnionFind:\n    def __init__(self, n):\n        self.n = n\n\
    \        self.par = [-1] * n\n        self.history = []\n        self.group_ =\
    \ n\n\n    def find(self, x):\n        while self.par[x] >= 0:\n            x\
    \ = self.par[x]\n        return x\n\n    def unite(self, x, y):\n        x = self.find(x)\n\
    \        y = self.find(y)\n        self.history.append((x, self.par[x]))\n   \
    \     self.history.append((y, self.par[y]))\n        if x == y:\n            return\
    \ False\n        if self.par[x] > self.par[y]:\n            x, y = y, x\n    \
    \    self.par[x] += self.par[y]\n        self.par[y] = x\n        self.group_\
    \ -= 1\n        return True\n\n    def size(self, x):\n        return -self.par[self.find(x)]\n\
    \n    def same(self, x, y):\n        return self.find(x) == self.find(y)\n\n \
    \   @property\n    def group(self):\n        return self.group_\n\n    def undo(self):\n\
    \        x, px = self.history.pop()\n        y, py = self.history.pop()\n    \
    \    self.par[x] = px\n        self.par[y] = py\n        if x != y:\n        \
    \    self.group_ += 1\n\n    def rollback(self, state):\n        state <<= 1\n\
    \        while len(self.history) > state:\n            self.undo()\n\n    def\
    \ get_state(self):\n        return len(self.history) >> 1\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/data_structure/RollbackUnionFind.py
  requiredBy: []
  timestamp: '2023-06-18 16:34:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/data_structure/RollbackUnionFind.py
layout: document
redirect_from:
- /library/expansion/data_structure/RollbackUnionFind.py
- /library/expansion/data_structure/RollbackUnionFind.py.html
title: expansion/data_structure/RollbackUnionFind.py
---
