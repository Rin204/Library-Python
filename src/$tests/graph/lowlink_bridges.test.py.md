---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/graph/lowLink.py
    title: src/graph/lowLink.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B&lang=ja\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.graph.lowLink import lowLink\n\n\nn, m = map(int, input().split())\n\
    edges = [[] for _ in range(n)]\nfor _ in range(m):\n    a, b = map(int, input().split())\n\
    \    edges[a].append(b)\n    edges[b].append(a)\n\n_, bridges = lowLink(edges)\n\
    bridges.sort(key=lambda x: x[0] * n + x[1])\nfor u, v in bridges:\n    print(u,\
    \ v)\n"
  dependsOn:
  - src/graph/lowLink.py
  isVerificationFile: true
  path: src/$tests/graph/lowlink_bridges.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/graph/lowlink_bridges.test.py
layout: document
redirect_from:
- /verify/src/$tests/graph/lowlink_bridges.test.py
- /verify/src/$tests/graph/lowlink_bridges.test.py.html
title: src/$tests/graph/lowlink_bridges.test.py
---
