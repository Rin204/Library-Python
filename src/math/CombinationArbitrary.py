from src.math.modinv import modinv
from src.math.PollardRho import primedict
from src.math.Garner import Garner


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
