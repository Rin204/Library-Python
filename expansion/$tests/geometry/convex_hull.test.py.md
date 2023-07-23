---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_4_A&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_4_A&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_4_A&lang=ja\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\ndef convex_hull(xy, multi=False):\n    xy.sort(key=lambda x: (x[1], x[0]))\n\
    \    res = []\n\n    def cross3(a, b, c):\n        return (b[0] - a[0]) * (c[1]\
    \ - a[1]) - (b[1] - a[1]) * (c[0] - a[0])\n\n    if multi:\n\n        def f(a,\
    \ b, c):\n            return cross3(a, b, c) > 0\n\n    else:\n\n        def f(a,\
    \ b, c):\n            return cross3(a, b, c) >= 0\n\n    for p in xy:\n      \
    \  while len(res) > 1 and f(res[-1], res[-2], p):\n            res.pop()\n   \
    \     res.append(p)\n\n    le = len(res)\n    for p in xy[::-1][1:]:\n       \
    \ while len(res) > le and f(res[-1], res[-2], p):\n            res.pop()\n   \
    \     res.append(p)\n    res.pop()\n    return res\n\n\nn = int(input())\nxy =\
    \ [list(map(int, input().split())) for _ in range(n)]\nres = convex_hull(xy, True)\n\
    print(len(res))\nfor x, y in res:\n    print(x, y)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/geometry/convex_hull.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/geometry/convex_hull.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/geometry/convex_hull.test.py
- /verify/expansion/$tests/geometry/convex_hull.test.py.html
title: expansion/$tests/geometry/convex_hull.test.py
---
