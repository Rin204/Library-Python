---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sqrt_of_formal_power_series
    links:
    - https://judge.yosupo.jp/problem/sqrt_of_formal_power_series
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sqrt_of_formal_power_series\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\nclass NTT998:\n    # fmt: off\n    rate2=(0, 911660635, 509520358, 369330050,\
    \ 332049552, 983190778, 123842337, 238493703, 975955924, 603855026, 856644456,\
    \ 131300601, 842657263, 730768835, 942482514, 806263778, 151565301, 510815449,\
    \ 503497456, 743006876, 741047443, 56250497, 867605899, 0)\n    irate2=(0, 86583718,\
    \ 372528824, 373294451, 645684063, 112220581, 692852209, 155456985, 797128860,\
    \ 90816748, 860285882, 927414960, 354738543, 109331171, 293255632, 535113200,\
    \ 308540755, 121186627, 608385704, 438932459, 359477183, 824071951, 103369235,\
    \ 0)\n    rate3=(0, 372528824, 337190230, 454590761, 816400692, 578227951, 180142363,\
    \ 83780245, 6597683, 70046822, 623238099, 183021267, 402682409, 631680428, 344509872,\
    \ 689220186, 365017329, 774342554, 729444058, 102986190, 128751033, 395565204,\
    \ 0)\n    irate3=(0, 509520358, 929031873, 170256584, 839780419, 282974284, 395914482,\
    \ 444904435, 72135471, 638914820, 66769500, 771127074, 985925487, 262319669, 262341272,\
    \ 625870173, 768022760, 859816005, 914661783, 430819711, 272774365, 530924681,\
    \ 0)\n    # fmt: on\n\n    def butterfly(A):\n        n = len(A)\n        h =\
    \ (n - 1).bit_length()\n        le = 0\n        while le < h:\n            if\
    \ h - le == 1:\n                p = 1 << (h - le - 1)\n                rot = 1\n\
    \                for s in range(1 << le):\n                    offset = s << (h\
    \ - le)\n                    for i in range(p):\n                        l = A[i\
    \ + offset]\n                        r = A[i + offset + p] * rot\n           \
    \             A[i + offset] = (l + r) % 998244353\n                        A[i\
    \ + offset + p] = (l - r) % 998244353\n                    rot *= NTT998.rate2[(~s\
    \ & -~s).bit_length()]\n                    rot %= 998244353\n               \
    \ le += 1\n            else:\n                p = 1 << (h - le - 2)\n        \
    \        rot = 1\n                for s in range(1 << le):\n                 \
    \   rot2 = rot * rot % 998244353\n                    rot3 = rot2 * rot % 998244353\n\
    \                    offset = s << (h - le)\n                    for i in range(p):\n\
    \                        a0 = A[i + offset]\n                        a1 = A[i\
    \ + offset + p] * rot\n                        a2 = A[i + offset + p * 2] * rot2\n\
    \                        a3 = A[i + offset + p * 3] * rot3\n                 \
    \       a1na3imag = (a1 - a3) % 998244353 * 911660635\n                      \
    \  A[i + offset] = (a0 + a2 + a1 + a3) % 998244353\n                        A[i\
    \ + offset + p] = (a0 + a2 - a1 - a3) % 998244353\n                        A[i\
    \ + offset + p * 2] = (a0 - a2 + a1na3imag) % 998244353\n                    \
    \    A[i + offset + p * 3] = (a0 - a2 - a1na3imag) % 998244353\n             \
    \       rot *= NTT998.rate3[(~s & -~s).bit_length()]\n                    rot\
    \ %= 998244353\n                le += 2\n\n    def butterfly_inv(A):\n       \
    \ n = len(A)\n        h = (n - 1).bit_length()\n        le = h\n        while\
    \ le:\n            if le == 1:\n                p = 1 << (h - le)\n          \
    \      irot = 1\n                for s in range(1 << (le - 1)):\n            \
    \        offset = s << (h - le + 1)\n                    for i in range(p):\n\
    \                        l = A[i + offset]\n                        r = A[i +\
    \ offset + p]\n                        A[i + offset] = (l + r) % 998244353\n \
    \                       A[i + offset + p] = (l - r) * irot % 998244353\n     \
    \               irot *= NTT998.irate2[(~s & -~s).bit_length()]\n             \
    \       irot %= 998244353\n                le -= 1\n            else:\n      \
    \          p = 1 << (h - le)\n                irot = 1\n                for s\
    \ in range(1 << (le - 2)):\n                    irot2 = irot * irot % 998244353\n\
    \                    irot3 = irot2 * irot % 998244353\n                    offset\
    \ = s << (h - le + 2)\n                    for i in range(p):\n              \
    \          a0 = A[i + offset]\n                        a1 = A[i + offset + p]\n\
    \                        a2 = A[i + offset + p * 2]\n                        a3\
    \ = A[i + offset + p * 3]\n                        a2na3iimag = (a2 - a3) * 86583718\
    \ % 998244353\n                        A[i + offset] = (a0 + a1 + a2 + a3) % 998244353\n\
    \                        A[i + offset + p] = (a0 - a1 + a2na3iimag) * irot % 998244353\n\
    \                        A[i + offset + p * 2] = (a0 + a1 - a2 - a3) * irot2 %\
    \ 998244353\n                        A[i + offset + p * 3] = (a0 - a1 - a2na3iimag)\
    \ * irot3 % 998244353\n                    irot *= NTT998.irate3[(~s & -~s).bit_length()]\n\
    \                    irot %= 998244353\n                le -= 2\n\n    def multiply(A,\
    \ B):\n        n = len(A)\n        m = len(B)\n        if min(n, m) <= 60:\n \
    \           C = [0] * (n + m - 1)\n            for i in range(n):\n          \
    \      if i % 8 == 0:\n                    for j in range(m):\n              \
    \          C[i + j] += A[i] * B[j]\n                        C[i + j] %= 998244353\n\
    \                else:\n                    for j in range(m):\n             \
    \           C[i + j] += A[i] * B[j]\n            return [c % 998244353 for c in\
    \ C]\n        A = A[:]\n        B = B[:]\n        z = 1 << (n + m - 2).bit_length()\n\
    \        A += [0] * (z - n)\n        B += [0] * (z - m)\n        NTT998.butterfly(A)\n\
    \        NTT998.butterfly(B)\n        for i in range(z):\n            A[i] *=\
    \ B[i]\n            A[i] %= 998244353\n        NTT998.butterfly_inv(A)\n     \
    \   A = A[: n + m - 1]\n        iz = pow(z, 998244353 - 2, 998244353)\n      \
    \  return [a * iz % 998244353 for a in A]\n\n\ndef modinv(a, MOD):\n    b = MOD\n\
    \    u = 1\n    v = 0\n    while b > 0:\n        t = a // b\n        a -= t *\
    \ b\n        u -= t * v\n        a, b = b, a\n        u, v = v, u\n\n    if a\
    \ != 1:\n        return -1\n\n    if u != 0:\n        u += MOD\n\n    return u\n\
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
    \ * n, n - 1)) % self.MOD\n\n\ndef cipolla(x, MOD):\n    if MOD == 2:\n      \
    \  return x\n    elif x == 0:\n        return 0\n    elif pow(x, (MOD - 1) //\
    \ 2, MOD) != 1:\n        return -1\n\n    y = 1\n    while pow((y * y - x) % MOD,\
    \ (MOD - 1) // 2, MOD) == 1:\n        y += 1\n\n    base = (y * y - x) % MOD\n\
    \n    def multi(a0, b0, a1, b1):\n        return (a0 * a1 + base * (b0 * b1 %\
    \ MOD)) % MOD, (a0 * b1 + a1 * b0) % MOD\n\n    def pow_(a, b, n):\n        if\
    \ n == 0:\n            return 1, 0\n\n        tmp = multi(a, b, a, b)\n      \
    \  ret = pow_(tmp[0], tmp[1], n >> 1)\n        if n & 1:\n            ret = multi(ret[0],\
    \ ret[1], a, b)\n\n        return ret\n\n    return pow_(y, 1, (MOD + 1) // 2)[0]\n\
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
    \ + self[:l] * g.inv(l)) * inv2\n            del g[l:]\n\n        return g[:deg]\n\
    \n\nFPS = FormalPowerSeries998\nn = int(input())\nF = FPS(map(int, input().split()))\n\
    F = F.sqrt()\nif F:\n    print(*F)\nelse:\n    print(-1)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/polynomial/sqrt_of_FormalPowerSeries.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/polynomial/sqrt_of_FormalPowerSeries.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/polynomial/sqrt_of_FormalPowerSeries.test.py
- /verify/expansion/$tests/polynomial/sqrt_of_FormalPowerSeries.test.py.html
title: expansion/$tests/polynomial/sqrt_of_FormalPowerSeries.test.py
---
