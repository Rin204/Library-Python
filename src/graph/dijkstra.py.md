---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/graph/dijkstra.test.py
    title: src/$tests/graph/dijkstra.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
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
  path: src/graph/dijkstra.py
  requiredBy: []
  timestamp: '2023-07-06 22:40:04+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/graph/dijkstra.test.py
documentation_of: src/graph/dijkstra.py
layout: document
redirect_from:
- /library/src/graph/dijkstra.py
- /library/src/graph/dijkstra.py.html
title: src/graph/dijkstra.py
---
