---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/graph/mincostflow.py
    title: src/graph/mincostflow.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B&lang=ja\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.graph.mincostflow import mcf_graph\n\n\nn, m, f = map(int, input().split())\n\
    G = mcf_graph(n)\nfor _ in range(m):\n    G.add_edge(*map(int, input().split()))\n\
    \nfl, c = G.flow(0, n - 1, f)\nif fl < f:\n    c = -1\n\nprint(c)\n"
  dependsOn:
  - src/graph/mincostflow.py
  isVerificationFile: true
  path: src/$tests/graph/mincostflow.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/graph/mincostflow.test.py
layout: document
redirect_from:
- /verify/src/$tests/graph/mincostflow.test.py
- /verify/src/$tests/graph/mincostflow.test.py.html
title: src/$tests/graph/mincostflow.test.py
---
