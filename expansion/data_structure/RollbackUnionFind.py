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
