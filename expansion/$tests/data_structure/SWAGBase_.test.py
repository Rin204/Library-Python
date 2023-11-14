# verification-helper: PROBLEM https://judge.yosupo.jp/problem/queue_operate_all_composite
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


class SWAGBase_:
    def ope(self, l, r):
        raise NotImplementedError

    def e(self):
        raise NotImplementedError

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


MOD = 998244353


class QueueOperateAllComposite(SWAGBase_):
    def ope(self, l, r):
        a = l >> 30
        b = l ^ (a << 30)
        c = r >> 30
        d = r ^ (c << 30)

        e = (a * c) % MOD
        f = (b * c + d) % MOD

        return (e << 30) | f

    def e(self):
        return 1 << 30


Q = int(input())
swag = QueueOperateAllComposite()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        swag.push((query[1] << 30) | query[2])
    elif query[0] == 1:
        swag.pop()
    else:
        res = swag.prod()
        a = res >> 30
        b = res ^ (a << 30)
        ans = (a * query[1] + b) % MOD
        print(ans)
