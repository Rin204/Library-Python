---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ''
    path: src/$tests/math/mat_pow.test.py
    title: src/$tests/math/mat_pow.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def mat_exp(A, B, n, MOD=-1):\n    le = len(A)\n    while n > 0:\n      \
    \  if n & 1:\n            C = [0] * le\n            for i in range(le):\n    \
    \            for j in range(le):\n                    C[i] += A[i][j] * B[j]\n\
    \                    if MOD != -1:\n                        C[i] %= MOD\n    \
    \        B = C\n        C = [[0] * le for _ in range(le)]\n        for i in range(le):\n\
    \            for k in range(le):\n                for j in range(le):\n      \
    \              C[i][j] += A[i][k] * A[k][j]\n                    if MOD != -1:\n\
    \                        C[i][j] %= MOD\n        A = C\n        n >>= 1\n\n  \
    \  return B\n"
  dependsOn: []
  isVerificationFile: false
  path: src/math/mat_exp.py
  requiredBy: []
  timestamp: '2023-07-16 19:41:28+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/math/mat_pow.test.py
documentation_of: src/math/mat_exp.py
layout: document
redirect_from:
- /library/src/math/mat_exp.py
- /library/src/math/mat_exp.py.html
title: src/math/mat_exp.py
---
