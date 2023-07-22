# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inv_of_formal_power_series
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


class NTT998:
    # fmt: off
    rate2=(0, 911660635, 509520358, 369330050, 332049552, 983190778, 123842337, 238493703, 975955924, 603855026, 856644456, 131300601, 842657263, 730768835, 942482514, 806263778, 151565301, 510815449, 503497456, 743006876, 741047443, 56250497, 867605899, 0)
    irate2=(0, 86583718, 372528824, 373294451, 645684063, 112220581, 692852209, 155456985, 797128860, 90816748, 860285882, 927414960, 354738543, 109331171, 293255632, 535113200, 308540755, 121186627, 608385704, 438932459, 359477183, 824071951, 103369235, 0)
    rate3=(0, 372528824, 337190230, 454590761, 816400692, 578227951, 180142363, 83780245, 6597683, 70046822, 623238099, 183021267, 402682409, 631680428, 344509872, 689220186, 365017329, 774342554, 729444058, 102986190, 128751033, 395565204, 0)
    irate3=(0, 509520358, 929031873, 170256584, 839780419, 282974284, 395914482, 444904435, 72135471, 638914820, 66769500, 771127074, 985925487, 262319669, 262341272, 625870173, 768022760, 859816005, 914661783, 430819711, 272774365, 530924681, 0)
    # fmt: on

    def butterfly(A):
        n = len(A)
        h = (n - 1).bit_length()
        le = 0
        while le < h:
            if h - le == 1:
                p = 1 << (h - le - 1)
                rot = 1
                for s in range(1 << le):
                    offset = s << (h - le)
                    for i in range(p):
                        l = A[i + offset]
                        r = A[i + offset + p] * rot
                        A[i + offset] = (l + r) % 998244353
                        A[i + offset + p] = (l - r) % 998244353
                    rot *= NTT998.rate2[(~s & -~s).bit_length()]
                    rot %= 998244353
                le += 1
            else:
                p = 1 << (h - le - 2)
                rot = 1
                for s in range(1 << le):
                    rot2 = rot * rot % 998244353
                    rot3 = rot2 * rot % 998244353
                    offset = s << (h - le)
                    for i in range(p):
                        a0 = A[i + offset]
                        a1 = A[i + offset + p] * rot
                        a2 = A[i + offset + p * 2] * rot2
                        a3 = A[i + offset + p * 3] * rot3
                        a1na3imag = (a1 - a3) % 998244353 * 911660635
                        A[i + offset] = (a0 + a2 + a1 + a3) % 998244353
                        A[i + offset + p] = (a0 + a2 - a1 - a3) % 998244353
                        A[i + offset + p * 2] = (a0 - a2 + a1na3imag) % 998244353
                        A[i + offset + p * 3] = (a0 - a2 - a1na3imag) % 998244353
                    rot *= NTT998.rate3[(~s & -~s).bit_length()]
                    rot %= 998244353
                le += 2

    def butterfly_inv(A):
        n = len(A)
        h = (n - 1).bit_length()
        le = h
        while le:
            if le == 1:
                p = 1 << (h - le)
                irot = 1
                for s in range(1 << (le - 1)):
                    offset = s << (h - le + 1)
                    for i in range(p):
                        l = A[i + offset]
                        r = A[i + offset + p]
                        A[i + offset] = (l + r) % 998244353
                        A[i + offset + p] = (l - r) * irot % 998244353
                    irot *= NTT998.irate2[(~s & -~s).bit_length()]
                    irot %= 998244353
                le -= 1
            else:
                p = 1 << (h - le)
                irot = 1
                for s in range(1 << (le - 2)):
                    irot2 = irot * irot % 998244353
                    irot3 = irot2 * irot % 998244353
                    offset = s << (h - le + 2)
                    for i in range(p):
                        a0 = A[i + offset]
                        a1 = A[i + offset + p]
                        a2 = A[i + offset + p * 2]
                        a3 = A[i + offset + p * 3]
                        a2na3iimag = (a2 - a3) * 86583718 % 998244353
                        A[i + offset] = (a0 + a1 + a2 + a3) % 998244353
                        A[i + offset + p] = (a0 - a1 + a2na3iimag) * irot % 998244353
                        A[i + offset + p * 2] = (a0 + a1 - a2 - a3) * irot2 % 998244353
                        A[i + offset + p * 3] = (a0 - a1 - a2na3iimag) * irot3 % 998244353
                    irot *= NTT998.irate3[(~s & -~s).bit_length()]
                    irot %= 998244353
                le -= 2

    def multiply(A, B):
        n = len(A)
        m = len(B)
        if min(n, m) <= 60:
            C = [0] * (n + m - 1)
            for i in range(n):
                if i % 8 == 0:
                    for j in range(m):
                        C[i + j] += A[i] * B[j]
                        C[i + j] %= 998244353
                else:
                    for j in range(m):
                        C[i + j] += A[i] * B[j]
            return [c % 998244353 for c in C]
        A = A[:]
        B = B[:]
        z = 1 << (n + m - 2).bit_length()
        A += [0] * (z - n)
        B += [0] * (z - m)
        NTT998.butterfly(A)
        NTT998.butterfly(B)
        for i in range(z):
            A[i] *= B[i]
            A[i] %= 998244353
        NTT998.butterfly_inv(A)
        A = A[: n + m - 1]
        iz = pow(z, 998244353 - 2, 998244353)
        return [a * iz % 998244353 for a in A]


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


