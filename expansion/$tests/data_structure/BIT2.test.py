# verification-helper: PROBLEM https://yukicoder.me/problems/no/649

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


Q, k = map(int, input().split())
Query = []
X = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        X.append(query[1])
        Query.append(query[1])
    else:
        Query.append(-1)

X = sorted(set(X))
dic = {x: i for i, x in enumerate(X)}

bit = BIT(len(dic))
for q in Query:
    if q == -1:
        p = bit.lower_bound(k) - 1
        if p == len(X):
            print(-1)
        else:
            print(X[p])
            bit.add(p, -1)
    else:
        bit.add(dic[q], 1)
