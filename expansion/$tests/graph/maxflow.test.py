# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A&lang=jp
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from collections import deque

# from dataclasses import dataclass


class mf_graph:
    # @dataclass
    class edge:
        # from_: int
        # to: int
        # cap: int
        # flow: int
        def __init__(self, from_, to, cap, flow):
            self.from_ = from_
            self.to = to
            self.cap = cap
            self.flow = flow

    # @dataclass
    class _edge:
        # to: int
        # rev: int
        # cap: int
        def __init__(self, to, rev, cap):
            self.to = to
            self.rev = rev
            self.cap = cap

    def __init__(self, n):
        self.n = n
        self.G = [[] for _ in range(n)]
        self.pos = []

    def add_edge(self, from_, to, cap):
        m = len(self.pos)
        self.pos.append((from_, len(self.G[from_])))
        from_id = len(self.G[from_])
        to_id = len(self.G[to])
        if from_ == to:
            to_id += 1

        self.G[from_].append(mf_graph._edge(to, to_id, cap))
        self.G[to].append(mf_graph._edge(from_, from_id, 0))
        return m

    def get_edge(self, i):
        _e = self.G[self.pos[i][0]][self.pos[i][1]]
        _re = self.G[_e.to][_e.rev]
        return mf_graph.edge(self.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap)

    def edges(self):
        m = len(self.pos)
        result = []
        for i in range(m):
            result.append(self.get_edge(i))

        return result

    def change_edge(self, i, new_cap, new_flow):
        _e = self.G[self.pos[i][0]][self.pos[i][1]]
        self.G[_e.to][_e.rev].cap = new_flow
        self.G[self.pos[i][0]][self.pos[i][1]].cap = new_cap - new_flow

    def flow(self, s, t, flow_limit=1 << 60):
        level = []
        iter = []
        que = deque()

        def bfs():
            nonlocal level
            level = [-1] * self.n
            level[s] = 0
            que.clear()
            que.append(s)
            while que:
                v = que.popleft()
                for e in self.G[v]:
                    if e.cap == 0 or level[e.to] >= 0:
                        continue
                    level[e.to] = level[v] + 1
                    if e.to == t:
                        return
                    que.append(e.to)

        def dfs(v, up):
            if v == s:
                return up

            nonlocal level, iter

            res = 0
            level_v = level[v]
            while iter[v] < len(self.G[v]):
                i = iter[v]
                iter[v] += 1
                e = self.G[v][i]
                if level_v <= level[e.to] or self.G[e.to][e.rev].cap == 0:
                    continue

                d = dfs(e.to, min(up - res, self.G[e.to][e.rev].cap))
                if d <= 0:
                    continue

                self.G[v][i].cap += d
                self.G[e.to][e.rev].cap -= d
                res += d
                if res == up:
                    return res

            level[v] = self.n
            return res

        flow = 0
        while flow < flow_limit:
            bfs()
            if level[t] == -1:
                break

            iter = [0] * self.n
            f = dfs(t, flow_limit - flow)
            if f == 0:
                break
            flow += f

        return flow

    def min_cut(self, s):
        visited = [False] * self.n
        que = deque()
        que.append(s)
        while que:
            p = que.popleft()
            visited[p] = True
            for e in self.G[p]:
                if e.cap and not visited[e.to]:
                    visited[e.to] = True
                    que.append(e.to)

        return visited


n, m = map(int, input().split())
G = mf_graph(n)
for _ in range(m):
    u, v, c = map(int, input().split())
    G.add_edge(u, v, c)

print(G.flow(0, n - 1))
