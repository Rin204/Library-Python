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
    PROBLEM: https://judge.yosupo.jp/problem/point_set_range_composite
    links:
    - https://judge.yosupo.jp/problem/point_set_range_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite\n\
    \nfrom pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \nfrom src.data_structure.SegmentTreeBase_ import SegmentTreeBase_\n\nMOD = 998244353\n\
    \n\nclass PointSetRangeComposite(SegmentTreeBase_):\n    def ope(self, l, r):\n\
    \        a = l >> 30\n        b = l ^ (a << 30)\n        c = r >> 30\n       \
    \ d = r ^ (c << 30)\n\n        e = (a * c) % MOD\n        f = (b * c + d) % MOD\n\
    \n        return (e << 30) | f\n\n    def e(self):\n        return 1 << 30\n\n\
    \nn, Q = map(int, input().split())\nA = [0] * n\nfor i in range(n):\n    a, b\
    \ = map(int, input().split())\n    A[i] = (a << 30) | b\nseg = PointSetRangeComposite(n,\
    \ A)\nfor _ in range(Q):\n    t, p, c, d = map(int, input().split())\n    if t\
    \ == 0:\n        seg[p] = (c << 30) | d\n    else:\n        res = seg.prod(p,\
    \ c)\n        a = res >> 30\n        b = res ^ (a << 30)\n        ans = (a * d\
    \ + b) % MOD\n        print(ans)\n"
  dependsOn:
  - src/data_structure/SegmentTreeBase_.py
  isVerificationFile: true
  path: src/$tests/data_structure/segtree3.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/data_structure/segtree3.test.py
layout: document
redirect_from:
- /verify/src/$tests/data_structure/segtree3.test.py
- /verify/src/$tests/data_structure/segtree3.test.py.html
title: src/$tests/data_structure/segtree3.test.py
---
