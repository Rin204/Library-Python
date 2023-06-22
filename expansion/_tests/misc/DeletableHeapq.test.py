# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
        if n == 0:
            self.n0 = 0
        else:
            self.n0 = 1 << (n.bit_length() - 1)

    def sum_(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def sum(self, l, r=-1):
        if r == -1:
            return self.sum_(l)
        else:
            return self.sum_(r) - self.sum_(l)

    def get(self, i):
        return self.sum(i, i + 1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def lower_bound(self, x):
        if x <= 0:
            return 0
        i = 0
        k = self.n0
        while k > 0:
            if i + k <= self.n and self.data[i + k] < x:
                x -= self.data[i + k]
                i += k
            k //= 2
        return i + 1


import heapq


class DeletableHeapq:
    def __init__(self, lst=None, reverse=False):
        if reverse:
            self.pm = -1
        else:
            self.pm = 1
        if lst is None:
            self.hq = []
        else:
            self.hq = [self.pm * x for x in lst]

        heapq.heapify(self.hq)
        self.tot = sum(self.hq) * self.pm
        self.cnt = {}
        for x in self.hq:
            self.cnt[x] = self.cnt.get(x, 0) + 1
        self.length = len(self.hq)

    def __bool__(self):
        return bool(self.hq)

    def __len__(self):
        return self.length

    @property
    def sum(self):
        return self.tot

    def top(self):
        if self.hq:
            return self.hq[0] * self.pm
        else:
            return None

    def __getitem__(self, i):
        # 先頭要素にアクセスしたいときのみ
        assert i == 0
        return self.top()

    def push(self, x):
        self.length += 1
        self.cnt[x * self.pm] = self.cnt.get(x * self.pm, 0) + 1
        self.tot += x
        heapq.heappush(self.hq, x * self.pm)

    def pop(self):
        if not self.hq:
            return None
        self.length -= 1
        x = heapq.heappop(self.hq)
        self.cnt[x] -= 1
        self.tot -= x * self.pm
        self._delete()
        return x * self.pm

    def remove(self, x):
        if self.cnt.get(x * self.pm, 0) == 0:
            return False
        self.length -= 1
        self.cnt[x * self.pm] -= 1
        self.tot -= x
        self._delete()
        return True

    def _delete(self):
        while self.hq and self.cnt.get(self.hq[0], 0) == 0:
            heapq.heappop(self.hq)


import random

random.seed(10)

n = 500000
t = 500000
A = random.choices(range(n), k=t + 10)
cnt = len(A)
tot = sum(A)
if random.random() > 0.5:
    hq = DeletableHeapq(A)
else:
    hq = DeletableHeapq(A, reverse=True)
bit = BIT(n)
for a in A:
    bit.add(a, 1)

for _ in range(t):
    if random.random() < 0.3:
        p = hq[0]
        assert bit.get(p) >= 1
        if hq.pm == 1:
            assert bit.lower_bound(1) - 1 == p
        else:
            assert bit.lower_bound(cnt) - 1 == p
        bit.add(p, -1)
        assert p == hq.pop()
        cnt -= 1
        tot -= p
    else:
        p = random.randrange(n)
        if bit.get(p) == 0 or random.random() < 0.5:
            bit.add(p, 1)
            hq.push(p)
            cnt += 1
            tot += p
        else:
            bit.add(p, -1)
            assert hq.remove(p)
            cnt -= 1
            tot -= p

    assert len(hq) == cnt
    assert hq.tot == tot, (_, hq.tot, tot)


a, b = map(int, input().split())
print(a + b)
