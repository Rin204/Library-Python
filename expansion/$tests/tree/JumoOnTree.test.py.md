---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/jump_on_tree
    links:
    - https://judge.yosupo.jp/problem/jump_on_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\nclass LCA:\n    def __init__(self, n, root=0, edges=None):\n        self.n\
    \ = n\n        self.root = root\n        self.logn = (self.n - 1).bit_length()\n\
    \        if edges is None:\n            self.edges = [[] for _ in range(n)]\n\
    \        else:\n            self.edges = edges\n            # \u30B3\u30D4\u30FC\
    \u3057\u3066\u306A\u3044\u306E\u3067\u6CE8\u610F\n\n        self.depth = [-1]\
    \ * n\n        self.par = [[-1] * n for _ in range(self.logn)]\n\n    def build(self):\n\
    \        self.depth[self.root] = 0\n        stack = [self.root]\n        while\
    \ stack:\n            pos = stack.pop()\n            for npos in self.edges[pos]:\n\
    \                if self.depth[npos] == -1:\n                    self.depth[npos]\
    \ = self.depth[pos] + 1\n                    stack.append(npos)\n            \
    \        self.par[0][npos] = pos\n\n        for i in range(1, self.logn):\n  \
    \          for j in range(self.n):\n                if self.par[i - 1][j] != -1:\n\
    \                    self.par[i][j] = self.par[i - 1][self.par[i - 1][j]]\n\n\
    \    def add_edge(self, u, v):\n        self.edges[u].append(v)\n        self.edges[v].append(u)\n\
    \n    def read_edges(self, indexed=1):\n        for _ in range(self.n - 1):\n\
    \            u, v = map(int, input().split())\n            u -= indexed\n    \
    \        v -= indexed\n            self.add_edge(u, v)\n\n    def lca(self, u,\
    \ v):\n        if self.depth[u] > self.depth[v]:\n            u, v = v, u\n\n\
    \        d = self.depth[v] - self.depth[u]\n        i = 0\n        while d > 0:\n\
    \            if d & 1:\n                v = self.par[i][v]\n            i += 1\n\
    \            d >>= 1\n\n        if u == v:\n            return u\n\n        d\
    \ = self.depth[u]\n        logn = (d - 1).bit_length()\n        for i in range(logn\
    \ - 1, -1, -1):\n            pu = self.par[i][u]\n            pv = self.par[i][v]\n\
    \            if pu != pv:\n                u = pu\n                v = pv\n\n\
    \        return self.par[0][u]\n\n    def dist(self, u, v):\n        return self.depth[u]\
    \ + self.depth[v] - 2 * self.depth[self.lca(u, v)]\n\n    def jump(self, u, v,\
    \ k):\n        if k == 0:\n            return u\n\n        p = self.lca(u, v)\n\
    \        du = self.depth[u] - self.depth[p]\n        dv = self.depth[v] - self.depth[p]\n\
    \        if du + dv < k:\n            return -1\n        if k <= du:\n       \
    \     d = k\n        else:\n            u = v\n            d = du + dv - k\n\n\
    \        i = 0\n        while d > 0:\n            if d & 1:\n                u\
    \ = self.par[i][u]\n            i += 1\n            d >>= 1\n\n        return\
    \ u\n\n\nn, Q = map(int, input().split())\nG = LCA(n)\nG.read_edges(0)\nG.build()\n\
    \nfor _ in range(Q):\n    u, v, k = map(int, input().split())\n    print(G.jump(u,\
    \ v, k))\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/tree/JumoOnTree.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/tree/JumoOnTree.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/tree/JumoOnTree.test.py
- /verify/expansion/$tests/tree/JumoOnTree.test.py.html
title: expansion/$tests/tree/JumoOnTree.test.py
---
