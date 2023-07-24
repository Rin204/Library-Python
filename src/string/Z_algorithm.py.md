---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ''
    path: src/$tests/string/Z_algorithm.test.py
    title: src/$tests/string/Z_algorithm.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def Z_algorithm(S):\n    le = len(S)\n    Z = [0] * le\n    Z[0] = le\n \
    \   i = 1\n    j = 0\n    while i < le:\n        while i + j < le and S[j] ==\
    \ S[i + j]:\n            j += 1\n        Z[i] = j\n        if j == 0:\n      \
    \      i += 1\n            continue\n\n        k = 1\n        while i + k < le\
    \ and k + Z[k] < j:\n            Z[i + k] = Z[k]\n            k += 1\n       \
    \ i += k\n        j -= k\n    return Z\n"
  dependsOn: []
  isVerificationFile: false
  path: src/string/Z_algorithm.py
  requiredBy: []
  timestamp: '2023-06-29 01:22:58+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/string/Z_algorithm.test.py
documentation_of: src/string/Z_algorithm.py
layout: document
redirect_from:
- /library/src/string/Z_algorithm.py
- /library/src/string/Z_algorithm.py.html
title: src/string/Z_algorithm.py
---
