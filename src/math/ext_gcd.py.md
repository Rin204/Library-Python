---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: src/math/Garner.py
    title: src/math/Garner.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def ext_gcd(a, b):\n    \"\"\"\n    return (x, y, gcd(a, b)) s.t. ax + by\
    \ = gcd(a, b)\n    \"\"\"\n    if b == 0:\n        return 1, 0, a\n    else:\n\
    \        y, x, g = ext_gcd(b, a % b)\n        return x, y - (a // b) * x, g\n"
  dependsOn: []
  isVerificationFile: false
  path: src/math/ext_gcd.py
  requiredBy:
  - src/math/Garner.py
  timestamp: '2023-06-29 01:22:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: src/math/ext_gcd.py
layout: document
redirect_from:
- /library/src/math/ext_gcd.py
- /library/src/math/ext_gcd.py.html
title: src/math/ext_gcd.py
---
