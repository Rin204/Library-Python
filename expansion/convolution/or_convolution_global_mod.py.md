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
  code: "MOD = 998244353\n\n\ndef or_convolution_global_mod(A, B):\n    n = max(len(A),\
    \ len(B))\n    l = (n - 1).bit_length()\n    n = 1 << l\n    A += [0] * (n - len(A))\n\
    \    B += [0] * (n - len(B))\n\n    def f(A):\n        for i in range(l):\n  \
    \          for bit in range(n):\n                if bit >> i & 1:\n          \
    \          A[bit] += A[bit ^ (1 << i)]\n                    A[bit] %= MOD\n\n\
    \    def invf(A):\n        for i in range(l):\n            for bit in range(n):\n\
    \                if bit >> i & 1:\n                    A[bit] -= A[bit ^ (1 <<\
    \ i)]\n                    A[bit] %= MOD\n\n    f(A)\n    f(B)\n    C = [a * b\
    \ % MOD for a, b in zip(A, B)]\n    invf(C)\n    return C\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/convolution/or_convolution_global_mod.py
  requiredBy: []
  timestamp: '2023-07-16 16:38:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/convolution/or_convolution_global_mod.py
layout: document
redirect_from:
- /library/expansion/convolution/or_convolution_global_mod.py
- /library/expansion/convolution/or_convolution_global_mod.py.html
title: expansion/convolution/or_convolution_global_mod.py
---
