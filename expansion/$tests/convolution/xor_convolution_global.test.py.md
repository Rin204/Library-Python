---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bitwise_xor_convolution
    links:
    - https://judge.yosupo.jp/problem/bitwise_xor_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_xor_convolution\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    MOD = 998244353\n\n\ndef xor_convolution_global_mod(A, B):\n    n = max(len(A),\
    \ len(B))\n    l = (n - 1).bit_length()\n    n = 1 << l\n    A += [0] * (n - len(A))\n\
    \    B += [0] * (n - len(B))\n\n    def f(A):\n        h = 1\n        while h\
    \ < len(A):\n            for i in range(0, len(A), h * 2):\n                for\
    \ j in range(i, i + h):\n                    x = A[j]\n                    y =\
    \ A[j + h]\n                    A[j] = (x + y) % MOD\n                    A[j\
    \ + h] = (x - y) % MOD\n            h *= 2\n\n    f(A)\n    f(B)\n    C = [a *\
    \ b % MOD for a, b in zip(A, B)]\n    f(C)\n    inv = pow(n, MOD - 2, MOD)\n \
    \   return [c * inv % MOD for c in C]\n\n\nn = int(input())\nA = list(map(int,\
    \ input().split()))\nB = list(map(int, input().split()))\nC = xor_convolution_global_mod(A,\
    \ B)\nprint(*C)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/convolution/xor_convolution_global.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/convolution/xor_convolution_global.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/convolution/xor_convolution_global.test.py
- /verify/expansion/$tests/convolution/xor_convolution_global.test.py.html
title: expansion/$tests/convolution/xor_convolution_global.test.py
---
