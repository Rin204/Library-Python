---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/data_structure/SegmentTreeBase_.py
    title: src/data_structure/SegmentTreeBase_.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/649
    links:
    - https://yukicoder.me/problems/no/649
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/649\n\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \nfrom random import randrange\n\n\nfrom src.data_structure.SegmentTreeBase_ import\
    \ SegmentTreeBase_\n\n\nclass PointAddRangeSum(SegmentTreeBase_):\n    def ope(self,\
    \ l, r):\n        return l + r\n\n    def e(self):\n        return 0\n\n\nQ, k\
    \ = map(int, input().split())\nQuery = []\nX = []\nfor _ in range(Q):\n    query\
    \ = list(map(int, input().split()))\n    if query[0] == 1:\n        X.append(query[1])\n\
    \        Query.append(query[1])\n    else:\n        Query.append(-1)\n\nX = sorted(set(X))\n\
    # \u4E8C\u5206\u63A2\u7D22\u306E\u30C6\u30B9\u30C8\u7528\nadd = randrange(100)\n\
    rev = randrange(2)\nX = [-1] * add + X\nif rev:\n    X = X[::-1]\ndic = {x: i\
    \ for i, x in enumerate(X)}\n\n\nseg = PointAddRangeSum(len(X))\nif not rev:\n\
    \    for q in Query:\n        if q == -1:\n            p = seg.max_right(add,\
    \ lambda x: x < k)\n            if p == len(X):\n                print(-1)\n \
    \           else:\n                print(X[p])\n                seg[p] = seg[p]\
    \ - 1\n        else:\n            seg[dic[q]] = seg[dic[q]] + 1\nelse:\n    for\
    \ q in Query:\n        if q == -1:\n            p = seg.min_left(len(X) - add,\
    \ lambda x: x < k) - 1\n            if p == -1:\n                print(-1)\n \
    \           else:\n                print(X[p])\n                seg[p] = seg[p]\
    \ - 1\n        else:\n            seg[dic[q]] = seg[dic[q]] + 1\n"
  dependsOn:
  - src/data_structure/SegmentTreeBase_.py
  isVerificationFile: true
  path: src/$tests/data_structure/segtree_bisect2.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/data_structure/segtree_bisect2.test.py
layout: document
redirect_from:
- /verify/src/$tests/data_structure/segtree_bisect2.test.py
- /verify/src/$tests/data_structure/segtree_bisect2.test.py.html
title: src/$tests/data_structure/segtree_bisect2.test.py
---
