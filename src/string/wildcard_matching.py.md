---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/convolution/NTT998.py
    title: src/convolution/NTT998.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ''
    path: src/$tests/string/wildcard_matching.test.py
    title: src/$tests/string/wildcard_matching.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import random\n\nfrom src.convolution.NTT998 import NTT998\n\n\ndef wildcard_matching(S,\
    \ T, wild=\"?\"):\n    n = len(S)\n    m = len(T)\n    A = [0] * n\n    B = [0]\
    \ * m\n    dic = {wild: 0}\n    for i, s in enumerate(S):\n        if s not in\
    \ dic:\n            dic[s] = random.randrange(998244353)\n        A[i] = dic[s]\n\
    \    for i, t in enumerate(T):\n        if t not in dic:\n            dic[t] =\
    \ random.randrange(998244353)\n        B[i] = dic[t]\n\n    S1 = [0] * n\n   \
    \ S2 = [0] * n\n    S3 = [0] * n\n    for i, x in enumerate(A):\n        y = int(x\
    \ > 0)\n        S1[i] = y\n        S2[i] = y * x\n        S3[i] = y * x * x %\
    \ 998244353\n\n    T1 = [0] * m\n    T2 = [0] * m\n    T3 = [0] * m\n    for i,\
    \ x in enumerate(B):\n        y = int(x > 0)\n        T1[m - 1 - i] = y\n    \
    \    T2[m - 1 - i] = y * x\n        T3[m - 1 - i] = y * x * x % 998244353\n\n\
    \    res1 = NTT998.multiply(S3, T1)\n    res2 = NTT998.multiply(S2, T2)\n    res3\
    \ = NTT998.multiply(S1, T3)\n    res = []\n    for i in range(n - m + 1):\n  \
    \      x = res1[i + m - 1] - 2 * res2[i + m - 1] + res3[i + m - 1]\n        if\
    \ x == 0:\n            res.append(i)\n\n    return res\n"
  dependsOn:
  - src/convolution/NTT998.py
  isVerificationFile: false
  path: src/string/wildcard_matching.py
  requiredBy: []
  timestamp: '2023-07-29 13:32:11+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/string/wildcard_matching.test.py
documentation_of: src/string/wildcard_matching.py
layout: document
redirect_from:
- /library/src/string/wildcard_matching.py
- /library/src/string/wildcard_matching.py.html
title: src/string/wildcard_matching.py
---
