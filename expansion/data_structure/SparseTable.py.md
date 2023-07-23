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
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SparseTable:\n    def __init__(self, A, ope):\n        self.n = len(A)\n\
    \        self.ope = ope\n        self.logn = (self.n - 1).bit_length()\n     \
    \   if self.n == 1:\n            self.logn = 1\n        self.table = [0] * (self.logn\
    \ * self.n)\n        for i in range(self.n):\n            self.table[i] = A[i]\n\
    \        for i in range(1, self.logn):\n            ma = self.n - (1 << i) + 1\n\
    \            d = 1 << (i - 1)\n            for j in range(ma):\n             \
    \   self.table[i * self.n + j] = ope(\n                    self.table[(i - 1)\
    \ * self.n + j], self.table[(i - 1) * self.n + j + d]\n                )\n\n \
    \       self.look = [0] * self.n\n        for i in range(2, self.n):\n       \
    \     self.look[i] = self.look[i >> 1] + 1\n\n    def prod(self, l, r):\n    \
    \    assert l < r\n        d = r - l\n        if d == 1:\n            return self.table[l]\n\
    \        logn = self.look[d - 1]\n        return self.ope(self.table[logn * self.n\
    \ + l], self.table[logn * self.n + r - (1 << logn)])\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/data_structure/SparseTable.py
  requiredBy: []
  timestamp: '2023-06-19 22:23:20+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/data_structure/SparseTable.py
layout: document
redirect_from:
- /library/expansion/data_structure/SparseTable.py
- /library/expansion/data_structure/SparseTable.py.html
title: expansion/data_structure/SparseTable.py
---
