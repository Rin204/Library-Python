---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/1038
    links:
    - https://yukicoder.me/problems/no/1038
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/1038\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n## yukicoder \u306E\u30AA\u30F3\u30E9\u30A4\u30F3\u5B9F\u884C\u3060\u3068TL\u306B\
    \u9593\u306B\u5408\u3063\u305F\u308A\u9593\u306B\u5408\u308F\u306A\u304B\u3063\
    \u305F\u308A\u3059\u308B\n\n\nclass CentroidDecomposition:\n    def __init__(self,\
    \ n, edges=None):\n        self.n = n\n        self.par = [-1] * n  # \u91CD\u5FC3\
    \u5206\u89E3\u6728\u306E\u89AA\n        self.depth = [-1] * n  # \u91CD\u5FC3\u5206\
    \u89E3\u6728\u306E\u6DF1\u3055\n        self.size = [-1] * n  # \u91CD\u5FC3\u5206\
    \u89E3\u6728\u306E\u90E8\u5206\u6728\u306E\u30B5\u30A4\u30BA\n        self.childcnt\
    \ = [0] * n  # \u91CD\u5FC3\u5206\u89E3\u6728\u306E\u5B50\u306E\u6570\n      \
    \  if edges is None:\n            self.edges = [[] for _ in range(n)]\n      \
    \  else:\n            self.edges = edges\n            # \u30B3\u30D4\u30FC\u3057\
    \u3066\u306A\u3044\u306E\u3067\u6CE8\u610F\n\n        self.centroids = []  # centroids[i]\
    \ := \u6DF1\u3055\u304C i \u306E\u91CD\u5FC3\u306E\u30EA\u30B9\u30C8\n       \
    \ self.treeind = []  # treeind[j * logn + i] := \u9802\u70B9 j \u304C\u6DF1\u3055\
    \ i \u306E\u91CD\u5FC3\u306E\u4F55\u756A\u76EE\u306E\u90E8\u5206\u6728\u304B\n\
    \        self.cent_dist = []  # cent_dist[j * logn + i] := \u9802\u70B9 j \u304C\
    \u6DF1\u3055 i \u306E\u91CD\u5FC3\u304B\u3089\u306E\u8DDD\u96E2\n\n    def add_edge(self,\
    \ u, v):\n        self.edges[u].append(v)\n        self.edges[v].append(u)\n\n\
    \    def read_edges(self, indexed=1):\n        for _ in range(self.n - 1):\n \
    \           u, v = map(int, input().split())\n            u -= indexed\n     \
    \       v -= indexed\n            self.add_edge(u, v)\n\n    def build(self):\n\
    \        stack = [(0, -1, 0, -1)]\n        while stack:\n            pos, bpos,\
    \ d, c = stack.pop()\n            st = [pos]\n            route = []\n       \
    \     sz = 0\n\n            if len(self.treeind) == d * self.n:\n            \
    \    self.treeind += [-1] * self.n\n                self.cent_dist += [-1] * self.n\n\
    \                self.centroids.append([])\n            if d >= 1:\n         \
    \       self.cent_dist[(d - 1) * self.n + pos] = 1\n\n            while st:\n\
    \                pos = st.pop()\n                self.depth[pos] = -2\n      \
    \          route.append(pos)\n                sz += 1\n                if d >=\
    \ 1:\n                    self.treeind[(d - 1) * self.n + pos] = c\n\n       \
    \         for npos in self.edges[pos]:\n                    if self.depth[npos]\
    \ == -1:\n                        st.append(npos)\n                        if\
    \ d >= 1:\n                            self.cent_dist[(d - 1) * self.n + npos]\
    \ = (\n                                self.cent_dist[(d - 1) * self.n + pos]\
    \ + 1\n                            )\n\n            g = -1\n            for pos\
    \ in route[::-1]:\n                self.size[pos] = 1\n                self.depth[pos]\
    \ = -1\n                if g != -1:\n                    continue\n          \
    \      isg = True\n                for npos in self.edges[pos]:\n            \
    \        if self.depth[npos] == -1:\n                        self.size[pos] +=\
    \ self.size[npos]\n                        if self.size[npos] * 2 > sz:\n    \
    \                        isg = False\n                            break\n\n  \
    \              if isg and 2 * self.size[pos] >= sz:\n                    g = pos\n\
    \n            self.centroids[d].append(g)\n\n            self.size[g] = sz\n \
    \           self.par[g] = bpos\n            self.depth[g] = d\n            self.cent_dist[d\
    \ * self.n + g] = 0\n\n            if sz != 1:\n                c = 0\n      \
    \          for npos in self.edges[g]:\n                    if self.depth[npos]\
    \ == -1:\n                        stack.append((npos, g, d + 1, c))\n        \
    \                c += 1\n                self.childcnt[g] = c\n\n        self.logn\
    \ = len(self.centroids)\n        nex = [0] * (self.n * self.logn)\n        for\
    \ i in range(self.n):\n            for j in range(self.logn):\n              \
    \  nex[i * self.logn + j] = self.cent_dist[j * self.n + i]\n\n        self.cent_dist,\
    \ nex = nex, self.cent_dist\n\n        for i in range(self.n):\n            for\
    \ j in range(self.logn):\n                nex[i * self.logn + j] = self.treeind[j\
    \ * self.n + i]\n\n        self.treeind = nex\n\n    def cent_ind_dist(self, u):\n\
    \        \"\"\"\n        u + u \u306E\u5404\u5148\u7956\u306E {\u9802\u70B9\u756A\
    \u53F7, \u8DDD\u96E2} \u3092\u8FD4\u3059\n        \"\"\"\n\n        ret = [(u,\
    \ 0)]\n        v = u\n        p = u * self.logn + self.depth[u] - 1\n        for\
    \ d in range(self.depth[u] - 1, -1, -1):\n            v = self.par[v]\n      \
    \      ret.append((v, self.cent_dist[p]))\n            p -= 1\n\n        return\
    \ ret\n\n\nclass BIT:\n    def __init__(self, n):\n        self.n = n\n      \
    \  self.data = [0] * (n + 1)\n        if n == 0:\n            self.n0 = 0\n  \
    \      else:\n            self.n0 = 1 << (n.bit_length() - 1)\n\n    def sum_(self,\
    \ i):\n        s = 0\n        while i > 0:\n            s += self.data[i]\n  \
    \          i -= i & -i\n        return s\n\n    def sum(self, l, r=-1):\n    \
    \    if r == -1:\n            return self.sum_(l)\n        else:\n           \
    \ return self.sum_(r) - self.sum_(l)\n\n    def get(self, i):\n        return\
    \ self.sum(i, i + 1)\n\n    def add(self, i, x):\n        i += 1\n        while\
    \ i <= self.n:\n            self.data[i] += x\n            i += i & -i\n\n   \
    \ def lower_bound(self, x):\n        if x <= 0:\n            return 0\n      \
    \  i = 0\n        k = self.n0\n        while k > 0:\n            if i + k <= self.n\
    \ and self.data[i + k] < x:\n                x -= self.data[i + k]\n         \
    \       i += k\n            k //= 2\n        return i + 1\n\n\nimport sys\n\n\
    input = sys.stdin.readline\n\n\nn, Q = map(int, input().split())\nG = CentroidDecomposition(n)\n\
    G.read_edges()\nG.build()\nlogn = len(G.centroids)\nbit = []\nsubbit = []\nL =\
    \ [0] * n\nsubL = [0] * n\n\nfor d in range(logn):\n    c = 0\n    c2 = 0\n  \
    \  for g in G.centroids[d]:\n        L[g] = c\n        if d != 0:\n          \
    \  subL[g] = c2\n        c += G.size[g]\n        c2 += G.size[g] + 1\n    bit.append(BIT(c))\n\
    \    if d != 0:\n        subbit.append(BIT(c2))\n\n\ndef add(x, y, z):\n    bg\
    \ = -1\n    for g, d in G.cent_ind_dist(x):\n        dd = y - d\n        if dd\
    \ >= 0:\n            bit[G.depth[g]].add(L[g], z)\n            bit[G.depth[g]].add(L[g]\
    \ + min(dd + 1, G.size[g]), -z)\n            if bg != -1:\n                subbit[G.depth[g]].add(subL[bg]\
    \ + 1, z)\n                subbit[G.depth[g]].add(subL[bg] + min(dd + 1, G.size[bg]\
    \ + 1), -z)\n        bg = g\n\n\ndef get(x):\n    bg = -1\n    ret = 0\n    for\
    \ g, d in G.cent_ind_dist(x):\n        ret += bit[G.depth[g]].sum(L[g] + d + 1)\n\
    \        if bg != -1:\n            ret -= subbit[G.depth[g]].sum(subL[bg] + d\
    \ + 1)\n        bg = g\n\n    return ret\n\n\nout = []\nfor _ in range(Q):\n \
    \   x, y, z = map(int, input().split())\n    x -= 1\n    out.append(get(x))\n\
    \    add(x, y, z)\n\nprint(*out, sep=\"\\n\")\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/tree/CentroidDecomposition.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/tree/CentroidDecomposition.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/tree/CentroidDecomposition.test.py
- /verify/expansion/$tests/tree/CentroidDecomposition.test.py.html
title: expansion/$tests/tree/CentroidDecomposition.test.py
---
