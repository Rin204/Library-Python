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
  code: "def manacher(S):\n    n = len(S)\n\n    n = 2 * n + 1\n    L = [0] * n\n\n\
    \    c = 0\n    for i in range(n):\n        j = 2 * c - i\n        if i + L[j]\
    \ < c + L[c]:\n            L[i] = L[j]\n        else:\n            j = c + L[c]\
    \ - i\n            while (\n                i - j >= 0\n                and i\
    \ + j < n\n                and ((i + j) & 1 == 0 or S[(i - j) >> 1] == S[(i +\
    \ j) >> 1])\n            ):\n                j += 1\n            L[i] = j\n  \
    \          c = i\n\n    return [l - 1 for l in L[1 : n - 1]]\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/string/manacher.py
  requiredBy: []
  timestamp: '2023-06-16 01:59:35+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/string/manacher.py
layout: document
redirect_from:
- /library/expansion/string/manacher.py
- /library/expansion/string/manacher.py.html
title: expansion/string/manacher.py
---
