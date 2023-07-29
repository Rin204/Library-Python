---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/geometry/convex_hull.py
    title: src/geometry/convex_hull.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_4_A&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_4_A&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_4_A&lang=ja\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.geometry.convex_hull import convex_hull\n\n\nn = int(input())\nxy = [list(map(int,\
    \ input().split())) for _ in range(n)]\nres = convex_hull(xy, True)\nprint(len(res))\n\
    for x, y in res:\n    print(x, y)\n"
  dependsOn:
  - src/geometry/convex_hull.py
  isVerificationFile: true
  path: src/$tests/geometry/convex_hull.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/geometry/convex_hull.test.py
layout: document
redirect_from:
- /verify/src/$tests/geometry/convex_hull.test.py
- /verify/src/$tests/geometry/convex_hull.test.py.html
title: src/$tests/geometry/convex_hull.test.py
---