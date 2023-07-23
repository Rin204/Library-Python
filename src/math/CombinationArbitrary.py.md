---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/math/Garner.py
    title: src/math/Garner.py
  - icon: ':x:'
    path: src/math/PollardRho.py
    title: src/math/PollardRho.py
  - icon: ':warning:'
    path: src/math/modinv.py
    title: src/math/modinv.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/math/Combination_Arbitrary.test.py
    title: src/$tests/math/Combination_Arbitrary.test.py
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
  code: "from src.math.modinv import modinv\nfrom src.math.PollardRho import primedict\n\
    from src.math.Garner import Garner\n\n\nclass CombinationPrimePowerMOD:\n    def\
    \ __init__(self, p, e, m=-1):\n        self.p = p\n        self.e = e\n      \
    \  self.m = p**e\n\n        self.le = self.m\n        if m != -1:\n          \
    \  self.le = min(m, self.le)\n\n        self.fact = [0] * (self.le + 1)\n    \
    \    self.invfact = [0] * (self.le + 1)\n        self.fact[0] = 1\n        self.invfact[0]\
    \ = 1\n        for i in range(1, self.le + 1):\n            if i % p == 0:\n \
    \               self.fact[i] = self.fact[i - 1]\n            else:\n         \
    \       self.fact[i] = self.fact[i - 1] * i % self.m\n            self.invfact[i]\
    \ = modinv(self.fact[i], self.m)\n\n    def nCk(self, n, k):\n        if n < 0\
    \ or n < k or k < 0:\n            return 0\n\n        ret = 1\n        r = n -\
    \ k\n        e0 = 0\n        eq = 0\n        i = 0\n        while n > 0:\n   \
    \         ret = ret * self.fact[n % self.m] % self.m\n            ret = ret *\
    \ self.invfact[k % self.m] % self.m\n            ret = ret * self.invfact[r %\
    \ self.m] % self.m\n            n //= self.p\n            k //= self.p\n     \
    \       r //= self.p\n            e0 += n - k - r\n            if e0 >= self.e:\n\
    \                return 0\n            i += 1\n            if i >= self.e:\n \
    \               eq += n - k - r\n\n        if not (self.p == 2 and self.e >= 3)\
    \ and (eq & 1):\n            ret = ret * (self.m - 1) % self.m\n        times\
    \ = self.p\n        while e0 > 0:\n            if e0 & 1:\n                ret\
    \ = ret * times % self.m\n            times = times * times % self.m\n       \
    \     e0 >>= 1\n\n        return ret\n\n\nclass CombinationArbitrary:\n    def\
    \ __init__(self, MOD, le=-1):\n        self.MOD = MOD\n        self.M = []\n \
    \       self.prime_nCk = []\n        primes = primedict(MOD)\n        for k, v\
    \ in primes.items():\n            self.M.append(k**v)\n            self.prime_nCk.append(CombinationPrimePowerMOD(k,\
    \ v, le))\n\n    def nCk(self, n, k):\n        if n < 0 or n < k or k < 0:\n \
    \           return 0\n\n        if self.MOD == 1:\n            return 0\n\n  \
    \      R = [pr.nCk(n, k) for pr in self.prime_nCk]\n        return Garner(R, self.M)[0]\n"
  dependsOn:
  - src/math/modinv.py
  - src/math/Garner.py
  - src/math/PollardRho.py
  isVerificationFile: false
  path: src/math/CombinationArbitrary.py
  requiredBy: []
  timestamp: '2023-07-09 17:47:05+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/math/Combination_Arbitrary.test.py
documentation_of: src/math/CombinationArbitrary.py
layout: document
redirect_from:
- /library/src/math/CombinationArbitrary.py
- /library/src/math/CombinationArbitrary.py.html
title: src/math/CombinationArbitrary.py
---
