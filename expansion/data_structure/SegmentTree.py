class SegmentTree:
    def __init__(self, n, ope, e, init=None):
        self.n = n
        self.n0 = 1 << (n - 1).bit_length()
        self.ope = ope
        self.e = e
        self.data = [e] * (2 * self.n0)
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

    def max_right(self, l, f):
        if l == self.n:
            return self.n
        l += self.n0
        sm = self.e
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
        sm = self.e
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
