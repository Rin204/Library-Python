---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A\n\
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
    \        return self.group_\n\n\ndef Kruskal(n, edges, is_sorted=False):\n   \
    \ if n == 1:\n        return 0\n    if not is_sorted:\n        edges.sort(key=lambda\
    \ x: x[2])\n    UF = UnionFind(n)\n    res = 0\n    for u, v, cost in edges:\n\
    \        if UF.unite(u, v):\n            res += cost\n            if UF.group\
    \ == 1:\n                return res\n    return -1\n\n\nn, m = map(int, input().split())\n\
    edges = [list(map(int, input().split())) for _ in range(m)]\nprint(Kruskal(n,\
    \ edges))\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/tree/Kruskal.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/tree/Kruskal.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/tree/Kruskal.test.py
- /verify/expansion/$tests/tree/Kruskal.test.py.html
title: expansion/$tests/tree/Kruskal.test.py
---
