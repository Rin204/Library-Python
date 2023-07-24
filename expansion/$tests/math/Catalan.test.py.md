---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/790
    links:
    - https://yukicoder.me/problems/no/790
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/790\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\nclass Combination:\n    def __init__(self, n, MOD=998244353):\n        self.fact\
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
    \ * n, n - 1)) % self.MOD\n\n\nn = int(input())\nC = Combination(n)\nprint(C.Catalan(n))\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/math/Catalan.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/math/Catalan.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/math/Catalan.test.py
- /verify/expansion/$tests/math/Catalan.test.py.html
title: expansion/$tests/math/Catalan.test.py
---