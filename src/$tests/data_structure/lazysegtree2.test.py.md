---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/data_structure/LazySegmentTreeBase_.py
    title: src/data_structure/LazySegmentTreeBase_.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_affine_range_sum
    links:
    - https://judge.yosupo.jp/problem/range_affine_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_range_sum\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.data_structure.LazySegmentTreeBase_ import LazySegmentTreeBase_\n\n\n\
    MOD = 998244353\n\n\nclass RangeAffineRangeSum(LazySegmentTreeBase_):\n    def\
    \ ope(self, l, r):\n        a0 = l >> 30\n        a1 = l ^ (a0 << 30)\n      \
    \  b0 = r >> 30\n        b1 = r ^ (b0 << 30)\n        c0 = (a0 + b0) % MOD\n \
    \       c1 = (a1 + b1) % MOD\n        return (c0 << 30) + c1\n\n    def e(self):\n\
    \        return 0\n\n    def mapping(self, f, x):\n        a0 = f >> 30\n    \
    \    a1 = f ^ (a0 << 30)\n        b0 = x >> 30\n        b1 = x ^ (b0 << 30)\n\
    \        c0 = (a0 * b0 + a1 * b1) % MOD\n        c1 = b1\n        return (c0 <<\
    \ 30) + c1\n\n    def composition(self, f, g):\n        a0 = f >> 30\n       \
    \ a1 = f ^ (a0 << 30)\n        b0 = g >> 30\n        b1 = g ^ (b0 << 30)\n   \
    \     c0 = (a0 * b0) % MOD\n        c1 = (a0 * b1 + a1) % MOD\n        return\
    \ (c0 << 30) + c1\n\n    def id_(self):\n        return 1 << 30\n\n\nn, Q = map(int,\
    \ input().split())\nA = list(map(int, input().split()))\nA = [(a << 30) + 1 for\
    \ a in A]\n\nseg = RangeAffineRangeSum(n, A)\nfor _ in range(Q):\n    query =\
    \ list(map(int, input().split()))\n    if query[0] == 0:\n        l, r, b, c =\
    \ query[1:]\n        seg.apply(l, r, (b << 30) + c)\n    else:\n        l, r =\
    \ query[1:]\n        print(seg.prod(l, r) >> 30)\n"
  dependsOn:
  - src/data_structure/LazySegmentTreeBase_.py
  isVerificationFile: true
  path: src/$tests/data_structure/lazysegtree2.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/data_structure/lazysegtree2.test.py
layout: document
redirect_from:
- /verify/src/$tests/data_structure/lazysegtree2.test.py
- /verify/src/$tests/data_structure/lazysegtree2.test.py.html
title: src/$tests/data_structure/lazysegtree2.test.py
---