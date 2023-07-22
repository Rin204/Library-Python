# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


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


n, Q = map(int, input().split())
bit = BIT(n)
for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 0:
        bit.add(x - 1, y)
    else:
        print(bit.sum(x - 1, y))
