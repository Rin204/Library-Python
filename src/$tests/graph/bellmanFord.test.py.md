---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/graph/bellmanFord.py
    title: src/graph/bellmanFord.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=jp
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=jp
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=jp\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.graph.bellmanFord import bellmanFord\n\n\nn, m, s = map(int, input().split())\n\
    edges = [list(map(int, input().split())) for _ in range(m)]\ndist = bellmanFord(n,\
    \ edges, s)\nif dist is None:\n    print(\"NEGATIVE CYCLE\")\nelse:\n    for d\
    \ in dist:\n        if d == 1 << 60:\n            print(\"INF\")\n        else:\n\
    \            print(d)\n"
  dependsOn:
  - src/graph/bellmanFord.py
  isVerificationFile: true
  path: src/$tests/graph/bellmanFord.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/graph/bellmanFord.test.py
layout: document
redirect_from:
- /verify/src/$tests/graph/bellmanFord.test.py
- /verify/src/$tests/graph/bellmanFord.test.py.html
title: src/$tests/graph/bellmanFord.test.py
---
