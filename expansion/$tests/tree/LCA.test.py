# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


class LCA:
    def __init__(self, n, root=0, edges=None):
        self.n = n
        self.root = root
        self.logn = (self.n - 1).bit_length()
        if edges is None:
            self.edges = [[] for _ in range(n)]
        else:
            self.edges = edges
            # コピーしてないので注意

        self.depth = [-1] * n
        self.par = [[-1] * n for _ in range(self.logn)]

    def build(self):
        self.depth[self.root] = 0
        stack = [self.root]
        while stack:
            pos = stack.pop()
            for npos in self.edges[pos]:
                if self.depth[npos] == -1:
                    self.depth[npos] = self.depth[pos] + 1
                    stack.append(npos)
                    self.par[0][npos] = pos

        for i in range(1, self.logn):
            for j in range(self.n):
                if self.par[i - 1][j] != -1:
                    self.par[i][j] = self.par[i - 1][self.par[i - 1][j]]

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def read_edges(self, indexed=1):
        for _ in range(self.n - 1):
            u, v = map(int, input().split())
            u -= indexed
            v -= indexed
            self.add_edge(u, v)

    def lca(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u

        d = self.depth[v] - self.depth[u]
        i = 0
        while d > 0:
            if d & 1:
                v = self.par[i][v]
            i += 1
            d >>= 1

        if u == v:
            return u

        d = self.depth[u]
        logn = (d - 1).bit_length()
        for i in range(logn - 1, -1, -1):
            pu = self.par[i][u]
            pv = self.par[i][v]
            if pu != pv:
                u = pu
                v = pv

        return self.par[0][u]

    def dist(self, u, v):
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]

    def jump(self, u, v, k):
        if k == 0:
            return u

        p = self.lca(u, v)
        du = self.depth[u] - self.depth[p]
        dv = self.depth[v] - self.depth[p]
        if du + dv < k:
            return -1
        if k <= du:
            d = k
        else:
            u = v
            d = du + dv - k

        i = 0
        while d > 0:
            if d & 1:
                u = self.par[i][u]
            i += 1
            d >>= 1

        return u


n, Q = map(int, input().split())
P = list(map(int, input().split()))
G = LCA(n)
for i, p in enumerate(P, 1):
    G.add_edge(i, p)

G.build()
for _ in range(Q):
    u, v = map(int, input().split())
    print(G.lca(u, v))
