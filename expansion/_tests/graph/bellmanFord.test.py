# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=jp
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


def bellmanFord(n, edges, s, inf=1 << 60):
    """
    edges = [(from1, to1, cost1), (from2, to2, cost2), ...)]
    """
    dist = [inf] * n
    dist[s] = 0

    for _ in range(n):
        update = False
        for u, v, d in edges:
            if dist[u] != inf and dist[v] > dist[u] + d:
                dist[v] = dist[u] + d
                update = True

        if not update:
            return dist

    return None


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
