# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum

from src.data_structure.SegmentTreeBase_ import SegmentTreeBase_


class PointAddRangeSum(SegmentTreeBase_):
    def e(self):
        return 0

    def ope(self, l, r):
        return l + r


n, Q = map(int, input().split())
A = list(map(int, input().split()))
seg = PointAddRangeSum(n, A)
for _ in range(Q):
    t, p, x = map(int, input().split())
    if t == 0:
        seg[p] = seg[p] + x
    else:
        print(seg.prod(p, x))
