---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ''
    path: src/$tests/convolution/xor_convolution.test.py
    title: src/$tests/convolution/xor_convolution.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def xor_convolution(A, B, MOD=-1):\n    \"\"\"\n    MOD \u304C\u5076\u6570\
    \u3060\u3068\u58CA\u308C\u308B\n    MOD = -1 \u3067\u6574\u6570\u6307\u5B9A\u306E\
    \u5834\u5408\uFF0Creturn \u306E\u76F4\u524D\u306E\u3068\u3053\u308D\u3092\u5207\
    \u308A\u6368\u3066\u306B\n    \"\"\"\n    n = max(len(A), len(B))\n    l = (n\
    \ - 1).bit_length()\n    n = 1 << l\n    A += [0] * (n - len(A))\n    B += [0]\
    \ * (n - len(B))\n\n    def f(A):\n        h = 1\n        while h < len(A):\n\
    \            for i in range(0, len(A), h * 2):\n                for j in range(i,\
    \ i + h):\n                    x = A[j]\n                    y = A[j + h]\n  \
    \                  if MOD != -1:\n                        A[j] = (x + y) % MOD\n\
    \                        A[j + h] = (x - y) % MOD\n            h *= 2\n\n    f(A)\n\
    \    f(B)\n    if MOD != -1:\n        C = [a * b % MOD for a, b in zip(A, B)]\n\
    \    else:\n        C = [a * b for a, b in zip(A, B)]\n    f(C)\n    if MOD !=\
    \ -1:\n        inv = pow(n, MOD - 2, MOD)\n        C = [c * inv % MOD for c in\
    \ C]\n    else:\n        C = [c / n for c in C]\n\n    return C\n"
  dependsOn: []
  isVerificationFile: false
  path: src/convolution/xor_convolution.py
  requiredBy: []
  timestamp: '2023-07-16 16:38:14+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/convolution/xor_convolution.test.py
documentation_of: src/convolution/xor_convolution.py
layout: document
redirect_from:
- /library/src/convolution/xor_convolution.py
- /library/src/convolution/xor_convolution.py.html
title: src/convolution/xor_convolution.py
---