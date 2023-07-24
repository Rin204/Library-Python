---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/math/ext_gcd.py
    title: src/math/ext_gcd.py
  _extendedRequiredBy:
  - icon: ''
    path: src/math/CombinationArbitrary.py
    title: src/math/CombinationArbitrary.py
  _extendedVerifiedWith:
  - icon: ''
    path: src/$tests/math/Garner.test.py
    title: src/$tests/math/Garner.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from src.math.ext_gcd import ext_gcd\n\n\ndef Garner(R, M):\n    r = 0\n\
    \    m = 1\n    for ri, mi in zip(R, M):\n        if ri < 0 or mi <= ri:\n   \
    \         ri %= mi\n\n        if m < mi:\n            m, mi = mi, m\n        \
    \    r, ri = ri, r\n\n        if m % mi == 0:\n            if r % mi != ri:\n\
    \                return -1, -1\n            continue\n\n        im, _, g = ext_gcd(m,\
    \ mi)\n        if im < 0:\n            im += mi\n\n        if (ri - r) % g !=\
    \ 0:\n            return -1, -1\n\n        ui = mi // g\n        x = ((ri - r)\
    \ // g % ui) * im % ui\n        r += x * m\n        m *= ui\n\n    return r, m\n"
  dependsOn:
  - src/math/ext_gcd.py
  isVerificationFile: false
  path: src/math/Garner.py
  requiredBy:
  - src/math/CombinationArbitrary.py
  timestamp: '2023-07-06 23:24:06+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/math/Garner.test.py
documentation_of: src/math/Garner.py
layout: document
redirect_from:
- /library/src/math/Garner.py
- /library/src/math/Garner.py.html
title: src/math/Garner.py
---
