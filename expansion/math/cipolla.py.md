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
  code: "def cipolla(x, MOD):\n    if MOD == 2:\n        return x\n    elif x == 0:\n\
    \        return 0\n    elif pow(x, (MOD - 1) // 2, MOD) != 1:\n        return\
    \ -1\n\n    y = 1\n    while pow((y * y - x) % MOD, (MOD - 1) // 2, MOD) == 1:\n\
    \        y += 1\n\n    base = (y * y - x) % MOD\n\n    def multi(a0, b0, a1, b1):\n\
    \        return (a0 * a1 + base * (b0 * b1 % MOD)) % MOD, (a0 * b1 + a1 * b0)\
    \ % MOD\n\n    def pow_(a, b, n):\n        if n == 0:\n            return 1, 0\n\
    \n        tmp = multi(a, b, a, b)\n        ret = pow_(tmp[0], tmp[1], n >> 1)\n\
    \        if n & 1:\n            ret = multi(ret[0], ret[1], a, b)\n\n        return\
    \ ret\n\n    return pow_(y, 1, (MOD + 1) // 2)[0]\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/math/cipolla.py
  requiredBy: []
  timestamp: '2023-07-22 13:02:18+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/math/cipolla.py
layout: document
title: cipolla
---

# 概要
$x ^ 2 \equiv y \pmod P$ を満たす x を返します．

## 使い方
```python
x = cipolla(y, P)
```