class Combination:
    def __init__(self, n, MOD=998244353):
        self.fact = [1] * (n + 1)
        self.invfact = [1] * (n + 1)
        self.MOD = MOD
        for i in range(1, n + 1):
            self.fact[i] = self.fact[i - 1] * i % MOD

        self.invfact[n] = pow(self.fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            self.invfact[i] = self.invfact[i + 1] * (i + 1) % MOD

    def extend(self, n):
        le = len(self.fact)
        if n < le:
            return
        self.fact.extend([1] * (n - le + 1))
        self.invfact.extend([1] * (n - le + 1))
        for i in range(le, n + 1):
            self.fact[i] = self.fact[i - 1] * i % self.MOD

        self.invfact[n] = pow(self.fact[n], self.MOD - 2, self.MOD)
        for i in range(n - 1, le - 1, -1):
            self.invfact[i] = self.invfact[i + 1] * (i + 1) % self.MOD

    def nPk(self, n, k):
        if k < 0 or n < k:
            return 0
        if n >= len(self.fact):
            self.extend(n)
        return self.fact[n] * self.invfact[n - k] % self.MOD

    def nCk(self, n, k):
        if k < 0 or n < k:
            return 0
        if n >= len(self.fact):
            self.extend(n)
        return (self.fact[n] * self.invfact[n - k] % self.MOD) * self.invfact[k] % self.MOD

    def nHk(self, n, k):
        if n == 0 and k == 0:
            return 1
        return self.nCk(n + k - 1, k)

    def Catalan(self, n):
        return (self.nCk(2 * n, n) - self.nCk(2 * n, n - 1)) % self.MOD


def cipolla(x, MOD):
    if MOD == 2:
        return x
    elif x == 0:
        return 0
    elif pow(x, (MOD - 1) // 2, MOD) != 1:
        return -1

    y = 1
    while pow((y * y - x) % MOD, (MOD - 1) // 2, MOD) == 1:
        y += 1

    base = (y * y - x) % MOD

    def multi(a0, b0, a1, b1):
        return (a0 * a1 + base * (b0 * b1 % MOD)) % MOD, (a0 * b1 + a1 * b0) % MOD

    def pow_(a, b, n):
        if n == 0:
            return 1, 0

        tmp = multi(a, b, a, b)
        ret = pow_(tmp[0], tmp[1], n >> 1)
        if n & 1:
            ret = multi(ret[0], ret[1], a, b)

        return ret

    return pow_(y, 1, (MOD + 1) // 2)[0]


class FormalPowerSeries998(list):
    Comb = Combination(200000)

    def __init__(self, n):
        if type(n) == int:
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
        if type(other) == int:
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


FPS = FormalPowerSeries998
n = int(input())
F = FPS(map(int, input().split()))
print(*F.inv())
