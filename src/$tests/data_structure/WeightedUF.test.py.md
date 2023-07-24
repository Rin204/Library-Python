---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/data_structure/WeightedUnionFind.py
    title: src/data_structure/WeightedUnionFind.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_B\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.data_structure.WeightedUnionFind import WeightedUnionFind\n\n\nn, Q =\
    \ map(int, input().split())\nUF = WeightedUnionFind(n)\nfor _ in range(Q):\n \
    \   query = list(map(int, input().split()))\n    if query[0] == 0:\n        x,\
    \ y, z = query[1:]\n        UF.unite(y, x, z)\n    else:\n        x, y = query[1:]\n\
    \        res = UF.diff(y, x)\n        if res is None:\n            print(\"?\"\
    )\n        else:\n            print(res)\n"
  dependsOn:
  - src/data_structure/WeightedUnionFind.py
  isVerificationFile: true
  path: src/$tests/data_structure/WeightedUF.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/data_structure/WeightedUF.test.py
layout: document
redirect_from:
- /verify/src/$tests/data_structure/WeightedUF.test.py
- /verify/src/$tests/data_structure/WeightedUF.test.py.html
title: src/$tests/data_structure/WeightedUF.test.py
---
