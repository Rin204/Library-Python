from src.data_structure.UnionFind import UnionFind


def Kruskal(n, edges, is_sorted=False):
    if n == 1:
        return 0
    if not is_sorted:
        edges.sort(key=lambda x: x[2])
    UF = UnionFind(n)
    res = 0
    for u, v, cost in edges:
        if UF.unite(u, v):
            res += cost
            if UF.group == 1:
                return res
    return -1
