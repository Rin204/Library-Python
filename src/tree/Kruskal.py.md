---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/data_structure/UnionFind.py
    title: src/data_structure/UnionFind.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/tree/Kruskal.test.py
    title: src/$tests/tree/Kruskal.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from src.data_structure.UnionFind import UnionFind\r\n\r\n\r\ndef Kruskal(n,\
    \ edges, is_sorted=False):\r\n    if n == 1:\r\n        return 0\r\n    if not\
    \ is_sorted:\r\n        edges.sort(key=lambda x: x[2])\r\n    UF = UnionFind(n)\r\
    \n    res = 0\r\n    for u, v, cost in edges:\r\n        if UF.unite(u, v):\r\n\
    \            res += cost\r\n            if UF.group == 1:\r\n                return\
    \ res\r\n    return -1\r\n"
  dependsOn:
  - src/data_structure/UnionFind.py
  isVerificationFile: false
  path: src/tree/Kruskal.py
  requiredBy: []
  timestamp: '2023-06-18 16:34:12+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/tree/Kruskal.test.py
documentation_of: src/tree/Kruskal.py
layout: document
redirect_from:
- /library/src/tree/Kruskal.py
- /library/src/tree/Kruskal.py.html
title: src/tree/Kruskal.py
---
