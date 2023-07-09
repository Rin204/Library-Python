class SCC:
    def __init__(self, n, edges=None):
        self.n = n
        if edges is None:
            self.edges = []
        else:
            self.edges = edges

    def add_edge(self, u, v):
        self.edges.append((u, v))

    def read_edges(self, m, indexed=1):
        for _ in range(m):
            u, v = map(int, input().split())
            u -= indexed
            v -= indexed
            self.add_edge(u, v)

    def build(self):
        start = [0] * (self.n + 1)
        elist = [0] * len(self.edges)
        for u, _ in self.edges:
            start[u + 1] += 1
        for i in range(1, self.n + 1):
            start[i] += start[i - 1]

        counter = start[:]
        for u, v in self.edges:
            elist[counter[u]] = v
            counter[u] += 1

        now_ord = 0
        group_num = 0
        visited = []
        low = [0] * self.n
        ord = [-1] * self.n
        ids = [0] * self.n
        bpos = [-1] * self.n

        def dfs(v):
            nonlocal now_ord, group_num

            visited.append(v)
            stack = [~v, v]
            while stack:
                pos = stack.pop()
                if pos >= 0:
                    if ord[pos] == -1:
                        low[pos] = ord[pos] = now_ord
                        now_ord += 1
                        visited.append(pos)
                        for i in range(start[pos], start[pos + 1]):
                            to = elist[i]
                            if ord[to] == -1:
                                stack.append(~to)
                                stack.append(to)
                                bpos[to] = pos
                            else:
                                low[pos] = min(low[pos], ord[to])
                else:
                    pos = ~pos
                    if low[pos] == ord[pos]:
                        while 1:
                            u = visited.pop()
                            ord[u] = self.n
                            ids[u] = group_num
                            if u == pos:
                                break
                        group_num += 1
                    if bpos[pos] != -1:
                        low[bpos[pos]] = min(low[bpos[pos]], low[pos])

        for i in range(self.n):
            if ord[i] == -1:
                dfs(i)

        for i in range(self.n):
            ids[i] = group_num - 1 - ids[i]

        return group_num, ids
