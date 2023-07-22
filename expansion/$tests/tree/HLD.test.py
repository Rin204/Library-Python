# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


class HLD:
    def __init__(self, n, edges=None):
        self.n = n
        if edges is None:
            self.edges = [[] for _ in range(n)]
        else:
            self.edges = edges
            # コピーしてないので注意

        self.size = [-1] * n
        self.par = [-1] * n
        self.depth = [-1] * n
        self.path_ind = [-1] * n
        self.path_root = []
        self.heavy_child = [-1] * n
        self.isheavy = [False] * n
        self.L = [-1] * n
        self.R = [-1] * n

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def read_edges(self, indexed=1):
        for _ in range(self.n - 1):
            u, v = map(int, input().split())
            u -= indexed
            v -= indexed
            self.add_edge(u, v)

    def build(self, root=0):
        self.depth[root] = 0
        st = [root]
        route = [root]
        while st:
            pos = st.pop()
            for npos in self.edges[pos]:
                if self.depth[npos] == -1:
                    self.depth[npos] = self.depth[pos] + 1
                    self.par[npos] = pos
                    st.append(npos)
                    route.append(npos)

        for pos in route[::-1]:
            self.size[pos] = 1
            ma = -1
            for npos in self.edges[pos]:
                if self.size[npos] != -1:
                    self.size[pos] += self.size[npos]
                    if self.size[npos] > ma:
                        ma = self.size[npos]
                        self.heavy_child[pos] = npos

            if ma != -1:
                self.isheavy[self.heavy_child[pos]] = True

        self.isheavy[root] = True

        path = 0
        st = [~root, root]
        self.path_root = [root]
        cc = 0
        while st:
            pos = st.pop()
            if pos >= 0:
                self.L[pos] = cc
                cc += 1
                if not self.isheavy[pos]:
                    path += 1
                    self.path_root.append(pos)

                self.path_ind[pos] = path
                for npos in self.edges[pos]:
                    if npos == self.par[pos] or npos == self.heavy_child[pos]:
                        continue
                    st.append(~npos)
                    st.append(npos)

                if self.heavy_child[pos] != -1:
                    npos = self.heavy_child[pos]
                    st.append(~npos)
                    st.append(npos)

            else:
                self.R[~pos] = cc

    def get_path(self, u, v):
        ll = [u]
        rr = [v]
        while self.path_ind[u] != self.path_ind[v]:
            if (
                self.depth[self.path_root[self.path_ind[u]]]
                >= self.depth[self.path_root[self.path_ind[v]]]
            ):
                u = self.path_root[self.path_ind[u]]
                ll.append(u)
                u = self.par[u]
                ll.append(u)
            else:
                v = self.path_root[self.path_ind[v]]
                rr.append(v)
                v = self.par[v]
                rr.append(v)

        ll += rr[::-1]
        res = []
        for i in range(0, len(ll), 2):
            res.append((ll[i], ll[i + 1]))

        return res

    def lca(self, u, v):
        while self.path_ind[u] != self.path_ind[v]:
            if (
                self.depth[self.path_root[self.path_ind[u]]]
                >= self.depth[self.path_root[self.path_ind[v]]]
            ):
                u = self.par[self.path_root[self.path_ind[u]]]
            else:
                v = self.par[self.path_root[self.path_ind[v]]]

        if self.depth[u] >= self.depth[v]:
            return v
        else:
            return u

    def dist(self, u, v):
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]

    def reorder(self, A, rev=False):
        ret = [0] * self.n
        for i in range(self.n):
            ret[self.L[i]] = A[i]

        if rev:
            ret = ret[::-1]
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


n, Q = map(int, input().split())
A = list(map(int, input().split()))
G = HLD(n)
G.read_edges(0)
G.build()
A = G.reorder(A)
bit = BIT(n)
for i, a in enumerate(A):
    bit.add(i, a)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        p, x = query[1:]
        bit.add(G.L[p], x)
    else:
        u, v = query[1:]
        ans = 0
        for l, r in G.get_path(u, v):
            l = G.L[l]
            r = G.L[r]
            if l > r:
                l, r = r, l
            ans += bit.sum(l, r + 1)
        print(ans)
