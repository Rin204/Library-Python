# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.tree.HLD import HLD
from src.data_structure.BIT import BIT


n, Q = map(int, input().split())
A = list(map(int, input().split()))
G = HLD(n)
G.read_edges(0)
G.build()
A = G.reorder(A)
bit = BIT(n)
for i, a in enumerate(A):
    bit.add(i, a)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        p, x = query[1:]
        bit.add(G.L[p], x)
    else:
        u, v = query[1:]
        ans = 0
        for l, r in G.get_path(u, v):
            l = G.L[l]
            r = G.L[r]
            if l > r:
                l, r = r, l
            ans += bit.sum(l, r + 1)
        print(ans)
