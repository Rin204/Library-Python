---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ''
    path: src/$tests/convolution/and_convolution.test.py
    title: src/$tests/convolution/and_convolution.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def and_convolution(A, B, MOD=-1):\n    n = max(len(A), len(B))\n    l =\
    \ (n - 1).bit_length()\n    n = 1 << l\n    A += [0] * (n - len(A))\n    B +=\
    \ [0] * (n - len(B))\n\n    def f(A):\n        for i in range(l):\n          \
    \  for bit in range(n):\n                if not bit >> i & 1:\n              \
    \      A[bit] += A[bit ^ (1 << i)]\n                    if MOD != -1:\n      \
    \                  A[bit] %= MOD\n\n    def invf(A):\n        for i in range(l):\n\
    \            for bit in range(n):\n                if not bit >> i & 1:\n    \
    \                A[bit] -= A[bit ^ (1 << i)]\n                    if MOD != -1:\n\
    \                        A[bit] %= MOD\n\n    f(A)\n    f(B)\n    if MOD != -1:\n\
    \        C = [a * b % MOD for a, b in zip(A, B)]\n    else:\n        C = [a *\
    \ b for a, b in zip(A, B)]\n    invf(C)\n    return C\n"
  dependsOn: []
  isVerificationFile: false
  path: src/convolution/and_convolution.py
  requiredBy: []
  timestamp: '2023-07-16 16:38:14+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/convolution/and_convolution.test.py
documentation_of: src/convolution/and_convolution.py
layout: document
redirect_from:
- /library/src/convolution/and_convolution.py
- /library/src/convolution/and_convolution.py.html
title: src/convolution/and_convolution.py
---
