# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.data_structure.DisjointSparseTable import DisjointSparseTable


def ope(l, r):
    return l + r


n, Q = map(int, input().split())
A = list(map(int, input().split()))
st = DisjointSparseTable(A, ope)
for _ in range(Q):
    l, r = map(int, input().split())
    print(st.prod(l, r))
