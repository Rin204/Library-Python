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
  code: "def popcount32(x):\n    x = x - ((x >> 1) & 0x55555555)\n    x = (x & 0x33333333)\
    \ + ((x >> 2) & 0x33333333)\n    x = (x + (x >> 4)) & 0x0F0F0F0F\n    x += x >>\
    \ 8\n    x += x >> 16\n    return x & 0x0000003F\n\n\ndef popcount64(x):\n   \
    \ x = (x & 0x5555555555555555) + ((x >> 1) & 0x5555555555555555)\n    x = (x &\
    \ 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)\n    x = (x & 0x0F0F0F0F0F0F0F0F)\
    \ + ((x >> 4) & 0x0F0F0F0F0F0F0F0F)\n    x = (x & 0x00FF00FF00FF00FF) + ((x >>\
    \ 8) & 0x00FF00FF00FF00FF)\n    x = (x & 0x0000FFFF0000FFFF) + ((x >> 16) & 0x0000FFFF0000FFFF)\n\
    \    x = (x & 0x00000000FFFFFFFF) + ((x >> 32) & 0x00000000FFFFFFFF)\n    return\
    \ x\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/misc/popcount.py
  requiredBy: []
  timestamp: '2023-06-18 15:16:26+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/misc/popcount.py
layout: document
redirect_from:
- /library/expansion/misc/popcount.py
- /library/expansion/misc/popcount.py.html
title: expansion/misc/popcount.py
---
