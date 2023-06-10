# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n
        self.group_ = n

    def find(self, x):
        if self.par[x] < 0:
            return x
        lst = []
        while self.par[x] >= 0:
            lst.append(x)
            x = self.par[x]
        for y in lst:
            self.par[y] = x
        return x

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x
        self.group_ -= 1
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    @property
    def group(self):
        return self.group_


def Kruskal(n, edges, is_sorted=False):
    if n == 1:
        return 0
    if not is_sorted:
        edges.sort(key=lambda x: x[2])
    UF = UnionFind(n)
    res = 0
    for u, v, cost in edges:
        if UF.unite(u, v):
            res += cost
            if UF.group == 1:
                return res
    return -1


n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
print(Kruskal(n, edges))
