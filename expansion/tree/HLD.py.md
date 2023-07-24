---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class HLD:\n    def __init__(self, n, edges=None):\n        self.n = n\n\
    \        if edges is None:\n            self.edges = [[] for _ in range(n)]\n\
    \        else:\n            self.edges = edges\n            # \u30B3\u30D4\u30FC\
    \u3057\u3066\u306A\u3044\u306E\u3067\u6CE8\u610F\n\n        self.size = [-1] *\
    \ n\n        self.par = [-1] * n\n        self.depth = [-1] * n\n        self.path_ind\
    \ = [-1] * n\n        self.path_root = []\n        self.heavy_child = [-1] * n\n\
    \        self.isheavy = [False] * n\n        self.L = [-1] * n\n        self.R\
    \ = [-1] * n\n\n    def add_edge(self, u, v):\n        self.edges[u].append(v)\n\
    \        self.edges[v].append(u)\n\n    def read_edges(self, indexed=1):\n   \
    \     for _ in range(self.n - 1):\n            u, v = map(int, input().split())\n\
    \            u -= indexed\n            v -= indexed\n            self.add_edge(u,\
    \ v)\n\n    def build(self, root=0):\n        self.depth[root] = 0\n        st\
    \ = [root]\n        route = [root]\n        while st:\n            pos = st.pop()\n\
    \            for npos in self.edges[pos]:\n                if self.depth[npos]\
    \ == -1:\n                    self.depth[npos] = self.depth[pos] + 1\n       \
    \             self.par[npos] = pos\n                    st.append(npos)\n    \
    \                route.append(npos)\n\n        for pos in route[::-1]:\n     \
    \       self.size[pos] = 1\n            ma = -1\n            for npos in self.edges[pos]:\n\
    \                if self.size[npos] != -1:\n                    self.size[pos]\
    \ += self.size[npos]\n                    if self.size[npos] > ma:\n         \
    \               ma = self.size[npos]\n                        self.heavy_child[pos]\
    \ = npos\n\n            if ma != -1:\n                self.isheavy[self.heavy_child[pos]]\
    \ = True\n\n        self.isheavy[root] = True\n\n        path = 0\n        st\
    \ = [~root, root]\n        self.path_root = [root]\n        cc = 0\n        while\
    \ st:\n            pos = st.pop()\n            if pos >= 0:\n                self.L[pos]\
    \ = cc\n                cc += 1\n                if not self.isheavy[pos]:\n \
    \                   path += 1\n                    self.path_root.append(pos)\n\
    \n                self.path_ind[pos] = path\n                for npos in self.edges[pos]:\n\
    \                    if npos == self.par[pos] or npos == self.heavy_child[pos]:\n\
    \                        continue\n                    st.append(~npos)\n    \
    \                st.append(npos)\n\n                if self.heavy_child[pos] !=\
    \ -1:\n                    npos = self.heavy_child[pos]\n                    st.append(~npos)\n\
    \                    st.append(npos)\n\n            else:\n                self.R[~pos]\
    \ = cc\n\n    def get_path(self, u, v):\n        ll = [u]\n        rr = [v]\n\
    \        while self.path_ind[u] != self.path_ind[v]:\n            if (\n     \
    \           self.depth[self.path_root[self.path_ind[u]]]\n                >= self.depth[self.path_root[self.path_ind[v]]]\n\
    \            ):\n                u = self.path_root[self.path_ind[u]]\n      \
    \          ll.append(u)\n                u = self.par[u]\n                ll.append(u)\n\
    \            else:\n                v = self.path_root[self.path_ind[v]]\n   \
    \             rr.append(v)\n                v = self.par[v]\n                rr.append(v)\n\
    \n        ll += rr[::-1]\n        res = []\n        for i in range(0, len(ll),\
    \ 2):\n            res.append((ll[i], ll[i + 1]))\n\n        return res\n\n  \
    \  def lca(self, u, v):\n        while self.path_ind[u] != self.path_ind[v]:\n\
    \            if (\n                self.depth[self.path_root[self.path_ind[u]]]\n\
    \                >= self.depth[self.path_root[self.path_ind[v]]]\n           \
    \ ):\n                u = self.par[self.path_root[self.path_ind[u]]]\n       \
    \     else:\n                v = self.par[self.path_root[self.path_ind[v]]]\n\n\
    \        if self.depth[u] >= self.depth[v]:\n            return v\n        else:\n\
    \            return u\n\n    def dist(self, u, v):\n        return self.depth[u]\
    \ + self.depth[v] - 2 * self.depth[self.lca(u, v)]\n\n    def reorder(self, A,\
    \ rev=False):\n        ret = [0] * self.n\n        for i in range(self.n):\n \
    \           ret[self.L[i]] = A[i]\n\n        if rev:\n            ret = ret[::-1]\n\
    \        return ret\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/tree/HLD.py
  requiredBy: []
  timestamp: '2023-07-08 17:00:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/tree/HLD.py
layout: document
redirect_from:
- /library/expansion/tree/HLD.py
- /library/expansion/tree/HLD.py.html
title: expansion/tree/HLD.py
---
