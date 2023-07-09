# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_sat
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.math.TwoSAT import TwoSAT


_, _, n, m = input().split()
n = int(n)
m = int(m)
G = TwoSAT(n)
for _ in range(m):
    a, b, _ = map(int, input().split())
    G.add_clause(abs(a) - 1, a > 0, abs(b) - 1, b > 0)

if G.check():
    print("s SATISFIABLE")
    res = G.assign()
    ans = ["v"]
    for i, r in enumerate(res, 1):
        if r:
            ans.append(i)
        else:
            ans.append(-i)
    ans.append(0)
    print(*ans)
else:
    print("s UNSATISFIABLE")
