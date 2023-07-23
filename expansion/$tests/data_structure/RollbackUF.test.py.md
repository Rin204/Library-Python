---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/1293
    links:
    - https://yukicoder.me/problems/no/1293
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/1293\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\nclass RollbackUnionFind:\n    def __init__(self, n):\n        self.n = n\n\
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
    \ get_state(self):\n        return len(self.history) >> 1\n\n\nn, d, w = map(int,\
    \ input().split())\nUF1 = RollbackUnionFind(n)\nUF2 = RollbackUnionFind(n)\nfor\
    \ _ in range(d):\n    a, b = map(int, input().split())\n    UF1.unite(a - 1, b\
    \ - 1)\nfor _ in range(w):\n    c, d = map(int, input().split())\n    UF2.unite(c\
    \ - 1, d - 1)\n\nans = -n\ndic = {}\nfor i in range(n):\n    p = UF1.find(i)\n\
    \    if p not in dic:\n        dic[p] = []\n    dic[p].append(i)\n\nfor group\
    \ in dic.values():\n    u = group[0]\n    state = UF2.get_state()\n    for v in\
    \ group:\n        UF2.unite(u, v)\n    ans += UF1.size(u) * UF2.size(u)\n    UF2.rollback(state)\n\
    \nprint(ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/data_structure/RollbackUF.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/data_structure/RollbackUF.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/data_structure/RollbackUF.test.py
- /verify/expansion/$tests/data_structure/RollbackUF.test.py.html
title: expansion/$tests/data_structure/RollbackUF.test.py
---
