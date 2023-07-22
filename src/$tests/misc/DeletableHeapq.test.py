# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.data_structure.BIT import BIT
from src.misc.DeletableHeapq import DeletableHeapq
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
