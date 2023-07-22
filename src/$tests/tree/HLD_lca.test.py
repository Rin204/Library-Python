# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.tree.HLD import HLD


n, Q = map(int, input().split())
P = list(map(int, input().split()))
G = HLD(n)
for i, p in enumerate(P, 1):
    G.add_edge(i, p)

G.build()
for _ in range(Q):
    u, v = map(int, input().split())
    print(G.lca(u, v))
