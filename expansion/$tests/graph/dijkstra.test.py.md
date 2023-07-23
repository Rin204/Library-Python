---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    import heapq\n\n\ndef dijkstra(edges, s=0, inf=1 << 60):\n    \"\"\"\n    edges[from]\
    \ = [(to1, cost1), (to2, cost2), ...)]\n    \"\"\"\n    n = len(edges)\n    dist\
    \ = [inf] * n\n    dist[s] = 0\n    hq = [s]\n    while hq:\n        tmp = heapq.heappop(hq)\n\
    \        d = tmp // n\n        pos = tmp - n * d\n        if dist[pos] < d:\n\
    \            continue\n        for npos, c in edges[pos]:\n            if dist[npos]\
    \ > dist[pos] + c:\n                dist[npos] = dist[pos] + c\n             \
    \   heapq.heappush(hq, npos + n * dist[npos])\n\n    return dist\n\n\nn, m, s\
    \ = map(int, input().split())\nedges = [[] for _ in range(n)]\nredges = [[] for\
    \ _ in range(n)]\nfor _ in range(m):\n    u, v, d = map(int, input().split())\n\
    \    edges[u].append((v, d))\n    redges[v].append((u, d))\n\ndist = dijkstra(edges,\
    \ s)\nfor d in dist:\n    if d == 1 << 60:\n        print(\"INF\")\n    else:\n\
    \        print(d)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/graph/dijkstra.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/graph/dijkstra.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/graph/dijkstra.test.py
- /verify/expansion/$tests/graph/dijkstra.test.py.html
title: expansion/$tests/graph/dijkstra.test.py
---
