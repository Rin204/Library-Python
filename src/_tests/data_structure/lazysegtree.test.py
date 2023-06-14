# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_range_sum
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.data_structure.LazySegmentTree import LazySegmentTree

MOD = 998244353


n, Q = map(int, input().split())
A = list(map(int, input().split()))
A = [(a << 30) + 1 for a in A]


def ope(l, r):
    a0 = l >> 30
    a1 = l ^ (a0 << 30)
    b0 = r >> 30
    b1 = r ^ (b0 << 30)
    c0 = (a0 + b0) % MOD
    c1 = (a1 + b1) % MOD
    return (c0 << 30) + c1


def mapping(f, x):
    a0 = f >> 30
    a1 = f ^ (a0 << 30)
    b0 = x >> 30
    b1 = x ^ (b0 << 30)
    c0 = (a0 * b0 + a1 * b1) % MOD
    c1 = b1
    return (c0 << 30) + c1


def composition(f, g):
    a0 = f >> 30
    a1 = f ^ (a0 << 30)
    b0 = g >> 30
    b1 = g ^ (b0 << 30)
    c0 = (a0 * b0) % MOD
    c1 = (a0 * b1 + a1) % MOD
    return (c0 << 30) + c1


seg = LazySegmentTree(n, ope, 0, mapping, composition, 1 << 30, A)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        l, r, b, c = query[1:]
        seg.apply(l, r, (b << 30) + c)
    else:
        l, r = query[1:]
        print(seg.prod(l, r) >> 30)
