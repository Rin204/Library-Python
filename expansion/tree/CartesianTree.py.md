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
  code: "def CartesianTree(A):\n    n = len(A)\n    P = [-1] * n\n    B = [-1] * n\n\
    \    p = -1\n\n    for i, a in enumerate(A):\n        while p >= 0 and a < A[B[p]]:\n\
    \            j = B[p]\n            p -= 1\n            if p >= 0 and a < A[B[p]]:\n\
    \                P[j] = B[p]\n            else:\n                P[j] = i\n\n\
    \        p += 1\n        B[p] = i\n\n    for i in range(p, 0, -1):\n        P[B[i]]\
    \ = B[i - 1]\n\n    i = B[0]\n    P[i] = i\n    return P\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/tree/CartesianTree.py
  requiredBy: []
  timestamp: '2023-07-05 23:59:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/tree/CartesianTree.py
layout: document
title: CartesianTree
---

# 概要
与えられた数列からCartesianTreeを求めます．
返り値は親の index 値を持つ形式（自分自身が親の場合，自分自身の index）


## 使い方
```
par = CartesianTree(A)
```
