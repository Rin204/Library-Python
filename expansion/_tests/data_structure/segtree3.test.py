# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


class SegmentTreeBase_:
    def ope(self, l, r):
        return None

    def e(self):
        return None

    def __init__(self, n, init=None):
        self.n = n
        self.n0 = 1 << (n - 1).bit_length()
        self.data = [self.e()] * (2 * self.n0)
        if init is not None:
            for i in range(n):
                self.data[self.n0 + i] = init[i]
            for i in range(self.n0 - 1, 0, -1):
                self.data[i] = self.ope(self.data[2 * i], self.data[2 * i + 1])

    def build(self):
        for i in range(self.n0 - 1, 0, -1):
            self.data[i] = self.ope(self.data[2 * i], self.data[2 * i + 1])

    def set(self, i, x):
        i += self.n0
        self.data[i] = x
        while i > 1:
            i >>= 1
            self.data[i] = self.ope(self.data[2 * i], self.data[2 * i + 1])

    def get(self, i):
        return self.data[i + self.n0]

    def __getitem__(self, i):
        return self.data[i + self.n0]

    def __setitem__(self, i, x):
        self.set(i, x)

    def prod(self, l, r):
        assert 0 <= l <= r <= self.n0
        l += self.n0
        r += self.n0
        lles = self.e()
        rres = self.e()
        while l < r:
            if l & 1:
                lles = self.ope(lles, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                rres = self.ope(self.data[r], rres)
            l >>= 1
            r >>= 1
        return self.ope(lles, rres)

    def max_right(self, l, f):
        if l == self.n:
            return self.n
        l += self.n0
        sm = self.e()
        while 1:
            while l % 2 == 0:
                l >>= 1
            if not f(self.ope(sm, self.data[l])):
                while l < self.n0:
                    l <<= 1
                    if f(self.ope(sm, self.data[l])):
                        sm = self.ope(sm, self.data[l])
                        l += 1
                return l - self.n0
            sm = self.ope(sm, self.data[l])
            l += 1
            if l & -l == l:
                break
        return self.n

    def min_left(self, r, f):
        if r == 0:
            return 0
        r += self.n0
        sm = self.e()
        while 1:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not f(self.ope(self.data[r], sm)):
                while r < self.n0:
                    r = 2 * r + 1
                    if f(self.ope(self.data[r], sm)):
                        sm = self.ope(self.data[r], sm)
                        r -= 1
                return r + 1 - self.n0
            sm = self.ope(self.data[r], sm)
            if r & -r == r:
                break
        return 0


MOD = 998244353


class PointSetRangeComposite(SegmentTreeBase_):
    def ope(self, l, r):
        a = l >> 30
        b = l ^ (a << 30)
        c = r >> 30
        d = r ^ (c << 30)

        e = (a * c) % MOD
        f = (b * c + d) % MOD

        return (e << 30) | f

    def e(self):
        return 1 << 30


n, Q = map(int, input().split())
A = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    A[i] = (a << 30) | b
seg = PointSetRangeComposite(n, A)
for _ in range(Q):
    t, p, c, d = map(int, input().split())
    if t == 0:
        seg[p] = (c << 30) | d
    else:
        res = seg.prod(p, c)
        a = res >> 30
        b = res ^ (a << 30)
        ans = (a * d + b) % MOD
        print(ans)
