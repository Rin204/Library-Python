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
  code: "import heapq\n\n\ndef dijkstra(edges, s=0, inf=1 << 60):\n    \"\"\"\n  \
    \  edges[from] = [(to1, cost1), (to2, cost2), ...)]\n    \"\"\"\n    n = len(edges)\n\
    \    dist = [inf] * n\n    dist[s] = 0\n    hq = [s]\n    while hq:\n        tmp\
    \ = heapq.heappop(hq)\n        d = tmp // n\n        pos = tmp - n * d\n     \
    \   if dist[pos] < d:\n            continue\n        for npos, c in edges[pos]:\n\
    \            if dist[npos] > dist[pos] + c:\n                dist[npos] = dist[pos]\
    \ + c\n                heapq.heappush(hq, npos + n * dist[npos])\n\n    return\
    \ dist\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/graph/dijkstra.py
  requiredBy: []
  timestamp: '2023-07-06 22:40:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/graph/dijkstra.py
layout: document
title: dijkstra
---

# 概要
ダイクストラ法です．

$edges[from] = [(to1, cost1), (to2, cost2), ...)]$の形式で辺情報を与えてください

## 使い方
inf は十分に大きい値を適当に設定してください
```
dist = dijkstra(edges, s=0, inf=1 << 60)
```
