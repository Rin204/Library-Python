---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/graph/dijkstra.py
    title: src/graph/dijkstra.py
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
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.graph.dijkstra import dijkstra\n\n\nn, m, s = map(int, input().split())\n\
    edges = [[] for _ in range(n)]\nredges = [[] for _ in range(n)]\nfor _ in range(m):\n\
    \    u, v, d = map(int, input().split())\n    edges[u].append((v, d))\n    redges[v].append((u,\
    \ d))\n\ndist = dijkstra(edges, s)\nfor d in dist:\n    if d == 1 << 60:\n   \
    \     print(\"INF\")\n    else:\n        print(d)\n"
  dependsOn:
  - src/graph/dijkstra.py
  isVerificationFile: true
  path: src/$tests/graph/dijkstra.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/graph/dijkstra.test.py
layout: document
redirect_from:
- /verify/src/$tests/graph/dijkstra.test.py
- /verify/src/$tests/graph/dijkstra.test.py.html
title: src/$tests/graph/dijkstra.test.py
---
