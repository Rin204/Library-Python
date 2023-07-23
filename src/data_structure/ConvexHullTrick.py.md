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
  code: "from collections import deque\n\n\nclass ConvexHullTrick:\n    def __init__(self):\n\
    \        self.deq = deque()\n\n    def check(f1, f2, f3):\n        return (f2[0]\
    \ - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])\n\n    def f(self,\
    \ _f, x):\n        return _f[0] * x + _f[1]\n\n    def add_line(self, a, b):\n\
    \        \"\"\"\n        add  f_i(x) = a * x + b\n        \"\"\"\n        f =\
    \ (a, b)\n        while len(self.deq) >= 2 and ConvexHullTrick.check(self.deq[-2],\
    \ self.deq[-1], f):\n            self.deq.pop()\n        self.deq.append(f)\n\n\
    \    def get(self, x):\n        \"\"\"\n        return min_i f_i(x)\n        \"\
    \"\"\n        while len(self.deq) >= 2 and self.f(self.deq[0], x) >= self.f(self.deq[1],\
    \ x):\n            self.deq.popleft()\n\n        return self.f(self.deq[0], x)\n"
  dependsOn: []
  isVerificationFile: false
  path: src/data_structure/ConvexHullTrick.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: src/data_structure/ConvexHullTrick.py
layout: document
redirect_from:
- /library/src/data_structure/ConvexHullTrick.py
- /library/src/data_structure/ConvexHullTrick.py.html
title: src/data_structure/ConvexHullTrick.py
---
