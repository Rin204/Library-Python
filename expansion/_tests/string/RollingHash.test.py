# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B&lang=ja

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


S = input()
T = input()
ls = len(S)
lt = len(T)
rh1 = RollingHash(S)
rh2 = RollingHash(T)
for i in range(ls - lt + 1):
    if rh1.get(i, i + lt) == rh2.get(0, lt):
        print(i)
