# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from src.misc.MadianHeap import MedianHeap
import random


A = [random.randrange(10**9) for _ in range(2000)]
hq = MedianHeap(A)
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

    A.sort()
    n = len(A)
    if n % 2 == 1:
        assert hq.get_med() == [A[n // 2], A[n // 2]]
    else:
        assert hq.get_med() == [A[n // 2 - 1], A[n // 2]]

    m = A[n // 2]
    assert hq.abs_sum() == sum(abs(a - m) for a in A)


a, b = map(int, input().split())
print(a + b)
