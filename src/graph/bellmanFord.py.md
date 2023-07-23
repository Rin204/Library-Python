---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/graph/bellmanFord.test.py
    title: src/$tests/graph/bellmanFord.test.py
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
  code: "def bellmanFord(n, edges, s, inf=1 << 60):\n    \"\"\"\n    edges = [(from1,\
    \ to1, cost1), (from2, to2, cost2), ...)]\n    \"\"\"\n    dist = [inf] * n\n\
    \    dist[s] = 0\n\n    for _ in range(n):\n        update = False\n        for\
    \ u, v, d in edges:\n            if dist[u] != inf and dist[v] > dist[u] + d:\n\
    \                dist[v] = dist[u] + d\n                update = True\n\n    \
    \    if not update:\n            return dist\n\n    return None\n"
  dependsOn: []
  isVerificationFile: false
  path: src/graph/bellmanFord.py
  requiredBy: []
  timestamp: '2023-07-06 22:40:04+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/graph/bellmanFord.test.py
documentation_of: src/graph/bellmanFord.py
layout: document
redirect_from:
- /library/src/graph/bellmanFord.py
- /library/src/graph/bellmanFord.py.html
title: src/graph/bellmanFord.py
---
