---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/data_structure/BIT.py
    title: src/data_structure/BIT.py
  - icon: ':x:'
    path: src/tree/HLD.py
    title: src/tree/HLD.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_path_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_path_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.tree.HLD import HLD\nfrom src.data_structure.BIT import BIT\n\n\nn, Q\
    \ = map(int, input().split())\nA = list(map(int, input().split()))\nG = HLD(n)\n\
    G.read_edges(0)\nG.build()\nA = G.reorder(A)\nbit = BIT(n)\nfor i, a in enumerate(A):\n\
    \    bit.add(i, a)\n\nfor _ in range(Q):\n    query = list(map(int, input().split()))\n\
    \    if query[0] == 0:\n        p, x = query[1:]\n        bit.add(G.L[p], x)\n\
    \    else:\n        u, v = query[1:]\n        ans = 0\n        for l, r in G.get_path(u,\
    \ v):\n            l = G.L[l]\n            r = G.L[r]\n            if l > r:\n\
    \                l, r = r, l\n            ans += bit.sum(l, r + 1)\n        print(ans)\n"
  dependsOn:
  - src/data_structure/BIT.py
  - src/tree/HLD.py
  isVerificationFile: true
  path: src/$tests/tree/HLD.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/tree/HLD.test.py
layout: document
redirect_from:
- /verify/src/$tests/tree/HLD.test.py
- /verify/src/$tests/tree/HLD.test.py.html
title: src/$tests/tree/HLD.test.py
---
