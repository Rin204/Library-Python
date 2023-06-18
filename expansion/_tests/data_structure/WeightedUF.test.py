# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_B
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


class WeightedUnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n
        self.group_ = n
        self.D = [0] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        lst = []
        while self.par[x] >= 0:
            lst.append(x)
            x = self.par[x]
        for y in lst[::-1]:
            self.D[y] += self.D[self.par[y]]
            self.par[y] = x
        return x

    def unite(self, x, y, d):
        # D[x] - D[y] = d
        xp = self.find(x)
        yp = self.find(y)
        d -= self.D[x]
        d += self.D[y]
        x = xp
        y = yp
        if x == y:
            assert d == 0
            return False

        if self.par[x] > self.par[y]:
            x, y = y, x
            d *= -1

        self.par[x] += self.par[y]
        self.par[y] = x
        self.group_ -= 1
        self.D[y] = -d
        return True

    def size(self, x):
        return -self.par[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    @property
    def group(self):
        return self.group_

    def diff(self, x, y):
        if self.same(x, y):
            return self.D[x] - self.D[y]
        else:
            return None


n, Q = map(int, input().split())
UF = WeightedUnionFind(n)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        x, y, z = query[1:]
        UF.unite(y, x, z)
    else:
        x, y = query[1:]
        res = UF.diff(y, x)
        if res is None:
            print("?")
        else:
            print(res)
