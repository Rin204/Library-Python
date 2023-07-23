---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/binomial_coefficient
    links:
    - https://judge.yosupo.jp/problem/binomial_coefficient
    - https://qiita.com/t_fuki/items/7cd50de54d3c5d063b4a
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/binomial_coefficient\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\ndef modinv(a, MOD):\n    b = MOD\n    u = 1\n    v = 0\n    while b > 0:\n\
    \        t = a // b\n        a -= t * b\n        u -= t * v\n        a, b = b,\
    \ a\n        u, v = v, u\n\n    if a != 1:\n        return -1\n\n    if u != 0:\n\
    \        u += MOD\n\n    return u\n\n\nfrom math import gcd\n\n\ndef MillerRabin(n):\n\
    \    if n <= 1:\n        return False\n    elif n == 2:\n        return True\n\
    \    elif n % 2 == 0:\n        return False\n\n    if n < 4759123141:\n      \
    \  A = [2, 7, 61]\n    else:\n        A = [2, 325, 9375, 28178, 450775, 9780504,\
    \ 1795265022]\n    s = 0\n    d = n - 1\n    while d % 2 == 0:\n        s += 1\n\
    \        d >>= 1\n\n    for a in A:\n        if a % n == 0:\n            return\
    \ True\n        x = pow(a, d, n)\n        if x != 1:\n            for t in range(s):\n\
    \                if x == n - 1:\n                    break\n                x\
    \ = x * x % n\n            else:\n                return False\n    return True\n\
    \n\ndef pollard(n):\n    # https://qiita.com/t_fuki/items/7cd50de54d3c5d063b4a\n\
    \n    if n % 2 == 0:\n        return 2\n\n    m = int(n**0.125) + 1\n    step\
    \ = 0\n\n    while 1:\n        step += 1\n\n        def f(x):\n            return\
    \ (x * x + step) % n\n\n        y = k = 0\n        g = q = r = 1\n\n        while\
    \ g == 1:\n            x = y\n            while k < 3 * r // 4:\n            \
    \    y = f(y)\n                k += 1\n            while k < r and g == 1:\n \
    \               ys = y\n                for _ in range(min(m, r - k)):\n     \
    \               y = f(y)\n                    q = q * abs(x - y) % n\n       \
    \         g = gcd(q, n)\n                k += m\n            k = r\n         \
    \   r <<= 1\n\n        if g == n:\n            g = 1\n            y = ys\n   \
    \         while g == 1:\n                y = f(y)\n                g = gcd(abs(x\
    \ - y), n)\n\n        if g == n:\n            continue\n        if MillerRabin(g):\n\
    \            return g\n        elif MillerRabin(n // g):\n            return n\
    \ // g\n        else:\n            return pollard(g)\n\n\ndef primefact(n):\n\
    \    res = []\n    while n > 1 and not MillerRabin(n):\n        p = pollard(n)\n\
    \        while n % p == 0:\n            res.append(p)\n            n //= p\n \
    \   if n != 1:\n        res.append(n)\n    return sorted(res)\n\n\ndef primedict(n):\n\
    \    P = primefact(n)\n    ret = {}\n    for p in P:\n        ret[p] = ret.get(p,\
    \ 0) + 1\n    return ret\n\n\ndef ext_gcd(a, b):\n    \"\"\"\n    return (x, y,\
    \ gcd(a, b)) s.t. ax + by = gcd(a, b)\n    \"\"\"\n    if b == 0:\n        return\
    \ 1, 0, a\n    else:\n        y, x, g = ext_gcd(b, a % b)\n        return x, y\
    \ - (a // b) * x, g\n\n\ndef Garner(R, M):\n    r = 0\n    m = 1\n    for ri,\
    \ mi in zip(R, M):\n        if ri < 0 or mi <= ri:\n            ri %= mi\n\n \
    \       if m < mi:\n            m, mi = mi, m\n            r, ri = ri, r\n\n \
    \       if m % mi == 0:\n            if r % mi != ri:\n                return\
    \ -1, -1\n            continue\n\n        im, _, g = ext_gcd(m, mi)\n        if\
    \ im < 0:\n            im += mi\n\n        if (ri - r) % g != 0:\n           \
    \ return -1, -1\n\n        ui = mi // g\n        x = ((ri - r) // g % ui) * im\
    \ % ui\n        r += x * m\n        m *= ui\n\n    return r, m\n\n\nclass CombinationPrimePowerMOD:\n\
    \    def __init__(self, p, e, m=-1):\n        self.p = p\n        self.e = e\n\
    \        self.m = p**e\n\n        self.le = self.m\n        if m != -1:\n    \
    \        self.le = min(m, self.le)\n\n        self.fact = [0] * (self.le + 1)\n\
    \        self.invfact = [0] * (self.le + 1)\n        self.fact[0] = 1\n      \
    \  self.invfact[0] = 1\n        for i in range(1, self.le + 1):\n            if\
    \ i % p == 0:\n                self.fact[i] = self.fact[i - 1]\n            else:\n\
    \                self.fact[i] = self.fact[i - 1] * i % self.m\n            self.invfact[i]\
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
    \      R = [pr.nCk(n, k) for pr in self.prime_nCk]\n        return Garner(R, self.M)[0]\n\
    \n\nT, MOD = map(int, input().split())\nComb = CombinationArbitrary(MOD)\nfor\
    \ _ in range(T):\n    n, k = map(int, input().split())\n    print(Comb.nCk(n,\
    \ k))\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/math/Combination_Arbitrary.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/math/Combination_Arbitrary.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/math/Combination_Arbitrary.test.py
- /verify/expansion/$tests/math/Combination_Arbitrary.test.py.html
title: expansion/$tests/math/Combination_Arbitrary.test.py
---
