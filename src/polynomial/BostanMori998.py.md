---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/convolution/NTT998.py
    title: src/convolution/NTT998.py
  - icon: ':warning:'
    path: src/math/modinv.py
    title: src/math/modinv.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/polynomial/BostanMori.test.py
    title: src/$tests/polynomial/BostanMori.test.py
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
  code: "from src.convolution.NTT998 import NTT998\nfrom src.math.modinv import modinv\n\
    \n\ndef BostanMori998(P, Q, n):\n    le = max(len(P), len(Q))\n    le = 1 << (le\
    \ - 1).bit_length()\n    P.extend([0] * (le - len(P)))\n    Q.extend([0] * (le\
    \ - len(Q)))\n    while n > 0:\n        P.extend([0] * le)\n        Q.extend([0]\
    \ * le)\n        R = [x * ((1, -1)[i & 1]) for i, x in enumerate(Q)]\n       \
    \ NTT998.butterfly(P)\n        NTT998.butterfly(Q)\n        NTT998.butterfly(R)\n\
    \n        P = [p * r % 998244353 for p, r in zip(P, R)]\n        NTT998.butterfly_inv(P)\n\
    \        P = P[n % 2 :: 2]\n\n        Q = [q * r % 998244353 for q, r in zip(Q,\
    \ R)]\n        NTT998.butterfly_inv(Q)\n        Q = Q[::2]\n\n        n >>= 1\n\
    \    return P[0] * modinv(Q[0], 998244353) % 998244353\n"
  dependsOn:
  - src/math/modinv.py
  - src/convolution/NTT998.py
  isVerificationFile: false
  path: src/polynomial/BostanMori998.py
  requiredBy: []
  timestamp: '2023-07-23 02:22:37+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/polynomial/BostanMori.test.py
documentation_of: src/polynomial/BostanMori998.py
layout: document
redirect_from:
- /library/src/polynomial/BostanMori998.py
- /library/src/polynomial/BostanMori998.py.html
title: src/polynomial/BostanMori998.py
---
