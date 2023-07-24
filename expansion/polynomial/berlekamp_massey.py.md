---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def modinv(a, MOD):\n    b = MOD\n    u = 1\n    v = 0\n    while b > 0:\n\
    \        t = a // b\n        a -= t * b\n        u -= t * v\n        a, b = b,\
    \ a\n        u, v = v, u\n\n    if a != 1:\n        return -1\n\n    if u != 0:\n\
    \        u += MOD\n\n    return u\n\n\ndef berlekamp_massey(A, MOD):\n    n =\
    \ len(A)\n    B = [MOD - 1]\n    C = [MOD - 1]\n    y = 1\n    for j in range(1,\
    \ n + 1):\n        l = len(C)\n        m = len(B)\n        x = 0\n        for\
    \ i in range(l):\n            x += C[i] * A[j - l + i]\n            x %= MOD\n\
    \        B.append(0)\n        m += 1\n        if x == 0:\n            continue\n\
    \        freq = x * modinv(y, MOD) % MOD\n        if l < m:\n            tmp =\
    \ C[:]\n            C = [0] * (m - l) + C\n            for i in range(m):\n  \
    \              C[m - 1 - i] -= freq * B[m - 1 - i]\n                C[m - 1 -\
    \ i] %= MOD\n            B = tmp\n            y = x\n        else:\n         \
    \   for i in range(m):\n                C[l - 1 - i] -= freq * B[m - 1 - i]\n\
    \                C[l - 1 - i] %= MOD\n\n    return C[::-1][1:]\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/polynomial/berlekamp_massey.py
  requiredBy: []
  timestamp: '2023-07-23 02:22:37+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/polynomial/berlekamp_massey.py
layout: document
redirect_from:
- /library/expansion/polynomial/berlekamp_massey.py
- /library/expansion/polynomial/berlekamp_massey.py.html
title: expansion/polynomial/berlekamp_massey.py
---