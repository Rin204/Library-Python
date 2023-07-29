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
  code: "def ext_gcd(a, b):\n    \"\"\"\n    return (x, y, gcd(a, b)) s.t. ax + by\
    \ = gcd(a, b)\n    \"\"\"\n    if b == 0:\n        return 1, 0, a\n    else:\n\
    \        y, x, g = ext_gcd(b, a % b)\n        return x, y - (a // b) * x, g\n\n\
    \ndef Garner(R, M):\n    r = 0\n    m = 1\n    for ri, mi in zip(R, M):\n    \
    \    if ri < 0 or mi <= ri:\n            ri %= mi\n\n        if m < mi:\n    \
    \        m, mi = mi, m\n            r, ri = ri, r\n\n        if m % mi == 0:\n\
    \            if r % mi != ri:\n                return -1, -1\n            continue\n\
    \n        im, _, g = ext_gcd(m, mi)\n        if im < 0:\n            im += mi\n\
    \n        if (ri - r) % g != 0:\n            return -1, -1\n\n        ui = mi\
    \ // g\n        x = ((ri - r) // g % ui) * im % ui\n        r += x * m\n     \
    \   m *= ui\n\n    return r, m\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/math/Garner.py
  requiredBy: []
  timestamp: '2023-07-06 23:24:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/math/Garner.py
layout: document
title: Garner
---

# 概要
$R = [R_1, R_2, \ldots]$, $M = [M_1, M_2, \ldots]$

が与えられたときに，
$x \% M_i = R_i$ を満たす x (なければ -1) と M の最小公倍数 を返します．

## 使い方
```python
x, m = Garner(R, M)
```
