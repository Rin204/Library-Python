def bellmanFord(n, edges, s, inf=1 << 60):
    """
    edges = [(from1, to1, cost1), (from2, to2, cost2), ...)]
    """
    dist = [inf] * n
    dist[s] = 0

    for _ in range(n):
        update = False
        for u, v, d in edges:
            if dist[u] != inf and dist[v] > dist[u] + d:
                dist[v] = dist[u] + d
                update = True

        if not update:
            return dist

    return None
