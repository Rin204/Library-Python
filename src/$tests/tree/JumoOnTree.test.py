# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.tree.LCA import LCA


n, Q = map(int, input().split())
G = LCA(n)
G.read_edges(0)
G.build()

for _ in range(Q):
    u, v, k = map(int, input().split())
    print(G.jump(u, v, k))
