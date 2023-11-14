from src.convolution.NTT998 import NTT998
from src.math.modinv import modinv
from src.math.Combination import Combination
from src.math.cipolla import cipolla


class FormalPowerSeries998(list):
    Comb = Combination(200000)

    def __init__(self, n):
        if isinstance(n, int):
            super().__init__([0] * n)
        else:
            super().__init__(n)

    def __getitem__(self, i):
        if isinstance(i, slice):
            return FormalPowerSeries998(super().__getitem__(i))
        return super().__getitem__(i)

    def resize(self, n):
        if n > len(self):
            self.extend([0] * (n - len(self)))
        else:
            del self[n:]

    def __add__(self, other):
        if len(self) > len(other):
            res = self[:]
            for i, x in enumerate(other):
                res[i] += x
                if res[i] >= 998244353:
                    res[i] -= 998244353
        else:
            res = other[:]
            for i, x in enumerate(self):
                res[i] += x
                if res[i] >= 998244353:
                    res[i] -= 998244353
        return res

    def __iadd__(self, other):
        if len(self) < len(other):
            super().__iadd__([0] * (len(other) - len(self)))
        for i, x in enumerate(other):
            self[i] += x
            if self[i] >= 998244353:
                self[i] -= 998244353
        return self

    def __sub__(self, other):
        res = self[:]
        if len(res) < len(other):
            super(FormalPowerSeries998, res).__iadd__([0] * (len(other) - len(res)))
        for i, x in enumerate(other):
            res[i] -= x
            if res[i] < 0:
                res[i] += 998244353
        return FormalPowerSeries998(res)

    def __isub__(self, other):
        if len(self) < len(other):
            super().__iadd__([0] * (len(other) - len(self)))
        for i, x in enumerate(other):
            self[i] -= x
            if self[i] < 0:
                self[i] += 998244353
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            return FormalPowerSeries998([x * other % 998244353 for x in self])
        return FormalPowerSeries998(NTT998.multiply(list(self), list(other)))

    def __imul__(self, other):
        return self.__mul__(other)

    def inv(self, deg=None):
        if deg is None:
            deg = len(self)
        if deg == 0:
            return FormalPowerSeries998([])
        g = FormalPowerSeries998([modinv(self[0], 998244353)])
        l = 1
        while l < deg:
            l *= 2
            g = g * 2 - (g * g * self[:l])
            del g[l:]
        return g[:deg]

    def __floordiv__(self, other):
        return self * other.inv(len(self))

    def differential(self):
        return FormalPowerSeries998([i * x % 998244353 for i, x in enumerate(self[1:], 1)])

    def integral(self):
        FormalPowerSeries998.Comb.extend(len(self) + 1)
        return FormalPowerSeries998(
            [0]
            + [
                (
                    FormalPowerSeries998.Comb.fact[i]
                    * FormalPowerSeries998.Comb.invfact[i + 1]
                    % 998244353
                )
                * x
                % 998244353
                for i, x in enumerate(self)
            ]
        )

    def log(self, deg=None):
        if deg is None:
            deg = len(self)
        return (self.differential() * self.inv(deg))[:deg].integral()[:deg]

    def exp(self, deg=None):
        if deg is None:
            deg = len(self)
        g = FormalPowerSeries998([1])
        l = 1
        while l < deg:
            l *= 2
            g *= (FormalPowerSeries998([1]) - g.log(deg=l) + self[:l])[:l]
            del g[l:]
        return g[:deg]

    def pow(self, k, deg=None):
        if deg is None:
            deg = len(self)

        if k == 0:
            res = FormalPowerSeries998(deg)
            res[0] = 1
            return res

        p = -1
        for i in range(deg):
            if self[i] != 0:
                p = i
                break

        if p == -1 or p > deg // k:
            return FormalPowerSeries998(deg)

        inv = modinv(self[p], 998244353)
        A = self[p:] * inv
        A = A.log(deg)
        A *= k % 998244353
        A = A.exp(deg)
        B = FormalPowerSeries998(p * k)
        super(FormalPowerSeries998, B).__iadd__(A[: deg - p * k])
        times = 1
        pp = self[p]
        while k > 0:
            if k & 1:
                times = times * pp % 998244353
            pp = pp * pp % 998244353
            k >>= 1

        B *= times
        return B

    def __pow__(self, k):
        return self.pow(k)

    def __ipow__(self, k):
        return self.pow(k)

    def sqrt(self, deg=None):
        if deg is None:
            deg = len(self)
        if len(self) == 0:
            return FormalPowerSeries998(deg)
        if self[0] == 0:
            for i in range(1, deg):
                if self[i] != 0:
                    if i % 2 == 1:
                        return FormalPowerSeries998([])
                    if deg <= i // 2:
                        break
                    ret = self[i:].sqrt(deg - i // 2)
                    if len(ret) == 0:
                        return FormalPowerSeries998([])
                    ret = FormalPowerSeries998([0] * (i // 2) + list(ret))
                    if len(ret) < deg:
                        ret.resize(deg)
                    return ret
            else:
                return FormalPowerSeries998(deg)

        sq = cipolla(self[0], 998244353)
        if sq == -1:
            return FormalPowerSeries998([])

        inv2 = 499122177
        g = FormalPowerSeries998([sq])
        l = 1
        while l < deg:
            l *= 2
            g = (g + self[:l] * g.inv(l)) * inv2
            del g[l:]

        return g[:deg]
