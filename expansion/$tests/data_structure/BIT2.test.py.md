---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/649
    links:
    - https://yukicoder.me/problems/no/649
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/649\n\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\nclass BIT:\n    def __init__(self, n):\n        self.n = n\n        self.data\
    \ = [0] * (n + 1)\n        if n == 0:\n            self.n0 = 0\n        else:\n\
    \            self.n0 = 1 << (n.bit_length() - 1)\n\n    def sum_(self, i):\n \
    \       s = 0\n        while i > 0:\n            s += self.data[i]\n         \
    \   i -= i & -i\n        return s\n\n    def sum(self, l, r=-1):\n        if r\
    \ == -1:\n            return self.sum_(l)\n        else:\n            return self.sum_(r)\
    \ - self.sum_(l)\n\n    def get(self, i):\n        return self.sum(i, i + 1)\n\
    \n    def add(self, i, x):\n        i += 1\n        while i <= self.n:\n     \
    \       self.data[i] += x\n            i += i & -i\n\n    def lower_bound(self,\
    \ x):\n        if x <= 0:\n            return 0\n        i = 0\n        k = self.n0\n\
    \        while k > 0:\n            if i + k <= self.n and self.data[i + k] < x:\n\
    \                x -= self.data[i + k]\n                i += k\n            k\
    \ //= 2\n        return i + 1\n\n\nQ, k = map(int, input().split())\nQuery = []\n\
    X = []\nfor _ in range(Q):\n    query = list(map(int, input().split()))\n    if\
    \ query[0] == 1:\n        X.append(query[1])\n        Query.append(query[1])\n\
    \    else:\n        Query.append(-1)\n\nX = sorted(set(X))\ndic = {x: i for i,\
    \ x in enumerate(X)}\n\nbit = BIT(len(dic))\nfor q in Query:\n    if q == -1:\n\
    \        p = bit.lower_bound(k) - 1\n        if p == len(X):\n            print(-1)\n\
    \        else:\n            print(X[p])\n            bit.add(p, -1)\n    else:\n\
    \        bit.add(dic[q], 1)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/data_structure/BIT2.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/data_structure/BIT2.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/data_structure/BIT2.test.py
- /verify/expansion/$tests/data_structure/BIT2.test.py.html
title: expansion/$tests/data_structure/BIT2.test.py
---
