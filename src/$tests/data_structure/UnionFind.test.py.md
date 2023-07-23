---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    \nfrom pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \nfrom src.data_structure.UnionFind import UnionFind\n\nn, Q = map(int, input().split())\n\
    UF = UnionFind(n)\nans = []\nfor _ in range(Q):\n    t, x, y = map(int, input().split())\n\
    \    if t == 0:\n        UF.unite(x, y)\n    else:\n        if UF.same(x, y):\n\
    \            ans.append(1)\n        else:\n            ans.append(0)\n\nprint(*ans,\
    \ sep=\"\\n\")\n"
  dependsOn: []
  isVerificationFile: true
  path: src/$tests/data_structure/UnionFind.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/data_structure/UnionFind.test.py
layout: document
redirect_from:
- /verify/src/$tests/data_structure/UnionFind.test.py
- /verify/src/$tests/data_structure/UnionFind.test.py.html
title: src/$tests/data_structure/UnionFind.test.py
---
