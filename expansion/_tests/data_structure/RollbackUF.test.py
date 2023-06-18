# verification-helper: PROBLEM https://yukicoder.me/problems/no/1293
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


class RollbackUnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n
        self.history = []
        self.group_ = n

    def find(self, x):
        while self.par[x] >= 0:
            x = self.par[x]
        return x

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.history.append((x, self.par[x]))
        self.history.append((y, self.par[y]))
        if x == y:
            return False
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
        self.group_ -= 1
        return True

    def size(self, x):
        return -self.par[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    @property
    def group(self):
        return self.group_

    def undo(self):
        x, px = self.history.pop()
        y, py = self.history.pop()
        self.par[x] = px
        self.par[y] = py
        if x != y:
            self.group_ += 1

    def rollback(self, state):
        state <<= 1
        while len(self.history) > state:
            self.undo()

    def get_state(self):
        return len(self.history) >> 1


n, d, w = map(int, input().split())
UF1 = RollbackUnionFind(n)
UF2 = RollbackUnionFind(n)
for _ in range(d):
    a, b = map(int, input().split())
    UF1.unite(a - 1, b - 1)
for _ in range(w):
    c, d = map(int, input().split())
    UF2.unite(c - 1, d - 1)

ans = -n
dic = {}
for i in range(n):
    p = UF1.find(i)
    if p not in dic:
        dic[p] = []
    dic[p].append(i)

for group in dic.values():
    u = group[0]
    state = UF2.get_state()
    for v in group:
        UF2.unite(u, v)
    ans += UF1.size(u) * UF2.size(u)
    UF2.rollback(state)

print(ans)
