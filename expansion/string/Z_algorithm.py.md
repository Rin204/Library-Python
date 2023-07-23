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
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Z_algorithm(S):\n    le = len(S)\n    Z = [0] * le\n    Z[0] = le\n \
    \   i = 1\n    j = 0\n    while i < le:\n        while i + j < le and S[j] ==\
    \ S[i + j]:\n            j += 1\n        Z[i] = j\n        if j == 0:\n      \
    \      i += 1\n            continue\n\n        k = 1\n        while i + k < le\
    \ and k + Z[k] < j:\n            Z[i + k] = Z[k]\n            k += 1\n       \
    \ i += k\n        j -= k\n    return Z\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/string/Z_algorithm.py
  requiredBy: []
  timestamp: '2023-06-16 01:52:55+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/string/Z_algorithm.py
layout: document
redirect_from:
- /library/expansion/string/Z_algorithm.py
- /library/expansion/string/Z_algorithm.py.html
title: expansion/string/Z_algorithm.py
---
