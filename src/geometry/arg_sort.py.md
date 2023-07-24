---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ''
    path: src/$tests/geometry/arg_sort.test.py
    title: src/$tests/geometry/arg_sort.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def arg_sort(xy):\n    def _area(p):\n        if p[0] == 0 and p[1] == 0:\n\
    \            return 2\n        elif p[1] < 0:\n            if p[0] < 0:\n    \
    \            return 0\n            else:\n                return 1\n        else:\n\
    \            if p[0] >= 0:\n                return 3\n            else:\n    \
    \            return 4\n\n    def merge_sort(xy):\n        if len(xy) <= 1:\n \
    \           return xy\n        L = xy[: len(xy) // 2]\n        R = xy[len(xy)\
    \ // 2 :]\n        L = merge_sort(L)\n        R = merge_sort(R)\n        res =\
    \ []\n        lp = 0\n        rp = 0\n        while lp < len(L) and rp < len(R):\n\
    \            if _area(L[lp]) < _area(R[rp]):\n                res.append(L[lp])\n\
    \                lp += 1\n            elif _area(L[lp]) > _area(R[rp]):\n    \
    \            res.append(R[rp])\n                rp += 1\n            else:\n \
    \               if L[lp][1] * R[rp][0] < L[lp][0] * R[rp][1]:\n              \
    \      res.append(L[lp])\n                    lp += 1\n                else:\n\
    \                    res.append(R[rp])\n                    rp += 1\n        res\
    \ += L[lp:] + R[rp:]\n        return res\n\n    return merge_sort(xy)\n"
  dependsOn: []
  isVerificationFile: false
  path: src/geometry/arg_sort.py
  requiredBy: []
  timestamp: '2023-07-16 17:06:17+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/geometry/arg_sort.test.py
documentation_of: src/geometry/arg_sort.py
layout: document
redirect_from:
- /library/src/geometry/arg_sort.py
- /library/src/geometry/arg_sort.py.html
title: src/geometry/arg_sort.py
---