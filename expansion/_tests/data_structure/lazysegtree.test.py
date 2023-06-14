# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_range_sum
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


class LazySegmentTree:
    def __init__(self, n, ope, e, mapping, composition, id_, init=None):
        self.n = n
        self.log = (n - 1).bit_length()
        self.n0 = 1 << self.log
        self.ope = ope
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id_ = id_
        self.data = [e] * (2 * self.n0)
        self.lazy = [id_] * self.n0
        if init is not None:
            for i in range(n):
                self.data[self.n0 + i] = init[i]
            for i in range(self.n0 - 1, 0, -1):
                self.data[i] = self.ope(self.data[2 * i], self.data[2 * i + 1])

    def _all_apply(self, p, f):
        self.data[p] = self.mapping(f, self.data[p])
        if p < self.n0:
            self.lazy[p] = self.composition(f, self.lazy[p])

    def _push(self, p):
        self._all_apply(2 * p, self.lazy[p])
        self._all_apply(2 * p + 1, self.lazy[p])
        self.lazy[p] = self.id_

    def _update(self, p):
        self.data[p] = self.ope(self.data[2 * p], self.data[2 * p + 1])

    def set(self, p, x):
        p += self.n0
        for i in range(self.log, 0, -1):
            self._push(p >> i)

        self.data[p] = x
        for i in range(1, self.log + 1):
            self._update(p >> i)

    def __setitem__(self, p, x):
        self.set(p, x)

    def get(self, p):
        p += self.n0
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        return self.data[p]

    def __getitem__(self, p):
        return self.get(p)

    def prod(self, l, r):
        assert 0 <= l <= r <= self.n0
        l += self.n0
        r += self.n0

        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push((r - 1) >> i)

        lles = self.e
        rres = self.e
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

    def all_prod(self):
        return self.data[1]

    def _apply(self, p, f):
        p += self.n0
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        self.data[p] = self.mapping(f, self.data[p])
        for i in range(1, self.log + 1):
            self._update(p >> i)

    def apply(self, l, r, f=None):
        if f is None:
            self._apply(l, r)
            return

        if l == r:
            return

        l += self.n0
        r += self.n0

        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push((r - 1) >> i)

        l2 = l
        r2 = r
        while l < r:
            if l & 1:
                self._all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self._all_apply(r, f)
            l >>= 1
            r >>= 1

        l = l2
        r = r2

        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l:
                self._update(l >> i)
            if ((r >> i) << i) != r:
                self._update((r - 1) >> i)

    def max_right(self, l, f):
        if l == self.n:
            return self.n
        l += self.n0
        for i in range(self.log, 0, -1):
            self._push(l >> i)

        sm = self.e
        while 1:
            while l % 2 == 0:
                l >>= 1
            if not f(self.ope(sm, self.data[l])):
                while l < self.n0:
                    self._push(l)
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

        for i in range(self.log, 0, -1):
            if ((r >> i) << i) != r:
                self._push((r - 1) >> i)

        sm = self.e
        while 1:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not f(self.ope(self.data[r], sm)):
                while r < self.n0:
                    self._push(r)
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


n, Q = map(int, input().split())
A = list(map(int, input().split()))
A = [(a << 30) + 1 for a in A]


def ope(l, r):
    a0 = l >> 30
    a1 = l ^ (a0 << 30)
    b0 = r >> 30
    b1 = r ^ (b0 << 30)
    c0 = (a0 + b0) % MOD
    c1 = (a1 + b1) % MOD
    return (c0 << 30) + c1


def mapping(f, x):
    a0 = f >> 30
    a1 = f ^ (a0 << 30)
    b0 = x >> 30
    b1 = x ^ (b0 << 30)
    c0 = (a0 * b0 + a1 * b1) % MOD
    c1 = b1
    return (c0 << 30) + c1


def composition(f, g):
    a0 = f >> 30
    a1 = f ^ (a0 << 30)
    b0 = g >> 30
    b1 = g ^ (b0 << 30)
    c0 = (a0 * b0) % MOD
    c1 = (a0 * b1 + a1) % MOD
    return (c0 << 30) + c1


seg = LazySegmentTree(n, ope, 0, mapping, composition, 1 << 30, A)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        l, r, b, c = query[1:]
        seg.apply(l, r, (b << 30) + c)
    else:
        l, r = query[1:]
        print(seg.prod(l, r) >> 30)
