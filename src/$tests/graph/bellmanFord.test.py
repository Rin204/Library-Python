# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=jp
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.graph.bellmanFord import bellmanFord


n, m, s = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
dist = bellmanFord(n, edges, s)
if dist is None:
    print("NEGATIVE CYCLE")
else:
    for d in dist:
        if d == 1 << 60:
            print("INF")
        else:
            print(d)
