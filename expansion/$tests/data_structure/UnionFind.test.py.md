---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    \nfrom pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\nclass UnionFind:\n    def __init__(self, n):\n        self.n = n\n       \
    \ self.par = [-1] * n\n        self.group_ = n\n\n    def find(self, x):\n   \
    \     if self.par[x] < 0:\n            return x\n        lst = []\n        while\
    \ self.par[x] >= 0:\n            lst.append(x)\n            x = self.par[x]\n\
    \        for y in lst:\n            self.par[y] = x\n        return x\n\n    def\
    \ unite(self, x, y):\n        x = self.find(x)\n        y = self.find(y)\n   \
    \     if x == y:\n            return False\n\n        if self.par[x] > self.par[y]:\n\
    \            x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n        self.group_ -= 1\n        return True\n\n    def size(self, x):\n\
    \        return -self.par[self.find(x)]\n\n    def same(self, x, y):\n       \
    \ return self.find(x) == self.find(y)\n\n    @property\n    def group(self):\n\
    \        return self.group_\n\n\nn, Q = map(int, input().split())\nUF = UnionFind(n)\n\
    ans = []\nfor _ in range(Q):\n    t, x, y = map(int, input().split())\n    if\
    \ t == 0:\n        UF.unite(x, y)\n    else:\n        if UF.same(x, y):\n    \
    \        ans.append(1)\n        else:\n            ans.append(0)\n\nprint(*ans,\
    \ sep=\"\\n\")\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/data_structure/UnionFind.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/data_structure/UnionFind.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/data_structure/UnionFind.test.py
- /verify/expansion/$tests/data_structure/UnionFind.test.py.html
title: expansion/$tests/data_structure/UnionFind.test.py
---
