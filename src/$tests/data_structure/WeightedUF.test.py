# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_B
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.data_structure.WeightedUnionFind import WeightedUnionFind


n, Q = map(int, input().split())
UF = WeightedUnionFind(n)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        x, y, z = query[1:]
        UF.unite(y, x, z)
    else:
        x, y = query[1:]
        res = UF.diff(y, x)
        if res is None:
            print("?")
        else:
            print(res)
