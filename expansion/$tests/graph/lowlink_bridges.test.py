# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B&lang=ja
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


def lowLink(edges):
    """
    edges[from] = [to1, to2, ...]
    """
    n = len(edges)
    ord = [-1] * n
    low = [-1] * n
    isartic = [False] * n
    bridge = []

    def dfs(root, k):
        x = root * (n + 1) + n
        stack = [~x, x]
        cnt = 0
        while stack:
            tmp = stack.pop()
            if tmp >= 0:
                pos = tmp // (n + 1)
                bpos = tmp - (n + 1) * pos

                if bpos != n and ord[pos] != -1:
                    low[bpos] = min(low[bpos], ord[pos])
                    stack.pop()
                    continue

                low[pos] = ord[pos] = k
                k += 1
                for npos in edges[pos]:
                    if npos == bpos:
                        continue

                    if ord[npos] == -1:
                        if bpos == n:
                            cnt += 1
                        x = npos * (n + 1) + pos
                        stack.append(~x)
                        stack.append(x)
                    else:
                        low[pos] = min(low[pos], ord[npos])
                        if npos == root:
                            cnt -= 1
            else:
                tmp = ~tmp
                pos = tmp // (n + 1)
                bpos = tmp - (n + 1) * pos

                if bpos != n and ord[bpos] < low[pos]:
                    bridge.append((min(pos, bpos), max(pos, bpos)))

                if bpos != n and bpos != root and low[pos] >= ord[bpos]:
                    isartic[bpos] = True

                if bpos != n:
                    low[bpos] = min(low[bpos], low[pos])

        if cnt >= 2:
            isartic[root] = True

        return k

    k = 0
    for i in range(n):
        if ord[i] == -1:
            k = dfs(i, k)

    return isartic, bridge


n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

_, bridges = lowLink(edges)
bridges.sort(key=lambda x: x[0] * n + x[1])
for u, v in bridges:
    print(u, v)
