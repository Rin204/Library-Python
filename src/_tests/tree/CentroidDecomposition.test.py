# verification-helper: PROBLEM https://yukicoder.me/problems/no/1038
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

## yukicoder のオンライン実行だとTLに間に合ったり間に合わなかったりする

from src.tree.CentroidDecomposition import CentroidDecomposition
from src.data_structure.BIT import BIT
import sys

input = sys.stdin.readline


n, Q = map(int, input().split())
G = CentroidDecomposition(n)
G.read_edges()
G.build()
logn = len(G.centroids)
bit = []
subbit = []
L = [0] * n
subL = [0] * n

for d in range(logn):
    c = 0
    c2 = 0
    for g in G.centroids[d]:
        L[g] = c
        if d != 0:
            subL[g] = c2
        c += G.size[g]
        c2 += G.size[g] + 1
    bit.append(BIT(c))
    if d != 0:
        subbit.append(BIT(c2))


def add(x, y, z):
    bg = -1
    for g, d in G.cent_ind_dist(x):
        dd = y - d
        if dd >= 0:
            bit[G.depth[g]].add(L[g], z)
            bit[G.depth[g]].add(L[g] + min(dd + 1, G.size[g]), -z)
            if bg != -1:
                subbit[G.depth[g]].add(subL[bg] + 1, z)
                subbit[G.depth[g]].add(subL[bg] + min(dd + 1, G.size[bg] + 1), -z)
        bg = g


def get(x):
    bg = -1
    ret = 0
    for g, d in G.cent_ind_dist(x):
        ret += bit[G.depth[g]].sum(L[g] + d + 1)
        if bg != -1:
            ret -= subbit[G.depth[g]].sum(subL[bg] + d + 1)
        bg = g

    return ret


out = []
for _ in range(Q):
    x, y, z = map(int, input().split())
    x -= 1
    out.append(get(x))
    add(x, y, z)

print(*out, sep="\n")
