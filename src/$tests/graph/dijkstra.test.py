# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.graph.dijkstra import dijkstra


n, m, s = map(int, input().split())
edges = [[] for _ in range(n)]
redges = [[] for _ in range(n)]
for _ in range(m):
    u, v, d = map(int, input().split())
    edges[u].append((v, d))
    redges[v].append((u, d))

dist = dijkstra(edges, s)
for d in dist:
    if d == 1 << 60:
        print("INF")
    else:
        print(d)
