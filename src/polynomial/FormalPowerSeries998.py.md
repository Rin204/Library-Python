---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/convolution/NTT998.py
    title: src/convolution/NTT998.py
  - icon: ':x:'
    path: src/math/Combination.py
    title: src/math/Combination.py
  - icon: ':x:'
    path: src/math/cipolla.py
    title: src/math/cipolla.py
  - icon: ':warning:'
    path: src/math/modinv.py
    title: src/math/modinv.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/polynomial/inv_of_FormalPowerSeries.test.py
    title: src/$tests/polynomial/inv_of_FormalPowerSeries.test.py
  - icon: ':x:'
    path: src/$tests/polynomial/log_of_FormalPowerSeries.test.py
    title: src/$tests/polynomial/log_of_FormalPowerSeries.test.py
  - icon: ':x:'
    path: src/$tests/polynomial/pow_of_FormalPowerSeries.test.py
    title: src/$tests/polynomial/pow_of_FormalPowerSeries.test.py
  - icon: ':x:'
    path: src/$tests/polynomial/sqrt_of_FormalPowerSeries.test.py
    title: src/$tests/polynomial/sqrt_of_FormalPowerSeries.test.py
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
  code: "from src.convolution.NTT998 import NTT998\nfrom src.math.modinv import modinv\n\
    from src.math.Combination import Combination\nfrom src.math.cipolla import cipolla\n\
    \n\nclass FormalPowerSeries998(list):\n    Comb = Combination(200000)\n\n    def\
    \ __init__(self, n):\n        if type(n) == int:\n            super().__init__([0]\
    \ * n)\n        else:\n            super().__init__(n)\n\n    def __getitem__(self,\
    \ i):\n        if isinstance(i, slice):\n            return FormalPowerSeries998(super().__getitem__(i))\n\
    \        return super().__getitem__(i)\n\n    def resize(self, n):\n        if\
    \ n > len(self):\n            self.extend([0] * (n - len(self)))\n        else:\n\
    \            del self[n:]\n\n    def __add__(self, other):\n        if len(self)\
    \ > len(other):\n            res = self[:]\n            for i, x in enumerate(other):\n\
    \                res[i] += x\n                if res[i] >= 998244353:\n      \
    \              res[i] -= 998244353\n        else:\n            res = other[:]\n\
    \            for i, x in enumerate(self):\n                res[i] += x\n     \
    \           if res[i] >= 998244353:\n                    res[i] -= 998244353\n\
    \        return res\n\n    def __iadd__(self, other):\n        if len(self) <\
    \ len(other):\n            super().__iadd__([0] * (len(other) - len(self)))\n\
    \        for i, x in enumerate(other):\n            self[i] += x\n           \
    \ if self[i] >= 998244353:\n                self[i] -= 998244353\n        return\
    \ self\n\n    def __sub__(self, other):\n        res = self[:]\n        if len(res)\
    \ < len(other):\n            super(FormalPowerSeries998, res).__iadd__([0] * (len(other)\
    \ - len(res)))\n        for i, x in enumerate(other):\n            res[i] -= x\n\
    \            if res[i] < 0:\n                res[i] += 998244353\n        return\
    \ FormalPowerSeries998(res)\n\n    def __isub__(self, other):\n        if len(self)\
    \ < len(other):\n            super().__iadd__([0] * (len(other) - len(self)))\n\
    \        for i, x in enumerate(other):\n            self[i] -= x\n           \
    \ if self[i] < 0:\n                self[i] += 998244353\n        return self\n\
    \n    def __mul__(self, other):\n        if type(other) == int:\n            return\
    \ FormalPowerSeries998([x * other % 998244353 for x in self])\n        return\
    \ FormalPowerSeries998(NTT998.multiply(list(self), list(other)))\n\n    def __imul__(self,\
    \ other):\n        return self.__mul__(other)\n\n    def inv(self, deg=None):\n\
    \        if deg is None:\n            deg = len(self)\n        if deg == 0:\n\
    \            return FormalPowerSeries998([])\n        g = FormalPowerSeries998([modinv(self[0],\
    \ 998244353)])\n        l = 1\n        while l < deg:\n            l *= 2\n  \
    \          g = g * 2 - (g * g * self[:l])\n            del g[l:]\n        return\
    \ g[:deg]\n\n    def __floordiv__(self, other):\n        return self * other.inv(len(self))\n\
    \n    def differential(self):\n        return FormalPowerSeries998([i * x % 998244353\
    \ for i, x in enumerate(self[1:], 1)])\n\n    def integral(self):\n        FormalPowerSeries998.Comb.extend(len(self)\
    \ + 1)\n        return FormalPowerSeries998(\n            [0]\n            + [\n\
    \                (\n                    FormalPowerSeries998.Comb.fact[i]\n  \
    \                  * FormalPowerSeries998.Comb.invfact[i + 1]\n              \
    \      % 998244353\n                )\n                * x\n                %\
    \ 998244353\n                for i, x in enumerate(self)\n            ]\n    \
    \    )\n\n    def log(self, deg=None):\n        if deg is None:\n            deg\
    \ = len(self)\n        return (self.differential() * self.inv(deg))[:deg].integral()[:deg]\n\
    \n    def exp(self, deg=None):\n        if deg is None:\n            deg = len(self)\n\
    \        g = FormalPowerSeries998([1])\n        l = 1\n        while l < deg:\n\
    \            l *= 2\n            g *= (FormalPowerSeries998([1]) - g.log(deg=l)\
    \ + self[:l])[:l]\n            del g[l:]\n        return g[:deg]\n\n    def pow(self,\
    \ k, deg=None):\n        if deg is None:\n            deg = len(self)\n\n    \
    \    if k == 0:\n            res = FormalPowerSeries998(deg)\n            res[0]\
    \ = 1\n            return res\n\n        p = -1\n        for i in range(deg):\n\
    \            if self[i] != 0:\n                p = i\n                break\n\n\
    \        if p == -1 or p > deg // k:\n            return FormalPowerSeries998(deg)\n\
    \n        inv = modinv(self[p], 998244353)\n        A = self[p:] * inv\n     \
    \   A = A.log(deg)\n        A *= k % 998244353\n        A = A.exp(deg)\n     \
    \   B = FormalPowerSeries998(p * k)\n        super(FormalPowerSeries998, B).__iadd__(A[:\
    \ deg - p * k])\n        times = 1\n        pp = self[p]\n        while k > 0:\n\
    \            if k & 1:\n                times = times * pp % 998244353\n     \
    \       pp = pp * pp % 998244353\n            k >>= 1\n\n        B *= times\n\
    \        return B\n\n    def __pow__(self, k):\n        return self.pow(k)\n\n\
    \    def __ipow__(self, k):\n        return self.pow(k)\n\n    def sqrt(self,\
    \ deg=None):\n        if deg is None:\n            deg = len(self)\n        if\
    \ len(self) == 0:\n            return FormalPowerSeries998(deg)\n        if self[0]\
    \ == 0:\n            for i in range(1, deg):\n                if self[i] != 0:\n\
    \                    if i % 2 == 1:\n                        return FormalPowerSeries998([])\n\
    \                    if deg <= i // 2:\n                        break\n      \
    \              ret = self[i:].sqrt(deg - i // 2)\n                    if len(ret)\
    \ == 0:\n                        return FormalPowerSeries998([])\n           \
    \         ret = FormalPowerSeries998([0] * (i // 2) + list(ret))\n           \
    \         if len(ret) < deg:\n                        ret.resize(deg)\n      \
    \              return ret\n            else:\n                return FormalPowerSeries998(deg)\n\
    \n        sq = cipolla(self[0], 998244353)\n        if sq == -1:\n           \
    \ return FormalPowerSeries998([])\n\n        inv2 = 499122177\n        g = FormalPowerSeries998([sq])\n\
    \        l = 1\n        while l < deg:\n            l *= 2\n            g = (g\
    \ + self[:l] * g.inv(l)) * inv2\n            del g[l:]\n\n        return g[:deg]\n"
  dependsOn:
  - src/convolution/NTT998.py
  - src/math/cipolla.py
  - src/math/modinv.py
  - src/math/Combination.py
  isVerificationFile: false
  path: src/polynomial/FormalPowerSeries998.py
  requiredBy: []
  timestamp: '2023-07-23 02:22:37+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/polynomial/inv_of_FormalPowerSeries.test.py
  - src/$tests/polynomial/pow_of_FormalPowerSeries.test.py
  - src/$tests/polynomial/sqrt_of_FormalPowerSeries.test.py
  - src/$tests/polynomial/log_of_FormalPowerSeries.test.py
documentation_of: src/polynomial/FormalPowerSeries998.py
layout: document
redirect_from:
- /library/src/polynomial/FormalPowerSeries998.py
- /library/src/polynomial/FormalPowerSeries998.py.html
title: src/polynomial/FormalPowerSeries998.py
---
