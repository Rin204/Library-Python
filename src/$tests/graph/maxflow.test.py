# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A&lang=jp
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.graph.maxflow import mf_graph


n, m = map(int, input().split())
G = mf_graph(n)
for _ in range(m):
    u, v, c = map(int, input().split())
    G.add_edge(u, v, c)

print(G.flow(0, n - 1))
