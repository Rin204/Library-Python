---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
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
  path: expansion/math/floor_sum.py
  requiredBy: []
  timestamp: '2023-06-27 23:34:17+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/math/floor_sum.py
layout: document
title: floor_sum
---

# 概要
$\sum_{i=0}^{n-1} ((a*i+b)//m)$ を求めます

## 使い方
```python
res = floor_sum(n, m, a, b)
```
