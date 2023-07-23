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
  code: "class SWAG:\n    def __init__(self, ope, e):\n        self.L = []\n     \
    \   self.R = []\n        self.Lcum = [e]\n        self.Rall = e\n        self.ope\
    \ = ope\n        self.e = e\n\n    def push(self, x):\n        self.R.append(x)\n\
    \        self.Rall = self.ope(self.Rall, x)\n\n    def pop(self):\n        if\
    \ not self.L:\n            while self.R:\n                self.L.append(self.R.pop())\n\
    \                self.Lcum.append(self.ope(self.L[-1], self.Lcum[-1]))\n     \
    \       self.Rall = self.e\n        self.L.pop()\n        self.Lcum.pop()\n\n\
    \    def prod(self):\n        return self.ope(self.Lcum[-1], self.Rall)\n\n  \
    \  def size(self):\n        return len(self.L) + len(self.R)\n\n    def __len__(self):\n\
    \        return self.size()\n\n    def clear(self):\n        self.L = []\n   \
    \     self.R = []\n        self.Lcum = [self.e]\n        self.Rall = self.e\n"
  dependsOn: []
  isVerificationFile: false
  path: src/data_structure/SWAG.py
  requiredBy: []
  timestamp: '2023-06-29 01:22:58+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: src/data_structure/SWAG.py
layout: document
redirect_from:
- /library/src/data_structure/SWAG.py
- /library/src/data_structure/SWAG.py.html
title: src/data_structure/SWAG.py
---
