---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B&lang=ja\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    import heapq\n\n# from dataclasses import dataclass\n\n\nclass mcf_graph:\n  \
    \  # @dataclass\n    class edge:\n        # from_: int\n        # to: int\n  \
    \      # cap: int\n        # flow: int\n        def __init__(self, from_, to,\
    \ cap, flow, cost):\n            self.from_ = from_\n            self.to = to\n\
    \            self.cap = cap\n            self.flow = flow\n            self.cost\
    \ = cost\n\n    # @dataclass\n    class _edge:\n        # to: int\n        # rev:\
    \ int\n        # cap: int\n        # cost: int\n        def __init__(self, to,\
    \ rev, cap, cost):\n            self.to = to\n            self.rev = rev\n   \
    \         self.cap = cap\n            self.cost = cost\n\n    def __init__(self,\
    \ n, inf=1 << 60):\n        self.n = n\n        self._edges = []\n        self.inf\
    \ = inf\n\n    def add_edge(self, from_, to, cap, cost):\n        m = len(self._edges)\n\
    \        self._edges.append(mcf_graph.edge(from_, to, cap, 0, cost))\n       \
    \ return m\n\n    def get_edge(self, i):\n        return self._edges[i]\n\n  \
    \  def edges(self):\n        return self._edges\n\n    def flow(self, s, t, flow_limit=1\
    \ << 60):\n        return self.slope(s, t, flow_limit)[-1]\n\n    class csr:\n\
    \        def __init__(self, n, elist):\n            self.start = [0] * (n + 1)\n\
    \            self.elist = [None] * len(elist)\n            for e in elist:\n \
    \               self.start[e[0] + 1] += 1\n            for i in range(1, n + 1):\n\
    \                self.start[i] += self.start[i - 1]\n            counter = self.start[:]\n\
    \            for e in elist:\n                self.elist[counter[e[0]]] = mcf_graph._edge(e[1].to,\
    \ e[1].rev, e[1].cap, e[1].cost)\n                counter[e[0]] += 1\n\n    def\
    \ slope(self, s, t, flow_limit=1 << 60):\n        m = len(self._edges)\n     \
    \   edge_idx = [0] * m\n\n        degree = [0] * self.n\n        redge_idx = [0]\
    \ * m\n        elist = [0] * (2 * m)\n        for i in range(m):\n           \
    \ e = self._edges[i]\n            edge_idx[i] = degree[e.from_]\n            degree[e.from_]\
    \ += 1\n            redge_idx[i] = degree[e.to]\n            degree[e.to] += 1\n\
    \            elist[2 * i] = (e.from_, mcf_graph._edge(e.to, -1, e.cap - e.flow,\
    \ e.cost))\n            elist[2 * i + 1] = (e.to, mcf_graph._edge(e.from_, -1,\
    \ e.flow, -e.cost))\n\n        g = mcf_graph.csr(self.n, elist)\n        for i\
    \ in range(m):\n            e = self._edges[i]\n            edge_idx[i] += g.start[e.from_]\n\
    \            redge_idx[i] += g.start[e.to]\n            g.elist[edge_idx[i]].rev\
    \ = redge_idx[i]\n            g.elist[redge_idx[i]].rev = edge_idx[i]\n\n    \
    \    result = self._slope(g, s, t, flow_limit)\n\n        for i in range(m):\n\
    \            e = g.elist[edge_idx[i]]\n            self._edges[i].flow = self._edges[i].cap\
    \ - e.cap\n\n        return result\n\n    def _slope(self, g, s, t, flow_limit):\n\
    \        dual_dist = [[0, 0] for _ in range(self.n)]\n        prev_e = [None]\
    \ * self.n\n        vis = [False] * self.n\n\n        que_min = []\n        que\
    \ = []\n\n        def dual_ref():\n            for i in range(self.n):\n     \
    \           dual_dist[i][1] = self.inf\n\n            nonlocal vis, que_min, que\n\
    \            vis = [False] * self.n\n            que = []\n            que_min\
    \ = [s]\n\n            dual_dist[s][1] = 0\n            while que_min or que:\n\
    \                if que_min:\n                    v = que_min.pop()\n        \
    \        else:\n                    v = heapq.heappop(que)[1]\n              \
    \  if vis[v]:\n                    continue\n                vis[v] = True\n \
    \               if v == t:\n                    break\n\n                dual_v,\
    \ dist_v = dual_dist[v]\n\n                for i in range(g.start[v], g.start[v\
    \ + 1]):\n                    e = g.elist[i]\n                    if e.cap ==\
    \ 0:\n                        continue\n                    cost = e.cost - dual_dist[e.to][0]\
    \ + dual_v\n                    if dual_dist[e.to][1] - dist_v > cost:\n     \
    \                   dist_to = dist_v + cost\n                        dual_dist[e.to][1]\
    \ = dist_to\n                        prev_e[e.to] = e.rev\n\n                \
    \        if dist_to == dist_v:\n                            heapq.heappush(que_min,\
    \ e.to)\n                        else:\n                            heapq.heappush(que,\
    \ (dist_to, e.to))\n\n            if not vis[t]:\n                return False\n\
    \n            for v in range(self.n):\n                if not vis[v]:\n      \
    \              continue\n                dual_dist[v][0] -= dual_dist[t][1] -\
    \ dual_dist[v][1]\n\n            return True\n\n        flow = 0\n        cost\
    \ = 0\n        prev_cost_per_flow = -1\n        result = [(0, 0)]\n\n        while\
    \ flow < flow_limit:\n            if not dual_ref():\n                break\n\
    \            c = flow_limit - flow\n            v = t\n            while v !=\
    \ s:\n                c = min(c, g.elist[g.elist[prev_e[v]].rev].cap)\n      \
    \          v = g.elist[prev_e[v]].to\n\n            v = t\n            while v\
    \ != s:\n                e = g.elist[prev_e[v]]\n                g.elist[prev_e[v]].cap\
    \ += c\n                g.elist[e.rev].cap -= c\n                v = e.to\n\n\
    \            d = -dual_dist[s][0]\n            flow += c\n            cost +=\
    \ c * d\n            if prev_cost_per_flow == d:\n                result.pop()\n\
    \            result.append((flow, cost))\n            prev_cost_per_flow = d\n\
    \n        return result\n\n\nn, m, f = map(int, input().split())\nG = mcf_graph(n)\n\
    for _ in range(m):\n    G.add_edge(*map(int, input().split()))\n\nfl, c = G.flow(0,\
    \ n - 1, f)\nif fl < f:\n    c = -1\n\nprint(c)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/graph/mincostflow.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/graph/mincostflow.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/graph/mincostflow.test.py
- /verify/expansion/$tests/graph/mincostflow.test.py.html
title: expansion/$tests/graph/mincostflow.test.py
---
