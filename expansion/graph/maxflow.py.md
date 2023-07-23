---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\n\n# from dataclasses import dataclass\n\n\n\
    class mf_graph:\n    # @dataclass\n    class edge:\n        # from_: int\n   \
    \     # to: int\n        # cap: int\n        # flow: int\n        def __init__(self,\
    \ from_, to, cap, flow):\n            self.from_ = from_\n            self.to\
    \ = to\n            self.cap = cap\n            self.flow = flow\n\n    # @dataclass\n\
    \    class _edge:\n        # to: int\n        # rev: int\n        # cap: int\n\
    \        def __init__(self, to, rev, cap):\n            self.to = to\n       \
    \     self.rev = rev\n            self.cap = cap\n\n    def __init__(self, n):\n\
    \        self.n = n\n        self.G = [[] for _ in range(n)]\n        self.pos\
    \ = []\n\n    def add_edge(self, from_, to, cap):\n        m = len(self.pos)\n\
    \        self.pos.append((from_, len(self.G[from_])))\n        from_id = len(self.G[from_])\n\
    \        to_id = len(self.G[to])\n        if from_ == to:\n            to_id +=\
    \ 1\n\n        self.G[from_].append(mf_graph._edge(to, to_id, cap))\n        self.G[to].append(mf_graph._edge(from_,\
    \ from_id, 0))\n        return m\n\n    def get_edge(self, i):\n        _e = self.G[self.pos[i][0]][self.pos[i][1]]\n\
    \        _re = self.G[_e.to][_e.rev]\n        return mf_graph.edge(self.pos[i][0],\
    \ _e.to, _e.cap + _re.cap, _re.cap)\n\n    def edges(self):\n        m = len(self.pos)\n\
    \        result = []\n        for i in range(m):\n            result.append(self.get_edge(i))\n\
    \n        return result\n\n    def change_edge(self, i, new_cap, new_flow):\n\
    \        _e = self.G[self.pos[i][0]][self.pos[i][1]]\n        self.G[_e.to][_e.rev].cap\
    \ = new_flow\n        self.G[self.pos[i][0]][self.pos[i][1]].cap = new_cap - new_flow\n\
    \n    def flow(self, s, t, flow_limit=1 << 60):\n        level = []\n        iter\
    \ = []\n        que = deque()\n\n        def bfs():\n            nonlocal level\n\
    \            level = [-1] * self.n\n            level[s] = 0\n            que.clear()\n\
    \            que.append(s)\n            while que:\n                v = que.popleft()\n\
    \                for e in self.G[v]:\n                    if e.cap == 0 or level[e.to]\
    \ >= 0:\n                        continue\n                    level[e.to] = level[v]\
    \ + 1\n                    if e.to == t:\n                        return\n   \
    \                 que.append(e.to)\n\n        def dfs(v, up):\n            if\
    \ v == s:\n                return up\n\n            nonlocal level, iter\n\n \
    \           res = 0\n            level_v = level[v]\n            while iter[v]\
    \ < len(self.G[v]):\n                i = iter[v]\n                iter[v] += 1\n\
    \                e = self.G[v][i]\n                if level_v <= level[e.to] or\
    \ self.G[e.to][e.rev].cap == 0:\n                    continue\n\n            \
    \    d = dfs(e.to, min(up - res, self.G[e.to][e.rev].cap))\n                if\
    \ d <= 0:\n                    continue\n\n                self.G[v][i].cap +=\
    \ d\n                self.G[e.to][e.rev].cap -= d\n                res += d\n\
    \                if res == up:\n                    return res\n\n           \
    \ level[v] = self.n\n            return res\n\n        flow = 0\n        while\
    \ flow < flow_limit:\n            bfs()\n            if level[t] == -1:\n    \
    \            break\n\n            iter = [0] * self.n\n            f = dfs(t,\
    \ flow_limit - flow)\n            if f == 0:\n                break\n        \
    \    flow += f\n\n        return flow\n\n    def min_cut(self, s):\n        visited\
    \ = [False] * self.n\n        que = deque()\n        que.append(s)\n        while\
    \ que:\n            p = que.popleft()\n            visited[p] = True\n       \
    \     for e in self.G[p]:\n                if e.cap and not visited[e.to]:\n \
    \                   visited[e.to] = True\n                    que.append(e.to)\n\
    \n        return visited\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/graph/maxflow.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/graph/maxflow.py
layout: document
redirect_from:
- /library/expansion/graph/maxflow.py
- /library/expansion/graph/maxflow.py.html
title: expansion/graph/maxflow.py
---
