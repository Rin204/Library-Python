---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/data_structure/DisjointSparseTable.py
    title: src/data_structure/DisjointSparseTable.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_sum
    links:
    - https://judge.yosupo.jp/problem/static_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.data_structure.DisjointSparseTable import DisjointSparseTable\n\n\ndef\
    \ ope(l, r):\n    return l + r\n\n\nn, Q = map(int, input().split())\nA = list(map(int,\
    \ input().split()))\nst = DisjointSparseTable(A, ope)\nfor _ in range(Q):\n  \
    \  l, r = map(int, input().split())\n    print(st.prod(l, r))\n"
  dependsOn:
  - src/data_structure/DisjointSparseTable.py
  isVerificationFile: true
  path: src/$tests/data_structure/DisjointSparseTable.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/data_structure/DisjointSparseTable.test.py
layout: document
redirect_from:
- /verify/src/$tests/data_structure/DisjointSparseTable.test.py
- /verify/src/$tests/data_structure/DisjointSparseTable.test.py.html
title: src/$tests/data_structure/DisjointSparseTable.test.py
---