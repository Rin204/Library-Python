---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/convolution/and_convolution_global.test.py
    title: src/$tests/convolution/and_convolution_global.test.py
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
  code: "MOD = 998244353\n\n\ndef and_convolution_global_mod(A, B):\n    n = max(len(A),\
    \ len(B))\n    l = (n - 1).bit_length()\n    n = 1 << l\n    A += [0] * (n - len(A))\n\
    \    B += [0] * (n - len(B))\n\n    def f(A):\n        for i in range(l):\n  \
    \          for bit in range(n):\n                if not bit >> i & 1:\n      \
    \              A[bit] += A[bit ^ (1 << i)]\n                    A[bit] %= MOD\n\
    \n    def invf(A):\n        for i in range(l):\n            for bit in range(n):\n\
    \                if not bit >> i & 1:\n                    A[bit] -= A[bit ^ (1\
    \ << i)]\n                    A[bit] %= MOD\n\n    f(A)\n    f(B)\n    C = [a\
    \ * b % MOD for a, b in zip(A, B)]\n    invf(C)\n    return C\n"
  dependsOn: []
  isVerificationFile: false
  path: src/convolution/and_convolution_global_mod.py
  requiredBy: []
  timestamp: '2023-07-16 16:38:14+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/convolution/and_convolution_global.test.py
documentation_of: src/convolution/and_convolution_global_mod.py
layout: document
redirect_from:
- /library/src/convolution/and_convolution_global_mod.py
- /library/src/convolution/and_convolution_global_mod.py.html
title: src/convolution/and_convolution_global_mod.py
---
