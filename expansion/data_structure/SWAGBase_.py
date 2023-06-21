class SWAGBase_:
    def ope(self, l, r):
        pass

    def e(self):
        pass

    def __init__(self):
        self.L = []
        self.R = []
        self.Lcum = [self.e()]
        self.Rall = self.e()

    def push(self, x):
        self.R.append(x)
        self.Rall = self.ope(self.Rall, x)

    def pop(self):
        if not self.L:
            while self.R:
                self.L.append(self.R.pop())
                self.Lcum.append(self.ope(self.L[-1], self.Lcum[-1]))
            self.Rall = self.e()
        self.L.pop()
        self.Lcum.pop()

    def prod(self):
        return self.ope(self.Lcum[-1], self.Rall)

    def size(self):
        return len(self.L) + len(self.R)

    def __len__(self):
        return self.size()

    def clear(self):
        self.L = []
        self.R = []
        self.Lcum = [self.e()]
        self.Rall = self.e()
