# verification-helper: PROBLEM https://judge.yosupo.jp/problem/assignment
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.graph.Hungarian import Hungarian


n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
mi, assign = Hungarian(A)
print(mi)
print(*assign)
