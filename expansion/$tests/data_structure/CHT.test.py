# verification-helper: PROBLEM https://yukicoder.me/problems/no/409
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
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


n, a, b, w = map(int, input().split())
D = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = w


ch = ConvexHullTrick()
for i, d in enumerate(D):
    ch.add_line(-2 * b * i, 2 * dp[i] + 2 * a * i + b * i * i + b * i)
    x = i + 1
    mi = ch.get(x)
    tmp = mi + 2 * a + 2 * d - 2 * a * x + b * x * x - b * x
    dp[x] = tmp // 2

ans = 1 << 60
for i in range(n + 1):
    d = n - i
    ans = min(ans, dp[i] - a * d + b * d * (d + 1) // 2)
print(ans)
