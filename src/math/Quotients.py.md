---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/math/Quotients.test.py
    title: src/$tests/math/Quotients.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Quotients(n):\n    \"\"\"\n    return [(x_i, l_i, r_i), ...]\n    s.t.\
    \ (n / i) == x \\\\forall i \\\\in [l, r), x_i < x_{i+1}\n    \"\"\"\n\n    ret\
    \ = []\n    l = 1\n    while l <= n:\n        p = n // l\n        r = n // p +\
    \ 1\n        ret.append((p, l, r))\n        l = r\n    return ret[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: src/math/Quotients.py
  requiredBy: []
  timestamp: '2023-07-06 23:56:16+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/math/Quotients.test.py
documentation_of: src/math/Quotients.py
layout: document
redirect_from:
- /library/src/math/Quotients.py
- /library/src/math/Quotients.py.html
title: src/math/Quotients.py
---
