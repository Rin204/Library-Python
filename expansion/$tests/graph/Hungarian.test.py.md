---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/assignment
    links:
    - https://judge.yosupo.jp/problem/assignment
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/assignment\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\ndef Hungarian(A, inf=1 << 60):\n    n = len(A) + 1\n    m = len(A[0]) + 1\n\
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
    \ ret\n\n\nn = int(input())\nA = [list(map(int, input().split())) for _ in range(n)]\n\
    mi, assign = Hungarian(A)\nprint(mi)\nprint(*assign)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/graph/Hungarian.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/graph/Hungarian.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/graph/Hungarian.test.py
- /verify/expansion/$tests/graph/Hungarian.test.py.html
title: expansion/$tests/graph/Hungarian.test.py
---
