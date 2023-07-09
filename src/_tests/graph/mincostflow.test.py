# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B&lang=ja
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.graph.mincostflow import mcf_graph


n, m, f = map(int, input().split())
G = mcf_graph(n)
for _ in range(m):
    G.add_edge(*map(int, input().split()))

fl, c = G.flow(0, n - 1, f)
if fl < f:
    c = -1

print(c)
