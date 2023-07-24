---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ''
    path: src/$tests/string/manacher.test.py
    title: src/$tests/string/manacher.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def manacher(S):\n    n = len(S)\n\n    n = 2 * n + 1\n    L = [0] * n\n\n\
    \    c = 0\n    for i in range(n):\n        j = 2 * c - i\n        if i + L[j]\
    \ < c + L[c]:\n            L[i] = L[j]\n        else:\n            j = c + L[c]\
    \ - i\n            while (\n                i - j >= 0\n                and i\
    \ + j < n\n                and ((i + j) & 1 == 0 or S[(i - j) >> 1] == S[(i +\
    \ j) >> 1])\n            ):\n                j += 1\n            L[i] = j\n  \
    \          c = i\n\n    return [l - 1 for l in L[1 : n - 1]]\n"
  dependsOn: []
  isVerificationFile: false
  path: src/string/manacher.py
  requiredBy: []
  timestamp: '2023-06-29 01:22:58+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/string/manacher.test.py
documentation_of: src/string/manacher.py
layout: document
redirect_from:
- /library/src/string/manacher.py
- /library/src/string/manacher.py.html
title: src/string/manacher.py
---
