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
  code: "MOD = 998244353\n\n\ndef xor_convolution_global_mod(A, B):\n    n = max(len(A),\
    \ len(B))\n    l = (n - 1).bit_length()\n    n = 1 << l\n    A += [0] * (n - len(A))\n\
    \    B += [0] * (n - len(B))\n\n    def f(A):\n        h = 1\n        while h\
    \ < len(A):\n            for i in range(0, len(A), h * 2):\n                for\
    \ j in range(i, i + h):\n                    x = A[j]\n                    y =\
    \ A[j + h]\n                    A[j] = (x + y) % MOD\n                    A[j\
    \ + h] = (x - y) % MOD\n            h *= 2\n\n    f(A)\n    f(B)\n    C = [a *\
    \ b % MOD for a, b in zip(A, B)]\n    f(C)\n    inv = pow(n, MOD - 2, MOD)\n \
    \   return [c * inv % MOD for c in C]\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/convolution/xor_convolution_global_mod.py
  requiredBy: []
  timestamp: '2023-07-16 16:38:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/convolution/xor_convolution_global_mod.py
layout: document
redirect_from:
- /library/expansion/convolution/xor_convolution_global_mod.py
- /library/expansion/convolution/xor_convolution_global_mod.py.html
title: expansion/convolution/xor_convolution_global_mod.py
---
