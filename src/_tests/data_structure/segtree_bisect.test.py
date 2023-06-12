# verification-helper: PROBLEM https://yukicoder.me/problems/no/649

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from random import randrange
from src.data_structure.SegmentTree import SegmentTree

Q, k = map(int, input().split())
Query = []
X = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        X.append(query[1])
        Query.append(query[1])
    else:
        Query.append(-1)

X = sorted(set(X))
# 二分探索のテスト用
add = randrange(100)
rev = randrange(2)
X = [-1] * add + X
if rev:
    X = X[::-1]
dic = {x: i for i, x in enumerate(X)}


def ope(l, r):
    return l + r


seg = SegmentTree(len(X), 0, ope)
if not rev:
    for q in Query:
        if q == -1:
            p = seg.max_right(add, lambda x: x < k)
            if p == len(X):
                print(-1)
            else:
                print(X[p])
                seg[p] = seg[p] - 1
        else:
            seg[dic[q]] = seg[dic[q]] + 1
else:
    for q in Query:
        if q == -1:
            p = seg.min_left(len(X) - add, lambda x: x < k) - 1
            if p == -1:
                print(-1)
            else:
                print(X[p])
                seg[p] = seg[p] - 1
        else:
            seg[dic[q]] = seg[dic[q]] + 1
