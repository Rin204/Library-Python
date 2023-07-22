# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_inversions_query
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.misc.MoBase_ import MoBase_
from src.data_structure.BIT import BIT
import sys

input = sys.stdin.readline

n, Q = map(int, input().split())
A = list(map(int, input().split()))
dic = {a: i for i, a in enumerate(sorted(set(A)))}
A = [dic[a] for a in A]


class Mo(MoBase_):
    def __init__(self, n, Q):
        super().__init__(n, Q)
        self.inv = 0

    def add_left(self, i):
        a = A[i]
        self.inv += bit.sum(a)
        bit.add(a, 1)

    def add_right(self, i):
        a = A[i]
        self.inv += bit.sum(a + 1, le)
        bit.add(a, 1)

    def delete_left(self, i):
        a = A[i]
        self.inv -= bit.sum(a)
        bit.add(a, -1)

    def delete_right(self, i):
        a = A[i]
        self.inv -= bit.sum(a + 1, le)
        bit.add(a, -1)

    def rem(self, i):
        ans[i] = self.inv


mo = Mo(n, Q)
for _ in range(Q):
    l, r = map(int, input().split())
    mo.insert(l, r)

le = len(dic)
bit = BIT(le)
ans = [0] * Q

mo.run()
print(*ans, sep="\n")
