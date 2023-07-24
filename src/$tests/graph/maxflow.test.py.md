---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/graph/maxflow.py
    title: src/graph/maxflow.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A&lang=jp
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A&lang=jp
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A&lang=jp\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.graph.maxflow import mf_graph\n\n\nn, m = map(int, input().split())\n\
    G = mf_graph(n)\nfor _ in range(m):\n    u, v, c = map(int, input().split())\n\
    \    G.add_edge(u, v, c)\n\nprint(G.flow(0, n - 1))\n"
  dependsOn:
  - src/graph/maxflow.py
  isVerificationFile: true
  path: src/$tests/graph/maxflow.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/graph/maxflow.test.py
layout: document
redirect_from:
- /verify/src/$tests/graph/maxflow.test.py
- /verify/src/$tests/graph/maxflow.test.py.html
title: src/$tests/graph/maxflow.test.py
---
