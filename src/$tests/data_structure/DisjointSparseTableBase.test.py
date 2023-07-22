# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.data_structure.DisjointSparseTableBase_ import DisjointSparseTableBase_


class RangeSum(DisjointSparseTableBase_):
    def ope(self, l, r):
        return l + r


n, Q = map(int, input().split())
A = list(map(int, input().split()))
st = RangeSum(A)
for _ in range(Q):
    l, r = map(int, input().split())
    print(st.prod(l, r))
