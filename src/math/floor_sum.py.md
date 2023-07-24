---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/math/floor_sum.test.py
    title: src/$tests/math/floor_sum.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def floor_sum(n, m, a, b):\n    \"\"\"\n    return \\\\sum_{i=0}^{n-1} ((a*i+b)//m)\n\
    \    \"\"\"\n    ret = 0\n    while True:\n        if a >= m:\n            ret\
    \ += (n - 1) * n // 2 * (a // m)\n            a %= m\n        if b >= m:\n   \
    \         ret += n * (b // m)\n            b %= m\n        y_max = (a * n + b)\
    \ // m\n        if y_max == 0:\n            return ret\n        x_max = y_max\
    \ * m - b\n        ret += (n - (x_max + a - 1) // a) * y_max\n        n, m, a,\
    \ b = y_max, a, m, -x_max % a\n"
  dependsOn: []
  isVerificationFile: false
  path: src/math/floor_sum.py
  requiredBy: []
  timestamp: '2023-06-29 01:22:58+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/math/floor_sum.test.py
documentation_of: src/math/floor_sum.py
layout: document
redirect_from:
- /library/src/math/floor_sum.py
- /library/src/math/floor_sum.py.html
title: src/math/floor_sum.py
---
