class MoBase_:
    def add_left(self, i):
        pass

    def add_right(self, i):
        pass

    def delete_left(self, i):
        pass

    def delete_right(self, i):
        pass

    def rem(self, i):
        pass

    def __init__(self, n, Q):
        self.n = n
        self.Q = Q
        self.width = int(max(1, n / max(1, Q * 2.0 / 3.0) ** 0.5))
        self.L = []
        self.R = []

    def insert(self, l, r):
        self.L.append(l)
        self.R.append(r)

    def run(self):
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
                self.add_left(nl)
            while nr < r:
                self.add_right(nr)
                nr += 1
            while nl < l:
                self.delete_left(nl)
                nl += 1
            while nr > r:
                nr -= 1
                self.delete_right(nr)
            self.rem(i)
