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
  code: "class MoBase_:\n    def add_left(self, i):\n        pass\n\n    def add_right(self,\
    \ i):\n        pass\n\n    def delete_left(self, i):\n        pass\n\n    def\
    \ delete_right(self, i):\n        pass\n\n    def rem(self, i):\n        pass\n\
    \n    def __init__(self, n, Q):\n        self.n = n\n        self.Q = Q\n    \
    \    self.width = int(max(1, n / max(1, Q * 2.0 / 3.0) ** 0.5))\n        self.L\
    \ = []\n        self.R = []\n\n    def insert(self, l, r):\n        self.L.append(l)\n\
    \        self.R.append(r)\n\n    def run(self):\n        def cmp(i):\n       \
    \     b = self.L[i] // self.width\n            res = b * self.n * 3\n        \
    \    if b % 2 == 0:\n                res += self.R[i]\n            else:\n   \
    \             res -= self.R[i]\n            return res\n\n        order = [(i,\
    \ cmp(i)) for i in range(self.Q)]\n\n        order.sort(key=lambda x: x[1])\n\
    \        nl = 0\n        nr = 0\n        for i, _ in order:\n            l = self.L[i]\n\
    \            r = self.R[i]\n            while nl > l:\n                nl -= 1\n\
    \                self.add_left(nl)\n            while nr < r:\n              \
    \  self.add_right(nr)\n                nr += 1\n            while nl < l:\n  \
    \              self.delete_left(nl)\n                nl += 1\n            while\
    \ nr > r:\n                nr -= 1\n                self.delete_right(nr)\n  \
    \          self.rem(i)\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/misc/MoBase_.py
  requiredBy: []
  timestamp: '2023-07-15 01:13:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/misc/MoBase_.py
layout: document
redirect_from:
- /library/expansion/misc/MoBase_.py
- /library/expansion/misc/MoBase_.py.html
title: expansion/misc/MoBase_.py
---
