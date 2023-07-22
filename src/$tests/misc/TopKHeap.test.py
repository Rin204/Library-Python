# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from src.misc.TopKHeap import TopKHeap
import random


k = random.randrange(1000, 2000)
A = [random.randrange(10**9) for _ in range(k)]
hq = TopKHeap(k, False, A)
Q = 1000
for _ in range(Q):
    t = random.randrange(2)
    if t == 0:
        a = random.randrange(10**9)
        hq.push(a)
        A.append(a)
    else:
        a = random.choice(A)
        hq.remove(a)
        A.remove(a)

    A.sort(reverse=True)
    assert hq.tot == sum(A[:k])

a, b = map(int, input().split())
print(a + b)
