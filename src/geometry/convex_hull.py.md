---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/geometry/convex_hull.test.py
    title: src/$tests/geometry/convex_hull.test.py
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
  code: "def convex_hull(xy, multi=False):\n    xy.sort(key=lambda x: (x[1], x[0]))\n\
    \    res = []\n\n    def cross3(a, b, c):\n        return (b[0] - a[0]) * (c[1]\
    \ - a[1]) - (b[1] - a[1]) * (c[0] - a[0])\n\n    if multi:\n\n        def f(a,\
    \ b, c):\n            return cross3(a, b, c) > 0\n\n    else:\n\n        def f(a,\
    \ b, c):\n            return cross3(a, b, c) >= 0\n\n    for p in xy:\n      \
    \  while len(res) > 1 and f(res[-1], res[-2], p):\n            res.pop()\n   \
    \     res.append(p)\n\n    le = len(res)\n    for p in xy[::-1][1:]:\n       \
    \ while len(res) > le and f(res[-1], res[-2], p):\n            res.pop()\n   \
    \     res.append(p)\n    res.pop()\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: src/geometry/convex_hull.py
  requiredBy: []
  timestamp: '2023-07-16 17:06:17+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/geometry/convex_hull.test.py
documentation_of: src/geometry/convex_hull.py
layout: document
redirect_from:
- /library/src/geometry/convex_hull.py
- /library/src/geometry/convex_hull.py.html
title: src/geometry/convex_hull.py
---
