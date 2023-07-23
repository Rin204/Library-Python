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
  dependsOn: []
  isVerificationFile: false
  path: src/polynomial/BostanMori998.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: src/polynomial/BostanMori998.py
layout: document
redirect_from:
- /library/src/polynomial/BostanMori998.py
- /library/src/polynomial/BostanMori998.py.html
title: src/polynomial/BostanMori998.py
---
