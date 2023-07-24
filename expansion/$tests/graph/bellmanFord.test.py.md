---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=jp
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=jp
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=jp\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\ndef bellmanFord(n, edges, s, inf=1 << 60):\n    \"\"\"\n    edges = [(from1,\
    \ to1, cost1), (from2, to2, cost2), ...)]\n    \"\"\"\n    dist = [inf] * n\n\
    \    dist[s] = 0\n\n    for _ in range(n):\n        update = False\n        for\
    \ u, v, d in edges:\n            if dist[u] != inf and dist[v] > dist[u] + d:\n\
    \                dist[v] = dist[u] + d\n                update = True\n\n    \
    \    if not update:\n            return dist\n\n    return None\n\n\nn, m, s =\
    \ map(int, input().split())\nedges = [list(map(int, input().split())) for _ in\
    \ range(m)]\ndist = bellmanFord(n, edges, s)\nif dist is None:\n    print(\"NEGATIVE\
    \ CYCLE\")\nelse:\n    for d in dist:\n        if d == 1 << 60:\n            print(\"\
    INF\")\n        else:\n            print(d)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/graph/bellmanFord.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/graph/bellmanFord.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/graph/bellmanFord.test.py
- /verify/expansion/$tests/graph/bellmanFord.test.py.html
title: expansion/$tests/graph/bellmanFord.test.py
---
