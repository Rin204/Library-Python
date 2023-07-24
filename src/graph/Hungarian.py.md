---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ''
    path: src/$tests/graph/Hungarian.test.py
    title: src/$tests/graph/Hungarian.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Hungarian(A, inf=1 << 60):\n    n = len(A) + 1\n    m = len(A[0]) + 1\n\
    \    P = [0] * m\n    way = [0] * m\n    U = [0] * n\n    V = [0] * m\n\n    for\
    \ i in range(1, n):\n        P[0] = i\n        minV = [inf] * m\n        used\
    \ = [False] * m\n        j0 = 0\n        while P[j0] != 0:\n            i0 = P[j0]\n\
    \            j1 = 0\n            used[j0] = True\n            delta = inf\n  \
    \          for j in range(1, m):\n                if used[j]:\n              \
    \      continue\n                if i0 == 0 or j == 0:\n                    cur\
    \ = -U[i0] - V[j]\n                else:\n                    cur = A[i0 - 1][j\
    \ - 1] - U[i0] - V[j]\n                if cur < minV[j]:\n                   \
    \ minV[j] = cur\n                    way[j] = j0\n                if minV[j] <\
    \ delta:\n                    delta = minV[j]\n                    j1 = j\n  \
    \          for j in range(m):\n                if used[j]:\n                 \
    \   U[P[j]] += delta\n                    V[j] -= delta\n                else:\n\
    \                    minV[j] -= delta\n            j0 = j1\n        P[j0] = P[way[j0]]\n\
    \        while j0 != 0:\n            j1 = way[j0]\n            P[j0] = P[j1]\n\
    \            j0 = j1\n\n    ret = [-1] * (n - 1)\n    for j in range(1, m):\n\
    \        if P[j] != 0:\n            ret[P[j] - 1] = j - 1\n\n    return -V[0],\
    \ ret\n"
  dependsOn: []
  isVerificationFile: false
  path: src/graph/Hungarian.py
  requiredBy: []
  timestamp: '2023-07-04 23:57:10+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/graph/Hungarian.test.py
documentation_of: src/graph/Hungarian.py
layout: document
redirect_from:
- /library/src/graph/Hungarian.py
- /library/src/graph/Hungarian.py.html
title: src/graph/Hungarian.py
---
