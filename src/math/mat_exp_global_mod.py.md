---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/math/mat_pow_gloabal_mod.test.py
    title: src/$tests/math/mat_pow_gloabal_mod.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "MOD = 998244353\n\n\ndef mat_exp_global_mod(A, B, n):\n    le = len(A)\n\
    \    while n > 0:\n        if n & 1:\n            C = [0] * le\n            for\
    \ i in range(le):\n                for j in range(le):\n                    C[i]\
    \ += A[i][j] * B[j]\n                    C[i] %= MOD\n            B = C\n    \
    \    C = [[0] * le for _ in range(le)]\n        for i in range(le):\n        \
    \    for k in range(le):\n                for j in range(le):\n              \
    \      C[i][j] += A[i][k] * A[k][j]\n                    C[i][j] %= MOD\n    \
    \    A = C\n        n >>= 1\n\n    return B\n"
  dependsOn: []
  isVerificationFile: false
  path: src/math/mat_exp_global_mod.py
  requiredBy: []
  timestamp: '2023-07-16 19:41:28+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/math/mat_pow_gloabal_mod.test.py
documentation_of: src/math/mat_exp_global_mod.py
layout: document
redirect_from:
- /library/src/math/mat_exp_global_mod.py
- /library/src/math/mat_exp_global_mod.py.html
title: src/math/mat_exp_global_mod.py
---
