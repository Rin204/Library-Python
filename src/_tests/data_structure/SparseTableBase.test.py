# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.data_structure.SparseTableBase_ import SparseTableBase_


class RangeMin(SparseTableBase_):
    def ope(self, l, r):
        return min(l, r)


n, Q = map(int, input().split())
A = list(map(int, input().split()))
st = RangeMin(A)
for _ in range(Q):
    l, r = map(int, input().split())
    print(st.prod(l, r))
