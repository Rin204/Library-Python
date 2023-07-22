# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sum_of_floor_of_linear
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.math.floor_sum import floor_sum


for _ in range(int(input())):
    n, m, a, b = map(int, input().split())
    print(floor_sum(n, m, a, b))
