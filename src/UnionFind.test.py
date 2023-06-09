# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind

from src.data_structure.UnionFind import UnionFind

n, Q = map(int, input().split())
UF = UnionFind(n)
ans = []
for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 0:
        UF.unite(x, y)
    else:
        if UF.same(x, y):
            ans.append(1)
        else:
            ans.append(0)

print(*ans, sep="\n")
