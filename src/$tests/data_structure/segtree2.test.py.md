---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/data_structure/SegmentTreeBase_.py
    title: src/data_structure/SegmentTreeBase_.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_range_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\n\
    \nfrom pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \nfrom src.data_structure.SegmentTreeBase_ import SegmentTreeBase_\n\n\nclass\
    \ PointAddRangeSum(SegmentTreeBase_):\n    def ope(self, l, r):\n        return\
    \ l + r\n\n    def e(self):\n        return 0\n\n\nn, Q = map(int, input().split())\n\
    A = list(map(int, input().split()))\nseg = PointAddRangeSum(n, A)\nfor _ in range(Q):\n\
    \    t, p, x = map(int, input().split())\n    if t == 0:\n        seg[p] = seg[p]\
    \ + x\n    else:\n        print(seg.prod(p, x))\n"
  dependsOn:
  - src/data_structure/SegmentTreeBase_.py
  isVerificationFile: true
  path: src/$tests/data_structure/segtree2.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/data_structure/segtree2.test.py
layout: document
redirect_from:
- /verify/src/$tests/data_structure/segtree2.test.py
- /verify/src/$tests/data_structure/segtree2.test.py.html
title: src/$tests/data_structure/segtree2.test.py
---
