# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from src.data_structure.SegmentTreeBase_ import SegmentTreeBase_

MOD = 998244353


class PointSetRangeComposite(SegmentTreeBase_):
    def ope(self, l, r):
        a = l >> 30
        b = l ^ (a << 30)
        c = r >> 30
        d = r ^ (c << 30)

        e = (a * c) % MOD
        f = (b * c + d) % MOD

        return (e << 30) | f

    def e(self):
        return 1 << 30


n, Q = map(int, input().split())
A = [0] * n
for i in range(n):
    a, b = map(int, input().split())
    A[i] = (a << 30) | b
seg = PointSetRangeComposite(n, A)
for _ in range(Q):
    t, p, c, d = map(int, input().split())
    if t == 0:
        seg[p] = (c << 30) | d
    else:
        res = seg.prod(p, c)
        a = res >> 30
        b = res ^ (a << 30)
        ans = (a * d + b) % MOD
        print(ans)
