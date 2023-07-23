---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
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
  code: "def MillerRabin(n):\n    if n <= 1:\n        return False\n    elif n ==\
    \ 2:\n        return True\n    elif n % 2 == 0:\n        return False\n\n    if\
    \ n < 4759123141:\n        A = [2, 7, 61]\n    else:\n        A = [2, 325, 9375,\
    \ 28178, 450775, 9780504, 1795265022]\n    s = 0\n    d = n - 1\n    while d %\
    \ 2 == 0:\n        s += 1\n        d >>= 1\n\n    for a in A:\n        if a %\
    \ n == 0:\n            return True\n        x = pow(a, d, n)\n        if x !=\
    \ 1:\n            for t in range(s):\n                if x == n - 1:\n       \
    \             break\n                x = x * x % n\n            else:\n      \
    \          return False\n    return True\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/math/MillerRabin.py
  requiredBy: []
  timestamp: '2023-06-10 16:58:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/math/MillerRabin.py
layout: document
redirect_from:
- /library/expansion/math/MillerRabin.py
- /library/expansion/math/MillerRabin.py.html
title: expansion/math/MillerRabin.py
---
