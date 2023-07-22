# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=CGL_4_A&lang=ja
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.geometry.convex_hull import convex_hull


n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
res = convex_hull(xy, True)
print(len(res))
for x, y in res:
    print(x, y)
