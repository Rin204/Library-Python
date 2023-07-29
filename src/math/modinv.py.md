---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ''
    path: src/math/CombinationArbitrary.py
    title: src/math/CombinationArbitrary.py
  - icon: ''
    path: src/polynomial/BostanMori998.py
    title: src/polynomial/BostanMori998.py
  - icon: ''
    path: src/polynomial/FormalPowerSeries998.py
    title: src/polynomial/FormalPowerSeries998.py
  - icon: ''
    path: src/polynomial/berlekamp_massey.py
    title: src/polynomial/berlekamp_massey.py
  - icon: ''
    path: src/polynomial/berlekamp_massey_global_mod.py
    title: src/polynomial/berlekamp_massey_global_mod.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def modinv(a, MOD):\n    b = MOD\n    u = 1\n    v = 0\n    while b > 0:\n\
    \        t = a // b\n        a -= t * b\n        u -= t * v\n        a, b = b,\
    \ a\n        u, v = v, u\n\n    if a != 1:\n        return -1\n\n    if u != 0:\n\
    \        u += MOD\n\n    return u\n"
  dependsOn: []
  isVerificationFile: false
  path: src/math/modinv.py
  requiredBy:
  - src/math/CombinationArbitrary.py
  - src/polynomial/berlekamp_massey_global_mod.py
  - src/polynomial/FormalPowerSeries998.py
  - src/polynomial/BostanMori998.py
  - src/polynomial/berlekamp_massey.py
  timestamp: '2023-07-09 17:47:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: src/math/modinv.py
layout: document
redirect_from:
- /library/src/math/modinv.py
- /library/src/math/modinv.py.html
title: src/math/modinv.py
---