---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SWAGBase_:\n    def ope(self, l, r):\n        pass\n\n    def e(self):\n\
    \        pass\n\n    def __init__(self):\n        self.L = []\n        self.R\
    \ = []\n        self.Lcum = [self.e()]\n        self.Rall = self.e()\n\n    def\
    \ push(self, x):\n        self.R.append(x)\n        self.Rall = self.ope(self.Rall,\
    \ x)\n\n    def pop(self):\n        if not self.L:\n            while self.R:\n\
    \                self.L.append(self.R.pop())\n                self.Lcum.append(self.ope(self.L[-1],\
    \ self.Lcum[-1]))\n            self.Rall = self.e()\n        self.L.pop()\n  \
    \      self.Lcum.pop()\n\n    def prod(self):\n        return self.ope(self.Lcum[-1],\
    \ self.Rall)\n\n    def size(self):\n        return len(self.L) + len(self.R)\n\
    \n    def __len__(self):\n        return self.size()\n\n    def clear(self):\n\
    \        self.L = []\n        self.R = []\n        self.Lcum = [self.e()]\n  \
    \      self.Rall = self.e()\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/data_structure/SWAGBase_.py
  requiredBy: []
  timestamp: '2023-06-21 23:36:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/data_structure/SWAGBase_.py
layout: document
redirect_from:
- /library/expansion/data_structure/SWAGBase_.py
- /library/expansion/data_structure/SWAGBase_.py.html
title: expansion/data_structure/SWAGBase_.py
---