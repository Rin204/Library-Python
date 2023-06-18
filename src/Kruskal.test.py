# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A

from src.tree.Kruskal import Kruskal

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
print(Kruskal(n, edges))
