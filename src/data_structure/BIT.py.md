---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ''
    path: src/$tests/data_structure/BIT.test.py
    title: src/$tests/data_structure/BIT.test.py
  - icon: ''
    path: src/$tests/data_structure/BIT2.test.py
    title: src/$tests/data_structure/BIT2.test.py
  - icon: ''
    path: src/$tests/misc/DeletableHeapq.test.py
    title: src/$tests/misc/DeletableHeapq.test.py
  - icon: ''
    path: src/$tests/misc/Mo.test.py
    title: src/$tests/misc/Mo.test.py
  - icon: ''
    path: src/$tests/misc/MoBase_.test.py
    title: src/$tests/misc/MoBase_.test.py
  - icon: ''
    path: src/$tests/tree/CentroidDecomposition.test.py
    title: src/$tests/tree/CentroidDecomposition.test.py
  - icon: ''
    path: src/$tests/tree/HLD.test.py
    title: src/$tests/tree/HLD.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BIT:\n    def __init__(self, n):\n        self.n = n\n        self.data\
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
    \ //= 2\n        return i + 1\n"
  dependsOn: []
  isVerificationFile: false
  path: src/data_structure/BIT.py
  requiredBy: []
  timestamp: '2023-06-10 15:38:57+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/tree/HLD.test.py
  - src/$tests/tree/CentroidDecomposition.test.py
  - src/$tests/data_structure/BIT2.test.py
  - src/$tests/data_structure/BIT.test.py
  - src/$tests/misc/MoBase_.test.py
  - src/$tests/misc/DeletableHeapq.test.py
  - src/$tests/misc/Mo.test.py
documentation_of: src/data_structure/BIT.py
layout: document
redirect_from:
- /library/src/data_structure/BIT.py
- /library/src/data_structure/BIT.py.html
title: src/data_structure/BIT.py
---
