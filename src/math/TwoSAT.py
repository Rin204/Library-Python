from src.graph.SCC import SCC


class TwoSAT:
    def __init__(self, n):
        self.n = n
        self.scc = SCC(2 * n)
        self._build = False

    def add_clause(self, i, pos_i, j, pos_j):
        """
        a V b
        pos_i = True -> a = i,
        pos_i = False -> a = ¬i
        """
        i0 = i
        i1 = i + self.n
        if not pos_i:
            i0, i1 = i1, i0

        j0 = j
        j1 = j + self.n
        if not pos_j:
            j0, j1 = j1, j0

        self.scc.add_edge(i1, j0)
        self.scc.add_edge(j1, i0)

    def check(self):
        _, self.ids = self.scc.build()

        for i in range(self.n):
            if self.ids[i] == self.ids[i + self.n]:
                return False
        return True

    def assign(self):
        ret = [False] * self.n
        for i in range(self.n):
            if self.ids[i] > self.ids[i + self.n]:
                ret[i] = True

        return ret
