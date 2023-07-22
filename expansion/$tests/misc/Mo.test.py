# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_inversions_query
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


class Mo:
    def __init__(self, n, Q):
        self.n = n
        self.Q = Q
        self.width = int(max(1, n / max(1, Q * 2.0 / 3.0) ** 0.5))
        self.L = []
        self.R = []

    def insert(self, l, r):
        self.L.append(l)
        self.R.append(r)

    def run(self, add_left, add_right, delete_left, delete_right, rem):
        def cmp(i):
            b = self.L[i] // self.width
            res = b * self.n * 3
            if b % 2 == 0:
                res += self.R[i]
            else:
                res -= self.R[i]
            return res

        order = [(i, cmp(i)) for i in range(self.Q)]

        order.sort(key=lambda x: x[1])
        nl = 0
        nr = 0
        for i, _ in order:
            l = self.L[i]
            r = self.R[i]
            while nl > l:
                nl -= 1
                add_left(nl)
            while nr < r:
                add_right(nr)
                nr += 1
            while nl < l:
                delete_left(nl)
                nl += 1
            while nr > r:
                nr -= 1
                delete_right(nr)
            rem(i)


class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
        if n == 0:
            self.n0 = 0
        else:
            self.n0 = 1 << (n.bit_length() - 1)

    def sum_(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def sum(self, l, r=-1):
        if r == -1:
            return self.sum_(l)
        else:
            return self.sum_(r) - self.sum_(l)

    def get(self, i):
        return self.sum(i, i + 1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def lower_bound(self, x):
        if x <= 0:
            return 0
        i = 0
        k = self.n0
        while k > 0:
            if i + k <= self.n and self.data[i + k] < x:
                x -= self.data[i + k]
                i += k
            k //= 2
        return i + 1


import sys

input = sys.stdin.readline

n, Q = map(int, input().split())
A = list(map(int, input().split()))
dic = {a: i for i, a in enumerate(sorted(set(A)))}
A = [dic[a] for a in A]

mo = Mo(n, Q)
for _ in range(Q):
    l, r = map(int, input().split())
    mo.insert(l, r)

n = len(dic)
bit = BIT(n)
ans = [0] * Q
inv = 0


def add_left(i):
    global inv
    a = A[i]
    inv += bit.sum(a)
    bit.add(a, 1)


def add_right(i):
    global inv
    a = A[i]
    inv += bit.sum(a + 1, n)
    bit.add(a, 1)


def delete_left(i):
    global inv
    a = A[i]
    inv -= bit.sum(a)
    bit.add(a, -1)


def delete_right(i):
    global inv
    a = A[i]
    inv -= bit.sum(a + 1, n)
    bit.add(a, -1)


def rem(i):
    ans[i] = inv


mo.run(add_left, add_right, delete_left, delete_right, rem)
print(*ans, sep="\n")
