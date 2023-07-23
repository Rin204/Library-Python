---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_B\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\nclass WeightedUnionFind:\n    def __init__(self, n):\n        self.n = n\n\
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
    \        else:\n            return None\n\n\nn, Q = map(int, input().split())\n\
    UF = WeightedUnionFind(n)\nfor _ in range(Q):\n    query = list(map(int, input().split()))\n\
    \    if query[0] == 0:\n        x, y, z = query[1:]\n        UF.unite(y, x, z)\n\
    \    else:\n        x, y = query[1:]\n        res = UF.diff(y, x)\n        if\
    \ res is None:\n            print(\"?\")\n        else:\n            print(res)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/data_structure/WeightedUF.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/data_structure/WeightedUF.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/data_structure/WeightedUF.test.py
- /verify/expansion/$tests/data_structure/WeightedUF.test.py.html
title: expansion/$tests/data_structure/WeightedUF.test.py
---
