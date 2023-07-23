---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_path_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_path_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\nclass HLD:\n    def __init__(self, n, edges=None):\n        self.n = n\n \
    \       if edges is None:\n            self.edges = [[] for _ in range(n)]\n \
    \       else:\n            self.edges = edges\n            # \u30B3\u30D4\u30FC\
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
    \        return ret\n\n\nclass BIT:\n    def __init__(self, n):\n        self.n\
    \ = n\n        self.data = [0] * (n + 1)\n        if n == 0:\n            self.n0\
    \ = 0\n        else:\n            self.n0 = 1 << (n.bit_length() - 1)\n\n    def\
    \ sum_(self, i):\n        s = 0\n        while i > 0:\n            s += self.data[i]\n\
    \            i -= i & -i\n        return s\n\n    def sum(self, l, r=-1):\n  \
    \      if r == -1:\n            return self.sum_(l)\n        else:\n         \
    \   return self.sum_(r) - self.sum_(l)\n\n    def get(self, i):\n        return\
    \ self.sum(i, i + 1)\n\n    def add(self, i, x):\n        i += 1\n        while\
    \ i <= self.n:\n            self.data[i] += x\n            i += i & -i\n\n   \
    \ def lower_bound(self, x):\n        if x <= 0:\n            return 0\n      \
    \  i = 0\n        k = self.n0\n        while k > 0:\n            if i + k <= self.n\
    \ and self.data[i + k] < x:\n                x -= self.data[i + k]\n         \
    \       i += k\n            k //= 2\n        return i + 1\n\n\nn, Q = map(int,\
    \ input().split())\nA = list(map(int, input().split()))\nG = HLD(n)\nG.read_edges(0)\n\
    G.build()\nA = G.reorder(A)\nbit = BIT(n)\nfor i, a in enumerate(A):\n    bit.add(i,\
    \ a)\n\nfor _ in range(Q):\n    query = list(map(int, input().split()))\n    if\
    \ query[0] == 0:\n        p, x = query[1:]\n        bit.add(G.L[p], x)\n    else:\n\
    \        u, v = query[1:]\n        ans = 0\n        for l, r in G.get_path(u,\
    \ v):\n            l = G.L[l]\n            r = G.L[r]\n            if l > r:\n\
    \                l, r = r, l\n            ans += bit.sum(l, r + 1)\n        print(ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/tree/HLD.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/tree/HLD.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/tree/HLD.test.py
- /verify/expansion/$tests/tree/HLD.test.py.html
title: expansion/$tests/tree/HLD.test.py
---
