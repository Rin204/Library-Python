---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/geometry/arg_sort.py
    title: src/geometry/arg_sort.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sort_points_by_argument
    links:
    - https://judge.yosupo.jp/problem/sort_points_by_argument
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sort_points_by_argument\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.geometry.arg_sort import arg_sort\n\n\nn = int(input())\nxy = [list(map(int,\
    \ input().split())) for _ in range(n)]\nxy = arg_sort(xy)\nfor x, y in xy:\n \
    \   print(x, y)\n"
  dependsOn:
  - src/geometry/arg_sort.py
  isVerificationFile: true
  path: src/$tests/geometry/arg_sort.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/geometry/arg_sort.test.py
layout: document
redirect_from:
- /verify/src/$tests/geometry/arg_sort.test.py
- /verify/src/$tests/geometry/arg_sort.test.py.html
title: src/$tests/geometry/arg_sort.test.py
---