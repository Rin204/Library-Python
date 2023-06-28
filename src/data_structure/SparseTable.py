class SparseTable:
    def __init__(self, A, ope):
        self.n = len(A)
        self.ope = ope
        self.logn = (self.n - 1).bit_length()
        if self.n == 1:
            self.logn = 1
        self.table = [0] * (self.logn * self.n)
        for i in range(self.n):
            self.table[i] = A[i]
        for i in range(1, self.logn):
            ma = self.n - (1 << i) + 1
            d = 1 << (i - 1)
            for j in range(ma):
                self.table[i * self.n + j] = ope(
                    self.table[(i - 1) * self.n + j], self.table[(i - 1) * self.n + j + d]
                )

        self.look = [0] * self.n
        for i in range(2, self.n):
            self.look[i] = self.look[i >> 1] + 1

    def prod(self, l, r):
        assert l < r
        d = r - l
        if d == 1:
            return self.table[l]
        logn = self.look[d - 1]
        return self.ope(self.table[logn * self.n + l], self.table[logn * self.n + r - (1 << logn)])
