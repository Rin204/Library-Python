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
  code: "class WeightedUnionFind:\n    def __init__(self, n):\n        self.n = n\n\
    \        self.par = [-1] * n\n        self.group_ = n\n        self.D = [0] *\
    \ n\n\n    def find(self, x):\n        if self.par[x] < 0:\n            return\
    \ x\n        lst = []\n        while self.par[x] >= 0:\n            lst.append(x)\n\
    \            x = self.par[x]\n        for y in lst[::-1]:\n            self.D[y]\
    \ += self.D[self.par[y]]\n            self.par[y] = x\n        return x\n\n  \
    \  def unite(self, x, y, d):\n        # D[x] - D[y] = d\n        xp = self.find(x)\n\
    \        yp = self.find(y)\n        d -= self.D[x]\n        d += self.D[y]\n \
    \       x = xp\n        y = yp\n        if x == y:\n            assert d == 0\n\
    \            return False\n\n        if self.par[x] > self.par[y]:\n         \
    \   x, y = y, x\n            d *= -1\n\n        self.par[x] += self.par[y]\n \
    \       self.par[y] = x\n        self.group_ -= 1\n        self.D[y] = -d\n  \
    \      return True\n\n    def size(self, x):\n        return -self.par[self.find(x)]\n\
    \n    def same(self, x, y):\n        return self.find(x) == self.find(y)\n\n \
    \   @property\n    def group(self):\n        return self.group_\n\n    def diff(self,\
    \ x, y):\n        if self.same(x, y):\n            return self.D[x] - self.D[y]\n\
    \        else:\n            return None\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/data_structure/WeightedUnionFind.py
  requiredBy: []
  timestamp: '2023-06-18 16:53:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/data_structure/WeightedUnionFind.py
layout: document
title: WeightedUnionFind
---

# 概要
UnionFind の各辺に重みを付けたものです．
各頂点に重みD[i]があるのを想定して差分を管理したりします

## 使い方
- \_\_init\_\_(n) := 長さ $N$ で初期化します．
- find(x) := x の代表元を返します．
- unite(x, y, d) := x の属する集合と y の属する集合を合併し，True を返します．もともと同じ集合に属した場合 False を返します．ここで，D[x] - D[y] = d となるように合併を行い，既に合併済みかつ長さ制約に矛盾がある場合は assert で落ちます
- size(x) := x の属する集合の大きさを返します．
- same(x, y) := x と y が同じ集合に属するなら True を，そうでないなら False を返します．
- group := 現在の集合の個数を返します．
- diff(x, y) := D[x] - D[y] を返します．x, y の属する集合が異なる場合は None を返します．
