# verification-helper: PROBLEM https://yukicoder.me/problems/no/2231
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

import random


class RollingHash:
    mask30 = (1 << 30) - 1
    mask31 = (1 << 31) - 1
    MOD = (1 << 61) - 1
    Base = None
    pw = [1]

    def __init__(self, S):
        if RollingHash.Base is None:
            RollingHash.Base = random.randrange(129, 1 << 30)
        for i in range(len(RollingHash.pw), len(S) + 1):
            RollingHash.pw.append(
                RollingHash.CalcMod(RollingHash.Mul(RollingHash.pw[i - 1], self.__class__.Base))
            )

        self.hash = [0] * (len(S) + 1)
        for i, s in enumerate(S, 1):
            self.hash[i] = RollingHash.CalcMod(
                RollingHash.Mul(self.hash[i - 1], RollingHash.Base) + ord(s)
            )

    def get(self, l, r):
        return RollingHash.CalcMod(
            self.hash[r] - RollingHash.Mul(self.hash[l], RollingHash.pw[r - l])
        )

    def Mul(l, r):
        lu = l >> 31
        ld = l & RollingHash.mask31
        ru = r >> 31
        rd = r & RollingHash.mask31
        middlebit = ld * ru + lu * rd
        return (
            ((lu * ru) << 1)
            + ld * rd
            + ((middlebit & RollingHash.mask30) << 31)
            + (middlebit >> 30)
        )

    def CalcMod(val):
        if val < 0:
            val %= RollingHash.MOD
        val = (val & RollingHash.MOD) + (val >> 61)
        if val > RollingHash.MOD:
            val -= RollingHash.MOD
        return val


import random


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


def wildcard_matching(S, T, wild="?"):
    n = len(S)
    m = len(T)
    A = [0] * n
    B = [0] * m
    dic = {wild: 0}
    for i, s in enumerate(S):
        if s not in dic:
            dic[s] = random.randrange(998244353)
        A[i] = dic[s]
    for i, t in enumerate(T):
        if t not in dic:
            dic[t] = random.randrange(998244353)
        B[i] = dic[t]

    S1 = [0] * n
    S2 = [0] * n
    S3 = [0] * n
    for i, x in enumerate(A):
        y = int(x > 0)
        S1[i] = y
        S2[i] = y * x
        S3[i] = y * x * x % 998244353

    T1 = [0] * m
    T2 = [0] * m
    T3 = [0] * m
    for i, x in enumerate(B):
        y = int(x > 0)
        T1[m - 1 - i] = y
        T2[m - 1 - i] = y * x
        T3[m - 1 - i] = y * x * x % 998244353

    res1 = NTT998.multiply(S3, T1)
    res2 = NTT998.multiply(S2, T2)
    res3 = NTT998.multiply(S1, T3)
    res = []
    for i in range(n - m + 1):
        x = res1[i + m - 1] - 2 * res2[i + m - 1] + res3[i + m - 1]
        if x == 0:
            res.append(i)

    return res


def solve():
    n, m = map(int, input().split())
    S = list(input())
    T = list(input())
    res = wildcard_matching(S, T)
    if not res:
        print(-1)
        return

    for i in range(n):
        if S[i] == "?":
            S[i] = "a"

    rhs = RollingHash(S)
    rht = RollingHash(T)

    def calc(i, l):
        if l <= i:
            return rhs.get(0, l)
        elif l <= i + m:
            return RollingHash.CalcMod(
                RollingHash.Mul(rhs.get(0, i), rhs.pw[l - i]) + rht.get(0, l - i)
            )
        else:
            return rhs.get(i + m, l)

    def get(i, l):
        if l < i:
            return S[l]
        elif l < i + m:
            return T[l - i]
        else:
            return S[l]

    ind = res[0]
    for i in range(1, len(res)):
        l = 0
        r = n
        while r - l > 1:
            mid = (l + r) // 2
            if calc(res[i], mid) == calc(ind, mid):
                l = mid
            else:
                r = mid

        if get(res[i], l) < get(ind, l):
            ind = res[i]

    for i in range(m):
        S[i + ind] = T[i]
    print(*S, sep="")


for _ in range(int(input())):
    solve()
