# verification-helper: PROBLEM https://judge.yosupo.jp/problem/binomial_coefficient
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


def modinv(a, MOD):
    b = MOD
    u = 1
    v = 0
    while b > 0:
        t = a // b
        a -= t * b
        u -= t * v
        a, b = b, a
        u, v = v, u

    if a != 1:
        return -1

    if u != 0:
        u += MOD

    return u


from math import gcd


def MillerRabin(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    if n < 4759123141:
        A = [2, 7, 61]
    else:
        A = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d >>= 1

    for a in A:
        if a % n == 0:
            return True
        x = pow(a, d, n)
        if x != 1:
            for t in range(s):
                if x == n - 1:
                    break
                x = x * x % n
            else:
                return False
    return True


def pollard(n):
    # https://qiita.com/t_fuki/items/7cd50de54d3c5d063b4a

    if n % 2 == 0:
        return 2

    m = int(n**0.125) + 1
    step = 0

    while 1:
        step += 1

        def f(x):
            return (x * x + step) % n

        y = k = 0
        g = q = r = 1

        while g == 1:
            x = y
            while k < 3 * r // 4:
                y = f(y)
                k += 1
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            k = r
            r <<= 1

        if g == n:
            g = 1
            y = ys
            while g == 1:
                y = f(y)
                g = gcd(abs(x - y), n)

        if g == n:
            continue
        if MillerRabin(g):
            return g
        elif MillerRabin(n // g):
            return n // g
        else:
            return pollard(g)


def primefact(n):
    res = []
    while n > 1 and not MillerRabin(n):
        p = pollard(n)
        while n % p == 0:
            res.append(p)
            n //= p
    if n != 1:
        res.append(n)
    return sorted(res)


def primedict(n):
    P = primefact(n)
    ret = {}
    for p in P:
        ret[p] = ret.get(p, 0) + 1
    return ret


def ext_gcd(a, b):
    """
    return (x, y, gcd(a, b)) s.t. ax + by = gcd(a, b)
    """
    if b == 0:
        return 1, 0, a
    else:
        y, x, g = ext_gcd(b, a % b)
        return x, y - (a // b) * x, g


def Garner(R, M):
    r = 0
    m = 1
    for ri, mi in zip(R, M):
        if ri < 0 or mi <= ri:
            ri %= mi

        if m < mi:
            m, mi = mi, m
            r, ri = ri, r

        if m % mi == 0:
            if r % mi != ri:
                return -1, -1
            continue

        im, _, g = ext_gcd(m, mi)
        if im < 0:
            im += mi

        if (ri - r) % g != 0:
            return -1, -1

        ui = mi // g
        x = ((ri - r) // g % ui) * im % ui
        r += x * m
        m *= ui

    return r, m


class CombinationPrimePowerMOD:
    def __init__(self, p, e, m=-1):
        self.p = p
        self.e = e
        self.m = p**e

        self.le = self.m
        if m != -1:
            self.le = min(m, self.le)

        self.fact = [0] * (self.le + 1)
        self.invfact = [0] * (self.le + 1)
        self.fact[0] = 1
        self.invfact[0] = 1
        for i in range(1, self.le + 1):
            if i % p == 0:
                self.fact[i] = self.fact[i - 1]
            else:
                self.fact[i] = self.fact[i - 1] * i % self.m
            self.invfact[i] = modinv(self.fact[i], self.m)

    def nCk(self, n, k):
        if n < 0 or n < k or k < 0:
            return 0

        ret = 1
        r = n - k
        e0 = 0
        eq = 0
        i = 0
        while n > 0:
            ret = ret * self.fact[n % self.m] % self.m
            ret = ret * self.invfact[k % self.m] % self.m
            ret = ret * self.invfact[r % self.m] % self.m
            n //= self.p
            k //= self.p
            r //= self.p
            e0 += n - k - r
            if e0 >= self.e:
                return 0
            i += 1
            if i >= self.e:
                eq += n - k - r

        if not (self.p == 2 and self.e >= 3) and (eq & 1):
            ret = ret * (self.m - 1) % self.m
        times = self.p
        while e0 > 0:
            if e0 & 1:
                ret = ret * times % self.m
            times = times * times % self.m
            e0 >>= 1

        return ret


class CombinationArbitrary:
    def __init__(self, MOD, le=-1):
        self.MOD = MOD
        self.M = []
        self.prime_nCk = []
        primes = primedict(MOD)
        for k, v in primes.items():
            self.M.append(k**v)
            self.prime_nCk.append(CombinationPrimePowerMOD(k, v, le))

    def nCk(self, n, k):
        if n < 0 or n < k or k < 0:
            return 0

        if self.MOD == 1:
            return 0

        R = [pr.nCk(n, k) for pr in self.prime_nCk]
        return Garner(R, self.M)[0]


T, MOD = map(int, input().split())
Comb = CombinationArbitrary(MOD)
for _ in range(T):
    n, k = map(int, input().split())
    print(Comb.nCk(n, k))
