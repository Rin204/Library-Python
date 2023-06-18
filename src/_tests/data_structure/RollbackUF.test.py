# verification-helper: PROBLEM https://yukicoder.me/problems/no/1293
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.data_structure.RollbackUnionFind import RollbackUnionFind


n, d, w = map(int, input().split())
UF1 = RollbackUnionFind(n)
UF2 = RollbackUnionFind(n)
for _ in range(d):
    a, b = map(int, input().split())
    UF1.unite(a - 1, b - 1)
for _ in range(w):
    c, d = map(int, input().split())
    UF2.unite(c - 1, d - 1)

ans = -n
dic = {}
for i in range(n):
    p = UF1.find(i)
    if p not in dic:
        dic[p] = []
    dic[p].append(i)

for group in dic.values():
    u = group[0]
    state = UF2.get_state()
    for v in group:
        UF2.unite(u, v)
    ans += UF1.size(u) * UF2.size(u)
    UF2.rollback(state)

print(ans)
