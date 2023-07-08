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
