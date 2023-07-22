# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sort_points_by_argument
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.geometry.arg_sort import arg_sort


n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
xy = arg_sort(xy)
for x, y in xy:
    print(x, y)
