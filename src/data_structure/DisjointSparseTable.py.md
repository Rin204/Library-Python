---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/data_structure/DisjointSparseTable.test.py
    title: src/$tests/data_structure/DisjointSparseTable.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class DisjointSparseTable:\n    def __init__(self, A, ope):\n        self.n\
    \ = len(A)\n        self.ope = ope\n        self.logn = self.n.bit_length()\n\
    \        self.table = [0] * (self.logn * self.n)\n        for i in range(self.n):\n\
    \            self.table[i] = A[i]\n        for i in range(1, self.logn):\n   \
    \         shift = 1 << i\n            for j in range(0, self.n, shift << 1):\n\
    \                t = min(j + shift, self.n)\n                self.table[i * self.n\
    \ + t - 1] = A[t - 1]\n                for k in range(t - 2, j - 1, -1):\n   \
    \                 self.table[i * self.n + k] = self.ope(A[k], self.table[i * self.n\
    \ + k + 1])\n                if self.n <= t:\n                    break\n    \
    \            self.table[i * self.n + t] = A[t]\n                r = min(t + shift,\
    \ self.n)\n                for k in range(t + 1, r):\n                    self.table[i\
    \ * self.n + k] = self.ope(self.table[i * self.n + k - 1], A[k])\n\n        self.look\
    \ = [0] * (1 << self.logn)\n        for i in range(2, 1 << self.logn):\n     \
    \       self.look[i] = self.look[i >> 1] + 1\n\n    def prod(self, l, r):\n  \
    \      assert l < r\n        r -= 1\n        if l == r:\n            return self.table[l]\n\
    \        logn = self.look[l ^ r]\n        return self.ope(self.table[logn * self.n\
    \ + l], self.table[logn * self.n + r])\n"
  dependsOn: []
  isVerificationFile: false
  path: src/data_structure/DisjointSparseTable.py
  requiredBy: []
  timestamp: '2023-06-29 01:22:58+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/data_structure/DisjointSparseTable.test.py
documentation_of: src/data_structure/DisjointSparseTable.py
layout: document
redirect_from:
- /library/src/data_structure/DisjointSparseTable.py
- /library/src/data_structure/DisjointSparseTable.py.html
title: src/data_structure/DisjointSparseTable.py
---
