---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/649
    links:
    - https://yukicoder.me/problems/no/649
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/649\n\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \nfrom random import randrange\nfrom src.data_structure.SegmentTree import SegmentTree\n\
    \nQ, k = map(int, input().split())\nQuery = []\nX = []\nfor _ in range(Q):\n \
    \   query = list(map(int, input().split()))\n    if query[0] == 1:\n        X.append(query[1])\n\
    \        Query.append(query[1])\n    else:\n        Query.append(-1)\n\nX = sorted(set(X))\n\
    # \u4E8C\u5206\u63A2\u7D22\u306E\u30C6\u30B9\u30C8\u7528\nadd = randrange(100)\n\
    rev = randrange(2)\nX = [-1] * add + X\nif rev:\n    X = X[::-1]\ndic = {x: i\
    \ for i, x in enumerate(X)}\n\n\ndef ope(l, r):\n    return l + r\n\n\nseg = SegmentTree(len(X),\
    \ ope, 0)\nif not rev:\n    for q in Query:\n        if q == -1:\n           \
    \ p = seg.max_right(add, lambda x: x < k)\n            if p == len(X):\n     \
    \           print(-1)\n            else:\n                print(X[p])\n      \
    \          seg[p] = seg[p] - 1\n        else:\n            seg[dic[q]] = seg[dic[q]]\
    \ + 1\nelse:\n    for q in Query:\n        if q == -1:\n            p = seg.min_left(len(X)\
    \ - add, lambda x: x < k) - 1\n            if p == -1:\n                print(-1)\n\
    \            else:\n                print(X[p])\n                seg[p] = seg[p]\
    \ - 1\n        else:\n            seg[dic[q]] = seg[dic[q]] + 1\n"
  dependsOn: []
  isVerificationFile: true
  path: src/$tests/data_structure/segtree_bisect.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/data_structure/segtree_bisect.test.py
layout: document
redirect_from:
- /verify/src/$tests/data_structure/segtree_bisect.test.py
- /verify/src/$tests/data_structure/segtree_bisect.test.py.html
title: src/$tests/data_structure/segtree_bisect.test.py
---
