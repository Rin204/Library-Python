import heapq

from dataclasses import dataclass


class mcf_graph:
    @dataclass
    class edge:
        from_: int
        to: int
        cap: int
        flow: int
        cost: int
        # def __init__(self, from_, to, cap, flow, cost):
        #     self.from_ = from_
        #     self.to = to
        #     self.cap = cap
        #     self.flow = flow
        #     self.cost = cost

    @dataclass
    class _edge:
        to: int
        rev: int
        cap: int
        cost: int
        # def __init__(self, to, rev, cap, cost):
        #     self.to = to
        #     self.rev = rev
        #     self.cap = cap
        #     self.cost = cost

    def __init__(self, n, inf=1 << 60):
        self.n = n
        self._edges = []
        self.inf = inf

    def add_edge(self, from_, to, cap, cost):
        m = len(self._edges)
        self._edges.append(mcf_graph.edge(from_, to, cap, 0, cost))
        return m

    def get_edge(self, i):
        return self._edges[i]

    def edges(self):
        return self._edges

    def flow(self, s, t, flow_limit=1 << 60):
        return self.slope(s, t, flow_limit)[-1]

    class csr:
        def __init__(self, n, elist):
            self.start = [0] * (n + 1)
            self.elist = [None] * len(elist)
            for e in elist:
                self.start[e[0] + 1] += 1
            for i in range(1, n + 1):
                self.start[i] += self.start[i - 1]
            counter = self.start[:]
            for e in elist:
                self.elist[counter[e[0]]] = mcf_graph._edge(e[1].to, e[1].rev, e[1].cap, e[1].cost)
                counter[e[0]] += 1

    def slope(self, s, t, flow_limit=1 << 60):
        m = len(self._edges)
        edge_idx = [0] * m

        degree = [0] * self.n
        redge_idx = [0] * m
        elist = [0] * (2 * m)
        for i in range(m):
            e = self._edges[i]
            edge_idx[i] = degree[e.from_]
            degree[e.from_] += 1
            redge_idx[i] = degree[e.to]
            degree[e.to] += 1
            elist[2 * i] = (e.from_, mcf_graph._edge(e.to, -1, e.cap - e.flow, e.cost))
            elist[2 * i + 1] = (e.to, mcf_graph._edge(e.from_, -1, e.flow, -e.cost))

        g = mcf_graph.csr(self.n, elist)
        for i in range(m):
            e = self._edges[i]
            edge_idx[i] += g.start[e.from_]
            redge_idx[i] += g.start[e.to]
            g.elist[edge_idx[i]].rev = redge_idx[i]
            g.elist[redge_idx[i]].rev = edge_idx[i]

        result = self._slope(g, s, t, flow_limit)

        for i in range(m):
            e = g.elist[edge_idx[i]]
            self._edges[i].flow = self._edges[i].cap - e.cap

        return result

    def _slope(self, g, s, t, flow_limit):
        dual_dist = [[0, 0] for _ in range(self.n)]
        prev_e = [None] * self.n
        vis = [False] * self.n

        que_min = []
        que = []

        def dual_ref():
            for i in range(self.n):
                dual_dist[i][1] = self.inf

            nonlocal vis, que_min, que
            vis = [False] * self.n
            que = []
            que_min = [s]

            dual_dist[s][1] = 0
            while que_min or que:
                if que_min:
                    v = que_min.pop()
                else:
                    v = heapq.heappop(que)[1]
                if vis[v]:
                    continue
                vis[v] = True
                if v == t:
                    break

                dual_v, dist_v = dual_dist[v]

                for i in range(g.start[v], g.start[v + 1]):
                    e = g.elist[i]
                    if e.cap == 0:
                        continue
                    cost = e.cost - dual_dist[e.to][0] + dual_v
                    if dual_dist[e.to][1] - dist_v > cost:
                        dist_to = dist_v + cost
                        dual_dist[e.to][1] = dist_to
                        prev_e[e.to] = e.rev

                        if dist_to == dist_v:
                            heapq.heappush(que_min, e.to)
                        else:
                            heapq.heappush(que, (dist_to, e.to))

            if not vis[t]:
                return False

            for v in range(self.n):
                if not vis[v]:
                    continue
                dual_dist[v][0] -= dual_dist[t][1] - dual_dist[v][1]

            return True

        flow = 0
        cost = 0
        prev_cost_per_flow = -1
        result = [(0, 0)]

        while flow < flow_limit:
            if not dual_ref():
                break
            c = flow_limit - flow
            v = t
            while v != s:
                c = min(c, g.elist[g.elist[prev_e[v]].rev].cap)
                v = g.elist[prev_e[v]].to

            v = t
            while v != s:
                e = g.elist[prev_e[v]]
                g.elist[prev_e[v]].cap += c
                g.elist[e.rev].cap -= c
                v = e.to

            d = -dual_dist[s][0]
            flow += c
            cost += c * d
            if prev_cost_per_flow == d:
                result.pop()
            result.append((flow, cost))
            prev_cost_per_flow = d

        return result
