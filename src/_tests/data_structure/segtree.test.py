# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from src.data_structure.SegmentTree import SegmentTree


def ope(l, r):
    return l + r


n, Q = map(int, input().split())
A = list(map(int, input().split()))
seg = SegmentTree(n, 0, ope, A)
for _ in range(Q):
    t, p, x = map(int, input().split())
    if t == 0:
        seg[p] = seg[p] + x
    else:
        print(seg.prod(p, x))
