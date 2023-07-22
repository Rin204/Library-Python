# verification-helper: PROBLEM https://yukicoder.me/problems/no/1038
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

## yukicoder のオンライン実行だとTLに間に合ったり間に合わなかったりする


class CentroidDecomposition:
    def __init__(self, n, edges=None):
        self.n = n
        self.par = [-1] * n  # 重心分解木の親
        self.depth = [-1] * n  # 重心分解木の深さ
        self.size = [-1] * n  # 重心分解木の部分木のサイズ
        self.childcnt = [0] * n  # 重心分解木の子の数
        if edges is None:
            self.edges = [[] for _ in range(n)]
        else:
            self.edges = edges
            # コピーしてないので注意

        self.centroids = []  # centroids[i] := 深さが i の重心のリスト
        self.treeind = []  # treeind[j * logn + i] := 頂点 j が深さ i の重心の何番目の部分木か
        self.cent_dist = []  # cent_dist[j * logn + i] := 頂点 j が深さ i の重心からの距離

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def read_edges(self, indexed=1):
        for _ in range(self.n - 1):
            u, v = map(int, input().split())
            u -= indexed
            v -= indexed
            self.add_edge(u, v)

    def build(self):
        stack = [(0, -1, 0, -1)]
        while stack:
            pos, bpos, d, c = stack.pop()
            st = [pos]
            route = []
            sz = 0

            if len(self.treeind) == d * self.n:
                self.treeind += [-1] * self.n
                self.cent_dist += [-1] * self.n
                self.centroids.append([])
            if d >= 1:
                self.cent_dist[(d - 1) * self.n + pos] = 1

            while st:
                pos = st.pop()
                self.depth[pos] = -2
                route.append(pos)
                sz += 1
                if d >= 1:
                    self.treeind[(d - 1) * self.n + pos] = c

                for npos in self.edges[pos]:
                    if self.depth[npos] == -1:
                        st.append(npos)
                        if d >= 1:
                            self.cent_dist[(d - 1) * self.n + npos] = (
                                self.cent_dist[(d - 1) * self.n + pos] + 1
                            )

            g = -1
            for pos in route[::-1]:
                self.size[pos] = 1
                self.depth[pos] = -1
                if g != -1:
                    continue
                isg = True
                for npos in self.edges[pos]:
                    if self.depth[npos] == -1:
                        self.size[pos] += self.size[npos]
                        if self.size[npos] * 2 > sz:
                            isg = False
                            break

                if isg and 2 * self.size[pos] >= sz:
                    g = pos

            self.centroids[d].append(g)

            self.size[g] = sz
            self.par[g] = bpos
            self.depth[g] = d
            self.cent_dist[d * self.n + g] = 0

            if sz != 1:
                c = 0
                for npos in self.edges[g]:
                    if self.depth[npos] == -1:
                        stack.append((npos, g, d + 1, c))
                        c += 1
                self.childcnt[g] = c

        self.logn = len(self.centroids)
        nex = [0] * (self.n * self.logn)
        for i in range(self.n):
            for j in range(self.logn):
                nex[i * self.logn + j] = self.cent_dist[j * self.n + i]

        self.cent_dist, nex = nex, self.cent_dist

        for i in range(self.n):
            for j in range(self.logn):
                nex[i * self.logn + j] = self.treeind[j * self.n + i]

        self.treeind = nex

    def cent_ind_dist(self, u):
        """
        u + u の各先祖の {頂点番号, 距離} を返す
        """

        ret = [(u, 0)]
        v = u
        p = u * self.logn + self.depth[u] - 1
        for d in range(self.depth[u] - 1, -1, -1):
            v = self.par[v]
            ret.append((v, self.cent_dist[p]))
            p -= 1

        return ret


class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
        if n == 0:
            self.n0 = 0
        else:
            self.n0 = 1 << (n.bit_length() - 1)

    def sum_(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def sum(self, l, r=-1):
        if r == -1:
            return self.sum_(l)
        else:
            return self.sum_(r) - self.sum_(l)

    def get(self, i):
        return self.sum(i, i + 1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def lower_bound(self, x):
        if x <= 0:
            return 0
        i = 0
        k = self.n0
        while k > 0:
            if i + k <= self.n and self.data[i + k] < x:
                x -= self.data[i + k]
                i += k
            k //= 2
        return i + 1


import sys

input = sys.stdin.readline


n, Q = map(int, input().split())
G = CentroidDecomposition(n)
G.read_edges()
G.build()
logn = len(G.centroids)
bit = []
subbit = []
L = [0] * n
subL = [0] * n

for d in range(logn):
    c = 0
    c2 = 0
    for g in G.centroids[d]:
        L[g] = c
        if d != 0:
            subL[g] = c2
        c += G.size[g]
        c2 += G.size[g] + 1
    bit.append(BIT(c))
    if d != 0:
        subbit.append(BIT(c2))


def add(x, y, z):
    bg = -1
    for g, d in G.cent_ind_dist(x):
        dd = y - d
        if dd >= 0:
            bit[G.depth[g]].add(L[g], z)
            bit[G.depth[g]].add(L[g] + min(dd + 1, G.size[g]), -z)
            if bg != -1:
                subbit[G.depth[g]].add(subL[bg] + 1, z)
                subbit[G.depth[g]].add(subL[bg] + min(dd + 1, G.size[bg] + 1), -z)
        bg = g


def get(x):
    bg = -1
    ret = 0
    for g, d in G.cent_ind_dist(x):
        ret += bit[G.depth[g]].sum(L[g] + d + 1)
        if bg != -1:
            ret -= subbit[G.depth[g]].sum(subL[bg] + d + 1)
        bg = g

    return ret


out = []
for _ in range(Q):
    x, y, z = map(int, input().split())
    x -= 1
    out.append(get(x))
    add(x, y, z)

print(*out, sep="\n")
