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
  code: "def make_popcount(n):\n    print(\"def popcount(x):\")\n    le = 1\n    while\
    \ le < n:\n        le *= 2\n    five = \"5\" * n\n    print(f\"    x = (x & 0x{five})\
    \ + ((x >> 1) & 0x{five})\")\n    three = \"3\" * n\n    print(f\"    x = (x &\
    \ 0x{three}) + ((x >> 2) & 0x{three})\")\n    d = 1\n    shift = 4\n    while\
    \ shift < le:\n        S = []\n        for _ in range((le + 2 * d - 1) // (2 *\
    \ d)):\n            S += [\"0\"] * d\n            S += [\"f\"] * d\n        S\
    \ = \"\".join(S[-n:])\n        print(f\"    x = (x & 0x{S}) + ((x >> {shift})\
    \ & 0x{S})\")\n        shift <<= 1\n        d <<= 1\n    print(\"    return x\"\
    )\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/misc/make_popcount.py
  requiredBy: []
  timestamp: '2023-06-18 15:16:26+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/misc/make_popcount.py
layout: document
redirect_from:
- /library/expansion/misc/make_popcount.py
- /library/expansion/misc/make_popcount.py.html
title: expansion/misc/make_popcount.py
---
