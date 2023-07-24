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
  path: expansion/graph/dijkstra.py
  requiredBy: []
  timestamp: '2023-07-06 22:40:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/graph/dijkstra.py
layout: document
redirect_from:
- /library/expansion/graph/dijkstra.py
- /library/expansion/graph/dijkstra.py.html
title: expansion/graph/dijkstra.py
---
