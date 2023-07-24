---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bitwise_and_convolution
    links:
    - https://judge.yosupo.jp/problem/bitwise_and_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    MOD = 998244353\n\n\ndef or_convolution_global_mod(A, B):\n    n = max(len(A),\
    \ len(B))\n    l = (n - 1).bit_length()\n    n = 1 << l\n    A += [0] * (n - len(A))\n\
    \    B += [0] * (n - len(B))\n\n    def f(A):\n        for i in range(l):\n  \
    \          for bit in range(n):\n                if bit >> i & 1:\n          \
    \          A[bit] += A[bit ^ (1 << i)]\n                    A[bit] %= MOD\n\n\
    \    def invf(A):\n        for i in range(l):\n            for bit in range(n):\n\
    \                if bit >> i & 1:\n                    A[bit] -= A[bit ^ (1 <<\
    \ i)]\n                    A[bit] %= MOD\n\n    f(A)\n    f(B)\n    C = [a * b\
    \ % MOD for a, b in zip(A, B)]\n    invf(C)\n    return C\n\n\nn = int(input())\n\
    A = list(map(int, input().split()))\nB = list(map(int, input().split()))\nA_ =\
    \ [0] * (1 << n)\nB_ = [0] * (1 << n)\nmask = (1 << n) - 1\nfor i in range(1 <<\
    \ n):\n    A_[i ^ mask] = A[i]\n    B_[i ^ mask] = B[i]\nC_ = or_convolution_global_mod(A_,\
    \ B_)\nC = [0] * (1 << n)\nfor i in range(1 << n):\n    C[i ^ mask] = C_[i]\n\
    print(*C)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/convolution/or_convolution_global.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/convolution/or_convolution_global.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/convolution/or_convolution_global.test.py
- /verify/expansion/$tests/convolution/or_convolution_global.test.py.html
title: expansion/$tests/convolution/or_convolution_global.test.py
---
