from collections import deque


class ConvexHullTrick:
    def __init__(self):
        self.deq = deque()

    def check(f1, f2, f3):
        return (f2[0] - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])

    def f(self, _f, x):
        return _f[0] * x + _f[1]

    def add_line(self, a, b):
        """
        add  f_i(x) = a * x + b
        """
        f = (a, b)
        while len(self.deq) >= 2 and ConvexHullTrick.check(self.deq[-2], self.deq[-1], f):
            self.deq.pop()
        self.deq.append(f)

    def get(self, x):
        """
        return min_i f_i(x)
        """
        while len(self.deq) >= 2 and self.f(self.deq[0], x) >= self.f(self.deq[1], x):
            self.deq.popleft()

        return self.f(self.deq[0], x)
