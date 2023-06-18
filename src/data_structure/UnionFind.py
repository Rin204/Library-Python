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
