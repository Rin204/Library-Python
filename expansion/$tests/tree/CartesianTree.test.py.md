---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/cartesian_tree
    links:
    - https://judge.yosupo.jp/problem/cartesian_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cartesian_tree\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\ndef CartesianTree(A):\n    n = len(A)\n    P = [-1] * n\n    B = [-1] * n\n\
    \    p = -1\n\n    for i, a in enumerate(A):\n        while p >= 0 and a < A[B[p]]:\n\
    \            j = B[p]\n            p -= 1\n            if p >= 0 and a < A[B[p]]:\n\
    \                P[j] = B[p]\n            else:\n                P[j] = i\n\n\
    \        p += 1\n        B[p] = i\n\n    for i in range(p, 0, -1):\n        P[B[i]]\
    \ = B[i - 1]\n\n    i = B[0]\n    P[i] = i\n    return P\n\n\nn = int(input())\n\
    A = list(map(int, input().split()))\nprint(*CartesianTree(A))\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/tree/CartesianTree.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/tree/CartesianTree.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/tree/CartesianTree.test.py
- /verify/expansion/$tests/tree/CartesianTree.test.py.html
title: expansion/$tests/tree/CartesianTree.test.py
---
