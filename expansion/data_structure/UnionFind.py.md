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
  path: expansion/data_structure/UnionFind.py
  requiredBy: []
  timestamp: '2023-06-18 16:34:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/data_structure/UnionFind.py
layout: document
title: UnionFind
---

# 概要
集合の合併 / どの集合に属しているかの判定を高速に行うものです．

## 使い方
- \_\_init\_\_(n) := 長さ $N$ で初期化します．
- find(x) := x の代表元を返します．
- unite(x, y) := x の属する集合と y の属する集合を合併し，True を返します．もともと同じ集合に属した場合 False を返します．
- size(x) := x の属する集合の大きさを返します．
- same(x, y) := x と y が同じ集合に属するなら True を，そうでないなら False を返します．
- group := 現在の集合の個数を返します．
 

