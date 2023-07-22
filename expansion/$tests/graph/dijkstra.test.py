# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
import heapq


def dijkstra(edges, s=0, inf=1 << 60):
    """
    edges[from] = [(to1, cost1), (to2, cost2), ...)]
    """
    n = len(edges)
    dist = [inf] * n
    dist[s] = 0
    hq = [s]
    while hq:
        tmp = heapq.heappop(hq)
        d = tmp // n
        pos = tmp - n * d
        if dist[pos] < d:
            continue
        for npos, c in edges[pos]:
            if dist[npos] > dist[pos] + c:
                dist[npos] = dist[pos] + c
                heapq.heappush(hq, npos + n * dist[npos])

    return dist


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
