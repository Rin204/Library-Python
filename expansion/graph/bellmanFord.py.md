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
  code: "def bellmanFord(n, edges, s, inf=1 << 60):\n    \"\"\"\n    edges = [(from1,\
    \ to1, cost1), (from2, to2, cost2), ...)]\n    \"\"\"\n    dist = [inf] * n\n\
    \    dist[s] = 0\n\n    for _ in range(n):\n        update = False\n        for\
    \ u, v, d in edges:\n            if dist[u] != inf and dist[v] > dist[u] + d:\n\
    \                dist[v] = dist[u] + d\n                update = True\n\n    \
    \    if not update:\n            return dist\n\n    return None\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/graph/bellmanFord.py
  requiredBy: []
  timestamp: '2023-07-06 22:40:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/graph/bellmanFord.py
layout: document
title: bellmanFord
---

# 概要
ベルマンフォードです．

$edges = [(from1, to1, cost1), (from2, to2, cost2), ...)]$の形式で辺情報を与えてください

## 使い方
inf は十分に大きい値を適当に設定してください
```
dist = bellmanFord(n, edges, s, inf=1 << 60)
```
負閉路がある場合は None を返します．
