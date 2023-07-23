---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: src/polynomial/FormalPowerSeries998.py
    title: src/polynomial/FormalPowerSeries998.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/math/Catalan.test.py
    title: src/$tests/math/Catalan.test.py
  - icon: ':x:'
    path: src/$tests/math/Combination.test.py
    title: src/$tests/math/Combination.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Combination:\n    def __init__(self, n, MOD=998244353):\n        self.fact\
    \ = [1] * (n + 1)\n        self.invfact = [1] * (n + 1)\n        self.MOD = MOD\n\
    \        for i in range(1, n + 1):\n            self.fact[i] = self.fact[i - 1]\
    \ * i % MOD\n\n        self.invfact[n] = pow(self.fact[n], MOD - 2, MOD)\n   \
    \     for i in range(n - 1, -1, -1):\n            self.invfact[i] = self.invfact[i\
    \ + 1] * (i + 1) % MOD\n\n    def extend(self, n):\n        le = len(self.fact)\n\
    \        if n < le:\n            return\n        self.fact.extend([1] * (n - le\
    \ + 1))\n        self.invfact.extend([1] * (n - le + 1))\n        for i in range(le,\
    \ n + 1):\n            self.fact[i] = self.fact[i - 1] * i % self.MOD\n\n    \
    \    self.invfact[n] = pow(self.fact[n], self.MOD - 2, self.MOD)\n        for\
    \ i in range(n - 1, le - 1, -1):\n            self.invfact[i] = self.invfact[i\
    \ + 1] * (i + 1) % self.MOD\n\n    def nPk(self, n, k):\n        if k < 0 or n\
    \ < k:\n            return 0\n        if n >= len(self.fact):\n            self.extend(n)\n\
    \        return self.fact[n] * self.invfact[n - k] % self.MOD\n\n    def nCk(self,\
    \ n, k):\n        if k < 0 or n < k:\n            return 0\n        if n >= len(self.fact):\n\
    \            self.extend(n)\n        return (self.fact[n] * self.invfact[n - k]\
    \ % self.MOD) * self.invfact[k] % self.MOD\n\n    def nHk(self, n, k):\n     \
    \   if n == 0 and k == 0:\n            return 1\n        return self.nCk(n + k\
    \ - 1, k)\n\n    def Catalan(self, n):\n        return (self.nCk(2 * n, n) - self.nCk(2\
    \ * n, n - 1)) % self.MOD\n"
  dependsOn: []
  isVerificationFile: false
  path: src/math/Combination.py
  requiredBy:
  - src/polynomial/FormalPowerSeries998.py
  timestamp: '2023-06-29 01:22:58+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/math/Combination.test.py
  - src/$tests/math/Catalan.test.py
documentation_of: src/math/Combination.py
layout: document
redirect_from:
- /library/src/math/Combination.py
- /library/src/math/Combination.py.html
title: src/math/Combination.py
---
