# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from src.data_structure.BIT import BIT

n, Q = map(int, input().split())
bit = BIT(n)
for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 0:
        bit.add(x - 1, y)
    else:
        print(bit.sum(x - 1, y))
