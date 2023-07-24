---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/math/floor_sum.py
    title: src/math/floor_sum.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sum_of_floor_of_linear
    links:
    - https://judge.yosupo.jp/problem/sum_of_floor_of_linear
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sum_of_floor_of_linear\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.math.floor_sum import floor_sum\n\n\nfor _ in range(int(input())):\n\
    \    n, m, a, b = map(int, input().split())\n    print(floor_sum(n, m, a, b))\n"
  dependsOn:
  - src/math/floor_sum.py
  isVerificationFile: true
  path: src/$tests/math/floor_sum.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/math/floor_sum.test.py
layout: document
redirect_from:
- /verify/src/$tests/math/floor_sum.test.py
- /verify/src/$tests/math/floor_sum.test.py.html
title: src/$tests/math/floor_sum.test.py
---
