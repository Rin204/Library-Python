---
data:
  _extendedDependsOn: []
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
    \n\ndef floor_sum(n, m, a, b):\n    \"\"\"\n    return \\\\sum_{i=0}^{n-1} ((a*i+b)//m)\n\
    \    \"\"\"\n    ret = 0\n    while True:\n        if a >= m:\n            ret\
    \ += (n - 1) * n // 2 * (a // m)\n            a %= m\n        if b >= m:\n   \
    \         ret += n * (b // m)\n            b %= m\n        y_max = (a * n + b)\
    \ // m\n        if y_max == 0:\n            return ret\n        x_max = y_max\
    \ * m - b\n        ret += (n - (x_max + a - 1) // a) * y_max\n        n, m, a,\
    \ b = y_max, a, m, -x_max % a\n\n\nfor _ in range(int(input())):\n    n, m, a,\
    \ b = map(int, input().split())\n    print(floor_sum(n, m, a, b))\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/math/floor_sum.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/math/floor_sum.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/math/floor_sum.test.py
- /verify/expansion/$tests/math/floor_sum.test.py.html
title: expansion/$tests/math/floor_sum.test.py
---
