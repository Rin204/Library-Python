---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/tree/LCA.py
    title: src/tree/LCA.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/lca
    links:
    - https://judge.yosupo.jp/problem/lca
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.tree.LCA import LCA\n\n\nn, Q = map(int, input().split())\nP = list(map(int,\
    \ input().split()))\nG = LCA(n)\nfor i, p in enumerate(P, 1):\n    G.add_edge(i,\
    \ p)\n\nG.build()\nfor _ in range(Q):\n    u, v = map(int, input().split())\n\
    \    print(G.lca(u, v))\n"
  dependsOn:
  - src/tree/LCA.py
  isVerificationFile: true
  path: src/$tests/tree/LCA.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/tree/LCA.test.py
layout: document
redirect_from:
- /verify/src/$tests/tree/LCA.test.py
- /verify/src/$tests/tree/LCA.test.py.html
title: src/$tests/tree/LCA.test.py
---
