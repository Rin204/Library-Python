---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bitwise_and_convolution
    links:
    - https://judge.yosupo.jp/problem/bitwise_and_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\ndef and_convolution(A, B, MOD=-1):\n    n = max(len(A), len(B))\n    l = (n\
    \ - 1).bit_length()\n    n = 1 << l\n    A += [0] * (n - len(A))\n    B += [0]\
    \ * (n - len(B))\n\n    def f(A):\n        for i in range(l):\n            for\
    \ bit in range(n):\n                if not bit >> i & 1:\n                   \
    \ A[bit] += A[bit ^ (1 << i)]\n                    if MOD != -1:\n           \
    \             A[bit] %= MOD\n\n    def invf(A):\n        for i in range(l):\n\
    \            for bit in range(n):\n                if not bit >> i & 1:\n    \
    \                A[bit] -= A[bit ^ (1 << i)]\n                    if MOD != -1:\n\
    \                        A[bit] %= MOD\n\n    f(A)\n    f(B)\n    if MOD != -1:\n\
    \        C = [a * b % MOD for a, b in zip(A, B)]\n    else:\n        C = [a *\
    \ b for a, b in zip(A, B)]\n    invf(C)\n    return C\n\n\nn = int(input())\n\
    A = list(map(int, input().split()))\nB = list(map(int, input().split()))\nC =\
    \ and_convolution(A, B, 998244353)\nprint(*C)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/convolution/and_convolution.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/convolution/and_convolution.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/convolution/and_convolution.test.py
- /verify/expansion/$tests/convolution/and_convolution.test.py.html
title: expansion/$tests/convolution/and_convolution.test.py
---
