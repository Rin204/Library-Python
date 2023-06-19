# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


class DisjointSparseTableBase_:
    def ope(self, l, r):
        pass

    def __init__(self, A):
        self.n = len(A)
        self.logn = self.n.bit_length()
        self.table = [0] * (self.logn * self.n)
        for i in range(self.n):
            self.table[i] = A[i]
        for i in range(1, self.logn):
            shift = 1 << i
            for j in range(0, self.n, shift << 1):
                t = min(j + shift, self.n)
                self.table[i * self.n + t - 1] = A[t - 1]
                for k in range(t - 2, j - 1, -1):
                    self.table[i * self.n + k] = self.ope(A[k], self.table[i * self.n + k + 1])
                if self.n <= t:
                    break
                self.table[i * self.n + t] = A[t]
                r = min(t + shift, self.n)
                for k in range(t + 1, r):
                    self.table[i * self.n + k] = self.ope(self.table[i * self.n + k - 1], A[k])

        self.look = [0] * (1 << self.logn)
        for i in range(2, 1 << self.logn):
            self.look[i] = self.look[i >> 1] + 1

    def prod(self, l, r):
        assert l < r
        r -= 1
        if l == r:
            return self.table[l]
        logn = self.look[l ^ r]
        return self.ope(self.table[logn * self.n + l], self.table[logn * self.n + r])


class RangeSum(DisjointSparseTableBase_):
    def ope(self, l, r):
        return l + r


n, Q = map(int, input().split())
A = list(map(int, input().split()))
st = RangeSum(A)
for _ in range(Q):
    l, r = map(int, input().split())
    print(st.prod(l, r))
