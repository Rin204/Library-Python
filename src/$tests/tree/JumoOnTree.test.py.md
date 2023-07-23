---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/tree/LCA.py
    title: src/tree/LCA.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/jump_on_tree
    links:
    - https://judge.yosupo.jp/problem/jump_on_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.tree.LCA import LCA\n\n\nn, Q = map(int, input().split())\nG = LCA(n)\n\
    G.read_edges(0)\nG.build()\n\nfor _ in range(Q):\n    u, v, k = map(int, input().split())\n\
    \    print(G.jump(u, v, k))\n"
  dependsOn:
  - src/tree/LCA.py
  isVerificationFile: true
  path: src/$tests/tree/JumoOnTree.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/tree/JumoOnTree.test.py
layout: document
redirect_from:
- /verify/src/$tests/tree/JumoOnTree.test.py
- /verify/src/$tests/tree/JumoOnTree.test.py.html
title: src/$tests/tree/JumoOnTree.test.py
---
